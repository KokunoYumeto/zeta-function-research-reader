#!/usr/bin/env python3
# Checks for claude-ab note 39_ (audit of CGS4-CGS10 of SOURCE_COEFFICIENT_GLUE.md and DCP4-DCP12 of SOURCE_CC_DOUBLE_PULLBACK.md).
# Written by a subagent in the first-pass audit (25 September 2026) and copied unchanged below this header by Claude
# (claude-ab lane), model claude-opus-5-5 (Opus 5.5) at maximum reasoning effort. Re-run at 19:41 UTC: 83/83 PASS,
# output identical to the first run. Item labels are the ones cited in 39_.
# cgs_dcp_checks.py -- verification items for the audit of
#   CGS4-CGS10 of SOURCE_COEFFICIENT_GLUE.md (lines 133-441) and
#   DCP4-DCP12 + three dated appendices of SOURCE_CC_DOUBLE_PULLBACK.md (lines 160-522).
# Self-contained: exact rational linear algebra (fractions), sympy (Smith normal form), mpmath.
# Item groups:  L = library validation, C = CGS, D = DCP (each run in two finite Mellin models),
#               E = extractable lemmas on random data, N = negative results, Z = numerical zeta inputs.
# Output: cgs_dcp_checks_OUTPUT.txt in the same folder.
# Library: exact finite linear algebra over Q and sheaves on finite T0 spaces.
#
# A sheaf on a finite T0 space is the same thing as a functor on its specialisation
# poset: x -> y iff y lies in the minimal open neighbourhood U_x.  Sections over an
# open W are the limit over W.  Cohomology is computed by the Roos (cosimplicial)
# complex, which is Gamma of the flabby resolution
#     C^n(F)(W) = prod over chains x_0 < ... < x_n with x_0 in W of F(x_n);
# supported cohomology is the subcomplex of chains starting in Z.  The Godement
# resolution (sum of point pushforwards) is implemented independently for a cross-check.
# Ext groups between functors are computed by the normalised bar complex.
from fractions import Fraction as Fr
import itertools


class Mat:
    __slots__ = ('r', 'c', 'a')

    def __init__(self, r, c, a=None):
        self.r, self.c = r, c
        self.a = a if a is not None else [[Fr(0)] * c for _ in range(r)]

    @classmethod
    def of(cls, rows, c=None):
        rows = [[Fr(x) for x in row] for row in rows]
        return cls(len(rows), c if c is not None else (len(rows[0]) if rows else 0), rows)

    @classmethod
    def eye(cls, n):
        M = cls(n, n)
        for i in range(n):
            M.a[i][i] = Fr(1)
        return M

    def copy(self):
        return Mat(self.r, self.c, [row[:] for row in self.a])

    def __mul__(self, o):
        if isinstance(o, Mat):
            assert self.c == o.r, ('shape', self.r, self.c, o.r, o.c)
            res = Mat(self.r, o.c)
            for i in range(self.r):
                ai, ri = self.a[i], res.a[i]
                for k in range(self.c):
                    x = ai[k]
                    if x:
                        ok = o.a[k]
                        for j in range(o.c):
                            y = ok[j]
                            if y:
                                ri[j] += x * y
            return res
        f = Fr(o)
        return Mat(self.r, self.c, [[f * x for x in row] for row in self.a])

    def __rmul__(self, o):
        return self.__mul__(o)

    def __add__(self, o):
        assert (self.r, self.c) == (o.r, o.c)
        return Mat(self.r, self.c, [[x + y for x, y in zip(r1, r2)] for r1, r2 in zip(self.a, o.a)])

    def __sub__(self, o):
        assert (self.r, self.c) == (o.r, o.c)
        return Mat(self.r, self.c, [[x - y for x, y in zip(r1, r2)] for r1, r2 in zip(self.a, o.a)])

    def __neg__(self):
        return self * (-1)

    @property
    def T(self):
        return Mat(self.c, self.r, [[self.a[i][j] for i in range(self.r)] for j in range(self.c)])

    def is_zero(self):
        return all(x == 0 for row in self.a for x in row)

    def __eq__(self, o):
        return isinstance(o, Mat) and (self.r, self.c) == (o.r, o.c) and self.a == o.a

    def col(self, j):
        return Mat(self.r, 1, [[self.a[i][j]] for i in range(self.r)])

    def sub(self, rows, cols):
        rows, cols = list(rows), list(cols)
        return Mat(len(rows), len(cols), [[self.a[i][j] for j in cols] for i in rows])

    def setblock(self, i0, j0, B, add=True):
        for i in range(B.r):
            for j in range(B.c):
                if add:
                    self.a[i0 + i][j0 + j] += B.a[i][j]
                else:
                    self.a[i0 + i][j0 + j] = B.a[i][j]

    def tofloat(self):
        return [[float(x) for x in row] for row in self.a]


def hstack(*Ms):
    Ms = [M for M in Ms]
    r = Ms[0].r
    assert all(M.r == r for M in Ms)
    return Mat(r, sum(M.c for M in Ms), [sum((M.a[i] for M in Ms), []) for i in range(r)])


def vstack(*Ms):
    c = Ms[0].c
    assert all(M.c == c for M in Ms)
    return Mat(sum(M.r for M in Ms), c, [row[:] for M in Ms for row in M.a])


def blockdiag(*Ms):
    R = Mat(sum(M.r for M in Ms), sum(M.c for M in Ms))
    i = j = 0
    for M in Ms:
        R.setblock(i, j, M, add=False)
        i += M.r
        j += M.c
    return R


def kron(A, B):
    R = Mat(A.r * B.r, A.c * B.c)
    for i in range(A.r):
        for j in range(A.c):
            x = A.a[i][j]
            if x:
                for k in range(B.r):
                    for l in range(B.c):
                        R.a[i * B.r + k][j * B.c + l] = x * B.a[k][l]
    return R


def rref(M):
    A = [row[:] for row in M.a]
    r, c = M.r, M.c
    piv, row = [], 0
    for col in range(c):
        if row == r:
            break
        p = next((i for i in range(row, r) if A[i][col] != 0), None)
        if p is None:
            continue
        A[row], A[p] = A[p], A[row]
        pv = A[row][col]
        A[row] = [x / pv for x in A[row]]
        for i in range(r):
            if i != row and A[i][col] != 0:
                f = A[i][col]
                A[i] = [x - f * y for x, y in zip(A[i], A[row])]
        piv.append(col)
        row += 1
    return Mat(r, c, A), piv


def rank(M):
    if M.r == 0 or M.c == 0:
        return 0
    return len(rref(M)[1])


def nullspace(M):
    """columns spanning ker M (M.c x k)"""
    if M.r == 0:
        return Mat.eye(M.c)
    R, piv = rref(M)
    free = [j for j in range(M.c) if j not in piv]
    N = Mat(M.c, len(free))
    for k, f in enumerate(free):
        N.a[f][k] = Fr(1)
        for i, p in enumerate(piv):
            N.a[p][k] = -R.a[i][f]
    return N


def colbasis(M):
    if M.c == 0 or M.r == 0:
        return Mat(M.r, 0)
    R, piv = rref(M)
    return M.sub(range(M.r), piv)


def solve(M, B):
    """X with M X = B, or None"""
    if M.c == 0:
        return Mat(0, B.c) if B.is_zero() else None
    R, piv = rref(hstack(M, B))
    if any(p >= M.c for p in piv):
        return None
    X = Mat(M.c, B.c)
    for i, p in enumerate(piv):
        for j in range(B.c):
            X.a[p][j] = R.a[i][M.c + j]
    return X


def in_span(M, v):
    return solve(M, v) is not None


class Cohom:
    """H at C^n of a complex, with incoming d_in: C^{n-1}->C^n and outgoing d_out: C^n->C^{n+1}."""

    def __init__(self, dim, d_in=None, d_out=None):
        Z = nullspace(d_out) if (d_out is not None and d_out.r > 0) else Mat.eye(dim)
        B = colbasis(d_in) if (d_in is not None and d_in.c > 0) else Mat(dim, 0)
        cur, Hc = B, []
        for j in range(Z.c):
            z = Z.col(j)
            test = hstack(cur, z) if cur.c else z
            if rank(test) > cur.c:
                cur = test
                Hc.append(z)
        self.dimC = dim
        self.B = B
        self.H = hstack(*Hc) if Hc else Mat(dim, 0)
        self.BH = cur
        self.dim = len(Hc)

    def coords(self, V):
        """coordinates (dim x k) of the classes of the cocycles V (dimC x k)"""
        if V.c == 0:
            return Mat(self.dim, 0)
        X = solve(self.BH, V)
        assert X is not None, 'not a cocycle'
        return X.sub(range(self.B.c, self.BH.c), range(V.c))


def complex_ok(ds):
    return all((ds[n + 1] * ds[n]).is_zero() for n in range(len(ds) - 1))


def hdims(dims, ds):
    rk = [rank(d) for d in ds]
    out = []
    for n in range(len(dims)):
        rin = rk[n - 1] if 0 <= n - 1 < len(rk) else 0
        rout = rk[n] if n < len(rk) else 0
        out.append(dims[n] - rin - rout)
    return out


class FinSpace:
    def __init__(self, pts, U):
        self.pts = list(pts)
        self.U = {x: frozenset(U[x]) for x in self.pts}
        for x in self.pts:
            assert x in self.U[x]
            for y in self.U[x]:
                assert self.U[y] <= self.U[x], 'minimal opens not transitive'

    def lt(self, x, y):
        return x != y and y in self.U[x]

    def is_open(self, W):
        return all(self.U[x] <= W for x in W)

    def opens(self):
        res = []
        for k in range(len(self.pts) + 1):
            for W in itertools.combinations(self.pts, k):
                W = frozenset(W)
                if self.is_open(W):
                    res.append(W)
        return res

    def srt(self, W):
        return [x for x in self.pts if x in W]

    def chains(self, W, n):
        Wl = self.srt(W)
        out = []

        def ext(ch):
            if len(ch) == n + 1:
                out.append(tuple(ch))
                return
            for y in Wl:
                if self.lt(ch[-1], y):
                    ext(ch + [y])
        for x in Wl:
            ext([x])
        return out

    def min_open(self, S):
        res = set()
        for x in S:
            res |= self.U[x]
        return frozenset(res)


class Sheaf:
    """functor on the specialisation poset; maps[(x,y)] : F(x) -> F(y) for y in U_x, y != x"""

    def __init__(self, X, dims, maps):
        self.X = X
        self.dims = dict(dims)
        self.maps = {}
        for x in X.pts:
            for y in X.pts:
                if X.lt(x, y):
                    m = maps[(x, y)]
                    assert (m.r, m.c) == (self.dims[y], self.dims[x]), ('map shape', x, y)
                    self.maps[(x, y)] = m

    def M(self, x, y):
        return Mat.eye(self.dims[x]) if x == y else self.maps[(x, y)]

    def functorial(self):
        X = self.X
        for x in X.pts:
            for y in X.pts:
                for z in X.pts:
                    if X.lt(x, y) and X.lt(y, z):
                        if not (self.M(y, z) * self.M(x, y) == self.M(x, z)):
                            return False
        return True

    def layout(self, W):
        pts = self.X.srt(W)
        off, t = {}, 0
        for x in pts:
            off[x] = t
            t += self.dims[x]
        return pts, off, t

    def sections(self, W):
        """basis (columns) of Gamma(W,F) inside the sum of stalks over W"""
        X = self.X
        pts, off, t = self.layout(W)
        blocks = []
        for x in pts:
            for y in pts:
                if X.lt(x, y):
                    row = Mat(self.dims[y], t)
                    row.setblock(0, off[x], self.M(x, y))
                    row.setblock(0, off[y], -Mat.eye(self.dims[y]))
                    blocks.append(row)
        C = vstack(*blocks) if blocks else Mat(0, t)
        return nullspace(C), pts, off, t

    def roos(self, W, Z=None, nmax=None):
        """Roos complex of F on the open W (chains in W); if Z is given, the subcomplex of
        chains starting in Z (= Gamma_Z of the flabby Roos resolution)."""
        X = self.X
        if nmax is None:
            nmax = len(W) + 1
        CH, OFF, dims = [], [], []
        for n in range(nmax + 1):
            ch = [s for s in X.chains(W, n) if Z is None or s[0] in Z]
            off, t = {}, 0
            for s in ch:
                off[s] = t
                t += self.dims[s[-1]]
            CH.append(ch)
            OFF.append(off)
            dims.append(t)
        ds = []
        for n in range(nmax):
            D = Mat(dims[n + 1], dims[n])
            for s in CH[n + 1]:
                r0 = OFF[n + 1][s]
                for i in range(n + 2):
                    tau = s[:i] + s[i + 1:]
                    if tau not in OFF[n]:
                        continue
                    sg = (-1) ** i
                    blk = self.M(s[n], s[n + 1]) if i == n + 1 else Mat.eye(self.dims[s[-1]])
                    D.setblock(r0, OFF[n][tau], blk * sg)
            ds.append(D)
        return dims, ds, CH, OFF

    def H(self, W, Z=None, nmax=None):
        dims, ds, _, _ = self.roos(W, Z, nmax)
        return hdims(dims, ds)


def roos_map(phi, F, G, CH, OFF_F, OFF_G, n):
    """chain map induced in degree n by a natural transformation phi (dict x->Mat)"""
    tf = sum(F.dims[s[-1]] for s in CH[n])
    tg = sum(G.dims[s[-1]] for s in CH[n])
    Mx = Mat(tg, tf)
    for s in CH[n]:
        Mx.setblock(OFF_G[n][s], OFF_F[n][s], phi[s[-1]])
    return Mx


def is_natural(phi, F, G):
    X = F.X
    for x in X.pts:
        for y in X.pts:
            if X.lt(x, y):
                if not (phi[y] * F.M(x, y) == G.M(x, y) * phi[x]):
                    return False
    return True


def direct_sum(*Fs):
    X = Fs[0].X
    dims = {x: sum(F.dims[x] for F in Fs) for x in X.pts}
    maps = {}
    for x in X.pts:
        for y in X.pts:
            if X.lt(x, y):
                maps[(x, y)] = blockdiag(*[F.M(x, y) for F in Fs])
    return Sheaf(X, dims, maps)


def godement_complex(F, W, Z=None, N=4):
    """Gamma_Z(W, G^*(F)) for the Godement resolution G(F)(z) = sum_{x in U_z} F(x).
    Returns dims and differentials of the complex (degrees 0..N-1)."""
    X = F.X
    stages = []
    cur = F
    for n in range(N + 1):
        q, rinv, newdims = {}, {}, {}
        for z in X.pts:
            Uz = X.srt(X.U[z])
            e = vstack(*[cur.M(z, x) for x in Uz]) if Uz else Mat(0, cur.dims[z])
            Lq = nullspace(e.T).T if e.r else Mat(0, 0)
            q[z] = Lq
            newdims[z] = Lq.r
            rinv[z] = solve(Lq, Mat.eye(Lq.r)) if Lq.r else Mat(e.r, 0)
        newmaps = {}
        for z in X.pts:
            for z2 in X.pts:
                if X.lt(z, z2):
                    Uz, Uz2 = X.srt(X.U[z]), X.srt(X.U[z2])
                    offz, t = {}, 0
                    for x in Uz:
                        offz[x] = t
                        t += cur.dims[x]
                    P = Mat(sum(cur.dims[x] for x in Uz2), t)
                    rr = 0
                    for x in Uz2:
                        P.setblock(rr, offz[x], Mat.eye(cur.dims[x]))
                        rr += cur.dims[x]
                    newmaps[(z, z2)] = q[z2] * P * rinv[z]
        stages.append((cur, q))
        cur = Sheaf(X, newdims, newmaps)
    keep = [x for x in X.srt(W) if (Z is None or x in Z)]
    dims, ds = [], []
    for n in range(N):
        Fn, qn = stages[n]
        dims.append(sum(Fn.dims[x] for x in keep))
    for n in range(N - 1):
        Fn, qn = stages[n]
        Fn1 = stages[n + 1][0]
        offn, t = {}, 0
        for x in keep:
            offn[x] = t
            t += Fn.dims[x]
        offn1, t1 = {}, 0
        for x in keep:
            offn1[x] = t1
            t1 += Fn1.dims[x]
        D = Mat(t1, t)
        for z in keep:
            Uz = X.srt(X.U[z])
            cz = 0
            for x in Uz:
                if x in offn:
                    D.setblock(offn1[z], offn[x], qn[z].sub(range(qn[z].r), range(cz, cz + Fn.dims[x])))
                cz += Fn.dims[x]
        ds.append(D)
    return dims, ds


def ext_complex(F, G, nmax):
    """normalised bar complex: C^n = sum over chains x0<..<xn of Hom(F(x0), G(xn))"""
    X = F.X
    CH, OFF, dims = [], [], []
    for n in range(nmax + 2):
        ch = X.chains(X.pts, n)
        off, t = {}, 0
        for s in ch:
            off[s] = t
            t += G.dims[s[-1]] * F.dims[s[0]]
        CH.append(ch)
        OFF.append(off)
        dims.append(t)
    ds = []
    for n in range(nmax + 1):
        D = Mat(dims[n + 1], dims[n])
        for s in CH[n + 1]:
            r0 = OFF[n + 1][s]
            g, f0 = G.dims[s[-1]], F.dims[s[0]]
            for i in range(n + 2):
                tau = s[:i] + s[i + 1:]
                sg = (-1) ** i
                if i == 0:
                    blk = kron(Mat.eye(g), F.M(s[0], s[1]).T)
                elif i == n + 1:
                    blk = kron(G.M(s[n], s[n + 1]), Mat.eye(f0))
                else:
                    blk = Mat.eye(g * f0)
                D.setblock(r0, OFF[n][tau], blk * sg)
        ds.append(D)
    return dims, ds


def ext_dims(F, G, nmax):
    dims, ds = ext_complex(F, G, nmax)
    return hdims(dims[:nmax + 1], ds[:nmax + 1])[:nmax + 1]


# ============================================================================================
# Main body: numbered checks.
# ============================================================================================
import random
import mpmath as mp
from sympy import Matrix as SMatrix, ZZ
from sympy.matrices.normalforms import smith_normal_form

RES = []


def report(tag, ok, detail=''):
    RES.append((tag, bool(ok)))
    print(('PASS ' if ok else 'FAIL ') + tag + ('  -- ' + detail if detail else ''), flush=True)


random.seed(20260925)


def rmat(r, c, lo=-3, hi=3):
    return Mat.of([[random.randint(lo, hi) for _ in range(c)] for _ in range(r)], c=c)


def nat_solve(F, G, lin):
    """Solve for natural transformations phi: F -> G subject to linear constraints
    lin = [(x, L, R, T)] meaning L phi_x R = T.  Returns (solvable, nullity, solution dict)."""
    X = F.X
    off, t = {}, 0
    for x in X.pts:
        off[x] = t
        t += G.dims[x] * F.dims[x]
    rows, rhs = [], []

    def addeq(blocks, target):
        # blocks: list of (x, K) with K acting on vec(phi_x); target: Mat (k x 1)
        k = target.r
        Row = Mat(k, t)
        for x, K in blocks:
            Row.setblock(0, off[x], K)
        rows.append(Row)
        rhs.append(target)
    for x in X.pts:
        for y in X.pts:
            if X.lt(x, y):
                K1 = kron(Mat.eye(G.dims[y]), F.M(x, y).T)
                K2 = kron(G.M(x, y), Mat.eye(F.dims[x]))
                n = G.dims[y] * F.dims[x]
                addeq([(y, K1), (x, -K2)], Mat(n, 1))
    for (x, L, R, T) in lin:
        K = kron(L, R.T)
        vecT = Mat(T.r * T.c, 1, [[T.a[i][j]] for i in range(T.r) for j in range(T.c)])
        addeq([(x, K)], vecT)
    A = vstack(*rows) if rows else Mat(0, t)
    b = vstack(*rhs) if rhs else Mat(0, 1)
    sol = solve(A, b) if A.r else Mat(t, 1)
    nul = t - rank(A)
    if sol is None:
        return False, nul, None
    phi = {}
    for x in X.pts:
        g, f = G.dims[x], F.dims[x]
        phi[x] = Mat(g, f, [[sol.a[off[x] + i * f + j][0] for j in range(f)] for i in range(g)])
    return True, nul, phi


def ker_functor(phi, F):
    X = F.X
    k = {x: nullspace(phi[x]) if phi[x].r else Mat.eye(F.dims[x]) for x in X.pts}
    maps = {}
    for x in X.pts:
        for y in X.pts:
            if X.lt(x, y):
                maps[(x, y)] = solve(k[y], F.M(x, y) * k[x])
    return Sheaf(X, {x: k[x].c for x in X.pts}, maps), k


def coker_functor(phi, G):
    X = G.X
    q, qi = {}, {}
    for x in X.pts:
        im = phi[x]
        Lq = nullspace(im.T).T if im.c else Mat.eye(G.dims[x])
        q[x] = Lq
        qi[x] = solve(Lq, Mat.eye(Lq.r))
    maps = {}
    for x in X.pts:
        for y in X.pts:
            if X.lt(x, y):
                maps[(x, y)] = q[y] * G.M(x, y) * qi[x]
    return Sheaf(X, {x: q[x].r for x in X.pts}, maps), q, qi


# ---------------------------------------------------------------- the finite model of X ----
UPTS = ['p1', 'p2', 'eta']
UMIN = {'p1': ['p1', 'eta'], 'p2': ['p2', 'eta'], 'eta': ['eta']}
Ufin = FinSpace(UPTS, UMIN)
UU = frozenset(UPTS)
# the programme's X = U u {m}: m has X as its only neighbourhood
Xfin = FinSpace(['m'] + UPTS, dict(UMIN, m=['m'] + UPTS))
# R-modules = functors on P' = P_X u {m'}: the (1-eps)-part of the full stalk sits at m'
Pp = FinSpace(['m', "m'"] + UPTS, dict(UMIN, m=['m'] + UPTS, **{"m'": ["m'"]}))
XP = frozenset(Pp.pts)
ZP = frozenset(['m', "m'"])
zeroU = Sheaf(Ufin, {x: 0 for x in UPTS}, {('p1', 'eta'): Mat(0, 0), ('p2', 'eta'): Mat(0, 0)})


def sheafU(d1, d2, de, M1=None, M2=None):
    M1 = M1 if M1 is not None else rmat(de, d1)
    M2 = M2 if M2 is not None else rmat(de, d2)
    return Sheaf(Ufin, {'p1': d1, 'p2': d2, 'eta': de}, {('p1', 'eta'): M1, ('p2', 'eta'): M2})


def glue(G, ap, am, R=None):
    """CGS1.3: the sheaf M(G, A_+, A_-, r) with r = S R (S = basis of Gamma(U,G))."""
    S, pts, off, t = G.sections(UU)
    if R is None:
        R = Mat(S.c, ap)
    r = S * R
    dims = {'m': ap, "m'": am}
    dims.update(G.dims)
    maps = {}
    for x in UPTS:
        maps[('m', x)] = r.sub(range(off[x], off[x] + G.dims[x]), range(ap))
    for k, M in G.maps.items():
        maps[k] = M
    return Sheaf(Pp, dims, maps)


def jshriek(G):
    return glue(G, 0, 0)


def jstar(G):
    S = G.sections(UU)[0]
    return glue(G, S.c, 0, Mat.eye(S.c))


def istar(ap, am):
    return glue(zeroU, ap, am)


def h_U(G, n=3):
    return G.H(UU, None, n)


print('=' * 100)
print('Checks for the audit of CGS4-CGS10 and DCP4-DCP12 (+ appendices).  Exact arithmetic over Q')
print('unless marked numerical.  Finite model X_fin = {m, p1, p2, eta}: the only open containing m is X_fin.')
print('=' * 100)

# ------------------------------------------------------------------ L: library validation --
ok = [W for W in Xfin.opens()] == [frozenset(), frozenset(['eta']), frozenset(['p1', 'eta']),
                                   frozenset(['p2', 'eta']), frozenset(['p1', 'p2', 'eta']), frozenset(Xfin.pts)]
report('L0  finite model: the opens of X_fin are the opens of U_fin and X_fin itself (CGS0)', ok,
       '%d opens' % len(Xfin.opens()))

agree, tried, d2 = True, 0, True
for trial in range(12):
    G = sheafU(random.randint(0, 3), random.randint(0, 3), random.randint(0, 3))
    ap = random.randint(0, 3)
    F = glue(G, ap, random.randint(0, 2), rmat(G.sections(UU)[0].c, ap))
    for W, Z in [(XP, None), (XP, ZP), (UU, None)]:
        dims, ds, _, _ = F.roos(W, Z)
        d2 &= complex_ok(ds)
        hR = hdims(dims, ds)[:3]
        hG = hdims(*godement_complex(F, W, Z, 5))[:3]
        agree &= (hR == hG)
        tried += 1
report('L1  Roos complex (flabby resolution by chains) has d^2 = 0 and agrees with the Godement resolution',
       agree and d2, '%d (sheaf, open, support) triples, degrees 0-2' % tried)

okx = True
for trial in range(6):
    G = sheafU(random.randint(0, 2), random.randint(0, 2), random.randint(0, 2))
    ap = random.randint(0, 2)
    F = glue(G, ap, random.randint(0, 2), rmat(G.sections(UU)[0].c, ap))
    G2 = sheafU(random.randint(0, 2), random.randint(0, 2), random.randint(0, 2))
    ap2 = random.randint(0, 2)
    F2 = glue(G2, ap2, random.randint(0, 2), rmat(G2.sections(UU)[0].c, ap2))
    dims, ds = ext_complex(F, F2, 3)
    okx &= complex_ok(ds)
    e0 = ext_dims(F, F2, 2)[0]
    okx &= (e0 == nat_solve(F, F2, [])[1])
    # representable projective P_x: Ext^n(P_x, F2) = F2(x) in degree 0 and 0 above
    for x in Pp.pts:
        Ux = Pp.U[x]
        P = Sheaf(Pp, {y: (1 if y in Ux else 0) for y in Pp.pts},
                  {(a, b): (Mat.eye(1) if a in Ux else Mat(1 if b in Ux else 0, 0))
                   for a in Pp.pts for b in Pp.pts if Pp.lt(a, b)})
        okx &= ext_dims(P, F2, 3) == [F2.dims[x], 0, 0, 0]
    # constant functor: Ext^n(Q_const, F2) = H^n(X, F2)
    C = Sheaf(Pp, {y: 1 for y in Pp.pts}, {(a, b): Mat.eye(1) for a in Pp.pts for b in Pp.pts if Pp.lt(a, b)})
    okx &= ext_dims(C, F2, 2) == F2.H(XP, None, 3)[:3]
report('L2  bar complex for Ext: d^2 = 0, Ext^0 = natural transformations, Ext(P_x,-) and Ext(const,-) correct', okx)

# ------------------------------------------------------------------ C: CGS4-CGS10 ----------
print('-' * 100)
print('CGS4-CGS10 (SOURCE_COEFFICIENT_GLUE.md, lines 133-441)')


def ext_maps(G, ap, am, M):
    """iota: j_!G -> M and pi: M -> i_*A as dicts"""
    J, I = jshriek(G), istar(ap, am)
    iota = {x: (Mat.eye(G.dims[x]) if x in UPTS else Mat(M.dims[x], 0)) for x in Pp.pts}
    pi = {x: (Mat.eye(M.dims[x]) if x in ('m', "m'") else Mat(0, M.dims[x])) for x in Pp.pts}
    return J, I, iota, pi


ok1 = ok2 = True
for trial in range(8):
    G = sheafU(random.randint(0, 3), random.randint(0, 3), random.randint(1, 3))
    hG = G.sections(UU)[0].c
    ap, am = random.randint(0, 3), random.randint(0, 2)
    R = rmat(hG, ap)
    M = glue(G, ap, am, R)
    J, I, iota, pi = ext_maps(G, ap, am, M)
    ok1 &= is_natural(iota, J, M) and is_natural(pi, M, I)
    for x in Pp.pts:
        ok1 &= rank(iota[x]) == J.dims[x] and rank(pi[x]) == I.dims[x] and \
            J.dims[x] + I.dims[x] == M.dims[x] and (pi[x] * iota[x]).is_zero()
    # CGS4.3: M = j_*G x_{i_* Gamma(U,G)} i_*A
    Js, IG = jstar(G), istar(hG, 0)
    alpha = {x: (Mat.eye(hG) if x == 'm' else Mat(IG.dims[x], Js.dims[x])) for x in Pp.pts}
    beta = {x: (R if x == 'm' else Mat(IG.dims[x], I.dims[x])) for x in Pp.pts}
    ok2 &= is_natural(alpha, Js, IG) and is_natural(beta, I, IG)
    SUM = direct_sum(Js, I)
    phi = {x: hstack(alpha[x], -beta[x]) for x in Pp.pts}
    P, kP = ker_functor(phi, SUM)
    can = {}
    for x in Pp.pts:
        if x == 'm':
            can[x] = vstack(R, Mat.eye(ap))
        elif x == "m'":
            can[x] = vstack(Mat(0, am), Mat.eye(am))
        else:
            can[x] = vstack(Mat.eye(G.dims[x]), Mat(0, G.dims[x]))
    ok2 &= is_natural(can, M, SUM)
    for x in Pp.pts:
        ok2 &= (phi[x] * can[x]).is_zero() and rank(can[x]) == M.dims[x] == P.dims[x]
report('C1  CGS4.1: 0 -> j_!G -> M -> i_*(A_+ + A_-) -> 0 is exact at every point (8 random data)', ok1)
report('C2  CGS4.3: M is canonically the fibre product j_*G x_{i_*Gamma(U,G)} i_*A (natural iso)', ok2)

# CGS4.4: classification of extensions, Baer sum, Ext dimensions, section criterion
ok3 = ok4 = ok5 = ok6 = True
details = []
for trial in range(6):
    if trial == 0:
        G = sheafU(0, 0, 1)                        # H^1(U,G) = 1: exercises CGS8.2 in degree 2
    elif trial == 1:
        G = sheafU(1, 1, 2)
    else:
        G = sheafU(random.randint(0, 3), random.randint(0, 3), random.randint(1, 3))
    hU = h_U(G)
    hG = hU[0]
    ap, am = random.randint(1, 2), random.randint(0, 2)
    R1, R2 = rmat(hG, ap), rmat(hG, ap)
    E1, E2 = glue(G, ap, am, R1), glue(G, ap, am, R2)
    J, I, i1, p1 = ext_maps(G, ap, am, E1)
    _, _, i2, p2 = ext_maps(G, ap, am, E2)
    # isomorphisms of extensions E1 -> E2 fixing both ends
    lin = [(x, Mat.eye(E2.dims[x]), i1[x], i2[x]) for x in Pp.pts] + \
          [(x, p2[x], Mat.eye(E1.dims[x]), p1[x]) for x in Pp.pts]
    solv, nul, _ = nat_solve(E1, E2, lin)
    solv_same, nul_same, phi_same = nat_solve(E1, E1, [(x, Mat.eye(E1.dims[x]), i1[x], i1[x]) for x in Pp.pts] +
                                              [(x, p1[x], Mat.eye(E1.dims[x]), p1[x]) for x in Pp.pts])
    ok3 &= (solv == (R1 == R2)) and solv_same and all(phi_same[x] == Mat.eye(E1.dims[x]) for x in Pp.pts)
    # Baer sum
    SUM12 = direct_sum(E1, E2)
    phi = {x: hstack(p1[x], -p2[x]) for x in Pp.pts}
    PB, kP = ker_functor(phi, SUM12)
    JJ = direct_sum(J, J)
    a = {x: solve(kP[x], blockdiag(i1[x], i2[x])) for x in Pp.pts}
    nabla = {x: hstack(Mat.eye(J.dims[x]), Mat.eye(J.dims[x])) for x in Pp.pts}
    JP = direct_sum(J, PB)
    psi = {x: vstack(nabla[x], -a[x]) for x in Pp.pts}
    EB, q, qi = coker_functor(psi, JP)
    iE = {x: q[x] * vstack(Mat.eye(J.dims[x]), Mat(PB.dims[x], J.dims[x])) for x in Pp.pts}
    piP = {x: p1[x] * kP[x].sub(range(E1.dims[x]), range(kP[x].c)) for x in Pp.pts}
    piE = {x: hstack(Mat(I.dims[x], J.dims[x]), piP[x]) * qi[x] for x in Pp.pts}
    good = is_natural(iE, J, EB) and is_natural(piE, EB, I)
    inv_m = solve(piE['m'], Mat.eye(ap))
    S, pts, off, t = G.sections(UU)
    rsum = S * (R1 + R2)
    for x in UPTS:
        rx = solve(iE[x], EB.M('m', x) * inv_m)
        good &= rx is not None and rx == rsum.sub(range(off[x], off[x] + G.dims[x]), range(ap))
    ok4 &= good
    # Ext dimensions (CGS4.4 in degree 1, CGS8.2 in all degrees)
    ed = ext_dims(istar(ap, am), J, 3)
    pred = [0, ap * hU[0], ap * hU[1], 0]
    ok5 &= ed == pred
    details.append('A_+=%d h(U,G)=%s Ext=%s' % (ap, hU[:2], ed))
    # section of M -> i_*A exists iff r = 0
    for RR in (R1, Mat(hG, ap)):
        Mx = glue(G, ap, am, RR)
        _, _, _, pix = ext_maps(G, ap, am, Mx)
        solv, _, _ = nat_solve(I, Mx, [(x, pix[x], Mat.eye(I.dims[x]), Mat.eye(I.dims[x])) for x in Pp.pts])
        ok6 &= (solv == RR.is_zero())
report('C3  CGS4.4: an isomorphism of extensions fixing both ends exists iff r = r\', and is then the identity', ok3)
report('C4  CGS4.4: the Baer sum (fibre product over i_*A, push-out along addition) has gluing map r1 + r2', ok4)
report('C5  CGS4.4 + CGS8.2: dim Ext^n(i_*A, j_!G) = dim(eps A) * dim H^{n-1}(U,G), n = 0..3', ok5,
       '; '.join(details[:3]))
report('C6  CGS4 (end): M -> i_*A has a section iff r = 0', ok6)

# CGS5: supported cohomology of a single sheaf
ok7 = ok8 = ok9 = ok10 = ok11 = True
det = []
for trial in range(8):
    if trial == 0:
        G = sheafU(0, 0, 1)
    elif trial == 1:
        G = sheafU(0, 1, 2)
    else:
        G = sheafU(random.randint(0, 3), random.randint(0, 3), random.randint(1, 3))
    hU = h_U(G, 3)
    S, pts, off, t = G.sections(UU)
    ap, am = random.randint(0, 3), random.randint(0, 2)
    R = rmat(S.c, ap, -1, 1)
    M = glue(G, ap, am, R)
    r = S * R
    rk = rank(r) if ap else 0
    hX = M.H(XP, None, 4)
    hZ = M.H(XP, ZP, 4)
    ok7 &= all(v == 0 for v in hX[1:4])
    pred = [am + (ap - rk), hU[0] - rk, hU[1], hU[2] if len(hU) > 2 else 0]
    ok8 &= hZ[:4] == pred
    det.append('hZ=%s pred=%s' % (hZ[:3], pred[:3]))
    # CGS5.3 model: K^0 = A_+ + A_-, K^q = B^{q-1}, d^0 = r, d^q = -d_B
    dB, dsB, _, _ = G.roos(UU, None, 3)
    Kd = [ap + am] + dB[:3]
    d0 = hstack(r, Mat(t, am))
    dsK = [d0] + [-D for D in dsB[:2]]
    ok9 &= complex_ok(dsK) and hdims(Kd, dsK)[:3] == hZ[:3]
    # CGS5.4 and the sign convention: snake-lemma boundary vs the text's (0,g)
    dP, dsP, CHP, OFFP = M.roos(XP, None, 3)
    dU, dsU, CHU, OFFU = M.roos(UU, None, 3)
    # restriction res: C(X) -> C(U) (projection onto chains in U); zero extension lift
    res = [Mat(dU[n], dP[n]) for n in range(3)]
    for n in range(3):
        for s in CHU[n]:
            res[n].setblock(OFFU[n][s], OFFP[n][s], Mat.eye(M.dims[s[-1]]))
    lift = [R_.T for R_ in res]
    # Fib (text convention): Fib^n = C^n(X) + C^{n-1}(U), d(x,u) = (dx, res x - du)
    fd = [dP[0], dP[1] + dU[0], dP[2] + dU[1]]
    dF0 = vstack(dsP[0], res[0])
    dF1 = blockdiag(dsP[1], -dsU[0])
    dF1.setblock(dP[2], 0, res[1])
    ok10 &= complex_ok([dF0, dF1])
    Hf1 = Cohom(fd[1], dF0, dF1)
    gam = [Mat(dU[0], 1, [[v] for v in col]) for col in zip(*S.a)] if S.c else []
    # (the augmentation Gamma(U,G) -> C^0(U) is the stalk vector: chains (x,) in the same order)
    for g in gam:
        # snake: lift by zero, apply d, the result is supported on chains starting in Z; kappa(z) = (z,0)
        z = dsP[0] * (lift[0] * g)
        kappa = vstack(z, Mat(dU[0], 1))
        # text: (0, g) in K^1 = B^0 mapped to Fib^1 by phi(b) = (0, b)
        text = vstack(Mat(dP[1], 1), g)
        ok10 &= (Hf1.coords(kappa) + Hf1.coords(text)).is_zero()
    # R^q j_* G: stalk at m = H^q(U,G), stalks on U vanish in positive degree
    for x in UPTS:
        ok11 &= all(v == 0 for v in G.H(Ufin.U[x], None, 3)[1:3])
report('C7  CGS5.1: H^q(X, M) = 0 for q >= 1 (8 random data, q = 1..3)', ok7)
report('C8  CGS5.2: H^0_Z = A_- + ker r, H^1_Z = coker r, H^q_Z = H^{q-1}(U,G) (q >= 2)', ok8, '; '.join(det[:3]))
report('C9  CGS5.3: the displayed supported complex K has d^2 = 0 and the cohomology of RGamma_Z', ok9)
report('C10 CGS5.4 sign convention: in the text\'s fibre convention the boundary g -> [(0,g)] equals MINUS the '
       'snake-lemma boundary (uniform; harmless)', ok10)
report('C11 CGS5.6: R^q j_*G vanishes on U for q >= 1 (its stalk at m is H^q(U,G))', ok11)

# CGS6: complexes, the full mapping fibre, CGS6.7, control
ok12 = ok13 = ok14 = True
ctrl = True
det = []
for trial in range(6):
    G0 = sheafU(random.randint(0, 2), random.randint(0, 2), random.randint(1, 2))
    G1 = sheafU(random.randint(0, 2), random.randint(0, 2), random.randint(1, 2))
    # random natural transformation g: G0 -> G1 (restricted to U)
    off, t = {}, 0
    for x in UPTS:
        off[x] = t
        t += G1.dims[x] * G0.dims[x]
    # build naturality system and take a random vector in its kernel
    rows = []
    for (x, y) in [('p1', 'eta'), ('p2', 'eta')]:
        K1 = kron(Mat.eye(G1.dims[y]), G0.M(x, y).T)
        K2 = kron(G1.M(x, y), Mat.eye(G0.dims[x]))
        Row = Mat(K1.r, t)
        Row.setblock(0, off[y], K1)
        Row.setblock(0, off[x], -K2)
        rows.append(Row)
    Nsp = nullspace(vstack(*rows))
    v = Nsp * rmat(Nsp.c, 1, -2, 2) if Nsp.c else Mat(t, 1)
    gU = {x: Mat(G1.dims[x], G0.dims[x], [[v.a[off[x] + i * G0.dims[x] + j][0] for j in range(G0.dims[x])]
                                          for i in range(G1.dims[x])]) for x in UPTS}
    assert is_natural(gU, G0, G1)
    S0, pts, off0, t0 = G0.sections(UU)
    S1, _, off1, t1 = G1.sections(UU)
    Gg = blockdiag(*[gU[x] for x in UPTS])            # stalkwise g on the section coordinates
    Gam_g = solve(S1, Gg * S0) if S0.c else Mat(S1.c, 0)
    ap0, ap1, am0, am1 = random.randint(1, 2), random.randint(2, 3), random.randint(0, 2), random.randint(0, 2)
    aplus = rmat(ap1, ap0)
    while rank(aplus) < ap0:
        aplus = rmat(ap1, ap0)
    aminus = rmat(am1, am0)
    R0 = rmat(S0.c, ap0)
    Lft = solve(aplus.T * aplus, aplus.T)             # left inverse of aplus
    R1 = Gam_g * R0 * Lft + rmat(S1.c, ap1) * (Mat.eye(ap1) - aplus * Lft)
    assert Gam_g * R0 == R1 * aplus                   # compatibility CGS1.5
    M0, M1 = glue(G0, ap0, am0, R0), glue(G1, ap1, am1, R1)
    Phi = {x: (aplus if x == 'm' else aminus if x == "m'" else gU[x]) for x in Pp.pts}
    assert is_natural(Phi, M0, M1)
    # supported hypercohomology from the Roos double complex on P'
    n_ = 4

    def tot(F0, F1, phi, W, Z):
        d0, ds0, CH0, O0 = F0.roos(W, Z, n_)
        d1, ds1, CH1, O1 = F1.roos(W, Z, n_)
        dims, ds = [], []
        for n in range(n_):
            dims.append(d0[n] + (d1[n - 1] if n >= 1 else 0))
        for n in range(n_ - 1):
            A00 = ds0[n]
            Phn = roos_map(phi, F0, F1, CH0, O0, O1, n) * ((-1) ** n)
            D = Mat(dims[n + 1], dims[n])
            D.setblock(0, 0, A00)
            D.setblock(d0[n + 1], 0, Phn)
            if n >= 1:
                D.setblock(d0[n + 1], d0[n], ds1[n - 1])
            ds.append(D)
        return dims, ds
    dimsZ, dsZ = tot(M0, M1, Phi, XP, ZP)
    ok12 &= complex_ok(dsZ)
    hZ = hdims(dimsZ, dsZ)[:3]
    # text model CGS6.3: K^n = A_+^n + A_-^n + B^{n-1}, B = Tot Gamma(U, Roos(G^*))
    # B on U: use the same Roos double complex restricted to U
    d0U, ds0U, CH0U, O0U = G0.roos(UU, None, n_)
    d1U, ds1U, CH1U, O1U = G1.roos(UU, None, n_)
    Bd = [d0U[n] + (d1U[n - 1] if n >= 1 else 0) for n in range(n_)]
    Bds = []
    for n in range(n_ - 1):
        D = Mat(Bd[n + 1], Bd[n])
        D.setblock(0, 0, ds0U[n])
        D.setblock(d0U[n + 1], 0, roos_map(gU, G0, G1, CH0U, O0U, O1U, n) * ((-1) ** n))
        if n >= 1:
            D.setblock(d0U[n + 1], d0U[n], ds1U[n - 1])
        Bds.append(D)
    ok12 &= complex_ok(Bds)
    r0 = S0 * R0
    r1 = S1 * R1
    # r~ : A_+^q -> B^q ; degree 0 into C^0(U;G0), degree 1 into the C^0(U;G1) summand of B^1
    rt0 = vstack(r0, Mat(Bd[0] - t0, ap0))
    rt1 = Mat(Bd[1], ap1)
    rt1.setblock(d0U[1], 0, r1)
    ok12 &= (Bds[0] * rt0 == rt1 * aplus)            # r~ is a chain map
    Ad = [ap0 + am0, ap1 + am1]
    Kd = [Ad[0], Ad[1] + Bd[0], Bd[1], Bd[2]]

    def Kdiff(sgn):
        # d_K(a+, a-, b) = (d a+, d a-, r~(a+) + sgn * d_B b), sgn = -1 is the text's convention
        D0 = Mat(Kd[1], Kd[0])
        D0.setblock(0, 0, blockdiag(aplus, aminus))
        D0.setblock(Ad[1], 0, rt0)
        D1 = Mat(Kd[2], Kd[1])
        D1.setblock(0, 0, rt1)
        D1.setblock(0, Ad[1], Bds[0] * sgn)
        D2 = Mat(Kd[3], Kd[2])
        D2.setblock(0, 0, Bds[1] * sgn)
        return [D0, D1, D2]
    dsK = Kdiff(-1)
    ok13 &= complex_ok(dsK) and hdims(Kd, dsK)[:3] == hZ
    if not (rt1 * aplus).is_zero():
        ctrl &= not complex_ok(Kdiff(+1))
    # CGS6.7: h^n(K) = dim coker(H^{n-1}A_+ -> H^{n-1}B) + dim ker(H^n A_+ -> H^n B) + h^n(A_-)
    HA = hdims([ap0, ap1], [aplus])
    HAm = hdims([am0, am1], [aminus])
    HB = hdims(Bd, Bds)

    def rk_induced(n):
        # rank of H^n(A_+) -> H^n(B)
        if n == 0:
            Z = nullspace(aplus)
            img = rt0 * Z
            Bb = Mat(Bd[0], 0)
        else:
            Z = Mat.eye(ap1)
            img = rt1 * Z
            Bb = colbasis(Bds[0])
        return rank(hstack(img, Bb) if Bb.c else img) - (Bb.c)
    rks = [rk_induced(0), rk_induced(1)]
    pred = [(HA[0] - rks[0]) + HAm[0],
            (HB[0] - rks[0]) + (HA[1] - rks[1]) + HAm[1],
            (HB[1] - rks[1])]
    ok14 &= pred == hZ
    det.append('hZ=%s' % hZ)
report('C12 CGS6.1-6.4: two-term complexes: supported hypercohomology from the double complex is a complex', ok12)
report('C13 CGS6.3-6.4: the mapping fibre K^n = A_+^n + A_-^n + B^{n-1} computes RGamma_Z(X, M^*)', ok13,
       '; '.join(det[:3]))
report('C14 CGS6.7: h^n(K) = coker(H^{n-1}A_+ -> H^{n-1}B) + ker(H^nA_+ -> H^nB) + H^n(A_-) (dimensions)', ok14)
# dedicated control: G0 = G1 = constant Q on U, g = id, A_+^0 = A_+^1 = Q, a_+ = id, r^0 = r^1 = id, A_- = 0.
# Then r~ o d_A = id != 0 and the variant with +d_B b has d_K^2 = 2 r~ d_A != 0.
QU0 = Sheaf(Ufin, {x: 1 for x in UPTS}, {('p1', 'eta'): Mat.eye(1), ('p2', 'eta'): Mat.eye(1)})
d0U, ds0U, CH0U, O0U = QU0.roos(UU, None, 3)
Bd = [d0U[0], d0U[1] + d0U[0], d0U[2] + d0U[1]]
idU = {x: Mat.eye(1) for x in UPTS}
B0 = vstack(ds0U[0], roos_map(idU, QU0, QU0, CH0U, O0U, O0U, 0))
B1 = Mat(Bd[2], Bd[1])
B1.setblock(0, 0, ds0U[1])
B1.setblock(d0U[2], 0, -roos_map(idU, QU0, QU0, CH0U, O0U, O0U, 1))
B1.setblock(d0U[2], d0U[1], ds0U[0])
Sg = QU0.sections(UU)[0]
rt0c = vstack(Sg, Mat(Bd[0] - Sg.r, 1))
rt1c = Mat(Bd[1], 1)
rt1c.setblock(d0U[1], 0, Sg)
def Kc(sgn):
    D0 = vstack(Mat.eye(1), rt0c)
    D1 = hstack(rt1c, B0 * sgn)
    D2 = B1 * sgn
    return [D0, D1, D2]
ctrl_ok = complex_ok([B0, B1]) and complex_ok(Kc(-1)) and not complex_ok(Kc(+1))
report('C15 (control) CGS6.3 with the wrong sign +d_B b is rejected (d_K^2 = 2 r~ d_A != 0), the text\'s sign '
       'is accepted', ctrl_ok, 'random trials with r~ d_A != 0 also reject it: %s' % ctrl)

# CGS6.5-6.6: boundary representative and the lift criterion (single sheaf, B = Roos(U))
ok16 = True
for trial in range(6):
    G = sheafU(random.randint(0, 2), random.randint(0, 2), random.randint(1, 3))
    S, pts, off, t = G.sections(UU)
    ap = random.randint(0, 2)
    R = rmat(S.c, ap, -1, 1)
    r = S * R
    dB, dsB, _, _ = G.roos(UU, None, 3)
    Kd = [ap] + dB[:3]
    dsK = [r] + [-D for D in dsB[:2]]
    HK1 = Cohom(Kd[1], dsK[0], dsK[1])
    # every cocycle b in B^0 = Gamma(U,G): del[b] = [(0,0,b)] ; zero iff b = r(a) - d_B c (here c in B^{-1} = 0)
    for j in range(S.c):
        b = S.col(j)
        zero = HK1.coords(b).is_zero()
        lift = solve(r, b) is not None if ap else b.is_zero()
        ok16 &= (zero == lift)
    # a coboundary b = d_B c in B^1 gives (0,0,b) = d_K(0,0,-c)
    c = rmat(dB[0], 1)
    ok16 &= (dsK[1] * (c * (-1)) == dsB[0] * c)
report('C16 CGS6.5-6.6: del[b] = [(0,0,b)] is well defined and vanishes iff b = r~(a_+) - d_B c', ok16)

# CGS6.7 over Z: the sequence need not split
A0 = SMatrix([[2], [1]])   # K^0 = Z (A_+^0), K^1 = A_+^1 + B^0 = Z^2, d = (2, 1): A_+ = [Z -2-> Z], r~ = id
snf = smith_normal_form(A0, domain=ZZ)
H1_free = (snf[0, 0] == 1 and snf[1, 0] == 0)      # H^1(K) = Z^2 / <(2,1)> = Z, torsion-free
# image of B^0 = {(0,b)} in H^1 = Z via (x,y) -> x - 2y is 2Z; the quotient is Z/2 = ker(H^1 A_+ -> H^1 B)
img_index = abs(0 - 2 * 1)
report('C17 CGS6.7 over Z: for A_+ = [Z -2-> Z], B = Z[0], r~ = id the sequence is 0 -> Z -2-> Z -> Z/2 -> 0, '
       'NOT split (text correctly declines to split it)', H1_free and img_index == 2,
       'SNF of d_K^0 = diag(1), H^1(K) = Z torsion-free, sub of index 2')

# CGS7: the selected residue functor (eps = 0 pushforward) has right adjoint M -> A_-
ok18 = True
for trial in range(6):
    G = sheafU(random.randint(0, 2), random.randint(0, 2), random.randint(1, 3))
    S = G.sections(UU)[0]
    ap, am = random.randint(0, 2), random.randint(0, 3)
    R = rmat(S.c, ap)
    M = glue(G, ap, am, R)
    for mdim in (1, 2):
        ok18 &= ext_dims(istar(0, mdim), M, 2) == [mdim * am, 0, 0]
    # CGS7.2: RGamma_Z(M) = A_-[0] + Fib(A_+ -> RGamma(U,G)); the Fib part is RGamma_Z of the eps = 1 summand
    hZ = M.H(XP, ZP, 3)[:3]
    hZ1 = glue(G, ap, 0, R).H(XP, ZP, 3)[:3]
    ok18 &= hZ == [hZ1[0] + am] + hZ1[1:]
report('C18 CGS7.1-7.2: Hom(i\'_*M, M) = Hom(M, A_-), Ext^{>0}(i\'_*M, M) = 0, and RGamma_Z = A_- + Fib(A_+ -> RGamma(U,G))', ok18)

# CGS8: equivariance of the boundary for an operator acting over the identity
ok19 = True
for trial in range(4):
    G0 = sheafU(random.randint(1, 2), random.randint(0, 2), random.randint(1, 2))
    # G = G0 (x) Q^3 with operator T = id (x) J, J = Jordan(2,2) + (3)
    Jm = Mat.of([[2, 1, 0], [0, 2, 0], [0, 0, 3]])
    G = Sheaf(Ufin, {x: 3 * G0.dims[x] for x in UPTS},
              {k: kron(Mv, Mat.eye(3)) for k, Mv in G0.maps.items()})
    TU = {x: kron(Mat.eye(G0.dims[x]), Jm) for x in UPTS}
    assert is_natural(TU, G, G)
    S, pts, off, t = G.sections(UU)
    TG = solve(S, blockdiag(*[TU[x] for x in UPTS]) * S)      # Gamma(U, T)
    # A_+ = the T-stable generalised 2-eigenspace intersected with a random stable piece: take A_+ = ker (TG-2)
    A = nullspace(TG - Mat.eye(S.c) * 2)
    ap = A.c
    TA = solve(A, TG * A)
    M = glue(G, ap, 1, A)
    TM = {x: (TA if x == 'm' else Mat.eye(1) * 5 if x == "m'" else TU[x]) for x in Pp.pts}
    ok19 &= is_natural(TM, M, M)
    # boundary Gamma(U,G) -> coker r = Gamma/A commutes with T; generalised eigenspaces map to the same eigenvalue
    Q = nullspace(A.T).T if A.c else Mat.eye(S.c)             # quotient Gamma -> coker r
    TQ = solve(Q.T, (Q * TG).T).T if Q.r else Mat(0, 0)
    ok19 &= (Q * TG == TQ * Q)
    for alpha, k in ((2, 2), (3, 1)):
        Pw = Mat.eye(S.c)
        for _ in range(k):
            Pw = Pw * (TG - Mat.eye(S.c) * alpha)
        Eal = nullspace(Pw)                                    # generalised alpha-eigenspace of Gamma(U,G)
        PwQ = Mat.eye(Q.r)
        for _ in range(k):
            PwQ = PwQ * (TQ - Mat.eye(Q.r) * alpha)
        ok19 &= (PwQ * Q * Eal).is_zero() if Eal.c and Q.r else True
report('C19 CGS8: an operator over the identity acts on (G, A_+, A_-, r); the boundary is equivariant and maps '
       'generalised alpha-eigenclasses to generalised alpha-eigenclasses', ok19)

# CGS9: the structure sheaf (finite model over Q: O_U replaced by the constant sheaf Q, flabby as in SS4)
QU = Sheaf(Ufin, {x: 1 for x in UPTS}, {('p1', 'eta'): Mat.eye(1), ('p2', 'eta'): Mat.eye(1)})
Rfin = glue(QU, 1, 1, Mat.eye(1))
hZ = Rfin.H(XP, ZP, 3)
J, I, iota, pi = ext_maps(QU, 1, 1, Rfin)
solv_sec, _, _ = nat_solve(I, Rfin, [(x, pi[x], Mat.eye(I.dims[x]), Mat.eye(I.dims[x])) for x in Pp.pts])
JS = jstar(QU)
rho = {x: (Mat.eye(1) if x == 'm' else Mat(0, 1) if x == "m'" else Mat.eye(1)) for x in Pp.pts}
solv_split, _, sec = nat_solve(JS, Rfin, [(x, rho[x], Mat.eye(JS.dims[x]), Mat.eye(JS.dims[x])) for x in Pp.pts])
report('C20 CGS9.1-9.5: for the structure sheaf H_Z = Q in degree 0 only; 0 -> j_!O -> R -> i_*(Q+Q) -> 0 has no '
       'section (class = id); 0 -> i_*Q -> R -> j_*O -> 0 splits by a -> (a,0)',
       is_natural(rho, Rfin, JS) and hZ[:3] == [1, 0, 0] and (not solv_sec) and solv_split and
       sec['m'] == Mat.eye(1) and (sec["m'"].r, sec["m'"].c) == (1, 0),
       'H_Z = %s; the unique section is 1 on the eps-part and 0 on the (1-eps)-part, i.e. a -> (a,0)' % hZ[:3])

# CGS9.2: partial fractions: Q -> sum_p Q/Z_(p) is onto with kernel Z (global sections of the Cousin resolution)
primes = [2, 3, 5, 7, 11, 13]
okpf = True
for trial in range(200):
    tgt = {p: Fr(random.randint(0, p ** 3 - 1), p ** random.randint(0, 3)) for p in random.sample(primes, 3)}
    x = sum(tgt.values(), Fr(0))
    for p in primes:
        # image of x in Q/Z_(p): x - t_p must be p-integral
        tp = tgt.get(p, Fr(0))
        okpf &= (x - tp).denominator % p != 0
kernel_ok = all(Fr(a, b).denominator == 1 for a, b in [(6, 3), (10, 5)])
report('C21 CGS9.2: partial fractions: every finite tuple in sum_p Q/Z_(p) is the image of a rational number '
       '(200 random tuples, p <= 13), so H^1(U, O_U) = 0 and H^0 = Z', okpf and kernel_ok)

# ============================================================================================
# DCP4-DCP12: the doubled source X^dbl, the three-point base Y and an exact finite Mellin model
# of the Connes-Consani coefficient data.
#   A   = Q[s]/(Pi),  Pi = Z E               (receiving space; 'Mellin coordinate' s)
#   S   = Q[s]/(E)                           (stand-in for S_00^even)
#   Sigma g = Z g                            (M_0 Sigma h = 2 zeta Mh: multiplication by the 'zeta' Z)
#   Fourier F g(s) = g(1-s) on S, R b(s) = b(1-s) on A   (Z(1-s) = Z(s), E(1-s) = E(s))
#   so R Sigma = Sigma F (the 'Poisson identity' DCP3.4 for S_00), J = Sigma(S), Q = A/J = Q[s]/(Z).
#   V_+ = V_- = S + Q^2 (endpoint lines), r_+ = Sigma, r_- = R Sigma (both kill the endpoint lines).
#   Dilation generator: L_A = mult by s, L_+ = (s, 0, 1), L_- = (1-s, 1, 0)  (DCP10.1 at the Lie level).
# Z = (s^2 - s + c)^2: c = 5/4 puts the double zeros at 1/2 +- i (on the line Re s = 1/2),
# c = 4/25 puts them at 1/5 and 4/5 (off the line).  Every DCP identity is checked in both models.
# ============================================================================================
print('-' * 100)
print('DCP4-DCP12 (SOURCE_CC_DOUBLE_PULLBACK.md, lines 160-504) in the finite Mellin model')


def padd(a, b):
    n = max(len(a), len(b))
    return [(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(n)]


def pmul(a, b):
    r = [Fr(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            r[i + j] += x * y
    return r


def pmod(a, m):
    a = [Fr(x) for x in a]
    m = [Fr(x) for x in m]
    while len(m) > 1 and m[-1] == 0:
        m.pop()
    dm = len(m) - 1
    for k in range(len(a) - 1, dm - 1, -1):
        if a[k] != 0:
            f = a[k] / m[-1]
            for j in range(dm + 1):
                a[k - dm + j] -= f * m[j]
    res = a[:dm] + [Fr(0)] * max(0, dm - len(a))
    return res[:dm]


def p1ms(a):
    res, pw = [Fr(0)], [Fr(1)]
    for x in a:
        res = padd(res, [x * y for y in pw])
        pw = pmul(pw, [Fr(1), Fr(-1)])
    return res


def mono(j):
    return [Fr(0)] * j + [Fr(1)]


def mult_mat(q, m, n):
    cols = [pmod(pmul(q, mono(j)), m) for j in range(n)]
    return Mat(n, n, [[cols[j][i] for j in range(n)] for i in range(n)])


def subst_mat(m, n):
    cols = [pmod(p1ms(mono(j)), m) for j in range(n)]
    return Mat(n, n, [[cols[j][i] for j in range(n)] for i in range(n)])


mp.mp.dps = 40


def peval(coeffs, z, der=0):
    """value of the der-th derivative / der! of the polynomial at z (mpmath)"""
    tot = mp.mpc(0)
    for k, a in enumerate(coeffs):
        if k >= der and a != 0:
            tot += mp.binomial(k, der) * mp.mpf(a.numerator) / a.denominator * mp.mpc(z) ** (k - der)
    return tot


# spaces
Xd = FinSpace(['mp', 'mm', 'p1', 'p2', 'eta'],
              {'mp': ['mp', 'p1', 'p2', 'eta'], 'mm': ['mm', 'p1', 'p2', 'eta'],
               'p1': ['p1', 'eta'], 'p2': ['p2', 'eta'], 'eta': ['eta']})
Yb = FinSpace(['xp', 'xm', 'e'], {'xp': ['xp', 'e'], 'xm': ['xm', 'e'], 'e': ['e']})
fmap = {'mp': 'xp', 'mm': 'xm', 'p1': 'e', 'p2': 'e', 'eta': 'e'}
XDALL = frozenset(Xd.pts)
UD = frozenset(['p1', 'p2', 'eta'])
Xplus = frozenset(['mp', 'p1', 'p2', 'eta'])
Xminus = frozenset(['mm', 'p1', 'p2', 'eta'])
Zp, Zm, Zpm = frozenset(['mp']), frozenset(['mm']), frozenset(['mp', 'mm'])
expected_opens = {frozenset(), frozenset(['eta']), frozenset(['p1', 'eta']), frozenset(['p2', 'eta']), UD,
                  Xplus, Xminus, XDALL}
report('D1  DCP1.1-2.1 (setting): the opens of the finite X^dbl are the opens of U, X_+, X_-, X^dbl; f is continuous',
       set(Xd.opens()) == expected_opens and
       all(Xd.is_open(frozenset(x for x in Xd.pts if fmap[x] in O)) for O in Yb.opens()),
       '%d opens; preimages of the 5 opens of Y are open' % len(Xd.opens()))



def snake_iota(N, Zset, Wopen):
    """For a sheaf N on X^dbl whose restriction to U is constant with stalk A: the boundary
    delta: Gamma(U,N) = A -> H^1_Z computed in the Roos resolution on the open Wopen (snake lemma),
    and the forget-support map iota: H^1_Z -> H^1(X^dbl).  Returns (delta, iota o delta) as matrices."""
    nA = N.dims['eta']
    dP_, dsP_, CHP_, OFFP_ = N.roos(XDALL, None, 3)
    dW, dsW, CHW, OFFW = N.roos(Wopen, None, 3)
    dZ_, dsZ_, CHZ_, OFFZ_ = N.roos(XDALL, Zset, 3)
    HZ1 = Cohom(dZ_[1], dsZ_[0], dsZ_[1])
    HX1 = Cohom(dP_[1], dsP_[0], dsP_[1])
    cols_delta, cols_iota = [], []
    for j in range(nA):
        b = Mat(nA, 1)
        b.a[j][0] = Fr(1)
        c0 = Mat(dW[0], 1)
        for x in ['p1', 'p2', 'eta']:
            c0.setblock(OFFW[0][(x,)], 0, b)
        z = dsW[0] * c0
        zz = Mat(dZ_[1], 1)
        for s in CHZ_[1]:
            zz.setblock(OFFZ_[1][s], 0, z.sub(range(OFFW[1][s], OFFW[1][s] + N.dims[s[-1]]), [0]))
        cols_delta.append(HZ1.coords(zz))
        full = Mat(dP_[1], 1)
        for s in CHZ_[1]:
            full.setblock(OFFP_[1][s], 0, zz.sub(range(OFFZ_[1][s], OFFZ_[1][s] + N.dims[s[-1]]), [0]))
        cols_iota.append(HX1.coords(full))
    return hstack(*cols_delta), hstack(*cols_iota)


def pullback(Om):
    """f^{-1} Omega on X^dbl for a sheaf Omega on Y (stalk at x is Omega(f(x)))"""
    dims = {x: Om.dims[fmap[x]] for x in Xd.pts}
    maps = {}
    for x in Xd.pts:
        for y in Xd.pts:
            if Xd.lt(x, y):
                maps[(x, y)] = Om.M(fmap[x], fmap[y])
    return Sheaf(Xd, dims, maps)


def run_dcp(c, label):
    out = {}
    tag = lambda s: s + '[' + label + ']'
    Zpol = pmul([c, Fr(-1), Fr(1)], [c, Fr(-1), Fr(1)])
    Epol = pmul([Fr(-2), Fr(-1), Fr(1)], [Fr(-6), Fr(-1), Fr(1)])
    Pi = pmul(Zpol, Epol)
    nA, nS, nZ = 8, 4, 4
    LA = mult_mat([Fr(0), Fr(1)], Pi, nA)
    RA = subst_mat(Pi, nA)
    LS = mult_mat([Fr(0), Fr(1)], Epol, nS)
    FS = subst_mat(Epol, nS)
    Sig = Mat(nA, nS, [[(pmul(Zpol, mono(j)) + [Fr(0)] * 8)[i] for j in range(nS)] for i in range(nA)])
    PQ = Mat(nZ, nA, [[pmod(mono(j), Zpol)[i] for j in range(nA)] for i in range(nZ)])   # A -> Q = A/J
    Z26 = Mat(nA, 2)
    rP = hstack(Sig, Z26)
    rM = hstack(RA * Sig, Z26)
    nV = nS + 2
    IA, IV = Mat.eye(nA), Mat.eye(nV)
    ok = (RA * RA == IA and FS * FS == Mat.eye(nS) and RA * Sig == Sig * FS and rank(Sig) == nS and
          (PQ * Sig).is_zero() and rank(PQ) == nZ)
    report(tag('D2  model: R^2 = 1, F^2 = 1, R Sigma = Sigma F (finite DCP3.4), Sigma injective, Q = A/J has dim 4'), ok)

    # the sheaf Omega on Y and N = f^{-1} Omega on X^dbl (explicit form DCP4.3)
    Om = Sheaf(Yb, {'xp': nV, 'xm': nV, 'e': nA}, {('xp', 'e'): rP, ('xm', 'e'): rM})
    N = Sheaf(Xd, {'mp': nV, 'mm': nV, 'p1': nA, 'p2': nA, 'eta': nA},
              {('mp', 'p1'): rP, ('mp', 'p2'): rP, ('mp', 'eta'): rP, ('mm', 'p1'): rM, ('mm', 'p2'): rM,
               ('mm', 'eta'): rM, ('p1', 'eta'): IA, ('p2', 'eta'): IA})
    # DCP4: the presheaf inverse image P(W) = Omega(smallest open containing f(W)) is already a sheaf, equal to N
    opensX = Xd.opens()
    Pdat = {}
    okP = N.functorial() and Om.functorial()
    for W in opensX:
        O = Yb.min_open({fmap[x] for x in W})
        SO, ptsO, offO, tO = Om.sections(O)
        SW, ptsW, offW, tW = N.sections(W)
        # canonical map P(W) -> Gamma(W, N): s -> (s_{f(x)})_{x in W}
        Cm = Mat(tW, tO)
        for x in ptsW:
            Cm.setblock(offW[x], offO[fmap[x]], Mat.eye(N.dims[x]))
        img = Cm * SO
        okP &= all(in_span(SW, img.col(j)) for j in range(img.c)) and rank(img) == SO.c == SW.c
        Pdat[W] = (O, SO, ptsO, offO)
    # sheaf condition on P directly, for every cover of every open

    def resP(W, W2):
        O, SO, ptsO, offO = Pdat[W]
        O2, SO2, ptsO2, offO2 = Pdat[W2]
        Pr = Mat(sum(Om.dims[y] for y in ptsO2), sum(Om.dims[y] for y in ptsO))
        rr = 0
        for y in ptsO2:
            Pr.setblock(rr, offO[y], Mat.eye(Om.dims[y]))
            rr += Om.dims[y]
        return solve(SO2, Pr * SO)
    ncov = 0
    for W in opensX:
        subs = [V for V in opensX if V <= W and V]
        for k in range(1, len(subs) + 1):
            for cov in itertools.combinations(subs, k):
                if frozenset().union(*cov) != W:
                    continue
                ncov += 1
                prod = vstack(*[resP(W, V) for V in cov])
                eqs = []
                offs, tt = [], 0
                for V in cov:
                    offs.append(tt)
                    tt += Pdat[V][1].c
                for a_ in range(len(cov)):
                    for b_ in range(a_ + 1, len(cov)):
                        I2 = cov[a_] & cov[b_]
                        if not I2:
                            continue
                        Ra, Rb = resP(cov[a_], I2), resP(cov[b_], I2)
                        Row = Mat(Ra.r, tt)
                        Row.setblock(0, offs[a_], Ra)
                        Row.setblock(0, offs[b_], -Rb)
                        eqs.append(Row)
                eqd = nullspace(vstack(*eqs)).c if eqs else tt
                okP &= rank(prod) == Pdat[W][1].c == eqd
    dims43 = {W: Pdat[W][1].c for W in opensX}
    okP &= dims43[Xplus] == nV and dims43[Xminus] == nV and dims43[UD] == nA and dims43[frozenset(['eta'])] == nA \
        and dims43[XDALL] == nS + 4
    report(tag('D3  DCP4.1-4.3: the presheaf inverse image is already a sheaf (all %d covers), equal to the explicit N; '
               'N(X_+-) = V_+-, N(V) = A, N(X^dbl) = V_+ x_A V_-' % ncov), okP)
    okF = all(v == 0 for v in N.H(UD, None, 3)[1:])
    for W in opensX:
        for W2 in opensX:
            if W2 < W and W2 and W <= UD:
                okF &= rank(resP(W, W2)) == dims43[W2]
    report(tag('D4  DCP4.2: N|_U is the constant sheaf A (all nonempty restrictions identity), flabby, H^{>0}(U,N) = 0'), okF)
    # DCP5: unit Omega -> f_* f^{-1} Omega is an isomorphism; R^q f_* = 0; but H^1(X^dbl) != 0
    okU = True
    for O in Yb.opens():
        SO, ptsO, offO, tO = Om.sections(O)
        pre = frozenset(x for x in Xd.pts if fmap[x] in O)
        SW, ptsW, offW, tW = N.sections(pre)
        Cm = Mat(tW, tO)
        for x in ptsW:
            Cm.setblock(offW[x], offO[fmap[x]], Mat.eye(N.dims[x]))
        okU &= rank(Cm * SO) == SO.c == SW.c
    hq = {y: N.H(frozenset(x for x in Xd.pts if fmap[x] in Yb.U[y]), None, 3) for y in Yb.pts}
    okR = all(all(v == 0 for v in hq[y][1:]) for y in Yb.pts)
    hX = N.H(XDALL, None, 3)
    hY = Om.H(frozenset(Yb.pts), None, 3)
    report(tag('D5  DCP5.1-5.3: Omega -> f_*f^{-1}Omega iso on all 5 opens; R^q f_* N = 0 (q > 0); '
               'H(X^dbl,N) = H(Y,Omega) = %s, H^1 != 0' % hX[:3]),
           okU and okR and hX[:3] == hY[:3] == [nS + 4, nZ, 0])
    out['H(X,N)'] = hX[:3]
    # DCP6: Cech complex D = [V_+ + V_- -> A], d = r_+ - r_-
    dD = hstack(rP, -rM)
    hD = hdims([2 * nV, nA], [dD])
    kerD = nullspace(dD)
    expl = []
    for j in range(nS):
        g = Mat(nS, 1)
        g.a[j][0] = Fr(1)
        v = vstack(FS * g, Mat(2, 1), g, Mat(2, 1))
        expl.append(v)
    for k in range(4):
        v = Mat(2 * nV, 1)
        v.a[[nS, nS + 1, nV + nS, nV + nS + 1][k]][0] = Fr(1)
        expl.append(v)
    E8 = hstack(*expl)
    okD = hD == hX[:2] and (dD * E8).is_zero() and rank(E8) == kerD.c == nS + 4 and rank(dD) == nS
    report(tag('D6  DCP6.1-6.3: the Cech complex computes H (Leray); H^0 = {((Fh,c),(h,d))}, H^1 = A/J = Q, '
               'im d = J'), okD)
    # DCP7.1 single supports
    hZp, hZm, hZpm = N.H(XDALL, Zp, 3)[:3], N.H(XDALL, Zm, 3)[:3], N.H(XDALL, Zpm, 3)[:3]
    Kp, Km = hdims([nV, nA], [rP]), hdims([nV, nA], [rM])
    report(tag('D7  DCP7.1: H_{m+-} = (2 endpoint lines, Q, 0) = cohomology of K_+- = [V_+- -> A]'),
           hZp == hZm == [2, nZ, 0] and Kp == Km == [2, nZ] and
           rank(hstack(nullspace(rP), vstack(Mat(nS, 2), Mat.eye(2)))) == 2 == nullspace(rP).c)
    out['H_Z'] = (hZp, hZm, hZpm)
    # chain maps K_+ -> D and K_- -> D, and the control
    fP0 = vstack(IV, Mat(nV, nV))
    fM0 = vstack(Mat(nV, nV), IV)
    okc = (dD * fP0 == IA * rP) and (dD * fM0 == (-IA) * rM)
    ctrl = not (dD * fM0 == IA * rM)
    report(tag('D8  DCP7.1: v+ -> (v+,0), b -> b and v- -> (0,v-), b -> -b are chain maps K_+- -> D'), okc)
    report(tag('D9  (control) DCP7.1 with the wrong sign b -> +b for the minus support is not a chain map'), ctrl)
    # convention-free content of the orientation sign: iota_+ delta_+ = - iota_- delta_- (Roos model, snake lemma)
    dP_, dsP_, CHP_, OFFP_ = N.roos(XDALL, None, 3)
    snake_and_iota = lambda Zs, Wo: snake_iota(N, Zs, Wo)
    dP1, iP1 = snake_and_iota(Zp, Xplus)
    dM1, iM1 = snake_and_iota(Zm, Xminus)
    dPM, iPM = snake_and_iota(Zpm, XDALL)
    okS = (iP1 + iM1).is_zero() and rank(iP1) == nZ and (iP1 * Mat.eye(nA)).c == nA
    # kernel of iota_+ delta_+ is exactly J: it kills Sigma(S)
    okS &= (iP1 * Sig).is_zero()
    okS &= rank(dPM) == nZ and (iPM).is_zero()
    ctrl2 = not (iP1 - iM1).is_zero()
    report(tag('D10 DCP7.1 sign, convention-free (Roos resolution + snake lemma): iota_+ delta_+ = - iota_- delta_- '
               ': A -> H^1(X^dbl), both of rank 4 with kernel J; iota o delta_Z = 0'), okS)
    report(tag('D11 (control) the variant "both supports map by +identity" (iota_+ delta_+ = iota_- delta_-) is false'),
           ctrl2)
    # DCP7.2: the Fourier lift and the vanishing boundary V_- -> H^1_{m+}
    okL = True
    for j in range(nV):
        v = Mat(nV, 1)
        v.a[j][0] = Fr(1)
        g = v.sub(range(nS), [0])
        lift = vstack(vstack(FS * g, Mat(2, 1)), v)
        okL &= (dD * lift).is_zero()
    # boundary H^0(X_-) -> H^1_{m+}(X^dbl) from the pair (X^dbl, X_-), Roos model
    dZ_, dsZ_, CHZ_, OFFZ_ = N.roos(XDALL, Zp, 3)
    HZ1 = Cohom(dZ_[1], dsZ_[0], dsZ_[1])
    dm_, dsm_, CHm_, OFFm_ = N.roos(Xminus, None, 3)
    SXm = N.sections(Xminus)[0]                      # Gamma(X_-, N) = V_- (stalk at m-)
    for j in range(SXm.c):
        c0 = Mat(dP_[0], 1)
        sec = SXm.col(j)
        ptsm, offm, tm = N.layout(Xminus)
        for x in ptsm:
            c0.setblock(OFFP_[0][(x,)], 0, sec.sub(range(offm[x], offm[x] + N.dims[x]), [0]))
        z = dsP_[0] * c0
        zz = Mat(dZ_[1], 1)
        for s in CHZ_[1]:
            zz.setblock(OFFZ_[1][s], 0, z.sub(range(OFFP_[1][s], OFFP_[1][s] + N.dims[s[-1]]), [0]))
        okL &= HZ1.coords(zz).is_zero()
    report(tag('D12 DCP7.2: (h,d) -> ((Fh,0,0),(h,d)) is a global section lifting V_-; the boundary '
               'V_- -> H^1_{m+}(X^dbl) is zero'), okL)
    # DCP7.3: fibre of D -> A[0] (via r_+ pr_+) and the change of coordinates
    dFib = vstack(dD, hstack(rP, Mat(nA, nV)))            # (k, b) = (r+v+ - r-v-, r+v+)
    T = vstack(hstack(Mat(nA, nA), IA), hstack(-IA, IA))  # (k,b) -> (b, b-k)
    Tinv = vstack(hstack(IA, -IA), hstack(IA, Mat(nA, nA)))
    dK = blockdiag(rP, rM)
    ok73 = (T * dFib == dK) and (T * Tinv == Mat.eye(2 * nA)) and (Tinv * T == Mat.eye(2 * nA))
    ok73 &= (hstack(IA, -IA) * dK == dD)                  # supported-to-global (b+,b-) -> b+ - b-
    ok73 &= (T * vstack(Mat(nA, nA), IA) == vstack(IA, IA))   # boundary b -> (0,b) -> (b,b)
    ok73 &= hdims([2 * nV, 2 * nA], [dK]) == hZpm[:2] == [4, 2 * nZ]
    report(tag('D13 DCP7.3: T(k,b) = (b, b-k) carries the fibre of D -> A[0] onto K = [V_+ + V_- -> A + A], '
               'd = (r_+, r_-); supported-to-global = b+ - b-; boundary b -> (b,b); H_{both} = (4, 8, 0)'), ok73)
    # DCP7.4-7.5 exactness with the displayed maps
    H0Z = nullspace(dK)                                   # 12 x 4
    H0 = kerD                                             # 12 x 8
    resA = hstack(rP, Mat(nA, nV))                        # H^0 -> A
    bnd = vstack(PQ, PQ)                                  # A -> Q + Q, b -> ([b],[b])
    dif = hstack(Mat.eye(nZ), -Mat.eye(nZ))               # Q + Q -> Q
    ex = rank(H0Z) == 4 and all(in_span(H0, H0Z.col(j)) for j in range(H0Z.c))
    ex &= nullspace(resA * H0).c == 4                     # kernel of restriction = the 4 endpoint lines
    ex &= rank(resA * H0) == nS and rank(hstack(resA * H0, Sig)) == nS   # image of restriction = J
    ex &= (bnd * resA * H0).is_zero() and nullspace(bnd).c == nS           # exact at A
    ex &= (dif * bnd).is_zero() and nullspace(dif).c == rank(bnd) == nZ    # exact at Q + Q
    ex &= rank(dif) == nZ and dif * vstack(Mat.eye(nZ), Mat(nZ, nZ)) == Mat.eye(nZ)
    report(tag('D14 DCP7.4-7.5: 0 -> C^4 -> H^0 -> A -> Q+Q -> Q -> 0 exact with the displayed maps; q -> (q,0) splits'),
           ex)
    out['ranks74'] = (rank(H0Z), rank(resA * H0), rank(bnd), rank(dif))
    # DCP8-DCP9: the faithful scalar extension M_full = R^dbl (x)_Z N
    V2 = 2 * nV
    rP2, rM2 = hstack(rP, Mat(nA, nV)), hstack(rM, Mat(nA, nV))
    Mf = Sheaf(Xd, {'mp': V2, 'mm': V2, 'p1': nA, 'p2': nA, 'eta': nA},
               {('mp', 'p1'): rP2, ('mp', 'p2'): rP2, ('mp', 'eta'): rP2, ('mm', 'p1'): rM2, ('mm', 'p2'): rM2,
                ('mm', 'eta'): rM2, ('p1', 'eta'): IA, ('p2', 'eta'): IA})
    Ip = Sheaf(Xd, {'mp': nV, 'mm': 0, 'p1': 0, 'p2': 0, 'eta': 0},
               {k: Mat(0, nV) if k[0] == 'mp' else Mat(0, 0) for k in Mf.maps})
    Im = Sheaf(Xd, {'mp': 0, 'mm': nV, 'p1': 0, 'p2': 0, 'eta': 0},
               {k: Mat(0, nV) if k[0] == 'mm' else Mat(0, 0) for k in Mf.maps})
    Dsum = direct_sum(N, Ip, Im)
    Phi = {x: Mat.eye(Mf.dims[x]) for x in Xd.pts}        # (v,w) -> (v; w) is the identity in these coordinates
    ok8 = Mf.functorial() and is_natural(Phi, Mf, Dsum) and all(Dsum.dims[x] == Mf.dims[x] for x in Xd.pts)
    # flabbiness of (i_+)_*V_+ : sections V_+ on opens containing m+, 0 elsewhere, restrictions onto
    for W in opensX:
        ok8 &= Ip.sections(W)[0].c == (nV if 'mp' in W else 0)
    ok8 &= all(v == 0 for v in Ip.H(XDALL, None, 3)[1:])
    report(tag('D15 DCP8.2-8.7: M_full = N + (i_+)_*V_+ + (i_-)_*V_- (natural iso); restriction (v,w) -> r(v); '
               'the extra summands are flabby'), ok8)
    # source action at the closed stalk: [tau] = 1, [n] = (n,0); on N: [tau] = [1]
    act = {'tau': Mat.eye(V2)}
    for n in range(-3, 4):
        act[n] = blockdiag(Mat.eye(nV) * n, Mat(nV, nV))
    keys = list(act)
    faithful = all(not (act[a] == act[b]) for a in keys for b in keys if a != b)
    mult = all(act[a] * act[b] == act[a * b] for a in range(-3, 4) for b in range(-3, 4) if -3 <= a * b <= 3)
    mult &= all(act['tau'] * act[n] == act[n] for n in range(-3, 4))
    addv = all(act[a] + act[b] == act[a + b] for a in range(-3, 4) for b in range(-3, 4) if -3 <= a + b <= 3)
    actN = {'tau': Mat.eye(nV)}                           # on N, (a,b_+,b_-) acts by a: [tau] = (1,1,1) -> 1
    for n in range(-3, 4):
        actN[n] = Mat.eye(nV) * n                         # [n] = (n,0,0) -> n
    nonfaithful_N = actN['tau'] == actN[1] and all(not (actN['tau'] == actN[n]) for n in range(-3, 4) if n != 1)
    report(tag('D16 DCP8.8: the source monoid Z u {tau} acts faithfully on the closed stalk V+V (tau -> 1, n -> (n,0)), '
               'multiplicatively and additively on integers; on N, [tau] = [1]'), faithful and mult and addv and
           nonfaithful_N)
    # eta vs iota_eps
    eta_ = {x: (vstack(IV, IV) if x in ('mp', 'mm') else IA) for x in Xd.pts}
    ie = {x: (vstack(IV, Mat(nV, nV)) if x in ('mp', 'mm') else IA) for x in Xd.pts}
    eplus = blockdiag(Mat(nV, nV), IV)                    # e_+ on the closed stalk at m+ of M_full; 0 on N
    ok89 = is_natural(eta_, N, Mf) and is_natural(ie, N, Mf)
    ok89 &= not (eta_['mp'] * (IV * 2) == act[2] * eta_['mp'])        # eta is not source-equivariant
    ok89 &= ie['mp'] * (IV * 2) == act[2] * ie['mp']                  # iota_eps is
    ok89 &= not (eplus * eta_['mp']).is_zero() and (eplus * ie['mp']).is_zero()   # eta not R^dbl-linear, iota_eps is
    ok89 &= eta_['mp'] - ie['mp'] == vstack(Mat(nV, nV), IV)
    report(tag('D17 DCP8.9: eta(v) = (v,v) is natural but not source-equivariant (nor R^dbl-linear); '
               'iota_eps(v) = (v,0) is both; eta - iota_eps = (0,v)'), ok89)
    # DCP9 cohomology, Cech, supports, direct image
    hMf = Mf.H(XDALL, None, 3)[:3]
    dD9 = hstack(rP2, -rM2)
    hD9 = hdims([2 * V2, nA], [dD9])
    hMfZp = Mf.H(XDALL, Zp, 3)[:3]
    hMfZpm = Mf.H(XDALL, Zpm, 3)[:3]
    okf = True
    for O in Yb.opens():
        pre = frozenset(x for x in Xd.pts if fmap[x] in O)
        okf &= Mf.sections(pre)[0].c == Om.sections(O)[0].c + nV * ('xp' in O) + nV * ('xm' in O)
    okf &= all(all(v == 0 for v in Mf.H(frozenset(x for x in Xd.pts if fmap[x] in Yb.U[y]), None, 3)[1:])
               for y in Yb.pts)
    ok9 = hMf == [nS + 4 + 2 * nV, nZ, 0] and hD9 == hMf[:2] and hMfZp == [2 + nV, nZ, 0] and \
        hMfZpm == [4 + 2 * nV, 2 * nZ, 0] and okf
    report(tag('D18 DCP9.1-9.4: H(M_full) = (H^0(N)+V_++V_-, Q, 0) = %s = Cech; H_{m+} = (C^2+V_+, Q, 0); '
               'H_{both} = (C^4+V_++V_-, Q+Q, 0); f_*M_full = Omega + k_+*V_+ + k_-*V_-, R^q f_* = 0' % hMf), ok9)
    out['H(M_full)'] = (hMf, hMfZp, hMfZpm)
    # DCP10: dilations (Lie level, exact) and jets (numerical, 40 digits)
    Lp = blockdiag(LS, Mat.of([[0]]), Mat.of([[1]]))
    Lm = blockdiag(Mat.eye(nS) - LS, Mat.of([[1]]), Mat.of([[0]]))
    ok10 = (rP * Lp == LA * rP) and (rM * Lm == LA * rM)
    Lm_bad = blockdiag(-LS, Mat.of([[1]]), Mat.of([[0]]))  # h -> h(a.) without the factor a
    ctrl3 = not (rM * Lm_bad == LA * rM)
    chars = (Lp.a[nS][nS], Lp.a[nS + 1][nS + 1], Lm.a[nS][nS], Lm.a[nS + 1][nS + 1])
    ok10 &= chars == (0, 1, 1, 0)
    report(tag('D19 DCP10.1: r_+ rho_+(a) = T_a r_+ and r_- rho_-(a) = T_a r_- (generators); endpoint characters '
               'a^(0,1,1,0) = (1,a,a,1), weights (0,2,2,0)'), ok10)
    report(tag('D20 (control) dropping the factor a in rho_-(a)h = a h(a.) breaks r_- rho_- = T_a r_-'), ctrl3)
    disc = Fr(1, 4) - c
    rho1 = mp.mpf(1) / 2 + (mp.sqrt(mp.mpf(disc.numerator) / disc.denominator) if disc > 0 else
                           mp.mpc(0, 1) * mp.sqrt(mp.mpf((-disc).numerator) / (-disc).denominator))
    rho2 = 1 - rho1
    tol = mp.mpf(10) ** (-30)

    def jet(bvec, z):
        co = [bvec.a[i][0] for i in range(nA)]
        return (peval(co, z, 0), peval(co, z, 1))
    okj = True
    for j in range(nS):
        for z in (rho1, rho2):
            v0, v1 = jet(Sig.col(j), z)
            okj &= abs(v0) < tol and abs(v1) < tol          # jets vanish on J: j_rho is defined on Q
    a = mp.mpf('1.7')
    LAf = mp.matrix([[mp.mpf(x.numerator) / x.denominator for x in row] for row in LA.a])
    Ta = mp.expm(mp.log(a) * LAf)
    RAf = mp.matrix([[mp.mpf(x.numerator) / x.denominator for x in row] for row in RA.a])
    worst = mp.mpf(0)
    for j in range(nA):
        b = Mat(nA, 1)
        b.a[j][0] = Fr(1)
        for z in (rho1, rho2):
            j0, j1 = jet(b, z)
            Tb = Ta * mp.matrix([[1 if i == j else 0] for i in range(nA)])
            t0 = sum(Tb[i] * mp.mpc(z) ** i for i in range(nA))
            t1 = sum(Tb[i] * i * mp.mpc(z) ** (i - 1) for i in range(1, nA))
            # DCP10.4: j(T_a b) = a^rho (1 + log a N) j(b), N = mult by t
            e0 = t0 - a ** z * j0
            e1 = t1 - a ** z * (j1 + mp.log(a) * j0)
            # DCP10.4 at the Lie level: j(L b) = (rho + N) j(b)
            Lb = LA * b
            l0, l1 = jet(Lb, z)
            e2 = l0 - z * j0
            e3 = l1 - (j0 + z * j1)
            # DCP11.5: j_rho(R b) = j_{1-rho}(b) with t -> -t
            Rb = RA * b
            r0, r1 = jet(Rb, z)
            k0, k1 = jet(b, 1 - z)
            e4, e5 = r0 - k0, r1 + k1
            worst = max(worst, *[abs(e) for e in (e0, e1, e2, e3, e4, e5)])
    okj &= worst < tol
    report(tag('D21 DCP10.3-10.4, DCP11.5 (numerical, 40 digits): jets at rho = %s vanish on J; '
               'j(T_a b) = a^rho(1 + log a N) j(b); j(Lb) = (rho+N) j(b); j_rho(Rb) = j_{1-rho}(b)|_{t->-t}'
               % mp.nstr(rho1, 6)), okj, 'max error %s' % mp.nstr(worst, 3))
    out['zeros'] = (mp.nstr(rho1, 8), mp.nstr(rho2, 8))
    # DCP11: the mirror
    wD0 = vstack(hstack(Mat(nV, nV), IV), hstack(IV, Mat(nV, nV)))   # (v+,v-) -> (v-,v+)
    ok11 = (RA * RA == IA) and (RA * rM == rP) and (dD * wD0 == (-RA) * dD)
    ctrl4 = not (dD * wD0 == RA * dD)
    wK1 = vstack(hstack(Mat(nA, nA), RA), hstack(RA, Mat(nA, nA)))   # (b+,b-) -> (R b-, R b+)
    ok11 &= (dK * wD0 == wK1 * dK)
    ctrl5 = not (dK * wD0 == (-wK1) * dK)
    # induced actions on Q and equivariance of DCP7.5
    PQi = solve(PQ, Mat.eye(nZ))
    RQ = PQ * RA * PQi
    ok11 &= (PQ * RA * Sig).is_zero() and RQ * RQ == Mat.eye(nZ)
    Delta = vstack(Mat.eye(nZ), Mat.eye(nZ))
    swR = vstack(hstack(Mat(nZ, nZ), RQ), hstack(RQ, Mat(nZ, nZ)))
    ok11 &= (swR * Delta == Delta * RQ) and (dif * swR == (-RQ) * dif)
    s_ = vstack(Mat.eye(nZ), -Mat.eye(nZ)) * Fr(1, 2)
    ok11 &= (dif * s_ == Mat.eye(nZ)) and (swR * s_ == s_ * (-RQ))
    # DCP11.4 at the Lie level: R L R = 1 - L on A, and W^{-1} L_- W = 1 - L_+ on the charts (W = identity swap)
    ok11 &= (RA * LA * RA == IA - LA) and (Lm == IV - Lp)
    # the mirror on the Cech complex of M_full
    wD0f = vstack(hstack(Mat(V2, V2), Mat.eye(V2)), hstack(Mat.eye(V2), Mat(V2, V2)))
    ok11 &= (dD9 * wD0f == (-RA) * dD9)
    report(tag('D22 DCP11.1-11.4: R^2 = 1, R r_- = r_+; w_D = (swap, -R) and w_K = (swap, (b+,b-) -> (Rb-,Rb+)) are '
               'chain maps; DCP7.5 is equivariant (R, swapped R, -R); s(q) = (q,-q)/2 is an equivariant section; '
               'R L R = 1 - L'), ok11)
    report(tag('D23 (control) w_D with +R in degree 1, and w_K with a sign, are NOT chain maps'), ctrl4 and ctrl5)
    # non-uniqueness of the equivariant section: s + Delta psi with R psi = - psi R
    # solve R psi + psi R = 0 for psi (4x4)
    rows = []
    for i in range(nZ):
        for k in range(nZ):
            row = [Fr(0)] * (nZ * nZ)
            for j in range(nZ):
                row[j * nZ + k] += RQ.a[i][j]        # (R psi)_{ik} = sum_j R_ij psi_jk
                row[i * nZ + j] += RQ.a[j][k]        # (psi R)_{ik} = sum_j psi_ij R_jk
            rows.append(row)
    Nps = nullspace(Mat.of(rows))
    okn = Nps.c > 0
    if okn:
        v = Nps.col(0)
        psi = Mat(nZ, nZ, [[v.a[i * nZ + k][0] for k in range(nZ)] for i in range(nZ)])
        s2 = s_ + Delta * psi
        okn &= (dif * s2 == Mat.eye(nZ)) and (swR * s2 == s2 * (-RQ)) and not (s2 == s_)
    report(tag('D24 (negative) DCP11.3: the equivariant section is NOT unique: s + Delta psi with R psi = -psi R '
               '(a %d-dimensional family) is another one' % Nps.c), okn)
    out['sections_family_dim'] = Nps.c
    # gluing class of N on the chart X_+: 0 -> j_!A -> N|X_+ -> i_*V_+ -> 0 has class r_+ != 0, so no section
    out['gluing_class_rank'] = rank(rP)
    out['LQ'] = PQ * LA * PQi
    out['Zpol'] = Zpol
    return out


res_on = run_dcp(Fr(5, 4), 'on-line c=5/4')
res_off = run_dcp(Fr(4, 25), 'off-line c=4/25')

# ---------------------------------------------------------------- E: extractable lemmas, general data --
okE1 = okE2 = True
for trial in range(8):
    vp, vm, na = random.randint(1, 3), random.randint(1, 3), random.randint(1, 3)
    Om = Sheaf(Yb, {'xp': vp, 'xm': vm, 'e': na}, {('xp', 'e'): rmat(na, vp, -1, 1), ('xm', 'e'): rmat(na, vm, -1, 1)})
    Nn = pullback(Om)
    for O in Yb.opens():
        SO, ptsO, offO, tO = Om.sections(O)
        pre = frozenset(x for x in Xd.pts if fmap[x] in O)
        SW, ptsW, offW, tW = Nn.sections(pre)
        Cm = Mat(tW, tO)
        for x in ptsW:
            Cm.setblock(offW[x], offO[fmap[x]], Mat.eye(Nn.dims[x]))
        okE1 &= rank(Cm * SO) == SO.c == SW.c
    for W in Xd.opens():
        O = Yb.min_open({fmap[x] for x in W})
        okE1 &= Om.sections(O)[0].c == Nn.sections(W)[0].c
    okE1 &= all(all(v == 0 for v in Nn.H(frozenset(x for x in Xd.pts if fmap[x] in Yb.U[y]), None, 3)[1:])
                for y in Yb.pts)
    okE1 &= Nn.H(XDALL, None, 3)[:3] == Om.H(frozenset(Yb.pts), None, 3)[:3]
    dp, ip = snake_iota(Nn, Zp, Xplus)
    dm, im_ = snake_iota(Nn, Zm, Xminus)
    Jp, Jm = Om.M('xp', 'e'), Om.M('xm', 'e')
    h1 = na - rank(hstack(Jp, Jm))
    okE2 &= (ip + im_).is_zero() and rank(ip) == h1
report('E1  pullback lemma (general Omega on Y, 8 random): the presheaf f^{-1}Omega is a sheaf, Omega = f_*f^{-1}Omega, '
       'R^q f_* f^{-1}Omega = 0, H(X^dbl, f^{-1}Omega) = H(Y, Omega)', okE1)
report('E2  orientation lemma (general data): iota_+ delta_+ = - iota_- delta_- : A -> H^1(X^dbl) = A/(J_+ + J_-)', okE2)

# ============================================================================================
# N: negative results
# ============================================================================================
print('-' * 100)
print('Negative results')
same = all(res_on[k] == res_off[k] for k in ('H(X,N)', 'H_Z', 'H(M_full)', 'ranks74', 'sections_family_dim',
                                               'gluing_class_rank'))
report('N1  every sheaf-theoretic invariant of DCP4-DCP12 is identical in the model with zeros on Re s = 1/2 '
       '(%s, %s) and the model with zeros off it (%s, %s): the constructions cannot see where the zeros are'
       % (res_on['zeros'] + res_off['zeros']), same,
       'H(X^dbl,N) = %s, H_Z = %s, ranks in DCP7.4 = %s' % (res_on['H(X,N)'], res_on['H_Z'], res_on['ranks74']))
# higher supported cohomology does not vanish for all coefficients; H^q(X,-) does; H^q_Z = 0 for q >= 3
G = sheafU(0, 0, 1)                                   # extension by zero from the generic point: H^1(U,G) = 1
M = jshriek(G)
hX, hZ = M.H(XP, None, 4), M.H(XP, ZP, 4)
ok = h_U(G)[:2] == [0, 1] and hZ[:4] == [0, 0, 1, 0] and hX[1:4] == [0, 0, 0]
allz = True
for trial in range(10):
    G2 = sheafU(random.randint(0, 3), random.randint(0, 3), random.randint(0, 3))
    ap = random.randint(0, 2)
    M2 = glue(G2, ap, random.randint(0, 2), rmat(G2.sections(UU)[0].c, ap))
    allz &= all(v == 0 for v in M2.H(XP, ZP, 5)[3:5]) and all(v == 0 for v in M2.H(XP, None, 5)[1:5])
report('N2  CGS5.2: H^2_Z(X, j_!G) = H^1(U,G) != 0 for G = extension by zero from the generic point, while '
       'H^q(X,-) = 0 (q >= 1) and H^q_Z = 0 (q >= 3) for all tested M (dim U = 1)', ok and allz,
       'H_Z(j_!G) = %s' % hZ[:4])
# GEX (appendix 1) in the finite model: Ext over Q[L] between Q = Q[s]/(Z) and the endpoint characters


def ext_L(LQ, lam):
    n = LQ.r
    Mt = (Mat.eye(n) * lam - LQ).T
    return nullspace(Mt).c, n - rank(Mt)              # (Hom(Q, Q_lam), Ext^1(Q, Q_lam))


okE = True
for res_, nm in ((res_on, 'on'), (res_off, 'off')):
    for lam in (0, 1):
        okE &= ext_L(res_['LQ'], lam) == (0, 0)
    PL = res_['LQ'] * (res_['LQ'] - Mat.eye(4))
    okE &= rank(PL) == 4
Zbad = pmul([Fr(0), Fr(-1), Fr(1)], [Fr(5, 4), Fr(-1), Fr(1)])     # s(s-1)(s^2-s+5/4): 'zeros' at 0 and 1
LQbad = mult_mat([Fr(0), Fr(1)], Zbad, 4)
ctrlE = ext_L(LQbad, 0) == (1, 1) and ext_L(LQbad, 1) == (1, 1) and rank(LQbad * (LQbad - Mat.eye(4))) < 4
report('N3  appendix 1 (GEX, algebraic core): Hom and Ext^1 over Q[L] between Q and the endpoint characters '
       '(L = 0, 1) vanish and L(L-1) is invertible on Q in both models -- this depends only on Z(0)Z(1) != 0',
       okE)
report('N4  (control) with Z(0) = Z(1) = 0 the same Ext groups are nonzero and L(L-1) is not invertible', ctrlE)
report('N5  the gluing class of N on each chart (CGS4.4 class of 0 -> j_!A -> N|X_+- -> i_*V_+- -> 0) is r_+- != 0, '
       'of the same rank in both models: nontrivial but independent of the zeros',
       res_on['gluing_class_rank'] == res_off['gluing_class_rank'] == 4)

# ============================================================================================
# Z: numerical checks of the analytic inputs used in DCP6-DCP11 (mpmath)
# ============================================================================================
print('-' * 100)
print('Numerical checks of the zeta inputs (mpmath, 25 digits)')
mp.mp.dps = 25
tpar = mp.mpf('0.7')
g = lambda v: mp.exp(-mp.pi * tpar * v * v)
ghat = lambda x: mp.exp(-mp.pi * x * x / tpar) / mp.sqrt(tpar)
Sg = lambda fn, u: 2 * mp.fsum(fn(n * u) for n in range(1, 80))
err = mp.mpf(0)
for u in (mp.mpf('0.5'), mp.mpf('0.9'), mp.mpf('1.7')):
    lhs = Sg(ghat, u)
    rhs = Sg(g, 1 / u) / u + g(0) / u - 1 / mp.sqrt(tpar)
    err = max(err, abs(lhs - rhs))
report('Z1  DCP3.4 (input): Sigma h^(u) = u^{-1} Sigma h(1/u) + u^{-1} h(0) - int h for a Gaussian with h(0), int h != 0',
       err < mp.mpf(10) ** -20, 'max error %s' % mp.nstr(err, 3))
Hf = lambda v: (v ** 4 - 3 * v ** 2 / (2 * mp.pi)) * mp.exp(-mp.pi * v * v)
h = lambda v: Hf(v / 2)
hhat = lambda x: 2 * Hf(2 * x)
eH = max(abs(mp.quad(lambda v: Hf(v) * mp.cos(2 * mp.pi * v * x), [-mp.inf, 0, mp.inf]) - Hf(x)) for x in (0.3, 1.1))
e0 = abs(h(0)) + abs(mp.quad(h, [-mp.inf, 0, mp.inf]))
err2 = max(abs(Sg(h, 1 / u) / u - Sg(hhat, u)) for u in (mp.mpf('0.6'), mp.mpf('1.3'), mp.mpf('2.2')))
report('Z2  DCP6.1/DCP7.2 (input): for h(v) = H(v/2), H = (v^4 - 3v^2/2pi)e^{-pi v^2} in S_00^even: '
       'R Sigma h = Sigma h^ (the Fourier lift); H^ = H checked by quadrature to 1e-15', eH < 1e-15 and e0 < 1e-20 and err2 < 1e-20,
       'Fourier self-duality of H err %s; moments %s; identity err %s' % (mp.nstr(eH, 2), mp.nstr(e0, 2), mp.nstr(err2, 2)))
MH = lambda s: mp.gamma((s + 4) / 2) / (2 * mp.pi ** ((s + 4) / 2)) - 3 / (2 * mp.pi) * mp.gamma((s + 2) / 2) / (2 * mp.pi ** ((s + 2) / 2))
Mh = lambda s: 2 ** s * MH(s)


def M0Sigma(s):
    f1 = lambda v: Sg(hhat, v) * v ** (-s)
    f2 = lambda u: Sg(h, u) * u ** (s - 1)
    return mp.quad(f1, [1, 2, 4, 8]) + mp.quad(f2, [1, 2, 4, 8, 16])


s1 = mp.mpf('2.5')
v1 = M0Sigma(s1)
e1 = abs(v1 - 2 * mp.zeta(s1) * Mh(s1)) / abs(v1)
rho1 = mp.zetazero(1)
v2 = M0Sigma(rho1)
report('Z3  DCP3.6 / DCP10.3 (input): M_0 Sigma h(s) = 2 zeta(s) Mh(s) at s = 2.5, and at the first zero '
       'rho_1 = 1/2 + 14.1347i the jet of Sigma h vanishes although Mh(rho_1) != 0',
       e1 < 1e-15 and abs(v2) < 1e-15 and abs(Mh(rho1)) > 1e-10,
       'rel err at 2.5: %s; |M_0 Sigma h(rho_1)| = %s; |Mh(rho_1)| = %s' % (mp.nstr(e1, 2), mp.nstr(abs(v2), 2),
                                                                         mp.nstr(abs(Mh(rho1)), 3)))
bfun = lambda u: mp.exp(-u - 1 / u)
a_ = mp.mpf('1.7')
s_ = mp.mpc('0.3', '2')
M0 = lambda fn, s: mp.quad(lambda u: fn(u) * u ** (s - 1), [0, 1, 4, 20, mp.inf])
Ta = lambda fn, a: (lambda u: fn(u / a))
Rf = lambda fn: (lambda u: fn(1 / u) / u)
eA = abs(M0(Ta(bfun, a_), s_) - a_ ** s_ * M0(bfun, s_))
eB = abs(M0(Rf(bfun), s_) - M0(bfun, 1 - s_))
eC = abs(M0(bfun, s_) - 2 * mp.besselk(s_, 2))
report('Z4  DCP10.2 and DCP11.5: M_0 T_a b = a^s M_0 b and M_0 R b(s) = M_0 b(1-s) for b = exp(-u-1/u) '
       '(M_0 b = 2K_s(2)), s = 0.3+2i, a = 1.7', max(eA, eB, eC) < 1e-15,
       'errors %s, %s, %s' % (mp.nstr(eA, 2), mp.nstr(eB, 2), mp.nstr(eC, 2)))
e5 = mp.mpf(0)
for (a, u) in ((mp.mpf('1.7'), mp.mpf('0.8')), (mp.mpf('0.4'), mp.mpf('2.3'))):
    e5 = max(e5, abs(Ta(Rf(bfun), a)(u) - a * Rf(Ta(bfun, 1 / a))(u)))
    # r_- rho_-(a) = T_a r_- :  R Sigma [a h(a.)](u) = (R Sigma h)(u/a)
    lhs = Rf(lambda w: Sg(lambda v: a * h(a * v), w))(u)
    rhs = Rf(lambda w: Sg(h, w))(u / a)
    e5 = max(e5, abs(lhs - rhs))
    # r_+ rho_+(a) = T_a r_+ : Sigma[h(./a)](u) = Sigma h(u/a)
    e5 = max(e5, abs(Sg(lambda v: h(v / a), u) - Sg(h, u / a)))
report('Z5  DCP11.4 (T_a R = a R T_{1/a}) and DCP10.1 (r_+- rho_+-(a) = T_a r_+-) pointwise on the real test functions',
       e5 < 1e-20, 'max error %s' % mp.nstr(e5, 2))

# ============================================================================================
print('=' * 100)
npass = sum(1 for _, o in RES if o)
print('%d items, %d PASS, %d FAIL' % (len(RES), npass, len(RES) - npass))
