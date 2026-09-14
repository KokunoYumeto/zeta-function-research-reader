"""Validate the completely read transcript segment against original records."""
from pathlib import Path
import hashlib
import json
import re

src = Path(r'workspace:/output/tau_f1_transcript_audit_2026-09-13/sources')
out = Path(__file__).resolve().parent
segment = src / 'audit_segment_U0029_U0040.md'
raw = segment.read_bytes()
text = raw.decode('utf-8').replace('\r\n','\n')
records = json.loads((src / 'transcript_records.json').read_text(encoding='utf-8'))
lookup = {r['locator']: r for r in records}
headers = list(re.finditer(r'^## ([UA]\d+) \| ([^|]+) \| (user|assistant) \| chain (\d+)\s*$', text, re.M))
coverage = []
users = []
for i,h in enumerate(headers):
    end = headers[i+1].start() if i+1<len(headers) else len(text)
    body = text[h.end():end].strip()
    locator = h.group(1)
    rec = lookup[locator]
    if body != rec['text'].strip():
        raise RuntimeError(f'Text mismatch: {locator}')
    if h.group(2).strip()!=rec['node_id'] or int(h.group(4))!=rec['chain_ordinal']:
        raise RuntimeError(f'Provenance mismatch: {locator}')
    startline = text.count('\n',0,h.start())+1
    endline = text.count('\n',0,end)
    coverage.append({'locator':locator,'role':rec['role'],'chain_ordinal':rec['chain_ordinal'],
                     'node_id':rec['node_id'],'line_start':startline,'line_end':endline,
                     'characters':len(body),'sha256_text':hashlib.sha256(body.encode()).hexdigest(),
                     'complete_body_read':True,'original_record_exact_match':True})
    if rec['role']=='user':
        users.append(f"## {locator} | {rec['node_id']} | chain {rec['chain_ordinal']}\n\n{rec['text']}\n")
report={'source':str(segment),'bytes':len(raw),'characters':len(text),
        'sha256':hashlib.sha256(raw).hexdigest(),'line_count':len(text.splitlines()),
        'records':coverage,'visible_record_count':len(coverage),'user_record_count':len(users),
        'read_windows_inclusive':[[1,740],[741,1420],[1421,2130],[2131,2840],
                                  [2841,3560],[3561,4280],[4281,4990],[4991,len(text.splitlines())]],
        'all_original_record_matches':True,
        'comparison_note':'Only CRLF-to-LF line endings and outer whitespace are ignored.'}
(out/'COVERAGE.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
(out/'USER_INPUTS_VERBATIM.md').write_text('\n'.join(users),encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k!='records'},indent=2))
for r in coverage:
    print(f"{r['locator']} {r['role']} L{r['line_start']}-{r['line_end']} chars={r['characters']} EXACT")
