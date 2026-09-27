#!/usr/bin/env python3
"""ref50_locks_scope.py -- (1) least occupied shells of the example primes of 50_ §12;
(2) scope of open question 2 of 50_ ('lock universality' for every prime p = 1 mod 4): which primes p = 1 (mod 4)
below X have no lock certificate (lock (a) or (b) of Proposition 50.11 for any odd mu)?  Pass C checked hard primes."""
import sys
from math import gcd
from sympy import primerange, divisors, factorint
X = int(float(sys.argv[1])) if len(sys.argv) > 1 else 200000
def occupied(p, R):
    a = (p + R) // 4
    if gcd(R, p * a) != 1: return False
    ds = [1]
    for q, e in factorint(a).items(): ds = [d * q**k for d in ds for k in range(2 * e + 1)]
    return any((4 * u + 1) % R == 0 or (u + a) % R == 0 for u in ds)
for p in (3361, 18481, 2840041, 12601):
    R = next(R for R in range(3, 3 * p, 4) if occupied(p, R))
    print(f"least occupied shell of {p}: R = {R}")
def has_lock(p):
    for mu in range(1, p, 2):
        N = (p + mu) // 2
        ds = divisors(N)
        for d in ds:
            if d % 2 and (d + p) % (4 * mu) == 0 and d < p: return ('a', mu, d)
            if (d + 1) % (4 * mu) == 0 and 7 * mu <= p + 2: return ('b', mu, d)
    return None
S840 = {1, 121, 169, 289, 361, 529}
nolock = [p for p in primerange(5, X) if p % 4 == 1 and has_lock(p) is None]
print(f"primes p = 1 (mod 4) below {X} with no lock certificate: {len(nolock)}; first: {nolock[:20]}")
print("   of these, hard:", [p for p in nolock if p % 840 in S840][:10], " p = 5 (mod 8):", [p for p in nolock if p % 8 == 5][:10])
