"""Read-only source-integrity checks; no mathematics or compilation."""
from pathlib import Path
import hashlib
import json
import re
from urllib.parse import unquote

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
assert len(index['result_nodes'])==140 and len(loc['locators'])==5507
assert index['sources']==loc['sources']
for key,row in index['sources'].items():
    raw=read(row['path']);assert len(raw)==row['bytes'] and sha(raw)==row['sha256'],key
for row in loc['locators']:
    assert 1<=row['line']<=len(read(index['sources'][row['source_id']]['path']).splitlines()),row
recoveries=[]
for row in load('arrival_04/assembly/INSERTION_MANIFEST.json')['cumulative']:
    raw=read(row['successor']['path']);assert sha(raw)==row['successor']['sha256']
    for edit in sorted(row['reversible_insertions'],key=lambda e:e['successor_byte_offset'],reverse=True):
        a=edit['successor_byte_offset'];b=a+edit['bytes'];assert sha(raw[a:b])==edit['sha256']
        raw=raw[:a]+raw[b:]
    assert sha(raw)==row['predecessor']['sha256'] and len(raw)==row['predecessor']['bytes']
    recoveries.append(dict(successor=row['successor']['path'],predecessor_sha256=sha(raw)))
assert len(recoveries)==3
derivation=load('SOURCE_PINS_AND_PUBLIC_DERIVATION.json');mathfiles=0
for row in derivation['files']:
    if Path(row['public_path']).suffix.lower() in ('.tex','.pdf'):
        assert row['action']=='exact' and row['original']==row['public']
        assert sha(read(row['public_path']))==row['original']['sha256'];mathfiles+=1
providers=load('arrival_04/PROVIDER_CLOSURE.json')['providers'];assert len(providers)==14
for row in providers:
    raw=read(row['path']);assert sha(raw)==row['sha256'] and len(raw)==row['bytes'],row['path']
pairs=load('PDF_LATEX_MAP.json')['pairs'];assert len(pairs)==1
assert {r['pdf']['path'] for r in pairs}=={p for p in expected if p.lower().endswith('.pdf')}
for row in pairs:
    for role in ('pdf','complete_latex'):
        raw=read(row[role]['path']);assert sha(raw)==row[role]['sha256'] and len(raw)==row[role]['bytes']
assert sha(read('prior_intakes/supporting_sources/D032_FULL_EN.tex'))=='316cbc52349cd6bc2dedbd0a493a530696d367ca0e292fc64ee3c3973327567e'
dated=load('DATED_RESULTS_INDEX.json');assert len(dated['entries'])==10
for row in dated['entries']:
    for point in row['proof_locations']:assert point['source_id'] in index['sources']
for target in re.findall(r'\]\(([^)]+)\)',read('DATED_PROOF_LINKS.md').decode()):
    assert unquote(target) in expected,target
assert len(load('timeline_evidence/COMMIT_CHRONOLOGY.json')['commits'])==49
assert all('/history/' not in p and '/recovered_provenance/' not in p and 'commits_page_1.json' not in p for p in expected)
print(json.dumps(dict(status='passed_package_identity_locator_and_recovery_checks',files=len(expected),result_nodes=140,
    formula_locators=5507,index_source_keys=len(index['sources']),complete_decisive_provider_entries=14,
    exact_tex_pdf_files=mathfiles,pdf_complete_latex_pairs=1,dated_result_entries=10,scoped_chronology_commits=49,
    cumulative_recoveries=recoveries,mathematical_reaudit=False,compilation=False,remote_actions=False),indent=2))
