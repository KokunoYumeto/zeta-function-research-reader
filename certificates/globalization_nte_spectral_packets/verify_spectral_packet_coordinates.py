#!/usr/bin/env python3
"""Bounded exact replay for Chapter 18's spectral-packet algebra.

The manuscript proves the analytic and divisor statements.  This script checks
only finite semiring tables, affine-coordinate identities, polynomial fibres,
spectral coefficient conversions, multiplicity aggregation on explicit finite
packets, and the critical length substitution.  It performs no scan, network
access, OCR, rendering, or filesystem write.
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


def check_split_zero_embedding() -> None:
    tau = object()

    def add(x: object, y: object) -> object:
        if x is tau:
            return y
        if y is tau:
            return x
        return x + y  # type: ignore[operator]

    def mul(x: object, y: object) -> object:
        if x is tau or y is tau:
            return tau
        return x * y  # type: ignore[operator]

    domain = [tau, -2, -1, 0, 1, 3]

    def embed(x: object) -> object:
        return tau if x is tau else complex(x)  # type: ignore[arg-type]

    table_pass = True
    for x in domain:
        for y in domain:
            table_pass &= embed(add(x, y)) == add(embed(x), embed(y))
            table_pass &= embed(mul(x, y)) == mul(embed(x), embed(y))
    check("split_zero_integer_to_complex_tables_commute", table_pass)

    fixed_domain = [x for x in domain if mul(-1, x) == x]
    fixed_codomain = [x for x in [tau, -2j, -1 + 3j, 0j, 1 + 0j] if mul(-1, x) == x]
    check(
        "split_zero_fixed_pairs_map_bijectively_on_test_universe",
        fixed_domain == [tau, 0]
        and fixed_codomain == [tau, 0j]
        and [embed(x) for x in fixed_domain] == fixed_codomain,
    )


def check_affine_coordinate() -> None:
    s = sp.symbols("s")
    z = sp.symbols("z")
    half = sp.Rational(1, 2)
    phi = sp.I * (s - half)
    phi_inverse = half - sp.I * z
    check("affine_inverse_left", zero(phi_inverse.subs(z, phi) - s))
    check(
        "affine_inverse_right",
        zero((sp.I * (phi_inverse - half)) - z),
    )
    check(
        "functional_involution_becomes_sign",
        zero((sp.I * ((1 - s) - half)) + phi),
    )

    beta, gamma = sp.symbols("beta gamma", real=True)
    phi_coordinates = sp.expand_complex(sp.I * (beta + sp.I * gamma - half))
    check(
        "affine_real_coordinates",
        zero(phi_coordinates - (-gamma + sp.I * (beta - half))),
    )


def check_laplacian_coordinate_and_fibres() -> None:
    s, z1, z2 = sp.symbols("s z1 z2")
    half = sp.Rational(1, 2)
    phi = sp.I * (s - half)
    lam = -phi**2 - sp.Rational(1, 4)
    check(
        "laplacian_affine_identity",
        zero(lam - ((s - half) ** 2 - sp.Rational(1, 4)))
        and zero(lam + s * (1 - s)),
    )
    check(
        "equal_laplacian_values_factor_through_sign_fibre",
        zero(
            ((-z1**2 - sp.Rational(1, 4)) - (-z2**2 - sp.Rational(1, 4)))
            + (z1 - z2) * (z1 + z2)
        ),
    )


def check_packet_spectral_polynomials() -> None:
    t, a, gamma = sp.symbols("t a gamma", real=True, nonzero=True)
    half = sp.Rational(1, 2)
    alpha = a + sp.I * gamma
    alpha_bar = a - sp.I * gamma
    A = sp.expand(alpha**2)
    B = sp.expand(alpha_bar**2)
    lam = A - sp.Rational(1, 4)
    lam_bar = B - sp.Rational(1, 4)

    c4 = 1 / (A * B)
    c2 = -(A + B) / (A * B)
    check("packet_coefficients_recover_A_plus_B", zero(A + B + c2 / c4))
    check("packet_coefficients_recover_A_times_B", zero(A * B - 1 / c4))

    spectral_from_roots = sp.expand((t - lam) * (t - lam_bar))
    spectral_from_coefficients = sp.expand(
        t**2
        + (c2 / c4 + half) * t
        + (1 / c4 + c2 / (4 * c4) + sp.Rational(1, 16))
    )
    check(
        "four_point_spectral_polynomial_coefficient_conversion",
        zero(spectral_from_roots - spectral_from_coefficients),
    )

    critical_c2 = 1 / gamma**2
    critical_lam = -1 / critical_c2 - sp.Rational(1, 4)
    check(
        "two_point_spectral_root_coefficient_conversion",
        zero(critical_lam + gamma**2 + sp.Rational(1, 4)),
    )

    modulus_A = a**2 + gamma**2
    recovered_a2 = (modulus_A + sp.re(A)) / 2
    recovered_gamma2 = (modulus_A - sp.re(A)) / 2
    check("spectral_inverse_recovers_a_squared", zero(recovered_a2 - a**2))
    check(
        "spectral_inverse_recovers_gamma_squared",
        zero(recovered_gamma2 - gamma**2),
    )

    centered_packet = {alpha, -alpha, alpha_bar, -alpha_bar}
    spectral_values = {
        sp.expand(point**2 - sp.Rational(1, 4)) for point in centered_packet
    }
    check(
        "four_point_packet_maps_to_exact_conjugate_spectral_pair",
        spectral_values == {lam, lam_bar},
    )


def check_divisor_aggregation_and_cycle_coordinate() -> None:
    a = sp.Rational(2, 3)
    gamma = sp.Rational(5, 7)
    m = 4
    alpha = a + sp.I * gamma
    packet = [alpha, -alpha, sp.conjugate(alpha), -sp.conjugate(alpha)]
    counts: dict[sp.Expr, int] = {}
    for point in packet:
        value = sp.expand(point**2 - sp.Rational(1, 4))
        counts[value] = counts.get(value, 0) + m
    check(
        "four_point_divisor_pushforward_has_two_coefficients_2m",
        len(counts) == 2 and set(counts.values()) == {2 * m},
    )

    gamma = sp.Rational(11, 13)
    packet = [sp.I * gamma, -sp.I * gamma]
    counts = {}
    for point in packet:
        value = sp.expand(point**2 - sp.Rational(1, 4))
        counts[value] = counts.get(value, 0) + m
    check(
        "critical_divisor_pushforward_has_one_coefficient_2m",
        len(counts) == 1 and next(iter(counts.values())) == 2 * m,
    )

    n = sp.symbols("n", positive=True, integer=True)
    nu = sp.symbols("nu", positive=True)
    spectral_value = -nu**2 - sp.Rational(1, 4)
    recovered_nu_squared = -spectral_value - sp.Rational(1, 4)
    length = 2 * sp.pi * n / nu
    check(
        "critical_frequency_squared_recovers_from_spectral_value",
        zero(recovered_nu_squared - nu**2),
    )
    check(
        "critical_length_returns_exact_fourier_frequency",
        zero(2 * sp.pi * n / length - nu),
    )
    check(
        "scaling_site_signed_fourier_exponents",
        zero(-2 * sp.pi * n / length + nu)
        and zero(2 * sp.pi * n / length - nu),
    )


def main() -> int:
    check_split_zero_embedding()
    check_affine_coordinate()
    check_laplacian_coordinate_and_fibres()
    check_packet_spectral_polynomials()
    check_divisor_aggregation_and_cycle_coordinate()
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
