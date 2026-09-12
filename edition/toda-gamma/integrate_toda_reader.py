"""Mechanical full-proof transfer; no source mathematics is abridged."""
from pathlib import Path
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SOURCE = Path('external-local-evidence/private-profile/Documents/math/work/toda_cv_exact_bridge_20260912.tex')
EXPECTED = '97652a43445708c0e6d2a959f45aed8a4f2a7f73f9cd4b6cd57e67b8fedb408e'
TARGET = ROOT / 'tex/satellites/29w_toda_source_relation_volumes.tex'

def sha(raw):
    return hashlib.sha256(raw).hexdigest()

def transform(raw):
    text = raw.decode('utf-8')
    assert text.count(r'\maketitle') == text.count(r'\end{document}') == 1
    body = text.split(r'\maketitle', 1)[1].split(r'\end{document}', 1)[0]
    assert r'\subsection' not in body
    headings = re.findall(r'\\section\{([^{}]*)\}', body)
    assert len(headings) == body.count(r'\section{')
    # Explicit TOC spacing preserves multi-digit subsection labels.
    body = re.sub(r'\\section\{([^{}]*)\}',
                  lambda m: r'\subsection[\hspace{0.4em}' + m[1] + ']{' + m[1] + '}', body)
    return body, headings

raw = SOURCE.read_bytes()
assert sha(raw) == EXPECTED, 'Original proof changed; re-read before transfer'
body, headings = transform(raw)
header = (HERE / 'TVB_HEADER.tex').read_text(encoding='utf-8')
chapter = header + body + '\n\\endgroup\n'
if TARGET.exists():
    previous = json.loads((HERE / 'TVB_TRANSFER.json').read_text())
    assert sha(TARGET.read_bytes()) == previous['target_sha256'], 'Unrecorded target edits'
TARGET.write_text(chapter, encoding='utf-8', newline='\n')
stage = HERE / 'original_sources'
stage.mkdir(exist_ok=True)
copy = stage / SOURCE.name
if copy.exists():
    assert copy.read_bytes() == raw, 'Original snapshot differs'
else:
    copy.write_bytes(raw)
tags = re.findall(r'\\tag\{(TVB\.[^}]+)\}', body)
assert len(tags) == len(set(tags)) == 49, 'Unexpected explicit tag inventory'
receipt = {'status': 'complete_body_mechanically_transferred',
           'source': {'path': str(SOURCE), 'sha256': EXPECTED, 'bytes': len(raw)},
           'snapshot': str(copy), 'target': str(TARGET),
           'target_sha256': sha(TARGET.read_bytes()), 'headings': headings,
           'explicit_tags': tags, 'source_body_characters': len(body),
           'transforms': ['Remove standalone preamble/title wrapper only',
                          'Demote section headings with explicit TOC spacing',
                          'Retain exact macro meanings in a local group',
                          'Prepend separately authored context; retain complete body'],
           'new_lean_execution': False, 'asymptotic_bound_claimed': False}
(HERE / 'TVB_TRANSFER.json').write_text(json.dumps(receipt, indent=2)+'\n', encoding='utf-8')
print(json.dumps({'status': receipt['status'], 'tags': len(tags), 'sections': len(headings)}))
