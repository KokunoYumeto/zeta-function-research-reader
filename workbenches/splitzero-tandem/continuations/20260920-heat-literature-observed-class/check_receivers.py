"""Exact finite diagnostics; synthetic data are not hypothetical zeta zeros."""
from pathlib import Path
import sympy as s
import json
B=Path(__file__).resolve().parent
checks=[]
def ok(name,value):
    assert bool(value),name
    checks.append(name)
n=s.symbols('n',nonnegative=True,integer=True)
ok('AC rho induction identity',s.expand((4*n+5)*(n+s.Rational(1,2))**2-(4*n+1)*(n+1)**2)==s.Rational(1,4))
for b in [s.Rational(1,2),s.Rational(9,2),s.Rational(13,2)]:
    for D in range(6):
        for v in [0,1,3]:
            rho2=lambda j:s.factorial(j)/s.rf(b,j)
            literal=s.prod(rho2(j+v)/rho2(j) for j in range(D+1))
            product=s.prod(s.Rational(j+r)/(j+b+r-1) for j in range(D+1) for r in range(1,v+1))
            ok(f'AC full determinant weight b={b} D={D} v={v}',s.simplify(literal-product)==0)
x,z,w=s.symbols('x z w')
for N in range(7):
    kernel=sum(s.hermite_prob(j,z)*s.hermite_prob(j,w)/(3*s.factorial(j)) for j in range(N+1))
    numerator=s.hermite_prob(N+1,z)*s.hermite_prob(N,w)-s.hermite_prob(N,z)*s.hermite_prob(N+1,w)
    ok(f'LR Christoffel Darboux N={N}',s.cancel(kernel-numerator/(3*s.factorial(N)*(z-w)))==0)
# Original style: a complete coefficient minimum followed by a specified jet observation.
# Test measure has mass 3 and Gaussian moments; jet unit 2+x is explicit.
N=5
mu=lambda j:0 if j%2 else 3*s.factorial2(j-1)
G=s.Matrix(N+1,N+1,lambda i,j:mu(i+j))
jets=[(s.I,0),(s.I,1),(-s.I,0),(-s.I,1)]
L=s.Matrix([[s.diff((2+x)*x**n,x,r).subs(x,a)/s.factorial(r) for n in range(N+1)] for a,r in jets])
M=L*G.inv()*L.conjugate().T
cols=[s.Matrix([s.diff((2+x)*s.hermite_prob(j,x),x,r).subs(x,a)/s.factorial(r) for a,r in jets]) for j in range(N+1)]
Mkernel=sum((t*t.conjugate().T/(3*s.factorial(j)) for j,t in enumerate(cols)),s.zeros(4))
ok('LR full confluent jet kernel equals coefficient inverse',s.simplify(M-Mkernel)==s.zeros(4))
H=M.inv()
t=s.Matrix([s.diff((2+x)*s.hermite_prob(N+1,x),x,r).subs(x,a)/s.factorial(r) for a,r in jets])
mass=3*s.factorial(N+1)
updated=H-H*t*t.conjugate().T*H/(mass+(t.conjugate().T*H*t)[0])
ok('LR attained rank one inverse with original test mass',s.simplify(updated*(M+t*t.conjugate().T/mass))==s.eye(4))
# OB tail resolvent identity, including all finite tail entries.
size=9
J=s.zeros(size)
for j in range(1,size):J[j-1,j]=J[j,j-1]=s.Rational(j,3)
z0=s.Rational(7,5)-s.I*s.Rational(2,3)
v=(z0*s.eye(size)-J).inv()[:,0]
energy=lambda u:s.simplify((u.conjugate().T*u)[0])
for r in range(size-2):
    tail=(z0*s.eye(size-r-1)-J[r+1:,r+1:]).inv()[:,0]
    a=s.Rational(r+1,3)
    Lt=energy(tail)
    ratio=energy(v[r+1:,0])/energy(v[r:,0])
    ok(f'OB exact tail resolvent ratio r={r}',s.simplify(ratio-a*a*Lt/(1+a*a*Lt))==0)
    low=a*a/(abs(z0)**2+a*a+s.Rational(r+2,3)**2)
    high=a*a/(s.Rational(2,3)**2+a*a)
    ok(f'OB Jensen directed bounds r={r}',s.simplify(ratio-low)>=0 and s.simplify(high-ratio)>=0)
result={'passed':len(checks),'checks':checks,'scope':'Exact algebraic and finite-matrix diagnostics on explicitly synthetic data. Analytic source and growing-degree claims are proved in TeX, not established by these tests.'}
(B/'EXACT_RECEIVER_CHECKS.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({'passed':len(checks)}))
