from pathlib import Path
import hashlib,json,subprocess,sys
from datetime import datetime,timezone
W=Path(__file__).resolve().parent.parent
T=W/'work/consecutive_first_window_replay_20260913'
T.mkdir(exist_ok=False)
checker=W/'work/check_consecutive_first_window_join_20260913.py'
pin=hashlib.sha256(checker.read_bytes()).hexdigest()
rows=[]
for mode,mutation in [(1,'none')]+[(m,k) for k in ('omit_phase','terminal_square','interior_single') for m in (0,1)]:
 name=f'{mutation}_mode{mode}'
 output=T/(name+'.json')
 argv=[sys.executable,'-B']+(['-O'] if mode else [])+[str(checker),'--mutation',mutation,'--output',str(output)]
 completed=subprocess.run(argv,cwd=W,capture_output=True,timeout=900)
 (T/(name+'.stdout')).write_bytes(completed.stdout);(T/(name+'.stderr')).write_bytes(completed.stderr)
 if hashlib.sha256(checker.read_bytes()).hexdigest()!=pin:raise RuntimeError('Checker changed during replay')
 d=json.loads(output.read_text())
 expected=0 if mutation=='none' else 1
 if completed.returncode!=expected or d['runtime']['optimization']!=mode:raise RuntimeError('Unexpected run outcome')
 if (d['failed']==0)!=(mutation=='none'):raise RuntimeError('Mutation sensitivity mismatch')
 if mutation=='none':
  normal=json.loads((W/'work/consecutive_first_window_checks_normal_v2_20260913.json').read_text())
  if normal['checks']!=d['checks'] or normal['cases']!=d['cases']:raise RuntimeError('Mode result mismatch')
 row={'argv':argv,'cwd':str(W),'returncode':completed.returncode,'passed':d['passed'],'failed':d['failed'],'runtime':d['runtime'],'files':[]}
 for p in (output,T/(name+'.stdout'),T/(name+'.stderr')):
  b=p.read_bytes();row['files'].append({'path':p.relative_to(T).as_posix(),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
 rows.append(row)
 (T/'PROGRESS.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({'job':name,'returncode':completed.returncode,'passed':d['passed'],'failed':d['failed']}),flush=True)
d={'utc':datetime.now(timezone.utc).isoformat(),'checker_sha256':pin,'actual_jobs':rows,
 'prior_positive':'The final ordinary-mode378-pass execution was performed by root through exec_command before this replay; its JSON remains separately retained. This runner executes only the remaining7 jobs and does not relabel that earlier invocation as its own.',
 'historical_failure':'Earlier development result had30 structural-expression equality failures at trace-zero checks; complete historical source/result retained. Final predicate performs exact rational cancellation, without changing any source/matrix or expected theorem.'}
(T/'REPLAY.json').write_text(json.dumps(d,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'receipt':str(T/'REPLAY.json'),'sha256':hashlib.sha256((T/'REPLAY.json').read_bytes()).hexdigest()}),flush=True)
