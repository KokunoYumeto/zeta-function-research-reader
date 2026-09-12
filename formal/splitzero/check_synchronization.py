#!/usr/bin/env python3
"""Audit every named declaration in the single synchronization source module."""
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ALLOWED = {'propext', 'Classical.choice', 'Quot.sound'}


def names():
    source = (ROOT / 'SplitZeroSynchronization.lean').read_text(encoding='utf-8')
    code = re.sub(r'/\-.*?\-/', '', source, flags=re.S)
    if re.search(r'\b(sorry|admit|axiom|unsafe|implemented_by|native_decide)\b', code):
        raise ValueError('forbidden proof escape in synchronization source')
    result = ['SplitZero.Synchronization.' + n for n in re.findall(
        r'^(?:abbrev|def|theorem|lemma)\s+([A-Za-z_][A-Za-z_0-9]*)\b', code, re.M)]
    if not result or len(result) != len(set(result)):
        raise ValueError('empty or duplicate source names')
    return result


def audit(log, expected):
    found = {}
    for name, content in re.findall(r"'([^']+)' depends on axioms:\s*\[([^\]]*)\]", log, re.S):
        if name in found:
            raise ValueError('duplicate report: ' + name)
        found[name] = {x.strip() for x in content.split(',') if x.strip()}
    for name in re.findall(r"'([^']+)' does not depend on any axioms", log):
        if name in found:
            raise ValueError('duplicate report: ' + name)
        found[name] = set()
    for name in expected:
        if name not in found:
            raise ValueError('missing report: ' + name)
        if found[name] - ALLOWED:
            raise ValueError('nonstandard axioms: ' + name)
    return {n: sorted(found[n]) for n in expected}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--prepare', action='store_true')
    parser.add_argument('--log', type=Path)
    args = parser.parse_args()
    expected = names()
    if args.prepare:
        (ROOT / 'AuditSynchronization.lean').write_text('import SplitZeroSynchronization\n\n' +
            ''.join('#print axioms ' + n + '\n' for n in expected), encoding='utf-8')
    result = {'named_targets': len(expected)}
    if args.log:
        result['axioms'] = audit(args.log.read_text(encoding='utf-8'), expected)
    print(json.dumps(result, indent=2))
