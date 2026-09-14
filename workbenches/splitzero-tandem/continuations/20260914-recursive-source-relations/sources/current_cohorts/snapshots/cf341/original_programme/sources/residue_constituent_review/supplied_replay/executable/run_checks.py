#!/usr/bin/env python3
"""Run one normal/optimized calibration batch, recording each actual command."""
from pathlib import Path
import argparse, hashlib, json, subprocess, sys, time
p=argparse.ArgumentParser();p.add_argument('mode',choices=['normal','optimized']);a=p.parse_args()
root=Path(__file__).resolve().parent; script=root/'check_residue_curvature.py'
opt=['-O'] if a.mode=='optimized' else []
receipts=[]
for negative in [None,'rank','laplacian','curvature']:
    args=[sys.executable,*opt,str(script)]+(['--negative',negative] if negative else [])
    label=a.mode+('.negative_'+negative if negative else '')
    start=time.time();r=subprocess.run(args,capture_output=True,text=True,timeout=40)
    (root/'checks'/f'{label}.stdout.txt').write_text(r.stdout)
    (root/'checks'/f'{label}.stderr.txt').write_text(r.stderr)
    receipts.append({'argv':args,'exit_code':r.returncode,'elapsed_seconds':round(time.time()-start,3),
                     'stdout':f'checks/{label}.stdout.txt','stderr':f'checks/{label}.stderr.txt'})
    (root/'checks'/f'EXECUTION_{a.mode}.json').write_text(json.dumps({'script_sha256':hashlib.sha256(script.read_bytes()).hexdigest(),'executions':receipts},indent=2))
    if negative is None:
        if r.returncode!=0: raise RuntimeError(r.stdout+r.stderr)
        (root/'checks'/f'{a.mode}.json').write_text(r.stdout)
    elif r.returncode!=1 or 'intentional' not in r.stderr:
        raise RuntimeError('negative control not rejected as specified')
print(f'{a.mode}: 12 methods passed; three false formulas rejected')
