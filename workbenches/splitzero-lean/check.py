#!/usr/bin/env python3
"""Fail closed on absent/nonstandard axiom reports for all named SplitZero declarations."""
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ALLOW = {"propext", "Classical.choice", "Quot.sound"}

def strip_comments(text):
    out, i, depth = [], 0, 0
    while i < len(text):
        if text.startswith('/-', i):
            depth += 1; i += 2
        elif depth and text.startswith('-/', i):
            depth -= 1; i += 2
        elif depth:
            out.append('\n' if text[i] == '\n' else ' '); i += 1
        elif text.startswith('--', i):
            j = text.find('\n', i)
            i = len(text) if j == -1 else j
        else:
            out.append(text[i]); i += 1
    if depth:
        raise ValueError('unterminated Lean comment')
    return ''.join(out)

def targets():
    names = []
    for path in sorted((ROOT / 'SplitZero').glob('*.lean')):
        raw = path.read_bytes()
        if raw.startswith(b'\xef\xbb\xbf') or b'\r' in raw:
            raise ValueError(f'noncanonical encoding: {path}')
        code = strip_comments(raw.decode('utf-8'))
        if re.search(r'\b(sorry|admit|axiom|unsafe|implemented_by)\b', code):
            raise ValueError(f'forbidden proof escape: {path}')
        for match in re.finditer(r'^(?:@\[[^\n]*\]\s*)?(?:(?:protected|private|noncomputable)\s+)?(?:theorem|lemma|def|instance)\s+([A-Za-z_][A-Za-z_0-9]*)\b', code, re.M):
            names.append('SplitZero.' + match.group(1))
    if not names or len(names) != len(set(names)):
        raise ValueError('empty or duplicated audit targets')
    return names

def audit(log, names):
    reports = {}
    pattern = r"'([^']+)' depends on axioms:\s*\[([^\]]*)\]"
    for name, axioms in re.findall(pattern, log, re.S):
        if name in reports:
            raise ValueError(f'duplicate report: {name}')
        reports[name] = {x.strip() for x in axioms.split(',') if x.strip()}
    for name in re.findall(r"'([^']+)' does not depend on any axioms", log):
        if name in reports:
            raise ValueError(f'duplicate report: {name}')
        reports[name] = set()
    for name in names:
        if name not in reports:
            raise ValueError(f'missing report: {name}')
        if reports[name] - ALLOW:
            raise ValueError(f'nonstandard axioms: {name}: {reports[name] - ALLOW}')
    return {name: sorted(reports[name]) for name in names}

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--prepare', action='store_true')
    parser.add_argument('--log', type=Path)
    args = parser.parse_args()
    names = targets()
    if args.prepare:
        (ROOT / 'Audit.lean').write_text('import SplitZero\n\n' + ''.join('#print axioms ' + n + '\n' for n in names), encoding='utf-8')
    result = {'named_targets': len(names), 'static_check': 'pass'}
    if args.log:
        result['axioms'] = audit(args.log.read_text(encoding='utf-8'), names)
    print(json.dumps(result, indent=2))
