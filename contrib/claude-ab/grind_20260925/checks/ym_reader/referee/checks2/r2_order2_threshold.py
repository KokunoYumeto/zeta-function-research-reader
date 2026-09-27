# Referee check: Corollary 3.5(b) of the YM reader with the independently computed exact order-2 norms
#   m(v2) = 6 + 11200/117 + 112/9 + 448 sqrt3/39,  t(v2) = 3/2 + 80/9 + 256/39 + 64 sqrt3/39
# replaced by rational upper bounds, instead of the workbench's (5834/39, 137/6).
from fractions import Fraction as Fr
import mpmath as mp
mp.mp.dps = 50
s3 = mp.sqrt(3)
m2_exact = 6 + mp.mpf(11200) / 117 + mp.mpf(112) / 9 + 448 * s3 / 39
t2_exact = mp.mpf(3) / 2 + mp.mpf(80) / 9 + mp.mpf(256) / 39 + 64 * s3 / 39
print("m(v2) =", mp.nstr(m2_exact, 15), " t(v2) =", mp.nstr(t2_exact, 15))
# rational upper bounds via sqrt3 < 17321/10000
s3u = Fr(17321, 10000)
assert Fr(17321, 10000)**2 > 3
m2u = 6 + Fr(11200, 117) + Fr(112, 9) + 448 * s3u / 39
t2u = Fr(3, 2) + Fr(80, 9) + Fr(256, 39) + 64 * s3u / 39
print("rational upper bounds:", float(m2u), float(t2u))
m1, t1 = Fr(64, 3), Fr(16, 3)

def D2(x, m2, t2):
    ell = (m1 + 4 * t1) * x + (m2 + 4 * t2) * x**2
    dl = 6 * (m1 * t2 + m2 * t1) * x**3 + 6 * m2 * t2 * x**4
    return (1 - ell)**2 - Fr(8, 3) * dl
def d2(x, m2, t2):
    Dx = D2(x, m2, t2)
    s = (Fr(3, 2) * m1 - 6 * t1) * x + (Fr(3, 2) * m2 - 6 * t2) * x**2
    return mp.mpf(3) / 2 * (1 + mp.sqrt(mp.mpf(Dx.numerator) / Dx.denominator)) + mp.mpf(s.numerator) / s.denominator
def root(m2, t2):
    lo, hi = Fr(0), Fr(1, 50)
    # D2 decreasing on the relevant range (ell' > 0, delta' > 0 while ell < 1); scan then bisect
    n = 2000
    for k in range(1, n + 1):
        x = hi * k / n
        if D2(x, m2, t2) <= 0:
            lo, hi = hi * (k - 1) / n, x; break
    for _ in range(120):
        mid = (lo + hi) / 2
        if D2(mid, m2, t2) > 0: lo = mid
        else: hi = mid
    return lo
for name, (m2, t2) in {"workbench (5834/39, 137/6)": (Fr(5834, 39), Fr(137, 6)), "exact values, rational upper bounds": (m2u, t2u)}.items():
    a = root(m2, t2)
    af = mp.mpf(a.numerator) / a.denominator
    print(f"{name}: alpha_2 = {mp.nstr(af, 15)}, g^2 >= {mp.nstr(1/(2*mp.sqrt(af)), 12)}, d_2(alpha_2) = {mp.nstr(d2(a, m2, t2), 10)}, "
          f"d_2(1/64) = {mp.nstr(d2(Fr(1,64), m2, t2), 10) if D2(Fr(1,64), m2, t2) >= 0 else 'n/a (outside)'}")
    print("    (3/2)m2 - 6 t2 =", float(Fr(3, 2) * m2 - 6 * t2), "> 0")
# with the unaudited cubic budget ||v3||_loc <= 944984/351 (the workbench's L10/L17 route)
def D2c(x, m2, t2, c3):
    ell = (m1 + 4 * t1) * x + (m2 + 4 * t2) * x**2
    dl = c3 * x**3 + 6 * m2 * t2 * x**4
    return (1 - ell)**2 - Fr(8, 3) * dl
for name, (m2, t2) in {"L17 as published": (Fr(5834, 39), Fr(137, 6)), "L17 with exact order-2 values": (m2u, t2u)}.items():
    lo, hi = Fr(0), Fr(1, 50)
    for k in range(1, 2001):
        x = hi * k / 2000
        if D2c(x, m2, t2, Fr(944984, 351)) <= 0:
            lo, hi = hi * (k - 1) / 2000, x; break
    for _ in range(120):
        mid = (lo + hi) / 2
        if D2c(mid, m2, t2, Fr(944984, 351)) > 0: lo = mid
        else: hi = mid
    af = mp.mpf(lo.numerator) / lo.denominator
    print(f"{name}: g^2 >= {mp.nstr(1/(2*mp.sqrt(af)), 12)}")
