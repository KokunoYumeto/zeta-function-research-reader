from pathlib import Path
import subprocess,sys,json,hashlib,datetime
W=Path(__file__).resolve().parent
SRC=W.parent/'output/split_zero_rh_tandem_2026-09-12/sources/web_relation_moment_delivery/Tau_Relation_Moment_Control'
OUT=W/'relation_moment_comparison_build_20260913';OUT.mkdir(exist_ok=True)
sha=lambda b:hashlib.sha256(b).hexdigest()
jobs=[]
for mode,opt in [('normal',[]),('optimized',['-O'])]:
 for case,extra,expected in [('positive',['--json',str(W/('relation_moment_comparison_'+mode+'_20260913.json'))],0),('action-order',['--negative-control','action-order'],1),('rank-transfer',['--negative-control','rank-transfer'],1)]:
  argv=[sys.executable,'-B',*opt,str(W/'check_relation_moment_comparison_20260913.py'),'--source-checker',str(SRC/'check_relation_moments.py'),*extra]
  p=subprocess.run(argv,capture_output=True)
  stem='check-'+mode+'-'+case
  for stream,b in [('stdout',p.stdout),('stderr',p.stderr)]: (OUT/(stem+'.'+stream+'.log')).write_bytes(b)
  jobs.append({'mode':mode,'case':case,'argv':argv,'exit_code':p.returncode,'expected_exit_code':expected,'stdout_sha256':sha(p.stdout),'stderr_sha256':sha(p.stderr)})
  if p.returncode!=expected:raise RuntimeError(jobs[-1])
  print(stem+' passed',flush=True)
positive=[json.loads((W/('relation_moment_comparison_'+mode+'_20260913.json')).read_text()) for mode in ['normal','optimized']]
for d in positive:
 if not d['passed'] or d['methods']!=10:raise RuntimeError('positive scope mismatch')
for key in ['passed','methods','names','failures','errors','source_checker_sha256','scope']:
 if positive[0][key]!=positive[1][key]:raise RuntimeError('payload mismatch '+key)
if positive[0]['optimization']!=0 or positive[1]['optimization']!=1 or not positive[0]['debug'] or positive[1]['debug']:raise RuntimeError('runtime modes')
build=[]
for n in range(2):
 argv=['pdflatex','-interaction=nonstopmode','-halt-on-error','-output-directory',str(OUT),str(W/'relation_moment_comparison_proof_20260913.tex')]
 p=subprocess.run(argv,capture_output=True)
 for stream,b in [('stdout',p.stdout),('stderr',p.stderr)]: (OUT/(f'build-final-{n+1}.'+stream+'.log')).write_bytes(b)
 build.append({'argv':argv,'exit_code':p.returncode,'stdout_sha256':sha(p.stdout),'stderr_sha256':sha(p.stderr)})
 if p.returncode:raise RuntimeError('tex build')
log=(OUT/'relation_moment_comparison_proof_20260913.log').read_text(errors='replace')
bad=[x for x in log.splitlines() if any(v in x for v in ['Overfull','Underfull','Missing character','undefined','LaTeX Warning','pdfTeX warning'])]
if bad:raise RuntimeError(bad)
qa=OUT/'qa';qa.mkdir(exist_ok=True)
argv=['pdftoppm','-r','100','-png',str(OUT/'relation_moment_comparison_proof_20260913.pdf'),str(qa/'page')]
p=subprocess.run(argv,capture_output=True)
(OUT/'render.stdout.log').write_bytes(p.stdout);(OUT/'render.stderr.log').write_bytes(p.stderr)
if p.returncode:raise RuntimeError('render')
receipt={'schema':'relation-moment-supplement-execution-v1','completed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'jobs':jobs,'methods_each_mode':10,'normal_optimized_mathematical_payload_equal':True,'normal_optimization':0,'optimized_optimization':1,'mutants_each_mode':2,'build':build,'render_argv':argv,'render_exit_code':p.returncode,'tex_warnings':bad,'tex_sha256':sha((W/'relation_moment_comparison_proof_20260913.tex').read_bytes()),'pdf_sha256':sha((OUT/'relation_moment_comparison_proof_20260913.pdf').read_bytes()),'visual_review':'pending actual image inspection'}
(W/'relation_moment_comparison_execution_20260913.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':True,'methods_per_mode':10,'mutants_per_mode':2,'rendered_pages':len(list(qa.glob('page-*.png')))}))
