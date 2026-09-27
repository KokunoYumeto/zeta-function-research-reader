from sympy import primerange, divisors, factorint, isprime
from fractions import Fraction as F
def EM(p, a):
    R = 4*a - p
    D = divisors(a*a)
    return [u for u in D if (4*u+1) % R == 0], [u for u in D if (u + a) % R == 0]
def P12(a):
    f = factorint(a); P1 = P2 = 1
    for l, v in f.items():
        if l % 3 == 1: P1 *= 2*v+1
        elif l % 3 == 2: P2 *= 2*v+1
    return P1, P2
bad = 0; n = 0
for p in primerange(5, 200000):
    if p % 4 != 1: continue
    a = (p+3)//4; E, M = EM(p, a); P1, P2 = P12(a)
    if p % 12 == 1:
        n += 1
        if not (sorted(E) == sorted(M) == sorted(u for u in divisors(a*a) if u % 3 == 2)): bad += 1
        if not (len(E) == len(M) == P1*(P2-1)//2): bad += 1
        if (len(E) + len(M) > 0) != any(l % 3 == 2 for l in factorint(a)): bad += 1
        if (P2 - 1) % 4: bad += 1
    else:  # p = 5 mod 12
        if not (len(E) == P1*(P2-1)//2 and len(M) == P1*(P2+1)//2 and 1 in M): bad += 1
        if (3*P2 - 1) % 4: bad += 1
print("Prop 3.2 (and p=5 mod 12 extension) for p<2e5: p=1 mod 12 count", n, "mismatches", bad)

# Prop 3.3 for all p = 1 mod 4 below 2e5
def crit7(a):
    f = factorint(a)
    if any(l % 7 in (5, 6) for l in f): return True
    n3 = sum(v for l, v in f.items() if l % 7 == 3)
    n24 = sum(v for l, v in f.items() if l % 7 in (2, 4))
    return n3 >= 3 or (n3 >= 1 and n24 >= 1)
bad = 0
for p in primerange(5, 200000):
    if p % 4 != 1: continue
    a = (p+7)//4
    E, M = EM(p, a)
    if (len(E)+len(M) > 0) != crit7(a): bad += 1
print("Prop 3.3 for all p = 1 mod 4 below 2e5: mismatches", bad)

# Prop 3.4 and the stronger mod-840 statement
surv = []; bad = 0
for p in primerange(13, 10**6):
    if p % 12 != 1: continue
    a3, a7 = (p+3)//4, (p+7)//4
    empty = (not any(l % 3 == 2 for l in factorint(a3))) and (not crit7(a7))
    char = (p % 24 == 1 and all(l % 3 == 1 for l in factorint(a3)) and all(l % 7 in (1, 2, 4) for l in factorint(a7)))
    if empty != char: bad += 1
    if empty: surv.append(p)
print("Prop 3.4 criterion mismatches below 1e6:", bad, "; survivors:", len(surv), "first:", surv[:5])
hard = {1, 121, 169, 289, 361, 529}
print("survivors mod 168:", sorted({p % 168 for p in surv}), "; mod 840:", sorted({p % 840 for p in surv}),
      "; all hard:", all(p % 840 in hard for p in surv))
for c in sorted(hard):
    print("  least survivor in class", c, ":", next(p for p in surv if p % 840 == c))
# Prop 3.5 identities on all n = 1 mod 24 (not only primes) below 3e5, non-square mod 840
cnt = 0; bad = 0
for n in range(1, 300000, 24):
    if n == 1: continue
    t = None
    if n % 7 == 3: t = (1, 2, 7)
    elif n % 7 == 5: t = (2, 1, 7)
    elif n % 7 == 6: t = (1, 1, 7)
    elif n % 5 == 2: t = (1, 2, 15)
    elif n % 5 == 3: t = (2, 1, 15)
    if t is None: continue
    A, B, R = t
    if (n + R) % (4*A*B) or (A + n*B) % R: bad += 1; continue
    D = (n + R)//(4*A*B); C = (A + n*B)//R
    cnt += 1
    if F(4, n) != F(1, A*B*D) + F(1, A*C*D) + F(1, n*B*C*D): bad += 1
print("Prop 3.5 identities on all integers n = 1 mod 24 below 3e5 in its classes (composites included):", cnt, "checked, bad", bad)
