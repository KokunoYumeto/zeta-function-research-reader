#!/usr/bin/env python3
"""Referee v2, script r14.  Prop 4.10 for every modulus (version 2).

The two-line race weights p by (1 + 1/p) log p; its difference from the one-line race for classes a, b mod q is
D(x) = sum_{p <= x} (1_{p = a} - 1_{p = b}) log p / p = phi(q)^{-1} sum_{chi != chi0} (conj chi(a) - conj chi(b)) sum_{p<=x} chi(p) log p/p.
 1. The character identity holds exactly (as numbers) at x = 10^6 for q = 7 and q = 9 (all pairs).
 2. D(x) converges: the spread of D(x) over x in {2.5e6, 5e6, 1e7} is small for q in {7, 9, 11, 16}
    (all pairs of classes), and D(x) log(x)/sqrt(x) (the Rubinstein-Sarnak normalisation) is tiny at 1e7.
"""
import numpy as np, math, cmath
from math import gcd
N = 10_000_000
sieve = np.ones(N + 1, bool); sieve[:2] = False
for i in range(2, int(N**0.5) + 1):
    if sieve[i]: sieve[i*i::i] = False
primes = np.nonzero(sieve)[0]
w = np.log(primes) / primes
ok = True
def D(q, a, b, x):
    m = primes <= x
    pr, ww = primes[m], w[m]
    return ww[pr % q == a].sum() - ww[pr % q == b].sum()
# 1: character identity for q = 7 (cyclic, generator 3) and q = 9 (cyclic, generator 2)
for q, g in ((7, 3), (9, 2)):
    units = [u for u in range(1, q) if gcd(u, q) == 1]; phi = len(units)
    dlog = {pow(g, k, q): k for k in range(phi)}
    x = 10**6; m = primes <= x; pr, ww = primes[m], w[m]
    S = {}
    for j in range(1, phi):
        chi = lambda n, j=j: 0 if gcd(int(n), q) != 1 else cmath.exp(2j * math.pi * j * dlog[int(n) % q] / phi)
        vals = np.array([chi(r) for r in range(q)])
        S[j] = (vals[pr % q] * ww).sum()
    for a in units:
        for b in units:
            if a == b: continue
            lhs = D(q, a, b, x)
            rhs = sum((cmath.exp(-2j * math.pi * j * dlog[a] / phi) - cmath.exp(-2j * math.pi * j * dlog[b] / phi)) * S[j] for j in range(1, phi)) / phi
            ok &= abs(lhs - rhs) < 1e-8
print(("[PASS] " if ok else "[FAIL] ") + "1 character identity for D(x) at x = 1e6, q = 7 and 9, all pairs (principal character cancels)")
ok2 = True; rep = []
for q in (7, 9, 11, 16):
    units = [u for u in range(1, q) if gcd(u, q) == 1]
    spread = 0; norm = 0
    for a in units:
        for b in units:
            if a >= b: continue
            vals = [D(q, a, b, x) for x in (2.5e6, 5e6, 1e7)]
            spread = max(spread, max(vals) - min(vals)); norm = max(norm, abs(vals[-1]) * math.log(1e7) / math.sqrt(1e7))
    rep.append((q, spread, norm)); ok2 &= spread < 0.01 and norm < 0.01
print(("[PASS] " if ok2 else "[FAIL] ") + "2 D(x) converges for q = 7, 9, 11, 16 (max spread over x = 2.5e6..1e7; normalised size at 1e7): "
      + "; ".join(f"q={q}: spread {s:.4f}, normalised {n:.2e}" for q, s, n in rep))
print("ALL CHECKS PASS" if (ok and ok2) else "SOME CHECKS FAILED")
