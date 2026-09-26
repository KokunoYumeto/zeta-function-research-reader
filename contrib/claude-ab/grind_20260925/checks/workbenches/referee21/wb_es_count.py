# Referee 21 (wbreader): Theorem 1.1(b) by an independent brute force (divisors of S^2 enumerated directly,
# pairs (y,z) recovered and re-verified with Fractions), and Theorem 1.1(a) by direct search for small p.
from fractions import Fraction as Fr
import sympy as sp
bad = shells = 0; minbad = 0
for p in sp.primerange(13, 400):
    if p % 12 != 1: continue
    h = (p-1)//12
    for a in range(3*h+1, 9*h+1):
        R, S = 4*a-p, p*a
        # all ordered (y,z): 1/y+1/z = R/S  <=>  (Ry-S)(Rz-S) = S^2, both factors positive
        pairs = set()
        for d in sp.divisors(S*S):
            if (d+S) % R == 0 and (S*S//d + S) % R == 0:
                y, z = (d+S)//R, (S*S//d+S)//R
                assert Fr(1,a)+Fr(1,y)+Fr(1,z) == Fr(4,p)
                pairs.add((y, z))
        # E_a, M_a from divisors of a^2
        D = sp.divisors(a*a)
        E = [u for u in D if (4*u+1) % R == 0]; M = [u for u in D if (u+a) % R == 0]
        shells += 1
        if len(pairs) != 2*len(E)+len(M) or len(M) % 2 or any(y == z for y, z in pairs): bad += 1
    # (a): least denominator of every solution lies in [3h+1, 9h] -- search x <= 3p/4 fully, y<=z
    for x in range(1, p+1):
        rem = Fr(4, p) - Fr(1, x)
        if rem <= 0: continue
        for y in range(x, int(2/rem)+1):
            r2 = rem - Fr(1, y)
            if r2 > 0 and r2.numerator == 1 and r2.denominator >= y:
                if not (3*h+1 <= x <= 9*h): minbad += 1
print("shells:", shells, " failures of 2|E|+|M| / |M| even / y!=z:", bad, " least-denominator violations:", minbad)
