#!/usr/bin/env python3
"""Replay and independently verify the exact U(3) derivative moments.

This certificate checks the five integer values displayed in
``split_zero_cue_hurwitz_phase_space_revised.tex`` at lines 1462--1491 and
computed by its embedded program at lines 1985--2044.  It deliberately uses
two exact implementations:

1. the source's sparse Laurent-polynomial multiplication; and
2. an independent SymPy expansion followed by monomial coefficient
   extraction after an explicit Laurent-to-polynomial shift.

No floating-point arithmetic, sampling, OCR, or external network access is
used.
"""

from __future__ import annotations

from collections import defaultdict
import hashlib
import itertools
import json
import math
from pathlib import Path
import platform
import sys
import time
import tracemalloc

import sympy


SOURCE_PATH = Path(
    r"[local]/Documents\Papors\Chatnotes\globalization cue"
    r"\split_zero_cue_hurwitz_phase_space_revised.tex"
)
EXPECTED_SOURCE_SHA256 = (
    "95cca3275f2012e32f9e506ec0211273d5e7da1fd72ad90f7167aa37094e94cc"
)
EXPECTED_MOMENTS = [14, 375, 15510, 847280, 55331424]


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def sparse_mul(
    left: dict[tuple[int, ...], int],
    right: dict[tuple[int, ...], int],
    variable_count: int,
) -> dict[tuple[int, ...], int]:
    result: defaultdict[tuple[int, ...], int] = defaultdict(int)
    for left_exponents, left_coefficient in left.items():
        for right_exponents, right_coefficient in right.items():
            exponents = tuple(
                left_exponents[index] + right_exponents[index]
                for index in range(variable_count)
            )
            result[exponents] += left_coefficient * right_coefficient
    return {exponents: coefficient for exponents, coefficient in result.items() if coefficient}


def sparse_power(
    polynomial: dict[tuple[int, ...], int],
    exponent: int,
    variable_count: int,
) -> dict[tuple[int, ...], int]:
    result = {tuple([0] * variable_count): 1}
    base = polynomial
    remaining = exponent
    while remaining:
        if remaining & 1:
            result = sparse_mul(result, base, variable_count)
        remaining >>= 1
        if remaining:
            base = sparse_mul(base, base, variable_count)
    return result


def invert_monomials(
    polynomial: dict[tuple[int, ...], int],
) -> dict[tuple[int, ...], int]:
    return {
        tuple(-exponent for exponent in exponents): coefficient
        for exponents, coefficient in polynomial.items()
    }


def source_sparse_moment(variable_count: int, moment_order: int) -> int:
    """Implement the embedded source algorithm with exact integers."""

    derivative: defaultdict[tuple[int, ...], int] = defaultdict(int)
    derivative[tuple([0] * variable_count)] = variable_count
    for degree in range(1, variable_count):
        coefficient = (variable_count - degree) * ((-1) ** degree)
        for subset in itertools.combinations(range(variable_count), degree):
            exponents = [0] * variable_count
            for index in subset:
                exponents[index] = 1
            derivative[tuple(exponents)] += coefficient

    vandermonde_squared = {tuple([0] * variable_count): 1}
    for left, right in itertools.combinations(range(variable_count), 2):
        factor: defaultdict[tuple[int, ...], int] = defaultdict(int)
        factor[tuple([0] * variable_count)] += 2
        forward = [0] * variable_count
        forward[left] += 1
        forward[right] -= 1
        factor[tuple(forward)] -= 1
        backward = [0] * variable_count
        backward[right] += 1
        backward[left] -= 1
        factor[tuple(backward)] -= 1
        vandermonde_squared = sparse_mul(
            vandermonde_squared, dict(factor), variable_count
        )

    powered = sparse_power(dict(derivative), moment_order, variable_count)
    absolute_power = sparse_mul(
        powered, invert_monomials(powered), variable_count
    )
    integrand = sparse_mul(absolute_power, vandermonde_squared, variable_count)
    constant_term = integrand.get(tuple([0] * variable_count), 0)
    denominator = math.factorial(variable_count)
    quotient, remainder = divmod(constant_term, denominator)
    if remainder:
        raise ArithmeticError(
            f"constant term {constant_term} is not divisible by {denominator}"
        )
    return quotient


def sympy_constant_term_moment(variable_count: int, moment_order: int) -> int:
    """Independently expand the Laurent polynomial with SymPy exactly."""

    variables = sympy.symbols(f"z0:{variable_count}")
    derivative = sympy.Integer(variable_count)
    for degree in range(1, variable_count):
        elementary = sum(
            math.prod(variables[index] for index in subset)
            for subset in itertools.combinations(range(variable_count), degree)
        )
        derivative += (variable_count - degree) * ((-1) ** degree) * elementary

    inverse_derivative = derivative.xreplace(
        {variable: sympy.Pow(variable, -1) for variable in variables}
    )
    vandermonde_squared = math.prod(
        (1 - variables[left] / variables[right])
        * (1 - variables[right] / variables[left])
        for left, right in itertools.combinations(range(variable_count), 2)
    )

    # Each variable has exponent at least -(moment_order + variable_count - 1).
    # Multiplying by the displayed monomial therefore gives an ordinary
    # polynomial without changing which coefficient represents the Laurent
    # constant term.
    shift = moment_order + variable_count - 1
    shift_monomial = math.prod(variable**shift for variable in variables)
    shifted = sympy.Poly(
        sympy.expand(
            derivative**moment_order
            * inverse_derivative**moment_order
            * vandermonde_squared
            * shift_monomial
        ),
        *variables,
        domain=sympy.ZZ,
    )
    target_monomial = math.prod(variable**shift for variable in variables)
    constant_term = int(shifted.coeff_monomial(target_monomial))
    denominator = math.factorial(variable_count)
    quotient, remainder = divmod(constant_term, denominator)
    if remainder:
        raise ArithmeticError(
            f"independent constant term {constant_term} is not divisible by {denominator}"
        )
    return quotient


def main() -> int:
    source_sha256 = sha256_file(SOURCE_PATH)
    if source_sha256 != EXPECTED_SOURCE_SHA256:
        raise RuntimeError(
            "source hash mismatch: "
            f"expected {EXPECTED_SOURCE_SHA256}, observed {source_sha256}"
        )

    tracemalloc.start()
    started = time.perf_counter()
    sparse_values = [source_sparse_moment(3, order) for order in range(1, 6)]
    sympy_values = [
        sympy_constant_term_moment(3, order) for order in range(1, 6)
    ]
    elapsed_seconds = time.perf_counter() - started
    _, peak_python_allocation_bytes = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    first_moment_closed_form = 3 * 4 * 7 // 6
    checks = {
        "source_hash_matches": source_sha256 == EXPECTED_SOURCE_SHA256,
        "sparse_values_match_display": sparse_values == EXPECTED_MOMENTS,
        "independent_values_match_display": sympy_values == EXPECTED_MOMENTS,
        "implementations_agree": sparse_values == sympy_values,
        "first_moment_matches_sum_of_squares": sparse_values[0]
        == first_moment_closed_form,
    }
    if not all(checks.values()):
        raise AssertionError(json.dumps(checks, sort_keys=True))

    receipt = {
        "schema_version": 1,
        "certificate_id": "CERT-N3-CUE-20260825-0001",
        "status": "exact_replay_passed_two_independent_implementations",
        "source": {
            "path": str(SOURCE_PATH),
            "sha256": source_sha256,
            "proposition_lines": "1462-1491",
            "embedded_program_lines": "1985-2044",
        },
        "mathematical_object": {
            "ensemble": "Haar U(3)",
            "polynomial": "Phi_3(z)=det(zI-U)",
            "derivative_coordinate": "Phi_3'(1)=3-2e_1+e_2",
            "orders": [1, 2, 3, 4, 5],
            "moments": sparse_values,
        },
        "methods": [
            {
                "id": "sparse_exact_laurent",
                "description": "source algorithm replay using integer exponent dictionaries",
                "values": sparse_values,
            },
            {
                "id": "sympy_shifted_exact_polynomial",
                "description": "independent exact expansion after an explicit Laurent monomial shift",
                "values": sympy_values,
            },
        ],
        "checks": checks,
        "environment": {
            "python": sys.version,
            "platform": platform.platform(),
            "sympy": sympy.__version__,
            "certificate_script_sha256": sha256_file(Path(__file__).resolve()),
            "elapsed_seconds": elapsed_seconds,
            "peak_python_allocation_bytes": peak_python_allocation_bytes,
            "memory_cap_bytes": 4 * 1024**3,
            "peak_python_allocation_below_cap": peak_python_allocation_bytes
            < 4 * 1024**3,
        },
        "nonclaims": [
            "This verifies only the five exact finite U(3) moment values and their displayed constant-term computation.",
            "It does not verify the later quadratic trace algebra, any quotient/lift comparison, or any zeta-zero implication.",
            "The source theorem giving the Haar-Weyl constant-term identity remains a human-authored mathematical input to be cited separately.",
        ],
    }
    print(json.dumps(receipt, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
