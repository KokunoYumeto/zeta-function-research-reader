"""Exact coefficient polynomials after an explicitly restored phase-coordinate map."""
from pathlib import Path
import json
import sympy as s
HERE=Path(__file__).resolve().parent
x,y,q=s.symbols('x y q')
phi=1+q+q**2+q**3+q**4

def red(v):
    return s.rem(s.expand(v),phi,q)

def Rn(n):
    out=s.zeros(4)
    for a in range(1,5):
        for r in range(4):
            total=5*n+r+1-a
            for h in range(max(-1,total//4)+1):
                if (total-4*h)%2: continue
                p=(total-4*h)//2; L=p+h-n
                out[a-1,r]+=x**h/(3**p*s.factorial(p)*s.factorial(h))*(-1)**L*5**L*s.rf(s.Rational(a,5),L)
    return out

R=[Rn(n) for n in range(5)]
Ri=[R[0].inv()]
for n in range(1,5):Ri.append(s.expand(-Ri[0]*sum((R[a]*Ri[n-a] for a in range(1,n+1)),s.zeros(4))))
D=s.diag(q,q**2,q**3,q**4)
G=[sum((Ri[a]*D*R[n-a] for a in range(n+1)),s.zeros(4)).applyfunc(red) for n in range(5)]
T=s.Matrix([[0,0,0,-x],[1,0,0,0],[0,1,0,-1],[0,0,1,0]])
Q=s.Matrix([[0,0,1,0],[0,-1,0,1],[1,0,-1,0],[0,1,0,x-1]])
W=y*s.eye(4)+T**2
Wbar=(y-1)*s.eye(4)-T**2
e0=s.eye(4)[:,0]
v=[(Wbar*gn*W*e0).applyfunc(red) for gn in G]
coeff={n:s.factor(red(sum((v[a].dot(Q*v[n-a]) for a in range(n+1)),s.S.Zero))) for n in [0,2,4]}
out={'coordinate_map':'x=eta/beta^2; p=alpha+beta*chi/(2k), b=beta*chi/k, k=2delta gamma; y=p/b is used only when b is nonzero. Full coefficients are 4i delta gamma beta^(5n/2-1) times b^4 times the coefficient polynomial divided by (alpha^2+chi^2)^2, for positive even n. Endpoint b=0 is evaluated by the homogeneous quartic coefficient.',
     'polynomials':{str(n):str(p) for n,p in coeff.items()},'coefficients':{},'real_equations':{},'resultants':{}}
for n,p in coeff.items():
    out['coefficients'][str(n)]=[str(s.factor(s.expand(p).coeff(y,r))) for r in range(5)]
    print('computed coefficient',n,flush=True)
    if n!=2:continue
    A=[s.expand(p).coeff(q,r) for r in range(4)]
    rt=s.sqrt(5)
    pairs=[(4*A[0]+(rt-1)*A[1]-(rt+1)*(A[2]+A[3]),2*A[1]+(rt-1)*(A[2]-A[3])),
           (4*A[0]-(rt+1)*A[1]+(rt-1)*(A[2]+A[3]),(rt-1)*A[1]-2*A[2]+2*A[3])]
    for j,(P,J) in enumerate(pairs,1):
        P=s.factor(P,extension=rt);J=s.factor(J,extension=rt)
        out['real_equations'][str(j)]=[str(P),str(J)]
        print('pair',j,'real equations',P,J,flush=True)
        resultant=s.factor(s.resultant(P,J,y),extension=rt)
        out['resultants'][str(j)]=str(resultant)
        print('pair',j,'resultant',resultant,flush=True)
(HERE/'ARBITRARY_UNIT_COEFFICIENT_DERIVATION.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
