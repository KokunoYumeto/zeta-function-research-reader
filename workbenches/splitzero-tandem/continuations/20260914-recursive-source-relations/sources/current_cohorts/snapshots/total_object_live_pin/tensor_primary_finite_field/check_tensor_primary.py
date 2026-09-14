"""Exact finite-group and coefficient checks for TPF; no floating point."""
from collections import Counter
from itertools import product
from pathlib import Path
from math import gcd, factorial
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parent

def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]

def mobius(n):
    sign = 1
    p = 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            sign = -sign
            if n % p == 0:
                return 0
        p += 1
    return -sign if n > 1 else sign

def order(q, n):
    x = q % n
    d = 1
    while x != 1:
        x = x * q % n
        d += 1
    return d

def d0(n, k):
    numerator = (n - 1)**k + (n - 1)*(-1)**k
    assert numerator % n == 0
    return numerator // n

count_cases = 0
branch_cases = 0
scalar_cases = 0
for n in range(2, 21):
    counts = [1] + [0]*(n - 1)
    for k in range(1, 61):
        counts = [sum(counts[(t - j) % n] for j in range(1, n))
                  for t in range(n)]
        expected = [d0(n, k)] + [((n - 1)**k - (-1)**k)//n]*(n - 1)
        assert counts == expected
        image_gcd = n
        for t, multiplicity in enumerate(counts):
            if multiplicity:
                image_gcd = gcd(image_gcd, t)
        image_order = n // image_gcd
        assert image_order == (1 if n == 2 and k % 2 == 0 else n)
        count_cases += 1
        for p in (3, 5, 7, 11, 13, 17, 19, 23, 29, 31):
            if p <= n:
                continue
            for c in (0, 1):
                w = k*c % p
                invariant_dim = counts[0] if w == 0 else 0
                assert invariant_dim == (d0(n, k) if c == 0 or k % p == 0 else 0)
                terminal_invariant = ((n - 1)*k % n == 0 and w == 0)
                assert terminal_invariant == (k % (n if c == 0 else p*n) == 0)
                branch_cases += 1
            K = k*(n - 2)
            denominator = pow(factorial(n - 2) % p, k, p)
            assert denominator != 0
            for unit in (0, 1, 2):
                coefficient = factorial(K) % p
                coefficient = coefficient * pow(denominator, -1, p) % p
                coefficient = coefficient * pow(unit, k, p) % p
                assert (coefficient != 0) == (K < p and unit % p != 0)
                scalar_cases += 1

orbit_cases = 0
tuple_checks = 0
for n in range(2, 10):
    for p in (3, 5, 7, 11, 13):
        if p <= n:
            continue
        d = order(p, n)
        for k in range(1, 6):
            tuples = {t for t in product(range(1, n), repeat=k) if sum(t) % n == 0}
            assert len(tuples) == d0(n, k)
            unseen = set(tuples)
            orbit_counts = Counter()
            while unseen:
                t = min(unseen)
                orbit = []
                v = t
                while v not in orbit:
                    orbit.append(v)
                    v = tuple(p*x % n for x in v)
                assert v == t and d % len(orbit) == 0
                for value in t:
                    char_order = n // gcd(value, n)
                    assert (p**len(orbit) - 1) % char_order == 0
                unseen.difference_update(orbit)
                orbit_counts[len(orbit)] += 1
                tuple_checks += len(orbit)
            fixed = {}
            for f in divisors(d):
                g = gcd(n, p**f - 1)
                fixed[f] = d0(g, k)
                explicit = sum(all((p**f*x - x) % n == 0 for x in t) for t in tuples)
                assert explicit == fixed[f]
            for e in divisors(d):
                numerator = sum(mobius(e//f)*fixed[f] for f in divisors(e))
                assert numerator % e == 0
                assert orbit_counts[e] == numerator//e
            terminal = (n - 1,)*k
            v = tuple(p*x % n for x in terminal)
            length = 1
            while v != terminal:
                v = tuple(p*x % n for x in v)
                length += 1
            assert length == d
            orbit_cases += 1

source = ROOT / "tensor_primary_finite_field.tex"
text = source.read_text(encoding="utf-8")
tags = re.findall(r"\\tag\{(TPF\.\d+)\}", text)
labels = re.findall(r"\\label\{([^}]+)\}", text)
refs = re.findall(r"\\eqref\{([^}]+)\}", text)
assert tags == [f"TPF.{i}" for i in range(1, 56)]
assert len(labels) == len(set(labels))
assert set(refs).issubset(labels)
report = {
    "status": "passed",
    "method": "exact integer finite-group enumeration, convolution, modular factorials",
    "all_character_multiplicity_cases": count_cases,
    "wild_and_terminal_invariant_cases": branch_cases,
    "coefficient_specialization_cases": scalar_cases,
    "original_field_orbit_cases": orbit_cases,
    "invariant_tuple_descent_checks": tuple_checks,
    "equation_tags": len(tags),
    "labels": len(labels),
    "resolved_references": len(refs),
    "tex_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
}
(ROOT / "EXACT_CHECKS.json").write_text(json.dumps(report, indent=2) + "\n",
                                      encoding="utf-8")
print(json.dumps(report, indent=2))
