"""Exact finite identities supporting zero_transport.tex.

The Taylor polynomials below retain arbitrary actual Taylor coefficients.
They are finite jet certificates, never replacements for the initial Xi.
Analytic convergence, positivity, factorization and root counts are proved
in the accompanying TeX, not inferred from the number of checks here.
"""
from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

import sympy as S

ROOT = Path(__file__).resolve().parents[1]
CHECKS: list[dict] = []


def exact(name: str, expression, *, hypotheses: str = "") -> None:
    # Extract a rational numerator only for equality checking; the formula
    # and its original domain are retained in the TeX and the receipt.
    num, den = S.fraction(S.together(expression))
    residual = S.expand(num)
    good = residual == 0
    CHECKS.append({
        "id": name,
        "passed": bool(good),
        "residual_numerator": str(residual),
        "hypotheses": hypotheses,
        "comparison_denominator": str(den),
    })
    if not good:
        raise AssertionError(f"{name}: {residual}")


r, s, t, z, x, y, w, a, b, c, eps = S.symbols(
    "r s t z x y w a b c eps"
)
r0 = S.symbols("r0", nonzero=True)
u, v = S.symbols("u v", real=True)
A = S.Function("A")(t, s)
Q = S.Function("Q")(t, s)
B = S.Function("B")(t, r)
V = S.Function("V")(t, r)
q = S.Function("q")


def L(g):
    return -S.diff(g, r, 2) / (4 * r**2) + S.diff(g, r) / (4 * r**3)


pull = q(-r**2 / 2)
exact("pullback_generator", L(pull) + S.Subs(S.diff(q(s), s, 2), s, -r**2 / 2) / 4,
      hypotheses="r != 0; removable continuation separately proved")
exact("base_unit_product", S.diff(A * Q, t) + S.diff(A * Q, s, 2) / 4
      - A * (S.diff(Q, t) + S.diff(Q, s, 2) / 4)
      - (S.diff(A, t) + S.diff(A, s, 2) / 4) * Q
      - S.diff(A, s) * S.diff(Q, s) / 2)
exact("cover_unit_product", S.diff(B * V, t) - L(B * V)
      - B * (S.diff(V, t) - L(V))
      - (S.diff(B, t) - L(B)) * V
      - S.diff(B, r) * S.diff(V, r) / (2 * r**2),
      hypotheses="r != 0")

for n in range(21):
    expected = S.Rational(n * (2 - n), 4) * r**(n - 4) if n not in (0, 2) else 0
    exact(f"monomial_{n}", L(r**n) - expected, hypotheses="r != 0")

coeff = S.symbols("a0:10")
g = sum(coeff[n] * r**n for n in range(10))
exact("only_poles_a1_a3", L(g) - coeff[1] / (4 * r**3)
      + 3 * coeff[3] / (4 * r)
      - sum(S.Rational(n * (2-n), 4) * coeff[n] * r**(n-4) for n in range(4,10)))
exact("removable_value", -2 * coeff[4] + S.diff(g, r, 4).subs(r, 0) / 12)
for n in (1, 3, 5, 7, 9, 11, 13, 15):
    j = n // 4 + 1
    iterated = r**n
    product = S.Integer(1)
    for ell in range(j):
        iterated = L(iterated)
        exponent = n - 4 * ell
        product *= S.Rational(exponent * (2-exponent), 4)
    exact(f"odd_pole_iterate_{n}", iterated - product * r**(n-4*j))
    CHECKS.append({"id": f"odd_pole_nonzero_{n}", "passed": product != 0,
                   "exact_coefficient": str(product), "pole_exponent": n-4*j})

F1 = (1+x*y)**3*w + y**2*(1+x*y)*(4+3*x*y)
F2 = y + 3*x*(1+x*y)**2*w + 3*x*y**2*(4+3*x*y)
F3 = 2*x-3*x**2*y-x**3*w
G = {x: -1/(2*r), y: 3*r, w: 26*r**2}
exact("original_spatial_F1", F1.subs(G) + r**2, hypotheses="r != 0")
exact("original_spatial_F2", F2.subs(G), hypotheses="r != 0")
exact("original_spatial_F3", F3.subs(G), hypotheses="r != 0")
exact("original_root_inverse", (y+1/x).subs(G)-r, hypotheses="r != 0")
P = c*r**3-2*r**2+b*r-2*a
exact("original_cubic_slice", P.subs({a: 2*s, b:0, c:0}) + 2*r**2+4*s)
exact("original_alpha_slice", S.diff(P,r).subs({a:2*s,b:0,c:0})/2+2*r)
for idx, F in enumerate((F1,F2,F3), 1):
    expected = (2*s,0,0)[idx-1]
    exact(f"additional_boundary_{idx}", F.subs({x:0,y:0,w:2*s})-expected)

rho = S.Rational(1,2)-S.I*(u+S.I*v)**2/2
exact("arithmetic_real_part", S.re(S.expand(rho))-S.Rational(1,2)-u*v)
exact("arithmetic_imag_part", S.im(S.expand(rho))-(v*v-u*u)/2)
exact("sheet_root_factor", -(r-r0)*(r+r0)/2 - (-r*r/2+r0*r0/2))
exact("paired_sheet_geometric_cancellation", 2/(4*r**2*2*r)-1/(4*r**3),
      hypotheses="r != 0")
As, Av, Zss, Zs = S.symbols("As Av Zss Zs", nonzero=True)
exact("paired_sheet_unit_velocity", (-r*As/Av)/(2*r**2)+As/(2*r*Av),
      hypotheses="r != 0; Av != 0")
exact("simple_cover_velocity", (-Zs+r*r*Zss)/(4*r*r*(-r*Zs))
      -1/(4*r**3)+Zss/(4*r*Zs), hypotheses="r != 0; Zs != 0")

M = S.symbols("M0:7")
fjet = 8*sum((-1)**k*M[k]*r**(4*k)/S.factorial(2*k) for k in range(6))
ftjet = 8*sum((-1)**k*M[k+1]*r**(4*k)/S.factorial(2*k) for k in range(5))
exact("actual_moment_generator_jet", L(fjet)-ftjet)
exact("actual_quarter_rotation_jet", S.expand(fjet.subs(r,S.I*r))-fjet)
exact("actual_initial_fourth_derivative", S.diff(fjet,r,4).subs(r,0)+96*M[1])

delta, h, a2, a3 = S.symbols("delta h a2 a3", nonzero=True)
jet = a2*delta**2+a3*delta**3
heatjet = jet - h*S.diff(jet,delta,2)/4
exact("double_weighted_heat_jet", heatjet-a2*(delta**2-h/2)-a3*(delta**3-3*h*delta/2))
for sign in (-1,1):
    rootjet=sign*eps/S.sqrt(2)+a3*eps**2/(2*a2)
    residual=S.expand(heatjet.subs({delta:rootjet,h:eps**2}))
    exact(f"double_root_order2_{sign}", residual.coeff(eps,2))
    exact(f"double_unit_drift_order3_{sign}", residual.coeff(eps,3))

lam, mu = S.symbols("lambda mu")
sigmajet=-r0**2/2+lam*eps/S.sqrt(2)+mu*eps**2
rootjet=r0-lam*eps/(S.sqrt(2)*r0)-(mu/r0+lam**2/(4*r0**3))*eps**2
inverse_residual=S.expand(rootjet**2+2*sigmajet)
for degree in (0,1,2):
    exact(f"inverse_root_jet_order_{degree}", inverse_residual.coeff(eps,degree))


def he(n):
    return sum(S.factorial(n)*(-1)**ell*y**(n-2*ell)
               /(2**ell*S.factorial(ell)*S.factorial(n-2*ell))
               for ell in range(n//2+1))


for m in range(1,10):
    exact(f"hermite_derivative_{m}", S.diff(he(m),y)-m*he(m-1))
    exact(f"hermite_recurrence_{m}", he(m+1)-y*he(m)+m*he(m-1))
    # Exact polynomial divisibility is the coefficient statement at every
    # Hermite root, not a numerical check on approximated roots.
    drift_residual=S.diff(he(m),y)+he(m+1)
    quotient,remainder=S.div(drift_residual,he(m),y)
    exact(f"common_unit_drift_remainder_{m}",remainder)
    exact(f"common_unit_drift_quotient_{m}",quotient-y)
    thermal=sum((-h/4)**ell*S.factorial(m)
                 *delta**(m-2*ell)/(S.factorial(ell)*S.factorial(m-2*ell))
                 for ell in range(m//2+1))
    exact(f"arithmetic_hermite_scale_{m}",thermal.subs({h:eps**2,delta:eps*y/S.sqrt(2)})
          -(eps/S.sqrt(2))**m*he(m))

tex=ROOT/"tex/zero_transport.tex"
receipt={
    "schema_version":1,
    "calculation":"Actual arithmetic zero transport through s=-r^2/2",
    "executed_utc":datetime.now(timezone.utc).isoformat(),
    "status":"passed",
    "check_count":len(CHECKS),
    "checks":CHECKS,
    "analytic_proof":str(tex),
    "analytic_proof_sha256":hashlib.sha256(tex.read_bytes()).hexdigest(),
    "checker_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "scope":"Exact finite algebraic identities and arbitrary Taylor-jet coefficients only.",
    "not_claimed":["Lean certification","new arithmetic zero","proof of analytic convergence by check count","global NS or RH counterexample"],
    "claim_record":{
        "proved_in_tex":["entire actual heat datum and moment coefficients","zero-free branch point for every real Newman time","exact holomorphic cover maps and full-iterate entire domain","full original slice inverse fibres and zero-divisor multiplicities","simple root equations with analytic units","all-multiplicity Hermite splitting and common analytic-unit drift","double pair exact center and gap equations","nonreal-time branch-locus fourth-root ramification"],
        "actual_initial_datum":"Z(0,s)=Xi(s)=xi(1/2+is)=8H_0(2s)",
        "branch_map":"a=2s=-r^2",
        "real_time_branch_zero":"excluded by positive theta integral",
        "arithmetic_counterexample_status":"none asserted or certified"
    }
}
(ROOT/"checks").mkdir(exist_ok=True)
destination=ROOT/"checks/zero_transport_check.json"
destination.write_text(json.dumps(receipt,indent=2),encoding="utf-8")
print(json.dumps({"status":"passed","checks":len(CHECKS),"receipt":str(destination)}))
