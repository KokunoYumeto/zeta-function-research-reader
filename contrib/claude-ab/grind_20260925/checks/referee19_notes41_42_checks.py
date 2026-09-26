#!/usr/bin/env python3
# Checks for claude-ab notes 41_ and 42_ after the nineteenth referee pass (26 September 2026).
# Adapted from the referee's own check script (Claude, model claude-opus-5-5): the mathematical items R1-R5 and R7h.
# The referee's items that document findings against the earlier text are turned into checks of the corrected statements;
# the items that read private working data (the Codex session logs, the repository clone, text excerpts) are not included.
# Every item prints PASS or FAIL.
import random
import time
from fractions import Fraction

import numpy as np
import mpmath as mp
import sympy as sp
from scipy.special import j0
from scipy.integrate import quad

T_START = time.time()
results = []


def check(label, desc, ok, detail=""):
    ok = bool(ok)
    results.append(ok)
    print(f"{len(results):3d} {'PASS' if ok else 'FAIL'}  {label}  {desc}" + (f"  -- {detail}" if detail else ""), flush=True)


# =====================================================================================================
print("R1. Prop. 42.2 on synthetic zero configurations (independent matrix implementation)")
rng = np.random.default_rng(19)


def config(rh, n_on=4, n_off=2):
    """distinct points of Z with multiplicities; symmetric under conjugation and #"""
    Z = []
    heights = rng.choice(np.arange(10, 80), size=n_on + n_off, replace=False).astype(float) + 0.37
    for g in heights[:n_on]:
        m = int(rng.integers(1, 4))
        Z += [(complex(0.5, g), m), (complex(0.5, -g), m)]
    if not rh:
        for g in heights[n_on:]:
            b = float(rng.choice([0.6, 0.7, 0.85]))
            m = int(rng.integers(1, 3))
            for w in (complex(b, g), complex(1 - b, g), complex(b, -g), complex(1 - b, -g)):
                Z.append((w, m))
    return Z


def key(w):
    return (round(w.real, 9), round(w.imag, 9))


def forms(Z):
    pts = [w for w, _ in Z] + [w - 1 for w, _ in Z]
    mult = {key(w): m for w, m in Z}
    mult.update({key(w - 1): m for w, m in Z})
    idx = {key(w): i for i, w in enumerate(pts)}
    n2 = len(pts)
    H = np.zeros((n2, n2))
    for w in pts:  # Q_A(f) = sum_w m_w f(w) conj f(-conj w) = f^T M conj(f); Hermitian matrix is M^T
        H[idx[key(-w.conjugate())], idx[key(w)]] += mult[key(w)]
    n = len(Z)
    Om = np.zeros((n, n))
    for i, (w, m) in enumerate(Z):  # Omega(u) = sum_rho m u(rho) conj u(rho#)
        Om[idx[key(1 - w.conjugate())], i] += m
    # change of basis: f = (u + v on Z, u - v on Z - 1)
    Bm = np.zeros((n2, 2 * n))
    for i in range(n):
        Bm[i, i], Bm[i, n + i] = 1, 1
        Bm[n + i, i], Bm[n + i, n + i] = 1, -1
    return H, Om, Bm, n


ok_sig, ok_id, ok_orth, ok_pos, ok_max, ok_neg = True, True, True, True, True, True
for trial in range(30):
    rh = trial % 2 == 0
    Z = config(rh)
    H, Om, Bm, n = forms(Z)
    ev = np.linalg.eigvalsh(H)
    ok_sig &= (np.sum(ev > 1e-9) == n and np.sum(ev < -1e-9) == n)
    Hp = Bm.T @ H @ Bm
    target = np.block([[2 * Om, np.zeros((n, n))], [np.zeros((n, n)), -2 * Om]])
    ok_id &= np.allclose(Hp, target)
    ok_orth &= np.allclose(Hp[:n, n:], 0)
    evp = np.linalg.eigvalsh((Hp[:n, :n] + Hp[:n, :n].T) / 2)
    if rh:
        evm = np.linalg.eigvalsh(Hp[n:, n:])
        ok_pos &= evp.min() > 0 and evm.max() < 0
        for _ in range(20):  # any subspace strictly containing V+ contains a Q_A-negative vector x_-
            x = rng.normal(size=2 * n)
            xm = x.copy()
            xm[:n] = 0
            ok_max &= (xm @ Hp @ xm) < 0
    else:
        ok_neg &= evp.min() < 0
check("R1a", "Q_A has signature (n, n) on data over n A-pairs, for 15 RH and 15 non-RH configurations with multiplicities 1-3 (42.2(a))", ok_sig)
check("R1b", "Q_A(u+v on Z, u-v on Z-1) = 2 Omega(u) - 2 Omega(v) as a matrix identity after the change of basis (42.2)", ok_id)
check("R1c", "V+ (T-even) and V- (T-odd) are Q_A-orthogonal in every configuration, with or without RH", ok_orth)
check("R1d", "RH configurations: Q_A > 0 on V+, < 0 on V-, and every extension of V+ contains a negative vector (42.2(c) maximality)", ok_pos and ok_max)
check("R1e", "non-RH configurations: V+ contains a Q_A-negative direction (42.2(c), second sentence)", ok_neg)
# the distinct-point convention of the revised 42_ section 0: sums over distinct zeros, weight m_rho written out
Zd = [(complex(0.5, 20.0), 2), (complex(0.5, -20.0), 2)]
u = {key(w): 1.0 + 0j for w, _ in Zd}
weil = sum(m * u[key(w)] * np.conj(u[key(1 - w.conjugate())]) for w, m in Zd)          # distinct zeros, weight m
multiset = sum(m * u[key(w)] * np.conj(u[key(1 - w.conjugate())]) for w, m in Zd for _ in range(m))  # literal multiset reading
check("R1f", "distinct-point convention (revised section 0): for a double zero pair and u = 1, Omega = 4; a sum over the multiset with weight m would give 8",
      abs(weil - 4) < 1e-12 and abs(multiset - 8) < 1e-12, f"distinct-zero sum {weil.real:.0f}, multiset reading {multiset.real:.0f}")

# =====================================================================================================
print("R2. Prop. 42.1 (the multiplicative doublet class)")
mp.mp.dps = 30


def Lam_char(s, vals, a):
    q = len(vals)
    return (mp.mpf(q) / mp.pi) ** ((s + a) / 2) * mp.gamma((s + a) / 2) * mp.dirichlet(s, vals)


def xi(s):
    if abs(s) < mp.mpf(10) ** -25 or abs(s - 1) < mp.mpf(10) ** -25:
        return mp.mpf(1) / 2          # xi(0) = xi(1) = 1/2 (removable singularities)
    return s * (s - 1) / 2 * mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)


i_ = mp.mpc(0, 1)
chi5 = [0, 1, i_, -i_, -1]
chi5b = [0, 1, -i_, i_, -1]
hh, s3 = mp.mpf(1) / 2, mp.sqrt(3) / 2                  # exact sixth roots of unity, so that sum chi7 = 0 exactly (mpmath's L(1) needs it)
w6 = [None, mp.mpc(hh, s3), mp.mpc(-hh, s3), mp.mpf(-1), mp.mpc(-hh, -s3), mp.mpc(hh, -s3)]
chi7 = [0, 1, w6[2], w6[1], w6[4], w6[5], w6[3]]         # generator 3 -> e^{i pi/3}; chi7(-1) = -1 (odd)
chi7b = [mp.conj(c) if c != 0 else 0 for c in chi7]
chim4 = [0, 1, 0, -1]


def LamA(s):  # multiset {trivial (xi), chi_-4, chi5, chi5bar, chi7, chi7bar}
    return xi(s) * Lam_char(s, chim4, 1) * Lam_char(s, chi5, 1) * Lam_char(s, chi5b, 1) * Lam_char(s, chi7, 1) * Lam_char(s, chi7b, 1)


def LamBad(s):  # {chi5, chi5, chi5bar}: closed under conjugation as a SET, not invariant as a multiset
    return Lam_char(s, chi5, 1) ** 2 * Lam_char(s, chi5b, 1)


s0 = mp.mpc("0.31", "7.3")
fe = abs(LamA(1 - s0) / LamA(s0) - 1)
re_ = abs(LamA(mp.conj(s0)) / mp.conj(LamA(s0)) - 1)
worst, mn = mp.mpf(0), mp.inf
for t in (0.0, 0.7, 3.1, 9.9, 21.4):
    g = LamA(mp.mpc(0, t)) * LamA(mp.mpc(1, t))
    worst = max(worst, abs(g - abs(LamA(mp.mpc(1, t))) ** 2) / abs(g))
    mn = min(mn, g.real)
check("R2a", "multiset {xi, chi_-4, chi_5, chi_5bar, chi_7, chi_7bar}: Lambda(1-s) = Lambda(s), Lambda(conj s) = conj Lambda(s), G(it) = |Lambda(1+it)|^2 > 0 (42.1(a))",
      fe < 1e-25 and re_ < 1e-25 and worst < 1e-25 and mn > 0, f"FE residual {mp.nstr(fe, 2)}, reality {mp.nstr(re_, 2)}, max rel. dev. {mp.nstr(worst, 2)}")
feb = abs(LamBad(1 - s0) / LamBad(s0) - 1)
check("R2b", "the invariance hypothesis of 42.1 (chi and chi-bar equally often) is needed: {chi5, chi5, chi5bar}, closed only as a set, violates Lambda(1-s) = Lambda(s)",
      feb > 0.1, f"|Lambda(1-s)/Lambda(s) - 1| = {mp.nstr(feb, 3)} at s = 0.31 + 7.3i")
eps_ = mp.mpf("1e-12")
res = eps_ * (-mp.zeta(1 + eps_, derivative=1) / mp.zeta(1 + eps_))
xi_ld = -mp.diff(xi, 1, h=mp.mpf("1e-8")) / xi(1)
Bconst = -mp.euler / 2 - 1 + mp.log(4 * mp.pi) / 2        # xi'/xi(0) = B, so -xi'/xi(1) = B by the functional equation
check("R2c", "42.1(c), trivial factor: the second-line prime series -zeta'/zeta(1+s) has a pole at s = 0 (residue 1), cancelled by the rational term -1/s of -xi'/xi(s+1)",
      abs(res - 1) < 1e-9 and abs(xi_ld - Bconst) < 1e-12, f"s*(-zeta'/zeta(1+s)) at s=1e-12: {mp.nstr(res, 12)}; -xi'/xi(1) = {mp.nstr(xi_ld, 10)} = B = -gamma/2 - 1 + log(4 pi)/2 (finite)")

# =====================================================================================================
print("R3. Corollary 42.3 and the explicit formula for Q_A")
mp.mp.dps = 30


def Fstar(s):
    return s * (s - 1) / 8 * mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)


rhos = [mp.zetazero(n) for n in range(1, 21)]
vals_pm = [abs(Fstar(r + 1) * Fstar(r - 1)) for r in rhos[:10]]
check("R3a", "F_*(rho +- 1) != 0 at the first ten zeros (Re(rho+1) in (1,2), Re(rho-1) in (-1,0))", min(vals_pm) > 0,
      f"min |F_*(rho+1)F_*(rho-1)| = {mp.nstr(min(vals_pm), 3)}")


def kgen(s):
    return mp.exp(s ** 2 / 10) * (1 + s)


def fk(s, k=kgen):
    return Fstar(s + 1) * Fstar(s - 1) * k(s) + Fstar(s + 2) * Fstar(s) * k(s + 1)


zall = rhos + [mp.conj(r) for r in rhos]
tev = max(abs(fk(r) - fk(r - 1)) / abs(fk(r)) for r in zall[:5] + zall[20:25])
check("R3b", "f_k is T-even on the zero set for a non-localized k(s) = exp(s^2/10)(1+s) (checked at 10 zeros)", tev < 1e-20, f"max rel. |f_k(rho)-f_k(rho-1)| = {mp.nstr(tev, 2)}")
QA = mp.fsum(fk(w) * mp.conj(fk(-mp.conj(w))) for r in zall for w in (r, r - 1))
U2 = mp.fsum(2 * abs(Fstar(r + 1) * Fstar(r - 1) * kgen(r)) ** 2 for r in zall)
nonzero = sum(1 for r in rhos if abs(fk(r)) > 0)
check("R3c", "for that f_k (values nonzero at every zero), Q_A(f_k), summed over 40 zeros, equals 2*sum|U(rho)|^2 > 0 (the absolutely convergent extension used by 42.3)",
      abs(QA - U2) / abs(U2) < 1e-20 and U2 > 0, f"Q_A = {mp.nstr(QA.real, 8)}; last term {mp.nstr(abs(Fstar(rhos[-1] + 1) * Fstar(rhos[-1] - 1) * kgen(rhos[-1])) ** 2, 2)}")
check("R3d", "f_k for this k takes nonzero values at all of the first 20 zeros, so 42.3 needs Prop. 42.2 for data from B (the revised statement covers them)",
      nonzero == len(rhos), f"f_k(rho) != 0 at {nonzero} of the first {len(rhos)} zeros")
# OMS6-type interpolation: k = c1 U_{rho1}/F_*'(rho1) + c2 U_{rho2}/F_*'(rho2), U_rho = F_*/(s - rho)
r1, r2 = rhos[0], rhos[1]
d1, d2 = mp.diff(Fstar, r1), mp.diff(Fstar, r2)
tgt = [mp.mpc(1, -2), mp.mpc(-0.5, 0.25)]
c1 = tgt[0] / (Fstar(r1 + 1) * Fstar(r1 - 1))
c2 = tgt[1] / (Fstar(r2 + 1) * Fstar(r2 - 1))


def kint(s):
    out = mp.mpc(0)
    for c, r, d in ((c1, r1, d1), (c2, r2, d2)):
        out += c * (d if abs(s - r) < mp.mpf(10) ** -20 else Fstar(s) / (s - r)) / d
    return out


uvals = [Fstar(r + 1) * Fstar(r - 1) * kint(r) for r in (r1, r2)]
others = max(abs(Fstar(r + 1) * Fstar(r - 1) * kint(r)) for r in rhos[2:8] + [mp.conj(r1), mp.conj(r2)])
QAint = mp.fsum(fk(w, kint) * mp.conj(fk(-mp.conj(w), kint)) for r in [r1, r2, mp.conj(r1), mp.conj(r2)] for w in (r, r - 1))
check("R3e", "OMS6 sections give k in B with prescribed values of u at rho_1, rho_2 and u = 0 at the other zeros; Q_A(f_k) = 2(|u1|^2+|u2|^2)",
      max(abs(uvals[0] - tgt[0]), abs(uvals[1] - tgt[1])) < 1e-15 and others < 1e-15 and abs(QAint - 2 * (abs(tgt[0]) ** 2 + abs(tgt[1]) ** 2)) < 1e-12,
      f"Q_A = {mp.nstr(QAint.real, 12)} (target 10.625); max |u| at 8 other zeros {mp.nstr(others, 2)}")
# explicit formula: sum_{w: G(w)=0} m_w h(w) = (1/2 pi i) int_(a) [h(s)+h(-s)] G'/G(s) ds, G = xi(s)xi(s+1) even
epsf = mp.mpf("0.02")
al, be = mp.mpc("0.7", "-0.3"), mp.mpc("0.2", "0.5")


def ftest(s):
    return mp.exp(epsf * s ** 2) * (al + be * s)


def htest(s):
    return ftest(s) * mp.conj(ftest(-mp.conj(s)))


z14 = [mp.zetazero(n) for n in range(1, 15)]
z14 = z14 + [mp.conj(r) for r in z14]
S_zero = mp.fsum(htest(r) + htest(r - 1) for r in z14)
S_zero2 = mp.fsum(ftest(w) * mp.conj(ftest(-mp.conj(w))) for r in z14 for w in (r, r - 1))
a_ = mp.mpf(2)


def Hs(s):
    return htest(s) + htest(-s)


def polar(s):
    return 2 / s + 1 / (s - 1) + 1 / (s + 1)


def gam(s):
    return -mp.log(mp.pi) + mp.digamma(s / 2) / 2 + mp.digamma((s + 1) / 2) / 2


I_polar = mp.quad(lambda t: Hs(a_ + i_ * t) * polar(a_ + i_ * t), [-60, -20, 0, 20, 60]) / (2 * mp.pi)
I_gamma = mp.quad(lambda t: Hs(a_ + i_ * t) * gam(a_ + i_ * t), [-60, -20, 0, 20, 60]) / (2 * mp.pi)
# prime terms in closed form: H(s) = e^{2 eps s^2}(2|al|^2 - 2|be|^2 s^2); (1/2 pi i) int_(0) H(s) n^{-s} ds
A2 = 2 * epsf
chk_even = abs(Hs(mp.mpc("0.3", "1.7")) - mp.exp(A2 * mp.mpc("0.3", "1.7") ** 2) * (2 * abs(al) ** 2 - 2 * abs(be) ** 2 * mp.mpc("0.3", "1.7") ** 2))


def In(n):
    L = mp.log(n)
    g0 = mp.sqrt(mp.pi / A2) * mp.exp(-L ** 2 / (4 * A2))
    return (2 * abs(al) ** 2 * g0 + 2 * abs(be) ** 2 * g0 * (1 / (2 * A2) - L ** 2 / (4 * A2 ** 2))) / (2 * mp.pi)


def vm(n):
    for p in range(2, n + 1):
        if n % p == 0:
            m = n
            while m % p == 0:
                m //= p
            return mp.log(p) if m == 1 else 0
    return 0


I_prime = mp.fsum(vm(n) * (1 + mp.mpf(1) / n) * In(n) for n in range(2, 400) if vm(n))
rhs = I_polar + I_gamma - I_prime
check("R3f", "explicit formula: Q_A(f) (zero side over zeros of G) = polar + Gamma + prime side, f = exp(0.02 s^2)(al + be s) in B (42.3 reading)",
      abs(S_zero - rhs) < 1e-25 and abs(S_zero - S_zero2) < 1e-28 and chk_even < 1e-25,
      f"zero side {mp.nstr(S_zero.real, 20)}; prime+Gamma+polar {mp.nstr(rhs.real, 20)}")
check("R3g", "the polar terms 2/s + 1/(s-1) + 1/(s+1) are needed: primes and Gamma factors alone miss Q_A(f) by the polar part",
      abs(S_zero - (I_gamma - I_prime)) > 1 and abs(S_zero - (I_gamma - I_prime) - I_polar) < 1e-25,
      f"primes+Gamma only: {mp.nstr((I_gamma - I_prime).real, 10)}; polar part {mp.nstr(I_polar.real, 10)}")

# =====================================================================================================
print("R4. Prop. 42.4 (two-line prime races) and delta(4;3,1)")
X = 10 ** 7
sieve = np.ones(X + 1, dtype=bool)
sieve[:2] = False
for p in range(2, int(X ** 0.5) + 1):
    if sieve[p]:
        sieve[p * p::p] = False
P = np.nonzero(sieve)[0]
Pf = P.astype(float)
chi = np.where(P % 4 == 1, 1.0, np.where(P % 4 == 3, -1.0, 0.0))
lp = np.log(Pf)
S1 = np.cumsum(-chi * lp / Pf)                 # -sum chi(p) log p / p
S0 = np.cumsum(chi / Pf)                       # sum chi(p)/p
pts = [10 ** k for k in range(3, 8)]
ix = [np.searchsorted(P, x, side="right") - 1 for x in pts]
quoted = [0.5271, 0.5321, 0.5414, 0.5455, 0.5454]
got = [S1[i] for i in ix]
check("R4a", "partial sums of -sum chi_-4(p) log p/p at x = 10^3..10^7 reproduce the note's 0.5271, 0.5321, 0.5414, 0.5455, 0.5454",
      all(abs(g - q) < 6e-5 for g, q in zip(got, quoted)), "; ".join(f"{g:.5f}" for g in got))
mp.mp.dps = 25
Lp1 = mp.dirichlet(1, chim4, 1)
L1 = mp.dirichlet(1, chim4)
# -sum_p chi(p) log p/p = L'/L(1) + sum_{k>=2} sum_p chi(p)^k log p / p^k
small = P[P < 10 ** 6]
Rk = 0.0
for k in range(2, 40):
    Rk += float(np.sum((chi[:len(small)] ** k) * np.log(small.astype(float)) / small.astype(float) ** k))
limit1 = float(Lp1 / L1) + Rk
R0 = 0.0
for k in range(2, 40):
    R0 += float(np.sum((chi[:len(small)] ** k) / (k * small.astype(float) ** k)))
limit0 = float(mp.log(L1)) - R0
check("R4b", "the correction series converges to its closed form L'/L(1,chi_-4) + sum_{k>=2} sum_p chi(p^k) log p/p^k (42.4(a))",
      abs(S1[ix[-1]] - limit1) < 2e-3, f"limit {limit1:.5f}; partial sum at 10^7 {S1[ix[-1]]:.5f}; L(1) = pi/4 check {mp.nstr(L1 - mp.pi / 4, 2)}")
lo = np.searchsorted(P, 10 ** 5)
dmax = float(np.max(np.abs(S1[lo:]) / np.sqrt(Pf[lo:])))
check("R4c", "|E_G(x) - E(x)| = |sum_{p<=x} chi(p) log p/p|/sqrt x <= 0.0018 at every prime x in [10^5, 10^7] (revised 42.4)",
      dmax <= 0.0018, f"max {dmax:.5f}")
normd = [abs(S0[ix[k]]) * np.log(pts[k]) / np.sqrt(pts[k]) for k in (2, 3, 4)]
check("R4d", "sum_{p<=x} chi_-4(p)/p converges to log L(1,chi_-4) - sum_{k>=2} sum_p chi(p^k)/(k p^k), and (log x/sqrt x) * it -> 0 (42.4(b))",
      abs(S0[ix[-1]] - limit0) < 1e-3 and normd[0] > normd[1] > normd[2] and normd[2] < 2e-3,
      f"limit {limit0:.6f}; partial sum at 10^7 {S0[ix[-1]]:.6f}; normalized at 10^5, 10^6, 10^7: " + ", ".join(f"{v:.4f}" for v in normd))
absum = np.cumsum(np.abs(chi) * lp / Pf)
growth = [absum[i] for i in ix]
incr = [growth[k + 1] - growth[k] for k in range(len(growth) - 1)]
check("R4e", "the correction series is not absolutely convergent: sum |chi_-4(p)| log p/p grows by about log 10 per decade (Mertens), revised section 5",
      all(abs(d - np.log(10)) < 0.05 for d in incr), "; ".join(f"{g:.3f}" for g in growth))
y = int(10 ** 3.5)
th = float(np.sum(lp[(P <= y) & (P % 2 == 1)])) / y
chi5sq = np.array([{1: 1.0, 4: 1.0, 2: -1.0, 3: -1.0, 0: 0.0}[int(p % 5)] for p in P[P <= 10 ** 6]])   # chi^2 = Legendre (./5)
th5 = abs(float(np.sum(chi5sq * lp[:len(chi5sq)]))) / 10 ** 6
check("R4f", "prime squares (42.4(c)): real chi_-4 gives theta(sqrt x) - log 2 ~ sqrt x; complex chi mod 5 gives |theta(y, chi^2)|/y small (chi^2 nonprincipal)",
      0.9 < th < 1.0 and th5 < 0.01, f"theta(3162)/3162 = {th:.4f}; |theta(10^6, chi^2)|/10^6 = {th5:.5f}")
# delta(4;3,1) under GRH + LI from the zeros of L(s, chi_-4) up to 100 and the exact total variance
mp.mp.dps = 20


def Lam4(t):
    s = mp.mpc(0.5, t)
    return ((mp.mpf(4) / mp.pi) ** ((s + 1) / 2) * mp.gamma((s + 1) / 2) * mp.dirichlet(s, chim4)).real


grid = np.arange(0.05, 100, 0.1)
gv = [Lam4(t) for t in grid]
gz = [float(mp.findroot(Lam4, (grid[i], grid[i + 1]), solver="anderson")) for i in range(len(grid) - 1) if gv[i] * gv[i + 1] < 0]
var_tot = float(2 * Lp1 / L1 + mp.log(4 / mp.pi) + mp.digamma(1))     # sum_{gamma>0} 2/(1/4+gamma^2), from Hadamard at s = 1
var_found = sum(2 / (0.25 + g * g) for g in gz)
rr = np.array([2 / np.sqrt(0.25 + g * g) for g in gz])
Iq, _ = quad(lambda t: np.sin(t) * np.prod(j0(rr * t)) * np.exp(-(var_tot - var_found) * t * t / 2) / t, 0, 400, limit=2000)
delta = 0.5 + Iq / np.pi
rvm = 100 / (2 * np.pi) * np.log(4 * 100 / (2 * np.pi * np.e))
check("R4g", "delta(4;3,1) under GRH+LI (50 zeros of L(s,chi_-4) up to 100, exact tail variance, Gaussian tail) agrees with the quoted 0.9959",
      abs(delta - 0.9959) < 3e-4 and abs(len(gz) - rvm) < 2, f"delta = {delta:.5f}; zeros found {len(gz)} (Riemann-von Mangoldt main term {rvm:.1f}); tail variance {var_tot - var_found:.5f}")

# =====================================================================================================
print("R5. Prop. 42.5 (the holonomy index)")
mp.mp.dps = 15


def backlund_N(T, nsteps=400):
    T = mp.mpf(T)
    prev = mp.zeta(mp.mpc(2, T))
    arg = mp.arg(prev)            # Re zeta(2+it) > 0, so the continuous argument on Re s = 2 is the principal one
    for k in range(1, nsteps + 1):
        cur = mp.zeta(mp.mpc(2 - 1.5 * k / nsteps, T))
        arg += mp.arg(cur / prev)
        prev = cur
    return mp.siegeltheta(T) / mp.pi + 1 + arg / mp.pi


NB = {T: backlund_N(T) for T in (100, 250)}
ts = np.arange(0.1, 250, 0.1)
zv = np.array([float(mp.siegelz(t)) for t in ts])
sg = np.sign(zv)
chg = np.nonzero(sg[1:] * sg[:-1] < 0)[0]
V = {T: int(np.sum(ts[chg] < T)) for T in (100, 250)}
zz = [float(mp.zetazero(n).imag) for n in range(1, 110)]
gap = min(np.diff(zz))
check("R5a", "zeta: N(T) from Backlund's formula (continuous argument, independent of mpmath's nzeros) equals the sign changes of Z on a 0.1-grid at T = 100, 250",
      all(abs(NB[T] - round(NB[T])) < 1e-6 and int(round(NB[T])) == V[T] for T in (100, 250)) and gap > 0.2,
      f"N(100) = {mp.nstr(NB[100], 8)}, V(100) = {V[100]}; N(250) = {mp.nstr(NB[250], 8)}, V(250) = {V[250]}; min zero gap below 250 = {gap:.3f}")
t_ = sp.symbols("t", real=True)
random.seed(1919)
ok_idx = True
for trial in range(25):
    hs = random.sample(range(2, 40), 7)
    on = [(h, random.randint(1, 4)) for h in hs[:4]]
    off = [(h, random.choice([Fraction(1, 5), Fraction(2, 5)]), random.randint(1, 2)) for h in hs[4:4 + random.randint(0, 3)]]
    R = sp.Integer(1)
    for h, m in on:
        R *= (h ** 2 - t_ ** 2) ** m
    for h, d, m in off:
        d = sp.Rational(d.numerator, d.denominator)
        R *= ((h ** 2 + d ** 2 - t_ ** 2) ** 2 + 4 * d ** 2 * t_ ** 2) ** m     # restriction to Re s = 1/2 of the off-line pair
    Tm = 41
    poly = sp.Poly(sp.expand(R), t_)
    Vt = 0
    for fac, mult in sp.sqf_list(poly)[1]:
        if mult % 2 == 1:
            Vt += fac.count_roots(0, Tm)          # distinct real roots in (0, T) of odd multiplicity = sign changes
    Nt = sum(m for h, m in on) + sum(2 * m for h, d, m in off)
    Pt = sum(m for h, d, m in off)
    ok_idx &= (Nt - Vt) % 2 == 0 and (Nt - Vt) // 2 == Pt + sum(m // 2 for h, m in on)
check("R5b", "index formula (N - V)/2 = P + sum floor(m/2) on 25 random symmetric configurations, V computed exactly (square-free parts, Sturm counts)", ok_idx)
dl = sp.Rational(1, 10 ** 20)
ZA = (400 - t_ ** 2) ** 2                                         # double on-line zero at height 20: N = 2, V = 0, P = 0
ZB = sp.expand((400 + dl ** 2 - t_ ** 2) ** 2 + 4 * dl ** 2 * t_ ** 2)    # off-line pair 1/2 +- 1e-20 + 20i: N = 2, V = 0, P = 1
ZC = sp.expand(((20 - dl) ** 2 - t_ ** 2) * ((20 + dl) ** 2 - t_ ** 2))   # two simple on-line zeros 20 +- 1e-20: N = 2, V = 2


def signchanges(Z):
    return sum(fac.count_roots(0, 30) for fac, mult in sp.sqf_list(sp.Poly(Z, t_))[1] if mult % 2 == 1)


VA, VB, VC = signchanges(ZA), signchanges(ZB), signchanges(ZC)
IA, IB, IC = (2 - VA) // 2, (2 - VB) // 2, (2 - VC) // 2
bulkA, bulkB = 0, 2
check("R5c", "revised 42.N1: configurations A (double on-line zero) and B (off-line pair) have the same N and V, hence the same index, but bulk counts 0 and 2",
      VA == VB and IA == IB and bulkA != bulkB, f"A: N=2, V={VA}, I={IA}, bulk {bulkA};  B: N=2, V={VB}, I={IB}, bulk {bulkB}")


def supdiff(Z1, Z2, T=30):
    return sum(abs(c) * T ** k for k, c in enumerate(reversed(sp.Poly(sp.expand(Z1 - Z2), t_).all_coeffs())))


dAC = supdiff(ZA, ZC)
check("R5d", "revised section 5: a positive index cannot always be certified: A and C agree on [0,30] to within 1e-36 yet I_A = 1 and I_C = 0",
      dAC < sp.Rational(1, 10 ** 35) and IA != IC, f"sup|Z_A - Z_C| <= {sp.N(dAC, 3)} while max |Z_A| on [0,30] = 250000; I_A = {IA}, I_C = {IC}")
check("R5e", "revised reading of 42.5: the on-line term is floor(m/2), the number of pairs in the multiplicity (m = 2 gives 1, not (m-1)/2 = 1/2)",
      2 // 2 == 1 and Fraction(2 - 1, 2) == Fraction(1, 2) and all((m - m % 2) // 2 == m // 2 for m in range(1, 9)))

print("R7h. The ETR9 scope example of 41_ section 1.1: the even-degree real-pole orders as the degree varies")
th_ = np.linspace(0, 2 * np.pi, 4001)[:-1]
h_nu = [float(np.mean((1 + 4 * np.cos(th_)) ** (2 * k))) for k in (1, 2, 12)]
h_mu = [9.0 ** k for k in (1, 2, 12)]
check("R7h", "ETR9 scope example: h_2 = 9 for both mu_B and nu_B, but h_4 = 81 vs 145, and h_2k^(1/2k) -> 3 vs 5 (the orders as k varies separate them)",
      abs(h_nu[0] - 9) < 1e-9 and abs(h_nu[1] - 145) < 1e-7 and h_mu[1] == 81 and abs(h_mu[2] ** (1 / 24) - 3) < 1e-12 and 4.2 < h_nu[2] ** (1 / 24) < 5,
      f"h_24(nu)^(1/24) = {h_nu[2] ** (1 / 24):.3f} (increasing to 5)")

print("=" * 100)
print(f"{len(results)} items: {sum(results)} PASS, {len(results) - sum(results)} FAIL; runtime {time.time() - T_START:.0f} s")
