#!/usr/bin/env python3
"""Referee checks for note 45 (Erdos 817). Independent code, exact integers (floats only for display)."""
import math, itertools, time
from fractions import Fraction as Fr
import mpmath as mp
T0 = time.time()
def out(*a): print(*a, flush=True)
mp.mp.dps = 30

def H(A):
    S = 1
    for a in A: S |= S << a
    return S          # bitset of subset sums
def members(S):
    out_ = []; i = 0
    while S:
        if S & 1: out_.append(i)
        S >>= 1; i += 1
    return out_
def has_int_kap(S, k, maxsum):
    for d in range(1, maxsum // (k - 1) + 1):
        T = S
        for j in range(1, k): T &= S >> (j*d)
        if T: return True
    return False
def has_mod_kap(vals, k, q):
    R = {v % q for v in vals}
    for x in R:
        for d in range(1, q):
            if all((x + j*d) % q in R for j in range(1, k)): return True
    return False

# decimals quoted in 45
out("19^(1/3) =", mp.nstr(mp.cbrt(19), 8))
out("97^(1/6) =", mp.nstr(mp.root(97, 6), 8), " 93^(1/6) =", mp.nstr(mp.root(93, 6), 8), " (note: 2.1435, 2.1277)",
    " 1651^(1/10) =", mp.nstr(mp.root(1651, 10), 8))
out("2.1277^6 =", mp.nstr(mp.mpf('2.1277')**6, 8), " 2.1285^6 =", mp.nstr(mp.mpf('2.1285')**6, 8))
out("Korsky-type rates: 5^(2/3) =", mp.nstr(mp.mpf(5)**(mp.mpf(2)/3), 6), " sqrt5 =", mp.nstr(mp.sqrt(5), 6),
    " 7^(2/5) =", mp.nstr(mp.mpf(7)**(mp.mpf(2)/5), 6))
def korsky_rate(k):
    best = None
    for p in [3, 5, 7, 11, 13, 17, 19, 23]:
        qpk = min(p, k) - 1
        r = mp.mpf(p)**(mp.mpf(2)/qpk)
        if best is None or r < best[0]: best = (r, p)
    return best
for k in (4, 5, 6):
    r, p = korsky_rate(k); out(f"  min_p p^(2/(min(p,k)-1)) for k={k}: {mp.nstr(r, 6)} at p={p}")
out("0.315 constant: sqrt(19/192) =", mp.nstr(mp.sqrt(mp.mpf(19)/192), 6),
    "; with r=1,2 factors (3/19^(1/3))^r:", [mp.nstr(mp.sqrt(mp.mpf(19)/192)*(3/mp.cbrt(19))**r, 5) for r in (1, 2)])

# Theorem 45.6 algebra: f_{m+3} - 19 f_m and 16/19 - kappa_m
ok = all((3**(m+3) - 2**(m+3)) - 19*(3**m - 2**m) == 8*3**m + 11*2**m for m in range(0, 60))
ok2 = all(Fr(16, 19) - Fr(8*3**m - 3*2**m, 12*(3**m - 2**m)) == Fr(5*(8*3**m - 27*2**m), 228*(3**m - 2**m)) for m in range(1, 60))
out("f_{m+3}-19f_m = 8*3^m+11*2^m:", ok, "; 16/19 - kappa_m identity:", ok2)
# min of 19^a 3^b over 3a+b=n is 19^q 3^r
okmin = all(min(19**a * 3**(n - 3*a) for a in range(n//3 + 1)) == 19**(n//3) * 3**(n % 3) for n in range(1, 60))
out("min 19^a 3^b over 3a+b=n equals M_n:", okmin)
# refined bound table 1,3,5,11,27,49 (smallest N with 19(M^2-1) <= 192 * sum_{j<n}(N-j)^2)
tab = []
for n in range(1, 7):
    M = 19**(n//3) * 3**(n % 3)
    N = n
    while 19*(M*M - 1) > 192*sum((N - j)**2 for j in range(n)): N += 1
    tab.append(N)
out("refined EP-03 bound table n<=6:", tab, "(note: 1, 3, 5, 11, 27, 49)")

# certificates
Bs = [1, 4, 5, 17, 21, 22]; HB = members(H(Bs))
out("B*: S =", sum(Bs), "|H| =", len(HB), "; mod 97 no 5-AP:", not has_mod_kap(HB, 5, 97),
    "; mod 93 no 6-AP:", not has_mod_kap(HB, 6, 93))
Ash = [3, 4, 7, 34, 37, 41, 216, 250, 253, 257]; HA = members(H(Ash))
marks = [0, 4, 7, 41, 257]
out("A#: distances =", sorted(b - a for a, b in itertools.combinations(marks, 2)) == Ash, " S =", sum(Ash), " 13*127 =", 13*127,
    " |H| =", len(HA), " mod 1651 no 6-AP:", not has_mod_kap(HA, 6, 1651),
    " integer 5-AP 0..1028:", all(257*j in set(HA) for j in range(5)))
# Proposition 45.9 on random distinct-distance rulers
import random; random.seed(7)
okr = 0; tested = 0
while tested < 200:
    m = random.randint(3, 7)
    t = sorted(random.sample(range(1, 400), m - 1)); t = [0] + t
    dist = [b - a for a, b in itertools.combinations(t, 2)]
    if len(set(dist)) != len(dist): continue
    tested += 1
    S = set(members(H(dist))); L = t[-1]
    if all(j*L in S for j in range(m)): okr += 1
out(f"Prop 45.9 on {tested} random distinct-distance rulers: m-term AP 0,L,...,(m-1)L present in {okr}")

# negative result 5: (0,1,5,22) cannot be extended to a 6-admissible five-mark ruler (z from 23 to 3000)
base = [0, 1, 5, 22]
ext_ok = []
for z in range(23, 3001):
    t = base + [z]
    dist = [b - a for a, b in itertools.combinations(t, 2)]
    if len(set(dist)) != len(dist): continue
    S = H(dist)
    if not has_int_kap(S, 6, sum(dist)): ext_ok.append(z)
out("(0,1,5,22,z) with distinct distances and 6-AP-free subset sums, 23<=z<=3000:", ext_ok[:10], "count", len(ext_ok))

# g4(7) witness and the composition example
W7 = [1, 3, 39, 180, 219, 243, 246]
out("g4(7) witness admissible:", not has_int_kap(H(W7), 4, sum(W7)), " max =", max(W7))
W6 = [2, 29, 45, 74, 77, 79]
S6 = H(W6)
T6 = set()
for x in itertools.product(range(3), repeat=6): T6.add(sum(c*a for c, a in zip(x, W6)))
out("optimal 6-set admissible:", not has_int_kap(S6, 4, sum(W6)), " |T| =", len(T6), " M_6 = 361; blocks 29+45=74:", 29 + 45 == 74, " 2+77=79:", 2 + 77 == 79)
# Corollary 45.5 and Theorem 45.1 lower bounds against the exact values
exact = {1: 1, 2: 3, 3: 5, 4: 14, 5: 40, 6: 79}
for n, g in exact.items():
    lb1 = (19**(Fr(n, 3)) if n % 3 == 0 else None)
    lo = math.ceil((mp.mpf(19)**(mp.mpf(n)/3) - 1)/(2*n))
    lo2 = math.ceil((mp.mpf(19)**(mp.mpf(n)/3) + n*(n - 1) - 1)/(2*n))
    up = 8*19**(math.ceil(n/3) - 1)
    assert lo <= g <= up and lo2 <= g
out("Theorem 45.1 / Cor 45.5 bounds consistent with exact g4(1..6): True")
out(f"total {time.time()-T0:.1f}s")
