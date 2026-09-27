#!/usr/bin/env python3
"""ref_G_independent.py -- referee check of the evaluator GGa of certify_hydro_radius.py (note 51_, Theorem 51.2).

The functions tails() and GGa() are extracted verbatim from ../certify_hydro_radius.py with the ast module (the script
itself is not executed), and compared with three independent evaluations at random complex points of the certified
domain |alpha| <= 0.95, |x| <= 0.2:
  (1) mpmath modified Bessel functions:  G = Gamma(1+alpha) (q/2)^(-alpha) q I'_alpha(q),  q = 2 sqrt(x),
      I'_alpha = (I_{alpha-1} + I_{alpha+1})/2;  G_alpha by mpmath numerical differentiation of the same expression;
  (2) Arb 0F1 (python-flint acb.hypgeom_0f1):  G = alpha 0F1(;1+alpha;x) + (2x/(1+alpha)) 0F1(;2+alpha;x);
  (3) direct mpmath summation of the series to 400 terms at 60 digits.
It checks that the independent values lie inside the Arb balls returned by GGa (point and box arguments), and that the
tail bounds 2 b_M, 2 d_M dominate the true tails at the worst corner of the domain.
"""
import ast, random, math
import mpmath as mp
from flint import acb, arb, ctx

SRC = '/home/claude/work/claude_grind_20260925/checks/ns51/certify_hydro_radius.py'
tree = ast.parse(open(SRC).read())
ns = {}
exec("import math\nfrom flint import acb, arb, ctx\nctx.prec = 128", ns)
keep_assign = {'M', 'AMAX', 'XMAX', 'FACT'}
for node in tree.body:
    if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id in keep_assign for t in node.targets):
        exec(compile(ast.Module([node], []), SRC, 'exec'), ns)
    if isinstance(node, ast.For) and ast.unparse(node).startswith('for m in range(1, M + 2)'):
        exec(compile(ast.Module([node], []), SRC, 'exec'), ns)
    if isinstance(node, ast.FunctionDef) and node.name in ('tails', 'GGa'):
        exec(compile(ast.Module([node], []), SRC, 'exec'), ns)
GGa = ns['GGa']; tails = ns['tails']; M = ns['M']
print(f"extracted GGa, tails from {SRC}; M = {M}")

mp.mp.dps = 60
res = []
def check(name, ok):
    res.append((name, bool(ok))); print(("PASS" if ok else "FAIL") + "  " + name)

def G_bessel(al, x):
    q = 2 * mp.sqrt(x)
    Ip = (mp.besseli(al - 1, q) + mp.besseli(al + 1, q)) / 2
    return mp.gamma(1 + al) * (q / 2) ** (-al) * q * Ip

def G_series(al, x, N=400):
    s = mp.mpc(0); base = mp.mpc(1)
    for m in range(N):
        if m > 0:
            base = base * x / (m * (m + al))
        s += (al + 2 * m) * base
    return s

def contains(ball, z, slack=0):
    re, im = ball.real, ball.imag
    return (abs(mp.mpf(re.mid().str(40, radius=False)) - z.real) <= mp.mpf(re.rad().str(20, radius=False)) + slack and
            abs(mp.mpf(im.mid().str(40, radius=False)) - z.imag) <= mp.mpf(im.rad().str(20, radius=False)) + slack)

random.seed(20260927)
npts = 60
bad_b = bad_d = bad_f = bad_s = 0
maxdiff = 0
for k in range(npts):
    ra = 0.95 * math.sqrt(random.random()); ta = random.uniform(-math.pi, math.pi)
    rx = 0.2 * math.sqrt(random.random()); tx = random.uniform(-math.pi, math.pi)
    a = complex(ra * math.cos(ta), ra * math.sin(ta)); x = complex(rx * math.cos(tx), rx * math.sin(tx))
    A = acb(a.real, a.imag); X = acb(x.real, x.imag)
    G, Ga = GGa(A, X)
    al = mp.mpc(a.real, a.imag); xx = mp.mpc(x.real, x.imag)
    gb = G_bessel(al, xx)
    gab = mp.diff(lambda t: G_bessel(t, xx), al)
    gs = G_series(al, xx)
    # 0F1 route (Arb)
    g0 = A * X.hypgeom_0f1(1 + A) + 2 * X / (1 + A) * X.hypgeom_0f1(2 + A)
    bad_b += not contains(G, gb, mp.mpf('1e-40'))
    bad_d += not contains(Ga, gab, mp.mpf('1e-30'))
    bad_s += not contains(G, gs, mp.mpf('1e-45'))
    bad_f += not G.overlaps(g0)
    maxdiff = max(maxdiff, abs(gb - gs))
check(f"GGa ball contains the mpmath-Bessel value of G at {npts} random points (|alpha|<=0.95, |x|<=0.2)", bad_b == 0)
check(f"GGa ball contains the mpmath numerical alpha-derivative of the Bessel expression at {npts} points", bad_d == 0)
check(f"GGa ball contains the 400-term mpmath series value at {npts} points", bad_s == 0)
check(f"GGa ball overlaps the Arb 0F1 representation alpha 0F1(1+a;x) + 2x/(1+a) 0F1(2+a;x) at {npts} points", bad_f == 0)
print(f"   max |G_Bessel - G_series| = {mp.nstr(maxdiff, 3)}")

# box arguments: random sub-boxes; the independent value at random points of the box must lie in the box enclosure
bad = 0
for k in range(40):
    ca = complex(random.uniform(-0.8, 0.8), random.uniform(-0.5, 0.5)); cx = complex(random.uniform(-0.14, 0.14), random.uniform(-0.14, 0.14))
    ha = random.choice([1e-6, 1e-4, 1e-2]); hx = random.choice([1e-6, 1e-4, 1e-3])
    A = acb(arb(ca.real, ha), arb(ca.imag, ha)); X = acb(arb(cx.real, hx), arb(cx.imag, hx))
    G, Ga = GGa(A, X)
    for j in range(5):
        a = mp.mpc(ca.real + random.uniform(-ha, ha), ca.imag + random.uniform(-ha, ha))
        x = mp.mpc(cx.real + random.uniform(-hx, hx), cx.imag + random.uniform(-hx, hx))
        if not contains(G, G_bessel(a, x), mp.mpf('1e-40')):
            bad += 1
        if not contains(Ga, mp.diff(lambda t: G_bessel(t, x), a), mp.mpf('1e-30')):
            bad += 1
check("box enclosures GGa(A, X) contain Bessel values/derivatives at 200 random interior points of 40 random boxes", bad == 0)

# tail bounds at the worst corner a = 0.95, X = 0.2 (alpha = -0.95 minimises |k + alpha|; |x| = 0.2 on a circle)
tG, tGa = tails(arb('0.95'), arb('0.2'))
worstG = worstGa = mp.mpf(0)
for th in [0, 0.5, 1, 2, 3, math.pi]:
    al = mp.mpf('-0.95'); x = mp.mpf('0.2') * mp.expj(th)
    base = mp.mpc(1); S = mp.mpc(0); tailG = mp.mpc(0); tailGa = mp.mpc(0)
    for m in range(0, 200):
        if m > 0:
            inv = 1 / (m + al); base = base * x * inv / m; S += inv
        if m >= M:
            tailG += (al + 2 * m) * base; tailGa += base * (1 - (al + 2 * m) * S)
    worstG = max(worstG, abs(tailG)); worstGa = max(worstGa, abs(tailGa))
check(f"true tail |sum_(m>=30) t_m| = {mp.nstr(worstG, 4)} <= 2 b_M = {tG}", worstG <= mp.mpf(tG.str(40, radius=False)))
check(f"true tail |sum_(m>=30) dt_m/dalpha| = {mp.nstr(worstGa, 4)} <= 2 d_M = {tGa}", worstGa <= mp.mpf(tGa.str(40, radius=False)))
# the stated ratio bounds for m >= 30 (a = 0.95, X = 0.2), checked exactly in rationals for 30 <= m <= 2000
from fractions import Fraction as Fr
a = Fr(95, 100); X = Fr(1, 5)
okr = True; H = sum(Fr(1) / (k - a) for k in range(1, 31)); worst_rb = worst_rd = Fr(0)
for m in range(30, 2001):
    b_ratio = (a + 2 * m + 2) / (a + 2 * m) * X / ((m + 1) * (m + 1 - a))
    Hn = H + Fr(1) / (m + 1 - a)
    d_ratio = X / ((m + 1) * (m + 1 - a)) * (1 + (a + 2 * m + 2) * Hn) / (1 + (a + 2 * m) * H)
    okr &= b_ratio <= 2 * X / ((m + 1) * (m + 1 - a)) <= Fr(1, 2) and d_ratio <= 5 * X / ((m + 1) * (m + 1 - a)) <= Fr(1, 2)
    worst_rb = max(worst_rb, b_ratio); worst_rd = max(worst_rd, d_ratio)
    H = Hn
check(f"ratio bounds b_(m+1)/b_m <= 2X/((m+1)(m+1-a)) <= 1/2 and d_(m+1)/d_m <= 5X/(...) <= 1/2 for 30 <= m <= 2000 "
      f"(worst ratios {float(worst_rb):.2e}, {float(worst_rd):.2e})", okr)
# analytic reason for all m >= 30: (a+2m+2)/(a+2m) <= 1 + 1/m <= 2, and
# (1 + (a+2m+2)H_{m+1})/(1 + (a+2m)H_m) <= (a+2m+2)/(a+2m) + (a+2m+2)/((m+1-a)(1+(a+2m)H_m)) <= 1 + 1/30 + 1 < 5.
n = len(res); npass = sum(ok for _, ok in res)
print(f"\nsummary: {n} checks, {npass} PASS, {n - npass} FAIL")
