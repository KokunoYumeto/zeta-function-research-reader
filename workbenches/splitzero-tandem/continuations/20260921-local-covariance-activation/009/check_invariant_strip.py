"""Exact checks of CGS path depth, sparse interpolation and retained angle."""
import json
from functools import lru_cache
from pathlib import Path
import sympy as s

BASE=Path(__file__).resolve().parent
checks=[]

def ok(name,truth):
    if truth is not True and truth != s.true:
        raise AssertionError(name)
    checks.append(name)

def zero(a):
    return all(s.simplify(x)==0 for x in a)

def pd(a):
    a=a.applyfunc(s.simplify)
    return zero(a-a.conjugate().T) and all(
        s.simplify(a[:j,:j].det())>0 for j in range(1,a.rows+1))

# Exhaustive finite support: all 81 possible leading positions.
for r0 in range(9):
    for s0 in range(9):
        lower=[(r,b) for r in range(9) for b in range(9) if (r,b)<(r0,s0)]
        ok(f'CGS3 height decrease pivot {(r0,s0)}',
           all(9*(r0-r)+s0-b>=1 for r,b in lower))

for k in [9,13]:
    for r0,s0 in [(8,0),(4,4),(0,8),(8,8)]:
        coeff={(r0,s0):s.Integer(1)}
        if r0:
            coeff[(r0-1,8)]=s.Rational(-2,3)
        if s0:
            coeff[(r0,s0-1)]=s.Rational(3,5)
        if (r0,s0)!=(0,0):
            coeff.setdefault((0,0),s.Rational(1,7))
        piv={(r0+i,s0+j) for i in range(k-7) for j in range(k-7)}
        points=[(a,b) for a in range(k+1) for b in range(k+1)]
        strip=[p for p in points if p not in piv]

        @lru_cache(None)
        def reduce(p):
            if p not in piv:
                return {p:s.Integer(1)},0
            i,j=p[0]-r0,p[1]-s0
            result={}; depth=0
            for (a,b),val in coeff.items():
                if (a,b)==(r0,s0):
                    continue
                tail,d=reduce((a+i,b+j));depth=max(depth,1+d)
                for t,x in tail.items():
                    result[t]=result.get(t,0)-val*x
            return {p:s.cancel(x) for p,x in result.items() if x},depth

        reductions={p:reduce(p) for p in points}
        path=max(d for _,d in reductions.values())
        C=sum(abs(x) for x in coeff.values())
        norm=max(sum(abs(x) for x in out.values()) for out,_ in reductions.values())
        tag=f'k={k} pivot={(r0,s0)}'
        ok(tag+' actual path length CGS4',path<=10*k)
        ok(tag+' full column-norm bound CGS4',norm<=C**(10*k))
        ok(tag+' exact strip identity',all(reductions[p][0]=={p:s.Integer(1)} for p in strip))
        for i in range(k-7):
            for j in range(k-7):
                out={}
                for (a,b),val in coeff.items():
                    for t,x in reductions[(a+i,b+j)][0].items():
                        out[t]=out.get(t,0)+val*x
                ok(tag+f' original conductor column {(i,j)} annihilated',
                   all(s.cancel(x)==0 for x in out.values()))
        # Independent execution of the original decreasing-lex elimination.
        f={p:s.Integer(1+p[0]+2*p[1]) for p in points}
        output=dict(f)
        for i,j in sorted(((i,j) for i in range(k-7) for j in range(k-7)),reverse=True):
            scalar=output[(r0+i,s0+j)]
            for (a,b),val in coeff.items():
                output[(a+i,b+j)]-=scalar*val
        expected={p:s.Integer(0) for p in strip}
        for p,val in f.items():
            for t,x in reductions[p][0].items():
                expected[t]+=val*x
        ok(tag+' path expansion equals original lex elimination',
           all(s.cancel(output[p]-expected.get(p,0))==0 for p in points))

# Original Gamma recurrence on an auxiliary sparse physical-root fixture.
y=s.symbols('y');N=5
p=[s.Integer(1),y]
for j in range(1,2*N):
    p.append(s.expand(y*p[-1]-j*s.Rational(2*j-1,2)*p[-2]))
mom=[s.Integer(1)]
for j in range(1,2*N+1):
    pj=s.Poly(p[j],y)
    mom.append(-sum(pj.nth(i)*mom[i] for i in range(j)))
G=s.Matrix(N+1,N+1,lambda i,j:mom[i+j])
Phi=s.Matrix(N+1,N+1,lambda i,j:s.Poly(p[j],y).nth(i)/
             s.sqrt(s.factorial(j)*s.rf(s.Rational(1,2),j)))
roots=[s.Integer(a)+s.I*s.Rational(b,4) for a in [-3,3] for b in [-1,1]]
E=s.Matrix(4,N+1,lambda i,j:p[j].subs(y,roots[i])/
           s.sqrt(s.factorial(j)*s.rf(s.Rational(1,2),j)))
L=s.zeros(N+1,4)
for j,r in enumerate(roots):
    lj=s.prod((y-z)/(r-z) for i,z in enumerate(roots) if i!=j)
    for i in range(N+1):
        L[i,j]=s.Poly(lj,y).nth(i)
ok('CGS9 exact sparse Lagrange right inverse',zero(E*Phi.inv()*L-s.eye(4)))
# R=4 is an explicit upper bound for the actual sqrt(9+1/16).
B=s.Integer(4)*s.Integer(24)**6
ok('CGS10 complete sparse interpolation norm bound',
   s.simplify(s.trace(L.conjugate().T*G*L))<=B)
ok('CGS11 full sparse evaluation lower bound',pd(E*E.conjugate().T-s.eye(4)/B))
Z=s.Matrix([[1,-1,0,0],[0,0,1,-1]])
BF=Z*E
ok('CGS12 actual zero low column retained',zero(BF[:,:1]))
ok('CGS12 sparse row lower bound',pd(BF*BF.conjugate().T-Z*Z.T/B))
embed=s.Matrix(N+1,N-1,lambda i,j:s.Poly((y*y-1)*y**j,y).nth(i))
J=Phi.inv()*embed
PI=s.simplify(J*(J.conjugate().T*J).inv()*J.conjugate().T)
Ctilde=s.simplify(BF*BF.conjugate().T)
CU=s.simplify(BF*PI*BF.conjugate().T)
ok('CGS19 actual projected covariance positive',pd(CU))
ok('CGS19 nonzero projection deficit',pd(Ctilde-CU))
S=Ctilde.inv()*CU # Similar to the Hermitian principal-angle matrix.
ok('CGS20 exact determinant-angle receiver',s.simplify(S.det()-CU.det()/Ctilde.det())==0)
ok('CGS20 negative control projection determinant nontrivial',0<s.simplify(S.det())<1)

report={'status':'passed','checks':len(checks),'details':checks,
 'scope':'All 81 conductor-pivot height cases; exact full lex elimination at eight auxiliary conductor fixtures; sparse Gamma interpolation and retained principal-angle determinant.',
 'mass':'The Gamma fixture factors the same original sqrt(2*pi) mass from both sides of each tested bound and identity.',
 'not_claimed':'No numerical evaluation of the original growing-k principal-angle determinant or invariant allocation.'}
(BASE/'INVARIANT_STRIP_EXACT_CHECKS.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'passed','checks':len(checks)}))
