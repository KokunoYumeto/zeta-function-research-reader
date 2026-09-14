from pathlib import Path
import json,hashlib,subprocess,sys,datetime,os
p=Path(r"workspace:\output\split_zero_rh_tandem_2026-09-12\sources\web_sga_trace_period_delivery\Tau_SGA_Trace_Period_Control")
w=Path(r"workspace:\work\sga_trace_period_replay_20260913")
w.mkdir(exist_ok=True)
manifest=json.loads((p/'MANIFEST.json').read_text())
for row in manifest['entries']:
 f=p/row['path']; b=f.read_bytes()
 if len(b)!=row['bytes'] or hashlib.sha256(b).hexdigest()!=row['sha256']: raise RuntimeError(row['path'])
env=os.environ.copy(); env['PYTHONPATH']=r'workspace:\work\kernel_layer_replay_dependencies_20260912'
jobs=[]
for opt in [False,True]:
 for control in [None,'jacobian','quantum','newton']:
  name=('optimized' if opt else 'normal')+'_'+(control or 'positive')
  args=[sys.executable]+(['-O'] if opt else [])+[str(p/'check_trace_period.py')]
  args+=['--negative',control] if control else ['--json',str(w/(name+'.json'))]
  started=datetime.datetime.now(datetime.timezone.utc).isoformat()
  r=subprocess.run(args,cwd=w,env=env,capture_output=True)
  (w/(name+'.stdout')).write_bytes(r.stdout); (w/(name+'.stderr')).write_bytes(r.stderr)
  report=json.loads((w/(name+'.json')).read_text()) if control is None else None
  ok=r.returncode==(1 if control else 0) and (control is not None or report['methods']==18 and report['success'])
  jobs.append({'name':name,'argv':args,'started':started,'returncode':r.returncode,'expected_returncode':1 if control else 0,'ok':ok,'report':report})
  (w/'PROGRESS.json').write_text(json.dumps(jobs,indent=2))
  print(name,r.returncode,ok,flush=True)
  if not ok: raise RuntimeError(name)
receipt={'archive_members':47,'manifest_entries_verified':len(manifest['entries']),'checker_sha256':hashlib.sha256((p/'check_trace_period.py').read_bytes()).hexdigest(),'python':sys.version,'sympy_path':env['PYTHONPATH'],'jobs':jobs,'scope':'Only the 18 new methods and three substantive false controls, both modes. No predecessor suite rerun; no Lean; no numerical quadrature rerun.'}
(w/'REPLAY.json').write_text(json.dumps(receipt,indent=2))
print('COMPLETE',len(jobs),flush=True)
