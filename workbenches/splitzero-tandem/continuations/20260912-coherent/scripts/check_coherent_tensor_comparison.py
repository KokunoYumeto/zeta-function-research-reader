"""Exact finite checks of the reflected comparison family, not zeta inputs.

Reproduce the 40 checks in work/pr14_tensor_trace_review.md, equation (17).
All validation uses explicit Boolean records and process exit status.
Python optimization therefore cannot remove the checks.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys

import sympy as s


ROOT = Path(__file__).resolve().parents[1]


def comparison_case(n: int, negative_control: bool) -> list[dict]:
    """Retain the original rational coordinates of the comparison family."""
    delta = s.Rational(1, 5)
    a = s.Rational(1, 2 * n)
    ones = s.ones(n)
    upper = s.Matrix(n, n, lambda i, j: 1 if i < j else 0)
    A_plus = (s.Rational(1, 2) + delta) * s.eye(n) + 2 * delta * upper
    A_minus = s.eye(n) - A_plus
    A = s.diag(A_plus, A_minus)
    G = s.eye(2 * n)
    Y = a * s.ones(1, 2 * n)
    C = s.Matrix([[-delta / a if j < n else delta / a for j in range(2 * n)]])
    if negative_control and n == 1:
        # This changes exactly the first factorization test, leaving W fixed.
        C[0, 0] += 1
    W = A.adjoint() * G + G * A - G
    K = s.BlockMatrix([[s.zeros(n), s.eye(n)], [s.eye(n), s.zeros(n)]]).as_explicit()
    variable = s.Symbol("lambda")
    expected_charpoly = ((variable - s.Rational(1, 2) - delta) ** n
                         * (variable - s.Rational(1, 2) + delta) ** n)

    conditions = [
        ("factorization", W == -(Y.adjoint() * C + C.adjoint() * Y)),
        ("exact_block_form", W == s.diag(2 * delta * ones, -2 * delta * ones)),
        ("layer_map_rank_one", Y.rank() == 1),
        ("control_rank_two", W.rank() == 2),
        ("reflection_action", A * K == K * (G - s.conjugate(A))),
        ("reflection_control_sign", K.adjoint() * W * K == -s.conjugate(W)),
        # Y*Y is positive of rank one; positive determinant of I-Y*Y
        # therefore certifies its one changed eigenvalue is positive.
        ("next_gram_positive_rank_one_test", (G - Y.adjoint() * Y).det() > 0),
        ("control_trace_zero", W.trace() == 0),
        ("control_square_trace", (W * W).trace() == 8 * delta ** 2 * n ** 2),
        ("full_characteristic_polynomial",
         s.expand(A.charpoly(variable).as_expr() - expected_charpoly) == 0),
    ]
    return [{"name": f"n={n}:{name}", "passed": bool(value)}
            for name, value in conditions]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=ROOT / "checks" / "coherent_tensor_comparison.json")
    parser.add_argument("--negative-control", action="store_true",
                        help="Deliberately break the first factorization; expected exit status 1.")
    args = parser.parse_args()
    rows = [record for n in (1, 2, 3, 4)
            for record in comparison_case(n, args.negative_control)]
    if len(rows) != 40:
        raise RuntimeError(f"Expected 40 finite validations, obtained {len(rows)}")
    failed = [row["name"] for row in rows if not row["passed"]]
    result = {
        "all_passed": not failed,
        "passed": sum(row["passed"] for row in rows),
        "total": len(rows),
        "failed": failed,
        "negative_control": args.negative_control,
        "python_optimization": sys.flags.optimize,
        "scope": ("Exact rational comparison family with same-metric reflection, "
                  "rank-one layer map and full characteristic multiplicities. "
                  "The chosen eigenvalues are not arithmetic-zeta inputs; these "
                  "40 records do not certify analytic estimates or an RH conclusion."),
        "parameters": {"n": [1, 2, 3, 4], "delta": "1/5", "a": "1/(2*n)"},
        "sympy_version": s.__version__,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "checks": rows,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key != "checks"}))
    return 0 if result["all_passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
