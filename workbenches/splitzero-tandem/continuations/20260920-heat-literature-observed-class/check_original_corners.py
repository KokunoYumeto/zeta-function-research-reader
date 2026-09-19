"""Exact algebra checks accompanying ORIGINAL_CORNER_NONVANISHING.tex.

The theorem is proved in the TeX; these computations independently check
its polynomial identities.  No floating point value establishes a theorem.
"""
from pathlib import Path
import hashlib
import json
import sympy as s

HERE = Path(__file__).resolve().parent
checks = []


def zero(name, expression):
    value = s.factor(s.cancel(s.expand(expression)))
    if value != 0:
        raise AssertionError((name, value))
    checks.append({"name": name, "exact_residual": "0"})


def matrix_zero(name, expression):
    for i in range(expression.rows):
        for j in range(expression.cols):
            zero(f"{name}[{i},{j}]", expression[i, j])


t, d = s.symbols("tau d", real=True)
om = s.symbols("omega", nonzero=True)
x = s.symbols("x")
alpha = -3*t + s.I*d
alphabar = -3*t - s.I*d
A, B = -t + s.I*d, t + s.I*d
r = om**2
F = alpha*om**2*(1-r)*(B**2*(1+r)**2-4*t**2*r)
G = om**2*(1-r)**2*(alpha*B**2-r*alphabar*s.conjugate(B)**2)
zero("NC12 first complete bracket equals F",
     alpha*(om*B+A*om**3)**2-alpha*(A*om**2+B*om**4)**2-F)
zero("NC12 second complete bracket equals G",
     alpha*(om*B+s.conjugate(A)*om**3)**2
     -alphabar*(A*om**2+s.conjugate(B)*om**4)**2-G)
zero("Z real and imaginary parts",
     alpha*B**2-((d**2*t-3*t**3)-s.I*d*(5*t**2+d**2)))

eps, C = s.symbols("epsilon C", real=True)
S = 1-C
F_abs_reduced = (9+eps**2)*(((1-eps**2)*C-1)**2+4*eps**2*C**2)
G_abs_diagonal = S*((3-eps**2)**2*S+eps**2*(5+eps**2)**2*C)
claimed_diagonal = (eps**2*(7-21*C+50*C**2)
                    +eps**4*(-1-6*C+20*C**2)
                    +eps**6*(2*C**2-C))
zero("incoming24 diagonal polynomial", F_abs_reduced-G_abs_diagonal-claimed_diagonal)
zero("incoming24 cross coefficient",
     -2*S*(-eps*(5+eps**2))*(3-eps**2)
     -2*eps*(5+eps**2)*(3-eps**2)*S)

delta, gamma = s.symbols("delta gamma", real=True)
aa, bb = s.symbols("unit_real unit_imag", real=True)
unit = aa+s.I*bb
roots = [delta+s.I*gamma, delta-s.I*gamma,
         -delta+s.I*gamma, -delta-s.I*gamma]
beta = 2*(gamma**2-delta**2)
eta = (delta**2+gamma**2)**2
V = s.Matrix([[w**n for n in range(4)] for w in roots])
U = s.diag(unit, s.conjugate(unit), s.conjugate(unit), unit)
J = s.eye(4)
J[0, 2] = -beta/3
J[1, 3] = -2*beta/3
E = s.diag(1, -1, 1, -1)
Popp = s.Matrix([[int(j == 3-i) for j in range(4)] for i in range(4)])
Pconj = s.Matrix([[int(j == (i^1)) for j in range(4)] for i in range(4)])
matrix_zero("V parity", V*E-Popp*V)
matrix_zero("U parity", U*Popp-Popp*U)
matrix_zero("J parity", J*E-E*J)
matrix_zero("V conjugation", s.conjugate(V)-Pconj*V)
matrix_zero("U conjugation", Pconj*s.conjugate(U)-U*Pconj)

ys = s.Matrix(s.symbols("Y1:5"))
Q0 = lambda y: y[0]*y[3]-y[1]*y[2]
zero("Q0 opposite sign +1", Q0(Popp*ys)-Q0(ys))
zero("Q0 conjugation-permutation sign -1", Q0(Pconj*ys)+Q0(ys))

w = s.symbols("w")
h = w**4+beta*w**2+eta
for index, root in enumerate(roots):
    zero(f"original root {index+1}", h.subs(w, root))
    card_numerator = s.Matrix([root*(root**2+beta), root**2+beta, root, 1])
    for row, other in enumerate(roots):
        expected = s.diff(h, w).subs(w, root) if row == index else 0
        zero(f"cardinal evaluation {index+1},{row+1}", (V*card_numerator)[row]-expected)
    if index == 0:
        tau_expr = (gamma**2-delta**2)/3
        d_expr = 2*delta*gamma
        expected = s.Matrix([root*(tau_expr+s.I*d_expr),
                             -tau_expr+s.I*d_expr, root, 1])
        matrix_zero("incoming22 exact numerator", J*card_numerator-expected)

# Exact rational inequalities used by the phase-uniform bound.
assert 78+27*s.Rational(1, 100)**2+3*s.Rational(1, 100)**4 < 79
checks.append({"name": "78epsilon2+27epsilon4+3epsilon6 <= 79epsilon2", "exact": True})
zero("remainder margin 23/50", s.Rational(5, 4)-s.Rational(79, 100)-s.Rational(23, 50))
zero("phase bound constant 23/500", 16*s.Rational(23, 50)/160-s.Rational(23, 500))
assert s.Rational(6000, 999999) < s.Rational(1, 100)
checks.append({"name": "gamma>=1000delta implies epsilon<1/100", "exact": True})
assert 3 > s.sqrt(5)
checks.append({"name": "fifth-root trig lower bounds from 3>sqrt(5)", "exact": True})

# Check the PCL2 coefficient/gamma-integral exponents with exact rationals.
row, col, p, hh = s.symbols("row col p h", integer=True)
nn = (2*p+4*hh+row-col-1)/5
LL = p+hh-nn
zero("PCL2 Gamma argument", row/5+LL-(col+3*p+hh+1)/5)
zero("PCL2 power of five", LL-((col+1-row)/5+3*p/5+hh/5))
zero("PCL2 power of radius two", nn-((row-col-1)/5+2*p/5+4*hh/5))
zero("integrated radius-two prefactor", (row-col-1)/5+(col+1)/5-row/5)
zero("matrix majorant square", 2*(24*4)**2-18432)

sources = {
    "NC": HERE / "providers/ORIGINAL_CONDUCTOR_COPRIMALITY.tex",
    "PCL": HERE / "providers/PCL_COMPLETE.tex",
}
result = {
    "status": "PASS",
    "sympy_version": s.__version__,
    "check_count": len(checks),
    "checks": checks,
    "source_sha256": {k: hashlib.sha256(v.read_bytes()).hexdigest() for k,v in sources.items()},
    "scope": "Exact symbolic algebra and rational inequalities. Full analytic proof is in ORIGINAL_CORNER_NONVANISHING.tex; these checks do not claim numerical certification of a specific original period.",
}
(HERE / "SYMBOLIC_CHECKS.json").write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
print(json.dumps({k: result[k] for k in ("status", "sympy_version", "check_count")}, indent=2))
