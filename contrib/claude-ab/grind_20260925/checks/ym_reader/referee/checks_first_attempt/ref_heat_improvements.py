# Referee check: (1) the g^2 = 13 diagnostics to more digits; (2) the heat prefactor with the sharper
# mean estimate |(mu - P_H)F| <= chi ||Q_H F||_X (instead of chi/(1-chi)), i.e. C = (1+256 chi)/(1-chi);
# (3) the benchmark table recomputed with that prefactor; (4) the radius at which the 'other radii' family
# reproduces U29b's rate 15/8, and its prefactor; (5) the family at R = alpha_5 (closed endpoint).
from fractions import Fraction as F
import mpmath as mp
mp.mp.dps = 50
m = {1: F(64, 3), 2: F(5834, 39), 3: F(336572872, 208845),
     4: F(17270702970768271, 341697152160), 5: F(1638684)}
t = {1: F(16, 3), 2: F(137, 6), 3: F(225985217, 1253070),
     4: F(110695177857394584026401, 18025447358750832000), 5: F(190128)}
def ell(x): return sum((m[i] + 4 * t[i]) * x**i for i in range(1, 6))
def delta(x): return sum(3 * (m[i] * t[j] + m[j] * t[i]) * x**(i + j) for i in range(1, 6) for j in range(1, 6) if i + j >= 6)
def D(x): return (1 - ell(x))**2 - F(8, 3) * delta(x)
def s(x): return sum((F(3, 2) * m[i] - 6 * t[i]) * x**i for i in range(1, 6))
def mpf(q): return mp.mpf(q.numerator) / q.denominator if isinstance(q, F) else mp.mpf(q)
def d5(x):
    x = F(x) if not isinstance(x, F) else x
    return mp.mpf(3) / 2 * (1 + mp.sqrt(mpf(D(x)))) + mpf(s(x))
def d5gt(x, c):
    rhs = (c - s(x)) * F(2, 3) - 1
    return D(x) >= 0 and (rhs < 0 or D(x) > rhs * rhs)

B = {'0': (F(149, 468), F(2361994073, 4691494080)), '1': (F(97, 468), F(376882691, 938298816)),
     '2': (F(73313, 657072), F(982069718963833, 3919180324550400)), 'K': (F(187, 468), F(586668421, 1563831360)),
     'J': (F(6779, 73008), F(152338674005989, 435464480505600))}
dd = F(13, 8)
def table(C, CJ, rows, label):
    print(label)
    for g2, dph in rows:
        x = 1 / (4 * F(g2)**2)
        u = (55 * x)**6 / (1 - (55 * x)**2)
        w = {k: B[k][0] * x**2 + B[k][1] * x**4 + C / dd**int(k) * u for k in '012'}
        beta = B['J'][0] * x**2 + B['J'][1] * x**4 + CJ * u
        l = {k: F(1, 3**int(k)) - w[k] for k in '012'}; uu = {k: F(1, 3**int(k)) + w[k] for k in '012'}
        fr = l['1']**2 / (uu['0'] * uu['2']); eE = beta / (dph * l['1']); eG = beta / (dph**2 * l['2'])
        print(f"  g^2={g2}: fraction {mp.nstr(mpf(fr), 14)}, eta_E {mp.nstr(mpf(eE), 14)}, eta_G {mp.nstr(mpf(eG), 14)}")
C_old = (1 + 255 * F(11, 24)) / (1 - F(11, 24))**2
CJfac = 1 + 6 / dd - 9 / dd**2 + 18 * F(339, 1000) / dd**2
def floor4(v): return F(int(v * 10000), 10000)
rows = [(10, floor4(d5(F(1, 400)))), (12, floor4(d5(F(1, 576)))), (F(25, 2), floor4(d5(F(1, 625)))),
        (13, F(29047, 10000)), (16, floor4(d5(F(1, 1024))))]
table(C_old, C_old * CJfac, rows, "workbench prefactor C = 67896/169:")
C_new = (1 + 256 * F(11, 24)) / (1 - F(11, 24))
print("sharper prefactor (1+256 chi)/(1-chi) at chi = 11/24:", C_new, "=", float(C_new), " vs 67896/169 =", float(C_old))
table(C_new, C_new * CJfac, rows, "with the sharper prefactor:")
# (4) 'other radii': find R with d5(R) = 15/8 (U29b's rate), its prefactor, and compare with U29b
lo, hi = F(1, 100), F(1, 55)
for _ in range(80):
    mid = (lo + hi) / 2
    if d5gt(mid, F(15, 8)): lo = mid
    else: hi = mid
R = lo; chi = 1 - d5(R) / 3
print("R with d5(R) = 15/8:", mp.nstr(mpf(R), 12), " 1/R =", mp.nstr(1 / mpf(R), 8),
      " C(R) (reader's formula) =", mp.nstr((1 + 255 * chi) / (1 - chi)**2, 10), " U29b: R1 = 45/4096 = ", float(F(45, 4096)), " prefactor 6184/25 =", 6184 / 25)
# (5) the closed endpoint R = alpha_5
lo, hi = F(18, 1000), F(19, 1000)
for _ in range(120):
    mid = (lo + hi) / 2
    lo, hi = (mid, hi) if D(mid) > 0 else (lo, mid)
a5 = lo; chi5 = 1 - d5(a5) / 3
print("R = alpha_5:", mp.nstr(mpf(a5), 20), " rate d5 =", mp.nstr(d5(a5), 10), " C =", mp.nstr((1 + 255 * chi5) / (1 - chi5)**2, 10),
      " sharper C =", mp.nstr((1 + 256 * chi5) / (1 - chi5), 10))
# exact chi at 1/55 with the sharper formula
chi55 = 1 - d5(F(1, 55)) / 3
print("R = 1/55 exact chi:", mp.nstr(chi55, 10), " C (reader) =", mp.nstr((1 + 255 * chi55) / (1 - chi55)**2, 10), " sharper C =", mp.nstr((1 + 256 * chi55) / (1 - chi55), 10))
