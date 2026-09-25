#!/usr/bin/env python3
# Checks for claude-ab note 40_ (OMS5-OMS7A of ORIGINAL_MELLIN_SPECTRAL_SYNTHESIS.md, with AC1-AC3 and CW1,
# and Proposition 40.4 on the convergence of the primary decomposition).
# Written by Claude (claude-ab lane), model claude-opus-5-5 (Opus 5.5) at maximum reasoning effort, 25 September 2026.
# Items marked "illustration" test numerical consequences on the first zeros; they are not proofs.
# First run at 20:54 UTC (31/31 PASS). Revised after the seventeenth referee pass: E3 now compares two independent
# computations, F2 allows for the equality at t = 0, and F2a and G1-G3 were added.
# Re-run at 21:46 UTC: 35/35 PASS (output in oms5_7a_checks_OUTPUT.txt).
import itertools
import random
from fractions import Fraction

import mpmath as mp

mp.mp.dps = 30
results = []


def check(label, desc, ok, detail=""):
    ok = bool(ok)
    results.append(ok)
    line = f"{len(results):3d} {'PASS' if ok else 'FAIL'}  {label}  {desc}"
    if detail:
        line += f"  -- {detail}"
    print(line)


def Cfac(s):
    # C(s) = s(s-1) pi^{-s/2} Gamma(s/2) / 8  (OMS6.4)
    return s * (s - 1) * mp.pi ** (-s / 2) * mp.gamma(s / 2) / 8


def Fstar(s):
    # F_*(s) = s(s-1)/8 pi^{-s/2} Gamma(s/2) zeta(s)  (OMS2.3, GEX2.1)
    return Cfac(s) * mp.zeta(s)


rho1 = mp.zetazero(1)
print("A. OMS6: the primary sections")
# A1: the recursion OMS6.1 inverts u(T) modulo T^m
random.seed(1)
maxerr = mp.mpf(0)
for m in range(1, 7):
    u = [mp.mpc(random.uniform(-2, 2), random.uniform(-2, 2)) for _ in range(m)]
    u[0] += 3
    c = [1 / u[0]]
    for n in range(1, m):
        c.append(-sum(u[r] * c[n - r] for r in range(1, n + 1)) / u[0])
    prod = [sum(u[r] * c[n - r] for r in range(n + 1)) for n in range(m)]
    maxerr = max(maxerr, abs(prod[0] - 1), *[abs(x) for x in prod[1:]] or [mp.mpf(0)])
check("A1", "OMS6.1: c_0 = 1/u_0, c_n = -u_0^{-1} sum u_r c_{n-r} inverts u(T) mod T^m (m = 1..6, random u)",
      maxerr < mp.mpf(10) ** -25, f"max error {mp.nstr(maxerr, 3)}")

# A2: Leibniz formula OMS6.4 for C^{(h)} against numerical differentiation, h = 0..4, at rho_1
maxrel = mp.mpf(0)
for h in range(5):
    direct = mp.diff(Cfac, rho1, h)
    s = rho1
    tot = mp.mpc(0)
    for a in range(0, 3):
        for b in range(0, h - a + 1):
            cc = h - a - b
            if cc < 0:
                continue
            poly = [s * (s - 1), 2 * s - 1, mp.mpf(2)][a]
            gam = mp.diff(mp.gamma, s / 2, cc) if cc > 0 else mp.gamma(s / 2)
            tot += mp.factorial(h) / (mp.factorial(a) * mp.factorial(b) * mp.factorial(cc)) * poly \
                * (-mp.log(mp.pi) / 2) ** b * mp.mpf(2) ** (-cc) * gam
    tot *= mp.pi ** (-s / 2) / 8
    maxrel = max(maxrel, abs(tot - direct) / abs(direct))
check("A2", "OMS6.4: Leibniz formula for C^{(h)}(rho_1), h = 0..4, against numerical differentiation",
      maxrel < mp.mpf(10) ** -15, f"max relative error {mp.nstr(maxrel, 3)}")

# A3: u_r of OMS6.4 (m = 1) against Taylor coefficients of F_* at rho_1
maxrel = mp.mpf(0)
for r in range(4):
    formula = sum(mp.diff(Cfac, rho1, h) / mp.factorial(h) * mp.zeta(rho1, 1, 1 + r - h) / mp.factorial(1 + r - h)
                  for h in range(r + 1))
    direct = mp.diff(Fstar, rho1, r + 1) / mp.factorial(r + 1)
    maxrel = max(maxrel, abs(formula - direct) / abs(direct))
check("A3", "OMS6.4: u_r = sum_h C^{(h)}(rho)/h! zeta^{(m+r-h)}(rho)/(m+r-h)! (m = 1, r = 0..3, rho_1)",
      maxrel < mp.mpf(10) ** -12, f"max relative error {mp.nstr(maxrel, 3)}")

# A4: jets of W_a: j_rho(a^s F) = a^rho exp((log a) T) j_rho(F) mod T^m (OMS6.5), F = exp(s^2/100), a = 3, m = 4


def Ftest(s):
    return mp.exp(s ** 2 / 100)


a = mp.mpf(3)
m = 4
lhs = mp.taylor(lambda s: a ** s * Ftest(s), rho1, m - 1)
jf = mp.taylor(Ftest, rho1, m - 1)
ex = [a ** rho1 * mp.log(a) ** r / mp.factorial(r) for r in range(m)]
rhs = [sum(ex[i] * jf[n - i] for i in range(n + 1)) for n in range(m)]
err = max(abs(lhs[n] - rhs[n]) / max(abs(rhs[n]), mp.mpf(10) ** -40) for n in range(m))
check("A4", "OMS6.5: j_rho W_a = multiplication by a^rho exp((log a)T) on jets (a = 3, m = 4, rho_1)",
      err < mp.mpf(10) ** -12, f"max relative error {mp.nstr(err, 3)}")

print("B. OMS7 and CW1: the Gaussian coefficient map")
s0 = mp.mpc(0.3, 2)
quad = mp.quad(lambda v: mp.exp(-v ** 2 + (s0 - mp.mpf(1) / 2) * v), [-mp.inf, 0, mp.inf])
check("B1", "CW1.3: F_b(s) = sqrt(pi) exp((s-1/2)^2/4) for b(u) = exp(-(log u)^2) (quadrature at s = 0.3+2i)",
      abs(quad - mp.sqrt(mp.pi) * mp.exp((s0 - mp.mpf(1) / 2) ** 2 / 4)) < mp.mpf(10) ** -20)
x = mp.mpf(10)
tx = mp.log(x)
s1 = mp.mpc(0.7, 1.5)
Kb = lambda uu: mp.sqrt(tx) * mp.exp(-(mp.log(uu) - mp.log(tx)) ** 2)
mell = mp.quad(lambda v: Kb(mp.exp(v)) * mp.exp((s1 - mp.mpf(1) / 2) * v), [-mp.inf, mp.log(tx), mp.inf])
B = lambda s: mp.sqrt(mp.pi) * mp.exp((s - mp.mpf(1) / 2) ** 2 / 4)
check("B2", "CW1.5: F_{K_b[x]}(s) = B(s)(log x)^s for K_b[x](u) = (log x)^{1/2} exp(-(log u - log log x)^2) (x = 10)",
      abs(mell - B(s1) * tx ** s1) < mp.mpf(10) ** -20)
jet = mp.taylor(lambda s: B(s) * tx ** s, rho1, 4)
Bjet = mp.taylor(lambda T: mp.sqrt(mp.pi) * mp.exp((rho1 - mp.mpf(1) / 2) ** 2 / 4)
                 * mp.exp((rho1 - mp.mpf(1) / 2) * T / 2 + T ** 2 / 4), 0, 4)
ll = [tx ** rho1 * mp.log(tx) ** r / mp.factorial(r) for r in range(5)]
prod = [sum(Bjet[i] * ll[n - i] for i in range(n + 1)) for n in range(5)]
err = max(abs(jet[n] - prod[n]) / abs(prod[n]) for n in range(5))
check("B3", "OMS7.1: j_rho K_b[x] = B(rho+T)(log x)^rho sum (log log x)^r T^r/r!, with B(rho+T) as displayed (orders 0..4)",
      err < mp.mpf(10) ** -12, f"max relative error {mp.nstr(err, 3)}")

print("C. OMS7.2-7.3: the supported-zero receiver G_L on the four-element Boolean lattice")
BOT, A_, B_, TOP = frozenset(), frozenset({0}), frozenset({1}), frozenset({0, 1})
L = [BOT, A_, B_, TOP]


def is_zero(v):
    return all(c == 0 for c in v)


def in_G(e):
    v, lam = e
    return lam == TOP or is_zero(v)


def add(e1, e2):
    return (tuple(p + q for p, q in zip(e1[0], e2[0])), e1[1] | e2[1])


def smul(sc, e):
    c, nu = sc
    return (tuple(c * p for p in e[0]), nu & e[1])


def apply(M, v):
    return tuple(sum(M[i][j] * v[j] for j in range(len(v))) for i in range(len(M)))


def G(M):
    return lambda e: (apply(M, e[0]), e[1])


random.seed(2)
vecs = [(0, 0), (1, 0), (0, 1), (2, -3), (Fraction(1, 2), 5)]
elems = [((0, 0), lam) for lam in L] + [(v, TOP) for v in vecs]
f = [[random.randint(-3, 3) for _ in range(2)] for _ in range(3)]
g = [[random.randint(-3, 3) for _ in range(3)] for _ in range(2)]
gf = [[sum(g[i][k] * f[k][j] for k in range(3)) for j in range(2)] for i in range(2)]
scal = [(0, lam) for lam in L] + [(c, TOP) for c in (1, -2, Fraction(3, 7))]
ok_closed = all(in_G(add(e1, e2)) for e1 in elems for e2 in elems) and all(in_G(smul(c, e)) for c in scal for e in elems)
check("C1", "G_L(V) is closed under (v,l)+(w,m) = (v+w, l v m) and under scalars from G_L(C)", ok_closed)
check("C2", "G_L(f) is well defined: it maps G_L(V) into G_L(W)", all(in_G(G(f)(e)) for e in elems))
check("C3", "G_L(f) preserves the addition and the G_L(C)-scalar action",
      all(G(f)(add(e1, e2)) == add(G(f)(e1), G(f)(e2)) for e1 in elems for e2 in elems)
      and all(G(f)(smul(c, e)) == smul(c, G(f)(e)) for c in scal for e in elems))
check("C4", "functoriality: G_L(g f) = G_L(g) G_L(f) and G_L(id) = id",
      all(G(gf)(e) == G(g)(G(f)(e)) for e in elems) and all(G([[1, 0], [0, 1]])(e) == e for e in elems))
bad = smul((2, A_), ((1, 0), TOP))
check("C5", "control: a scalar (c, nu) with c != 0 and nu non-top is not in G_L(C) and leaves G_L(V) [expected: outside]",
      (not in_G(((2,), A_))) and (not in_G(bad)))
check("C6", "G_L(V) is a commutative monoid, not a group: (0, a) has no additive inverse",
      all(add(((0, 0), A_), e)[1] != BOT for e in elems))

print("D. OMS5.6: the Cauchy estimate |F^{(r)}(rho)/r!| (1+|gamma|)^M <= 2^{r+M} b_{2,M}(F), F = exp(s^2/100)")
zeros = [mp.zetazero(n) for n in range(1, 31)]
tgrid = [mp.mpf(k) / 10 for k in range(-1200, 1201)]
worst = mp.mpf(0)
for M in range(3):
    # a lower estimate of b_{2,M}(F) by sampling makes the check conservative
    bM = max((1 + abs(t)) ** M * abs(Ftest(mp.mpc(sg, t))) for sg in (-2, 2) for t in tgrid)
    for rr in range(3):
        for z in zeros[:10]:
            lhs = (1 + abs(z.imag)) ** M * abs(mp.diff(Ftest, z, rr) / mp.factorial(rr))
            worst = max(worst, lhs / (2 ** (rr + M) * bM))
check("D1", "OMS5.6 with the explicit constant C_{r,M} = 2^{r+M} (r, M = 0..2, first 10 zeros)", worst <= 1,
      f"max ratio {mp.nstr(worst, 4)}")

print("E. OMS7A with AC1-AC2: the adelic split and the source inverse")
h0 = lambda xx: (1 - 2 * mp.pi * xx ** 2) * mp.exp(-mp.pi * xx ** 2)
h1 = lambda xx: 2 * mp.pi * xx ** 2 * mp.exp(-mp.pi * xx ** 2)
mom = lambda h: (h(0), mp.quad(h, [-mp.inf, mp.inf]))
m0, m1 = mom(h0), mom(h1)
check("E1", "AC1.4: m(h_0) = (1, 0), m(h_1) = (0, 1)",
      abs(m0[0] - 1) + abs(m0[1]) + abs(m1[0]) + abs(m1[1] - 1) < mp.mpf(10) ** -25)
fstar = lambda v: mp.pi / 2 * v ** 2 * (2 * mp.pi * v ** 2 - 3) * mp.exp(-mp.pi * v ** 2)
check("E2", "OMS2.3: f_* lies in H_00 (f_*(0) = 0, integral 0)",
      abs(fstar(0)) + abs(mp.quad(fstar, [-mp.inf, mp.inf])) < mp.mpf(10) ** -25)


def Eper(h, y, N=None):
    # E h(y) = y^{1/2} sum_{n>=1} h(n y)
    N = N or int(40 / y) + 40
    return mp.sqrt(y) * mp.fsum(h(n * y) for n in range(1, N + 1))


bb = mp.mpf("1.7")
s3 = mp.mpf("2.5")
# Mellin side of AC2.12: with k = J(t_1 (x) f_*) = 2 E f_*, the transform of J R_b c, i.e. of 2 E(f_*(./b)), is b^s F_k(s).
# Both sides are computed independently: the left by quadrature of the periodized dilated source, the right from GEX2.1.
kdil = lambda uu: 2 * Eper(lambda v: fstar(v / bb), uu, int(60 * bb / uu) + 60)
lhs3 = mp.quad(lambda v: kdil(mp.exp(v)) * mp.exp((s3 - mp.mpf(1) / 2) * v), [-6, -2, 0, 2, 6])
rhs3 = bb ** s3 * 2 * Fstar(s3)
check("E3", "AC2.12 on the Mellin side: F_{J R_b c}(s) = b^s F_{Jc}(s) for c = [t_1 (x) f_*], b = 1.7, s = 2.5 (quadrature)",
      abs(lhs3 - rhs3) < mp.mpf(10) ** -12, f"difference {mp.nstr(abs(lhs3 - rhs3), 3)}")


def mobius(n):
    res, p, k = 1, 2, n
    while p * p <= k:
        if k % p == 0:
            k //= p
            if k % p == 0:
                return 0
            res = -res
        p += 1
    if k > 1:
        res = -res
    return res


kfun = lambda uu: 2 * Eper(fstar, uu)
err = mp.mpf(0)
for xx in (mp.mpf(0.7), mp.mpf(1.3)):
    hk = mp.fsum(mobius(n) * (n * xx) ** (-mp.mpf(1) / 2) * kfun(n * xx) for n in range(1, 40)) / 2
    err = max(err, abs(hk - fstar(xx)))
check("E4", "AC2.9: h_k = (1/2) sum mu(n) (nx)^{-1/2} k(nx) recovers f_* from k = 2 E f_* (x = 0.7, 1.3)",
      err < mp.mpf(10) ** -20, f"max error {mp.nstr(err, 3)}")


def kstar(uu):
    # k_* = E f_*, with k_*(u) = k_*(1/u) (OMS2.3) used for u < 1
    return Eper(fstar, uu) if uu >= 1 else Eper(fstar, 1 / uu)


u5 = mp.mpf("0.8")  # exact decimal input: a binary float 0.8 is not exactly 1/1.25
check("E5", "OMS2.3: k_*(u) = k_*(1/u) (Poisson, since f_* is Fourier self-dual with f_*(0) = 0 = integral; u = 0.8, 0.5)",
      max(abs(Eper(fstar, uu, 400) - Eper(fstar, 1 / uu)) for uu in (u5, mp.mpf("0.5"))) < mp.mpf(10) ** -20)
for sv in (mp.mpf(2.5), mp.mpc(0.5, 3)):
    mel = mp.quad(lambda v: kstar(mp.exp(v)) * mp.exp((sv - mp.mpf(1) / 2) * v), [-12, 0, 12])
    check("E6" if sv == 2.5 else "E7", f"OMS2.3/GEX2.1: F_{{E f_*}}(s) = F_*(s) at s = {mp.nstr(sv, 3)}",
          abs(mel - Fstar(sv)) < mp.mpf(10) ** -15, f"difference {mp.nstr(abs(mel - Fstar(sv)), 3)}")
check("E8", "OMS2.5/GEX2.2: F_*(0) = F_*(1) = 1/8 (limits)",
      abs(mp.limit(Fstar, 0) - mp.mpf(1) / 8) + abs(mp.limit(Fstar, 1) - mp.mpf(1) / 8) < mp.mpf(10) ** -20)

print("F. Proposition 40.4: the inputs of the proof")
# F1: |chi(-1+it)| >= 1/(2 pi^2) and |zeta(-1+it)| >= 3/pi^4 (left side of the rectangle)
chi = lambda s: 2 ** s * mp.pi ** (s - 1) * mp.sin(mp.pi * s / 2) * mp.gamma(1 - s)
chi2 = lambda s: mp.pi ** (s - mp.mpf(1) / 2) * mp.gamma((1 - s) / 2) / mp.gamma(s / 2)
tg = [mp.mpf(k) / 4 for k in range(-400, 401)]
e_forms = max(abs(chi(mp.mpc(-1, t)) - chi2(mp.mpc(-1, t))) / abs(chi2(mp.mpc(-1, t))) for t in tg[::20])
check("F1", "OMS3.2: the two expressions for chi agree on Re s = -1", e_forms < mp.mpf(10) ** -20)
mchi = min(abs(chi2(mp.mpc(-1, t))) for t in tg)
check("F2", "|chi(-1+it)| >= 1/(2 pi^2) (from OMS3.6 with N = 0; equality at t = 0, so a relative margin 1e-25 is allowed), t in [-100, 100]",
      mchi >= (1 - mp.mpf(10) ** -25) / (2 * mp.pi ** 2), f"min {mp.nstr(mchi, 8)} vs {mp.nstr(1 / (2 * mp.pi ** 2), 8)}")
cf = max(abs(abs(chi2(mp.mpc(-1, t))) ** 2 - mp.pi ** -3 * (t / 2) * mp.coth(mp.pi * t / 2) * (mp.mpf(1) / 4 + (t / 2) ** 2))
         for t in tg[::7] if t != 0)
check("F2a", "closed form |chi(-1+it)|^2 = pi^{-3} y coth(pi y)(1/4 + y^2), y = t/2 (OMS3.6, N = 0)", cf < mp.mpf(10) ** -25,
      f"max error {mp.nstr(cf, 3)}")
mz = min(abs(mp.zeta(mp.mpc(-1, t))) for t in tg)
check("F3", "|zeta(-1+it)| >= 3/pi^4, t in [-100, 100]", mz >= 3 / mp.pi ** 4, f"min {mp.nstr(mz, 6)}")
mz2 = min(abs(mp.zeta(mp.mpc(2, t))) for t in tg)
check("F4", "|zeta(2+it)| >= 1/zeta(2) = 6/pi^2, t in [-100, 100]", mz2 >= 6 / mp.pi ** 2, f"min {mp.nstr(mz2, 6)}")

# F5 (illustration): good heights: some t in [T, T+1] with min_{-1<=sigma<=2} |zeta(sigma+it)| >= T^{-1}
sg = [mp.mpf(-1) + mp.mpf(k) / 10 for k in range(31)]
ok = True
det = []
for T in (50, 100, 200):
    best = max(min(abs(mp.zeta(mp.mpc(s_, T + mp.mpf(j) / 50))) for s_ in sg) for j in range(51))
    det.append(f"T={T}: {mp.nstr(best, 3)}")
    ok = ok and best >= mp.mpf(T) ** -1
check("F5", "illustration of the good-heights lemma: max over t in [T,T+1] of min over sigma of |zeta| >= 1/T",
      ok, "; ".join(det))


# F6-F8: the interpolating representatives G_rho of Proposition 40.4(ii)
def Grep(z, zp):
    return lambda s: mp.exp((s - z) ** 2) * (s - 1) * mp.zeta(s) / ((s - z) * (z - 1) * zp)


zp = [mp.zeta(z, 1, 1) for z in zeros]
eps = mp.mpf(10) ** -12
v_at = max(abs(Grep(zeros[i], zp[i])(zeros[i] + eps) - 1) for i in range(30))
check("F6", "G_rho(rho) = 1 (limit, first 30 zeros)", v_at < mp.mpf(10) ** -9, f"max |G-1| {mp.nstr(v_at, 3)}")
v_off = max(abs(Grep(zeros[i], zp[i])(zeros[j])) for i in range(10) for j in range(30) if j != i)
check("F7", "G_rho(eta) = 0 at the other zeros (first 10 rho, first 30 eta)", v_off < mp.mpf(10) ** -20,
      f"max {mp.nstr(v_off, 3)}")
# F8 (illustration): sampled b_{2,0}(G_rho) |zeta'(rho)| grows at most polynomially in gamma
vals = []
for i in (0, 4, 9, 19, 29):
    z = zeros[i]
    Gz = Grep(z, zp[i])
    samp = []
    for s_ in (-2, -1, 0, 1, 2):
        for k in range(-60, 61):
            pt = mp.mpc(s_, z.imag + mp.mpf(k) / 10)
            if abs(pt - z) > mp.mpf(10) ** -6:
                samp.append(abs(Gz(pt)))
    vals.append((z.imag, max(samp) * abs(zp[i])))
slope = (mp.log(vals[-1][1]) - mp.log(vals[0][1])) / (mp.log(vals[-1][0]) - mp.log(vals[0][0]))
check("F8", "illustration: sampled b_{2,0}(G_rho)|zeta'(rho)| over gamma = 14..102 grows like a power of gamma",
      slope < 4, "; ".join(f"g={mp.nstr(g, 4)}: {mp.nstr(v, 4)}" for g, v in vals) + f"; log-log slope {mp.nstr(slope, 3)}")

# F9: the maximum-principle step of Proposition 40.4(i) on a rectangle around rho_1
z = zeros[0]
Gz = Grep(z, zp[0])
H = lambda s: Gz(s) * (s - z) / mp.zeta(s)
T1, T2 = z.imag - mp.mpf(1.5), z.imag + mp.mpf(1.5)
bd = []
for k in range(0, 301):
    sgm = mp.mpf(-1) + 3 * mp.mpf(k) / 300
    bd += [abs(H(mp.mpc(sgm, T1))), abs(H(mp.mpc(sgm, T2)))]
for k in range(0, 301):
    tt = T1 + (T2 - T1) * mp.mpf(k) / 300
    bd += [abs(H(mp.mpc(-1, tt))), abs(H(mp.mpc(2, tt)))]
check("F9", "Prop. 40.4(i), maximum principle: 1/|zeta'(rho_1)| = |H(rho_1)| <= max over the rectangle boundary",
      1 / abs(zp[0]) <= max(bd), f"1/|zeta'| = {mp.nstr(1 / abs(zp[0]), 5)}, boundary max {mp.nstr(max(bd), 5)}")

print("G. Proposition 40.5 (all multiplicities): interpolants at a triple zero of a model")
z1, z2 = zeros[0], zeros[1]
mm = 3
lam = mm + 1
Zm = lambda s: mp.zeta(s) * (s - z1) ** 2  # the zeros of zeta, with rho_1 made a triple zero
# V(s) = (s-1) Z(s)/(s - rho_1)^3 = (s-1) zeta(s)/(s - rho_1) is entire; near rho_1 use its Taylor series
aV = mp.taylor(lambda s: (s - 1) * mp.zeta(s), z1, 16)
vser = aV[1:]


def Vm(s):
    if abs(s - z1) < mp.mpf(10) ** -6:
        return mp.fsum(vser[n] * (s - z1) ** n for n in range(len(vser)))
    return (s - 1) * mp.zeta(s) / (s - z1)


vj = vser[:mm]
inv = [1 / vj[0]]
for n in range(1, mm):
    inv.append(-sum(vj[r] * inv[n - r] for r in range(1, n + 1)) / vj[0])
eml = [((-lam) ** (i // 2) / mp.factorial(i // 2)) if i % 2 == 0 else mp.mpf(0) for i in range(mm)]
worst_jet, worst_off = mp.mpf(0), mp.mpf(0)
for k in range(mm):
    tk = [mp.mpf(1) if i == k else mp.mpf(0) for i in range(mm)]
    a1 = [sum(tk[i] * eml[n - i] for i in range(n + 1)) for n in range(mm)]
    q = [sum(a1[i] * inv[n - i] for i in range(n + 1)) for n in range(mm)]
    Gk = lambda s, q=q: mp.exp(lam * (s - z1) ** 2) * Vm(s) * sum(q[i] * (s - z1) ** i for i in range(mm))
    jet = mp.taylor(Gk, z1, mm - 1)
    worst_jet = max(worst_jet, max(abs(jet[i] - tk[i]) for i in range(mm)))
    worst_off = max(worst_off, abs(Gk(z2)))
check("G1", "Prop. 40.5: G_{rho,k} = e^{lam(s-rho)^2} V_rho(s) q_{rho,k}(s-rho) has jet T^k mod T^3 at a triple zero (k = 0, 1, 2)",
      worst_jet < mp.mpf(10) ** -12, f"max jet error {mp.nstr(worst_jet, 3)}")
check("G2", "... and vanishes at the other zeros (checked at rho_2)", worst_off < mp.mpf(10) ** -20, f"|G(rho_2)| {mp.nstr(worst_off, 3)}")
# c_{rho,k}: Taylor coefficients of (s - rho)^3/Z(s) = (s - rho)/zeta(s) = 1/(sum b_{n+1} T^n), b = Taylor coefficients of zeta
bz = mp.taylor(mp.zeta, z1, 8)
den = bz[1:]
cz = [1 / den[0]]
for n in range(1, mm):
    cz.append(-sum(den[r] * cz[n - r] for r in range(1, n + 1)) / den[0])
pp = lambda s: mp.fsum(cz[k] * (s - z1) ** (k - mm) for k in range(mm))
reg = max(abs(1 / Zm(z1 + d) - pp(z1 + d)) for d in (mp.mpf(10) ** -3, mp.mpc(0, 1) * mp.mpf(10) ** -3))
check("G3", "sum_k c_{rho,k}(s-rho)^{k-m} is the principal part of 1/Z at rho: 1/Z - principal part stays bounded near rho",
      reg < 10, f"|1/Z - pp| at distance 1e-3: {mp.nstr(reg, 4)}; |1/Z| there {mp.nstr(abs(1 / Zm(z1 + mp.mpf(10) ** -3)), 4)}")

n_pass = sum(results)
print("=" * 100)
print(f"{len(results)} items: {n_pass} PASS, {len(results) - n_pass} FAIL")
