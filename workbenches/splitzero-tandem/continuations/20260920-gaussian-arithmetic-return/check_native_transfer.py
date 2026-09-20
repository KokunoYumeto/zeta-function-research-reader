"""Exact finite identities and negative controls for NG6, NG18--23.
The finite measures test identities; they are not hypothetical zeta zeros.
"""
from pathlib import Path
import json, hashlib
import sympy as S
import numpy as np

P=Path(__file__).parent
checks=[]; controls=[]
def ck(name, condition):
    if not bool(condition): raise RuntimeError(name)
    checks.append(name)
def nc(name, rejected):
    if not bool(rejected): raise RuntimeError('Negative control failed: '+name)
    controls.append(name)

nodes=list(map(S.Integer,range(1,13)))
eta=[1+S.Rational(i%3,7) for i in range(12)]
ratios=[S.Rational(1+i%5,3) for i in range(12)]
lam=[w*r for w,r in zip(eta,ratios)]
ell=min(ratios); u=max(ratios); B=S.Integer(12)
def gram(xs,ws,n):
    moments=[sum(w*x**j for x,w in zip(xs,ws)) for j in range(2*n-1)]
    return S.Matrix(n,n,lambda i,j:moments[i+j])
for n in range(1,5):
 for a in [S.Integer(1),S.Integer(3)]:
    D={}
    for label,ws in [('l',lam),('e',eta)]:
        for t in [-2,-1,0,1,2]:
            D[label,t]=gram(nodes,[w*(x+a)**t for x,w in zip(nodes,ws)],n).det()
        coeff=-gram(nodes,ws,n).inv()*S.Matrix([sum(w*x**(n+j) for x,w in zip(nodes,ws)) for j in range(n)])
        val=abs((-a)**n+sum(coeff[j]*(-a)**j for j in range(n)))
        ck(f'NG7 Heine n={n},a={a},{label}',val==D[label,1]/D[label,0])
        for j in [-1,0,1]:
            ck(f'Convex integer slopes n={n},a={a},{label},j={j}',D[label,j]**2<=D[label,j-1]*D[label,j+1])
    pos=(D['l',2]/D['l',0])/(D['e',2]/D['e',0])
    ck(f'NG8 positive quotient n={n},a={a}',ell/u<=pos<=u/ell)
    neg=(D['l',0]/D['l',-2])/(D['e',0]/D['e',-2])
    width=(u/ell)*((a+B)**2/a**2)**2
    ck(f'NG9 rational quotient n={n},a={a}',1/width<=neg<=width)
    valratio=(D['l',1]/D['l',0])/(D['e',1]/D['e',0])
    bound=width*((a+B)/a)**3
    ck(f'NG6 characteristic comparison n={n},a={a}',1/bound<=valratio**2<=bound)
    for j in [-2,-1,0]:
        gap=(D['e',j+2]/D['e',j+1])/(D['e',j+1]/D['e',j])
        ck(f'Christoffel gap n={n},a={a},j={j}',1<=gap<=(a+B)/a)
nc('Equal characteristic values are not implied by comparable metrics',valratio!=1)

y=S.symbols('y')
Q=S.Poly(((y-3)**2+S.Rational(1,9))*((y+3)**2+S.Rational(1,9)),y)
q=Q.degree()
xs=list(map(S.Integer,range(-8,9)))
ws=[1+S.Rational(abs(int(x))%3,5) for x in xs]
def moment(j,relation=False):
    return sum(w*x**j*(Q.eval(x)**2 if relation else 1) for x,w in zip(xs,ws))
def polynomial_norm(n,relation=False):
    G=S.Matrix(n,n,lambda i,j:moment(i+j,relation))
    v=S.Matrix([moment(n+j,relation) for j in range(n)])
    return moment(2*n,relation)-(v.T*G.inv()*v)[0] if n else moment(0,relation)
for N in range(q-1,2*q+1):
    H=S.Matrix(N+1,N+1,lambda i,j:moment(i+j))
    Hy=S.Matrix(N+1,N+1,lambda i,j:moment(i+j+1))
    J=S.Matrix(q,N+1,lambda i,j:S.Poly(S.rem(y**j,Q.as_expr(),y),y).nth(i))
    G=(J*H.inv()*J.T).inv()
    L=H.inv()*J.T*G
    C=J*H.inv()*Hy*L
    M=S.Matrix(q,q,lambda i,j:S.Poly(S.rem(y**(j+1),Q.as_expr(),y),y).nth(i))
    ck(f'Original minimum right inverse N={N}',J*L==S.eye(q))
    ck(f'Original minimum metric N={N}',L.T*H*L==G)
    ck(f'Actual compression selfadjoint N={N}',G*C==C.T*G)
    ck(f'NG21 rank-one difference N={N}',(C-M).rank()<=1)
    ck(f'Parity nilpotence N={N}',(C-M)**2==S.zeros(q))
    d=N+1-q
    fulltrace=S.trace((H.inv()*Hy)**2)
    if d:
        Hr=S.Matrix(d,d,lambda i,j:moment(i+j,True))
        Hry=S.Matrix(d,d,lambda i,j:moment(i+j+1,True))
        reltrace=S.trace((Hr.inv()*Hry)**2)
        coupling=(polynomial_norm(d,True)-polynomial_norm(N+1))/polynomial_norm(d-1,True)
    else: reltrace=S.Integer(0);coupling=S.Integer(0)
    ck(f'NG19 exact full coupling N={N}',S.trace(C*C)==fulltrace-reltrace-2*coupling)
    if d: ck(f'Positive full coupling N={N}',coupling>0)
    Lambda=S.Matrix([[1,0,1,0],[0,1,0,2],[0,0,0,1]])
    Hb=(Lambda*G.inv()*Lambda.T).inv()
    Lb=G.inv()*Lambda.T*Hb
    Mb=Lambda*M*Lb;Cb=Lambda*C*Lb
    ck(f'NG22 attained section N={N}',Lambda*Lb==S.eye(3) and Lb.T*G*Lb==Hb)
    ck(f'Observed rank-one difference N={N}',(Mb-Cb).rank()<=1)
    Madj=Hb.inv()*Mb.T*Hb
    ck(f'NG23 squared difference rank N={N}',(Madj*Mb-Cb*Cb).rank()<=2)
nc('Removing full cross block changes trace square',S.trace(C*C)!=fulltrace-reltrace)
nc('Observed metric adjoint differs from coordinate transpose',Madj!=Mb.T)
nc('Original full-root matrix differs from y^q quotient',M!=S.Matrix(q,q,lambda i,j:int(i==j+1)))

# Independent numerical stress tests of the general finite trace bound,
# including a large rank-one singular outlier. These do not certify a limit.
rng=np.random.default_rng(72901)
for dim in [6,9,14]:
    A=rng.normal(size=(dim,dim)); C=(A+A.T)/2
    codim=2; U,_=np.linalg.qr(rng.normal(size=(dim,dim-codim)))
    Cb=U.T@C@U
    for scale in [1.0,1e6]:
        M=Cb+scale*np.outer(rng.normal(size=dim-codim),rng.normal(size=dim-codim))
        for t in [1/1024,0.3,2.0]:
            eigen=np.linalg.eigvalsh(C)/dim
            singular=np.linalg.svd(M,compute_uv=False)/dim
            lhs=abs(np.sum(singular**2*np.exp(-t*singular**2))-np.sum(eigen**2*np.exp(-t*eigen**2)))
            ck(f'NG23 numeric outlier dim={dim},scale={scale},t={t}',lhs<=4*(codim+1)/(np.e*t))

proof=P/'NATIVE_GAUSSIAN_TRANSFER.tex'
receipt={'result':'PASS','checks':len(checks),'negative_controls':len(controls),
 'scope':'Exact finite positive-measure identities plus labelled numerical rank-one stress examples; asymptotic convergence is proved in NG10-26.',
 'proof_sha256_at_run':hashlib.sha256(proof.read_bytes()).hexdigest(),
 'check_names':checks,'negative_control_names':controls}
(P/'NATIVE_TRANSFER_CHECKS.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:receipt[k] for k in ['result','checks','negative_controls']}))
