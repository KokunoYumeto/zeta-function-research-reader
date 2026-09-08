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


def zero(name, expr):
    vals = list(expr) if isinstance(expr, s.MatrixBase) else [expr]
    residuals = [s.trigsimp(s.cancel(s.expand(e))) for e in vals]
    passed = all(e == 0 for e in residuals)
    CHECKS.append(dict(name=name, passed=passed,
                       residuals=[str(e) for e in residuals]))
    if not passed:
        raise AssertionError((name, residuals))


x, y, t = s.symbols('x y t', real=True)
coords = [x, y]
xx = s.Matrix(coords)
J = s.Matrix([[0, -1], [1, 0]])


def grad(f):
    return s.Matrix([s.diff(f, c) for c in coords])


def lap(f):
    if isinstance(f, s.MatrixBase):
        return f.applyfunc(lap)
    return sum(s.diff(f, c, 2) for c in coords)


k1, k2, T, Q = s.symbols('k1 k2 T Q', real=True)
k = s.Matrix([k1, k2])
k2norm = k.dot(k)
phase = k.dot(xx)
F = s.Function('F')
P = s.Function('P')
g = s.Function('g')(x, y)
f0 = F(phase)
f1 = s.diff(F(s.Symbol('r')), s.Symbol('r')).subs(s.Symbol('r'), phase)
f2 = s.diff(F(s.Symbol('r')), s.Symbol('r'), 2).subs(s.Symbol('r'), phase)
p0 = P(phase)
r = s.Symbol('r')


def primitive_reduce(expr):
    """Use precisely P'=F, retaining F and all of its derivatives."""
    replacements = {}
    for n in range(1, 7):
        replacements[s.Subs(s.diff(P(r), r, n), r, phase)] = (
            F(phase) if n == 1 else s.Subs(s.diff(F(r), r, n-1), r, phase))
    return expr.xreplace(replacements)


V = T*f0*g
Psi = Q*p0*g
v = primitive_reduce(J*grad(Psi))
lapV_formula = T*(k2norm*f2*g + 2*f1*k.dot(grad(g)) + f0*lap(g))
zero('complete_temperature_laplacian', lap(V)-lapV_formula)
lapv_formula = Q*J*(k2norm*k*f2*g + k2norm*f1*grad(g)
                    + 2*f1*k*k.dot(grad(g))
                    + 2*f0*grad(k.dot(grad(g)))
                    + f0*k*lap(g) + p0*grad(lap(g)))
zero('complete_velocity_laplacian', primitive_reduce(lap(v))-lapv_formula)
scalar_nonlinear = Q*T*(f0**2-p0*f1)*g*(J*k).dot(grad(g))
zero('all_localized_scalar_self_advection',
     primitive_reduce(v.dot(grad(V)))-scalar_nonlinear)
matrix_v_formula = Q*J*(k*k.T*f1*g
                         +f0*(k*grad(g).T+grad(g)*k.T)
                         +p0*s.hessian(g, coords))
zero('complete_localized_velocity_gradient',
     primitive_reduce(v.jacobian(coords))-matrix_v_formula)

a, b, c = s.symbols('a b c', real=True)
D = s.Matrix([[a, b], [c, -a]])
Psi_time = s.Function('Psi')(x, y, t)
v_time = J*grad(Psi_time)
Dx = D*xx
material_v = v_time.diff(t) + v_time.jacobian(coords)*Dx
material_psi = s.diff(Psi_time, t) + Dx.dot(grad(Psi_time))
zero('full_vector_material_commutator',
     material_v-D*v_time-J*grad(material_psi))
zero('trace_free_J_identity', D*J+J*D.T)

z1, z2 = s.symbols('z1 z2', real=True)
z = s.Matrix([z1, z2])
r2 = z.dot(z)
zdot = -D.T*z
S = J*z*z.T/r2
Sprime = S.diff(z1)*zdot[0] + S.diff(z2)*zdot[1]
Sprime_formula = -(J*D.T*z*z.T + J*z*(D.T*z).T)/r2 + 2*z.dot(D.T*z)*S/r2
zero('full_parent_shear_derivative', Sprime-Sprime_formula)

A0, alpha, angle = s.symbols('A0 alpha angle', real=True)
rot = s.Matrix([[s.cos(alpha), -s.sin(alpha)], [s.sin(alpha), s.cos(alpha)]])
phase1 = rot*s.Matrix([s.sin(angle), s.cos(angle)])
baseG = -A0*rot*s.Matrix([0, 1])
zero('first_stage_invariant_temperature_coupling',
     (J*phase1).dot(baseG)+A0*s.sin(angle))

delta, K, d, qphase, TE, OE = s.symbols('delta K d qphase TE OE', nonzero=True)
g1, g2, dg1, dg2 = s.symbols('g1 g2 dg1 dg2')
GE = s.Matrix([g1, g2])
dG = s.Matrix([dg1, dg2])
TdotE = -(J*z).dot(GE)/(K*qphase)*OE
Tdotd = -delta*K**2*qphase*d*TE+d*TdotE
candidate_residual = Tdotd + delta*K**2*qphase*d*TE + (J*z).dot(GE+dG)/(K*qphase)*d*OE
zero('coupled_common_damping_temperature_defect',
     candidate_residual-(J*z).dot(dG)/(K*qphase)*d*OE)

mu, nu, kap, eps, lam, sig = s.symbols('mu nu kappa epsilon lambda sigma', positive=True)
zero('physical_thermal_coefficient_pullback', kap*nu**2*mu-(nu**3/mu)*(kap*mu**2/nu))
zero('physical_viscosity_coefficient_pullback', eps*nu*mu-(nu**2/mu)*(eps*mu**2/nu))
zero('growth_crossing_thermal_cost_power',
     nu**2/mu*lam**(-s.Rational(7, 8))*(mu*lam)**2
     -nu**2*mu*lam**s.Rational(9, 8))
zero('growth_crossing_vector_cost_power',
     nu**2/mu*lam**(-s.Rational(7, 8))*(mu*lam)**2/(2*nu*sig)
     -nu*mu/(2*sig)*lam**s.Rational(9, 8))
zero('growth_crossing_curl_cost_power',
     nu**2/mu*lam**(-s.Rational(7, 8))*(mu*lam)**3/(2*nu*sig)
     -nu*mu**2/(2*sig)*lam**s.Rational(17, 8))

PORTABLE_RECEIPT = {
    'schema': 'coupled-viscous-portable-component-v1',
    'component': 'replay_exact.py',
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
(OUTPUT_DIRECTORY / 'root_replay.json').write_text(
    json.dumps(PORTABLE_RECEIPT, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
print(json.dumps({'all_passed': PORTABLE_RECEIPT['all_passed'],
                  'checks_count': PORTABLE_RECEIPT['checks_count']}))
