"""Repair the four concrete first-build layout findings reversibly."""
from pathlib import Path
import json,shutil,hashlib,re
BASE=Path(__file__).resolve().parent
def pin(p):return {'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
def require(v,msg):
    if not v:raise RuntimeError(msg)
hist=BASE/'history/first_build_a567ae6c';require(not hist.exists(),'Preserve previous build')
hist.mkdir(parents=True)
for rel in ['Complete_Gamma_Return.pdf','Complete_Gamma_Return.log','Complete_Gamma_Return.fls','BUILD_RECEIPT.json','SOURCE_TRANSPORTS.json','sources/LET.tex','sources/PHT.tex','sources/HCT.tex']:
    q=hist/rel;q.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(BASE/rel,q)
changes={
'LET':[(r'''\[
 \chi(S)=\prod_{a,b=0}^k
 [S-c-(2a-k)\delta-i(2b-k)\gamma]^e,\qquad
 f(S)=\prod_{j=0}^{l-1}(S-c-t_j),\quad t_j=2j+\tfrac12,
 \qquad \sigma(y)=\frac{|\Gamma(1/4+iy/2)|^2}{2\pi}.
 \tag{LET2}
\]''',r'''\[
\begin{gathered}
 \chi(S)=\prod_{a,b=0}^k
 [S-c-(2a-k)\delta-i(2b-k)\gamma]^e,\\
 f(S)=\prod_{j=0}^{l-1}(S-c-t_j),\quad t_j=2j+\tfrac12,
 \qquad \sigma(y)=\frac{|\Gamma(1/4+iy/2)|^2}{2\pi}.
\end{gathered}\tag{LET2}
\]'''),(r'\section{A scalar ratio transport retaining the degree \(l\)}',r'\section{A scalar ratio transport retaining the degree \texorpdfstring{\(l\)}{l}}')],
'PHT':[(r'measure, with norms $h_j=H_{j+1}^{(a)}(u)/H_j^{(a)}(u)$.',r'''measure, with norms
\[h_j=H_{j+1}^{(a)}(u)/H_j^{(a)}(u).\]''')],
'HCT':[(r'''Use column vectors $\mathbf P^{(a)}=(P_0^{(a)},P_1^{(a)},\ldots)^T$
as formal polynomial sequences.''',r'''Use column vectors
\[\mathbf P^{(a)}=(P_0^{(a)},P_1^{(a)},\ldots)^T\]
as formal polynomial sequences.''')]
}
report=[];trans=json.loads((BASE/'SOURCE_TRANSPORTS.json').read_text())
for name,ops in changes.items():
    p=BASE/'sources'/f'{name}.tex';s=p.read_text(encoding='utf8');before=s;beforepin=pin(p)
    for old,new in ops:
        require(s.count(old)==1,'Layout target differs: '+name);s=s.replace(old,new,1)
    recovered=s
    for old,new in reversed(ops):require(recovered.count(new)==1,'Reverse target differs');recovered=recovered.replace(new,old,1)
    require(recovered==before,'Complete fragment inverse differs')
    require(re.findall(r'\\tag\{([^}]+)\}',before)==re.findall(r'\\tag\{([^}]+)\}',s),'Equation tags changed')
    p.write_text(s,encoding='utf8');row={'name':name,'before':beforepin,'after':pin(p),'operations':[{'before':a,'after':b} for a,b in ops],'exact_complete_fragment_inverse':True};report.append(row)
    t=next(r for r in trans['proofs'] if r['name']==name);t['initial_fragment_pin']=t['fragment_pin'];t['fragment_pin']=pin(p);t['presentation_reflow']=row
(BASE/'PRESENTATION_REFLOW.json').write_text(json.dumps({'scope':'LET2 display, LET heading bookmark, PHT norm display and HCT vector display only','mathematical_changes':0,'repairs':report,'prior_build':'history/first_build_a567ae6c'},indent=2)+'\n',encoding='utf8')
(BASE/'SOURCE_TRANSPORTS.json').write_text(json.dumps(trans,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
print(json.dumps({'four_concrete_findings_repaired':True,'full_inverse_verified':True}))
