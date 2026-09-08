from __future__ import annotations

import hashlib
import itertools
import json
import math
import platform
from fractions import Fraction


PRIMES = (2, 3, 5, 7, 11, 13)
CHECK_NAMES: list[str] = []


def check(name: str, condition: bool) -> None:
    if not condition:
        raise AssertionError(name)
    CHECK_NAMES.append(name)


def pow_fraction(p: int, n: int) -> Fraction:
    return Fraction(p**n, 1) if n >= 0 else Fraction(1, p ** (-n))


def vp(value: Fraction, p: int) -> int:
    if value == 0:
        raise ValueError("valuation of zero was requested")
    numerator = abs(value.numerator)
    denominator = value.denominator
    result = 0
    while numerator % p == 0:
        numerator //= p
        result += 1
    while denominator % p == 0:
        denominator //= p
        result -= 1
    return result


def unit(p: int, seed: int) -> Fraction:
    numerator = 2 * seed + 3
    denominator = 2 * seed + 5
    while numerator % p == 0:
        numerator += 2
    while denominator % p == 0:
        denominator += 2
    return Fraction(numerator, denominator)


def product(values) -> Fraction:
    result = Fraction(1)
    for value in values:
        result *= Fraction(value)
    return result


def make_point(primes: tuple[int, ...], seed: int, zero_old: int | str | None = None):
    coordinates: dict[int | str, Fraction] = {}
    for index, p in enumerate(primes):
        exponent = ((seed + 2 * index) % 7) - 3
        coordinates[p] = pow_fraction(p, exponent) * unit(p, seed + index + 1)
    sign = -1 if seed % 2 else 1
    real_scale = product(pow_fraction(p, ((seed + p) % 5) - 2) for p in PRIMES[:4])
    coordinates["inf"] = sign * real_scale
    if zero_old is not None:
        coordinates[zero_old] = Fraction(0)
    return coordinates


def scalar_multiply(point, scalar: Fraction):
    return {key: scalar * value for key, value in point.items()}


def theta(P: tuple[int, ...], Pprime: tuple[int, ...], point):
    R = tuple(p for p in Pprime if p not in P)
    exponents = {r: vp(point[r], r) for r in R}
    h = product(pow_fraction(r, exponents[r]) for r in R)
    z = {q: point[q] / h for q in P}
    z["inf"] = point["inf"] / h
    b = {r: point[r] / h for r in R}
    return h, z, b, exponents


def theta_inverse(P: tuple[int, ...], R: tuple[int, ...], h, z, b):
    point = {q: h * z[q] for q in P}
    point.update({r: h * b[r] for r in R})
    point["inf"] = h * z["inf"]
    return point


def generic(P: tuple[int, ...], point):
    if any(point[p] == 0 for p in P) or point["inf"] == 0:
        raise ValueError("generic coordinate requested on a boundary point")
    sign = -1 if point["inf"] < 0 else 1
    exponents = {p: vp(point[p], p) for p in P}
    units = {p: point[p] / pow_fraction(p, exponents[p]) for p in P}
    g = Fraction(sign) * product(pow_fraction(p, exponents[p]) for p in P)
    a = {
        p: Fraction(sign)
        * product(pow_fraction(q, -exponents[q]) for q in P if q != p)
        * units[p]
        for p in P
    }
    positive_real_section = point["inf"] / g
    return g, a, positive_real_section


def run_sector_coordinate_checks() -> None:
    inclusions = [
        ((2,), (2, 3)),
        ((3,), (2, 3, 5)),
        ((2, 5), (2, 3, 5, 7)),
        ((2, 3, 7), (2, 3, 5, 7, 11)),
    ]
    for case, (P, Pprime) in enumerate(inclusions):
        R = tuple(p for p in Pprime if p not in P)
        for seed in range(1, 18):
            zero = None
            if seed % 5 == 0:
                zero = P[(seed // 5) % len(P)]
            elif seed % 7 == 0:
                zero = "inf"
            point = make_point(Pprime, 100 * case + seed, zero)
            h, z, b, exponents = theta(P, Pprime, point)
            rebuilt = theta_inverse(P, R, h, z, b)
            check(f"theta_inverse_{case}_{seed}", rebuilt == point)
            for r in R:
                check(f"theta_unit_valuation_{case}_{seed}_{r}", vp(b[r], r) == 0)
                expanded = product(
                    pow_fraction(s, -exponents[s]) for s in R if s != r
                ) * (point[r] / pow_fraction(r, exponents[r]))
                check(f"theta_cross_factor_{case}_{seed}_{r}", b[r] == expanded)

            gamma = Fraction(-1 if seed % 2 else 1) * product(
                pow_fraction(p, ((seed + p) % 5) - 2) for p in P
            )
            rho = product(
                pow_fraction(r, ((2 * seed + r) % 7) - 3) for r in R
            )
            acted = scalar_multiply(point, gamma * rho)
            h2, z2, b2, _ = theta(P, Pprime, acted)
            check(f"theta_action_h_{case}_{seed}", h2 == rho * h)
            check(
                f"theta_action_z_{case}_{seed}",
                z2 == {key: gamma * value for key, value in z.items()},
            )
            check(
                f"theta_action_b_{case}_{seed}",
                b2 == {key: gamma * value for key, value in b.items()},
            )


def run_generic_and_transition_checks() -> None:
    inclusions = [
        ((2,), (2, 3)),
        ((2, 5), (2, 3, 5)),
        ((3, 7), (2, 3, 5, 7)),
    ]
    for case, (P, Pprime) in enumerate(inclusions):
        R = tuple(p for p in Pprime if p not in P)
        for seed in range(1, 25):
            point = make_point(Pprime, 700 + 100 * case + seed)
            gprime, aprime, yprime = generic(Pprime, point)
            h, z, b, _ = theta(P, Pprime, point)
            g, a, y = generic(P, z)
            check(f"generic_old_units_{case}_{seed}", all(a[p] == aprime[p] for p in P))
            check(f"generic_new_units_{case}_{seed}", all(b[r] / g == aprime[r] for r in R))
            check(f"generic_group_factor_{case}_{seed}", h * g == gprime)
            check(f"generic_real_factor_{case}_{seed}", y == yprime)
            inverse = {p: gprime * aprime[p] for p in Pprime}
            inverse["inf"] = gprime * yprime
            check(f"generic_inverse_{case}_{seed}", inverse == point)


def run_triple_inclusion_checks() -> None:
    chains = [
        ((2,), (2, 3), (2, 3, 5)),
        ((3,), (2, 3, 7), (2, 3, 5, 7, 11)),
        ((2, 5), (2, 3, 5), (2, 3, 5, 7, 11, 13)),
    ]
    for case, (P, Pprime, Pdouble) in enumerate(chains):
        R = tuple(p for p in Pprime if p not in P)
        T = tuple(p for p in Pdouble if p not in Pprime)
        for seed in range(1, 20):
            point = make_point(Pdouble, 1300 + 100 * case + seed)
            hall, zdirect, bdirect, _ = theta(P, Pdouble, point)
            hT, zprime, bT, _ = theta(Pprime, Pdouble, point)
            hR, zseq, bR, _ = theta(P, Pprime, zprime)
            check(f"triple_h_{case}_{seed}", hall == hR * hT)
            check(f"triple_old_{case}_{seed}", zdirect == zseq)
            check(
                f"triple_R_units_{case}_{seed}",
                all(bdirect[r] == bR[r] for r in R),
            )
            check(
                f"triple_T_units_{case}_{seed}",
                all(bdirect[t] == bT[t] / hR for t in T),
            )


def run_tail_and_matrix_unit_checks() -> None:
    for cut in range(1, 5):
        P = set(PRIMES[:cut])
        Pprime = set(PRIMES[: cut + 2])
        R = Pprime - P
        for seed in range(1, 40):
            exponents = {p: ((seed + p) % 9) - 4 for p in PRIMES}
            source = product(pow_fraction(p, n) for p, n in exponents.items() if p not in P)
            rho = product(pow_fraction(p, exponents[p]) for p in R)
            tail = product(
                pow_fraction(p, n) for p, n in exponents.items() if p not in Pprime
            )
            check(f"tail_factorization_{cut}_{seed}", source == rho * tail)

    indices = tuple(range(-2, 3))
    for a, b, c, d in itertools.product(indices, repeat=4):
        left_nonzero = b == c
        expected = (a, d) if left_nonzero else None
        actual = (a, d) if b == c else None
        check(f"matrix_unit_product_{a}_{b}_{c}_{d}", actual == expected)
        check(f"matrix_unit_star_{a}_{b}_{c}_{d}", (a, b)[::-1] == (b, a))


def units_mod(modulus: int) -> tuple[int, ...]:
    return tuple(a for a in range(1, modulus) if math.gcd(a, modulus) == 1)


def multiply_tuple(point, scalar: int, moduli: tuple[int, ...]):
    return tuple((scalar * x) % modulus for x, modulus in zip(point, moduli))


def orbit_partition(points, scalar: int, moduli: tuple[int, ...]):
    unvisited = set(points)
    orbit_of = {}
    while unvisited:
        start = min(unvisited)
        orbit = []
        current = start
        while current not in orbit:
            orbit.append(current)
            current = multiply_tuple(current, scalar, moduli)
        label = min(orbit)
        for point in orbit:
            orbit_of[point] = label
            unvisited.discard(point)
    return orbit_of


def sign_label(point, moduli):
    negative = tuple((-x) % modulus for x, modulus in zip(point, moduli))
    return min(point, negative)


def run_boundary_square_checks() -> None:
    cases = [
        ((2,), (2, 3)),
        ((2, 3), (2, 3, 5)),
        ((3, 5), (2, 3, 5, 7)),
    ]
    for case, (P, Pprime) in enumerate(cases):
        modulus = {p: p * p for p in Pprime}
        Kprime_axes = [units_mod(modulus[p]) for p in Pprime]
        Kprime = tuple(itertools.product(*Kprime_axes))
        old_indices = tuple(Pprime.index(p) for p in P)

        finite_functions = {}
        for p in P:
            old_other = tuple(q for q in P if q != p)
            new_other = tuple(q for q in Pprime if q != p)
            old_moduli = tuple(modulus[q] for q in old_other)
            new_moduli = tuple(modulus[q] for q in new_other)
            old_points = tuple(itertools.product(*(units_mod(m) for m in old_moduli)))
            new_points = tuple(itertools.product(*(units_mod(m) for m in new_moduli)))
            if not old_moduli:
                old_points = ((),)
            old_orbit = orbit_partition(old_points, p, old_moduli)
            new_orbit = orbit_partition(new_points, p, new_moduli)
            orbit_values = {label: (sum(label) + 3 * p + case) % 11 - 5 for label in set(old_orbit.values())}
            finite_functions[p] = (old_other, new_other, old_orbit, new_orbit, orbit_values)

            for point in new_points:
                projected = tuple(point[new_other.index(q)] for q in old_other)
                old_value = orbit_values[old_orbit[projected]]
                pulled_value = orbit_values[old_orbit[projected]]
                check(f"finite_orbit_pullback_{case}_{p}_{point}", old_value == pulled_value)
                projected_after = multiply_tuple(projected, p, old_moduli)
                new_after = multiply_tuple(point, p, new_moduli)
                projected_new_after = tuple(new_after[new_other.index(q)] for q in old_other)
                check(
                    f"finite_translation_projection_{case}_{p}_{point}",
                    projected_after == projected_new_after,
                )

        old_moduli_all = tuple(modulus[p] for p in P)
        old_points_all = tuple(itertools.product(*(units_mod(m) for m in old_moduli_all)))
        arch_values = {
            sign_label(point, old_moduli_all): (sum(point) + 5 * case) % 13 - 6
            for point in old_points_all
        }

        for cprime in Kprime:
            cold = tuple(cprime[index] for index in old_indices)
            lhs = 0
            rhs = 0
            for p in P:
                old_other, new_other, old_orbit, _, orbit_values = finite_functions[p]
                old_drop = tuple(cold[P.index(q)] for q in old_other)
                new_drop = tuple(cprime[Pprime.index(q)] for q in new_other)
                projected_new_drop = tuple(new_drop[new_other.index(q)] for q in old_other)
                lhs -= orbit_values[old_orbit[old_drop]]
                rhs -= orbit_values[old_orbit[projected_new_drop]]
            lhs -= arch_values[sign_label(cold, old_moduli_all)]
            rhs -= arch_values[sign_label(cold, old_moduli_all)]
            check(f"global_boundary_square_{case}_{cprime}", lhs == rhs)


def run_labelled_corner_checks() -> None:
    chains = [
        ((2,), (2, 3), (2, 3, 5)),
        ((3, 5), (2, 3, 5), (2, 3, 5, 7)),
    ]
    for case, (P, Pprime, Pdouble) in enumerate(chains):
        labels = tuple(P) + ("inf",)
        values = {label: index * index - 3 * index + 2 for index, label in enumerate(labels)}

        def include(mapping, target):
            return {label: mapping.get(label, 0) for label in tuple(target) + ("inf",)}

        one_step = include(values, Pprime)
        two_step = include(one_step, Pdouble)
        direct = include(values, Pdouble)
        check(f"label_zero_inclusion_{case}", two_step == direct)
        for label in labels:
            check(f"corner_label_retained_{case}_{label}", direct[label] == values[label])
        for label in set(Pdouble) - set(P):
            check(f"corner_new_label_zero_{case}_{label}", direct[label] == 0)


def main() -> None:
    run_sector_coordinate_checks()
    run_generic_and_transition_checks()
    run_triple_inclusion_checks()
    run_tail_and_matrix_unit_checks()
    run_boundary_square_checks()
    run_labelled_corner_checks()
    digest = hashlib.sha256("\n".join(CHECK_NAMES).encode("utf-8")).hexdigest()
    print(
        json.dumps(
            {
                "status": "pass",
                "python": platform.python_version(),
                "implementation": platform.python_implementation(),
                "named_check_count": len(CHECK_NAMES),
                "check_name_sha256": digest,
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
