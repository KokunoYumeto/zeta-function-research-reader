#!/usr/bin/env python3
"""Referee checks for note 46 (YM, NS, S6, Keller map). mpmath at 50 digits from the exact F26 rationals."""
import itertools, time
from fractions import Fraction as Fr
import mpmath as mp
import sympy as sp
T0 = time.time()
def out(*a): print(*a, flush=True)
mp.mp.dps = 50

m = {1: Fr(64, 3), 2: Fr(5834, 39), 3: Fr(336572872, 208845),
     4: Fr(17270702970768271, 341697152160), 5: Fr(1638684)}
t = {1: Fr(16, 3), 2: Fr(137, 6), 3: Fr(225985217, 1253070),
     4: Fr(110695177857394584026401, 18025447358750832000), 5: Fr(190128)}

def make(mm, tt, K):
    def ell(x): return sum(mp.mpf(mm[i].numerator)/mm[i].denominator*x**i + 4*mp.mpf(tt[i].numerator)/tt[i].denominator*x**i for i in range(1, K+1))
    def dl(x): return sum(3*(mp.mpf(mm[i].numerator)/mm[i].denominator*mp.mpf(tt[j].numerator)/tt[j].denominator
                             + mp.mpf(mm[j].numerator)/mm[j].denominator*mp.mpf(tt[i].numerator)/tt[i].denominator)*x**(i+j)
                          for i in range(1, K+1) for j in range(1, K+1) if i + j >= K + 1)
    def D(x): return (1 - ell(x))**2 - mp.mpf(8)/3*dl(x)
    def d(x): return mp.mpf(3)/2*(1 + mp.sqrt(D(x))) + sum((mp.mpf(3)/2*mp.mpf(mm[i].numerator)/mm[i].denominator - 6*mp.mpf(tt[i].numerator)/tt[i].denominator)*x**i for i in range(1, K+1))
    def wstar(x): return mp.mpf(3)/4*(1 - ell(x) - mp.sqrt(D(x)))
    alpha = mp.findroot(D, (mp.mpf('0.017'), mp.mpf('0.0195')), solver='anderson')
    return ell, dl, D, d, wstar, alpha

ell5, dl5, D5, d5, w5, a5 = make(m, t, 5)
ell4, dl4, D4, d4, w4, a4 = make(m, t, 4)
out("alpha_5 =", mp.nstr(a5, 22), " threshold 1/(2 sqrt alpha_5) =", mp.nstr(1/(2*mp.sqrt(a5)), 22))
out("alpha_[4] =", mp.nstr(a4, 22), " threshold =", mp.nstr(1/(2*mp.sqrt(a4)), 18))
for g2 in (Fr(37, 10), Fr(15, 4), Fr(4)):
    x = mp.mpf(1)/(4*mp.mpf(g2.numerator)**2/mp.mpf(g2.denominator)**2)
    out(f"g^2={g2}: xi={mp.nstr(x, 10)}, d5={mp.nstr(d5(x), 10)}, w*={mp.nstr(w5(x), 8)}, d_[4]={mp.nstr(d4(x), 10) if x <= a4 else 'outside alpha_[4]'}")
out("d5(alpha5) =", mp.nstr(d5(a5), 10), " d5(0) =", mp.nstr(d5(mp.mpf(0)), 10), " d5(1/55) =", mp.nstr(d5(mp.mpf(1)/55), 10), "> 13/8:", d5(mp.mpf(1)/55) > mp.mpf(13)/8)
# chi = 1 - d5/3 in [0, 1/2)
chis = [1 - d5(a5*k/200)/3 for k in range(201)]
out("0 <= chi < 1/2 on [0, alpha5] (201-point grid):", min(chis) >= -mp.mpf(10)**-40 and max(chis) < mp.mpf(1)/2)
# d5 decreasing and d5 >= d_[4] on [0, alpha_[4]]
xs = [a4*k/400 for k in range(401)]
dec = all(d5(xs[i+1]) <= d5(xs[i]) + mp.mpf(10)**-40 for i in range(400))
dom = min(d5(x) - d4(x) for x in xs)
out("d5 decreasing on [0, alpha_[4]] (grid):", dec, "; min over grid of d5 - d_[4]:", mp.nstr(dom, 8))
# sensitivity: m5, t5 doubled
m2 = dict(m); t2 = dict(t); m2[5] = 2*m[5]; t2[5] = 2*t[5]
_, _, _, d5s, _, a5s = make(m2, t2, 5)
out("sensitivity (m5,t5 x2): alpha =", mp.nstr(a5s, 8), " threshold g^2 =", mp.nstr(1/(2*mp.sqrt(a5s)), 6), " d5(1/64) =", mp.nstr(d5s(mp.mpf(1)/64), 6))
# identity d5 = 3(1 - chi) with chi = 4 sum t_i x^i + (2/3) w*
x = mp.mpf('0.01')
chi = 4*sum(mp.mpf(t[i].numerator)/t[i].denominator*x**i for i in range(1, 6)) + mp.mpf(2)/3*w5(x)
out("d5 = 3(1-chi) at x=0.01:", mp.nstr(d5(x) - 3*(1 - chi), 5))
# w* small root of (2/3)w^2 - (1-l)w + delta = 0
out("w* root check at x=0.01:", mp.nstr(mp.mpf(2)/3*w5(x)**2 - (1 - ell5(x))*w5(x) + dl5(x), 5))
out("ell5(alpha5) =", mp.nstr(ell5(a5), 8))

# Proposition 46.5 numbers
for L in (2, 3, 4):
    M = 12*L*L*(2*L + 1)
    out(f"L={L}: M_L={M}, 3/(16 M_L) = {Fr(3, 16*M)} = 1/(64 L^2 (2L+1)) = {Fr(1, 64*L*L*(2*L+1))}")
out("L=j^2 radius ~ 1/(128 j^6): ratio at j=50:", float(Fr(1, 64*50**4*(2*50**2 + 1)) * 128 * 50**6))

# Keller map F and the escaping curve gamma
x_, y_, w_, tau = sp.symbols('x y w tau')
F = sp.Matrix([(1 + x_*y_)**3*w_ + y_**2*(1 + x_*y_)*(4 + 3*x_*y_),
               y_ + 3*x_*(1 + x_*y_)**2*w_ + 3*x_*y_**2*(4 + 3*x_*y_),
               2*x_ - 3*x_**2*y_ - x_**3*w_])
DF = F.jacobian([x_, y_, w_])
out("det DF =", sp.simplify(DF.det()))
z = sp.sqrt(1 - 8*tau)
gam = sp.Matrix([1/z, -sp.Rational(3, 2)*z, sp.Rational(13, 2)*z**2])
Fg = sp.simplify(F.subs({x_: gam[0], y_: gam[1], w_: gam[2]}))
out("F(gamma(tau)) =", list(Fg))
lhs = sp.simplify(DF.subs({x_: gam[0], y_: gam[1], w_: gam[2]}) * gam.diff(tau))
out("DF(gamma) gamma' =", list(lhs), "(should be V=(2,0,0))")
out("gamma(0) =", list(gam.subs(tau, 0)))

# S6-5: P never +-6 on Z^4 (mod 9 argument) and gcd on D4
vals = set()
for a in itertools.product(range(-9, 10), repeat=4):
    vals.add((a[0]*(a[0]**2 - 3*(a[1]**2 + a[2]**2 + a[3]**2)), sum(a) % 2 == 0))
allvals = {v for v, _ in vals}; d4vals = {v for v, e in vals if e}
import math
g = 0
for v in d4vals: g = math.gcd(g, v)
out("S6-5: +-6 attained on Z^4 (|a_i|<=9):", 6 in allvals or -6 in allvals, "; gcd over D4:", g,
    "; 3|P => 9|P on Z^4:", all(v % 9 == 0 for v in allvals if v % 3 == 0))
out("Gram det 6^4*4 =", 6**4*4, " sqrt =", math.isqrt(6**4*4))
# the Pell/NS constant quoted in 47 sec 1.2 : attained or only approached?
s2 = mp.sqrt(2); c = 1/mp.sqrt(4 + 2*s2)
vr = (mp.mpf(1), 1 - s2)
best = None
for mm_ in range(-400, 401):
    for nn in range(-400, 401):
        if mm_ == 0 and nn == 0: continue
        val = abs(vr[0]*mm_ + vr[1]*nn) * mp.sqrt(mm_**2 + nn**2)
        if best is None or val < best[0]: best = (val, mm_, nn)
out("NS->ES constant: 1/sqrt(4+2sqrt2) =", mp.nstr(c, 15), "; min over |k|<=400 of |v_r.k| ||k|| =", mp.nstr(best[0], 20), "at", best[1:], "; excess:", mp.nstr(best[0] - c, 5))
vu = (vr[0]/mp.sqrt(vr[0]**2 + vr[1]**2), vr[1]/mp.sqrt(vr[0]**2 + vr[1]**2))
out("  with the UNIT eigenvector the infimum would be 1/sqrt(8) =", mp.nstr(1/mp.sqrt(8), 10), "(different normalisation)")
out(f"total {time.time()-T0:.1f}s")
