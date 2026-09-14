"""Make the current source/PDF status precise after the clean cumulative build."""
from pathlib import Path
import json, shutil
from prepare_successor import STAGE,SUPPORT,HISTORY,sha,row,save,verify_predecessor

pdf=STAGE/'Split_Zero_Cohomology_and_Arithmetic_Weight_Control.pdf'
pin=sha(pdf)
if pin!='bf4e1c2a6d98140e0c25b305e60074918d92ba97f7f00ba689d0c6cf2da87397':
    raise RuntimeError('Unexpected final cumulative candidate.')
build=json.loads((STAGE/'build/GRAPH_SUCCESSOR_BUILD_RECEIPT.json').read_text(encoding='utf-8'))
if build['pdf_sha256']!=pin or build['pages']!=1929 or build['compiled_input_count']!=279 or any(build['warnings'].values()):
    raise RuntimeError('Clean cumulative build facts do not match.')
revision=STAGE/'history/source_assembly_revisions/before_clean_cumulative_status'
for name in ['README_GRAPH_SUCCESSOR.md','README_CURRENT_EDITION.md','CURRENT_SOURCE_MANIFEST.json','provenance/SOURCE_BUILD_READINESS.json']:
    target=revision/name; target.parent.mkdir(parents=True,exist_ok=True); shutil.copy2(STAGE/name,target)
readme=STAGE/'README_GRAPH_SUCCESSOR.md'
text=readme.read_text(encoding='utf-8')
old='''**Source-stage status:** assembled, not yet cumulatively typeset or visually
accepted. Any PDF currently at the repository root or in its copied `build`
folder is the historical predecessor PDF. It is not a PDF of these new sources.
The isolated 295-page reader has its own independent build and review receipts.
Those receipts do not certify the cumulative successor's layout.'''
new='''**Current status:** the complete cumulative source compiles to 1,929 pages in
three passes with 279 exact compiler inputs and no undefined commands, missing
glyphs, reference warnings, font warnings or overfull boxes. The current PDF is
the cumulative successor with SHA-256
`bf4e1c2a6d98140e0c25b305e60074918d92ba97f7f00ba689d0c6cf2da87397`.
Its complete rendered-page review is in progress; compilation does not certify
visual acceptance. The isolated 295-page reader has separate build/review
receipts, which do not certify this cumulative layout. The full predecessor PDF
and first cumulative candidate remain in history.'''
if text.count(old)!=1: raise RuntimeError('README state anchor changed.')
readme.write_text(text.replace(old,new),encoding='utf-8')
(STAGE/'README_CURRENT_EDITION.md').write_text(
    '# Current cumulative edition\n\n'
    'The cumulative phase-graph successor compiles to **1,929 pages** through\n'
    'three passes, with all **279 actual source inputs** matching the assembled\n'
    'full-source hashes and all recorded warning categories empty.\n\n'
    'The current PDF is `Split_Zero_Cohomology_and_Arithmetic_Weight_Control.pdf`;\n'
    'its SHA-256 is `'+pin+'`. Full rendered-page review is in progress, so\n'
    'this is a compiled candidate awaiting visual acceptance.\n\n'
    'Read `README_GRAPH_SUCCESSOR.md` for source scope and guarded rebuild.\n'
    'Every predecessor file and original new proof remains in the exact source\n'
    'history. The research programme continues; no RH endpoint is asserted.\n',encoding='utf-8')
expected=STAGE/'provenance/ASSEMBLED_SOURCE_EXPECTATIONS.json'
current={'status':'compiled_cumulative_successor_pending_visual_acceptance',
    'pdf':pdf.name,'pdf_sha256':pin,'pdf_bytes':pdf.stat().st_size,'pages':1929,
    'complete_new_body_count':38,'actual_compiled_input_count':279,
    'source_assembly_receipt':{'path':'provenance/GRAPH_SUCCESSOR_SOURCE_ASSEMBLY.json',**row(STAGE/'provenance/GRAPH_SUCCESSOR_SOURCE_ASSEMBLY.json')},
    'source_expectations':{'path':'provenance/ASSEMBLED_SOURCE_EXPECTATIONS.json',**row(expected)},
    'compiled_source_pins':{'path':'provenance/CURRENT_COMPILED_SOURCE_PINS.json',**row(STAGE/'provenance/CURRENT_COMPILED_SOURCE_PINS.json')},
    'build_receipt':{'path':'build/GRAPH_SUCCESSOR_BUILD_RECEIPT.json',**row(STAGE/'build/GRAPH_SUCCESSOR_BUILD_RECEIPT.json')},
    'source_label_transports':{'path':'provenance/GRAPH_LABEL_TRANSPORT.json',**row(STAGE/'provenance/GRAPH_LABEL_TRANSPORT.json')},
    'source_display_transports':{'path':'provenance/ARTICLE_DISPLAY_WIDTH_TRANSPORTS.json',**row(STAGE/'provenance/ARTICLE_DISPLAY_WIDTH_TRANSPORTS.json')},
    'source_state_transport':{'path':'provenance/TOCDEPTH_STATE_TRANSPORT.json',**row(STAGE/'provenance/TOCDEPTH_STATE_TRANSPORT.json')},
    'predecessor_manifest':{'path':'history/cumulative_1624_predecessor/CURRENT_SOURCE_MANIFEST.json',**row(HISTORY/'CURRENT_SOURCE_MANIFEST.json')},
    'build_command':'python scripts/build_graph_successor.py',
    'warning_categories':build['warnings'],'visual_review':'In progress; not yet accepted.',
    'entire_programme_complete':False}
save(STAGE/'CURRENT_SOURCE_MANIFEST.json',current)
ready_path=STAGE/'provenance/SOURCE_BUILD_READINESS.json'
ready=json.loads(ready_path.read_text(encoding='utf-8'))
ready.update({'status':'clean_cumulative_build_complete_pending_visual_acceptance',
    'expected_source_manifest_sha256':sha(expected),
    'current_source_manifest_sha256':sha(STAGE/'CURRENT_SOURCE_MANIFEST.json'),
    'pdf_sha256':pin,'pages':1929,'tex_runs':6,
    'final_candidate_passes':3,'new_pdf_certified':'Compilation and exact input closure only; visual review pending.',
    'actual_fls_verification':'All279 actual inputs exactly match assembled source membership and complete bytes.',
    'visual_acceptance':'In progress.',
    'next_command':'Review newly rendered pages and complete the exact inherited-page transfer.'})
save(ready_path,ready)
for path in SUPPORT.glob('*.py'):
    target=STAGE/'provenance/source_assembly_tools'/path.name; shutil.copy2(path,target)
for path in (SUPPORT/'contract_review').glob('*'):
    if path.is_file() and path.suffix.lower() in ['.md','.json','.py']:
        target=STAGE/'provenance/source_assembly_tools/contract_review'/path.name
        target.parent.mkdir(parents=True,exist_ok=True); shutil.copy2(path,target)
preservation=verify_predecessor()
print(json.dumps({'status':current['status'],'pdf_sha256':pin,'pages':1929,
    'baseline_files_preserved':preservation['count'],
    'baseline_files_changed_current_paths':preservation['preserved_at_historical_path'],
    'current_source_manifest_sha256':sha(STAGE/'CURRENT_SOURCE_MANIFEST.json')}))
