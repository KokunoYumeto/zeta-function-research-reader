"""Read-only mapping of final continuation pages to the frozen reviewed reader."""
from pathlib import Path
from collections import defaultdict
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
BASE = HERE / 'version_224'

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

report = {'frozen_baseline_sha256': '08a5293305eb1fd7b0ce22816a2ded717d002bf7a5f44e7177560efbb3a1b5eb',
          'continuation_sha256': hashlib.sha256((ROOT / 'Tau_Split_Zero_Total_Counterfactual.pdf').read_bytes()).hexdigest(),
          'new_or_changed_pages': [r['page'] for r in rows if not r['matching_reviewed_baseline_pages']],
          'page_mapping': rows}
(HERE / 'baseline_page_mapping.json').write_text(json.dumps(report, indent=2), encoding='utf-8')
print(json.dumps({'continuation_sha256': report['continuation_sha256'],
                  'pages': len(rows),
                  'new_or_changed_pages': report['new_or_changed_pages']}, indent=2))

