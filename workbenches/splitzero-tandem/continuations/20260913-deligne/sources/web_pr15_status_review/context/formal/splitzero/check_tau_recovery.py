#!/usr/bin/env python3
"""Enumerated source checks and transitive axiom audit; shared parser stays unchanged."""
from __future__ import annotations
import argparse
import hashlib
import json
import re
from pathlib import Path
from check_derived import audit, strip_comments
ROOT = Path(__file__).resolve().parent

def preflight(root: Path = ROOT):
    spec = json.loads((root / 'TAU_RECOVERY_TARGETS.json').read_text(encoding='utf-8'))
    modules = (root / 'TAU_RECOVERY_MODULES.txt').read_text(encoding='utf-8').splitlines()
    if not spec or list(spec) != modules or len(modules) != len(set(modules)):
        raise ValueError('module manifest mismatch')
    names = []
    hashes = {}
    for module, targets in spec.items():
        if not re.fullmatch(r'SplitZero[A-Za-z]+', module) or not targets:
            raise ValueError('invalid module or empty targets')
        data = (root / (module + '.lean')).read_bytes()
        code = strip_comments(data.decode('utf-8'))
        if re.search(r'\b(sorry|admit|axiom|unsafe|implemented_by|native_decide)\b', code):
            raise ValueError('forbidden proof escape in ' + module)
        if b'\r' in data or data.startswith(b'\xef\xbb\xbf'):
            raise ValueError('noncanonical source encoding')
        for name in targets:
            if not re.fullmatch(r'SplitZero(?:\.[A-Za-z_][A-Za-z_0-9]*)+', name):
                raise ValueError('invalid declaration')
            names.append(name)
        hashes[module + '.lean'] = hashlib.sha256(data).hexdigest()
    if len(names) != len(set(names)):
        raise ValueError('duplicate declaration')
    return spec, names, hashes

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--prepare', action='store_true')
    parser.add_argument('log', type=Path, nargs='?')
    args = parser.parse_args()
    spec, names, hashes = preflight()
    result = {'modules': len(spec), 'selected_targets': len(names), 'source_sha256': hashes}
    if args.prepare:
        text = ''.join('import ' + module + '\n' for module in spec)
        text += '\n' + ''.join('#print axioms ' + name + '\n' for name in names)
        (ROOT / 'AuditTauRecovery.lean').write_text(text, encoding='utf-8')
    if args.log:
        result['axioms'] = audit(args.log.read_text(encoding='utf-8'), names)
    elif not args.prepare:
        raise ValueError('supply --prepare or the executed Lean log')
    (ROOT / 'TauRecoveryReceipt.json').write_text(json.dumps(result, indent=2, sort_keys=True)+'\n', encoding='utf-8')
    print(json.dumps(result, indent=2, sort_keys=True))
if __name__ == '__main__':
    main()
