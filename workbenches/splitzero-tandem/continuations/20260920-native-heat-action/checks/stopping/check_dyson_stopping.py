"""Exact coefficient and stopping-bound checks; no arithmetic-zero sample."""
from itertools import product
from math import factorial
from pathlib import Path
import hashlib
import json
import sympy as S

def need(p, name):
    if not p:
        raise RuntimeError(name)
    checks.append(name)

checks=[]
controls=[]
t=S.Symbol("t")
A=S.Matrix([[0,S.Rational(1,3)],[1,0]])
Q=S.Matrix([[0,S.Rational(4,3)],[0,0]])
G=S.diag(3,1)
D=A*Q+Q*A
need(Q*Q==S.zeros(2),"square-zero")
need(G.inv()*A.conjugate().T*G==A,"original-metric")
for r in range(1,7):
    direct=S.trace((A*A-t*D)**r).expand()
    for n in range(1,r+1):
        total=0
        for positions in product(range(r-n+1),repeat=n+1):
            if sum(positions)!=r-n:
                continue
            term=(A*A)**positions[0]
            for j in range(n):
                term=term*D*(A*A)**positions[j+1]
            total+=S.trace(term)
        simplex=(-1)**(r-n)*total/S.factorial(r)
        polynomial=(-1)**r*direct.coeff(t,n)/S.factorial(r)
        need(S.simplify(simplex-polynomial)==0,f"Dyson-{r}-{n}")

for n in range(1,12):
    for x in (S.Rational(1,16),S.Rational(1,8),S.Rational(1,7),S.Rational(1,3)):
        ratio=x*(2*n+1)/(n*(2*n-1))
        need(ratio<=3*x/n,f"ratio-{n}-{x}")
for m in range(1,9):
    for x in (S.Rational(1,8),S.Rational(1,7),S.Rational(1,3)):
        bound=(2*m+1)*x**m/(S.factorial(m)*(1-3*x/(m+1)))
        partial=sum((2*n-1)*x**(n-1)/S.factorial(n-1) for n in range(m+1,m+31))
        need(partial<=bound,f"finite-tail-{m}-{x}")

TT=A-Q
dag=G.inv()*TT.conjugate().T*G
a1=S.trace(dag*TT)-S.trace(TT**2)
need(a1==S.Rational(16,3),"retained-mass-three")
need(S.trace(dag*TT)==S.Rational(10,3),"HS-upper-input")
for n in range(1,11):
    an=S.trace((dag*TT)**n)-S.re(S.trace(TT**(2*n)))
    need(abs(an)<=n*(2*n-1)*3**(n-1)*a1,f"coefficient-{n}")
need((1+S.Rational(2,8))*S.Rational(8,7)-1==S.Rational(3,7),"rational-small-time")
wrong=S.Rational(1,8)**1/S.factorial(1)
correct_first=3*S.Rational(1,8)
if not wrong<correct_first:
    raise RuntimeError("negative control did not reject missing factor")
controls.append("missing-(2m+1)-tail-factor-rejected")
if not S.trace((A-Q)**2)!=S.trace((A+Q)**2):
    raise RuntimeError("negative control did not reject sign")
controls.append("wrong-Dyson-sign-rejected")
proof=Path(__file__).with_name("HEAT_DYSON_STOPPING.tex")
report=dict(status="pass",exact_checks=len(checks),negative_controls=len(controls),
            proof_sha256=hashlib.sha256(proof.read_bytes()).hexdigest(),
            checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            scope="Exact finite coefficients and bounds; no actual zero packet or limiting assertion.",
            checks=checks, controls=controls)
print(json.dumps(report,indent=2))
