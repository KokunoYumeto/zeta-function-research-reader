"""Exact symbolic certificate for the first peeled N=3 CUE phase cover.

The script verifies the polynomial and rational identities used in the written
coordinate proof.  It does not certify the semialgebraic inequalities or any
interface to the separate quotient/lift curve; those remain in the human proof.
"""

from __future__ import annotations

import json
import platform

import sympy as sp


CERTIFICATE_ID = "CERT-N3-PHASE-20260825-0001"


def main() -> None:
    x, y, u, v, j, x_coord = sp.symbols("x y u v j X", real=True)
    imaginary_unit = sp.I
    checks: list[str] = []

    def check_zero(name: str, expression: sp.Expr) -> None:
        reduced = sp.factor(sp.cancel(sp.together(sp.expand(expression))))
        if reduced != 0:
            raise AssertionError(f"{name}: nonzero remainder {reduced}")
        checks.append(name)

    radius_squared = x**2 + y**2
    denominator = 9 - 12 * x + 4 * radius_squared
    lambda_numerator = 1 - 4 * x + 4 * radius_squared
    d_numerator = 4 - 4 * x + radius_squared

    u_xy = lambda_numerator / denominator
    v_xy = radius_squared / denominator
    w_xy = d_numerator / denominator

    beta = x + imaginary_unit * y
    beta_bar = x - imaginary_unit * y
    rationalized_z_numerator = (
        beta_bar
        * (2 - beta_bar)
        * (1 - 2 * beta)
        * (3 - 2 * beta)
    )
    expanded_z_numerator = sp.expand_complex(rationalized_z_numerator)
    real_z_numerator = sp.re(expanded_z_numerator)
    imaginary_z_numerator = sp.im(expanded_z_numerator)

    expected_real_z_numerator = (
        -4 * radius_squared**2
        + 16 * radius_squared * x
        - 13 * radius_squared
        - 6 * x**2
        + 6 * x
    )
    expected_imaginary_z_numerator = 6 * y * (x - 1)
    check_zero(
        "rationalized_Z_real_part",
        real_z_numerator - expected_real_z_numerator,
    )
    check_zero(
        "rationalized_Z_imaginary_part",
        imaginary_z_numerator - expected_imaginary_z_numerator,
    )

    check_zero(
        "w_equals_one_minus_u_plus_two_v_over_two",
        2 * d_numerator - (denominator - lambda_numerator + 2 * radius_squared),
    )

    trace_numerator = (
        9 * lambda_numerator**2
        - 16 * lambda_numerator * radius_squared
        - 10 * lambda_numerator * denominator
        - 16 * radius_squared * denominator
        + denominator**2
    )
    check_zero(
        "Z_plus_conjugate_Z_trace_identity",
        trace_numerator - 32 * real_z_numerator,
    )

    conjugate_z_numerator = sp.conjugate(rationalized_z_numerator)
    check_zero(
        "Z_times_conjugate_Z_norm_identity",
        rationalized_z_numerator * conjugate_z_numerator
        - lambda_numerator * radius_squared * d_numerator * denominator,
    )

    h = 1 - 3 * u + 8 * v
    g = 1 - 3 * u + 2 * v
    discriminant = 18 * u + 32 * v - 1 - (9 * u - 16 * v) ** 2
    x_inverse = (1 - 9 * u + 32 * v) / (4 * h)
    radius_squared_inverse = 6 * v / h
    y_squared_inverse = discriminant / (16 * h**2)

    check_zero(
        "inverse_radius_is_x_squared_plus_y_squared",
        radius_squared_inverse - x_inverse**2 - y_squared_inverse,
    )
    check_zero(
        "inverse_denominator",
        9 - 12 * x_inverse + 4 * radius_squared_inverse - 6 / h,
    )
    check_zero(
        "inverse_u_coordinate",
        1 - 4 * x_inverse + 4 * radius_squared_inverse - 6 * u / h,
    )
    check_zero("inverse_v_coordinate", radius_squared_inverse / (6 / h) - v)
    check_zero("open_disk_inequality_coordinate", 1 - radius_squared_inverse - g / h)
    check_zero("h_decomposition", h - g - 6 * v)

    h_xy = 1 - 3 * u_xy + 8 * v_xy
    g_xy = 1 - 3 * u_xy + 2 * v_xy
    discriminant_xy = discriminant.subs({u: u_xy, v: v_xy})
    check_zero("forward_h_is_six_over_D", h_xy - 6 / denominator)
    check_zero(
        "forward_g_is_six_times_one_minus_radius_over_D",
        g_xy - 6 * (1 - radius_squared) / denominator,
    )
    check_zero(
        "forward_discriminant_is_sixteen_h_squared_y_squared",
        discriminant_xy - 16 * h_xy**2 * y**2,
    )

    x_from_uv = 9 * u - 16 * v + 1
    delta_trace = 36 * u - x_from_uv**2
    check_zero("two_discriminants_are_identical", delta_trace - discriminant)

    trace = (9 * u**2 - 16 * u * v - 10 * u - 16 * v + 1) / 16
    norm = u * v * (1 - u + 2 * v) / 2
    s_direct = norm - trace**2 / 4
    s_factored = (u - 1) ** 2 * delta_trace / 1024
    check_zero("quadratic_trace_S_factorization", s_direct - s_factored)

    j_xy = imaginary_unit * imaginary_z_numerator / denominator**2
    check_zero(
        "J_coordinate_formula",
        j_xy - imaginary_unit * y * (u_xy - 1) * h_xy / 8,
    )
    check_zero(
        "physical_J_satisfies_quadratic_cover",
        j_xy**2 + s_factored.subs({u: u_xy, v: v_xy}),
    )

    y_from_j = -8 * imaginary_unit * j / ((u - 1) * h)
    check_zero(
        "lifted_inverse_recovers_J",
        imaginary_unit * y_from_j * (u - 1) * h / 8 - j,
    )
    inverse_sheet_expression = sp.together(
        y_from_j**2 - discriminant / (16 * h**2)
    )
    inverse_sheet_numerator = sp.expand(inverse_sheet_expression.as_numer_denom()[0])
    inverse_sheet_remainder = sp.rem(
        inverse_sheet_numerator,
        j**2 + s_factored,
        j,
    )
    check_zero("lifted_inverse_sheet_relation_modulo_cover", inverse_sheet_remainder)

    v_from_x = (9 * u + 1 - x_coord) / 16
    check_zero(
        "affine_u_v_to_u_X_inverse",
        (9 * u - 16 * v_from_x + 1) - x_coord,
    )
    check_zero(
        "affine_u_X_to_u_v_inverse",
        v_from_x.subs(x_coord, x_from_uv) - v,
    )

    output = {
        "certificate_id": CERTIFICATE_ID,
        "status": "pass",
        "python": platform.python_version(),
        "sympy": sp.__version__,
        "arithmetic": "exact symbolic polynomial and rational identities",
        "checks": checks,
        "check_count": len(checks),
        "coordinates": {
            "domain": "beta_0=x+i*y with x^2+y^2<1",
            "base": "u=|lambda|^2, v=|c|^2",
            "sheet": "J=Z-(Z+conjugate(Z))/2",
            "base_discriminant": "18*u+32*v-1-(9*u-16*v)^2",
            "trace_discriminant": "36*u-(9*u-16*v+1)^2",
        },
        "nonclaims": [
            "Inequality signs and semialgebraic surjectivity are proved in the TeX, not by symbolic cancellation.",
            "No map to the separate s(s-1), 2s-1 quotient/lift curve is asserted.",
            "No zeta-zero or critical-line consequence is asserted.",
        ],
    }
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
