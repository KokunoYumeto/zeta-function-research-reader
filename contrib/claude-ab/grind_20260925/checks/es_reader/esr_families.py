# claude-ab: independent check of the archive's Theorem "Four unconditional parameterized denominator families"
import sympy as sp
k = sp.symbols('k', integer=True, nonnegative=True)
g1, g2 = 31*k+30, 31*k+15
m3, m4 = 23*k+15, 23*k+19
w3, w4 = 1116*k+727, 4464*k+3683
rows = []
n1 = 248*k+209; rows.append((n1, 2*g1, 2*n1*(k+1), 2*n1*g1*(k+1)))
n2 = 248*k+89;  rows.append((n2, 2*g2, n2*(2*k+1), 2*n2*g2*(2*k+1)))
n3 = 17112*k+11137; rows.append((n3, 186*m3, 12*n3*m3*w3, 124*m3*w3))
n4 = 17112*k+14113; rows.append((n4, 186*m4, 6*n4*m4*w4, 31*m4*w4))
ok = True
for i,(n,a,b,c) in enumerate(rows,1):
    e = sp.expand(4*a*b*c - n*(b*c + a*c + a*b))
    print(f"row {i}: n = {n}; 4abc - n(bc+ac+ab) = {e}")
    ok &= (e == 0)
# numeric spot check with exact fractions for k = 0..200
from fractions import Fraction as F
for kv in range(201):
    for (n,a,b,c) in rows:
        N,A,B,C = [int(x.subs(k,kv)) for x in (n,a,b,c)]
        ok &= (A>0 and B>0 and C>0 and F(4,N) == F(1,A)+F(1,B)+F(1,C))
# the four progressions: are they contained in the classical Mordell-covered classes? (n mod 840, and gcd info)
for (n,_,_,_) in rows:
    print("progression", n, "residues mod 840 of first 6 terms:", sorted({int(n.subs(k,kv))%840 for kv in range(6)}), "; mod 24:", sorted({int(n.subs(k,kv))%24 for kv in range(24)}))
# every progression meets all six hard classes mod 840 (gcd(248,840) = 8, gcd(17112,840) = 24), with primes in each
from math import gcd
hard = [1, 121, 169, 289, 361, 529]
for (n,_,_,_) in rows:
    A, B = int(n.coeff(k)), int(n.subs(k, 0))
    hits = sorted({(A*kv + B) % 840 for kv in range(840)} & set(hard))
    least = []
    for h in hard:
        kv = 0
        while not ((A*kv + B) % 840 == h and sp.isprime(A*kv + B)):
            kv += 1
        least.append((h, A*kv + B))
    print("progression", n, ": gcd with 840 =", gcd(A, 840), "; hard classes met:", hits, "; gcd(A,B) =", gcd(A, B), "; least prime per class:", least)
    ok &= (hits == hard and gcd(A, B) == 1)
print("ALL PASS" if ok else "FAIL")
