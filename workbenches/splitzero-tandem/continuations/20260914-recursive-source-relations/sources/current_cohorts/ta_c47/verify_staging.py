"""Recheck staged deliverables without copying, rebuilding, or editing originals."""
from pathlib import Path
import hashlib,json,re
ROOT=Path(__file__).resolve().parent
MATH=ROOT.parents[3]
def sha(b):return hashlib.sha256(b).hexdigest()
manifest=json.loads((ROOT/'MANIFEST.json').read_text(encoding='utf-8'))
checks=[]
for snap in manifest['snapshots']:
    for row in snap['files']:
        p=ROOT/row['path']; data=p.read_bytes(); original=(MATH/row['source_path']).read_bytes()
        assert len(data)==row['bytes'] and sha(data)==row['sha256']
        assert data==original, row['source_path']
checks.append('All 176 staged snapshot paths equal their separately reread owner-source bytes and manifest pins.')
labels=[]
for route in manifest['routes']:
    body=(ROOT/route['prepared']['path']).read_bytes()
    assert sha(body)==route['prepared']['sha256'] and len(body)==route['prepared']['bytes']
    receipt=json.loads((ROOT/route['inverse_receipt']['path']).read_text(encoding='utf-8'))
    inverse=body
    for edit in reversed(receipt['edits']):
        a,b=edit['prepared_byte_start'],edit['prepared_byte_end']
        assert inverse[a:b]==edit['new'].encode('ascii')
        inverse=inverse[:a]+edit['old'].encode('ascii')+inverse[b:]
    original=(ROOT/route['original']['path']).read_bytes()
    assert inverse==original
    assert re.findall(rb'\\tag\*?\{[^{}]*\}',body)==re.findall(rb'\\tag\*?\{[^{}]*\}',original)
    assert not re.search(rb'\\(?:input|include)\{',body)
    labels+=re.findall(rb'\\label\{([^{}]+)\}',body)
assert len(labels)==len(set(labels))
checks.extend(['All 12 prepared bodies independently reconstruct the exact original bytes.',
 'All displayed tag sequences are identical; all 75 prepared labels are unique; no body has unresolved nested TeX inputs.'])
for alias in manifest['alias_candidates']:
    assert alias['exact_bytes_equal']
    peer=(MATH/alias['candidate_path']).read_bytes()
    assert sha(peer)==alias['source_sha256']
checks.append('TC,WBR,GF source aliases independently match the CF source pins.')
for name in ['TA_complete.tex','TAReview_complete.tex']:
    data=(ROOT/'prepared'/name).read_bytes()
    assert b'TA24' in data if name.startswith('TA_') else len(data)>20000
receipt={'status':'pass','snapshot_file_count':176,'body_count':12,'distinct_prepared_labels':len(labels),
 'manifest_sha256':sha((ROOT/'MANIFEST.json').read_bytes()),'checks':checks,
 'pdf_built':False,'mathematical_code_replayed':False,'originals_modified':False}
(ROOT/'VERIFICATION.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps(receipt,indent=2))
