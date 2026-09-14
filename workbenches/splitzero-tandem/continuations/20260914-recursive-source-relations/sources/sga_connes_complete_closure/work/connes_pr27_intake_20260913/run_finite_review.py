"""Sequential reviewed finite execution, subprocess output isolated from source."""
import hashlib
import json
import os
import platform
import re
import subprocess
import sys
import time
from pathlib import Path
import sympy
import mpmath

ROOT = Path(__file__).resolve().parent
OUT = ROOT/'finite_output'
OUT.mkdir(exist_ok=True)
SRC = ROOT/'source/workbenches/tau-specialization-curvature-formal'
env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1')
env['OPENBLAS_NUM_THREADS']='1'
env['OMP_NUM_THREADS']='1'
receipt = {'schema':'pr27-finite-review-v1','python':sys.version,'executable':sys.executable,'sympy':sympy.__version__,'mpmath':mpmath.__version__,'platform':platform.platform(),'no_local_lean':True,'no_installs':True,'sequential':True,'runs':[],'comparisons':[]}

def run(label,args,expect=0):
    start=time.monotonic()
    result=subprocess.run([sys.executable,'-B',*args],cwd=OUT,env=env,capture_output=True,timeout=180)
    for kind,data in [('stdout',result.stdout),('stderr',result.stderr)]:
        (OUT/(label+'.'+kind)).write_bytes(data)
    item={'label':label,'args':args,'exit_code':result.returncode,'expected_exit':expect,'seconds':round(time.monotonic()-start,3),'stdout_sha256':hashlib.sha256(result.stdout).hexdigest(),'stderr_sha256':hashlib.sha256(result.stderr).hexdigest()}
    receipt['runs'].append(item)
    print(label, result.returncode, flush=True)
    if (expect==0 and result.returncode!=0) or (expect!=0 and result.returncode==0):
        raise RuntimeError('unexpected result '+label)
    return result

for name,methods in [('specialization',17),('laplacian',10)]:
    normal=run(name+'.normal',[str(SRC/('check_'+name+'.py'))])
    optimized=run(name+'.optimized',['-O',str(SRC/('check_'+name+'.py'))])
    if normal.stdout != optimized.stdout:
        raise RuntimeError('normal/-O record mismatch')
    parsed=json.loads(normal.stdout)
    if parsed['status']!='PASS' or parsed['methods']!=methods or parsed['errors'] or parsed['failures']:
        raise RuntimeError('suite result mismatch')
    receipt['comparisons'].append({'suite':name,'methods':methods,'normal_optimized_byte_equal':True})
    for mode,flags in [('normal',[]),('optimized',['-O'])]:
        result=run(name+'.negative.'+mode,[*flags,str(SRC/('check_'+name+'.py')),'--negative'],expect=1)
        if b'intentional' not in result.stderr or b'negative control' not in result.stderr:
            raise RuntimeError('negative failed for wrong reason')

for mode,flags in [('normal',[]),('optimized',['-O'])]:
    result=run('independent_negatives.'+mode,[*flags,str(ROOT/'review_negatives.py')])
    if json.loads(result.stdout)['status']!='PASS':
        raise RuntimeError('independent negative failed')

for job in ['103666603149','103666609598']:
    full=(ROOT/'evidence'/('job_'+job+'.full.log')).read_text(encoding='utf-8')
    lines=[re.sub(r'^\d{4}-\d{2}-\d{2}T\S+\s?','',line) for line in full.splitlines()]
    reports=[line for line in lines if re.match(r"^'SplitZero\.",line)]
    for name,prefixes in [('specialization',('SplitZero.RelationCurve.','SplitZero.SpecializationChart.','SplitZero.ActionHull.','SplitZero.CurvatureRestriction.')),('laplacian',('SplitZero.LaplacianControl.',))]:
        selected=[line for line in reports if any(line.startswith("'"+prefix) for prefix in prefixes)]
        path=OUT/(job+'.'+name+'.audit.log')
        path.write_text('\n'.join(selected)+'\n',encoding='utf-8',newline='\n')
        for mode,flags in [('normal',[]),('optimized',['-O'])]:
            run(job+'.'+name+'.audit.'+mode,[*flags,str(SRC/('check_'+name+'.py')),'--audit',str(path)])

manifest=json.loads((ROOT/'SOURCE_MANIFEST.json').read_text(encoding='utf-8'))
for file in manifest['files']:
    actual=hashlib.sha256((ROOT/'source'/file['path']).read_bytes()).hexdigest()
    if actual != file['sha256']:
        raise RuntimeError('source changed: '+file['path'])
receipt['source_files_unchanged']=len(manifest['files'])
receipt['status']='PASS'
(ROOT/'FINITE_RECEIPT.json').write_text(json.dumps(receipt,sort_keys=True,indent=2)+'\n',encoding='utf-8')
print('PASS; source preserved',receipt['source_files_unchanged'],flush=True)
