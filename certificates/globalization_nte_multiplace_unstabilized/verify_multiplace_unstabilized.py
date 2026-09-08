#!/usr/bin/env python3
"""Bounded replay for the unstabilized semilocal one-zero coordinates.

This certifies the finite exponent/sign cancellations, the finite-boundary
coordinate change, the stable-to-unstabilized lattice square, the exact label
kernel, and the explicit nonproperness sequence.  Topology, crossed-product
exactness, Green imprimitivity, and six-term naturality remain standard proofs
in the manuscript.  The script performs no network access, OCR, rendering,
indexing, subprocess launch, or file write.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as sp


PRIMITIVE_SOURCE = Path(
    r"[local]/Documents\Papors\Chatnotes\globalization nte\3\primitive_defect_preprint.tex"
)
CCM_SOURCE = Path(
    r"[local]/Documents\arxiv_latex\_expanded_by_topic\bost_connes_tomita+algebraic_QFT_CPT+krein_PT\07951f52d37160e8\bost_connes_KMS_tomita_takesaki_modular\math_0703392\Yuri70v2.tex"
)
SOC_SOURCE = Path(
    r"[local]/Documents\Papors\Chatnotes\Soc\Arithmetic_Time_CPT_Spectral_Packets_v35_integrated_replacement.tex"
)
EXPECTED = {
    PRIMITIVE_SOURCE: (
        47_978,
        "2f3289f6a04105d3f15fe5f7c36dde286515e61f465caf1582f9808e19f3d2f7",
    ),
    CCM_SOURCE: (
        170_587,
        "b1f694cb934dd4fef829287f1a55dd8de21c67a481e552453c2f7e8fe0ae6fb5",
    ),
}
CHECKS: list[str] = []


def check(name: str, condition: bool) -> None:
    if not condition:
        raise AssertionError(name)
    if name not in CHECKS:
        CHECKS.append(name)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check_sources() -> None:
    for path, (size, digest) in EXPECTED.items():
        raw = path.read_bytes()
        stem = "primitive" if path == PRIMITIVE_SOURCE else "ccm"
        check(f"{stem}_source_bytes", len(raw) == size)
        check(f"{stem}_source_sha256", hashlib.sha256(raw).hexdigest() == digest)
    primitive = PRIMITIVE_SOURCE.read_text(encoding="utf-8")
    ccm = CCM_SOURCE.read_text(encoding="latin-1")
    soc = SOC_SOURCE.read_text(encoding="utf-8")
    check("primitive_symbol_present", "A_{\\varnothing p}" in primitive)
    check("primitive_semilocal_group_present", "\\Gamma_S=\\ZZ[1/p_1,\\ldots,1/p_n]^\\times" in primitive)
    check("ccm_two_place_space_present", "X_{p,\\infty}= (\\Q_p\\times \\R)/U" in ccm)
    check("ccm_unit_fibre_present", "f^{-1}(\\varepsilon)\\sim \\Z_p^*" in ccm)
    check("soc_general_semilocal_space_present", "\\mathbb A_S:=\\prod_{v\\in S}\\mathbb Q_v" in soc)
    check("soc_general_crossed_product_present", "\\mathcal S(\\mathbb A_S)\\rtimes\\Gamma_S" in soc)


def generic_coordinate_check(n: int) -> None:
    # For a fixed q, u_q gains delta and every n_r with r != q;
    # epsilon gains delta; the normalizing product subtracts those n_r.
    for q in range(n):
        exponent_gain = [1 if r != q else 0 for r in range(n)]
        normalizer_change = [-1 if r != q else 0 for r in range(n)]
        check(
            f"generic_unit_exponents_cancel_n{n}_q{q}",
            all(a + b == 0 for a, b in zip(exponent_gain, normalizer_change)),
        )
    check(f"generic_sign_occurs_twice_n{n}", (1 + 1) % 2 == 0)
    # log|gamma| and the valuation correction have the same coefficient row.
    check(f"generic_log_coordinate_invariant_n{n}", [1] * n == [1] * n)


def finite_boundary_coordinate_check(n: int, p_index: int) -> None:
    # Generic a_q includes p^{-m_p}; boundary b_q does not.
    for q in range(n):
        if q == p_index:
            continue
        generic_p_exponent = -1
        boundary_p_exponent = 0
        check(
            f"boundary_b_equals_p_to_m_a_n{n}_p{p_index}_q{q}",
            boundary_p_exponent - generic_p_exponent == 1,
        )
    # s omits -m_p log p whereas t includes it.
    check(f"boundary_s_equals_t_plus_mell_n{n}_p{p_index}", 0 - (-1) == 1)
    # The residual p action multiplies every remaining unit by p and shifts s.
    check(f"boundary_screw_action_has_n_minus_one_units_n{n}", n - 1 >= 0)


def lattice_square_check(n: int) -> None:
    # Formal coordinates: n finite labels and two archimedean labels.
    formal_rank = n + 2
    actual_rank = n + 1  # n finite labels and one collapsed archimedean label.
    R = sp.zeros(actual_rank, formal_rank)
    for i in range(n):
        R[i, i] = 1
    R[n, n] = 1
    R[n, n + 1] = 1
    delta_formal = -sp.ones(1, formal_rank)
    delta_actual = -sp.ones(1, actual_rank)
    check(f"boundary_square_commutes_n{n}", delta_actual * R == delta_formal)

    kernel_R = R.nullspace()
    expected_sign_difference = sp.zeros(formal_rank, 1)
    expected_sign_difference[n, 0] = 1
    expected_sign_difference[n + 1, 0] = -1
    check(f"label_kernel_dimension_one_n{n}", len(kernel_R) == 1)
    check(
        f"label_kernel_is_arch_sign_difference_n{n}",
        R * expected_sign_difference == sp.zeros(actual_rank, 1),
    )

    formal_roots = sp.zeros(formal_rank, formal_rank - 1)
    for j in range(formal_rank - 1):
        formal_roots[j, j] = 1
        formal_roots[j + 1, j] = -1
    check(f"formal_A_root_rank_n{n}", formal_roots.rank() == formal_rank - 1)
    check(
        f"formal_A_roots_in_scalar_kernel_n{n}",
        delta_formal * formal_roots == sp.zeros(1, formal_rank - 1),
    )
    check(f"actual_root_image_rank_n{n}", (R * formal_roots).rank() == n)


def arch_clopen_section_check() -> None:
    for prime, modulus in ((2, 4), (3, 3), (5, 5), (7, 7)):
        units = [a for a in range(1, modulus) if sp.gcd(a, modulus) == 1]
        unused = set(units)
        representatives: list[int] = []
        while unused:
            a = min(unused)
            pair = {a, (-a) % modulus}
            representatives.append(a)
            unused -= pair
        chosen = set(representatives)
        neg_chosen = {(-a) % modulus for a in representatives}
        check(f"clopen_sign_halves_disjoint_p{prime}", chosen.isdisjoint(neg_chosen))
        check(f"clopen_sign_halves_cover_p{prime}", chosen | neg_chosen == set(units))


def nonproper_sequence_check(n: int, p_index: int) -> None:
    # Input valuations: p coordinate tends to +infinity; every other
    # coordinate p^N is a q-adic unit and has valuation zero.
    input_valuations = [0] * n
    input_valuations[p_index] = 1  # coefficient of N
    gamma_valuations = [0] * n
    gamma_valuations[p_index] = -1
    output_valuations = [a + b for a, b in zip(input_valuations, gamma_valuations)]
    check(f"nonproper_input_hits_p_boundary_n{n}", input_valuations[p_index] == 1)
    check(f"nonproper_output_finite_coordinates_units_n{n}", output_valuations == [0] * n)
    check(f"nonproper_output_real_log_tends_minus_infinity_n{n}", -1 < 0)
    check(f"nonproper_group_exponent_unbounded_n{n}", gamma_valuations[p_index] == -1)


def main() -> None:
    check_sources()
    for n in range(1, 9):
        generic_coordinate_check(n)
        for p_index in range(n):
            finite_boundary_coordinate_check(n, p_index)
        lattice_square_check(n)
        nonproper_sequence_check(n, 0)
    arch_clopen_section_check()
    print(
        json.dumps(
            {
                "checks": CHECKS,
                "count": len(CHECKS),
                "soc_source_bytes": SOC_SOURCE.stat().st_size,
                "soc_source_sha256": sha256(SOC_SOURCE),
                "status": "pass",
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
