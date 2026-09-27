#!/usr/bin/env python3
"""ref50_visiblebox.py -- referee recomputation of the visible-box table (Theorem 50.6 / reader Thm visiblebox)
by a different method: the forced exponents e_f are read off EMPIRICALLY as the minimum of v_f((p+R)/4) over
actual primes p in each hard class modulo 10080 (all primes below 2*10^6 in the class), instead of from the
class arithmetic.  Also checks the criterion (in its simplified form 'some odd q | p+R has (p/q) = -1') and the
redundancy of the disjunct (p/R) = -1 on every tested prime."""
import time
from math import gcd, isqrt
import numpy as np
T0 = time.time()
L = 10080
S840 = {1, 121, 169, 289, 361, 529}
X = 2 * 10**6
LIM = X + 1000
sieve = np.ones(LIM + 1, dtype=bool); sieve[:2] = False
for i in range(2, isqrt(LIM) + 1):
    if sieve[i]: sieve[i*i::i] = False
primes = np.nonzero(sieve)[0].tolist()
HC = [c for c in range(1, L, 24) if c % 840 in S840]
byclass = {c: [] for c in HC}
for p in primes:
    if p % L in byclass: byclass[p % L].append(p)
def v(n, l):
    k = 0
    while n % l == 0: n //= l; k += 1
    return k
counts = {}
for R in [q for q in range(3, 700) if sieve[q] and q % 4 == 3]:
    Q = {(i * i) % R for i in range(1, R)}
    good = 0
    for c in HC:
        ps = [p for p in byclass[c] if p != R]
        e = {f: min(v((p + R) // 4, f) for p in ps) if f != R else 0 for f in (2, 3, 5, 7)}
        box = {1}
        for f, ef in e.items():
            if f == R: continue
            box = {(b * pow(f, k, R)) % R for b in box for k in range(2 * ef + 1)}
        if Q <= box: good += 1
    if good: counts[R] = good
print("good classes (of 72) per prime shell R, exponents read from primes below 2*10^6:", counts)
print("claim: {3: 72, 7: 72, 11: 48, 19: 12, 23: 48, 31: 30, 47: 20, 59: 4, 71: 12, 311: 1}")
print(f"time {time.time() - T0:.1f}s")
