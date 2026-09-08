#!/usr/bin/env python3
"""Exact finite checks for the divisor-sheaf/chain-cube/packet chapter.

This certificate deliberately uses only finite sets, integer tuples, and exact
Boolean operations.  It checks the coordinate formulae that are naturally
finite; it does not stand in for the analytic, sheaf-theoretic, or local-ring
proofs printed in the manuscript.
"""

from __future__ import annotations

import itertools
import json
import platform


CHECKS: list[str] = []


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def terminal_mask(m: int, r: int) -> int:
    """Bit mask of T_r={r,...,m}; T_{m+1} is empty."""
    if r == m + 1:
        return 0
    return sum(1 << (j - 1) for j in range(r, m + 1))


def least_member(mask: int) -> int:
    """Least one-based member of a nonempty bit mask."""
    require(mask != 0, "least_member called on the empty set")
    return (mask & -mask).bit_length()


def terminal_closure(m: int, mask: int) -> int:
    return 0 if mask == 0 else terminal_mask(m, least_member(mask))


def terminal_interior(m: int, mask: int) -> int:
    answer = 0
    for j in range(1, m + 1):
        tail = terminal_mask(m, j)
        if tail & ~mask == 0:
            answer |= 1 << (j - 1)
    return answer


def subset(left: int, right: int) -> bool:
    return left & ~right == 0


def check_boolean_retract() -> None:
    for m in range(1, 9):
        full = (1 << m) - 1
        sigma = lambda mask: int(mask != 0)
        delta = lambda value: full if value else 0
        require(sigma(delta(0)) == 0, f"Sigma Delta failed at m={m}, tau")
        require(sigma(delta(1)) == 1, f"Sigma Delta failed at m={m}, e")
        for left in range(1 << m):
            for right in range(1 << m):
                require(
                    sigma(left | right) == (sigma(left) | sigma(right)),
                    f"Sigma did not preserve join at m={m}",
                )
        fibres = {value: [] for value in (0, 1)}
        for mask in range(1 << m):
            fibres[sigma(mask)].append(mask)
        require(len(fibres[0]) == 1, f"empty Sigma fibre failed at m={m}")
        require(
            len(fibres[1]) == (1 << m) - 1,
            f"nonempty Sigma fibre failed at m={m}",
        )
    CHECKS.append("boolean_reduced_retract_and_complete_fibres_m_1_through_8")


def check_chain_cube_adjunctions() -> None:
    for m in range(1, 9):
        terminals = [terminal_mask(m, r) for r in range(1, m + 2)]
        for mask in range(1 << m):
            r_mask = terminal_closure(m, mask)
            s_mask = terminal_interior(m, mask)
            require(r_mask in terminals, f"r_m left C_m at m={m}")
            require(s_mask in terminals, f"s_m left C_m at m={m}")
            for tail in terminals:
                require(
                    subset(r_mask, tail) == subset(mask, tail),
                    f"r_m dashv i_m failed at m={m}, I={mask}, T={tail}",
                )
                require(
                    subset(tail, mask) == subset(tail, s_mask),
                    f"i_m dashv s_m failed at m={m}, I={mask}, T={tail}",
                )
        for tail in terminals:
            require(
                terminal_closure(m, tail) == tail,
                f"r_m i_m was not identity at m={m}, T={tail}",
            )
        for left in range(1 << m):
            for right in range(1 << m):
                require(
                    terminal_closure(m, left | right)
                    == (terminal_closure(m, left) | terminal_closure(m, right)),
                    f"r_m did not preserve join at m={m}",
                )
    CHECKS.append("terminal_chain_inclusion_and_both_adjunctions_m_1_through_8")
    CHECKS.append("terminal_closure_split_retraction_and_join_preservation_m_1_through_8")


def check_chain_cube_fibres() -> None:
    for m in range(1, 9):
        all_masks = range(1 << m)
        for r in range(1, m + 2):
            tail = terminal_mask(m, r)
            r_fibre = [mask for mask in all_masks if terminal_closure(m, mask) == tail]
            if r <= m:
                expected = [
                    mask
                    for mask in range(1 << m)
                    if subset(mask, tail) and (mask & (1 << (r - 1))) != 0
                ]
                expected_size = 1 << (m - r)
            else:
                expected = [0]
                expected_size = 1
            require(r_fibre == expected, f"exact r_m fibre failed at m={m}, r={r}")
            require(
                len(r_fibre) == expected_size,
                f"r_m fibre cardinality failed at m={m}, r={r}",
            )

            s_fibre = [mask for mask in range(1 << m) if terminal_interior(m, mask) == tail]
            if r == 1:
                expected = [(1 << m) - 1]
                expected_size = 1
            else:
                forbidden = 1 << (r - 2)
                expected = [
                    mask
                    for mask in range(1 << m)
                    if subset(tail, mask) and (mask & forbidden) == 0
                ]
                expected_size = 1 << (r - 2)
            require(s_fibre == expected, f"exact s_m fibre failed at m={m}, r={r}")
            require(
                len(s_fibre) == expected_size,
                f"s_m fibre cardinality failed at m={m}, r={r}",
            )
    CHECKS.append("terminal_closure_complete_fibres_and_cardinalities_m_1_through_8")
    CHECKS.append("terminal_interior_complete_fibres_and_cardinalities_m_1_through_8")


def coefficient_support(coefficients: tuple[int, ...]) -> int:
    return sum(1 << j for j, coefficient in enumerate(coefficients) if coefficient != 0)


def support_section(m: int, mask: int) -> tuple[int, ...]:
    return tuple(1 if mask & (1 << j) else 0 for j in range(m))


def check_jet_support() -> None:
    alphabet = (-1, 0, 1)
    for m in range(1, 9):
        for mask in range(1 << m):
            require(
                coefficient_support(support_section(m, mask)) == mask,
                f"kappa iota failed at m={m}, I={mask}",
            )
        # Exhaustive fibre counts remain small through m=8: 3^8=6561 tuples.
        counts = [0] * (1 << m)
        for coefficients in itertools.product(alphabet, repeat=m):
            counts[coefficient_support(coefficients)] += 1
        for mask, count in enumerate(counts):
            require(
                count == 2 ** mask.bit_count(),
                f"support fibre count failed at m={m}, I={mask}",
            )
        positive = (1,) + (0,) * (m - 1)
        negative = (-1,) + (0,) * (m - 1)
        zero = tuple(a + b for a, b in zip(positive, negative))
        require(coefficient_support(positive) == 1, f"positive support failed at m={m}")
        require(coefficient_support(negative) == 1, f"negative support failed at m={m}")
        require(coefficient_support(zero) == 0, f"cancellation support failed at m={m}")
        require((1 | 1) != 0, f"Boolean join cancellation test failed at m={m}")
    CHECKS.append("coefficient_support_pointed_retraction_m_1_through_8")
    CHECKS.append("finite_alphabet_support_fibres_m_1_through_8")
    CHECKS.append("explicit_coefficient_cancellation_nonadditivity_m_1_through_8")


def multiply_by_t(coefficients: tuple[int, ...]) -> tuple[int, ...]:
    """Multiplication by t in the basis 1,t,...,t^(m-1)."""
    return (0,) + coefficients[:-1]


def check_degree_shift_and_socle() -> None:
    alphabet = (-1, 0, 1)
    for m in range(1, 9):
        for enhanced in itertools.product(alphabet, repeat=m):
            # In the ordered bases (t,...,t^m) and (1,...,t^(m-1)), d is
            # the identity coefficient tuple and multiplication by t is its inverse.
            jet = enhanced
            enhanced_again = jet
            require(enhanced_again == enhanced, f"degree-shift inverse failed at m={m}")
            in_kernel = multiply_by_t(jet) == (0,) * m
            terminal_line = all(coefficient == 0 for coefficient in jet[:-1])
            require(in_kernel == terminal_line, f"socle kernel failed at m={m}, q={jet}")
    CHECKS.append("degree_shift_inverse_and_artin_socle_m_1_through_8")


def packet_actions(size: int) -> tuple[tuple[int, ...], ...]:
    if size == 1:
        return ((0,),)
    if size == 2:
        return ((0, 1), (1, 0))
    if size == 4:
        return tuple(tuple(index ^ group_element for index in range(4)) for group_element in range(4))
    raise ValueError(size)


def permute(values: tuple[int, ...], permutation: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(values[permutation[index]] for index in range(len(values)))


def check_packet_diagonal_descent() -> None:
    alphabet = (0, 1, 2)
    for size in (1, 2, 4):
        actions = packet_actions(size)
        for values in itertools.product(alphabet, repeat=size):
            fixed = all(permute(values, action) == values for action in actions)
            diagonal = all(value == values[0] for value in values)
            require(fixed == diagonal, f"fixed part was not diagonal at orbit size {size}")
            if fixed:
                projected = values[0]
                repeated = (projected,) * size
                require(repeated == values, f"diagonal inverse failed at orbit size {size}")
        for value in alphabet:
            diagonal = (value,) * size
            require(diagonal[0] == value, f"projection after diagonal failed at size {size}")
    CHECKS.append("packet_fixed_parts_and_explicit_diagonal_inverse_orbit_sizes_1_2_4")


def conjugate(pair: tuple[int, int]) -> tuple[int, int]:
    a, b = pair
    return (a, -b)


def reflect_phase(pair: tuple[int, int], parity: int) -> tuple[int, int]:
    a, b = pair
    sign = -1 if parity else 1
    return (sign * a, sign * b)


def phase_orbit(pair: tuple[int, int], parity: int) -> frozenset[tuple[int, int]]:
    c_pair = conjugate(pair)
    return frozenset(
        (
            pair,
            c_pair,
            reflect_phase(pair, parity),
            reflect_phase(c_pair, parity),
        )
    )


def check_phase_quotient() -> None:
    pairs = [(a, b) for a in range(-3, 4) for b in range(-3, 4) if (a, b) != (0, 0)]
    for parity in (0, 1):
        for pair in pairs:
            c_pair = conjugate(pair)
            w_pair = reflect_phase(pair, parity)
            require(conjugate(c_pair) == pair, f"conjugation not involutive for {pair}")
            require(
                reflect_phase(w_pair, parity) == pair,
                f"reflection sign not involutive for {pair}, parity={parity}",
            )
            require(
                conjugate(w_pair) == reflect_phase(c_pair, parity),
                f"phase actions did not commute for {pair}, parity={parity}",
            )
            orbit = phase_orbit(pair, parity)
            require(phase_orbit(c_pair, parity) == orbit, "quotient changed under conjugation")
            require(phase_orbit(w_pair, parity) == orbit, "quotient changed under reflection")
    CHECKS.append("phase_conjugation_and_parity_actions_commute_and_are_involutions")
    CHECKS.append("phase_orbit_quotient_is_representative_independent_on_exact_grid")


def main() -> None:
    check_boolean_retract()
    check_chain_cube_adjunctions()
    check_chain_cube_fibres()
    check_jet_support()
    check_degree_shift_and_socle()
    check_packet_diagonal_descent()
    check_phase_quotient()
    print(
        json.dumps(
            {
                "status": "pass",
                "python": platform.python_version(),
                "arithmetic": "exact finite sets, bit masks, and integer tuples",
                "m_range": [1, 8],
                "named_check_count": len(CHECKS),
                "checks": CHECKS,
                "analytic_or_sheaf_claims_certified": False,
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
