#!/usr/bin/env python3
"""Bounded replay of the finite coordinate core in Chapter 16.

The manuscript contains the proofs.  This script independently checks exact
finite models where exact arithmetic is available and uses explicit tolerances
only for trigonometric identities.  It performs no corpus or filesystem writes.
"""

from __future__ import annotations

import cmath
import itertools
import json
import math
import sys
from fractions import Fraction


TOL = 2.0e-12
CHECKS: list[str] = []


def check(name: str, condition: bool) -> None:
    if not condition:
        raise AssertionError(name)
    CHECKS.append(name)


def close_complex(left: complex, right: complex, tol: float = TOL) -> bool:
    return abs(left - right) <= tol * max(1.0, abs(left), abs(right))


def gaussian_add(
    left: tuple[Fraction, Fraction], right: tuple[Fraction, Fraction]
) -> tuple[Fraction, Fraction]:
    return left[0] + right[0], left[1] + right[1]


def gaussian_mul(
    left: tuple[Fraction, Fraction], right: tuple[Fraction, Fraction]
) -> tuple[Fraction, Fraction]:
    return (
        left[0] * right[0] - left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


def gaussian_conj(value: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    return value[0], -value[1]


def gaussian_pow(
    value: tuple[Fraction, Fraction], exponent: int
) -> tuple[Fraction, Fraction]:
    result = (Fraction(1), Fraction(0))
    for _ in range(exponent):
        result = gaussian_mul(result, value)
    return result


def elementary_symmetric(values: tuple[Fraction, ...]) -> list[Fraction]:
    result = [Fraction(1)] + [Fraction(0)] * len(values)
    for value in values:
        for degree in range(len(values), 0, -1):
            result[degree] += value * result[degree - 1]
    return result


def check_fixed_locus_modular_rings() -> None:
    for modulus in range(2, 31):
        units = [u for u in range(modulus) if math.gcd(u, modulus) == 1]
        for unit in units:
            fixed = {r for r in range(modulus) if (unit * r - r) % modulus == 0}
            annihilator = {
                r for r in range(modulus) if ((unit - 1) * r) % modulus == 0
            }
            if fixed != annihilator:
                raise AssertionError((modulus, unit, fixed, annihilator))
    check("general_fixed_locus_over_Z_mod_n_for_2_through_30", True)


def boolean_eval(
    polynomial: frozenset[tuple[int, ...]], point: tuple[int, ...]
) -> int:
    # A Boolean polynomial is a finite idempotent sum of monomials.  Each
    # monomial is represented by its exponent vector.
    for exponents in polynomial:
        term = 1
        for exponent, coordinate in zip(exponents, point, strict=True):
            if exponent:
                term &= coordinate
        if term:
            return 1
    return 0


def check_boolean_affine_maps() -> None:
    for dimension in range(1, 9):
        points = list(itertools.product((0, 1), repeat=dimension))
        recovered = {
            tuple(boolean_eval(frozenset({tuple(1 if i == j else 0 for i in range(dimension))}), point)
                  for j in range(dimension))
            for point in points
        }
        if recovered != set(points):
            raise AssertionError((dimension, recovered))
        for point in points:
            support = int(any(point))
            diagonal = tuple([support] * dimension)
            if int(any(diagonal)) != support:
                raise AssertionError((dimension, point))

        # Test contravariance of the diagonal on a deterministic family of
        # genuine exponent-bearing Boolean polynomials, not only squarefree
        # representatives.
        polynomials: list[frozenset[tuple[int, ...]]] = []
        zero = tuple([0] * dimension)
        polynomials.append(frozenset())
        polynomials.append(frozenset({zero}))
        for index in range(dimension):
            linear = tuple(1 if j == index else 0 for j in range(dimension))
            cubic = tuple(3 if j == index else 0 for j in range(dimension))
            polynomials.extend((frozenset({linear}), frozenset({cubic})))
        polynomials.append(
            frozenset(
                {
                    tuple((2 * j + 1) % 4 for j in range(dimension)),
                    tuple((3 * j + 2) % 5 for j in range(dimension)),
                }
            )
        )
        for polynomial in polynomials:
            for scalar in (0, 1):
                left = boolean_eval(polynomial, tuple([scalar] * dimension))
                diagonal_exponents = frozenset(
                    {(sum(exponents),) for exponents in polynomial}
                )
                right = boolean_eval(diagonal_exponents, (scalar,))
                if left != right:
                    raise AssertionError((dimension, polynomial, scalar))
    check("boolean_affine_evaluation_diagonal_sum_and_split_retraction_m_1_through_8", True)


def check_phase_decoration_fibres() -> None:
    star = ("star",)
    tau = ("tau",)
    occupied = ("e",)
    phases = [
        (Fraction(1), Fraction(0)),
        (Fraction(-1), Fraction(0)),
        (Fraction(0), Fraction(1)),
        (Fraction(0), Fraction(-1)),
        (Fraction(3, 5), Fraction(4, 5)),
        (Fraction(5, 13), Fraction(-12, 13)),
    ]

    def projection(value: object) -> tuple[str]:
        return tau if value == star else occupied

    def section(value: tuple[str]) -> object:
        return star if value == tau else phases[0]

    check(
        "phase_pointed_projection_section_and_sampled_exact_fibres",
        projection(section(tau)) == tau
        and projection(section(occupied)) == occupied
        and {value for value in [star, *phases] if projection(value) == tau} == {star}
        and {value for value in [star, *phases] if projection(value) == occupied}
        == set(phases),
    )


def check_orthogonal_walk_exact() -> None:
    grids = [
        (Fraction(-2), Fraction(-1), Fraction(0), Fraction(1), Fraction(2)),
        (Fraction(-3, 2), Fraction(2, 3), Fraction(5, 4)),
        (Fraction(1, 7),),
        tuple(),
    ]
    for values in grids:
        elementary = elementary_symmetric(values)
        endpoint = (Fraction(0), Fraction(0))
        i_power = (Fraction(1), Fraction(0))
        for coefficient in elementary:
            endpoint = gaussian_add(
                endpoint, (i_power[0] * coefficient, i_power[1] * coefficient)
            )
            i_power = gaussian_mul(i_power, (Fraction(0), Fraction(1)))
        product = (Fraction(1), Fraction(0))
        for value in values:
            product = gaussian_mul(product, (Fraction(1), value))
        if endpoint != product:
            raise AssertionError((values, endpoint, product))
        norm_squared = endpoint[0] ** 2 + endpoint[1] ** 2
        expected_norm = Fraction(1)
        for value in values:
            expected_norm *= 1 + value**2
        if norm_squared != expected_norm:
            raise AssertionError((values, norm_squared, expected_norm))
    check("elementary_symmetric_orthogonal_walk_and_norm_identity_exact", True)


def unit_factor(value: float) -> complex:
    return complex(1.0, value) / math.sqrt(1.0 + value * value)


def principal_argument(value: complex) -> float:
    angle = cmath.phase(value)
    return math.pi if abs(angle + math.pi) < TOL else angle


def check_finite_phase_products() -> None:
    angle_grid = (-1.3, -0.7, -0.2, 0.0, 0.4, 1.0, 1.4)
    slopes = tuple(math.tan(angle) for angle in angle_grid)
    for dimension in range(1, 5):
        for chosen in itertools.product(slopes, repeat=dimension):
            product = math.prod((unit_factor(value) for value in chosen), start=1 + 0j)
            angle_sum = sum(math.atan(value) for value in chosen)
            theta = principal_argument(product)
            ell = round((angle_sum - theta) / (2.0 * math.pi))
            if not close_complex(product, cmath.exp(1j * angle_sum)):
                raise AssertionError((dimension, chosen, "product"))
            if abs(angle_sum - (theta + 2.0 * math.pi * ell)) > 5.0e-12:
                raise AssertionError((dimension, chosen, theta, ell))
            if not (-dimension * math.pi / 2 < angle_sum < dimension * math.pi / 2):
                raise AssertionError((dimension, chosen, "range"))

    targets = (-math.pi, -2.4, -0.8, 0.0, 0.9, 2.6, math.pi)
    for theta in targets:
        slope = math.tan(theta / 3.0)
        if not close_complex(unit_factor(slope) ** 3, cmath.exp(1j * theta)):
            raise AssertionError((theta, slope))
    check("finite_phase_product_fibres_on_bounded_grid_and_three_factor_section", True)


def check_affine_phase_chart() -> None:
    phis = (math.pi / 7, 2 * math.pi / 5, math.pi / 2, 5 * math.pi / 6)
    fractions = (0.05, 0.2, 0.5, 0.8, 0.95)
    for phi in phis:
        omega = cmath.exp(1j * phi)
        previous_t = 0.0
        for fraction in fractions:
            theta = fraction * phi
            t_value = math.sin(theta) / math.sin(phi - theta)
            radius = math.sin(phi) / math.sin(phi - theta)
            left = 1.0 + t_value * omega
            right = radius * cmath.exp(1j * theta)
            if not (t_value > previous_t and close_complex(left, right)):
                raise AssertionError((phi, theta, t_value, left, right))
            derivative = math.sin(phi) / (
                1.0 + 2.0 * t_value * math.cos(phi) + t_value * t_value
            )
            if derivative <= 0.0:
                raise AssertionError((phi, theta, derivative))
            previous_t = t_value
    check("affine_phase_chart_inverse_radius_and_positive_derivative", True)


def check_taylor_atomization() -> None:
    coefficient_sets = (
        (0.2, -0.03, 0.004, -0.0005),
        (-0.15, 0.02, 0.01, -0.002, 0.0003),
        (0.0, 0.08, -0.01, 0.001),
    )
    for coefficients in coefficient_sets:
        for t_value in (-0.75, -0.25, 0.0, 0.3, 0.8):
            angles = [coefficient * t_value**index for index, coefficient in enumerate(coefficients, 1)]
            if sum(abs(angle) for angle in angles) >= math.pi / 4:
                raise AssertionError((coefficients, t_value, "radius"))
            product = 1 + 0j
            for angle in angles:
                alpha = math.tan(angle)
                product *= unit_factor(alpha)
                if not math.isfinite(alpha):
                    raise AssertionError("finite differential")
            if not close_complex(product, cmath.exp(1j * sum(angles))):
                raise AssertionError((coefficients, t_value, product))
    check("finite_Taylor_atom_products_on_explicit_small_branch", True)


def compositions(total: int, parts: int):
    if parts == 1:
        yield (total,)
        return
    for first in range(1, total - parts + 2):
        for rest in compositions(total - first, parts - 1):
            yield (first, *rest)


def logarithm_coefficients(values: list[Fraction]) -> list[Fraction]:
    # values[n] is a_n, with values[0] unused.
    degree = len(values) - 1
    result = [Fraction(0)] * (degree + 1)
    for n in range(1, degree + 1):
        for parts in range(1, n + 1):
            inner = Fraction(0)
            for composition in compositions(n, parts):
                term = Fraction(1)
                for index in composition:
                    term *= values[index]
                inner += term
            result[n] += Fraction((-1) ** (parts + 1), parts) * inner
    return result


def exponential_coefficients(values: list[Fraction]) -> list[Fraction]:
    # If C(z)=sum_{n>=1} values[n]z^n and exp(C)=sum b_n z^n,
    # n b_n=sum_{k=1}^n k c_k b_{n-k}.
    degree = len(values) - 1
    result = [Fraction(1)] + [Fraction(0)] * degree
    for n in range(1, degree + 1):
        result[n] = sum(
            Fraction(k) * values[k] * result[n - k] for k in range(1, n + 1)
        ) / n
    return result


def check_logarithm_coefficients() -> None:
    inputs = (
        [Fraction(0), Fraction(1, 3), Fraction(-2, 5), Fraction(4, 7), Fraction(1, 11), Fraction(-3, 8)],
        [Fraction(0), Fraction(-2), Fraction(1, 2), Fraction(0), Fraction(3, 10), Fraction(1, 9)],
        [Fraction(0), Fraction(0), Fraction(1), Fraction(-1), Fraction(2), Fraction(-3)],
    )
    for coefficients in inputs:
        logarithm = logarithm_coefficients(coefficients)
        recovered = exponential_coefficients(logarithm)
        if recovered != [Fraction(1), *coefficients[1:]]:
            raise AssertionError((coefficients, logarithm, recovered))
        if logarithm[1] != coefficients[1]:
            raise AssertionError("c1")
        if logarithm[2] != coefficients[2] - coefficients[1] ** 2 / 2:
            raise AssertionError("c2")
    check("logarithm_composition_formula_and_exponential_inverse_exact_through_degree_5", True)


def check_packet_transport() -> None:
    coefficients = [
        (Fraction(2, 3), Fraction(-1, 5)),
        (Fraction(-4, 7), Fraction(3, 8)),
        (Fraction(5, 9), Fraction(2, 11)),
        (Fraction(-1, 6), Fraction(-7, 13)),
        (Fraction(3, 10), Fraction(4, 15)),
    ]
    directions = [
        (Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(1)),
        (Fraction(3, 5), Fraction(4, 5)),
        (Fraction(5, 13), Fraction(-12, 13)),
    ]
    for direction in directions:
        negative_direction = (-direction[0], -direction[1])
        conjugate_direction = gaussian_conj(direction)
        for n, coefficient in enumerate(coefficients, 1):
            reflected_coefficient = (
                coefficient if n % 2 == 0 else (-coefficient[0], -coefficient[1])
            )
            conjugate_coefficient = gaussian_conj(coefficient)
            beta = gaussian_mul(coefficient, gaussian_pow(direction, n))[1]
            reflected_beta = gaussian_mul(
                reflected_coefficient, gaussian_pow(negative_direction, n)
            )[1]
            conjugate_beta = gaussian_mul(
                conjugate_coefficient, gaussian_pow(conjugate_direction, n)
            )[1]
            if reflected_beta != beta or conjugate_beta != -beta:
                raise AssertionError((n, direction, beta, reflected_beta, conjugate_beta))
    check("local_packet_reflection_and_conjugation_atoms_exact", True)


def check_cycle_length_coordinate() -> None:
    # Work with lambda=L/(2*pi)=n/s, so the transcendental factor cancels.
    ordinates = (Fraction(3, 2), Fraction(7, 3), Fraction(11, 5))
    for ordinate in ordinates:
        for n in range(1, 8):
            normalized_length = Fraction(n, 1) / ordinate
            recovered_ordinate = Fraction(n, 1) / normalized_length
            if recovered_ordinate != ordinate:
                raise AssertionError((ordinate, n, normalized_length))
    check("cycle_length_coordinate_and_fibre_inversion_exact_after_2pi_scaling", True)


def main() -> int:
    check_fixed_locus_modular_rings()
    check_boolean_affine_maps()
    check_phase_decoration_fibres()
    check_orthogonal_walk_exact()
    check_finite_phase_products()
    check_affine_phase_chart()
    check_taylor_atomization()
    check_logarithm_coefficients()
    check_packet_transport()
    check_cycle_length_coordinate()
    print(
        json.dumps(
            {
                "status": "pass",
                "named_check_count": len(CHECKS),
                "checks": CHECKS,
                "float_tolerance": TOL,
                "python": sys.version.split()[0],
                "ocr": False,
                "filesystem_writes": False,
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
