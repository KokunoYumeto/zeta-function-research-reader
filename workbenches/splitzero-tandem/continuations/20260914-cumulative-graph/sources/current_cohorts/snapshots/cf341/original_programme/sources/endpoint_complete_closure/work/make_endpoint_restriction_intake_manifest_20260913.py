"""Seal the new restriction intake and describe six portable finite jobs."""
from pathlib import Path
import hashlib,json

WORK=Path(__file__).resolve().parent;W=WORK.parent
R=W/'output'/'split_zero_rh_tandem_2026-09-12'
RAW=R/'sources/web_endpoint_restriction_delivery/Tau_Endpoint_Restriction_Control'
REPLAY=WORK/'endpoint_restriction_replay_20260913'
LOCAL='sources/local_endpoint_restriction_continuations/'
def h(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def entry(p,role):
    dest=p.relative_to(R).as_posix() if p.is_relative_to(R) else LOCAL+p.relative_to(WORK).as_posix()
    return {'workspace_relative':p.relative_to(W).as_posix(),'suggested_reader_destination':dest,'role':role,'bytes':p.stat().st_size,'sha256':h(p)}

def main():
    rawscript=RAW/'check_restriction_control.py';supp=WORK/'endpoint_restriction_calibration_check_20260913.py';jobs=[]
    for opt in [False,True]:
        mode='optimized' if opt else 'normal'
        jobs.append({'label':'restriction-original-'+mode,'script':rawscript.relative_to(R).as_posix(),'script_sha256':h(rawscript),'optimized':opt,'args':['--json','{output}'],'expected_exit_code':0,'output_kind':'json-option','runtime_profile':'sympy-1.14.0','companion_files':[],'expected_fields':{'tests_run':19,'failures':0,'errors':0,'passed':True},'retained_result':{'path':LOCAL+'endpoint_restriction_replay_20260913/'+mode+'.json','sha256':h(REPLAY/(mode+'.json'))},'scope':'19 original finite Gaussian polynomial/matrix methods; no arithmetic integration certificate','normal_optimized_equality_ignore_fields':[]})
        jobs.append({'label':'restriction-startup-'+mode,'script':rawscript.relative_to(R).as_posix(),'script_sha256':h(rawscript),'optimized':opt,'args':['--inject-failure'],'expected_exit_code':1,'output_kind':'absent','stderr_contains':'intentional negative control','runtime_profile':'sympy-1.14.0','companion_files':[],'scope':'Explicit false startup guard; zero test methods and zero formula mutants','test_methods_executed':0,'normal_optimized_equality_ignore_fields':[]})
        jobs.append({'label':'restriction-calibration-'+mode,'script':LOCAL+supp.name,'script_sha256':h(supp),'optimized':opt,'args':['--source-checker',rawscript.relative_to(R).as_posix(),'--json','{output}'],'expected_exit_code':0,'output_kind':'json-option','runtime_profile':'sympy-1.14.0','companion_files':[rawscript.relative_to(R).as_posix()],'expected_fields':{'status':'PASS','strict_threshold_verified':True,'strict_improvement_verified':True},'retained_result':{'path':LOCAL+'endpoint_restriction_replay_20260913/calibration-'+mode+'.json','sha256':h(REPLAY/('calibration-'+mode+'.json'))},'scope':'Independent exact rational calibration enclosure; literal mass7, four actual kernels, nilpotent action, two spectra, six trace moments and strict decimal upper bound','working_directory':'reader-root','normal_optimized_equality_ignore_fields':[]})
    jp=WORK/'endpoint_restriction_portable_jobs_20260913.json';jp.write_text(json.dumps({'schema':'endpoint-restriction-portable-jobs-v1','jobs':jobs,'job_count':6,'all_jobs_executed_locally':True,'fresh_payload_comparison':'Within each lane normal/-O bytes equal; against delivered historical JSON compare parsed payload because explicit CRLF/LF byte map differs.'},indent=2)+'\n',encoding='utf-8')
    files=[entry(p,'original_source_byte_exact') for p in sorted(RAW.rglob('*')) if p.is_file()]
    for name,role in [
      ('endpoint_restriction_intake_20260913.md','complete_standalone_source_and_proof_audit'),
      ('endpoint_restriction_independent_review_20260913.md','independent_complete_mathematical_review'),
      ('endpoint_restriction_gaussian_independent_20260913.md','independent_complete_gaussian_derivation_appended_in_review'),
      ('endpoint_restriction_raw_intake_20260913.json','raw_byte_extraction_manifest'),
      ('endpoint_restriction_calibration_check_20260913.py','exact_rational_calibration_supplement'),
      ('replay_endpoint_restriction_intake_20260913.py','native_sequential_replay_helper'),
      ('endpoint_restriction_portable_jobs_20260913.json','portable_jobs'),
      ('endpoint_restriction_json_equality_correction_20260913.md','pinned_arithmetic_equality_wording_correction'),
      ('endpoint_restriction_json_equality_correction_20260913.json','exact_byte_and_payload_correction_evidence'),
      ('make_endpoint_restriction_intake_manifest_20260913.py','manifest_builder')
    ]:files.append(entry(WORK/name,role))
    files.extend(entry(p,'fresh_exact_replay_result_or_log') for p in sorted(REPLAY.iterdir()) if p.is_file())
    # The mathematical user paste is retained by root in the reader logbook.
    files.append(entry(R/'logbook/USER_RESTRICTION_PROOF_20260913.txt','complete_mathematical_user_paste'))
    files.append(entry(R/'logbook/ENDPOINT_RESTRICTION_USER_DELIVERY_20260913.json','root_full_user_delivery_provenance'))
    report={'schema':'endpoint-restriction-intake-final-v1','archive_name':'Tau_Endpoint_Restriction_Control_2026-09-13.zip','archive_bytes':691968,'archive_sha256':'619056abe8d8881da57604822d5ba5821795e1ed80db5d6a44910435d4def20e','raw_members':32,'raw_manifest_entries':31,'patch_additions_byte_verified':15,'inherited_arithmetic_entries_byte_verified':31,'inherited_arithmetic_tests_executed_this_intake':False,'original_method_count_per_successful_mode':19,'startup_guard_executions':2,'startup_guard_methods':0,'formula_mutants':0,'supplemental_exact_calibration_modes':2,'portable_job_count':6,'markdown_math_nodes':253,'html_math_nodes':253,'all_body_math_annotations_identical':True,'numbered_equations':65,'complete_raw_tex_lines':962,'full_mathematical_audit':True,'numerical_arithmetic_zeta_certificate':False,'new_lean_run':False,'fresh_pdf_or_browser_render':False,'original_bytes_changed':False,'current_gamma_cut_changed':False,'remote_changes':False,'typed_expansions':['padding/truncation/endomorphism projection types','both quotient metrics and source-image singular-value maps','full commutator with arithmetic action','unscaled alternating tensor map with literal q!','rectangular exterior map evaluated on its source top wedge','g0=1 zero branch separate from divided scalar formula','rounded decimal values distinguished from exact rational upper endpoints'],'prior_pinned_audit_and_manifest_preserved':True,'json_equality_correction':'separate supplemental files preserve the exact old claim and prove actual CRLF/LF/parsed relationships','file_count':len(files),'files':files}
    out=WORK/'endpoint_restriction_intake_manifest_20260913.json';out.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8');print(out,len(files),h(out))

if __name__=='__main__':main()
