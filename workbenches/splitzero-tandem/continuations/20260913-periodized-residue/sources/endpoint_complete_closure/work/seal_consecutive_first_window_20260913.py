"""Seal already inspected CJ sources, final PDF, and retained execution evidence."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json
W=Path(__file__).resolve().parent.parent
T=W/'work'
def pin(p,role):
    b=p.read_bytes()
    return {'workspace_relative':p.relative_to(W).as_posix(),'role':role,
            'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
source=T/'consecutive_first_window_join_20260913.tex'
pdf=T/'consecutive_first_window_build_20260913/consecutive_first_window_join_20260913.pdf'
execution=T/'consecutive_first_window_closure_execution_20260913.json'
e=json.loads(execution.read_text())
for key,p in [('source',source),('pdf',pdf)]:
    if e[key]['sha256']!=pin(p,key)['sha256']:
        raise RuntimeError('Source/PDF changed after final build/render')
for f in e['rendered_pages']:
    if pin(W/f['workspace_relative'],'image')['sha256']!=f['sha256']:
        raise RuntimeError('Rendered page changed after review')
review=T/'consecutive_first_window_complete_independent_review_20260913.md'
v={'schema':'cj-final-direct-visual-review-v1','utc':datetime.now(timezone.utc).isoformat(),
   'source':pin(source,'full_proof'),'pdf':pin(pdf,'final_six_page_pdf'),
   'pages_inspected':[1,2,3,4,5,6], 'inspection':'Every final 110-dpi page was directly viewed after the final rank-one proof and complete-spectrum edits. No overlap, clipped equation, missing sign, illegible symbol or page-number defect found.',
   'rendered_pages':e['rendered_pages'],'execution':pin(execution,'final_build_render'),
   'complete_mathematical_review':pin(review,'independent_full_review')}
visual=T/'consecutive_first_window_final_visual_20260913.json'
visual.write_text(json.dumps(v,indent=2)+'\n',encoding='utf-8')
files={}
def add(p,role):
    if p.is_file(): files[p.relative_to(W).as_posix()]=pin(p,role)
    else: raise FileNotFoundError(p)
for name in ['consecutive_first_window_join_20260913.tex','check_consecutive_first_window_join_20260913.py',
             'replay_consecutive_first_window_join_20260913.py','close_consecutive_first_window_20260913.py',
             'seal_consecutive_first_window_20260913.py','consecutive_first_window_closure_execution_20260913.json',
             'consecutive_first_window_complete_independent_review_20260913.md','consecutive_first_window_final_visual_20260913.json',
             'consecutive_first_window_checks_normal_v2_20260913.json',
             'endpoint_first_window_conclusion_addition_20260913.tex','endpoint_first_window_crosswalk_addition_20260913.md']:
    add(T/name,'current_cj_proof_check_review_integration')
for name in ['consecutive_first_window_checks_normal_20260913.json','check_consecutive_first_window_join_development_20260913.py']:
    add(T/name,'preserved_failed_development_evidence')
for folder,role in [('consecutive_first_window_replay_20260913','seven_retained_processes_and_raw_logs'),
                    ('consecutive_first_window_final_visual_20260913','final_build_render_and_all_viewed_pages'),
                    ('pr25_relation_dependencies_20260913','exact_collected_pr25_source_owner_review_and_proposal')]:
    for p in sorted((T/folder).rglob('*')):
        if p.is_file():add(p,role)
for name in ['consecutive_first_window_join_20260913.pdf','consecutive_first_window_join_20260913.log']:
    add(T/'consecutive_first_window_build_20260913'/name,'final_compiled_pdf_and_log')
for rel in ['output/split_zero_rh_tandem_2026-09-12/tex/cyclic_control_determinant_increments.tex',
            'output/split_zero_rh_tandem_2026-09-12/tex/toda_cv_exact_bridge.tex',
            'work/arithmetic_volume_upper_route_20260913.tex','work/endpoint_product_sharpening_20260913.tex']:
    add(W/rel,'complete_inherited_mathematical_dependency')
manifest={'schema':'consecutive-first-window-final-v1','utc':datetime.now(timezone.utc).isoformat(),
 'status':'complete_local_full_CJ_proof_review_pdf_and_retained_evidence',
 'proof_labels':'CJ.1-CJ.22','pdf_pages':6,'complete_current_source_read':True,
 'new_mathematical_check_executions':0,'existing_positive_checks_each_mode':378,
 'existing_negative_cases_each_mode':3,'recorded_execution_results':8,
 'seven_job_replay_contains_exact_argv_returncodes_and_raw_logs':True,
 'ordinary_positive_provenance':'Separately retained root ordinary-mode result; original tool invocation was completed before the seven-job replay. The replay does not attribute its own argv/log to this earlier run.',
 'historical_development_failure_preserved':True,'new_lean':False,'global_tex_modified':False,'remote_publication':False,
 'portable_jobs':[{'script':'work/check_consecutive_first_window_join_20260913.py',
  'modes':['normal','optimized'],'runtime':'Python with SymPy 1.13.1',
  'positive_args':['--mutation','none','--output','{output}/cj-positive.json'],
  'expected_checks':378,'expected_positive_exit':0,
  'negative_cases':[['--mutation',m,'--output','{output}/cj-'+m+'.json'] for m in ['omit_phase','terminal_square','interior_single']],
  'negative_expected_exit':1}],
 'required_existing_closures':['Full CV/TVB cumulative chapters','arithmetic_volume_upper_manifest_20260913.json','arithmetic_endpoint_intake_manifest_20260913.json','endpoint_product_manifest_20260913.json'],
 'file_count':len(files),'files':[files[k] for k in sorted(files)]}
out=T/'consecutive_first_window_final_manifest_20260913.json'
out.write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'manifest':pin(out,'manifest'),'source':pin(source,'source'),'pdf':pin(pdf,'pdf'),'file_count':len(files)},indent=2))
