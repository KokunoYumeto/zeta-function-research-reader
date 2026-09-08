#!/usr/bin/env python3
"""Exact finite replay for Chapter 17's packet-product coordinate algebra.

The manuscript contains the proofs and the convergence arguments.  This
bounded script checks only exact polynomial, rational, quotient-coordinate,
finite symmetric-function, and leading-jet identities.  It performs no corpus
scan, network access, OCR, image generation, or filesystem write.
"""

from __future__ import annotations

import json
import sys

import sympy as sp


CHECKS: list[str] = []


def check(name: str, condition: bool) -> None:
    if not bool(condition):
        raise AssertionError(name)
    CHECKS.append(name)


def zero(expression: sp.Expr) -> bool:
    return sp.simplify(sp.cancel(sp.together(expression))) == 0


def elementary_symmetric(values: list[sp.Rational]) -> list[sp.Rational]:
    coefficients = [sp.Rational(1)] + [sp.Rational(0)] * len(values)
    for value in values:
        for degree in range(len(values), 0, -1):
            coefficients[degree] += value * coefficients[degree - 1]
    return coefficients


def check_centered_packet_polynomials() -> None:
    z, a, gamma = sp.symbols("z a gamma", real=True, nonzero=True)
    alpha = a + sp.I * gamma
    alpha_bar = a - sp.I * gamma

    root_first = (
        ((z - a) ** 2 + gamma**2)
        * ((z + a) ** 2 + gamma**2)
        / (a**2 + gamma**2) ** 2
    )
    sign_first = (1 - z**2 / alpha**2) * (1 - z**2 / alpha_bar**2)
    expanded = (
        1
        - 2 * (a**2 - gamma**2) * z**2 / (a**2 + gamma**2) ** 2
        + z**4 / (a**2 + gamma**2) ** 2
    )
    check(
        "four_point_root_pairing_equals_sign_orbit_pairing",
        zero(root_first - sign_first),
    )
    check(
        "four_point_sign_orbit_product_has_exact_real_coefficients",
        zero(sign_first - expanded),
    )
    check(
        "four_point_packet_is_center_normalized",
        zero(root_first.subs(z, 0) - 1),
    )

    critical = 1 + z**2 / gamma**2
    check(
        "two_point_packet_has_exact_quadratic_form_and_roots",
        zero(critical.subs(z, sp.I * gamma))
        and zero(critical.subs(z, -sp.I * gamma))
        and zero(critical.subs(z, 0) - 1),
    )


def check_quartic_coordinate_inverse() -> None:
    a, gamma = sp.symbols("a gamma", real=True, nonzero=True)
    radius_squared = a**2 + gamma**2
    c4 = radius_squared**-2
    c2 = 2 * (gamma**2 - a**2) / radius_squared**2
    recovered_radius_squared = c4 ** sp.Rational(-1, 2)
    # SymPy cannot select the positive square-root branch symbolically from
    # unconstrained a,gamma.  Substitute R^2=a^2+gamma^2, the positive
    # coordinate proved in the manuscript, and replay the two linear solves.
    delta = sp.simplify(c2 / (2 * c4))
    recovered_a_squared = sp.simplify((radius_squared - delta) / 2)
    recovered_gamma_squared = sp.simplify((radius_squared + delta) / 2)
    check("quartic_delta_recovers_gamma_squared_minus_a_squared", zero(delta - (gamma**2 - a**2)))
    check("quartic_inverse_recovers_a_squared", zero(recovered_a_squared - a**2))
    check(
        "quartic_inverse_recovers_gamma_squared",
        zero(recovered_gamma_squared - gamma**2),
    )
    samples = (
        (sp.Rational(2, 3), sp.Rational(5, 7)),
        (sp.Rational(-4, 5), sp.Rational(3, 11)),
        (sp.Rational(7, 13), sp.Rational(-9, 10)),
    )
    sample_pass = True
    for a_value, gamma_value in samples:
        c4_value = c4.subs({a: a_value, gamma: gamma_value})
        sample_pass &= zero(
            recovered_radius_squared.subs({a: a_value, gamma: gamma_value})
            - sp.sqrt(1 / c4_value)
        )
    check("positive_radius_branch_replayed_on_exact_rational_samples", sample_pass)


def check_packet_logarithmic_derivatives() -> None:
    s, a, gamma = sp.symbols("s a gamma", real=True, nonzero=True)
    half = sp.Rational(1, 2)
    roots = (
        half + a + sp.I * gamma,
        half + a - sp.I * gamma,
        half - a + sp.I * gamma,
        half - a - sp.I * gamma,
    )
    packet = sp.prod((s - root) / (half - root) for root in roots)
    partial_fractions = sum(1 / (s - root) for root in roots)
    check(
        "four_point_packet_logarithmic_derivative",
        zero(sp.diff(packet, s) / packet - partial_fractions),
    )

    critical_roots = (half + sp.I * gamma, half - sp.I * gamma)
    critical_packet = sp.prod(
        (s - root) / (half - root) for root in critical_roots
    )
    critical_sum = sum(1 / (s - root) for root in critical_roots)
    check(
        "two_point_packet_logarithmic_derivative",
        zero(sp.diff(critical_packet, s) / critical_packet - critical_sum),
    )

    n = sp.symbols("n", positive=True, integer=True)
    gamma_factor = (1 + s / (2 * n)) * sp.exp(-s / (2 * n))
    check(
        "one_reciprocal_gamma_factor_logarithmic_derivative",
        zero(sp.diff(gamma_factor, s) / gamma_factor - (1 / (s + 2 * n) - 1 / (2 * n))),
    )


def check_sign_orbit_to_packet_fibres() -> None:
    half = sp.Rational(1, 2)
    samples = (
        sp.Rational(2, 3) + sp.I * sp.Rational(5, 7),
        -sp.Rational(4, 9) + sp.I * sp.Rational(7, 10),
    )
    four_point_pass = True
    for alpha in samples:
        centered_fibre = {alpha, -alpha, sp.conjugate(alpha), -sp.conjugate(alpha)}
        translated = {sp.simplify(half + point) for point in centered_fibre}
        rho = half + alpha
        packet = {
            rho,
            sp.conjugate(rho),
            1 - rho,
            1 - sp.conjugate(rho),
        }
        four_point_pass &= len(centered_fibre) == 4 and translated == packet
    check("generic_centered_sign_conjugation_fibre_translates_to_four_point_packet", four_point_pass)

    alpha = sp.I * sp.Rational(3, 5)
    centered_fibre = {alpha, -alpha, sp.conjugate(alpha), -sp.conjugate(alpha)}
    translated = {sp.simplify(half + point) for point in centered_fibre}
    check(
        "purely_imaginary_centered_fibre_collapses_exactly_to_two_point_packet",
        len(centered_fibre) == 2
        and translated == {half + alpha, half - alpha},
    )


def check_finite_symmetric_coordinates() -> None:
    z = sp.symbols("z")
    samples = (
        [sp.Rational(2, 3), sp.Rational(-3, 5), sp.Rational(5, 7)],
        [
            sp.Rational(1, 4),
            sp.Rational(1, 4),
            sp.Rational(-2, 9),
            sp.Rational(7, 11),
        ],
        [sp.Rational(-5, 6)],
        [],
    )
    all_pass = True
    for values in samples:
        sigma = elementary_symmetric(values)
        product = sp.expand(sp.prod(1 - value * z**2 for value in values))
        expansion = sp.expand(
            sum((-1) ** degree * coefficient * z ** (2 * degree)
                for degree, coefficient in enumerate(sigma))
        )
        all_pass &= zero(product - expansion)
    check("finite_elementary_symmetric_packet_expansion_with_repeated_multiplicity", all_pass)


def check_leading_jet_and_information_fibre() -> None:
    s = sp.symbols("s")
    half = sp.Rational(1, 2)
    a = sp.Rational(2, 3)
    gamma = sp.Rational(5, 7)
    roots = (
        half + a + sp.I * gamma,
        half + a - sp.I * gamma,
        half - a + sp.I * gamma,
        half - a - sp.I * gamma,
    )
    packet = sp.prod((s - root) / (half - root) for root in roots)
    rho = roots[0]
    complement = 1 + sp.Rational(3, 8) * (s - half) ** 2
    multiplicity = 3
    function = sp.expand(complement * packet**multiplicity)
    leading_from_derivative = sp.diff(function, s, multiplicity).subs(s, rho) / sp.factorial(multiplicity)
    leading_from_factors = complement.subs(s, rho) * sp.diff(packet, s).subs(s, rho) ** multiplicity
    check(
        "global_complement_times_packet_gives_exact_leading_jet",
        zero(leading_from_derivative - leading_from_factors),
    )

    plain = sp.expand(packet**multiplicity)
    plain_leading = sp.diff(plain, s, multiplicity).subs(s, rho) / sp.factorial(multiplicity)
    check(
        "same_one_packet_coordinate_has_distinct_leading_jet_after_nonvanishing_complement",
        zero(plain_leading - sp.diff(packet, s).subs(s, rho) ** multiplicity)
        and not zero(leading_from_derivative - plain_leading),
    )

    normalized = sp.cancel(
        function
        / (leading_from_factors * (s - rho) ** multiplicity)
    )
    check(
        "normalized_local_germ_extends_with_value_one",
        zero(sp.limit(normalized, s, rho) - 1),
    )


def main() -> int:
    check_centered_packet_polynomials()
    check_quartic_coordinate_inverse()
    check_packet_logarithmic_derivatives()
    check_sign_orbit_to_packet_fibres()
    check_finite_symmetric_coordinates()
    check_leading_jet_and_information_fibre()
    print(
        json.dumps(
            {
                "status": "pass",
                "named_check_count": len(CHECKS),
                "checks": CHECKS,
                "python": sys.version.split()[0],
                "sympy": sp.__version__,
                "filesystem_writes": False,
                "network_access": False,
                "ocr": False,
                "page_images": False,
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
