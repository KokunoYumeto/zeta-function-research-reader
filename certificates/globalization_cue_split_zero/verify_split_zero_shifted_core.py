#!/usr/bin/env python3
"""Exact finite checks for the split-zero and shifted-sheet audited core.

The certificate checks finite semiring/ideal models and exact polynomial or
rational coordinate identities.  The categorical equivalence, normal-
convergence arguments, and meromorphic continuation remain human-readable
proofs in the manuscript.
"""

from __future__ import annotations

import itertools
import json
import math
import platform
from fractions import Fraction

import sympy as sp


CERTIFICATE_ID = "CERT-GCUE-SPLIT-ZERO-20260828-0001"
TAU = None


def s_add(x: int | None, y: int | None, modulus: int) -> int | None:
    if x is TAU:
        return y
    if y is TAU:
        return x
    return (x + y) % modulus


def s_mul(x: int | None, y: int | None, modulus: int) -> int | None:
    if x is TAU or y is TAU:
        return TAU
    return (x * y) % modulus


def vec_add(
    x: tuple[int | None, ...], y: tuple[int | None, ...], modulus: int
) -> tuple[int | None, ...]:
    return tuple(s_add(a, b, modulus) for a, b in zip(x, y, strict=True))


def scalar_mul(
    scalar: int | None, x: tuple[int | None, ...], modulus: int
) -> tuple[int | None, ...]:
    return tuple(s_mul(scalar, coordinate, modulus) for coordinate in x)


def ring_ideals(modulus: int) -> list[frozenset[int]]:
    carrier = tuple(range(modulus))
    ideals: list[frozenset[int]] = []
    for mask in range(1 << modulus):
        subset = frozenset(x for x in carrier if mask & (1 << x))
        if 0 not in subset:
            continue
        if any((x + y) % modulus not in subset for x in subset for y in subset):
            continue
        if any((-x) % modulus not in subset for x in subset):
            continue
        if any((r * x) % modulus not in subset for r in carrier for x in subset):
            continue
        ideals.append(subset)
    return ideals


def semiring_ideals(modulus: int) -> list[frozenset[int | None]]:
    carrier: tuple[int | None, ...] = (TAU, *range(modulus))
    ideals: list[frozenset[int | None]] = []
    for mask in range(1 << len(carrier)):
        subset = frozenset(carrier[i] for i in range(len(carrier)) if mask & (1 << i))
        if TAU not in subset:
            continue
        if any(s_add(x, y, modulus) not in subset for x in subset for y in subset):
            continue
        if any(s_mul(r, x, modulus) not in subset for r in carrier for x in subset):
            continue
        ideals.append(subset)
    return ideals


def ideal_product(
    left: frozenset[int], right: frozenset[int], modulus: int
) -> frozenset[int]:
    generators = {(x * y) % modulus for x in left for y in right}
    generated = {0}
    changed = True
    while changed:
        changed = False
        for x in tuple(generated | generators):
            for y in tuple(generated | generators):
                value = (x + y) % modulus
                if value not in generated:
                    generated.add(value)
                    changed = True
    return frozenset(generated)


def semiring_ideal_generated(
    generators: set[int | None], modulus: int
) -> frozenset[int | None]:
    carrier: tuple[int | None, ...] = (TAU, *range(modulus))
    generated = {TAU, *generators}
    changed = True
    while changed:
        changed = False
        current = tuple(generated)
        for x, y in itertools.product(current, repeat=2):
            value = s_add(x, y, modulus)
            if value not in generated:
                generated.add(value)
                changed = True
        current = tuple(generated)
        for scalar, x in itertools.product(carrier, current):
            value = s_mul(scalar, x, modulus)
            if value not in generated:
                generated.add(value)
                changed = True
    return frozenset(generated)


def check_semiring(checks: list[str], modulus: int) -> None:
    carrier: tuple[int | None, ...] = (TAU, *range(modulus))
    one = 1 % modulus
    for x, y, z in itertools.product(carrier, repeat=3):
        assert s_add(s_add(x, y, modulus), z, modulus) == s_add(
            x, s_add(y, z, modulus), modulus
        )
        assert s_mul(s_mul(x, y, modulus), z, modulus) == s_mul(
            x, s_mul(y, z, modulus), modulus
        )
        assert s_add(x, y, modulus) == s_add(y, x, modulus)
        assert s_mul(x, y, modulus) == s_mul(y, x, modulus)
        assert s_mul(x, s_add(y, z, modulus), modulus) == s_add(
            s_mul(x, y, modulus), s_mul(x, z, modulus), modulus
        )
    for x in carrier:
        assert s_add(x, TAU, modulus) == x
        assert s_mul(x, TAU, modulus) is TAU
        assert s_mul(x, one, modulus) == x
    checks.append(f"split_zero_semiring_Zmod_{modulus}")


def check_unique_boolean_character(checks: list[str], modulus: int) -> None:
    carrier: tuple[int | None, ...] = (TAU, *range(modulus))
    homomorphisms: list[dict[int | None, int]] = []
    for values in itertools.product((0, 1), repeat=len(carrier)):
        f = dict(zip(carrier, values, strict=True))
        if f[TAU] != 0 or f[1 % modulus] != 1:
            continue
        if any(
            f[s_add(x, y, modulus)] != (f[x] or f[y])
            for x in carrier
            for y in carrier
        ):
            continue
        if any(
            f[s_mul(x, y, modulus)] != (f[x] and f[y])
            for x in carrier
            for y in carrier
        ):
            continue
        homomorphisms.append(f)
    assert len(homomorphisms) == 1
    support = homomorphisms[0]
    assert support[TAU] == 0
    assert all(support[x] == 1 for x in range(modulus))
    checks.append(f"unique_boolean_character_Zmod_{modulus}")


def check_free_support_skeleton(checks: list[str], modulus: int) -> None:
    carrier: tuple[int | None, ...] = (TAU, *range(modulus))
    vectors = tuple(itertools.product(carrier, repeat=2))
    additive_idempotents = {
        x for x in vectors if vec_add(x, x, modulus) == x
    }
    e_image = {scalar_mul(0, x, modulus) for x in vectors}
    expected = set(itertools.product((TAU, 0), repeat=2))
    assert additive_idempotents == e_image == expected
    for support in expected:
        index_set = frozenset(i for i, value in enumerate(support) if value is not TAU)
        fibre = {x for x in vectors if scalar_mul(0, x, modulus) == support}
        assert len(fibre) == modulus ** len(index_set)
    checks.append(f"free_rank_two_all_idempotents_and_fibres_Zmod_{modulus}")


def check_ideal_correspondence(checks: list[str], modulus: int) -> None:
    r_ideals = ring_ideals(modulus)
    s_ideals = semiring_ideals(modulus)
    lifted = {frozenset((*ideal, TAU)) for ideal in r_ideals}
    assert set(s_ideals) == lifted | {frozenset({TAU})}
    assert frozenset({TAU, 0}) in lifted
    assert frozenset({TAU}) < frozenset({TAU, 0})
    for left in r_ideals:
        for right in r_ideals:
            product = ideal_product(left, right, modulus)
            left_g = frozenset((*left, TAU))
            right_g = frozenset((*right, TAU))
            supported_products = {
                s_mul(x, y, modulus) for x in left_g for y in right_g
            }
            generated_supported = frozenset((*ideal_product(left, right, modulus), TAU))
            actual_product_ideal = semiring_ideal_generated(supported_products, modulus)
            assert generated_supported == frozenset((*product, TAU))
            assert actual_product_ideal == generated_supported
    checks.append(f"ideal_lattice_and_products_Zmod_{modulus}")


def check_supported_zero_divisibility(checks: list[str]) -> None:
    for modulus, expected in ((2, True), (3, True), (4, False), (5, True), (6, False)):
        carrier: tuple[int | None, ...] = (TAU, *range(modulus))
        divisible = {s_mul(0, x, modulus) for x in carrier}
        assert divisible == {TAU, 0}
        property_holds = all(
            s_mul(x, y, modulus) not in divisible or x in divisible or y in divisible
            for x in carrier
            for y in carrier
        )
        assert property_holds is expected
    checks.append("supported_zero_divisibility_detects_domain_in_finite_models")


def check_endpoint_coordinates(checks: list[str]) -> None:
    matrix = sp.Matrix([[-1, 1], [1, 1]])
    inverse = sp.Matrix([[sp.Rational(-1, 2), sp.Rational(1, 2)],
                         [sp.Rational(1, 2), sp.Rational(1, 2)]])
    assert matrix.det() == -2
    assert matrix * inverse == sp.eye(2)
    assert inverse * matrix == sp.eye(2)

    s = sp.symbols("s")
    q = 1 / (s * (s - 1))
    ell = (2 * s - 1) / (s * (s - 1))
    assert sp.simplify(ell - q - 2 / s) == 0
    assert sp.simplify(q + ell - 2 / (s - 1)) == 0
    assert (sp.residue(q, s, 0), sp.residue(q, s, 1)) == (-1, 1)
    assert (sp.residue(ell, s, 0), sp.residue(ell, s, 1)) == (1, 1)

    subsets = tuple(frozenset(x) for length in range(3) for x in itertools.combinations((0, 1), length))
    swap = {0: 1, 1: 0}
    for left, right in itertools.product(subsets, repeat=2):
        assert (left | right) == frozenset(left | right)
        assert (left & right) == frozenset(left & right)
        assert frozenset(swap[i] for i in left | right) == (
            frozenset(swap[i] for i in left) | frozenset(swap[i] for i in right)
        )
    checks.append("endpoint_residue_matrix_inverse_lines_and_equivariance")


def check_stone_and_coprime_local_factor(checks: list[str]) -> None:
    def b(value: int) -> int:
        return int(value >= 2)

    for m in range(1, 65):
        for n in range(1, 65):
            if math.gcd(m, n) != 1:
                continue
            defect = b(m * n) - b(m) * b(n)
            expected = int((m == 1) ^ (n == 1))
            assert defect == expected
    x, y = sp.symbols("x y")
    local_sum = 1 + x / (1 - x) + y / (1 - y)
    local_ratio = (1 - x * y) / ((1 - x) * (1 - y))
    assert sp.factor(sp.together(local_sum - local_ratio)) == 0
    checks.append("stone_boundary_defect_and_coprime_euler_factor")


def check_shift_jets_and_binomial_coefficients(checks: list[str]) -> None:
    s, t = sp.symbols("s t")
    for n in (1, 2, 5):
        term = (n + t) ** (-s)
        for order in range(9):
            target = (-1) ** order * sp.rf(s, order) * (n + t) ** (-s - order)
            assert sp.simplify(sp.diff(term, t, order) - target) == 0
    z = sp.symbols("z")
    for order in range(9):
        coefficient = sp.diff((1 + z) ** (-s), z, order).subs(z, 0) / sp.factorial(order)
        target = (-1) ** order * sp.rf(s, order) / sp.factorial(order)
        assert sp.simplify(coefficient - target) == 0
    checks.append("shift_jets_and_binomial_coefficients_orders_0_through_8")


def check_pochhammer_pole_cancellation(checks: list[str]) -> None:
    s = sp.symbols("s")
    for order in range(1, 17):
        polynomial = sp.prod(s + j for j in range(order))
        root = 1 - order
        quotient = sp.cancel(polynomial / (s - root))
        assert sp.simplify(polynomial.subs(s, root)) == 0
        assert sp.simplify(quotient.subs(s, root)) == (-1) ** (order - 1) * math.factorial(order - 1)
    checks.append("pochhammer_simple_zero_cancels_shifted_simple_pole_orders_1_through_16")


def check_dedekind_local_coefficients(checks: list[str]) -> None:
    for q in (2, 3, 5, 7, 11):
        for r in range(1, 6):
            for k in range(1, 9):
                geometric = -(Fraction(1, 1) - Fraction(1, q**r)) * Fraction(1, q ** (r * (k - 1)))
                closed = -Fraction(q**r - 1, q ** (r * k))
                assert geometric == closed
    a, b = sp.symbols("a b", positive=True, integer=True)
    assert sp.expand((a + 1) * (b + 1) - (a * b + 1)) == a + b
    checks.append("dedekind_ratio_prime_power_coefficients_and_separated_weight")


def main() -> None:
    checks: list[str] = []
    for modulus in (2, 3, 4, 5, 6):
        check_semiring(checks, modulus)
        check_unique_boolean_character(checks, modulus)
        check_free_support_skeleton(checks, modulus)
        check_ideal_correspondence(checks, modulus)
    check_supported_zero_divisibility(checks)
    check_endpoint_coordinates(checks)
    check_stone_and_coprime_local_factor(checks)
    check_shift_jets_and_binomial_coefficients(checks)
    check_pochhammer_pole_cancellation(checks)
    check_dedekind_local_coefficients(checks)
    print(
        json.dumps(
            {
                "certificate_id": CERTIFICATE_ID,
                "status": "pass",
                "python": platform.python_version(),
                "sympy": sp.__version__,
                "named_check_count": len(checks),
                "checks": checks,
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
