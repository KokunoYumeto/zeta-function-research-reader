from math import gcd, lcm
from sympy import isprime
from sympy.ntheory.modular import crt
def in_W(p, a, m, n):
    R = 4*a - p
    return R >= 1 and (p*a) % m == 0 and (p*a) % n == 0 and gcd(m, n) == 1 and (m + n) % R == 0
def verify_L_path(p, a, m, k):
    if not (4*a > p and a + k < p): return False
    return all(in_W(p, a + i, m + i, 1) for i in range(k + 1))
target = {c for c in range(840) if gcd(c, 840) == 1 and c % 3 == 2}
hits = {}
for R in range(1, 2000, 2):
    if len(hits) == len(target): break
    mods = [R, R + 4, R + 8]; res = [-1 % R, -2 % (R + 4), -3 % (R + 8)]
    m0, M = [int(x) for x in crt(mods, res)]
    if m0 == 0: m0 = M
    for j in range(40):
        m = m0 + j*M
        L = lcm(m, m + 1, m + 2)
        step = (4*L) % 840
        # classes reachable along t: 4m - R + step*t mod 840
        base = (4*m - R) % 840
        reach = {(base + step*t) % 840 for t in range(840)}
        todo = (reach & target) - set(hits)
        if not todo: continue
        for t in range(0, 20000):
            c = (base + step*t) % 840
            if c not in todo or c in hits: continue
            a = m + t*L; p = 4*a - R
            if isprime(p) and verify_L_path(p, a, m, 2):
                hits[c] = p
                todo.discard(c)
                if not todo: break
print("covered", len(set(hits) & target), "of", len(target), "unit classes mod 840 with c = 2 mod 3")
print("largest least witness found:", max(hits.values()) if hits else None)
