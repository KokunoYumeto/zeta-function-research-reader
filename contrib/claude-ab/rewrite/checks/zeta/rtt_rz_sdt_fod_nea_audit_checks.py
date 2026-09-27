#!/usr/bin/env python3
# Copied from the first-pass audit of RTT, RZ, SDT, FOD and NEA (one subagent of claude-ab, 25 September 2026, about 11:58-12:23 UTC), for note 27_.
# Unchanged below this header, except for this comment block. Run: python3 rtt_rz_sdt_fod_nea_audit_checks.py
"""checks27.py -- numerical checks for audit27 (blocks RTT, RZ, SDT, FOD, NEA).
Each item prints PASS/FAIL.  'control' items are negative controls: they PASS when a
deliberately wrong variant (flipped sign etc.) is detected as wrong."""
import random
import mpmath as mp

mp.mp.dps = 30
pi = mp.pi
RES = []

def report(tag, ok, detail=""):
    RES.append((tag, bool(ok)))
    print(f"[{'PASS' if ok else 'FAIL'}] {tag}  {detail}", flush=True)

def rel(a, b):
    return abs(a - b) / max(mp.mpf(1e-300), abs(b))

def C0(s):
    return s * (s - 1) / 8 * pi ** (-s / 2) * mp.gamma(s / 2)

def F0(s):
    return C0(s) * mp.zeta(s)

def F0lim(s0, eps=mp.mpf('1e-25')):
    with mp.workdps(70):
        return (F0(s0 + eps) + F0(s0 - eps)) / 2

def f0(v):
    v = mp.mpmathify(v)
    return pi / 2 * v ** 2 * (2 * pi * v ** 2 - 3) * mp.exp(-pi * v ** 2)

def contour(func, center, radius):
    g = lambda th: func(center + radius * mp.expj(th)) * 1j * radius * mp.expj(th)
    return mp.quad(g, [0, pi / 2, pi, 3 * pi / 2, 2 * pi]) / (2j * pi)

def chi1(s):
    return 2 ** s * pi ** (s - 1) * mp.sin(pi * s / 2) * mp.gamma(1 - s)

def chi2(s):
    return pi ** (s - mp.mpf(1) / 2) * mp.gamma((1 - s) / 2) / mp.gamma(s / 2)

ZEROS = [mp.zetazero(k) for k in range(1, 26)]
rho1 = ZEROS[0]

print("=" * 70)
print("BLOCK 1: RESIDUE_TRACE_TRANSFER_INDEPENDENT (RTT)")
print("=" * 70)

# RTT2.5 / RZ1.7: F0(0)=F0(1)=1/8
v0, v1 = F0lim(mp.mpf(0)), F0lim(mp.mpf(1))
report("RTT2.5 F0(0)=F0(1)=1/8", rel(v0, mp.mpf(1)/8) < 1e-20 and rel(v1, mp.mpf(1)/8) < 1e-20,
       f"F0(0)={mp.nstr(v0,15)} F0(1)={mp.nstr(v1,15)}")

# RTT2.2: H_zeta(s)=s^2 zeta'(1-s), H(0)=-1, (H+1)/s^2 -> -gamma_1
with mp.workdps(50):
    H = lambda s: s ** 2 * mp.zeta(1 - s, derivative=1)
    s = mp.mpf('1e-8')
    h0 = H(s)
    coef = (H(s) + 1) / s ** 2
    g1 = mp.stieltjes(1)
report("RTT2.2 H_zeta(0)=-1", abs(h0 + 1) < 1e-14, f"H(1e-8)={mp.nstr(h0,20)}")
report("RTT2.2 H_zeta(s)=-1-gamma_1 s^2+...", abs(coef + g1) < 1e-6,
       f"(H+1)/s^2={mp.nstr(coef,12)} -gamma_1={mp.nstr(-g1,12)}")

# RTT2.3: Euler-Maclaurin with remainder sign -
def zeta_EM(z, M, N=60, sign=-1):
    tot = 1 / (z - 1) + mp.mpf(1) / 2
    for k in range(1, M + 1):
        tot += mp.bernoulli(2 * k) / mp.factorial(2 * k) * mp.rf(z, 2 * k - 1)
    w = z + 2 * M
    I = mp.mpf(0)
    for n in range(1, N + 1):
        I += mp.quad(lambda y: mp.bernpoly(2 * M, y) * (n + y) ** (-w), [0, 1])
    # tail: int_N^inf B~_{2M}(x) x^{-w} dx ~ -w B_{2M+2} N^{-w-1}/((2M+1)(2M+2))
    I += -w * mp.bernoulli(2 * M + 2) * mp.mpf(N) ** (-w - 1) / ((2 * M + 1) * (2 * M + 2))
    return tot + sign * mp.rf(z, 2 * M) / mp.factorial(2 * M) * I

with mp.workdps(20):
    worst = 0
    errs = []
    for z in [mp.mpf('2.5'), mp.mpc(0.3, 5), mp.mpc(-1.5, 2), mp.mpc(-3.2, -4)]:
        for M in [3, 6]:
            if mp.re(z) > 1 - 2 * M:
                e = rel(zeta_EM(z, M, N=120), mp.zeta(z))
                errs.append(mp.nstr(e, 2))
                worst = max(worst, e)
    print("   per-point rel errors:", errs)
    report("RTT2.3 Euler-Maclaurin formula (M=3,6; 4 points incl. Re z<0)", worst < 1e-9,
           f"max rel err={mp.nstr(worst,3)}")
    bad = rel(zeta_EM(mp.mpc(-1.5, 2), 3, sign=+1), mp.zeta(mp.mpc(-1.5, 2)))
    report("RTT2.3 control: remainder with + sign is wrong", bad > 1e-3, f"rel err={mp.nstr(bad,3)}")

# RTT3.2-3.3: local jet of f'(rho - t) for f(v)=v^m u(v): only t^{m-1} survives mod t^m
ok = True
for m in range(1, 6):
    u = lambda v: 2 + v + 3 * v ** 2 + mp.exp(v) * (1 + 0.5j)
    fprime = lambda v: mp.diff(lambda x: x ** m * u(x), v)
    g = lambda t: fprime(-t)
    coeffs = mp.taylor(g, 0, m - 1)
    target = m * (-1) ** (m - 1) * u(0)
    ok &= all(abs(c) < 1e-12 for c in coeffs[:m - 1]) and abs(coeffs[m - 1] - target) < 1e-10
report("RTT3.3 jet of zeta'(rho-t) mod t^m = m(-1)^{m-1}u(0)t^{m-1} (synthetic, m=1..5)", ok)

# RTT5.4: Res_{s=rho} F(s)(-(s-rho))^{m-1}/Z(s) * m(-1)^{m-1}u(0) = m F(rho), Z=(s-rho)^m u
ok = True
rho = mp.mpc(0.3, 1.7)
Fs = lambda s: mp.exp(s ** 2 / 3 + 0.2j * s)
for m in range(1, 5):
    u = lambda v: 1.5 - 0.7j + v + v ** 2 / 3
    Z = lambda s: (s - rho) ** m * u(s - rho)
    res = contour(lambda s: Fs(s) * (-(s - rho)) ** (m - 1) / Z(s), rho, 0.3)
    ok &= rel(res * m * (-1) ** (m - 1) * u(0), m * Fs(rho)) < 1e-15
report("RTT5.4 residue of isolator e_{1-rho,m-1} with coefficient (RTT5.3) gives m F(rho)", ok)

# RTT4.2: Res_{s=rho1} F zeta'/zeta = F(rho1) (m=1)
Fg = lambda s: mp.exp((s - rho1) ** 2 / 4 + 0.3 * s)
res = contour(lambda s: Fg(s) * mp.zeta(s, derivative=1) / mp.zeta(s), rho1, 0.5)
report("RTT4.1-4.2 Res F*zeta'/zeta at rho_1 = F(rho_1)", rel(res, Fg(rho1)) < 1e-15,
       f"rel={mp.nstr(rel(res, Fg(rho1)),3)}")

# RTT9.1: two forms of chi and functional equation
ok = True
for s in [mp.mpc(0.3, 7), mp.mpc(2.2, -1.1), mp.mpc(-1.7, 3.3)]:
    ok &= rel(chi1(s), chi2(s)) < 1e-20 and rel(mp.zeta(s), chi2(s) * mp.zeta(1 - s)) < 1e-20
report("RTT9.1 chi forms agree and zeta(s)=chi(s)zeta(1-s)", ok)

# RTT9.2: zeta'(1-s) = chi'/chi^2 zeta(s) - zeta'(s)/chi(s)
ok = True
for s in [mp.mpc(0.3, 7), mp.mpc(2.2, -1.1), mp.mpc(-1.7, 3.3)]:
    lhs = mp.zeta(1 - s, derivative=1)
    cp = mp.diff(chi2, s)
    rhs = cp / chi2(s) ** 2 * mp.zeta(s) - mp.zeta(s, derivative=1) / chi2(s)
    ok &= rel(lhs, rhs) < 1e-15
report("RTT9.2 differentiated functional equation", ok)

# RTT3.3 vs RTT9.2 consistency at actual zeros (m=1): zeta'(sigma) = -chi(sigma) zeta'(1-sigma)
ok = True
for sig in ZEROS[:4]:
    ok &= rel(mp.zeta(sig, derivative=1), -chi2(sig) * mp.zeta(1 - sig, derivative=1)) < 1e-15
report("RTT3.3/RTT9.2 u_sigma(0)=(-1)^m chi(sigma) u_{1-sigma}(0) at rho_1..rho_4", ok)

# RTT9.3 / RZ1.8 / FOD1.7: trivial-zero values
ok = True
for r in range(1, 5):
    a = F0lim(mp.mpf(-2 * r))
    b = r * (2 * r + 1) * (-1) ** r * pi ** r / (2 * mp.factorial(r)) * mp.zeta(-2 * r, derivative=1)
    c = (1 + 2 * r) * (2 * r) / mp.mpf(8) * pi ** (-(1 + 2 * r) / mp.mpf(2)) * mp.gamma((1 + 2 * r) / mp.mpf(2)) * mp.zeta(1 + 2 * r)
    ok &= rel(a, b) < 1e-18 and rel(b, c) < 1e-20 and abs(c) > 0
report("RTT9.3/RZ1.8 F0(-2r) = r(2r+1)(-1)^r pi^r zeta'(-2r)/(2 r!) = F0(1+2r) != 0 (r=1..4)", ok)

# RTT9.4: Weil explicit formula for A(s)=exp(alpha w^2+beta w), w=s-1/2
def explicit(alpha, beta, flip=None):
    alpha, beta = mp.mpf(alpha), mp.mpf(beta)
    A = lambda s: mp.exp(alpha * (s - 0.5) ** 2 + beta * (s - 0.5))
    h = lambda v: mp.exp(-(v + beta) ** 2 / (4 * alpha)) / mp.sqrt(4 * pi * alpha)
    lhs = mp.fsum(A(r) + A(mp.conj(r)) for r in ZEROS)
    P = mp.fsum(mp.mangoldt(n) / mp.sqrt(n) * (h(mp.log(n)) + h(-mp.log(n)))
                for n in range(2, 400) if mp.mangoldt(n) != 0)
    T = mp.sqrt(90 / alpha)
    Ainf = mp.quad(lambda t: A(0.5 + 1j * t) * (mp.re(mp.digamma(0.25 + 0.5j * t)) - mp.log(pi)),
                   mp.linspace(-T, T, 41)) / (2 * pi)
    sgnP = +1 if flip == 'P' else -1
    rhs = A(0) + A(1) + Ainf + sgnP * P
    return lhs, rhs

with mp.workdps(25):
    for (al, be) in [(0.02, 0), (0.02, 0.3), (0.05, -0.2)]:
        l, r = explicit(al, be)
        report(f"RTT9.4 explicit formula alpha={al} beta={be}", abs(l - r) < 1e-15,
               f"sum_rho A={mp.nstr(l,15)} RHS={mp.nstr(r,15)}")
    l, r = explicit(0.02, 0.3, flip='P')
    report("RTT9.4 control: prime term with + sign fails", abs(l - r) > 1e-4, f"diff={mp.nstr(abs(l-r),3)}")

print("=" * 70)
print("BLOCK 2: ORIGINAL_ZETA_RESOLVENT_AND_PROJECTORS (RZ)")
print("=" * 70)

# RZ1.5-1.6: Mellin of f0
ok = True
for s in [mp.mpf('2.3'), mp.mpc(1.7, 3), mp.mpc(0.6, -2)]:
    m = mp.quad(lambda v: f0(v) * v ** (s - 1), [0, 1, 3, 8])
    ok &= rel(m, C0(s)) < 1e-20
report("RZ1.6 int_0^inf f0(v) v^{s-1} dv = s(s-1)/8 pi^{-s/2} Gamma(s/2)", ok)
intf0 = mp.quad(f0, [-mp.inf, 0, mp.inf])
report("RZ1.6/SDT0.1 f0 in S: even, f0(0)=0, int f0 = 0", abs(intf0) < 1e-25 and f0(0) == 0 and f0(0.7) == f0(-0.7),
       f"int f0={mp.nstr(intf0,3)}")
fh = lambda xi: mp.quad(lambda x: f0(x) * mp.cos(2 * pi * x * xi), [-mp.inf, 0, mp.inf])
report("SDT8.1 context: f0 is Fourier self-dual (hat f0 = f0)",
       max(abs(fh(x) - f0(x)) for x in [0.37, 1.2]) < 1e-20)

# Theta-type sum with Poisson dual for small u
def Sig(u):  # sum_{n>=1} f0(n u)
    if u < 0.5:
        return Sig(1 / u) / u
    N = int(12 / u) + 2
    return mp.fsum(f0(n * u) for n in range(1, N))
d = max(abs(mp.fsum(f0(n * u) for n in range(1, 200)) - mp.fsum(f0(n / u) for n in range(1, 200)) / u) for u in [mp.mpf('0.7'), mp.mpf('1.9')])
report("SDT8.1 Poisson: sum f0(nu) = u^{-1} sum f0(n/u) (R Sigma h = Sigma hat h)", d < 1e-25, f"max diff={mp.nstr(d,3)}")

# RZ1.5: F0 = M k0 (u^{s-1/2} convention, k0 = u^{1/2} sum f0(nu));  = Theta Sigma f0 (FOD1.5)
ok = True
for s in [mp.mpf(2), mp.mpc(3, 1)]:
    m = mp.quad(lambda u: Sig(u) * u ** (s - 1), [mp.mpf('1e-3'), 0.1, 0.5, 1, 2, 5, 12])
    ok &= rel(m, F0(s)) < 1e-15
report("RZ1.5/FOD1.5/SDT7.3 int Sigma f0 u^{s-1} du = F0(s) (s=2, 3+i)", ok)

# RZ1.12: M(u d/du k) = -(s-1/2) M k, M(Dk)=s Mk; k=u^{1/2}e^{-pi u^2}
k = lambda u: mp.sqrt(u) * mp.exp(-pi * u ** 2)
Mk = lambda s: mp.gamma(s / 2) * pi ** (-s / 2) / 2
s = mp.mpc(1.3, 2)
mud = mp.quad(lambda u: u * mp.diff(k, u) * u ** (s - 0.5) / u, [0, 0.5, 1, 3, 8])
mk = mp.quad(lambda u: k(u) * u ** (s - 0.5) / u, [0, 0.5, 1, 3, 8])
report("RZ1.12 Mellin of u d/du and D=1/2-u d/du", rel(mk, Mk(s)) < 1e-18 and rel(mud, -(s - 0.5) * Mk(s)) < 1e-15
       and rel(0.5 * mk - mud, s * Mk(s)) < 1e-15)

# RZ4.4: inverse k_H(e^x) = (1/2pi) int H(1/2+it) e^{-itx} dt
ok = True
for x in [mp.mpf(-0.4), mp.mpf(0.3)]:
    val = mp.quad(lambda t: Mk(0.5 + 1j * t) * mp.expj(-t * x), mp.linspace(-80, 80, 17)) / (2 * pi)
    ok &= rel(val, mp.exp(x / 2) * mp.exp(-pi * mp.exp(2 * x))) < 1e-15
report("RZ4.4 Mellin inversion on the critical line", ok)

# RZ4.6: sup_x e^{N|x|}|g^{(j)}(x)| <= (N+2)^j/pi * b_{N+2,j+2}(H) for H=exp((s-1/2)^2)
ok = True
g = lambda x: mp.exp(-x ** 2 / 4) / (2 * mp.sqrt(pi))
for N in range(0, 3):
    for j in range(0, 3):
        lhs = max(mp.exp(N * abs(x)) * abs(mp.diff(g, x, j)) for x in mp.linspace(-40, 40, 401))
        A, M = N + 2, j + 2
        tmax = mp.findroot(lambda t: M / (1 + t) - 2 * t, 1)
        b = mp.exp((A + 0.5) ** 2) * (1 + tmax) ** M * mp.exp(-tmax ** 2)
        ok &= lhs <= (N + 2) ** j / pi * b
report("RZ4.6 source seminorm bound (sample H=e^{(s-1/2)^2}, N,j<=2)", ok)

# RZ3.2: removable value of the resolvent
with mp.workdps(60):
    lam = mp.mpc(0.3, 2)
    F = lambda s: mp.exp(s ** 2)
    R = lambda s: (F(s) - F0(s) * F(lam) / F0(lam)) / (lam - s)
    val = R(lam + mp.mpf('1e-25'))
    tgt = -mp.diff(F, lam) + mp.diff(F0, lam) * F(lam) / F0(lam)
report("RZ3.2 removable value R_lam F(lam) = -F'(lam)+F0'(lam)F(lam)/F0(lam)", rel(val, tgt) < 1e-15)

# RZ3.7: (lam-s)R_lam F = F - F0 F(lam)/F0(lam), R_lam((lam-s)F)=F  (pointwise)
s = mp.mpc(-0.7, 5.5)
ok = rel((lam - s) * R(s), F(s) - F0(s) * F(lam) / F0(lam)) < 1e-20
G2 = lambda x: (lam - x) * F(x)
ok &= rel((G2(s) - F0(s) * G2(lam) / F0(lam)) / (lam - s), F(s)) < 1e-20
report("RZ3.7 two resolvent identities (pointwise)", ok)

# RZ7.1: Riesz projector at rho_1, s outside and inside the contour
Ft = lambda s: mp.exp((s - mp.mpc(0.5, 14)) ** 2 / 4 + 0.3 * s)
F0p = mp.diff(F0, rho1)
Pr = lambda s: F0(s) / (s - rho1) * Ft(rho1) / F0p
ok = True
for s in [mp.mpc(2, 3), rho1 + mp.mpc(0.1, 0.05), mp.mpc(0.9, 14.0)]:
    Rl = lambda l: (Ft(s) - F0(s) * Ft(l) / F0(l)) / (l - s)
    val = contour(Rl, rho1, 0.4)
    ok &= rel(val, Pr(s)) < 1e-15
    val1 = contour(lambda l: (l - rho1) * Rl(l), rho1, 0.4)
    ok &= abs(val1) < 1e-15 * abs(Pr(s))
report("RZ7.1/RZ7.7 Riesz integral = P_rho F (s outside/inside); r=m coefficient vanishes", ok)

# RZ5.10-5.11: a_r formula and Leibniz formula for C^{(h)}
def Cder(h, s):
    Pd = [s * (s - 1), 2 * s - 1, mp.mpf(2)]
    tot = 0
    for a in range(0, min(2, h) + 1):
        for b in range(0, h - a + 1):
            c = h - a - b
            tot += mp.factorial(h) / (mp.factorial(a) * mp.factorial(b) * mp.factorial(c)) * Pd[a] * \
                   (-mp.log(pi) / 2) ** b * mp.mpf(2) ** (-c) * mp.diff(mp.gamma, s / 2, c)
    return pi ** (-s / 2) / 8 * tot
ok = all(rel(Cder(h, rho1), mp.diff(C0, rho1, h)) < 1e-15 for h in range(0, 4))
report("RZ5.11 Leibniz formula for C^{(h)}(rho_1), h=0..3", ok)
ok = True
for r in range(0, 3):
    ar = mp.diff(F0, rho1, 1 + r) / mp.factorial(1 + r)
    sm = mp.fsum(Cder(h, rho1) / mp.factorial(h) * mp.diff(mp.zeta, rho1, 1 + r - h) / mp.factorial(1 + r - h)
                 for h in range(0, r + 1))
    ok &= rel(ar, sm) < 1e-12
report("RZ5.10 a_r = sum_h C^{(h)}/h! zeta^{(m+r-h)}/(m+r-h)! at rho_1 (m=1, r=0..2)", ok)

# RZ8.9: (n^s F)^{(j)}(rho) triangular formula
n, Fz, pt = 3, (lambda s: mp.exp(s ** 2 / 5 + 0.1j * s)), mp.mpc(0.5, 14.13)
ok = True
for j in range(0, 4):
    lhs = mp.diff(lambda s: mp.power(n, s) * Fz(s), pt, j)
    rhs = mp.power(n, pt) * mp.fsum(mp.binomial(j, l) * mp.log(n) ** (j - l) * mp.diff(Fz, pt, l) for l in range(j + 1))
    ok &= rel(lhs, rhs) < 1e-12
report("RZ8.9 (T_n F)^{(j)}(rho) triangular formula, j=0..3", ok)

# RZ9.4: (F^#)^{(j)}(rho^#) = (-1)^j conj(F^{(j)}(rho))
Fc = lambda s: mp.exp((1 + 2j) * s ** 2 / 7 + 0.3 * s)
Fsh = lambda s: mp.conj(Fc(1 - mp.conj(s)))  # not holomorphic-safe for mp.diff; use series instead
rh = mp.mpc(0.3, 5)
rhs_ = 1 - mp.conj(rh)
# F^#(s) = conj(F(1-conj s)) is holomorphic: F^#(s)=sum conj(c_k)(1-s-conj(rho))^k ... evaluate derivatives via Cauchy
ok = True
for j in range(0, 4):
    dj = contour(lambda s: Fsh(s) / (s - rhs_) ** (j + 1), rhs_, 0.5) * mp.factorial(j)
    ok &= rel(dj, (-1) ** j * mp.conj(mp.diff(Fc, rh, j))) < 1e-12
report("RZ9.4 reflection of jets (-1)^j conj", ok)

# RZ9.9: A_rho^# = (-1)^m A_{rho^#}; at rho_1 (on line, m=1): A^# = -A
Arho = lambda s: F0(s) / (s - rho1)
ok = all(rel(mp.conj(Arho(1 - mp.conj(s))), -Arho(s)) < 1e-15 for s in [mp.mpc(0.2, 3), mp.mpc(1.7, -2)])
report("RZ9.9 A_rho^#=(-1)^m A_{rho^#} at rho_1 (and F0^#=F0)", ok)

print("=" * 70)
print("Synthetic Weil-form identities (RZ10-11, RTT1, RTT7-8) on a #-closed toy divisor")
print("=" * 70)
sh = lambda r: 1 - mp.conj(r)
_base = [(mp.mpc('0.5', '14.1'), 1), (mp.mpc('0.5', '-14.1'), 1), (mp.mpc('0.3', '20'), 2), (mp.mpc('0.3', '-20'), 2)]
Zs = _base[:2] + [(r, m) for r, m in _base[2:]] + [(sh(r), m) for r, m in _base[2:]]  # exactly #-closed
def W_RZ(F, G): return mp.fsum(m * mp.conj(F(sh(r))) * G(r) for r, m in Zs)
def W_RTT(F, G): return mp.fsum(m * F(r) * mp.conj(G(sh(r))) for r, m in Zs)
Fa = lambda s: mp.exp((0.1 + 0.2j) * s ** 2 / 50 + (0.3 - 0.1j) * s)
Gb = lambda s: mp.exp((-0.2 + 0.1j) * s ** 2 / 60 + 0.5j * s + 1)
a = mp.mpf('1.7')
T = lambda a, F: (lambda s: mp.power(a, s) * F(s))
ok = rel(W_RZ(Fa, Gb), mp.conj(W_RZ(Gb, Fa))) < 1e-25
ok &= rel(W_RZ(T(a, Fa), T(a, Gb)), a * W_RZ(Fa, Gb)) < 1e-25                      # RZ11.1
ok &= rel(W_RZ(lambda s: s * Fa(s), Gb), W_RZ(Fa, lambda s: (1 - s) * Gb(s))) < 1e-25   # RZ11.3
ok &= rel(W_RZ(T(a, Fa), Gb), W_RZ(Fa, lambda s: a * mp.power(a, -s) * Gb(s))) < 1e-25  # RZ11.4
lamb = mp.mpc(0.2, 3)
Rv = lambda l, F: (lambda s: F(s) / (l - s))  # values of R_l F on the divisor
ok &= rel(W_RZ(Rv(lamb, Fa), Gb), -W_RZ(Fa, Rv(1 - mp.conj(lamb), Gb))) < 1e-25       # RZ11.5
report("RZ10.1 Hermitian; RZ11.1 similitude; RZ11.3; RZ11.4; RZ11.5 resolvent sign", ok)
ind = lambda z0: (lambda s: mp.mpf(1) if abs(s - z0) < 1e-9 else mp.mpf(0))
x, y = ind(mp.mpc('0.3', '20')), ind(sh(mp.mpc('0.3', '20')))
plus = lambda s: x(s) + y(s); minus = lambda s: x(s) - y(s)
report("RZ10.7 off-line pair: W(x+y)=2m, W(x-y)=-2m (m=2)", W_RZ(plus, plus) == 4 and W_RZ(minus, minus) == -4)
ok = rel(W_RTT(Fa, Gb), W_RZ(Gb, Fa)) < 1e-25
E = lambda F: [F(r) for r, _ in Zs]
idx = {i: [j for j, (r2, _) in enumerate(Zs) if abs(r2 - sh(r)) < 1e-12][0] for i, (r, _) in enumerate(Zs)}
ip = lambda u, v: mp.fsum(Zs[i][1] * u[i] * mp.conj(v[i]) for i in range(len(Zs)))
Jv = lambda v: [v[idx[i]] for i in range(len(v))]
ok &= rel(W_RTT(Fa, Gb), ip(E(Fa), Jv(E(Gb)))) < 1e-25                                  # RTT1.4
ok &= rel(W_RTT(Fa, T(a, Gb)), a * W_RTT(T(1 / a, Fa), Gb)) < 1e-25                      # RTT7.2a
ok &= rel(W_RTT(Fa, lambda s: s * Gb(s)), W_RTT(Fa, Gb) - W_RTT(lambda s: s * Fa(s), Gb)) < 1e-25  # RTT7.2b
ok &= rel(W_RTT(T(a, Fa), Gb), W_RTT(Fa, lambda s: a * mp.power(a, -s) * Gb(s))) < 1e-25  # RTT8.1
report("RTT0.4 convention = RZ form swapped; RTT1.4; RTT7.2 (both); RTT8.1", ok)
Ud = [mp.power(a, 1 - r) for r, _ in Zs]
Dstar = [mp.power(a, mp.conj(r)) for r, _ in Zs]
JDJ = [Dstar[idx[i]] for i in range(len(Zs))]
report("RTT8.3 U_a = J D_a^* J", max(abs(Ud[i] - JDJ[i]) for i in range(len(Zs))) < 1e-25)
diff_on = [abs(Ud[i] - Dstar[i]) > 1e-10 for i in range(len(Zs))]
report("RTT8.3 scope: U_a = D_a^* exactly at on-line zeros (fails at off-line ones)",
       diff_on == [abs(mp.re(r) - 0.5) > 1e-9 for r, _ in Zs])

print("=" * 70)
print("BLOCK 3: CC_STRONG_DUAL_TOPOLOGY_AND_JETS (SDT)")
print("=" * 70)
ok = True
for nn in range(0, 7):
    for xx in mp.linspace(-30, 30, 241):
        wn = mp.exp(nn * xx) + mp.exp(-nn * xx)
        wn1 = mp.exp((nn + 1) * xx) + mp.exp(-(nn + 1) * xx)
        ok &= wn / wn1 <= 2 * mp.exp(-abs(xx)) * (1 + mp.mpf('1e-25'))
report("SDT2.2 w_n/w_{n+1} <= 2 e^{-|x|} (n=0..6, grid)", ok)

random.seed(27)
ok = True
for m in range(1, 8):
    u = [mp.mpc(random.uniform(0.5, 2), random.uniform(-1, 1))] + \
        [mp.mpc(random.uniform(-1, 1), random.uniform(-1, 1)) for _ in range(m)]
    inv = [1 / u[0]]
    for r in range(1, m):
        inv.append(-mp.fsum(u[hh] * inv[r - hh] for hh in range(1, r + 1)) / u[0])
    P = mp.matrix(m, m)
    for i in range(m):
        for j in range(m):
            kk = m - 1 - i - j
            P[i, j] = (-1) ** j * inv[kk] if kk >= 0 else 0
    ok &= rel(mp.det(P), u[0] ** (-m)) < 1e-20
    if m == 3:
        up = lambda t: mp.fsum(u[q] * t ** q for q in range(len(u)))
        for i in range(m):
            for j in range(m):
                rr = contour(lambda t: t ** i * (-t) ** j / (t ** m * up(t)), 0, 0.2)
                ok &= abs(rr - P[i, j]) < 1e-18
report("SDT8.8 residue matrix P_ij=(-1)^j[t^{m-1-i-j}]1/u, det P = u(0)^{-m} (m=1..7)", ok)

# SDT7.4: SSI inverse on raw target F=2F0 returns f0; Taylor data at 0
ok = True
for xx in [mp.mpf(0.5), mp.mpf(1.1)]:
    val = mp.quad(lambda t: C0(2 + 1j * t) * xx ** (-2 - 1j * t), mp.linspace(-120, 120, 25)) / (2 * pi)
    ok &= rel(val, f0(xx)) < 1e-15
report("SDT7.4 f_F with F=2F0 equals f0 (line Re s=2)", ok)
ok = True
tay = mp.taylor(f0, 0, 8)
for r in range(1, 5):
    ok &= rel(tay[2 * r], F0lim(mp.mpf(-2 * r)) / mp.zeta(-2 * r, derivative=1)) < 1e-15
report("SDT7.4 f^{(2r)}(0)/(2r)! = F(-2r)/(2 zeta'(-2r)) for F=2F0, r=1..4", ok)

print("=" * 70)
print("BLOCKS 4-5: FOD / NEA")
print("=" * 70)
vm1 = F0lim(mp.mpf(-1))
report("FOD1.7/NEA1.8 F0(-1)=F_+(0)=pi/24", rel(vm1, pi / 24) < 1e-20, f"{mp.nstr(vm1,15)}")
Fp = lambda l: F0(l - 1)
ok = rel(F0lim(mp.mpf(0)), mp.mpf(1) / 8) < 1e-20 and rel(F0lim(mp.mpf(1)), mp.mpf(1) / 8) < 1e-20
for r in range(1, 4):
    ok &= rel(F0lim(mp.mpf(-2 * r)), F0(mp.mpf(1 + 2 * r))) < 1e-18
report("NEA1.8 F_+(1)=F_+(2)=1/8, F_+(1-2r)=F_+(2+2r)", ok)
ok = all(abs(F0(r - 1)) > mp.mpf('1e-40') and abs(F0(r + 1)) > mp.mpf('1e-40') for r in ZEROS[:6])
report("FOD4.5-4.6 F_+ nonzero at rho, F0 nonzero at rho+1 (rho_1..rho_6)", ok)

# FOD1.4 Theta^{-1}
Th = lambda s: pi ** (-s / 2) * mp.gamma(s / 2) / 4   # Theta of e^{-pi u^2}
ok = True
for uu in [mp.mpf(0.6), mp.mpf(1.4)]:
    val = uu ** (-0.5) / pi * mp.quad(lambda t: Th(0.5 + 1j * t) * uu ** (-1j * t), mp.linspace(-80, 80, 17))
    ok &= rel(val, mp.exp(-pi * uu ** 2)) < 1e-15
report("FOD1.4 Theta^{-1}F(u) = u^{-1/2}/pi int F(1/2+it) u^{-it} dt", ok)

# NEA7.7 log-modulus of dilation characters
a0 = mp.mpf(3)
vals = [2 * mp.log(abs(mp.power(a0, r + 1))) / mp.log(a0) for r in ZEROS[:5]]
report("NEA7.7 2 log|a^{rho+1}|/log a = 2 Re rho + 2 (=3 for computed zeros)", all(abs(v - 3) < 1e-20 for v in vals))

# FOD/NEA algebra in a toy polynomial model (M=C[s], two coprime divisors)
try:
    import sympy as sp
    S = sp.symbols('s')
    p = (S - 2) ** 2 * (S + 1)        # toy 'original' divisor
    pp = (S - 3) ** 2 * S             # toy 'normal' divisor
    sa, ta, hh = sp.gcdex(p, pp, S)   # sa*p + ta*pp = 1
    one_minus_c = sp.expand(sa * p)   # 1-c in (p)
    c = sp.expand(ta * pp)            # c in (pp)
    ok = hh == 1 and sp.expand(c + one_minus_c - 1) == 0
    f, gg = S ** 3 + 2, 5 * S - 7
    mix = sp.expand(c * f + (1 - c) * gg)
    ok &= sp.rem(mix - f, p, S) == 0 and sp.rem(mix - gg, pp, S) == 0             # FOD2.2
    i_, b_ = sp.expand(p * (S + 4)), sp.expand(pp * (S ** 2 - 1))
    kk = sp.expand(-c * i_ + (1 - c) * b_)
    ok &= sp.rem(kk, p, S) == 0 and sp.rem(kk, pp, S) == 0                           # FOD3.2 k in K
    report("FOD2.2/FOD3.2/FOD5.3 CRT identities in toy model C[s]", ok)
except Exception as e:
    report("FOD toy algebra (sympy)", False, str(e))

print("=" * 70)
npass = sum(1 for _, o in RES if o)
print(f"SUMMARY: {npass}/{len(RES)} PASS")
