"""Preserve the prior complete candidate and import the final whole ACM body."""
from pathlib import Path
import hashlib,json,shutil
ROOT=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
pdf=ROOT/'Phase_Graph_Mixed_Residual_Reader.pdf';oldpin=sha(pdf)
hist=ROOT/'history'/('candidate_'+oldpin[:16]);hist.mkdir(parents=True,exist_ok=True)
names=['Phase_Graph_Mixed_Residual_Reader.pdf','BUILD_RECEIPT.json','SOURCE_MANIFEST.json',
 'SOURCE_TRANSPORT_VERIFICATION.json','PORTABLE_PREPARE_RECEIPT.json','EXTRA_DEPENDENCIES.json',
 'originals/ACM.tex','tex/bodies/ACM.tex','tex/main.tex']
preserved=[]
for name in names:
    p=ROOT/name;dest=hist/name;dest.parent.mkdir(parents=True,exist_ok=True)
    shutil.copyfile(p,dest);assert sha(p)==sha(dest)
    preserved.append({'path':name,'sha256':sha(p),'bytes':p.stat().st_size})
source=ROOT.parent/'relation_tail_control/backprop/replacement/ACM.tex'
pin='d37d83fa1d655b99559fbeeb62b2aa6b93bb1554fc4e050d30efac8a9dae831a'
assert sha(source)==pin
extra_path=ROOT/'EXTRA_DEPENDENCIES.json';extra=json.loads(extra_path.read_text())
for e in extra['files']:
    if e['key']=='ACM':e['path']=str(source);e['sha256']=pin
extra_path.write_text(json.dumps(extra,indent=2)+'\n')
shutil.copyfile(source,ROOT/'originals/ACM.tex')
(hist/'PRESERVED.json').write_text(json.dumps({'pdf_sha256':oldpin,'files':preserved,
 'reason':'Complete subsequent precision correction: zero-possible row value nonnegative; explicit subset permutation map and inverse'},indent=2)+'\n')
print(json.dumps({'historical_candidate':str(hist),'acm_sha256':pin}))
