"""Seal the fully reviewed cumulative PDF and exact current source pointers."""
import json,shutil
from pathlib import Path
from prepare_successor import STAGE,SUPPORT,sha,row,save,verify_predecessor

qa=SUPPORT/'page_qa';finalqa=qa/'candidate_2e226e1d_guarded/final_seal_v2'
acceptance=finalqa/'FINAL_PDF_VISUAL_ACCEPTANCE.json'
expected='d5a4bb691f54c0bfee8fa05981e77ce56e1d4c371c246967baf851e538297f4c'
if sha(acceptance)!=expected:raise RuntimeError('Unexpected final visual acceptance')
a=json.loads(acceptance.read_text(encoding='utf-8'))
pdf=STAGE/'Split_Zero_Cohomology_and_Arithmetic_Weight_Control.pdf'
if a['status']!='PASS' or a['pages']!=1929 or a['pdf_sha256']!=sha(pdf):raise RuntimeError('Visual acceptance PDF mismatch')
history=STAGE/'history/source_assembly_revisions/before_final_visual_acceptance'
names=['CURRENT_SOURCE_MANIFEST.json','README_CURRENT_EDITION.md','README_GRAPH_SUCCESSOR.md','provenance/SOURCE_BUILD_READINESS.json','provenance/SUCCESSOR_SOURCE_ASSEMBLY_STATE.json','provenance/PREDECESSOR_PRESERVATION_CHECK.json']
for name in names:
    p=STAGE/name;t=history/name;t.parent.mkdir(parents=True,exist_ok=True)
    if t.exists() and t.read_bytes()!=p.read_bytes():raise RuntimeError('Existing finalization history conflict')
    if not t.exists():shutil.copy2(p,t)

# This is a compact exact receipt annex; raster evidence retains its original
# pinned workspace locations instead of making a false portable-raster claim.
annex=STAGE/'provenance/cumulative_visual_qa';copied=[]
targets=[(finalqa/'FINAL_PDF_VISUAL_ACCEPTANCE.json','FINAL_PDF_VISUAL_ACCEPTANCE.json'),
 (finalqa/'INTERMEDIATE_PAGE_AUTHORITY.json','INTERMEDIATE_PAGE_AUTHORITY.json'),
 (qa/'candidate_2e226e1d_guarded/EXACT_RENDER_COMPARISON.json','EXACT_RENDER_COMPARISON.json'),
 (qa/'candidate_2e226e1d/ACTUAL_PAGE_970_REVIEW.json','ACTUAL_PAGE_970_REVIEW.json'),
 (qa/'candidate_2e226e1d/changed_pages/page_0970.png','page_0970.png'),
 (qa/'candidate_bf4e1c2a/SUCCESSOR_RENDER_TRANSFER.json','strict/SUCCESSOR_RENDER_TRANSFER.json'),
 (qa/'contract_review/COMPLETED_SUCCESSOR_OUTPUT_AUDIT.json','strict/COMPLETED_SUCCESSOR_OUTPUT_AUDIT.json')]
for source in (qa/'footer_digit_composition').rglob('*'):
    if source.is_file() and source.suffix in ['.json','.md','.py','.png']:
        targets.append((source,'footer/'+source.relative_to(qa/'footer_digit_composition').as_posix()))
for source in (SUPPORT/'contract_review').rglob('*'):
    if source.is_file() and source.suffix in ['.json','.md','.py']:
        targets.append((source,'independent/'+source.relative_to(SUPPORT/'contract_review').as_posix()))
for source in (qa/'candidate_bf4e1c2a/reviews').rglob('*'):
    if source.is_file() and source.suffix in ['.json','.md','.csv']:
        targets.append((source,'actual/'+source.relative_to(qa/'candidate_bf4e1c2a/reviews').as_posix()))
for source in [qa/'after_ocq_exact_transfer.py',qa/'seal_cumulative_visual_acceptance.py']:
    targets.append((source,'tools/'+source.name))
for source,relative in targets:
    target=annex/relative;target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(source,target)
    if row(source)!=row(target):raise RuntimeError('Receipt copy differs')
    copied.append({'source':str(source),'annex_path':relative,**row(target)})
save(annex/'ANNEX_COPY_MANIFEST.json',{'status':'exact_receipt_copies_verified','files':copied,
 'scope':'Complete mathematical source is in the repository. This annex preserves visual receipts and selected direct evidence. Full raster sets and the original cross-page record inventories remain at their exact pinned workspace paths; no self-contained raster archive is claimed.'})

current_path=STAGE/'CURRENT_SOURCE_MANIFEST.json';m=json.loads(current_path.read_text(encoding='utf-8'))
m.update({'status':'compiled_and_fully_visually_accepted_cumulative_successor',
 'visual_review':'PASS: all1929 physical pages covered by explicit actual inspection and independently audited exact pixel transports.',
 'visual_acceptance':{'path':'provenance/cumulative_visual_qa/FINAL_PDF_VISUAL_ACCEPTANCE.json',**row(annex/'FINAL_PDF_VISUAL_ACCEPTANCE.json')},
 'visual_receipt_annex':{'path':'provenance/cumulative_visual_qa/ANNEX_COPY_MANIFEST.json',**row(annex/'ANNEX_COPY_MANIFEST.json')},
 'included_mathematical_wave':'38 complete phase-graph and relation-control proof bodies through PGRT, PGRC, PGGL and corresponding complete ACM/HC/R63-R66 backward-use updates.',
 'entire_programme_complete':False})
save(current_path,m)
(STAGE/'README_CURRENT_EDITION.md').write_text('''# Current cumulative edition

The cumulative phase-graph and relation-control edition is **1,929 pages**.
It includes the complete 38-body proof wave and the updated earlier ACM, HC,
and R63–R66 use sites. Every full original and prior edition remains preserved.

The current PDF is `Split_Zero_Cohomology_and_Arithmetic_Weight_Control.pdf`.
SHA-256: `'''+sha(pdf)+'''`.

Three compiler passes completed with **279 exact source inputs** and no
recorded warnings. All 1,929 pages have visual acceptance. The final PDF has
1,928 complete-page RGB and geometry matches to accepted intermediate pages;
the repaired OCQ.1 page was freshly inspected. The intermediate authority
explicitly distinguishes actual page inspections, inherited reviewed pixels,
and the 305 exact footer-only compositions. Its known collision is excluded
from inheritance. Read `provenance/cumulative_visual_qa` for the exact chain.

The full source repository builds through `python scripts/build_graph_successor.py`.
The research programme continues beyond this edition's explicitly recorded wave.
''',encoding='utf-8')
p=STAGE/'README_GRAPH_SUCCESSOR.md';t=p.read_text(encoding='utf-8')
old='''Its complete rendered-page review is in progress; compilation does not certify
visual acceptance. The isolated 295-page reader has separate build/review
receipts, which do not certify this cumulative layout. The full predecessor PDF
and first cumulative candidate remain in history.'''
new='''Its complete rendered-page review is accepted. The exact 1,929-page authority
chain is recorded in `provenance/cumulative_visual_qa/FINAL_PDF_VISUAL_ACCEPTANCE.json`.
Every prior PDF, the intermediate collision finding, and its reversible spacing
repair remain preserved. The isolated reader has separate build/review receipts.'''
if t.count(old)!=1:raise RuntimeError('README final status anchor differs')
p.write_text(t.replace(old,new),encoding='utf-8')
ready_path=STAGE/'provenance/SOURCE_BUILD_READINESS.json';r=json.loads(ready_path.read_text(encoding='utf-8'))
r.update({'status':'cumulative_build_and_full_visual_acceptance_complete','current_source_manifest_sha256':sha(current_path),
 'new_pdf_certified':'Three-pass build, exact279-source closure, and all1929-page visual acceptance complete for this exact edition.',
 'visual_acceptance':{'path':'provenance/cumulative_visual_qa/FINAL_PDF_VISUAL_ACCEPTANCE.json',**row(annex/'FINAL_PDF_VISUAL_ACCEPTANCE.json')},
 'next_command':'Continue subsequent mathematical waves in a successor while preserving this accepted edition.'});save(ready_path,r)
save(STAGE/'provenance/SUCCESSOR_SOURCE_ASSEMBLY_STATE.json',{'status':'cumulative_successor_complete_for_recorded_wave',
 'pdf_sha256':sha(pdf),'pages':1929,'compiled_input_count':279,'complete_new_body_count':38,'tex_runs':9,
 'visual_acceptance_sha256':expected,'whole_programme_complete':False})
shutil.copy2(Path(__file__),STAGE/'provenance/source_assembly_tools'/Path(__file__).name)
preserved=verify_predecessor()
handoff={'status':'PASS_SOURCE_BUILD_AND_FULL_VISUAL_ACCEPTANCE_FOR_RECORDED_WAVE','repository':str(STAGE),'pdf':{'path':str(pdf),**row(pdf)},
 'pages':1929,'complete_new_body_count':38,'compiled_input_count':279,'current_source_manifest':{'path':str(current_path),**row(current_path)},
 'build_receipt':{'path':str(STAGE/'build/GRAPH_SUCCESSOR_BUILD_RECEIPT.json'),**row(STAGE/'build/GRAPH_SUCCESSOR_BUILD_RECEIPT.json')},
 'visual_acceptance':{'path':str(annex/'FINAL_PDF_VISUAL_ACCEPTANCE.json'),**row(annex/'FINAL_PDF_VISUAL_ACCEPTANCE.json')},
 'predecessor_preservation':{'path':str(STAGE/'provenance/PREDECESSOR_PRESERVATION_CHECK.json'),**row(STAGE/'provenance/PREDECESSOR_PRESERVATION_CHECK.json')},
 'baseline_files_preserved':preserved['count'],'baseline_mutations':0,'remote_publication':False,'whole_programme_complete':False}
save(STAGE/'CUMULATIVE_GRAPH_SUCCESSOR_HANDOFF.json',handoff)
print(json.dumps({'status':handoff['status'],'handoff_sha256':sha(STAGE/'CUMULATIVE_GRAPH_SUCCESSOR_HANDOFF.json'),'current_manifest_sha256':sha(current_path),'preserved_baseline_files':preserved['count']}))
