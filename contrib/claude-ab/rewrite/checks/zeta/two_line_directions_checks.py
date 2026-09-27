#!/usr/bin/env python3
# Checks for claude-ab note 42_ (the four continuation directions of 22_ section 5).
# Written by Claude (claude-ab lane), model claude-opus-5-5 (Opus 5.5) at maximum reasoning effort, 25 September 2026.
# C3's first tolerance (2% at y = 3162) was too tight for theta(y)/y = 0.968 there; it now checks the ratio at three sizes.
import random

import mpmath as mp
import numpy as np

mp.mp.dps = 30
results = []


def check(label, desc, ok, detail=""):
    ok = bool(ok)
    results.append(ok)
    print(f"{len(results):3d} {'PASS' if ok else 'FAIL'}  {label}  {desc}" + (f"  -- {detail}" if detail else ""))


print("A. Direction 1: the multiplicative doublet class")
chi = [0, 1, 1j, -1j, -1]            # chi mod 5 with chi(2) = i (so chi(3) = -i, chi(4) = -1, chi(-1) = -1)
chib = [0, 1, -1j, 1j, -1]
q, a = 5, 1


def Lam(s, c):
    return (mp.mpf(q) / mp.pi) ** ((s + a) / 2) * mp.gamma((s + a) / 2) * mp.dirichlet(s, c)


def LamD(s):
    return Lam(s, chi) * Lam(s, chib)


ts = [mp.mpf(x) for x in (0.3, 2.0, 7.5, 14.0, 33.3)]
worst_im, worst_diff, minval = mp.mpf(0), mp.mpf(0), mp.inf
for t in ts:
    g = LamD(mp.mpc(0, t)) * LamD(mp.mpc(1, t))
    worst_im = max(worst_im, abs(g.imag) / abs(g))
    worst_diff = max(worst_diff, abs(g - abs(LamD(mp.mpc(1, t))) ** 2) / abs(g))
    minval = min(minval, g.real)
check("A1", "G_Lambda(it) = Lambda(it)Lambda(1+it) is real and equals |Lambda(1+it)|^2 > 0 for the doublet chi, chi-bar mod 5",
      worst_im < 1e-25 and worst_diff < 1e-25 and minval > 0, f"max rel. imaginary part {mp.nstr(worst_im, 3)}; min {mp.nstr(minval, 4)}")
s0 = mp.mpc(0.3, 4.1)
check("A2", "the doublet satisfies Lambda(s) = Lambda(1 - s) and Lambda(conj s) = conj Lambda(s) (total root number 1)",
      abs(LamD(s0) - LamD(1 - s0)) / abs(LamD(s0)) < 1e-25 and abs(LamD(mp.conj(s0)) - mp.conj(LamD(s0))) / abs(LamD(s0)) < 1e-25)

print("B. Direction 2: the chiral cross form on the two-line value space")
random.seed(3)
# a synthetic zero configuration symmetric under conjugation and #: on-line zeros with multiplicities, one off-line quadruple
online = [(0.5 + 14.1j, 1), (0.5 + 21.0j, 2)]
offq = [(0.8 + 30.0j, 1)]
Z = []
for r, m in online:
    Z += [(r, m), (r.conjugate(), m)]
for r, m in offq:
    for w in (r, 1 - r.conjugate(), r.conjugate(), 1 - r):
        Z.append((w, m))
key = lambda w: (round(w.real, 9), round(w.imag, 9))
mult = {key(w): m for w, m in Z}
sharp = lambda w: 1 - w.conjugate()
A = lambda w: -w.conjugate()


def Omega(u):
    return sum(m * u[key(w)] * np.conj(u[key(sharp(w))]) for w, m in Z)


def QA(fv):  # fv: values on the two-line set Z u (Z - 1)
    tot = 0
    for w, m in Z:
        for x in (w, w - 1):
            tot += m * fv[key(x)] * np.conj(fv[key(A(x))])
    return tot


ok_dec, ok_real = True, True
for _ in range(50):
    u = {key(w): complex(random.gauss(0, 1), random.gauss(0, 1)) for w, _m in Z}
    v = {key(w): complex(random.gauss(0, 1), random.gauss(0, 1)) for w, _m in Z}
    fv = {}
    for w, _m in Z:
        fv[key(w)] = u[key(w)] + v[key(w)]
        fv[key(w - 1)] = u[key(w)] - v[key(w)]
    lhs = QA(fv)
    rhs = 2 * Omega(u) - 2 * Omega(v)
    ok_dec = ok_dec and abs(lhs - rhs) < 1e-9 * (1 + abs(lhs))
    ok_real = ok_real and abs(Omega(u).imag) < 1e-9
check("B1", "Q_A(u + v on Z, u - v on Z - 1) = 2 Omega(u) - 2 Omega(v): Weil's form on T-even data, minus it on T-odd data",
      ok_dec)
check("B2", "Omega(u) = sum m u(rho) conj u(rho^#) is real", ok_real)
fixA = [w for w, _m in Z if abs(A(w) - w) < 1e-12] + [w - 1 for w, _m in Z if abs(A(w - 1) - (w - 1)) < 1e-12]
check("B3", "A has no fixed point on the two-line zero set (so Q_A is an orthogonal sum of hyperbolic planes)", len(fixA) == 0)
w0 = offq[0][0]
u = {key(w): 0j for w, _m in Z}
u[key(w0)] = 1
u[key(sharp(w0))] = -1
check("B4", "with an off-line pair, Omega takes a negative value (u = 1 at rho, -1 at rho^#), so T-even data detect it",
      Omega(u).real < 0, f"Omega = {Omega(u).real:.1f}")
Zon = [(w, m) for w, m in Z if abs(w.real - 0.5) < 1e-12]
u = {key(w): complex(random.gauss(0, 1), random.gauss(0, 1)) for w, _m in Zon}
val = sum(m * abs(u[key(w)]) ** 2 for w, m in Zon)
om = sum(m * u[key(w)] * np.conj(u[key(sharp(w))]) for w, m in Zon)
check("B5", "on on-line zeros Omega(u) = sum m |u(rho)|^2 >= 0", abs(om - val) < 1e-9 and val > 0)

print("B'. The explicit T-even test functions f_k at the first zeta zero")


def Fstar(s):
    return s * (s - 1) / 8 * mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)


r1, r2 = mp.zetazero(1), mp.zetazero(2)
zp1 = mp.zeta(r1, 1, 1)


def kloc(s):  # entire, value 1 at rho_1, zero at every other nontrivial zero
    if abs(s - r1) < mp.mpf(10) ** -12:
        return mp.mpf(1)
    return mp.exp((s - r1) ** 2) * (s - 1) * mp.zeta(s) / ((s - r1) * (r1 - 1) * zp1)


def f_k(s, sign=1):
    return Fstar(s + 1) * Fstar(s - 1) * kloc(s) + sign * Fstar(s + 2) * Fstar(s) * kloc(s + 1)


fe0, fe1 = f_k(r1), f_k(r1 - 1)
check("B'1", "f_k(rho_1 - 1) = f_k(rho_1) = F_*(rho_1 + 1)F_*(rho_1 - 1) (T-even data)",
      abs(fe0 - fe1) / abs(fe0) < 1e-20 and abs(fe0 - Fstar(r1 + 1) * Fstar(r1 - 1)) / abs(fe0) < 1e-20)
check("B'2", "f_k vanishes at the other zeros of G (checked at rho_2, rho_2 - 1, conj rho_1, conj rho_1 - 1)",
      max(abs(f_k(x)) for x in (r2, r2 - 1, mp.conj(r1), mp.conj(r1) - 1)) < 1e-15 * abs(fe0))
QA_even = fe0 * mp.conj(fe1) + fe1 * mp.conj(fe0)
fo0, fo1 = f_k(r1, -1), f_k(r1 - 1, -1)
QA_odd = fo0 * mp.conj(fo1) + fo1 * mp.conj(fo0)
check("B'3", "Q_A(f_k) = 2|f_k(rho_1)|^2 > 0 for the T-even f_k and -2|f_k(rho_1)|^2 for the T-odd one",
      abs(QA_even - 2 * abs(fe0) ** 2) / abs(fe0) ** 2 < 1e-20 and abs(QA_odd + 2 * abs(fo0) ** 2) / abs(fo0) ** 2 < 1e-20,
      f"|f_k(rho_1)| = {mp.nstr(abs(fe0), 5)}")

print("C. Direction 3: the prime squares and the two-line race")
X = 10 ** 7
sieve = np.ones(X + 1, dtype=bool)
sieve[:2] = False
for p in range(2, int(X ** 0.5) + 1):
    if sieve[p]:
        sieve[p * p::p] = False
primes = np.nonzero(sieve)[0]
chi4 = np.where(primes % 4 == 1, 1.0, np.where(primes % 4 == 3, -1.0, 0.0))
lp = np.log(primes.astype(float))
cum_diff = np.cumsum(-chi4 * lp / primes)      # theta_G race minus theta race: -sum chi(p) log p / p
cum_theta = np.cumsum(-chi4 * lp)               # theta(x;4,3) - theta(x;4,1)
pts = [10 ** 3, 10 ** 4, 10 ** 5, 10 ** 6, 10 ** 7]
idx = [np.searchsorted(primes, x, side='right') - 1 for x in pts]
diffs = [cum_diff[i] for i in idx]
check("C1", "sum_{p<=x} -chi_{-4}(p) log p / p converges (x = 10^3 ... 10^7), so E_G(x) - E(x) = O(1/sqrt x)",
      max(diffs[-3:]) - min(diffs[-3:]) < 0.02, "; ".join(f"x=10^{k}: {d:.5f}" for k, d in zip(range(3, 8), diffs)))
E = [cum_theta[i] / np.sqrt(x) for i, x in zip(idx, pts)]
EG = [(cum_theta[i] + cum_diff[i]) / np.sqrt(x) for i, x in zip(idx, pts)]
check("C2", "the normalized races E(x) and E_G(x) differ by less than 0.03 at x = 10^5, 10^6, 10^7",
      max(abs(e - g) for e, g in zip(E[2:], EG[2:])) < 0.03, "; ".join(f"E={e:.4f}, E_G={g:.4f}" for e, g in zip(E, EG)))
sq = primes[primes <= int(X ** 0.5)]
sq = sq[sq % 2 == 1]
rat = [np.log(primes[(primes <= y) & (primes % 2 == 1)].astype(float)).sum() / y for y in (10 ** 3, int(X ** 0.5), 10 ** 6)]
check("C3", "the prime-square term for chi_{-4}: sum_{p <= y, p odd} chi(p)^2 log p = theta(y) - log 2 with y = sqrt x is of size y (ratio -> 1 by the PNT)",
      all(0.95 < r_ < 1.0 for r_ in rat) and rat[0] < rat[2], "; ".join(f"y={y}: {r_:.4f}" for y, r_ in zip((10 ** 3, int(X ** 0.5), 10 ** 6), rat)))

print("D. Direction 4: the holonomy index I(T) = (N(T) - V(T))/2")


def sign_changes(func, T, step):
    n, prev = 0, None
    t = mp.mpf(step)
    while t <= T:
        v = func(t)
        sg = 1 if v > 0 else -1 if v < 0 else 0
        if prev is not None and sg != 0 and sg != prev:
            n += 1
        if sg != 0:
            prev = sg
        t += step
    return n


for T in (100, 250):
    N = mp.nzeros(T)
    V = sign_changes(mp.siegelz, T, mp.mpf("0.01"))
    check(f"D{1 if T == 100 else 2}", f"for zeta at T = {T}: N(T) = V(T), i.e. I(T) = 0 (all zeros up to T on the line and simple)",
          N == V, f"N = {N}, V = {V}")
# a symmetric model with a double on-line zero, a simple on-line zero and one off-line quadruple
x = mp.mpf
fac_on = [(x(10), 1), (x(17), 2)]
fac_off = [(x("0.8"), x(24), 1)]


def Pmodel(t):
    s = mp.mpf(1) / 2 + 1j * t
    v = mp.mpf(1)
    for g, m in fac_on:
        v *= ((s - 0.5) ** 2 + g ** 2) ** m
    for b, g, m in fac_off:
        v *= (((s - b) ** 2 + g ** 2) * ((s - 1 + b) ** 2 + g ** 2)) ** m
    return v.real


Tm = 30
Nm = sum(m for g, m in fac_on if g <= Tm) + sum(2 * m for b, g, m in fac_off if g <= Tm)
Vm = sign_changes(Pmodel, Tm, mp.mpf("0.05"))
Pm = sum(m for b, g, m in fac_off if g <= Tm)
Im = (Nm - Vm) // 2
check("D3", "model with a double on-line zero and one off-line pair: I = P + sum floor(m/2) = 1 + 1 = 2",
      Im == Pm + sum(m // 2 for g, m in fac_on if g <= Tm) and Im == 2, f"N = {Nm}, V = {Vm}, I = {Im}")
ok = True
random.seed(7)
for _ in range(200):
    on = [(random.randint(1, 4)) for _ in range(random.randint(0, 5))]
    off = [(random.randint(1, 3)) for _ in range(random.randint(0, 4))]
    N_ = sum(on) + 2 * sum(off)
    V_ = sum(1 for m in on if m % 2 == 1)
    ok = ok and (N_ - V_) % 2 == 0 and (N_ - V_) // 2 == sum(off) + sum(m // 2 for m in on)
check("D4", "the counting identity N - V = 2P + 2 sum floor(m/2) on 200 random configurations", ok)

n_pass = sum(results)
print("=" * 100)
print(f"{len(results)} items: {n_pass} PASS, {len(results) - n_pass} FAIL")
