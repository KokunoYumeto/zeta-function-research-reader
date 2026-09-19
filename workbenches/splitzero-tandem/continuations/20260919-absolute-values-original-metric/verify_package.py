"""Read-only publication integrity checks, not mathematics or compilation."""
from pathlib import Path
import hashlib
import json

ROOT=Path(__file__).resolve().parent
def sha(raw):return hashlib.sha256(raw).hexdigest()
def read(name):
    p=(ROOT/name).resolve();assert p.is_relative_to(ROOT),name
    return p.read_bytes()
def load(name):return json.loads(read(name))
allow=load('ALLOWLIST.json');expected={r['path'] for r in allow['files']}|{'ALLOWLIST.json'}
assert {p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*') if p.is_file()}==expected
for row in allow['files']:
    raw=read(row['path']);assert len(raw)==row['bytes'] and sha(raw)==row['sha256'],row['path']
    assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==row['git_blob']
index=load('research_index/PROGRAM_INDEX.json');loc=load('research_index/FORMULA_LOCATORS.json')
assert len(index['result_nodes'])==132 and len(loc['locators'])==5344
assert index['sources']==loc['sources']
for key,row in index['sources'].items():
    raw=read(row['path']);assert len(raw)==row['bytes'] and sha(raw)==row['sha256'],key
for row in loc['locators']:
    assert 1<=row['line']<=len(read(index['sources'][row['source_id']]['path']).splitlines()),row
recoveries=[]
for row in load('arrival_03/assembly/INSERTION_MANIFEST.json')['cumulative']:
    raw=read(row['successor']['path']);assert sha(raw)==row['successor']['sha256']
    for edit in sorted(row['reversible_insertions'],key=lambda e:e['successor_byte_offset'],reverse=True):
        a=edit['successor_byte_offset'];b=a+edit['bytes'];assert sha(raw[a:b])==edit['sha256']
        raw=raw[:a]+raw[b:]
    assert sha(raw)==row['predecessor']['sha256'] and len(raw)==row['predecessor']['bytes']
    recoveries.append(dict(successor=row['successor']['path'],predecessor_sha256=sha(raw)))
foundation=[]
for row in load('arrival_03/foundation_updates/FOUNDATION_CORRECTIONS.json')['derivatives']:
    old=read(row['preserved']['path']);new=read(row['successor']['path'])
    assert sha(old)==row['predecessor']['sha256']==row['preserved']['sha256']
    assert sha(new)==row['successor']['sha256']
    canonical=new.decode('utf-8').replace('\r\n','\n').encode()
    canonical=canonical[:-row['complete_proof_appendix_bytes']].decode('utf-8')
    for op in reversed(row['exact_replacements']):
        a=op['character_offset'];b=a+len(op['after'])
        assert canonical[a:b]==op['after'],row['successor']['path']
        canonical=canonical[:a]+op['before']+canonical[b:]
    assert canonical==old.decode('utf-8').replace('\r\n','\n')
    foundation.append(dict(successor=row['successor']['path'],historical_bytes_exact=True,reverse_replacements_verified=True,newline_convention=row['newline_normalization']))
derivation=load('SOURCE_PINS_AND_PUBLIC_DERIVATION.json');mathfiles=0
for row in derivation['files']:
    if Path(row['public_path']).suffix.lower() in ('.tex','.pdf'):
        assert row['action']=='exact' and row['original']==row['public']
        assert sha(read(row['public_path']))==row['original']['sha256'];mathfiles+=1
available=load('PROVIDER_AVAILABILITY.json');excluded={row['sha256'] for row in available['unbundled']}
providers=load('arrival_03/PROVIDER_CLOSURE.json')['providers'];assert len(providers)==43
bundled=0
for row in providers:
    if row['sha256'] in excluded:continue
    raw=read(row['path']);assert sha(raw)==row['sha256'] and len(raw)==row['bytes'];bundled+=1
assert bundled==42 and len(excluded)==1
pairs=load('PDF_LATEX_MAP.json')['pairs'];assert len(pairs)==1
assert {r['pdf']['path'] for r in pairs}=={p for p in expected if p.lower().endswith('.pdf')}
for row in pairs:
    for role in ('pdf','complete_latex'):
        raw=read(row[role]['path']);assert sha(raw)==row[role]['sha256'] and len(raw)==row[role]['bytes']
incoming=[p for p in expected if p.startswith('arrival_03/inputs/')];assert len(incoming)==10
assert all(p.lower().endswith('.md') for p in incoming)
assert sha(read('prior_intakes/supporting_sources/D032_FULL_EN.tex'))=='316cbc52349cd6bc2dedbd0a493a530696d367ca0e292fc64ee3c3973327567e'
print(json.dumps(dict(status='passed_package_identity_locator_and_recovery_checks',files=len(expected),result_nodes=132,
    formula_locators=5344,index_source_keys=len(index['sources']),provider_entries=43,bundled_provider_entries=42,
    unbundled_archival_container=1,exact_tex_pdf_files=mathfiles,pdf_complete_latex_pairs=1,
    original_classified_mathematical_notes=10,cumulative_recoveries=recoveries,foundation_recoveries=foundation,
    mathematical_reaudit=False,compilation=False,remote_actions=False),indent=2))
