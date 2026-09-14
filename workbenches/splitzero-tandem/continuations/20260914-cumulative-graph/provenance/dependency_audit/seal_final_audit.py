"""Bind the independently checked source closure to the actual compiled PDF."""
from pathlib import Path
import hashlib,json,datetime

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
STAGE=ROOT/'cumulative_source_v1'
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
check=read(HERE/'FINAL_ASSEMBLY_CHECK.json')
graph=read(HERE/'FINAL_ASSEMBLY_INCLUSION_GRAPH.json')
build=read(STAGE/'build/CURRENT_BUILD_RECEIPT.json')
pins=read(STAGE/'provenance/CURRENT_COMPILED_SOURCE_PINS.json')['files']
assert check['pass']
assert pins==build['compiled_sources']
missing=set(graph['files'])-set(pins)
assert not missing
for rel,r in pins.items():
    assert sha(STAGE/rel)==r['sha256'],('recorded source changed',rel)
for rel,r in graph['files'].items():
    assert r['sha256']==pins[rel]['sha256']
pdf=STAGE/build['pdf']
assert sha(pdf)==build['pdf_sha256']
assert all(not x for x in build['warnings'].values())
for name in ['AP_COMPLETE_BODY_TRANSFER_CHECK.json','BC_COMPLETE_BODY_TRANSFER_CHECK.json',
             'CONCLUSION_COMPLETE_BLOCK_TRANSFER_CHECK.json','TYPOGRAPHY_INDEPENDENT_CHECK.json']:
    assert read(HERE/name)['pass'],name
evidence_names=['FINAL_ASSEMBLY_CHECK.json','FINAL_ASSEMBLY_INCLUSION_GRAPH.json',
 'EXPECTED_FINAL_ACTIVE_PATCHES.json','HISTORICAL_PRESERVATION_CHECK.json',
 'AP_COMPLETE_BODY_TRANSFER_CHECK.json','BC_COMPLETE_BODY_TRANSFER_CHECK.json',
 'CONCLUSION_COMPLETE_BLOCK_TRANSFER_CHECK.json','TYPOGRAPHY_INDEPENDENT_CHECK.json',
 'DEPENDENCY_CHANGE_USE_LEDGER.json','ROOT_AND_SIGNED_PROOF_REVIEW.json',
 'BOUNDARY_NEW_PROOFS_REVIEW.md','READING_AND_FINDINGS.md']
out={'status':'PASS: independently checked active proof propagation and compiler/PDF binding',
 'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'scope':'Bounded theorem-level cross-lane dependency closure, complete accepted source transfer, historical preservation and actual compiler source binding. This does not claim a new independent proof of every statement in the entire cumulative reader.',
 'assembly':str(STAGE),'pdf':{'path':str(pdf),'sha256':sha(pdf),'bytes':pdf.stat().st_size,'pages_from_build_receipt':build['pages']},
 'recursive_tex_files':len(graph['files']),'recursive_input_edges':len(graph['edges']),
 'compiler_recorded_sources':len(pins),'compiler_only_inputs':sorted(set(pins)-set(graph['files'])),
 'all_recursive_sources_compiled_with_same_hash':True,
 'explicit_active_paths_checked':len(check['patch_checks']),
 'reversible_presentation_source_maps':len(read(HERE/'TYPOGRAPHY_INDEPENDENT_CHECK.json')['checks']),
 'complete_conclusion_block_checks':len(read(HERE/'CONCLUSION_COMPLETE_BLOCK_TRANSFER_CHECK.json')['checks']),
 'historical_preservation':check['historical'],
 'unresolved_findings_in_audited_scope':[],
 'warning_counts':{k:len(v) for k,v in build['warnings'].items()},
 'evidence':[{ 'path':str(HERE/name),'sha256':sha(HERE/name)} for name in evidence_names]}
(HERE/'FINAL_AUDIT_RECEIPT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:out[k] for k in ['status','recursive_tex_files','compiler_recorded_sources','explicit_active_paths_checked','reversible_presentation_source_maps','complete_conclusion_block_checks','unresolved_findings_in_audited_scope']},indent=2))
