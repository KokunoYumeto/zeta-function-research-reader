# Checks for the Yang-Mills reader: the heat and complement constants of HEAT_AND_COMPLEMENT.md (H9-H30),
# recomputed from the fifth-reference rationals (F26) and the manuscript's stated inherited row bounds only.
# The constants 8, 32, 1/8, 30 and 48 are checked here as arithmetic of the manuscript's formulas; their derivations are in the
# reader (Propositions 4.2 and 4.5), and ymr_referee_checks.py checks the sharpened constants of version 2.
# Prepared by Claude (Opus 5.5).  Needs sympy and mpmath.
from fractions import Fraction as F
import itertools, sympy as sp, mpmath as mp
mp.mp.dps = 50
ok = True
def check(name, cond, val=None):
    global ok
    ok &= bool(cond)
    print(("PASS " if cond else "FAIL ") + name + ("" if val is None else f"  [{val}]"))

m = {1: F(64, 3), 2: F(5834, 39), 3: F(336572872, 208845),
     4: F(17270702970768271, 341697152160), 5: F(1638684)}
t = {1: F(16, 3), 2: F(137, 6), 3: F(225985217, 1253070),
     4: F(110695177857394584026401, 18025447358750832000), 5: F(190128)}
def ell(x): return sum((m[i] + 4 * t[i]) * x**i for i in range(1, 6))
def delta(x): return sum(3 * (m[i] * t[j] + m[j] * t[i]) * x**(i + j) for i in range(1, 6) for j in range(1, 6) if i + j >= 6)
def D(x): return (1 - ell(x))**2 - F(8, 3) * delta(x)
def s(x): return sum((F(3, 2) * m[i] - 6 * t[i]) * x**i for i in range(1, 6))
def d5_gt(x, c):
    """exact test d5(x) > c, with d5 = 3/2 (1 + sqrt D) + s"""
    rhs = (c - s(x)) * F(2, 3) - 1          # need sqrt(D) > rhs
    if D(x) < 0: return False
    return rhs < 0 or D(x) > rhs * rhs
def d5_float(x):
    return 1.5 * (1 + mp.sqrt(mp.mpf(D(x).numerator) / D(x).denominator)) + mp.mpf(s(x).numerator) / s(x).denominator

# H9: t(G_z) <= 4 faces * spin 1/2 * norm 8 = 16, and F10 gives ||Gamma(h,G_z)|| <= 2 t ||Kh|| = 32 ||Kh||
check("H9: t(G_z) <= 4*(1/2)*8 = 16, so 2*t = 32", 4 * F(1, 2) * 8 == 16 and 2 * 16 == 32)
# plaquette trace norm 2^(l-k): l = 4 occurrences, 2k = 2 cyclic sign changes (+,+,-,-)
signs = [1, 1, -1, -1]; changes = sum(1 for i in range(4) if signs[i] != signs[(i + 1) % 4])
check("F12 for a plaquette: ||A||_1 = 2^(l-k) = 8", changes == 2 and 2**(4 - changes // 2) == 8)
# H10: |P_H Gamma(h,G_z)| = 3|sum z_q a_q| <= 3 sum|a_q| and ||Kh|| >= 3*8*sum|a_q|
check("H10: 3 / (3*8) = 1/8", F(3, 3 * 8) == F(1, 8))
# H11: (1/8 + 32 chi/(1-chi)) * 8/(1-chi) = (1 + 255 chi)/(1-chi)^2
c = sp.symbols('chi')
check("H11 identity (1/8 + 32chi/(1-chi))*8/(1-chi) = (1+255chi)/(1-chi)^2",
      sp.simplify((sp.Rational(1, 8) + 32 * c / (1 - c)) * 8 / (1 - c) - (1 + 255 * c) / (1 - c)**2) == 0)
# H12
R = F(1, 55)
lo, hi = F(18, 1000), F(19, 1000)
for _ in range(90):
    mid = (lo + hi) / 2
    lo, hi = (mid, hi) if D(mid) > 0 else (lo, mid)
check("H12: R = 1/55 < alpha_5", R < lo, float(lo))
check("H12: d5(1/55) > 13/8 (exact test), i.e. chi(1/55) < 11/24", d5_gt(R, F(13, 8)), mp.nstr(d5_float(R), 12))
C = (1 + 255 * F(11, 24)) / (1 - F(11, 24))**2
check("H12: C = (1+255*11/24)/(13/24)^2 = 67896/169", C == F(67896, 169), C)
check("H12: 3(1-chi) >= 3*13/24 = 13/8 (the decay rate)", 3 * (1 - F(11, 24)) == F(13, 8))
# H13: Cauchy tail on the circle R for an even function: sum_{n>=3} (x/R)^(2n) = (x/R)^6/(1-(x/R)^2)
x = sp.symbols('x', positive=True)
check("H13: sum_{n>=3} q^(2n) = q^6/(1-q^2)", sp.simplify(sp.summation(sp.Symbol('q')**(2 * sp.Symbol('n', integer=True)), (sp.Symbol('n', integer=True), 3, sp.oo)).rewrite(sp.Piecewise).args[0][0] - sp.Symbol('q')**6 / (1 - sp.Symbol('q')**2)) == 0)
# centre map: U_(n,i) -> (-1)^(sum_{k<i} n_k) U_(n,i) sends every W_p to -W_p (all faces of the L=2 box)
L = 2
def sgn(n, i): return (-1)**sum(n[k] for k in range(i))
allneg = True; nf = 0
for n in itertools.product(range(-L, L + 1), repeat=3):
    for i in range(3):
        for j in range(i + 1, 3):
            ei = tuple(1 if k == i else 0 for k in range(3)); ej = tuple(1 if k == j else 0 for k in range(3))
            n_i = tuple(a + b for a, b in zip(n, ei)); n_j = tuple(a + b for a, b in zip(n, ej))
            if max(n_i[i], n_j[j]) > L: continue
            nf += 1
            prod = sgn(n, i) * sgn(n_i, j) * sgn(n_j, i) * sgn(n, j)
            allneg &= (prod == -1)
check(f"centre map multiplies every one of the {nf} faces of the L=2 box by -1 (M_2 = 240)", allneg and nf == 240)
# H17: int_0^oo |9tau-6| e^{-d tau} dtau = 6/d - 9/d^2 + 18/d^2 e^{-2d/3}
d, tau = sp.symbols('d tau', positive=True)
I = sp.integrate((6 - 9 * tau) * sp.exp(-d * tau), (tau, 0, sp.Rational(2, 3))) + sp.integrate((9 * tau - 6) * sp.exp(-d * tau), (tau, sp.Rational(2, 3), sp.oo))
check("H17: signed-weight integral identity", sp.simplify(I - (6 / d - 9 / d**2 + 18 / d**2 * sp.exp(-2 * d / 3))) == 0)
check("H17: exp(-13/12) < 339/1000", mp.e**(-mp.mpf(13) / 12) < mp.mpf(339) / 1000, mp.nstr(mp.e**(-mp.mpf(13) / 12), 10))
dd = F(13, 8)
CJ = C * (1 + 6 / dd - 9 / dd**2 + 18 * F(339, 1000) / dd**2)
check("H18: C_J = 5156090136/3570125", CJ == F(5156090136, 3570125), CJ)
check("H18: C_J < C(1 + 6/d + 9/d^2)", CJ < C * (1 + 6 / dd + 9 / dd**2))
# H14 kinetic diagonal: Gamma(W_p,W_p) = 4 - W_p^2 = 3 - chi_1 ; ||chi_1||_X = 9 * 3 = 27 (spin-1 character on 4 links: dim 3^4? no:)
# (the manuscript's 30 = 3 + 27 and 606 = 30 + 12*48 are checked as arithmetic only)
check("H14 arithmetic: 3 + 27 = 30 and 30 + 12*48 = 606", 3 + 27 == 30 and 30 + 12 * 48 == 606)

# H19-H30 at the benchmark couplings, from the stated inherited row bounds
B = {'0': (F(149, 468), F(2361994073, 4691494080)), '1': (F(97, 468), F(376882691, 938298816)),
     '2': (F(73313, 657072), F(982069718963833, 3919180324550400)), 'K': (F(187, 468), F(586668421, 1563831360)),
     'J': (F(6779, 73008), F(152338674005989, 435464480505600))}
def widths(xv):
    u = (55 * xv)**6 / (1 - (55 * xv)**2)
    w = {k: B[k][0] * xv**2 + B[k][1] * xv**4 + C / dd**int(k) * u for k in '012'}
    w['K'] = B['K'][0] * xv**2 + B['K'][1] * xv**4 + 606 * u
    beta = B['J'][0] * xv**2 + B['J'][1] * xv**4 + CJ * u
    return w, beta
def floor4(v): return F(int(v * 10000), 10000)
rows = [(10, F(977, 1000), F(11, 1000), F(12, 1000)), (12, F(997, 1000), F(12, 10000), F(12, 10000)),
        (F(25, 2), F(998, 1000), F(1, 1000), F(1, 1000)), (13, F(999, 1000), F(1, 2000), F(1, 2000)),
        (16, F(9999, 10000), F(1, 25000), F(1, 25000))]
for g2, obs, loss, inc in rows:
    xv = 1 / (4 * F(g2)**2)
    w, beta = widths(xv)
    l = {k: F(1, 3**int(k)) - w[k] for k in '012'}; uu = {k: F(1, 3**int(k)) + w[k] for k in '012'}
    dph = F(29047, 10000) if g2 == 13 else floor4(d5_float(xv))
    check(f"g^2 = {g2}: d_ph = {dph} is below d5(xi)", d5_gt(xv, dph) or d5_float(xv) >= dph)
    fr = l['1']**2 / (uu['0'] * uu['2']); etaE = beta / (dph * l['1']); etaG = beta / (dph**2 * l['2'])
    check(f"g^2 = {g2}: observed fraction > {obs}, energy loss < {loss}, state increase < {inc}",
          fr > obs and etaE < loss and etaG < inc, f"{float(fr):.11f}, {float(etaE):.11f}, {float(etaG):.11f}")
    if g2 == 13:
        check("g^2 = 13 diagnostics match the manuscript (0.99904459483, 0.00043585425, 0.00045023706)",
              abs(float(fr) - 0.99904459483) < 1e-10 and abs(float(etaE) - 0.00043585425) < 1e-10 and abs(float(etaG) - 0.00045023706) < 1e-10)
        check("H30 at g^2 = 13: widths below 119, 73, 45, 178 (x 1e-6)",
              w['0'] < F(119, 10**6) and w['1'] < F(73, 10**6) and w['2'] < F(45, 10**6) and w['K'] < F(178, 10**6),
              [float(w[k]) for k in ('0', '1', '2', 'K')])
    if g2 == 16:
        uK = 3 + w['K']
        check("H29 at g^2 = 16: section-energy change u1*uK/l0^2 - 1 < 1/20000", uu['1'] * uK / l['0']**2 - 1 < F(1, 20000),
              float(uu['1'] * uK / l['0']**2 - 1))
# continuum path: xi_n = c_n^2/4 <= alpha_5  <=>  c_n <= 2 sqrt(alpha_5);  xi_n < 1/55  <=>  c_n < 2/sqrt(55)
# (version 2: the earlier check here was vacuous; it now computes the two endpoints of Proposition 3.6)
a5v = mp.mpf(lo.numerator) / lo.denominator
check("path scope: 2 sqrt(alpha_5) = 0.27147... and 2/sqrt(55) = 0.26968..., and (c^2/4 at these c) = alpha_5 and 1/55",
      abs(2 * mp.sqrt(a5v) - mp.mpf('0.271477')) < 1e-5 and abs(2 / mp.sqrt(55) - mp.mpf('0.269680')) < 1e-5
      and abs((2 * mp.sqrt(a5v))**2 / 4 - a5v) < 1e-40 and abs((2 / mp.sqrt(55))**2 / 4 - mp.mpf(1) / 55) < 1e-40)
# other radii R < alpha_5 (floating point): C(R) = (1+255 chi)/(1-chi)^2 with chi = 1 - d5(R)/3, rate d5(R)
vals = []
for Rr in (F(1, 55), F(184, 10000)):
    dR = d5_float(Rr); chiR = 1 - dR / 3; vals.append((float(Rr), float(dR), float((1 + 255 * chiR) / (1 - chiR)**2)))
check("other radii: at R = 1/55 exact chi gives C = 391.98 and rate 1.6376; at R = 0.0184, C = 443.37 and rate 1.5747",
      abs(vals[0][2] - 391.979) < 0.01 and abs(vals[0][1] - 1.63763) < 1e-4 and abs(vals[1][2] - 443.369) < 0.01 and abs(vals[1][1] - 1.57467) < 1e-4, vals)
print("ALL PASS" if ok else "SOME CHECK FAILED")
