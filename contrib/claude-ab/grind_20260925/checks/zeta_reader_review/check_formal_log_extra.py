#!/usr/bin/env python3
"""F4 spot check: in the Hilbert monoid {n = 1 mod 4}, n = p p' r r' (four distinct primes = 3 mod 4) has three
factorizations into atoms and all proper M-divisors are atoms, so r_n = 1 - 3 + 0 = -2."""
from fractions import Fraction
N = 60000
M = [n for n in range(1, N+1) if n % 4 == 1]
d = [0]*(N+1)
for n in M: d[n] = 1
om = [0]*(N+1)
for n in range(2, N+1):
    m, c, p = n, 0, 2
    while p*p <= m:
        while m % p == 0: m //= p; c += 1
        p += 1
    om[n] = c + (1 if m > 1 else 0)
r = [Fraction(0)]*(N+1)
for n in M:
    if n == 1: continue
    s = Fraction(0); a = 2
    while a*a <= n:
        if n % a == 0 and d[a] and d[n//a]:
            s += om[a]*r[a] + (om[n//a]*r[n//a] if a*a != n else 0)
        a += 1
    r[n] = d[n] - s/om[n]
exp = {3*7*11*19: -2, 3*7*11*23: -2, 7*11*19*23: -2, 9*49: Fraction(-1, 2), 9*7*11: -1}
for n, e in exp.items():
    print(f"Hilbert monoid: r_{n} = {r[n]} (expected {e})")
print("ALL CHECKS PASS" if all(r[n] == e for n, e in exp.items()) else "SOME CHECK FAILED")
