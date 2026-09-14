"""Run the declared ordinary/optimized exact formulas and five mutations."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys

ROOT=Path(__file__).resolve().parent
CHECK=ROOT/'gamma_finite_metric_transfer_check_20260913.py'
FAULTS=[None,'mass','tensor-cross','boundary-sign','conjugation','schur-denominator']

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def require(value,message):
    if not value:
        raise RuntimeError(message)

records=[]
for optimized in (False,True):
    for fault in FAULTS:
        mode='optimized' if optimized else 'normal'
        label=mode if fault is None else mode+'_'+fault.replace('-','_')
        output=ROOT/f'gamma_finite_metric_transfer_check_{label}_20260913.json'
        argv=[sys.executable,'-B']+(['-O'] if optimized else [])+[str(CHECK),'--output',str(output)]
        if fault is not None:
            argv += ['--fault',fault]
        result=subprocess.run(argv,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,timeout=60)
        payload=json.loads(output.read_text(encoding='utf-8'))
        require(result.returncode==(0 if fault is None else 1),'wrong process return code')
        require(payload['check_count']==121,'wrong declared check count')
        require(payload['failed_count']==(0 if fault is None else 1),'wrong exact failure count')
        require(payload['python_optimized'] is optimized,'process optimization flag not observed')
        require(payload['script_sha256']==digest(CHECK),'checker byte pin mismatch')
        records.append({'argv':argv,'returncode':result.returncode,'optimized':optimized,'fault':fault,
                        'stdout':result.stdout,'stderr':result.stderr,'output':output.name,
                        'output_sha256':digest(output),'failed_checks':[c['name'] for c in payload['checks'] if not c['passed']]})
        print(label, result.returncode, payload['failed_count'], flush=True)
normal=json.loads((ROOT/'gamma_finite_metric_transfer_check_normal_20260913.json').read_text())
optimized=json.loads((ROOT/'gamma_finite_metric_transfer_check_optimized_20260913.json').read_text())
normal.pop('python_optimized'); optimized.pop('python_optimized')
require(normal==optimized,'positive execution records differ beyond the optimization flag')
receipt={'schema':'gamma-finite-metric-transfer-replay-v1','status':'passed',
         'checker_sha256':digest(CHECK),'validator_sha256':digest(Path(__file__)),
         'proof_sha256_at_execution':digest(ROOT/'gamma_finite_metric_transfer_20260913.tex'),
         'jobs':records,'normal_optimized_equal_except_observed_flag':True,
         'scope':'Exact algebraic calibration and proved tail-bound integer comparisons; no actual zero-packet claim and no Lean.'}
(ROOT/'gamma_finite_metric_transfer_validation_20260913.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
