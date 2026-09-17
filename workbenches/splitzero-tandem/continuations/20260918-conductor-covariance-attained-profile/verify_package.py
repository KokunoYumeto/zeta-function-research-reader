"""Read-only checks of the public package. No external inputs or dependencies."""
from pathlib import Path
import hashlib
import json
import re

ROOT=Path(__file__).resolve().parent
def sha(b): return hashlib.sha256(b).hexdigest()
def read(p):
    path=(ROOT/p).resolve()
    assert path.is_relative_to(ROOT),p
    return path.read_bytes()
def load(p): return json.loads(read(p))

allow=load('ALLOWLIST.json')
for row in allow['files']:
    b=read(row['path'])
    assert len(b)==row['bytes'] and sha(b)==row['sha256'],row['path']
    assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==row['git_blob']
index=load('research_index/PROGRAM_INDEX.json')
loc=load('research_index/FORMULA_LOCATORS.json')
assert len(index['result_nodes'])==23
assert len(index['sources'])==16 and loc['sources']==index['sources']
for key,row in index['sources'].items():
    b=read(row['path'])
    assert len(b)==row['bytes'] and sha(b)==row['sha256'],key
for row in loc['locators']:
    lines=read(index['sources'][row['source_id']]['path']).splitlines()
    assert 1<=row['line']<=len(lines),row
assert len(loc['locators'])==3908
insertion=load('evidence/assembly/INSERTION_MANIFEST.json')
recoveries=[]
for row in insertion['cumulative']:
    b=read(row['successor']['path'])
    assert sha(b)==row['successor']['sha256']
    for edit in sorted(row['reversible_insertions'],key=lambda e:e['successor_byte_offset'],reverse=True):
        a=edit['successor_byte_offset']; n=edit['bytes']
        assert sha(b[a:a+n])==edit['sha256']
        b=b[:a]+b[a+n:]
    assert len(b)==row['predecessor']['bytes'] and sha(b)==row['predecessor']['sha256']
    recoveries.append({'successor':row['successor']['path'],'predecessor_sha256':sha(b)})
body=read('DUAL_WEB_FULL_BODY.tex')
for target in ['DUAL_WEB_PROOF_SUPPLEMENT.tex']+[r['successor']['path'] for r in insertion['cumulative']]:
    b=read(target)
    assert b.count(body)==1,target
    # Complete main TeX sources require packages, but no separate source inputs.
    text=b.decode('utf-8')
    text=re.sub(r'(?<!\\)%[^\n]*','',text)
    assert not re.search(r'\\(?:input|include|bibliography)\s*\{',text),target
manifest=load('SOURCE_PINS_AND_PUBLIC_DERIVATION.json')
mathfiles=[]
for row in manifest['files']:
    if Path(row['public_path']).suffix.lower() in ['.tex','.pdf']:
        b=read(row['public_path'])
        assert row['action']=='exact' and row['original']==row['public']
        assert sha(b)==row['original']['sha256']
        mathfiles.append(row['public_path'])
# This is an exact insertion-only citation derivative, not a rewritten proof.
original=read(index['sources']['weighted_conductor']['path'])
cited=read(index['sources']['weighted_conductor_cited_derivative']['path'])
stripped=re.sub(rb'% BEGIN WCF_CITATION_INSERT[^\r\n]*\r?\n.*?% END WCF_CITATION_INSERT[^\r\n]*\r?\n',b'',cited,flags=re.S)
if stripped!=original:
    spans=load('evidence/citation/INSERTION_SPANS.json')
    # The insertion receipt explicitly names its delimiters; no heuristic deletion.
    rows=spans.get('insertions',spans.get('spans',[])) if isinstance(spans,dict) else spans
    stripped=cited
    for row in reversed(rows):
        marker=row.get('text_utf8') or row.get('text') or row.get('inserted_text')
        if marker:
            raw=marker.encode(); assert stripped.count(raw)==1; stripped=stripped.replace(raw,b'',1)
assert stripped==original,'Citation derivative recovery failed'
print(json.dumps({'status':'passed_bounded_package_integrity_checks','allowlisted_files':len(allow['files'])+1,
                  'result_nodes':23,'source_snapshots':16,'formula_locators':3908,
                  'exact_math_files':len(mathfiles),'cumulative_recoveries':recoveries,
                  'standalone_and_cumulative_TeX_source_inputs':0,'conductor_citation_recovery':True,
                  'remote_actions':False,'new_mathematical_audit':False},indent=2))
