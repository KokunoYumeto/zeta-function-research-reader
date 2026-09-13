from pathlib import Path
import subprocess,sys,json,hashlib,datetime,re
W=Path(__file__).resolve().parent
SRC=W.parent/'output/split_zero_rh_tandem_2026-09-12/sources/web_relation_moment_delivery/Tau_Relation_Moment_Control'
OUT=W/'relation_moment_replay_20260913';OUT.mkdir(exist_ok=True)
sha=lambda b:hashlib.sha256(b).hexdigest()
manifest=json.loads((SRC/'MANIFEST.sha256.json').read_text())
for name,row in manifest.items():
 b=(SRC/name).read_bytes()
 if len(b)!=row['bytes'] or sha(b)!=row['sha256']:raise RuntimeError('manifest mismatch '+name)
# Parse every add-only hunk and compare its complete reconstructed payload.
patch=(SRC/'INTEGRATION.patch').read_bytes().decode('utf-8').splitlines(keepends=True)
targets=[];current=None;payload=[]
def finish():
 if current is not None:
  b=''.join(payload).encode();name=current.rsplit('/',1)[-1]
  if b!=(SRC/name).read_bytes():raise RuntimeError('patch payload differs '+name)
  targets.append({'path':current,'bytes':len(b),'sha256':sha(b)})
for line in patch:
 if line.startswith('diff --git '):finish();current=None;payload=[]
 elif line.startswith('+++ b/'):
  current=line[len('+++ b/'):].strip()
 elif line.startswith('--- '):
  if line.strip()!='--- /dev/null':raise RuntimeError('not add only')
 elif line.startswith('@@ '):
  if not re.match(r'@@ -0,0 \+1,\d+ @@',line):raise RuntimeError('unexpected hunk')
 elif current is not None and line.startswith('+'):payload.append(line[1:])
 elif current is not None and (line.startswith('-') or line.startswith(' ')):raise RuntimeError('unexpected non-add line')
finish()
jobs=[]
for mode,opt in [('normal',[]),('optimized',['-O'])]:
 for case,extra,expected in [('positive',['--json',str(OUT/(mode+'.json')),'--calibration',str(OUT/(mode+'-calibration.json'))],0),('omitted-cross-pairing',['--negative-control'],1)]:
  args=[sys.executable,'-B',*opt,str(SRC/'check_relation_moments.py'),*extra]
  before=datetime.datetime.now(datetime.timezone.utc).isoformat()
  p=subprocess.run(args,cwd=OUT,capture_output=True)
  prefix=mode+'-'+case
  for stream,b in [('stdout',p.stdout),('stderr',p.stderr)]: (OUT/(prefix+'.'+stream+'.log')).write_bytes(b)
  row={'mode':mode,'case':case,'argv':args,'started_utc':before,'exit_code':p.returncode,'expected_exit_code':expected,'passed':p.returncode==expected,'stdout_sha256':sha(p.stdout),'stderr_sha256':sha(p.stderr)}
  jobs.append(row)
  if p.returncode!=expected:raise RuntimeError(row)
  print(prefix+' passed',flush=True)
positive=[json.loads((OUT/(m+'.json')).read_text()) for m in ['normal','optimized']]
if positive[0]!=positive[1] or any(x['test_methods']!=22 or not x['passed'] for x in positive):raise RuntimeError('positive result scope mismatch')
if (OUT/'normal-calibration.json').read_bytes()!=(OUT/'optimized-calibration.json').read_bytes():raise RuntimeError('calibrations differ')
receipt={'schema':'relation-moment-actual-replay-v1','python':sys.version,'checker_sha256':sha((SRC/'check_relation_moments.py').read_bytes()),'source_manifest_entries':len(manifest),'all_source_manifest_entries_verified':True,'all_patch_payloads_verified':targets,'jobs':jobs,'normal_optimized_exact_payloads_equal':True,'methods_per_mode':22,'historical_restriction_19_methods_rerun':False}
(W/'relation_moment_replay_receipt_20260913.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':True,'methods_per_mode':22,'manifest_entries':len(manifest),'patch_files':len(targets)}))
