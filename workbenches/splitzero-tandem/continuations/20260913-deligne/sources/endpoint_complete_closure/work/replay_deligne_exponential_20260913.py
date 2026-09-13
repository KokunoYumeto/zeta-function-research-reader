from pathlib import Path
import json, subprocess,sys,hashlib,time,os
src=Path(r'workspace:\output\split_zero_rh_tandem_2026-09-12\sources\web_deligne_exponential_delivery\Tau_Deligne_Exponential_Comparison')
out=Path(r'workspace:\work\deligne_exponential_replay_20260913');out.mkdir(exist_ok=True)
manifest=json.loads((src/'MANIFEST.json').read_text()); verified=[]
for f in manifest['files']:
 b=(src/f['path']).read_bytes()
 if len(b)!=f['bytes'] or hashlib.sha256(b).hexdigest()!=f['sha256']:raise RuntimeError(f)
 verified.append(f)
(out/'MANIFEST_VERIFICATION.json').write_text(json.dumps({'verified':len(verified),'files':verified},indent=2))
jobs=[]
for mode in [0,1]:
 for control in [None,'connection-sign','erase-log-boundary','omit-curvature-atom']:
  name=('optimized' if mode else 'normal')+('-'+control if control else '')
  cmd=[sys.executable]+(['-O'] if mode else [])+[str(src/'check_exponential.py')]
  if control:cmd+=['--negative-control',control]
  else:cmd+=['--json',str(out/(name+'.json'))]
  start=time.time();p=subprocess.run(cmd,cwd=out,capture_output=True)
  (out/(name+'.stdout')).write_bytes(p.stdout);(out/(name+'.stderr')).write_bytes(p.stderr)
  job={'id':name,'argv':cmd,'cwd':str(out),'exit_code':p.returncode,'expected_exit':1 if control else 0,'seconds':time.time()-start,'runtime':sys.version,'optimization':mode,'checker_sha256':hashlib.sha256((src/'check_exponential.py').read_bytes()).hexdigest()}
  jobs.append(job);(out/'PROGRESS.json').write_text(json.dumps(jobs,indent=2));print(name,p.returncode,flush=True)
  if p.returncode!=job['expected_exit']:raise RuntimeError(job)
(out/'REPLAY.json').write_text(json.dumps({'jobs':jobs,'scope':'22 new exact finite methods normal and optimized, three false-control variants in both modes; predecessor not rerun'},indent=2))
