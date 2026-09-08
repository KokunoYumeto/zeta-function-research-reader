#!/usr/bin/env python3
"""Exact finite checks for the modern CUE--Mellin local programme.

The certificate checks only finite rational and polynomial algebra.  The
measure-theoretic, analytic-convergence, Haar-coordinate, and Galois-theoretic
implications are proved separately in the human-readable manuscript.
"""

from __future__ import annotations

import json
import math
import platform

import sympy as sp


CERTIFICATE_ID = "CERT-CUE-MELLIN-20260828-0001"

u, v, X = sp.symbols("u v X")
alpha, alpha_bar, beta, beta_bar = sp.symbols(
    "alpha alpha_bar beta beta_bar"
)


def check_zero(checks: list[str], name: str, expression: sp.Expr) -> None:
    remainder = sp.factor(sp.cancel(sp.together(sp.expand(expression))))
    if remainder != 0:
        raise AssertionError(f"{name}: nonzero remainder {remainder}")
    checks.append(name)


def check_rational_zero(checks: list[str], name: str, expression: sp.Expr) -> None:
    """Check a rational identity without globally expanding its denominator."""

    numerator = sp.factor(sp.together(expression).as_numer_denom()[0])
    if numerator != 0:
        raise AssertionError(f"{name}: nonzero numerator {numerator}")
    checks.append(name)


def trace_polynomials(maximum: int) -> list[sp.Expr]:
    w = (1 - u + 2 * v) / 2
    trace = (9 * u**2 - 16 * u * v - 10 * u - 16 * v + 1) / 16
    norm = u * v * w
    values = [sp.Integer(2), trace]
    for index in range(1, maximum):
        values.append(sp.expand(trace * values[index] - norm * values[index - 1]))
    return values[: maximum + 1]


def descended_kernel(order: int) -> sp.Expr:
    """The closed finite trace-descent formula in the maintained local source."""

    w = (1 - u + 2 * v) / 2
    traces = trace_polynomials(order)
    total = sp.Integer(0)
    for m in range(order + 1):
        diagonal = sp.Integer(0)
        for p in range(order - m + 1):
            for q in range(m + 1):
                diagonal += (
                    sp.Rational(
                        math.comb(order - m, p) ** 2 * math.comb(m, q) ** 2,
                        p + q + 1,
                    )
                    * u**p
                    * v ** (m - q)
                    * w**q
                )

        off_diagonal = sp.Integer(0)
        for ell in range(1, min(m, order - m) + 1):
            coefficient = sp.Integer(0)
            for p in range(order - m - ell + 1):
                for q in range(m - ell + 1):
                    coefficient += (
                        sp.Rational(
                            math.comb(order - m, p + ell)
                            * math.comb(order - m, p)
                            * math.comb(m, q + ell)
                            * math.comb(m, q),
                            p + q + ell + 1,
                        )
                        * u**p
                        * v ** (m - q - ell)
                        * w**q
                    )
            off_diagonal += (-1) ** ell * traces[ell] * coefficient

        total += math.comb(order, m) ** 2 * (diagonal + off_diagonal)
    return sp.factor(sp.expand(total))


def n2_haar_moment(order: int) -> sp.Rational:
    z1, z2 = sp.symbols("z1 z2")
    derivative = 2 - z1 - z2
    conjugate = 2 - 1 / z1 - 1 / z2
    density = (1 - z1 / z2) * (1 - z2 / z1)
    expression = sp.expand(derivative**order * conjugate**order * density / 2)
    constant = sp.Integer(0)
    for term in sp.Add.make_args(expression):
        powers = term.as_powers_dict()
        if powers.get(z1, 0) == 0 and powers.get(z2, 0) == 0:
            constant += term
    return sp.Rational(constant)


def n2_hypergeometric_moment(order: int) -> sp.Rational:
    return sp.factor(
        4**order
        * sum(
            sp.Integer(math.comb(order, n) ** 2)
            * sp.rf(sp.Rational(1, 2), n)
            / sp.rf(2, n)
            for n in range(order + 1)
        )
    )


def terminating_gauss_distribution(m: int, order: int) -> list[sp.Rational]:
    weights = [
        sp.rf(-order, n) ** 2 / (sp.rf(m, n) * sp.factorial(n))
        for n in range(order + 1)
    ]
    normalizer = sum(weights)
    return [sp.factor(weight / normalizer) for weight in weights]


def main() -> None:
    checks: list[str] = []

    expected_kernels = {
        1: (5 + u + 6 * v) / 4,
        2: (
            sp.Rational(47, 24)
            + sp.Rational(11, 4) * u
            + sp.Rational(28, 3) * v
            - sp.Rational(11, 8) * u**2
            + 4 * u * v
            + sp.Rational(10, 3) * v**2
        ),
        3: (
            sp.Rational(105, 32)
            + sp.Rational(465, 32) * u
            + sp.Rational(75, 2) * v
            - sp.Rational(225, 32) * u**2
            + sp.Rational(195, 4) * u * v
            + sp.Rational(405, 8) * v**2
            - sp.Rational(65, 32) * u**3
            - sp.Rational(15, 2) * u**2 * v
            + sp.Rational(225, 8) * u * v**2
            + sp.Rational(35, 4) * v**3
        ),
        4: sp.Rational(1, 320)
        * (
            1759 * u**4
            - 16224 * u**3 * v
            - 11812 * u**3
            + 3024 * u**2 * v**2
            - 12816 * u**2 * v
            - 2334 * u**2
            + 50176 * u * v**3
            + 165984 * u * v**2
            + 117312 * u * v
            + 18732 * u
            + 8064 * v**4
            + 78848 * v**3
            + 121296 * v**2
            + 40752 * v
            + 1719
        ),
    }

    kernels: dict[int, sp.Expr] = {}
    for order in range(1, 9):
        kernel = descended_kernel(order)
        kernels[order] = kernel
        polynomial = sp.Poly(kernel, u, v, domain=sp.QQ)
        if polynomial.total_degree() != order:
            raise AssertionError(
                f"kernel_degree_{order}: {polynomial.total_degree()} != {order}"
            )
        checks.append(f"kernel_degree_{order}")
        expected_lead = sp.Rational(math.comb(2 * order + 1, order), order + 1)
        if polynomial.coeff_monomial(v**order) != expected_lead:
            raise AssertionError(f"kernel_v_lead_{order}")
        checks.append(f"kernel_v_lead_{order}")
        if order in expected_kernels:
            check_zero(
                checks,
                f"explicit_descended_kernel_{order}",
                kernel - expected_kernels[order],
            )

    n2_values: dict[int, int] = {}
    for order in range(0, 8):
        haar = n2_haar_moment(order)
        hypergeometric = n2_hypergeometric_moment(order)
        if haar != hypergeometric:
            raise AssertionError(
                f"n2_moment_{order}: Haar={haar}, hypergeometric={hypergeometric}"
            )
        checks.append(f"n2_haar_equals_terminating_3f2_{order}")
        n2_values[order] = int(haar)

    # The exact N=3 arrow from the recursive state to the retained local
    # (lambda,c,d) coordinates.  Conjugate coordinates are kept independent,
    # so these are rational identities before imposing alpha_bar=conj(alpha)
    # and beta_bar=conj(beta).
    u1 = 1 / (1 - alpha)
    u1_bar = 1 / (1 - alpha_bar)
    u2 = (1 + u1 - beta * (1 - u1_bar)) / (1 - beta)
    u2_bar = (1 + u1_bar - beta_bar * (1 - u1)) / (1 - beta_bar)
    eta2 = (2 - u2_bar) / (1 + u2)
    eta2_bar = (2 - u2) / (1 + u2_bar)

    lam = ((1 - 2 * alpha_bar) * (1 - alpha)) / (
        (3 - 2 * alpha) * (1 - alpha_bar)
    )
    lam_bar = ((1 - 2 * alpha) * (1 - alpha_bar)) / (
        (3 - 2 * alpha_bar) * (1 - alpha)
    )
    c = alpha_bar * (1 - alpha) / (
        (3 - 2 * alpha) * (1 - alpha_bar)
    )
    c_bar = alpha * (1 - alpha_bar) / (
        (3 - 2 * alpha_bar) * (1 - alpha)
    )
    d = (2 - alpha) / (3 - 2 * alpha)
    d_bar = (2 - alpha_bar) / (3 - 2 * alpha_bar)
    eta2_retained = -(
        (beta - 1) / (beta_bar - 1)
    ) * (c + beta_bar * d) / (1 - lam * beta)
    check_rational_zero(
        checks,
        "n3_recursive_eta2_equals_retained_phase_coordinate",
        eta2 - eta2_retained,
    )
    retained_A = (1 - lam * beta) * (1 - lam_bar * beta_bar)
    retained_B = (c + beta_bar * d) * (c_bar + beta * d_bar)
    check_rational_zero(
        checks,
        "n3_retained_B_over_A_equals_eta2_norm_square",
        retained_B / retained_A - eta2 * eta2_bar,
    )

    gram = sp.Matrix(
        [
            [sp.Rational(47, 24), sp.Rational(11, 8), sp.Rational(14, 3)],
            [sp.Rational(11, 8), -sp.Rational(11, 8), 2],
            [sp.Rational(14, 3), 2, sp.Rational(10, 3)],
        ]
    )
    vector = sp.Matrix([1, u, v])
    check_zero(checks, "psi2_affine_gram_identity", (vector.T * gram * vector)[0] - kernels[2])
    gram_minor = gram.extract([0, 1], [0, 1]).det()
    if gram_minor != -sp.Rational(55, 12):
        raise AssertionError(f"psi2_gram_minor: {gram_minor}")
    checks.append("psi2_gram_minor_is_negative_55_over_12")

    q3 = (
        -7 * X**3
        + (549 * u + 669) * X**2
        - (6645 * u**2 + 22746 * u + 8997) * X
        + 13783 * u**3
        + 125949 * u**2
        + 138933 * u
        + 19087
    )
    transformed = sp.expand(kernels[3].subs(v, (9 * u + 1 - X) / 16))
    check_zero(checks, "psi3_affine_trace_transform", transformed - sp.Rational(5, 16384) * q3)

    expected_discriminant = 2**18 * 3**3 * (
        290275 * u**6
        + 731094 * u**5
        + 2234709 * u**4
        + 2884436 * u**3
        + 3453789 * u**2
        + 1714038 * u
        + 984779
    )
    check_zero(
        checks,
        "q3_discriminant",
        sp.discriminant(q3, X) - expected_discriminant,
    )

    q3_zero = sp.Poly(q3.subs(u, 0), X, domain=sp.QQ)
    if not q3_zero.is_irreducible:
        raise AssertionError("q3_u_zero_is_not_irreducible_over_Q")
    checks.append("q3_u_zero_irreducible_over_Q")
    modular_values = [int(q3_zero.eval(point)) % 11 for point in range(11)]
    if any(value == 0 for value in modular_values):
        raise AssertionError(f"q3_mod_11_has_root: {modular_values}")
    checks.append("q3_u_zero_has_no_root_mod_11")
    q3_fraction_field = sp.Poly(q3, X, domain=sp.QQ.frac_field(u))
    if not q3_fraction_field.is_irreducible:
        raise AssertionError("q3_not_irreducible_over_Q_of_u")
    checks.append("q3_irreducible_over_Q_of_u")
    if expected_discriminant.subs(u, 0) != 2**18 * 3**3 * 984779:
        raise AssertionError("q3_discriminant_specialization")
    checks.append("q3_discriminant_nonzero_specialization")

    gauss_checks = 0
    for m in range(1, 7):
        for order in range(0, 7):
            probabilities = terminating_gauss_distribution(m, order)
            if sum(probabilities) != 1 or any(value < 0 for value in probabilities):
                raise AssertionError(f"gauss_distribution_m{m}_s{order}")
            mean = sum(index * value for index, value in enumerate(probabilities))
            second = sum(
                index * (index - 1) * value
                for index, value in enumerate(probabilities)
            )
            if order == 0:
                if mean != 0 or second != 0:
                    raise AssertionError(f"gauss_zero_order_m{m}")
            else:
                expected_mean = sp.Rational(order**2, m + 2 * order - 1)
                expected_second = sp.Rational(
                    order**2 * (order - 1) ** 2,
                    (m + 2 * order - 2) * (m + 2 * order - 1),
                )
                if mean != expected_mean or second != expected_second:
                    raise AssertionError(
                        f"gauss_factorial_moments_m{m}_s{order}: "
                        f"{mean}, {second}"
                    )
            gauss_checks += 1
    checks.append("terminating_gauss_probability_and_factorial_moments_42_cases")

    output = {
        "schema_version": 1,
        "certificate_id": CERTIFICATE_ID,
        "status": "pass",
        "python": platform.python_version(),
        "sympy": sp.__version__,
        "arithmetic": "exact integers, rationals, Laurent constant terms, and polynomial algebra",
        "check_count": len(checks),
        "checks": checks,
        "n2_integer_moments_0_through_7": n2_values,
        "descended_kernel_orders_checked": list(range(1, 9)),
        "explicit_descended_kernels_checked": [1, 2, 3, 4],
        "gauss_terminating_cases_checked": gauss_checks,
        "q3_mod_11_values_before_nonzero_scalar_normalization": modular_values,
        "scope_boundary": [
            "The all-order trace formula and degree theorem are proved in the manuscript; the script checks orders one through eight and the printed orders one through four.",
            "The exact N=3 recursive-state to retained-coordinate arrow and its squared-modulus identity are checked as rational identities with conjugate coordinates kept independent.",
            "The noninteger Gauss-law convergence and tail asymptotic are proved analytically in the manuscript; the script checks forty-two terminating integer laws exactly.",
            "The fixed-length multiplier theorem is a lattice proof in the manuscript and is not inferred from finite samples.",
            "The generic S3 conclusion uses the standard irreducible-cubic discriminant criterion in the manuscript; the script certifies the exact polynomial, specialization, modular root test, fraction-field irreducibility, and discriminant.",
            "No large-N limit, individual zeta zero, or endpoint theorem is certified here.",
        ],
    }
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
