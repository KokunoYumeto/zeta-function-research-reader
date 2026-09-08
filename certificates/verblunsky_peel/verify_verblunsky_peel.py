#!/usr/bin/env python3
"""Exact symbolic replay for the phase-rotated Verblunsky derivative peel."""

from __future__ import annotations

import json
import platform

import sympy as sp


def exact_zero(expr: sp.Expr, name: str, checks: list[dict[str, str]]) -> None:
    value = sp.factor(sp.cancel(expr))
    if value != 0:
        raise AssertionError(f"{name}: expected 0, obtained {value}")
    checks.append({"name": name, "status": "exact_zero"})


def conjugate_polynomial(coefficients: list[sp.Expr]) -> list[sp.Expr]:
    return [sp.conjugate(value) for value in reversed(coefficients)]


def polynomial_value_at_one(coefficients: list[sp.Expr]) -> sp.Expr:
    return sp.expand(sum(coefficients))


def polynomial_derivative_at_one(coefficients: list[sp.Expr]) -> sp.Expr:
    return sp.expand(sum(index * value for index, value in enumerate(coefficients)))


def szego_step(coefficients: list[sp.Expr], alpha: sp.Expr) -> list[sp.Expr]:
    shifted = [sp.Integer(0), *coefficients]
    reversed_coefficients = conjugate_polynomial(coefficients)
    padded_reversed = [*reversed_coefficients, sp.Integer(0)]
    return [
        sp.expand(left - sp.conjugate(alpha) * right)
        for left, right in zip(shifted, padded_reversed, strict=True)
    ]


def finite_ladder_check(
    size: int, disk_betas: list[sp.Expr], terminal_beta: sp.Expr, checks: list[dict[str, str]]
) -> None:
    if len(disk_betas) != max(size - 1, 0):
        raise AssertionError("wrong disk-beta count")

    betas = [*disk_betas, terminal_beta]
    phi = [sp.Integer(1)]
    product = sp.Integer(1)

    for n, beta in enumerate(betas):
        a_value = polynomial_value_at_one(phi)
        d_value = polynomial_derivative_at_one(phi)
        u_value = sp.cancel(d_value / a_value)
        alpha = sp.cancel(sp.conjugate(beta) * sp.conjugate(a_value) / a_value)
        recovered_beta = sp.cancel(sp.conjugate(alpha) * sp.conjugate(a_value) / a_value)
        exact_zero(recovered_beta - beta, f"N={size}, n={n}: triangular beta recovery", checks)

        eta = sp.cancel((size - 1 - sp.conjugate(u_value)) / (size - n + u_value))
        product = sp.cancel(product * (1 - beta * eta))
        phi_next = szego_step(phi, alpha)

        if n < size - 1:
            next_a = polynomial_value_at_one(phi_next)
            next_d = polynomial_derivative_at_one(phi_next)
            next_u = sp.cancel(next_d / next_a)
            transition = sp.cancel(
                (1 + u_value - beta * (n - sp.conjugate(u_value))) / (1 - beta)
            )
            exact_zero(next_u - transition, f"N={size}, n={n}: polynomial T transition", checks)

        phi = phi_next

    derivative = polynomial_derivative_at_one(phi)
    exact_zero(product - derivative / size, f"N={size}: complete derivative telescope", checks)


def main() -> None:
    checks: list[dict[str, str]] = []

    a, a_bar, d, d_bar, alpha_bar = sp.symbols("A Abar D Dbar alphabar", nonzero=True)
    beta = sp.cancel(alpha_bar * a_bar / a)
    u = sp.cancel(d / a)
    u_bar = sp.cancel(d_bar / a_bar)
    n, size = sp.symbols("n N", integer=True)
    next_a = a - alpha_bar * a_bar
    next_d = a + d - alpha_bar * (n * a_bar - d_bar)
    transition = (1 + u - beta * (n - u_bar)) / (1 - beta)
    exact_zero(next_d / next_a - transition, "differentiated Szego transition", checks)

    b, b_bar, w, w_bar = sp.symbols("beta betabar w wbar")
    next_w = (w + 1 + b * (w_bar + 1)) / (1 - b)
    next_w_bar = (w_bar + 1 + b_bar * (w + 1)) / (1 - b_bar)
    real_next_w = (next_w + next_w_bar) / 2
    claimed_real_next_w = (
        (1 - b * b_bar) * ((w + w_bar) / 2 + 1) / ((1 - b) * (1 - b_bar))
    )
    exact_zero(real_next_w - claimed_real_next_w, "half-plane real-part transport", checks)

    state, state_bar = sp.symbols("u ubar")
    eta_difference = (size - n + state) * (size - n + state_bar) - (
        size - 1 - state_bar
    ) * (size - 1 - state)
    claimed_eta_difference = (2 * size - n - 1) * (1 - n + state + state_bar)
    exact_zero(eta_difference - claimed_eta_difference, "eta modulus-square difference", checks)

    next_state = (1 + state - b * (n - state_bar)) / (1 - b)
    eta = (size - 1 - state_bar) / (size - n + state)
    exact_zero(
        (1 - b) * (size - n - 1 + next_state)
        - (size - n + state) * (1 - b * eta),
        "one-step telescope",
        checks,
    )

    recovered_alpha = b_bar * a_bar / a
    recovered_alpha_bar = b * a / a_bar
    exact_zero(recovered_alpha_bar * a_bar / a - b, "triangular inverse recovers beta", checks)
    exact_zero(a - recovered_alpha_bar * a_bar - a * (1 - b), "A transition under inverse", checks)

    m = sp.symbols("m", integer=True, positive=True)
    exact_zero((2 * m + 1 - 1) / 2 - m, "Theta-to-mu density coefficient", checks)
    exact_zero((2 * m + 1 - 3) / 2 - (m - 1), "Theta-to-mu density exponent", checks)

    disk_pool = [
        (1 + sp.I) / 5,
        (-2 + sp.I) / 6,
        (1 - 2 * sp.I) / 7,
        (-1 - sp.I) / 4,
        (2 - sp.I) / 8,
    ]
    terminal_pool = [
        sp.Integer(1),
        (3 + 4 * sp.I) / 5,
        (-5 + 12 * sp.I) / 13,
        -sp.I,
        (-3 + 4 * sp.I) / 5,
        sp.I,
    ]
    for finite_size in range(1, 7):
        finite_ladder_check(
            finite_size,
            disk_pool[: max(finite_size - 1, 0)],
            terminal_pool[finite_size - 1],
            checks,
        )

    output = {
        "certificate_id": "CERT-VERBLUNSKY-PEEL-20260826-0001",
        "status": "pass",
        "arithmetic": "exact SymPy rational/Gaussian-rational algebra",
        "python": platform.python_version(),
        "sympy": sp.__version__,
        "check_count": len(checks),
        "checks": checks,
        "scope_boundary": [
            "finite algebra and exact finite-ladder replay only",
            "the conditional-independence/product-measure argument remains a written proof",
            "no video frame, asymptotic CUE theorem, or zeta-zero statement is certified",
        ],
    }
    print(json.dumps(output, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
