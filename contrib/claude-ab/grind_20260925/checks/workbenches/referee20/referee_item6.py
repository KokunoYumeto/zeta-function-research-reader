import sympy as sp, math, time
from fractions import Fraction as Fr
T0=time.time()
p = 87481
print("p prime:", sp.isprime(p), " p mod 840 =", p % 840, " p mod 4 =", p % 4)
lo, hi = p//4 + 1, (p - 1)//2   # p/4 < a < p/2
nsh = 0; nonpos = 0; occ = 0; maxL = None
for a in range(lo, hi + 1):
    R = 4*a - p
    fa = sp.factorint(a)
    tau = math.prod(e + 1 for e in fa.values())
    divs_a = sp.divisors(a)
    res = {}
    for d in divs_a:
        for dd in (d, p*d):
            r = dd % R; res[r] = res.get(r, 0) + 1
    E = sum(c*c for c in res.values())
    L = Fr(8*tau*tau, sp.totient(R)) - E
    nsh += 1
    if L <= 0: nonpos += 1
    if maxL is None or L > maxL: maxL = L
    # occupancy: E_a or M_a nonempty (divisors of a^2)
    ds = [1]
    for q, e in fa.items(): ds = [x*q**k for x in ds for k in range(2*e + 1)]
    if any((4*u + 1) % R == 0 or (u + a) % R == 0 for u in ds): occ += 1
print("first-half shells:", nsh, " L_a <= 0 on:", nonpos, " max L_a:", maxL, " occupied shells:", occ)
print(f"{time.time()-T0:.1f}s")
