"""Exact finite checks of BK local unit maps, not substitutes for analytic proofs."""
import json
from pathlib import Path
import sympy as S

z = S.Symbol('z')
a = 1+2*z+z**2
u = 2-z+3*z**2
rows=[]
checks=0

def require(condition, message):
    global checks
    checks += 1
    if not condition:
        raise RuntimeError(message)

def trunc(expr, depth):
    if depth == 0:
        return S.Integer(0)
    return S.series(expr,z,0,depth).removeO().expand()

for n in range(7):
    for m in range(7):
        source=[z**j for j in range(max(n-m,0),n)]
        target=[z**j for j in range(max(m-n,0),m)]
        images=[trunc((u/a)*z**(m-n)*v,m) for v in source]
        back=[trunc((a/u)*z**(n-m)*w,n) for w in target]
        require(len(source)==min(n,m)==len(target),f'dimensions {n,m}')
        for v,w in zip(source,images):
            require(trunc((a/u)*z**(n-m)*w,n)==v,f'left inverse {n,m,v}')
            require(trunc(a*z**n*w,m)==0,f'target kernel {n,m,v}')
        for w,v in zip(target,back):
            require(trunc((u/a)*z**(m-n)*v,m)==w,f'right inverse {n,m,w}')
            require(trunc(u*z**m*v,n)==0,f'source kernel {n,m,w}')
        matrix=S.Matrix([[w.coeff(z,j) for w in images] for j in range(max(m-n,0),m)])
        rank=matrix.rank() if source else 0
        require(rank==min(n,m),f'rank {n,m}')
        rows.append({'ord_h':n,'ord_g':m,'rank':rank,'source_dim':len(source),'target_dim':len(target)})

c0,c1,s=S.symbols('c0 c1 s')
mel=(s-1)*(c0+c1*(s-1))
H=2*S.pi**(s/2)*mel/(s*(s-1)*S.gamma(s/2))
require(S.limit(H,s,1)==2*c0,'rho=1 H endpoint factor')
require(S.limit(mel/(s-1),s,1)==c0,'rho=1 source moment')
rho,d=S.symbols('rho d')
lam=1-rho
require(S.expand(-(1-d-rho)-(d-lam))==0,'Fourier inverse sign')

report={'checks_passed':checks,'guards':'explicit conditional RuntimeError; active under python -O',
        'local_units':{'a':str(a),'u':str(u)},'local_cases':rows,
        'scope':'Exact BK.15-16 unit/power maps and source endpoint/sign checks. Analytic claims have written proofs.'}
Path(__file__).with_name('CHECKS.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'checks_passed':checks,'local_cases':len(rows),'guards':report['guards']}))
