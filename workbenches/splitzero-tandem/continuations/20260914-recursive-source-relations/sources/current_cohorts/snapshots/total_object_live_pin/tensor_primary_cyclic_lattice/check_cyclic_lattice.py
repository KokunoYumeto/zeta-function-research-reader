"""Exact finite checks of TCL identities; the TeX contains the general proofs."""
from fractions import Fraction as Q
from itertools import product
from math import factorial, prod, comb
from pathlib import Path
import hashlib
import json
import re


def clean(d):
    return {b: c for b, c in d.items() if c}


def add(a, b):
    d = dict(a)
    for t, c in b.items():
        d[t] = d.get(t, 0) + c
    return clean(d)


def scale(a, c):
    return clean({t: c * x for t, x in a.items()})


def multiply(a, b, m):
    d = {}
    for s, x in a.items():
        for t, y in b.items():
            u = tuple(v + w for v, w in zip(s, t))
            if all(v < m for v in u):
                d[u] = d.get(u, 0) + x * y
    return clean(d)


def reduce_mod(a, p):
    return clean({t: int(Q(c).numerator % p)
                   * pow(Q(c).denominator, -1, p) % p
                  for t, c in a.items()})


def rank_mod(columns, basis, p):
    rows = [[col.get(b, 0) % p for col in columns] for b in basis]
    lead = 0
    for col in range(len(columns)):
        pivot = next((i for i in range(lead, len(rows))
                      if rows[i][col]), None)
        if pivot is None:
            continue
        rows[lead], rows[pivot] = rows[pivot], rows[lead]
        inv = pow(rows[lead][col], -1, p)
        rows[lead] = [v * inv % p for v in rows[lead]]
        for i in range(lead + 1, len(rows)):
            c = rows[i][col]
            if c:
                rows[i] = [(x - c * y) % p
                           for x, y in zip(rows[i], rows[lead])]
        lead += 1
        if lead == len(rows):
            break
    return lead


def translated_to_original(poly, rho, m):
    """Expand every actual y_i=s_i-rho into the original s monomials."""
    out = {}
    for b, c in poly.items():
        for a in product(*(range(v + 1) for v in b)):
            coefficient = c * prod(comb(v, w) * (-rho) ** (v - w)
                                   for v, w in zip(b, a))
            out[a] = out.get(a, 0) + coefficient
    return clean(out)


records = []
primes = [2, 3, 5, 7, 11, 13, 17, 19]
for m in range(1, 6):
    for k in range(1, 7):
        if m ** k > 625:
            continue
        basis = list(product(range(m), repeat=k))
        zero = (0,) * k
        one = {zero: 1}
        K = k * (m - 1)
        J = {}
        if m > 1:
            for i in range(k):
                b = tuple(int(j == i) for j in range(k))
                J[b] = 1
        a = [1] + [j * j + 2 for j in range(1, m)]
        inv = [1]
        for r in range(1, m):
            inv.append(-sum(a[j] * inv[r - j] for j in range(1, r + 1)))
        U = clean({b: prod(a[j] for j in b) for b in basis})
        Uinv = clean({b: prod(inv[j] for j in b) for b in basis})
        assert multiply(U, Uinv, m) == one
        V = [{b: Q(1, prod(factorial(v) for v in b))
              for b in basis if sum(b) == r} for r in range(K + 1)]
        W = [multiply(U, v, m) for v in V]
        powers = [one]
        for r in range(1, K + 2):
            powers.append(multiply(J, powers[-1], m))
        assert not powers[K + 1]
        for r in range(K + 1):
            assert powers[r] == scale(V[r], factorial(r))
            assert multiply(J, V[r], m) == (scale(V[r + 1], r + 1)
                                              if r < K else {})
            assert multiply(J, W[r], m) == (scale(W[r + 1], r + 1)
                                              if r < K else {})
            assert multiply(Uinv, W[r], m) == V[r]
            pivot = max(b for b in basis if sum(b) == r)
            assert V[r][pivot] * prod(factorial(v) for v in pivot) == 1
        # Verify all original Z^j columns independently by repeated M-products.
        rho = Q(2, 3)
        M = add(J, scale(one, k * rho))
        Mpowers = [one]
        for j in range(1, K + 1):
            Mpowers.append(multiply(M, Mpowers[-1], m))
        for j in range(K + 1):
            original = multiply(U, Mpowers[j], m)
            candidate = {}
            for r in range(j + 1):
                candidate = add(candidate, scale(W[r],
                    comb(j, r) * (k * rho) ** (j - r) * factorial(r)))
            assert original == candidate
            if m ** k <= 25:
                assert translated_to_original(original, rho, m) == \
                       translated_to_original(candidate, rho, m)
        prime_records = []
        for p in primes:
            if p <= m:
                continue
            Wmod = [reduce_mod(w, p) for w in W]
            Jmod = reduce_mod(J, p)
            cols = [reduce_mod(multiply(U, powers[r], m), p)
                    for r in range(K + 1)]
            assert rank_mod(cols, basis, p) == min(p, K + 1)
            for r, col in enumerate(cols):
                assert bool(col) == (r < p)
                direct_v = 0
                fact = factorial(r)
                while fact and fact % p == 0:
                    fact //= p
                    direct_v += 1
                floor_v = sum(r // p ** a for a in range(1, K + 2))
                assert direct_v == floor_v
                product_J = reduce_mod(multiply(Jmod, Wmod[r], m), p)
                expected = reduce_mod(scale(Wmod[r + 1], r + 1), p) \
                    if r < K else {}
                assert product_J == expected
                if r < p:
                    assert col == reduce_mod(scale(Wmod[r], factorial(r)), p)
                else:
                    assert not col
            last = min(p - 1, K)
            assert reduce_mod(powers[last], p)
            assert not reduce_mod(powers[last + 1], p)
            prime_records.append({"p": p, "cyclic_image_rank": min(p, K + 1),
                "tor_rank": max(0, K + 1 - p),
                "top_depth": sum(K // p ** a for a in range(1, K + 2))})
        records.append({"m": m, "k": k, "K": K, "ambient_rank": m ** k,
                        "primes": prime_records})

# The divided-difference identity is independently expanded for arbitrary
# rational polynomial coefficients and distinct complex rational centres.
# These numerical centres are algebraic test inputs, not claimed zeta zeros.
import sympy as sp
X, Y = sp.symbols("X Y")
for degree in range(1, 10):
    coeff = [sp.Rational(j + 2, j + 3) for j in range(degree + 1)]
    lhs = sum(coeff[r] * (X ** r - Y ** r) for r in range(degree + 1))
    D = sum(coeff[r] * sum(X ** (r - 1 - j) * Y ** j for j in range(r))
            for r in range(1, degree + 1))
    assert sp.expand(lhs - (X - Y) * D) == 0

root = Path(__file__).parent
tex = (root / "tensor_primary_cyclic_lattice.tex").read_text(encoding="utf-8")
tags = [int(x) for x in re.findall(r"\\tag\{TCL\.(\d+)\}", tex)]
assert tags == list(range(1, 38))
result = {"status": "passed", "packet_cases": len(records),
          "prime_packet_cases": sum(len(r["primes"]) for r in records),
          "divided_difference_degrees": list(range(1, 10)),
          "tags": tags, "source_sha256": hashlib.sha256(tex.encode()).hexdigest(),
          "cases": records,
          "scope": "Exact finite checks supplement, and do not replace, general TeX proofs."}
(root / "EXACT_CHECKS.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
print(json.dumps({k: v for k, v in result.items() if k != "cases"}, indent=2))
