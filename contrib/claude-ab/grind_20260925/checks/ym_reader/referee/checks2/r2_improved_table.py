# Improved benchmark table (Prop. 4.4 of the YM reader), exact rational arithmetic, using:
#  (a) the sharper mean bound |(mu - P_H)F| <= chi ||Q_H F||  =>  C' = (1+255 chi)/(1-chi) = 2829/13 at chi = 11/24,
#      C_J' = C' [1 + 6/d - 9/d^2 + 18 (339/1000)/d^2];
#  (b) kinetic tail prefactor 134 >= 3 + (11/24)(27 + 192 + 24 + 24 sqrt3)  (instead of 606);
#  (c) observed fraction >= max( l1^2/(u0 u2), 1 - beta/(9 l2) ).
# The inherited degree-2 and degree-4 row bounds (H18 table) are used unchanged.
from fractions import Fraction as Fr
import mpmath as mp
mp.mp.dps = 40
m = {1: Fr(64, 3), 2: Fr(5834, 39), 3: Fr(336572872, 208845), 4: Fr(17270702970768271, 341697152160), 5: Fr(1638684)}
t = {1: Fr(16, 3), 2: Fr(137, 6), 3: Fr(225985217, 1253070), 4: Fr(110695177857394584026401, 18025447358750832000), 5: Fr(190128)}
def d5(x):
    ell = sum((m[i] + 4 * t[i]) * x**i for i in range(1, 6))
    dl = sum(3 * (m[i] * t[j] + m[j] * t[i]) * x**(i + j) for i in range(1, 6) for j in range(1, 6) if i + j >= 6)
    Dx = (1 - ell)**2 - Fr(8, 3) * dl; s = sum((Fr(3, 2) * m[i] - 6 * t[i]) * x**i for i in range(1, 6))
    return mp.mpf(3) / 2 * (1 + mp.sqrt(mp.mpf(Dx.numerator) / Dx.denominator)) + mp.mpf(s.numerator) / s.denominator
chi = Fr(11, 24); d = Fr(13, 8)
Cold = (1 + 255 * chi) / (1 - chi)**2; Cnew = (1 + 255 * chi) / (1 - chi)
def CJ(C): return C * (1 + 6 / d - 9 / d**2 + 18 * Fr(339, 1000) / d**2)
s3u = Fr(17321, 10000)
Kpref = 3 + chi * (27 + 192 + 24 + 24 * s3u)
assert Kpref < 134
B = {'0': (Fr(149, 468), Fr(2361994073, 4691494080)), '1': (Fr(97, 468), Fr(376882691, 938298816)),
     '2': (Fr(73313, 657072), Fr(982069718963833, 3919180324550400)), 'K': (Fr(187, 468), Fr(586668421, 1563831360)),
     'J': (Fr(6779, 73008), Fr(152338674005989, 435464480505600))}
def widths(x, C, KP):
    u = (55 * x)**6 / (1 - (55 * x)**2)
    w = {k: B[k][0] * x**2 + B[k][1] * x**4 + C / d**int(k) * u for k in '012'}
    w['K'] = B['K'][0] * x**2 + B['K'][1] * x**4 + KP * u
    return w, B['J'][0] * x**2 + B['J'][1] * x**4 + CJ(C) * u
def floor4(v): return Fr(int(v * 10000), 10000)
print("C' =", Cnew, "=", float(Cnew), " C_J' =", float(CJ(Cnew)), " kinetic prefactor <=", float(Kpref), "-> 134")
print("g^2  | observed fraction (reader -> improved) | eta_E (reader -> improved) | eta_G (reader -> improved) | Delta/kappa in")
for g2 in (Fr(10), Fr(12), Fr(25, 2), Fr(13), Fr(16)):
    x = 1 / (4 * g2**2)
    dph = Fr(29047, 10000) if g2 == 13 else floor4(d5(x))
    out = []
    for (C, KP, useJ) in ((Cold, 606, False), (Cnew, 134, True)):
        w, beta = widths(x, C, KP)
        l = {k: Fr(1, 3**int(k)) - w[k] for k in '012'}; uu = {k: Fr(1, 3**int(k)) + w[k] for k in '012'}
        fr = l['1']**2 / (uu['0'] * uu['2'])
        if useJ: fr = max(fr, 1 - beta / (9 * l['2']))
        out.append((fr, beta / (dph * l['1']), beta / (dph**2 * l['2']), (3 + w['K']) / (1 - w['0'])))
    (f0, e0, g0, _), (f1, e1, g1, ub) = out
    print(f"{str(g2):5}| {float(f0):.6f} -> {float(f1):.6f} | {float(e0):.3e} -> {float(e1):.3e} | {float(g0):.3e} -> {float(g1):.3e} | [{mp.nstr(d5(x), 6)}, {float(ub):.6f}]")
