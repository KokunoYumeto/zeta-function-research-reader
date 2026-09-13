"""Sequential immutable-source replay and complete finite byte audit."""
from pathlib import Path
import hashlib,json,os,subprocess,sys,time

WORK=Path(__file__).resolve().parent
R=WORK.parent/'output'/'split_zero_rh_tandem_2026-09-12'
RAW=R/'sources'/'web_endpoint_restriction_delivery'/'Tau_Endpoint_Restriction_Control'
OUT=WORK/'endpoint_restriction_replay_20260913'
def sha(x):return hashlib.sha256(x).hexdigest()
def require(c,m):
    if not c:raise RuntimeError(m)

def main():
    OUT.mkdir(exist_ok=True)
    listed=json.loads((RAW/'MANIFEST.sha256.json').read_text())
    for n,v in listed.items():
        d=(RAW/n).read_bytes();require(len(d)==v['bytes'] and sha(d)==v['sha256'],'raw byte mismatch '+n)
    inherited=json.loads((RAW/'checks/inherited_manifest.json').read_text())
    old=R/'sources/web_arithmetic_endpoint_delivery/Tau_Arithmetic_Endpoint_Bounds'
    for v in inherited['files']:
        d=(old/v['path']).read_bytes();require(len(d)==v['bytes'] and sha(d)==v['sha256'],'inherited byte mismatch')
    lines=(RAW/'INTEGRATION.patch').read_bytes().splitlines(keepends=True);pos=0;patch=[]
    while pos<len(lines):
        if not lines[pos].startswith(b'diff --git '):pos+=1;continue
        first=pos;pos+=1
        while pos<len(lines) and not lines[pos].startswith(b'diff --git '):pos+=1
        part=lines[first:pos];require(b'new file mode 100644\n' in part,'patch changes existing file')
        n=next(t for t in part if t.startswith(b'+++ b/'))[6:].rstrip(b'\r\n').decode()
        require(n.startswith('workbenches/tau-endpoint-restriction-control/'),'patch prefix')
        rel=n.split('/',2)[2];start=next(i for i,t in enumerate(part) if t.startswith(b'@@'));body=[]
        for t in part[start+1:]:
            if t.startswith(b'+'):body.append(t[1:])
            elif t==b'\\ No newline at end of file\n':
                require(body and body[-1].endswith(b'\n'),'invalid newline marker');body[-1]=body[-1][:-1]
            else:raise RuntimeError('non-addition hunk')
        d=b''.join(body);require(d==(RAW/rel).read_bytes(),'patch bytes '+rel)
        patch.append({'path':n,'bytes':len(d),'sha256':sha(d)})
    env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1','PYTHONHASHSEED':'0','OMP_NUM_THREADS':'1','OPENBLAS_NUM_THREADS':'1','MKL_NUM_THREADS':'1'}
    checker=RAW/'check_restriction_control.py';supp=WORK/'endpoint_restriction_calibration_check_20260913.py'
    jobs=[]
    for mode,flags in [('normal',[]),('optimized',['-O'])]:
        jobs += [(mode,flags,checker,['--json',str(OUT/(mode+'.json'))],0),
                 ('startup-'+mode,flags,checker,['--inject-failure'],1),
                 ('calibration-'+mode,flags,supp,['--source-checker',str(checker),'--json',str(OUT/('calibration-'+mode+'.json'))],0)]
    records=[]
    for label,flags,script,args,code in jobs:
        start=time.monotonic();p=subprocess.run([sys.executable,*flags,str(script),*args],cwd=OUT,env=env,capture_output=True,timeout=180)
        (OUT/(label+'.stdout')).write_bytes(p.stdout);(OUT/(label+'.stderr')).write_bytes(p.stderr)
        require(p.returncode==code,'unexpected exit '+label)
        record={'label':label,'script_name':script.name,'script_sha256':sha(script.read_bytes()),'optimized':bool(flags),'returncode':p.returncode,'seconds':time.monotonic()-start,'stdout_sha256':sha(p.stdout),'stderr_sha256':sha(p.stderr)}
        if label.startswith('startup'):
            require(b'intentional negative control' in p.stderr and b'Ran 19 tests' not in p.stderr,'wrong startup guard')
            record.update({'test_methods_executed':0,'mathematical_mutant':False})
        elif label.startswith('calibration'):
            payload=json.loads((OUT/(label+'.json')).read_text());require(payload['status']=='PASS' and payload['strict_threshold_verified'],'calibration failure')
            record['payload_sha256']=sha((OUT/(label+'.json')).read_bytes())
        else:
            payload=json.loads((OUT/(label+'.json')).read_text());require(payload==json.loads((RAW/'checks'/('normal.json')).read_text()),'original successful result differs')
            require(payload['tests_run']==19 and payload['passed'] and payload['errors']==payload['failures']==0,'suite failed')
            record['payload']=payload
        records.append(record);print(label,p.returncode,round(record['seconds'],3),flush=True)
    for stem in ['', 'calibration-']:
        require((OUT/(stem+'normal.json')).read_bytes()==(OUT/(stem+'optimized.json')).read_bytes(),'mode payload mismatch')
    receipt={'schema':'endpoint-restriction-intake-replay-v1','python':sys.version,'raw_manifest_entries_verified':len(listed),'inherited_manifest_entries_byte_verified':len(inherited['files']),'inherited_tests_executed_this_replay':False,'patch_additions':patch,'patch_byte_exact':True,'originals_modified':False,'current_gamma_cut_modified':False,'runs':records,'new_raw_methods_per_successful_mode':19,'startup_controls_test_methods':0,'mathematical_mutants':0,'both_payload_pairs_identical':True}
    (OUT/'REPLAY.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8');print('receipt',OUT/'REPLAY.json')

if __name__=='__main__':main()
