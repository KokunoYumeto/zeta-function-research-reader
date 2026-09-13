#!/usr/bin/env python3
"""Strict source-closure and transitive axiom audit, reusing the original parser."""
from __future__ import annotations
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import sys

REPO = Path(__file__).resolve().parents[2]
ROOT = REPO / 'formal' / 'splitzero'
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from check_derived import audit, strip_comments

SPEC = importlib.util.spec_from_file_location('original_integration', REPO / 'workbenches/tau-split-integration/run_integration.py')
if SPEC is None or SPEC.loader is None:
    raise RuntimeError('missing original integration runner')
original = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(original)
JOINT = ['SplitZeroPeriodTransport', 'SplitZeroResidueSupport', 'SplitZeroJointHomotopy',
         'SplitZeroConormalTower', 'SplitZeroLaplacianControl', 'SplitZeroHomologyExample']


def main() -> None:
    if len(sys.argv) == 2 and sys.argv[1] == '--selftest':
        original.selftest()
        return
    if len(sys.argv) == 2 and sys.argv[1] == '--negative':
        audit("'SplitZero.bad' depends on axioms: [sorryAx]", ['SplitZero.bad'])
        raise RuntimeError('forbidden report accepted')
    if len(sys.argv) != 1:
        raise ValueError('unknown argument')
    original.preserve_core()
    spec = json.loads((HERE / 'TARGETS.json').read_text())
    if set(spec) != {'SplitZeroMetricVariation', 'SplitZeroArithmeticLogTransfer', 'SplitZeroMetricVariationSupport'}:
        raise ValueError('unexpected source set')
    names = []
    for module, declarations in spec.items():
        code = strip_comments((ROOT / (module + '.lean')).read_text())
        if re.search(r'\b(sorry|admit|axiom|unsafe|implemented_by|native_decide)\b', code):
            raise ValueError('proof escape in ' + module)
        if re.search(r'\b(?:def|structure|inductive)\s+G\b', code):
            raise ValueError('replacement scalar')
        if not declarations:
            raise ValueError('empty audit source')
        for name in declarations:
            if not re.fullmatch(r'SplitZero\.[A-Za-z_][A-Za-z_0-9.]*', name):
                raise ValueError('invalid declaration')
            names.append(name)
    if len(names) != len(set(names)):
        raise ValueError('duplicate declaration')
    modules = original.closure(list(spec) + JOINT)
    logs = ROOT / '.metric-transfer-logs'
    logs.mkdir(exist_ok=True)
    out = ROOT / '.lake/build/lib/lean'
    out.mkdir(parents=True, exist_ok=True)
    for module in modules:
        original.run(['lake', 'env', 'lean', '--trust=0', '-DwarningAsError=true',
                      '-o', str(out / (module + '.olean')), module + '.lean'], logs / (module + '.log'))
    body = ''.join('import ' + m + '\n' for m in list(spec) + JOINT)
    body += '\n' + ''.join('#print axioms ' + n + '\n' for n in names)
    (ROOT / 'AuditArithmeticMetricTransfer.lean').write_text(body)
    text = original.run(['lake', 'env', 'lean', '--trust=0', '-DwarningAsError=true',
                         'AuditArithmeticMetricTransfer.lean'], logs / 'axioms.log')
    reports = audit(text, names)
    record = {
        'commit': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip(),
        'strict_modules': modules, 'new_modules': list(spec), 'selected_targets': len(names),
        'axioms': reports, 'source_sha256': {m: hashlib.sha256((ROOT/(m+'.lean')).read_bytes()).hexdigest() for m in modules},
        'scope': 'Source secants, signed finite log certificate, original support quotient. No arithmetic integral or uniform tensor estimate certified.',
    }
    (logs / 'receipt.json').write_text(json.dumps(record, indent=2, sort_keys=True)+'\n')
    print(json.dumps(record, indent=2, sort_keys=True), flush=True)

if __name__ == '__main__':
    main()
