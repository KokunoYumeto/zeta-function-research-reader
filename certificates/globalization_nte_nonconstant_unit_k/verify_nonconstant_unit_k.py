"""Bounded coordinate replay for the nonconstant unit-fibre K-theory chapter.

This checks finite permutation modules, invariant/coinvariant transition maps,
and bounded matrices for the finite and archimedean connecting maps.  It does
not certify the C*-algebraic mapping-torus, Green-imprimitivity, or six-term
exact-sequence theorems used in the manuscript.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import reduce
from hashlib import sha256
from itertools import product
from math import gcd, lcm
from typing import Iterable

from sympy import Matrix


CHECKS: list[str] = []


def check(condition: bool, name: str) -> None:
    if not condition:
        raise AssertionError(name)
    CHECKS.append(name)


def prime_power(q: int, m: int) -> int:
    return q**m


def units(q: int, m: int) -> tuple[int, ...]:
    modulus = prime_power(q, m)
    return tuple(a for a in range(modulus) if gcd(a, modulus) == 1)


def multiplicative_order(a: int, modulus: int) -> int:
    if gcd(a, modulus) != 1:
        raise ValueError((a, modulus))
    x = 1
    for n in range(1, modulus + 1):
        x = (x * a) % modulus
        if x == 1:
            return n
    raise AssertionError("order search failed")


def tuple_mul(x: tuple[int, ...], y: tuple[int, ...], moduli: tuple[int, ...]) -> tuple[int, ...]:
    return tuple((a * b) % n for a, b, n in zip(x, y, moduli))


def tuple_neg(x: tuple[int, ...], moduli: tuple[int, ...]) -> tuple[int, ...]:
    return tuple((-a) % n for a, n in zip(x, moduli))


@dataclass(frozen=True)
class FiniteTranslation:
    p: int
    qs: tuple[int, ...]
    exponents: tuple[int, ...]
    moduli: tuple[int, ...]
    points: tuple[tuple[int, ...], ...]
    g: tuple[int, ...]
    order: int
    orbits: tuple[tuple[tuple[int, ...], ...], ...]
    orbit_of: dict[tuple[int, ...], int]


def finite_translation(p: int, qs: Iterable[int], exponents: Iterable[int]) -> FiniteTranslation:
    qs_t = tuple(qs)
    exps_t = tuple(exponents)
    if len(qs_t) != len(exps_t):
        raise ValueError("prime and exponent tuple lengths differ")
    moduli = tuple(prime_power(q, m) for q, m in zip(qs_t, exps_t))
    coordinate_units = [units(q, m) for q, m in zip(qs_t, exps_t)]
    points = tuple(product(*coordinate_units)) if qs_t else ((),)
    g = tuple(p % n for n in moduli)
    coordinate_orders = [multiplicative_order(p % n, n) for n in moduli]
    order = reduce(lcm, coordinate_orders, 1)

    unvisited = set(points)
    orbit_list: list[tuple[tuple[int, ...], ...]] = []
    orbit_of: dict[tuple[int, ...], int] = {}
    while unvisited:
        start = min(unvisited)
        orbit: list[tuple[int, ...]] = []
        x = start
        while x not in orbit:
            orbit.append(x)
            x = tuple_mul(g, x, moduli)
        check(x == start, f"orbit_closes_at_start_p{p}_{qs_t}_{exps_t}_{start}")
        index = len(orbit_list)
        for y in orbit:
            check(y in unvisited, f"orbit_partition_no_repeat_p{p}_{qs_t}_{exps_t}_{y}")
            unvisited.remove(y)
            orbit_of[y] = index
        orbit_list.append(tuple(orbit))

    result = FiniteTranslation(
        p=p,
        qs=qs_t,
        exponents=exps_t,
        moduli=moduli,
        points=points,
        g=g,
        order=order,
        orbits=tuple(orbit_list),
        orbit_of=orbit_of,
    )
    check(all(len(o) == order for o in result.orbits), f"uniform_orbit_length_p{p}_{qs_t}_{exps_t}")
    check(sum(len(o) for o in result.orbits) == len(points), f"orbit_partition_size_p{p}_{qs_t}_{exps_t}")
    check(len(points) == order * len(result.orbits), f"orbit_stabilizer_count_p{p}_{qs_t}_{exps_t}")
    return result


def reduce_point(point: tuple[int, ...], coarse: FiniteTranslation) -> tuple[int, ...]:
    return tuple(a % n for a, n in zip(point, coarse.moduli))


def transition_columns(
    coarse: FiniteTranslation, fine: FiniteTranslation, coinvariant: bool
) -> tuple[tuple[int, ...], ...]:
    check(coarse.p == fine.p and coarse.qs == fine.qs, "transition_same_translation_data")
    check(all(a <= b for a, b in zip(coarse.exponents, fine.exponents)), "transition_directed_exponents")
    check(fine.order % coarse.order == 0, "transition_orbit_order_divisibility")
    degree = fine.order // coarse.order
    columns: list[tuple[int, ...]] = []
    used_supports: set[int] = set()

    for coarse_index, coarse_orbit in enumerate(coarse.orbits):
        fine_indices = sorted(
            {
                fine.orbit_of[y]
                for y in fine.points
                if coarse.orbit_of[reduce_point(y, coarse)] == coarse_index
            }
        )
        expected_count = (
            (len(fine.points) // len(coarse.points))
            * coarse.order
            // fine.order
        )
        check(len(fine_indices) == expected_count, f"fine_orbit_count_over_{coarse_index}")
        check(not (used_supports & set(fine_indices)), f"transition_disjoint_support_{coarse_index}")
        used_supports.update(fine_indices)

        column = [0] * len(fine.orbits)
        for j in fine_indices:
            column[j] = degree if coinvariant else 1

        if coinvariant:
            x = min(coarse_orbit)
            actual = [0] * len(fine.orbits)
            for y in fine.points:
                if reduce_point(y, coarse) == x:
                    actual[fine.orbit_of[y]] += 1
            check(actual == column, f"coinvariant_pullback_multiplicity_{coarse_index}")
        else:
            for y in fine.points:
                actual = int(coarse.orbit_of[reduce_point(y, coarse)] == coarse_index)
                predicted = int(fine.orbit_of[y] in fine_indices)
                check(actual == predicted, f"invariant_characteristic_pullback_{coarse_index}_{y}")
        columns.append(tuple(column))

    check(used_supports == set(range(len(fine.orbits))), "transition_supports_partition_fine_orbits")
    check(all(any(value != 0 for value in column) for column in columns), "transition_columns_nonzero")
    return tuple(columns)


def compose_columns(
    first: tuple[tuple[int, ...], ...], second: tuple[tuple[int, ...], ...]
) -> tuple[tuple[int, ...], ...]:
    # first: A -> B, second: B -> C, both stored by source columns.
    result: list[tuple[int, ...]] = []
    for col in first:
        out = [0] * len(second[0])
        for b, coefficient in enumerate(col):
            if coefficient:
                for c, value in enumerate(second[b]):
                    out[c] += coefficient * value
        result.append(tuple(out))
    return tuple(result)


def check_transition_chain(p: int, qs: tuple[int, ...], levels: tuple[tuple[int, ...], ...]) -> None:
    objects = [finite_translation(p, qs, level) for level in levels]
    for coinvariant in (False, True):
        ab = transition_columns(objects[0], objects[1], coinvariant)
        bc = transition_columns(objects[1], objects[2], coinvariant)
        ac = transition_columns(objects[0], objects[2], coinvariant)
        check(compose_columns(ab, bc) == ac, f"transition_composition_p{p}_{qs}_{coinvariant}")
        matrix = Matrix.hstack(*[Matrix(c) for c in ab])
        check(matrix.rank() == len(ab), f"transition_injective_rank_p{p}_{qs}_{coinvariant}")


@dataclass(frozen=True)
class GlobalFiniteModel:
    primes: tuple[int, ...]
    exponents: tuple[int, ...]
    points: tuple[tuple[int, ...], ...]
    moduli: tuple[int, ...]
    half: tuple[tuple[int, ...], ...]
    partner: dict[tuple[int, ...], tuple[int, ...]]


def global_model(primes: tuple[int, ...], exponents: tuple[int, ...]) -> GlobalFiniteModel:
    moduli = tuple(q**m for q, m in zip(primes, exponents))
    points = tuple(product(*[units(q, m) for q, m in zip(primes, exponents)]))
    partner = {x: tuple_neg(x, moduli) for x in points}
    check(all(partner[partner[x]] == x for x in points), f"sign_involution_{primes}_{exponents}")
    check(all(partner[x] != x for x in points), f"sign_action_free_{primes}_{exponents}")
    half = tuple(sorted(x for x in points if x < partner[x]))
    check(len(half) * 2 == len(points), f"clopen_half_cardinality_{primes}_{exponents}")
    return GlobalFiniteModel(primes, exponents, points, moduli, half, partner)


def global_boundary_check(primes: tuple[int, ...], exponents: tuple[int, ...]) -> None:
    model = global_model(primes, exponents)
    point_index = {x: i for i, x in enumerate(model.points)}
    half_index = {x: i for i, x in enumerate(model.half)}

    finite_columns: list[list[int]] = []
    finite_labels: list[tuple[int, int]] = []
    for p_index, p in enumerate(primes):
        qs = primes[:p_index] + primes[p_index + 1 :]
        ys_exponents = exponents[:p_index] + exponents[p_index + 1 :]
        translation = finite_translation(p, qs, ys_exponents)
        for orbit_index, orbit in enumerate(translation.orbits):
            orbit_set = set(orbit)
            column = []
            for x in model.points:
                y = x[:p_index] + x[p_index + 1 :]
                column.append(-int(y in orbit_set))
            check(any(value == -1 for value in column), f"finite_boundary_nonzero_{p}_{orbit_index}")
            finite_columns.append(column)
            finite_labels.append((p_index, orbit_index))

    arch_columns: list[list[int]] = []
    for h in model.half:
        column = [0] * len(model.points)
        column[point_index[h]] = -1
        column[point_index[model.partner[h]]] = -1
        arch_columns.append(column)
        check(column[point_index[h]] == column[point_index[model.partner[h]]], f"arch_even_column_{h}")

    boundary_columns = finite_columns + arch_columns
    boundary = Matrix.hstack(*[Matrix(c) for c in boundary_columns])

    # The odd-difference matrix on finite columns controls both the global
    # K0 kernel and the cokernel after quotienting by the archimedean image.
    odd_finite_rows: list[list[int]] = []
    for h in model.half:
        row = []
        for column in finite_columns:
            row.append(column[point_index[h]] - column[point_index[model.partner[h]]])
        odd_finite_rows.append(row)
    odd_finite = Matrix(odd_finite_rows)
    check(
        boundary.cols - boundary.rank() == len(finite_columns) - odd_finite.rank(),
        f"global_kernel_dimension_odd_condition_{primes}_{exponents}",
    )
    check(
        boundary.rows - boundary.rank() == len(model.half) - odd_finite.rank(),
        f"global_cokernel_dimension_odd_quotient_{primes}_{exponents}",
    )

    # Test the explicit inverse h -> (h, -S_h|_H) on several bounded tuples.
    coefficient_tests = [
        [0] * len(finite_columns),
        [1 if i % 2 == 0 else -1 for i in range(len(finite_columns))],
        [((i * i + 2 * i + 3) % 5) - 2 for i in range(len(finite_columns))],
    ]
    for test_index, coeffs in enumerate(coefficient_tests):
        finite_value = [
            sum(coeff * column[row] for coeff, column in zip(coeffs, finite_columns))
            for row in range(len(model.points))
        ]
        is_even = all(
            finite_value[point_index[h]] == finite_value[point_index[model.partner[h]]]
            for h in model.half
        )
        if is_even:
            # finite_value is the finite contribution to the boundary, namely
            # -S_h.  Since each archimedean column is -r^*(basis), its
            # coefficient must equal finite_value = -S_h.
            arch_coeffs = [finite_value[point_index[h]] for h in model.half]
            total = [
                finite_value[row]
                + sum(coeff * column[row] for coeff, column in zip(arch_coeffs, arch_columns))
                for row in range(len(model.points))
            ]
            check(all(value == 0 for value in total), f"kernel_inverse_{primes}_{test_index}")
            # Uniqueness follows because each arch column has a unique pair.
            recovered = [finite_value[point_index[h]] for h in model.half]
            check(recovered == arch_coeffs, f"kernel_inverse_unique_{primes}_{test_index}")
        else:
            differences = [
                finite_value[point_index[h]] - finite_value[point_index[model.partner[h]]]
                for h in model.half
            ]
            check(any(value != 0 for value in differences), f"kernel_even_obstruction_{primes}_{test_index}")

    # The odd map kills every archimedean column and maps each finite column
    # to its displayed finite odd-difference column.
    for j, column in enumerate(arch_columns):
        odd = [column[point_index[h]] - column[point_index[model.partner[h]]] for h in model.half]
        check(all(value == 0 for value in odd), f"odd_kills_arch_{primes}_{j}")
    for j, column in enumerate(finite_columns):
        odd = [column[point_index[h]] - column[point_index[model.partner[h]]] for h in model.half]
        check(odd == list(odd_finite[:, j]), f"finite_odd_difference_{primes}_{j}")

    if len(primes) == 1:
        check(len(finite_columns) == 1, "one_prime_finite_invariant_Z")
        check(odd_finite.rank() == 0, "one_prime_finite_odd_map_zero")
        check(boundary.cols - boundary.rank() == 1, "one_prime_global_K0_rank_one")
        check(boundary.rows - boundary.rank() == len(model.half), "one_prime_global_cokernel_half_rank")


def main() -> None:
    check_transition_chain(2, (3,), ((1,), (2,), (3,)))
    check_transition_chain(3, (2,), ((2,), (3,), (4,)))
    check_transition_chain(2, (3, 5), ((1, 1), (2, 2), (3, 2)))
    check_transition_chain(3, (2, 5), ((2, 1), (3, 2), (4, 2)))
    check_transition_chain(5, (2, 3), ((2, 1), (3, 2), (4, 2)))

    global_boundary_check((2,), (3,))
    global_boundary_check((3,), (2,))
    global_boundary_check((2, 3), (3, 2))
    global_boundary_check((2, 5), (3, 2))
    global_boundary_check((3, 5), (2, 2))
    global_boundary_check((2, 3, 5), (2, 2, 2))

    digest = sha256("\n".join(CHECKS).encode("utf-8")).hexdigest()
    print(
        "NONCONSTANT_UNIT_K_OK "
        f"checks={len(CHECKS)} check_name_sha256={digest} "
        "lean=false ocr=false"
    )


if __name__ == "__main__":
    main()
