#!/usr/bin/env python3
from pathlib import Path
import difflib,hashlib,json,subprocess,tempfile,zipfile
root=Path(__file__).resolve().parent
prefix=Path('workbenches/tau-sga-trace-period-control')
exclude={'INTEGRATION.patch','MANIFEST.json','checks/integration-validation.json'}
payload=[]
for p in sorted(root.rglob('*')):
 if not p.is_file() or '__pycache__' in p.parts:continue
 rel=p.relative_to(root).as_posix()
 if rel in exclude or p.suffix in {'.png','.pyc'} or p.stat().st_size==0:continue
 try:p.read_text(encoding='utf-8')
 except UnicodeDecodeError:continue
 payload.append(p)
chunks=[]
for p in payload:
 dest=(prefix/p.relative_to(root)).as_posix()
 lines=p.read_text(encoding='utf-8').splitlines(keepends=True)
 if lines and not lines[-1].endswith('\n'):
  # Keep byte-exact source and use the Git no-final-newline marker.
  lines[-1]+='\n';no_eol=True
 else:no_eol=False
 diff=list(difflib.unified_diff([],lines,fromfile='/dev/null',tofile='b/'+dest,n=3))
 if not diff:continue
 if no_eol:diff.append('\\ No newline at end of file\n')
 chunks.append('diff --git a/'+dest+' b/'+dest+'\nnew file mode 100644\n'+''.join(diff))
patch=root/'INTEGRATION.patch';patch.write_text(''.join(chunks))
with tempfile.TemporaryDirectory(prefix='tau-sga-patch-') as td:
 subprocess.run(['git','apply','--check',str(patch)],cwd=td,check=True,capture_output=True)
 subprocess.run(['git','apply',str(patch)],cwd=td,check=True,capture_output=True)
 for p in payload:
  out=Path(td)/prefix/p.relative_to(root)
  if out.read_bytes()!=p.read_bytes():raise RuntimeError('Patch byte mismatch: '+str(p))
record={'files_added':len(payload),'existing_files_modified':0,'local_apply_check':True,'applied_bytes_match':True,'remote_write':False,'prefix':str(prefix)}
(root/'checks'/'integration-validation.json').write_text(json.dumps(record,indent=2)+'\n')
rows=[]
for p in sorted(root.rglob('*')):
 if p.is_file() and p.name!='MANIFEST.json' and '__pycache__' not in p.parts:
  b=p.read_bytes();rows.append({'path':p.relative_to(root).as_posix(),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
(root/'MANIFEST.json').write_text(json.dumps({'algorithm':'sha256','entries':rows},indent=2)+'\n')
archive=root.parent/'Tau_SGA_Trace_Period_Control_2026-09-13.zip'
with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 for p in sorted(root.rglob('*')):
  if p.is_file() and '__pycache__' not in p.parts:z.write(p,root.name+'/'+p.relative_to(root).as_posix())
with zipfile.ZipFile(archive) as z:
 if z.testzip() is not None:raise RuntimeError('ZIP CRC failure')
 for row in rows:
  data=z.read(root.name+'/'+row['path'])
  if len(data)!=row['bytes'] or hashlib.sha256(data).hexdigest()!=row['sha256']:raise RuntimeError('ZIP manifest mismatch')
print(json.dumps({'archive':str(archive),'bytes':archive.stat().st_size,'manifest_entries':len(rows),'integration':record},indent=2))
