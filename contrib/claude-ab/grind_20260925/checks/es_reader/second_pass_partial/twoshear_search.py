# Targeted search for two consecutive L-edges (m,1)@a -> (m+1,1)@a+1 -> (m+2,1)@a+2
# at primes p = 4a - R, R = 4a - p >= 1, shells p/4 < a, a+2 < p.
# Conditions (from the definition of W, n = 1): m | pa, m+1 | p(a+1), m+2 | p(a+2),
# R | m+1, R+4 | m+2, R+8 | m+3.  We search m, a with m+i | a+i (the p-free branch);
# the branch p | m+i is impossible when m+2 <= a+2 < p unless m+i >= p.
import sys
from math import gcd
from sympy import isprime
def lcm(a,b): return a//gcd(a,b)*b
LIM = int(sys.argv[1]) if len(sys.argv) > 1 else 10**7
found = {1:[],5:[],7:[],11:[]}
R = 1
while R*(R+4) <= 4*LIM:
    # m = -1 mod R, -2 mod R+4, -3 mod R+8  (CRT; moduli may share factors)
    # brute over m in one period of lcm
    Lm = lcm(lcm(R, R+4), R+8)
    # solve incrementally
    sols = [m for m in range(1, Lm+1) if (m+1) % R == 0 and (m+2) % (R+4) == 0 and (m+3) % (R+8) == 0] if Lm < 2*10**6 else None
    if sols is None:
        R += 1; continue
    for m0 in sols:
        m = m0
        while 4*m - R <= LIM:
            Lc = lcm(lcm(m, m+1), m+2)
            a = m
            while 4*a - R <= LIM:
                p = 4*a - R
                if p > 3 and isprime(p) and 4*a > p and a + 2 < p:
                    found[p % 12].append((p, R, a, m))
                a += Lc
            m += Lm
    R += 1
for k in found:
    v = sorted(found[k])
    print(f"p = {k} mod 12: {len(v)} two-L-edge paths with p <= {LIM}; first: {v[:5]}")
