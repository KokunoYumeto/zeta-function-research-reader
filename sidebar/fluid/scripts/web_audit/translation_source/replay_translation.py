"""Exact translation identities; original expressions stored before cancellation."""
from pathlib import Path
import sympy as S
import json,hashlib,sys
R=Path(__file__).resolve().parent
t=S.symbols('t',real=True)
x=S.symbols('x1:4',real=True)
d=[S.Function('d'+str(j))(t) for j in range(3)]
# Independent polynomial jets avoid a CAS ambiguity in substituting a moving
# coordinate inside an unevaluated partial-time Derivative. The written proof
# above is for arbitrary smooth fields, not just these finite replay fixtures.
basis=[1,t,t*t,*x,t*x[0],x[0]*x[1],x[1]*x[2],x[2]*x[0],x[0]*x[1]*x[2]]
a=S.symbols('a0:33')
u=[sum(a[11*i+j]*basis[j] for j in range(11)) for i in range(3)]
p=x[0]*x[1]*x[2]+t*x[0]+t*t*x[2]
nu=S.symbols('nu',nonnegative=True)
def shift(expr,sign):return expr.subs(dict(zip(x,[x[j]+sign*d[j] for j in range(3)])),simultaneous=True)
def residual(v,q):
 return [S.diff(v[i],t)+sum(v[j]*S.diff(v[i],x[j]) for j in range(3))+S.diff(q,x[i])-nu*sum(S.diff(v[i],z,2) for z in x) for i in range(3)]
original=residual(u,p)
checks=[]
def check(label,left,right):
 delta=S.expand((left-right).doit())
 if delta!=0:delta=S.simplify(delta)
 assert delta==0,(label,delta)
 checks.append({'label':label,'left':str(left),'right':str(right),'exact_expanded_difference':str(delta)})
translated=[shift(v,-1) for v in u]
tr=residual(translated,shift(p,-1))
for i in range(3):
 check('translated residual '+str(i+1),tr[i],shift(original[i],-1)-sum(S.diff(d[j],t)*S.diff(translated[i],x[j]) for j in range(3)))
frame=[shift(u[i],1)-S.diff(d[i],t) for i in range(3)]
fr=residual(frame,shift(p,1))
for i in range(3):check('moving frame residual '+str(i+1),fr[i],shift(original[i],1)-S.diff(d[i],t,2))
check('translation divergence',sum(S.diff(translated[i],x[i]) for i in range(3)),shift(sum(S.diff(u[i],x[i]) for i in range(3)),-1))
check('moving frame divergence',sum(S.diff(frame[i],x[i]) for i in range(3)),shift(sum(S.diff(u[i],x[i]) for i in range(3)),1))
C,lam,T,t0,zc0=S.symbols('C lam T t0 zc0',real=True)
tau=S.symbols('tau',positive=True)
check('source centre primitive nonzero lambda, T-t=tau>0',S.diff(zc0+C/lam*((T-t)**lam-(T-t0)**lam),t).subs(T,t+tau),-C*tau**(lam-1))
check('source centre primitive zero lambda',S.diff(zc0+C*S.log((T-t)/(T-t0)),t),-C/(T-t))
Us,Ls,ts,s,beta=S.symbols('Us Ls ts s beta',positive=True)
drift=-Us/Ls/s*(-C*ts**(beta-1)*s**(beta-1))
check('retained moving profile drift',S.expand_power_base(drift,force=False),S.expand_power_base(Us/ts*s**(beta-2)*(C*ts**beta/Ls),force=False))
out={'scope':'Exact finite polynomial-jet checks of coordinate translation, frame residual, divergence and retained drift; coefficients and time-dependent centre are retained. General smooth-field maps and proofs are in source_corrections.tex. No source-profile existence theorem.',
 'python':sys.version,'sympy':S.__version__,'count':len(checks),'all_passed':True,'checks':checks,
 'proof_sha256':hashlib.sha256((R/'source_corrections.tex').read_bytes()).hexdigest(),
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(R/'translation_receipt.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(str(len(checks))+' exact retained-translation checks passed')
