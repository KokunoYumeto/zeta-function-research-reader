"""Synchronize current edition pointers with the new build; QA remains explicit."""
import json,shutil
from prepare_successor import STAGE,SUPPORT,sha,row,save

newsha='2e226e1def3dbf1f6c5170494be0656795fbdd6b930e00e7db584375b6e4c479'
oldsha='bf4e1c2a6d98140e0c25b305e60074918d92ba97f7f00ba689d0c6cf2da87397'
pdf=STAGE/'Split_Zero_Cohomology_and_Arithmetic_Weight_Control.pdf'
assert sha(pdf)==newsha
build=json.loads((STAGE/'build/GRAPH_SUCCESSOR_BUILD_RECEIPT.json').read_text(encoding='utf-8'))
assert build['pdf_sha256']==newsha and build['pages']==1929 and build['compiled_input_count']==279 and not any(build['warnings'].values())
for name in ['README_CURRENT_EDITION.md','README_GRAPH_SUCCESSOR.md']:
    p=STAGE/name;t=p.read_text(encoding='utf-8');assert oldsha in t;p.write_text(t.replace(oldsha,newsha),encoding='utf-8')
p=STAGE/'CURRENT_SOURCE_MANIFEST.json';m=json.loads(p.read_text(encoding='utf-8'));assert m['pdf_sha256']==oldsha
m.update({'pdf_sha256':newsha,'pdf_bytes':pdf.stat().st_size,
 'source_expectations':{'path':'provenance/ASSEMBLED_SOURCE_EXPECTATIONS.json',**row(STAGE/'provenance/ASSEMBLED_SOURCE_EXPECTATIONS.json')},
 'compiled_source_pins':{'path':'provenance/CURRENT_COMPILED_SOURCE_PINS.json',**row(STAGE/'provenance/CURRENT_COMPILED_SOURCE_PINS.json')},
 'build_receipt':{'path':'build/GRAPH_SUCCESSOR_BUILD_RECEIPT.json',**row(STAGE/'build/GRAPH_SUCCESSOR_BUILD_RECEIPT.json')},
 'source_ocq_spacing_transport':{'path':'provenance/OCQ_TAG_SPACING_TRANSPORT.json',**row(STAGE/'provenance/OCQ_TAG_SPACING_TRANSPORT.json')},
 'reviewed_intermediate_pdf_resolver':{'path':'provenance/BF4_REVIEW_PDF_HISTORICAL_RESOLVER.json',**row(STAGE/'provenance/BF4_REVIEW_PDF_HISTORICAL_RESOLVER.json')},
 'visual_review':'Full changed-page inspections complete, known collision repaired and freshly inspected; final exact page-authority aggregation pending.'})
save(p,m)
p=STAGE/'provenance/SOURCE_BUILD_READINESS.json';r=json.loads(p.read_text(encoding='utf-8'))
r.update({'pdf_sha256':newsha,'expected_source_manifest_sha256':sha(STAGE/'provenance/ASSEMBLED_SOURCE_EXPECTATIONS.json'),
 'current_source_manifest_sha256':sha(STAGE/'CURRENT_SOURCE_MANIFEST.json'),'tex_runs':9,
 'next_command':'Seal exact page-authority aggregation and full visual acceptance.'});save(p,r)
for path in [SUPPORT/'repair_ocq_tag_spacing.py',SUPPORT/'update_current_after_ocq.py']:
    shutil.copy2(path,STAGE/'provenance/source_assembly_tools'/path.name)
print(json.dumps({'current_manifest_sha256':sha(STAGE/'CURRENT_SOURCE_MANIFEST.json'),'pdf_sha256':newsha}))
