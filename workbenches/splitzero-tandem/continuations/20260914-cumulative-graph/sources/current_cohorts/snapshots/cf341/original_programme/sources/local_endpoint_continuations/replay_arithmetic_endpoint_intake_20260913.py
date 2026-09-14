"""Byte audit and sequential replay of the delivered finite endpoint checker."""
from pathlib import Path, PurePosixPath
import datetime, hashlib, json, os, subprocess, sys, time, zipfile

WORK = Path(__file__).resolve().parent
R = WORK.parent / 'output' / 'split_zero_rh_tandem_2026-09-12'
SOURCE = R / 'sources' / 'web_arithmetic_endpoint_delivery' / 'Tau_Arithmetic_Endpoint_Bounds'
OUT = WORK / 'arithmetic_endpoint_intake_replay_20260913'

def digest(data):
    return hashlib.sha256(data).hexdigest()

def require(condition, message):
    if not condition:
        raise RuntimeError(message)

def main():
    OUT.mkdir(exist_ok=True)
    inventory = json.loads((SOURCE / 'MANIFEST.sha256.json').read_text())
    checked=[]
    for name, meta in inventory.items():
        path=(SOURCE / name).resolve()
        require(path.is_relative_to(SOURCE.resolve()), name)
        data=path.read_bytes()
        require(len(data)==meta['bytes'] and digest(data)==meta['sha256'], name)
        checked.append({'path':name, **meta})
    inherited = json.loads((SOURCE / 'checks' / 'inherited-manifest.json').read_text())
    gamma = R / 'sources' / 'web_gamma_convolution_delivery' / 'Tau_Gamma_Convolution_Descent'
    inherited_checked=[]
    for meta in inherited['files']:
        data=(gamma / meta['path']).read_bytes()
        require(len(data)==meta['bytes'] and digest(data)==meta['sha256'], meta['path'])
        inherited_checked.append(meta)
    # Parse the complete add-only patch without changing a Git checkout.
    patch=(SOURCE / 'INTEGRATION.patch').read_bytes()
    lines=patch.splitlines(keepends=True)
    patch_members=[]
    pos=0
    while pos < len(lines):
        if not lines[pos].startswith(b'diff --git '):
            pos+=1
            continue
        start=pos; pos+=1
        while pos<len(lines) and not lines[pos].startswith(b'diff --git '): pos+=1
        segment=lines[start:pos]
        require(any(x==b'new file mode 100644\n' for x in segment),'patch contains non-addition')
        path_line=next(x for x in segment if x.startswith(b'+++ b/'))
        path=path_line[len(b'+++ b/'):].rstrip(b'\r\n').decode()
        require(path.startswith('workbenches/tau-arithmetic-endpoint-bounds/'),'unexpected patch prefix')
        rel=path.split('/',2)[2]
        hunk=next(i for i,x in enumerate(segment) if x.startswith(b'@@'))
        body=segment[hunk+1:]
        additions=[]
        for line in body:
            if line.startswith(b'+'):
                additions.append(line[1:])
            elif line==b'\\ No newline at end of file\n':
                require(bool(additions) and additions[-1].endswith(b'\n'),'invalid no-newline marker')
                additions[-1]=additions[-1][:-1]
            else:
                raise RuntimeError('not a single pure-add hunk: '+rel)
        data=b''.join(additions)
        require(data==(SOURCE/rel).read_bytes(),'patch differs: '+rel)
        patch_members.append({'path':path,'bytes':len(data),'sha256':digest(data)})
    checker=SOURCE/'check_endpoint_bounds.py'
    expected=digest(checker.read_bytes())
    runs=[]
    env={**os.environ,'PYTHONHASHSEED':'0','PYTHONDONTWRITEBYTECODE':'1','OMP_NUM_THREADS':'1','OPENBLAS_NUM_THREADS':'1','MKL_NUM_THREADS':'1'}
    for name, flags, extra in [('normal',[],[]),('optimized',['-O'],[]),('fail-normal',[],['--fail-control']),('fail-optimized',['-O'],['--fail-control'])]:
        require(digest(checker.read_bytes())==expected,'checker changed before replay')
        cmd=[sys.executable,*flags,str(checker),*extra]
        start=time.monotonic()
        result=subprocess.run(cmd,cwd=OUT,env=env,capture_output=True,timeout=180)
        elapsed=time.monotonic()-start
        (OUT/(name+'.stdout')).write_bytes(result.stdout)
        (OUT/(name+'.stderr')).write_bytes(result.stderr)
        record={'name':name,'python_flags':flags,'checker_args':extra,'returncode':result.returncode,'seconds':elapsed,'stdout_sha256':digest(result.stdout),'stderr_sha256':digest(result.stderr)}
        if extra:
            require(result.returncode==1 and b'intentional verification-control failure' in result.stderr,'failure control did not fail as declared')
            record.update({'guard_failure':True,'test_methods_executed':0,'mathematical_mutant':False})
        else:
            payload=json.loads(result.stdout)
            require(result.returncode==0 and payload['status']=='PASS' and payload['methods']==18 and not payload['errors'] and not payload['failures'],name+' failed')
            require(payload==json.loads((SOURCE/'checks'/(name+'.json')).read_text()),'historical payload mismatch')
            record['payload']=payload
        runs.append(record)
        print(name,result.returncode,round(elapsed,3),flush=True)
    require((OUT/'normal.stdout').read_bytes()==(OUT/'optimized.stdout').read_bytes(),'mode output mismatch')
    receipt={'schema':'arithmetic-endpoint-intake-replay-v1','created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'python_version':sys.version,'checker_sha256':expected,'raw_manifest_entries_verified':len(checked),'raw_manifest_files':checked,'inherited_gamma_entries_verified':len(inherited_checked),'inherited_gamma_files':inherited_checked,'inherited_gamma_tests_executed_this_replay':False,'patch_added_files':len(patch_members),'patch_byte_exact':True,'patch_members':patch_members,'runs':runs,'normal_optimized_payload_bytes_equal':True,'arithmetic_analytic_inequalities_certified_by_tests':False,'lean_executed':False,'original_sources_modified':False}
    (OUT/'REPLAY.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
    print('receipt',OUT/'REPLAY.json',flush=True)

if __name__=='__main__':
    main()
