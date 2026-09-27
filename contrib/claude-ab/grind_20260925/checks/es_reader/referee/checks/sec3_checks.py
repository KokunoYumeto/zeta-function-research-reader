# Independent referee checks for Section 3 of the ES reader.
from sympy import primerange, divisors, factorint, isprime
from fractions import Fraction as F
from math import gcd

def ordered_pairs_brute(p, a):
    # count ordered (y,z) with 1/a+1/y+1/z = 4/p
    r = F(4, p) - F(1, a)
    if r <= 0: return 0, 0
    cnt = 0; eq = 0
    # y ranges over 1/y < r  and  y <= z  => y <= 2/r ; count unordered then convert
    y = int(1/r) + 1
    while F(2, y) >= r:
        s = r - F(1, y)
        if s > 0 and s.numerator == 1:
            z = s.denominator
            if z >= y:
                if z == y: cnt += 1; eq += 1
                else: cnt += 2
        y += 1
    return cnt, eq

def EM(p, a):
    R = 4*a - p
    D = divisors(a*a)
    E = [u for u in D if (4*u+1) % R == 0]
    M = [u for u in D if (u + a) % R == 0]
    return E, M

# (1) Theorem 3.1(b): pairs with p<260 odd prime, p/4<a<p
n_pairs = 0; n_R1 = 0; bad = 0; n_eq = 0
for p in primerange(3, 260):
    for a in range(p//4 + 1, p):
        E, M = EM(p, a)
        c, eq = ordered_pairs_brute(p, a)
        n_pairs += 1
        if 4*a - p == 1: n_R1 += 1
        if eq: n_eq += 1
        if c != 2*len(E) + len(M): bad += 1
        if (eq > 0) != (4*a - p == 1): bad += 1
print("Thm3.1(b) p<260, p/4<a<p: pairs =", n_pairs, " R=1 cases =", n_R1, " y=z cases =", n_eq, " mismatches =", bad)

n_pairs = 0; bad = 0
for p in primerange(3, 120):
    for a in range(p//4 + 1, 3*p + 1):
        if a % p == 0: continue
        E, M = EM(p, a)
        c, eq = ordered_pairs_brute(p, a)
        n_pairs += 1
        if c != 2*len(E) + len(M): bad += 1
print("Thm3.1(b) p<120, p/4<a<=3p, p!|a: pairs =", n_pairs, " mismatches =", bad)

# shells counts for p = 1 mod 12 below 700 and 1000 (shells 3h+1..9h)
for B in (700, 1000):
    s1 = sum(9*((p-1)//12) - 3*((p-1)//12) for p in primerange(13, B) if p % 12 == 1)
    s2 = sum(len(range(p//4+1, p)) for p in primerange(13, B) if p % 12 == 1)
    print(f"shells for p=1 mod 12 below {B}: [3h+1,9h] count = {s1}; (p/4,p) count = {s2}")

# (a): all solutions at odd primes below 400
def all_solutions(p):
    sols = []
    for x in range(p//4 + 1, 3*p//4 + 1):
        r = F(4, p) - F(1, x)
        if r <= 0: continue
        y = max(x, int(1/r) + 1)
        while F(2, y) >= r:
            s = r - F(1, y)
            if s > 0 and s.numerator == 1 and s.denominator >= y:
                sols.append((x, y, s.denominator))
            y += 1
    return sols
tot = 0; badA = 0
for p in primerange(3, 400):
    for (x, y, z) in all_solutions(p):
        tot += 1
        exc = (p % 4 == 3 and (x, y, z) == ((p+1)//2, (p+1)//2, p*(p+1)//4))
        if not (F(p, 4) < x <= F(3*p, 4)): badA += 1
        if not exc and not (2*x < p and x < y): badA += 1
print("Thm3.1(a): solutions (x<=y<=z) at odd primes below 400 =", tot, " violations =", badA)

# every p = 1 mod 12 below 30000 has an occupied shell in (p/4, p/2)
miss = [p for p in primerange(13, 30000) if p % 12 == 1 and not any(sum(map(len, EM(p, a))) for a in range(p//4+1, (p+1)//2))]
print("p=1 mod 12 below 30000 with no occupied shell:", miss)

# prime counts
print("#p=1 mod 12 < 2e5:", sum(1 for p in primerange(2, 200000) if p % 12 == 1),
      " < 1e6:", sum(1 for p in primerange(2, 10**6) if p % 12 == 1),
      " #p=1 mod 4 < 3e4:", sum(1 for p in primerange(2, 30000) if p % 4 == 1))
