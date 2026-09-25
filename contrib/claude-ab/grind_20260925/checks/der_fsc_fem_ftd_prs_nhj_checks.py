#!/usr/bin/env python3
"""Checks for note 19_ (content map of DER, FSC, FEM, FTD, PRS and NHJ4-NHJ9, 24-25 September 2026).

 DER4.2  the product injective complex on global sections: d1 d0 = 0, rank d1 = 3, kernel of d1 = span(1,-1,1,-1),
         the sum of the four corners annihilates the image (DER5.4); DER4.5-4.7: iota, pi, h with pi iota = id,
         d h + h d = id - iota pi in degrees 1 and 2 (generic-stalk level, ev = id); DER6.3 homotopy.
 PRS3.1  total product Cech differential squares to zero (random finite-dimensional model of d : P -> A).
 FSC2    in a finite model of X = U u {m+, m-} (U = {o, 2, 3, 5}), the closure of (p, p) contains (m+, m-) and the
         intersection of the closures of the prime points is {m+, m-}.
 NHJ7    the telescoping identity sum_{a<n} F_{t,nm+a} - n^{1-s} F_{t,m} = 8 g_t F0 (n - n^{1-s})/s at sample points,
         and W_n* W_n = n I, W_n W_n* = n P_n on truncated coefficient vectors.
 PRS1.5  |1/zeta(-1+it)| <= 4 pi^2 zeta(2) (1+|t|)^{-3/2} on a sample of t (the GZR2 bound used in PRS1.6).
claude-ab, model claude-opus-5-5 (Opus 5.5, maximum reasoning effort), 25 September 2026.
"""
import os, itertools, random
import numpy as np
import sympy as sp
import mpmath as mp
out = []
def say(s=""):
    print(s); out.append(s)

# ---- DER4 ----
d0 = sp.Matrix([1, -1, 1, -1])                                   # z -> (z, -z, z, -z)
d1 = sp.Matrix([[-1, 0, 1, 0], [1, 0, 0, 1], [0, -1, -1, 0], [0, 1, 0, -1]])   # (a+,a-,b+,b-) -> 4 corners
say("DER4.2: d1*d0 = %s ; rank d1 = %d ; nullspace d1 = %s ; sum-functional * d1 = %s"
    % (list(d1 * d0), d1.rank(), [list(v) for v in d1.nullspace()], list(sp.Matrix([[1, 1, 1, 1]]) * d1)))
iota1 = sp.Matrix([1, 0, 0, -1]); iota2 = sp.Matrix([[1, 0], [0, 0], [0, 0], [0, 1]])
pi1 = sp.Matrix([[1, 1, 0, 0]]); pi2 = sp.Matrix([[1, 0, 1, 0], [0, 1, 0, 1]])   # ev = id at the generic level
dsm = sp.Matrix([[-1], [1]])                                      # T_small differential a -> (-a, +a)
h1 = sp.Matrix([[0, -1, 0, 0]]); h2 = sp.Matrix([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, -1, 0], [0, 1, 0, 0]])
say("DER4.5-4.6: pi1*iota1 = %s, pi2*iota2 = %s, chain maps: d1*iota1 - iota2*dsm = %s, pi2*d1 - dsm*pi1 = %s"
    % (list(pi1 * iota1), list(pi2 * iota2), list(d1 * iota1 - iota2 * dsm), list(pi2 * d1 - dsm * pi1)))
I4 = sp.eye(4)
say("DER4.7: h1*d0 = %s ; deg 1: d0*h1 + h2*d1 - (I - iota1*pi1) = %s ; deg 2: d1*h2 - (I - iota2*pi2) = %s"
    % (list(h1 * d0), list(d0 * h1 + h2 * d1 - (I4 - iota1 * pi1)), list(d1 * h2 - (I4 - iota2 * pi2))))
# DER6: target resolution at the diagonal (mixed corners pulled back to zero); generic-level model with ev = id
e0 = sp.Matrix([1, -1, 1, -1]); e1 = sp.Matrix([[-1, 0, 1, 0], [0, 1, 0, -1]])
c1 = sp.Matrix([1, 0, 0, -1]); c2 = sp.eye(2); hh = sp.Matrix([[-1, 0], [0, 0], [0, 0], [0, -1]])
say("DER6.2-6.3: e1*e0 = %s ; e1*hh - c2 = %s ; hh*dsm - c1 = %s" % (list(e1 * e0), list(e1 * hh - c2), list(hh * dsm - c1)))

# ---- PRS3.1 ----
rng = np.random.default_rng(1)
p, a = 3, 2
D = rng.integers(-3, 4, size=(a, p)).astype(float)
Ip, Ia = np.eye(p), np.eye(a)
dC0 = np.vstack([np.kron(Ip, D), np.kron(D, Ip)])                   # p (x) q -> (p (x) dq, dp (x) q)
dC1 = np.hstack([np.kron(D, Ia), -np.kron(Ia, D)])                 # (x, y) -> (d (x) 1)x - (1 (x) d)y
say("PRS3.1: max |d_C1 d_C0| = %g (random 2x3 integer d)" % np.abs(dC1 @ dC0).max())

# ---- FSC2 ----
U = ['o', 2, 3, 5]; X = U + ['m+', 'm-']
opensU = [set()] + [set(['o']) | set(S) for r in range(4) for S in itertools.combinations([2, 3, 5], r)]
opensX = [set(o) for o in opensU] + [set(U) | {'m+'}, set(U) | {'m-'}, set(X)]
def closure(pt):
    return {x for x in X if all(pt in O for O in opensX if x in O)}
cl = {x: closure(x) for x in X}
say("FSC2: closure(2) = %s ; closure(3) = %s ; intersection over primes = %s"
    % (sorted(map(str, cl[2])), sorted(map(str, cl[3])), sorted(map(str, cl[2] & cl[3] & cl[5]))))
prod_ok = all(('m+' in cl[pp] and 'm-' in cl[pp]) for pp in [2, 3, 5])
say("FSC2: (m+, m-) lies in closure((p,p)) = closure(p) x closure(p) for p = 2, 3, 5: %s" % prod_ok)

# ---- NHJ7 ----
mp.mp.dps = 25
F0 = lambda s: s * (s - 1) / 8 * mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)
t = mp.mpf("0.3")
g = lambda s: mp.e ** (t * s ** 2)
def psi(m, s):
    first = 0 if m == 0 else mp.mpf(m) ** (1 - s)
    return (first - mp.mpf(m + 1) ** (1 - s) + 8 * F0(s)) / s
worst = 0
for s in [mp.mpc(0.3, 2.2), mp.mpc(-1.4, 0.7), mp.mpc(2.5, -3)]:
    for n in [2, 3, 7]:
        for m in [0, 1, 4]:
            lhs = sum(g(s) * psi(n * m + aa, s) for aa in range(n)) - mp.mpf(n) ** (1 - s) * g(s) * psi(m, s)
            rhs = 8 * g(s) * F0(s) * (n - mp.mpf(n) ** (1 - s)) / s
            worst = max(worst, abs(lhs - rhs))
say("NHJ7.2: max |telescoped discrepancy - 8 g_t F0 (n - n^{1-s})/s| over 27 cases = %s" % mp.nstr(worst, 3))
Nc = 60
for n in [2, 3, 5]:
    Mrows = Nc // n
    W = np.zeros((Nc, Mrows))
    for m in range(Mrows):
        for aa in range(n):
            W[n * m + aa, m] = 1.0
    P = np.zeros((Nc, Nc))
    for m in range(Mrows):
        blk = slice(n * m, n * m + n); P[blk, blk] = 1.0 / n
    say("NHJ7.5 (n=%d, %d coefficients): |W*W - nI| = %g ; |WW* - nP| = %g ; P idempotent: %g"
        % (n, Nc, np.abs(W.T @ W - n * np.eye(Mrows)).max(), np.abs(W @ W.T - n * P).max(), np.abs(P @ P - P).max()))

# ---- PRS1.5 / GZR2 bound ----
worst_ratio = 0
for tt in list(np.linspace(0, 60, 241)) + [100, 250, 1000]:
    val = 1 / abs(mp.zeta(mp.mpc(-1, tt)))
    bound = 4 * mp.pi ** 2 * mp.zeta(2) * (1 + abs(tt)) ** mp.mpf(-1.5)
    worst_ratio = max(worst_ratio, val / bound)
say("PRS1.5: max over sampled t in [0, 1000] of |1/zeta(-1+it)| / (4 pi^2 zeta(2) (1+|t|)^{-3/2}) = %s (must be <= 1)" % mp.nstr(worst_ratio, 6))
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "der_fsc_fem_ftd_prs_nhj_checks_OUTPUT.txt"), "w") as fh:
    fh.write("\n".join(out) + "\n")
