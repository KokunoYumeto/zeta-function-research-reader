#!/usr/bin/env python3
"""Fail-closed audit of the explicitly enumerated SplitZero derived declarations."""
from __future__ import annotations
import argparse
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ALLOWED = frozenset({'propext', 'Classical.choice', 'Quot.sound'})


def strip_comments(text: str) -> str:
    out: list[str] = []
    i = depth = 0
    while i < len(text):
        if text.startswith('/-', i):
            depth += 1
            i += 2
        elif depth and text.startswith('-/', i):
            depth -= 1
            i += 2
        elif depth:
            out.append('\n' if text[i] == '\n' else ' ')
            i += 1
        elif text.startswith('--', i):
            j = text.find('\n', i)
            i = len(text) if j < 0 else j
        else:
            out.append(text[i])
            i += 1
    if depth:
        raise ValueError('unterminated Lean comment')
    return ''.join(out)


def preflight(root: Path = ROOT) -> tuple[dict[str, list[str]], dict[str, str]]:
    spec = json.loads((root / 'DERIVED_TARGETS.json').read_text(encoding='utf-8'))
    if not isinstance(spec, dict) or not spec:
        raise ValueError('empty or malformed target manifest')
    seen: set[str] = set()
    hashes: dict[str, str] = {}
    for module, targets in spec.items():
        if not re.fullmatch(r'SplitZero[A-Za-z]+', module):
            raise ValueError('invalid module name')
        if not isinstance(targets, list) or not targets:
            raise ValueError('empty module targets')
        data = (root / (module + '.lean')).read_bytes()
        if b'\r' in data or data.startswith(b'\xef\xbb\xbf'):
            raise ValueError('noncanonical source encoding: ' + module)
        code = strip_comments(data.decode('utf-8'))
        if re.search(r'\b(sorry|admit|axiom|unsafe|implemented_by|native_decide)\b', code):
            raise ValueError('forbidden proof escape: ' + module)
        for name in targets:
            if not isinstance(name, str) or not re.fullmatch(r'SplitZero(?:\.[A-Za-z_][A-Za-z_0-9]*)+', name):
                raise ValueError('invalid declaration name')
            if name in seen:
                raise ValueError('duplicate target: ' + name)
            seen.add(name)
        hashes[module + '.lean'] = hashlib.sha256(data).hexdigest()
    return spec, hashes


def audit(log: str, expected: list[str]) -> dict[str, list[str]]:
    if not expected or len(expected) != len(set(expected)):
        raise ValueError('empty or duplicate expected targets')
    found: dict[str, set[str]] = {}
    for name, content in re.findall(r"'([^']+)' depends on axioms:\s*\[([^\]]*)\]", log, re.S):
        if name in found:
            raise ValueError('duplicate report: ' + name)
        found[name] = {x.strip() for x in content.split(',') if x.strip()}
    for name in re.findall(r"'([^']+)' does not depend on any axioms", log):
        if name in found:
            raise ValueError('duplicate report: ' + name)
        found[name] = set()
    if set(found) != set(expected):
        raise ValueError(f'report mismatch: missing={set(expected)-set(found)}, unexpected={set(found)-set(expected)}')
    for name, axioms in found.items():
        if axioms - ALLOWED:
            raise ValueError(f'nonstandard axioms: {name}: {axioms-ALLOWED}')
    return {name: sorted(found[name]) for name in expected}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('log', type=Path, nargs='?')
    parser.add_argument('--prepare', action='store_true')
    args = parser.parse_args()
    spec, hashes = preflight()
    names = [n for ns in spec.values() for n in ns]
    if args.prepare:
        text = ''.join('import ' + m + '\n' for m in spec) + '\n'
        text += ''.join('#print axioms ' + n + '\n' for n in names)
        (ROOT / 'AuditDerived.lean').write_text(text, encoding='utf-8')
    result = {'modules': len(spec), 'selected_targets': len(names), 'source_sha256': hashes}
    if args.log is not None:
        result['axioms'] = audit(args.log.read_text(encoding='utf-8'), names)
    elif not args.prepare:
        raise ValueError('provide an audit log or --prepare')
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
