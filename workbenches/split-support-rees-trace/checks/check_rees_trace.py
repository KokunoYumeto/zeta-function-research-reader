#!/usr/bin/env python3
"""Finite exact checks for the split-support Rees/trace continuation.

Run: python check_rees_trace.py [--output results.json]
Dependency: sympy. No network, numerical zeta zeros, or floating-point tests.
Failures use explicit exceptions, so python -O does not disable checks.
The general statements are proved in RESEARCH_NOTE.md, not by these cases.
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
import platform
from collections import Counter
from fractions import Fraction
from pathlib import Path
from typing import Iterator

import sympy as sp

T, z, u, s, eps = sp.symbols('T z u s eps')
COUNTS: Counter[str] = Counter()


def require(name: str, condition: bool) -> None:
    if not condition:
        raise ArithmeticError(f'Check failed: {name}')
    COUNTS[name.split('/')[0]] += 1


def equal(name: str, left: sp.Expr, right: sp.Expr) -> None:
    require(name, sp.cancel(sp.expand(left - right)) == 0)


def matrix_equal(name: str, left: sp.Matrix, right: sp.Matrix) -> None:
    require(name + '/shape', left.shape == right.shape)
    for i in range(left.rows):
        for j in range(left.cols):
            equal(name + f'/entry{i}_{j}', left[i, j], right[i, j])


def compositions(n: int, r: int) -> Iterator[tuple[int, ...]]:
    if n < 0 or r < 1:
        raise ValueError('Expected n >= 0 and r >= 1')
    if r == 1:
        yield (n,)
        return
    for j in range(n + 1):
        for rest in compositions(n - j, r - 1):
            yield (j,) + rest


# None is external absence; Fraction(0) is supported scalar zero.
Scalar = Fraction | None


def plus(a: Scalar, b: Scalar) -> Scalar:
    if a is None:
        return b
    if b is None:
        return a
    return a + b


def times(a: Scalar, b: Scalar) -> Scalar:
    return None if a is None or b is None else a * b


def amp(a: Scalar) -> Fraction:
    return Fraction(0) if a is None else a


def mixed_product(a: tuple[Scalar, Scalar], b: tuple[Scalar, Scalar]) -> tuple[Scalar, Scalar]:
    return (
        plus(times(a[0], b[0]), times(Fraction(-1), times(a[1], b[1]))),
        plus(times(a[0], b[1]), times(a[1], b[0])),
    )


def test_support() -> None:
    values = [None, Fraction(-1), Fraction(0), Fraction(1), Fraction(2)]
    E = (Fraction(1), Fraction(0))
    states = list(itertools.product(values, repeat=2))
    for x in states:
        Ex = mixed_product(E, x)
        require('support/idempotent', mixed_product(E, Ex) == Ex)
        require('support/amplitude', tuple(map(amp, Ex)) == tuple(map(amp, x)))
        expected = (None, None) if x == (None, None) else tuple(map(amp, x))
        require('support/synchronization', Ex == expected)
    nulls = [x for x in states if tuple(map(amp, x)) == (0, 0)]
    require('support/four-null-faces', len(nulls) == 4)
    for x, y in itertools.product(states, repeat=2):
        out = mixed_product(x, y)
        a, b, c, d = map(amp, x + y)
        require('support/product-amplitude', tuple(map(amp, out)) == (a*c-b*d, a*d+b*c))
        px, qx = (v is not None for v in x)
        py, qy = (v is not None for v in y)
        expected_mask = ((px and py) or (qx and qy), (px and qy) or (qx and py))
        require('support/product-mask', tuple(v is not None for v in out) == expected_mask)
    for level in [-2, -1, 0, 1, 2, 3]:
        # Concrete descending filtration with coordinate weights 2 and 0.
        def belongs(x: tuple[Scalar, Scalar]) -> bool:
            return all(v == 0 or weight >= level for v, weight in zip(map(amp, x), (2, 0)))
        lhs = {mixed_product(E, x) for x in states if belongs(x)}
        image = {mixed_product(E, x) for x in states}
        rhs = {x for x in image if belongs(x)}
        require('support/strict-pullback', lhs == rhs)


def test_power_indices() -> None:
    cases = [(0,), (3,), (0, 2), (1, 3), (0, 1, 3), (1, 2, 2, 4)]
    for exponents in cases:
        r = len(exponents)
        length = sum(exponents)
        for m in range(1, 7):
            multis = list(compositions(m, r))
            require('powers/symmetric-rank', len(multis) == math.comb(m + r - 1, r - 1))
            vals = [sum(a*b for a, b in zip(alpha, exponents)) for alpha in multis]
            require('powers/symmetric-length', sum(vals) == math.comb(m + r - 1, r) * length)
            require('powers/per-rank', Fraction(sum(vals), len(vals)) == Fraction(m*length, r))
            tensor_vals = [sum(exponents[j] for j in inds) for inds in itertools.product(range(r), repeat=m)]
            require('powers/tensor-length', sum(tensor_vals) == m * r**(m-1) * length)
        for j in range(1, r+1):
            vals = [sum(exponents[i] for i in inds) for inds in itertools.combinations(range(r), j)]
            require('powers/exterior-length', sum(vals) == math.comb(r-1, j-1) * length)
    for a, b in itertools.product(range(6), repeat=2):
        require('powers/composition-length', a + b == len(range(a)) + len(range(a, a+b)))


def polynomial_valuation(p: sp.Expr) -> int:
    poly = sp.Poly(p, T)
    if poly.is_zero:
        raise ValueError('Zero polynomial has no finite valuation')
    return min(monomial[0] for monomial, _ in poly.terms())


def determinantal_valuations(M: sp.Matrix) -> list[int]:
    result = []
    for size in range(1, M.rows+1):
        minors = []
        for rows in itertools.combinations(range(M.rows), size):
            for cols in itertools.combinations(range(M.cols), size):
                det = sp.expand(M.extract(rows, cols).det())
                if det != 0:
                    minors.append(det)
        g = minors[0]
        for minor in minors[1:]:
            g = sp.gcd(g, minor)
        result.append(polynomial_valuation(g))
    return result


def test_nondiagonal_lattices() -> None:
    cases = [(0, 2, 3), (1, 1, 4), (2, 3, 5)]
    U = sp.Matrix([[1, T, 0], [0, 1, T**2], [0, 0, 1]])
    V = sp.Matrix([[1, 0, 0], [T+1, 1, 0], [T, T**2, 1]])
    equal('smith/U-unit', U.det(), 1)
    equal('smith/V-unit', V.det(), 1)
    for a in cases:
        M = U * sp.diag(*(T**j for j in a)) * V
        vals = determinantal_valuations(M)
        require('smith/determinantal-indices', vals == list(itertools.accumulate(a)))
        equal('smith/determinant-length', M.det(), T**sum(a))
        require('smith/generic-isomorphism', M.subs(T, 1).det() != 0)


def test_duality() -> None:
    for a in range(1, 9):
        P = sp.Matrix(a, a, lambda i, j: int(i+j == a-1))
        require('duality/residue-perfect', abs(P.det()) == 1)
        N = sp.zeros(a)
        for j in range(a-1):
            N[j+1, j] = 1
        matrix_equal('duality/T-adjoint', N.T * P, P * N)
        require('duality/T-nilpotent', N**a == sp.zeros(a))
    F = sp.Matrix([[2, 1], [0, 3]])
    matrix_equal('duality/contragredient', F.T * F.inv().T, sp.eye(2))
    for a in [1, 2, 4]:
        P = sp.kronecker_product(sp.Matrix(a, a, lambda i, j: int(i+j == a-1)), sp.eye(2))
        FV = sp.kronecker_product(sp.eye(a), F)
        FD = sp.kronecker_product(sp.eye(a), F.inv().T)
        matrix_equal('duality/residue-F-invariance', FV.T * P * FD, P)


def test_graded_traces() -> None:
    cases = [((-2, 0), (1, 4), (2, 3)), ((0, 1, 2), (0, 3, 5), (1, -1, 2))]
    for lam, mu, eig in cases:
        for n in range(1, 5):
            Q = sum(z**(-l) * f**n for l, f in zip(lam, eig))
            P = sum(z**(-m) * f**n for m, f in zip(mu, eig))
            D = sum(sum(z**(-m+j) * f**n for j in range(m-l)) for l, m, f in zip(lam, mu, eig))
            equal('traces/character', P-Q, (1-z)*D)
            equal('traces/ungraded-cancellation', (P-Q).subs(z, 1), 0)
            equal('traces/derivative', (-z*sp.diff(P-Q, z)).subs(z, 1), D.subs(z, 1))
    J = sp.Matrix([[2, 1], [0, 2]])
    for n in range(1, 6):
        for a in [1, 2, 4]:
            tr = sp.trace(J**n)
            char = tr * (z**(-a)-1)
            D = sum(tr*z**(-a+j) for j in range(a))
            equal('traces/nonsemisimple-character', char, (1-z)*D)


def test_determinant_jets() -> None:
    matrices = [sp.Matrix([[2]]), sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[2, 1], [0, 2]])]
    for F in matrices:
        for a in [1, 2, 3]:
            I = sp.eye(F.rows)
            numerator = (I-u*F).det()
            denominator = (I-u*z**(-a)*F).det()
            B = numerator / denominator
            equal('determinants/neutral-value', B.subs(z, 1), 1)
            derivative = (z*sp.diff(B, z)/B).subs(z, 1)
            resolvent = -a*u*sp.trace(F*(I-u*F).inv())
            equal('determinants/jet-resolvent', derivative, resolvent)
            D_F = sp.kronecker_product(sp.eye(a), F)
            D_poly = (sp.eye(D_F.rows)-u*D_F).det()
            equal('determinants/defect-determinant', D_poly, numerator**a)
            equal('determinants/jet-defect', derivative, u*sp.diff(D_poly, u)/D_poly)
    lam, mu, eig = (0, 1), (2, 4), (2, -1)
    Q = sp.prod(1-u*z**(-l)*f for l, f in zip(lam, eig))
    P = sp.prod(1-u*z**(-m)*f for m, f in zip(mu, eig))
    B = Q/P
    equal('determinants/unequal-block-jet', (z*sp.diff(B, z)/B).subs(z, 1),
          -sum((m-l)*u*f/(1-u*f) for l, m, f in zip(lam, mu, eig)))


def test_arithmetic_local_factors() -> None:
    S = sp.Matrix([[0, 1], [1, 0]])
    invariant = sp.Matrix([1, 1])
    matrix_equal('arithmetic/inertia-invariant', S*invariant, invariant)
    equal('arithmetic/split-factor', (sp.eye(2)-u*sp.eye(2)).det(), (1-u)**2)
    equal('arithmetic/inert-factor', (sp.eye(2)-u*S).det(), 1-u**2)
    equal('arithmetic/ramified-factor', (sp.eye(1)-u*sp.eye(1)).det(), 1-u)
    for n in range(1, 9):
        equal('arithmetic/inert-power-trace', sp.trace(S**n), 0 if n % 2 else 2)
    x, ell, a = sp.symbols('x ell a', positive=True)
    for poly in [1-x, (1-x)**2, 1-x*x]:
        B = poly / poly.subs(x, x*sp.exp(a*eps*ell))
        lhs = (sp.diff(B, eps)/B).subs(eps, 0)
        equal('arithmetic/norm-coupled-jet', lhs, -a*ell*x*sp.diff(poly, x)/poly)
    # Duplication formula with every power of 2 and pi retained.
    two_power = sp.expand(s + (1-s))
    pi_power = sp.expand(-s/2-(s+1)/2+sp.Rational(1,2))
    equal('arithmetic/Gaussian-completion-two', two_power, 1)
    equal('arithmetic/Gaussian-completion-pi', pi_power, -s)


def jet(poly: sp.Expr) -> sp.Expr:
    return sp.expand(poly.subs(eps, 0) + eps*sp.diff(poly, eps).subs(eps, 0))


def test_jets_and_divisor() -> None:
    polys = [0, 1, s+eps, s*s+2*s*eps+3*eps**2, eps**2, 1+s*eps+eps**3]
    for f, g in itertools.product(polys, repeat=2):
        f, g = sp.sympify(f), sp.sympify(g)
        equal('jets/multiplicative', jet(f*g), jet(jet(f)*jet(g)))
        equal('jets/additive', jet(f+g), jet(f)+jet(g))
    a = sp.symbols('a', nonzero=True)
    for g in [(s-2)**3*(s+1), (s-2)**2/(s-1), s*s+1]:
        B = g.subs(s, s-a*eps)/g
        equal('jets/logarithmic-first', sp.diff(B, eps).subs(eps, 0), -a*sp.diff(g, s)/g)
    g = (s-2)**3*(s+1)**2/(s-1)
    J = -2*sp.diff(g, s)/g
    for rho, order in [(2, 3), (-1, 2), (1, -1)]:
        equal('jets/residue-order', sp.residue(J, s, rho), -2*order)
    equal('jets/finite-contour-count', sum(sp.residue(J, s, rho) for rho in [2, -1, 1]), -8)
    # The pole correction between completed Lambda and xi is not dropped.
    ratio = (s-a*eps)*(s-a*eps-1)/(s*(s-1))
    equal('jets/xi-pole-correction', sp.diff(ratio, eps).subs(eps, 0), -a*(1/s+1/(s-1)))


def test_rank_profile() -> None:
    # Independently enumerate the predecessor's endomorphism-spread invariant.
    for alpha, beta in [(2, 0), (1, 1), (3, -2)]:
        for n in range(1, 10):
            weights = [(n-j)*alpha+j*beta for j in range(n+1)]
            pairwise = sum(max(x-y, 0) for x, y in itertools.product(weights, repeat=2))
            require('profiles/end-spread', pairwise == abs(alpha-beta)*n*(n+1)*(n+2)//6)
            require('profiles/degree', sum(weights) == n*(n+1)*(alpha+beta)//2)


def run() -> dict:
    for test in [test_support, test_power_indices, test_nondiagonal_lattices,
                 test_duality, test_graded_traces, test_determinant_jets,
                 test_arithmetic_local_factors, test_jets_and_divisor, test_rank_profile]:
        test()
    return {
        'status': 'passed',
        'arithmetic': 'exact rational numbers and symbolic polynomials',
        'python_version': platform.python_version(),
        'sympy_version': sp.__version__,
        'suites': dict(sorted(COUNTS.items())),
        'finite_assertions': sum(COUNTS.values()),
        'scope': 'Finite instances of stated algebraic proofs; no formal verification or RH claim.'
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    result = run()
    text = json.dumps(result, indent=2, sort_keys=True) + '\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding='utf-8')
    print(text, end='')
