"""Exact Taylor coefficients of the original period factors at inverse period zero."""
from pathlib import Path
import sympy as s,json
B=Path(__file__).resolve().parent
beta,eta,zeta=s.symbols('beta eta zeta')
phi=zeta**4+zeta**3+zeta**2+zeta+1
def red(x):return s.rem(s.Poly(s.expand(x),zeta),s.Poly(phi,zeta)).as_expr()
def mr(M):return M.applyfunc(red)
def Rn(n):
    out=s.zeros(4)
    for a in range(1,5):
        for r in range(4):
            total=5*n+r+1-a
            if total<0:continue
            for h in range(total//4+1):
                p2=total-4*h
                if p2%2:continue
                p=p2//2;L=p+h-n
                assert L>=0
                out[a-1,r]+=beta**p*eta**h/(3**p*s.factorial(p)*s.factorial(h))*(-1)**L*5**L*s.rf(s.Rational(a,5),L)
    return out
N=4
R=[Rn(n) for n in range(N+1)]
Ri=[R[0].inv()]
for n in range(1,N+1):Ri.append(s.expand(-Ri[0]*sum((R[k]*Ri[n-k] for k in range(1,n+1)),s.zeros(4))))
Q=s.Matrix([[0,0,1,0],[0,-1,0,beta],[1,0,-beta,0],[0,beta,0,eta-beta**2]])
out={'R_coefficients':[[[str(x) for x in row] for row in r.tolist()] for r in R],
 'scope':'Real nonzero unit a: scalar unit factors cancel exactly in the original conjugated operator; f_j(0,z)=4i delta gamma times the coefficients below. Inverse period z=0 is a coefficient boundary, not a finite period.', 'factors':[]}
e0=s.Matrix([1,0,0,0])
for j in range(1,5):
    D=s.diag(*[zeta**((-j*a)%5) for a in range(1,5)])
    vv=[mr(sum((Ri[l]*D*R[n-l]*e0 for l in range(n+1)),s.zeros(4,1))) for n in range(N+1)]
    coeff=[red(sum((vv[l].T*Q*vv[n-l])[0] for l in range(n+1))) for n in range(N+1)]
    coeff=[s.factor(q) for q in coeff]
    print('factor',j,'coefficients',coeff,flush=True)
    out['factors'].append({'j':j,'coefficients':[str(c) for c in coeff]})
(B/'ORIGINAL_PERIOD_JETS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
