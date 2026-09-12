#!/usr/bin/env python3
"""Independently generate finite congruences and compare the fibre-quotient formula.
Run with Python 3. No dependencies. No floating-point or RH assertions.
"""
from itertools import product
import json

TAU = None

def add_scalar(a, b, q):
    if a is TAU:
        return b
    if b is TAU:
        return a
    return (a + b) % q

def mul_scalar(a, b, q):
    return TAU if a is TAU or b is TAU else a * b % q

def add(x, y, q):
    return tuple(add_scalar(a, b, q) for a, b in zip(x, y))

def scale(a, x, q):
    return tuple(mul_scalar(a, b, q) for b in x)

def mask(x):
    return frozenset(i for i, a in enumerate(x) if a is not TAU)

def amp(x):
    return tuple(0 if a is TAU else a for a in x)

def apply(A, x, q):
    out = []
    for row in A:
        value = TAU
        for a, b in zip(row, x):
            value = add_scalar(value, mul_scalar(a, b, q), q)
        out.append(value)
    return tuple(out)

def test(q, A, ordinary=False):
    alphabet = (TAU, *range(q))
    n, m = len(A), len(A[0])
    src = list(product(alphabet, repeat=m))
    dst = list(product(alphabet, repeat=n))
    ix = {x: j for j, x in enumerate(dst)}
    parent = list(range(len(dst)))
    def root(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i
    def join(i, j):
        i, j = root(i), root(j)
        if i == j:
            return False
        parent[j] = i
        return True
    for x in src:
        y = apply(A, x, q)
        z = (TAU,) * n if ordinary else scale(0, y, q)
        join(ix[y], ix[z])
    changed = True
    while changed:
        changed = False
        groups = {}
        for i in range(len(dst)):
            groups.setdefault(root(i), []).append(i)
        for group in groups.values():
            x = dst[group[0]]
            for j in group[1:]:
                y = dst[j]
                for z in dst:
                    changed |= join(ix[add(x, z, q)], ix[add(y, z, q)])
                for a in alphabet:
                    changed |= join(ix[scale(a, x, q)], ix[scale(a, y, q)])
    if ordinary:
        return len({root(i) for i in range(len(dst))}), 0
    spans = {}
    for bits in product((0, 1), repeat=n):
        K = frozenset(i for i, b in enumerate(bits) if b)
        allowed = [j for j in range(m)
                   if frozenset(i for i in range(n) if A[i][j] is not TAU) <= K]
        spans[K] = {
            tuple(sum(c * (0 if A[i][j] is TAU else A[i][j])
                      for c, j in zip(coeffs, allowed)) % q for i in range(n))
            for coeffs in product(range(q), repeat=len(allowed))
        }
    count = 0
    for x in dst:
        for y in dst:
            difference = tuple((a - b) % q for a, b in zip(amp(x), amp(y)))
            predicted = mask(x) == mask(y) and difference in spans[mask(x)]
            actual = root(ix[x]) == root(ix[y])
            count += 1
            if actual != predicted:
                raise ArithmeticError((q, A, x, y, actual, predicted))
    return len({root(i) for i in range(len(dst))}), count

def main():
    cases = [
        (4, ((2,),)),
        (2, ((1, 1), (TAU, 0))),
        (3, ((1, 1), (TAU, 0))),
        (3, ((1, TAU), (1, 1))),
        (3, ((1, 0), (2, TAU), (TAU, 1))),
        (2, ((0, 1), (TAU, 1), (0, TAU))),
    ]
    records = []
    for q, A in cases:
        classes, comparisons = test(q, A)
        records.append({'modulus': q, 'rows': len(A), 'columns': len(A[0]),
                        'classes': classes, 'comparisons': comparisons})
    ordinary_classes, _ = test(4, ((2,),), ordinary=True)
    if records[0]['classes'] != 3 or ordinary_classes != 2:
        raise ArithmeticError('The original two congruences have been conflated')
    print(json.dumps({'status': 'passed', 'cases': records,
                      'exact_pair_comparisons': sum(r['comparisons'] for r in records),
                      'ordinary_mod_two_classes': ordinary_classes,
                      'scope': 'Finite congruence checks; general proof in the note.'},
                     sort_keys=True, indent=2))

if __name__ == '__main__':
    main()
