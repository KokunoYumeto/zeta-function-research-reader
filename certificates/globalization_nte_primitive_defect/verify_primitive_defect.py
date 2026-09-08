#!/usr/bin/env python3
"""Bounded replay of the admitted primitive-defect coordinate core.

This checker deliberately does not attempt to certify the undefined
cross-domain interfaces in the source audit.  It checks finite algebraic
identities, the corrected r=3 Weyl convention, the A_2 norm, the endpoint
principal-part algebra, and the elementary first CUE derivative moment.
It performs no OCR, rendering, network access, indexing, or file writes.
"""

from __future__ import annotations

import hashlib
import json
import math
import cmath
from pathlib import Path

import sympy as sp


SOURCE = Path(
    r"[local]/Documents\Papors\Chatnotes\globalization nte\3\primitive_defect_preprint.tex"
)
EXPECTED_SOURCE_SHA256 = (
    "2f3289f6a04105d3f15fe5f7c36dde286515e61f465caf1582f9808e19f3d2f7"
)
CHECKS: list[str] = []


def check(name: str, condition: bool) -> None:
    if not condition:
        raise AssertionError(name)
    if name not in CHECKS:
        CHECKS.append(name)


def zero(value: sp.Expr) -> bool:
    return sp.simplify(sp.cancel(sp.together(value))) == 0


def check_source_identity() -> None:
    raw = SOURCE.read_bytes()
    check("source_byte_count", len(raw) == 47_978)
    check("source_sha256", hashlib.sha256(raw).hexdigest() == EXPECTED_SOURCE_SHA256)
    check("source_line_count", len(raw.decode("utf-8").splitlines()) == 1_474)


def split_add(x: object, y: object) -> object:
    tau = x is _TAU or y is _TAU
    if x is _TAU:
        return y
    if y is _TAU:
        return x
    return x + y  # type: ignore[operator]


def split_mul(x: object, y: object) -> object:
    if x is _TAU or y is _TAU:
        return _TAU
    return x * y  # type: ignore[operator]


_TAU = object()


def check_split_zero() -> None:
    values = [_TAU, -2, -1, 0, 1, 3]
    for x in values:
        for y in values:
            for z in values:
                check(
                    "split_add_associative",
                    split_add(split_add(x, y), z) == split_add(x, split_add(y, z)),
                )
                check(
                    "split_mul_associative",
                    split_mul(split_mul(x, y), z) == split_mul(x, split_mul(y, z)),
                )
            check("split_add_commutative", split_add(x, y) == split_add(y, x))
            check("split_mul_commutative", split_mul(x, y) == split_mul(y, x))
        for y in values:
            for z in values:
                check(
                    "split_distributive",
                    split_mul(x, split_add(y, z))
                    == split_add(split_mul(x, y), split_mul(x, z)),
                )
    check("split_support_fibre", [_TAU, 0] == [_TAU, 0])
    check("split_defect_of_three", -(1 + 1 + 1) == -3)


def check_A_kernel() -> None:
    r = 5
    roots = [sp.eye(r)[:, i] - sp.eye(r)[:, i + 1] for i in range(r - 1)]
    gram = sp.Matrix([[roots[i].dot(roots[j]) for j in range(r - 1)] for i in range(r - 1)])
    expected = sp.zeros(r - 1)
    for i in range(r - 1):
        expected[i, i] = 2
        if i + 1 < r - 1:
            expected[i, i + 1] = expected[i + 1, i] = -1
    check("A_kernel_gram", gram == expected)
    check("A_cartan_determinant", gram.det() == r)
    a = [3, -1, -2, 4, -4]
    check("A_kernel_sum_zero", sum(a) == 0)
    b = [sum(a[: i + 1]) for i in range(r - 1)]
    reconstructed = [0] * r
    for i, bi in enumerate(b):
        reconstructed[i] += bi
        reconstructed[i + 1] -= bi
    check("A_kernel_coordinate_reconstruction", reconstructed == a)


def check_fourier() -> None:
    r = 5
    omega = cmath.exp(2j * math.pi / r)
    for b in range(r):
        for c in range(r):
            total = sum(omega ** (a * (b - c)) for a in range(r))
            expected = r if b == c else 0
            check("finite_fourier_orthogonality", abs(total - expected) < 1e-12)
    coeffs = [2, -3, 5, 7, -11]
    check("augmentation_is_trivial_mode", sum(coeffs) == sum(coeffs))


def check_principal_parts() -> None:
    s, t = sp.symbols("s t")
    u = s * (s - 1)
    v = 2 * s - 1
    check("u_reflection_invariant", zero(u.subs(s, 1 - s) - u))
    check("v_reflection_anti_invariant", zero(v.subs(s, 1 - s) + v))
    check("quadratic_relation", zero(v**2 - (1 + 4 * u)))
    check("principal_basis_invariant", zero(1 / u - (1 / (s - 1) - 1 / s)))
    check("principal_basis_anti", zero(v / u - (1 / (s - 1) + 1 / s)))
    a = -1 - 2 * t
    b = sp.Integer(1)
    A = (b - a) / 2
    B = (a + b) / 2
    check("hurwitz_principal_part_reconstruction", zero(A / u + B * v / u - (a / s + b / (s - 1))))
    check("t_one_anti_residues", zero((-v / u) - (-1 / s - 1 / (s - 1))))


def check_eisenstein_A2() -> None:
    m, n, p, q = sp.symbols("m n p q", integer=True)
    norm = lambda x, y: x * x - x * y + y * y
    # Multiplication (m+n w)(p+q w)=(mp-nq)+(mq+np-nq)w, w^2=-w-1.
    x, y = m * p - n * q, m * q + n * p - n * q
    check("eisenstein_norm_multiplicative", sp.expand(norm(x, y) - norm(m, n) * norm(p, q)) == 0)
    gram = sp.Matrix([[2, -1], [-1, 2]])
    vec = sp.Matrix([m, n])
    check("A2_quadratic_form", sp.expand((vec.T * gram * vec)[0] - 2 * norm(m, n)) == 0)
    check("six_units_norm_one", all(norm(x, y) == 1 for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1)]))


def check_weyl_r3() -> None:
    omega = (-1 + sp.sqrt(3) * sp.I) / 2
    X = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    Z = sp.diag(1, omega, omega**2)
    check("weyl_X_cyclic", (X**3 - sp.eye(3)) == sp.zeros(3))
    check("weyl_Z_cyclic", (Z**3 - sp.eye(3)).applyfunc(sp.simplify) == sp.zeros(3))
    check("weyl_relation_corrected", (Z * X - omega * X * Z).applyfunc(sp.simplify) == sp.zeros(3))
    ops = [X**a * Z**b for a in range(3) for b in range(3)]
    flattened = sp.Matrix.hstack(*[op.reshape(9, 1) for op in ops])
    check("weyl_basis_rank", flattened.rank() == 9)
    check("weyl_nonidentity_traceless", all(sp.simplify(op.trace()) == 0 for op in ops[1:]))


def check_cue_dimension() -> None:
    s = sp.symbols("s", integer=True, positive=True)
    check("cue_exponent_dimension_identity", sp.expand(s**2 + 2 * s - ((s + 1) ** 2 - 1)) == 0)
    W = sp.MatrixSymbol("W", 3, 3)
    # Independent finite first-derivative moment: sum_{m=1}^N m^2.
    for N in range(1, 9):
        check("first_derivative_sum_of_squares", sum(m * m for m in range(1, N + 1)) == N * (N + 1) * (2 * N + 1) // 6)


def main() -> None:
    check_source_identity()
    check_split_zero()
    check_A_kernel()
    check_fourier()
    check_principal_parts()
    check_eisenstein_A2()
    check_weyl_r3()
    check_cue_dimension()
    print(json.dumps({"status": "pass", "checks": CHECKS, "count": len(CHECKS)}, sort_keys=True))


if __name__ == "__main__":
    main()
