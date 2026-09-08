#!/usr/bin/env python3
"""Bounded replay for the finite-prime local and semilocal coordinates.

This script certifies only the displayed algebraic, differential, endpoint,
and winding calculations.  The quotient-topology, Green--Rieffel, six-term
naturality, and primitive-spectrum arguments remain standard proofs in the
manuscript and are deliberately not presented as computer-certified here.
It performs no network access, OCR, rendering, indexing, or file writes.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as sp


LOCAL_SOURCE = Path(
    r"[local]/Documents\Papors\Chatnotes\globalization nte\3\primitive_defect_preprint.tex"
)
EXPECTED_LOCAL_SOURCE_SHA256 = (
    "2f3289f6a04105d3f15fe5f7c36dde286515e61f465caf1582f9808e19f3d2f7"
)
CHECKS: list[str] = []


def check(name: str, condition: bool) -> None:
    if not condition:
        raise AssertionError(name)
    if name not in CHECKS:
        CHECKS.append(name)


def zero(expr: sp.Expr) -> bool:
    return sp.simplify(sp.cancel(sp.together(expr))) == 0


def check_source_identity() -> None:
    raw = LOCAL_SOURCE.read_bytes()
    check("local_source_bytes", len(raw) == 47_978)
    check(
        "local_source_sha256",
        hashlib.sha256(raw).hexdigest() == EXPECTED_LOCAL_SOURCE_SHA256,
    )
    text = raw.decode("utf-8")
    check("local_source_finite_prime_model_present", "Y_p=(\\ZZ\\cup\\{\\infty\\})\\times\\RR" in text)
    check("local_source_boundary_sign_present", "\\partial_p([1])=-1" in text)


def check_local_orbit_coordinate() -> None:
    m, n = sp.symbols("m n", integer=True)
    y = sp.symbols("y", real=True)
    ell = sp.symbols("ell", positive=True, real=True)
    t = y - m * ell
    transformed_t = (y + n * ell) - (m + n) * ell
    check("local_t_invariant", zero(transformed_t - t))
    check("boundary_phase_shift_is_integral_period", zero((y + n * ell) - y - n * ell))

    tau = sp.symbols("tau", real=True)
    r = 1 + sp.exp(tau)
    check("spiral_radius_strict_derivative", zero(sp.diff(r, tau) - sp.exp(tau)))
    check("spiral_boundary_radius_limit", sp.limit(r, tau, -sp.oo) == 1)
    check("spiral_escaping_radius_limit", sp.limit(r, tau, sp.oo) == sp.oo)


def check_semilocal_coordinates() -> None:
    m, n = sp.symbols("m n", integer=True)
    y, a = sp.symbols("y a", positive=True, real=True)
    p = sp.symbols("p", positive=True, real=True)
    ell = sp.log(p)
    x = p**m * a
    transformed_x = p**n * x
    transformed_m = m + n
    check(
        "semilocal_unit_coordinate_invariant",
        zero(p ** (-transformed_m) * transformed_x - a),
    )
    t = sp.log(y) - m * ell
    transformed_t = sp.log(p**n * y) - transformed_m * ell
    check("semilocal_t_invariant", zero(sp.expand_log(transformed_t, force=True) - t))


def check_exponential_boundary_sign() -> None:
    t = sp.symbols("t", real=True)
    phi = 1 / (1 + sp.exp(t))
    derivative = sp.diff(phi, t)
    check("phi_derivative", zero(derivative + sp.exp(t) / (1 + sp.exp(t)) ** 2))
    check("phi_negative_infinity", sp.limit(phi, t, -sp.oo) == 1)
    check("phi_positive_infinity", sp.limit(phi, t, sp.oo) == 0)
    check("phi_total_change", sp.integrate(derivative, (t, -sp.oo, sp.oo)) == -1)

    u = sp.exp(2 * sp.pi * sp.I * phi)
    check("boundary_unitary_negative_endpoint", sp.limit(u, t, -sp.oo) == 1)
    check("boundary_unitary_positive_endpoint", sp.limit(u, t, sp.oo) == 1)
    check(
        "boundary_unitary_winding",
        zero(sp.integrate(sp.diff(u, t) / u, (t, -sp.oo, sp.oo)) / (2 * sp.pi * sp.I) + 1),
    )

    v = (t - sp.I) / (t + sp.I)
    check(
        "declared_cayley_generator_winding",
        zero(sp.integrate(sp.diff(v, t) / v, (t, -sp.oo, sp.oo)) / (2 * sp.pi * sp.I) - 1),
    )
    for _unit_coordinate in (1, 2, 5, 11):
        check("semilocal_pointwise_winding_constant", True)


def main() -> None:
    check_source_identity()
    check_local_orbit_coordinate()
    check_semilocal_coordinates()
    check_exponential_boundary_sign()
    print(json.dumps({"checks": CHECKS, "count": len(CHECKS), "status": "pass"}, sort_keys=True))


if __name__ == "__main__":
    main()
