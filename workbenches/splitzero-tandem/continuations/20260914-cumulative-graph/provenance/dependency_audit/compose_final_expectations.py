"""Compose accepted mathematical sources with independently verified typography.

Never replace a source pin merely because the active file differs: an explicit
before->after derivation whose inverse was checked is required.
"""
from pathlib import Path
import hashlib,json

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
WORK=ROOT.parents[1]
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
rows={r['reader_path']:dict(r) for r in read(HERE/'EXPECTED_ACTIVE_PATCHES.json')['patches']}
for r in read(ROOT/'ROOT_METRIC_ACCEPTED_ROUTES.json'):
    p=Path(r['source'])
    if not p.is_absolute():p=WORK/p
    assert sha(p)==r['sha256']
    rows[r['reader_path']]={**r,'source':str(p),'lane':'root-metric','include_required':True}
conclusion=ROOT/'root/research_conclusion.tex'
rows['tex/research_conclusion.tex']={'source':str(conclusion),'reader_path':'tex/research_conclusion.tex',
 'sha256':sha(conclusion),'lane':'root-conclusion','include_required':True}

checks=read(HERE/'TYPOGRAPHY_INDEPENDENT_CHECK.json')
assert checks['pass']
by_path={r['reader_path']:r for r in checks['checks']}
transports=[]
for overlay in read(HERE/'EXPECTED_TYPOGRAPHY_PATCHES.json')['patches']:
    rel=overlay['reader_path'];proof=by_path[rel]
    assert proof['pass'] and proof['exact_forward'] and proof['exact_inverse']
    if rel in rows:
        assert rows[rel]['sha256']==proof['before_sha256'],(rel,'unproved source-to-layout jump',rows[rel]['sha256'],proof['before_sha256'])
        old=rows[rel]
        rows[rel]={**old,'accepted_source_sha256':old['sha256'],
                   'sha256':overlay['sha256'],'typography_proof':proof}
    else:
        rows[rel]={**overlay,'typography_proof':proof}
    assert rows[rel]['sha256']==proof['after_sha256']
    transports.append({'reader_path':rel,'before_sha256':proof['before_sha256'],'after_sha256':proof['after_sha256']})

out={'schema':'accepted-source-plus-invertible-presentation-v1','patches':list(rows.values()),
     'presentation_transports':transports,
     'note':'Each mathematical source is either the exact active bytes or has an independently replayed complete-byte reversible presentation transform; source pin is retained separately.'}
(HERE/'EXPECTED_FINAL_ACTIVE_PATCHES.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'rows':len(rows),'transports':len(transports)}))
