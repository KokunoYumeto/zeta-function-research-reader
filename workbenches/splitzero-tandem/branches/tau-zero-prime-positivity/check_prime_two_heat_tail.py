"""Exact algebra checks for PT. The complete analytic proof remains in the note."""
from pathlib import Path
import hashlib
import json
import sympy as sp

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "PRIME_TWO_HEAT_TAIL_DERIVATION.md"
checks = []


def equal(name, actual, expected):
    difference = sp.simplify(actual - expected)
    assert difference == 0, (name, difference)
    checks.append({"name": name, "result": "exact equality"})


def positive(name, value):
    value = sp.Rational(value)
    assert value > 0, (name, value)
    checks.append({"name": name, "result": "positive rational", "value": str(value)})


v, n = sp.symbols("v n", positive=True)
d, h, c0 = sp.symbols("d h c0")
lam = 2*n + sp.Rational(1, 2)
c = lam**2 - sp.Rational(1, 4)
T = lambda f: sp.diff(f, v, 2) - f/4
shift = lambda f: sp.diff(f, v) + f/2
P = -2*v**2 + d*v
filtered = sp.exp(lam*v)*T(T(P*sp.exp(-lam*v)))
target = -2*c*c*v*v + (c*c*d+16*lam*c)*v - 4*lam*c*d - 16*lam**2 - 8*c
equal("PT34 full filtered arch polynomial", filtered, target)
equal("PT12 repeated endpoint root +1/2", T(T((v+d)*sp.exp(v/2))), 0)
equal("PT12 repeated endpoint root -1/2", T(T((v+d)*sp.exp(-v/2))), 0)
equal("PT29 convolution derivative coefficient",
      sp.exp(lam*v)*shift(shift(sp.exp(-lam*v)*(v+1/n-h)/(4*n*n))), v-h)
equal("PT30 grouped exponential coefficient",
      1/n - 1/(n*(2*n+1)) + v-h + 2*c0,
      v-h+2/(2*n+1)+2*c0)
equal("PT21 mixed kernel polynomial",
      sp.exp(lam*v)*T(T((v+d)*sp.exp(-lam*v))), c*c*(v+d)-4*lam*c)

q = sp.symbols("q")
on_rational = lambda f: 6*q*sp.diff(f, q)+4*q*q*sp.diff(f, q, 2)
equal("PT18 rational W kernel", on_rational(on_rational(1/(1-q))),
      4*q*(9+55*q+31*q*q+q**3)/(1-q)**5)

moment = 1/(1-q)
S = {}
for j in range(1, 6):
    moment = sp.simplify(q*sp.diff(moment, q))
    S[j] = sp.simplify(moment.subs(q, sp.Rational(1, 4)))
for j, expected in {2: sp.Rational(20,27), 3: sp.Rational(44,27),
                    4: sp.Rational(380,81), 5: sp.Rational(4108,243)}.items():
    equal(f"PT37 geometric moment {j}", S[j], expected)

cauchy = 108/sp.Rational(19,10)**4 + sp.Rational(9,2)/sp.Rational(19,10)**2 + sp.Rational(9,32)
equal("PT17 rational margin", 10-cauchy, sp.Rational(771431,4170272))
positive("PT17 strict margin", 10-cauchy)
positive("PT2 nonempty interval via log bound", sp.Rational(279,400)-sp.Rational(25,36))
positive("PT4 support upper bound", sp.Rational(1,10)-sp.Rational(7,75))
equal("PT35 strong W lower bound", sp.Rational(9,8)*sp.Rational(3,4)*100000, 84375)
equal("PT35 mixed bracket bound", sp.Rational(2,3)*84375-10, 56240)
arch = 36*S[5]+240*S[4]+420*S[3]+148*S[2]
equal("PT37 complete kernel bound", arch, sp.Rational(68272,27))
equal("PT37 complete arch contribution bound", arch/4, sp.Rational(17068,27))
equal("PT39 full derivative bound", arch/4-28120*sp.Rational(2,5), -sp.Rational(286628,27))
positive("PT39 strict total sign margin", sp.Rational(286628,27))
equal("PT39 original interval upper endpoint", sp.Rational(19,25)-sp.Rational(1,32), sp.Rational(583,800))

receipt = {
    "source": SOURCE.name,
    "source_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
    "scope": "Exact symbolic identities and rational inequalities. Analytic convergence, global heat differentiability and support maps are proved in the source and its stated dependencies.",
    "sympy_version": sp.__version__,
    "checks": checks,
    "check_count": len(checks),
    "all_passed": True,
}
(ROOT / "PRIME_TWO_HEAT_TAIL_CHECKS.json").write_text(json.dumps(receipt, indent=2)+"\n", encoding="utf-8")
print(json.dumps({"all_passed": True, "check_count": len(checks), "source_sha256": receipt["source_sha256"]}))
