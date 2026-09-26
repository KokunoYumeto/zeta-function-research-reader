# Referee 21 (wbreader): YM-01 constants from the F26 rationals (read from FIFTH_REFERENCE.md at fa79faf, (F26)).
from fractions import Fraction as Fr
import mpmath as _mp
def F(q): return _mp.mpf(q.numerator)/q.denominator
import mpmath as mp
mp.mp.dps = 40
m = {1: Fr(64,3), 2: Fr(5834,39), 3: Fr(336572872,208845), 4: Fr(17270702970768271,341697152160), 5: Fr(1638684)}
t = {1: Fr(16,3), 2: Fr(137,6), 3: Fr(225985217,1253070), 4: Fr(110695177857394584026401,18025447358750832000), 5: Fr(190128)}
def make(m, t):
    def ell(x): return sum(F(m[i]+4*t[i])*x**i for i in range(1,6))
    def dl(x): return sum(F(3*(m[i]*t[j]+m[j]*t[i]))*x**(i+j) for i in range(1,6) for j in range(1,6) if i+j>=6)
    def D(x): return (1-ell(x))**2 - mp.mpf(8)/3*dl(x)
    def wstar(x): return mp.mpf(3)/4*(1-ell(x)-mp.sqrt(max(D(x),0)))
    def chi(x): return 4*sum(F(t[i])*x**i for i in range(1,6)) + mp.mpf(2)/3*wstar(x)
    def d5(x): return mp.mpf(3)/2*(1+mp.sqrt(max(D(x),0))) + sum(F(Fr(3,2)*m[i]-6*t[i])*x**i for i in range(1,6))
    return ell, dl, D, wstar, chi, d5
ell, dl, D, wstar, chi, d5 = make(m, t)
alpha = mp.findroot(D, 0.0184)
print("alpha_5 =", mp.nstr(alpha, 25), " threshold g^2 =", mp.nstr(1/(2*mp.sqrt(alpha)), 22))
print("d5(1/64) =", mp.nstr(d5(mp.mpf(1)/64), 15), " 3(1-chi)(1/64) =", mp.nstr(3*(1-chi(mp.mpf(1)/64)), 15))
x1575 = mp.mpf(1)/(4*(mp.mpf(15)/4)**2)
print("xi at g^2=15/4:", x1575, " (<= alpha?)", x1575 <= alpha, " d5 =", mp.nstr(d5(x1575), 12))
print("d5(0) =", d5(mp.mpf(0)), " d5(alpha) =", mp.nstr(d5(alpha), 12), " ell(alpha) =", mp.nstr(ell(alpha), 8))
# monotonicity and d5 <= 3 on (0, alpha]: sample densely (the proof: w_* increasing, chi increasing)
xs = [alpha*k/4000 for k in range(1,4001)]
vals = [d5(x) for x in xs]
print("d5 decreasing on grid:", all(vals[i+1] < vals[i] for i in range(len(vals)-1)), " max d5 on grid:", mp.nstr(max(vals), 12), " min:", mp.nstr(min(vals),12))
print("chi in [0,1/2) on grid:", all(0 <= chi(x) < 0.5 for x in xs))
# sensitivity: m5, t5 doubled
m2 = dict(m); t2 = dict(t); m2[5] = 2*m[5]; t2[5] = 2*t[5]
ell2, dl2, D2, w2, chi2, d52 = make(m2, t2)
a2 = mp.findroot(D2, 0.0179)
print("x2 sensitivity: alpha =", mp.nstr(a2, 8), " threshold g^2 =", mp.nstr(1/(2*mp.sqrt(a2)), 6), " d5(1/64) =", mp.nstr(d52(mp.mpf(1)/64), 6))
# the Neumann radius at L=2 and generally
for L in (2,3,4):
    M = 12*L*L*(2*L+1); print("L=",L," M_L=",M," 3/(16 M)=",Fr(3,16*M), " 1/(64L^2(2L+1))=", Fr(1,64*L*L*(2*L+1)))
# (3/2) m_i - 6 t_i
print("coefficients (3/2)m_i-6t_i:", [float(Fr(3,2)*m[i]-6*t[i]) for i in range(1,6)])
