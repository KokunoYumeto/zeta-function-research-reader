"""Exact algebraic checks accompanying UZ; the analytic proofs are in the source."""
from pathlib import Path
import hashlib
import json
import re
import sympy as S

root = Path(__file__).resolve().parent
source = root / "FAITHFUL_UNCOMPLETED_ZETA_HEAT.md"
checks = []
def check(name, condition):
    if condition is not True:
        raise AssertionError(name)
    checks.append({"name": name, "passed": True})
def zero(name, expression):
    check(name, S.simplify(expression) == 0)

u, d = S.symbols("u d", nonzero=True)
a, ap, y, yp, ypp = S.symbols("a ap y yp ypp")
# C=u^d c, a=c'/c: all three singular coefficients cancel.
meromorphic_operator = (
    ypp - 2*d*yp/u + d*(d+1)*y/u**2
    + 2*(d/u+a)*(yp-d*y/u)
    + (d*(d-1)/u**2+2*d*a/u+ap+a*a)*y
)
zero("UZ28 full local connection cancellation", meromorphic_operator-(ypp+2*a*yp+(ap+a*a)*y))
zero("UZ4 coordinate heat coefficient", S.Rational(1,4)*(-2*S.I)**2+1)

m = S.symbols("m", integer=True, positive=True)
kappa = (-1)**m * 2*m*(2*m+1)*S.pi**m/S.factorial(m)
xi_positive_factor = m*(2*m+1)*S.factorial(2*m)/(4**m*S.factorial(m)*S.pi**m)
r = (-1)**m*S.factorial(2*m)/(2*(2*S.pi)**(2*m))
zero("UZ23 all-m exact Gamma factor ratio", xi_positive_factor/kappa-r)

# Exact factorization through Gamma recurrence, with Gamma(1+u/2)
# treated as an unchanged formal factor that cancels in the comparison.
for j in range(1,8):
    original_unit_without_gamma = (
        S.Rational(1,2)*(-2*j+u)*(-2*j-1+u)
        *2*(-1)**j/S.factorial(j)
        /S.prod(1-u/(2*k) for k in range(1,j+1))
    )
    factored_unit_without_gamma = (
        (-1)**j*2*j*(2*j+1)/S.factorial(j)
        *(1-u/(2*j))*(1-u/(2*j+1))
        /S.prod(1-u/(2*k) for k in range(1,j+1))
    )
    zero(f"UZ13 unchanged local factors m={j}",
         original_unit_without_gamma-factored_unit_without_gamma)

# Full arbitrary-symbol triangular jet map and its inverse.
N = 5
c = S.symbols("c0:"+str(N+1))
x = S.symbols("x0:"+str(N+1))
ys = []
for j in range(N+1):
    ys.append((x[j]-sum(c[i]*ys[j-i] for i in range(1,j+1)))/c[0])
for j in range(N+1):
    zero(f"UZ18 exact inverse jet order {j}",
         sum(c[i]*ys[j-i] for i in range(j+1))-x[j])

# Leading orientation for reflected local variables.
for dp,dv in [(0,1),(1,0),(-1,0),(0,-1)]:
    cp, cv, yr = S.symbols("cp cv yr", nonzero=True)
    reflection = (-1)**S.Integer(dv)*u**(dv-dp)*cv/cp
    reflected_section = (-u)**(-dv)*yr
    zero(f"UZ51 frame orientations d={dp},d_reflected={dv}",
         reflection*reflected_section-u**(-dp)*cv*yr/cp)
zero("UZ49 endpoint reflected residue", -1/S.Rational(1,2)+2)
zero("UZ49 zero-endpoint reflected slope", -S.Rational(1,2)/(-1)-S.Rational(1,2))
s = S.symbols("s")
zero("UZ41 endpoint filter multiplier",
     (s-S.Rational(1,2))**2-S.Rational(1,4)-s*(s-1))
zero("UZ15 completion polynomial retains reflected equality",
     (1-s)*(-s)-s*(s-1))
text = source.read_text(encoding="utf-8")
tags = re.findall(r"\\tag\{(UZ\d+)\}", text)
check("UZ1-53 unique and complete", tags == [f"UZ{i}" for i in range(1,54)])
check("SZW10 carrier identity explicitly retained", r"\tau=z_{0_L},\quad e=z_{1_L}" in text)
check("No extra disjoint unsupported carrier", r"\{\tau\}\sqcup" not in text)
receipt = {
    "source": source.name,
    "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
    "scope": "Exact symbolic algebra and source consistency; analytic proofs remain in UZ.",
    "count": len(checks),
    "checks": checks,
}
(root/"FAITHFUL_UNCOMPLETED_ZETA_HEAT_CHECKS.json").write_text(
    json.dumps(receipt,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"passed":len(checks),"source_sha256":receipt["source_sha256"]}))

