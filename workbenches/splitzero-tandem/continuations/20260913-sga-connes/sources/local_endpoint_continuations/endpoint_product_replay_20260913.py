"""Replay actual formula mutations, retaining full output records."""
import hashlib,json,subprocess,sys
from pathlib import Path
base=Path(__file__).resolve().parent
checker=base/'endpoint_product_check_20260913.py'
runs=[]
for optimized in [False,True]:
    mode='optimized' if optimized else 'normal'
    for mutant in ['none','mass','interior','beta','schur','phase','raw_factorial']:
        output=base/f'endpoint_product_check_{mode}_{mutant}_20260913.json'
        args=[sys.executable]+(['-O'] if optimized else [])+[checker.name,'--mutant',mutant,'--output',output.name]
        proc=subprocess.run(args,cwd=base,capture_output=True,text=True)
        record=json.loads(output.read_text(encoding='utf-8')) if output.exists() else {}
        expected=0 if mutant=='none' else 1
        ok=proc.returncode==expected and record.get('checks_executed')==415 and ((record.get('failed_count')==0) if mutant=='none' else record.get('failed_count',0)>0)
        runs.append({'mode':mode,'mutant':mutant,'exit_code':proc.returncode,'checks_executed':record.get('checks_executed'),'failed_count':record.get('failed_count'),'accepted':ok,'record':output.name,'record_sha256':hashlib.sha256(output.read_bytes()).hexdigest() if output.exists() else None,'stdout':proc.stdout,'stderr':proc.stderr})
        print(json.dumps({k:runs[-1][k] for k in ['mode','mutant','exit_code','checks_executed','failed_count','accepted']}),flush=True)
receipt={'schema':'endpoint-product-replay-v1','checker_sha256':hashlib.sha256(checker.read_bytes()).hexdigest(),'all_accepted':all(r['accepted'] for r in runs),'runs':runs,'scope':'415 exact auxiliary mathematical checks per run; repeated modes and formula mutations are not additional mathematical checks.'}
(base/'endpoint_product_replay_20260913.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
raise SystemExit(0 if receipt['all_accepted'] else 1)
