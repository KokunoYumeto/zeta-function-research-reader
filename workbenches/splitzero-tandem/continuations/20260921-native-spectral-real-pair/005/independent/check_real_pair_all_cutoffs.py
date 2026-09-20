"""Exact reciprocal identities and a bounded certified nonresonance calculation.

The finite symbolic checks support the all-degree proof in the TeX and review.
The interval calculation proves only 1 <= D <= 100, using the saved full-series
certificate and retaining its outward enclosures and source hash.
"""
from pathlib import Path
import hashlib
import json
import platform

import sympy as sp
import flint
from flint import arb

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
checks = []


def check(name, value):
    values = list(value) if isinstance(value, sp.MatrixBase) else [value]
    for expression in values:
        assert sp.cancel(sp.expand(expression)) == 0, (name, expression)
    checks.append({"name": name, "scalar_entries": len(values)})


c, d, e, c3, d2, e1, f = sp.symbols("c d e c3 d2 e1 f")
x, tau = sp.symbols("x tau")
lam, theta = sp.symbols("lambda theta", real=True)


def coefficient_h(n):
    if n < 0:
        return sp.Integer(0)
    return sp.Add(*[
        (-1)**(n-k) * sp.binomial(n-k, k) * d**(n-2*k)
        * e**k / c**(n-k+1)
        for k in range(n//2+1)
    ])


H = [coefficient_h(n) for n in range(13)]


def coefficient_square(n):
    if n < 0:
        return sp.Integer(0)
    return sp.Add(*[H[j]*H[n-j] for j in range(n+1)])


K = [-(c3*coefficient_square(n) + d2*coefficient_square(n-1)
       + e1*coefficient_square(n-2) + f*coefficient_square(n-3))
     for n in range(11)]

for n in range(13):
    check(f"reciprocal quadratic coefficient {n}",
          c*H[n] + d*coefficient_h(n-1) + e*coefficient_h(n-2)
          - int(n == 0))
    check(f"complete Chebyshev coefficient {n}",
          H[n].subs({d: -2*sp.I*c*lam*theta, e: -c*lam**2})
          - (sp.I*lam)**n*sp.chebyshevu(n, theta)/c)

for n in range(11):
    get_k = lambda j: K[j] if j >= 0 else sp.Integer(0)
    check(f"first period correction convolution {n}",
          c*K[n] + d*get_k(n-1) + e*get_k(n-2)
          + c3*coefficient_h(n) + d2*coefficient_h(n-1)
          + e1*coefficient_h(n-2) + f*coefficient_h(n-3))
    check(f"first correction parameter derivative {n}",
          K[n] - c3*sp.diff(H[n], c) - d2*sp.diff(H[n], d)
          - e1*sp.diff(H[n], e) + f*coefficient_square(n-3))

# Every omitted higher symbol coefficient has positive degree >= 2 after
# g(tau*x, tau)/tau**2. The displayed check includes independent jets through
# g_8 and leaves every original coefficient free.
scaled = c + d*x + e*x**2 + tau*(c3+d2*x+e1*x**2+f*x**3)
high = sp.Add(*[sp.Symbol(f"g{j}_0")*tau**(j-2)*x**j
               for j in range(4, 9)])
check("higher original coefficients have zero scaled constant",
      high.subs(tau, 0))
check("higher original coefficients have zero scaled first derivative",
      sp.diff(high, tau).subs(tau, 0))
formal_reciprocal = sp.Add(*[(H[n]+tau*K[n])*x**n for n in range(11)])
product = sp.expand(scaled*formal_reciprocal)
for n in range(11):
    check(f"scaled inverse constant convolution {n}",
          product.coeff(x, n).coeff(tau, 0)-int(n == 0))
    check(f"scaled inverse first convolution {n}",
          product.coeff(x, n).coeff(tau, 1))

# This is the algebraic induction step for every integer degree, with no
# numeric cutoff: F_{n+1}=(e/c)F_n for F_n=H_n^2-H_{n-1}H_{n+1}.
u, v, p, q = sp.symbols("u v p q")
w = p*u+q*v
F0 = u*u-v*w
F1 = w*w-u*(p*w+q*u)
check("Cassini induction step for arbitrary degree", F1+q*F0)
check("Cassini initial coefficient", H[0]**2-1/c**2)
for n in range(1, 12):
    check(f"Cassini coefficient {n}",
          H[n]**2-H[n-1]*H[n+1]-(e/c)**n/c**2)

# Arbitrary positive weights are kept as independent symbols in these
# structural identities. No replacement of the original Gamma norm occurs.
for D in range(2, 9):
    rho = sp.symbols(f"rho0:{D+1}", positive=True)
    gj = {j: sp.Symbol(f"g{j}") for j in range(2, D+1)}
    C = sp.Matrix(D-1, D-1, lambda i, j:
                  gj[j+2-i]*rho[j+2]/rho[i] if j >= i else 0)
    check(f"full nonzero forward block determinant D={D}",
          C.det()-gj[2]**(D-1)*rho[D-1]*rho[D]/(rho[0]*rho[1]))

Delta = d*(d*d-2*c*e)
Knum = 2*c*d*e1+2*c3*d*e+(2*c*e-3*d*d)*d2-c*c*f
check("D=3 original leading inverse coefficient", H[3]+Delta/c**4)
check("D=3 complete next coefficient before resonance",
      K[3]-Knum/c**4-4*c3*Delta/c**5)
check("D=1 resonant diagonal", H[0]-1/c)
check("D=1 resonant upper right", K[1].subs(d, 0)+d2/c**2)

# Bounded certified propagation. Printed Arb balls are outward enclosures;
# they are read as balls, never as rounded point estimates. The certificate's
# original 650-term series has its entire tail included by its saved proof.
certificate_path = ROOT / "REAL_PAIR_CERTIFICATE.json"
certificate = json.loads(certificate_path.read_text(encoding="utf-8"))
original_script = ROOT / "certify_real_pair.py"
assert certificate["status"] == "CERTIFIED"
assert all(certificate["checks"].values())
assert hashlib.sha256(original_script.read_bytes()).hexdigest() == certificate["script_sha256"]
flint.ctx.prec = 256
flint.ctx.threads = 1
c_ball = arb(certificate["period_order2_coefficient_c"])
b_ball = arb(certificate["half_mu2"])
R_ball = arb(certificate["mixed_first_moment_dreal"])
assert c_ball > 0 and b_ball > 0
theta_ball = R_ball/(2*(c_ball*b_ball).sqrt())
assert theta_ball > arb("0.9977939")
assert theta_ball < arb("0.9977941")
assert theta_ball > -1 and theta_ball < 1
phi = theta_ball.acos()
assert phi.sin() > 0
rows = []
root_rows = []
global_gap = None
smallest_u = None
for D in range(1, 101):
    u_ball = ((D+1)*phi).sin()/phi.sin()
    assert u_ball.abs_lower() > arb("0.28"), (D, u_ball)
    if smallest_u is None or u_ball.abs_lower() < smallest_u[0]:
        smallest_u = (u_ball.abs_lower(), D)
    minimum_gap = None
    for k in range(1, D+1):
        root = (arb.pi()*k/(D+1)).cos()
        difference = theta_ball-root
        assert difference.abs_lower() > arb("0.0000195"), (D, k, difference)
        gap = difference.abs_lower()
        root_rows.append({"D": D, "k": k,
                          "theta_minus_root": difference.str(40)})
        if minimum_gap is None or gap < minimum_gap[0]:
            minimum_gap = (gap, k)
        if global_gap is None or gap < global_gap[0]:
            global_gap = (gap, D, k)
    rows.append({"D": D, "U_D_theta": u_ball.str(40),
                 "U_D_abs_lower": u_ball.abs_lower().str(40),
                 "nearest_root_k": minimum_gap[1],
                 "minimum_root_gap_lower": minimum_gap[0].str(40),
                 "nonresonance_certified": True,
                 "inverse_singular_pole_exponents": [D+2, D]+[0]*(D-1),
                 "exterior_pole_exponents": [D+2]+[2*(D+1)]*D})

source_names = ["REAL_PAIR_COLLISION.tex", "REAL_PAIR_ES_RETURN.tex",
                "REAL_PAIR_ALL_CUTOFFS.tex"]
sources = {name: hashlib.sha256((HERE/name).read_bytes()).hexdigest()
           for name in source_names if (HERE/name).exists()}
out = {
    "status": "PASS",
    "scope": "Exact algebraic identities supporting the all-degree proof; certified nonresonance only for integers 1 <= D <= 100. No all-degree nonresonance claim.",
    "symbolic_check_groups": len(checks),
    "symbolic_scalar_entries": sum(row["scalar_entries"] for row in checks),
    "checks": checks,
    "source_sha256": sources,
    "proof_sha256": sources["REAL_PAIR_ALL_CUTOFFS.tex"],
    "root_certificate_sha256": hashlib.sha256(certificate_path.read_bytes()).hexdigest(),
    "root_certificate_script_sha256": certificate["script_sha256"],
    "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "versions": {"python": platform.python_version(), "sympy": sp.__version__,
                 "python_flint": flint.__version__},
    "interval_precision_bits": flint.ctx.prec,
    "retained_input_balls": {"c": str(c_ball), "abs_B_squared": str(b_ball), "R": str(R_ball)},
    "theta": theta_ball.str(40),
    "theta_rational_outer_interval": ["9977939/10000000", "9977941/10000000"],
    "nonresonance_cutoffs": [1, 100],
    "root_intervals_checked": len(root_rows),
    "uniform_U_abs_lower_strict": "7/25",
    "minimum_U_abs_lower": {"D": smallest_u[1], "value": smallest_u[0].str(40)},
    "uniform_root_separation_lower_strict": "39/2000000",
    "minimum_root_gap_lower": {"D": global_gap[1], "k": global_gap[2], "value": global_gap[0].str(40)},
    "cutoffs": rows,
    "root_separations": root_rows,
}
output_path = HERE / "REAL_PAIR_ALL_CUTOFFS_CHECK.json"
output_path.write_text(json.dumps(out, indent=2)+"\n", encoding="utf-8")
print(json.dumps({key: out[key] for key in [
    "status", "symbolic_check_groups", "symbolic_scalar_entries",
    "root_intervals_checked", "theta", "minimum_U_abs_lower",
    "minimum_root_gap_lower", "uniform_root_separation_lower_strict"]}, indent=2))
