#!/usr/bin/env python3
"""Recheck the inherited metric/source integration before the new proof targets."""
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


def load_previous():
    path = REPO / 'workbenches/tau-arithmetic-metric-transfer/run_metric_transfer.py'
    spec = importlib.util.spec_from_file_location('metric_previous', path)
    if spec is None or spec.loader is None:
        raise RuntimeError('missing inherited runner')
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    prior = load_previous()
    if sys.argv[1:] == ['--selftest']:
        prior.original.selftest()
        return
    if sys.argv[1:] == ['--negative']:
        audit("'SplitZero.false' depends on axioms: [sorryAx]", ['SplitZero.false'])
        raise RuntimeError('forbidden axiom accepted')
    if sys.argv[1:]:
        raise ValueError('unknown argument')
    prior.main()
    targets = json.loads((HERE/'TARGETS.json').read_text())
    expected = {'SplitZeroMetricResolvent','SplitZeroCertifiedTraceBounds','SplitZeroMetricResolventSupport'}
    if set(targets) != expected:
        raise ValueError('unexpected new source set')
    names = []
    for module, decls in targets.items():
        code = strip_comments((ROOT/(module+'.lean')).read_text())
        if re.search(r'\b(sorry|admit|axiom|unsafe|implemented_by|native_decide)\b', code):
            raise ValueError('proof escape in '+module)
        if not decls:
            raise ValueError('empty target list')
        for name in decls:
            if not re.fullmatch(r'SplitZero\.[A-Za-z_][A-Za-z_0-9.]*', name):
                raise ValueError('invalid target '+name)
            names.append(name)
    if len(names) != len(set(names)):
        raise ValueError('duplicate target')
    closure = prior.original.closure(list(targets)+prior.JOINT)
    logs = ROOT/'.source-resolvent-logs'
    logs.mkdir(exist_ok=True)
    out = ROOT/'.lake/build/lib/lean'
    for module in targets:
        prior.original.run(['lake','env','lean','--trust=0','-DwarningAsError=true',
                            '-o',str(out/(module+'.olean')),module+'.lean'], logs/(module+'.log'))
    body = ''.join('import '+m+'\n' for m in list(targets)+prior.JOINT)
    body += '\n'+''.join('#print axioms '+n+'\n' for n in names)
    (ROOT/'AuditSourceResolvent.lean').write_text(body)
    text = prior.original.run(['lake','env','lean','--trust=0','-DwarningAsError=true',
                               'AuditSourceResolvent.lean'],logs/'axioms.log')
    reports = audit(text,names)
    previous = json.loads((ROOT/'.metric-transfer-logs/receipt.json').read_text())
    checked = list(dict.fromkeys(previous['strict_modules']+list(targets)))
    if not set(closure).issubset(checked):
        raise ValueError('uncompiled local dependency in closure')
    record = {
        'commit': subprocess.check_output(['git','rev-parse','HEAD'],cwd=REPO,text=True).strip(),
        'strict_modules': checked,
        'new_modules': list(targets),
        'selected_new_targets':len(names),
        'selected_inherited_targets':previous['selected_targets'],
        'axioms':reports,
        'source_sha256':{m:hashlib.sha256((ROOT/(m+'.lean')).read_bytes()).hexdigest() for m in checked},
        'scope':'Original canonical source resolvent and supported boundary; certified trace-input enclosures and signed endpoint composition. No new arithmetic integrals or tensor-uniform upper estimate.'
    }
    (logs/'receipt.json').write_text(json.dumps(record,indent=2,sort_keys=True)+'\n')
    print(json.dumps(record,indent=2,sort_keys=True),flush=True)

if __name__ == '__main__':
    main()
