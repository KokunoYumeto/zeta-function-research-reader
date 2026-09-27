#!/usr/bin/env python3
"""ref50_examples.py -- the example p = 2,458,369 of Proposition 50.7 (mu = 17) and the record p* under the
missed shift conditions of ref50_more_shifts.py."""
from math import gcd
from sympy import factorint, legendre_symbol, divisors
def is_sol(p, x, y, z): return 4 * x * y * z == p * (x * y + y * z + z * x)
def eight_nr(p):
    out = []
    for name, S in (("p+1", p+1), ("p+2", p+2), ("p+3", p+3), ("p+4", p+4), ("p+7", p+7), ("p+8", p+8), ("2p+1", 2*p+1), ("3p+1", 3*p+1)):
        out += [(name, q) for q in factorint(S) if q > 2 and legendre_symbol(p % q, q) == -1]
    return out
p = 2458369
print("p =", p, "mod 840:", p % 840, "mod 9:", p % 9, "mod 17:", p % 17, "; eight-shift non-residue factors:", eight_nr(p))
print("   p+17 =", factorint(p + 17), "; non-residue factors:", [q for q in factorint(p + 17) if q > 2 and legendre_symbol(p % q, q) == -1])
N = (p + 17) // 2
for h in divisors(N):
    if (h + 1) % 68 == 0:
        e = N // h; t = (h + 1) // 68; a = 34 * e * t; R = 17 + 2 * e; u = 289 * t
        y = p * (a + u) // R; z = p * (a + a * a // u) // R
        print(f"   lock (b): h = {h}, R = {R}, a = {a}, u = {u}: 4/p = 1/{a} + 1/{y} + 1/{z}; exact: {is_sol(p, a, y, z) and (4*a - p == R)}")
        break
ps = 8803369
print("p* mod 840:", ps % 840, "mod 10080:", ps % 10080)
for name, S in (("p+16", ps + 16), ("p+36", ps + 36), ("p+6", ps + 6), ("6p+1", 6 * ps + 1), ("p+20", ps + 20)):
    nr = [q for q in factorint(S) if q > 7 and legendre_symbol(ps % q, q) == -1]
    print(f"   {name} = {factorint(S)}; non-residue prime factors (> 7): {nr}")
