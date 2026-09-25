#!/usr/bin/env python3
# Checks for 32_ (first-pass audit of NHI/NHIR, HSR/HSRA and HBW/HBWR, in the programme's working folder
# quantum_tau_programme_bridge_20260924/next_edition_after_647). Written by a Claude subagent of claude-ab
# (Opus 5.5, max effort), 25 September 2026, and copied here unchanged apart from this header.
"""checks32.py -- audit checks for NHI/NHIR, HSR/HSRA, HBW/HBWR.

Each item prints PASS/FAIL, a one-line description and an error measure.
Exact (sympy) arithmetic where the claim is algebraic; mpmath (40-80 digits)
otherwise.  Gaussian-weighted quantities at zeta zeros are compared relative
to the Gaussian factor.  Coordinate identities for the specialization maps
(which are algebraic in the zero coordinates) are tested on a synthetic
reflection-symmetric divisor with off-line points, since all computed zeta
zeros are on the line.
"""
import itertools, random, sys
import mpmath as mp
import sympy as sp

mp.mp.dps = 50
random.seed(32)
RESULTS = []


def report(tag, desc, err, tol, extra=""):
    ok = (err <= tol)
    RESULTS.append(ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {tag}: {desc} | err={mp.nstr(err, 3)} (tol {mp.nstr(tol, 2)}){(' ' + extra) if extra else ''}")


# ---------------------------------------------------------------- helpers
def _F0_raw(s):
    # s(s-1)/8 pi^{-s/2} Gamma(s/2) zeta(s), with (s-1)zeta(s) regularised at s=1
    if abs(s - 1) < mp.mpf(10) ** (-mp.mp.dps + 5):
        sz1 = 1 + mp.euler * (s - 1)
    else:
        sz1 = (s - 1) * mp.zeta(s)
    return s / 8 * mp.power(mp.pi, -s / 2) * mp.gamma(s / 2) * sz1


def F0(s):
    """F_0 = xi/4, evaluated through the functional equation on Re s < 1/2."""
    s = mp.mpc(s)
    return _F0_raw(s) if mp.re(s) >= 0.5 else _F0_raw(1 - s)


def phi(m, s):
    s = mp.mpc(s)
    if m == 0:
        return -1 / s
    return (mp.power(m, 1 - s) - mp.power(m + 1, 1 - s)) / s


def g(t, s):
    return mp.exp(t * s * s)


def F_tm(t, m, s):
    return g(t, s) * (phi(m, s) + 8 * F0(s) / s)


def Bfun(v, der=0):
    """B(v) = 1/(e^v-1) - 1/v and its derivatives (der<=4); Bernoulli series near 0."""
    v = mp.mpc(v)
    if abs(v) < 0.5:
        tot = mp.mpc(0)
        for n in range(1 + der, 100):
            Bn = mp.bernoulli(n)
            if Bn == 0:
                continue
            tot += Bn / mp.factorial(n) * mp.ff(n - 1, der) * v ** (n - 1 - der)
        return tot
    E = mp.exp(v)
    if der == 0:
        return 1 / (E - 1) - 1 / v
    eul = {1: [1], 2: [1, 1], 3: [1, 4, 1], 4: [1, 11, 11, 1]}[der]      # Eulerian polynomials
    q = (-1) ** der * E * sum(c * E ** i for i, c in enumerate(eul)) / (E - 1) ** (der + 1)
    return q + (-1) ** (der + 1) * mp.factorial(der) / v ** (der + 1)


_L0 = 30
_XCUT = mp.mpf(400)


def _logquad(f, ya, yb):
    """int_{e^ya}^{e^yb} f(x) dx via x = e^y, unit subintervals (log-oscillation safe)."""
    N = int(mp.ceil(yb - ya))
    pts = [ya + (yb - ya) * j / N for j in range(N + 1)]
    return mp.quad(lambda y: f(mp.exp(y)) * mp.exp(y), pts)


def _binom_neg(p, k):          # binomial(-p, k) for integer p >= 1
    return (-1) ** k * mp.binomial(p + k - 1, k)


def GA(s, u, du=0):
    """Gamma(s) * (d/du)^du A_s(u) = int_0^inf x^{s-1} B^{(du)}(x+u) dx  (HBW1.2), computed as
    exact small-x expansion on [0,e^-30] + log-substituted quadrature + exact large-x expansion."""
    eps = mp.exp(-_L0)
    small = sum(Bfun(u, du + k) / mp.factorial(k) * eps ** (s + k) / (s + k) for k in range(4))
    mid = _logquad(lambda x: mp.power(x, s - 1) * Bfun(x + u, du), -_L0, mp.log(_XCUT))
    p = du + 1   # B^{(du)}(v) = q^{(du)}(v) + (-1)^{du+1} du!/v^{du+1}; q-part on [X,inf) is O(e^-400)
    tail = sum(_binom_neg(p, k) * u ** k * _XCUT ** (s - p - k) / (p + k - s) for k in range(60))
    return small + mid + (-1) ** (du + 1) * mp.factorial(du) * tail


def A_integral(s, u, du=0):
    return GA(s, u, du) / mp.gamma(s)


def split_HBW82(s, u):
    """Right side of HBW8.2 / HBWR4.2, each integral computed robustly."""
    eps = mp.exp(-_L0)
    I01_small = sum(Bfun(u, 1 + k) / mp.factorial(k) * eps ** (s + 1 + k) / (s + 1 + k) for k in range(4))
    I01 = I01_small + _logquad(lambda x: mp.power(x, s) * Bfun(x + u, 1), -_L0, 0)
    I1inf = _logquad(lambda x: mp.power(x, s - 1) * (Bfun(x + u) + 1 / x), 0, mp.log(_XCUT))
    I1inf += sum((-1) ** (k + 1) * u ** k * _XCUT ** (s - 1 - k) / (1 + k - s) for k in range(1, 60))
    return Bfun(1 + u) / s - I01 / s - 1 / (1 - s) + I1inf


def A_series(s, u, du=0, K=120):
    """DLMF-type series sum_k zeta(s-k)(-u)^k/k!  (|u| < 2 pi)."""
    tot = mp.mpc(0)
    for k in range(du, K):
        tot += mp.zeta(s - k) * (-1) ** k * mp.ff(k, du) * u ** (k - du) / mp.factorial(k)
    return tot


def Li(a, z, tol=None):
    """Li_a(z) = sum_{n>=1} n^{-a} z^n by direct summation (|z|<1)."""
    tot = mp.mpc(0)
    n = 1
    zn = mp.mpc(z)
    eps = mp.mpf(10) ** (-mp.mp.dps + 3)
    while True:
        term = zn * mp.power(n, -a)
        tot += term
        if abs(term) < eps * max(1, abs(tot)) and n > 20:
            break
        n += 1
        zn *= z
    return tot


def K_s(s, z):
    """HBW0.3: K_s(z) = -(1-z)/(s z) Li_{s-1}(z)."""
    return -(1 - z) / (s * z) * Li(s - 1, z)


def relerr(a, b):
    return abs(a - b) / max(abs(b), mp.mpf(10) ** (-200))



# exact representation k^{1-s} = prod_p X_p^{e_p}  (X_p = p^{1-s} independent symbols)
_X = {}
def pw(k):
    out = sp.Integer(1)
    for p, e in sp.factorint(k).items():
        if p not in _X:
            _X[p] = sp.Symbol(f"X{p}")
        out *= _X[p] ** e
    return out
def phi_exact(k, s):
    return -1 / s if k == 0 else (pw(k) - pw(k + 1)) / s

rho1 = mp.zetazero(1)
rho2 = mp.zetazero(2)
sharp = lambda r: 1 - mp.conj(r)

# ======================================================================
# C01  F_0 special values (NHI0.2 = HSR0.2 = HBW0.1 = HBWR0.1)
mp.mp.dps = 80
errs = []
errs.append(abs(F0(1) - mp.mpf(1) / 8))
errs.append(abs(F0(mp.mpf(10) ** -40) - mp.mpf(1) / 8))  # F0(0) via reflection
errs.append(abs(F0(2) - mp.pi / 24))
errs.append(abs(F0(-1) - mp.pi / 24))
wrong = []
for k in range(1, 7):
    eps = mp.mpf(10) ** -35
    direct = _F0_raw(mp.mpf(-2 * k) + eps)          # raw product: Gamma pole x zeta zero
    formula = k * (2 * k + 1) * (-1) ** k * mp.pi ** k * mp.zeta(-2 * k, 1, 1) / (2 * mp.factorial(k))
    formula_bad = k * (2 * k + 1) * (-1) ** k * mp.pi ** k * mp.zeta(-2 * k, 1, 1) / mp.factorial(2 * k)
    errs.append(relerr(direct, formula) - mp.mpf(10) ** -30)   # O(eps) limit error allowed
    errs.append(relerr(F0(1 + 2 * k), formula))
    wrong.append(relerr(formula_bad, formula))
err = max(max(errs), 0)
report("C01", "F0(0)=F0(1)=1/8, F0(-1)=F0(2)=pi/24, F0(-2k)=k(2k+1)(-1)^k pi^k zeta'(-2k)/(2*k!) k<=6",
       err, mp.mpf(10) ** -25,
       f"[reading 2j! as (2j)! instead: rel.err {mp.nstr(min(wrong[1:]), 3)}..{mp.nstr(max(wrong), 3)} for k>=2 -> must be 2*(j!)]")
mp.mp.dps = 50

# ======================================================================
# C02  NHI0.3 / HBW0.2: residue of phi_m at 0 is -1 for every m; 8F0(0)=1 -> psi_m entire
s = sp.symbols('s')
res_ok = True
for m in range(0, 7):
    ph = -1 / s if m == 0 else (sp.Integer(m) ** (1 - s) - sp.Integer(m + 1) ** (1 - s)) / s
    r = sp.residue(ph, s, 0)
    res_ok &= sp.simplify(r + 1) == 0
eps = mp.mpf(10) ** -20
num = max(abs(phi(m, eps) + 8 * F0(eps) / eps - (phi(m, -eps) + 8 * F0(-eps) / (-eps))) for m in range(6))
report("C02", "Res_{s=0} phi_m = -1 (m=0..6, exact) and psi_m = phi_m+8F0/s bounded at 0 (8F0(0)=1)",
       0 if res_ok else 1, 0, f"[|psi_m(eps)-psi_m(-eps)| max {mp.nstr(num, 3)}]")
report("C02b", "psi_m continuous through 0 numerically (removable singularity)", num, mp.mpf(10) ** -15)

# ======================================================================
# C03  NHI2.1-2.2, NHI1.2, NHI1.4 (exact telescoping; integral identity; w-derivative)
w, th, t_ = sp.symbols('w theta t', positive=True)
tele_ok = True
for n in range(1, 13):
    tot = sum(phi_exact(m, s) for m in range(n))
    tele_ok &= sp.expand(tot + pw(n) / s) == 0
ws = sp.symbols('ws')
lhs = (sp.exp(-w * s) - 1) / s
rhs = -w * sp.integrate(sp.exp(-th * w * s), (th, 0, 1), conds='none')
int_ok = sp.simplify(lhs - rhs) == 0
F0f = sp.Function('F0')
E = sp.exp(t_ * s ** 2) * (sp.exp(-w * s) - 8 * F0f(s)) / s
der_ok = sp.simplify(sp.diff(E, w) + sp.exp(t_ * s ** 2) * sp.exp(-w * s)) == 0
# numeric: sum_{m<n} F_{t,m} = -n E_{t,log n}
tt = mp.mpf('0.3'); sv = mp.mpc('0.37', '2.9')
nerr = 0
for n in range(1, 9):
    lhsn = sum(F_tm(tt, m, sv) for m in range(n))
    Etw = g(tt, sv) * (mp.exp(-mp.log(n) * sv) - 8 * F0(sv)) / sv
    nerr = max(nerr, relerr(lhsn, -n * Etw))
report("C03", "sum_{m<n} phi_m = -n^{1-s}/s (exact, n<=12); (e^{-ws}-1)/s = -w int_0^1 e^{-thws}; dE/dw = -g e^{-ws}; sum F_tm = -n E_{t,log n}",
       nerr if (tele_ok and int_ok and der_ok) else 1, mp.mpf(10) ** -40,
       f"[exact parts: {tele_ok}, {bool(int_ok)}, {der_ok}]")

# ======================================================================
# C04  NHI1.3 strip bound, uniform in theta
mp.mp.dps = 20
worst = 0
for trial in range(40):
    a = mp.mpf(random.uniform(0.1, 3)); t = mp.mpf(random.uniform(0.1, 2)); N = random.randint(0, 6)
    wv = mp.mpc(random.uniform(-4, 4), random.uniform(-6, 6)); theta = mp.mpf(random.uniform(0, 1))
    CN = max((1 + abs(y)) ** N * mp.exp(-t * y * y / 2) for y in [mp.mpf(k) / 20 for k in range(0, 400)])
    bound = CN * mp.exp(t * a * a + a * abs(mp.re(wv)) + mp.im(wv) ** 2 / (2 * t))
    lhs = 0
    for x in [-a, -a / 2, 0, a / 2, a]:
        for y in [mp.mpf(k) / 10 for k in range(-300, 301)]:
            sv = mp.mpc(x, y)
            lhs = max(lhs, (1 + abs(y)) ** N * abs(g(t, sv) * mp.exp(-theta * wv * sv)))
    worst = max(worst, lhs / bound)
report("C04", "NHI1.3: b_{a,N}(g_t e^{-theta w s}) <= C_{N,t} exp(ta^2+a|Re w|+(Im w)^2/(2t)); max ratio over 40 random cases",
       max(worst - 1, 0), mp.mpf(10) ** -3, f"[max ratio {mp.nstr(worst, 4)}]")
mp.mp.dps = 50

# ======================================================================
# C05  NHI0.1 normalisations of Theta and Theta^{-1}; Theta a(1) = (1/2) int a(e^x) e^x dx (NHI8.3)
a_fun = lambda u: mp.exp(-mp.log(u) ** 2)                 # in A (Gaussian in log u)
Theta = lambda sv: mp.quad(lambda x: a_fun(mp.exp(x)) * mp.exp(x * sv), [-mp.inf, 0, mp.inf]) / 2
closed = lambda sv: mp.sqrt(mp.pi) / 2 * mp.exp(sv * sv / 4)
e1 = max(relerr(Theta(sv), closed(sv)) for sv in [mp.mpf(1), mp.mpc(0.5, 3), mp.mpc(-1.2, 0.7)])
Thinv = lambda u: mp.power(u, -0.5) / mp.pi * mp.quad(lambda y: closed(mp.mpc(0.5, y)) * mp.power(u, mp.mpc(0, -y)), [-mp.inf, 0, mp.inf])
e2 = max(relerr(Thinv(u), a_fun(u)) for u in [mp.mpf('0.5'), mp.mpf(1), mp.mpf(3)])
report("C05", "Theta a(s)=(1/2)int a(u)u^s du/u and Theta^{-1}F(u)=u^{-1/2}/pi int F(1/2+iy)u^{-iy}dy are inverse; Theta a(1)=F(1)",
       max(e1, e2), mp.mpf(10) ** -30)

# ======================================================================
# C06  NHI5.2-5.3: finite-block inverse of the Gaussian multiplier
rho_s, tt_s = sp.symbols('rho t')
mblk = 5
x = sp.symbols('x')
def taylor(expr):
    return sp.series(expr, x, 0, mblk).removeO()
G = taylor(sp.exp(tt_s * (rho_s + x) ** 2))
Gi = taylor(sp.exp(-tt_s * (rho_s + x) ** 2))
prod = sp.expand(G * Gi)
trunc = sum(prod.coeff(x, k) * x ** k for k in range(mblk))
blk_ok = sp.simplify(trunc - 1) == 0
report("C06", "NHI5.3: Taylor(e^{ts^2})*Taylor(e^{-ts^2}) = 1 mod (s-rho)^5, symbolic rho,t", 0 if blk_ok else 1, 0)

# ======================================================================
# C07  NHI6.2 / HSR7.1: cover telescoping and the discrepancy delta_{n,t} (= NCI delta_{n,t})
cov_ok = True
for n in range(2, 8):
    for m in range(0, 7):
        lhs = sum(phi_exact(n * m + a, s) for a in range(n))
        cov_ok &= sp.expand(lhs - pw(n) * phi_exact(m, s)) == 0
tt = mp.mpf('0.2'); sv = mp.mpc('0.61', '-3.3'); nerr = 0
for n in range(2, 6):
    for m in range(0, 5):
        lhs = sum(F_tm(tt, n * m + a, sv) for a in range(n)) - mp.power(n, 1 - sv) * F_tm(tt, m, sv)
        rhs = 8 * g(tt, sv) * F0(sv) * (n - mp.power(n, 1 - sv)) / sv
        nerr = max(nerr, relerr(lhs, rhs))
report("C07", "sum_a phi_{nm+a} = n^{1-s} phi_m (exact, n<=7, m<=6); sum_a F_{t,nm+a} - n^{1-s}F_{t,m} = 8g_tF0(n-n^{1-s})/s",
       nerr if cov_ok else 1, mp.mpf(10) ** -40, f"[exact part {cov_ok}]")

# ======================================================================
# C08  (audit) remainder on the full dual B': W_n^* H lam - H U_n' lam = conj(lam(delta_{n,t}))/(1-z)
tt = mp.mpf('0.25'); s0 = mp.mpc('0.3', '1.7'); err = 0
lam = lambda Ffun: Ffun(s0)                                    # lam = ev_{s0}, not in I-perp
coef = lambda m: mp.conj(F_tm(tt, m, s0))                       # [z^m] H^B lam
for n in (2, 3, 4):
    delta = 8 * g(tt, s0) * F0(s0) * (n - mp.power(n, 1 - s0)) / s0
    for m in range(0, 9):
        Wn = sum(coef(n * m + a) for a in range(n))
        HU = mp.conj(mp.power(n, 1 - s0) * F_tm(tt, m, s0))
        err = max(err, relerr(Wn - HU, mp.conj(delta)))
ev1 = [mp.conj(F_tm(tt, m, mp.mpf(1))) for m in range(6)]
e_ev1 = max([abs(ev1[0])] + [abs(v - mp.exp(tt)) for v in ev1[1:]])
report("C08", "on B' (no ideal): W_n^*H lam - H U_n' lam = conj(lam(delta_nt))/(1-z) (lam=ev_s0); H(ev_1) = e^t z/(1-z)",
       max(err, e_ev1), mp.mpf(10) ** -40)

# ======================================================================
# C09  NHI8 / NHIR3: tail annihilator.  psi_m(1)=8F0(1)=1 for m>=1, psi_0(1)=0; with Phi(1)=0 ev_1 kills every tail
ok = True
for m in range(0, 8):
    phm1 = (-1 if m == 0 else sp.Integer(m) ** 0 - sp.Integer(m + 1) ** 0)
    psi1 = phm1 + 1                       # 8F0(1) = 1
    ok &= (psi1 == (0 if m == 0 else 1))
    PhiAlt = 1 - sp.Integer(1)            # Phi(s) = 1 - s : Phi(0)=1, Phi(1)=0
    ok &= ((phm1 + PhiAlt) == (-1 if m == 0 else 0))
# numeric: psi_m(1) with the actual F0
nume = max(abs(phi(m, 1) + 8 * F0(1) - (0 if m == 0 else 1)) for m in range(8))
report("C09", "psi_m(1)=0 (m=0), =1 (m>=1) [8F0(1)=1]; for Phi=1-s, psi^Phi_m(1)=0 for m>=1 so ev_1 kills that tail",
       nume if ok else 1, mp.mpf(10) ** -45)

# ======================================================================
# C10  HSR3.2 / HBW0.5 at actual zeros: conj(F_{t,m}(rho#)) = e^{t(1-rho)^2} phi_m(1-rho); fails for j=1 >= m_rho
err = 0; neg = mp.inf; ctrl_err = 0
for rho in (rho1, rho2):
    for tt in (mp.mpf('0.05'), mp.mpf(1)):
        gauss = abs(mp.exp(tt * (1 - rho) ** 2))
        for m in range(0, 6):
            lhs = mp.conj(F_tm(tt, m, sharp(rho)))
            rhs = mp.exp(tt * (1 - rho) ** 2) * phi(m, 1 - rho)
            err = max(err, abs(lhs - rhs) / (gauss * abs(phi(m, 1 - rho))))
        # j = 1 (not < m_rho = 1): the correction derivative survives, = conj(8 g_t(rho) F0'(rho)/rho)
        m = 2
        d_full = mp.conj(mp.diff(lambda z: F_tm(tt, m, z), rho))
        d_noc = mp.diff(lambda z: g(tt, z) * phi(m, z), mp.conj(rho))
        pred = mp.conj(8 * g(tt, rho) * mp.diff(F0, rho) / rho)
        ctrl_err = max(ctrl_err, relerr(d_full - d_noc, pred))
        neg = min(neg, abs(pred) / abs(d_noc))
rp = rho1 + mp.mpf('1e-10')      # displaced point (not a zero): identity must fail, by ~|8F0'(rho)1e-10/rho|/|phi_m|
disp = abs(mp.conj(F_tm(1, 3, sharp(rp))) - mp.exp((1 - rp) ** 2) * phi(3, 1 - rp)) / abs(mp.exp((1 - rp) ** 2) * phi(3, 1 - rp))
report("C10", "HSR3.2/HBW0.5: conj F_{t,m}(rho#) = e^{t(1-rho)^2}phi_m(1-rho) at rho_1,rho_2 (t=0.05,1), rel. to Gaussian",
       err, mp.mpf(10) ** -35, f"[|F0(rho_1)| ~ 1.7e-54 at 50 digits; control at rho_1+1e-10: rel. diff {mp.nstr(disp, 3)} (nonzero)]")
if not disp > mp.mpf(10) ** -20:
    RESULTS.append(False)
report("C10b", "control j=1>=m_rho: jet formula HBW0.5 fails by exactly conj(8g_t(rho)F0'(rho)/rho) (rel. err of that prediction)",
       ctrl_err, mp.mpf(10) ** -25, f"[size of the surviving correction rel. to main term: >= {mp.nstr(neg, 3)}; nonzero]")
if not neg > mp.mpf(10) ** -12:
    RESULTS.append(False)

# ======================================================================
# C11  HSR3.3 / HBW0.3-0.4: generating function sum phi_m(s) z^m = K_s(z); removable value -1/s
err = 0
for sv in (1 - rho1, mp.mpc('0.3', '2'), mp.mpc('0.8', '-5')):
    for zv in (mp.mpc('0.3', '0.4'), mp.mpf('-0.6'), mp.mpc('0.1', '-0.7')):
        ser = sum(phi(m, sv) * zv ** m for m in range(0, 400))
        err = max(err, relerr(ser, K_s(sv, zv)))
    err = max(err, relerr(K_s(sv, mp.mpf(10) ** -48), -1 / sv))
    # HSR3.3 form with rho = 1 - s: (z-1)/((1-rho) z) Li_{-rho}(z)
    rr = 1 - sv; zv = mp.mpc('0.2', '0.5')
    err = max(err, relerr((zv - 1) / ((1 - rr) * zv) * Li(-rr, zv), K_s(sv, zv)))
# full generating identity HBW0.4 with the correction: sum g psi_m z^m = g (K_s + 8F0/(s(1-z)))
tt = mp.mpf('0.1'); sv = mp.mpc('0.4', '1.3'); zv = mp.mpc('0.35', '-0.25')
ser = sum(F_tm(tt, m, sv) * zv ** m for m in range(0, 200))
err = max(err, relerr(ser, g(tt, sv) * (K_s(sv, zv) + 8 * F0(sv) / (sv * (1 - zv)))))
report("C11", "sum_m phi_m(s)z^m = -(1-z)Li_{s-1}(z)/(sz) (incl. s=1-rho_1), K_s(0)=-1/s, HBW0.4 with 8F0/(s(1-z))",
       err, mp.mpf(10) ** -35)

# ======================================================================
# C12  HBW1.1-1.4 and HBW2.1-2.2: singular decomposition at the receiving boundary
err = 0
for sv in (mp.mpc('0.35', '2.2'), mp.mpc('0.8', '-1.1')):
    for uv in (mp.mpf('0.4'), mp.mpc('0.25', '0.6')):
        Li_s = Li(sv, mp.exp(-uv))
        Aint = A_integral(sv, uv)
        Aser = A_series(sv, uv)
        err = max(err, relerr(Li_s, mp.gamma(1 - sv) * mp.power(uv, sv - 1) + Aint))
        err = max(err, relerr(Aint, Aser))
        Li_s1 = Li(sv - 1, mp.exp(-uv))
        dA = A_integral(sv, uv, 1)
        err = max(err, relerr(Li_s1, mp.gamma(2 - sv) * mp.power(uv, sv - 2) - dA))
        # HBW2.2 (without correction term): g K_s(e^{-u}) = C_t (e^u-1) u^{s-2} + R_{t,s}(u)
        tt = mp.mpf('0.3')
        Ct = -mp.exp(tt * sv ** 2) * mp.gamma(2 - sv) / sv
        R = mp.exp(tt * sv ** 2) * (mp.exp(uv) - 1) / sv * dA
        err = max(err, relerr(g(tt, sv) * K_s(sv, mp.exp(-uv)), Ct * (mp.exp(uv) - 1) * mp.power(uv, sv - 2) + R))
report("C12", "Li_s(e^{-u}) = Gamma(1-s)u^{s-1} + A_s(u) (integral = zeta series), Li_{s-1} = Gamma(2-s)u^{s-2} - dA, HBW2.2",
       err, mp.mpf(10) ** -30)

# ======================================================================
# C13  HBW8.2 = HBWR4.2 split formula; continuation across negative real u; HBW8.4 reflection and bound
mp.mp.dps = 40
err = 0
for sv in (mp.mpc('0.4', '3'), mp.mpc('0.15', '-7')):
    for uv in (mp.mpf('0.7'), mp.mpf('-1.0'), mp.mpc('-0.5', '1.5')):
        direct = GA(sv, uv)
        split = split_HBW82(sv, uv)
        err = max(err, relerr(split, direct))
        err = max(err, relerr(direct / mp.gamma(sv), A_series(sv, uv)))
e_refl = 0; worst = 0
for re_ in [k / 20 for k in range(1, 20)]:
    for im_ in [k / 2 for k in range(-80, 81)]:
        sv = mp.mpc(re_, im_)
        e_refl = max(e_refl, relerr(mp.sin(mp.pi * sv) * mp.gamma(2 - sv) / (mp.pi * (1 - sv)), 1 / mp.gamma(sv)))
        worst = max(worst, abs(1 / mp.gamma(sv)) / (2 * mp.exp(mp.pi * abs(im_)) / (mp.pi * abs(1 - sv))))
report("C13", "HBW8.2/HBWR4.2 split formula = defining integral = zeta series (u=0.7,-1,-0.5+1.5i); 1/Gamma reflection; HBW8.4 bound",
       max(err, e_refl), mp.mpf(10) ** -25, f"[max |1/Gamma| / bound = {mp.nstr(worst, 3)} (<=1)]")
mp.mp.dps = 50
if worst > 1:
    RESULTS.append(False)

# ======================================================================
# C14  HBW2.3, HBW3.1, HBW4.4-4.5 symbolically (generic C(s)); monodromy L -> L + 2 pi i
L, U, nn = sp.symbols('L U n', positive=True)
Cf = sp.Function('C')
base = Cf(s) * (sp.exp(U) - 1) * sp.exp((s - 2) * L)          # u^{s-2} = e^{(s-2)L}, U = u
def S_j(j, expr=base):
    return sp.diff(expr, s, j) / sp.factorial(j)
ok = True
for j in range(0, 4):
    closed_j = (sp.exp(U) - 1) * sp.exp((s - 2) * L) * sum(sp.diff(Cf(s), s, j - k) / sp.factorial(j - k) * L ** k / sp.factorial(k) for k in range(j + 1))
    ok &= sp.simplify(S_j(j) - closed_j) == 0
    mono = S_j(j).subs(L, L + 2 * sp.pi * sp.I)
    rhs = sp.exp(2 * sp.pi * sp.I * (s - 1)) * sum((2 * sp.pi * sp.I) ** k / sp.factorial(k) * S_j(j - k) for k in range(j + 1))
    ok &= sp.simplify(sp.expand(mono - rhs)) == 0
    cnt = sp.diff(nn ** (1 - s) * base, s, j) / sp.factorial(j)
    rhs2 = nn ** (1 - s) * sum((-sp.log(nn)) ** k / sp.factorial(k) * S_j(j - k) for k in range(j + 1))
    ok &= sp.simplify(sp.expand(cnt - rhs2)) == 0
# HBW4.4 geometric sheet sum (numeric, several n, s, u)
e44 = 0
for n in (2, 3, 7):
    for sv in (mp.mpc('0.3', '4'), mp.mpc('0.7', '-2')):
        for uv in (mp.mpf('0.3'), mp.mpc('0.2', '0.5')):
            lhs = sum(mp.exp(a * uv / n) for a in range(n)) * (mp.exp(uv / n) - 1) * mp.power(uv / n, sv - 2) / n
            e44 = max(e44, relerr(lhs, mp.power(n, 1 - sv) * (mp.exp(uv) - 1) * mp.power(uv, sv - 2)))
report("C14", "HBW2.3 closed form, HBW3.1 monodromy e^{2pi i(s-1)}sum (2pi i)^k/k! S_{j-k}, HBW4.5 counting n^{1-s}sum(-log n)^k/k! S_{j-k} (exact, j<=3); HBW4.4",
       e44 if ok else 1, mp.mpf(10) ** -40, f"[symbolic {ok}]")

# ======================================================================
# C15  HBWR3.3-3.4: (M-I)^{-1} finite series and N recovered from M (Jordan block m=4)
mblk = 4
Nm = mp.matrix(mblk, mblk)
for i in range(mblk - 1):
    Nm[i, i + 1] = 1
sv = mp.mpc('0.3', '2.0'); a_s = mp.exp(2j * mp.pi * (sv - 1))
expN = mp.eye(mblk); P = mp.eye(mblk)
for k in range(1, mblk):
    P = P * Nm
    expN += (2j * mp.pi) ** k / mp.factorial(k) * P
M = a_s * expN
Bs = M - a_s * mp.eye(mblk)
inv = mp.zeros(mblk, mblk); P = mp.eye(mblk)
for h in range(mblk):
    inv += (-1) ** h * P / (a_s - 1) ** (h + 1)
    P = P * Bs
e1 = mp.mnorm((M - mp.eye(mblk)) * inv - mp.eye(mblk), 1)
X = M * (1 / a_s) - mp.eye(mblk); logM = mp.zeros(mblk, mblk); P = mp.eye(mblk)
for h in range(1, mblk):
    P = P * X
    logM += (-1) ** (h + 1) * P / h
e2 = mp.mnorm(logM / (2j * mp.pi) - Nm, 1)
report("C15", "HBWR3.3 (M-I)^{-1}=sum (-1)^h B^h/(a-1)^{h+1}; HBWR3.4 N=(1/2pi i)sum (-1)^{h+1}(a^{-1}M-I)^h/h", max(e1, e2), mp.mpf(10) ** -40)

# ======================================================================
# C16  HBW4.2-4.3 sheet formula and Cauchy bounds; NHIR4.2 tail bound
mp.mp.dps = 30
err = 0; worst = 0
for trial in range(6):
    deg = 80
    cf = [mp.mpc(random.gauss(0, 1), random.gauss(0, 1)) * mp.mpf(0.97) ** k for k in range(deg)]
    f = lambda zz: sum(c * zz ** k for k, c in enumerate(cf))
    for n in (2, 3, 5):
        zv = mp.mpc(random.uniform(-0.3, 0.3), random.uniform(-0.3, 0.3))
        Wcoef = [sum(cf[n * m + a] for a in range(n) if n * m + a < deg) for m in range(deg // n + 1)]
        W = sum(c * zv ** m for m, c in enumerate(Wcoef))
        root = mp.power(zv, mp.mpf(1) / n)
        sheet = sum(sum(mp.power(om, -a) * mp.power(zv, -mp.mpf(a) / n) for a in range(n)) * f(om * root)
                    for om in [mp.exp(2j * mp.pi * k / n) for k in range(n)]) / n
        err = max(err, relerr(sheet, W))
        # HBW4.2: |W_n^* f(z)| <= sum_a R^{-a}/(1-r/R^n) sup_{|w|<=R}|f|
        R = mp.mpf('0.9'); r = mp.mpf('0.5') * R ** n
        supf = max(abs(f(R * mp.exp(2j * mp.pi * k / 256))) for k in range(256))
        supW = max(abs(sum(c * (r * mp.exp(2j * mp.pi * k / 64)) ** m for m, c in enumerate(Wcoef))) for k in range(64))
        worst = max(worst, supW / (sum(R ** (-a) for a in range(n)) / (1 - r / R ** n) * supf))
    # NHIR4.2 tail operator
    Mt = 7; R = mp.mpf('0.85'); r = mp.mpf('0.6')
    supf = max(abs(f(R * mp.exp(2j * mp.pi * k / 256))) for k in range(256))
    supJ = max(abs(sum(cf[Mt + j] * (r * mp.exp(2j * mp.pi * k / 64)) ** j for j in range(deg - Mt))) for k in range(64))
    worst = max(worst, supJ / (R ** (-Mt) / (1 - r / R) * supf))
report("C16", "HBW4.3 root-of-unity sheet formula = coefficient definition of W_n^*; HBW4.2 and NHIR4.2 Cauchy bounds (max ratio)",
       err, mp.mpf(10) ** -25, f"[max bound ratio {mp.nstr(worst, 3)} (<=1)]")
mp.mp.dps = 50
if worst > 1:
    RESULTS.append(False)

# ======================================================================
# Synthetic reflection-symmetric divisor for coordinate identities (HSR/HSRA/HBW6/HBW9)
offs = [(mp.mpf('0.31'), mp.mpf('17.3'), 2), (mp.mpf('0.12'), mp.mpf('25.9'), 1), (mp.mpf('0.46'), mp.mpf('31.7'), 3)]
ons = [(mp.mpf('14.134725'), 1), (mp.mpf('21.022040'), 2)]
Z = []  # list of (rho, mult)
for b, gm, mu in offs:
    for rr in (mp.mpc(b, gm), mp.mpc(b, -gm), mp.mpc(1 - b, gm), mp.mpc(1 - b, -gm)):
        Z.append((rr, mu))
for gm, mu in ons:
    for rr in (mp.mpc(0.5, gm), mp.mpc(0.5, -gm)):
        Z.append((rr, mu))
idx = {}
for i, (rr, mu) in enumerate(Z):
    idx[(mp.nstr(mp.re(rr), 12), mp.nstr(mp.im(rr), 12))] = i
def index_of(rr):
    return idx[(mp.nstr(mp.re(rr), 12), mp.nstr(mp.im(rr), 12))]
Js = [index_of(sharp(rr)) for rr, mu in Z]
mult = [mu for rr, mu in Z]
def d_r(r, rr):
    return mp.exp(-1j * mp.im(rr) * mp.log(r)) * (mp.power(r, mp.re(rr)) - mp.power(r, 1 - mp.re(rr)))
def ip(xv, yv):
    return sum(mult[i] * xv[i] * mp.conj(yv[i]) for i in range(len(Z)))
rand = lambda: [mp.mpc(random.gauss(0, 1), random.gauss(0, 1)) for _ in Z]
Ftest = lambda sv: mp.exp(mp.mpf('0.1') * sv * sv) * (sv ** 2 + mp.mpc(1, 2) * sv + 3)
Gtest = lambda sv: mp.exp(mp.mpf('0.05') * sv * sv) * (sv - mp.mpc(0.3, -1))
rpar = mp.mpf('2.7')

# ======================================================================
# C17  HSR1.1, HSR8.3-8.4, HSR8.8, HSRA5.1, 24_ 3.3, HBW6.2 coefficient; Omega T_n Omega = U_n
y = rand(); err = 0
# d_r identities
for i, (rr, mu) in enumerate(Z):
    err = max(err, abs(d_r(rpar, Z[Js[i]][0]) + d_r(rpar, rr)))
    err = max(err, abs(mp.exp(2j * mp.im(rr) * mp.log(rpar)) * d_r(rpar, rr) - mp.conj(d_r(rpar, rr))))
    err = max(err, abs(d_r(rpar, rr) - mp.conj(mp.power(rpar, rr) - mp.power(rpar, sharp(rr)))))
    if mp.re(rr) == 0.5:
        err = max(err, abs(d_r(rpar, rr)))
beta = lambda Ff: [mp.conj(d_r(rpar, rr)) * Ff(sharp(rr)) for rr, mu in Z]
EF = lambda Ff: [Ff(rr) for rr, mu in Z]
JD = lambda yv: [d_r(rpar, Z[Js[i]][0]) * yv[Js[i]] for i in range(len(Z))]
sigma = lambda yv, Ff: ip(beta(Ff), yv)                     # sigma_r(ybar)(F)
err = max(err, abs(sigma(y, Ftest) - ip(EF(Ftest), JD(y))))
Kr = lambda yv: [-mp.exp(2j * mp.im(rr) * mp.log(rpar)) * mp.conj(yv[Js[i]]) for i, (rr, mu) in enumerate(Z)]
err = max(err, max(abs(a - b) for a, b in zip(Kr(Kr(y)), y)))
err = max(err, abs(ip(Kr(y), Kr(y)) - ip(y, y)))
Omega = lambda Ff: (lambda sv: mp.conj(Ff(1 - mp.conj(sv))))
lhs = mp.conj(sigma(y, Omega(Ftest)))                       # Omega^vee sigma_r(ybar) at F
rhs = sigma(Kr(y), Ftest)                                   # sigma_r(conj(K_r y)) at F
err = max(err, abs(lhs - rhs))
err = max(err, max(abs(a - b) for a, b in zip(beta(Omega(Ftest)), Kr(beta(Ftest)))))
# Omega T_n Omega = U_n pointwise
for n in (2, 3):
    Tn = lambda Ff, n=n: (lambda sv: mp.power(n, sv) * Ff(sv))
    for sv in (mp.mpc(0.2, 3), mp.mpc(-1.1, 0.4)):
        err = max(err, abs(Omega(Tn(Omega(Ftest)))(sv) - mp.power(n, 1 - sv) * Ftest(sv)))
# HBW6.2: sigma_r(conj e_rho) = m_rho conj(d_r(rho)) eps_{rho#,0}
for i, (rr, mu) in enumerate(Z):
    e = [mp.mpc(0)] * len(Z); e[i] = mp.mpc(1)
    err = max(err, abs(sigma(e, Ftest) - mu * mp.conj(d_r(rpar, rr)) * Ftest(sharp(rr))))
report("C17", "d_r(rho#)=-d_r, e^{2i gamma log r}d_r=conj d_r, d_r=conj(r^rho-r^{rho#}); sigma formula; K_r^2=1, isometry; HSR8.4, HSR8.8; Omega T_n Omega=U_n; HBW6.2",
       err, mp.mpf(10) ** -40)

# ======================================================================
# C18  HSR3.1, HSR7.2-7.5, HSR6.4, HSR10.2, HSR10.4, HSRA8.1, HBW9 coefficient identity (synthetic divisor)
tt = mp.mpf('0.004')   # small t keeps synthetic Gaussian factors O(1)
def Xi_coef(yv, m, r=rpar, t=tt):
    return sum(mult[i] * d_r(r, rr) * yv[i] * mp.exp(t * (1 - rr) ** 2) * phi(m, 1 - rr) for i, (rr, mu) in enumerate(Z))
scale = max(abs(Xi_coef(y, m)) for m in range(8))
err = 0
for n in (2, 3):
    Tny = [mp.power(n, rr) * y[i] for i, (rr, mu) in enumerate(Z)]
    for m in range(0, 7):
        W = sum(Xi_coef(y, n * m + a) for a in range(n))
        err = max(err, abs(W - Xi_coef(Tny, m)) / scale)
    bT = beta(lambda sv, n=n: mp.power(n, sv) * Ftest(sv))
    Ustar_b = [mp.conj(mp.power(n, 1 - rr)) * v for (rr, mu), v in zip(Z, beta(Ftest))]
    err = max(err, max(abs(a - b) for a, b in zip(bT, Ustar_b)))
    bU = beta(lambda sv, n=n: mp.power(n, 1 - sv) * Ftest(sv))
    Tstar_b = [mp.conj(mp.power(n, rr)) * v for (rr, mu), v in zip(Z, beta(Ftest))]
    err = max(err, max(abs(a - b) for a, b in zip(bU, Tstar_b)))
    for rr, mu in Z:   # T_n^* - U_n = D_n (defect at scale n)
        err = max(err, abs(mp.conj(mp.power(n, rr)) - mp.power(n, 1 - rr) - d_r(n, rr)))
        err = max(err, abs(mp.power(n, 1 - mp.conj(rr)) - n / mp.conj(mp.power(n, rr))))   # U_n^* = n (T_n^*)^{-1}
# HSR6.4 Gram pairing
gram = ip(beta(Ftest), beta(Gtest))
gram2 = sum(mu * abs(d_r(rpar, rr)) ** 2 * Ftest(sharp(rr)) * mp.conj(Gtest(sharp(rr))) for rr, mu in Z)
err = max(err, abs(gram - gram2))
# HSR10.2 parameter change and HSR10.4 Gaussian change
s2 = mp.mpf('5.5'); t2 = mp.mpf('0.009'); Delta = t2 - tt
offmask = [mp.re(rr) != 0.5 for rr, mu in Z]
yO = [v if o else mp.mpc(0) for v, o in zip(y, offmask)]
Vy = [(d_r(rpar, rr) / d_r(s2, rr) * yO[i]) if offmask[i] else 0 for i, (rr, mu) in enumerate(Z)]
Gy = [mp.exp(Delta * (1 - rr) ** 2) * yO[i] for i, (rr, mu) in enumerate(Z)]
for m in range(0, 6):
    err = max(err, abs(Xi_coef(yO, m, rpar, tt) - Xi_coef(Vy, m, s2, tt)) / scale)
    err = max(err, abs(Xi_coef(yO, m, rpar, t2) - Xi_coef(Gy, m, rpar, tt)) / scale)
# HSRA8.1: K_r G y = e^{-Delta} c^rho e^{Delta(1-rho)^2} (K_r y), c = e^{2 Delta}
KG = Kr(Gy); Ky = Kr(yO)
for i, (rr, mu) in enumerate(Z):
    err = max(err, abs(KG[i] - mp.exp(Delta * rr ** 2) * Ky[i]))
    err = max(err, abs(KG[i] - mp.exp(-Delta) * mp.exp(2 * Delta * rr) * mp.exp(Delta * (1 - rr) ** 2) * Ky[i]))
# HBW9 / HBWR7: C_{t'}(1-rho)(V y)_rho = e^{-2 pi i k rho} C_t(1-rho) y_rho
Ct = lambda t, sv: -mp.exp(t * sv ** 2) * mp.gamma(2 - sv) / sv
for k in (-2, 1, 3):
    tb, tp = mp.mpf('0.02'), mp.mpf('0.013')
    for i, (rr, mu) in enumerate(Z):
        Vk = mp.exp(-2j * mp.pi * k * rr) * mp.exp((tb - tp) * (1 - rr) ** 2) * y[i]
        lhs = Ct(tp, 1 - rr) * Vk
        rhs = mp.exp(-2j * mp.pi * k * rr) * Ct(tb, 1 - rr) * y[i]
        err = max(err, abs(lhs - rhs) / abs(rhs))
report("C18", "W_n^*Xi=Xi T_n; beta T_n=U_n^* beta, beta U_n=T_n^* beta; T_n^*-U_n=D_n; Gram HSR6.4; Xi_r=Xi_s V_rs; Xi_t2=Xi_t1 G; HSRA8.1; HBW9 coefficient",
       err, mp.mpf(10) ** -35)

# ======================================================================
# C19  HSR10.1 limit and 24_ Lemma 24.5 range; HSR10.5 singular values; HSR7.3 norms <= n and <= 1
err = 0
for r, q in ((2.7, 5.5), (1.3, 9.0), (30.0, 2.0)):
    r = mp.mpf(r); q = mp.mpf(q)
    lim = mp.sqrt(r) * mp.log(r) / (mp.sqrt(q) * mp.log(q))
    for xx in (mp.mpf(10) ** -12, mp.mpf('0.1'), mp.mpf('0.49')):
        bx = mp.mpf('0.5') + xx
        ratio = (mp.power(r, bx) - mp.power(r, 1 - bx)) / (mp.power(q, bx) - mp.power(q, 1 - bx))
        err = max(err, abs(ratio - mp.sqrt(r / q) * mp.sinh(xx * mp.log(r)) / mp.sinh(xx * mp.log(q))) / abs(ratio))
        lo, hi = sorted([lim, (r - 1) / (q - 1)])
        if not (lo - mp.mpf(10) ** -9 <= ratio <= hi + mp.mpf(10) ** -9):
            err = 1
    err = max(err, abs(((mp.power(r, 0.5 + mp.mpf(10) ** -20) - mp.power(r, 0.5 - mp.mpf(10) ** -20)) /
                        (mp.power(q, 0.5 + mp.mpf(10) ** -20) - mp.power(q, 0.5 - mp.mpf(10) ** -20))) - lim))
Delta = mp.mpf('0.7')
for rr, mu in Z:
    sv_ = mp.exp(Delta * ((1 - mp.re(rr)) ** 2 - mp.im(rr) ** 2))
    err = max(err, abs(abs(mp.exp(Delta * (1 - rr) ** 2)) - sv_) / sv_)
    for n in (2, 5):
        if not (1 <= abs(mp.power(n, rr)) <= n):
            err = 1
    if not abs(d_r(rpar, rr)) < rpar - 1:
        err = 1
report("C19", "HSR10.1 ratio -> sqrt(r)log r/(sqrt(s)log s), lies in 24_ Lemma 24.5 range; HSR10.5 s_rho; 1<=|n^rho|<=n; |d_r|<r-1 (sharper than HSR3 r+1)", err, mp.mpf(10) ** -18)

# ======================================================================
# C20  HBW9.2 / HBWR7.2: 2 pi k gamma + delta((1-beta)^2-gamma^2) <= delta + pi^2 k^2/delta
worst = -mp.inf
for delta in (mp.mpf('0.1'), mp.mpf('0.5'), mp.mpf(2)):
    for k in range(-4, 5):
        for b in (mp.mpf('0.001'), mp.mpf('0.3'), mp.mpf('0.999')):
            gstar = mp.pi * k / delta
            for gm in [gstar + mp.mpf(j) / 50 for j in range(-100, 101)]:
                val = 2 * mp.pi * k * gm + delta * ((1 - b) ** 2 - gm ** 2) - (delta + mp.pi ** 2 * k ** 2 / delta)
                worst = max(worst, val)
report("C20", "HBW9.2: log|diag V_{k;t,t'}| <= delta + pi^2 k^2/delta (max excess over grid, must be <= 0)", max(worst, 0), 0,
       f"[max excess {mp.nstr(worst, 3)}]")

# ======================================================================
# C21  HBW8.7/HBW2.2 at the actual zero rho_1: remainder R_{t,1-rho}(u) = O(u), compared relative to C_t
tt = mp.mpf(1); sv = 1 - rho1
Ct1 = -mp.exp(tt * sv ** 2) * mp.gamma(2 - sv) / sv
Ct_formula = -mp.exp(tt * (1 - rho1) ** 2) * mp.gamma(1 + rho1) / (1 - rho1)       # a_rho / (d_r y)
err = relerr(Ct1, Ct_formula)
rows = []
mp.mp.dps = 40
for uv in (mp.mpf('0.2'), mp.mpf('0.05'), mp.mpf('0.0125')):
    full = g(tt, sv) * K_s(sv, mp.exp(-uv))
    sing = Ct1 * (mp.exp(uv) - 1) * mp.power(uv, -1 - rho1)
    Rser = mp.exp(tt * sv ** 2) * (mp.exp(uv) - 1) / sv * A_series(sv, uv, 1, K=80)
    err = max(err, abs(full - sing - Rser) / max(abs(sing), abs(full)))
    rows.append(abs(full - sing) / abs(Ct1))
mp.mp.dps = 50
ratios = [rows[i] / rows[i + 1] for i in range(2)]
report("C21", "HBW8.7 at rho_1: C_t(1-rho)=-e^{t(1-rho)^2}Gamma(1+rho)/(1-rho); g K_{1-rho}(e^{-u}) = sing + R, R=O(u) (rel. to C_t)",
       err, mp.mpf(10) ** -25, f"[|R|/|C_t| at u=.2,.05,.0125: {', '.join(mp.nstr(v, 3) for v in rows)}; successive ratios {', '.join(mp.nstr(v, 3) for v in ratios)} (~4 => O(u))]")

# ======================================================================
# C22  HBW8.12 isolator at rho_1: F_rho(rho)=1, F_rho(rho_2)=0; F0'(rho_1) != 0
d1 = mp.diff(F0, rho1)
iso = lambda sv: F0(sv) / (d1 * (sv - rho1))
e1 = abs(iso(rho1 + mp.mpf(10) ** -22) - 1)
e2 = abs(iso(rho2)) / abs(mp.diff(F0, rho2) / d1)
report("C22", "HBW8.12 isolator F0/(F0'(rho)(s-rho)): value 1 at rho_1, 0 at rho_2; |F0'(rho_1)| > 0", max(e1, e2), mp.mpf(10) ** -18,
       f"[|F0'(rho_1)| = {mp.nstr(abs(d1), 5)}]")

# ======================================================================
# C23  (audit, negative result) Hardy membership: |phi_m(s)| m^{Re s} -> |1-s|/|s|; K_{1-rho} in H^2 iff Re rho < 1/2
err = 0
for sv in (mp.mpc('0.3', '2'), mp.mpc('0.7', '2'), 1 - rho1):
    lim = abs(1 - sv) / abs(sv)
    vals = [abs(phi(m, sv)) * mp.power(m, mp.re(sv)) for m in (10 ** 4, 10 ** 6, 10 ** 8)]
    err = max(err, abs(vals[-1] - lim) / lim)
report("C23", "|phi_m(s)| ~ |1-s| m^{-Re s}/|s| (so sum|phi_m(1-rho)|^2<inf iff Re rho<1/2): rel. dev. at m=1e8",
       err, mp.mpf(10) ** -6)

# ======================================================================
# C24  HSR0.4 multinomial Leibniz formula for F0^{(j)}
mp.mp.dps = 40
sv = mp.mpc(2, 1); err = 0
P = lambda z: z * (z - 1) / 8
Pd = [P(sv), (2 * sv - 1) / 8, mp.mpf(1) / 4] + [0] * 5
for j in range(0, 4):
    tot = 0
    for j0, j1, j2 in itertools.product(range(j + 1), repeat=3):
        j3 = j - j0 - j1 - j2
        if j3 < 0:
            continue
        mc = mp.factorial(j) / (mp.factorial(j0) * mp.factorial(j1) * mp.factorial(j2) * mp.factorial(j3))
        tot += (mc * Pd[j0] * (-mp.log(mp.pi) / 2) ** j1 * mp.power(mp.pi, -sv / 2)
                * mp.mpf(2) ** (-j2) * mp.diff(mp.gamma, sv / 2, j2) * mp.zeta(sv, 1, j3))
    err = max(err, relerr(tot, mp.diff(F0, sv, j)))
mp.mp.dps = 50
report("C24", "HSR0.4 four-factor Leibniz formula for F0^{(j)}(s), j<=3 at s=2+i", err, mp.mpf(10) ** -20)

# ======================================================================
print()
print(f"SUMMARY: {sum(RESULTS)} PASS / {len(RESULTS) - sum(RESULTS)} FAIL (of {len(RESULTS)} recorded outcomes)")
sys.exit(0 if all(RESULTS) else 1)
