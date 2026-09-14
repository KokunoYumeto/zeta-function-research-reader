"""Record source-only readiness without relabelling the copied old PDF."""
from pathlib import Path
import hashlib, json, shutil
from prepare_successor import STAGE,SUPPORT,HISTORY,sha,row,save,preserve,verify_predecessor

for name in ['prepare_successor.py','assemble_graph_sources.py','finalize_source_readiness.py','WORK_LOG.md']:
    source=SUPPORT/name
    target=STAGE/'provenance/source_assembly_tools'/name
    target.parent.mkdir(parents=True,exist_ok=True)
    shutil.copy2(source,target)

preserve('README_CURRENT_EDITION.md')
(STAGE/'README_CURRENT_EDITION.md').write_text(
    '# Current source stage\n\n'
    'This repository is the cumulative phase-graph successor source stage.\n'
    'Read `README_GRAPH_SUCCESSOR.md` for source scope and the guarded serial build.\n'
    'The source assembly is complete; cumulative compilation and visual acceptance\n'
    'have not been performed by the source-stage task. The PDF copied at the root\n'
    'is the historical 1,624-page predecessor and does not typeset the new sources.\n\n'
    'The complete earlier current-edition README, manifests, proofs and PDF remain\n'
    'in the preserved predecessor history. No earlier source bytes were lost.\n',encoding='utf-8')
preserve('CURRENT_SOURCE_MANIFEST.json')
save(STAGE/'CURRENT_SOURCE_MANIFEST.json',{
    'status':'assembled_cumulative_successor_sources_not_yet_compiled',
    'complete_body_count':38,'expected_compiled_input_count':279,
    'source_assembly_receipt':{'path':'provenance/GRAPH_SUCCESSOR_SOURCE_ASSEMBLY.json',**row(STAGE/'provenance/GRAPH_SUCCESSOR_SOURCE_ASSEMBLY.json')},
    'source_expectations':{'path':'provenance/ASSEMBLED_SOURCE_EXPECTATIONS.json',**row(STAGE/'provenance/ASSEMBLED_SOURCE_EXPECTATIONS.json')},
    'predecessor_manifest':{'path':'history/cumulative_1624_predecessor/CURRENT_SOURCE_MANIFEST.json',**row(HISTORY/'CURRENT_SOURCE_MANIFEST.json')},
    'copied_root_pdf_role':'historical_predecessor_not_the_successor_typesetting',
    'build_command':'python scripts/build_graph_successor.py',
    'new_pdf_certified':False,'tex_runs_by_source_stage':0,
    'visual_review':'Required after actual successor compilation.'})
preservation=verify_predecessor()
assembly=json.loads((STAGE/'provenance/GRAPH_SUCCESSOR_SOURCE_ASSEMBLY.json').read_text(encoding='utf-8'))
expected=json.loads((STAGE/'provenance/ASSEMBLED_SOURCE_EXPECTATIONS.json').read_text(encoding='utf-8'))
for name,entry in expected['files'].items():
    if row(STAGE/name)!=entry: raise RuntimeError('Expected source differs: '+name)
ready={
    'status':'source_ready_for_serial_guarded_cumulative_build',
    'source_assembly_sha256':sha(STAGE/'provenance/GRAPH_SUCCESSOR_SOURCE_ASSEMBLY.json'),
    'expected_source_manifest_sha256':sha(STAGE/'provenance/ASSEMBLED_SOURCE_EXPECTATIONS.json'),
    'guarded_build_script_sha256':sha(STAGE/'scripts/build_graph_successor.py'),
    'current_source_manifest_sha256':sha(STAGE/'CURRENT_SOURCE_MANIFEST.json'),
    'baseline_file_count':preservation['count'],
    'baseline_current_paths_unchanged':len(preservation['unchanged_at_original_path']),
    'baseline_changed_files_preserved_in_history':preservation['preserved_at_historical_path'],
    'new_complete_body_count':38,'expected_compiled_input_count':len(expected['files']),
    'baseline_mutations':0,'tex_runs':0,'new_pdf_certified':False,
    'next_command':'python scripts/build_graph_successor.py',
    'actual_fls_verification':'Performed by guarded build after three completed XeLaTeX passes.',
    'visual_acceptance':'Not yet performed for cumulative successor.'}
save(STAGE/'provenance/SOURCE_BUILD_READINESS.json',ready)
print(json.dumps(ready,indent=2))
