import sympy as sp
from fractions import Fraction as Fr
hard = [p for p in sp.primerange(1000, 20000) if p % 840 in (1, 121, 169, 289, 361, 529)]
out = []
for p in hard[:12]:
    h = (p - 1)//12
    for a in range((p + 1)//2, 9*h + 1):           # least-denominator shells beyond p/2
        R = 4*a - p; S = p*a
        ds = [1]
        for q, e in sp.factorint(a).items(): ds = [x*q**k for x in ds for k in range(2*e + 1)]
        for u in ds:
            if (u + a) % R == 0:                     # middle state in shell a
                d = p*u; y = (d + S)//R; z = (S*S//d + S)//R
                if min(y, z) >= a:                   # a is the least denominator
                    out.append((p, a, y, z, float(Fr(11*a, 3*(p + 3)))))
                    break
print("hard primes tested:", hard[:12])
print("middle solutions whose least denominator a > p/2 (so 11a > 3(p+3)):", out[:6], "count:", len(out))
