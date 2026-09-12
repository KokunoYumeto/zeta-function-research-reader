#!/usr/bin/env python3
"""Reject missing, duplicated, or nonstandard transitive axiom reports."""
import pathlib
import re
import sys
root = pathlib.Path(__file__).resolve().parent
expected = re.findall(r'^#print axioms (\S+)', (root / 'Audit.lean').read_text(), re.M)
text = pathlib.Path(sys.argv[1]).read_text(encoding='utf-8')
allowed = {'propext', 'Classical.choice', 'Quot.sound'}
seen = {}
for name, ax in re.findall(r"'([^']+)' depends on axioms:\s*\[([^\]]*)\]", text, re.S):
    if name in seen:
        raise SystemExit('Duplicate report: ' + name)
    seen[name] = {x.strip() for x in ax.split(',') if x.strip()}
for name in re.findall(r"'([^']+)' does not depend on any axioms", text):
    if name in seen:
        raise SystemExit('Duplicate report: ' + name)
    seen[name] = set()
if set(seen) != set(expected) or len(expected) != len(set(expected)):
    raise SystemExit('Axiom-report coverage mismatch')
for name, axioms in seen.items():
    if axioms - allowed:
        raise SystemExit(f'Forbidden axioms in {name}: {axioms - allowed}')
print(f'PASS: {len(expected)} selected declarations; only standard axioms')
