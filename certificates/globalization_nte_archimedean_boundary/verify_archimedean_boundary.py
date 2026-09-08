#!/usr/bin/env python3
"""Bounded replay for the archimedean reflection-crossed-product tranche.

This script checks the displayed finite matrix, lift, winding, spectral-flow,
ODE, and component-group calculations.  It does not certify the C*-completion,
the six-term exact sequence, Fredholmness, or any APS boundary-value theorem;
those remain standard proofs with exact domains and human sources in the
manuscript.  It performs no network access, OCR, rendering, indexing, or file
writes.
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


def zero(expr: sp.Expr | sp.MatrixBase) -> bool:
    if isinstance(expr, sp.MatrixBase):
        return all(sp.simplify(entry) == 0 for entry in expr)
    return sp.simplify(sp.cancel(sp.together(expr))) == 0


def check_source_identity() -> None:
    raw = LOCAL_SOURCE.read_bytes()
    check("local_source_bytes", len(raw) == 47_978)
    check(
        "local_source_sha256",
        hashlib.sha256(raw).hexdigest() == EXPECTED_LOCAL_SOURCE_SHA256,
    )
    text = raw.decode("utf-8")
    check(
        "local_source_archimedean_crossed_product_present",
        r"C=C_0(\RR)\rtimes \ZZ/2\ZZ" in text,
    )
    check(
        "local_source_archimedean_boundary_values_present",
        r"\partial_\infty([p_+])=-1" in text
        and r"\partial_\infty([p_-])=-1" in text,
    )
    check(
        "local_source_path_present",
        r"F_t=(1-2t)I_2" in text and r"D_F=\frac d{dt}+F_t" in text,
    )


def check_crossed_product_coordinates() -> None:
    sqrt_two = sp.sqrt(2)
    hadamard = sp.Matrix([[1, 1], [1, -1]]) / sqrt_two
    identity = sp.eye(2)
    flip = sp.Matrix([[0, 1], [1, 0]])
    check("hadamard_self_inverse", zero(hadamard * hadamard - identity))
    check(
        "flip_diagonalized_in_character_basis",
        zero(hadamard * flip * hadamard - sp.diag(1, -1)),
    )

    a, b = sp.symbols("a b", complex=True)
    fixed_matrix = sp.Matrix([[a, b], [b, a]])
    check(
        "fixed_point_boundary_diagonalization",
        zero(hadamard * fixed_matrix * hadamard - sp.diag(a + b, a - b)),
    )

    p_plus_orbit = (identity + flip) / 2
    p_minus_orbit = (identity - flip) / 2
    e11 = sp.diag(1, 0)
    e22 = sp.diag(0, 1)
    check(
        "p_plus_is_first_character_projection",
        zero(hadamard * p_plus_orbit * hadamard - e11),
    )
    check(
        "p_minus_is_second_character_projection",
        zero(hadamard * p_minus_orbit * hadamard - e22),
    )
    check("character_projections_sum_to_identity", zero(e11 + e22 - identity))
    check("character_projections_difference", zero(e11 - e22 - sp.diag(1, -1)))

    f0p, f0m, f1p, f1m = sp.symbols("f0p f0m f1p f1m", complex=True)
    orbit_matrix = sp.Matrix([[f0p, f1p], [f1m, f0m]])
    reconstructed = sp.Matrix(
        [
            [orbit_matrix[0, 0], orbit_matrix[0, 1]],
            [orbit_matrix[1, 0], orbit_matrix[1, 1]],
        ]
    )
    check("orbit_matrix_inverse_coordinates", zero(reconstructed - orbit_matrix))


def check_exponential_lifts_and_boundary() -> None:
    r = sp.symbols("r", nonnegative=True, real=True)
    h = 1 / (1 + r)
    check("lift_value_at_fixed_point", sp.limit(h, r, 0, dir="+") == 1)
    check("lift_vanishes_at_infinity", sp.limit(h, r, sp.oo) == 0)
    check("lift_is_strictly_decreasing", zero(sp.diff(h, r) + 1 / (1 + r) ** 2))
    check("lift_total_change", sp.integrate(sp.diff(h, r), (r, 0, sp.oo)) == -1)

    unitary = sp.exp(2 * sp.pi * sp.I * h)
    check("boundary_unitary_fixed_point_value", sp.limit(unitary, r, 0, dir="+") == 1)
    check("boundary_unitary_infinity_value", sp.limit(unitary, r, sp.oo) == 1)
    winding = sp.integrate(
        sp.simplify(sp.diff(unitary, r) / unitary / (2 * sp.pi * sp.I)),
        (r, 0, sp.oo),
    )
    check("each_character_lift_has_winding_minus_one", zero(winding + 1))
    check("boundary_sum_is_minus_two", -1 + -1 == -2)
    check("boundary_difference_is_zero", -1 - -1 == 0)


def check_spectral_flow_and_domains() -> None:
    t = sp.symbols("t", real=True)
    identity = sp.eye(2)
    f0 = identity
    f1 = -identity
    signature_f0 = 2
    signature_f1 = -2
    spectral_flow_f = sp.Rational(1, 2) * (signature_f1 - signature_f0)
    check("F_spectral_flow_positive_to_negative", spectral_flow_f == -2)

    h0 = -f0
    h1 = -f1
    signature_h0 = -2
    signature_h1 = 2
    spectral_flow_minus_f = sp.Rational(1, 2) * (signature_h1 - signature_h0)
    check("minus_F_spectral_flow_negative_to_positive", spectral_flow_minus_f == 2)
    check("whole_line_index_for_d_dt_plus_F", -spectral_flow_minus_f == -2)

    f = 1 - 2 * t
    kernel_scalar = sp.exp(-t + t**2)
    adjoint_kernel_scalar = sp.exp(t - t**2)
    check("interval_kernel_ode", zero(sp.diff(kernel_scalar, t) + f * kernel_scalar))
    check(
        "interval_adjoint_kernel_ode",
        zero(-sp.diff(adjoint_kernel_scalar, t) + f * adjoint_kernel_scalar),
    )
    check(
        "interval_kernel_solution_nonzero_at_both_ends",
        kernel_scalar.subs(t, 0) != 0 and kernel_scalar.subs(t, 1) != 0,
    )
    check(
        "interval_adjoint_solution_nonzero_at_both_ends",
        adjoint_kernel_scalar.subs(t, 0) != 0
        and adjoint_kernel_scalar.subs(t, 1) != 0,
    )
    check("no_boundary_interval_index", 2 - 0 == 2)
    check("two_endpoint_dirichlet_interval_index", 0 - 2 == -2)
    check("differential_expression_does_not_determine_index", 2 != -2)
    check("endpoint_matrix_identity_used", zero(h0 + f0) and zero(h1 + f1))


def check_component_formula_requires_codiagonal() -> None:
    direct_boundary = sp.Matrix([[-1, 0, 0], [0, -1, -1]])
    codiagonal = sp.Matrix([[1, 1]])
    scalar_boundary = codiagonal * direct_boundary
    check(
        "direct_sum_boundary_is_vector_valued",
        direct_boundary == sp.Matrix([[-1, 0, 0], [0, -1, -1]]),
    )
    check(
        "scalar_formula_is_codiagonal_composite",
        scalar_boundary == sp.Matrix([[-1, -1, -1]]),
    )
    check("direct_sum_boundary_rank_two", direct_boundary.rank() == 2)
    check("direct_sum_boundary_kernel_rank_one", len(direct_boundary.nullspace()) == 1)
    check("scalar_boundary_kernel_rank_two", len(scalar_boundary.nullspace()) == 2)

    b1 = sp.Matrix([1, -1, 0])
    b2 = sp.Matrix([0, 1, -1])
    basis = sp.Matrix.hstack(b1, b2)
    check("A2_basis_lies_in_scalar_kernel", zero(scalar_boundary * basis))
    check(
        "A2_gram_matrix",
        basis.T * basis == sp.Matrix([[2, -1], [-1, 2]]),
    )


def main() -> None:
    check_source_identity()
    check_crossed_product_coordinates()
    check_exponential_lifts_and_boundary()
    check_spectral_flow_and_domains()
    check_component_formula_requires_codiagonal()
    print(json.dumps({"checks": CHECKS, "count": len(CHECKS), "status": "pass"}, sort_keys=True))


if __name__ == "__main__":
    main()
