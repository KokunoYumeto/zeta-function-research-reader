# Referee check (independent of the reader's scripts): the numbers of Theorem 3.1 and Corollary 3.5
# of the Yang-Mills reader, recomputed from the ten rationals of F26 only.
from fractions import Fraction as F
import mpmath as mp
mp.mp.dps = 60

m = {1: F(64, 3), 2: F(5834, 39), 3: F(336572872, 208845),
     4: F(17270702970768271, 341697152160), 5: F(1638684)}
t = {1: F(16, 3), 2: F(137, 6), 3: F(225985217, 1253070),
     4: F(110695177857394584026401, 18025447358750832000), 5: F(190128)}

def mk(N, mm=m, tt=t):
    def ell(x): return sum((mm[i] + 4 * tt[i]) * x**i for i in range(1, N + 1))
    def dlt(x): return sum(3 * (mm[i] * tt[j] + mm[j] * tt[i]) * x**(i + j)
                           for i in range(1, N + 1) for j in range(1, N + 1) if i + j >= N + 1)
    def D(x): return (1 - ell(x))**2 - mp.mpf(8) / 3 * dlt(x)
    def s(x): return sum((mp.mpf(3) / 2 * mm[i] - 6 * tt[i]) * x**i for i in range(1, N + 1))
    def d(x):
        x = mp.mpf(x); return mp.mpf(3) / 2 * (1 + mp.sqrt(max(D(x), 0))) + s(x)
    def wstar(x):
        x = mp.mpf(x); return mp.mpf(3) / 4 * (1 - ell(x) - mp.sqrt(max(D(x), 0)))
    return ell, dlt, D, s, d, wstar

def conv(v):  # tolerate Fraction coefficients inside mpmath expressions
    return mp.mpf(v.numerator) / v.denominator if isinstance(v, F) else v
for dct in (m, t):
    for k in dct: dct[k] = conv(dct[k])

def first_root(D, lo=mp.mpf('1e-9'), hi=mp.mpf('0.1')):
    # scan for the first sign change, then bisect
    xs = [lo + (hi - lo) * k / 20000 for k in range(20001)]
    for a, b in zip(xs, xs[1:]):
        if D(a) > 0 and D(b) <= 0:
            return mp.findroot(D, (a, b), solver='bisect', tol=mp.mpf(10)**-50)
    return None

out = []
def rep(*a):
    s = ' '.join(str(x) for x in a); print(s); out.append(s)

for N in range(1, 6):
    ell, dlt, D, s, d, wstar = mk(N)
    a = first_root(D)
    thr = 1 / (2 * mp.sqrt(a))
    rep(f"N={N}: alpha_N = {mp.nstr(a, 22)}  threshold g^2 >= {mp.nstr(thr, 20)}  d_N(alpha_N) = {mp.nstr(d(a), 12)}  ell_N(alpha_N) = {mp.nstr(ell(a), 8)}")
    # monotonicity on a fine grid, and the derivative identity sign (delta' + ell' w*) > 0
    grid = [a * k / 4000 for k in range(4001)]
    vals = [d(x) for x in grid]
    rep(f"   d_N strictly decreasing on a 4001-point grid of [0, alpha_N]: {all(v1 > v2 for v1, v2 in zip(vals, vals[1:]))}")
    for x in (F(1, 64), F(4, 225), F(1, 100), F(1, 55), F(1, 400)):
        xv = conv(x)
        if xv <= a:
            rep(f"   d_{N}({x}) = {mp.nstr(d(xv), 14)}")
# Theorem 3.1 specific
ell, dlt, D, s, d, wstar = mk(5)
a5 = first_root(D)
rep("check alpha_5 bracket (F29):", mp.mpf('0.018424953576117616681') < a5 < mp.mpf('0.018424953576117616682'))
rep("d5(1/64) =", mp.nstr(d(mp.mpf(1) / 64), 14), " w*(1/64) =", mp.nstr(wstar(mp.mpf(1) / 64), 10))
rep("d5 at g^2 = 3.6836:", mp.nstr(d(1 / (4 * mp.mpf('3.6836')**2)), 10))
rep("d5 at g^2 = 37/10:", mp.nstr(d(1 / (4 * (mp.mpf(37) / 10)**2)), 10))
# Corollary 3.5 (b) g^2 = 4.1 and g^2 = 5
ell2, dlt2, D2, s2, d2, w2 = mk(2)
for g2 in (mp.mpf('4.1'), mp.mpf(5)):
    rep(f"d_2 at g^2={g2}: {mp.nstr(d2(1 / (4 * g2**2)), 10)}")
ell1, dlt1, D1, s1, d1, w1 = mk(1)
for g2 in (5, 10):
    rep(f"d_1 at g^2={g2}: {mp.nstr(d1(mp.mpf(1) / (4 * g2**2)), 10)}")
rep("(3/2)m_2 - 6t_2 =", F(3, 2) * F(5834, 39) - 6 * F(137, 6))
rep("generic cubic coefficient 6(m1 t2 + m2 t1) =", 6 * (F(64, 3) * F(137, 6) + F(5834, 39) * F(16, 3)), "vs L10 944984/351 =", float(F(944984, 351)))
rep("generic quartic 6 m2 t2 =", 6 * F(5834, 39) * F(137, 6), "(L10 has 799258/39)")
rep("ell_2 x^2 coefficient m2 + 4 t2 =", F(5834, 39) + 4 * F(137, 6), "(L10 has 3132/13)")
# sensitivity: m5, t5 doubled
m2x = dict(m); t2x = dict(t); m2x[5] = 2 * m[5]; t2x[5] = 2 * t[5]
ellS, dltS, DS, sS, dS, wS = mk(5, m2x, t2x)
aS = first_root(DS)
rep("sensitivity (m5,t5 doubled): threshold", mp.nstr(1 / (2 * mp.sqrt(aS)), 8), " d5(1/64) =", mp.nstr(dS(mp.mpf(1) / 64), 8))
# small-x expansion: d5 = 3 - 12 t1 x + O(x^2) = 3 - 64 x + ...
for x in (mp.mpf('1e-4'), mp.mpf('1e-5')):
    rep(f"(3 - d5(x))/x at x={x}: {mp.nstr((3 - d(x)) / x, 10)}")
open('./ref_gap_arithmetic_OUTPUT.txt', 'w').write('\n'.join(out) + '\n')
