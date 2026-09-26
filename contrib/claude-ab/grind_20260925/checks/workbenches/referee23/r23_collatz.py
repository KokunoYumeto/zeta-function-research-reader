#!/usr/bin/env python3
"""Referee 23: independent checks of the Collatz passages (Section 2) of the workbench reader.
Own code from the definitions; no author or workbench code imported."""
import sys, math, random, time
from fractions import Fraction as Fr
import mpmath as mp
mp.mp.dps = 120
t0 = time.time()
def say(tag, ok, msg=""):
    print(("[PASS] " if ok else "[FAIL] ") + tag + (": " + msg if msg else "")); sys.stdout.flush()

L3 = mp.log(3, 2)
# ---------------------------------------------------------------- continued fraction of log2 3 and upper best approximations
def cf(x, n):
    out = []
    for _ in range(n):
        a = int(mp.floor(x)); out.append(a); x = 1 / (x - a)
    return out
a = cf(L3, 40)
print("CF of log2 3:", a[:25])
# convergents p_k/q_k
P = [1, a[0]]; Q = [0, 1]
for k in range(1, len(a)):
    P.append(a[k] * P[-1] + P[-2]); Q.append(a[k] * Q[-1] + Q[-2])
conv = list(zip(P[1:], Q[1:]))  # (p_k, q_k), k = 0..
# upper best approximations = semiconvergents above log2 3: for odd k, (p_{k-1} + t p_k)/(q_{k-1}+t q_k), t = 1..a_{k+1}
ups = []
for k in range(len(conv) - 1):
    pk, qk = conv[k]
    if mp.mpf(pk) / qk > L3:  # upper convergent
        # intermediate fractions between this and the next upper convergent
        pass
# simpler: generate upper best approximations directly by the standard algorithm
def upper_best(alpha, count):
    """successive fractions p/q > alpha such that no fraction with smaller denominator lies in (alpha, p/q]"""
    res = []
    # start with ceil(alpha)/1
    p, q = int(mp.ceil(alpha)), 1
    res.append((p, q))
    # lower neighbour: floor(alpha)/1 ; mediant walk (Stern-Brocot) toward alpha from both sides
    lp, lq = int(mp.floor(alpha)), 1
    up, uq = p, q
    while len(res) < count:
        mp_, mq = lp + up, lq + uq
        if mp.mpf(mp_) / mq > alpha:
            up, uq = mp_, mq; res.append((up, uq))
        else:
            lp, lq = mp_, mq
    return res
UB = upper_best(L3, 80)
UBd = {q: p for p, q in UB}
print("upper best approximations (last few with q < 1e12):", [(p, q) for p, q in UB if q < 10**12][-6:])

def least_den(s):
    """least-denominator fraction in (log2 3, log2(3+1/s)]; s may be an mpf/int/Fraction"""
    beta = mp.log(3 + 1 / mp.mpf(s), 2)
    for p, q in UB:
        if mp.mpf(p) / q <= beta:
            return p, q
    return None

# ---------------------------------------------------------------- Theorem 2.8 exactly with integers
s = 330751
mstar = None
for m in range(1, 5000):
    A = (3**m).bit_length()           # least A with 2^A > 3^m
    if (2**A) * s**m <= (3 * s + 1)**m:  # 2^A <= (3+1/s)^m
        mstar = (m, A); break
m, A = mstar
# k bound: (4s)^m <= 2^k (3s+1)^m  -> least k
k = 0
while (4 * s)**m > 2**k * (3 * s + 1)**m:
    k += 1
say("Thm 2.8: least m with a power of 2 in (3^m,(3+1/s)^m], s=330751, exact integers; A > m log2 3; least k",
    m == 1636 and A == 2593 and k == 679, f"m={m}, A={A}, k>={k}, m*log2(3)={mp.nstr(m*L3, 15)}")
print("   least-denominator routine at s=330751:", least_den(330751))

# ---------------------------------------------------------------- the 2^33 consequence
s33 = 2**33 + 1
pq = least_den(s33)
m33 = pq[1]; A33 = pq[0]
kb = m33 * (2 - mp.log(3 + mp.mpf(1) / s33, 2))
say("2^33 consequence: least denominator for s = 2^33+1 is 301994/190537, and k >= 79,080", pq == (301994, 190537) and math.ceil(kb) == 79080,
    f"fraction {pq}, k-bound {mp.nstr(kb, 15)}")
# which range of s gives this fraction
def srange(p, q):
    # fraction p/q is the least-denominator one for s in (s_lo, s_hi]; s_hi = 1/(2^{p/q}-3); s_lo from previous upper best approx
    i = [j for j, (pp, qq) in enumerate(UB) if (pp, qq) == (p, q)][0]
    pp, qq = UB[i - 1]
    return 1 / (mp.power(2, mp.mpf(pp) / qq) - 3), 1 / (mp.power(2, mp.mpf(p) / q) - 3)
lo, hi = srange(301994, 190537)
print(f"   301994/190537 is the least-denominator fraction for s in ({mp.nstr(lo, 8)}, {mp.nstr(hi, 8)}] = (2^{mp.nstr(mp.log(lo,2),6)}, 2^{mp.nstr(mp.log(hi,2),6)}]")

# ---------------------------------------------------------------- Corollary 2.9
p9, q9 = 114208327604, 72057431991
lo, hi = srange(p9, q9)
prev = UB[[j for j, (pp, qq) in enumerate(UB) if (pp, qq) == (p9, q9)][0] - 1]
say("Cor 2.9: previous upper best approximation is 10439860591/6586818670", prev == (10439860591, 6586818670), str(prev))
say("Cor 2.9: s_lo = 2.1689015534e20 ~ 2^67.556, s_hi = 4.3585e21 ~ 2^71.884",
    mp.nstr(lo, 11) == '2.1689015534e+20' and mp.nstr(hi, 5) == '4.3585e+21', f"s_lo={mp.nstr(lo, 14)} (2^{mp.nstr(mp.log(lo,2),8)}), s_hi={mp.nstr(hi, 14)} (2^{mp.nstr(mp.log(hi,2),8)})")
say("Cor 2.9: hypothesis bound 2.17e20 exceeds s_lo, and 2^68 > 2.17e20", mp.mpf('2.17e20') > lo and 2**68 > 2.17e20)
for s in (mp.mpf('2.17e20'), mp.mpf(2)**68, mp.mpf(2)**71, mp.mpf(2)**40, lo * (1 + mp.mpf(10)**-30), lo * (1 - mp.mpf(10)**-30)):
    print(f"   s = {mp.nstr(s, 10)}: least-denominator fraction {least_den(s)}")
Ab = q9 * L3
say("Cor 2.9: 72057431991*log2 3 = 114208327603.99999999999...", mp.nstr(Ab, 25).startswith('114208327603.99999999999'), mp.nstr(Ab, 25))
kb9 = Fr(q9) * (2 - Fr(10439860591, 6586818670))
say("Cor 2.9: 72057431991*(2 - 10439860591/6586818670) = 29906536377.99..., so k >= 29,906,536,378", math.floor(kb9) == 29906536377 and math.ceil(kb9) == 29906536378,
    f"{float(kb9):.6f}")
say("Cor 2.9: 2m - A at the minimal pair = 29906536378 ; A+m = 186265759595", 2 * q9 - p9 == 29906536378 and p9 + q9 == 186265759595)
# at s_lo exactly, log2(3+1/s_lo) = 10439860591/6586818670 ; proof uses k >= m*(2 - log2(3+1/s)) with s > s_lo -> strictly larger
print(f"   Eliahou check: least-denominator fraction at s=2^40: {least_den(mp.mpf(2)**40)} (Eliahou: 17,087,915)")
# Oliveira e Silva-type range 20*2^58
print(f"   at s=20*2^58: {least_den(20*mp.mpf(2)**58)}")

# ---------------------------------------------------------------- Proposition 2.1 exact count and strict bound
random.seed(23)
ok = True
for _ in range(3000):
    A_ = random.randint(1, 14); M = 2**A_; N = random.randint(1, 4000); b = random.randint(0, 10**6); h = random.randint(0, M - 1)
    c = sum(1 for k_ in range(b, b + N) if (k_ - h) % M == 0)
    c2 = (b + N - 1 - h) // M - (b - 1 - h) // M
    if c != c2 or c not in (N // M, -(-N // M)): ok = False
    if abs(Fr(c, N) - Fr(1, M)) > Fr(M - 1, M * N): ok = False
say("Prop 2.1: count formula, floor/ceil, |P(w)-2^-A| <= (1-2^-A)/N (3000 random cases)", ok)
# cylinder claim itself: odd n=2k+1 has word w iff k = h_w mod 2^A -- test all words of small A
def word(n, m):
    w = []
    x = n
    for _ in range(m):
        y = 3 * x + 1; e = (y & -y).bit_length() - 1; w.append(e); x = y >> e
    return tuple(w)
ok = True
for m in (1, 2, 3, 4):
    classes = {}
    for k_ in range(0, 2**13):
        w = word(2 * k_ + 1, m)
        A_ = sum(w)
        if A_ > 11: continue
        classes.setdefault(w, set()).add(k_ % 2**A_)
    if any(len(v) != 1 for v in classes.values()): ok = False
say("Prop 2.1 cylinder: each word with A<=11 (m<=4) is one class of k mod 2^A (k<2^13)", ok)

# ---------------------------------------------------------------- Theorem 2.2(a) for H < m as well, and the (c) inequalities
def Q(m, H):  # Pr(Bin(H,1/2) <= m-1)
    return Fr(sum(math.comb(H, i) for i in range(0, min(m - 1, H) + 1)), 2**H) if m >= 1 else Fr(0)
def exact_delta(N, b, m):
    cnt = {}
    for k_ in range(b, b + N):
        w = word(2 * k_ + 1, m); cnt[w] = cnt.get(w, 0) + 1
    return 1 - sum(min(Fr(c, N), Fr(1, 2**sum(w))) for w, c in cnt.items())
ok = True; nn = 0
for (N, b) in ((2**10, 0), (2**10, 12345), (3000, 777), (2**12, 99), (5000, 10**7)):
    for m in range(1, 16):
        D = exact_delta(N, b, m)
        for H in range(0, 40):
            lo_ = max(Fr(0), Q(m, H) - Fr(N, 2**(H + 1)))
            hi_ = min(Fr(1), Q(m, H) + Fr(math.comb(H, m), N))
            nn += 1
            if not (lo_ <= D <= hi_): ok = False
say("Thm 2.2(a) sandwich holds for EVERY H >= 0 (also H < m, where Q=1 and binom(H,m)=0)", ok, f"{nn} (N,b,m,H) cases with exact Delta")
# the (c) bounds on exact Delta at moderate N (sanity) and the workbench's (4.3)/(4.4) forms
ok = True; nc = 0
for (N, b) in ((2**12, 5), (2**14, 1000), (2**14, 0)):
    Lg = math.log2(N)
    for m in range(1, 16):
        D = float(exact_delta(N, b, m))
        for d in [x / 100 for x in range(1, 51)]:
            if m <= (0.5 - d) * Lg and d * Lg >= 1:
                nc += 1
                if D > 2 * N ** (-d * d / (2 * math.log(2))): ok = False
                if D > N ** (-d) + N ** (-d * d / (2 * math.log(2))): ok = False   # workbench (4.3)
            if m >= (0.5 + d) * Lg and d * Lg >= 2 and d <= 0.5:
                nc += 1
                if 1 - D > 2 * N ** (-d * d / (16 * math.log(2))): ok = False
                H = math.ceil((1 + d) * Lg)
                if 1 - D > 0.5 * N ** (-d) + math.exp(-2 * (d * Lg / 2 - 0.5) ** 2 / H): ok = False  # workbench (4.4)
say("Thm 2.2(c) reader's bounds and the workbench's (4.3)-(4.4) hold on exact Delta", ok, f"{nc} cases")
# the workbench's (4.4) exponent vs the reader's: compare log(1-Delta bound)/log N for large L
for d in (0.1, 0.25, 0.5):
    Lg = 1000.0
    H = math.ceil((1 + d) * Lg)
    wb = max(-d, -2 * (d * Lg / 2 - 0.5) ** 2 / H / math.log(2) / Lg)
    rd = -d * d / (16 * math.log(2))
    print(f"   delta={d}: exponent of N in the workbench's (4.4) ~ {wb:.4f}; in the reader's (c) {rd:.4f}")

# ---------------------------------------------------------------- Proposition 2.5 example and model tail constants
F = Fr(0); coef = 1; Aw = 0
w = (1, 1, 1, 1, 4)
def Fm(x, w):
    for e in w: x = Fr(3 * x + 1, 2**e)
    return x
n0 = None
for n in range(3, 2**(sum(w) + 1) + 3, 2):
    if word(n, 5) == w: n0 = n; break
say("Prop 2.5 example: F_5(3)=235/64, n0=95, F_5(95)=91", Fm(3, w) == Fr(235, 64) and n0 == 95 and Fm(95, w) == 91)
c = mp.sqrt(15) / 4
okt = all(mp.sqrt(2) * c**(h - 1) <= mp.mpf(3) / 2 * (mp.mpf(31) / 32)**h for h in range(1, 2000))
okt &= (Fr(1, 2) * (Fr(31, 20) * Fr(32, 31) + Fr(3, 2)) == Fr(31, 20))
say("tail constants: sqrt2 (sqrt15/4)^(h-1) <= (3/2)(31/32)^h (h=1..1999) and (1/2)((31/20)(32/31)+3/2) = 31/20", okt)
# Prop 2.6 inequality at x >= 2, equality at 7
okc = all(0.5 * (math.sqrt((x - 2) / 2) + math.sqrt((3 * x - 1) / 2)) <= math.sqrt(15) / 4 * math.sqrt(x - 1) + 1e-12 for x in [2 + i / 100 for i in range(0, 5000)])
say("Prop 2.6 inequality on a grid of x in [2,52)", okc)
print(f"elapsed {time.time()-t0:.1f}s")
