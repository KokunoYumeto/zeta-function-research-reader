"""Reproduce the 366 exact Split-Zero carrier/sector assertions.

Run from any directory:
    python scripts/check_split_zero_carriers.py

Requires SymPy. No floating-point arithmetic is used. The general proofs
are in tex/split_zero_carriers.tex; finite checks are supporting evidence.
The script always writes its JSON receipt in checks/ beside the package.
"""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from itertools import product
from pathlib import Path

import sympy as S


def run_checks() -> dict:
    q = 3
    masks = list(product([0, 1], repeat=2))
    scalar = [(0, mask) for mask in masks] + [
        (a, (1, 1)) for a in range(1, q)
    ]
    vector = [((0, 0), mask) for mask in masks] + [
        (a, (1, 1))
        for a in product(range(q), repeat=2)
        if a != (0, 0)
    ]

    def lattice_add(x, y):
        a, mask = x
        b, other = y
        amplitude = (
            (a + b) % q
            if isinstance(a, int)
            else tuple((u + v) % q for u, v in zip(a, b))
        )
        return amplitude, tuple(max(u, v) for u, v in zip(mask, other))

    def lattice_multiply(x, y):
        a, mask = x
        b, other = y
        amplitude = (
            (a * b) % q
            if isinstance(a, int)
            else tuple((u * v) % q for u, v in zip(a, b))
        )
        return amplitude, tuple(min(u, v) for u, v in zip(mask, other))

    def scalar_embedding(x):
        amplitude, mask = x
        return tuple((amplitude, support) for support in mask)

    def vector_embedding(x):
        amplitude, mask = x
        return tuple(zip(amplitude, mask))

    def mixed_add(x, y):
        return tuple(
            ((a + c) % q, max(s, t))
            for (a, s), (c, t) in zip(x, y)
        )

    def mixed_multiply(x, y):
        return tuple(
            ((a * c) % q, min(s, t))
            for (a, s), (c, t) in zip(x, y)
        )

    checks = 0
    scopes = []
    for name, domain, embedding in [
        ("scalar_lattice_diagonal_embedding", scalar, scalar_embedding),
        ("vector_lattice_embedding", vector, vector_embedding),
    ]:
        start = checks
        assert len({embedding(x) for x in domain}) == len(domain)
        checks += 1
        for x, y in product(domain, repeat=2):
            assert embedding(lattice_add(x, y)) == mixed_add(
                embedding(x), embedding(y)
            )
            checks += 1
            assert embedding(lattice_multiply(x, y)) == mixed_multiply(
                embedding(x), embedding(y)
            )
            checks += 1
        scopes.append(
            {
                "name": name,
                "domain_size": len(domain),
                "assertions": checks - start,
                "scope": "Injectivity and exhaustive preservation of addition and multiplication.",
            }
        )

    beta, gamma = S.symbols("beta gamma", real=True)
    spectral_parameter = beta + S.I * gamma
    coordinates = [
        S.expand(
            spectral_parameter
            + epsilon * (1 - spectral_parameter)
            + delta * S.conjugate(spectral_parameter)
            + epsilon * delta * (1 - S.conjugate(spectral_parameter))
        )
        for epsilon, delta in [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    ]
    assert coordinates == [2, 0, 4 * beta - 2, 4 * S.I * gamma]
    checks += 1
    assert (
        S.expand(
            S.Rational(1, 2)
            + (coordinates[2] + coordinates[3]) / 4
            - spectral_parameter
        )
        == 0
    )
    checks += 1
    scopes.append(
        {
            "name": "quartet_coordinates_and_affine_inverse",
            "assertions": 2,
            "scope": "Exact symbolic identities over real beta and gamma.",
        }
    )

    def vandermonde_column(z):
        return S.Matrix([1, z, z * z])

    first = vandermonde_column(S.Rational(1, 2))
    second = vandermonde_column(S.Integer(2))
    moment = 4 * first * first.T + second * second.T
    assert moment[:2, :2] == S.Matrix([[5, 4], [4, 5]])
    checks += 1
    defect = moment[2, 2] - 2 * moment[1, 1] + moment[0, 0]
    assert defect == S.Rational(45, 4)
    checks += 1
    scopes.append(
        {
            "name": "two_by_two_packet_counterexample_and_size_three_defect",
            "assertions": 2,
            "weights": ["4", "1"],
            "atoms": ["1/2", "2"],
            "scope": "Exact rational moment matrix and diagonal defect.",
        }
    )

    return {
        "all_passed": True,
        "exact_assertions": checks,
        "finite_field": q,
        "scalar_carrier_size": len(scalar),
        "vector_carrier_size": len(vector),
        "two_by_two_counterexample": str(moment[:2, :2]),
        "three_by_three_defect": str(defect),
        "scopes": scopes,
        "sympy_version": S.__version__,
        "limitations": (
            "Finite-field checks and symbolic identities supplement the general proofs. "
            "They do not establish an arithmetic theta-packet zero-defect conclusion or RH."
        ),
    }


def main() -> None:
    # Python -O disables assert, so fail closed under optimized execution.
    if not __debug__:
        raise RuntimeError("Run without -O: exact assertions must remain enabled.")
    receipt = run_checks()
    script = Path(__file__).resolve()
    receipt["script_sha256"] = hashlib.sha256(script.read_bytes()).hexdigest()
    receipt["completed_utc"] = datetime.now(timezone.utc).isoformat()
    target = script.parent.parent / "checks" / "split_zero_carriers_exact.json"
    target.parent.mkdir(parents=True, exist_ok=True)
    rendered = json.dumps(receipt, indent=2, ensure_ascii=False) + "\n"
    target.write_text(rendered, encoding="utf-8")
    print(rendered, end="")


if __name__ == "__main__":
    main()
