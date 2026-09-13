"""Seal OW.1--40 proof, actual visual review, original jobs and portable dependencies."""
from pathlib import Path
import datetime, hashlib, json, shutil, subprocess, sys

W=Path(__file__).resolve().parent
ROOT=W.parent
BUILD=W/'au_weight_optimizer_final_build_20260913'
HISTORY=W/'au_weight_optimizer_execution_history_20260913'
def now(): return datetime.datetime.now(datetime.timezone.utc).isoformat()
def pin(p,role=None):
    data=p.read_bytes()
    result={'workspace_relative':p.relative_to(ROOT).as_posix(),
            'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}
    if role: result['role']=role
    return result
def write(p,data): p.write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
source=W/'au_weight_optimizer_20260913.tex'
if pin(source)['sha256']!='677482a95ecbeafecf26f898f7426fb74ba31a5375cbe8862551e2c1a78e0952':
    raise RuntimeError('Reviewed source changed')
review=W/'au_weight_optimizer_ow40_independent_review_20260913.md'
if pin(source)['sha256'] not in review.read_text(encoding='utf-8'):
    raise RuntimeError('Extension review does not bind the source')
build=json.loads((BUILD/'BUILD.json').read_text(encoding='utf-8'))
if build['pages']!=12 or build['layout_log_issues'] or build['missing_labels']:
    raise RuntimeError('Final build metadata has unresolved issues')
pdf=BUILD/'au_weight_optimizer_20260913.pdf'
if pin(pdf)['sha256']!=build['pdf']['sha256']: raise RuntimeError('PDF changed')
images=sorted(BUILD.glob('page-*.png'))
if len(images)!=12: raise RuntimeError('Need all twelve actual images')
visual={'schema':'au-weight-optimizer-all-page-visual-v1','reviewed_utc':now(),
 'source':pin(source),'pdf':pin(pdf),'pages':12,
 'actual_view_method':'All twelve individual 110 dpi PNG pages were viewed with view_image, in three groups: 1-4, 5-8, 9-12.',
 'pages_viewed':list(range(1,13)),
 'findings':'Every equation and tag remains within the text area; no clipping, overlap, missing glyphs, unreadable text or orphan section title. Section transitions and page numbers were checked on the actual final images.',
 'compiler_issues':[],'images':[pin(p) for p in images],
 'historical_images':'The older nine page images in au_weight_optimizer_build_20260913 were left untouched and are not evidence for the current twelve-page PDF.'}
write(W/'au_weight_optimizer_final_visual_20260913.json',visual)

# This probe records the environment now; it is explicitly not a historical assertion or checker replay.
probe_code='import sys,sympy,json;print(json.dumps({"python":sys.version,"executable":sys.executable,"optimize":sys.flags.optimize,"debug":__debug__,"sympy":sympy.__version__}))'
argv=[sys.executable,'-c',probe_code]
started=now(); probe=subprocess.run(argv,capture_output=True)
(HISTORY/'current-runtime.stdout').write_bytes(probe.stdout)
(HISTORY/'current-runtime.stderr').write_bytes(probe.stderr)
if probe.returncode: raise RuntimeError('Runtime metadata probe failed')
runtime={'schema':'au-optimizer-current-runtime-probe-v1','started':started,'finished':now(),
         'argv':argv,'exit_code':probe.returncode,'stdout':pin(HISTORY/'current-runtime.stdout'),
         'stderr':pin(HISTORY/'current-runtime.stderr'),
         'observed':json.loads(probe.stdout),
         'scope':'Current read-only version probe. The original historical commands record their interpreter path and optimization flag but did not emit dependency-version strings. No mathematical checks were rerun.'}
write(HISTORY/'CURRENT_RUNTIME.json',runtime)

execution=json.loads((HISTORY/'EXECUTION.json').read_text(encoding='utf-8'))
if len(execution['events'])!=20 or len(execution['current_results'])!=12:
    raise RuntimeError('Unexpected recovered execution count')
jobs=[]
for result in execution['current_results']:
    result_path=Path(result['result']['path'])
    payload=json.loads(result_path.read_text(encoding='utf-8'))
    if result['check_count']!=207 or not result['matching_actual_events']:
        raise RuntimeError('Result does not bind its current actual execution')
    args=['check_au_weight_optimizer_20260913.py']
    if payload['fault']: args+=['--fault',payload['fault']]
    args+=['--output','{output}/'+result_path.name]
    jobs.append({'id':result_path.stem,'mode':'optimized' if payload['optimized'] else 'normal',
      'python_flags':['-O'] if payload['optimized'] else [],'args':args,
      'cwd':'{source_group}','expected_exit_code':1 if payload['fault'] else 0,
      'expected_status':payload['status'],'expected_check_count':207,
      'expected_fault':payload['fault'],'expected_failures':payload['failures'],
      'expected_optimized':payload['optimized'],'retained_result':pin(result_path),
      'original_completed_events':[pin(Path(p)) for p in result['matching_actual_events']]})
portable={'schema':'au-optimizer-portable-job-spec-v1',
 'status':'Dispatch specification; original completed executions are separately retained. This spec was not executed during finalization.',
 'source_group_files':[pin(W/'check_au_weight_optimizer_20260913.py'),pin(W/'au_weight_optimizer_20260913.py')],
 'runtime_profile':{'python':'3.13','dependency':'sympy==1.13.1','basis':'Current concrete interpreter probe; use the literal dependency profile for future portable replay.'},
 'execution':'Run jobs sequentially in a temporary isolated source group with both files adjacent. Preserve raw stdout/stderr, actual argv, interpreter versions, exits and result JSON. Check exact failure names as well as return codes; use explicit predicates rather than removable assert statements.',
 'jobs':jobs,'job_count':12,'mode_pairs':6,
 'finite_scope':json.loads((W/'au_weight_optimizer_checks_normal_20260913.json').read_text(encoding='utf-8'))['scope']}
write(W/'au_weight_optimizer_portable_dependencies_20260913.json',portable)

log=W/'au_weight_optimizer_logbook_20260913.md'
old=HISTORY/'lane_log_before_finalization.md'
if not old.exists(): shutil.copyfile(log,old)
addition='''

## OW.40 finalization — 13 September 2026

The complete current source OW.1–40 and OW.22a was read again, together with both preceding full mathematical reviews and the newly independent OW.30–40/R48 derivation. No mathematical correction was needed. The current primary TeX is SHA-256 677482a95ecbeafecf26f898f7426fb74ba31a5375cbe8862551e2c1a78e0952. Its complete proofs preserve the original source mass, source chart, raw derivatives, signed minors, all q+1 moment factors and every zero coefficient.

The earlier less-than-one gain concerns precisely the old separate-moment family. The source now also proves H_q <= S_q diag(beta_j^-1) < (M_k/2) diag(beta_j^-1), with the literal finite sum S_q=sum beta_j mu_(2j). The full stronger diagonal family H_q <= (sum r_j mu_(2j)) diag(r_j^-1) is optimized by the exact bijection t_j=r_j mu_(2j)/sum r_l mu_(2l). Its cofactor polynomial has kappa_j=|psi_j|^2 mu_(2j), and its bound is U_mom=sum_(j=0)^q log mu_(2j)-log d(kappa)-log V_(2q-1)^nu. OW.39 preserves every term of the exact gain, including q log(2(q+1)); its q log k ratio is 2 for fixed multiplicity one and 3 for fixed multiplicity greater than one. OW.40 proves the complete original-kernel comparison loss by the quotient-first Schur complement V_q=det H_q/(psi* H_q psi). These are full proofs in the source and new independent review, with no additional arithmetic asymptotic assumed.

R48 was read completely and agrees with these exact formulas. No global or frozen publication file was edited. A separate final PDF build retained the earlier twelve-page PDF and its mismatched older nine-page image history without changing any bytes there. The new twelve-page PDF was compiled twice, rendered at 110 dpi, and all twelve individual pages were actually viewed. The build has no TeX warning, overfull/underfull box, missing equation label, or visual defect.

No mathematical checker was rerun during finalization. Twenty original completed command events were recovered from their exact session records: eight historical jobs at 153 checks and twelve current jobs at 207 checks. Each current result matches its original completed execution, including flags, failure list and concrete interpreter path. Both current positive jobs pass all 207 checks. In each mode, the minor-sign control rejects eight identities, factorial two, stationarity-sign twenty-two, cosh-factor two and omitted-zero-moment product two. All event records, raw emitted output and existing result JSON files are retained. A current version probe records Python/SymPy now and is not claimed to retroactively establish versions omitted from the original event.

The final manifest and portable dependency specification distinguish the twelve current jobs from the eight historical jobs and retain the sealed AU dependency closure. No Lean was run and no arithmetic-source asymptotic was inferred from the explicit finite density fixtures.
'''
if '## OW.40 finalization — 13 September 2026' not in log.read_text(encoding='utf-8'):
    with log.open('a',encoding='utf-8',newline='') as stream: stream.write(addition)

review_record={'schema':'au-optimizer-final-source-review-v1','reviewed_utc':now(),
 'source':pin(source),'source_fully_read':True,
 'scope':['OW.1-40','OW.22a','complete prior optimizer and maps reviews','independent OW.30-40 extension review','complete R48'],
 'mathematical_corrections':[],
 'result':'All current claims follow from their full written proofs and declared sealed AU source inequality. Boundary cases, phases, q+1 moment factors, full mixed-moment Schur complement and asymptotic scope were verified.',
 'reviews':[pin(W/'au_weight_optimizer_complete_independent_review_20260913.md'),
            pin(W/'au_weight_optimizer_independent_maps_review_20260913.md'),pin(review)],
 'R48':pin(W/'endpoint_weight_conclusion_addition_20260913.tex'),
 'finite_checks_scope':'Recovered existing completed event evidence; no repeat mathematical run.'}
write(W/'au_weight_optimizer_final_source_review_20260913.json',review_record)

roles={}
def add(p,role):
    if not p.exists(): raise FileNotFoundError(p)
    roles[p]=role
for name in ['au_weight_optimizer_20260913.tex','au_weight_optimizer_20260913.py','check_au_weight_optimizer_20260913.py',
             'au_weight_optimizer_complete_independent_review_20260913.md','au_weight_optimizer_independent_maps_review_20260913.md',
             'au_weight_optimizer_ow40_independent_review_20260913.md','au_weight_optimizer_logbook_20260913.md',
             'au_weight_optimizer_final_source_review_20260913.json','au_weight_optimizer_final_visual_20260913.json',
             'au_weight_optimizer_portable_dependencies_20260913.json','endpoint_weight_conclusion_addition_20260913.tex',
             'endpoint_weight_crosswalk_addition_20260913.md','build_au_weight_optimizer_final_20260913.py',
             'collect_au_weight_optimizer_execution_20260913.py','finalize_au_weight_optimizer_20260913.py']:
    add(W/name,'current optimizer proof, review and integration evidence')
for p in W.glob('au_weight_optimizer_checks_*_20260913.json'): add(p,'original current 207-check result')
for p in BUILD.iterdir():
    if p.is_file(): add(p,'final exact-source build and all-page render')
for p in HISTORY.iterdir():
    if p.is_file(): add(p,'retained original execution history and separately dated metadata probe')
for p in (W/'au_weight_optimizer_build_20260913').iterdir():
    if p.is_file(): add(p,'unchanged earlier build and image history; not current visual evidence')
au=W/'arithmetic_volume_upper_manifest_20260913.json'
add(au,'sealed AU dependency manifest')
for item in json.loads(au.read_text(encoding='utf-8'))['files']:
    p=W/item['path']; actual=pin(p)
    if actual['sha256']!=item['sha256'] or actual['bytes']!=item['bytes']:
        raise RuntimeError('Sealed AU dependency does not match '+item['path'])
    add(p,'sealed AU original analytic dependency closure; not replayed')
manifest={'schema':'au-weight-optimizer-final-package-v1','status':'complete-local-result',
 'created_utc':now(),'proof_labels':['OW.1-40','OW.22a'],'source':pin(source),'pdf':pin(pdf),
 'pdf_pages':12,'primary_source_unchanged':True,'new_lean':False,
 'mathematical_status':'Complete optimum of both declared diagonal source families, exact arithmetic volume consequences and complete finite loss against the original low-degree kernel. No unproved arithmetic asymptotic or RH conclusion asserted.',
 'current_actual_jobs':12,'current_mode_pairs':6,'current_positive_checks_each_mode':207,
 'historical_actual_jobs':8,'historical_positive_checks_each_mode':153,
 'checks_rerun_during_finalization':False,
 'execution_receipt':pin(HISTORY/'EXECUTION.json'),
 'runtime_scope':runtime['scope'],'portable_dependencies':pin(W/'au_weight_optimizer_portable_dependencies_20260913.json'),
 'source_review':pin(W/'au_weight_optimizer_final_source_review_20260913.json'),
 'visual_review':pin(W/'au_weight_optimizer_final_visual_20260913.json'),
 'declared_analytic_dependency':pin(au),
 'file_count':len(roles),'files':[pin(p,role) for p,role in sorted(roles.items(),key=lambda kv:str(kv[0]))]}
target=W/'au_weight_optimizer_final_manifest_20260913.json'
write(target,manifest)
print(json.dumps({'manifest':pin(target),'files':len(roles),'source':manifest['source'],'pdf':manifest['pdf'],
                  'review':pin(review),'runtime_current':runtime['observed']}))
