#!/usr/bin/env python3
"""Strict continuation of the actual resolvent and original SplitZero closure."""
from __future__ import annotations
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import sys

REPO = Path(__file__).resolve().parents[2]
ROOT = REPO / 'formal/splitzero'
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from check_derived import audit, strip_comments


def previous():
    path = REPO / 'workbenches/tau-source-resolvent/run_resolvent.py'
    spec = importlib.util.spec_from_file_location('resolvent_previous', path)
    if spec is None or spec.loader is None:
        raise RuntimeError('missing recovered runner')
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    prior = previous()
    if sys.argv[1:] in (['--selftest'], ['--negative']):
        prior.main()
        return
    if sys.argv[1:]:
        raise ValueError('unknown argument')
    prior.main()
    legacy = prior.load_previous()
    targets = json.loads((HERE / 'TARGETS.json').read_text())
    expected = {'SplitZeroMetricSandwich', 'SplitZeroMixedSupportMetric',
                'SplitZeroSourceProjectorContrast'}
    if set(targets) != expected:
        raise ValueError('unexpected source target set')
    names = []
    for module, decls in targets.items():
        code = strip_comments((ROOT / (module + '.lean')).read_text())
        if re.search(r'\b(sorry|admit|axiom|unsafe|implemented_by|native_decide)\b', code):
            raise ValueError('proof escape in ' + module)
        if not decls:
            raise ValueError('empty target list')
        for name in decls:
            if not re.fullmatch(r'SplitZero\.[A-Za-z_][A-Za-z_0-9.]*', name):
                raise ValueError('invalid target ' + name)
            names.append(name)
    if len(names) != len(set(names)):
        raise ValueError('duplicate target')
    joint = list(targets) + ['SplitZeroSynchronization', 'SplitZeroJointHomotopy',
                              'SplitZeroCertifiedTraceBounds', 'SplitZeroConormalTower']
    closure = legacy.original.closure(joint)
    logs = ROOT / '.mixed-metric-logs'
    logs.mkdir(exist_ok=True)
    out = ROOT / '.lake/build/lib/lean'
    prior_record = json.loads((ROOT / '.source-resolvent-logs/receipt.json').read_text())
    checked = list(prior_record['strict_modules'])
    for module in closure:
        if module in checked:
            continue
        legacy.original.run(['lake', 'env', 'lean', '--trust=0', '-DwarningAsError=true',
                             '-o', str(out / (module + '.olean')), module + '.lean'],
                            logs / (module + '.log'))
        checked.append(module)
    body = ''.join('import ' + m + '\n' for m in joint)
    body += '\n' + ''.join('#print axioms ' + n + '\n' for n in names)
    (ROOT / 'AuditMixedSourceMetric.lean').write_text(body)
    text = legacy.original.run(['lake', 'env', 'lean', '--trust=0', '-DwarningAsError=true',
                                'AuditMixedSourceMetric.lean'], logs / 'axioms.log')
    reports = audit(text, names)
    if not set(closure).issubset(checked):
        raise ValueError('uncompiled local dependency')
    record = {
        'commit': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=REPO, text=True).strip(),
        'strict_modules': checked,
        'new_modules': list(targets),
        'new_selected_targets': len(names),
        'recovered_selected_targets': prior_record['selected_new_targets'],
        'inherited_selected_targets': prior_record['selected_inherited_targets'],
        'axioms': reports,
        'source_sha256': {m: hashlib.sha256((ROOT / (m + '.lean')).read_bytes()).hexdigest()
                          for m in checked},
        'scope': 'Original canonical metric sandwiches, actual mixed-support joins and boundary quotients, full Gram cross terms, and common-source projector trace identities. No arithmetic integral, tensor-uniform upper bound or complete external-product formalization is certified.'
    }
    (logs / 'receipt.json').write_text(json.dumps(record, indent=2, sort_keys=True) + '\n')
    print(json.dumps(record, indent=2, sort_keys=True), flush=True)

if __name__ == '__main__':
    main()
