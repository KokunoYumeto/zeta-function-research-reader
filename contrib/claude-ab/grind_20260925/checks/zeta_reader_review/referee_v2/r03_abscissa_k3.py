#!/usr/bin/env python3
"""Referee v2, script r03.  Prop 5.1 (every tensor degree) and its k = 3 example.

S = {0.7 +- 10i, 0.3 +- 10i}, weights m (here 1 and also 2 for one point), k = 3.
 1. Exact grouping of the k-tuples by their sum w (exact integers: w = (Re*10, Im)); every c_w > 0.
 2. Rightmost w: Re w = 3 beta_max = 2.1; the set {2.1 +- 10i, 2.1 +- 30i}; none is real; no real w at all.
 3. The identity D(s) = sum_n (sum m n^rho)^3 n^-s = sum_w c_w zeta(s - w) at s = 6 (absolute convergence).
 4. Near the abscissa 3.1: |sum c_w zeta(s-w)| stays bounded at s = 3.1 + eps (real), and grows like c/eps
    at s = 3.1 + eps + 10i and 3.1 + eps + 30i (the poles), eps -> 0.
 5. Even k (k = 2, 4) with conjugation-stable S: the real point 1 + k beta_max is a pole with c_w > 0.
"""
import itertools
from collections import Counter
import mpmath as mp
mp.mp.dps = 30
ok_all = True
def rep(name, cond, info=""):
    global ok_all
    ok_all &= bool(cond); print(("[PASS] " if cond else "[FAIL] ") + name + ("" if not info else ": " + str(info)))

S = [((7, 10), 1), ((7, -10), 1), ((3, 10), 1), ((3, -10), 1)]     # (10*Re, Im), weight
def group(S, k):
    c = Counter()
    for tup in itertools.product(range(len(S)), repeat=k):
        w = (sum(S[i][0][0] for i in tup), sum(S[i][0][1] for i in tup))
        m = 1
        for i in tup: m *= S[i][1]
        c[w] += m
    return c
c3 = group(S, 3)
top = sorted(w for w in c3 if w[0] == 21)
rep("1-2 k=3: all c_w > 0; rightmost sums are 2.1 +- 10i, 2.1 +- 30i; no real sum at all",
    all(v > 0 for v in c3.values()) and top == [(21, -30), (21, -10), (21, 10), (21, 30)] and not any(w[1] == 0 for w in c3),
    f"{len(c3)} distinct w; top c_w = { {f'{w[0]/10}{w[1]:+d}i': c3[w] for w in top} }")

def D_series(s, N=4000):
    tot = mp.mpf(0)
    for n in range(1, N + 1):
        a = sum(m * mp.power(n, mp.mpc(x / 10, y)) for (x, y), m in S)
        tot += a**3 * mp.power(n, -s)
    return tot
def D_zeta(s, c):
    return mp.fsum(v * mp.zeta(s - mp.mpc(w[0] / 10, w[1])) for w, v in c.items())
s0 = mp.mpf(6)
lhs, rhs = D_series(s0), D_zeta(s0, c3)
rep("3  sum_n (sum m n^rho)^3 n^-6 (N = 4000 terms) matches sum c_w zeta(6 - w)", abs(lhs - rhs) / abs(rhs) < 1e-6, f"rel. diff {mp.nstr(abs(lhs - rhs)/abs(rhs), 3)}")

real_vals, pole_vals = [], []
for eps in (mp.mpf('1e-2'), mp.mpf('1e-4'), mp.mpf('1e-6')):
    real_vals.append(abs(D_zeta(mp.mpf('3.1') + eps, c3)))
    pole_vals.append((abs(D_zeta(mp.mpc(mp.mpf('3.1') + eps, 10), c3)) * eps, abs(D_zeta(mp.mpc(mp.mpf('3.1') + eps, 30), c3)) * eps))
rep("4  real point 3.1 is not a pole (bounded), 3.1+10i and 3.1+30i are (eps*|D| -> c_w = 3 and 1)",
    max(real_vals) < 100 and abs(pole_vals[-1][0] - 3) < 1e-4 and abs(pole_vals[-1][1] - 1) < 1e-4,
    f"|D(3.1+eps)| = {[mp.nstr(v, 6) for v in real_vals]}; eps|D| at +10i, +30i = {[(mp.nstr(a, 6), mp.nstr(b, 6)) for a, b in pole_vals]}")

S2 = [((7, 10), 2), ((7, -10), 2), ((3, 10), 1), ((3, -10), 1)]   # conjugation-stable, weights 2,2,1,1
res = []
for k in (2, 4):
    ck = group(S2, k)
    res.append((k, ck.get((7 * k, 0), 0), all(v > 0 for v in ck.values())))
rep("5  even k (2, 4), conjugation-stable S with weights: real point 1 + k beta_max is a pole, c_w > 0",
    all(r[1] > 0 and r[2] for r in res), f"c at real w = k*0.7: {[(r[0], r[1]) for r in res]}")
print("ALL CHECKS PASS" if ok_all else "SOME CHECKS FAILED")
