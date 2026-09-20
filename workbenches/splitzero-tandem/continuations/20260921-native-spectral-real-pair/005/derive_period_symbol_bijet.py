"""Exact original centred factor jets on the real-unit phase, no sampled roots."""
from pathlib import Path
import sympy as s,json,itertools
B=Path(__file__).resolve().parent
beta,eta,zeta=s.symbols('beta eta zeta')
phi=zeta**4+zeta**3+zeta**2+zeta+1
loc={'beta':beta,'eta':eta,'zeta':zeta}
parse=lambda x:s.sympify(x,locals=loc)
def red(x):return s.rem(s.Poly(s.expand(x),zeta),s.Poly(phi,zeta)).as_expr()
def mr(M):return M.applyfunc(red)
data=json.loads((B/'ORIGINAL_PERIOD_JETS.json').read_text(encoding='utf-8'))
R=[s.Matrix([[parse(x) for x in row] for row in rr]) for rr in data['R_coefficients']]
N=2
Ri=[R[0].inv()]
for n in range(1,N+1):Ri.append(s.expand(-Ri[0]*sum((R[k]*Ri[n-k] for k in range(1,n+1)),s.zeros(4))))
Q=s.Matrix([[0,0,1,0],[0,-1,0,beta],[1,0,-beta,0],[0,beta,0,eta-beta**2]])
out={'scope':'[xi^k z^n] of exp(-xi) f_j(xi,z)/(4i delta gamma) at chi=0. Original common nonzero real unit cancels in the conjugation.','factors':[]}
for j in range(1,5):
    D=s.diag(*[zeta**((-j*a)%5) for a in range(1,5)])
    T=[mr(sum((Ri[l]*D*R[n-l] for l in range(n+1)),s.zeros(4))) for n in range(N+1)]
    cs={}
    for k in range(4):
        for n in range(N+1):
            c=red(sum((T[l][:,a].T*Q*T[n-l][:,k-a])[0]/(s.factorial(a)*s.factorial(k-a))
                      for a in range(k+1) for l in range(n+1)))
            cs[f'{k},{n}']=str(s.factor(c))
    out['factors'].append({'j':j,'coefficients':cs})
    print('j',j,'leading', {k:v for k,v in cs.items() if k in ['0,2','1,1','2,0','3,0']},flush=True)
L=[parse(f['coefficients']['0,2']) for f in out['factors']]
M=[parse(f['coefficients']['1,1']) for f in out['factors']]
G=[]
for k in range(4):
    c=0
    for inds in itertools.combinations(range(4),k):
        c+=s.prod(M[j] if j in inds else L[j] for j in range(4))
    G.append(s.factor(red(c)))
print('Product coefficients xi^k z^(8-k) after (4i delta gamma)^4:',G,flush=True)
out['product_leading']=[str(c) for c in G]
inv=[1/G[0]]
for k in range(1,4):inv.append(s.factor(-sum(G[l]*inv[k-l] for l in range(1,k+1))/G[0]))
print('Reciprocal coefficients xi^k z^(-8-k):',inv,flush=True)
out['reciprocal_leading']=[str(c) for c in inv]
(B/'ORIGINAL_PERIOD_SYMBOL_BIJET.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
