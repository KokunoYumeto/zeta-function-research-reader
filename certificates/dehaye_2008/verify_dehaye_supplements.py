#!/usr/bin/env python3
"""Exact audit of the computational supplements to Dehaye (2008).

This script does not re-prove the representation-theoretic derivation in the
paper.  It checks every coefficient in the three attached numerator data
files, the exact transformations among the three moment families, the
embedded TeX table prefixes, and the real-root counts stated for the Hardy
numerators.  All arithmetic before the optional numerical root locator is
exact over ZZ(u) or QQ(u).
"""

from __future__ import annotations

import hashlib
import json
import math
import platform
import re
from pathlib import Path

import sympy as sp


U = sp.Symbol("u")
YVAR = sp.Symbol("y")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def parse_magma_polynomial_list(path: Path) -> list[sp.Poly]:
    text = path.read_text(encoding="utf-8")
    lines = [line for line in text.splitlines() if not line.lstrip().startswith("//")]
    body = "\n".join(lines)
    start = body.find("[")
    end = body.rfind("]")
    if start < 0 or end <= start:
        raise AssertionError(f"{path.name}: missing outer list brackets")
    payload = body[start + 1 : end]
    entries = [entry.strip() for entry in payload.split(",") if entry.strip()]
    result: list[sp.Poly] = []
    for index, entry in enumerate(entries, start=1):
        expression = sp.sympify(entry.replace("^", "**"), locals={"u": U})
        try:
            polynomial = sp.Poly(expression, U, domain=sp.ZZ)
        except Exception as exc:  # pragma: no cover - fail-closed diagnostic
            raise AssertionError(f"{path.name} entry {index} is not in ZZ[u]") from exc
        result.append(polynomial)
    return result


def latex_polynomial_to_poly(text: str) -> sp.Poly:
    cleaned = re.sub(r"u\^\{(\d+)\}", r"u**\1", text)
    cleaned = cleaned.replace("$", "").replace("\\", "")
    cleaned = re.sub(r"\s+", "", cleaned)
    cleaned = re.sub(r"(?<=\d)u", "*u", cleaned)
    expression = sp.sympify(cleaned, locals={"u": U})
    return sp.Poly(expression, U, domain=sp.ZZ)


def parse_tex_table(path: Path) -> dict[int, sp.Poly]:
    text = path.read_text(encoding="utf-8")
    pattern = re.compile(
        r"(?ms)(\d+)\s*&\s*\$?\s*(.*?)\s*\$?(?:\\\\\\hline|\Z)"
    )
    result: dict[int, sp.Poly] = {}
    for match in pattern.finditer(text):
        result[int(match.group(1))] = latex_polynomial_to_poly(match.group(2))
    if not result:
        raise AssertionError(f"{path.name}: no TeX table rows parsed")
    return result


def alpha(a: int, r: int) -> int:
    discriminant_floor = math.isqrt(a * a + 4 * r)
    return (discriminant_floor - a) // 2


def denominator_y(r: int) -> sp.Poly:
    expression = sp.Integer(1)
    for a in range(1, r):
        if a % 2:
            expression *= (U * U - a * a) ** alpha(a, r)
    return sp.Poly(sp.expand(expression), U, domain=sp.ZZ)


def exact_equal(left: sp.Expr, right: sp.Expr, name: str) -> None:
    difference = sp.cancel(left - right)
    if difference != 0:
        raise AssertionError(f"{name}: nonzero exact difference {sp.factor(difference)}")


def validate_polynomial_family(
    name: str, polynomials: list[sp.Poly], expected_count: int
) -> dict[str, object]:
    if len(polynomials) != expected_count:
        raise AssertionError(f"{name}: expected {expected_count} entries, got {len(polynomials)}")
    degrees: list[int] = []
    coefficient_counts: list[int] = []
    for index, polynomial in enumerate(polynomials, start=1):
        if polynomial.LC() != 1:
            raise AssertionError(f"{name} entry {index}: not monic")
        if any(monomial[0] % 2 for monomial, _ in polynomial.terms()):
            raise AssertionError(f"{name} entry {index}: odd power of u occurs")
        degrees.append(polynomial.degree())
        coefficient_counts.append(len(polynomial.terms()))
    return {
        "entries": len(polynomials),
        "all_monic": True,
        "all_even": True,
        "degrees": degrees,
        "coefficient_counts": coefficient_counts,
    }


def real_root_count_of_even_polynomial(polynomial: sp.Poly) -> int:
    coefficients: dict[tuple[int], sp.Integer] = {}
    for (exponent,), coefficient in polynomial.terms():
        coefficients[(exponent // 2,)] = coefficient
    reduced = sp.Poly.from_dict(coefficients, YVAR, domain=sp.ZZ)
    positive_roots = int(reduced.count_roots(0, sp.oo))
    zero_roots = min(exponent[0] for exponent, _ in reduced.terms())
    return 2 * positive_roots + zero_roots


def main() -> None:
    source_root = Path(
        r"[local]/Documents\arxiv_latex\library\random_matrix_zeta"
        r"\dehaye_2008_joint_derivative_moments\source"
    )
    files = {
        name: source_root / name
        for name in (
            "ComplexM",
            "NormedM",
            "NormedV",
            "NumeratorsComplexM",
            "NumeratorsNormedM",
            "NumeratorsNormedV",
            "MagmaCode",
            "joint_moments.bbl",
            "rootsUpTo30.pdf",
            "conrey_ghosh.pdf",
        )
    }
    for name, path in files.items():
        if not path.is_file():
            raise AssertionError(f"missing supplement: {name}")

    complex_numerators = parse_magma_polynomial_list(files["NumeratorsComplexM"])
    norm_m_numerators = parse_magma_polynomial_list(files["NumeratorsNormedM"])
    norm_v_numerators = parse_magma_polynomial_list(files["NumeratorsNormedV"])

    family_checks = {
        "X_r": validate_polynomial_family("X_r", complex_numerators, 60),
        "hat_X_2h": validate_polynomial_family("hat_X_2h", norm_m_numerators, 30),
        "tilde_X_2h": validate_polynomial_family("tilde_X_2h", norm_v_numerators, 30),
    }

    table_complex = parse_tex_table(files["ComplexM"])
    table_norm_m = parse_tex_table(files["NormedM"])
    table_norm_v = parse_tex_table(files["NormedV"])
    for r, polynomial in table_complex.items():
        if polynomial != complex_numerators[r - 1]:
            raise AssertionError(f"ComplexM table mismatch at r={r}")
    for r, polynomial in table_norm_m.items():
        if r % 2 or polynomial != norm_m_numerators[r // 2 - 1]:
            raise AssertionError(f"NormedM table mismatch at r={r}")
    for r, polynomial in table_norm_v.items():
        if r % 2 or polynomial != norm_v_numerators[r // 2 - 1]:
            raise AssertionError(f"NormedV table mismatch at r={r}")

    y_polynomials = {r: denominator_y(r) for r in range(0, 61)}
    norm_m_numerator: dict[int, sp.Poly] = {
        0: sp.Poly(1, U, domain=sp.QQ)
    }
    transformed_checks = 0
    for h in range(1, 31):
        r = 2 * h
        reconstructed_hat = sp.Poly(0, U, domain=sp.QQ)
        for j in range(h + 1):
            source_r = r - j
            denominator_quotient = y_polynomials[r].exquo(y_polynomials[source_r])
            term = (
                (-1) ** (h + j)
                * math.comb(h, j)
                * 2**j
                * complex_numerators[source_r - 1]
                * denominator_quotient
            )
            reconstructed_hat += term.set_domain(sp.QQ)
        if reconstructed_hat != norm_m_numerators[h - 1].set_domain(sp.QQ):
            raise AssertionError(f"hat_X_{r} exact polynomial transformation failed")
        norm_m_numerator[r] = reconstructed_hat
        transformed_checks += 1

        tilde_sum = sp.Poly(0, U, domain=sp.QQ)
        for j in range(h + 1):
            denominator_quotient = y_polynomials[r].exquo(y_polynomials[2 * j])
            term = (
                (-1) ** (h + j)
                * math.comb(h, j)
                * norm_m_numerator[2 * j]
                * denominator_quotient
            )
            tilde_sum += term.set_domain(sp.QQ)
        reconstructed_tilde = tilde_sum.mul_ground(
            sp.Rational(2**h * math.factorial(h), math.factorial(r))
        )
        if reconstructed_tilde != norm_v_numerators[h - 1].set_domain(sp.QQ):
            raise AssertionError(f"tilde_X_{r} exact polynomial transformation failed")
        transformed_checks += 1

    expected_real_counts = [
        0, 0, 2, 2, 4, 6, 8, 8, 12, 14,
        16, 18, 20, 22, 28, 28, 30, 34, 36, 38,
        40, 46, 44, 46, 54, 52, 58, 60, 62, 68,
    ]
    exact_real_counts = [
        real_root_count_of_even_polynomial(polynomial)
        for polynomial in norm_v_numerators
    ]
    if exact_real_counts != expected_real_counts:
        raise AssertionError(
            f"Hardy numerator real-root counts differ: {exact_real_counts}"
        )

    bbl_text = files["joint_moments.bbl"].read_text(encoding="utf-8")
    bibliography_entries = len(re.findall(r"\\bibitem", bbl_text))
    if bibliography_entries != 30:
        raise AssertionError(f"expected 30 bibliography entries, got {bibliography_entries}")

    result = {
        "schema_version": 1,
        "status": "pass",
        "python": platform.python_version(),
        "sympy": sp.__version__,
        "source_root": str(source_root),
        "files": {
            name: {"bytes": path.stat().st_size, "sha256": sha256(path)}
            for name, path in files.items()
        },
        "family_checks": family_checks,
        "embedded_table_rows": {
            "ComplexM": sorted(table_complex),
            "NormedM": sorted(table_norm_m),
            "NormedV": sorted(table_norm_v),
        },
        "exact_moment_family_transformations": transformed_checks,
        "denominators_checked": 60,
        "hardy_real_root_counts_exact": exact_real_counts,
        "first_h_with_nonreal_roots": 21,
        "nonreal_root_count_at_h_21": 4,
        "bibliography_entries": bibliography_entries,
        "scope_boundary": [
            "Every coefficient and all exact family transformations in the three numerator data files are checked.",
            "Real-root counts use exact polynomial root isolation after the substitution y=u^2.",
            "This certificate does not re-prove Dehaye's representation-theoretic derivation or the conjectural zeta/Hardy transfer.",
            "The two PDF figures are hash-bound here but require separate visual inspection.",
        ],
    }
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
