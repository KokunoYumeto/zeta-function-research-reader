"""Independent exact checks for the retained NS/arithmetic correspondence.

One non-critical Python worker, exactly 5,000,000,000-byte Windows job.
Reuses only the resource function AST from the existing three-point checker;
does not execute that checker or launch any subprocess, Lean, or zero search.
"""
from pathlib import Path
import ast
import ctypes
import hashlib
import json
import os
import time

ROOT = Path(__file__).resolve().parents[1]
RESOURCE_SOURCE = ROOT / "scripts" / "check_s6_three_point_fields.py"
resource_tree = ast.parse(RESOURCE_SOURCE.read_text(encoding="utf-8"))
resource_nodes = [node for node in resource_tree.body
                  if isinstance(node, ast.FunctionDef)
                  and node.name == "install_memory_ceiling"]
if len(resource_nodes) != 1:
    raise RuntimeError("The established resource function is not uniquely available")
exec(compile(ast.Module(body=resource_nodes, type_ignores=[]),
             str(RESOURCE_SOURCE), "exec"), globals())
RESOURCE = install_memory_ceiling()
RESOURCE["function_reused_from"] = str(RESOURCE_SOURCE.relative_to(ROOT))
RESOURCE["source_sha256"] = hashlib.sha256(RESOURCE_SOURCE.read_bytes()).hexdigest()

import sympy as S

STARTED = time.monotonic()
PROOF = ROOT / "tex" / "ns_arithmetic_flow.tex"
PROOF_BEFORE = hashlib.sha256(PROOF.read_bytes()).hexdigest()
ROWS = []


def exact(name, residual):
    values = list(residual) if isinstance(residual, S.MatrixBase) else (
        list(residual) if isinstance(residual, (list, tuple)) else [residual])
    differences = [S.expand(S.together(value).as_numer_denom()[0])
                   for value in values]
    if any(value != 0 for value in differences):
        raise AssertionError((name, differences))
    ROWS.append({"id": name, "status": "pass", "entries": len(values),
                 "method": "exact_symbolic_zero_residual"})


# Retain all original polynomial coefficients, including F1's factor 1/2.
x = S.symbols("x1 x2 x3", real=True)
x1, x2, x3 = x
F = S.Matrix([
    (1+x1*x2)**3*x3+x2**2*(1+x1*x2)*(4+3*x1*x2),
    x2+3*x1*(1+x1*x2)**2*x3+3*x1*x2**2*(4+3*x1*x2),
    2*x1-3*x1**2*x2-x1**3*x3])
DF = F.jacobian(x)
original_S = S.diag(S.Rational(1, 2), 1, 1)*F
J = original_S.jacobian(x)
W = -DF.adjugate()/2
J_inverse = W*S.diag(2, 1, 1)
exact("original_DF_determinant_minus_two", DF.det()+2)
exact("retained_J_determinant_minus_one", J.det()+1)
exact("original_coordinate_derivative_scaling",
      J-S.diag(S.Rational(1, 2), 1, 1)*DF)
exact("full_original_J_left_inverse", J_inverse*J-S.eye(3))
exact("full_original_J_right_inverse", J*J_inverse-S.eye(3))
exact("one_coordinate_observation_kernel_in_original_W_basis",
      J[0,:]*W-S.Matrix([[S.Rational(1,2),0,0]]))
physical_velocity = S.Matrix(S.symbols("physical_u1:4", real=True))
exact("three_coordinate_velocity_reconstruction",
      J_inverse*(J*physical_velocity)-physical_velocity)


# Independent finite Taylor jets of a heat solution give every coefficient
# of the complete second physical-time derivative at an arbitrary base point.
t, z, th = S.symbols("t z theta", real=True)
theta1, theta2, v, acc = S.symbols("theta1 theta2 v acc", real=True)
h = S.symbols("h0:5")
initial_profile = sum(h[j]*z**j/S.factorial(j) for j in range(5))
heat_profile = sum((-th/4)**j/S.factorial(j)
                   *S.diff(initial_profile, z, 2*j) for j in range(3))
exact("independent_heat_jet_equation",
      S.diff(heat_profile, th)+S.diff(heat_profile, z, 2)/4)
composed = heat_profile.subs(
    {th: theta1*t+theta2*t**2/2, z: v*t+acc*t**2/2})
first_at_zero = S.diff(composed, t).subs(t, 0)
second_at_zero = S.diff(composed, t, 2).subs(t, 0)
exact("first_time_chain_rule_all_terms", first_at_zero+theta1*h[2]/4-v*h[1])
exact("fixed_actual_Xi_time_map_has_pure_temporal_defect",
      first_at_zero.subs(theta1,0)-v*h[1])
expected_second = theta1**2*h[4]/16-theta1*v*h[3]/2
expected_second += (v**2-theta2/4)*h[2]+acc*h[1]
exact("second_time_chain_rule_all_four_derivatives",
      second_at_zero-expected_second)
expected_coefficients = {1: acc, 2: v**2-theta2/4,
                         3: -theta1*v/2, 4: theta1**2/16}
for j in range(1, 5):
    exact(f"second_time_derivative_h{j}_coefficient",
          S.expand(second_at_zero).coeff(h[j])-expected_coefficients[j])


# Generic Taylor coefficients prove the NS/material Hessian identity without
# imposing any special velocity, force, pressure, or coordinate polynomial.
origin = dict.fromkeys(x, S.Integer(0))
origin[t] = S.Integer(0)
u0 = S.Matrix(S.symbols("u0_1:4", real=True))
ut = S.Matrix(S.symbols("ut_1:4", real=True))
Du = S.Matrix(3, 3, S.symbols("du0:9", real=True))
u_lap = S.Matrix(S.symbols("ulap1:4", real=True))
u_jet = S.Matrix([
    u0[i]+ut[i]*t+sum(Du[i, j]*x[j] for j in range(3))
    +u_lap[i]*x[i]**2/2 for i in range(3)])
g = S.Matrix(S.symbols("g1:4", real=True))
h11, h12, h13, h22, h23, h33 = S.symbols(
    "s11 s12 s13 s22 s23 s33", real=True)
H = S.Matrix([[h11,h12,h13],[h12,h22,h23],[h13,h23,h33]])
scalar_jet = (g.T*S.Matrix(x))[0]+(S.Matrix(x).T*H*S.Matrix(x))[0]/2
scalar_velocity = sum(u_jet[i]*S.diff(scalar_jet, x[i]) for i in range(3))
material_derivative = S.diff(scalar_velocity, t)+sum(
    u_jet[i]*S.diff(scalar_velocity, x[i]) for i in range(3))
material_at_zero = material_derivative.subs(origin)
nu = S.symbols("nu", positive=True)
pressure_gradient = S.Matrix(S.symbols("p1:4", real=True))
force = S.Matrix(S.symbols("f1:4", real=True))
force_acceleration = nu*u_lap-pressure_gradient+force
NS_ut = force_acceleration-Du*u0
after_NS = material_at_zero.subs(dict(zip(ut, NS_ut)), simultaneous=True)
expected_acceleration = g.dot(force_acceleration)+(u0.T*H*u0)[0]
exact("generic_material_derivative_before_NS",
      material_at_zero-g.dot(ut+Du*u0)-(u0.T*H*u0)[0])
exact("generic_NS_force_and_full_Hessian_identity",
      after_NS-expected_acceleration)
exact("generic_jet_retains_each_velocity_Laplacian",
      S.Matrix([sum(S.diff(u_jet[i], xx, 2) for xx in x)
                for i in range(3)])-u_lap)


# The profile Laplacian is checked with a generic full Hessian and a
# non-affine volume-preserving material chart. Its off-diagonal matrix and
# first-order coefficient derivatives are nonzero.
hp1, hp2 = S.symbols("hp1 hp2")
physical_profile = hp1*scalar_jet+hp2*scalar_jet**2/2
physical_laplacian = sum(S.diff(physical_profile, xx, 2) for xx in x)
expected_laplacian = hp2*g.dot(g)+hp1*S.trace(H)
exact("generic_full_physical_profile_Laplacian",
      physical_laplacian.subs(origin)-expected_laplacian)
q = S.symbols("q1 q2 q3", real=True)
q1, q2, q3 = q
X = S.Matrix([q1+2*q2+q2**2, q2+3*q3+q3**2, q3])
A = X.jacobian(q)
Ainv = A.adjugate()  # Determinant is checked immediately below.
exact("nonaffine_material_chart_unit_determinant", A.det()-1)
G = Ainv*Ainv.T
pullback_profile = physical_profile.subs(dict(zip(x, X)), simultaneous=True)
material_laplacian = sum(
    S.diff(G[a,b]*S.diff(pullback_profile, q[b]), q[a])
    for a in range(3) for b in range(3))
q_origin = dict.fromkeys(q, S.Integer(0))
exact("full_nonaffine_material_profile_Laplacian",
      material_laplacian.subs(q_origin)-expected_laplacian)
drift = S.Matrix([sum(S.diff(G[a,b],q[a]) for a in range(3))
                  for b in range(3)])
if not any(component.subs(q_origin) != 0 for component in drift):
    raise AssertionError("The material test must exercise nonzero metric drift")
ROWS.append({"id": "nonaffine_material_test_has_nonzero_metric_drift",
             "status": "pass", "method": "exact_nonzero_coefficients",
             "drift_at_origin": [str(component.subs(q_origin)) for component in drift]})
residual = -theta1*hp2/4+v*hp1-nu*material_laplacian.subs(q_origin)
exact("full_advective_viscous_profile_residual",
      residual+(theta1/4+nu*g.dot(g))*hp2-(v-nu*S.trace(H))*hp1)


# Independent Gaussian integrals test the convention and its 32*pi factor.
omega, r = S.symbols("omega r", real=True)
epsilon = S.symbols("epsilon", positive=True)
gaussian_mass = S.integrate(S.sqrt(S.pi/epsilon)
    *S.exp(-omega**2/(4*epsilon)), (omega, -S.oo, S.oo))
exact("Gaussian_approximate_identity_mass_2pi", gaussian_mass-2*S.pi)
gaussian_transform = S.integrate(S.exp(-omega**2)*S.cos(r*omega),
                                 (omega, -S.oo, S.oo))
exact("unchanged_Gaussian_Fourier_factor",
      gaussian_transform-S.sqrt(S.pi)*S.exp(-r**2/4))
profile_derivative = S.diff(4*S.sqrt(S.pi)*S.exp(-r**2/4), r)
gaussian_norm = S.integrate(profile_derivative**2, (r,-S.oo,S.oo))
gaussian_frequency_norm = 32*S.pi*S.integrate(
    omega**2*S.exp(-2*omega**2), (omega,-S.oo,S.oo))
exact("derivative_Gaussian_Parseval_factor_32pi",
      gaussian_norm-gaussian_frequency_norm)


# The full local unit is independent of the zero multiplicity.
unit_coefficients = S.symbols("unit0:5")
unit = sum(unit_coefficients[j]*z**j/S.factorial(j) for j in range(5))
for multiplicity in (1, 3):
    factored = z**multiplicity*unit
    for n in range(5):
        exact(f"zero_unit_jet_m{multiplicity}_n{n}",
              S.diff(factored,z,multiplicity+n).subs(z,0)
              -S.factorial(multiplicity+n)*unit_coefficients[n]/S.factorial(n))


PROOF_AFTER = hashlib.sha256(PROOF.read_bytes()).hexdigest()
if PROOF_BEFORE != PROOF_AFTER:
    raise RuntimeError("The proof changed during the replay")
ROWS.append({"id": "proof_bytes_stable_during_replay", "status": "pass",
             "method": "sha256_before_after", "sha256": PROOF_AFTER})
receipt = {
    "status": "pass", "check_count": len(ROWS), "checks": ROWS,
    "resource": RESOURCE, "sympy_version": S.__version__,
    "elapsed_seconds": time.monotonic()-STARTED,
    "proof_sha256": PROOF_AFTER,
    "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "scope": "Original full F and DS inverse; generic heat and material jets; all force/Hessian terms; full nonaffine material Laplacian and metric drift; Gaussian 32*pi factor; full unit jets. Analytic flow, topology and norm compactness are reviewed in TeX.",
    "Lean_run": False, "subprocesses_launched": 0,
    "Navier_Stokes_counterexample": False,
}
out = ROOT / "checks" / "ns_arithmetic_flow_checks.json"
out.parent.mkdir(exist_ok=True)
out.write_text(json.dumps(receipt, indent=2)+"\n", encoding="utf-8")
print(json.dumps({key: receipt[key] for key in
                  ("status","check_count","elapsed_seconds","proof_sha256","resource")},
                 indent=2))
