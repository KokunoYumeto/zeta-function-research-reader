# ymr_referee_checks.py -- claude-ab (Opus 5.5), 27 September 2026.
# Checks of the YM referee findings adopted in the YM reader, version 2, recomputed from the fifth-reference
# rationals (F26), the manuscript's inherited row bounds, and the first-pass audit's order-2 values.
from fractions import Fraction as F
import random, mpmath as mp
mp.mp.dps = 50
ok = True
def check(name, cond, val=None):
    global ok
    ok &= bool(cond)
    print(("PASS " if cond else "FAIL ") + name + ("" if val is None else f"  [{val}]"))
m = {1: F(64, 3), 2: F(5834, 39), 3: F(336572872, 208845), 4: F(17270702970768271, 341697152160), 5: F(1638684)}
t = {1: F(16, 3), 2: F(137, 6), 3: F(225985217, 1253070), 4: F(110695177857394584026401, 18025447358750832000), 5: F(190128)}
def mk(mm, tt, N):
    def ell(x): return sum((mm[i] + 4 * tt[i]) * x**i for i in range(1, N + 1))
    def delta(x): return sum(3 * (mm[i] * tt[j] + mm[j] * tt[i]) * x**(i + j) for i in range(1, N + 1) for j in range(1, N + 1) if i + j >= N + 1)
    def D(x): return (1 - ell(x))**2 - F(8, 3) * delta(x)
    def s(x): return sum((F(3, 2) * mm[i] - 6 * tt[i]) * x**i for i in range(1, N + 1))
    def d(x):
        Dx = D(x); Dv = mp.mpf(Dx.numerator) / Dx.denominator
        return mp.mpf(3) / 2 * (1 + mp.sqrt(max(Dv, 0))) + mp.mpf(s(x).numerator) / s(x).denominator
    def alpha():
        lo, hi = F(0), F(1, 20)
        # first positive root: bisection on the first sign change (D(0)=1>0)
        for _ in range(200):
            mid = (lo + hi) / 2
            # ensure D stays positive on [0, mid] by scanning coarse grid
            lo, hi = (mid, hi) if D(mid) > 0 and all(D(mid * k / 64) > 0 for k in range(1, 64)) else (lo, mid)
        return lo
    return D, d, alpha
# ---- Finding 1: order-2 threshold with the first pass's values rounded up
m2, t2 = F(1340674, 10**4), F(197954, 10**4)
s3 = F(17320509, 10**7); check("sqrt(3) < 1.7320509", s3 * s3 > 3)
m2up = 6 + F(11200, 117) + F(112, 9) + F(448, 39) * s3; t2up = F(3, 2) + F(80, 9) + F(256, 39) + F(64, 39) * s3
check("closed forms bounded: m(v2) < 134.0674, t(v2) < 19.7954", m2up < m2 and t2up < t2, (float(m2up), float(t2up)))
check("closed forms agree with the first pass's 134.0673186784, 19.7953312398 to 1e-9",
      abs(float(6 + F(11200, 117) + F(112, 9)) + float(F(448, 39)) * 3**0.5 - 134.0673186784) < 1e-9 and abs(float(F(3, 2) + F(80, 9) + F(256, 39)) + float(F(64, 39)) * 3**0.5 - 19.7953312398) < 1e-9)
D2, d2, al2 = mk({1: m[1], 2: m2}, {1: t[1], 2: t2}, 2)
a2 = al2(); thr = 1 / (2 * mp.sqrt(mp.mpf(a2.numerator) / a2.denominator))
check("N=2 with audited values: alpha_2 = 0.0157977..., g^2 >= 3.97807...", abs(float(a2) - 0.0157977173) < 1e-9 and abs(float(thr) - 3.978074) < 1e-5, (float(a2), float(thr)))
check("d_2(alpha_2) = 1.52055, d_2(1/64) = 1.64707", abs(float(d2(a2)) - 1.520547) < 1e-5 and abs(float(d2(F(1, 64))) - 1.647071) < 1e-5, (float(d2(a2)), float(d2(F(1, 64)))))
check("g^2 = 4 is xi = 1/64 <= alpha_2", F(1, 64) <= a2)
# ---- Finding 2: the mean lemma, randomised test on l^1(n) (independent of the referee's code)
random.seed(7); worst = 0.0
import numpy as np
for trial in range(3000):
    n = random.randint(1, 7); chi = random.uniform(0.05, 0.95)
    Mx = np.random.randn(n + 1, n)                    # row 0 = p, rows 1..n = T
    Mx *= chi / np.abs(Mx).sum(axis=0)                # every column has l^1 sum exactly chi: |py|+||Ty||_1 <= chi||y||_1
    p, T = Mx[0], Mx[1:]
    S = np.linalg.inv(np.eye(n) - T)
    worst = max(worst, np.abs(p @ S).max() / chi)     # norm of pS: l^1 -> R is the max |entry|
check("lemma |p S y| <= chi ||y||_1 on 3000 random cases (max ratio)", worst <= 1 + 1e-12, round(worst, 6))
chiR = F(11, 24)
Cold, Cnew = (1 + 255 * chiR) / (1 - chiR)**2, (1 + 255 * chiR) / (1 - chiR)
check("C' = (1+255*11/24)/(13/24) = 2829/13, and C'/C = 13/24", Cnew == F(2829, 13) and Cnew / Cold == F(13, 24), (Cnew, float(Cnew)))
dd = F(13, 8)
def CJ(C): return C * (1 + 6 / dd - 9 / dd**2 + 18 * F(339, 1000) / dd**2)
check("C_J' = C_J * 13/24 = 782.29...", abs(float(CJ(Cnew)) - 782.2925) < 1e-3, float(CJ(Cnew)))
# other radii with the new prefactor
D5, d5, al5 = mk(m, t, 5)
def pref(R, new=True):
    dR = d5(R); c = 1 - dR / 3
    return float(dR), float((1 + 255 * c) / ((1 - c) if new else (1 - c)**2))
a5 = F(18424953576117616681, 10**21)
r55, rA, r45 = pref(F(1, 55)), pref(a5), pref(F(45, 4096))
check("new prefactors: 213.97 at 1/55 (rate 1.6376), 241.99 at alpha_5 (rate 1.5453), 85.00 at 45/4096 (rate 2.2588)",
      abs(r55[1] - 213.97) < 0.01 and abs(rA[1] - 241.99) < 0.01 and abs(r45[1] - 85.00) < 0.01 and abs(r45[0] - 2.2588) < 1e-4, (r55, rA, r45))
check("old prefactor at 45/4096 = 112.89", abs(pref(F(45, 4096), False)[1] - 112.895) < 0.01, pref(F(45, 4096), False))
# U29b comparison as xi -> 0: ratio of right sides = (C_T/C_1)(55*45/4096)^6 e^{tau/4}
C1 = F(6184, 25)
check("U29b: C_1 = (1+255*3/8)/(5/8)^2 = 6184/25, rate 3(1-3/8) = 15/8", (1 + 255 * F(3, 8)) / F(5, 8)**2 == C1)
rat = float(Cold / C1) * (55 * 45 / 4096)**6
check("Theorem 4.1 (old constant) vs U29b as xi->0: ratio 0.0790 e^{tau/4}, crossing at tau = 10.15", abs(rat - 0.0790) < 5e-4 and abs(4 * mp.log(1 / rat) - 10.15) < 0.01, (rat, float(4 * mp.log(1 / rat))))
ratn = float(Cnew / C1) * (55 * 45 / 4096)**6
check("with 2829/13: ratio %.4f e^{tau/4}, crossing at tau = %.2f" % (ratn, float(4 * mp.log(1 / ratn))), True)
# ---- Finding 4: kinetic row
off = 8 * 24 + 4 * (6 + 6 * s3)
check("kinetic row with the first pass's block norms: 30 + 8*24 + 4*(6+6 sqrt3) = 287.57 < 606", abs(float(30 + 8 * 24 + 4 * (6 + 6 * F(17320508, 10**7))) - 287.569) < 1e-3 and 30 + off < 606)
KP = 3 + chiR * (27 + off)
check("with the sharper mean: 3 + (11/24)(27 + 192 + 24 + 24 sqrt3) < 134", KP < 134, float(KP))
check("Gamma(W_p,W_q) = (3/4)P0 - (1/4)P1 from 2Gamma = (c_p+c_q)W_pW_q - K(W_pW_q), Casimirs 9/2, 13/2",
      (F(6) - F(9, 2)) / 2 == F(3, 4) and (F(6) - F(13, 2)) / 2 == F(-1, 4))
check("block norms: (3/4)16 + (1/4)48 = 24 and (3/4)8 + (1/4)24 sqrt3 = 6 + 6 sqrt3", F(3, 4) * 16 + F(1, 4) * 48 == 24)
check("diagonal: Gamma(W_p,W_p) = 3 - chi_1 from 2Gamma = 6(1+chi_1) - 8 chi_1", 6 - 8 == -2 and F(6, 2) == 3)
# ---- the benchmark table (Prop 4.4) with C', C_J', 134 and the fraction max{l1^2/(u0u2), 1-beta/(9 l2)}
B = {'0': (F(149, 468), F(2361994073, 4691494080)), '1': (F(97, 468), F(376882691, 938298816)),
     '2': (F(73313, 657072), F(982069718963833, 3919180324550400)), 'K': (F(187, 468), F(586668421, 1563831360)),
     'J': (F(6779, 73008), F(152338674005989, 435464480505600))}
def widths(xv, C, KPf):
    u = (55 * xv)**6 / (1 - (55 * xv)**2)
    w = {k: B[k][0] * xv**2 + B[k][1] * xv**4 + C / dd**int(k) * u for k in '012'}
    w['K'] = B['K'][0] * xv**2 + B['K'][1] * xv**4 + KPf * u
    return w, B['J'][0] * xv**2 + B['J'][1] * xv**4 + CJ(C) * u
def floor4(v): return F(int(v * 10000), 10000)
expect = {10: (0.99458, 5.712e-3, 6.052e-3), 13: (0.99977, 2.362e-4, 2.439e-4), 16: (0.999981, 1.933e-5, 1.974e-5)}
print("g^2 | fraction | eta_E | eta_G | gap window [d5, (3+wK)/(1-w0)] (new constants) | old upper end")
for g2 in (F(10), F(12), F(25, 2), F(13), F(16)):
    xv = 1 / (4 * g2**2)
    dph = F(29047, 10000) if g2 == 13 else floor4(d5(xv))
    w, beta = widths(xv, Cnew, 134)
    l = {k: F(1, 3**int(k)) - w[k] for k in '012'}; uu = {k: F(1, 3**int(k)) + w[k] for k in '012'}
    fr = max(l['1']**2 / (uu['0'] * uu['2']), 1 - beta / (9 * l['2']))
    eE, eG = beta / (dph * l['1']), beta / (dph**2 * l['2'])
    ub = (3 + w['K']) / (1 - w['0'])
    wo, _ = widths(xv, Cold, 606); ubo = (3 + wo['K']) / (1 - wo['0'])
    print(f"{str(g2):5} | {float(fr):.6f} | {float(eE):.4e} | {float(eG):.4e} | [{float(d5(xv)):.5f}, {float(ub):.6f}] | {float(ubo):.6f}")
    if int(g2) in expect and g2.denominator == 1:
        e = expect[int(g2)]
        check(f"g^2 = {g2}: table values as the referee reported", abs(float(fr) - e[0]) < 1e-5 and abs(float(eE) - e[1]) / e[1] < 1e-3 and abs(float(eG) - e[2]) / e[2] < 1e-3)
# ---- Finding 3 identity: J = (R - 3 Phi)^*(R - 3 Phi) so ||Phi c - R c/3||^2 = c^* J c / 9 (checked on random matrices)
Rm = np.random.randn(7, 4); Mx = np.random.randn(7, 7); A = Mx @ Mx.T + 7 * np.eye(7)   # A self-adjoint positive
Ph = np.linalg.solve(A, Rm); c = np.random.randn(4)                                     # Phi = A^{-1} R (kappa = 1)
G0, G1, G2 = Rm.T @ Rm, Rm.T @ Ph, Ph.T @ Ph
J = G0 - 6 * G1 + 9 * G2
check("with Phi = A^{-1}R, G1 is symmetric and J = G0 - 6G1 + 9G2 = (R-3Phi)^*(R-3Phi)",
      np.allclose(G1, G1.T) and np.allclose(J, (Rm - 3 * Ph).T @ (Rm - 3 * Ph)))
lhs = np.linalg.norm(Ph @ c - Rm @ c / 3)**2
check("||Phi c - Rc/3||^2 = c^* J c / 9", abs(lhs - c @ J @ c / 9) < 1e-9)
# ---- the erratum in the web continuation (p. 153)
check("record erratum: 38/81 + 1564/810 = 12/5, not 40/27", F(38, 81) + F(1564, 810) == F(12, 5) and F(12, 5) != F(40, 27))
check("the value 40/27 = 3*(1/81)*8 + 15*(1/810)*64 = 8/27 + 32/27", 3 * F(1, 81) * 8 + 15 * F(1, 810) * 64 == F(40, 27))
# ---- Proposition 3.6 quantified: 2 sqrt(alpha5) and the spacing bound
check("2 sqrt(alpha_5) = 0.27147", abs(float(2 * mp.sqrt(mp.mpf(a5.numerator) / a5.denominator)) - 0.271477) < 1e-5)
# ---- d_N'(0) = -64 for every N (so the lower bound loses first order)
for N in (1, 2, 5):
    DN, dN, _ = mk(m, t, N)
    h = F(1, 10**12)
    check(f"d_{N}'(0) = -64 (difference quotient)", abs(float((dN(h) - 3) / (mp.mpf(1) / 10**12)) + 64) < 1e-3)
# ---- the order-3 threshold from the referee's (numerical) order-3 norms, rounded up
mm = {1: F(64, 3), 2: F(1340674, 10**4), 3: F(12031425, 10**4)}; tt = {1: F(16, 3), 2: F(197954, 10**4), 3: F(1272887, 10**4)}
D3, d3, al3 = mk(mm, tt, 3); a3 = al3()
thr3 = 1 / (2 * mp.sqrt(mp.mpf(a3.numerator) / a3.denominator))
check("N=3 with the referee's order-3 values: alpha_3 = 0.018111, g^2 >= 3.71533, d_3(1/64) = 1.90235",
      abs(float(a3) - 0.018111069) < 1e-8 and abs(float(thr3) - 3.715335) < 1e-5 and abs(float(d3(F(1, 64))) - 1.902346) < 1e-5, (float(a3), float(thr3), float(d3(F(1, 64)))))
print("ALL PASS" if ok else "SOME CHECK FAILED")
