# Referee 21 (wbreader): ES first-two-shell sieves and the 989 two-shell survivors below 10^6,
# computed from the definitions E_a, M_a (divisors of a^2), independent of the author's script.
import math
LIM = 10**6
spf = list(range(LIM//4+10))
for i in range(2, int(len(spf)**0.5)+1):
    if spf[i] == i:
        for j in range(i*i, len(spf), i):
            if spf[j] == j: spf[j] = i
def fac(n):
    f = {}
    while n > 1:
        p = spf[n]; f[p] = f.get(p, 0)+1; n //= p
    return f
def divsq(a):
    ds = [1]
    for p, e in fac(a).items():
        ds = [d*p**k for d in ds for k in range(2*e+1)]
    return ds
sieve = bytearray([1])*LIM; sieve[0]=sieve[1]=0
for i in range(2, int(LIM**0.5)+1):
    if sieve[i]: sieve[i*i::i] = bytearray(len(sieve[i*i::i]))
primes = [p for p in range(13, LIM) if sieve[p] and p % 12 == 1]
bad3 = bad7 = cnt3 = 0; survivors = []
for p in primes:
    h = (p-1)//12
    # R = 3 shell
    a = 3*h+1; R = 4*a-p; D = divsq(a)
    E = [u for u in D if (4*u+1) % R == 0]; M = [u for u in D if (u+a) % R == 0]
    f = fac(a)
    P1 = math.prod(2*e+1 for q, e in f.items() if q % 3 == 1); P2 = math.prod(2*e+1 for q, e in f.items() if q % 3 == 2)
    if not (R == 3 and E == M and len(E) == P1*(P2-1)//2 and (3*P1*(P2-1)) % 4 == 0 and bool(E) == any(q % 3 == 2 for q in f)): bad3 += 1
    occ3 = bool(E or M)
    # R = 7 shell
    a = 3*h+2; R = 4*a-p; D = divsq(a); f = fac(a)
    E = [u for u in D if (4*u+1) % R == 0]; M = [u for u in D if (u+a) % R == 0]
    n3 = sum(e for q, e in f.items() if q % 7 == 3); n24 = sum(e for q, e in f.items() if q % 7 in (2, 4))
    pred = any(q % 7 in (5, 6) for q in f) or n3 >= 3 or (n3 >= 1 and n24 >= 1)
    if not (R == 7 and a % 7 != 0 and bool(E or M) == pred): bad7 += 1
    occ7 = bool(E or M)
    if not occ3 and not occ7: survivors.append(p)
print("primes p=1 mod 12 below 1e6:", len(primes), " R3 failures:", bad3, " R7 failures:", bad7)
print("both shells unoccupied:", len(survivors), " all = 1 mod 24:", all(p % 24 == 1 for p in survivors), " first:", survivors[:3])
# 18 non-square unit classes = 1 mod 24 mod 840
units = [c for c in range(840) if math.gcd(c, 840) == 1]
sq = sorted({c*c % 840 for c in units})
c24 = [c for c in units if c % 24 == 1]
print("unit squares mod 840:", sq, " classes =1 mod 24:", len(c24), " non-square among them:", len([c for c in c24 if c not in sq]))
