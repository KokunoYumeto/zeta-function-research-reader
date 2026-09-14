"""Time-bounded exact fixture replay; no Lean, network calls, or source edits."""
import hashlib
import json
import os
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
import sympy

ROOT=Path(__file__).resolve().parent
SOURCE=ROOT/'files/workbenches/tau-confluent-transfer/check_transfer_core.py'
OUT=ROOT/'fresh_checks'
OUT.mkdir(exist_ok=True)
expected='fcaef2ee4c972cb71255ed3365930b3a558edc2b66dce5567301b38aff7ed4aa'
actual=hashlib.sha256(SOURCE.read_bytes()).hexdigest()
if actual!=expected: raise ValueError('Public checker source hash mismatch')
records=[]
env=dict(os.environ, PYTHONDONTWRITEBYTECODE='1')
for mode,flags in [('normal',[]),('optimized',['-O'])]:
    for negative in [False,True]:
        label=mode+('_negative' if negative else '')
        command=[sys.executable,*flags,str(SOURCE),*(['--negative-control'] if negative else [])]
        start=time.monotonic()
        try:
            result=subprocess.run(command,capture_output=True,text=True,encoding='utf-8',timeout=45 if not negative else 10,env=env,cwd=ROOT)
            stdout=result.stdout; stderr=result.stderr
            timed_out=False; code=result.returncode
        except subprocess.TimeoutExpired as exc:
            stdout=(exc.stdout or b'').decode('utf-8') if isinstance(exc.stdout,bytes) else exc.stdout or ''
            stderr=(exc.stderr or b'').decode('utf-8') if isinstance(exc.stderr,bytes) else exc.stderr or ''
            timed_out=True; code=None
        (OUT/(label+'.stdout')).write_text(stdout,encoding='utf-8')
        (OUT/(label+'.stderr')).write_text(stderr,encoding='utf-8')
        parsed=None
        if not negative and not timed_out and code==0:
            parsed=json.loads(stdout)
            if parsed!={'errors':0,'failures':0,'scope':'exact finite Gaussian/atomic fixtures; not actual zeta packets, interval certificates, or Lean proofs','success':True,'tests_run':8}: raise ValueError('Unexpected test record')
        if negative and not timed_out:
            if code==0 or 'deliberate negative control' not in stderr: raise ValueError('Negative control did not fail as intended')
        entry={'mode':mode,'negative_control':negative,'seconds':round(time.monotonic()-start,3),'timeout':timed_out,'exit_code':code,'record':parsed,'stdout_sha256':hashlib.sha256(stdout.encode()).hexdigest(),'stderr_sha256':hashlib.sha256(stderr.encode()).hexdigest()}
        records.append(entry)
        print(json.dumps(entry),flush=True)
        if timed_out: break
    if records[-1]['timeout']: break
normal=[r['record'] for r in records if not r['negative_control']]
receipt={'created_utc':datetime.now(timezone.utc).isoformat(),'head':'dfcbba5cbf7fec8c9301fe242c13e741d762013e','checker_sha256':actual,'python':sys.version,'sympy':sympy.__version__,'fresh_local_fixture_replay':True,'source_modified':False,'lean_or_heavy_build':False,'time_limit_per_suite_seconds':45,'runs':records,'both_full_modes_passed':len(normal)==2 and all(x and x['success'] for x in normal),'records_identical':len(normal)==2 and normal[0]==normal[1],'scope':'Public eight-method exact Gaussian/atomic core only; not the unpublished 20-method suite, prior archive, actual arithmetic integrals, or a Lean certificate'}
(ROOT/'FRESH_CORE_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
