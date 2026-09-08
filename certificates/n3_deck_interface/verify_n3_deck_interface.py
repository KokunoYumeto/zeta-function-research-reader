"""Exact symbolic certificate for the first-peeled N=3/deck-curve interface.

The script verifies the rational and polynomial identities in the written
coordinate proof.  The fibre classifications, denominator inequalities, and
fixed-locus obstruction are elementary set-theoretic arguments retained in
the TeX proof rather than delegated to symbolic cancellation.
"""

from __future__ import annotations

import json
import platform

import sympy as sp


CERTIFICATE_ID = "CERT-N3-DECK-20260826-0001"


def main() -> None:
    x, y, u, v, j = sp.symbols("x y u v j", real=True)
    imaginary_unit = sp.I
    checks: list[str] = []

    def check_zero(name: str, expression: sp.Expr) -> None:
        reduced = sp.factor(sp.cancel(sp.together(sp.expand(expression))))
        if reduced != 0:
            raise AssertionError(f"{name}: nonzero remainder {reduced}")
        checks.append(name)

    # The affine deck curve is b^2=1+4a, parametrized by
    # F(s)=(s(s-1),2s-1) with inverse s=(b+1)/2.
    s = sp.symbols("s")
    a_from_s = s * (s - 1)
    b_from_s = 2 * s - 1
    check_zero("deck_curve_parametrization", b_from_s**2 - 1 - 4 * a_from_s)
    check_zero("deck_curve_left_inverse", (b_from_s + 1) / 2 - s)

    a, b = sp.symbols("a b")
    s_from_b = (b + 1) / 2
    reconstructed_a = s_from_b * (s_from_b - 1)
    curve_relation_remainder = sp.rem(
        sp.together(reconstructed_a - a).as_numer_denom()[0],
        b**2 - 1 - 4 * a,
        b,
    )
    check_zero("deck_curve_right_inverse_modulo_curve", curve_relation_remainder)

    # Lossless carrier map: use the full recovered beta_0 as the deck parameter.
    beta = x + imaginary_unit * y
    beta_conjugate = x - imaginary_unit * y
    a_carrier = beta * (beta - 1)
    b_carrier = 2 * beta - 1
    check_zero("carrier_lands_on_deck_curve", b_carrier**2 - 1 - 4 * a_carrier)
    check_zero("carrier_inverse_recovers_beta", (b_carrier + 1) / 2 - beta)

    # Comparing physical conjugation with the target deck involution gives the
    # exact equality condition conjugate(beta)=1-beta, i.e. 2*x-1=0.
    check_zero(
        "carrier_parameter_equivariance_defect",
        beta_conjugate - (1 - beta) - (2 * x - 1),
    )
    carrier_conjugate_a = beta_conjugate * (beta_conjugate - 1)
    carrier_conjugate_b = 2 * beta_conjugate - 1
    decked_carrier_a = a_carrier
    decked_carrier_b = -b_carrier
    check_zero(
        "carrier_first_coordinate_equivariance_defect_factor",
        carrier_conjugate_a
        - decked_carrier_a
        + 2 * imaginary_unit * y * (2 * x - 1),
    )
    check_zero(
        "carrier_second_coordinate_equivariance_defect",
        carrier_conjugate_b - decked_carrier_b - 2 * (2 * x - 1),
    )

    # Equivariant sheet map: retain y and send s_sheet=1/2+i*y.
    s_sheet = sp.Rational(1, 2) + imaginary_unit * y
    a_sheet = s_sheet * (s_sheet - 1)
    b_sheet = 2 * s_sheet - 1
    check_zero("sheet_first_coordinate", a_sheet + sp.Rational(1, 4) + y**2)
    check_zero("sheet_second_coordinate", b_sheet - 2 * imaginary_unit * y)
    check_zero("sheet_lands_on_deck_curve", b_sheet**2 - 1 - 4 * a_sheet)
    check_zero(
        "sheet_map_equivariance_first_coordinate",
        a_sheet.subs(y, -y) - a_sheet,
    )
    check_zero(
        "sheet_map_equivariance_second_coordinate",
        b_sheet.subs(y, -y) + b_sheet,
    )

    # Translate the sheet map into the physical (u,v,J) coordinates.
    h = 1 - 3 * u + 8 * v
    denominator = (u - 1) * h
    discriminant = 18 * u + 32 * v - 1 - (9 * u - 16 * v) ** 2
    cover_s = (u - 1) ** 2 * discriminant / 1024
    y_from_j = -8 * imaginary_unit * j / denominator
    s_sheet_from_j = sp.Rational(1, 2) + 8 * j / denominator
    check_zero(
        "physical_sheet_parameter_equals_half_plus_i_y",
        s_sheet_from_j - (sp.Rational(1, 2) + imaginary_unit * y_from_j),
    )
    a_sheet_from_j = s_sheet_from_j * (s_sheet_from_j - 1)
    b_sheet_from_j = 2 * s_sheet_from_j - 1
    check_zero(
        "physical_sheet_second_coordinate",
        b_sheet_from_j - 16 * j / denominator,
    )
    check_zero(
        "physical_sheet_first_coordinate",
        a_sheet_from_j - (64 * j**2 / denominator**2 - sp.Rational(1, 4)),
    )
    base_expression = -sp.Rational(1, 4) - discriminant / (16 * h**2)
    base_difference = sp.together(a_sheet_from_j - base_expression)
    base_numerator = sp.expand(base_difference.as_numer_denom()[0])
    base_remainder = sp.rem(base_numerator, j**2 + cover_s, j)
    check_zero("physical_sheet_base_square_modulo_cover", base_remainder)
    check_zero(
        "physical_sheet_curve_equation",
        b_sheet_from_j**2 - 1 - 4 * a_sheet_from_j,
    )
    check_zero(
        "physical_sheet_equivariance_first_coordinate",
        a_sheet_from_j.subs(j, -j) - a_sheet_from_j,
    )
    check_zero(
        "physical_sheet_equivariance_second_coordinate",
        b_sheet_from_j.subs(j, -j) + b_sheet_from_j,
    )

    # The recovered beta_0 used by the carrier is exactly x+i*y in the
    # existing inverse coordinates.
    x_from_uv = (1 - 9 * u + 32 * v) / (4 * h)
    beta_from_uvj = x_from_uv + 8 * j / denominator
    check_zero(
        "physical_carrier_beta_coordinate",
        beta_from_uvj - (x_from_uv + imaginary_unit * y_from_j),
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
            "source": "(u,v,J) in the physical first-peeled N=3 cover",
            "recovered_beta": "(1-9u+32v)/(4h)+8J/((u-1)h)",
            "target_curve": "C_ab={(a,b): b^2=1+4a}",
            "carrier_parameter": "s=beta_0",
            "equivariant_sheet_parameter": "s_sheet=1/2+8J/((u-1)h)=1/2+i*y",
        },
        "human_proof_obligations": [
            "h>0 and u<1 make every displayed denominator nonzero.",
            "The carrier is a bijection onto F(D) because the existing lifted map and F are bijections.",
            "The sheet-map fibres are the exact horizontal open intervals at fixed y.",
            "No equivariant injective set map exists because the source involution has an interval of fixed points and the target deck involution has one fixed point.",
        ],
        "nonclaims": [
            "The carrier map is not asserted to intertwine the two involutions outside Re(beta_0)=1/2.",
            "The equivariant sheet map is not injective and does not retain the real coordinate x.",
            "No zeta-zero, critical-line, or CUE-distribution consequence is asserted.",
        ],
    }
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
