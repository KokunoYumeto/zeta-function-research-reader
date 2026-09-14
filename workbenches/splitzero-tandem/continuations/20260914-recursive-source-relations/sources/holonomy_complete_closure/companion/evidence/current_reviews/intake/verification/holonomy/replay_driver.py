"""New 22-case holonomy replay plus separate substantive negatives only."""
from __future__ import annotations
import ast
from datetime import datetime,timezone
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import time

ROOT=Path(__file__).resolve().parent
RAW=Path('source-workspace/output/split_zero_rh_tandem_2026-09-12/sources/web_holonomy_descent_delivery/Tau_Holonomy_Descent_Control')
PYTHON=Path('local-profile/miniconda3/python.exe')
DEPENDENCIES=Path('source-workspace/work/kernel_layer_replay_dependencies_20260912')

def stamp():return datetime.now(timezone.utc).isoformat()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(path,value):path.write_text(json.dumps(value,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def must(condition,message):
    if not condition:raise RuntimeError(message)
def snapshot():return {p.relative_to(RAW).as_posix():{'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(RAW.rglob('*')) if p.is_file()}

def main():
    must(not (ROOT/'execution_receipt.json').exists(),'Refusing to replace earlier execution evidence')
    before=snapshot();write(ROOT/'raw_snapshot_before.json',before)
    manifest=json.loads((RAW/'MANIFEST.json').read_text(encoding='utf-8'))
    rows=[]
    for relative,pin in manifest['files'].items():
        target=(RAW/relative).resolve()
        must(target.is_relative_to(RAW.resolve()),'Manifest target outside raw directory')
        actual=before.get(relative)
        rows.append({'path':relative,'expected':pin,'actual':actual,'valid':actual==pin})
    unlisted=sorted(set(before)-set(manifest['files'])-{'MANIFEST.json'})
    manifest_result={'checked_utc':stamp(),'source':str(RAW),'manifest_sha256':sha(RAW/'MANIFEST.json'),
                     'row_count':len(rows),'all_rows_valid':all(r['valid'] for r in rows),'unlisted_except_manifest':unlisted,'rows':rows}
    write(ROOT/'manifest_validation.json',manifest_result)
    must(manifest_result['all_rows_valid'] and not unlisted,'Raw manifest failure; see receipt')
    source_script=RAW/'scripts/check_holonomy.py'
    syntax=ast.parse(source_script.read_text(encoding='utf-8'))
    methods=[n.name for n in syntax.body if isinstance(n,ast.FunctionDef) and any(isinstance(d,ast.Name) and d.id=='case' for d in n.decorator_list)]
    negative_script=ROOT/'substantive_negative_controls.py'
    negative_syntax=ast.parse(negative_script.read_text(encoding='utf-8'))
    code_audit={'audited_utc':stamp(),'source_script_sha256':sha(source_script),'new_method_count':len(methods),'new_methods':methods,
                'source_assert_count':sum(isinstance(n,ast.Assert) for n in ast.walk(syntax)),
                'separate_negative_assert_count':sum(isinstance(n,ast.Assert) for n in ast.walk(negative_syntax)),
                'source_imports':[ast.unparse(n) for n in ast.walk(syntax) if isinstance(n,(ast.Import,ast.ImportFrom))],
                'complete_script_manifest_validation_handoff_read':True,
                'supplied_negative_defect':'main always raises if negative returns; support branch compares literal fixed unequal tuples. Other two branches compute substantive formulas.',
                'separate_negative_design':'Actual target computations/mutations; explicit rejection at formula comparison. If mutant equality unexpectedly passes, main returns zero. No unconditional rejection guard.',
                'supplied_negative_logs':'Retained historical source evidence only; supplied negative CLI branches are not newly executed.',
                'no_predecessor_import_or_execution':True,'reader_builder_and_browser_not_executed':True}
    write(ROOT/'code_audit.json',code_audit)
    must(len(methods)==22 and code_audit['source_assert_count']==0 and code_audit['separate_negative_assert_count']==0,'Unexpected case inventory or removable assertion')
    executable=ROOT/'executable';must(not executable.exists(),'Fresh executable copy required');executable.mkdir()
    script=executable/'check_holonomy.py';shutil.copyfile(source_script,script)
    must(sha(source_script)==sha(script),'Checker copy hash mismatch')
    import sympy
    must(sys.version_info[:3]==(3,13,9),'Wrong Python version')
    must(Path(sys.executable).resolve()==PYTHON.resolve(),'Wrong Python interpreter')
    must(sympy.__version__=='1.14.0' and Path(sympy.__file__).resolve().is_relative_to(DEPENDENCIES.resolve()),'Wrong SymPy runtime')
    environment=os.environ.copy();environment['PYTHONPATH']=str(DEPENDENCIES);environment['PYTHONDONTWRITEBYTECODE']='1'
    runtime={'python_executable':sys.executable,'python_version':sys.version,'sympy_version':sympy.__version__,'sympy_file':sympy.__file__,
             'PYTHONPATH':environment['PYTHONPATH'],'PYTHONDONTWRITEBYTECODE':environment['PYTHONDONTWRITEBYTECODE']}
    write(ROOT/'runtime.json',runtime)
    receipt={'status':'RUNNING','started_utc':stamp(),'runtime':runtime,'source_script_sha256':sha(source_script),
             'negative_script_sha256':sha(negative_script),'driver_sha256':sha(Path(__file__)),
             'raw_manifest_rows':len(rows),'executions':[],'no_predecessor_suite_run':True,'no_lean_run':True,
             'supplied_negative_branches_run':False,'new_controls_only':True,'no_reader_browser_run':True}
    successes=[]
    for mode,opt in [('normal',[]),('optimized',['-O'])]:
        for negative in [None,'erase-variance','support-is-absence','omit-fourier-factor']:
            label=mode+('.negative-'+negative if negative else '.suite')
            argv=[str(PYTHON),*opt,str(negative_script if negative else script)]
            if negative:argv+=['--negative',negative]
            started=stamp();tic=time.perf_counter()
            process=subprocess.run(argv,cwd=ROOT,env=environment,capture_output=True,timeout=300)
            elapsed=time.perf_counter()-tic
            stdout=ROOT/(label+'.stdout.json');stderr=ROOT/(label+'.stderr.txt')
            stdout.write_bytes(process.stdout);stderr.write_bytes(process.stderr)
            row={'label':label,'mode':mode,'negative':negative,'argv':argv,'cwd':str(ROOT),'started_utc':started,'finished_utc':stamp(),
                 'elapsed_seconds':elapsed,'exit_code':process.returncode,'stdout_path':str(stdout),'stdout_sha256':sha(stdout),
                 'stderr_path':str(stderr),'stderr_sha256':sha(stderr)}
            receipt['executions'].append(row);write(ROOT/'execution_receipt.json',receipt)
            if negative is None:
                must(process.returncode==0 and not process.stderr,'New positive suite failed; stop and report recorded evidence')
                result=json.loads(process.stdout.decode('utf-8'))
                must(result['status']=='pass' and result['count']==22 and result['methods']==methods,'Incomplete or mismatched positive case inventory')
                row['verified_method_count']=22;row['verified_method_names']=result['methods'];successes.append(process.stdout)
                print(mode+': all 22 genuinely new methods passed',flush=True)
            else:
                error=process.stderr.decode('utf-8')
                result=json.loads(process.stdout.decode('utf-8'))
                marker='ArithmeticError: MUTATION_REJECTED:'+negative+':'
                must(process.returncode==1 and marker in error and result['control']==negative,'Separate false control did not fail substantively; report before correction')
                must('BASELINE_FAILED' not in error and not any(s in error for s in ['ModuleNotFoundError','ImportError','SyntaxError']),'Negative failed before mutation comparison')
                row['verified_substantive_formula_failure']=True;row['evidence']=result
            write(ROOT/'execution_receipt.json',receipt)
    after=snapshot();write(ROOT/'raw_snapshot_after.json',after)
    must(before==after,'Raw packet changed during replay')
    must(successes[0]==successes[1],'Positive normal/optimized outputs differ')
    receipt.update({'status':'PASS','finished_utc':stamp(),'raw_files_unchanged':len(before),'raw_packet_unchanged':True,
                    'positive_methods_each_mode':22,'positive_method_invocations_total':44,
                    'separate_substantive_negatives_each_mode':3,'negative_invocations_total':6,
                    'checker_process_invocations_total':8,'normal_optimized_success_records_byte_identical':True})
    write(ROOT/'execution_receipt.json',receipt)
    print(json.dumps({k:v for k,v in receipt.items() if k not in ['runtime','executions']},indent=2),flush=True)

if __name__=='__main__':main()
