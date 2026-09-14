"""Record exactly the new fixture checker once normally and once under -O."""
from __future__ import annotations
import ast
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import subprocess
import time

ROOT = Path(__file__).resolve().parent
SCRIPT = ROOT / 'check_additional_fourth_jet.py'
PYTHON = Path('runtime:research-python/python.exe')
DEPENDENCIES = Path('workspace:/work/kernel_layer_replay_dependencies_20260912')

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def stamp():
    return datetime.now(timezone.utc).isoformat()

def write_json(path, value):
    path.write_text(json.dumps(value,indent=2,ensure_ascii=False)+'\n', encoding='utf-8')

def main():
    if (ROOT / 'execution_receipt.json').exists():
        raise RuntimeError('Refusing to replace an existing execution receipt')
    syntax = ast.parse(SCRIPT.read_text(encoding='utf-8'))
    assertions = sum(isinstance(n,ast.Assert) for n in ast.walk(syntax))
    if assertions:
        raise RuntimeError('Removable Python assertion found before execution')
    write_json(ROOT / 'code_audit.json', {
        'audited_utc':stamp(),'script_sha256':sha(SCRIPT),'python_assert_count':assertions,
        'imports':[ast.unparse(n) for n in ast.walk(syntax) if isinstance(n,(ast.Import,ast.ImportFrom))],
        'scope':'One new fixed nonscalar fixture; exact scalar determinant recurrences independently compared with noncommutative Q recursion and RCX32.',
        'failure_mechanism':'Explicit AssertionError from check; no Python assert statements.',
        'ordered_solution_recurrence':'(n+1)B[n+1]=-(B[n]A+B[n-1]R)/u',
        'independent_Q_recurrence':'Q[n+1]=Q[n] prime-(A+tR)Q[n]/u',
        'source_snapshot_sha256':sha(ROOT/'reviewed_companion_snapshot.tex'),
        'no_predecessor_imports':True,'no_lean_entrypoints':True,
    })
    env = os.environ.copy()
    env['PYTHONPATH'] = str(DEPENDENCIES)
    env['PYTHONDONTWRITEBYTECODE'] = '1'
    receipt = {'status':'RUNNING','started_utc':stamp(),'script_sha256':sha(SCRIPT),
               'driver_sha256':sha(Path(__file__)), 'source_snapshot_sha256':sha(ROOT/'reviewed_companion_snapshot.tex'),
               'environment':{'PYTHONPATH':env['PYTHONPATH'],'PYTHONDONTWRITEBYTECODE':env['PYTHONDONTWRITEBYTECODE']},
               'executions':[],'no_prior_reruns':True,'no_lean_execution':True}
    math_records = []
    for mode,opt in [('normal',[]),('optimized',['-O'])]:
        argv = [str(PYTHON),*opt,str(SCRIPT)]
        started = stamp()
        tic = time.perf_counter()
        process = subprocess.run(argv,cwd=ROOT,env=env,capture_output=True,timeout=180)
        elapsed = time.perf_counter()-tic
        stdout = ROOT / (mode+'.stdout.json')
        stderr = ROOT / (mode+'.stderr.txt')
        stdout.write_bytes(process.stdout)
        stderr.write_bytes(process.stderr)
        row = {'mode':mode,'argv':argv,'cwd':str(ROOT),'started_utc':started,'finished_utc':stamp(),
               'elapsed_seconds':elapsed,'exit_code':process.returncode,
               'stdout_path':str(stdout),'stdout_sha256':sha(stdout),
               'stderr_path':str(stderr),'stderr_sha256':sha(stderr)}
        receipt['executions'].append(row)
        write_json(ROOT/'execution_receipt.json',receipt)
        if process.returncode != 0:
            receipt['status']='FAIL';receipt['first_failure']=mode
            write_json(ROOT/'execution_receipt.json',receipt)
            print(json.dumps(receipt,indent=2))
            raise RuntimeError('First checker failure recorded; stop and report before any correction')
        result = json.loads(process.stdout.decode('utf-8'))
        if result['status'] != 'PASS' or result['sympy'] != '1.14.0' or result['optimization_level'] != (1 if opt else 0) or process.stderr:
            receipt['status']='FAIL';receipt['first_failure']='output/runtime validation in '+mode
            write_json(ROOT/'execution_receipt.json',receipt)
            raise RuntimeError('First output validation failure recorded; stop and report before correction')
        if not Path(result['sympy_file']).resolve().is_relative_to(DEPENDENCIES.resolve()):
            receipt['status']='FAIL';receipt['first_failure']='wrong SymPy import location'
            write_json(ROOT/'execution_receipt.json',receipt)
            raise RuntimeError('Dependency location failure recorded; report before correction')
        row['exact_check_count']=result['exact_check_count']
        row['python']=result['python'];row['sympy']=result['sympy'];row['sympy_file']=result['sympy_file']
        row['comparison']=result['comparison']
        mathematical = dict(result)
        del mathematical['optimization_level']
        math_records.append(mathematical)
        write_json(ROOT/'execution_receipt.json',receipt)
        print(mode+': PASS; '+str(result['exact_check_count'])+' exact fixture checks',flush=True)
    if math_records[0] != math_records[1]:
        receipt['status']='FAIL';receipt['first_failure']='normal/optimized mathematical records differ'
        write_json(ROOT/'execution_receipt.json',receipt)
        raise RuntimeError('Record comparison failure; report before correction')
    receipt['status']='PASS';receipt['finished_utc']=stamp()
    receipt['normal_optimized_records_identical_except_optimization_level']=True
    receipt['checker_invocations']=2
    receipt['exact_checks_per_mode']=math_records[0]['exact_check_count']
    receipt['comparison']=math_records[0]['comparison']
    write_json(ROOT/'execution_receipt.json',receipt)
    print(json.dumps({'status':'PASS','comparison':receipt['comparison']},indent=2),flush=True)

if __name__ == '__main__':
    main()
