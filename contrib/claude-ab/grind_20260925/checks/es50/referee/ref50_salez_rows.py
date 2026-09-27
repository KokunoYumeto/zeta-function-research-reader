#!/usr/bin/env python3
"""ref50_salez_rows.py -- the 'free' rows of Theorem 50.4 are single Salez charts with small constants:
  p+1  : (2b) with (B, C, F) = (1, 1, R)      p+2  : (2b) with (1, 2, R)      2p+1 : (2b) with (2, 1, R)
  p+4  : (1c) with (B, D, E) = (1, 1, R)      p+8  : (1c) with (1, 2, R)
(and the missed rows: p+4s is (1c) with B^2 D = s; p+t is (2b)(1, t, R); tp+1 is (2b)(t, 1, R)).
For every prime p = 1 (mod 24) below 2*10^5 and every (shift, q) with (p/q) = -1, the shell certificate of
Table 50.4 and the Salez chart give the same unordered triple {x, y, z}."""
from sympy import primerange, factorint, legendre_symbol
from fractions import Fraction as Fr
def shell(p, R, u, ch):
    a = (p + R) // 4; N = p * a; d = p * p * u if ch == 'E' else p * u
    return tuple(sorted((a, (N + d) // R, (N + N * N // d) // R)))
def c2b(p, B, C, F):     # Type I: D = (p+F)/(4BC), A = (pB+C)/F, denominators (BCD, ACD, pABD)
    assert (p + F) % (4 * B * C) == 0 and (p * B + C) % F == 0
    D = (p + F) // (4 * B * C); A = (p * B + C) // F
    return tuple(sorted((B * C * D, A * C * D, p * A * B * D)))
def c1c(p, B, D, E):     # Type II: A = (p+E)/(4BD), C = (p+E+4B^2D)/(4BDE), denominators (pBCD, pACD, ABD)
    assert (p + E) % (4 * B * D) == 0 and (p + E + 4 * B * B * D) % (4 * B * D * E) == 0
    A = (p + E) // (4 * B * D); C = (p + E + 4 * B * B * D) // (4 * B * D * E)
    return tuple(sorted((p * B * C * D, p * A * C * D, A * B * D)))
n = 0; bad = 0
for p in primerange(25, 200000):
    if p % 24 != 1: continue
    for name, S in (("p+1", p+1), ("p+2", p+2), ("p+4", p+4), ("p+8", p+8), ("2p+1", 2*p+1)):
        for q in factorint(S):
            if q == 2 or legendre_symbol(p % q, q) != -1: continue
            if name in ("p+1", "p+4"): R = q
            else: R = q if q % 8 == 7 else 3 * q
            a = (p + R) // 4
            if name == "p+1": s, t = shell(p, R, a, 'E'), c2b(p, 1, 1, R)
            if name == "p+2": s, t = shell(p, R, a // 2, 'E'), c2b(p, 1, 2, R)
            if name == "2p+1": s, t = shell(p, R, 2 * a, 'E'), c2b(p, 2, 1, R)
            if name == "p+4": s, t = shell(p, R, 1, 'M'), c1c(p, 1, 1, R)
            if name == "p+8": s, t = shell(p, R, 2, 'M'), c1c(p, 1, 2, R)
            n += 1; bad += (s != t) or not (4 * s[0] * s[1] * s[2] == p * (s[0]*s[1] + s[1]*s[2] + s[0]*s[2]))
print(f"rows p+1, p+2, 2p+1, p+4, p+8 versus Salez (2b)/(1c): {n} certificates compared, {bad} mismatches")
