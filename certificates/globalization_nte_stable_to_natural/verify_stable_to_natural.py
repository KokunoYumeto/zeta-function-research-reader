#!/usr/bin/env python3
"""Finite-coordinate replay for the stable-to-natural extension morphism.

This certificate checks the exact algebraic identities that have finite matrix
or lattice coordinates.  It does not replace the printed proofs of
essentiality, Green imprimitivity, linking-algebra stabilization, multiplier
extension, Busby reconstruction, or C*-exactness.
"""

from __future__ import annotations

import json
import random
import sys
from dataclasses import dataclass, field

import sympy as sp


@dataclass
class Ledger:
    checks: int = 0
    names: list[str] = field(default_factory=list)

    def require(self, condition: bool, name: str) -> None:
        if not condition:
            raise AssertionError(name)
        self.checks += 1
        self.names.append(name)


def cantor(j: int, k: int) -> int:
    return ((j + k) * (j + k + 1)) // 2 + k


def block_diag(blocks: list[sp.Matrix]) -> sp.Matrix:
    if not blocks:
        return sp.zeros(0, 0)
    return sp.diag(*blocks)


def repeat_unit_fibres(matrix: sp.Matrix, unit_count: int) -> sp.Matrix:
    return sp.kronecker_product(sp.eye(unit_count), matrix)


def place_corner(
    block: sp.Matrix, place: int, place_count: int, unit_count: int
) -> sp.Matrix:
    """Put one 2x2 block in the named place corner of every unit fibre."""
    fibre_dim = 2 * place_count
    result = sp.zeros(unit_count * fibre_dim, unit_count * fibre_dim)
    for unit in range(unit_count):
        offset = unit * fibre_dim + 2 * place
        result[offset : offset + 2, offset : offset + 2] = block
    return result


def compress_place(
    matrix: sp.Matrix, place: int, place_count: int, unit: int
) -> sp.Matrix:
    fibre_dim = 2 * place_count
    offset = unit * fibre_dim + 2 * place
    return matrix[offset : offset + 2, offset : offset + 2]


def label_map(prime_count: int) -> sp.Matrix:
    """R_P: Z^(n+2) -> Z^(n+1), merging only the two sign labels."""
    result = sp.zeros(prime_count + 1, prime_count + 2)
    for p in range(prime_count):
        result[p, p] = 1
    result[prime_count, prime_count] = 1
    result[prime_count, prime_count + 1] = 1
    return result


def enriched_label_map(prime_count: int) -> sp.Matrix:
    """Add the split D_2 carrier, retaining both archimedean coordinates."""
    base = label_map(prime_count)
    arch = sp.zeros(2, prime_count + 2)
    arch[0, prime_count] = 1
    arch[1, prime_count + 1] = 1
    return base.col_join(arch)


def main() -> int:
    ledger = Ledger()
    rng = random.Random(0x5A17E)

    # Cantor-pairing ranges are disjoint, so the declared isometries have
    # orthogonal ranges and compression recovers the named input coordinate.
    pairs = [(j, k) for j in range(12) for k in range(32)]
    values = [cantor(j, k) for j, k in pairs]
    ledger.require(len(values) == len(set(values)), "cantor_pairing_injective")
    ledger.require(min(values) == 0, "cantor_pairing_contains_zero")

    for prime_count in range(1, 9):
        place_count = prime_count + 1
        unit_count = prime_count + 2

        # Algebraic multiplier-corner identity
        # beta(mu((b_v))) = sum_v T_v beta(b_v) T_v^*.
        for trial in range(5):
            blocks = [
                sp.Matrix(
                    2,
                    2,
                    [rng.randint(-7, 7) for _ in range(4)],
                )
                for _ in range(place_count)
            ]
            mu = block_diag(blocks)
            beta_mu = repeat_unit_fibres(mu, unit_count)
            corner_sum = sp.zeros(*beta_mu.shape)
            for place, block in enumerate(blocks):
                corner_sum += place_corner(
                    block, place, place_count, unit_count
                )
            ledger.require(
                beta_mu == corner_sum,
                f"ideal_factorization_n{prime_count}_trial{trial}",
            )

            for unit in range(unit_count):
                for place, block in enumerate(blocks):
                    ledger.require(
                        compress_place(
                            beta_mu, place, place_count, unit
                        )
                        == block,
                        (
                            "corner_inverse_"
                            f"n{prime_count}_t{trial}_u{unit}_v{place}"
                        ),
                    )

            # The same finite block calculation is the algebraic content of
            # tau_nat alpha = dot(j) dot(mu) tau^oplus.
            tau_blocks = [
                sp.Matrix(
                    2,
                    2,
                    [rng.randint(-11, 11) for _ in range(4)],
                )
                for _ in range(place_count)
            ]
            busby_left = repeat_unit_fibres(
                block_diag(tau_blocks), unit_count
            )
            busby_right = sp.zeros(*busby_left.shape)
            for place, block in enumerate(tau_blocks):
                busby_right += place_corner(
                    block, place, place_count, unit_count
                )
            ledger.require(
                busby_left == busby_right,
                f"busby_corner_equation_n{prime_count}_trial{trial}",
            )

        r_map = label_map(prime_count)
        formal_boundary = -sp.ones(1, prime_count + 2)
        natural_boundary = -sp.ones(1, prime_count + 1)
        ledger.require(
            natural_boundary * r_map == formal_boundary,
            f"connecting_map_naturality_n{prime_count}",
        )
        ledger.require(
            r_map.rank() == prime_count + 1,
            f"label_map_rank_n{prime_count}",
        )

        sign_difference = sp.zeros(prime_count + 2, 1)
        sign_difference[prime_count, 0] = 1
        sign_difference[prime_count + 1, 0] = -1
        ledger.require(
            r_map * sign_difference == sp.zeros(prime_count + 1, 1),
            f"sign_difference_kernel_n{prime_count}",
        )
        nullspace = r_map.nullspace()
        ledger.require(
            len(nullspace) == 1,
            f"label_map_kernel_dimension_n{prime_count}",
        )
        ledger.require(
            sp.Matrix.hstack(nullspace[0], sign_difference).rank() == 1,
            f"label_map_exact_kernel_n{prime_count}",
        )

        enriched = enriched_label_map(prime_count)
        ledger.require(
            enriched.rank() == prime_count + 2,
            f"enriched_label_map_injective_n{prime_count}",
        )
        ledger.require(
            enriched * sign_difference != sp.zeros(prime_count + 3, 1),
            f"enrichment_retains_sign_difference_n{prime_count}",
        )

        # Constant unit-fibre inclusion is split by every evaluation.  A
        # displayed nonconstant rank function stays outside its image.
        for scalar in range(-5, 6):
            constant = sp.Matrix([scalar] * unit_count)
            for point in range(unit_count):
                ledger.require(
                    constant[point, 0] == scalar,
                    (
                        "evaluation_left_inverse_"
                        f"n{prime_count}_s{scalar}_k{point}"
                    ),
                )
        nonconstant = sp.Matrix(list(range(unit_count)))
        ledger.require(
            len(set(nonconstant)) > 1,
            f"nonconstant_unit_class_outside_image_n{prime_count}",
        )

    # Minimal commutative symmetric carrier: C has no two nonzero orthogonal
    # projections, while C^2 has the two coordinate projections and their swap.
    projections_c = [0, 1]
    ledger.require(
        not any(
            p != 0 and q != 0 and p * q == 0
            for p in projections_c
            for q in projections_c
        ),
        "one_scalar_carrier_cannot_hold_two_sign_projections",
    )
    e_plus = sp.Matrix([1, 0])
    e_minus = sp.Matrix([0, 1])
    swap = sp.Matrix([[0, 1], [1, 0]])
    ledger.require(
        e_plus.dot(e_minus) == 0,
        "D2_sign_projections_orthogonal",
    )
    ledger.require(
        swap * e_plus == e_minus and swap * e_minus == e_plus,
        "D2_swap_symmetry",
    )

    output = {
        "status": "pass",
        "checks": ledger.checks,
        "prime_counts": [1, 8],
        "unit_fibre_samples": "n+2",
        "lean_used": False,
        "scope": [
            "Cantor-corner orthogonality and compression",
            "constant-unit ideal factorization",
            "finite matrix form of the Busby corner equation",
            "boundary-map naturality",
            "exact sign-difference kernel",
            "injectivity after split sign enrichment",
            "evaluation left inverses and nonconstant classes",
            "minimal two-coordinate symmetric sign carrier",
        ],
        "nonclaims": [
            "No C*-analytic theorem is replaced by this replay.",
            "No endpoint or individual-zero conclusion is tested.",
        ],
        "python": sys.version,
        "sympy": sp.__version__,
    }
    print(json.dumps(output, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
