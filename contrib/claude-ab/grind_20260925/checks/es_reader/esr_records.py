# claude-ab: independent replay of the strict-record prefix (Ionascu-Wilson classes C_i, h(p)) through 8,803,369 and h(806521)
import numpy as np, sys
N = 8_803_369 + 10
# primes up to N
sieve = np.ones(N+1, dtype=bool); sieve[:2] = False
for i in range(2, int(N**0.5)+1):
    if sieve[i]: sieve[i*i::i] = False
primes = np.nonzero(sieve)[0]
# smallest prime factor up to N//4 + 200 for a = (p+R)/4
M = N//4 + 400
spf = np.zeros(M+1, dtype=np.int64)
for i in range(2, M+1):
    if spf[i] == 0:
        spf[i::i] = np.where(spf[i::i]==0, i, spf[i::i])
def factor(n):
    f = {}
    while n > 1:
        q = int(spf[n]); e = 0
        while n % q == 0: n //= q; e += 1
        f[q] = e
    return f
def occupied(p, R):
    # shell a = (p+R)/4 (p = 1 mod 4, R = 3 mod 4); need u | a^2 with u = -4^{-1} (mod R) or u = -a (mod R)
    a = (p + R)//4
    f = factor(a)
    res = {1 % R}
    for q, e in f.items():
        powers = [pow(q, k, R) for k in range(2*e+1)]
        res = {(x*y) % R for x in res for y in powers}
    t1 = (-pow(4, -1, R)) % R
    t2 = (-a) % R
    return (t1 in res) or (t2 in res)
def h(p):
    if p == 2: return 1
    if p % 4 == 3: return 1
    i = 1
    while True:
        R = 4*i - 1
        if occupied(p, R): return i
        i += 1
records = []; best = 0; hs = {}
for p in primes:
    p = int(p)
    hp = h(p)
    if p in (118801, 806521): hs[p] = hp
    if hp > best:
        best = hp; records.append((p, hp, 4*hp-1))
print("strict records (p, h, R):", records)
print("h(118801) =", hs.get(118801), " h(806521) =", hs.get(806521))
print("number of records:", len(records), "; odd records:", len(records)-1)
