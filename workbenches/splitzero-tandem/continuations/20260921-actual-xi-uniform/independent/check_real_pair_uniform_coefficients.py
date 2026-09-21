"""Exact identities for the full-unit two-pole coefficient derivation.

No freely chosen polynomial is substituted for the actual programme unit.
Formal polynomial tests verify universal algebraic identities; the full
analytic coefficient bounds are proved in RUC1--30 by contour integration.
"""
from pathlib import Path
import hashlib
import json
import platform

import sympy as S

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
checks = []


def check(name, expression):
    entries = list(expression) if isinstance(expression, S.MatrixBase) else [expression]
    for value in entries:
        assert S.cancel(value) == 0, (name, value)
    checks.append({"name": name, "scalar_entries": len(entries)})


a, b, t, z = S.symbols("alpha beta t z", nonzero=True)
Fa, Fb, Fp = S.symbols("Falpha Fbeta Fprime")
f = S.symbols("f0:7")
F = sum(f[j]*t**j for j in range(7))
q = (t-a)*(t-b)
F_a, F_b = F.subs(t, a), F.subs(t, b)
L = (F_a*(t-b)-F_b*(t-a))/(a-b)
quotient, polynomial_remainder = S.div(F, S.expand(q), t)
check("full interpolation polynomial equals division remainder", L-polynomial_remainder)
check("exact unit division without omitted coefficients", F-L-q*quotient)


def complete_h(n):
    return sum((a**(n-j)*b**j for j in range(n+1)), S.Integer(0)) if n >= 0 else S.Integer(0)


def principal(n, fa=Fa, fb=Fb):
    return (fb*b**(-n-1)-fa*a**(-n-1))/(a-b)


inverse_coefficients = []
for n in range(10):
    prev = inverse_coefficients[n-1] if n >= 1 else 0
    prev2 = inverse_coefficients[n-2] if n >= 2 else 0
    value = S.cancel(((f[n] if n < len(f) else 0)+(a+b)*prev-prev2)/(a*b))
    inverse_coefficients.append(value)
    remainder_n = sum((f[j]*complete_h(j-n-2) for j in range(n+2, len(f))), S.Integer(0))
    check(f"contour coefficient agrees with exact polynomial quotient n{n}",
          quotient.coeff(t, n)-remainder_n)
    check(f"complete inverse coefficient principal plus remainder n{n}",
          value-principal(n, F_a, F_b)-remainder_n)
    check(f"coalescent limit retains the unit derivative n{n}",
          -S.diff(F.subs(t, a)*a**(-n-1), a)
          -(n+1)*F_a*a**(-n-2)+S.diff(F, t).subs(t, a)*a**(-n-1))
    if n:
        check(f"adjacent reconstruction alpha n{n}",
              a*principal(n)-principal(n-1)-Fb*b**(-n-1))
        check(f"adjacent reconstruction beta n{n}",
              b*principal(n)-principal(n-1)-Fa*a**(-n-1))
    if n < 7:
        check(f"Hankel determinant with full residues n{n}",
              principal(n)*principal(n+2)-principal(n+1)**2+Fa*Fb/(a*b)**(n+3))
    coalescent = lambda j: (j+1)*Fa*a**(-j-2)-Fp*a**(-j-1)
    if n:
        check(f"coalescent adjacent reconstruction n{n}",
              a*coalescent(n)-coalescent(n-1)-Fa*a**(-n-1))
    if n < 7:
        check(f"coalescent Hankel determinant n{n}",
              coalescent(n)*coalescent(n+2)-coalescent(n+1)**2+Fa**2/a**(2*n+6))

# A universal two-exponential proof with arbitrary current powers: no
# induction cutoff is used in this algebraic identity.
X, Y, ca, cb = S.symbols("X Y ca cb")
P0 = ca*X+cb*Y
P1 = ca*X/a+cb*Y/b
P2 = ca*X/a**2+cb*Y/b**2
check("all-index rank-two Hankel identity",
      P0*P2-P1**2-ca*cb*X*Y*(1/a-1/b)**2)

# The parity reduction retains complex real/imaginary parts without a
# numeric angle or phase approximation.
xr, xi = S.symbols("Xreal Ximag", real=True)
Xcomplex = xr+S.I*xi
check("even real-slice principal numerator",
      (-S.conjugate(Xcomplex)-Xcomplex)+2*xr)
check("odd real-slice principal numerator",
      (S.conjugate(Xcomplex)-Xcomplex)+2*S.I*xi)

for ell in range(1, 8):
    divided = -(F_b*b**(ell-1)-F_a*a**(ell-1))/(b-a)
    check(f"negative-index divided difference l{ell}",
          principal(-ell, F_a, F_b)-divided)
    check(f"coalescent negative index l{ell}",
          (1-ell)*F_a*a**(ell-2)-S.diff(F, t).subs(t, a)*a**(ell-1)
          +S.diff(F.subs(t, a)*a**(ell-1), a))

# Exact finite matrix reconstructions include every lower correction.
for D in range(1, 6):
    rho = S.symbols(f"rho0:{D+1}", nonzero=True)
    A_a, A_b = -Fa/(a*(a-b)), Fb/(b*(a-b))
    ua = S.Matrix([a**i/rho[i] for i in range(D+1)])
    va = S.Matrix([[rho[j]*a**(-j) for j in range(D+1)]])
    ub = S.Matrix([b**i/rho[i] for i in range(D+1)])
    vb = S.Matrix([[rho[j]*b**(-j) for j in range(D+1)]])
    full = S.Matrix(D+1, D+1, lambda i, j: principal(j-i)*rho[j]/rho[i])
    check(f"weighted full principal matrix outer products D{D}",
          full-A_a*ua*va-A_b*ub*vb)
    upper = S.Matrix(D+1, D+1,
                     lambda i, j: principal(j-i)*rho[j]/rho[i] if j >= i else 0)
    correction = S.Matrix(D+1, D+1,
                     lambda i, j: -principal(j-i)*rho[j]/rho[i] if i > j else 0)
    check(f"all lower correction signs D{D}", upper-full-correction)
    if D >= 2:
        corner = S.Matrix([[principal(D-1)*rho[D-1]/rho[0], principal(D)*rho[D]/rho[0]],
                           [principal(D-2)*rho[D-1]/rho[1], principal(D-1)*rho[D]/rho[1]]])
        check(f"weighted exterior principal minor D{D}",
              corner.det()-Fa*Fb/(a*b)**(D+1)*rho[D-1]*rho[D]/rho[0]/rho[1])

# Actual order-one quotient: polynomial remainder is another exact
# divided difference, with a separate uniform contour denominator.
one_remainder = S.cancel((F-F_a)/(t-a))
for n in range(7):
    one_coeff = -sum(f[j]*a**(j-n-1) for j in range(min(n, 6)+1))
    one_rem_coeff = sum((f[j]*a**(j-n-1) for j in range(n+1, 7)), S.Integer(0))
    check(f"order-one original quotient coefficient n{n}",
          one_coeff+F_a*a**(-n-1)-one_rem_coeff)
    check(f"order-one quotient polynomial remainder n{n}",
          S.expand(one_remainder).coeff(t, n)-one_rem_coeff)

# The proof of the uniform real determinant threshold records each exact
# error exponent. Checking the factors prevents a lost power of the root.
r, R = S.symbols("r R", positive=True)
for n in range(6):
    check(f"first Hankel relative-error power n{n}",
          r**(-n-2)*R**(-n-2)*r**(2*n+6)-r**2*(r/R)**(n+2))
    check(f"middle Hankel relative-error power n{n}",
          r**(-n-3)*R**(-n-1)*r**(2*n+6)-r**2*(r/R)**(n+1))
    check(f"last Hankel relative-error power n{n}",
          r**(-n-4)*R**(-n)*r**(2*n+6)-r**2*(r/R)**n)
    check(f"quadratic Hankel relative-error power n{n}",
          R**(-2*n-2)*r**(2*n+6)-r**4*(r/R)**(2*n+2))

sources = {
    "proof": HERE/"REAL_PAIR_UNIFORM_COEFFICIENTS.tex",
    "analytic_object": HERE/"REAL_PAIR_LOCAL_ALGEBRA.tex",
    "original_weighted_conductor": ROOT/"source_dependencies"/"WEIGHTED_CONDUCTOR_FORWARD.tex",
}
out = {
    "status": "PASS",
    "scope": "Exact algebraic identities supporting RUC1--30; no numerical root rerun and no finite test used as a substitute for the contour proof or all-index identities.",
    "groups": len(checks),
    "scalar_entries": sum(row["scalar_entries"] for row in checks),
    "checks": checks,
    "source_sha256": {key: hashlib.sha256(path.read_bytes()).hexdigest() for key, path in sources.items()},
    "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "versions": {"python": platform.python_version(), "sympy": S.__version__},
}
(HERE/"REAL_PAIR_UNIFORM_COEFFICIENTS_CHECK.json").write_text(
    json.dumps(out, indent=2)+"\n", encoding="utf-8")
print(json.dumps({key: out[key] for key in ["status", "groups", "scalar_entries", "source_sha256", "checker_sha256"]}, indent=2))
