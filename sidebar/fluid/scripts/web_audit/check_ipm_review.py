# Portable adaptation of ipm/review/core_replay.py
# Only import/output/inventory handling changed; the delimited mathematics is a raw source byte slice.
from __future__ import annotations
from fractions import Fraction
from itertools import combinations
import sympy as s
import sympy as sp
import sympy as S
from portable_common import begin, finish
begin('ipm_review')
# BEGIN UNCHANGED MATHEMATICAL BODY
checks = []


def equal(name, lhs, rhs=0, hypotheses=()):
    residual = lhs - rhs
    numerator, denominator = s.fraction(s.together(residual))
    expanded_numerator = s.expand(numerator)
    passed = expanded_numerator == 0
    checks.append({
        "name": name,
        "hypotheses": list(hypotheses),
        "lhs": str(lhs),
        "rhs": str(rhs),
        "original_residual": str(residual),
        "rational_denominator": str(denominator),
        "expanded_numerator": str(expanded_numerator),
        "passed": passed,
    })
    if not passed:
        raise AssertionError(name)


k1, k2, A, a, adot, h, hp, I = s.symbols(
    "k1 k2 A a adot h hprime I", real=True
)
kappa = k1**2 + k2**2
k = s.Matrix([k1, k2])
e2 = s.Matrix([0, 1])
m = s.Matrix([k1*k2/kappa, -k1**2/kappa])
nonzero_k = ("k1,k2 real", "k1**2+k2**2>0")
equal("transversality", k.dot(m), hypotheses=nonzero_k)
pressure_symbol = s.I*k2/kappa
for j in range(2):
    equal(f"pressure_velocity_component_{j+1}",
          -s.I*k[j]*pressure_symbol-e2[j], m[j], nonzero_k)

# Differentiated fields, retaining the affine background and full wave.
x2 = s.symbols("x2", real=True)
rho = A*x2+a*h
pressure_gradient = -A*x2*e2-a*k2/kappa*k*h
velocity = a*m*h
for j in range(2):
    equal(f"affine_darcy_component_{j+1}",
          velocity[j]+pressure_gradient[j]+rho*e2[j],
          hypotheses=nonzero_k+("h=H prime at k dot x",))
equal("affine_divergence", a*hp*k.dot(m), hypotheses=nonzero_k)
equal("full_affine_transport_before_amplitude_ode",
      adot*h+velocity.dot(A*e2+a*k*hp),
      (adot-A*k1**2*a/kappa)*h, nonzero_k)
equal("full_affine_transport_with_amplitude_ode",
      (adot*h+velocity.dot(A*e2+a*k*hp)).subs(adot,A*k1**2*a/kappa),
      hypotheses=nonzero_k+("adot=A*k1**2*a/kappa",))
flow_derivative = s.eye(2)+I*hp*m*k.T
equal("flow_area_determinant", flow_derivative.det(), 1, nonzero_k)
equal("flow_phase_increment", k.dot(I*m*h), hypotheses=nonzero_k)
equal("transported_density_coefficient_derivative",
      A*m[1]*a+A*k1**2*a/kappa, hypotheses=nonzero_k)

# Both directions of the general mean translation, with no omitted drift.
sig_t, Uadv, sig_2, b, bd, G = s.symbols(
    "sigma_t U_dot_grad_sigma sigma_x2 b bprime G"
)
equal("forward_mean_translation",
      2*s.pi*sig_t+2*s.pi*b*sig_2+bd
      +2*s.pi*Uadv-2*s.pi*b*sig_2,
      2*s.pi*(sig_t+Uadv)+bd)
rho_t, uadv, rho_2 = s.symbols("rho_t u_dot_grad_rho rho_x2")
equal("inverse_mean_translation",
      (rho_t-b*rho_2-bd)/(2*s.pi)+(uadv+b*rho_2)/(2*s.pi),
      (rho_t+uadv-bd)/(2*s.pi))
q0, cs = s.symbols("P_sigma c_source")
equal("source_potential_gauge_roundtrip", (2*s.pi*q0+2*s.pi*cs)/(2*s.pi), q0+cs)

# The two coordinate directions and the energy density retain their factors.
phase, transverse = s.symbols("s r", real=True)
coordinate_map = s.Matrix([
    (phase*k1-transverse*k2)/kappa,
    (phase*k2+transverse*k1)/kappa,
])
equal("energy_coordinate_phase", k.dot(coordinate_map), phase, nonzero_k)
equal("energy_coordinate_jacobian",
      coordinate_map.jacobian([phase,transverse]).det(), 1/kappa, nonzero_k)
equal("velocity_squared_length", m.dot(m), k1**2/kappa, nonzero_k)

# END UNCHANGED MATHEMATICAL BODY
finish('ipm_review', checks)
