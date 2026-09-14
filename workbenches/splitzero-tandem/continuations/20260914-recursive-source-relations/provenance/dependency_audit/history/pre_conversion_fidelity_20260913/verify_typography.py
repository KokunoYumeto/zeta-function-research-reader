"""Independently replay and invert declared presentation-only byte edits."""
from pathlib import Path
import hashlib,json

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
STAGE=ROOT/'cumulative_source_v1'
def sha(b):return hashlib.sha256(b).hexdigest()
def read(p):return json.loads(p.read_text(encoding='utf-8'))
checks=[]
rows=[]

def replay_record(lane,original,active,expected_before,expected_after,edits,source=None):
    before=Path(original).read_bytes();after=Path(active).read_bytes()
    assert sha(before)==expected_before and sha(after)==expected_after
    newline='\r\n' if b'\r\n' in before else '\n'
    after_newline='\r\n' if b'\r\n' in after else '\n'
    def eb(s):return s.replace('\r\n','\n').replace('\n',newline).encode()
    def ea(s):return s.replace('\r\n','\n').replace('\n',after_newline).encode()
    forward=before
    for e in edits:
        old,new=eb(e['old']),eb(e['new'])
        assert forward.count(old)==1
        forward=forward.replace(old,new,1)
    inverse=after
    for e in reversed(edits):
        old,new=ea(e['old']),ea(e['new'])
        assert inverse.count(new)==1
        inverse=inverse.replace(new,old,1)
    def transport(b,src,dst):
        if src==dst:return b
        assert b.count(src.encode())==b.count(b'\n')
        return b.replace(src.encode(),dst.encode())
    assert transport(forward,newline,after_newline)==after
    assert transport(inverse,after_newline,newline)==before
    rel=Path(active).relative_to(STAGE).as_posix()
    checks.append({'reader_path':rel,'before_sha256':sha(before),'after_sha256':sha(after),'exact_forward':True,'exact_inverse':True,'edits':edits,'newline_transport':{'before':repr(newline),'after':repr(after_newline)},'pass':True})
    rows.append({'lane':lane,'source':str(source or active),'reader_path':rel,'sha256':sha(after),'accepted_before_sha256':sha(before),'include_required':True})

for r in read(ROOT/'cohort_staging/typography_overlay_20260913/OVERLAY_PROPOSALS.json')['records']:
    before=Path(r['original']['path']).read_bytes()
    after=Path(r['active_path']).read_bytes()
    old,new=r['old'].encode(),r['new'].encode()
    assert before.count(old)==1 and after.count(new)==1
    assert sha(before)==r['original']['sha256']
    assert sha(after)==r['proposed_overlay']['sha256']
    assert before.replace(old,new,1)==after
    assert after.replace(new,old,1)==before
    rel=Path(r['active_path']).relative_to(STAGE).as_posix()
    checks.append({'reader_path':rel,'before_sha256':sha(before),'after_sha256':sha(after),'exact_forward':True,'exact_inverse':True,'edits':[{'old':r['old'],'new':r['new']}],'pass':True})
    rows.append({'lane':'typography-cohort','source':r['proposed_overlay']['path'],'reader_path':rel,'sha256':sha(after),'include_required':True})

for r in read(ROOT/'typesetting_v21/OVERLAY_MANIFEST.json')['files']:
    before=(ROOT/'typesetting_v21/originals'/r['path']).read_bytes()
    after=(STAGE/r['path']).read_bytes()
    assert sha(before)==r['before']['sha256']
    assert sha(after)==r['after']['sha256']
    newline='\r\n' if b'\r\n' in before else '\n'
    def eb(s):return s.replace('\r\n','\n').replace('\n',newline).encode()
    forward=before
    for e in r['edits']:
        old,new=eb(e['old']),eb(e['new'])
        assert forward.count(old)==1
        forward=forward.replace(old,new,1)
    inverse=after
    for e in reversed(r['edits']):
        old,new=eb(e['old']),eb(e['new'])
        assert inverse.count(new)==1
        inverse=inverse.replace(new,old,1)
    assert forward==after and inverse==before
    checks.append({'reader_path':r['path'],'before_sha256':sha(before),'after_sha256':sha(after),'exact_forward':True,'exact_inverse':True,'edits':r['edits'],'pass':True})
    rows.append({'lane':'typography-v21','source':str(STAGE/r['path']),'reader_path':r['path'],'sha256':sha(after),'include_required':True})

for r in read(ROOT/'cohort_staging/typesetting_boundary/OVERLAY_PROPOSALS.json')['records']:
    replay_record('typography-boundary',r['before']['path'],r['active_path'],r['before']['sha256'],r['after']['sha256'],[{'old':r['old_display'],'new':r['new_display']}],r['after']['path'])

r=read(ROOT/'typesetting_root/RMT_DISPLAY_INVERSE.json')
replay_record('typography-root',ROOT/'recursive_metric_transport.tex',STAGE/r['file'],r['before_sha256'],r['after_sha256'],r['edits'])

r=read(ROOT/'cohort_staging/typesetting_root_conclusion/OVERLAY_PROPOSALS.json')
replay_record('typography-conclusion',r['accepted_before']['path'],r['active_source'],r['accepted_before']['sha256'],r['proposed_after']['sha256'],[{'old':e['old_display'],'new':e['new_display']} for e in r['records']],r['proposed_after']['path'])

r=read(ROOT/'STRUCTURAL_URL_PRESENTATION_INVERSE.json')
active=ROOT.parents[1]/r['file']
after=active.read_bytes()
assert sha(after)==r['after_sha256']
inverse=after
for e in reversed(r['changes']):
    old,new=e['old'].encode(),e['new'].encode()
    assert inverse.count(new)==1
    inverse=inverse.replace(new,old,1)
structural_newline_transport=False
if sha(inverse)!=r['before_sha256']:
    # This recorded URL wrapper was written by the builder using CRLF whereas
    # the accepted complete source uses LF. Verify that additional inverse too.
    assert b'\r\n' in inverse
    inverse=inverse.replace(b'\r\n',b'\n')
    structural_newline_transport=True
assert sha(inverse)==r['before_sha256']
forward=inverse
for e in r['changes']:
    old,new=e['old'].encode(),e['new'].encode()
    assert forward.count(old)==1
    forward=forward.replace(old,new,1)
if structural_newline_transport:forward=forward.replace(b'\n',b'\r\n')
assert forward==after
rel=active.relative_to(STAGE).as_posix()
checks.append({'reader_path':rel,'before_sha256':sha(inverse),'after_sha256':sha(after),'exact_forward':True,'exact_inverse':True,'edits':r['changes'],'explicit_lf_to_crlf_transport':structural_newline_transport,'pass':True})
rows.append({'lane':'typography-structural-url','source':str(active),'reader_path':rel,'sha256':sha(after),'include_required':True})

(HERE/'TYPOGRAPHY_INDEPENDENT_CHECK.json').write_text(json.dumps({'checks':checks,'pass':all(r['pass'] for r in checks)},indent=2)+'\n',encoding='utf-8')
(HERE/'EXPECTED_TYPOGRAPHY_PATCHES.json').write_text(json.dumps({'patches':rows},indent=2)+'\n',encoding='utf-8')
print(json.dumps({'checked':len(checks),'pass':True}))
