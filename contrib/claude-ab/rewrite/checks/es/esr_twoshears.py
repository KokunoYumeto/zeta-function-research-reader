# Exact scope of the no-two-shears theorem of the bounded-transport supplement (section 5,
# Theorem "No two consecutive positive Euclidean shell steps", stated for p = 12h+1 and a in [3h+1, 9h]).
# Full graph, from the definitions only: vertices (a,m,n) with p/4 < a < p and (m,n) in
#   W_a = {(m,n): m,n | pa, gcd(m,n) = 1, R_a | m+n},  R_a = 4a - p,
# edges (a,m,n) -> (a+1,m+n,n) [L] and (a,m,n) -> (a+1,m,m+n) [J] whenever the target lies in W_{a+1}.
# Claim checked: a directed path of length two exists for no prime p = 1 mod 3, and for some p = 2 mod 3.
# Prepared by Claude (Opus 5.5) for the Erdos-Straus reader.  Needs sympy.
import sys
from math import gcd
from sympy import primerange, divisors

LIM = int(sys.argv[1]) if len(sys.argv) > 1 else 2000

def W(p, a):
    R = 4 * a - p
    D = divisors(p * a)
    return {(m, n) for m in D for n in D if gcd(m, n) == 1 and (m + n) % R == 0}

stats = {}
first = {}
for p in primerange(5, LIM):
    lo = p // 4 + 1
    Ws = {a: W(p, a) for a in range(lo, p)}
    succ = {}
    for a in range(lo, p - 1):
        for (m, n) in Ws[a]:
            for t in ((m + n, n), (m, m + n)):
                if t in Ws[a + 1]:
                    succ.setdefault((a, m, n), []).append((a + 1,) + t)
    edges = sum(len(v) for v in succ.values())
    paths = [(v, w, x) for v, ws in succ.items() for w in ws for x in succ.get(w, [])]
    key = p % 12
    s = stats.setdefault(key, [0, 0, 0])
    s[0] += 1; s[1] += edges; s[2] += len(paths)
    if paths and key not in first:
        first[key] = (p, paths[0])
ok = True
for key in sorted(stats):
    n, e, P = stats[key]
    print(f"p = {key:2d} mod 12: {n} primes below {LIM}, {e} edges, {P} directed paths of length two"
          + (f"; first at p = {first[key][0]}: {first[key][1]}" if key in first else ""))
    if key % 3 == 1 and P != 0: ok = False
    if key % 3 == 2 and P == 0: ok = False
print("ALL PASS (no two-step path for p = 1 mod 3; two-step paths occur for p = 2 mod 3)" if ok else "FAIL")

# Part 2: complete search for two-edge L-paths up to LIM2, using the shape of an edge proved in the reader
# (an L-edge (a,m,n) -> (a+1,m+n,n) forces n = 1, m | a, m+1 | a+1, R_a | m+1, R_a+4 | m+2).
# Two L-edges through (a+i, m+i, 1), i = 0,1,2:  m+i | a+i  and  R+4i | m+i+1.
# For odd R the moduli R, R+4, R+8 are pairwise coprime; m is fixed modulo R(R+4)(R+8) by CRT, and
# lcm(m,m+1,m+2) | K = a - m.  J-paths correspond one-to-one by exchanging coordinates.
from math import lcm
from sympy import isprime
from sympy.ntheory.modular import crt
LIM2 = int(sys.argv[2]) if len(sys.argv) > 2 else 10**7
count = {}
firsts = {}
R = 1
while 3 * R - 4 <= LIM2:
    M = R * (R + 4) * (R + 8)
    m0 = int(crt([R, R + 4, R + 8], [-1 % R, -2 % (R + 4), -3 % (R + 8)])[0])
    if m0 == 0: m0 = M
    m = m0
    while 4 * m - R <= LIM2:
        Lm = lcm(m, m + 1, m + 2)
        a = m
        while 4 * a - R <= LIM2:
            p = 4 * a - R
            if p > 3 and a + 2 < p and isprime(p):
                count[p % 12] = count.get(p % 12, 0) + 1
                firsts.setdefault(p % 12, (p, R, a, m))
            a += Lm
        m += M
    R += 2
ok2 = all(k % 3 == 2 for k in count)
for k in sorted(count):
    print(f"part 2: p = {k:2d} mod 12, p <= {LIM2}: {count[k]} two-L-edge paths (and as many two-J-edge paths); first (p,R,a,m) = {firsts[k]}")
print("part 2: " + ("PASS (every two-edge path has p = 2 mod 3)" if ok2 else "FAIL"))
