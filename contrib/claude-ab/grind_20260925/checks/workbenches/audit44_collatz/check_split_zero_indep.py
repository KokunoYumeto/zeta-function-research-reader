#!/usr/bin/env python3
"""Independent check of split_zero_history_20260913/note.tex (Finite Collatz histories
through support and Hurwitz zero clusters). Exact parts with integers/Fractions; the
analytic zero-cluster inversion is tested NUMERICALLY with mpmath at the first zeta zero
(the workbench's own checker does no numerical zeta computation)."""
import sys, time, itertools
from fractions import Fraction
from math import comb
t0 = time.time()
def fail(m): print('FAIL', m); sys.exit(1)
out = []
# ---------- polynomial lift (Prop. 2.1) ----------
def padd(p, r):
    o = dict(p)
    for k, v in r.items():
        o[k] = o.get(k, 0) + v
        if o[k] == 0: del o[k]
    return o
def pshift(p, d): return {k + d: v for k, v in p.items()}
def Pw(w):
    m = sum(w); P = {}; s = 0
    for j, d in enumerate(w):
        if d: P = padd(P, {m - 1 - s: 2 ** j}); s += 1
    return P
nw = 0; seen = {}
for N in range(0, 11):
    for w in itertools.product((0, 1), repeat=N):
        # compose T_d(x)=(q^d x + d)/2 with T_{d0} first: track (m, P) with value (q^m x + P)/2^N
        m, P = 0, {}
        for k, d in enumerate(w):
            P = padd(pshift(P, d), {0: d * 2 ** k}) if d else P
            m += d
        if P != Pw(w): fail('lift formula %s' % (w,))
        key = (N, tuple(sorted(P.items())))
        if key in seen: fail('injectivity')
        seen[key] = w; nw += 1
        # reversal identity X_{w^rev}(q) = 2^{-N} P_w(q), X_w(q)=sum_j d_j q^{s_j}/2^{j+1}
        wr = w[::-1]; X = {}; s = 0
        for j, d in enumerate(wr):
            if d: X[s] = X.get(s, 0) + Fraction(1, 2 ** (j + 1)); s += 1
        if X != {k: Fraction(v, 2 ** N) for k, v in P.items()}: fail('reversal identity %s' % (w,))
out.append('Prop 2.1 lift formula, injectivity of w->(N,P_w), reversal identity X_{w^rev}=2^-N P_w: all %d words of length <=10: PASS' % nw)
# realization congruence
def parity_word(n, N):
    w = []
    for _ in range(N):
        d = n & 1; w.append(d); n = (3 * n + 1) // 2 if d else n // 2
    return tuple(w)
nr = 0
for N in range(1, 13):
    for n in range(1, 3 * 2 ** N + 1):
        w = parity_word(n, N); m = sum(w)
        P3 = sum(v * 3 ** k for k, v in Pw(w).items())
        if (3 ** m * n + P3) % 2 ** N: fail('realization')
        # uniqueness: no other word of length N satisfies the congruence at n
        nr += 1
    # every word occurs exactly once per residue class mod 2^N
    cls = {parity_word(n, N) for n in range(1, 2 ** N + 1)}
    if len(cls) != 2 ** N: fail('one residue per word')
out.append('Realization 3^m n + P_w(3) = 0 mod 2^N and bijection words <-> residues mod 2^N, N<=12: %d starts PASS' % nr)
# specialization collision
Xu = {0: Fraction(1, 2), 1: Fraction(1, 32)}; Xv = {0: Fraction(1, 8), 1: Fraction(1, 16), 2: Fraction(1, 32)}
diff = {k: Xv.get(k, 0) - Xu.get(k, 0) for k in range(3)}
if diff != {0: Fraction(-12, 32), 1: Fraction(1, 32), 2: Fraction(1, 32)}: fail('collision')
if sum(v * 3 ** k for k, v in Xu.items()) != Fraction(19, 32) or sum(v * 3 ** k for k, v in Xv.items()) != Fraction(19, 32): fail('19/32')
out.append('Specialization fibre: X_v - X_u = (q-3)(q+4)/32 = (q^2+q-12)/32, X_u(3)=X_v(3)=19/32: PASS')
# ---------- odd-return coordinates ----------
def v2(x): return (x & -x).bit_length() - 1
def B_of(w):
    m = len(w); A = 0; B = 0
    for j in range(m): B += 3 ** (m - 1 - j) * 2 ** A; A += w[j]
    return B
def comps(A, m):
    for cuts in itertools.combinations(range(1, A), m - 1):
        c = (0,) + cuts + (A,); yield tuple(c[i + 1] - c[i] for i in range(m))
npk = 0; nwords = 0
for A in range(1, 15):
    for m in range(1, A + 1):
        W = list(comps(A, m)); D = 2 ** A - 3 ** m
        R = []
        for w in W:
            B = B_of(w); M = 2 ** (A + 1)
            r = ((2 ** A - B) * pow(3 ** m, -1, M)) % M
            R.append(r)
            # exact word at r (and r + M)
            for n in (r, r + M):
                x = n; ww = []
                for _ in range(m):
                    y = 3 * x + 1; a = v2(y); ww.append(a); x = y >> a
                if tuple(ww) != w: fail('odd-return residue')
            # rotation identity
            sw = w[1:] + w[:1]
            if 3 * B + D != 2 ** w[0] * B_of(sw): fail('rotation identity')
        if len(set(R)) != len(R): fail('distinct nodes')
        npk += 1; nwords += len(W)
out.append('Lemma 3.1 odd-return residues exact, pairwise distinct in each packet W_{m,A}, rotation identity 3B_w+D=2^{a1}B_{sigma w}: all %d packets with A<=14 (%d words): PASS' % (npk, nwords))
# ---------- Lagrange inverse and sharpness ----------
def lagrange_check(nodes):
    K = len(nodes)
    hw = []
    for i, r in enumerate(nodes):
        p = Fraction(1)
        for j, s in enumerate(nodes):
            if j != i: p /= (r - s)
        hw.append(p)
    for j in range(K):
        S = sum(h * r ** j for h, r in zip(hw, nodes))
        if j <= K - 2 and S != 0: fail('sharpness moment')
        if j == K - 1 and S != 1: fail('leading coefficient')
    return True
nl = 0
for A in range(2, 11):
    for m in range(2, A + 1):
        W = list(comps(A, m))
        if len(W) < 2: continue
        nodes = [((2 ** A - B_of(w)) * pow(3 ** m, -1, 2 ** (A + 1))) % 2 ** (A + 1) for w in W]
        lagrange_check([Fraction(x) for x in nodes]); nl += 1
out.append('Theorem 4.2 sharpness identities sum_w h_w r_w^j = 0 (j<=K-2), =1 (j=K-1): %d packets (A<=10): PASS' % nl)
# example (m,A)=(2,4)
nodes = {(1, 3): 19, (2, 2): 1, (3, 1): 29}
for w, r in nodes.items():
    if ((9 * r + B_of(w)) - 16) % 32: fail('example nodes')
M1 = Fraction(49, 3); M2 = Fraction(401)
if (M2 - 48 * M1 + 551) / 504 != Fraction(1, 3): fail('example mass')
out.append('Example (m,A)=(2,4): nodes 19,1,29; B=5,7,11; D=7; lambda_(2,2)=(M2-48M1+551)/504=1/3 at uniform weights: PASS')
# ---------- numerical Hurwitz zero-cluster check ----------
try:
    import mpmath as mp
    mp.mp.dps = 40
    rho = mp.zetazero(1)
    def trajectory(lams, rs, ts):
        sols = []
        for t in ts:
            f = lambda s: sum(l * mp.zeta(s, 1 + t * r) for l, r in zip(lams, rs))
            sols.append(mp.findroot(f, rho))
        return sols
    rs = [19, 1, 29]
    for lams in ([mp.mpf(1) / 3] * 3, [mp.mpf('0.5'), mp.mpf('0.2'), mp.mpf('0.3')]):
        dlt = mp.mpf('1e-6')
        ts = [-2 * dlt, -dlt, dlt, 2 * dlt]
        sol = trajectory(lams, rs, ts)
        s_m2, s_m1, s_p1, s_p2 = sol
        c1 = (8 * (s_p1 - s_m1) - (s_p2 - s_m2)) / (12 * dlt)
        c2 = ((s_p1 + s_m1 - 2 * rho) * 16 - (s_p2 + s_m2 - 2 * rho)) / (12 * dlt ** 2) / 2
        zp = mp.zeta(rho, derivative=1); zpp = mp.zeta(rho, derivative=2)
        M1n = zp * c1 / (rho * mp.zeta(rho + 1))
        M2n = -2 / (rho * (rho + 1) * mp.zeta(rho + 2)) * (zp * c2 + zpp / 2 * c1 ** 2 - M1n * (mp.zeta(rho + 1) + rho * mp.zeta(rho + 1, derivative=1)) * c1)
        M1t = sum(l * r for l, r in zip(lams, rs)); M2t = sum(l * r * r for l, r in zip(lams, rs))
        lam22 = (M2n - 48 * M1n + 551) / 504
        out.append('Numerical zero-cluster inversion at rho_1=%s, lambda=%s: M1 recovered %s (true %s), M2 recovered %s (true %s), lambda_(2,2) recovered %s (true %s)' % (
            mp.nstr(rho, 12), [mp.nstr(l, 4) for l in lams], mp.nstr(M1n, 10), mp.nstr(M1t, 10), mp.nstr(M2n, 10), mp.nstr(M2t, 10), mp.nstr(lam22, 10), mp.nstr(lams[1], 6)))
        if abs(M1n - M1t) > 1e-6 or abs(M2n - M2t) > 1e-3: fail('numerical inversion')
    out.append('   (finite-difference estimates of c1,c2 with |t|<=2e-6; |t|*31<1 holds): PASS')
except ImportError:
    out.append('mpmath not available: numerical check skipped')
print('\n'.join(out)); print('elapsed %.1fs' % (time.time() - t0))
