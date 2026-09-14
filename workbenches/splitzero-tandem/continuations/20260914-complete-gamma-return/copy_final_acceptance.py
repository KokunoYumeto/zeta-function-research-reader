"""Copy the final proof authorities, continuation prompt and durable workflow."""
from pathlib import Path
import hashlib, json, shutil
BASE = Path(__file__).resolve().parent
ROOT = Path(r'C:\Users\Floris\Documents\math\work\backpropagation_20260913\root')
FH = ROOT/'joint_schur_intake/future_hankel'
NB = ROOT/'joint_schur_intake/next_bulk_density'
def pin(p): return {'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
def require(v,msg):
    if not v: raise RuntimeError(msg)
records=[]
def copy(src,rel,expected=None):
    before=pin(src)
    if expected: require(before['sha256']==expected,'Final source pin differs: '+str(src))
    dst=BASE/rel; dst.parent.mkdir(parents=True,exist_ok=True)
    require(not dst.exists(),'Preserve existing final copy: '+str(dst))
    shutil.copy2(src,dst)
    require(src.read_bytes()==dst.read_bytes() and before==pin(src)==pin(dst),'Copy changed')
    records.append({'source':str(src),'destination':rel,**before,'byte_exact':True})
proofs=json.loads((BASE/'FINAL_PROOF_PINS.json').read_text())['proofs']
for name,r in proofs.items():
    src=Path(r['path']); original=BASE/'originals'/r['original_filename']
    require(pin(src)['sha256']==r['sha256'] and src.read_bytes()==original.read_bytes(),'Final proof changed: '+name)
for name,expected in [
 ('FINAL_PROOF_RECEIPT.json','dcf5043dbdcd7049b2bef8800f3595c3442f895492b9b9b0e48a298557ed1977'),
 ('PARITY_TODA_INDEPENDENT_REVIEW.md','662dd547a4013607c5d4818a103819f6f01fec96d38af731915e9aabb7653cd8'),
 ('CONTIGUOUS_INDEPENDENT_REVIEW.md',None),
 ('CONTIGUOUS_EXACT_CHECK.json',None),
 ('check_contiguous_exact.py',None),
 ('low_endpoint_review/REVIEW.md','ec37eb7ee5bc23e785c11f76509fac3f80e516efaa176d6ac6173e8e86839b83'),
 ('low_endpoint_review/RECEIPT.json',None),
]: copy(FH/name,'provenance/proof_acceptance/'+name,expected)
copy(NB/'future_hankel/CONTINUE_COMPLETE_GAMMA_RETURN.md','00_CONTINUE_THE_PROGRAMME.md')
copy(ROOT/'CURRENT_RESEARCH_WORKFLOW_4000_CHARS.md','CURRENT_RESEARCH_WORKFLOW_4000_CHARS.md')
workflow=(BASE/'CURRENT_RESEARCH_WORKFLOW_4000_CHARS.md').read_text(encoding='utf8')
require(len(workflow)==4000,'Durable workflow character count differs')
(BASE/'provenance/FINAL_AUTHORITY_COPY_RECEIPT.json').write_text(json.dumps({'status':'Final author source pins and exact authority/prompt/workflow copies verified','workflow_characters':len(workflow),'workflow_role':'Current durable workflow; no goal-tool status or wording change claimed','records':records},indent=2)+'\n',encoding='utf8')
print(json.dumps({'copied':len(records),'workflow_characters':len(workflow),'receipt':pin(BASE/'provenance/FINAL_AUTHORITY_COPY_RECEIPT.json')}))
