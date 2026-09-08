"""Portable replay: original mathematical computation block retained byte-for-byte.

I/O and provenance are adapted explicitly; see provenance/replay_adaptations.json.
Complete analytic proofs are in tex/coupled_viscous_control.tex.
"""
from __future__ import annotations

from pathlib import Path
import hashlib
import json
import sympy as s
import sympy as sp
from portable_support import start_replay

PORTABLE_CONTEXT, OUTPUT_DIRECTORY = start_replay(__file__)
CHECKS = []
checks = []


def check(name: str, expression: sp.Expr | sp.MatrixBase) -> None:
    if isinstance(expression, sp.MatrixBase):
        residuals = [sp.simplify(sp.expand(e)) for e in expression]
    else:
        residuals = [sp.simplify(sp.expand(expression))]
    passed = all(e == 0 for e in residuals)
    CHECKS.append({"name": name, "passed": passed,
                   "exact_residuals": [str(e) for e in residuals]})
    if not passed:
        raise AssertionError((name, residuals))


s = sp.symbols("s", real=True)
chi = sp.Function("chi")(s)
F = sp.sin(s) + chi * (s - sp.sin(s))
Fp = sp.cos(s) + sp.diff(chi, s) * (s - sp.sin(s)) + chi * (1 - sp.cos(s))
Fpp = ((chi - 1) * sp.sin(s) + 2 * sp.diff(chi, s) * (1 - sp.cos(s))
       + sp.diff(chi, s, 2) * (s - sp.sin(s)))
Fppp = ((chi - 1) * sp.cos(s) + 3 * sp.diff(chi, s) * sp.sin(s)
        + 3 * sp.diff(chi, s, 2) * (1 - sp.cos(s))
        + sp.diff(chi, s, 3) * (s - sp.sin(s)))
check("actual_F_first_derivative", sp.diff(F, s) - Fp)
check("actual_F_second_derivative", sp.diff(F, s, 2) - Fpp)
check("actual_F_third_derivative", sp.diff(F, s, 3) - Fppp)

t, x1, x2 = sp.symbols("t x1 x2", real=True)
lam = sp.symbols("lambda", positive=True)
kth, nphys = sp.symbols("kappa_th nu_phys", nonnegative=True)
z1, z2, th, om = (sp.Function(n)(t) for n in ("zeta1", "zeta2", "Theta", "Omega"))
d11, d12, d21 = sp.symbols("D11 D12 D21", real=True)
G1, G2 = sp.symbols("G1 G2", real=True)
D = sp.Matrix([[d11, d12], [d21, -d11]])
J = sp.Matrix([[0, -1], [1, 0]])
zeta = sp.Matrix([z1, z2])
kappa = z1**2 + z2**2
K = lam**2 * kappa
position = sp.Matrix([x1, x2])
old_u = D * position
old_theta = G1 * x1 + G2 * x2
phase = lam * (z1 * x1 + z2 * x2)
profile = sp.Function("F")
fphase = profile(phase)
dfphase = sp.Subs(sp.diff(profile(s), s), s, phase)
d2fphase = sp.Subs(sp.diff(profile(s), s, 2), s, phase)
d3fphase = sp.Subs(sp.diff(profile(s), s, 3), s, phase)
velocity = om / (lam * kappa) * J * zeta * fphase
theta = th * fphase
zeta_dot = -D.T * zeta
phase_subs = {sp.diff(z1, t): zeta_dot[0], sp.diff(z2, t): zeta_dot[1]}


def adv(v: sp.MatrixBase, h: sp.Expr) -> sp.Expr:
    return v[0] * sp.diff(h, x1) + v[1] * sp.diff(h, x2)


def lap(h: sp.Expr) -> sp.Expr:
    return sp.diff(h, x1, 2) + sp.diff(h, x2, 2)


def curl(v: sp.MatrixBase) -> sp.Expr:
    return sp.diff(v[1], x1) - sp.diff(v[0], x2)


a = -((J * zeta).dot(sp.Matrix([G1, G2]))) / (lam * kappa)
b = lam * z1
check("phase_transport", (sp.diff(phase, t) + adv(old_u, phase)).subs(phase_subs))
check("wave_velocity_divergence", sp.diff(velocity[0], x1) + sp.diff(velocity[1], x2))
check("wave_vorticity", curl(velocity) - om * dfphase)
check("wave_self_scalar_advection", adv(velocity, theta))
check("wave_self_vorticity_advection", adv(velocity, om * dfphase))

total_u = old_u + velocity
total_theta = old_theta + theta
Rtheta = (sp.diff(total_theta, t) + adv(total_u, total_theta) - kth * lap(total_theta)
          - sp.diff(old_theta, t) - adv(old_u, old_theta) + kth * lap(old_theta))
expected_Rtheta = (sp.diff(th, t) - a * om) * fphase - kth * K * th * d2fphase
check("exact_scalar_residual", (Rtheta - expected_Rtheta).subs(phase_subs))
old_omega = d21 - d12
total_omega = old_omega + om * dfphase
Romega = (sp.diff(total_omega, t) + adv(total_u, total_omega)
          - sp.diff(total_theta, x1) - nphys * lap(total_omega)
          - sp.diff(old_omega, t) - adv(old_u, old_omega)
          + sp.diff(old_theta, x1) + nphys * lap(old_omega))
expected_Romega = (sp.diff(om, t) - b * th) * dfphase - nphys * K * om * d3fphase
check("exact_vorticity_residual", (Romega - expected_Romega).subs(phase_subs))

# Full momentum coefficient identities for arbitrary evolving profiles T,V.
cvec = J * zeta / (lam * kappa)
cdot = cvec.diff(t).subs(phase_subs)
coefficient = 2 * zeta.dot(D * J * zeta) / (lam * kappa**2)
check("trace_free_DJ_identity", D * J + J * D.T)
check("momentum_V_coefficient", cdot + D * cvec - coefficient * zeta)
check("momentum_T_coefficient", b * cvec - sp.Matrix([0, 1]) + z2 * zeta / kappa)
Vformal, Tformal = sp.symbols("V T", real=True)
pressure_gradient = (-coefficient * Vformal + z2 / kappa * Tformal) * zeta
check("full_momentum_pressure_cancellation",
      (cdot + D * cvec) * Vformal + (b * cvec - sp.Matrix([0, 1])) * Tformal
      + pressure_gradient)

# Material-coordinate Laplacian square with arbitrary g and P.
aa1, aa2 = sp.symbols("a1 a2", real=True)
kk = sp.symbols("kappa", positive=True)
q1, q2, h11, h12, h22 = sp.symbols("q1 q2 H11 H12 H22", real=True)
g = sp.Function("g")(aa1, aa2)
P = sp.Function("P")(s)


def qgrad(h: sp.Expr) -> sp.Expr:
    return q1 * sp.diff(h, aa1) + q2 * sp.diff(h, aa2)


def hh(h: sp.Expr) -> sp.Expr:
    return h11 * sp.diff(h, aa1, 2) + 2 * h12 * sp.diff(h, aa1, aa2) + h22 * sp.diff(h, aa2, 2)


def LL(h: sp.Expr) -> sp.Expr:
    return lam**2 * kk * sp.diff(h, s, 2) + 2 * lam * qgrad(sp.diff(h, s)) + hh(h)


expected_L2 = (lam**4 * kk**2 * sp.diff(P, s, 4) * g
               + 4 * lam**3 * kk * sp.diff(P, s, 3) * qgrad(g)
               + 2 * lam**2 * kk * sp.diff(P, s, 2) * hh(g)
               + 4 * lam**2 * sp.diff(P, s, 2) * qgrad(qgrad(g))
               + 4 * lam * sp.diff(P, s) * qgrad(hh(g)) + P * hh(hh(g)))
check("localized_Laplacian_square_six_terms", LL(LL(P * g)) - expected_L2)
check("localized_scalar_Laplacian",
      LL(profile(s) * g)
      - (lam**2 * kk * sp.diff(profile(s), s, 2) * g
         + 2 * lam * sp.diff(profile(s), s) * qgrad(g) + profile(s) * hh(g)))

# Modewise common-diffusivity factorization; no time coefficient is normalized.
delta, n = sp.symbols("delta n", nonnegative=True)
tau = sp.Function("tau")(t)
at, bt, kt = (sp.Function(name)(t) for name in ("a", "b", "K"))
Theta, Omega = sp.Function("Tamp")(t), sp.Function("Oamp")(t)
factor = sp.exp(-n**2 * tau)
ymode = factor * sp.Matrix([Theta, Omega])
A = sp.Matrix([[-delta * kt * n**2, at], [bt, -delta * kt * n**2]])
common_subs = {sp.diff(tau, t): delta * kt,
               sp.diff(Theta, t): at * Omega, sp.diff(Omega, t): bt * Theta}
check("modewise_common_heat_factor", (ymode.diff(t) - A * ymode).subs(common_subs))

# Algebraic core obstruction; the global periodic contradiction is proved in TeX.
eigenvalue = sp.symbols("eigenvalue", real=True)
check("affine_core_second_derivative_obstruction", sp.diff(s, s, 2) - eigenvalue * s + eigenvalue * s)
check("affine_core_third_derivative_obstruction", sp.diff(s, s, 3) - eigenvalue * sp.diff(s, s) + eigenvalue)

PORTABLE_RECEIPT = {
    'schema': 'coupled-viscous-portable-component-v1',
    'component': 'replay_profile_diffusion.py',
    'checks': CHECKS,
    'checks_count': len(CHECKS),
    'all_passed': all(item['passed'] for item in CHECKS),
    'sympy_version': sp.__version__,
    'portable_provenance': PORTABLE_CONTEXT,
    'scope': 'Original exact finite symbolic identities; analytic proofs remain in the included TeX. The historical source hash is not a fresh PDF verification.',
    'infinite_viscous_sequence_proved': False,
    'navier_stokes_disproof_established': False,
    'lean_used': False,
}
(OUTPUT_DIRECTORY / 'profile_diffusion_replay.json').write_text(
    json.dumps(PORTABLE_RECEIPT, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
print(json.dumps({'all_passed': PORTABLE_RECEIPT['all_passed'],
                  'checks_count': PORTABLE_RECEIPT['checks_count']}))
