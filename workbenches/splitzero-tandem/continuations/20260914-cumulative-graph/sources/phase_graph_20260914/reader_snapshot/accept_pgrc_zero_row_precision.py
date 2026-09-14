"""Retain the preceding candidate while accepting the zero-row prose correction."""
from pathlib import Path
import hashlib,json,shutil
ROOT=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
pdf=ROOT/'Phase_Graph_Mixed_Residual_Reader.pdf';oldpin=sha(pdf)
hist=ROOT/'history'/('candidate_'+oldpin[:16]);hist.mkdir(parents=True,exist_ok=True)
names=['Phase_Graph_Mixed_Residual_Reader.pdf','BUILD_RECEIPT.json','SOURCE_MANIFEST.json',
 'EXTRA_DEPENDENCIES.json','originals/PGRC.tex','tex/bodies/PGRC.tex','tex/main.tex']
preserved=[]
for name in names:
    p=ROOT/name;dest=hist/name;dest.parent.mkdir(parents=True,exist_ok=True)
    shutil.copyfile(p,dest);assert sha(p)==sha(dest)
    preserved.append({'path':name,'sha256':sha(p),'bytes':p.stat().st_size})
source=ROOT.parent/'relation_tail_control/relation_row_correlations.tex'
pin='cf96278c08ca55de3622eeb09235b51e4476219b187f913a92bc1ee4ec85a699'
assert sha(source)==pin
extra_path=ROOT/'EXTRA_DEPENDENCIES.json';extra=json.loads(extra_path.read_text())
for e in extra['files']:
    if e['key']=='PGRC':e['path']=str(source);e['sha256']=pin
extra_path.write_text(json.dumps(extra,indent=2)+'\n')
shutil.copyfile(source,ROOT/'originals/PGRC.tex')
(hist/'PRESERVED.json').write_text(json.dumps({'pdf_sha256':oldpin,'files':preserved,
 'reason':'PGRC15 prose retains zero rows by using nonnegative for the first inverse quadratic value; every equation unchanged'},indent=2)+'\n')
print(json.dumps({'historical_candidate':str(hist),'pgrc_sha256':pin}))
