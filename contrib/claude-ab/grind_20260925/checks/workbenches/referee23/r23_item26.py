#!/usr/bin/env python3
"""Referee 23: at p = 67369 (item 26), the first occupied shell in (p/4, p/2) is a = 16850 (R = 31)."""
from sympy import divisors
p = 67369
first = None
for a in range(p // 4 + 1, p // 2 + 1):
    R = 4 * a - p; a2 = a * a
    E = [u for u in divisors(a2) if (4 * u + 1) % R == 0]; M = [u for u in divisors(a2) if (u + a) % R == 0]
    if E or M:
        first = (a, R, E, M); break
print("p=67369: first occupied shell a, R, E_a, M_a =", first)
