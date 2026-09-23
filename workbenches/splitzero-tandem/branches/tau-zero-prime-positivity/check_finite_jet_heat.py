"""Exact algebra checks for FJ; no assumed numerical zeta zeros."""
from pathlib import Path
import json, hashlib
import sympy as s

B=Path(__file__).resolve().parent
m,t,beta=s.symbols('m t beta', real=True)
a=s.I*beta
b=m*(m-1)/2
M=s.Matrix([[m,-t*m*a/2,-t*b],[t*m*a/2,t*b,0],[-t*b,0,0]])
checks=[]
def zero(name, value):
    ok=s.cancel(s.expand(value))==0
    checks.append({'name':name,'passed':bool(ok)})
    if not ok: raise AssertionError((name,value))
for i in range(3):
    for j in range(3):zero(f'Hermitian {i},{j}',M[i,j]-s.conjugate(M[j,i]))
zero('full determinant',M.det()+t**3*b**3)
v=s.Matrix([t*b/m,0,1])
zero('specified negative direction',(s.conjugate(v).T*M*v)[0]+t*t*b*b/m)
block=M.extract([0,2],[0,2]);coupling=M.extract([0,2],[1])
zero('retained unit coefficient has zero Schur correction',(s.conjugate(coupling).T*block.inv()*coupling)[0])
zero('actual second coefficient',m*(m-1)*(2*m-3)/4-b*b/m-m*(m-1)*(m-2)/4)
y=s.symbols('y')
for n in range(2,15):
    p=s.Poly(sum((-1)**j*s.factorial(n)/(s.factorial(j)*s.factorial(n-2*j))*y**(n-2*j) for j in range(n//2+1)),y)
    C=s.zeros(n)
    for j in range(n-1):C[j+1,j]=1
    for j in range(n):C[j,n-1]=-p.nth(j)
    zero(f'original heat root p2 m={n}',s.trace(C*C)-2*n*(n-1))
    zero(f'original heat root p4 m={n}',s.trace(C**4)-4*n*(n-1)*(2*n-3))
    pprev=sum((-1)**j*s.factorial(n-1)/(s.factorial(j)*s.factorial(n-1-2*j))*y**(n-1-2*j) for j in range((n-1)//2+1))
    zero(f'Hermite derivative m={n}',s.diff(p.as_expr(),y)-n*pprev)

# Symbolic exact fixed-test section, with original complex coordinate retained.
rho, sigma, x=s.symbols('rho sigma x')
den=(x+rho-sigma)**3
jets=[t*(m-1)/2,0,1]
target=sum(jets[j]*x**j for j in range(3))
num=s.Poly(s.expand(den*target),x)
trunc=sum(num.nth(j)*x**j for j in range(3))
F=trunc/den
for j in range(3):zero(f'fixed rational jet {j}',s.diff(F,x,j).subs(x,0)/s.factorial(j)-jets[j])

u,delta,aa=s.symbols('u delta aa')
for sign in [-1,1]:
    root=sign*s.I*u/s.sqrt(2)-aa*u**2/2
    trial=u**2/2+root**2-3*root**3/delta
    coeff=s.expand(trial).coeff(u,3)
    zero(f'double zero cubic value branch {sign}',coeff-sign*s.I/s.sqrt(2)*(-aa+3/(2*delta)))
K=s.Matrix([[s.Rational(1,2),-s.Rational(5,6)],[-s.Rational(5,6),s.Rational(1,2)]])
for eig,vec in [(s.Rational(-1,3),s.Matrix([1,1])),(s.Rational(4,3),s.Matrix([1,-1]))]:
    for i,e in enumerate(K*vec-eig*vec):zero(f'endpoint eigenvalue {eig} component {i}',e)
zero('specified endpoint correction',(s.Matrix([[1,1]])*K*s.Matrix([1,1]))[0]+s.Rational(2,3))

report={'status':'passed','exact_checks':len(checks),'checks':checks,
 'proof_sha256':hashlib.sha256((B/'FINITE_JET_COMPLEMENT_AND_HEAT_TRUNCATION.md').read_bytes()).hexdigest(),
 'scope':'Symbolic first heat matrix, Schur complement, negative direction, exact original polynomial moments and fixed rational jets. Infinite density and index are proved in the source, not certified by these finite checks.'}
(B/'FINITE_JET_HEAT_CHECKS.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k!='checks'}))
