#!/usr/bin/env python3
"""Independent check of chapter 1 (history_law_cutoff_20260914/RESEARCH_NOTE.md):
exact cylinders (Lemma 2.1), interval counts (2.1)-(2.2), TV sandwich (3.2), rounding
refinement (3.3), support bound (3.4), dyadic identity (3.5), descent counter (6.1) and a
numerical look at the Gaussian window (4.1). No workbench code imported."""
import sys, time, math, random
from fractions import Fraction
from math import comb
t0 = time.time()
def v2(x): return (x & -x).bit_length() - 1
def word(n, m):
    w = []
    for _ in range(m):
        x = 3 * n + 1; a = v2(x); w.append(a); n = x >> a
    return tuple(w)
def fail(msg): print('FAIL', msg); sys.exit(1)
out = []
def Bw(w):
    m = len(w); A = 0; B = 0
    for j in range(m):
        B += 3 ** (m - 1 - j) * 2 ** A; A += w[j]
    return B, A
rcache = {}
def r_h(w):
    if w in rcache: return rcache[w]
    B, A = Bw(w); m = len(w); M = 2 ** (A + 1)
    r = ((2 ** A - B) * pow(3 ** m, -1, M)) % M
    if r % 2 == 0: fail('r even')
    rcache[w] = (r, (r - 1) // 2, A); return rcache[w]

# Lemma 2.1 on all odd n < 2^20, m = 1..6
c = 0
for n in range(1, 1 << 20, 2):
    j = (n - 1) // 2
    for m in (1, 3, 6):
        w = word(n, m); r, h, A = r_h(w)
        if (j - h) % (2 ** A): fail('Lemma 2.1 n=%d m=%d' % (n, m))
        c += 1
out.append('Lemma 2.1 (exact cylinder j = h_w mod 2^A): %d (n,m) cases, all odd n<2^20, m in {1,3,6}: PASS' % c)

def law(N, b, m):
    P = {}
    for j in range(b, b + N):
        w = word(2 * j + 1, m); P[w] = P.get(w, 0) + 1
    return P
def Q(m, H): return Fraction(sum(comb(H, j) for j in range(0, min(m - 1, H) + 1)), 2 ** H)
def K(m, H): return comb(H, m) if H >= m else 0
def TV(P, N):  # exact half-L1 distance to G_m; words outside supp P contribute G mass
    s = Fraction(0)
    for w, cnt in P.items():
        s += min(Fraction(cnt, N), Fraction(1, 2 ** sum(w)))
    return 1 - s
ncount = 0; nsand = 0; ndy = 0
cases = [(N, b, m) for N in (1, 5, 37, 256, 1000, 4096) for b in (0, 17, 10 ** 30 + 3) for m in (1, 2, 4, 7)]
for (N, b, m) in cases:
    P = law(N, b, m)
    for w, cnt in P.items():
        r, h, A = r_h(w); M = 2 ** A
        C = (b + N - 1 - h) // M - (b - 1 - h) // M
        if C != cnt: fail('count (2.1)')
        if abs(Fraction(cnt, N) - Fraction(1, M)) > Fraction(1, N): fail('(2.2)')
        ncount += 1
    d = TV(P, N)
    for H in range(0, 41):
        lo = max(Fraction(0), Q(m, H) - Fraction(N, 2 ** (H + 1)))
        hi = min(Fraction(1), Q(m, H) + Fraction(K(m, H), N))
        ref = min(Fraction(1), Q(m, H) + sum(comb(A - 1, m - 1) * (Fraction(N, 2 ** A) - (N // 2 ** A)) for A in range(m, H + 1)) / N)
        if not (lo <= d <= hi and d <= ref): fail('sandwich N=%d b=%d m=%d H=%d' % (N, b, m, H))
        nsand += 1
    hs = m - 1
    while K(m, hs + 1) <= N: hs += 1
    if d < Q(m, hs) - Fraction(N - K(m, hs), 2 ** (hs + 1)): fail('(3.4)')
    L = N.bit_length() - 1
    if N == 2 ** L:
        ident = Q(m, L) - sum(Fraction(1, 2 ** sum(w)) for w in P if sum(w) > L)
        if ident != d: fail('dyadic identity (3.5)')
        ndy += 1
out.append('Counts (2.1)/(2.2): %d word counts over %d (N,b,m) cases incl. b=1e30+3: PASS' % (ncount, len(cases)))
out.append('TV sandwich (3.2) and rounding refinement (3.3) for H=0..40: %d checks; support bound (3.4) all cases; dyadic identity (3.5) exact in %d dyadic cases: PASS' % (nsand, ndy))

# Descent counter (6.1): N=4096, b=0, m=5, H=16
N, b, m, H = 4096, 0, 5, 16
P = law(N, b, m)
def tau(w):
    best = None; A = 0; B = 0
    for j in range(1, len(w) + 1):
        B = 3 * B + 2 ** A; A += w[j - 1]
        D = 2 ** A - 3 ** j
        if D > 0:
            t = B // D; best = t if best is None else min(best, t)
    return best
Dlow = 0; acc = 0
from itertools import product
def words_upto(m, H):
    # all positive words of length m with sum <= H
    def rec(prefix, rem, k):
        if k == 0: yield tuple(prefix); return
        for a in range(1, rem - (k - 1) + 1):
            yield from rec(prefix + [a], rem - a, k - 1)
    yield from rec([], H, m)
for w in words_upto(m, H):
    r, h, A = r_h(w); M = 2 ** A
    C = (b + N - 1 - h) // M - (b - 1 - h) // M
    t = tau(w)
    U = b + N - 1 if t is None else min(b + N - 1, (t - 1) // 2)
    Z = ((U - h) // M - (b - 1 - h) // M) if U >= b else 0
    Dlow += C - Z; acc += C
R = N - acc
actual = 0
for j in range(b, b + N):
    n = 2 * j + 1; x = n
    for _ in range(m):
        y = 3 * x + 1; x = y >> v2(y)
        if x < n: actual += 1; break
if not (Dlow <= actual <= Dlow + R): fail('(6.1)')
out.append('Descent counter (6.1) fixture N=4096,b=0,m=5,H=16: accounted %d, overflow %d, bounds %d..%d, direct count %d (note: 3929,167,3320..3487,3487): %s' % (acc, R, Dlow, Dlow + R, actual, 'PASS' if (acc, R, Dlow, Dlow + R, actual) == (3929, 167, 3320, 3487, 3487) else 'DIFFERS'))

# Gaussian window: exact TV via dyadic identity for N=2^L, several c (display only)
def Phi(x): return 0.5 * (1 + math.erf(x / math.sqrt(2)))
rows = []
for L in (16, 20):
    N = 2 ** L
    for c in (-1.0, -0.5, 0.0, 0.5, 1.0):
        m = int(math.floor(L / 2 + c * math.sqrt(L)))
        if m < 1: continue
        seen = set(); tail = Fraction(0)
        for j in range(0, N):
            w = word(2 * j + 1, m); A = sum(w)
            if A > L and w not in seen:
                seen.add(w); tail += Fraction(1, 2 ** A)
        d = Q(m, L) - tail
        rows.append((L, c, m, float(d), Phi(2 * c)))
out.append('Gaussian window illustration (exact TV at b=0 via (3.5); finite N, not a limit certificate):')
for (L, c, m, d, ph) in rows:
    out.append('   N=2^%d c=%+.1f m=%d  TV=%.4f  Phi(2c)=%.4f' % (L, c, m, d, ph))
print('\n'.join(out)); print('elapsed %.1fs' % (time.time() - t0))
