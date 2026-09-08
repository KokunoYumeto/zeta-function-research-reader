"""Exact differential identities for the uncut affine Boussinesq wave.

This verifies the local general-profile residuals, the explicit pressure lift,
and the frozen viscous eigenvalue polynomial. It does not check localization,
a cascade, finite energy, or Navier--Stokes blowup. Every original frequency
and coefficient is retained. Only exact symbolic arithmetic is used.
"""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


def main() -> None:
    x1, x2, phase = sp.symbols("x1 x2 s", real=True)
    z1, z2 = sp.symbols("zeta1 zeta2", real=True)
    a, b, c = sp.symbols("D11 D12 D21", real=True)
    g1, g2 = sp.symbols("G1 G2", real=True)
    th, om = sp.symbols("Theta Omega", real=True)
    thdot, omdot = sp.symbols("Theta_dot Omega_dot", real=True)
    lam = sp.symbols("lambda", positive=True)
    kappa, nu = sp.symbols("kappa nu", nonnegative=True)
    x = sp.Matrix([x1, x2])
    zeta = sp.Matrix([z1, z2])
    g = sp.Matrix([g1, g2])
    D = sp.Matrix([[a, b], [c, -a]])
    J = sp.Matrix([[0, -1], [1, 0]])
    e2 = sp.Matrix([0, 1])
    zdot = -D.T * zeta
    q = zeta.dot(zeta)
    P = sp.Function("P")
    F = sp.Function("F")
    pf = P(phase)
    ff = F(phase)
    coeff = om / (lam * q)
    psi = om * pf / (lam**2 * q)
    theta = th * ff
    velocity = coeff * J * zeta * ff
    vort = om * sp.diff(ff, phase)

    # Work with an independent phase coordinate, then apply the chain rule
    # for s=lambda*zeta(t).x. This keeps all profile derivatives symbolic.
    def reduce_profile(expr):
        for n in range(5, 0, -1):
            expr = expr.subs(sp.diff(pf, phase, n), sp.diff(ff, phase, n - 1))
        return expr

    def dx(expr, j):
        return sp.diff(expr, x[j]) + lam * zeta[j] * sp.diff(expr, phase)

    def dt(expr):
        return (
            sp.diff(expr, z1) * zdot[0]
            + sp.diff(expr, z2) * zdot[1]
            + sp.diff(expr, th) * thdot
            + sp.diff(expr, om) * omdot
            + lam * zdot.dot(x) * sp.diff(expr, phase)
        )

    def adv(vector, expr):
        return sum(vector[j] * dx(expr, j) for j in range(2))

    def lap(expr):
        return sum(dx(dx(expr, j), j) for j in range(2))

    def grad(expr):
        return sp.Matrix([dx(expr, j) for j in range(2)])

    records = []

    def check(name, expression):
        entries = list(expression) if isinstance(expression, sp.MatrixBase) else [expression]
        residuals = [sp.cancel(sp.expand(reduce_profile(entry))) for entry in entries]
        assert all(value == 0 for value in residuals), (name, residuals)
        records.append({"name": name, "passed": True, "residual": [str(v) for v in residuals]})

    base_velocity = D * x
    check("trace_free", sp.trace(D))
    check("phase_transport", lam * (zdot + D.T * zeta).dot(x))
    check("streamfunction_velocity", J * grad(psi) - velocity)
    check("streamfunction_vorticity", lap(psi) - vort)
    check("velocity_divergence", dx(velocity[0], 0) + dx(velocity[1], 1))
    check("velocity_curl", dx(velocity[1], 0) - dx(velocity[0], 1) - vort)
    check("self_advection_temperature", adv(velocity, theta))
    check("self_advection_vorticity", adv(velocity, vort))
    check("self_advection_velocity", sp.Matrix([adv(velocity, velocity[j]) for j in range(2)]))

    scalar_residual = dt(theta) + adv(base_velocity, theta) + velocity.dot(g) + adv(velocity, theta)
    expected_scalar = (thdot + coeff * (J * zeta).dot(g)) * ff
    check("general_profile_scalar_residual", scalar_residual - expected_scalar)

    vort_residual = dt(vort) + adv(base_velocity, vort) + adv(velocity, vort) - dx(theta, 0)
    expected_vort = (omdot - lam * z1 * th) * sp.diff(ff, phase)
    check("general_profile_vorticity_residual", vort_residual - expected_vort)

    check(
        "general_profile_thermal_diffusion",
        scalar_residual - kappa * lap(theta)
        - (expected_scalar - kappa * lam**2 * q * th * sp.diff(ff, phase, 2)),
    )
    check(
        "general_profile_viscous_diffusion",
        vort_residual - nu * lap(vort)
        - (expected_vort - nu * lam**2 * q * om * sp.diff(ff, phase, 3)),
    )

    coeffdot = dt(coeff)
    h = coeffdot * J * zeta + 2 * coeff * D * J * zeta - th * e2
    momentum_increment = sp.Matrix([
        dt(velocity[j]) + adv(base_velocity, velocity[j])
        + adv(velocity, base_velocity[j]) + adv(velocity, velocity[j])
        - theta * e2[j] for j in range(2)
    ])
    check("general_profile_momentum_increment", momentum_increment - h * ff)
    check("momentum_curl_compatibility", (J * zeta).dot(h) - omdot / lam + z1 * th)
    pressure = -zeta.dot(h) * pf / (lam * q)
    check(
        "general_profile_pressure_lift",
        (momentum_increment + grad(pressure)).subs(omdot, lam * z1 * th),
    )
    inviscid_odes = {
        thdot: -coeff * (J * zeta).dot(g),
        omdot: lam * z1 * th,
    }
    check("inviscid_scalar_equation", scalar_residual.subs(inviscid_odes))
    check("inviscid_vorticity_equation", vort_residual.subs(inviscid_odes))

    sine_rules = {
        ff: sp.sin(phase),
        sp.diff(ff, phase): sp.cos(phase),
        sp.diff(ff, phase, 2): -sp.sin(phase),
        sp.diff(ff, phase, 3): -sp.cos(phase),
        sp.diff(ff, phase, 4): sp.sin(phase),
    }

    def to_sine(expr):
        # Derivative replacements must precede substitution of the base function.
        for n in range(4, 0, -1):
            expr = expr.subs(sp.diff(ff, phase, n), sine_rules[sp.diff(ff, phase, n)])
        return expr.subs(ff, sp.sin(phase))

    diffusive_odes = {
        thdot: -kappa * lam**2 * q * th - coeff * (J * zeta).dot(g),
        omdot: lam * z1 * th - nu * lam**2 * q * om,
    }
    check(
        "sine_diffusive_scalar_equation",
        to_sine(scalar_residual - kappa * lap(theta)).subs(diffusive_odes),
    )
    check(
        "sine_diffusive_vorticity_equation",
        to_sine(vort_residual - nu * lap(vort)).subs(diffusive_odes),
    )
    hnu = h + nu * lam**2 * q * coeff * J * zeta
    diffusive_momentum = momentum_increment - nu * sp.Matrix([lap(velocity[j]) for j in range(2)])
    check(
        "sine_diffusive_momentum_increment",
        to_sine(diffusive_momentum - hnu * ff),
    )
    pressure_nu = -zeta.dot(hnu) * pf / (lam * q)
    pressure_gradient = grad(pressure_nu).applyfunc(reduce_profile)
    check(
        "sine_diffusive_pressure_lift",
        (diffusive_momentum + pressure_gradient).applyfunc(to_sine).subs(diffusive_odes),
    )

    # Frozen hydrostatic background is exact even when both diffusivities are positive.
    A, r = sp.symbols("A r", positive=True)
    angle, mu = sp.symbols("phi mu", real=True)
    k = lam * r
    B = sp.Matrix([
        [-kappa * k**2, A * sp.sin(angle) / k],
        [k * sp.sin(angle), -nu * k**2],
    ])
    characteristic = (mu * sp.eye(2) - B).det()
    check(
        "frozen_characteristic_polynomial",
        characteristic - (
            mu**2 + (kappa + nu) * k**2 * mu
            + kappa * nu * k**4 - A * sp.sin(angle)**2
        ),
    )
    radicand = (kappa - nu)**2 * k**4 / 4 + A * sp.sin(angle)**2
    check(
        "growth_threshold_difference",
        radicand - (kappa + nu)**2 * k**4 / 4
        - (A * sp.sin(angle)**2 - kappa * nu * k**4),
    )
    inviscid_vector = sp.Matrix([1, k / sp.sqrt(A)])
    check(
        "inviscid_growing_eigenline_for_positive_sine",
        B.subs({kappa: 0, nu: 0}) * inviscid_vector
        - sp.sqrt(A) * sp.sin(angle) * inviscid_vector,
    )
    hydro_pressure = -A * x2**2 / 2
    check("frozen_hydrostatic_pressure", sp.Matrix([
        sp.diff(hydro_pressure, x1), sp.diff(hydro_pressure, x2)
    ]) - (-A * x2) * e2)

    # A time-dependent noncommuting affine amplitude matrix still commutes
    # with a scalar diffusion factor. Retain both original signed couplings.
    damping, damping_rate, alpha_c, beta_c = sp.symbols('damping damping_rate alpha_c beta_c', real=True)
    Zc = sp.Matrix([th, om])
    Ac = sp.Matrix([[0, -alpha_c], [beta_c, 0]])
    check('common_damping_through_time_dependent_coupling',
          -damping_rate*damping*Zc+damping*Ac*Zc
          -(Ac-damping_rate*sp.eye(2))*(damping*Zc))
    check('equal_diffusion_amplitude_matrix',
          B.subs(kappa, nu)-(B.subs({kappa:0,nu:0})-nu*k**2*sp.eye(2)))
    mode = sp.symbols('m', integer=True)
    check('phase_mode_diffusion_factor',sp.diff(sp.exp(sp.I*mode*phase),phase,2)
          +mode**2*sp.exp(sp.I*mode*phase))

    examples = []
    for label, diffusivity in [
        ("growing", sp.Rational(1, 100)),
        ("neutral", sp.Rational(1, 12)),
        ("decaying", sp.Integer(1)),
    ]:
        parameters = {A: 9, lam: 2, r: 3, angle: sp.pi / 2, kappa: diffusivity, nu: diffusivity}
        matrix = B.subs(parameters)
        rates = sorted(matrix.eigenvals().keys())
        margin = (A * sp.sin(angle)**2 - kappa * nu * k**4).subs(parameters)
        examples.append({
            "label": label,
            "A": "9", "lambda": "2", "r": "3", "phi": "pi/2",
            "kappa": str(diffusivity), "nu": str(diffusivity),
            "matrix": [[str(matrix[i, j]) for j in range(2)] for i in range(2)],
            "eigenvalues": [str(v) for v in rates],
            "threshold_margin": str(margin),
        })
    assert examples[0]["eigenvalues"][-1] == "66/25"
    assert examples[1]["eigenvalues"][-1] == "0"
    assert examples[2]["eigenvalues"][-1] == "-33"

    result = {
        "schema_version": 1,
        "artifact": "Exact affine Boussinesq core differential replay",
        "sympy_version": sp.__version__,
        "scope": "Local uncut general-profile wave, exact momentum pressure lift, and sine-mode diffusion; not finite-energy blowup or Navier–Stokes.",
        "source": "https://cims.nyu.edu/~tristanb/boussinesq.pdf",
        "source_location": "Sections 1.2 and 3.1, Lemma 3.1",
        "original_conventions": {
            "J": [[0, -1], [1, 0]],
            "buoyancy_direction": [0, 1],
            "vorticity": "partial_1 u_2 - partial_2 u_1",
            "domain": "R^2",
            "lambda": "positive, retained",
            "zeta": "nonzero, retained",
            "q": "|zeta|^2, named q to distinguish the thermal diffusion coefficient kappa",
        },
        "formulas": {
            "phase": "s=lambda*zeta.x; zeta_dot=-D^T*zeta",
            "general_profile": "theta_wave=Theta*F(s), psi=Omega*P(s)/(lambda^2*q), v=Omega*J*zeta*F(s)/(lambda*q), omega_wave=Omega*F'(s), P'=F",
            "inviscid_amplitudes": "Theta_dot=-(J*zeta.G)*Omega/(lambda*q); Omega_dot=lambda*zeta_1*Theta",
            "sine_diffusive_amplitudes": "Theta_dot=-kappa*lambda^2*q*Theta-(J*zeta.G)*Omega/(lambda*q); Omega_dot=lambda*zeta_1*Theta-nu*lambda^2*q*Omega",
            "frozen_matrix": [["-kappa*(lambda*r)^2", "A*sin(phi)/(lambda*r)"], ["lambda*r*sin(phi)", "-nu*(lambda*r)^2"]],
            "eigenvalues": "-(kappa+nu)*(lambda*r)^2/2 +/- sqrt((kappa-nu)^2*(lambda*r)^4/4+A*sin(phi)^2)",
            "positive_growth_iff": "A*sin(phi)^2 > kappa*nu*lambda^4*r^4",
        },
        "checks": records,
        "exact_rational_examples": examples,
        "all_passed": True,
    }
    output = Path(__file__).resolve().parents[1] / "checks" / "boussinesq_core_check.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"all_passed": True, "exact_checks": len(records), "rational_examples": len(examples), "output": str(output)}))


if __name__ == "__main__":
    main()
