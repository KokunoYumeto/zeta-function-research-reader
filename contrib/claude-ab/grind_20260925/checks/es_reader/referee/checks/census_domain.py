from sympy import primerange, factorint
def occ(p, R):
    a = (p + R)//4; res = {1 % R}
    for q, e in factorint(a).items():
        pw = [pow(q, k, R) for k in range(2*e + 1)]
        res = {(x*y) % R for x in res for y in pw}
    return ((-pow(4, -1, R)) % R in res) or ((-a) % R in res)
from collections import Counter
c = Counter(); c3 = Counter(); n = 0
for p in primerange(2, 3*10**6):
    if p % 24 != 1: continue
    if not occ(p, 7) and not occ(p, 11):
        n += 1; c[p % 72] += 1
        c3[(p % 72, occ(p, 3))] += 1
print("primes p = 1 mod 24 below 3e6 with R=7 and R=11 shells both empty:", n, "; residues mod 72:", dict(c))
print("split by R=3 occupancy (residue mod 72, R3 occupied):", dict(c3))
