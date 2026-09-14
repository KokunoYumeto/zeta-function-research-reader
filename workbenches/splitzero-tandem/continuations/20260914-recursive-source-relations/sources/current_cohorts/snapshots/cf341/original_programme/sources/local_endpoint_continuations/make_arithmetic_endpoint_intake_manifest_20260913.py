"""Build the final byte manifest from reviewed arithmetic intake files."""
from pathlib import Path
import hashlib, json

WORK=Path(__file__).resolve().parent
W=WORK.parent
R=W/'output'/'split_zero_rh_tandem_2026-09-12'
RAW=R/'sources'/'web_arithmetic_endpoint_delivery'/'Tau_Arithmetic_Endpoint_Bounds'

def entry(path, role):
    data=path.read_bytes()
    return {'workspace_relative':path.relative_to(W).as_posix(),'role':role,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}

files=[]
for p in sorted(RAW.rglob('*')):
    if p.is_file(): files.append(entry(p,'original_source_byte_exact'))
for name,role in [
    ('arithmetic_endpoint_intake_20260913.md','complete_derivation_and_intake_audit'),
    ('arithmetic_endpoint_analytic_independent_review_20260913.md','independent_complete_analytic_review'),
    ('arithmetic_endpoint_leading_line_transport_20260913.tex','complete_typed_correction_proof_AL1_AL11'),
    ('arithmetic_endpoint_leading_line_review_20260913.md','independent_complete_typed_correction_review'),
    ('arithmetic_endpoint_raw_intake_manifest_20260913.json','raw_extraction_receipt'),
    ('replay_arithmetic_endpoint_intake_20260913.py','native_replay_and_byte_audit_helper'),
    ('endpoint_criterion_pr23_c720f405_20260913.md','immutable_upstream_endpoint_source'),
    ('pr24_confluent_transfer_dfcbba5_20260913.md','immutable_upstream_confluent_source'),
    ('make_arithmetic_endpoint_intake_manifest_20260913.py','manifest_builder')
]: files.append(entry(WORK/name,role))
for p in sorted((WORK/'arithmetic_endpoint_intake_replay_20260913').iterdir()):
    if p.is_file(): files.append(entry(p,'fresh_finite_replay_or_math_annotation_audit'))
files.append(entry(R/'logbook'/'ARITHMETIC_ENDPOINT_USER_SOURCE_2_20260913.txt','complete_second_user_paste'))
raw=json.loads((WORK/'arithmetic_endpoint_raw_intake_manifest_20260913.json').read_text())
receipt=json.loads((WORK/'arithmetic_endpoint_intake_replay_20260913'/'REPLAY.json').read_text())
payload={
 'schema':'arithmetic-endpoint-intake-final-v1',
 'archive':{'name':raw['archive_name'],'bytes':raw['archive_bytes'],'sha256':raw['archive_sha256'],'members':raw['member_count']},
 'findings':{
  'original_analytic_dyadic_norm_theorem_verified_by_full_written_proofs':True,
  'literal_source_equation_36_constant_64_valid':True,
  'domain':'fixed finite h; integers n>=k>=3; fixed real 0<b<pi/2',
  'required_source_typing_correction':'The graded multiplication isomorphism after (13) has n>=q; the exact sequence itself admits n=q-1, with zero relation source.',
  'correction_proof_labels':'AL.1-AL.11',
  'confluent_presentation_domain':'Doubled orders at original nodes require reflection-stable chi (includes exact quartet); general chi uses all roots of conjugate(psi)*psi with coincident orders added.',
  'new_finite_methods_per_mode':18,
  'normal_and_optimized_pass':True,
  'normal_and_optimized_payloads_identical':True,
  'guard_failure_controls':2,
  'guard_control_test_methods_executed':0,
  'mathematical_mutants_executed':0,
  'manifest_entries_verified':receipt['raw_manifest_entries_verified'],
  'inherited_gamma_entries_verified':receipt['inherited_gamma_entries_verified'],
  'inherited_gamma_test_replayed_in_this_intake':False,
  'patch_files_byte_verified':receipt['patch_added_files'],
  'markdown_body_math_nodes':225,'html_total_math_nodes':226,'toc_duplicate':'g/h','numbered_displays':48,
  'all_original_html_body_math_annotations_equal':True,
  'numerical_enclosure_of_analytic_constants':False,
  'new_lean_run':False,
  'fresh_pdf_compile_or_render':False,
  'raw_sources_changed':False,
  'current_gamma_reader_changed':False,
  'remote_changes':False,
  'second_user_paste_complete':True,
  'first_user_paste_owner':'root and endpoint_product_sharpening',
  'following_balanced_window_or_product_theorems_owner':'parallel owner and endpoint_product_sharpening; excluded from this source proof claim'
 },
 'portable_checker':{'relative_to_raw_package':'check_endpoint_bounds.py','dependency':'sympy','companions':[],'positive_modes':[[],['-O']],'negative_arguments':['--fail-control'],'success_methods':18,'guard_negative_exits':1,'stdout_json':True},
 'publication_note':'Fresh fail-control stderr includes native traceback locations; any public alias rendering must retain original and public hashes separately. Original mathematical sources and checker bytes remain exact.',
 'file_count':len(files),'files':files
}
out=WORK/'arithmetic_endpoint_intake_manifest_20260913.json'
out.write_text(json.dumps(payload,indent=2)+'\n',encoding='utf-8')
print(out,len(files),hashlib.sha256(out.read_bytes()).hexdigest())
