"""Finite diagnostics for NP: not an analytic or actual-xi verification."""
from pathlib import Path
import json, itertools, math
import sympy as s
import numpy as np

checks=[]
def ck(name, value):
    if not bool(value): raise AssertionError(name)
    checks.append(name)

# Check the noncommuting marked recurrence in a complete original-style
# power companion, including wraparound coefficients, not a nilpotent proxy.
t=s.symbols('t'); roots=list(range(2,10)); q=len(roots)
poly=s.Poly(s.prod(t-r for r in roots),t)
A=s.zeros(q)
for j in range(q-1): A[j+1,j]=1
for j in range(q): A[j,q-1]=-poly.nth(j)
B=s.zeros(q); B[0,q-1]=1
u=s.Rational(3,2); lam=roots[2]; scale=s.Rational(5,7)
vpoly=s.Poly(s.cancel(poly.as_expr()/(t-lam)),t)
v=s.Matrix([scale*vpoly.nth(j) for j in range(q)])
W=[s.eye(q)]
for n in range(6): W.append(-(W[n]*A+(W[n-1]*B if n else s.zeros(q)))/(u*(n+1)))
ck('companion eigenclass', A*v==lam*v)
for jstar in range(5):
    row=s.zeros(1,q); row[0,jstar]=1
    coeff=[(row*sum((W[n]*(lam/u)**(j-n)/s.factorial(j-n) for n in range(j+1)),s.zeros(q))*v)[0] for j in range(7)]
    ck(f'marked order {jstar+2}',all(s.simplify(coeff[j])==0 for j in range(1,jstar+2)))
    expected=scale*(jstar+1)*(-u)**(-jstar-1)
    ck(f'marked coefficient {jstar+2}',s.simplify(s.factorial(jstar+2)*coeff[jstar+2]-expected)==0)

# Exhaust all vanishing-order triples and original mod-five charges.
for i in range(1,5):
    charges=[(j-i)%5 for j in range(1,5) if j!=i]
    for nu in itertools.product(range(1,4),repeat=3):
        if min(nu)!=1: continue
        for charge in range(5):
            values=[sum(a*b for a,b in zip(alpha,nu)) for alpha in itertools.product(range(5),repeat=3) if sum(alpha)<=4 and sum(a*b for a,b in zip(alpha,charges))%5==charge]
            ck(f'jet i={i} nu={nu} charge={charge}',min(values)<=4 and (min(values)==0)==(charge==0))

# Two nonorthonormal positive metrics and scalar/vector observations.
for q,b in [(4,1),(5,2)]:
    A=s.diag(*range(1,q+1))
    J=s.Matrix(q,q,lambda i,j: (i+2*j+1)%4-1)
    G=J.T*J+s.diag(*range(2,q+2))
    Lam=s.Matrix(b,q,lambda i,j:(j+1)**i)
    Q=(Lam*G.inv()*Lam.T).inv()
    I=s.Matrix.hstack(*Lam.nullspace()); r=I.cols
    H=I.T*G*I; L=G.inv()*Lam.T*Q; JK=H.inv()*I.T*G
    T=JK*A*I; C=JK*A*L; B=Lam*A*I; D=Lam*A*L
    ck(f'{q}: full metric decomposition',I*JK+L*Lam==s.eye(q))
    ck(f'{q}: full cross blocks', C!=s.zeros(r,b) and B!=s.zeros(b,r))
    # Exact recovery map on the complete q-step stack.
    Rec=s.zeros(q,b*q)
    for a in range(q):
        e=s.eye(q)[:,a]; obs=Lam*e
        theta=obs.T*Q/(obs.T*Q*obs)[0]
        p=s.Poly(s.prod((t-(c+1))/(a-c) for c in range(q) if c!=a),t)
        for j in range(q): Rec[:,j*b:(j+1)*b]+=e*p.nth(j)*theta
    O=s.Matrix.vstack(*[Lam*A**j for j in range(q)])
    ck(f'{q}: explicit inverse',Rec*O==s.eye(q))
    Y=[s.zeros(b,b*(q-1))]
    for j in range(q-1):
        zj=s.zeros(b,b*(q-1)); zj[:,j*b:(j+1)*b]=s.eye(b)
        Y.append(zj+D*Y[j]+sum((B*T**(j-1-l)*C*Y[l] for l in range(j)),s.zeros(b,b*(q-1))))
    W=s.Matrix.vstack(*Y[1:])
    CT=s.Matrix([[s.rem(t**j,T.charpoly(t).as_expr(),t).expand().coeff(t,h) for h in range(r)] for j in range(q-1)])
    short=s.Matrix.vstack(*[B*T**j for j in range(r)])
    full=s.Matrix.vstack(s.zeros(b,r), W*s.kronecker_product(CT,s.eye(b))*short)
    ck(f'{q}: triangular feedback identity', full==O*I)
    ck(f'{q}: unit triangular determinant', W.det()==1)
    def ar(mat): return np.array(mat,dtype=float)
    def root(mat):
        val,vec=np.linalg.eigh(ar(mat));return (vec*np.sqrt(val))@vec.T
    cr=0.
    for a in range(q):
        e=s.eye(q)[:,a];obs=Lam*e
        p=s.Poly(s.prod((t-(c+1))/(a-c) for c in range(q) if c!=a),t)
        cr+=math.sqrt(float((e.T*G*e)[0]))*np.linalg.norm([float(p.nth(j)) for j in range(q)])/math.sqrt(float((obs.T*Q*obs)[0]))
    sq=root(s.kronecker_product(s.eye(q-1),Q))
    cw=np.linalg.norm(sq@ar(W)@np.linalg.inv(sq),2);ct=np.linalg.norm(ar(CT),2)
    gram=short.T*s.kronecker_product(s.eye(r),Q)*short
    ck(f'{q}: quantitative lower bound',np.linalg.eigvalsh(ar(gram)-(cr*cw*ct)**-2*ar(H)).min()>-1e-10)

# Integer guard with stable transcendental evaluation, including tiny p.
for k,p,c,zeta in itertools.product([9,101],[1.,1e-8,1e-80],[1.,3.],[.2,.8]):
    d=math.expm1(math.log1p(zeta*math.sqrt(p))/(2*k))
    threshold=2*math.log2(c/d); depth=math.ceil(threshold)-1
    value=math.expm1(2*k*math.log1p(2**(-(depth+1)/2)*c))
    prev=math.expm1(2*k*math.log1p(2**(-depth/2)*c))
    ck(f'heat {k},{p},{c},{zeta}',value<=zeta*math.sqrt(p)*(1+1e-12) and prev>zeta*math.sqrt(p)*(1-1e-12))

out={'scope':'Finite synthetic diagnostics only; universal and analytic claims are proved in TeX.','passed':len(checks),'checks':checks}
Path(__file__).with_name('NATIVE_PRECISION_CHECKS.json').write_text(json.dumps(out,indent=2))
print(json.dumps({'passed':len(checks)}))
