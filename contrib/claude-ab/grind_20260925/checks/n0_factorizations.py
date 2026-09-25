#!/usr/bin/env python3
"""List the factorizations of n0 (smallest element with two factorizations) for the
one-sided monoids M_{1} = {n = 1 mod q} and the even monoids M_{+-1} = {n = +-1 mod q},
q <= 12.  Companion to first_negative_coefficient.py (note 11_, revision 2).
claude-ab, model claude-opus-5-5 (Opus 5.5, max effort)."""
from math import gcd

def factorizations(x, inM):
    D = [d for d in range(1, x + 1) if x % d == 0 and inM(d)]
    Dset = set(D)
    atoms = [d for d in D if d != 1 and not any(e not in (1, d) and d % e == 0 and d // e in Dset for e in D)]
    res = []
    def rec(y, start, acc):
        if y == 1:
            res.append(tuple(acc)); return
        for i in range(start, len(atoms)):
            u = atoms[i]
            if y % u == 0 and (y // u) in Dset:
                rec(y // u, i, acc + [u])
    rec(x, 0, [])
    return res

def n0_of(inM, N=60000):
    for n in range(2, N + 1):
        if inM(n) and len(factorizations(n, inM)) >= 2:
            return n
    return None

for q in range(3, 13):
    for name, H in (("one-sided {1}", {1}), ("even {+-1}", {1, q - 1})):
        inM = lambda n, q=q, H=H: n == 1 or (gcd(n, q) == 1 and n % q in H)
        if H == set(u for u in range(1, q) if gcd(u, q) == 1):
            print(f"q={q:2d} {name:14s}: H = G, free"); continue
        # search only elements of M (fast enough up to 8000)
        n0 = None
        for n in range(2, 8001):
            if inM(n) and len(factorizations(n, inM)) >= 2:
                n0 = n; break
        fs = factorizations(n0, inM) if n0 else []
        print(f"q={q:2d} {name:14s}: n0 = {n0}: " + "  =  ".join("·".join(map(str, f)) for f in fs))
