"""Reprepare a copied reader using retained local sources only."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess,sys
ROOT=Path(__file__).resolve().parent
DEST=ROOT/'verification'/'portable_prepare'
DEST.mkdir(parents=True,exist_ok=True)
for name in ['prepare_reader.py','SOURCE_DEPENDENCIES.json','EXTRA_DEPENDENCIES.json','DISPLAY_REFLOWS.json']:
    shutil.copyfile(ROOT/name,DEST/name)
shutil.copytree(ROOT/'originals',DEST/'originals',dirs_exist_ok=True)
# Deliberately create no sibling source_snapshot or other external dependency tree.
run=subprocess.run([sys.executable,str(DEST/'prepare_reader.py')],cwd=DEST,
    stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
assert run.returncode==0,run.stdout.decode(errors='replace')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
main=json.loads((ROOT/'SOURCE_MANIFEST.json').read_text())
copied=json.loads((DEST/'SOURCE_MANIFEST.json').read_text())
assert main['order']==copied['order']
assert main['main_sha256']==copied['main_sha256']
checks=[]
for original,clone in zip(main['files'],copied['files']):
    assert original['key']==clone['key']
    assert original['sha256']==clone['sha256']
    assert original['body_sha256']==clone['body_sha256']
    checks.append({'key':original['key'],'original_sha256':original['sha256'],'prepared_sha256':original['body_sha256']})
receipt={'utc':datetime.now(timezone.utc).isoformat(),'local_originals_only':True,
 'no_sibling_source_snapshot':not (DEST.parent/'source_snapshot').exists(),
 'main_sha256':main['main_sha256'],'all_source_bodies_identical':True,
 'source_count':len(checks),'checks':checks,
 'scope':'Preparation replay from copied local originals/configuration; compiler closure separately verified by actual FLS membership'}
(ROOT/'PORTABLE_PREPARE_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'source_count':len(checks),'all_source_bodies_identical':True}))
