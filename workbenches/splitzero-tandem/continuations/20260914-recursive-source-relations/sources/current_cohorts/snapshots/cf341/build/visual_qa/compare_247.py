"""Read-only mapping of final continuation pages to the frozen reviewed reader."""
from pathlib import Path
from collections import defaultdict
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
BASE = HERE / 'version_247'

def content(text):
    lines = text.splitlines()
    if lines and lines[0].strip() == 'Tau-based Split-Zero: original-source counterfactual':
        lines = lines[1:]
    if lines and re.fullmatch(r'[0-9ivxlcdm]+', lines[-1].strip()):
        lines = lines[:-1]
    return '\n'.join(lines).strip()

baseline = defaultdict(list)
for path in sorted(BASE.glob('text-*.txt')):
    number = int(path.stem.split('-')[1])
    baseline[content(path.read_text(encoding='utf-8'))].append(number)

rows = []
for path in sorted(HERE.glob('text-*.txt')):
    number = int(path.stem.split('-')[1])
    text = path.read_text(encoding='utf-8')
    rows.append({'page': number,
                 'text_sha256': hashlib.sha256(text.encode('utf-8')).hexdigest(),
                 'matching_reviewed_baseline_pages': baseline.get(content(text), []),
                 'start': '\n'.join(text.splitlines()[:4])})

report = {'frozen_baseline_sha256': '6aa8f6a5e9ea44c03a4e6544e5a8a5b5714f093a7d626fb07f2e10c1d4973543',
          'continuation_sha256': hashlib.sha256((ROOT / 'Tau_Split_Zero_Total_Counterfactual.pdf').read_bytes()).hexdigest(),
          'new_or_changed_pages': [r['page'] for r in rows if not r['matching_reviewed_baseline_pages']],
          'pages_requiring_visual_review': [r['page'] for r in rows if not any(n <= 240 for n in r['matching_reviewed_baseline_pages'])], 'page_mapping': rows}
(HERE / 'baseline_page_mapping.json').write_text(json.dumps(report, indent=2), encoding='utf-8')
print(json.dumps({'continuation_sha256': report['continuation_sha256'],
                  'pages': len(rows),
                  'new_or_changed_pages': report['new_or_changed_pages'], 'pages_requiring_visual_review': report['pages_requiring_visual_review']}, indent=2))


