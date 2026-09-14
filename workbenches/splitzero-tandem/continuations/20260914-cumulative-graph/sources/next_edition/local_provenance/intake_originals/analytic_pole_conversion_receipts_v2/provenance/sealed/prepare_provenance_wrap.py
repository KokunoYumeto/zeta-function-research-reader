"""Exact non-mathematical provenance wrapping; original proof TeX stays intact."""
from pathlib import Path
import hashlib,json
R=Path(__file__).resolve().parent
def pin(b):return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
source=R/'build/analytic_pole/endpoint_analytic_pole_source.tex';raw=source.read_bytes()
tokens=[
 (r'ACTUAL\_TAYLOR\_UNIT\_FORMAL\_GAUGE.md','ACTUAL_TAYLOR_UNIT_FORMAL_GAUGE.md'),
 (r'../f1\_scaling\_frobenius/ACTUAL\_TAU\_SCALING\_AND\_EXPONENTIAL\_FLOW.md','../f1_scaling_frobenius/ACTUAL_TAU_SCALING_AND_EXPONENTIAL_FLOW.md'),
 ('9ded2486160b76bf65f92d44b73cdd0c59a3ca7e5334f88682e10592d5a45b2f','9ded2486160b76bf65f92d44b73cdd0c59a3ca7e5334f88682e10592d5a45b2f'),
 ('4e4cb66e3cbbff6379ae389ddaaad65045ac0ed380f17a87ac7c4241c45e6c08','4e4cb66e3cbbff6379ae389ddaaad65045ac0ed380f17a87ac7c4241c45e6c08')]
edits=[]
for before,visible in tokens:
    b=before.encode();after=(r'\nolinkurl{'+visible+'}').encode()
    if raw.count(b)!=1:raise RuntimeError('Expected exact one provenance token: '+before)
    a=raw.index(b);edits.append({'original_start_byte':a,'original_end_byte':a+len(b),'before':before,'after':after.decode(),'visible_token':visible})
edits.sort(key=lambda e:e['original_start_byte']);parts=[];cursor=0;offset=0
for e in edits:
    prefix=raw[cursor:e['original_start_byte']];parts.append(prefix);offset+=len(prefix)
    after=e['after'].encode();e['reader_start_byte']=offset;e['reader_end_byte']=offset+len(after)
    parts.append(after);offset+=len(after);cursor=e['original_end_byte']
parts.append(raw[cursor:]);reader=b''.join(parts);inverse=reader
for e in reversed(edits):
    a,b=e['reader_start_byte'],e['reader_end_byte']
    if inverse[a:b]!=e['after'].encode():raise RuntimeError('Provenance wrap inverse span mismatch')
    inverse=inverse[:a]+e['before'].encode()+inverse[b:]
if inverse!=raw:raise RuntimeError('Provenance wrap inverse failed')
conversion=json.loads((R/'build/analytic_pole/endpoint_analytic_pole_conversion.json').read_text(encoding='utf-8'))
spans=[]
for span in conversion['literal_emission_spans']:
    if span['node_type']!='Math':continue
    a,b=span['payload_start_byte'],span['payload_end_byte'];delta=0
    for e in edits:
        if not(e['original_end_byte']<=a or e['original_start_byte']>=b):raise RuntimeError('Provenance edit overlaps mathematical payload')
        if e['original_end_byte']<=a:delta+=len(e['after'].encode())-len(e['before'].encode())
    if raw[a:b]!=reader[a+delta:b+delta] or hashlib.sha256(reader[a+delta:b+delta]).hexdigest()!=span['payload_sha256']:
        raise RuntimeError('Full emitted mathematical payload changed')
    spans.append({'index':span['index'],'original_start_byte':a,'original_end_byte':b,'reader_start_byte':a+delta,'reader_end_byte':b+delta,'payload_sha256':span['payload_sha256'],'bytes':span['payload_bytes']})
if len(spans)!=256:raise RuntimeError('Incomplete full-proof mathematical payload transport')
target=R/'layout/analytic_pole_source.tex';target.parent.mkdir(exist_ok=True)
if target.exists():raise RuntimeError('Reader derivative already exists')
target.write_bytes(reader)
wrapper=R/'tex/analytic_pole.tex';w=wrapper.read_bytes();old=b'build/analytic_pole/endpoint_analytic_pole_source.tex';new=b'layout/analytic_pole_source.tex'
if w.count(old)!=1:raise RuntimeError('Expected one full-source input route')
new_wrapper=w.replace(old,new,1)
if new_wrapper.replace(new,old,1)!=w:raise RuntimeError('Wrapper inverse failed')
wtarget=R/'tex/analytic_pole_reader.tex'
if wtarget.exists():raise RuntimeError('Reader wrapper already exists')
wtarget.write_bytes(new_wrapper)
receipt={'schema':'analytic-pole-nonmathematical-provenance-wrap-v1','status':'exact-wrapper-and-text-inverses-verified',
 'original_tex':{'path':source.relative_to(R).as_posix(),**pin(raw)},'reader_tex':{'path':target.relative_to(R).as_posix(),**pin(reader)},
 'edits':edits,'exact_inverse_restores_every_original_TeX_byte':True,'all_256_math_payloads_preserved_exactly':True,
 'math_payload_byte_transport':spans,'original_wrapper':{'path':wrapper.relative_to(R).as_posix(),**pin(w)},
 'reader_wrapper':{'path':wtarget.relative_to(R).as_posix(),**pin(new_wrapper)},
 'wrapper_path_edit':{'before':old.decode(),'after':new.decode(),'inverse_restores_entire_wrapper':True},
 'scope':'Only two provenance filename/path tokens and two SHA-256 tokens receive breakable literal wrapping. Their visible characters, all mathematical expressions and all surrounding proof prose are retained. No formula layout or mathematical payload changes.'}
(R/'layout/PROVENANCE_WRAP.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='')
print(json.dumps({'reader_tex':pin(reader),'reader_wrapper':pin(new_wrapper),'math_payloads':len(spans),'provenance_edits':len(edits)}))
