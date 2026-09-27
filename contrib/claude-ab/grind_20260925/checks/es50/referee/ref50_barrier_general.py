#!/usr/bin/env python3
"""ref50_barrier_general.py -- the width-one and group barriers coincide whenever every prime factor of R is
= 3 (mod 4) (the 2-Sylow subgroup of (Z/R)^x is then elementary abelian); they can differ only when R has a prime
factor = 1 (mod 4).  (1) exhaustive over all cyclic and 2-generated subgroups K for all such R < 700;
(2) every separating shell (width-one kills, group barrier silent) among the shells R < 3p of the primes
p = 1 (mod 24) below 3000 has a prime factor = 1 (mod 4)."""
from math import gcd
from itertools import combinations
from sympy import factorint, primerange
def subgroup(gens, R):
    K = {1}; fr = [1]
    while fr:
        nx = []
        for k in fr:
            for g in gens:
                y = (k * g) % R
                if y not in K: K.add(y); nx.append(y)
        fr = nx
    return K
def times4(K, R):
    out = set(K); cur = set(K)
    while True:
        cur = {(4 * k) % R for k in cur}
        if cur <= out: return out
        out |= cur
bad = 0; nsub = 0; nR = 0
for R in range(3, 700, 4):
    if any(q % 4 == 1 for q in factorint(R)): continue
    nR += 1
    units = [x for x in range(2, R) if gcd(x, R) == 1]
    subs = {frozenset(subgroup([g], R)) for g in units}
    subs |= {frozenset(subgroup([g, h], R)) for g, h in combinations(units[:40], 2)}
    for K in subs:
        nsub += 1
        w1 = ((R - 1) in K) or ((-4) % R in K)
        gb = (R - 1) in times4(K, R)
        if w1 != gb: bad += 1
print(f"(1) R < 700, R = 3 (mod 4), all prime factors = 3 (mod 4): {nR} values of R, {nsub} subgroups, disagreements {bad}")
sep = []
for p in [p for p in primerange(25, 3000) if p % 24 == 1]:
    for R in range(3, 3 * p, 4):
        if R % p == 0: continue
        a = (p + R) // 4
        K = subgroup([q % R for q in factorint(a)], R)
        w1 = not (((R - 1) in K) or ((-4) % R in K))
        gb = not ((R - 1) in times4(K, R))
        if w1 and not gb: sep.append((p, R))
print(f"(2) separating shells: {len(sep)}; all have a prime factor = 1 (mod 4): {all(any(q % 4 == 1 for q in factorint(R)) for p, R in sep)}; "
      f"smallest R: {min(R for p, R in sep)}; R values: {sorted({R for p, R in sep})[:15]} ...")
