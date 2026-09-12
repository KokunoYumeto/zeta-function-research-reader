#!/usr/bin/env python3
"""Audit the new source and exact selected axiom reports using the inherited parser."""
from __future__ import annotations
import argparse
import hashlib
import json
import re
from pathlib import Path
from check_derived import audit, strip_comments
ROOT = Path(__file__).resolve().parent

def prepare():
    spec = json.loads((ROOT / 'CONORMAL_CYCLIC_TARGETS.json').read_text(encoding='utf-8'))
    if not isinstance(spec, dict) or not spec:
        raise ValueError('empty manifest')
    hashes, seen = {}, set()
    for module, names in spec.items():
        if not re.fullmatch(r'SplitZero[A-Za-z]+', module) or not isinstance(names, list) or not names:
            raise ValueError('invalid module entry')
        raw = (ROOT / (module + '.lean')).read_bytes()
        code = strip_comments(raw.decode('utf-8'))
        if re.search(r'\b(sorry|admit|axiom|unsafe|implemented_by|native_decide)\b', code):
            raise ValueError('forbidden proof escape: ' + module)
        for name in names:
            if not isinstance(name, str) or not re.fullmatch(r'SplitZero(?:\.[A-Za-z_][A-Za-z_0-9]*)+', name) or name in seen:
                raise ValueError('invalid or duplicate target')
            seen.add(name)
        hashes[module + '.lean'] = hashlib.sha256(raw).hexdigest()
    (ROOT / 'CONORMAL_CYCLIC_MODULES.txt').write_text(''.join(m+'\n' for m in spec), encoding='utf-8')
    source = ''.join('import '+m+'\n' for m in spec) + '\n'
    source += ''.join('#print axioms '+n+'\n' for ns in spec.values() for n in ns)
    (ROOT / 'AuditConormalCyclic.lean').write_text(source, encoding='utf-8')
    return spec, hashes

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('log', type=Path, nargs='?')
    args = p.parse_args()
    spec, hashes = prepare()
    names = [n for ns in spec.values() for n in ns]
    out = {'modules': len(spec), 'selected_targets': len(names), 'source_sha256': hashes}
    if args.log is not None:
        out['axioms'] = audit(args.log.read_text(encoding='utf-8'), names)
    print(json.dumps(out, indent=2, sort_keys=True))

if __name__ == '__main__':
    main()
