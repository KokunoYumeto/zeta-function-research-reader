from pathlib import Path
import argparse,hashlib,json,os,subprocess,sys
here=Path(__file__).resolve().parent
parser=argparse.ArgumentParser()
parser.add_argument("--output-directory",type=Path,
    default=here/"gamma_exact_coefficient_join_build_20260913/checks")
parser.add_argument("--dependency-path",type=Path)
args=parser.parse_args()
script=here/"gamma_exact_coefficient_join_check_20260913.py"
source=here/"gamma_exact_coefficient_join_20260913.tex"
out=args.output_directory.resolve()
out.mkdir(parents=True,exist_ok=True)
def H(p):return hashlib.sha256(p.read_bytes()).hexdigest()
env=os.environ.copy()
dependency=args.dependency_path
if dependency is None and (here/"kernel_layer_replay_dependencies_20260912").is_dir():
    dependency=here/"kernel_layer_replay_dependencies_20260912"
if dependency is not None:env["PYTHONPATH"]=str(dependency.resolve())
env["PYTHONDONTWRITEBYTECODE"]="1"
env["OMP_NUM_THREADS"]="1"
env["OPENBLAS_NUM_THREADS"]="1"
records=[]
mutants=[None,"coefficient-factorial","initial-mass","coordinate-sign",
         "determinant-phase","derivative-degree","cochain-sign"]
for optimized in [False,True]:
    for mutant in mutants:
        name=("optimized" if optimized else "normal")+("-"+mutant if mutant else "")
        result=out/(name+".json")
        command=[sys.executable,"-B"]+(["-O"] if optimized else [])+[str(script),"--json",str(result)]
        if mutant:command+=["--mutant",mutant]
        run=subprocess.run(command,cwd=out,env=env,capture_output=True,text=True,timeout=120)
        log=out/(name+".log")
        log.write_text(run.stdout+run.stderr,encoding="utf-8")
        if not result.is_file():raise RuntimeError((name,"result missing",run.stderr))
        record=json.loads(result.read_text())
        expected=1 if mutant else 0
        if run.returncode!=expected or record["checks"]!=143 or len(record["failed_checks"])!=expected or record["sympy"]!="1.14.0":
            raise RuntimeError((name,run.returncode,record))
        if any(not r["passed"] and not r["mutant"] for r in record["records"]):
            raise RuntimeError("A nonmutant formula failed")
        records.append({"mode":name,"command":command,"exit_code":run.returncode,
            "checks":record["checks"],"failed_checks":record["failed_checks"],
            "result_sha256":H(result),"log_sha256":H(log)})
        print(name,run.returncode,record["failed_checks"],flush=True)
receipt={"source_sha256":H(source),"checker_sha256":H(script),"sympy":"1.14.0",
 "checks_per_run":143,"run_count":14,"runs":records,
 "normal_optimized_records_equal":(out/"normal.json").read_bytes()==(out/"optimized.json").read_bytes(),
 "scope":"Finite exact coefficient/coordinate/derivative/cochain/section regressions; each negative mode perturbs one actual displayed formula and must fail exactly one of the same 143 checks.",
 "new_lean_execution":False,"arithmetic_interval_certificate":False}
(out/"replay_receipt.json").write_text(json.dumps(receipt,indent=2)+"\n",encoding="utf-8")
print("receipt_sha256",H(out/"replay_receipt.json"),flush=True)
