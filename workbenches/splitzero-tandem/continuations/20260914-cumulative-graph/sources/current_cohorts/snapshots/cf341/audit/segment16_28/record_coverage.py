from pathlib import Path
import hashlib
import json
import re
from collections import Counter
from difflib import SequenceMatcher

ROOT = Path(__file__).resolve().parents[4]
SOURCE = ROOT / 'output/tau_f1_transcript_audit_2026-09-13/sources'
OUT = Path(__file__).resolve().parent
segment = SOURCE / 'audit_segment_U0016_U0028.md'
records_path = SOURCE / 'transcript_records.json'
raw = segment.read_bytes()
txt = raw.decode('utf-8').replace('\r\n', '\n')
records = json.loads(records_path.read_text(encoding='utf-8'))
lookup = {r['locator']: r for r in records}
headers = list(re.finditer(r'^## ([UA]\d+) \| (.*?) \| (user|assistant) \| chain (\d+)\s*$', txt, re.M))
selected = []
comparisons = []
changed_spans = Counter()
for i, match in enumerate(headers):
    locator = match.group(1)
    original = lookup[locator]
    end = headers[i + 1].start() if i + 1 < len(headers) else len(txt)
    payload = txt[match.end():end].strip()
    original_payload = original['text'].strip()
    if payload != original_payload:
        for tag, a0, a1, b0, b1 in SequenceMatcher(None, original_payload, payload, autojunk=False).get_opcodes():
            if tag != 'equal':
                changed_spans[(original_payload[a0:a1], payload[b0:b1])] += 1
    # Compare the exact visible text after converting CRLF to LF. Both
    # original record text and the current segment are retained as witnesses.
    comparisons.append({
        'locator': locator,
        'node_id': original['node_id'],
        'chain_ordinal': original['chain_ordinal'],
        'role': original['role'],
        'original_text_sha256': original['text_sha256'],
        'original_characters': original['characters'],
        'segment_payload_sha256': hashlib.sha256(payload.encode()).hexdigest(),
        'segment_start_line': txt[:match.start()].count('\n') + 1,
        'segment_end_line': txt[:end].count('\n'),
        'read_in_full': True,
        'payload_equals_original_after_outer_whitespace': payload == original['text'].strip(),
    })
    selected.append(original)

if len(selected) != 35:
    raise RuntimeError(f'Expected 35 visible records, got {len(selected)}')
if [r['locator'] for r in selected if r['role'] == 'user'] != [f'U{i:04}' for i in range(16, 29)]:
    raise RuntimeError('Missing a user input in the assigned interval')

(OUT / 'original_visible_records.json').write_text(json.dumps(selected, ensure_ascii=False, indent=2), encoding='utf-8')
(OUT / 'user_inputs_verbatim.md').write_text('\n\n'.join(
    f"## {r['locator']} | node {r['node_id']} | chain {r['chain_ordinal']}\n\n{r['text']}"
    for r in selected if r['role'] == 'user') + '\n', encoding='utf-8')

source_codes = []
for locator in ['A0935', 'A0945', 'A0953']:
    r = lookup[locator]
    code = json.loads(r['text'])['text']
    (OUT / f'{locator}_original_code.txt').write_text(code, encoding='utf-8')
    source_codes.append({k: r[k] for k in ['locator', 'chain_ordinal', 'node_id', 'text_sha256', 'characters']})

coverage = {
    'initial_read_source_serialization': {
        'sha256': '1dbb7fdc4004376bdcb312396dc6e12eccc9bdb8e6f2618b057a681e4682b919',
        'bytes': 204419,
        'lines': 5036,
        'line_endings': 'CRLF',
    },
    'source': str(segment),
    'source_sha256': hashlib.sha256(raw).hexdigest(),
    'source_bytes': len(raw),
    'source_line_count': len(txt.splitlines()),
    'complete_read_windows_1_based_inclusive': [[1,650],[651,1300],[1301,1950],[1951,2700],[2701,3380],[3381,4050],[4051,4690],[4691,5036]],
    'visible_record_count': len(selected),
    'user_record_count': 13,
    'comparisons': comparisons,
    'all_changed_spans_between_original_and_display_segment': [
        {'original': a, 'display_segment': b, 'occurrences': count}
        for (a,b),count in changed_spans.most_common()
    ],
    'additional_original_code_records_read_in_full': source_codes,
    'tool_output_limit': 'Original tool outputs in this interval are redacted. Original code records document exact generated mathematical text; they do not prove the historical command succeeded.',
    'scope': 'Entire assigned visible segment was read, without PDF extraction or OCR. All reconstruction claims are pinned to visible nodes or the additional original code witnesses. Later source notebooks are not treated as the authority for what the user said.'
}
(OUT / 'READ_COVERAGE.json').write_text(json.dumps(coverage, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps({k: coverage[k] for k in ['source_sha256', 'source_bytes', 'source_line_count', 'visible_record_count', 'user_record_count']}, indent=2))
