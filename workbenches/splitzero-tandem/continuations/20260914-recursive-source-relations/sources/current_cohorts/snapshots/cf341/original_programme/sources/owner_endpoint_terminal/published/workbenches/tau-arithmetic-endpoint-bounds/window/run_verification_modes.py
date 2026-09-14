"""Portable bounded runner: four sequential checks, with retained terminal logs."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys
import time
OUT=Path(__file__).resolve().parent
def sha(p):
    with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
results=[]
for name,flags,negative in [('normal',[],False),('optimized',['-O'],False),
                            ('negative_normal',[],True),('negative_optimized',['-O'],True)]:
    cmd=[sys.executable,*flags,str(OUT/'verify_window_product.py')]
    if negative:cmd.append('--negative-control')
    began=time.perf_counter()
    run=subprocess.run(cmd,cwd=OUT,capture_output=True,timeout=60)
    (OUT/(name+'.stdout')).write_bytes(run.stdout)
    (OUT/(name+'.stderr')).write_bytes(run.stderr)
    good=(run.returncode!=0 if negative else run.returncode==0)
    if negative:good=good and b'intentional false Gaussian fixture' in run.stderr
    row={'mode':name,'returncode':run.returncode,'expected_outcome_observed':good,
         'seconds':time.perf_counter()-began,
         'stdout_sha256':sha(OUT/(name+'.stdout')),'stderr_sha256':sha(OUT/(name+'.stderr'))}
    if not negative:
        portable=OUT/'PORTABLE_CHECK_RECEIPT.json'
        saved=OUT/(name+'_CHECK_RECEIPT.json')
        saved.write_bytes(portable.read_bytes())
        row['receipt_sha256']=sha(saved)
    results.append(row)
if not all(row['expected_outcome_observed'] for row in results):raise RuntimeError(results)
normal=json.loads((OUT/'normal_CHECK_RECEIPT.json').read_text())
optimized=json.loads((OUT/'optimized_CHECK_RECEIPT.json').read_text())
if normal['checks']!=optimized['checks']:raise RuntimeError('mode check records differ')
receipt={'schema':'window-product-portable-terminal-modes-v1','status':'PASS',
         'runs':results,'normal_optimized_check_records_identical':True,
         'script_sha256':sha(OUT/'verify_window_product.py'),'runner_sha256':sha(Path(__file__)),
         'portable_exact_checks':normal['exact_checks'],
         'approximate_display_checks':normal['approximate_display_checks'],
         'scope':'Four sequential short SymPy checks; no Lean or analytic/interval replay.'}
(OUT/'TERMINAL_MODES_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps(receipt,indent=2))
