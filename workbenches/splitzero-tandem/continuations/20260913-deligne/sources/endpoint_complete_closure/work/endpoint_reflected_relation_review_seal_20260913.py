"""Seal completed RF source reviews and actual fixture receipts; no math rerun."""
from pathlib import Path
import hashlib
import json
import re

W = Path(__file__).resolve().parent
def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()
def require(value, message):
    if not value:
        raise RuntimeError(message)
def row(name, role):
    p = W / name
    return {'path':name,'sha256':sha(p),'bytes':p.stat().st_size,'role':role}

source_name = 'endpoint_reflected_relation_fibre_product_20260913.tex'
source_pin = '0847a516e883e7814c414f4c1bc26abfc2dd4f8493b0aac384b109888c5dc749'
old_pin = '1acac595a7f89229569b8e28f63981bce4e072c623b39266af038a6b70671d52'
normal_name = 'endpoint_reflected_relation_power_fixtures_normal_20260913.json'
optimized_name = 'endpoint_reflected_relation_power_fixtures_optimized_20260913.json'
checker_name = 'endpoint_reflected_relation_power_fixtures_20260913.py'
normal = json.loads((W/normal_name).read_text(encoding='utf-8'))
optimized = json.loads((W/optimized_name).read_text(encoding='utf-8'))
require(sha(W/source_name)==source_pin,'Source changed')
require(sha(W/'endpoint_reflected_relation_review_input_RF1_26_20260913.tex')==source_pin,'Reviewed new input changed')
require(sha(W/'endpoint_reflected_relation_review_input_RF1_17_20260913.tex')==old_pin,'Reviewed historical input changed')
require(normal['source']['sha256']==source_pin and optimized['source']['sha256']==source_pin,'Wrong execution source')
require(normal['checker']['sha256']==sha(W/checker_name)==optimized['checker']['sha256'],'Wrong execution code')
require(normal['runtime']['optimization']==0 and normal['runtime']['__debug__'] is True,'Normal actual mode incorrect')
require(optimized['runtime']['optimization']==1 and optimized['runtime']['__debug__'] is False,'Optimized actual mode incorrect')
require(normal['passed']==optimized['passed']==189 and normal['failed']==optimized['failed']==0,'Unexpected check counts')
require(normal['fixtures']==optimized['fixtures'] and normal['checks']==optimized['checks'],'Modes disagree on exact fixture outputs')
require(all(c['passed'] for c in normal['checks']),'Nonpassing check')
for name,pin in normal['historical_files_preserved'].items():
    require(sha(W/name)==pin,'Historical file changed: '+name)
require(normal['historical_files_preserved']==optimized['historical_files_preserved'],'Historical preservation scope changed')
for name in ['endpoint_reflected_relation_power_wrong_normal_20260913.json',
             'endpoint_reflected_relation_power_wrong_optimized_20260913.json']:
    require(not (W/name).exists(),'Rejected mode probe wrote an output')
source = (W/source_name).read_text(encoding='utf-8')
require([int(n) for n in re.findall(r'\\tag\{RF\.(\d+)\}',source)]==list(range(1,27)),'Equation tag closure incorrect')
old = (W/'endpoint_reflected_relation_review_input_RF1_17_20260913.tex').read_text(encoding='utf-8')
start = source.index('\\section{Reflected kernel transport and every power of the norm kernel}')
end = source.index('\\section{Provenance and verification scope}')
reconstructed = source[:start]+source[end:]
reconstructed = reconstructed.replace('On the two kernel $\\C[S]$-modules of the quotient maps to $\\A_\\chi$,\nthe comparison map has',
                                      'On the two kernel modules over $\\A_\\chi$, the comparison map has')
require(reconstructed==old,'Source diff contains an unreviewed change')

receipt_name = 'endpoint_reflected_relation_power_execution_receipt_20260913.json'
manifest_name = 'endpoint_reflected_relation_final_manifest_20260913.json'
require(not (W/receipt_name).exists() and not (W/manifest_name).exists(),'A final receipt or manifest already exists')
receipt = {
    'schema':'reflected-relation-actual-executions/v1',
    'path_base':'directory containing this receipt, source, checker and named companions',
    'source':row(source_name,'complete current RF.1--RF.26 source'),
    'checker':row(checker_name,'exact code executed in both new positive modes'),
    'runtime':{'python':normal['runtime']['python'],'sympy':normal['runtime']['sympy']},
    'positive_runs':[
        {'portable_argv_template':['python',checker_name,'0','NEW_NORMAL_OUTPUT.json'],
         'actual_argv_aliased':['<PYTHON>',checker_name,'0',normal_name],
         'actual_mode':0,'actual_debug':True,'exit_code':0,'passed':189,'failed':0,
         'result':row(normal_name,'actual ordinary-mode complete exact result')},
        {'portable_argv_template':['python','-O',checker_name,'1','NEW_OPTIMIZED_OUTPUT.json'],
         'actual_argv_aliased':['<PYTHON>','-O',checker_name,'1',optimized_name],
         'actual_mode':1,'actual_debug':False,'exit_code':0,'passed':189,'failed':0,
         'result':row(optimized_name,'actual optimized-mode complete exact result')},
    ],
    'mode_rejection_probes':[
        {'portable_argv_template':['python',checker_name,'1','NEW_REJECTED_NORMAL_OUTPUT.json'],
         'actual_argv_aliased':['<PYTHON>',checker_name,'1','endpoint_reflected_relation_power_wrong_normal_20260913.json'],
         'actual_mode':0,'incorrect_declared_mode':1,'exit_code':1,
         'reported_error_tail':'RuntimeError: runtime: actual optimization mode','output_created':False},
        {'portable_argv_template':['python','-O',checker_name,'0','NEW_REJECTED_OPTIMIZED_OUTPUT.json'],
         'actual_argv_aliased':['<PYTHON>','-O',checker_name,'0','endpoint_reflected_relation_power_wrong_optimized_20260913.json'],
         'actual_mode':1,'incorrect_declared_mode':0,'exit_code':1,
         'reported_error_tail':'RuntimeError: runtime: actual optimization mode','output_created':False},
    ],
    'mode_probe_evidence_scope':'Actual exit codes and exact final error line are transcribed from both tool executions; full native-path tracebacks are not serialized. The absence of result files is independently checked by this seal script.',
    'actual_argv_alias_definition':'<PYTHON> denotes the actual Python 3.13.9 executable recorded by the results. Absolute file arguments are displayed relative to the work directory containing the checker and outputs; flags, declared modes, and literal output basenames are unchanged. portable_argv_template is a proposed replay invocation, not a literal past invocation.',
    'exact_fixture_and_check_records_identical_between_positive_modes':True,
    'historical_106_run_preserved':normal['historical_files_preserved'],
    'new_check_count_scope':{'total_per_positive_run':189,'runtime_and_provenance_per_positive_run':12,'mathematical_checks_per_positive_run':177},
    'not_run':['Lean','compiler','PDF render','historical 106-check script'],
}
(W/receipt_name).write_text(json.dumps(receipt,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
members = [
    (source_name,'current full mathematical source'),
    ('endpoint_reflected_relation_review_input_RF1_17_20260913.tex','exact historical complete source snapshot'),
    ('endpoint_reflected_relation_review_input_RF1_26_20260913.tex','exact complete source reviewed now'),
    ('endpoint_reflected_relation_revision_20260913.diff','complete reviewed source diff'),
    ('endpoint_reflected_relation_complete_review_20260913.md','unchanged historical complete review'),
    ('endpoint_reflection_independent_typing_review_20260913.md','unchanged historical independent review'),
    ('endpoint_reflected_relation_final_complete_review_20260913.md','new complete final review with full persistent fixture proof'),
    ('endpoint_reflection_independent_typing_review_final_20260913.md','new independent complete RF.1--RF.26 review'),
    ('endpoint_reflected_relation_fixtures_20260913.py','unchanged historical checker, not rerun'),
    ('endpoint_reflected_relation_fixtures_20260913.json','unchanged actual historical 106-pass ordinary-mode result'),
    (checker_name,'new exact semilinear and ideal-power checker'),
    (normal_name,'actual 189-pass ordinary-mode result'),
    (optimized_name,'actual 189-pass optimized-mode result'),
    (receipt_name,'actual positive modes and explicit mode-rejection records'),
    ('endpoint_reflected_relation_fixture_requirements_20260913.txt','portable exact SymPy version requirement'),
    (Path(__file__).name,'read-only-input closure sealer; writes only new receipt and manifest'),
]
manifest = {
    'schema':'reflected-relation-complete-review-closure/v1',
    'path_base':'all file paths relative to the directory containing this manifest',
    'source_sha256':source_pin,'historical_source_sha256':old_pin,
    'equations':list(range(1,27)),'full_source_read':True,'full_source_diff_read':True,
    'unresolved_defects':[],'historical_module_typing_defect_closed':True,
    'files':[row(name,role) for name,role in members],
    'new_checker_required_siblings':[source_name]+list(normal['historical_files_preserved']),
    'dependency_resolution':{'requirement':'sympy==1.14.0','optional_local_vendor_directory':'kernel_layer_replay_dependencies_20260912',
       'portable_behavior':'The checker prepends that sibling directory; if it is absent, normal Python import resolution uses installed SymPy and rejects every version except 1.14.0.'},
    'execution_receipt':receipt_name,
    'portable_run_note':'Run each invocation with an as-yet nonexistent JSON output file directly beside the checker. The checker refuses to overwrite existing evidence. All named source and historical companions must remain exact siblings; no source-path or hash-literal adaptation is required when this layout is retained.',
    'historical_execution_note':'The historical 106-pass result names the RF.1--RF.17 source hash. The old source snapshot is included; the historical checker has not been executed against RF.1--RF.26 or attributed a new execution.',
    'scope_exclusions':['Gamma 478-page source audit mutation','cumulative publication','root proof edits','compiler reruns','PDF visual QA','zero-location claim'],
}
(W/manifest_name).write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps({'manifest':row(manifest_name,'final complete review closure'),'receipt':row(receipt_name,'actual execution receipt'),'review':row('endpoint_reflected_relation_final_complete_review_20260913.md','complete final review'),'file_count':len(members)},indent=2))
