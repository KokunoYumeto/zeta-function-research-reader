#!/usr/bin/env python3
# Checks for claude-ab note 36_ (audit of the Deligne reader DELIGNE_WEIGHT_CONTROL_FULL.md, parts DP0-DP9, DMG0-DMG7, DLM1-DLM15).
# Written by a subagent in the first-pass audit (25 September 2026) and copied unchanged below this header by Claude
# (claude-ab lane), model claude-opus-5-5 (Opus 5.5) at maximum reasoning effort. Re-run at 16:59 UTC: 47/47 PASS,
# output identical to the first run apart from the timing column. Requires sympy, mpmath and python-flint.
# Item labels C01-C46 are the ones cited in 36_.
# -*- coding: utf-8 -*-
"""
deligne_part1_checks.py

Finite-dimensional model checks for the audit of the reconstruction items
DP0-DP9, DMG0-DMG7 and DLM1-DLM15 (Deligne, "La conjecture de Weil II",
Sections 1.3-1.9, as reconstructed in the audited document).

Every check prints "[Cnn] PASS" or "[Cnn] FAIL" with a one-line description.
Some checks are "negative" checks: they PASS when a counterexample to a
tempting but false statement is exhibited (the description says so).

Arithmetic:
  * all nilpotent / filtration / Frobenius-model computations are exact
    (fractions.Fraction; subspaces stored in canonical RREF);
  * the power-series positivity checks with complex eigenvalues use mpmath
    at 50 significant digits.

Conventions (as in the audited text):
  * geometric Frobenius F, Tate line Q(1) on which F acts by Q^{-1};
  * N : V(1) -> V, so that after choosing a basis F N F^{-1} = Q^{-1} N;
  * weight of an eigenvalue a relative to Q: w_Q(a) = 2 log|a| / log Q;
  * a Jordan string e_d, e_{d-2}, ..., e_{-d} with N e_k = e_{k-2},
    N e_{-d} = 0; monodromy filtration M_i = span{e_k : k <= i};
  * primitive part P_i = ker(N : Gr_i -> Gr_{i-2}), nonzero only for i <= 0.
"""

import itertools
import math
import random
from fractions import Fraction as Fr

import time

import flint
import mpmath as mp
import sympy as sp

random.seed(20260925)
mp.mp.dps = 50

RESULTS = []
T0 = time.time()


def check(cid, desc, ok, detail=""):
    ok = bool(ok)
    RESULTS.append((cid, desc, ok))
    line = f"[{cid}] {'PASS' if ok else 'FAIL'} ({time.time() - T0:6.1f}s) - {desc}"
    if detail:
        line += f"\n        {detail}"
    print(line, flush=True)
    return ok


# =====================================================================
# Exact linear algebra over Q
# =====================================================================
def zeros(m, n):
    return [[Fr(0)] * n for _ in range(m)]


def eye(n):
    A = zeros(n, n)
    for i in range(n):
        A[i][i] = Fr(1)
    return A


def mmul(A, B):
    n = len(B[0])
    Bt = [[B[k][j] for k in range(len(B))] for j in range(n)]
    return [[sum((a * b for a, b in zip(row, col)), Fr(0)) for col in Bt] for row in A]


def mv(A, v):
    return [sum((a * x for a, x in zip(row, v)), Fr(0)) for row in A]


def madd(A, B):
    return [[a + b for a, b in zip(r, s)] for r, s in zip(A, B)]


def msub(A, B):
    return [[a - b for a, b in zip(r, s)] for r, s in zip(A, B)]


def msc(c, A):
    c = Fr(c)
    return [[c * a for a in r] for r in A]


def mpow(A, k):
    R = eye(len(A))
    for _ in range(k):
        R = mmul(R, A)
    return R


def tr(A):
    return [list(r) for r in zip(*A)]


def kron(A, B):
    p, q = len(B), len(B[0])
    return [[A[i // p][j // q] * B[i % p][j % q] for j in range(len(A[0]) * q)]
            for i in range(len(A) * p)]


def vkron(u, v):
    return [a * b for a in u for b in v]


def is_zero(A):
    return all(x == 0 for r in A for x in r)


def diag(entries):
    n = len(entries)
    D = zeros(n, n)
    for i, e in enumerate(entries):
        D[i][i] = Fr(e)
    return D


def rref(rows, ncols):
    R = [list(r) for r in rows]
    piv = []
    r = 0
    for c in range(ncols):
        if r >= len(R):
            break
        p = next((i for i in range(r, len(R)) if R[i][c] != 0), None)
        if p is None:
            continue
        R[r], R[p] = R[p], R[r]
        pv = R[r][c]
        R[r] = [x / pv for x in R[r]]
        for i in range(len(R)):
            if i != r and R[i][c] != 0:
                f = R[i][c]
                R[i] = [a - f * b for a, b in zip(R[i], R[r])]
        piv.append(c)
        r += 1
    return R[:r], piv


def nullspace(rows, ncols):
    if not rows:
        return [[Fr(int(i == j)) for i in range(ncols)] for j in range(ncols)]
    R, piv = rref(rows, ncols)
    free = [c for c in range(ncols) if c not in piv]
    out = []
    for f in free:
        x = [Fr(0)] * ncols
        x[f] = Fr(1)
        for i, p in enumerate(piv):
            x[p] = -R[i][f]
        out.append(x)
    return out


def inv(A):
    n = len(A)
    aug = [list(A[i]) + [Fr(int(i == j)) for j in range(n)] for i in range(n)]
    R, piv = rref(aug, 2 * n)
    if piv[:n] != list(range(n)) or len(piv) < n:
        raise ValueError("singular")
    return [r[n:] for r in R]


def rank(A):
    if not A:
        return 0
    return len(rref(A, len(A[0]))[1])


def expnil(N, lam=1):
    """exp(lam*N) for nilpotent N (finite sum)."""
    n = len(N)
    R = eye(n)
    term = eye(n)
    k = 1
    while True:
        term = msc(Fr(lam) / k, mmul(term, N))
        if is_zero(term):
            return R
        R = madd(R, term)
        k += 1


class Sub:
    """Subspace of Q^n stored by its canonical reduced row echelon basis."""

    def __init__(self, n, vecs):
        self.n = n
        vecs = [list(v) for v in vecs if any(x != 0 for x in v)]
        self.rows = tuple(tuple(r) for r in rref(vecs, n)[0]) if vecs else ()

    @property
    def dim(self):
        return len(self.rows)

    def __eq__(self, other):
        return self.n == other.n and self.rows == other.rows

    def __add__(self, other):
        return Sub(self.n, list(self.rows) + list(other.rows))

    def contains(self, other):
        return (self + other).dim == self.dim


def full(n):
    return Sub(n, [[Fr(int(i == j)) for i in range(n)] for j in range(n)])


def zero(n):
    return Sub(n, [])


def coord_sub(n, idxs):
    return Sub(n, [[Fr(int(i == j)) for i in range(n)] for j in idxs])


def image(A, S=None):
    n = len(A)
    if S is None:
        return Sub(n, tr(A))
    return Sub(n, [mv(A, list(v)) for v in S.rows])


def kernel(A):
    return Sub(len(A[0]), nullspace(A, len(A[0])))


def ann(S):
    return Sub(S.n, nullspace([list(r) for r in S.rows], S.n))


def meet(S, T):
    return ann(ann(S) + ann(T))


def preimage(A, S):
    a = ann(S)
    n = len(A[0])
    if a.dim == 0:
        return full(n)
    return Sub(n, nullspace(mmul([list(r) for r in a.rows], A), n))


def span_kron(S, T):
    return Sub(S.n * T.n, [vkron(list(u), list(v)) for u in S.rows for v in T.rows])


def rand_invertible(n, lo=-2, hi=2):
    while True:
        A = [[Fr(random.randint(lo, hi)) for _ in range(n)] for _ in range(n)]
        try:
            return A, inv(A)
        except ValueError:
            continue


# =====================================================================
# Monodromy filtrations
# =====================================================================
def nil_index(N):
    """least d >= 0 with N^(d+1) = 0"""
    n = len(N)
    P = N
    d = 0
    while not is_zero(P):
        P = mmul(P, N)
        d += 1
        if d > n:
            raise ValueError("not nilpotent")
    return d


class Filt:
    """Increasing filtration; levels[i] for lo <= i <= hi, levels[lo] = bottom, levels[hi] = top."""

    def __init__(self, n, levels, lo, hi):
        self.n, self.levels, self.lo, self.hi = n, levels, lo, hi

    def __call__(self, i):
        if i >= self.hi:
            return self.levels[self.hi]
        if i <= self.lo:
            return self.levels[self.lo]
        return self.levels[i]


def mono_filt(N, center=0):
    """Closed formula M_i = sum_{a-b=i, a,b>=0} ker N^{a+1} cap im N^b (independent of DLM1.2)."""
    n = len(N)
    d = nil_index(N)
    kers = [kernel(mpow(N, k)) for k in range(d + 2)]
    ims = [image(mpow(N, k)) for k in range(d + 2)]
    levels = {}
    for i in range(-d - 1, d + 1):
        S = zero(n)
        for a in range(max(0, i), d + 1):
            b = a - i
            if 0 <= b <= d:
                S = S + meet(kers[a + 1], ims[b])
        levels[i + center] = S
    return Filt(n, levels, -d - 1 + center, d + center)


def subquot_mono(N, A, B):
    """DLM1.2 recursion on the subquotient A/B; returns (levels, d) with levels[d]=A, levels[-d-1]=B."""
    if A.dim == B.dim:
        return {0: A, -1: B}, 0
    d = 0
    P = N
    while not B.contains(image(P, A)):
        P = mmul(P, N)
        d += 1
    if d == 0:
        return {0: A, -1: B}, 0
    Nd = mpow(N, d)
    km = meet(A, preimage(Nd, B))        # M_{d-1} = ker N^d (mod B)
    bm = image(Nd, A) + B                # M_{-d}  = im N^d  (mod B)
    lev, dd = subquot_mono(N, km, bm)
    res = {d: A, -d - 1: B}
    for i in range(-d, d):
        if i >= dd:
            res[i] = km
        elif i <= -dd - 1:
            res[i] = bm
        else:
            res[i] = lev[i]
    return res, d


def mono_filt_rec(N):
    n = len(N)
    lev, d = subquot_mono(N, full(n), zero(n))
    return Filt(n, lev, -d - 1, d)


def filt_equal(M1, M2, lo, hi):
    return all(M1(i) == M2(i) for i in range(lo, hi + 1))


def grdim(M, i):
    return M(i).dim - M(i - 1).dim


def prim_sub(N, M, i):
    """representative subspace of P_i = ker(N: Gr_i -> Gr_{i-2}) (contains M_{i-1})."""
    return meet(M(i), preimage(N, M(i - 3))) + M(i - 1)


def prim_dim(N, M, i):
    return prim_sub(N, M, i).dim - M(i - 1).dim


def jordan(sizes):
    """basis f_1..f_m per block, N f_t = f_{t+1}; f_1 = top vector e_d."""
    n = sum(sizes)
    J = zeros(n, n)
    pos = 0
    for m in sizes:
        for t in range(m - 1):
            J[pos + t + 1][pos + t] = Fr(1)
        pos += m
    return J


def rand_nilpotent(sizes):
    J = jordan(sizes)
    T, Ti = rand_invertible(len(J))
    return mmul(mmul(T, J), Ti), T


def to_flint(A):
    n, m = len(A), len(A[0])
    return flint.fmpq_mat(n, m, [flint.fmpq(x.numerator, x.denominator) for row in A for x in row])


def jordan_type(N):
    """sorted list of block sizes from ranks of powers (ranks computed with python-flint, exact)."""
    n = len(N)
    Nf = to_flint(N)
    r = [n]
    P = Nf
    while len(r) < n + 2:
        rk = P.rank()
        r.append(rk)
        if rk == 0:
            r += [0] * (n + 2 - len(r))
            break
        P = P * Nf
    sizes = []
    for k in range(1, n + 1):
        ge_k = r[k - 1] - r[k]          # number of blocks of size >= k
        ge_k1 = r[k] - r[k + 1]         # number of blocks of size >= k+1
        sizes += [k] * (ge_k - ge_k1)
    return sorted(sizes)


# =====================================================================
# Frobenius-weight models
# =====================================================================
def string_model(specs):
    """specs: list of (d, center). Basis per string: e_d, e_{d-2}, ..., e_{-d};
    N e_k = e_{k-2}; weight(e_k) = center + k; W-degree (centre) = center."""
    n = sum(d + 1 for d, c in specs)
    N = zeros(n, n)
    w, cen, lvl = [], [], []
    pos = 0
    for d, c in specs:
        for t in range(d + 1):
            k = d - 2 * t
            w.append(c + k)
            cen.append(c)
            lvl.append(k)
            if t < d:
                N[pos + t + 1][pos + t] = Fr(1)
        pos += d + 1
    return dict(n=n, N=N, w=w, cen=cen, lvl=lvl)


def weight_filt(w, shift=0):
    """M_i = span{basis vectors with weight <= i + shift}."""
    n = len(w)
    lo, hi = min(w) - shift - 1, max(w) - shift
    levels = {i: coord_sub(n, [j for j in range(n) if w[j] <= i + shift]) for i in range(lo, hi + 1)}
    return Filt(n, levels, lo, hi)


def equivariant_g(w, cen, mixed=False):
    """random invertible g preserving every weight space (and W when mixed)."""
    n = len(w)
    g = zeros(n, n)
    groups = {}
    for i in range(n):
        groups.setdefault((w[i], cen[i]), []).append(i)
    for idx in groups.values():
        A, _ = rand_invertible(len(idx), -2, 2)
        for a in range(len(idx)):
            for b in range(len(idx)):
                g[idx[a]][idx[b]] = A[a][b]
    if mixed:
        for i in range(n):
            for j in range(n):
                if w[i] == w[j] and cen[i] < cen[j]:
                    g[i][j] = Fr(random.randint(-2, 2))
    return g, inv(g)


def weight_space_dims(M, w, i):
    """multiset {weight: dim} of Gr_i^M, for a filtration by F-stable subspaces (F diagonal, weights w)."""
    n = len(w)
    out = {}
    for ww in sorted(set(w)):
        E = coord_sub(n, [j for j in range(n) if w[j] == ww])
        dd = meet(M(i), E).dim - meet(M(i - 1), E).dim
        if dd:
            out[ww] = dd
    return out


def prim_weight_dims(N, M, w, i):
    n = len(w)
    out = {}
    for ww in sorted(set(w)):
        E = coord_sub(n, [j for j in range(n) if w[j] == ww])
        dd = meet(meet(M(i), preimage(N, M(i - 3))), E).dim - meet(M(i - 1), E).dim
        if dd:
            out[ww] = dd
    return out


def kernel_weights(N, w):
    """set of weights w with ker(N) cap E_w != 0.  Since N maps E_w to E_{w-2}, ker N is the direct sum
    of the kernels of the column blocks N|E_w, so each block is tested separately (exact, via flint)."""
    ws = set()
    for ww in set(w):
        cols = [j for j in range(len(w)) if w[j] == ww]
        block = [[N[i][j] for j in cols] for i in range(len(N))]
        if to_flint(block).rank() < len(cols):
            ws.add(ww)
    return ws


def tensor_model(m1, m2):
    n1, n2 = m1["n"], m2["n"]
    N = madd(kron(m1["N"], eye(n2)), kron(eye(n1), m2["N"]))
    w = [a + b for a in m1["w"] for b in m2["w"]]
    return dict(n=n1 * n2, N=N, w=w)


def dual_model(m):
    return dict(n=m["n"], N=msc(-1, tr(m["N"])), w=[-x for x in m["w"]])


print("=" * 78)
print("deligne_part1_checks.py : audit checks for DP0-DP9, DMG0-DMG7, DLM1-DLM15")
print("=" * 78)

# =====================================================================
# DP0 / DP1 : conventions, rank-one characters, twists
# =====================================================================
print("\n--- DP0-DP1: weights, Tate twists, rank-one characters, the 1.3.6 degree factor")

q, r_, d_, a_, c_, n_, beta = sp.symbols("q r d a c n beta", positive=True)
wq = lambda z, base: 2 * sp.log(z) / sp.log(base)
# C01: (r) multiplies F_x by N(x)^{-r} and lowers the weight by 2r
Nx = q ** d_
expr = sp.simplify(sp.expand_log(wq(a_ * Nx ** (-r_), Nx) - wq(a_, Nx), force=True))
check("C01", "DP0: Tate twist (r) multiplies F_x by N(x)^{-r} and changes w_{N(x)} by -2r",
      sp.simplify(expr + 2 * r_) == 0, f"w(a N^-r) - w(a) = {expr}")

# C02: rank-one chi = c^deg * eps : |chi(F_x)| = |c|^{d_x} and w_{N(x)}(chi(F_x)) = w_q(c)
expr = sp.simplify(sp.expand_log(wq(c_ ** d_, q ** d_) - wq(c_, q), force=True))
ok = expr == 0
# numerical toy: finite geometric image of exponent h, recover c and eps
h = 6
bb = sp.Rational(7, 3)
cc = sp.root(bb, h)
eps_vals = [sp.exp(2 * sp.pi * sp.I * k / h) for k in range(h)]
ok2 = True
for dx in range(1, 5):
    for e in eps_vals:
        chi = cc ** dx * e                      # chi(F_x) with |chi|=|c|^dx
        ok2 &= sp.simplify(chi ** h - bb ** dx * e ** h) == 0     # chi^h = b^deg
        ok2 &= sp.simplify(sp.Abs(chi) - sp.Abs(cc) ** dx) == 0
check("C02", "DP1.2-1.3: chi = c^deg eps with eps^h = 1 gives chi^h = b^deg, |chi(F_x)| = |c|^{d_x}, "
      "and w_{N(x)}(chi(F_x)) = w_q(c)", ok and ok2)

# C03: determinant weight sum (DP1.5): sum_j w_{N(x)}(alpha_j) = w_{N(x)}(prod alpha_j) = n*beta
al = sp.symbols("al1:5", positive=True)
lhs = sum(wq(x, q ** d_) for x in al)
rhs = wq(sp.Mul(*al), q ** d_)
check("C03", "DP1.5: weights of eigenvalues add to the weight of the determinant (only the SUM is controlled)",
      sp.simplify(sp.expand_log(lhs - rhs, force=True)) == 0)

# C04: DP1.6 / DMG7.10: a constant line over F_p with Frobenius b acts at x (degree d over F_q, q=p^f) by b^{fd}
ok = True
for f in range(1, 5):
    for d in range(1, 5):
        deg_over_Fp = f * d                    # [k(x):F_p] = [F_q:F_p][k(x):F_q]
        # geometric Frobenius of k(x) = (geometric Frobenius of F_p)^{[k(x):F_p]}
        exponent_line = deg_over_Fp
        rank_n = 3
        det_exponent = rank_n * exponent_line
        ok &= det_exponent == rank_n * f * d
        # the 'division by f' variant disagrees as soon as f>1
        if f > 1:
            ok &= Fr(rank_n * d, f) != det_exponent
check("C04", "DP1.6 / DMG7.10-11: twist by constant F_p-line with Frobenius b multiplies det at x by b^{n f d} "
      "(not b^{n d/f}); DMG7's b^{rgd} is the same statement", ok)

# =====================================================================
# DP2 : central element, determinant weights of tensor / exterior powers
# =====================================================================
print("\n--- DP2 / DMG2: central element and determinant-weight bookkeeping")

u_, m_ = sp.symbols("u m", positive=True)
# |u|^r = |c|^m  and beta = w_q(c)/r  =>  |u| = q^{m beta/2}
sol = sp.solve(sp.Eq(u_ ** r_, c_ ** m_), u_)
ok = any(sp.simplify(sp.expand_log(sp.log(s) - m_ * (wq(c_, q) / r_) / 2 * sp.log(q), force=True)) == 0 for s in sol)
check("C05", "DP2.3 / DMG2.3: u^r = c^m eps(z) and beta = w_q(c)/r give |u| = q^{m beta/2}", ok)

# C06: DP2.4 exterior-power determinant weights: sums over a-subsets == {sum a(g) g}
ok = True
for trial in range(40):
    weights = sorted(random.sample(range(-4, 7), random.randint(1, 4)))
    mult = {g: random.randint(1, 3) for g in weights}
    multiset = [g for g in weights for _ in range(mult[g])]
    ntot = len(multiset)
    for a in range(1, ntot + 1):
        subset_sums = {sum(s) for s in itertools.combinations(multiset, a)}
        combo_sums = set()
        for avec in itertools.product(*[range(mult[g] + 1) for g in weights]):
            if sum(avec) == a:
                combo_sums.add(sum(x * g for x, g in zip(avec, weights)))
        ok &= subset_sums == combo_sums
    # DP6.2: max determinant weight of wedge^{N_beta+1} equals r_beta
    for b in weights:
        Nb = sum(mult[g] for g in weights if g > b)
        rb = b + sum(mult[g] * g for g in weights if g > b)
        mx = max(sum(s) for s in itertools.combinations(multiset, Nb + 1))
        ok &= mx == rb
check("C06", "DP2.4 and DP6.2: determinant weights of wedge^a are exactly {sum a(g)g : 0<=a(g)<=n(g), sum a(g)=a}; "
      "max for a = N_beta+1 is r_beta", ok)

# C07: DMG2 commutator-power identity [y^e,h] = [y,h]^e when y commutes with [y,h]
a1, b1 = sp.symbols("a1 b1", nonzero=True)
y = sp.diag(a1, b1)
hh = sp.Matrix([[0, 1], [1, 0]])
cmm = y * hh * y.inv() * hh.inv()
ok = sp.simplify(y * cmm - cmm * y) == sp.zeros(2)
for e in range(1, 7):
    ok &= sp.simplify(y ** e * hh * y.inv() ** e * hh.inv() - cmm ** e) == sp.zeros(2)
yy = sp.diag(1, -1)   # commutator of order 2 -> y^2 central relative to h
cm2 = yy * hh * yy.inv() * hh.inv()
ok &= (cm2 ** 2 == sp.eye(2)) and (yy ** 2 * hh == hh * yy ** 2)
check("C07", "DP2 / DMG2.2: if y commutes with c=[y,h] then [y^e,h]=c^e; exponent of the finite centre kills it", ok)

# C08: DMG5 degree bookkeeping
mm, aa, dX, dY = sp.symbols("m a d_X d_Y", positive=True)
lhs1 = (q ** dX) ** ((mm / dX) * beta / 2)
lhs2 = (q ** dY) ** ((aa * mm / dY) * beta / 2)
ok = sp.simplify(sp.powsimp(lhs1 / q ** (mm * beta / 2), force=True)) == 1
ok &= sp.simplify(sp.powsimp(lhs2 / q ** (aa * mm * beta / 2), force=True)) == 1
check("C08", "DMG5.2-5.4: |u| = (q^{d_X})^{(m/d_X) beta/2} = q^{m beta/2} and |u^a| = (q^{d_Y})^{(am/d_Y) beta/2}", ok)

# C08b: DMG6.5-6.6 ultrametric root bound: roots of a monic polynomial satisfy |x|_p <= max(1, max_i |a_i|_p)
def vp(x, p):
    x = Fr(x)
    if x == 0:
        return math.inf
    v = 0
    num, den = x.numerator, x.denominator
    while num % p == 0:
        num //= p
        v += 1
    while den % p == 0:
        den //= p
        v -= 1
    return v


ok = True
for trial in range(200):
    p = random.choice([2, 3, 5, 7])
    roots = [Fr(random.randint(-30, 30), random.choice([1, p, p * p, 3 * p, 5])) for _ in range(random.randint(1, 5))]
    xs = sp.Symbol("xs")
    poly = sp.Poly(sp.prod([xs - sp.Rational(rt.numerator, rt.denominator) for rt in roots]), xs)
    coeffs = [Fr(int(sp.fraction(cf)[0]), int(sp.fraction(cf)[1])) for cf in poly.all_coeffs()[1:]]
    bound_v = min([0] + [vp(cf, p) for cf in coeffs])          # |a|_p = p^{-v}: max |a| <-> min v
    ok &= all(vp(rt, p) >= bound_v for rt in roots)
check("C08b", "DMG6.5-6.6: a root x of a monic polynomial with coefficients a_i satisfies |x|_p <= max(1, max|a_i|_p) "
      "(200 random rational examples)", ok)

# =====================================================================
# DP3-DP5 : positivity and pole radii
# =====================================================================
print("\n--- DP3-DP5: even tensor powers of iota-real data, positivity, pole radii")


def series_exp(cf, M):
    b = [mp.mpc(0)] * (M + 1)
    b[0] = mp.mpc(1)
    for nn in range(1, M + 1):
        s = mp.mpc(0)
        for k in range(1, nn + 1):
            s += k * cf[k] * b[nn - k]
        b[nn] = s / nn
    return b


def series_mul(a, b, M):
    return [sum(a[i] * b[nn - i] for i in range(nn + 1)) for nn in range(M + 1)]


def local_factor(eigs, dx, k2, M):
    """Taylor coefficients of det(1 - F_x^{(tensor 2k)} t^{dx})^{-1}: log = sum_j (sum eig^j)^{2k}/j t^{j dx}."""
    cf = [mp.mpc(0)] * (M + 1)
    j = 1
    while j * dx <= M:
        pj = sum(e ** j for e in eigs)
        cf[j * dx] += pj ** k2 / j
        j += 1
    return series_exp(cf, M)


def random_real_multiset():
    out = [mp.mpf(random.uniform(-3, 3)) for _ in range(random.randint(0, 2))]
    for _ in range(random.randint(0, 2)):
        z = mp.mpc(random.uniform(-3, 3), random.uniform(0.1, 3))
        out += [z, mp.conj(z)]
    if not out:
        out = [mp.mpf(1.5)]
    return out


tol = mp.mpf(10) ** (-30)
ok_real, ok_nonneg, ok_dom = True, True, True
M = 14
for trial in range(25):
    pts = [(random_real_multiset(), random.randint(1, 3)) for _ in range(random.randint(2, 4))]
    for k in (1, 2, 3):
        facs = [local_factor(e, dx, 2 * k, M) for e, dx in pts]
        prod = [mp.mpc(1)] + [mp.mpc(0)] * M
        for fct in facs:
            prod = series_mul(prod, fct, M)
        for fct in facs:
            for nn in range(M + 1):
                ok_real &= abs(mp.im(fct[nn])) < tol * (1 + abs(fct[nn]))
                ok_nonneg &= mp.re(fct[nn]) > -tol * (1 + abs(fct[nn]))
                ok_dom &= mp.re(fct[nn]) <= mp.re(prod[nn]) + tol * (1 + abs(prod[nn]))
check("C09", "DP4.1-4.2: for iota-real eigenvalue multisets, every local factor of the 2k-th tensor power has "
      "real nonnegative Taylor coefficients, dominated coefficientwise by the product",
      ok_real and ok_nonneg and ok_dom)

# C10 (negative): reality is necessary
f1 = local_factor([mp.mpc(0, 1)], 1, 2, 4)          # eigenvalue i, k=1 : (Tr)^2 = -1
f2 = local_factor([mp.mpc(1), mp.mpc(0, 1)], 1, 2, 4)  # Tr = 1+i, (Tr)^2 = 2i
check("C10", "DP4 negative: without iota-reality positivity fails (eigenvalue i gives coefficient -1; {1,i} gives "
      "a non-real coefficient 2i)",
      mp.re(f1[1]) < 0 and abs(mp.im(f2[1]) - 2) < tol,
      f"[t^1] for {{i}}: {mp.nstr(f1[1], 5)};  [t^1] for {{1,i}}: {mp.nstr(f2[1], 5)}")

# C11: pole radius of det(1 - a^{2k} t^d)^{-1} is |a|^{-2k/d}; DP5.3 algebra
ok = True
for trial in range(10):
    aabs = mp.mpf(random.uniform(1.2, 2.5))
    arg = mp.mpf(random.uniform(0, 2 * mp.pi))
    alpha = aabs * mp.e ** (1j * arg)
    for k in (1, 2):
        for dx in (1, 2, 3):
            Mx = 60 * dx
            cf = local_factor([alpha], dx, 2 * k, Mx)  # single eigenvalue: det(1 - alpha^{2k} t^dx)^{-1}
            est = abs(cf[Mx]) ** (mp.mpf(-1) / Mx)
            ok &= abs(est - aabs ** (mp.mpf(-2 * k) / dx)) < mp.mpf("1e-10")
kk = sp.symbols("k", positive=True)
w_ = sp.symbols("w", real=True)
# |alpha|^{2k/d} = q^{k w};  q^{k w} <= q^{(2kr+2)/2}  <=>  w <= r + 1/k
ineq_ok = sp.simplify((kk * r_ + 1) / kk - (r_ + 1 / kk)) == 0
check("C11", "DP5.2-5.3: the reciprocal local determinant has pole radius |alpha|^{-2k/d_x}; radius >= q^{-(2kr+2)/2} "
      "<=> w_{N(x)}(alpha) <= r + 1/k", ok and ineq_ok)

# C12: DP6 squeeze and exterior-power reality
ok_squeeze, ok_real_wedge = True, True
n_pure_cfg = 0
for trial in range(60):
    classes = sorted(random.sample(range(-3, 6), random.randint(1, 3)))
    nmult = {g: random.randint(1, 3) for g in classes}
    pure = random.random() < 0.3
    wts = {}
    for g in classes:
        if pure or nmult[g] == 1:
            wts[g] = [Fr(g)] * nmult[g]
        else:
            pert = [Fr(random.randint(-4, 4), 2) for _ in range(nmult[g] - 1)]
            pert.append(-sum(pert))
            wts[g] = [Fr(g) + p for p in pert]
    is_pure = all(x == g for g in classes for x in wts[g])
    n_pure_cfg += is_pure
    violated = False
    for b in classes:
        rb = b + sum(nmult[g] * g for g in classes if g > b)
        higher = sum(sum(wts[g]) for g in classes if g > b)
        for x in wts[b]:
            if x + higher > rb:
                violated = True
    ok_squeeze &= (violated == (not is_pure))
for trial in range(20):
    ms = random_real_multiset() + random_real_multiset()
    for a in range(1, len(ms) + 1):
        prods = [mp.fprod(s) for s in itertools.combinations(ms, a)]
        poly = [mp.mpc(1)]
        for p_ in prods:
            poly = [poly[i] - (p_ * poly[i - 1] if i > 0 else 0) for i in range(len(poly))] + [-p_ * poly[-1]]
        ok_real_wedge &= all(abs(mp.im(cfx)) < mp.mpf("1e-25") * (1 + abs(cfx)) for cfx in poly)
check("C12", "DP6: with determinant equalities fixed, the wedge^{N_beta+1} bound is violated iff some constituent "
      "is impure; wedge powers of iota-real data are iota-real", ok_squeeze and ok_real_wedge,
      f"{n_pure_cfg} pure and {60 - n_pure_cfg} impure weight configurations tested")

# C13: DP7 real companion
ok_pure, ok_nonpure, conv_fails = True, True, False


def conj_closed(ms, eps=mp.mpf("1e-30")):
    rem = list(ms)
    for z in ms:
        cz = mp.conj(z)
        idx = min(range(len(rem)), key=lambda i: abs(rem[i] - cz))
        if abs(rem[idx] - cz) > eps * (1 + abs(cz)):
            return False
        rem.pop(idx)
    return True


for trial in range(20):
    Nx_ = mp.mpf(random.choice([4, 5, 9, 16]))
    wt = random.choice([1, 2, 3])
    eig = [mp.sqrt(Nx_ ** wt) * mp.e ** (1j * mp.mpf(random.uniform(0, 6.28))) for _ in range(3)]
    comp = eig + [Nx_ ** wt / a for a in eig]
    ok_pure &= conj_closed(comp)
    bad = [mp.mpf(1.3) * eig[0]] + eig[1:]
    compb = bad + [Nx_ ** wt / a for a in bad]
    ok_nonpure &= (not conj_closed(compb))
Nx_ = mp.mpf(9)
real_bad = [mp.mpf(2)]
conv_fails = conj_closed(real_bad + [Nx_ / real_bad[0]]) and abs(real_bad[0] ** 2 - Nx_) > 1
beta_r = mp.mpf("0.73")
eig = [mp.mpf(4) ** (beta_r / 2) * mp.e ** (1j * mp.mpf(0.4))]
ok_Lbeta = conj_closed(eig + [mp.mpf(4) ** beta_r / eig[0]])
check("C13", "DP7: pure weight n => F + F^v(-n) is iota-real (also with L_beta, real beta); impure complex "
      "eigenvalue => not real; converse fails (a real eigenvalue 2 with N(x)^n=9 gives a real companion)",
      ok_pure and ok_nonpure and conv_fails and ok_Lbeta)

# =====================================================================
# DLM1 : monodromy filtration, primitive parts, strictness
# =====================================================================
print("\n--- DLM1: monodromy filtration, primitive decomposition, strictness")

partitions = [[1], [2], [3], [2, 2], [3, 1], [4, 2, 1], [3, 3, 1], [5, 2], [4, 4], [2, 1, 1, 1], [6, 3, 2]]
ok_rec, ok_low, ok_iso, ok_prim_pos, ok_decomp, ok_14, ok_strict, ok_kerG = (True,) * 8
for sizes in partitions:
    N, T = rand_nilpotent(sizes)
    n = len(N)
    M = mono_filt(N)
    Mr = mono_filt_rec(N)
    d = nil_index(N)
    ok_rec &= filt_equal(M, Mr, -d - 3, d + 3)
    for i in range(-d - 2, d + 3):
        ok_low &= M(i - 2).contains(image(N, M(i)))
    for k in range(0, d + 2):
        Nk = mpow(N, k)
        ok_iso &= M(-k).contains(image(Nk, M(k))) and M(-k - 1).contains(image(Nk, M(k - 1)))
        ok_iso &= grdim(M, k) == grdim(M, -k)
        ok_iso &= meet(M(k), preimage(Nk, M(-k - 1))) == M(k - 1)
    for i in range(1, d + 3):
        ok_prim_pos &= prim_dim(N, M, i) == 0
    for i in range(-d - 2, d + 3):
        ok_decomp &= grdim(M, i) == sum(prim_dim(N, M, -j) for j in range(abs(i), d + 3) if (j - i) % 2 == 0)
    for j in range(0, d + 2):
        ok_14 &= grdim(M, -j) == prim_dim(N, M, -j) + grdim(M, j + 2)
    imN = image(N)
    for i in range(-d - 3, d + 3):
        ok_strict &= image(N, M(i + 2)) == meet(imN, M(i))
    K = kernel(N)
    for i in range(-d - 2, d + 3):
        ok_kerG &= (meet(K, M(i)).dim - meet(K, M(i - 1)).dim) == prim_dim(N, M, i)
check("C14", "DLM1.2: closed formula and the text's recursion (M_d=V, M_{d-1}=ker N^d, M_{-d}=im N^d, recurse) "
      "give the same filtration (random conjugated nilpotents)", ok_rec)
check("C15", "DLM1.1: N M_i in M_{i-2} and N^k : Gr_k -> Gr_{-k} is an isomorphism", ok_low and ok_iso)
check("C16", "DLM1.3-1.5: P_i = 0 for i>0; Gr_{-j} = P_{-j} + N^{j+1}Gr_{j+2}; dim Gr_i = sum_{j>=|i|, j=i mod 2} dim P_{-j}",
      ok_prim_pos and ok_14 and ok_decomp)
check("C17", "DLM1.6-1.7: strictness N(M_{i+2}) = im N cap M_i for all i, and Gr_i(ker N) = P_i", ok_strict and ok_kerG)

# C18: Jordan string conventions (1.6.7): N e_{-d} = 0, primitive = lowest vector
ok = True
for d in range(0, 6):
    m = string_model([(d, 0)])
    N = m["N"]
    M = mono_filt(N)
    for i in range(-d - 1, d + 1):
        ok &= M(i) == coord_sub(m["n"], [j for j in range(m["n"]) if m["lvl"][j] <= i])
    bottom = [Fr(int(t == d)) for t in range(d + 1)]
    top = [Fr(int(t == 0)) for t in range(d + 1)]
    ok &= all(x == 0 for x in mv(N, bottom))
    if d >= 1:
        ok &= any(x != 0 for x in mv(N, top))                 # so the exception cannot be i = d
    ok &= prim_dim(N, M, -d) == 1 and all(prim_dim(N, M, i) == 0 for i in range(-d + 1, d + 2))
check("C18", "DLM1 / correction 1: on a string M_i = span{e_k: k<=i}; N e_{-d} = 0 while N e_d != 0 (d>=1); "
      "the primitive vector is the lowest one", ok)

# =====================================================================
# DLM2 : SL(2), tensor products, duals, Clebsch-Gordan
# =====================================================================
print("\n--- DLM2: SL(2) triple, tensor and dual filtrations, Clebsch-Gordan")

ok = True
for d in range(0, 9):
    n = d + 1
    H = zeros(n, n)
    Fm = zeros(n, n)
    Em = zeros(n, n)
    for r in range(n):           # basis e_r = e_{-d+2r}
        H[r][r] = Fr(-d + 2 * r)
        if r >= 1:
            Fm[r - 1][r] = Fr(1)                     # F e_r = e_{r-1}
        if r + 1 <= d:
            Em[r + 1][r] = Fr((d - r) * (r + 1))     # E e_r = (d-r)(r+1) e_{r+1}
    br = lambda A, B: msub(mmul(A, B), mmul(B, A))
    ok &= br(H, Em) == msc(2, Em) and br(H, Fm) == msc(-2, Fm) and br(Em, Fm) == H
check("C19", "DLM2.1: H e_r=(-d+2r)e_r, F e_r=e_{r-1}, E e_r=(d-r)(r+1)e_{r+1} satisfy [H,E]=2E, [H,F]=-2F, [E,F]=H (d<=8)", ok)

ok_t, ok_d = True, True
pairs = [([2], [2]), ([3], [2]), ([2, 1], [3]), ([3, 1], [2, 2]), ([4], [3]), ([2, 2, 1], [2])]
for s1, s2 in pairs:
    N1, _ = rand_nilpotent(s1)
    N2, _ = rand_nilpotent(s2)
    n1, n2 = len(N1), len(N2)
    Nt = madd(kron(N1, eye(n2)), kron(eye(n1), N2))
    M1, M2, Mt = mono_filt(N1), mono_filt(N2), mono_filt(Nt)
    dt = nil_index(Nt)
    for i in range(-dt - 2, dt + 3):
        S = zero(n1 * n2)
        for a in range(M1.lo, M1.hi + 1):
            S = S + span_kron(M1(a), M2(i - a))
        ok_t &= Mt(i) == S
for sizes in partitions:
    N, _ = rand_nilpotent(sizes)
    n = len(N)
    M = mono_filt(N)
    Ms = mono_filt_rec(msc(-1, tr(N)))
    d = nil_index(N)
    for i in range(-d - 2, d + 3):
        ok_d &= Ms(i) == ann(M(-i - 1))
check("C20", "DLM2.3: M_i(V'(x)V'') = sum_{a+b=i} M_a V' (x) M_b V'' for N'(x)1+1(x)N'' (random conjugated pairs)", ok_t)
check("C21", "DLM2.4: with the contragredient operator -N^t, M_i(V*) = (M_{-i-1}V)^perp", ok_d)

ok_cg, ok_pd = True, True
for d1 in range(0, 7):
    for d2 in range(0, 7):
        N1 = jordan([d1 + 1])
        N2 = jordan([d2 + 1])
        Nt = madd(kron(N1, eye(d2 + 1)), kron(eye(d1 + 1), N2))
        expected = sorted(j + 1 for j in range(abs(d1 - d2), d1 + d2 + 1) if (j - d1 - d2) % 2 == 0)
        ok_cg &= jordan_type(Nt) == expected
for s1, s2 in pairs:
    N1, _ = rand_nilpotent(s1)
    N2, _ = rand_nilpotent(s2)
    n1, n2 = len(N1), len(N2)
    Nt = madd(kron(N1, eye(n2)), kron(eye(n1), N2))
    M1, M2, Mt = mono_filt(N1), mono_filt(N2), mono_filt(Nt)
    d1, d2 = nil_index(N1), nil_index(N2)
    for j in range(0, d1 + d2 + 3):
        predicted = 0
        for j1 in range(0, d1 + 1):
            for j2 in range(0, d2 + 1):
                if abs(j1 - j2) <= j <= j1 + j2 and (j - j1 - j2) % 2 == 0:
                    predicted += prim_dim(N1, M1, -j1) * prim_dim(N2, M2, -j2)
        ok_pd &= prim_dim(Nt, Mt, -j) == predicted
check("C22", "DLM2.5: Jordan type of N'(x)1+1(x)N'' on S_{d'}(x)S_{d''} is {S_j : j in P(d',d'')}, each once (d',d''<=6)", ok_cg)
check("C23", "DLM2.6 + DLM3.3 (dimensions): dim P_{-j}(V'(x)V'') = sum over (j',j'') with j in P(j',j'') of "
      "dim P_{-j'} dim P_{-j''}", ok_pd)

# =====================================================================
# DLM3 : Tate twists and weights
# =====================================================================
print("\n--- DLM3: Tate twists on primitive decompositions (weights; Q(1) has weight -2)")

ok_gr, ok_prim, ok_twist, witness_fails = True, True, True, True
for trial in range(6):
    beta0 = random.randint(-2, 3)
    specs = [(random.randint(0, 3), beta0) for _ in range(random.randint(1, 3))]
    m = string_model(specs)
    g, gi = equivariant_g(m["w"], m["cen"])
    N = mmul(mmul(g, m["N"]), gi)
    w = m["w"]
    M = mono_filt(N)
    d = nil_index(N)
    for i in range(-d, d + 1):
        grw = weight_space_dims(M, w, i)
        ok_gr &= (not grw) or set(grw) == {beta0 + i}
        # twist bookkeeping: Gr_i ~ sum_j P_{-j}(-(i+j)/2): weight(P_{-j}) + (i+j) must equal weight(Gr_i)
        pred = {}
        wit = {}
        for j in range(abs(i), d + 1):
            if (j - i) % 2:
                continue
            for ww, dd in prim_weight_dims(N, M, w, -j).items():
                pred[ww + (i + j)] = pred.get(ww + (i + j), 0) + dd       # twist -(i+j)/2 raises by i+j
                wit[ww - (i + j)] = wit.get(ww - (i + j), 0) + dd         # witness sign lowers by i+j
        ok_twist &= pred == grw
        if any(j != -i for j in range(abs(i), d + 1) if (j - i) % 2 == 0 and prim_dim(N, M, -j)):
            witness_fails &= (wit != grw)
    for j in range(0, d + 1):
        pw = prim_weight_dims(N, M, w, -j)
        ok_prim &= (not pw) or set(pw) == {beta0 - j}
check("C24", "DLM3.2 / DLM10.1, pure model of weight beta: Gr_i is pure of weight beta+i and P_{-j} of weight beta-j", ok_gr and ok_prim)
check("C25", "DLM3.2 / correction 3: Gr_i = sum_j P_{-j}(-(i+j)/2) matches the weights exactly; the positive twist "
      "((i+j)/2) is inconsistent whenever a summand with j != -i is present", ok_twist and witness_fails)

ok_tp, ok_dual = True, True
for trial in range(5):
    b1_, b2_ = random.randint(-2, 2), random.randint(-2, 2)
    m1 = string_model([(random.randint(0, 2), b1_) for _ in range(random.randint(1, 2))])
    m2 = string_model([(random.randint(0, 2), b2_) for _ in range(random.randint(1, 2))])
    mt = tensor_model(m1, m2)
    Mt = mono_filt(mt["N"])
    dt = nil_index(mt["N"])
    for j in range(0, dt + 1):
        pw = prim_weight_dims(mt["N"], Mt, mt["w"], -j)
        ok_tp &= (not pw) or set(pw) == {b1_ + b2_ - j}
    md = dual_model(m1)
    Md = mono_filt(md["N"])
    dd_ = nil_index(md["N"])
    for j in range(0, dd_ + 1):
        pw = prim_weight_dims(md["N"], Md, md["w"], -j)
        ok_dual &= (not pw) or set(pw) == {-b1_ - j}
        # P_{-j}(V)^*(j) has weight -(b1-j) - 2j = -b1 - j
        ok_dual &= (-(b1_ - j) - 2 * j) == (-b1_ - j)
check("C26", "DLM3.3: primitive parts of a tensor product of pure models (weights b', b'') have weight b'+b''-j, i.e. "
      "P_{-j'}(x)P_{-j''} twisted by ((j-j'-j'')/2)", ok_tp)
check("C27", "DLM3.4: P_{-j}(V*) has weight -beta-j = weight of P_{-j}(V)^*(j) (dual operator -N^t)", ok_dual)

# =====================================================================
# DLM4 : uniqueness recursion of the relative monodromy filtration
# =====================================================================
print("\n--- DLM4 / DLM11: relative monodromy filtration (mixed models)")


def rel_mono(N, W, alist):
    """DLM4.2 recursion. W: dict a -> W_a (increasing); alist: sorted degrees."""
    n = len(N)
    a = alist[-1]
    top = W[a]
    if len(alist) > 1:
        lowerM = rel_mono(N, W, alist[:-1])
        lower = W[alist[-2]]
    else:
        lowerM = lambda i: zero(n)
        lower = zero(n)
    _, c = subquot_mono(N, top, lower)
    R = n + 2
    Mloc = {}
    for rr in range(R, -1, -1):
        s = rr + 2
        Mlow = lowerM(a - s) if s > c else Mloc[a - s]
        Mloc[a + rr] = meet(top, preimage(mpow(N, rr + 1), Mlow))          # third formula
        if rr > c:
            Mloc[a - rr] = lowerM(a - rr)                                  # first formula
        else:
            Mloc[a - rr] = lowerM(a - rr) + image(mpow(N, rr), Mloc[a + rr])  # second formula
    lo, hi = a - R, a + R

    def f(i):
        if i > hi:
            return top
        if i < lo:
            return lowerM(i)
        return Mloc[i]
    return f


def rel_condition(N, M, W, alist, n, kmax):
    ok = True
    for idx, a in enumerate(alist):
        Wa = W[a]
        Wl = W[alist[idx - 1]] if idx > 0 else zero(n)
        for k in range(0, kmax + 1):
            A = meet(M(a + k), Wa) + Wl
            A1 = meet(M(a + k - 1), Wa) + Wl
            B = meet(M(a - k), Wa) + Wl
            B1 = meet(M(a - k - 1), Wa) + Wl
            Nk = mpow(N, k)
            ok &= B.contains(image(Nk, A)) and B1.contains(image(Nk, A1))
            ok &= (A.dim - A1.dim) == (B.dim - B1.dim)
            ok &= meet(A, preimage(Nk, B1)) == A1
    return ok


ok_rec_rel, ok_cond, ok_nonabs = True, True, False
n_mixed, n_offdiag = 0, 0
for trial in range(8):
    specs = [(random.randint(0, 2), random.randint(-2, 2)) for _ in range(random.randint(2, 3))]
    m = string_model(specs)
    n = m["n"]
    w, cen = m["w"], m["cen"]
    N0 = m["N"]
    X = zeros(n, n)
    for i in range(n):
        for j in range(n):
            if w[i] == w[j] - 2 and cen[i] < cen[j]:
                X[i][j] = Fr(random.randint(-2, 2))
    n_mixed += len(set(cen)) > 1
    n_offdiag += any(x != 0 for row in X for x in row)
    Nmix = madd(N0, X)
    g, gi = equivariant_g(w, cen, mixed=True)
    N = mmul(mmul(g, Nmix), gi)
    alist = sorted(set(cen))
    W = {a: coord_sub(n, [j for j in range(n) if cen[j] <= a]) for a in alist}
    Mw = weight_filt(w)
    # sanity: the model really satisfies F N F^{-1} = Q^{-1} N with F = diag(2^w), Q = 4
    Fm = diag([Fr(2) ** x if x >= 0 else Fr(1, 2 ** (-x)) for x in w])
    ok_cond &= mmul(mmul(Fm, N), inv(Fm)) == msc(Fr(1, 4), N)
    ok_cond &= all(W[a].contains(image(N, W[a])) for a in alist)
    ok_cond &= all(Mw(i - 2).contains(image(N, Mw(i))) for i in range(min(w) - 2, max(w) + 3))
    ok_cond &= rel_condition(N, Mw, W, alist, n, n)
    Mr = rel_mono(N, W, alist)
    ok_rec_rel &= all(Mr(i) == Mw(i) for i in range(min(w) - 3, max(w) + 4))
    # the relative filtration is in general NOT the absolute monodromy filtration shifted
    Mabs = mono_filt(N)
    if len(set(cen)) > 1 and not any(all(Mabs(i) == Mw(i + s) for i in range(-n - 2, n + 3)) for s in range(-6, 7)):
        ok_nonabs = True
check("C28", "DLM11.1 (mixed Frobenius models, Q=4): the Frobenius weight filtration satisfies N^b: Gr^M_{a+b}Gr^W_a(b) ~ "
      "Gr^M_{a-b}Gr^W_a for every a,b", ok_cond,
      f"8 models, {n_mixed} with several W-degrees, {n_offdiag} with nonzero W-lowering extension part")
check("C29", "DLM4.2: the three recursion formulas (descending r) reconstruct exactly that filtration", ok_rec_rel)
check("C30", "DLM4 remark: in mixed models the relative filtration differs from every shift of the absolute monodromy "
      "filtration (so W is genuinely needed)", ok_nonabs)

# C31: the inequality in (1.6.13)
ok = True
for a in range(-3, 4):
    for rr in range(0, 5):
        for j in range(a - 6, a + 1):
            for k in range(a + rr + 1, a + rr + 10):
                ok &= (k - 2 * rr - 2 >= 2 * j - k)
witness_impossible = all(not (k - 2 * i - 2 >= k) for i in range(0, 6) for k in range(-10, 10))
minus_variant = all((k - 2 * i - 2 >= -k) and all(k - 2 * i - 2 >= 2 * j - k for j in range(-5, 1))
                    for i in range(0, 6) for k in range(i + 1, i + 12))
check("C31", "DLM4 / correction 2: k-2r-2 >= 2j-k whenever k >= a+r+1 and j <= a; the displayed 'k-2i-2 >= k' is "
      "impossible for i>=0; the one-sign repair 'k-2i-2 >= -k' holds and implies the needed inequality for j<=0",
      ok and witness_impossible and minus_variant)

# =====================================================================
# DLM5-DLM6 : Frobenius / logarithm conventions, independence of the lift
# =====================================================================
print("\n--- DLM5-DLM6: F N F^{-1} = Q^{-1} N, independence of the lift, the 1.7.5 displays")

Qv = Fr(4)
m = string_model([(2, 0), (1, 1), (0, -1)])
n = m["n"]
w = m["w"]
F1 = diag([Fr(2) ** x if x >= 0 else Fr(1, 2 ** (-x)) for x in w])      # eigenvalue Q^{w/2} = 2^w
N = m["N"]
ok_rel = mmul(mmul(F1, N), inv(F1)) == msc(1 / Qv, N)
ok_conj = True
for nn in (1, 2, 3):
    for lam in (Fr(1), Fr(-3, 2), Fr(5, 7)):
        Fn = mpow(F1, nn)
        mu = lam / (1 - Qv ** (-nn))
        lhs = mmul(mmul(expnil(N, mu), Fn), expnil(N, -mu))
        ok_conj &= lhs == mmul(expnil(N, mu * (1 - Qv ** (-nn))), Fn)
        ok_conj &= lhs == mmul(expnil(N, lam), Fn)
# alternative conventions for the displayed coefficient 1 - q^n
ok_alt = True
for nn in (1, 2):
    for lam in (Fr(1), Fr(2, 3)):
        Fn = mpow(F1, nn)
        mu = lam / (1 - Qv ** nn)
        # (i) Frobenius on the left of the unipotent factor: F''^n = F'^n exp(lam N), conjugate by exp(-mu N)
        ok_alt &= mmul(mmul(expnil(N, -mu), Fn), expnil(N, mu)) == mmul(Fn, expnil(N, lam))
        # (ii) arithmetic Frobenius Phi = F^{-1}: Phi N Phi^{-1} = Q N, Phi''^n = exp(lam N) Phi'^n
        Phin = mpow(inv(F1), nn)
        ok_alt &= mmul(mmul(expnil(N, mu), Phin), expnil(N, -mu)) == mmul(expnil(N, lam), Phin)
check("C32", "DLM5.3: in the model F = diag(Q^{w/2}), N lowering weight by 2, F N F^{-1} = Q^{-1} N", ok_rel)
check("C33", "DLM6.2 / correction 5: exp(mu N) F^n exp(-mu N) = exp(mu(1-Q^{-n})N) F^n, so mu = lam/(1-Q^{-n}) "
      "conjugates F^n to exp(lam N) F^n", ok_conj)
check("C34", "Correction 5 caveat: the displayed factor 1-q^n is EXACT for F''^n = F'^n exp(lam N) with conjugation "
      "exp(-mu N)(.)exp(mu N), and for arithmetic Frobenius; the 'correction' is convention-dependent", ok_alt)

# C35: generalized-eigenspace filtration is lift-independent; 1.7.5 index check
ok_lift = True
F2 = mmul(expnil(N, Fr(3, 2)), F1)                    # another lift
for Fx in (F1, F2):
    ok_lift &= mmul(mmul(Fx, N), inv(Fx)) == msc(1 / Qv, N)
gen = {}
for label, Fx in (("F1", F1), ("F2", F2)):
    spaces = {}
    for ww in sorted(set(w)):
        lamv = Fr(2) ** ww if ww >= 0 else Fr(1, 2 ** (-ww))
        spaces[ww] = kernel(mpow(msub(Fx, msc(lamv, eye(n))), n))
    gen[label] = spaces
filtF1 = {}
for i in range(min(w) - 3, max(w) + 2):
    S1 = zero(n)
    S2 = zero(n)
    for ww in gen["F1"]:
        if ww <= i:
            S1 = S1 + gen["F1"][ww]
            S2 = S2 + gen["F2"][ww]
    ok_lift &= S1 == S2
    filtF1[i] = S1
for i in range(min(w) - 1, max(w) + 2):
    ok_lift &= filtF1[i - 2].contains(image(N, filtF1[i]))          # N M_i(1) in M_{i-2}
# N maps V_j to V_{j-2}
for ww in gen["F2"]:
    tgt = gen["F2"].get(ww - 2, zero(n))
    ok_lift &= tgt.contains(image(N, gen["F2"][ww]))
# 'sum over j < i' would give Gr_i of weight i-1
wrong_ok = True
for i in range(min(w), max(w) + 1):
    Wi = [x for x in w if x < i]
    Wi1 = [x for x in w if x < i - 1]
    grw = sorted(set(Wi) - set(Wi1)) if len(Wi) > len(Wi1) else []
    if grw:
        wrong_ok &= grw == [i - 1]
check("C35", "DLM6.1: the filtration by generalized eigenspaces of weight <= i is the same for F' and F''=exp(lam N)F', "
      "N maps V_j to V_{j-2}; a sum over j < i would give Gr_i of weight i-1 (correction 4)", ok_lift and wrong_ok)

# C36: DLM10 reduction: rescaling N by e != 0 changes neither M nor P
ok = True
for sizes in partitions[:8]:
    N_, _ = rand_nilpotent(sizes)
    M0 = mono_filt(N_)
    d = nil_index(N_)
    for e in (Fr(2), Fr(-3), Fr(1, 5)):
        Me = mono_filt(msc(e, N_))
        ok &= filt_equal(M0, Me, -d - 2, d + 2)
        ok &= all(prim_sub(N_, M0, i) == prim_sub(msc(e, N_), Me, i) for i in range(-d - 1, 1))
check("C36", "DLM3/DLM10/DLM13: M and the primitive subspaces are unchanged when N is replaced by eN, e != 0", ok)

# =====================================================================
# DLM8 : tensor-power inclusion
# =====================================================================
print("\n--- DLM8-DLM9: invariants of tensor powers, amplification algebra")

N1 = jordan([2])
Nt = madd(kron(N1, eye(2)), kron(eye(2), N1))
ok_uni = kernel(N1).dim == 1 and kernel(Nt).dim == 2
Kt = kernel(Nt)
ok_uni &= Kt.contains(span_kron(kernel(N1), kernel(N1)))
sig = diag([-1, -1])      # finite-order inertia acting by chi (+) chi^{-1}, chi(sigma) = -1
ok_fin = kernel(msub(sig, eye(2))).dim == 0 and kernel(msub(kron(sig, sig), eye(4))).dim == 4
ww_, rr_, bt = sp.symbols("w r beta", real=True)
alg = sp.simplify(sp.solve(sp.Eq(rr_ * ww_ / 2, (rr_ * bt + 2) / 2), ww_)[0] - (bt + 2 / rr_)) == 0
check("C37", "DLM8.6: (V^I)^{(x)r} is contained in (V^{(x)r})^I and is generally smaller (unipotent S_1: 1 < 2; "
      "finite-order chi+chi^{-1}: 0 < 4); DLM8.7 algebra |a|^r <= N^{(r beta+2)/2} <=> w <= beta + 2/r",
      ok_uni and ok_fin and alg)

# =====================================================================
# DLM10 : Jordan-string vector, dual eigenvalue, algebraic core lemma
# =====================================================================
print("\n--- DLM10: the Jordan-string vector, the dual primitive eigenvalue, the purity criterion")

ok_z = True
Qq = Fr(7)
alpha_ = Fr(3, 5)
for j in range(0, 6):
    m = string_model([(j, 0)])
    n = m["n"]
    N = m["N"]
    Fdiag = diag([alpha_ * Qq ** ((k + j) // 2) for k in m["lvl"]])   # F e_{-j} = alpha e_{-j}
    ok_z &= mmul(mmul(Fdiag, N), inv(Fdiag)) == msc(1 / Qq, N)
    ytop = [Fr(int(t == 0)) for t in range(n)]
    z = [Fr(0)] * (n * n)
    for s in range(0, j + 1):
        v1 = mv(mpow(N, s), ytop)
        v2 = mv(mpow(N, j - s), ytop)
        z = [a + ((-1) ** s) * b for a, b in zip(z, vkron(v1, v2))]
    Nt = madd(kron(N, eye(n)), kron(eye(n), N))
    Ft = kron(Fdiag, Fdiag)
    ok_z &= any(x != 0 for x in z)
    ok_z &= all(x == 0 for x in mv(Nt, z))
    ok_z &= mv(Ft, z) == [alpha_ ** 2 * Qq ** j * x for x in z]
    # degree 0: z lies in the span of e_k (x) e_{-k}
    lv = [a + b for a in m["lvl"] for b in m["lvl"]]
    ok_z &= all(z[i] == 0 or lv[i] == 0 for i in range(n * n))
    # dual: lowest vector of V* in degree -j is e_j^*, with eigenvalue alpha^{-1} Q^{-j}
    Fd = inv(tr(Fdiag))
    Nd = msc(-1, tr(N))
    estar = [Fr(int(t == 0)) for t in range(n)]            # e_j^* (dual of the top vector)
    ok_z &= all(x == 0 for x in mv(Nd, estar))
    ok_z &= mv(Fd, estar) == [x / (alpha_ * Qq ** j) for x in estar]
check("C38", "DLM10.2: z = sum_s (-1)^s N^s y (x) N^{j-s} y (y = top of a j-string) is nonzero, killed by N(x)1+1(x)N, "
      "of degree 0, and has eigenvalue Q^j alpha^2; P_{-j}(V*) has eigenvalue alpha^{-1}Q^{-j} (Q=7, alpha=3/5)", ok_z)

bb_, jj = sp.symbols("beta j", real=True)
wa = sp.symbols("w_alpha", real=True)
up = sp.solve(sp.Eq(2 * wa + 2 * jj, 2 * bb_), wa)[0]            # boundary of |alpha^2 Q^j| <= Q^beta
lowb = sp.solve(sp.Eq(-wa - 2 * jj, -bb_ - jj), wa)[0]           # boundary of |alpha^{-1}Q^{-j}| <= Q^{(-beta-j)/2}
check("C39", "DLM10.3-10.6 algebra: upper bound w(alpha) <= beta-j, lower bound w(alpha) >= beta-j, "
      "and Q^{(beta-j)/2} Q^{(i+j)/2} = Q^{(beta+i)/2}",
      sp.simplify(up - (bb_ - jj)) == 0 and sp.simplify(lowb - (bb_ - jj)) == 0
      and sp.simplify((bb_ - jj) + (sp.Symbol("i") + jj) - (bb_ + sp.Symbol("i"))) == 0)


def purity_criterion(specs, beta0):
    """(ii) of the extracted lemma: weights on ker N for V(x)V are <= 2beta and on ker N* for V*(x)V* are <= -2beta."""
    m = string_model(specs)
    mt = tensor_model(m, m)
    md = dual_model(m)
    mdt = tensor_model(md, md)
    k1 = kernel_weights(mt["N"], mt["w"])
    k2 = kernel_weights(mdt["N"], mdt["w"])
    return max(k1) <= 2 * beta0 and max(k2) <= -2 * beta0


def simple_criterion(specs, beta0):
    """bounds on ker N of V and V* only (no tensor square)."""
    m = string_model(specs)
    md = dual_model(m)
    return max(kernel_weights(m["N"], m["w"])) <= beta0 and max(kernel_weights(md["N"], md["w"])) <= -beta0


ok_equiv = True
count_pure = 0
for trial in range(40):
    beta0 = random.randint(-1, 1)
    specs = [(random.randint(0, 2), beta0 + random.choice([0, 0, 0, -1, 1])) for _ in range(random.randint(1, 2))]
    is_pure = all(c == beta0 for _, c in specs)
    count_pure += is_pure
    ok_equiv &= purity_criterion(specs, beta0) == is_pure
check("C40", "Extracted lemma (algebraic core of DLM10): for (V,N,F) with F N F^{-1}=Q^{-1}N, Gr^M_i is pure of weight "
      "beta+i for all i  <=>  ker N on V(x)V has weights <= 2beta and ker N* on V*(x)V* has weights <= -2beta",
      ok_equiv, f"{count_pure} pure and {40 - count_pure} impure random configurations")
neg = simple_criterion([(1, 1)], 0) and not purity_criterion([(1, 1)], 0)
check("C41", "Negative: the bounds on ker N of V and V* alone (the DLM8 input without the tensor square) do not force "
      "purity: a 1-string centred at beta+1 passes them but fails the tensor-square criterion", neg)

# =====================================================================
# DLM13 : positive combinations of commuting logarithms
# =====================================================================
print("\n--- DLM13: positive combinations of commuting logarithms")

m1 = string_model([(1, 0)])
m2 = string_model([(2, 0)])
mt = tensor_model(m1, m2)
A1 = kron(m1["N"], eye(m2["n"]))
A2 = madd(kron(m1["N"], eye(m2["n"])), kron(eye(m1["n"]), m2["N"]))
Mw = weight_filt(mt["w"])
ok_pos = True
for c1, c2 in ((1, 1), (2, 1), (1, 3), (Fr(1, 2), 5)):
    Nc = madd(msc(c1, A1), msc(c2, A2))
    Mc = mono_filt(Nc)
    ok_pos &= all(Mc(i) == Mw(i) for i in range(-5, 6))
differs = []
for c1, c2 in ((1, 0), (1, -1)):
    Nc = madd(msc(c1, A1), msc(c2, A2))
    Mc = mono_filt(Nc)
    differs.append(any(Mc(i) != Mw(i) for i in range(-5, 6)))
check("C42", "DLM13: for commuting N1 = N(x)1, N2 = N(x)1+1(x)N on S_1(x)S_2 the filtration of c1N1+c2N2 equals the "
      "weight filtration for positive (c1,c2); it differs for (1,0) and (1,-1)", ok_pos and all(differs))

# =====================================================================
# BRIDGES : commuting counting operators, regraded operators, ramification operators
# =====================================================================
print("\n--- BRIDGES: W_p (commuting), p^rho S_p (regraded), P_b (ramification)")

# (a) commuting operator: no weight scale; unipotent corrections are not conjugate
N = jordan([3])
Wc = eye(3)
ok_a = mmul(mmul(Wc, N), inv(Wc)) == N
F_corr = mmul(expnil(N, 1), Wc)
ok_a &= rank(msub(F_corr, eye(3))) != rank(msub(Wc, eye(3)))   # exp(N)W not conjugate to W
Wblk = diag([2, 2, 5, 5])                                      # commutes with N = J_2 (+) J_2
Nb = jordan([2, 2])
ok_a &= mmul(Wblk, Nb) == mmul(Nb, Wblk)
E2 = kernel(msub(Wblk, msc(2, eye(4))))
ok_a &= E2.contains(image(Nb, E2)) and image(Nb, E2).dim > 0      # N preserves, does not lower, eigen-filtration
# any W in the commutant of a single Jordan block is a polynomial a + bN + cN^2: one eigenvalue on every Gr_i,
# so 'Gr_i pure of W-weight beta+i' is impossible unless N = 0
N3 = jordan([3])
M3 = mono_filt(N3)
for (a0, b0, c0) in ((2, 1, 0), (5, -3, 7), (Fr(1, 3), 0, 2)):
    Wpoly = madd(madd(msc(a0, eye(3)), msc(b0, N3)), msc(c0, mpow(N3, 2)))
    ok_a &= mmul(Wpoly, N3) == mmul(N3, Wpoly)
    # W preserves every M_i (M is built from N only), so its eigenvalues on each Gr_i lie among those on V;
    # W - a0 is nilpotent, hence a0 is the only eigenvalue on V and on every Gr_i
    ok_a &= all(M3(i).contains(image(Wpoly, M3(i))) for i in range(-3, 3))
    ok_a &= rank(mpow(msub(Wpoly, msc(a0, eye(3))), 3)) == 0
check("C43", "Bridge (a): an operator W commuting with N has Q=1: mu = lam/(1-Q^{-n}) is undefined, exp(lam N)W need not "
      "be conjugate to W, N preserves (does not lower) the eigenvalue filtration of W, and on a Jordan block W has a "
      "single eigenvalue on all Gr_i (so Gr_i cannot have weight beta+i unless N=0)", ok_a)

# (a') regraded operator p^rho S_p on Jordan blocks: S_p eps^j = p^{-j} eps^j, N eps^j = eps^{j+1}
pP = Fr(3)
ok_s = True
for dlen in (1, 2, 3, 4):
    Nj = jordan([dlen + 1])            # basis eps^0..eps^d, N eps^j = eps^{j+1}
    Sp = diag([pP ** (-j) for j in range(dlen + 1)])
    ok_s &= mmul(mmul(Sp, Nj), inv(Sp)) == msc(1 / pP, Nj)
    ok_s &= mmul(Nj, Sp) == msc(pP, mmul(Sp, Nj))                  # the form N P = b P N with b = p
# weights of p^rho S_p on level j: 2rho - 2j; monodromy degree of eps^j: d - 2j; centre 2rho - d
two_blocks_const_rho = [(1, 2 * 1 - 1), (3, 2 * 1 - 3)]            # rho = 1: centres 1 and -1
pure_regraded = [(1, 0), (3, 0)]                                   # rho_b = (0 + d_b)/2: centre 0
ok_s &= (not any(purity_criterion(two_blocks_const_rho, b0) for b0 in range(-3, 4)))
ok_s &= purity_criterion(pure_regraded, 0)
# p^{H/2}: H eps^j = (d-2j) eps^j ; its weights coincide with the monodromy degrees
for dlen in (1, 2, 3):
    Nj = jordan([dlen + 1])
    lvl = [dlen - 2 * j for j in range(dlen + 1)]
    Mm = mono_filt(Nj)
    ok_s &= all(Mm(i) == weight_filt(lvl)(i) for i in range(-dlen - 1, dlen + 1))
check("C44", "Bridge (a'): S_p N S_p^{-1} = p^{-1} N; with one scalar rho on blocks of different lengths the centres "
      "2rho-d differ and the DLM10 purity criterion fails for every beta; with rho_b = (beta+d_b)/2 (e.g. P = p^{H/2}) "
      "it holds and the P-weight filtration is the monodromy filtration", ok_s)

# (b) ramification operators P_b with N P_b = b P_b N
ok_b = True
bP = Fr(9)
m = string_model([(2, 1), (1, 1), (0, 1)])
Pb = diag([Fr(3) ** x if x >= 0 else Fr(1, 3 ** (-x)) for x in m["w"]])   # |eigenvalue| = b^{w/2}
N = m["N"]
ok_b &= mmul(N, Pb) == msc(bP, mmul(Pb, N))
ok_b &= mmul(mmul(Pb, N), inv(Pb)) == msc(1 / bP, N)
for nn in (1, 2):
    lam = Fr(2, 3)
    mu = lam / (1 - bP ** (-nn))
    Pn = mpow(Pb, nn)
    ok_b &= mmul(mmul(expnil(N, mu), Pn), expnil(N, -mu)) == mmul(expnil(N, lam), Pn)
Mm = mono_filt(N)
ok_b &= all(Mm(i) == weight_filt(m["w"], shift=1)(i) for i in range(-4, 5))    # pure of weight 1 in base b
# |b| = 1: b = -1 on a string; P^2 = 1 and exp(N)P^2 is not conjugate to P^2
N3 = jordan([3])
Pm = diag([1, -1, 1])
ok_b &= mmul(mmul(Pm, N3), inv(Pm)) == msc(-1, N3)
ok_b &= rank(msub(mmul(expnil(N3, 1), mpow(Pm, 2)), eye(3))) != rank(msub(mpow(Pm, 2), eye(3)))
check("C45", "Bridge (b): N P_b = b P_b N <=> P_b N P_b^{-1} = b^{-1} N; for |b|>1 the DLM6 construction applies verbatim "
      "(lift-independence with mu = lam/(1-b^{-n})); for |b| = 1 it fails (b=-1: P^2=1 not conjugate to exp(N)P^2)", ok_b)

# =====================================================================
# Sensitivity controls: wrong variants must be detected
# =====================================================================
print("\n--- CONTROLS: deliberately wrong variants are detected (guards against vacuous PASS)")

ctrl = []
# tensor formula shifted by one
N1, _ = rand_nilpotent([3])
N2, _ = rand_nilpotent([2])
Nt = madd(kron(N1, eye(2)), kron(eye(3), N2))
M1, M2, Mt = mono_filt(N1), mono_filt(N2), mono_filt(Nt)
wrong = any(Mt(i) != sum((span_kron(M1(a), M2(i - a - 1)) for a in range(M1.lo, M1.hi + 1)), zero(6))
            for i in range(-4, 5))
ctrl.append(wrong)
# dual formula without the -1 shift
N_, _ = rand_nilpotent([3, 1])
M_ = mono_filt(N_)
Ms_ = mono_filt(msc(-1, tr(N_)))
ctrl.append(any(Ms_(i) != ann(M_(-i)) for i in range(-3, 4)))
# purity criterion with the wrong centre
ctrl.append(not purity_criterion([(2, 0), (1, 0)], 1) and not purity_criterion([(2, 0), (1, 0)], -1))
# relative recursion with a trivial W (single degree) does not return the mixed weight filtration
m = string_model([(1, 1), (0, -1)])
Nmix = madd(m["N"], zeros(3, 3))
Wtriv = {0: full(3)}
Mr_triv = rel_mono(Nmix, Wtriv, [0])
Mw_ = weight_filt(m["w"])
ctrl.append(any(Mr_triv(i) != Mw_(i) for i in range(-4, 5)))
# positive twist sign in DLM3.2 disagrees with computed weights for a 2-string
m = string_model([(2, 0)])
M = mono_filt(m["N"])
grw = weight_space_dims(M, m["w"], 2)
pw = prim_weight_dims(m["N"], M, m["w"], -2)
ctrl.append({ww - (2 + 2): dd for ww, dd in pw.items()} != grw and {ww + (2 + 2): dd for ww, dd in pw.items()} == grw)
check("C46", "Controls: an off-by-one tensor formula, a dual formula without the shift, the wrong centre in the purity "
      "criterion, a trivial W in the relative recursion, and the positive twist sign are all detected as mismatches",
      all(ctrl), f"individual controls: {ctrl}")

# =====================================================================
print("\n" + "=" * 78)
npass = sum(1 for _, _, o in RESULTS if o)
print(f"SUMMARY: {npass} PASS, {len(RESULTS) - npass} FAIL, {len(RESULTS)} checks")
print("=" * 78)
