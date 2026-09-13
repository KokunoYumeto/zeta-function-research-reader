from pathlib import Path
import hashlib,json,os,subprocess,sys,time
W=Path(r'workspace:')
R=W/'output/split_zero_rh_tandem_2026-09-12'
P=R/'sources/web_gamma_convolution_delivery/Tau_Gamma_Convolution_Descent'
O=W/'work/gamma_convolution_replay_20260913'
O.mkdir(parents=True,exist_ok=True)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def require(v,m):
    if not v:raise RuntimeError(m)
manifest=json.loads((P/'MANIFEST.sha256.json').read_text())
checks=[]
for name,record in manifest.items():
    target=(P/name).resolve()
    require(target.is_relative_to(P.resolve()),'manifest path escaped')
    require(target.stat().st_size==record['bytes'] and sha(target)==record['sha256'],'manifest mismatch '+name)
    checks.append(name)
require(len(checks)==37,'manifest count')
before={str(p.relative_to(P)):sha(p) for p in P.rglob('*') if p.is_file()}
env=os.environ.copy();env['PYTHONPATH']=str(W/'work/kernel_layer_replay_dependencies_20260912')
env['PYTHONDONTWRITEBYTECODE']='1';env['OMP_NUM_THREADS']='1';env['OPENBLAS_NUM_THREADS']='1'
records=[]
for optimized in (False,True):
    for negative in (False,True):
        name=('optimized' if optimized else 'normal')+('-false-control' if negative else '')
        output=O/(name+'.json')
        command=[sys.executable,'-B']+(['-O'] if optimized else [])+[str(P/'check_gamma_descent.py')]
        command+=['--fail-control'] if negative else ['--json',str(output)]
        start=time.monotonic();run=subprocess.run(command,cwd=O,env=env,capture_output=True,text=True,timeout=300)
        log=O/(name+'.log');log.write_text(run.stdout+run.stderr,encoding='utf-8')
        require(run.returncode==(1 if negative else 0),'unexpected exit '+name)
        rec={'mode':name,'command':command,'exit_code':run.returncode,'elapsed_seconds':time.monotonic()-start,'log_sha256':sha(log)}
        if negative:
            require('deliberately false exact equality' in run.stderr,'missing false-control exception')
            rec['scope']='Startup guard only; zero regression methods are run.'
        else:
            data=json.loads(output.read_text())
            require(data=={'status':'passed','test_methods':17,'failures':0,'errors':0,'scope':'exact polynomial/matrix calibrations; no arithmetic quadrature, Lean or RH certificate','sympy':'1.14.0'},'unexpected result record')
            rec['result']=data;rec['result_sha256']=sha(output)
        records.append(rec)
after={str(p.relative_to(P)):sha(p) for p in P.rglob('*') if p.is_file()}
require(before==after,'preserved source changed')
receipt={'archive_sha256':'4b93cc5e9db76fdc6dec406c05197e2de5d7daab5957a855ee8b77711652b61a',
 'checker_sha256':sha(P/'check_gamma_descent.py'),'manifest_entries_verified':checks,'original_source_files_unchanged':len(after),
 'runs':records,'normal_optimized_records_equal':(O/'normal.json').read_bytes()==(O/'optimized.json').read_bytes(),
 'inherited_toda_suite_replayed':False,'negative_control_scope':'Unconditional false startup guard; no deliberately perturbed theorem formula is checked.'}
(O/'replay_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps(receipt,indent=2))
