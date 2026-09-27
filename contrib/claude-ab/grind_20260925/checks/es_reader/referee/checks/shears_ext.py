# Directed shear paths of length k on the full shell range p/4 < a < p (definitions as in the reader's Prop. 2.1).
from math import gcd, lcm
from sympy import isprime, divisors
from sympy.ntheory.modular import crt

def in_W(p, a, m, n):
    R = 4*a - p
    return R >= 1 and (p*a) % m == 0 and (p*a) % n == 0 and gcd(m, n) == 1 and (m + n) % R == 0

def verify_L_path(p, a, m, k):
    # vertices (a+i, m+i, 1), i = 0..k ; edges are L-shears
    if not (4*a > p and a + k < p): return False
    for i in range(k + 1):
        if not in_W(p, a + i, m + i, 1): return False
    return True

def least_prime_with_path(k, Rmax=60, tmax=4000):
    best = None
    for R in range(1, Rmax, 2):
        mods = [R + 4*i for i in range(k + 1)]
        res = [(-(i + 1)) % (R + 4*i) for i in range(k + 1)]
        sol = crt(mods, res)
        if sol is None: continue
        m0, M = int(sol[0]), int(sol[1])
        if m0 == 0: m0 = M
        for m in (m0, m0 + M, m0 + 2*M):
            L = lcm(*[m + i for i in range(k + 1)])
            for t in range(tmax):
                a = m + t*L; p = 4*a - R
                if best is not None and p >= best[0]: break
                if p > 3 and isprime(p) and verify_L_path(p, a, m, k):
                    best = (p, R, a, m); break
    return best

for k in (2, 3, 4, 5):
    b = least_prime_with_path(k)
    print(f"length {k}: least prime found (p, R, a, m) = {b}, p mod 3 = {b[0] % 3}, verified from definitions: {verify_L_path(b[0], b[2], b[3], k)}")

# every unit class mod 840 that is 2 mod 3 contains a prime with a two-edge path?
classes = set()
hits = {}
for R in range(1, 200, 2):
    mods = [R, R + 4, R + 8]; res = [-1 % R, -2 % (R + 4), -3 % (R + 8)]
    m0, M = [int(x) for x in crt(mods, res)]
    if m0 == 0: m0 = M
    for j in range(6):
        m = m0 + j*M
        L = lcm(m, m + 1, m + 2)
        for t in range(0, 400):
            a = m + t*L; p = 4*a - R
            if p > 10**12: break
            c = p % 840
            if c in hits: continue
            if isprime(p) and verify_L_path(p, a, m, 2):
                hits[c] = p
target = [c for c in range(840) if gcd(c, 840) == 1 and c % 3 == 2]
print("unit classes mod 840 with c = 2 mod 3:", len(target), "; covered by primes with a two-edge path:", len(set(target) & set(hits)),
      "; any hit class = 1 mod 3:", any(c % 3 == 1 for c in hits))
print("sample:", sorted(hits.items())[:6])
