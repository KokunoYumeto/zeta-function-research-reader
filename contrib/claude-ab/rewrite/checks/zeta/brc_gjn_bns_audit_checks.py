#!/usr/bin/env python3
# Checks for 33_ (first-pass audit of BRC/BRR, GJN/GJNR and BNS, in the programme's working folder
# quantum_tau_programme_bridge_20260924/next_edition_after_719). Written by a Claude subagent of claude-ab
# (Opus 5.5, max effort), 25 September 2026, and copied here unchanged apart from this header and the
# location of the source files, read only for the informational hash lines (environment variable PROGRAMME_SOURCE_DIR).
"""
checks33b.py -- independent checks for the audit of
  BRC0-11 / BRR0-9  (BOUNDARY_RAMIFICATION_AND_COUNTING_COMPARISON.md, ..._ROOT_REVIEW.md)
  GJN0-8 / GJNR0-10 (GLOBAL_JET_RAMIFICATION_NORM_SHIFT.md, GJN_INDEPENDENT_REVIEW.md)
  BNS0-7            (BOUNDARY_NORM_SHIFT_INDEPENDENT_CHECK.md)
in quantum_tau_programme_bridge_20260924/next_edition_after_719.

Conventions (as in the files): u = coordinate of the receiving punctured disk, l = log u is the
universal-cover coordinate, h(u) = (e^u-1)/u, H_{lam,j} = h(u) u^{-lam} (log u)^j / j!,
P_a f(u) = h(u)/h(u^a) f(u^a) with log(u^a) = a log u, C_b f(u) = h(u)/h(u/b) f(u/b),
T_{a,b} = P_a C_b, M = continuation along one positive loop (l -> l + 2 pi i),
N = lowering H_{lam,j} -> H_{lam,j-1}.  "Germ-level" checks evaluate the operators on actual
functions of l; "germ algebra" checks use the exact exponent/polynomial representation.
Synthetic zero sets (exact rational exponents, with off-line points and collisions) are used for
the algebraic identities; actual zeros rho_k = mpmath.zetazero(k) are used for analytic identities.
Each item prints PASS/FAIL, a one-line description and an error measure.
"""
import hashlib
import random
from fractions import Fraction as Fr

import mpmath as mp
import numpy as np
import sympy as sp

mp.mp.dps = 50
RES = []


def rep(tag, ok, desc, err):
    print(f"{tag} {'PASS' if ok else 'FAIL'} | {desc} | err: {err}")
    RES.append(bool(ok))


def ns(x, d=3):
    return mp.nstr(x, d)


# ----------------------------------------------------------------------------------------------
# hashes of the audited files (informational)
import os
SRC = os.environ.get("PROGRAMME_SOURCE_DIR", "quantum_tau_programme_bridge_20260924/next_edition_after_719") + "/"
for fn in ["BOUNDARY_RAMIFICATION_AND_COUNTING_COMPARISON.md", "BOUNDARY_RAMIFICATION_ROOT_REVIEW.md",
           "GLOBAL_JET_RAMIFICATION_NORM_SHIFT.md", "GJN_INDEPENDENT_REVIEW.md",
           "BOUNDARY_NORM_SHIFT_INDEPENDENT_CHECK.md", "PEER_EULER_AND_RAMIFICATION_INTAKE_REVIEW.md"]:
    try:
        raw = open(SRC + fn, "rb").read()
        a = hashlib.sha256(raw).hexdigest()
        b = hashlib.sha256(raw.replace(b"\r\n", b"\n")).hexdigest()
        print(f"# sha256 {fn}: stored {a[:8]}..{a[-8:]}  CRLF->LF {b[:8]}..{b[-8:]}")
    except OSError:
        print(f"# sha256 {fn}: not readable here")

# ----------------------------------------------------------------------------------------------
# common analytic helpers
TWOPI_I = mp.mpc(0, 1) * 2 * mp.pi


def h(u):
    u = mp.mpmathify(u)
    return mp.mpf(1) if u == 0 else mp.expm1(u) / u


def rel(a, b):
    a = mp.mpmathify(a)
    b = mp.mpmathify(b)
    d = max(abs(a), abs(b))
    return mp.mpf(0) if d == 0 else abs(a - b) / d


def F0(s):
    s = mp.mpmathify(s)
    return s * (s - 1) / 8 * mp.power(mp.pi, -s / 2) * mp.gamma(s / 2) * mp.zeta(s)


def Ct(s, t):
    s = mp.mpmathify(s)
    return -mp.exp(t * s * s) * mp.gamma(2 - s) / s


RHO = [mp.zetazero(k) for k in (1, 2, 3)]

# germ-level operators acting on callables of the cover coordinate l = log u


def P_op(a, f):
    return lambda l: h(mp.exp(l)) / h(mp.exp(a * l)) * f(a * l)


def C_op(b, f):
    lb = mp.log(b)
    return lambda l: h(mp.exp(l)) / h(mp.exp(l) / b) * f(l - lb)


def T_op(a, b, f):
    lb = mp.log(b)
    return lambda l: h(mp.exp(l)) / h(mp.exp(a * l) / b) * f(a * l - lb)


def M_op(k, f):
    sh = TWOPI_I * k
    return lambda l: f(l + sh)


lamA = mp.mpc('-0.7', '2.3')
lamB = mp.mpc('0.2', '-1.1')


def ftest(l):  # a generic multivalued germ (not of the special jet form), plus holomorphic parts
    u = mp.exp(l)
    return mp.exp(-lamA * l) * l ** 2 + 3 * mp.exp(-lamB * l) * l + mp.exp(u) / (1 - u / 3) + mp.cos(u) * mp.exp(l / 2)


PTS = [mp.mpc(x, y) for x in ('-2.5', '-1.2', '-0.4') for y in ('-7', '-2', '0.3', '4', '9')]  # |u|<1, arg up to 9
LP = [mp.mpc(x, y) for x in ('-1.5', '-0.5') for y in ('-3', '0.5', '5')]

# ----------------------------------------------------------------------------------------------
# exact germ algebra: h(u) * sum_lam u^{-lam} sum_j c_j (log u)^j/j!, lam = (Fraction re, Fraction im)


def tomp(c):
    if isinstance(c, Fr):
        return mp.mpf(c.numerator) / c.denominator
    return c


def lamval(k):
    return mp.mpc(tomp(Fr(k[0])), tomp(Fr(k[1])))


def mul(c, lam):
    return (c * Fr(lam[0]), c * Fr(lam[1]))


class G:
    def __init__(self, d=None):
        self.d = {k: list(v) for k, v in (d or {}).items()}

    @staticmethod
    def H(lam, j, c=1):
        v = [0] * (j + 1)
        v[j] = c
        return G({lam: v})

    def add(self, o):
        out = G(self.d)
        for k, v in o.d.items():
            w = out.d.get(k, [])
            n = max(len(w), len(v))
            w = list(w) + [0] * (n - len(w))
            v2 = list(v) + [0] * (n - len(v))
            out.d[k] = [w[i] + v2[i] for i in range(n)]
        return out

    def scale(self, s):
        return G({k: [s * c for c in v] for k, v in self.d.items()})

    def P(self, a):
        return G({mul(a, k): [c * a ** j for j, c in enumerate(v)] for k, v in self.d.items()})

    def N(self):
        return G({k: (list(v[1:]) if len(v) > 1 else [0]) for k, v in self.d.items()})

    def grade(self, q):
        return G({k: [c * q ** j for j, c in enumerate(v)] for k, v in self.d.items()})

    def C(self, b):
        lb = mp.log(b)
        out = {}
        for k, v in self.d.items():
            bl = mp.exp(lamval(k) * lb)
            out[k] = [bl * mp.fsum(tomp(v[j]) * (-lb) ** (j - l) / mp.factorial(j - l) for j in range(l, len(v)))
                      for l in range(len(v))]
        return G(out)

    def M(self):
        out = {}
        for k, v in self.d.items():
            q = mp.exp(-TWOPI_I * lamval(k))
            out[k] = [q * mp.fsum(tomp(v[j]) * TWOPI_I ** (j - l) / mp.factorial(j - l) for j in range(l, len(v)))
                      for l in range(len(v))]
        return G(out)

    def T(self, a, b):
        return self.C(b).P(a)

    def trimmed(self):
        out = {}
        for k, v in self.d.items():
            w = list(v)
            while w and w[-1] == 0:
                w.pop()
            if w:
                out[k] = w
        return out

    def eq_exact(self, o):
        return self.trimmed() == o.trimmed()

    def dist(self, o):
        diff = self.add(o.scale(-1)).trimmed()
        num = max([abs(tomp(c)) for v in diff.values() for c in v] + [mp.mpf(0)])
        den = max([abs(tomp(c)) for v in self.d.values() for c in v] + [abs(tomp(c)) for v in o.d.values() for c in v]
                  + [mp.mpf('1e-300')])
        return num / den

    def ev(self, l):
        tot = 0
        for k, v in self.d.items():
            tot += mp.exp(-lamval(k) * l) * mp.fsum(tomp(c) * l ** j / mp.factorial(j) for j, c in enumerate(v))
        return h(mp.exp(l)) * tot

    def coords(self):  # {(lam,j): coeff} nonzero
        return {(k, j): c for k, v in self.d.items() for j, c in enumerate(v) if c != 0}


def rank_exact(cols):
    """exact rank of a list of column dicts {rowkey: Fraction/int}"""
    rows = sorted({k for c in cols for k in c}, key=str)
    idx = {r: i for i, r in enumerate(rows)}
    Mx = [[Fr(0)] * len(cols) for _ in rows]
    for j, c in enumerate(cols):
        for k, v in c.items():
            Mx[idx[k]][j] = Fr(v)
    rank = 0
    ncol = len(cols)
    for c in range(ncol):
        piv = next((r for r in range(rank, len(Mx)) if Mx[r][c] != 0), None)
        if piv is None:
            continue
        Mx[rank], Mx[piv] = Mx[piv], Mx[rank]
        pv = Mx[rank][c]
        for r in range(len(Mx)):
            if r != rank and Mx[r][c] != 0:
                f = Mx[r][c] / pv
                Mx[r] = [x - f * y for x, y in zip(Mx[r], Mx[rank])]
        rank += 1
    return rank


# synthetic zero set with collisions (exponents exact); rhoA*{1,2,3,4,6} all "zeros", an off-line zero whose
# double is an on-line zero, and on-line zeros.
rhoA = (Fr(1, 10), Fr(3))
ZC = {rhoA: 2, mul(2, rhoA): 3, mul(3, rhoA): 2, mul(4, rhoA): 1, mul(6, rhoA): 2,
      (Fr(1, 4), Fr(7)): 2, (Fr(1, 2), Fr(14)): 1, (Fr(1, 2), Fr(5)): 2, (Fr(1, 2), Fr(11)): 1}


# ==============================================================================================
def c01():
    eps = mp.mpf('1e-30')
    errs = [rel(F0(eps), mp.mpf(1) / 8), rel(F0(1 + eps), mp.mpf(1) / 8), rel(F0(2), mp.pi / 24),
            rel(F0(-1), mp.pi / 24)]
    wrong = []
    for j in range(1, 6):
        zp = mp.zeta(-2 * j, derivative=1)
        good = j * (2 * j + 1) * (-1) ** j * mp.pi ** j / (2 * mp.factorial(j)) * zp
        bad = j * (2 * j + 1) * (-1) ** j * mp.pi ** j / mp.factorial(2 * j) * zp
        errs += [rel(good, F0(1 + 2 * j)), rel(good, F0(-2 * j + eps))]
        wrong.append(rel(bad, F0(1 + 2 * j)))
    err = max(errs)
    ok = err < 1e-25 and min(wrong[1:]) > 0.5
    rep("C01", ok, "BRC0.3/GJN0.6/HBW0.1: F0(0)=F0(1)=1/8, F0(-1)=F0(2)=pi/24, F0(-2j)=j(2j+1)(-1)^j pi^j zeta'(-2j)/(2*j!) "
        "(j<=5; vs F0(1+2j) and vs near-limit); reading '2j!'=(2j)! fails for j>=2",
        f"max rel {ns(err)}; (2j)! reading min rel dev (j>=2) {ns(min(wrong[1:]))}")


def c02():
    grid = [mp.mpf(k) / 200 for k in range(1, 200)]
    zmax = max(mp.zeta(s) for s in grid)
    etamin = min(mp.altzeta(s) for s in grid)
    e1 = max(rel(mp.altzeta(s), (1 - mp.power(2, 1 - s)) * mp.zeta(s)) for s in grid[::20])
    # paired terms (2j-1)^{-s}-(2j)^{-s} = s int_{2j-1}^{2j} x^{-s-1} dx > 0
    s = mp.mpf('0.37')
    e2 = max(rel((2 * j - 1) ** (-s) - (2 * j) ** (-s), s * mp.quad(lambda x: x ** (-s - 1), [2 * j - 1, 2 * j]))
             for j in (1, 2, 7, 50))
    f0min = min(F0(x) for x in [mp.mpf('1e-30')] + grid + [1 - mp.mpf('1e-30')])
    with mp.workdps(20):
        nz = mp.nzeros(14)
    ok = zmax < 0 and etamin > 0 and e1 < 1e-40 and e2 < 1e-40 and f0min > 0 and nz == 0
    rep("C02", ok, "BRC2.1-2.2/GJN2.3: paired eta terms = s*int x^{-s-1}>0, eta=(1-2^{1-s})zeta, zeta<0 on (0,1) (199 pts), "
        "F0>0 on [0,1], N(14)=0 (so eta0 = Im rho1 = 14.13...)",
        f"max zeta {ns(zmax)}, min eta {ns(etamin)}, rel {ns(max(e1, e2))}, min F0 {ns(f0min, 6)}, N(14)={nz}")


def c03():
    r = mp.mpf('2.5')
    t = mp.mpf('0.1')
    rhos = RHO + [mp.conj(x) for x in RHO]
    eta = min(abs(x.imag) for x in rhos)
    bound = 1 - mp.exp(-2 * mp.pi * eta)
    ok = True
    for rho in rhos:
        sg, ga = rho.real, rho.imag
        d = mp.exp(-1j * ga * mp.log(r)) * (r ** sg - r ** (1 - sg))
        ok &= abs(d) < r - 1 <= r + 1
        ok &= abs(mp.gamma(1 + rho)) <= mp.gamma(1 + sg) <= 1
        ok &= abs(mp.exp(t * (1 - rho) ** 2)) <= mp.exp(t) * mp.exp(-t * ga ** 2) * (1 + mp.mpf('1e-45'))
        for k in range(6):
            for n in (2, 3):
                ok &= abs(mp.exp(-TWOPI_I * n ** k * rho) - 1) >= bound
    random.seed(1)
    et = mp.mpf('0.05')
    bs = 1 - mp.exp(-2 * mp.pi * et)
    minratio = mp.inf
    for _ in range(400):
        sg = mp.mpf(random.random())
        ga = et * (1 + 3 * random.random()) * random.choice([-1, 1])
        if random.random() < 0.3:
            ga = et * random.choice([-1, 1])
        rho = mp.mpc(sg, ga)
        for Nn in (1, 2, 4, 8, 16, 3, 9, 27):
            minratio = min(minratio, abs(mp.exp(-TWOPI_I * Nn * rho) - 1) / bs)
    ok &= minratio >= 1
    rep("C03", ok, "BRC2.3-2.4, BRC10.1-10.2: |d_r(rho)|<r-1<=r+1, |Gamma(1+rho)|<=Gamma(1+Re rho)<=1(<=2), Gaussian bound, "
        "|e^{-2pi i n^k rho}-1| >= 1-e^{-2pi eta} (rho1..3 and conjugates, k<=5; 400 synthetic points, eta=0.05)",
        f"min ratio |e^(-2pi i N rho)-1|/(1-e^(-2pi eta)) on synthetic set = {ns(minratio, 6)} (must be >=1)")


def c04():
    errs = []
    for (m, n) in [(2, 3), (3, 2), (2, 5), (4, 1)]:
        L, R = P_op(m, P_op(n, ftest)), P_op(m * n, ftest)
        errs += [rel(L(l), R(l)) for l in PTS]
    for (k, n) in [(1, 2), (-1, 3), (2, 2)]:
        L, R = M_op(k, P_op(n, ftest)), P_op(n, M_op(n * k, ftest))
        errs += [rel(L(l), R(l)) for l in PTS]
    for n in (2, 3, 4, 5):
        for l in PTS:
            u = mp.exp(l)
            errs.append(rel(h(u) / h(u ** n), u ** (n - 1) * mp.expm1(u) / mp.expm1(u ** n)))
    errs += [rel(P_op(1, ftest)(l), ftest(l)) for l in PTS]
    single = []
    multi = []
    for n in (2, 3):
        g = (lambda n_: (lambda l: mp.exp(l / n_)))(n)
        Pg = P_op(n, g)
        for l in PTS:
            single.append(rel(M_op(1, Pg)(l), Pg(l)))
            multi.append(rel(M_op(1, g)(l), g(l)))
    err = max(errs + single)
    rep("C04", err < 1e-40 and min(multi) > 0.1,
        "BRC1.1-1.2/BRR1 on full germs (cover coordinate): A_n=h(u)/h(u^n)=u^(n-1)(e^u-1)/(e^(u^n)-1); P_mP_n=P_mn; P_1=1; "
        "M^kP_n=P_nM^(nk); P_n(u^(1/n)) single-valued although u^(1/n) is not (ambient non-injectivity)",
        f"max rel {ns(err)}; monodromy defect of u^(1/n) min {ns(min(multi))}")


def c05():
    errs = []
    wrong = []
    for (a, b) in [(2, 3), (3, 2), (2, 5)]:
        L, R = C_op(b, P_op(a, ftest)), P_op(a, C_op(b ** a, ftest))
        errs += [rel(L(l), R(l)) for l in PTS]
        L2, R2 = T_op(a, b, ftest), P_op(a, C_op(b, ftest))
        errs += [rel(L2(l), R2(l)) for l in PTS]
    for (a, b, c, d) in [(2, 3, 3, 2), (3, 2, 2, 5), (2, 2, 2, 3)]:
        L = T_op(a, b, T_op(c, d, ftest))
        R = T_op(a * c, b ** c * d, ftest)
        errs += [rel(L(l), R(l)) for l in PTS]
        W1, W2 = T_op(a * c, b * d ** a, ftest), T_op(a * c, b * d, ftest)
        wrong += [max(rel(L(l), W1(l)) for l in PTS), max(rel(L(l), W2(l)) for l in PTS)]
    for (a, b, k) in [(2, 3, 3), (3, 2, 2), (1, 5, 3)]:
        F = ftest
        for _ in range(k):
            F = T_op(a, b, F)
        R = T_op(a ** k, b ** sum(a ** i for i in range(k)), ftest)
        errs += [rel(F(l), R(l)) for l in PTS]
    err = max(errs)
    rep("C05", err < 1e-40 and min(wrong) > 1e-3,
        "GJN5.4-5.5/GJNR4.5/GJNR7.3 on full germs: C_bP_a=P_aC_{b^a}; T_{a,b}=P_aC_b; T_{a,b}T_{c,d}=T_{ac,b^c d} "
        "(the forms b d^a and b d fail); T_{a,b}^k = T_{a^k, b^(1+a+...+a^(k-1))}",
        f"max rel {ns(err)}; min deviation of wrong forms {ns(min(wrong))}")


def Hf(lam, j):
    return lambda l: h(mp.exp(l)) * mp.exp(-lam * l) * l ** j / mp.factorial(j)


def Vf(lam, j):
    return lambda l: mp.expm1(mp.exp(l)) * mp.exp((-1 - lam) * l) * (-l) ** j / mp.factorial(j)


def c06():
    errs = []
    for rho in RHO[:2]:
        g = (lambda r_: (lambda l: mp.expm1(mp.exp(l)) * mp.exp((-1 - r_) * l)))(rho)
        for n in (2, 3, 5):
            Pg = P_op(n, g)
            for l in LP:
                u = mp.exp(l)
                errs.append(rel(Pg(l), mp.expm1(u) * mp.exp((-1 - n * rho) * l)))
                sheet = mp.fsum(mp.exp(a * u / n) * mp.expm1(u / n) * mp.exp((-1 - rho) * (l - mp.log(n)))
                                for a in range(n)) / n
                errs.append(rel(sheet, mp.power(n, rho) * mp.expm1(u) * mp.exp((-1 - rho) * l)))
                errs.append(rel(mp.fsum(mp.exp(r * u / n) for r in range(n)) / n, h(u) / h(u / n)))
        q = mp.exp(-TWOPI_I * rho)
        for j in range(4):
            for n in (2, 3):
                PV = P_op(n, Vf(rho, j))
                errs += [rel(PV(l), n ** j * Vf(n * rho, j)(l)) for l in LP]
            MV = M_op(1, Vf(rho, j))
            for l in LP:
                rhs = q * mp.fsum((-TWOPI_I) ** a / mp.factorial(a) * Vf(rho, j - a)(l) for a in range(j + 1))
                errs.append(rel(MV(l), rhs))
                dv = mp.diff(lambda r_: mp.expm1(mp.exp(l)) * mp.exp((-1 - r_) * l), rho, j) / mp.factorial(j)
                errs.append(rel(dv, Vf(rho, j)(l)))
    err = max(errs)
    rep("C06", err < 1e-30,
        "BRC3.1, BRC3.4, GJN7.4/GJNR8.5, BRC8.1-8.2 at actual rho1,rho2 (n=2,3,5; j<=3): P_n[(e^u-1)u^(-1-rho)]=(e^u-1)u^(-1-n rho); "
        "omega=1 sheet sum = n^rho (e^u-1)u^(-1-rho); (1/b)sum e^(ru/b)=h(u)/h(u/b); P_nV=n^j V_(n rho); MV formula; V=(1/j!)d^j/drho^j",
        f"max rel {ns(err)}")


def c07():
    def phi(m, s):
        return -1 / s if m == 0 else (mp.power(m, 1 - s) - mp.power(m + 1, 1 - s)) / s

    t = mp.mpf('0.1')
    errs = []
    for s in (mp.mpc('0.3', '2.1'), 1 - RHO[0]):
        corr = 8 * F0(s) / s
        gt = mp.exp(t * s * s)
        for n in (2, 3, 5):
            for q in range(16):
                lhs = gt * mp.fsum(phi(n * q + a, s) + corr for a in range(n))
                rhs = gt * (mp.power(n, 1 - s) * (phi(q, s) + corr) + (n - mp.power(n, 1 - s)) * corr)
                errs.append(rel(lhs, rhs))
                errs.append(rel(mp.fsum(phi(n * q + a, s) for a in range(n)), mp.power(n, 1 - s) * phi(q, s)))
    s = 1 - RHO[0]
    corr_rel = abs(mp.exp(t * s * s) * 8 * F0(s) / s) / abs(mp.exp(t * s * s))  # correction relative to the Gaussian
    random.seed(7)
    cs = [mp.mpc(random.gauss(0, 1), random.gauss(0, 1)) for _ in range(30)]
    fpoly = lambda z: mp.fsum(c * z ** k for k, c in enumerate(cs))
    for n in (2, 3, 5):
        z = mp.mpc('0.3', '0.2')
        zr = mp.power(z, mp.mpf(1) / n)
        roots = [mp.exp(TWOPI_I * k / n) for k in range(n)]
        sheet = mp.fsum(w ** (-a) * mp.power(z, -mp.mpf(a) / n) * fpoly(w * zr) for w in roots for a in range(n)) / n
        coef = mp.fsum(mp.fsum(cs[n * qq + a] for a in range(n) if n * qq + a < 30) * z ** qq for qq in range(30 // n + 1))
        errs.append(rel(sheet, coef))
    err = max(errs)
    rep("C07", err < 1e-35 and corr_rel < 1e-40,
        "HBW4.1/4.3, BNS5.3, GJN7.5, GJNR8.6: sum_(a<n) psi_(nq+a) = n^(1-s) psi_q + (n-n^(1-s)) 8F0/s (q<=15; n=2,3,5; generic s and "
        "s=1-rho1); W_n*K_s=n^(1-s)K_s coefficientwise; sheet formula = coefficient formula; correction at s=1-rho1 vs Gaussian",
        f"max rel {ns(err)}; |8F0(s)/s| at s=1-rho1 relative to e^(ts^2): {ns(corr_rel)}")


def c08():
    t = mp.mpf('0.1')
    rho = RHO[0]
    s0 = 1 - rho
    c = mp.taylor(lambda s: Ct(s, t), s0, 4)
    e = mp.taylor(lambda s: 1 / Ct(s, t), s0, 4)
    errs = []
    for m in range(5):
        errs.append(abs(mp.fsum(c[i] * e[m - i] for i in range(m + 1)) - (1 if m == 0 else 0)))
    d = [1 / c[0]]
    for k in range(1, 5):
        d.append(-mp.fsum(c[a] * d[k - a] for a in range(1, k + 1)) / c[0])
    errs += [rel(d[k], e[k]) for k in range(5)]
    for l in LP[:4]:
        u = mp.exp(l)
        S = [mp.diff(lambda s: Ct(s, t) * h(u) * mp.exp((s - 1) * l), s0, j) / mp.factorial(j) for j in range(4)]
        for j in range(4):
            viaH = mp.fsum(c[j - k] * Hf(rho, k)(l) for k in range(j + 1))
            viaV = mp.fsum((-1) ** k * c[j - k] * Vf(rho, k)(l) for k in range(j + 1))
            errs += [rel(S[j], viaH), rel(S[j], viaV)]
            inv = (-1) ** j * mp.fsum(e[j - k] * S[k] for k in range(j + 1))
            errs.append(rel(inv, Vf(rho, j)(l)))
    err = max(errs)
    rep("C08", err < 1e-25,
        "BNS0.1/HBW2.3, GJN1.2-1.3, BRC8.4 at actual rho1 (t=0.1, j<=3): S_j:=(1/j!)d^j/ds^j[C_t h u^(s-1)] = sum c_(j-l)H_(rho,l) "
        "= sum (-1)^k c_(j-k) V_(rho,k); inverse via Taylor coeffs of 1/C_t; GJN1.3 recursion = those coeffs",
        f"max rel {ns(err)} (all quantities carry the factor e^(t(1-rho)^2)Gamma(1+rho) ~ {ns(abs(Ct(s0, t)))})")


def c09():
    t = mp.mpf('0.1')
    rho = RHO[0]
    s0 = 1 - rho
    c = mp.taylor(lambda s: Ct(s, t), s0, 4)
    errs = []
    wrongs = []
    for (a, b) in [(2, 3), (3, 2)]:
        lb = mp.log(b)
        cw = mp.taylor(lambda s: Ct(s, t), 1 - a * rho, 4)
        for l in LP[:3]:
            def F(s, l=l, a=a, b=b):
                base = lambda L: h(mp.exp(L)) * mp.exp((s - 1) * L)
                return Ct(s, t) * T_op(a, b, base)(l)
            for j in range(4):
                lhs = mp.diff(F, s0, j) / mp.factorial(j)

                def rhs(cc):
                    tot = 0
                    for ell in range(j + 1):
                        inner = mp.fsum(cc[j - r] * (-lb) ** (r - ell) / mp.factorial(r - ell) for r in range(ell, j + 1))
                        tot += a ** ell * Hf(a * rho, ell)(l) * inner
                    return mp.power(b, rho) * tot
                errs.append(rel(lhs, rhs(c)))
                wrongs.append(rel(lhs, rhs(cw)))
    err = max(errs)
    rep("C09", err < 1e-25 and min(wrongs) > 0.5,
        "GJN7.1-7.3/GJNR8.2-8.3 at actual rho1 ((a,b)=(2,3),(3,2); j<=3): T_(a,b)S_(t,1-rho,j) = b^rho sum a^l H_(a rho,l) "
        "sum_r C_t^(j-r)(1-rho)/(j-r)! (-log b)^(r-l)/(r-l)!; using C_t(1-a rho) instead fails",
        f"max rel {ns(err)}; min rel deviation with C_t(1-a rho) {ns(min(wrongs))}")


def c10():
    t = mp.mpf('0.1')
    rho = RHO[0]
    s0 = 1 - rho
    n = 2
    sn = 1 + n * (s0 - 1)
    Dn = mp.taylor(lambda s: Ct(s, t) / Ct(1 + n * (s - 1), t), s0, 4)
    errs = []
    nonsc = []
    for l in LP[:3]:
        u = mp.exp(l)
        Sp = [mp.diff(lambda sg: Ct(sg, t) * h(u) * mp.exp((sg - 1) * l), sn, k) / mp.factorial(k) for k in range(4)]

        def F(s, l=l):
            return Ct(s, t) * P_op(n, lambda L: h(mp.exp(L)) * mp.exp((s - 1) * L))(l)
        for j in range(4):
            lhs = mp.diff(F, s0, j) / mp.factorial(j)
            rhs = mp.fsum(Dn[j - k] * n ** k * Sp[k] for k in range(j + 1))
            errs.append(rel(lhs, rhs))
            nonsc.append(rel(lhs, n ** j * Sp[j]))
    C0, Cn = Ct(s0, t), Ct(sn, t)
    dC0, dCn = mp.diff(lambda s: Ct(s, t), s0), mp.diff(lambda s: Ct(s, t), sn)
    errs.append(rel(Dn[1], dC0 / Cn - n * C0 * dCn / Cn ** 2))
    m = 4
    A = mp.matrix(m, m)
    for j in range(m):
        for k in range(j + 1):
            A[k, j] = Dn[j - k] * n ** k
    Lw = mp.matrix(m, m)
    for j in range(1, m):
        Lw[j - 1, j] = 1
    errs.append(mp.mnorm(Lw * A - n * A * Lw, 1) / mp.mnorm(A, 1))
    err = max(errs)
    rep("C10", err < 1e-25 and min(nonsc) > 1e-3,
        "BNS3.3-3.6, BNS4.4 at actual rho1 (n=2, s=1-rho1, s_n=1+n(s-1)=1-2rho1, j<=3): P_nS_(t,s,j) = sum D_n^(j-k)/(j-k)! n^k S_(t,s_n,k), "
        "D_n=C_t(s)/C_t(s_n); D_n' formula; N_out P_n = n P_n N_s in these bases; P_nS_j != n^j S_(t,s_n,j)",
        f"max rel {ns(err)}; min rel gap to n^j S_(s_n,j) {ns(min(nonsc))}")


def c11():
    errs = []
    with mp.workdps(40):
        lam0 = mp.mpc('0.3', '1.7')
        lams = [lam0, lam0 + 1, lam0 + 2, lam0 + mp.mpc(0, '0.25'), 2 * lam0]
        funcs = [(lambda lm, jj: (lambda l: h(mp.exp(l)) * mp.exp(-lm * l) * l ** jj / mp.factorial(jj)))(lm, jj)
                 for lm in lams for jj in range(3)]
        # sample points spread over |u| in (e^-4, e^-0.2) and arg u in (-8, 8) on the cover
        pts = [mp.mpc(-4 + mp.mpf(38) / 110 * k, -8 + mp.mpf(16) / 9 * m) for k in range(12) for m in range(10)]
        A = mp.matrix(len(pts), len(funcs))
        for cix, f in enumerate(funcs):
            col = [f(l + TWOPI_I) - f(l) for l in pts]  # monodromy difference (M-I)f
            nrm = mp.sqrt(mp.fsum(abs(x) ** 2 for x in col))
            for rix, x in enumerate(col):
                A[rix, cix] = x / nrm
        sv = mp.svd_c(A, compute_uv=False)
        smin = min(sv[i] for i in range(sv.rows))
        # BNS1 exceptional case: exponent u^a with a = 2 (lam=-2): constants holomorphic, log-terms not
        f0 = lambda l: h(mp.exp(l)) * mp.exp(2 * l)
        f1 = lambda l: h(mp.exp(l)) * mp.exp(2 * l) * l
        exc0 = max(rel(f0(l + TWOPI_I), f0(l)) for l in pts[:5])
        exc1 = min(abs(f1(l + TWOPI_I) - f1(l)) / abs(f1(l)) for l in pts[:5])
    q, w = sp.symbols('q w')
    d = 5
    Mx = sp.zeros(d, d)
    for j in range(d):
        bj = w ** j / sp.factorial(j)
        img = sp.Poly(sp.expand(q * bj.subs(w, w + 2 * sp.pi * sp.I) - bj), w)
        for k in range(d):
            Mx[k, j] = sp.simplify(img.coeff_monomial(w ** k) * sp.factorial(k))
    tri = all(Mx[k, j] == 0 for k in range(d) for j in range(d) if k > j)
    dia = all(sp.simplify(Mx[k, k] - (q - 1)) == 0 for k in range(d))
    ok = smin > 1e-20 and exc0 < 1e-35 and exc1 > 0.1 and tri and dia   # noise floor at 40 digits ~1e-38
    rep("C11", ok,
        "GJN1.4/GJNR2.2/BNS1/BNS6: classes h u^(-lam)(log u)^j, j<3, for lam in {l0,l0+1,l0+2,l0+0.25i,2l0} (integer differences, equal "
        "monodromy eigenvalues) have injective monodromy difference (sampled SVD, 120 pts, 40 digits); p->q p(w+2pi i)-p triangular, "
        "diagonal q-1 (sympy); BNS1 exceptional case u^2 (holomorphic) vs u^2 log u",
        f"min singular value (normalised cols) {ns(smin)} vs noise ~1e-38; u^2 monodromy defect {ns(exc0)}; u^2 log u defect {ns(exc1)}")


def c12():
    random.seed(12)
    v = G()
    for lam, m in ZC.items():
        for j in range(m):
            v = v.add(G.H(lam, j, Fr(random.randint(-9, 9), random.randint(1, 5))))
    w_ = v.add(v.P(2)).add(v.P(3).scale(Fr(2, 7)))  # an element of the closure E~ (with collisions)
    exact = True
    for b in (2, 3, 5):
        exact &= w_.P(b).N().eq_exact(w_.N().P(b).scale(b))           # N P_b = b P_b N
        exact &= w_.N().P(b).eq_exact(w_.P(b).N().scale(Fr(1, b)))    # P_b N = b^-1 N P_b
    grading = True
    for qq in (2, 3, Fr(1, 2)):
        grading &= v.grade(qq).N().scale(1).eq_exact(v.N().grade(qq).scale(qq))  # N Gamma_q = q Gamma_q N on E itself
        grading &= set(v.grade(qq).trimmed()) <= set(ZC)
    # monodromy-defined N (BNS4.3 finite log series), germ level, actual and synthetic exponents

    def NM(g, q, d):
        def out(l):
            tot = 0
            for k in range(1, d):
                dk = mp.fsum(mp.binomial(k, i) * (-1) ** (k - i) * q ** (-i) * g(l + i * TWOPI_I) for i in range(k + 1))
                tot += (-1) ** (k + 1) * dk / k
            return tot / TWOPI_I
        return out
    errs = []
    defect = []
    pc = [mp.mpc('0.7', '-0.2'), mp.mpc('-1.1', '0.4'), mp.mpc('0.3', '0.9'), mp.mpc('0.5', '0.5')]
    for lam in (RHO[0], mp.mpc('0.1', '3')):
        f = (lambda lm: (lambda l: h(mp.exp(l)) * mp.exp(-lm * l) * mp.fsum(pc[j] * l ** j / mp.factorial(j) for j in range(4))))(lam)
        q = mp.exp(-TWOPI_I * lam)
        Nf = NM(f, q, 4)
        for l in LP[:3]:
            ex = h(mp.exp(l)) * mp.exp(-lam * l) * mp.fsum(pc[j] * l ** (j - 1) / mp.factorial(j - 1) for j in range(1, 4))
            errs.append(rel(Nf(l), ex))
        for b in (2, 3):
            lhs, rhs = NM(P_op(b, f), q ** b, 4), P_op(b, Nf)
            errs += [rel(lhs(l), b * rhs(l)) for l in LP[:3]]
            lhsC, rhsC = NM(C_op(b, f), q, 4), C_op(b, Nf)
            errs += [rel(lhsC(l), rhsC(l)) for l in LP[:3]]
            defect += [rel(lhsC(l), b * rhsC(l)) for l in LP[:3]]
            for a in (2, 3):
                lhsT, rhsT = NM(T_op(a, b, f), q ** a, 4), T_op(a, b, Nf)
                errs += [rel(lhsT(l), a * rhsT(l)) for l in LP[:3]]
    err = max(errs)
    ok = exact and grading and err < 1e-30 and min(defect) > 0.1
    rep("C12", ok,
        "GJN4.4/GJNR3.6/BNS4.4 norm-shift: exact N P_b = b P_b N and P_b N = b^-1 N P_b on a colliding closure element (b=2,3,5); "
        "germ level with N:=(2pi i)^-1 log(q^-1 M) (finite series): N P_b = b P_b N, N C_b = C_b N, N T_(a,b) = a T_(a,b) N (rho1 and 0.1+3i); "
        "C_b violates the b-scaling; the E-preserving grading H_(rho,j)->q^j H_(rho,j) also satisfies N G = q G N",
        f"exact={exact}, grading={grading}; max rel {ns(err)}; min rel defect of C_b {ns(min(defect))}")


def c13():
    A_ = 12
    tags = [(a, r, j) for a in range(1, A_ + 1) for r in ZC for j in range(ZC[r])]
    cols = []
    for (a, r, j) in tags:
        img = G.H(r, j).P(a)   # Pi(e_{a,rho,j}) = [P_a H_{rho,j}]
        cols.append(img.coords())
    exact_form = all(cols[i] == {(mul(a, r), j): a ** j} for i, (a, r, j) in enumerate(tags))
    rk = rank_exact(cols)
    fib = {}
    for (a, r, j) in tags:
        fib.setdefault((mul(a, r), j), []).append((a, r))
    exp_ker = sum(len(v) - 1 for v in fib.values())
    kerdim = len(tags) - rk
    basis = []
    for (lam, j), prs in fib.items():
        a0, r0 = prs[0]
        for (a, r) in prs[1:]:
            vec = {(a, r, j): Fr(1, a ** j), (a0, r0, j): -Fr(1, a0 ** j)}
            basis.append(vec)
    idx = {tg: i for i, tg in enumerate(tags)}
    inker = True
    for vec in basis:
        tot = {}
        for tg, cf in vec.items():
            for key, val in cols[idx[tg]].items():
                tot[key] = tot.get(key, 0) + cf * val
        inker &= all(x == 0 for x in tot.values())
    rb = rank_exact([{tg: cf for tg, cf in vec.items()} for vec in basis])
    maxfib = max(len(v) for v in fib.values())
    # descent of scaled lowering and of ramification; failure of unscaled lowering
    desc = True
    unscaled_fail = 0
    for (a, r, j) in tags:
        Pi = lambda aa, rr, jj: G.H(rr, jj).P(aa)
        if j >= 1:
            desc &= Pi(a, r, j - 1).scale(a).eq_exact(Pi(a, r, j).N())           # Pi Nhat = N Pi
            unscaled_fail += (not Pi(a, r, j - 1).eq_exact(Pi(a, r, j).N()))
        for b in (2, 3):
            if a * b <= A_:
                desc &= Pi(a * b, r, j).eq_exact(Pi(a, r, j).P(b))                # Pi Phat_b = P_b Pi
    # tagged counting (GJNR4.1-4.4), numerically

    def Chat(b, vec):  # vec: {(a,r,j): coeff}
        out = {}
        lb = mp.log(b)
        for (a, r, j), cf in vec.items():
            bl = mp.exp(a * lamval(r) * lb)
            for l in range(j + 1):
                out[(a, r, l)] = out.get((a, r, l), 0) + tomp(cf) * bl * (-a * lb) ** (j - l) / mp.factorial(j - l)
        return out

    def Phat(b, vec):
        return {(b * a, r, j): cf for (a, r, j), cf in vec.items()}

    def PiV(vec):
        g = G()
        for (a, r, j), cf in vec.items():
            g = g.add(G.H(r, j, cf).P(a))
        return g

    def vdist(x, y):
        keys = set(x) | set(y)
        num = max(abs(tomp(x.get(k, 0)) - tomp(y.get(k, 0))) for k in keys)
        den = max([abs(tomp(v)) for v in list(x.values()) + list(y.values())] + [mp.mpf('1e-300')])
        return num / den
    errs = []
    small = [tg for tg in tags if tg[0] <= 3]
    for tg in small:
        e = {tg: 1}
        for b in (2, 3):
            errs.append(PiV(Chat(b, e)).dist(PiV(e).C(b)))                     # Pi Chat_b = C_b Pi
            for a in (2, 3):
                errs.append(vdist(Chat(b, Phat(a, e)), Phat(a, Chat(b ** a, e))))   # Chat_b Phat_a = Phat_a Chat_{b^a}
        Th = lambda a, b, x: Phat(a, Chat(b, x))
        for (a, b, c, d) in [(2, 3, 2, 2), (3, 2, 2, 3)]:
            errs.append(vdist(Th(a, b, Th(c, d, e)), Th(a * c, b ** c * d, e)))
    # actual zeros: no collisions among {c*rho: c<=7, |Im rho|<=100} (all actual zeros there lie on Re=1/2)
    with mp.workdps(20):
        gam = [mp.zetazero(k).imag for k in range(1, 30)]
        Zact = [mp.mpc(0.5, g) for g in gam] + [mp.mpc(0.5, -g) for g in gam]
        pts = [(c, z) for c in range(1, 8) for z in Zact]
        mind = min(abs(c1 * z1 - c2 * z2) for (c1, z1) in pts for (c2, z2) in pts if (c1, z1) != (c2, z2))
    err = max(errs)
    ok = exact_form and kerdim == exp_ker and inker and rb == len(basis) == exp_ker and desc and unscaled_fail > 0 \
        and err < 1e-35 and mind > 0.1
    rep("C13", ok,
        f"GJN3.1-3.4/GJN4.2-4.3/GJNR3-4 tagged space (synthetic colliding set, tags a<=12, {len(tags)} tags, max fibre {maxfib}): "
        "Pi e=a^j[H_(a rho,j)], dim ker Pi = sum(fibre-1), GJN3.4 vectors in ker and a basis; Pi Nhat=N Pi, Pi Phat_b=P_b Pi, unscaled lowering fails; "
        "Pi Chat_b=C_b Pi, Chat_b Phat_a=Phat_a Chat_(b^a), That comp. law; actual zeros |Im|<=100: no collisions c rho=c' rho'",
        f"dim ker={kerdim} (formula {exp_ker}), basis rank {rb}; unscaled failures {unscaled_fail}; max rel {ns(err)}; "
        f"min |c rho - c' rho'| (actual) {ns(mind)}")


def dval_factory(Z, cap=None):
    eta0 = min(abs(k[1]) for k in Z)

    def dval(lam):
        best = 0
        cmax = int(abs(Fr(lam[1])) / eta0)
        if cap is not None:
            cmax = min(cmax, cap)
        for c in range(1, cmax + 1):
            r = (Fr(lam[0]) / c, Fr(lam[1]) / c)
            if r in Z:
                best = max(best, Z[r])
        return best
    return dval


def c14():
    dval = dval_factory(ZC)
    W = sorted({mul(c, r) for c in range(1, 13) for r in ZC}, key=lambda k: (k[1], k[0]))
    dW = {lam: dval(lam) for lam in W}
    # GJN2.4: E~ = sum_a P_a E (window), exactly the blocks j<d_lam; stability d_(b lam) >= d_lam
    gens = []
    for a in range(1, 13):
        for r, m in ZC.items():
            for j in range(m):
                gens.append(G.H(r, j).P(a).coords())
    d12 = dval_factory(ZC, cap=12)   # the window generators only use tags a <= 12
    span_ok = rank_exact(gens) == sum(d12(lam) for lam in W) and \
        {k for g in gens for k in g} == {(lam, j) for lam in W for j in range(d12(lam))}
    stab = all(dval(mul(b, lam)) >= dW[lam] for lam in W for b in (2, 3))
    out = {}
    blocks_ok = True
    for a in (2, 3, 4, 5):
        imgs = []
        for lam in W:
            mu = (Fr(lam[0]) / a, Fr(lam[1]) / a)
            for j in range(dval(mu)):
                im_ = G.H(mu, j).P(a)
                blocks_ok &= all(jj < dW[k] for (k, jj) in im_.coords())      # image inside E~
                imgs.append(im_.coords())
        rk = rank_exact(imgs) if imgs else 0
        cok = sum(dW.values()) - rk
        formula = sum(dW[lam] - dval((Fr(lam[0]) / a, Fr(lam[1]) / a)) for lam in W)
        # the image in each lam-block is exactly the degrees j < d_(lam/a)
        for lam in W:
            got = {jj for im_ in imgs for (k, jj) in im_ if k == lam}
            blocks_ok &= got == set(range(dval((Fr(lam[0]) / a, Fr(lam[1]) / a))))
        low = min(W, key=lambda k: abs(k[1]))
        lowfull = dval((low[0] / a, low[1] / a)) == 0 and dW[low] == ZC[low]
        out[a] = (cok, formula, lowfull)
    # partial block produced by a collision: lam = 6 rhoA, a = 2: degrees {2}
    lam6 = mul(6, rhoA)
    partial = (dW[lam6], dval(mul(3, rhoA))) == (3, 2)
    # induced operators on the quotient block at lam* = rhoA (q=0,r=2) and at rhoB=(1/4,7) (q=0,r=2), a=2
    errs = []
    for lam in (rhoA, (Fr(1, 4), Fr(7))):
        qd = dval((lam[0] / 2, lam[1] / 2))
        rr = dW.get(lam, dval(lam)) - qd
        lamc = lamval(lam)
        for b in (2, 3):
            Cq = mp.matrix(rr, rr)
            Mq = mp.matrix(rr, rr)
            for l_ in range(rr):
                imgC = G.H(lam, qd + l_).C(b).d[lam]
                imgM = G.H(lam, qd + l_).M().d[lam]
                for k in range(qd, qd + l_ + 1):
                    Cq[k - qd, l_] = imgC[k]
                    Mq[k - qd, l_] = imgM[k]
            Nb = mp.matrix(rr, rr)
            for l_ in range(1, rr):
                Nb[l_ - 1, l_] = 1
            Cf = mp.exp(lamc * mp.log(b)) * sum(((-mp.log(b)) ** k / mp.factorial(k) * Nb ** k for k in range(1, rr)), mp.eye(rr))
            Mf = mp.exp(-TWOPI_I * lamc) * sum((TWOPI_I ** k / mp.factorial(k) * Nb ** k for k in range(1, rr)), mp.eye(rr))
            errs.append(mp.mnorm(Cq - Cf, 1) / mp.mnorm(Cf, 1))
            errs.append(mp.mnorm(Mq - Mf, 1) / mp.mnorm(Mf, 1))
    err = max(errs)
    ok = span_ok and stab and blocks_ok and all(c == f and lf for (c, f, lf) in out.values()) and partial and err < 1e-40
    rep("C14", ok,
        "GJN2.4 closure (window c<=12, synthetic colliding set): sum_a P_aE = (+) span{H_(lam,j): j<d_lam}, d_(b lam)>=d_lam; GJNR6.1-6.5: "
        "image of P_a in lam-block = degrees j<d_(lam/a), coker P_a = (+) span{H_(lam,j): d_(lam/a)<=j<d_lam} (a=2..5), lowest-height block "
        "fully in coker, collision partial block at 6rhoA; induced C_b=b^lam exp(-log b N), M=e^(-2pi i lam)exp(2pi i N) on quotient blocks",
        f"coker dims (computed,formula) {[(a, out[a][0], out[a][1]) for a in out]}; induced-operator max rel {ns(err)}")


def c15():
    r0 = (Fr(1, 20), Fr(2))
    ZR = {r0: 3, mul(2, r0): 2, mul(4, r0): 4, mul(8, r0): 1, mul(16, r0): 2,
          (Fr(3, 10), Fr(5)): 2, (Fr(3, 5), Fr(10)): 3, (Fr(1, 2), Fr(7)): 2, (Fr(1, 2), Fr(14)): 1,
          (Fr(1, 10), Fr(3)): 2, (Fr(3, 10), Fr(9)): 1, (Fr(9, 10), Fr(27)): 2}
    basis = [(r, j) for r in ZR for j in range(ZR[r])]
    mZ = lambda lam: ZR.get(lam, 0)
    results = {}
    allok = True
    comp_err = []
    for a in (2, 3):
        for b in (1, 3):
            # compare iterate with the closed form GJNR7.3 in the germ algebra
            for (r, j) in basis[:6]:
                x = G.H(r, j)
                y = x
                for k in range(1, 4):
                    y = y.T(a, b)
                    z = x.T(a ** k, b ** sum(a ** i for i in range(k)))
                    comp_err.append(y.dist(z))
            for L in range(0, 7):
                rows = {}
                for ci, (r, j) in enumerate(basis):
                    y = G.H(r, j)
                    for k in range(1, L + 1):
                        y = y.T(a, b)
                        for (lam, jj), cf in y.coords().items():
                            if jj >= mZ(lam):  # outside E (includes lam not a zero)
                                rows.setdefault((k, lam, jj), {})[ci] = tomp(cf)
                Om = np.zeros((max(len(rows), 1), len(basis)), dtype=complex)
                for ri, (key, dct) in enumerate(rows.items()):
                    rmax = max(abs(v) for v in dct.values())   # row scaling (kernel unchanged) avoids float overflow
                    for ci, val in dct.items():
                        Om[ri, ci] = complex(val / rmax)
                cn = np.linalg.norm(Om, axis=0)
                Omn = Om / np.where(cn > 0, cn, 1)
                sv = np.linalg.svd(Omn, compute_uv=False) if len(rows) else np.array([])
                rank = int(np.sum(sv > 1e-10))
                kdim = len(basis) - rank
                mu = {r: min(mZ(mul(a ** k, r)) for k in range(L + 1)) for r in ZR}
                pred = sum(mu.values())
                predvec_ok = all(cn[ci] == 0 for ci, (r, j) in enumerate(basis) if j < mu[r])
                allok &= (kdim == pred) and predvec_ok
                results[(a, b, L)] = kdim
    # one-step block return criterion (GJN6.3): whole block returns iff a rho in Z and m_rho <= m_(a rho)
    block_ok = True
    for a in (2, 3):
        for r in ZR:
            y = G.H(r, ZR[r] - 1).P(a)
            returns = all(jj < mZ(lam) for (lam, jj) in y.coords())
            block_ok &= returns == (mZ(mul(a, r)) >= ZR[r])
    zero_after = results[(2, 1, 5)] == 0 and results[(2, 3, 6)] == 0 and results[(3, 1, 3)] == 0
    bind = all(results[(a, 1, L)] == results[(a, 3, L)] for a in (2, 3) for L in range(7))
    # actual zeros: {rho : a rho in Z} is empty for a=2..10 on the verified range (Re(a rho)=a/2>=1)
    with mp.workdps(20):
        Zact = [mp.zetazero(k) for k in range(1, 30)]
        act_empty = all(abs(a * z1 - z2) > 0.1 for a in range(2, 11) for z1 in Zact for z2 in Zact)
    ok = allok and block_ok and zero_after and bind and max(comp_err) < 1e-40 and act_empty
    rep("C15", ok,
        "GJN6.3/GJNR7.2-7.5 (synthetic chains r0,2r0,..,16r0 with m=3,2,4,1,2 etc.): E_(a,L)={v in E: T_(a,b)^k v in E, k<=L} = "
        "(+)_rho span{H_(rho,j): j<min_(0<=k<=L) m_(a^k rho)} (a=2,3; b=1,3; L<=6), independent of b, =0 once a^k Re rho>=1; "
        "block returns iff m_rho<=m_(a rho); T^k = T_(a^k, b^(1+..+a^(k-1))) in germ algebra; actual rho_k (k<30): a rho never a zero",
        f"dims a=2,b=1: {[results[(2, 1, L)] for L in range(7)]}, a=3,b=1: {[results[(3, 1, L)] for L in range(7)]}; "
        f"iterate max rel {ns(max(comp_err))}")


def c16():
    lamf = (Fr(1, 5), Fr(4))
    lam = lamval(lamf)
    errs = []
    ranks_ok = True
    for d in range(1, 6):
        Nm = mp.matrix(d, d)
        for j in range(1, d):
            Nm[j - 1, j] = 1
        for b in (1, 2, 3, 7):
            Cm = mp.matrix(d, d)
            for j in range(d):
                v = G.H(lamf, j).C(b).d[lamf]
                for k in range(len(v)):
                    Cm[k, j] = v[k]
            form = mp.exp(lam * mp.log(b)) * sum(((-mp.log(b)) ** k / mp.factorial(k) * Nm ** k for k in range(1, d)), mp.eye(d))
            errs.append(mp.mnorm(Cm - form, 1) / mp.mnorm(form, 1))
            errs.append(mp.mnorm(Cm * Nm - Nm * Cm, 1) / mp.mnorm(Cm, 1))
            Dm = Cm * Nm - Nm * Cm / b
            errs.append(mp.mnorm(Dm - (1 - mp.mpf(1) / b) * Cm * Nm, 1) / mp.mnorm(Cm, 1))
            Dn_ = np.array([[complex(Dm[i, k]) for k in range(d)] for i in range(d)])
            rk = np.linalg.matrix_rank(Dn_ / max(np.abs(Dn_).max(), 1e-300), tol=1e-10) if np.abs(Dn_).max() > 1e-30 else 0
            ranks_ok &= rk == ((d - 1) if b >= 2 else 0)
    # germ algebra C_b vs function-level C_op
    g = G.H(lamf, 3, Fr(2, 3)).add(G.H((Fr(7, 10), Fr(-1)), 2, Fr(-1, 2)))
    for b in (2, 3):
        Cg = g.C(b)
        errs += [rel(Cg.ev(l), C_op(b, g.ev)(l)) for l in LP]
        errs += [rel(g.M().ev(l), M_op(1, g.ev)(l)) for l in LP]
        errs += [rel(g.P(b).ev(l), P_op(b, g.ev)(l)) for l in LP]
    # faithfulness: |b^rho1| = b^(1/2) strictly increasing, exponents a*rho distinct
    mods = [abs(mp.power(b, RHO[0])) for b in range(1, 41)]
    faith = all(mods[i] < mods[i + 1] for i in range(39))
    err = max(errs)
    rep("C16", err < 1e-40 and ranks_ok and faith,
        "GJN5.1-5.3/BNS2.1-2.2/HBW5.1: C_b on a length-d block (d<=5) = b^lam exp(-(log b)N), commutes with N, "
        "C_bN - b^-1 N C_b = (1-b^-1)C_bN of rank d-1 (b=2,3,7), 0 (b=1); germ algebra agrees with function-level C_b, M, P_b; "
        "faithfulness: |b^rho1| strictly increasing in b",
        f"max rel {ns(err)}; ranks ok={ranks_ok}")


def c17():
    errs = []
    for lam in (mp.mpc('0.2', '4'), RHO[0], mp.mpc('0.9', '-2.5'), mp.mpc('0.35', '0.6')):
        q = mp.exp(-TWOPI_I * lam)
        for d in (1, 3, 5):
            Nm = mp.matrix(d, d)
            for j in range(1, d):
                Nm[j - 1, j] = 1
            U = sum((TWOPI_I ** k / mp.factorial(k) * Nm ** k for k in range(1, d)), mp.eye(d))
            Mm = q * U
            D = U - mp.eye(d)
            errs.append(mp.mnorm(D ** d, 1))
            B = sum(((-q * D / (q - 1)) ** k for k in range(1, d)), mp.eye(d)) / (q - 1)
            errs.append(mp.mnorm((Mm - mp.eye(d)) * B - mp.eye(d), 1))
            errs.append(mp.mnorm(B * (Mm - mp.eye(d)) - mp.eye(d), 1))
    err = max(errs)
    rep("C17", err < 1e-35,
        "GJN6.1-6.2/GJNR5.1-5.2/HBWR3.3: M=q exp(2pi i N), D=exp(2pi i N)-I, D^d=0, (M-I)^-1 = (q-1)^-1 sum_(k<d)(-qD/(q-1))^k "
        "two-sided (lam=0.2+4i, rho1, 0.9-2.5i, 0.35+0.6i; d=1,3,5; |q| up to e^(88.8))",
        f"max abs {ns(err)}")


def c18():
    errs = []
    K = lambda s: s * (s - 1) / 8 * mp.power(mp.pi, -s / 2) * mp.gamma(s / 2)
    chi = lambda s: mp.power(2, s) * mp.power(mp.pi, s - 1) * mp.sin(mp.pi * s / 2) * mp.gamma(1 - s)
    for s in (mp.mpc('0.3', '2.1'), mp.mpc('-1.7', '0.4'), mp.mpc('2.5', '-3.3'), mp.mpc('0.5', '14')):
        errs += [rel(K(1 - s) / K(s), chi(s)),
                 rel(mp.power(mp.pi, s - mp.mpf(1) / 2) * mp.gamma((1 - s) / 2) / mp.gamma(s / 2), chi(s)),
                 rel(mp.zeta(s), chi(s) * mp.zeta(1 - s)),
                 rel(mp.gamma(s / 2) * mp.gamma(1 - s / 2), mp.pi / mp.sin(mp.pi * s / 2)),
                 rel(mp.gamma((1 - s) / 2) * mp.gamma(1 - s / 2), mp.power(2, s) * mp.sqrt(mp.pi) * mp.gamma(1 - s))]
    t = mp.mpf('0.1')
    s0 = 1 - RHO[0]
    Dt = lambda s: 8 * mp.exp(t * s * s) / s
    Dc = mp.taylor(Dt, s0, 3)
    Fc = mp.taylor(F0, s0, 3)
    scale = abs(Dc[0] * Fc[1])
    leib = []
    for j in range(4):
        direct = mp.diff(lambda s: Dt(s) * F0(s), s0, j)
        L = mp.fsum(mp.binomial(j, l) * Dc[j - l] * mp.factorial(j - l) * Fc[l] * mp.factorial(l) for l in range(1, j + 1))
        leib.append(abs(direct - L) / scale)
    ok = max(errs) < 1e-35 and max(leib) < 1e-25 and scale > 0
    rep("C18", ok,
        "GJNR1.1-1.4/GJN0.7: K(1-s)/K(s) = pi^(s-1/2)Gamma((1-s)/2)/Gamma(s/2) = chi(s) = 2^s pi^(s-1) sin(pi s/2)Gamma(1-s), zeta=chi zeta(1-s), "
        "reflection/duplication; GJN0.8/GJNR10.1 at s0=1-rho1 (m=1): d^j/ds^j[D_t F0](s0) = sum_(l=m..j) C(j,l)D_t^(j-l)F0^(l) (j<=3), "
        "j=0 value 0, j=1 value nonzero",
        f"chi max rel {ns(max(errs))}; Leibniz max err relative to |D_t(s0)F0'(s0)| {ns(max(leib))}; |D_t F0'|(s0)={ns(scale)}")


def c19():
    errs = []
    for n in (2, 3):
        Gn = (lambda nn: (lambda s: F0(s) * F0(s / nn)))(n)
        errs.append(rel(Gn(mp.mpf('1e-30')), mp.mpf(1) / 64))
        lam = n * RHO[0]
        dG = mp.diff(Gn, lam)
        pred = F0(lam) * mp.diff(F0, RHO[0]) / n    # BRC4.3 with m=1: leading coefficient carries n^-m
        errs.append(rel(dG, pred))
        errs.append(abs(Gn(lam)) / abs(dG))            # order exactly one: G(lam)=0, G'(lam)!=0
        J = lambda s: Gn(s) / (dG * (s - lam))
        errs.append(abs(J(lam + mp.mpf('1e-25')) - 1))
        for z in (RHO[0], RHO[1], n * RHO[1], RHO[2]):
            errs.append(abs(J(z)))
    # BRC4.2 additivity of orders at a collision (exact polynomial model): P has zeros rhoA (m=2), 2rhoA (m=3)
    s = sp.symbols('s')
    zA = sp.Rational(1, 10) + 3 * sp.I
    P = (s - zA) ** 2 * (s - 2 * zA) ** 3
    Gp = sp.expand(P * P.subs(s, s / 2))
    order = next(k for k in range(10) if sp.simplify(sp.diff(Gp, s, k).subs(s, 2 * zA)) != 0)
    err = max(errs)
    rep("C19", err < 1e-20 and order == 5,
        "BRC4.1-4.4 at actual zeros (n=2,3): G_n=F0(s)F0(s/n), G_n(0)=1/64, simple zero at n rho1 with G_n'(n rho1) = F0(n rho1)F0'(rho1)/n, "
        "isolator J=G_n/(G_n'(lam)(s-lam)) -> 1 at lam, J=0 at rho1, rho2, n rho2, rho3; order additivity at a collision (model: 3+2=5)",
        f"max {ns(err)}; collision order {order}")


def c20():
    r = mp.mpf('2.5')
    t, tp = mp.mpf('0.3'), mp.mpf('0.05')
    base = {(Fr(1, 10), Fr(3)): 2, (Fr(1, 5), Fr(6)): 1, (Fr(3, 25), Fr(5)): 1, (Fr(9, 25), Fr(15)): 2,
            (Fr(1, 3), Fr(8)): 1, (Fr(2, 3), Fr(16)): 1}
    ZO = {}
    for k, m in base.items():
        ZO[k] = m
        ZO[(1 - k[0], k[1])] = m
    ZL = {(Fr(1, 2), Fr(10)): 1, (Fr(1, 2), Fr(12)): 2, (Fr(1, 2), Fr(15)): 1}
    sharp = lambda k: (1 - k[0], k[1])
    dr = lambda lam: mp.exp(-1j * lam.imag * mp.log(r)) * (r ** lam.real - r ** (1 - lam.real))
    kap = lambda lam, tt: -dr(lam) * mp.exp(tt * (1 - lam) ** 2) * mp.gamma(1 + lam) / (1 - lam)
    errs = []
    # K_r antilinear isometric involution; d_r identities used in HSR8.8/BRC11.8
    random.seed(20)
    y = {k: mp.mpc(random.gauss(0, 1), random.gauss(0, 1)) for k in ZO}
    Kr = lambda yy: {k: -mp.exp(2j * lamval(k).imag * mp.log(r)) * mp.conj(yy[sharp(k)]) for k in ZO}
    nrm = lambda yy: mp.sqrt(mp.fsum(ZO[k] * abs(yy[k]) ** 2 for k in ZO))
    Ky = Kr(y)
    errs.append(rel(nrm(Ky), nrm(y)))
    KKy = Kr(Ky)
    errs.append(max(abs(KKy[k] - y[k]) for k in ZO) / nrm(y))
    iy = {k: 1j * v for k, v in y.items()}
    Kiy = Kr(iy)
    errs.append(max(abs(Kiy[k] + 1j * Ky[k]) for k in ZO) / nrm(y))
    for k in ZO:
        lam = lamval(k)
        errs.append(rel(dr(lamval(sharp(k))), -dr(lam)))
        errs.append(rel(mp.exp(2j * lam.imag * mp.log(r)) * dr(lam), mp.conj(dr(lam))))
    # return supports (BRC5.1, BRC11.4-11.6) and BRC6 finiteness
    disjoint = True
    intervals = True
    for n in range(2, 7):
        An = {k for k in ZO if mul(n, k) in ZO}
        Ansh = {sharp(k) for k in An}
        disjoint &= not (An & Ansh)
        intervals &= all(k[0] < Fr(1, n) for k in An) and all(k[0] > 1 - Fr(1, n) for k in Ansh)
    nonempty = {mul(2, (Fr(1, 10), Fr(3))) in ZO, mul(3, (Fr(3, 25), Fr(5))) in ZO} == {True}
    online_target = abs(dr(lamval((Fr(1, 2), Fr(15))))) == 0 and (Fr(1, 10), Fr(3)) not in {k for k in ZO if mul(5, k) in ZO}
    fin = True
    for n in (2, 3):
        for k in ZO:
            ks = [kk for kk in range(1, 12) if mul(n ** kk, k) in ZO]
            fin &= all(n ** kk * k[0] < 1 for kk in ks)
    # BRC5.3 pointwise: P_2 S_(r,t)y = S_(r,t')(Ly) for y supported on A_2
    A2 = [k for k in ZO if mul(2, k) in ZO]
    yA = {k: y[k] for k in A2}
    S = lambda coeffs, tt: (lambda l: mp.expm1(mp.exp(l)) * mp.fsum(ZO[k] * kap(lamval(k), tt) * cf * mp.exp((-1 - lamval(k)) * l)
                                                                  for k, cf in coeffs.items()))
    Ly = {mul(2, k): ZO[k] * kap(lamval(k), t) * yA[k] / (ZO[mul(2, k)] * kap(lamval(mul(2, k)), tp)) for k in A2}
    for l in LP:
        errs.append(rel(P_op(2, S(yA, t))(l), S(Ly, tp)(l)))
    # BRC7/BRC10 at a collision lam = 2*(1/10+3i) = 1*(1/5+6i): the division factors agree
    rA = lamval((Fr(1, 10), Fr(3)))
    errs.append(rel(mp.exp(-TWOPI_I * 2 * rA) - 1, mp.exp(-TWOPI_I * lamval((Fr(1, 5), Fr(6)))) - 1))
    err = max(errs)
    ok = err < 1e-35 and disjoint and intervals and nonempty and online_target and fin
    rep("C20", ok,
        "BRC5/BRC6/BRC11 on a synthetic #-symmetric divisor WITH off-line zeros and nonempty A_2, A_3: K_r antilinear isometric involution, "
        "d_r(rho#)=-d_r(rho), e^(2i gamma log r)d_r=conj d_r; supp E_n in Re<1/n, supp K_rE_n in Re>1-1/n, disjoint (n=2..6); on-line target "
        "(5(0.1+3i)=0.5+15i) has d_r=0 so is excluded; n^k rho in Z only while n^k Re rho<1; BRC5.3 pointwise; BRC10 factor equal at collisions",
        f"max rel {ns(err)}")


def c21():
    # at Im(l)<0 the singular term is ~e^(-N*gamma*|Im l|) ~ e^(-170) against an O(1) holomorphic remainder, so the
    # cancellation of the remainder under M-I must be resolved: work at 160 digits.
    errs = []
    with mp.workdps(160):
        rho = mp.zetazero(1)
        tpi = mp.mpc(0, 2) * mp.pi
        bco = mp.mpc('0.8', '-0.3')
        R = lambda u: mp.cos(u) + u ** 2 + 3
        for Nn in (2, 4):
            q = mp.exp(-tpi * Nn * rho)
            fB = lambda l, q=q: mp.expm1(mp.exp(l)) * bco / (q - 1) * mp.exp((-1 - rho) * l) + R(mp.exp(l))
            f = lambda l: mp.expm1(mp.exp(l)) * bco * mp.exp((-1 - rho) * l) + R(mp.exp(l))
            PfB, Pf = P_op(Nn, fB), P_op(Nn, f)
            for l in [mp.mpc(x, y) for x in ('-1.5', '-0.5') for y in ('-3', '0.5', '5')]:
                u = mp.exp(l)
                lhs = PfB(l + tpi) - PfB(l)
                rhs = Pf(l) - h(u) / h(u ** Nn) * R(u ** Nn)
                errs.append(rel(lhs, rhs))
                errs.append(rel(lhs, mp.expm1(u) * bco * mp.exp((-1 - Nn * rho) * l)))
    err = max(errs)
    rep("C21", err < 1e-30,
        "BRC10.5 on full germs at actual rho1 (N=2,4): (M-I)P_N[(e^u-1)(b/(e^(-2pi i N rho)-1))u^(-1-rho) + R] = P_N[(e^u-1)b u^(-1-rho) + R] "
        "- A_N(u)R(u^N), R holomorphic (remainder retained, cancels only under M-I)",
        f"max rel {ns(err)}")


for fn in (c01, c02, c03, c04, c05, c06, c07, c08, c09, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20, c21):
    fn()
print(f"SUMMARY: {sum(RES)}/{len(RES)} PASS")
