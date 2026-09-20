"""Run the two independently authored finite checkers, keeping every receipt."""
import concurrent.futures
import hashlib
import json
from pathlib import Path
import subprocess
import sys

P=Path(__file__).resolve().parent
OUT=P/'root_replay'
OUT.mkdir(exist_ok=True)
jobs=[]
for mode,flags in [('normal',[]),('optimized',['-O'])]:
    jobs.append((mode+'_root',flags,'check_original_kernel.py',[],True))
    jobs.append((mode+'_independent',flags,'independent/check_identities.py',[],True))
    jobs.append((mode+'_receiver_independent',flags,'independent/check_receiver.py',[],True))
    for control in ['adjoint','diagonal','degree','mass','four-sign']:
        jobs.append((mode+'_root_control_'+control,flags,'check_original_kernel.py',['--control',control],False))
    jobs.append((mode+'_independent_control',flags,'independent/check_identities.py',['--negative-control'],False))

def run(job):
    name,flags,script,args,success=job
    result=subprocess.run([sys.executable,'-B','-X','utf8',*flags,str(P/script),*args],
                          cwd=P,capture_output=True,text=True,encoding='utf-8',timeout=240)
    (OUT/(name+'.stdout.txt')).write_text(result.stdout,encoding='utf-8')
    (OUT/(name+'.stderr.txt')).write_text(result.stderr,encoding='utf-8')
    if success != (result.returncode==0):
        raise RuntimeError(f'{name}: unexpected exit {result.returncode}')
    if not success and not any(word in result.stderr for word in ['ArithmeticError','deliberate corruption']):
        raise RuntimeError(f'{name}: failed for an unrelated reason')
    return {'name':name,'returncode':result.returncode,'expected_success':success,
            'script':script,'script_sha256':hashlib.sha256((P/script).read_bytes()).hexdigest(),
            'stdout_sha256':hashlib.sha256(result.stdout.encode()).hexdigest(),
            'stderr_sha256':hashlib.sha256(result.stderr.encode()).hexdigest()}

receiver_only = sys.argv[1:]==['--receiver-only']
if receiver_only:
    jobs=[job for job in jobs if job[0].endswith('_receiver_independent')]
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
    records=[]
    for record in pool.map(run,jobs):
        records.append(record)
        print(record['name'],record['returncode'],flush=True)

receipt={'status':'passed','runs':records,'scope':
    'Exact finite algebra fixtures only. Root controls mutate the dual, cross terms, degree, mass and four signs. Independent control checks failure-path activation. Neither checker evaluates actual arithmetic moments or the original period.'}
(OUT/('REPLAY_RECEIVER.json' if receiver_only else 'REPLAY.json')).write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print('All checker runs and deliberate controls behaved as expected.',flush=True)
