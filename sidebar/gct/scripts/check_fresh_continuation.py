"""Replay all authored proof inputs in a fresh tree without literature shelves.

This is an integration check for a completed mathematical checkpoint, not an
audit that the continuing research goal is complete. It is deliberately not
called recursively from reproduce.py.
"""
from pathlib import Path
import datetime, hashlib, json, shutil, subprocess, sys

ROOT=Path(__file__).resolve().parents[1]
stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%f')
DEST=ROOT/'build'/('fresh_continuation_'+stamp)
DEST.mkdir(parents=True,exist_ok=False)
excluded={'shelf','sources','source','build','qa','checkout','checkout_material',
          '__pycache__','.git','fresh_reproduction','publication'}
suffixes={'.tex','.bib','.py','.json','.md'}
copied=[]
for path in ROOT.rglob('*'):
    if not path.is_file() or path.suffix not in suffixes:
        continue
    relative=path.relative_to(ROOT)
    if any(part in excluded or part.startswith('fresh_continuation_') for part in relative.parts):
        continue
    target=DEST/relative
    target.parent.mkdir(parents=True,exist_ok=True)
    shutil.copyfile(path,target)
    copied.append({'path':relative.as_posix(),
                   'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
# build/combined.bib and the full inclusion fragment are rebuilt by reproduce.py.
run=subprocess.run([sys.executable,'-X','utf8',str(DEST/'scripts/reproduce.py')],
                   cwd=DEST,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
output=run.stdout.decode('utf-8',errors='replace')
(DEST/'replay_output.txt').write_text(output,encoding='utf-8')
receipt={'status':'passed' if run.returncode==0 else 'failed',
         'timestamp_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
         'tree':str(DEST),'copied_files':len(copied),'authored_inputs':copied,
         'source_shelves_copied':False,'exit_code':run.returncode,'output':output,
         'scope':'Fresh authored-input reproduction, not completion of the continuing research goal'}
if (DEST/'checks/reproduction.json').exists():
    receipt['reproduction']=json.loads((DEST/'checks/reproduction.json').read_text(encoding='utf-8'))
(ROOT/'checks/fresh_continuation.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
print(json.dumps({'status':receipt['status'],'copied_files':len(copied),
                  'exit_code':run.returncode,'tree':str(DEST)}))
if run.returncode:
    print(output[-8000:])
    raise SystemExit(run.returncode)
