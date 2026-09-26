#!/usr/bin/env python3
"""Referee checks for note 44 (Collatz). Independent code; exact integers."""
import math, time, random
from fractions import Fraction as Fr
import numpy as np
T0 = time.time()
def out(*a): print(*a, flush=True)

def v2(n):
    return (n & -n).bit_length() - 1
def T(n):
    m = 3*n + 1; a = v2(m); return m >> a, a

# 1. hypothesis of Thm 44.9: all odd n <= 330749 reach 1 (so the least element of a nontrivial cycle is >= 330751)
LIM = 330749
reach = bytearray(LIM + 1)   # reach[n]=1 if known to reach 1
reach[1] = 1
bad = []
for n in range(3, LIM + 1, 2):
    x = n; path = []
    steps = 0
    while x >= n or (x <= LIM and not reach[x] and x != 1):
        # iterate until we fall below n (all smaller odd numbers already verified) -- standard stopping-time check
        x, _ = T(x); steps += 1
        if x < n: break
        if steps > 10**5: bad.append(n); break
    if x < n or x == 1:
        reach[n] = 1
out("Thm 44.9 hypothesis: all odd n <= 330749 reach 1 (stopping-time induction):", not bad and all(reach[n] for n in range(1, LIM + 1, 2)))

# 2. m* and k for s = 330751, by a different route: continued-fraction style scan with exact integer tests
s = 330751
# need 3^m < 2^A <= (3+1/s)^m  <=>  3^m s^m < 2^A s^m <= (3s+1)^m ; A = floor(m log2 3) + 1
mstar = None
for m in range(1, 4000):
    A = m * 3  # placeholder
    # smallest A with 2^A > 3^m:
    A = (3**m).bit_length()
    if 2**A * s**m <= (3*s + 1)**m:
        mstar = m; break
# k: least integer with 2^k >= (4s/(3s+1))^m  at m = mstar; exact via integer comparison
num = (4*s)**mstar; den = (3*s + 1)**mstar
k = 0
while (den << k) < num: k += 1
out(f"m* = {mstar} (note: 1636);  least k with (4s)^m <= 2^k (3s+1)^m at m*: {k} (note: >= 679)")
# monotonicity: (4s/(3s+1))^m increasing since 4s > 3s+1
out("4s > 3s+1:", 4*s > 3*s + 1)
# the workbench's (C37): (4s)^1634 > 2^678 (3s+1)^1634
out("(C37) (4s)^1634 > 2^678 (3s+1)^1634:", (4*s)**1634 > (2**678) * (3*s + 1)**1634)

# 3. cylinder words: every word of length m=1..3 with A <= 11 is realised, exactly one class mod 2^(A+1)
from math import comb
for m in (1, 2, 3):
    cls = {}
    for n in range(1, 2**15, 2):
        x = n; w = []
        for _ in range(m):
            x, a = T(x); w.append(a)
        A = sum(w)
        if A <= 11:
            cls.setdefault(tuple(w), set()).add(n % 2**(A + 1))
    out(f"m={m}: words with A<=11 realised: {len(cls)} (all words: C(11,{m}) = {comb(11, m)}); one class each: {all(len(c) == 1 for c in cls.values())}")

# 4. Theorem 44.4 on fresh parameters (e up to 40, b up to 10), independent implementation incl. the height claim
def word(n, L):
    w = []
    for _ in range(L):
        n, a = T(n); w.append(a)
    return n, w
def nu3(n):
    k = 0
    while n % 3 == 0: n //= 3; k += 1
    return k
badfam = 0; nfam = 0
random.seed(1)
for e in range(2, 41, 2):
    he = (2**e + 2)//3
    for b in range(1, 11):
        for sig in (0, 1):
            a = 1
            while 2**(a + e + 2*b - sig) >= 3**(a + b): a += 1
            J = 2**(e + 2*b - sig); Q = 3**(a + b); K = 2**a * J
            d, r = (4, 3) if sig == 0 else (32, 27)
            # CRT
            x = (-he * 3**b * pow(J, -1, Q)) % Q
            n0 = next(x + k*Q for k in range(d) if (x + k*Q) % d == r)
            num = K*n0 + 2**a * he * 3**b
            assert num % Q == 0
            m0 = num//Q - 1
            for v in (0, 3, 10**20 + 1):
                n = n0 + d*Q*v; m = m0 + d*K*v
                lw = [1] if sig == 0 else [1, 2, 1]
                rw = [1]*a + [e] + [2]*(b - 1) + ([3] if sig == 0 else [1, 1, 3])
                yn, wn = word(n, len(lw)); ym, wm = word(m, len(rw))
                nfam += 1
                ok = (wn == lw and wm == rw and yn == ym and 0 < m < n and n % 2 == 1 and m % 2 == 1
                      and nu3(n) == b + nu3(e - 1) and a >= e and a <= b + 2*e - 2*sig)
                if not ok: badfam += 1
out(f"Thm 44.4 (independent, e<=40, b<=10, both sigma, 3 values of v): {nfam} pairs, failures {badfam}")

# 5. Prop 44.8: cycle equation for word (1,2^{m-1}): n D = 2*4^{m-1} - 3^{m-1}, n-1 = 2*3^{m-1}/D
ok8 = True
for m in range(1, 60):
    D = 2*4**(m-1) - 3**m; N = 2*4**(m-1) - 3**(m-1)
    if Fr(N, D) - 1 != Fr(2*3**(m-1), D): ok8 = False
    if D % 2 == 0 or D % 3 == 0: ok8 = False
    if m >= 3 and D < 5: ok8 = False
out("Prop 44.8 algebra (n-1 = 2*3^{m-1}/D, D odd and prime to 3, D>=5 for m>=3), m<60:", ok8)

# 6. Thm 44.12 example: residues for (m,A)=(2,4), and the moment/Lagrange formula
res = {}
for n in range(1, 64, 2):
    _, w = word(n, 2)
    if sum(w) == 4: res.setdefault(tuple(w), set()).add(n % 32)
out("(m,A)=(2,4) residues mod 32:", {k: sorted(v) for k, v in sorted(res.items())})
r = {(1, 3): 19, (2, 2): 1, (3, 1): 29}
lam = {(1, 3): Fr(1, 2), (2, 2): Fr(1, 5), (3, 1): Fr(3, 10)}
M1 = sum(lam[w]*r[w] for w in r); M2 = sum(lam[w]*r[w]**2 for w in r)
out("weights (0.5,0.2,0.3): M1 =", M1, "M2 =", M2, " lambda_(2,2) from (M2-48M1+551)/504 =", (M2 - 48*M1 + 551)/504)
# the q-fixture
import sympy as sp
q = sp.symbols('q')
Xu = sp.Rational(1, 2) + q/32; Xv = sp.Rational(1, 8) + q/16 + q**2/32
out("fixture: Xv - Xu =", sp.factor(Xv - Xu), "; Xu(3) =", Xu.subs(q, 3), "Xv(3) =", Xv.subs(q, 3))

# 7. Theorem 44.2 numerical window at N = 2^20 (b = 0: odd starts 1..2^21-1)
N = 2**20; L = 20
starts = np.arange(1, 2*N, 2, dtype=np.int64)
def tv_for_m(m):
    x = starts.copy()
    codes = np.zeros(N, dtype=object)
    words = [[] for _ in range(0)]
    A = np.zeros(N, dtype=np.int64)
    key = np.zeros(N, dtype=np.int64)  # encode word injectively: append (a) in unary-binary: key = key*2^a + 1 style
    keys = [0]*N
    ws = np.zeros((m, N), dtype=np.int64)
    for i in range(m):
        y = 3*x + 1
        a = np.zeros(N, dtype=np.int64)
        tmp = y.copy()
        while True:
            even = (tmp & 1) == 0
            if not even.any(): break
            a[even] += 1; tmp[even] >>= 1
        ws[i] = a; A += a; x = tmp
    # empirical law
    from collections import Counter
    C = Counter(map(tuple, ws.T.tolist()))
    s = 0.0
    for w, c in C.items():
        s += min(c/N, 2.0**(-sum(w)))
    return 1 - s
from statistics import NormalDist
vals = []
for c in (-1, -0.5, 0, 0.5, 1):
    m = math.floor(L/2 + c*math.sqrt(L))
    vals.append((c, m, round(tv_for_m(m), 3), round(NormalDist().cdf(2*c), 3)))
out("TV at N=2^20 (c, m, TV, Phi(2c)):", vals, " (note: 0.004, 0.044, 0.342, 0.668, 0.895 vs 0.023, 0.159, 0.5, 0.841, 0.977)")
out(f"total {time.time()-T0:.1f}s")
