# Replicates the partial pass's C2 'min member coordinates' check and classifies its failures by orbit-table row.
from math import gcd
from sympy import divisors, isprime
def hits(p, jmax):
    h = (p - 1)//12; out = []
    for j in range(jmax):
        a = 3*h + j + 1; R = 4*j + 3
        for A0 in divisors(a):
            for B0 in divisors(a//A0):
                if gcd(A0, B0) != 1: continue
                for eps in (0, 1):
                    if (A0 + p**(1 - eps)*B0) % R == 0: out.append((A0, j, B0, eps))
    return out
def code(rec, J, M):
    A0, j, B0, eps = rec; Lam = 2*J*M
    return (A0 - 1)*Lam + 2*M*j + 2*(B0 - 1) + eps
fails = {}; tot = {}
for p in range(13, 2500, 12):
    if not isprime(p): continue
    h = (p - 1)//12
    for (J, M) in [(3*h, 6*h), (6*h, 9*h)]:
        H = hits(p, J)
        for x in H:
            A0, j, B0, eps = x; R = 4*j + 3; mem = {x}
            for (s, t) in [(1, 0), (0, 1), (1, 1)]:
                al, be = (A0, B0) if s == 0 else (B0, A0); eta = eps ^ t
                if (al + p**(1 - eta)*be) % R == 0: mem.add((al, j, be, eta))
            if (p - 1) % R == 0: key = "R|p-1"
            elif (p*p - 1) % R == 0: key = "R|p^2-1 only"
            elif eps == 1: key = "else eps=1"
            else: key = "else eps=0"
            tot[key] = tot.get(key, 0) + 1
            mn = min(mem, key=lambda z: code(z, J, M))
            if not (mn[0] == min(A0, B0) and mn[2] == max(A0, B0)):
                k2 = key + (" (A>B, one-point orbit)" if (len(mem) == 1 and A0 > B0) else " (other)")
                fails[k2] = fails.get(k2, 0) + 1
print("hits per row:", tot); print("failures:", fails)
