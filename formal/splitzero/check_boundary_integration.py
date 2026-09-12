#!/usr/bin/env python3
"""Fail-closed source and transitive-axiom audit for the boundary integration."""
from __future__ import annotations
import argparse
import hashlib
import json
import re
from pathlib import Path
from check_derived import audit, strip_comments

ROOT = Path(__file__).resolve().parent


def preflight(root: Path = ROOT):
    spec = json.loads((root / 'BOUNDARY_INTEGRATION_TARGETS.json').read_text(encoding='utf-8'))
    if not isinstance(spec, dict) or not spec:
        raise ValueError('empty or invalid manifest')
    names, hashes = [], {}
    for module, targets in spec.items():
        if not re.fullmatch(r'SplitZero[A-Za-z]+', module):
            raise ValueError('invalid module')
        if not isinstance(targets, list) or not targets:
            raise ValueError('missing module targets')
        raw = (root / (module + '.lean')).read_bytes()
        if b'\r' in raw or raw.startswith(b'\xef\xbb\xbf'):
            raise ValueError('noncanonical source')
        code = strip_comments(raw.decode('utf-8'))
        if re.search(r'\b(sorry|admit|axiom|unsafe|implemented_by|native_decide)\b', code):
            raise ValueError('forbidden proof escape')
        hashes[module + '.lean'] = hashlib.sha256(raw).hexdigest()
        for name in targets:
            if not isinstance(name, str) or not re.fullmatch(r'SplitZero(?:\.[A-Za-z_][A-Za-z_0-9]*)+', name):
                raise ValueError('invalid target name')
            if name in names:
                raise ValueError('duplicate target')
            names.append(name)
    return spec, names, hashes


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--prepare', action='store_true')
    parser.add_argument('log', nargs='?', type=Path)
    args = parser.parse_args()
    spec, names, hashes = preflight()
    if args.prepare:
        text = ''.join('import ' + m + '\n' for m in spec) + '\n'
        text += ''.join('#print axioms ' + name + '\n' for name in names)
        (ROOT / 'AuditBoundaryIntegration.lean').write_text(text, encoding='utf-8')
        (ROOT / 'BOUNDARY_INTEGRATION_MODULES.txt').write_text('\n'.join(spec) + '\n', encoding='utf-8')
    result = {'modules': len(spec), 'selected_targets': len(names), 'source_sha256': hashes}
    if args.log is not None:
        result['axioms'] = audit(args.log.read_text(encoding='utf-8'), names)
    elif not args.prepare:
        raise ValueError('provide --prepare or an audit log')
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
