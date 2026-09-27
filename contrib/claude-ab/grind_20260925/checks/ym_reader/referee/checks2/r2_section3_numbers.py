# Referee check (independent of the reader's scripts): Section 3 numbers of the YM reader.
# Recomputes alpha_N, thresholds, d_N values from the F26 rationals; Prop. 3.6 constants;
# the sensitivity remark (m5, t5 doubled); Prop. 5.1; exact rational brackets where claimed.
from fractions import Fraction as Fr
import mpmath as mp
mp.mp.dps = 60

m = {1: Fr(64, 3), 2: Fr(5834, 39), 3: Fr(336572872, 208845),
     4: Fr(17270702970768271, 341697152160), 5: Fr(1638684)}
t = {1: Fr(16, 3), 2: Fr(137, 6), 3: Fr(225985217, 1253070),
     4: Fr(110695177857394584026401, 18025447358750832000), 5: Fr(190128)}

def polys(N, mm=m, tt=t):
    ell = {i: mm[i] + 4 * tt[i] for i in range(1, N + 1)}
    dl = {}
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i + j >= N + 1:
                dl[i + j] = dl.get(i + j, 0) + 3 * (mm[i] * tt[j] + mm[j] * tt[i])
    s = {i: Fr(3, 2) * mm[i] - 6 * tt[i] for i in range(1, N + 1)}
    return ell, dl, s

def ev(c, x):
    return sum(v * x**k for k, v in c.items())

def D(N, x, mm=m, tt=t):
    ell, dl, s = polys(N, mm, tt)
    return (1 - ev(ell, x))**2 - Fr(8, 3) * ev(dl, x)

def d(N, x, mm=m, tt=t):
    ell, dl, s = polys(N, mm, tt)
    Dx = (1 - ev(ell, x))**2 - Fr(8, 3) * ev(dl, x)
    return mp.mpf(3) / 2 * (1 + mp.sqrt(mp.mpf(Dx.numerator) / Dx.denominator)) + mp.mpf(ev(s, x).numerator) / ev(s, x).denominator

def first_root(N, mm=m, tt=t, lo=Fr(0), hi=Fr(1, 20), it=200):
    # D(0)=1>0; find first sign change on a fine scan, then bisect exactly
    n = 4000
    prev = Fr(0)
    for k in range(1, n + 1):
        x = hi * k / n
        if D(N, x, mm, tt) <= 0:
            lo, hi = prev, x
            break
        prev = x
    for _ in range(it):
        mid = (lo + hi) / 2
        if D(N, mid, mm, tt) > 0: lo = mid
        else: hi = mid
    return lo, hi

print("== Theorem 3.1 / Corollary 3.5 ==")
for N in range(1, 6):
    lo, hi = first_root(N)
    a = mp.mpf(lo.numerator) / lo.denominator
    thr = 1 / (2 * mp.sqrt(a))
    print(f"N={N}: alpha_N in [{mp.nstr(a, 22)}, ...], g^2 threshold = {mp.nstr(thr, 20)}, d_N(alpha_N) = {mp.nstr(d(N, lo), 12)}")
lo5, hi5 = first_root(5)
print("F29 bracket 0.018424953576117616681 < alpha5 < ...682:", Fr(18424953576117616681, 10**21) < lo5 and hi5 < Fr(18424953576117616682, 10**21))
print("d5(1/64) =", mp.nstr(d(5, Fr(1, 64)), 14), " d5(4/225) =", mp.nstr(d(5, Fr(4, 225)), 12), " d5(1/55) =", mp.nstr(d(5, Fr(1, 55)), 12))
print("d4(1/64) =", mp.nstr(d(4, Fr(1, 64)), 10), " d4(4/225) =", mp.nstr(d(4, Fr(4, 225)), 10))
for g2 in (Fr(41, 10), Fr(5)):
    print(f"d2 at g^2={g2}: {mp.nstr(d(2, 1 / (4 * g2**2)), 10)}")
for g2 in (Fr(5), Fr(10)):
    print(f"d1 at g^2={g2}: {mp.nstr(d(1, 1 / (4 * g2**2)), 10)}")
print("(3/2)m2 - 6t2 =", Fr(3, 2) * m[2] - 6 * t[2], " generic cubic 6(m1t2+m2t1) =", 6 * (m[1] * t[2] + m[2] * t[1]))
print("D1 == 1 - 256x/3 exactly:", all(D(1, Fr(k, 1000)) == 1 - Fr(256, 3) * Fr(k, 1000) for k in range(0, 12)))

# sensitivity: m5, t5 doubled
m2x = dict(m); t2x = dict(t); m2x[5] = 2 * m[5]; t2x[5] = 2 * t[5]
lo, hi = first_root(5, m2x, t2x)
a = mp.mpf(lo.numerator) / lo.denominator
print("m5,t5 doubled: threshold", mp.nstr(1 / (2 * mp.sqrt(a)), 10), " d5(1/64) =", mp.nstr(d(5, Fr(1, 64), m2x, t2x), 10))

# slope of d_N at 0 : d_N = 3 - 12 t1 x + O(x^2) = 3 - 64x
for x in (Fr(1, 10**5), Fr(1, 10**7)):
    print(f"(3 - d5(x))/x at x={x}: {mp.nstr((3 - d(5, x)) / (mp.mpf(x.numerator) / x.denominator), 12)}")

print("== Prop. 3.6 ==")
print("2 sqrt(alpha5) =", mp.nstr(2 * mp.sqrt(mp.mpf(lo5.numerator) / lo5.denominator), 12), "  2/sqrt(55) =", mp.nstr(2 / mp.sqrt(55), 12))
print("1/alpha5 =", mp.nstr(1 / (mp.mpf(lo5.numerator) / lo5.denominator), 10))

print("== Prop. 5.1 ==")
ok = True
for k in range(1, 3001):
    x = Fr(3, 256) * k / 3000
    y = 256 * x / 3
    # d1 >= 3 - 128x  <=>  sqrt(1-y) >= 1 - y  (true on [0,1])
    ok &= (1 - y) >= (1 - y)**2
print("d1(x) >= 3 - 128 x on (0, 3/256] (via 1-y >= (1-y)^2):", ok)
print("sharper: d1(x) >= 3 - 64x - 16384 x^2/3 on (0,3/256]:",
      all(d(1, Fr(3, 256) * k / 500) >= 3 - 64 * mp.mpf(3) / 256 * k / 500 - mp.mpf(16384) / 3 * (mp.mpf(3) / 256 * k / 500)**2 - mp.mpf(10)**-40 for k in range(1, 501)))
print("M_L = 12 L^2 (2L+1): M_2 =", 12 * 4 * 5, " 3/(16*240) =", Fr(3, 16 * 240), " 3/(4*240) =", Fr(3, 4 * 240))
