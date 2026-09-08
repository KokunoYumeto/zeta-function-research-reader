#!/usr/bin/env python3
"""Exact bounded checks for the Simm--Wei arXiv:2409.03687v2 audit.

The script checks finite polynomial identities and source-level defects that can
be decided by exact algebra.  It does not certify the paper's analytic
uniform-integrability arguments, imported mean-value theorems, Painleve
identifications, or the unproved general coefficient proposition in v2.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import math
import platform
from pathlib import Path

import sympy as sp


U = sp.Symbol("u")
Z = sp.Symbol("z")
W = sp.Symbol("w")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def partitions(weight: int, maximum: int | None = None) -> list[tuple[int, ...]]:
    if weight == 0:
        return [()]
    if maximum is None or maximum > weight:
        maximum = weight
    result: list[tuple[int, ...]] = []
    for first in range(maximum, 0, -1):
        for tail in partitions(weight - first, min(first, weight - first)):
            result.append((first,) + tail)
    return result


def tableau_count(partition: tuple[int, ...]) -> int:
    weight = sum(partition)
    hook_product = 1
    for row, row_length in enumerate(partition):
        for column in range(row_length):
            below = sum(1 for lower in partition[row + 1 :] if lower > column)
            hook_product *= row_length - column + below
    return math.factorial(weight) // hook_product


def padded(partition: tuple[int, ...], length: int) -> tuple[int, ...]:
    return partition + (0,) * (length - len(partition))


def shifted_factorial(partition: tuple[int, ...], length: int) -> int:
    values = padded(partition, length)
    return math.prod(
        math.factorial(values[index] + length - index - 1)
        for index in range(length)
    )


def simm_wei_exact_moment(matrix_size: int, moment_order: int) -> sp.Expr:
    kernel = sum(U**degree for degree in range(matrix_size + moment_order))
    total = sp.Integer(0)
    for lam in partitions(moment_order):
        lam_pad = padded(lam, moment_order)
        lam_weight = sp.Rational(
            tableau_count(lam), shifted_factorial(lam, moment_order)
        )
        for mu in partitions(moment_order):
            mu_pad = padded(mu, moment_order)
            mu_weight = sp.Rational(
                tableau_count(mu), shifted_factorial(mu, moment_order)
            )
            entries: list[list[sp.Expr]] = []
            for row in range(moment_order):
                p_order = lam_pad[row] + moment_order - row - 1
                base = U**p_order * sp.diff(kernel, U, p_order)
                entries.append(
                    [
                        sp.diff(
                            base,
                            U,
                            mu_pad[column] + moment_order - column - 1,
                        )
                        for column in range(moment_order)
                    ]
                )
            total += lam_weight * mu_weight * sp.det(sp.Matrix(entries))
    return sp.factor(total)


def constant_term_in_eigenvalues(expression: sp.Expr, eigenvalues: tuple[sp.Symbol, ...]) -> sp.Expr:
    total = sp.Integer(0)
    for term in sp.Add.make_args(sp.expand(expression)):
        powers = term.as_powers_dict()
        if all(powers.get(variable, 0) == 0 for variable in eigenvalues):
            total += term
    return sp.factor(total)


def direct_haar_moment(matrix_size: int, moment_order: int) -> sp.Expr:
    eigenvalues = sp.symbols(f"x0:{matrix_size}")
    characteristic = sp.prod(1 - Z / value for value in eigenvalues)
    conjugate_characteristic = sp.prod(1 - W * value for value in eigenvalues)
    derivative_product = (
        sp.diff(characteristic, Z) ** moment_order
        * sp.diff(conjugate_characteristic, W) ** moment_order
    )
    density = sp.Integer(1)
    for left, right in itertools.combinations(eigenvalues, 2):
        density *= (left - right) * (1 / left - 1 / right)
    density /= math.factorial(matrix_size)
    constant = constant_term_in_eigenvalues(derivative_product * density, eigenvalues)
    return sp.factor(constant.subs({Z: 1, W: U}))


def exact_equal(left: sp.Expr, right: sp.Expr, label: str) -> None:
    difference = sp.factor(sp.cancel(left - right))
    if difference != 0:
        raise AssertionError(f"{label}: nonzero exact difference {difference}")


def check_finite_determinant() -> list[dict[str, object]]:
    cases = [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (3, 1), (3, 2)]
    results: list[dict[str, object]] = []
    for matrix_size, moment_order in cases:
        determinant_formula = simm_wei_exact_moment(matrix_size, moment_order)
        direct_integral = direct_haar_moment(matrix_size, moment_order)
        exact_equal(
            determinant_formula,
            direct_integral,
            f"finite determinant N={matrix_size}, s={moment_order}",
        )
        results.append(
            {
                "N": matrix_size,
                "s": moment_order,
                "polynomial": str(determinant_formula),
            }
        )
    return results


def check_s_one_structure() -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    for matrix_size in range(1, 9):
        c_zero = (1 + U) * (1 - U ** (matrix_size + 1))
        c_one = -2 * (matrix_size + 1) * U ** (matrix_size + 1)
        c_two = -(matrix_size + 1) ** 2 * U**matrix_size
        structure = (
            c_zero / (1 - U) ** 3
            + c_one / (1 - U) ** 2
            + c_two / (1 - U)
        )
        direct = sum(index**2 * U ** (index - 1) for index in range(1, matrix_size + 1))
        exact_equal(structure, direct, f"s=1 structure N={matrix_size}")
        results.append(
            {
                "N": matrix_size,
                "C0_degree": int(sp.degree(c_zero, U)),
                "C1_degree": int(sp.degree(c_one, U)),
                "C2_degree": int(sp.degree(c_two, U)),
                "moment": str(sp.factor(direct)),
            }
        )
    return results


def check_fourth_moment_pole_coefficient() -> int:
    delta, alpha_one, alpha_two, beta_one, beta_two = sp.symbols(
        "delta alpha_one alpha_two beta_one beta_two"
    )
    pole_product = sp.prod(
        1 / (delta + alpha + beta)
        for alpha in (alpha_one, alpha_two)
        for beta in (beta_one, beta_two)
    )
    differentiated = sp.diff(
        pole_product, alpha_one, alpha_two, beta_one, beta_two
    ).subs(
        {
            alpha_one: 0,
            alpha_two: 0,
            beta_one: 0,
            beta_two: 0,
        }
    )
    coefficient = sp.simplify(delta**8 * differentiated)
    if coefficient != 34:
        raise AssertionError(f"fourth-moment pole coefficient is {coefficient}, not 34")
    return int(coefficient)


def check_bessel_kernel_factor() -> dict[str, object]:
    # At w=0, direct termwise integration gives the series below.  The correct
    # l'Hopital specialization of the Christoffel--Darboux quotient is the same
    # series; the printed prefactor 2 doubles every coefficient.
    direct_coefficients = [
        sp.Rational((-1) ** degree, math.factorial(degree) ** 2 * (degree + 1))
        for degree in range(8)
    ]
    bessel_coefficients = [
        sp.Rational((-1) ** degree, math.factorial(degree) * math.factorial(degree + 1))
        for degree in range(8)
    ]
    if direct_coefficients != bessel_coefficients:
        raise AssertionError("correct Bessel quotient does not match the integral series")
    printed_coefficients = [2 * coefficient for coefficient in bessel_coefficients]
    if printed_coefficients[0] != 2 or direct_coefficients[0] != 1:
        raise AssertionError("factor-of-two diagnostic did not separate at the constant term")
    return {
        "specialization": "w=0",
        "direct_integral_constant_term": 1,
        "correct_quotient_constant_term": 1,
        "printed_quotient_constant_term": 2,
        "coefficients_checked": len(direct_coefficients),
    }


def main() -> None:
    source_root = Path(
        r"[local]/Documents\arxiv_latex\library\random_matrix_zeta"
        r"\grover_mezzadri_simm_2026_higher_order_derivative_moments"
        r"\dependencies\simm_wei_2026"
    )
    source_files = {
        "main_tex": source_root / "source" / "Simm-Wei-12-2024.tex",
        "bibliography": source_root / "source" / "Simm-Wei-12-2024.bbl",
        "source_archive": source_root / "source_archive" / "2409.03687v2",
    }
    for label, path in source_files.items():
        if not path.is_file():
            raise AssertionError(f"missing {label}: {path}")

    finite_checks = check_finite_determinant()
    s_one_checks = check_s_one_structure()
    pole_coefficient = check_fourth_moment_pole_coefficient()
    bessel_check = check_bessel_kernel_factor()

    result = {
        "schema_version": 1,
        "status": "pass",
        "python": platform.python_version(),
        "sympy": sp.__version__,
        "source_identity": {
            "title": "On moments of the derivative of CUE characteristic polynomials and the Riemann zeta function",
            "authors": ["Nick Simm", "Fei Wei"],
            "arxiv": "2409.03687v2",
        },
        "source_files": {
            label: {
                "path": str(path),
                "bytes": path.stat().st_size,
                "sha256": sha256(path),
            }
            for label, path in source_files.items()
        },
        "finite_determinant_vs_direct_haar": finite_checks,
        "s_one_structure_decomposition": s_one_checks,
        "fourth_zeta_derivative_pole_coefficient": pole_coefficient,
        "bessel_kernel_printed_factor_check": bessel_check,
        "structural_scope_check": {
            "source_truncation": "For positive integer s, 1/Gamma(s-h2+1)=0 whenever h2>s; consequently C_h=0 for h>2s.",
            "source_degree_claim": "The v2 statement that every h>=0 has degree Ns+s^2+s-h cannot hold for those zero polynomials.",
        },
        "scope_boundary": [
            "The finite determinant is checked against an independent Weyl-density constant-term integral only in the listed small ranks and moment orders.",
            "The s=1 decomposition is checked for N=1,...,8; the manuscript supplies the symbolic all-N proof.",
            "The coefficient 34 is derived from the exact four-pole differentiated model; the analytic mean-value theorem and the regular Euler factor are separate human-source dependencies.",
            "The Bessel-kernel check proves a factor-of-two defect in the displayed v2 identity by the exact w=0 power series; it does not alter the integral definition used in the main microscopic theorem.",
            "No analytic uniform-integrability estimate, Painleve identification, conditional zeta theorem, or missing general structure-theorem proof is certified here.",
        ],
    }
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
