import sympy as sp, time
from fractions import Fraction as Fr
T0 = time.time()
p = 7510085481569082811681
print("p prime (BPSW):", sp.isprime(p), " p mod 840:", p % 840, " p mod 24:", p % 24)
found = None
for a in range((p + 3)//4, (p + 3)//4 + 200):
    R = 4*a - p
    if R <= 0: continue
    f = sp.factorint(a, limit=10**7)
    if not all(sp.isprime(q) for q in f):   # incomplete factorisation; skip this shell
        continue
    ds = [1]
    for q, e in f.items(): ds = [x*q**k for x in ds for k in range(2*e + 1)]
    S = p*a
    for u in ds:
        if (4*u + 1) % R == 0:           # exterior: d = p^2 u
            d = p*p*u; y = (d + S)//R; z = (S*S//d + S)//R
            found = (a, y, z, 'E'); break
        if (u + a) % R == 0:             # middle: d = p u
            d = p*u; y = (d + S)//R; z = (S*S//d + S)//R
            found = (a, y, z, 'M'); break
    if found: break
print("first solution found:", found)
if found:
    a, y, z, _ = found
    print("check 1/a+1/y+1/z == 4/p:", Fr(1, a) + Fr(1, y) + Fr(1, z) == Fr(4, p), " shell offset a-(p+3)/4 =", a - (p + 3)//4)
print(f"{time.time()-T0:.1f}s")
