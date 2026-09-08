"""Exact finite identities accompanying arithmetic_fluid_bridge.tex.

Run: python scripts/verify_arithmetic_fluid_bridge.py
No external source is modified. No numerical search or Lean process is run.
The assertions check polynomial/rational identities; the manuscript separately
proves convergence, positivity, domain, and finite-energy statements.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as s


ROOT = Path(__file__).resolve().parents[1]
checks = []


def equal(name, expression, expected=0):
    difference = s.cancel(s.expand(expression - expected))
    if difference != 0:
        raise AssertionError((name, difference))
    checks.append({"id": name, "status": "PASS", "expected": str(expected)})


x, y, z, t, nu = s.symbols("x y z t nu", real=True)
ell, lam = s.symbols("ell lam", positive=True)
u = s.Function("u")(t, x)
Fh = s.Function("F")(t, x)
hopf = -2 * nu * s.diff(Fh, x) / Fh
residual = s.diff(hopf, t) + hopf * s.diff(hopf, x) - nu * s.diff(hopf, x, 2)
residual = residual.subs(s.diff(Fh, t, x), nu * s.diff(Fh, x, 3))
residual = residual.subs(s.diff(Fh, t), nu * s.diff(Fh, x, 2))
equal("cole_hopf_exact_residual", residual)

heat_summand = s.exp(-nu * t * lam**2 + s.I * x * lam)
equal("arithmetic_heat_summand", s.diff(heat_summand, t) - nu * s.diff(heat_summand, x, 2))

coordinates = (x, y, z)
completion = (u, -y * s.diff(u, x), s.Integer(0))
equal("completion_divergence", sum(s.diff(completion[i], coordinates[i]) for i in range(3)))
burgers_rhs = nu * s.diff(u, x, 2) - u * s.diff(u, x)
completion_residuals = []
for i in range(3):
    value = s.diff(completion[i], t)
    value += sum(completion[j] * s.diff(completion[i], coordinates[j]) for j in range(3))
    value -= nu * sum(s.diff(completion[i], q, 2) for q in coordinates)
    value = value.subs(s.diff(u, t, x), s.diff(burgers_rhs, x)).subs(s.diff(u, t), burgers_rhs)
    completion_residuals.append(s.expand(value))
for i, expected in enumerate((0, 2 * y * s.diff(u, x)**2, 0)):
    equal(f"completion_momentum_{i+1}", completion_residuals[i], expected)

a = s.symbols("a", positive=True)
real_hopf = 2 * nu * a * s.sin(x) / (1 + a * s.cos(x))
shear_curl = s.diff(real_hopf * s.diff(real_hopf, x), x).subs(x, 0)
equal("positive_real_seed_shear_pressure_curl", shear_curl, 4 * nu**2 * a**2 / (1 + a)**2)

a0, b0 = s.symbols("a0 b0", real=True)
affine = s.Matrix([(a0 * x + b0) / (1 + a0 * t), -a0 * y / (1 + a0 * t), 0])
pressure = -a0**2 * y**2 / (1 + a0 * t)**2
for i in range(3):
    value = s.diff(affine[i], t) + sum(affine[j] * s.diff(affine[i], coordinates[j]) for j in range(3))
    value += s.diff(pressure, coordinates[i]) - nu * sum(s.diff(affine[i], q, 2) for q in coordinates)
    equal(f"affine_ns_momentum_{i+1}", value)

k = s.symbols("k", integer=True, nonnegative=True)
periodic_mode = s.exp(-nu * (2 * s.pi * k / ell)**2 * t) * s.cos(2 * s.pi * k * x / ell)
equal("periodic_bc_shear_heat_mode", s.diff(periodic_mode, t) - nu * s.diff(periodic_mode, x, 2))

r, de, dr = s.symbols("r de dr", positive=True)
equal("rindler_coordinate_metric", -r * (de + dr/r)**2 + 2 * (de + dr/r) * dr, -r * de**2 + dr**2/r)

Fp = s.Matrix([
    (1+x*y)**3*z + y**2*(1+x*y)*(4+3*x*y),
    y + 3*x*(1+x*y)**2*z + 3*x*y**2*(4+3*x*y),
    2*x - 3*x**2*y - x**3*z,
])
A = Fp.jacobian(coordinates)
equal("original_fable_determinant", A.det(), -2)
target = s.Matrix([-s.Rational(1,4), 0, 0])
points = [(0,0,-s.Rational(1,4)), (1,-s.Rational(3,2),s.Rational(13,2)), (-1,s.Rational(3,2),s.Rational(13,2))]
for j, point in enumerate(points):
    value = Fp.subs(dict(zip(coordinates, point)))
    for i in range(3):
        equal(f"original_fable_fibre_{j}_{i}", value[i], target[i])

chart_u = s.symbols("chart_u")
substitutions = {y: (chart_u-1)/x, z: (5-3*chart_u)/x**2}
equal("complete_fibre_F2_elimination", x * Fp[1].subs(substitutions, simultaneous=True), 4*chart_u+2)
equal("complete_fibre_F1_elimination", x*x * Fp[0].subs(substitutions, simultaneous=True), chart_u**2+chart_u)
origin = {x:0,y:0,z:0}
equal("direct_polynomial_velocity_divergence_at_origin", s.trace(A).subs(origin), 1)
equal("original_polynomial_euclidean_diffusion_defect", sum(s.diff(Fp[0], q, 2) for q in coordinates).subs(origin), 8)
metric_origin = (A.T * A).subs(origin)
assert metric_origin == s.diag(4,1,1)
checks.append({"id":"induced_metric_at_origin", "status":"PASS", "expected":"diag(4,1,1)"})

matrix = s.Matrix([
    [-s.Rational(1,4),0,1,-1], [0,0,-s.Rational(3,2),s.Rational(3,2)],
    [0,-s.Rational(1,4),s.Rational(13,2),s.Rational(13,2)], [1,1,1,1],
])
inverse = s.Matrix([
    [-4,-s.Rational(8,3),0,0],
    [s.Rational(104,27),s.Rational(208,81),-s.Rational(4,27),s.Rational(26,27)],
    [s.Rational(2,27),-s.Rational(23,81),s.Rational(2,27),s.Rational(1,54)],
    [s.Rational(2,27),s.Rational(31,81),s.Rational(2,27),s.Rational(1,54)],
])
assert matrix * inverse == s.eye(4) and inverse * matrix == s.eye(4)
equal("four_point_affine_determinant", matrix.det(), s.Rational(81,16))
checks.append({"id":"four_point_affine_inverse", "status":"PASS", "expected":"both products I_4"})

result = {
    "schema_version": 1,
    "status": "PASS",
    "method": "exact symbolic polynomial and rational arithmetic",
    "sympy_version": s.__version__,
    "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "check_count": len(checks),
    "checks": checks,
    "analytic_claims": "proved separately in arithmetic_fluid_bridge.tex; no numerical test substitutes for convergence or admissibility",
    "navier_stokes_counterexample": False,
    "lean_used": False,
}
destination = ROOT / "checks" / "arithmetic_fluid_bridge_checks.json"
destination.parent.mkdir(parents=True, exist_ok=True)
destination.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"status":result["status"],"check_count":len(checks),"output":destination.relative_to(ROOT).as_posix()}))
