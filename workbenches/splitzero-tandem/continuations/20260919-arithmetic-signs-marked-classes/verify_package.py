"""Read-only package integrity checks; not mathematics, compilation or Lean."""
from pathlib import Path
import hashlib
import json

ROOT=Path(__file__).resolve().parent
def sha(raw): return hashlib.sha256(raw).hexdigest()
def read(name):
    p=(ROOT/name).resolve(); assert p.is_relative_to(ROOT),name
    return p.read_bytes()
def load(name): return json.loads(read(name))

allow=load('ALLOWLIST.json')
expected={row['path'] for row in allow['files']}|{'ALLOWLIST.json'}
assert {p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*') if p.is_file()}==expected
for row in allow['files']:
    raw=read(row['path'])
    assert len(raw)==row['bytes'] and sha(raw)==row['sha256'],row['path']
    assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==row['git_blob']
index=load('research_index/PROGRAM_INDEX.json'); loc=load('research_index/FORMULA_LOCATORS.json')
assert len(index['result_nodes'])==116 and len(loc['locators'])==4956
assert index['sources']==loc['sources']
for key,row in index['sources'].items():
    raw=read(row['path']); assert len(raw)==row['bytes'] and sha(raw)==row['sha256'],key
for row in loc['locators']:
    assert 1<=row['line']<=len(read(index['sources'][row['source_id']]['path']).splitlines()),row
recoveries=[]
for intake in ('first_intake','arrival_02'):
    manifest=load(intake+'/assembly/INSERTION_MANIFEST.json')
    for row in manifest['cumulative']:
        raw=read(row['successor']['path']); assert sha(raw)==row['successor']['sha256']
        for edit in sorted(row['reversible_insertions'],key=lambda e:e['successor_byte_offset'],reverse=True):
            start=edit['successor_byte_offset']; end=start+edit['bytes']
            assert sha(raw[start:end])==edit['sha256']
            raw=raw[:start]+raw[end:]
        assert sha(raw)==row['predecessor']['sha256'] and len(raw)==row['predecessor']['bytes']
        recoveries.append(dict(intake=intake,successor=row['successor']['path'],predecessor_sha256=sha(raw)))
derivation=load('SOURCE_PINS_AND_PUBLIC_DERIVATION.json'); math_files=0
for row in derivation['files']:
    if Path(row['public_path']).suffix.lower() in ('.tex','.pdf'):
        assert row['action']=='exact' and row['original']==row['public']
        assert sha(read(row['public_path']))==row['original']['sha256']; math_files+=1
providers=load('arrival_02/PROVIDER_CLOSURE.json')['providers']; assert len(providers)==32
for row in providers: assert sha(read(row['path']))==row['sha256']
assert sha(read('first_intake/supporting_sources/D032_FULL_EN.tex'))=='316cbc52349cd6bc2dedbd0a493a530696d367ca0e292fc64ee3c3973327567e'
assert sha(read('arrival_02/providers/EC_COMPLETE.tex'))=='0cf2cf0117ab8c4204b0da9aaab8bcba5237b69d0679267899844bcfef72fc2e'
pairs=load('PDF_LATEX_MAP.json')['pairs']
assert {row['pdf']['path'] for row in pairs}=={p for p in expected if p.lower().endswith('.pdf')}
for row in pairs:
    for role in ('pdf','complete_latex'):
        raw=read(row[role]['path']); assert sha(raw)==row[role]['sha256'] and len(raw)==row[role]['bytes']
print(json.dumps(dict(status='passed_package_identity_and_locator_checks',files=len(expected),result_nodes=116,
    formula_locators=4956,index_source_keys=len(index['sources']),decisive_original_providers=32,
    exact_tex_and_pdf_files=math_files,pdf_complete_latex_pairs=len(pairs),cumulative_recoveries=recoveries,mathematical_reaudit=False,
    compilation=False,remote_actions=False),indent=2))
