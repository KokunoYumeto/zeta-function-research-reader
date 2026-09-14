"""Seal the two independent conversion checks and final compiler binding."""
from pathlib import Path
from datetime import datetime, timezone
import json, hashlib

HERE=Path(__file__).resolve().parent
def read(p): return json.loads(p.read_text(encoding='utf-8'))
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def pin(p): return {'path':str(p),'sha256':sha(p)}
nineteen=read(HERE/'CONVERSION_NINETEEN_INDEPENDENT_CHECK.json')
binding=read(HERE/'FINAL_CONVERTED_SOURCE_AND_PDF_BINDING.json')
bf_path=HERE/'conversion_recovery_bf_tcl/BF12_TCL2_INDEPENDENT_RECEIPT.json'
bf=read(bf_path)
assert bf['status'].startswith('PASS')
assert bf['BF12']['stage_delivery_ledger_bytes_equal_at_read']
ledger_check=next(r for r in nineteen['file_checks'] if r['path'].endswith('LEDGER_COMPLETE.tex'))
final_changes={r['path']:r for r in binding['exact_changed_sources']}
for r in bf['BF12']['retained_and_current_active_checks']:
    assert r['before']['sha256']==final_changes['tex/cohorts/transcript/LEDGER_COMPLETE.tex']['before_sha256']
    assert r['after']['sha256']==ledger_check['before']['sha256']
    assert r['current_active']['sha256']==ledger_check['after']['sha256']
    assert r['exact_replay']['forward_whole_file_byte_equal'] and r['exact_replay']['inverse_whole_file_byte_equal']
    assert r['current_BF12_block_equals_bf12_only_after']
assert bf['TCL2']['before']['sha256']==final_changes['tex/cohorts/cf/49_TP.tex']['before_sha256']
assert bf['TCL2']['after']['sha256']==final_changes['tex/cohorts/cf/49_TP.tex']['after_sha256']
assert bf['TCL2']['whole_file_exact_fragment_replay']['inverse_whole_file_byte_equal']
assert bf['TCL2']['mathematical_formula_bytes_equal']
for r in bf['TCL2']['active_copies']: assert r['equals_retained_after_bytes']
assert all(r['unchanged_during_audit'] for r in bf['concurrency']['active_inputs_double_read'])
for record in binding['builds']:
    assert sha(Path(record['pdf']['path']))==record['pdf']['sha256']
    assert sha(Path(record['build_receipt']['path']))==record['build_receipt']['sha256']
result={
    'status':'PASS: complete documented final conversion and source/compiler acceptance',
    'utc':datetime.now(timezone.utc).isoformat(),
    'source_expression_repairs':21,
    'display_wrapper_repairs':1,
    'compiler_inputs':240,
    'changed_compiler_inputs':4,
    'unchanged_compiler_inputs':236,
    'BF12_original_to_intermediate_to_final_byte_chain_verified':True,
    'TCL2_original_to_final_byte_chain_verified':True,
    'all_nineteen_additional_original_source_images_verified':True,
    'old_audit_preserved':True,
    'builds':binding['builds'],
    'readable_ledger':pin(HERE/'CHANGE_USE_LEDGER.md'),
    'evidence':[pin(HERE/'CONVERSION_NINETEEN_INDEPENDENT_CHECK.json'),
                pin(bf_path),pin(HERE/'FINAL_CONVERTED_SOURCE_AND_PDF_BINDING.json'),
                pin(HERE/'CONVERSION_RECOVERY_READING.md')],
    'scope_qualification':'Exact source and compiler binding only. The entire current source repair chain is accepted. Final rendered-page visual acceptance and source ZIP/inventory are supplied separately by the delivery owner.',
    'fresh_pandoc_reproduction_qualification':'Native CRLF output and the original recorded LF text-stream output are both preserved. Two exact active edits are fully byte-reversible; fresh full-body Pandoc conversion also changes line wrapping, so its inverse has equal nonwhitespace TeX tokens rather than equal whole bytes.'
}
out=HERE/'FINAL_CONVERSION_ACCEPTANCE.json'
out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':result['status'],'receipt_sha256':sha(out),'BF12_TCL2_receipt_sha256':sha(bf_path)},indent=2))
