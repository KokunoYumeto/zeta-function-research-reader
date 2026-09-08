"""Exact independent algebra checks for the Euler/viscosity bridge.

These checks do not certify the analytic energy or heat-distribution proof,
and do not check the released Euler construction or run Lean.
"""

import hashlib
import json
from pathlib import Path

import sympy as s

BASE = Path(__file__).resolve().parents[1]
results = []


def zero_check(name, expressions):
    residuals = [s.simplify(s.expand(e)) for e in expressions]
    passed = all(e == 0 for e in residuals)
    results.append({"name": name, "passed": passed,
                    "exact_residuals": [str(e) for e in residuals]})
    if not passed:
        raise AssertionError((name, residuals))


x, y, z, t = s.symbols("x y z t", real=True)
nu, a, A, M = s.symbols("nu a A M", positive=True)
coordinates = (x, y, z)
u = s.Matrix([t*y**2, t**2*z**3, t**3*x**4])
p_E = x*y*z*t
q = x**3*y**2*z*t**2


def grad(f):
    return s.Matrix([s.diff(f, v) for v in coordinates])


def lap(v):
    return v.applyfunc(lambda f: sum(s.diff(f, c, 2) for c in coordinates))


def curl(v):
    return s.Matrix([s.diff(v[2], y)-s.diff(v[1], z),
                     s.diff(v[0], z)-s.diff(v[2], x),
                     s.diff(v[1], x)-s.diff(v[0], y)])


transport = s.Matrix([sum(u[j]*s.diff(u[i], coordinates[j]) for j in range(3))
                      for i in range(3)])
f_E = s.diff(u, t)+transport+grad(p_E)
f_NS = f_E-nu*lap(u)+grad(q)
p_NS = p_E+q
zero_check("polynomial_velocity_is_divergence_free",
           [sum(s.diff(u[j], coordinates[j]) for j in range(3))])
zero_check("same_velocity_NS_residual_with_pressure_adjustment",
           list(s.diff(u, t)+transport+grad(p_NS)-nu*lap(u)-f_NS))
zero_check("pressure_independent_curl_force_identity",
           list(curl(f_NS)-curl(f_E)+nu*lap(curl(u))))
assert any(e != 0 for e in lap(curl(u)))
results.append({"name": "viscous_curl_correction_is_nontrivial",
                "passed": True, "delta_curl_u": [str(e) for e in lap(curl(u))]})

gaussian_1d_mass = s.integrate(s.exp(-x*x/(2*a)), (x, -s.oo, s.oo))
gaussian_1d_moment = s.integrate(x*x*s.exp(-x*x/(2*a)), (x, -s.oo, s.oo))
norm_G_squared = (4*s.pi*a)**(-3)*gaussian_1d_mass**3
cross_gradient_norm_squared = (4*s.pi*a)**(-3)/(4*a*a)*(
    2*gaussian_1d_moment*gaussian_1d_mass**2)
C0 = s.sqrt(s.Rational(1, 2))*(8*s.pi)**(-s.Rational(3, 4))
zero_check("Gaussian_L2_norm_exact_constant",
           [norm_G_squared-(8*s.pi*a)**(-s.Rational(3, 2))])
zero_check("curl_heat_L2_to_Linfinity_exact_constant",
           [cross_gradient_norm_squared-C0**2*a**(-s.Rational(5, 2))])

objective = M/a-A/a**s.Rational(9, 4)
a_star = (9*A/(4*M))**s.Rational(4, 5)
expected_lower = s.Rational(5, 9)*s.Rational(4, 9)**s.Rational(4, 5)*A**(-s.Rational(4, 5))*M**s.Rational(9, 5)
zero_check("optimized_laplacian_lower_bound_critical_point",
           [s.diff(objective, a).subs(a, a_star)])
zero_check("optimized_laplacian_lower_bound_exact_value",
           [objective.subs(a, a_star)-expected_lower])

d = s.Matrix(3, 3, s.symbols("d11 d12 d13 d21 d22 d23 d31 d32 d33", real=True))
curl_norm_squared = (d[1, 2]-d[2, 1])**2+(d[2, 0]-d[0, 2])**2+(d[0, 1]-d[1, 0])**2
nonnegative_remainder = 2*sum(d[j, j]**2 for j in range(3))+(d[1, 2]+d[2, 1])**2+(d[2, 0]+d[0, 2])**2+(d[0, 1]+d[1, 0])**2
zero_check("Frobenius_gradient_to_curl_bound_sum_of_squares",
           [2*sum(entry**2 for entry in d)-curl_norm_squared-nonnegative_remainder])

proof_path = BASE/"tex"/"euler_viscosity_bridge.tex"
report = {
    "schema": "exact-algebra-checks-v1",
    "scope": "Algebra, Gaussian constants, and optimization only; the analytic proof is in the TeX file.",
    "sympy_version": s.__version__,
    "proof_file": "tex/euler_viscosity_bridge.tex",
    "proof_sha256": hashlib.sha256(proof_path.read_bytes()).hexdigest(),
    "checks": results,
    "all_passed": all(item["passed"] for item in results),
    "lean_run": False,
    "source_Euler_construction_independently_verified": False,
}
target = BASE/"research"/"euler_viscosity_bridge_checks.json"
target.write_text(json.dumps(report, indent=2)+"\n", encoding="utf-8")
print(json.dumps({"all_passed": report["all_passed"], "checks": len(results),
                  "report": str(target)}, indent=2))
