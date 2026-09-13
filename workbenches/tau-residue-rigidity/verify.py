#!/usr/bin/env python3
"""Strict compilation and exact-target audit, reusing the original SplitZero checker."""
from __future__ import annotations
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import sys

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
ROOT = REPO / 'formal' / 'splitzero'
helper_path = REPO / 'workbenches' / 'tau-split-integration' / 'run_integration.py'
spec = importlib.util.spec_from_file_location('original_integration', helper_path)
if spec is None or spec.loader is None:
    raise RuntimeError('cannot load original integration checker')
helper = importlib.util.module_from_spec(spec)
spec.loader.exec_module(helper)


def main() -> None:
    helper.preserve_core()
    helper.selftest()
    targets_by_module = json.loads((HERE / 'TARGETS.json').read_text())
    if len(targets_by_module) != 3:
        raise ValueError('expected the three complete modules')
    targets = []
    for module, suffixes in targets_by_module.items():
        text = helper.strip_comments((ROOT / (module + '.lean')).read_text())
        if re.search(r'\b(sorry|admit|axiom|unsafe|implemented_by|native_decide)\b', text):
            raise ValueError('proof escape in ' + module)
        if re.search(r'\b(?:def|structure|inductive)\s+G\b', text):
            raise ValueError('replacement scalar in ' + module)
        targets.extend('SplitZero.MonicResidue.' + n for n in suffixes)
    if len(targets) != len(set(targets)):
        raise ValueError('duplicate targets')
    closure = helper.closure(list(targets_by_module) + helper.JOINT)
    logs = ROOT / '.residue-rigidity-logs'
    logs.mkdir(exist_ok=True)
    out = ROOT / '.lake/build/lib/lean'
    out.mkdir(parents=True, exist_ok=True)
    for module in closure:
        helper.run(['lake', 'env', 'lean', '--trust=0', '-DwarningAsError=true',
                    '-o', str(out / (module + '.olean')), module + '.lean'],
                   logs / (module + '.log'))
    audit_source = ''.join('import ' + m + '\n' for m in list(targets_by_module) + helper.JOINT)
    audit_source += '\n' + ''.join('#print axioms ' + n + '\n' for n in targets)
    (ROOT / 'AuditResidueRigidity.lean').write_text(audit_source)
    output = helper.run(['lake', 'env', 'lean', '--trust=0', '-DwarningAsError=true',
                         'AuditResidueRigidity.lean'], logs / 'audit.log')
    reports = helper.audit(output, targets)
    receipt = {
        'commit': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip(),
        'selected_targets': len(targets), 'axioms': reports, 'strict_closure': closure,
        'source_sha256': {m: hashlib.sha256((ROOT / (m + '.lean')).read_bytes()).hexdigest()
                          for m in closure},
        'scope': 'monic residue duality, exact invariant-constituent response, original supported source detection',
        'analytic_purity_or_RH_certificate': False,
    }
    (logs / 'receipt.json').write_text(json.dumps(receipt, indent=2, sort_keys=True) + '\n')
    print(json.dumps(receipt, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
