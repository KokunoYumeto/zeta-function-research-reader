"""Exact phase, moment and weighted cofactor identities for FPZ15--24."""
from pathlib import Path
import hashlib,json
import sympy as s
B=Path(__file__).resolve().parent
t=s.symbols('t');m0,m1,m2,m3=s.symbols('m0:4')
omega=-s.I*t+s.I*t**3/3
g=s.series(s.exp(-4*omega)*(m0+m1*omega+m2*omega**2/2+m3*omega**3/6),t,0,4).removeO().expand()
expected=[m0,-s.I*(m1-4*m0),-m2/2+4*m1-8*m0,
          s.I*(m3/6-2*m2+s.Rational(25,3)*m1-12*m0)]
checks=[]
for j in range(4):
    assert s.expand(g.coeff(t,j)-expected[j])==0
    checks.append('full original Cayley coefficient '+str(j))
for D in range(1,5):
    gs=s.symbols('g0:'+str(D+1));rs=(s.Integer(1),)+s.symbols('r1:'+str(D+1),nonzero=True)
    A=s.Matrix(D+1,D+1,lambda i,j:gs[j-i]*rs[j]/rs[i] if j>=i else 0)
    assert s.factor(A.det()-gs[0]**(D+1))==0
    Astar=A.subs(gs[0],0)
    C=Astar[:D,1:]
    assert s.factor(C.det()-gs[1]**D*rs[D])==0
    # This adjugate is the complete leading inverse numerator at the zero.
    target=s.zeros(D+1);target[0,D]=(-gs[1])**D*rs[D]
    assert (Astar.adjugate()-target).applyfunc(s.factor)==s.zeros(D+1)
    checks.extend(['weighted determinant D='+str(D),'rank minor D='+str(D),'complete adjugate D='+str(D)])
u,us=s.symbols('u us',nonzero=True)
assert s.factor(1/u-1/us+(u-us)/(u*us))==0
checks.append('exact original-period conversion')
out={'status':'PASS','exact_identities':len(checks),'checks':checks,
     'proof_sha256':hashlib.sha256((B/'FINITE_PERIOD_ZERO_BODY.tex').read_bytes()).hexdigest(),
     'scope':'Exact symbolic phase and weighted-cofactor checks supplement the complete all-degree proof. The independent full-series ball certificate proves the finite point.'}
(B/'FINITE_PERIOD_RETURN_CHECK.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
