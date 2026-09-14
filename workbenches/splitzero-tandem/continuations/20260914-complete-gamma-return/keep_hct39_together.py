"""Repair only the observed page-14/15 split inside the HCT39 display."""
from pathlib import Path
import json,hashlib,shutil,re
BASE=Path(__file__).resolve().parent
def pin(p):return {'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
def require(v,msg):
    if not v:raise RuntimeError(msg)
require(pin(BASE/'Complete_Gamma_Return.pdf')['sha256']=='6d2b87de435099467570cdcce1a674e0e5e7658e9bf8fcc4b7c8c2b344ff6b06','Pre-repair PDF differs')
require((BASE/'qa/ACTUAL_VISUAL_REVIEW.json').exists(),'Need durable actual pre-repair page review')
hist=BASE/'history/pre_hct39_pagination_6d2b87de';require(not hist.exists(),'Keep prior build')
hist.mkdir(parents=True)
for rel in ['Complete_Gamma_Return.pdf','Complete_Gamma_Return.log','Complete_Gamma_Return.fls','BUILD_RECEIPT.json','SOURCE_TRANSPORTS.json','sources/HCT.tex']:
    dest=hist/rel;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(BASE/rel,dest)
shutil.copytree(BASE/'qa',hist/'qa')
p=BASE/'sources/HCT.tex';before=p.read_text(encoding='utf8');beforepin=pin(p)
old=r' +\log(1+\kappa_{n+1}^{(a+s)})\notag\\'
new=r' +\log(1+\kappa_{n+1}^{(a+s)})\notag\\*'
require(before.count(old)==1,'Exact HCT39 row occurrence differs')
after=before.replace(old,new,1)
require(after.replace(new,old,1)==before,'Full fragment inverse differs')
require(re.findall(r'\\tag\{([^}]+)\}',before)==re.findall(r'\\tag\{([^}]+)\}',after),'Tag set differs')
p.write_text(after,encoding='utf8')
row={'name':'HCT','before':beforepin,'after':pin(p),'operations':[{'before':old,'after':new}],'exact_complete_fragment_inverse':True,'scope':'Forbid the single page break inside HCT39; all mathematical tokens preserved'}
trans=json.loads((BASE/'SOURCE_TRANSPORTS.json').read_text())
t=next(r for r in trans['proofs'] if r['name']=='HCT');t['pre_pagination_fragment_pin']=t['fragment_pin'];t['fragment_pin']=pin(p);t['pagination_reflow']=row
(BASE/'SOURCE_TRANSPORTS.json').write_text(json.dumps(trans,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
(BASE/'HCT39_PAGINATION_REFLOW.json').write_text(json.dumps({'mathematical_changes':0,'repair':row,'prior_build':hist.relative_to(BASE).as_posix()},indent=2)+'\n',encoding='utf8')
print(json.dumps({'single_display_pagination_repaired':True,'full_inverse_verified':True}))
