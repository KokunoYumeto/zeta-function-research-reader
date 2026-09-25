#!/usr/bin/env python3
# Checks for 33_ (first-pass audit of BML/BMR/BMRL, in the programme's working folder
# quantum_tau_programme_bridge_20260924/next_edition_after_719). Written by a Claude subagent of claude-ab
# (Opus 5.5, max effort), 25 September 2026, and copied here unchanged apart from this header.
"""checks33a.py -- audit checks for BML0-11 (FULL_BOUNDARY_MONODROMY_DIFFERENCE_LIFT.md),
BMR0-13 (its review) and BMRL0-6 (BOUNDARY_LIFT_LOCAL_COUNTING_INDEPENDENT_REVIEW.md).

Each item prints PASS/FAIL, a one-line description and an error measure.
 * Exact (sympy) arithmetic where the claim is algebraic.
 * mpmath (50 digits) otherwise.  Quantities carrying the Gaussian e^{t(1-rho)^2} at zeta zeros are
   compared by relative error (i.e. relative to the Gaussian-weighted size of the quantity).
 * Operator / function identities are algebraic in the zero coordinates, so they are tested on a
   synthetic divisor closed under rho -> conj(rho) and rho -> 1-rho, with off-line quadruples and
   multiplicities (all computed zeta zeros are on the line), and also at the actual zero rho_1.
 * The polylogarithm side is computed independently with mpmath.polylog (principal branch); the
   regular remainder is computed from the zeta series A_s(u) = sum_k zeta(s-k)(-u)^k/k! and, where
   stated, from the defining integral BML1.5.
Controls ("wrong sign" variants) are reported in brackets and must be large.
"""
import random
import mpmath as mp
import sympy as sp

mp.mp.dps = 50
random.seed(33)
RESULTS = []


def report(tag, desc, err, tol, extra=""):
    ok = bool(err <= tol)
    RESULTS.append(ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {tag}: {desc} | err={mp.nstr(err, 3)} (tol {mp.nstr(tol, 2)})"
          f"{(' ' + extra) if extra else ''}")


def relerr(a, b):
    return abs(a - b) / max(abs(b), mp.mpf(10) ** (-300))


# ----------------------------------------------------------------------------------- basic objects
R_PAR = mp.mpf(2)          # r > 1
T_PAR = mp.mpf('0.05')     # Gaussian parameter t > 0
TWO_PI_I = 2j * mp.pi


def d_r(rho, r=R_PAR):
    s, g = mp.re(rho), mp.im(rho)
    return mp.expj(-g * mp.log(r)) * (mp.power(r, s) - mp.power(r, 1 - s))


def gauss(rho, t=T_PAR):
    return mp.exp(t * (1 - rho) ** 2)


def lam(rho):
    return mp.exp(-TWO_PI_I * rho)          # BML2.1


def bcoef(rho):
    return 1 / (lam(rho) - 1)


def c_n(n, u):                               # BML7.1, finite sum form
    return sum(mp.exp(a * u / n) for a in range(n)) / n


_ZC = {}


def zeta_shifts(s, K):
    key = (mp.re(s), mp.im(s), K)
    if key not in _ZC:
        _ZC[key] = [mp.zeta(s - k) for k in range(K)]
    return _ZC[key]


def A_ser(s, u, du=0, K=170):
    """(d/du)^du of A_s(u) = sum_k zeta(s-k)(-u)^k/k!  (|u|<2 pi)."""
    zl = zeta_shifts(s, K)
    tot = mp.mpc(0)
    for k in range(du, K):
        tot += zl[k] * (-1) ** k * u ** (k - du) / mp.factorial(k - du)
    return tot


def Bv(v, der=0):
    """B(v)=1/(e^v-1)-1/v and first two derivatives (closed form; used only for |v|>=0.3)."""
    E = mp.exp(v)
    if der == 0:
        return 1 / (E - 1) - 1 / v
    if der == 1:
        return -E / (E - 1) ** 2 + 1 / v ** 2
    if der == 2:
        return E * (E + 1) / (E - 1) ** 3 - 2 / v ** 3
    if der == 3:
        return -E * (E * E + 4 * E + 1) / (E - 1) ** 4 + 6 / v ** 4
    raise ValueError


def Bv_small(v, der=0, N=80):
    """Bernoulli series of B^{(der)} for |v| < 2 pi."""
    tot = mp.mpc(0)
    for n in range(1 + der, N):
        Bn = mp.bernoulli(n)
        if Bn == 0:
            continue
        tot += Bn / mp.factorial(n) * mp.ff(n - 1, der) * v ** (n - 1 - der)
    return tot


def A_int(s, u, du=0, L0=30, X=mp.mpf(200)):
    """Defining integral BML1.5 (and its u-derivatives):
       Gamma(s) d^du A_s(u) = int_0^inf x^{s-1} B^{(du)}(x+u) dx."""
    eps = mp.exp(-L0)
    Bf = (lambda v, d: Bv_small(v, d)) if abs(u) < 0.3 else (lambda v, d: Bv(v, d))
    head = sum(Bf(u, du + k) / mp.factorial(k) * eps ** (s + k) / (s + k) for k in range(3))
    ya, yb = -L0, mp.log(X)
    N = int(mp.ceil(yb - ya))
    pts = [ya + (yb - ya) * j / N for j in range(N + 1)]

    def integrand(y):
        x = mp.exp(y)
        v = x + u
        Bval = Bv_small(v, du) if abs(v) < 0.3 else Bv(v, du)
        return mp.exp(s * y) * Bval
    mid = mp.quad(integrand, pts)
    # tail: B^{(du)}(v) = O(e^{-v}) + (-1)^{du+1} du!/v^{du+1}; expand 1/(x+u)^{p} in powers of u/x
    p = du + 1
    tail = mp.mpc(0)
    for k in range(80):
        coeff = (-1) ** k * mp.binomial(p + k - 1, k) * u ** k
        tail += coeff * X ** (s - p - k) / (p + k - s)
    tail *= (-1) ** (du + 1) * mp.factorial(du)
    return (head + mid + tail) / mp.gamma(s)


def K_poly(s, z):
    """K_s(z) = -(1-z)/(s z) Li_{s-1}(z), principal branch (HBW0.3 / BMR1.3)."""
    return -(1 - z) / (s * z) * mp.polylog(s - 1, z)


# points on the universal cover: p = (|u|, arg u); positive winding adds 2 pi to arg
def uval(p):
    return p[0] * mp.expj(p[1])


def upow(p, a):
    return mp.exp(a * (mp.log(p[0]) + 1j * p[1]))


def Lf(p):                                   # L = log u /(2 pi i)
    return (mp.log(p[0]) + 1j * p[1]) / TWO_PI_I


def rot(p, k=1):
    return (p[0], p[1] + 2 * mp.pi * k)


def scale(p, n):                             # canonical lift of u -> u/n (BMRL1)
    return (p[0] / n, p[1])


# synthetic divisor: closed under conj and rho -> 1-rho (so rho# = 1-conj(rho) too), multiplicities
SYN = [(mp.mpc('0.3', '5'), 1), (mp.mpc('0.3', '-5'), 1), (mp.mpc('0.7', '5'), 1), (mp.mpc('0.7', '-5'), 1),
       (mp.mpc('0.2', '8.5'), 2), (mp.mpc('0.2', '-8.5'), 2), (mp.mpc('0.8', '8.5'), 2), (mp.mpc('0.8', '-8.5'), 2),
       (mp.mpc('0.5', '3'), 1), (mp.mpc('0.5', '-3'), 1), (mp.mpc('0.5', '11.2'), 1), (mp.mpc('0.5', '-11.2'), 1)]
OFF = [i for i, (rho, m) in enumerate(SYN) if mp.re(rho) != mp.mpf('0.5')]


def rand_y(offline_only=True):
    y = []
    for i, (rho, m) in enumerate(SYN):
        if offline_only and i not in OFF:
            y.append(mp.mpc(0))
        else:
            y.append(mp.mpc(random.uniform(-1, 1), random.uniform(-1, 1)))
    return y


def By(y):
    return [bcoef(rho) * y[i] for i, (rho, m) in enumerate(SYN)]


def Tn(y, n):
    return [mp.power(n, rho) * y[i] for i, (rho, m) in enumerate(SYN)]


def a_coef(rho, yv, t=T_PAR):                 # BML1.4
    return -d_r(rho) * yv * gauss(rho, t) * mp.gamma(1 + rho) / (1 - rho)


def S_fun(y, p, t=T_PAR):                     # BML1.4 singular sum on the cover
    u = uval(p)
    return (mp.exp(u) - 1) * sum(m * a_coef(rho, y[i], t) * upow(p, -1 - rho) for i, (rho, m) in enumerate(SYN))


def R_fun(y, u, t=T_PAR):                     # BML1.5 regular remainder (single valued)
    tot = mp.mpc(0)
    for i, (rho, m) in enumerate(SYN):
        if y[i] == 0 or d_r(rho) == 0:
            continue
        tot += m * d_r(rho) * y[i] * gauss(rho, t) * (mp.exp(u) - 1) / (1 - rho) * A_ser(1 - rho, u, 1)
    return tot


def f_dec(y, p):                              # BML1.3 right side
    return S_fun(y, p) + R_fun(y, uval(p))


def f_poly(y, p):                             # BML1.3 left side, principal sheet (-pi<arg<pi)
    z = mp.exp(-uval(p))
    return sum(m * d_r(rho) * y[i] * gauss(rho) * K_poly(1 - rho, z) for i, (rho, m) in enumerate(SYN)
               if y[i] != 0)


def K_fun(y, p):                              # BML6.1: K y = f(By) + L R(y)
    return f_dec(By(y), p) + Lf(p) * R_fun(y, uval(p))


def Q_n(y, n, u):                             # BML7.3
    return R_fun(Tn(y, n), u) - c_n(n, u) * R_fun(y, u / n)


rho1 = mp.zetazero(1)

# ==========================================================================================
# C01  BML1.3-1.5: f = S + R on the principal sheet (polylog side independent), plus A_s series
#      = defining integral BML1.5
worst = mp.mpf(0)
for rho in [rho1, mp.mpc('0.3', '5'), mp.mpc('0.8', '-8.5')]:
    s = 1 - rho
    for p in [(mp.mpf('0.4'), mp.mpf(0)), (mp.mpf('0.4'), mp.mpf('1.2')), (mp.mpf('0.4'), mp.mpf('2.5')),
              (mp.mpf('0.9'), mp.mpf('-2.0')), (mp.mpf('1.3'), mp.mpf('3.0'))]:
        u = uval(p)
        lhs = gauss(rho) * K_poly(s, mp.exp(-u))
        sing = -gauss(rho) * mp.gamma(1 + rho) / (1 - rho) * (mp.exp(u) - 1) * upow(p, -1 - rho)
        reg = gauss(rho) * (mp.exp(u) - 1) / (1 - rho) * A_ser(s, u, 1)
        worst = max(worst, relerr(sing + reg, lhs))
eint = mp.mpf(0)
for (s, u) in [(1 - rho1, mp.mpf('0.7')), (1 - rho1, mp.mpc('-0.5', '1.5')), (mp.mpc('0.7', '-5'), mp.mpc('0.2', '-0.9'))]:
    eint = max(eint, relerr(A_int(s, u, 0), A_ser(s, u, 0)))
    eint = max(eint, relerr(A_int(s, u, 1), A_ser(s, u, 1)))
report("C01", "BML1.3-1.5: e^{t(1-rho)^2}K_{1-rho}(e^{-u}) = a-term (e^u-1)u^{-1-rho} + R-term (rho_1, 2 synthetic; "
       "5 points incl. Re u<0); A_s, dA_s: integral BML1.5 = zeta series", max(worst, eint), mp.mpf(10) ** -30,
       f"[decomposition {mp.nstr(worst, 3)}, integral-vs-series {mp.nstr(eint, 3)}]")

# ==========================================================================================
# C02  BML2.1: positive winding multiplies the rho-term by lambda = e^{-2 pi i rho} (not e^{+2 pi i rho});
#      tested on the principal-branch jump of the actual function across the negative u-axis
mp.mp.dps = 60
worst = mp.mpf(0); ctrl = mp.mpf(10) ** 9
for rho in [rho1, mp.mpc('0.3', '5'), mp.mpc('0.8', '-8.5')]:
    s = 1 - rho
    for r0 in [mp.mpf('0.8'), mp.mpf('2.1')]:
        epsl = mp.mpf(10) ** -45
        x = mp.exp(r0)
        F_plus = K_poly(s, x * mp.expj(-epsl))      # u = r0 e^{+i pi}  (approached from Im u > 0)
        F_minus = K_poly(s, x * mp.expj(+epsl))     # u = r0 e^{-i pi}
        jump = F_plus - F_minus                     # = (M - I)F at the point with arg -pi
        p = (r0, -mp.pi)
        singm = -mp.gamma(1 + rho) / (1 - rho) * (mp.exp(uval(p)) - 1) * upow(p, -1 - rho)
        worst = max(worst, relerr((lam(rho) - 1) * singm, jump))
        ctrl = min(ctrl, relerr((mp.exp(TWO_PI_I * rho) - 1) * singm, jump))
mp.mp.dps = 50
report("C02", "BML2.1 sign: (M-I)K_{1-rho}(e^{-u}) = (e^{-2pi i rho}-1)x(singular term), R has no jump "
       "(jump of principal polylog across u<0; rho_1 + synthetic)", worst, mp.mpf(10) ** -35,
       f"[control lambda=e^{{+2pi i rho}}: min rel.err {mp.nstr(ctrl, 3)}]")

# ==========================================================================================
# C03  BML2.2: the two half-plane bounds; the finite set |Im rho|<=1 is empty (so C_B = 1/(1-e^{-2pi}));
#      sharper: |b_rho + 1_{gamma<0}| <= 1/(e^{2pi|gamma|}-1) <= 1/(e^{2 pi gamma_1}-1) ~ 2.7e-39
#      (b+1 is evaluated stably as lam/(lam-1); comparisons are relative)
viol = mp.mpf(0)
for sg in [mp.mpf(k) / 20 for k in range(1, 20)]:
    for gm in [1, 1.5, 2, 3.7, 14.13, 50]:
        gm = mp.mpf(gm)
        viol = max(viol, 1 - abs(lam(mp.mpc(sg, gm)) - 1) / (mp.e ** (2 * mp.pi) - 1))
        viol = max(viol, 1 - abs(lam(mp.mpc(sg, -gm)) - 1) / (1 - mp.e ** (-2 * mp.pi)))
nz_below = mp.nzeros(14)
g1 = mp.im(rho1)
bound_sharp = 1 / (mp.exp(2 * mp.pi * g1) - 1)
CB = 1 / (1 - mp.exp(-2 * mp.pi))
maxdev = mp.mpf(0); maxb = mp.mpf(0)
for k in range(1, 41):
    rk = mp.zetazero(k)
    for rr in [rk, mp.conj(rk)]:
        l = lam(rr)
        dev = abs(l / (l - 1)) if mp.im(rr) < 0 else abs(1 / (l - 1))
        maxdev = max(maxdev, dev)
        maxb = max(maxb, abs(bcoef(rr)))
        viol = max(viol, dev * (mp.exp(2 * mp.pi * abs(mp.im(rr))) - 1) - 1)
viol = max(viol, maxb / CB - 1, maxdev / bound_sharp - 1)
report("C03", "BML2.2: |lam-1|>=e^{2pi}-1 (gamma>=1), >=1-e^{-2pi} (gamma<=-1); no zeros with |gamma|<=14 "
       "(so C_B=1/(1-e^{-2pi})); ||B+P_-|| <= 1/(e^{2pi gamma_1}-1) on zeros 1..40 (relative violations)",
       max(viol, mp.mpf(nz_below)), mp.mpf(10) ** -40,
       f"[N(14)={nz_below}; C_B={mp.nstr(CB, 8)}; max|b| over zeros 1..40 = {mp.nstr(maxb, 8)} (sup over line zeros is 1, not attained); max|b+1_(g<0)|={mp.nstr(maxdev, 4)} "
       f"vs 1/(e^(2pi g1)-1)={mp.nstr(bound_sharp, 4)}]")

# ==========================================================================================
# C04  BML3.1 / BML3.5 / HBW9 at coefficient level (exact) and the norm bound of BML3.5
rs, t1, t2, tt, tp, ys = sp.symbols('rho t1 t2 t tp y')
kk, ll = sp.symbols('k l', integer=True)
dd = sp.Symbol('d')


def a_sym(t, y):
    return -dd * y * sp.exp(t * (1 - rs) ** 2) * sp.gamma(1 + rs) / (1 - rs)


G21 = sp.exp((t2 - t1) * (1 - rs) ** 2)
e1 = sp.simplify(sp.powsimp(a_sym(t1, G21 * ys) - a_sym(t2, ys), combine='exp'))
V = sp.exp(-2 * sp.pi * sp.I * kk * rs) * sp.exp((tt - tp) * (1 - rs) ** 2)
e2 = sp.simplify(sp.powsimp(sp.exp(-2 * sp.pi * sp.I * kk * rs) * a_sym(tt, ys) - a_sym(tp, V * ys), combine='exp'))
t3 = sp.Symbol('t3')
V1 = sp.exp(-2 * sp.pi * sp.I * kk * rs) * sp.exp((tt - tp) * (1 - rs) ** 2)
V2 = sp.exp(-2 * sp.pi * sp.I * ll * rs) * sp.exp((tp - t3) * (1 - rs) ** 2)
V3 = sp.exp(-2 * sp.pi * sp.I * (kk + ll) * rs) * sp.exp((tt - t3) * (1 - rs) ** 2)
e3 = sp.simplify(sp.powsimp(sp.expand(V2 * V1 - V3), combine='exp'))
exact_ok = (e1 == 0 and e2 == 0 and e3 == 0)
excess = -mp.inf
for k in range(-3, 4):
    for de in [mp.mpf('0.05'), mp.mpf('0.3'), mp.mpf(1), mp.mpf(2)]:
        for sg in [mp.mpf(j) / 10 for j in range(0, 11)]:
            for gm in [mp.mpf(j) / 4 for j in range(-240, 241)]:
                lg = 2 * mp.pi * k * gm + de * ((1 - sg) ** 2 - gm ** 2)
                excess = max(excess, lg - (de + mp.pi ** 2 * k * k / de))
report("C04", "BML3.1 a_{t1}(G21 y)=a_{t2}(y); BML3.5 lam^k a_t(y)=a_{t'}(V_k y); V_l V_k=V_{k+l} (exact); "
       "log|diag V_k| <= delta+pi^2k^2/delta (grid, k=-3..3)", (0 if exact_ok else 1) + max(excess, 0), 0,
       f"[exact: {e1 == 0},{e2 == 0},{e3 == 0}; max excess {mp.nstr(excess, 3)}]")

# ==========================================================================================
# C05  BML4.2-4.3, BML5, BML8.2-8.3 on the synthetic divisor, as functions on the cover
worst = mp.mpf(0); ctrl = mp.mpf(10) ** 9
for trial in range(3):
    y = rand_y()
    for p in [(mp.mpf('0.6'), mp.mpf('0.9')), (mp.mpf('1.1'), mp.mpf('-2.6') + 4 * mp.pi)]:
        lhs = S_fun(By(y), rot(p)) - S_fun(By(y), p)          # (M-I) S(By)
        worst = max(worst, relerr(lhs, S_fun(y, p)))
        yb = [y[i] / (mp.exp(TWO_PI_I * rho) - 1) for i, (rho, m) in enumerate(SYN)]   # wrong-sign inverse
        ctrl = min(ctrl, relerr(S_fun(yb, rot(p)) - S_fun(yb, p), S_fun(y, p)))
# finite-model operator algebra: d = diag(lam-1) on H_O, h = diag(b); dh = hd = I; ker d = 0 (Hom = 0)
lams = [lam(SYN[i][0]) for i in OFF]
dh = max(abs((l - 1) * (1 / (l - 1)) - 1) for l in lams)
minsing = min(abs(l - 1) for l in lams)
worst = max(worst, dh)
report("C05", "BML4.2-4.3/BML5/BML8.3: (M-I)S(By)=S(y) on two sheets; dh+hd=I; min|lam-1|>0 so Hom_M(triv,D)=0 "
       "(synthetic divisor, random y)", worst, mp.mpf(10) ** -40,
       f"[min|lam-1| = {mp.nstr(minsing, 5)}; control b=1/(e^{{+2pi i rho}}-1): min rel.err {mp.nstr(ctrl, 3)}]")

# ==========================================================================================
# C06  BML6.2: (M-I)K y = f(y) as whole functions; f(y), f(By) at the base point from the polylog
worst = mp.mpf(0); ctrl = mp.mpf(10) ** 9
for trial in range(2):
    y = rand_y()
    for p in [(mp.mpf('0.5'), mp.mpf('0.4')), (mp.mpf('0.8'), mp.mpf('-2.1'))]:
        u = uval(p)
        Ry = R_fun(y, u)
        K_rot = f_dec(By(y), rot(p)) + Lf(rot(p)) * Ry
        K_base = f_poly(By(y), p) + Lf(p) * Ry
        target = f_poly(y, p)
        worst = max(worst, relerr(K_rot - K_base, target))
        ctrl = min(ctrl, relerr(f_dec(By(y), rot(p)) - f_poly(By(y), p), target))   # without L R term
report("C06", "BML6.2: (M-I)[f(By)+L R(y)] = f(y) pointwise (f from polylog; synthetic divisor, 2 base points)",
       worst, mp.mpf(10) ** -35, f"[control without the L R(y) term: min rel.err {mp.nstr(ctrl, 3)}]")

# ==========================================================================================
# C07  BML7.1 closed form, c_n(0)=1; BMR8.2 / BMRL1.7 c_m(u)c_n(u/m)=c_{mn}(u)  (exact)
Y = sp.Symbol('Y')
ok = True
for n in range(1, 9):
    ok &= sp.expand(sum(Y ** a for a in range(n)) * (Y - 1) - (Y ** n - 1)) == 0
    ok &= sp.Rational(sum(1 for a in range(n)), n) == 1
Xs = sp.Symbol('X')
for m in range(1, 7):
    for n in range(1, 7):
        cm = sp.Rational(1, m) * sum(Xs ** (a * n) for a in range(m))       # c_m(u), X = e^{u/(mn)}
        cn = sp.Rational(1, n) * sum(Xs ** b for b in range(n))             # c_n(u/m)
        cmn = sp.Rational(1, m * n) * sum(Xs ** c for c in range(m * n))    # c_{mn}(u)
        ok &= sp.expand(cm * cn - cmn) == 0
report("C07", "BML7.1: (1/n)sum e^{au/n} = (e^u-1)/(n(e^{u/n}-1)), c_n(0)=1; BMR8.2: c_m(u)c_n(u/m)=c_mn(u), "
       "m,n<=6 (exact)", 0 if ok else 1, 0)

# ==========================================================================================
# C08  BML7.2: C_n S(y) = S(T_n y): exact single term, and numerically on a non-principal sheet
uu, nn = sp.symbols('u n', positive=True)
single = (sp.exp(uu) - 1) / (nn * (sp.exp(uu / nn) - 1)) * (sp.exp(uu / nn) - 1) * (uu / nn) ** (-1 - rs) \
    - nn ** rs * (sp.exp(uu) - 1) * uu ** (-1 - rs)
ex_ok = sp.simplify(sp.powsimp(sp.expand_power_base(sp.cancel(single), force=True), force=True)) == 0
worst = mp.mpf(0)
y = rand_y()
for n in [2, 3, 7]:
    for p in [(mp.mpf('0.7'), mp.mpf('5.0')), (mp.mpf('1.4'), mp.mpf('-3.3'))]:
        lhs = c_n(n, uval(p)) * S_fun(y, scale(p, n))
        worst = max(worst, relerr(lhs, S_fun(Tn(y, n), p)))
report("C08", "BML7.2: c_n(u)(e^{u/n}-1)(u/n)^{-1-rho} = n^rho(e^u-1)u^{-1-rho} (exact); C_nS(y)=S(T_n y) "
       "on sheets arg 5.0, -3.3", (0 if ex_ok else 1) + worst, mp.mpf(10) ** -40, f"[exact: {ex_ok}]")

# ==========================================================================================
# C09  BML7.3-7.4 (BMR8.3): Q_n(e_rho) is exactly the sum of the non-identity sheets of HBW4.3 applied to
#      the actual receiver function; and W_n^* K_s = n^{1-s} K_s (all sheets)
worst = mp.mpf(0); sizes = []
u0 = mp.mpf('0.5')
for rho in [rho1, mp.mpc('0.3', '5')]:
    s = 1 - rho
    kap = d_r(rho) if mp.re(rho) != mp.mpf('0.5') else mp.mpf(1)   # d_r(rho_1)=0: test K_{1-rho} itself
    F = lambda z: kap * gauss(rho) * K_poly(s, z)                  # Xi e_rho (m=1)
    Rr = lambda u: kap * gauss(rho) * (mp.exp(u) - 1) / (1 - rho) * A_ser(s, u, 1)
    for n in [2, 3, 5]:
        tot = mp.mpc(0); other = mp.mpc(0)
        for j in range(n):
            om = mp.expj(2 * mp.pi * j / n)
            sheet = sum(om ** (-a) * mp.exp(a * u0 / n) for a in range(n)) / n * F(om * mp.exp(-u0 / n))
            tot += sheet
            if j != 0:
                other += sheet
        worst = max(worst, relerr(tot, mp.power(n, rho) * F(mp.exp(-u0))))
        Qn = mp.power(n, rho) * Rr(u0) - c_n(n, u0) * Rr(u0 / n)
        worst = max(worst, relerr(Qn, other))
        sizes.append(abs(Qn) / abs(kap * gauss(rho)))
report("C09", "BML7.3-7.4/BMR8.3: Q_n(e_rho)=R(T_n e_rho)-C_nR(e_rho) = sum of the n-1 non-identity sheets of "
       "W_n^*(Xi e_rho); W_n^*K_s=n^{1-s}K_s (rho_1, synthetic; n=2,3,5)", worst, mp.mpf(10) ** -35,
       f"[|Q_n|/|coefficient x Gaussian| in {mp.nstr(min(sizes), 3)}..{mp.nstr(max(sizes), 3)}: nonzero; "
       f"at rho_1 coefficient 1 used since d_r(rho_1)=0]")

# ==========================================================================================
# C10  BML7.5 / BMR8.4 / BMRL3.5 with all signs, on two sheets
worst = mp.mpf(0); ctrl = mp.mpf(10) ** 9
y = rand_y()
for n in [2, 3]:
    for p in [(mp.mpf('0.9'), mp.mpf('2.2')), (mp.mpf('0.9'), mp.mpf('2.2') + 2 * mp.pi)]:
        u = uval(p)
        lhs = c_n(n, u) * K_fun(y, scale(p, n)) - K_fun(Tn(y, n), p)
        base = -Q_n(By(y), n, u) - Lf(p) * Q_n(y, n, u)
        logt = mp.log(n) / TWO_PI_I * c_n(n, u) * R_fun(y, u / n)
        worst = max(worst, relerr(base - logt, lhs))
        ctrl = min(ctrl, relerr(base + logt, lhs))
report("C10", "BML7.5: C_nKy-K(T_ny) = -Q_n(By)-L Q_n(y)-(log n/2pi i)C_nR(y) (n=2,3; arg 2.2 and 2.2+2pi)",
       worst, mp.mpf(10) ** -35, f"[control with +log n term: min rel.err {mp.nstr(ctrl, 3)}]")

# ==========================================================================================
# C11  BMR8.5 / BMRL3.6 cocycle Q_mn = Q_m T_n + C_m Q_n = Q_n T_m + C_n Q_m
worst = mp.mpf(0)
y = rand_y()
u = mp.mpc('0.7', '0.3')
for (m, n) in [(2, 3), (2, 2), (4, 3)]:
    lhs = Q_n(y, m * n, u)
    r1 = Q_n(Tn(y, n), m, u) + c_n(m, u) * Q_n(y, n, u / m)
    r2 = Q_n(Tn(y, m), n, u) + c_n(n, u) * Q_n(y, m, u / n)
    worst = max(worst, relerr(r1, lhs), relerr(r2, lhs))
report("C11", "BMR8.5/BMRL3.6: Q_mn(y) = Q_m(T_n y)+C_m Q_n(y) = Q_n(T_m y)+C_n Q_m(y) ((m,n)=(2,3),(2,2),(4,3))",
       worst, mp.mpf(10) ** -35)

# ==========================================================================================
# C12  BML10 / BMR6: lam b = 1 + b (exact); graph-norm bound BML10.3; forward bound sqrt 2; normality
lb = sp.Symbol('lambda_')
ex_ok = sp.simplify(lb * (1 / (lb - 1)) - (1 + 1 / (lb - 1))) == 0
BIG = SYN + [(mp.mpc('0.35', '30'), 1), (mp.mpc('0.35', '-30'), 1), (mp.mpc('0.65', '30'), 1), (mp.mpc('0.65', '-30'), 1),
             (mp.mpc('0.1', '60'), 3), (mp.mpc('0.1', '-60'), 3), (mp.mpc('0.9', '60'), 3), (mp.mpc('0.9', '-60'), 3)]
offB = [(rho, m) for (rho, m) in BIG if mp.re(rho) != mp.mpf('0.5')]
CBs = max(abs(bcoef(rho)) for rho, m in offB)
ratio = -mp.inf
normerr = mp.mpf(0)
for trial in range(50):
    yv = [mp.mpc(random.gauss(0, 1), random.gauss(0, 1)) * mp.exp(-2 * mp.pi * max(mp.im(rho), 0) * random.random())
          for rho, m in offB]
    nrm = lambda v: mp.sqrt(sum(m * abs(v[i]) ** 2 for i, (rho, m) in enumerate(offB)))
    byv = [bcoef(rho) * yv[i] for i, (rho, m) in enumerate(offB)]
    lbyv = [lam(rho) * byv[i] for i, (rho, m) in enumerate(offB)]
    ratio = max(ratio, (nrm(byv) ** 2 + nrm(lbyv) ** 2) / ((CBs ** 2 + (1 + CBs) ** 2) * nrm(yv) ** 2))
    xv = yv
    Mx = [lam(rho) * xv[i] for i, (rho, m) in enumerate(offB)]
    Msx = [mp.conj(lam(rho)) * xv[i] for i, (rho, m) in enumerate(offB)]
    dmx = [(lam(rho) - 1) * xv[i] for i, (rho, m) in enumerate(offB)]
    ratio = max(ratio, nrm(dmx) ** 2 / (2 * (nrm(xv) ** 2 + nrm(Mx) ** 2)))
    normerr = max(normerr, abs(nrm(Mx) - nrm(Msx)) / nrm(Mx))
    ratio = max(ratio, max(abs(lam(rho)) ** 2 / (1 + abs(lam(rho)) ** 4) for rho, m in offB))
report("C12", "BML10.2-10.3/BMR6: lam b=1+b (exact); ||By||^2+||lam By||^2 <= (C_B^2+(1+C_B)^2)||y||^2; "
       "||(M-I)x|| <= sqrt2 ||x||_graph; ||Mx||=||M*x||; |lam|^2<=1+|lam|^4 (|lam| up to e^377)",
       (0 if ex_ok else 1) + max(ratio - 1, 0) + normerr, mp.mpf(10) ** -40,
       f"[max bound ratio {mp.nstr(ratio, 6)} (<=1); normality rel.err {mp.nstr(normerr, 3)}; exact {ex_ok}]")

# ==========================================================================================
# C13  BML11.1-11.2, 11.6 (exact in the symbol L) and one instance with the actual remainder;
#      truncation: iota(A) = (M-I)[(L^2-L)A/2] is a coboundary one log-level up; (M-I)^k L^k = k!
Ls, An, lg = sp.symbols('L A a_n')
ok = sp.expand(((Ls + 1) * An - Ls * An) - An) == 0                                  # (M-I)(LA)=A
ok &= sp.expand(((Ls + 1) ** 2 - (Ls + 1) - Ls ** 2 + Ls) / 2 - Ls) == 0             # (M-I)(L^2-L)/2 = L
for k in range(1, 7):
    fd = sum((-1) ** (k - i) * sp.binomial(k, i) * (Ls + i) ** k for i in range(k + 1))
    ok &= sp.expand(fd - sp.factorial(k)) == 0                                       # (M-I)^k L^k = k!
ok &= sp.expand((Ls - lg) * An - (Ls * An - lg * An)) == 0                            # C_n(LA)=(L-a_n)C_nA
y = rand_y()
p = (mp.mpf('0.6'), mp.mpf('1.0'))
u = uval(p)
Ay = R_fun(y, u)
num = relerr((Lf(rot(p)) - Lf(p)) * Ay, Ay)
p2 = scale(p, 3)
num = max(num, relerr(Lf(p2), Lf(p) - mp.log(3) / TWO_PI_I))
report("C13", "BML11.2 (M-I)(LA)=A; BML11.6 L(u/n)=L-log n/(2pi i); (M-I)[(L^2-L)A/2]=LA; (M-I)^k L^k=k! "
       "(exact, k<=6); instance with A=R(y)", (0 if ok else 1) + num, mp.mpf(10) ** -45,
       f"[exact {ok}; |R(y)(u)| = {mp.nstr(abs(Ay), 4)} (nonzero)]")

# ==========================================================================================
# C14  Negative-result input: dA_s(0) = -zeta(s-1) (from the integral BML1.5); zeta(-rho) != 0
#      (functional equation); Q_n(e_rho)'(0) = (n^rho - 1/n) R'(0) with R'(0) = -d e^{t(1-rho)^2} zeta(-rho)/(1-rho)
worst = mp.mpf(0); mins = []
for rho in [rho1, mp.mpc('0.3', '5'), mp.mpc('0.2', '-8.5')]:
    s = 1 - rho
    worst = max(worst, relerr(A_int(s, mp.mpf(0), 1), -mp.zeta(s - 1)))
    zr = mp.zeta(-rho)
    fe = mp.power(2, -rho) * mp.power(mp.pi, -rho - 1) * mp.sin(-mp.pi * rho / 2) * mp.gamma(1 + rho) * mp.zeta(1 + rho)
    worst = max(worst, relerr(fe, zr))
    mins.append(abs(zr))
    kap = d_r(rho) if mp.re(rho) != mp.mpf('0.5') else mp.mpf(1)
    Rr = lambda u: kap * gauss(rho) * (mp.exp(u) - 1) / (1 - rho) * A_ser(s, u, 1)
    Rp0 = -kap * gauss(rho) * zr / (1 - rho)
    worst = max(worst, relerr(mp.diff(Rr, 0), Rp0))
    for n in [2, 3]:
        Qf = lambda u: mp.power(n, rho) * Rr(u) - c_n(n, u) * Rr(u / n)
        worst = max(worst, relerr(mp.diff(Qf, 0), (mp.power(n, rho) - mp.mpf(1) / n) * Rp0))
report("C14", "dA_s(0)=-zeta(s-1) (integral BML1.5); zeta(-rho)=2^-rho pi^(-rho-1) sin(-pi rho/2)Gamma(1+rho)zeta(1+rho)!=0; "
       "Q_n(e_rho)'(0)=(n^rho-1/n)R'(0)", worst, mp.mpf(10) ** -30,
       f"[min |zeta(-rho)| = {mp.nstr(min(mins), 4)}; so R(e_rho), Q_n(e_rho) != 0 at every off-line rho]")

# ==========================================================================================
# C15  RH-equivalent-by-construction readings: lambda_rho < 0 iff Re rho = 1/2; d_r(rho)=0 iff Re rho=1/2;
#      |lambda_rho| = e^{2 pi gamma} (hyperbolic winding), at zeros 1..25 and synthetic off-line points
worst = mp.mpf(0); offdev = []
for k in range(1, 26):
    rk = mp.zetazero(k)
    for rr in [rk, mp.conj(rk)]:
        l = lam(rr)
        worst = max(worst, abs(l / abs(l) + 1), abs(d_r(rr)))
        worst = max(worst, relerr(abs(l), mp.exp(2 * mp.pi * mp.im(rr))))
for rho, m in SYN:
    l = lam(rho)
    pred = 2 * abs(mp.cos(mp.pi * mp.re(rho)))
    worst = max(worst, abs(abs(l / abs(l) + 1) - pred))
    if mp.re(rho) != 0.5:
        offdev.append(abs(l / abs(l) + 1))
report("C15", "lam_rho=-e^{2pi gamma} and d_r=0 at zeta zeros 1..25 (Re=1/2); |lam/|lam|+1|=2|cos(pi sigma)| "
       "(!=0 off line)", worst, mp.mpf(10) ** -40, f"[off-line |phase+1| min {mp.nstr(min(offdev), 4)}]")

# ==========================================================================================
# C16  BML11.5 and its truncation dependence (Lemma 33a.4), exact finite model:
#      V_k = D (+) span{L^j u^p : 1<=j<=k, 0<=p<=P}; (M-I)L^j = sum_{i=1}^{j-1} C(j,i) L^i  ([u^p]=0 in G)
P = 2
lam_ex = [sp.Integer(2), sp.Integer(-3), sp.Rational(1, 5), sp.Rational(7, 2)]      # any values != 1
dims_ok = True; rec = []
for k in range(1, 5):
    nD = len(lam_ex); nT = k * (P + 1)
    Mt = sp.zeros(nD + nT, nD + nT)
    for i, l in enumerate(lam_ex):
        Mt[i, i] = l - 1
    idx = lambda j, p: nD + (j - 1) * (P + 1) + p
    for j in range(1, k + 1):
        for p in range(P + 1):
            for i in range(1, j):
                Mt[idx(i, p), idx(j, p)] = sp.binomial(j, i)
    rank = Mt.rank()
    h0 = (nD + nT) - rank; h1 = (nD + nT) - rank
    kern = Mt.nullspace()
    kern_in_L1 = all(all(v[q] == 0 for q in range(nD + nT) if not (nD <= q < nD + P + 1)) for v in kern)
    # is iota(u^0) (L^1 u^0) in the image?
    target = sp.zeros(nD + nT, 1); target[idx(1, 0)] = 1
    aug = Mt.row_join(target)
    in_image = aug.rank() == rank
    rec.append((k, h0, h1, kern_in_L1, in_image))
    dims_ok &= (h0 == P + 1) and (h1 == P + 1) and kern_in_L1 and (in_image == (k >= 2))
report("C16", "BML11.5 (k=1): H^0=H^1=iota(O) (dim P+1 in model); for k log-levels H^0=iota_1, H^1~top level, "
       "and iota_1 classes are coboundaries once k>=2 (exact)", 0 if dims_ok else 1, 0,
       f"[(k,dimH0,dimH1,H0 in iota_1,iota(1) in image) = {rec}]")

# ==========================================================================================
# C17  Correspondence: the log summand = the integer slots rho=-k of the same family; Jordan blocks
#      A_k = (e^u-1)u^{k-1}: C_n A_k = n^{-k} A_k; C_n(L A_k) = n^{-k}(L - log n/(2 pi i))A_k;
#      A_k holomorphic at 0 for k>=0 ([A_k]=0: block collapses), A_{-1}=(e^u-1)/u^2 has principal part 1/u
#      ([A_{-1}] != 0: the NPE4.2-type block n(I-(log n/2pi i)N) at rho=1, i.e. source point rho#=0)
u_ = sp.Symbol('u', positive=True)
ok = True; princ = []
for k in [-1, 0, 1, 2, 3]:
    for n in [2, 3, 5]:
        Ak = (sp.exp(u_) - 1) * u_ ** (k - 1)
        cn = (sp.exp(u_) - 1) / (n * (sp.exp(u_ / n) - 1))
        ok &= sp.simplify(cn * Ak.subs(u_, u_ / n) - sp.Integer(n) ** (-k) * Ak) == 0
    ser = sp.series((sp.exp(u_) - 1) * u_ ** (k - 1), u_, 0, 3).removeO()
    neg = [ser.coeff(u_, -j) for j in range(1, 4)]
    princ.append((k, neg))
    ok &= (any(c != 0 for c in neg) == (k == -1))
report("C17", "log summand <-> integer slots: C_n[(e^u-1)u^{k-1}] = n^{-k}(same) (exact, k=-1..3, n=2,3,5); "
       "principal part nonzero only for k=-1 (rho=1)", 0 if ok else 1, 0,
       f"[principal-part coeffs of u^-1,u^-2,u^-3: {princ}]")

# ==========================================================================================
# C18  Constants used in BML1/BMR1: |Gamma(1+rho)| <= Gamma(1+sigma) <= 1 (BMR1 says <= 2);
#      |d_r| < r-1 (BMR1 uses r+1); exact Gaussian modulus e^{t(1-sigma)^2 - t gamma^2}
worst = -mp.inf
pts = [mp.zetazero(k) for k in range(1, 11)] + [rho for rho, m in SYN]
for rho in pts:
    sg, gm = mp.re(rho), mp.im(rho)
    worst = max(worst, abs(mp.gamma(1 + rho)) - mp.gamma(1 + sg), mp.gamma(1 + sg) - 1,
                abs(d_r(rho)) - (R_PAR - 1),
                relerr(abs(gauss(rho)), mp.exp(T_PAR * (1 - sg) ** 2 - T_PAR * gm ** 2)) - mp.mpf(10) ** -40)
report("C18", "BMR1 constants: |Gamma(1+rho)|<=Gamma(1+sigma)<=1; |d_r|<r-1; |e^{t(1-rho)^2}|=e^{t(1-s)^2-t g^2}",
       max(worst, 0), 0, f"[max excess {mp.nstr(worst, 3)} (<=0)]")

print()
print(f"SUMMARY: {sum(RESULTS)} PASS / {len(RESULTS) - sum(RESULTS)} FAIL (of {len(RESULTS)} recorded outcomes)")
