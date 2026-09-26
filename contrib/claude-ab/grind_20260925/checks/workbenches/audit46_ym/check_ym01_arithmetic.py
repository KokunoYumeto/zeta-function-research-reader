#!/usr/bin/env python3
"""Independent re-derivation of the closed-form arithmetic of YM-01 (FIFTH_REFERENCE.md F26-F38).

Inputs: only the ten rational bounds (m_i, t_i) of F26, typed in from the source.
Everything else (ell, delta, D, alpha, threshold, d5 values, w_* values, monotonicity,
the chi<1/2 claim, the nonnegativity of the d5 coefficients) is recomputed here with
exact rationals and 60-digit mpmath, without importing any workbench code.
Written for audit 46 (read-only; nothing in the repository is touched).
"""
from fractions import Fraction as F
import mpmath as mp
mp.mp.dps = 60

m = {1: F(64, 3), 2: F(5834, 39), 3: F(336572872, 208845),
     4: F(17270702970768271, 341697152160), 5: F(1638684)}
t = {1: F(16, 3), 2: F(137, 6), 3: F(225985217, 1253070),
     4: F(110695177857394584026401, 18025447358750832000), 5: F(190128)}

ok_all = True
def report(name, ok, val=None):
    global ok_all
    ok_all &= bool(ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + ("" if val is None else f": {val}"))

b = {(i, j): 3 * (m[i] * t[j] + m[j] * t[i]) for i in range(1, 6) for j in range(1, 6)}
def ell(x): return sum((m[i] + 4 * t[i]) * x**i for i in range(1, 6))
def delta(x): return sum(b[i, j] * x**(i + j) for i in range(1, 6) for j in range(1, 6) if i + j >= 6)
def D(x): return (1 - ell(x))**2 - F(8, 3) * delta(x)

# A1: the hand-derivable first coefficients (v1 = (1/3) sum_p W_p, ||W_p||_X = 8, 4 plaquettes per edge)
report("A1 m1 = 4 plaquettes * (sum j_e = 2) * (8/3)", m[1] == 4 * 2 * F(8, 3), m[1])
report("A1 t1 = 4 plaquettes * (j_e = 1/2) * (8/3)", t[1] == 4 * F(1, 2) * F(8, 3), t[1])
report("A1 ell'(0) = m1 + 4 t1 = 128/3 (source check 'first-linear-factor-two')", m[1] + 4 * t[1] == F(128, 3))

# A2: sign change and uniqueness of the first positive root on [0, 19/1000]
report("A2 D(18/1000) > 0", D(F(18, 1000)) > 0, float(D(F(18, 1000))))
report("A2 D(19/1000) < 0", D(F(19, 1000)) < 0, float(D(F(19, 1000))))
report("A2 ell(19/1000) < 1 (so D' < 0 on [0,19/1000])", ell(F(19, 1000)) < 1, float(ell(F(19, 1000))))
# D has no root on (0, 18/1000]: D decreasing there and D(18/1000) > 0; D(0) = 1.

# A3: exact bisection for alpha
lo, hi = F(18, 1000), F(19, 1000)
for _ in range(80):
    mid = (lo + hi) / 2
    if D(mid) > 0: lo = mid
    else: hi = mid
report("A3 alpha bracket inside source's (F29)",
       F('0.018424953576117616681') < lo and hi < F('0.018424953576117616682'),
       f"{mp.mpf(lo.numerator)/lo.denominator}")
alpha = mp.mpf(lo.numerator) / lo.denominator
thr = 1 / (2 * mp.sqrt(alpha))
report("A3 threshold 1/(2 sqrt alpha) inside (3.683551983985727304439, ...440)",
       mp.mpf('3.683551983985727304439') < thr < mp.mpf('3.683551983985727304440'), mp.nstr(thr, 25))
# xi <= alpha  <=>  1/(4 g^4) <= alpha  <=>  g^2 >= 1/(2 sqrt alpha)
report("A3 ell(alpha) and delta(alpha)", True, f"ell={float(ell(lo)):.6f}, delta={float(delta(lo)):.3e}, theta=8delta/(3(1-ell)^2)={float(F(8,3)*delta(lo)/(1-ell(lo))**2):.9f}")

# A4: d5 and w_* at the quoted couplings (F38) with 60-digit arithmetic
def mpf(q): return mp.mpf(q.numerator) / q.denominator
def wstar(x): return mp.mpf(3) / 4 * (1 - mpf(ell(x)) - mp.sqrt(mpf(D(x))))
def d5(x):
    return mp.mpf(3) / 2 * (1 + mp.sqrt(mpf(D(x)))) + sum(mpf(F(3, 2) * m[i] - 6 * t[i]) * mpf(x)**i for i in range(1, 6))
def chi(x): return 4 * sum(mpf(t[i]) * mpf(x)**i for i in range(1, 6)) + mp.mpf(2) / 3 * wstar(x)
table = [(F(37, 10), '1.6207', '0.046581'), (F(15, 4), '1.6993', '0.026352'), (F(4), '1.9068', '0.005752')]
for g2, dq, wq in table:
    x = 1 / (4 * g2 * g2)
    dv, wv = d5(x), wstar(x)
    report(f"A4 g^2={g2}: xi={x} <= alpha", x <= lo)
    report(f"A4 g^2={g2}: d5 > {dq}", dv > mp.mpf(dq), mp.nstr(dv, 12))
    report(f"A4 g^2={g2}: w_* < {wq}", wv < mp.mpf(wq), mp.nstr(wv, 12))
    report(f"A4 g^2={g2}: d5 == 3(1-chi) (F35 algebra)", abs(dv - 3 * (1 - chi(x))) < mp.mpf('1e-50'))

# A5: nonnegative coefficients (3/2)m_i - 6 t_i ; endpoint values
coef = {i: F(3, 2) * m[i] - 6 * t[i] for i in range(1, 6)}
report("A5 all (3/2)m_i - 6t_i >= 0", all(c >= 0 for c in coef.values()), {i: float(c) for i, c in coef.items()})
report("A5 d5(0) = 3 (strong-coupling electric gap 3 kappa)", d5(F(0)) == 3)
d_end = d5(lo)
report("A5 d5 at alpha endpoint > 3/2 (chi < 1/2)", d_end > mp.mpf(1.5), mp.nstr(d_end, 15))

# A6: monotonicity of d5 on a fine grid (sanity, not a proof; the proof is the w' > 0 argument after F35)
xs = [lo * k / 2000 for k in range(1, 2001)]
vals = [d5(x) for x in xs]
report("A6 d5 decreasing on a 2000-point grid of (0, alpha]", all(vals[k] > vals[k + 1] for k in range(len(vals) - 1)))

# A7: majorant identity: w_* is the small root of (2/3)w^2 - (1-ell)w + delta = 0
for x in [F(1, 100), F(1, 64), lo]:
    wv = wstar(x)
    res = mp.mpf(2) / 3 * wv**2 - (1 - mpf(ell(x))) * wv + mpf(delta(x))
    report(f"A7 majorant root identity at x={float(x):.6f}", abs(res) < mp.mpf('1e-40'), mp.nstr(res, 5))

# A8: what the d5 bound gives at g^2 = 4 in plain numbers
x4 = F(1, 64)
print(f"INFO g^2=4: xi=1/64, ell={float(ell(x4)):.6f}, delta={float(delta(x4)):.4e}, D={float(D(x4)):.6f}, chi={mp.nstr(chi(x4),8)}, d5={mp.nstr(d5(x4),10)}")
print(f"INFO sensitivity: x^5 (m5+4t5) at alpha = {float(lo**5*(m[5]+4*t[5])):.5f}; x^4 (m4+4t4) = {float(lo**4*(m[4]+4*t[4])):.5f}")
# A9: the same bound in lattice units, a*Delta_L >= a*kappa*d5 = 2 g^2 d5(1/(4 g^4))
for g2 in [F(37, 10), F(15, 4), F(4), F(13), F(16)]:
    x = 1 / (4 * g2 * g2)
    print(f"INFO lattice units: g^2={g2}: a*Delta_L >= 2 g^2 d5 = {mp.nstr(2 * mpf(g2) * d5(x), 8)}  (strong-coupling leading value 6 g^2 = {float(6*g2)})")
gthr = 1 / (2 * mp.sqrt(mpf(lo)))
print(f"INFO lattice units at the domain edge g^2 = 1/(2 sqrt alpha5): a*Delta_L >= {mp.nstr(2 * gthr * d5(lo), 8)}")
print("ALL PASS" if ok_all else "SOME FAIL")

# A10: sensitivity of alpha_5 and of d5(1/64) to the largest finite inputs (m5, t5), and to (m4, t4)
def alpha_with(mm, tt):
    bb = {(i, j): 3 * (mm[i] * tt[j] + mm[j] * tt[i]) for i in range(1, 6) for j in range(1, 6)}
    el = lambda x: sum((mm[i] + 4 * tt[i]) * x**i for i in range(1, 6))
    de = lambda x: sum(bb[i, j] * x**(i + j) for i in range(1, 6) for j in range(1, 6) if i + j >= 6)
    DD = lambda x: (1 - el(x))**2 - F(8, 3) * de(x)
    a, bnd = F(0), F(19, 1000)
    for _ in range(70):
        md = (a + bnd) / 2
        if DD(md) > 0: a = md
        else: bnd = md
    dd = lambda x: mp.mpf(3) / 2 * (1 + mp.sqrt(mpf(DD(x)))) + sum(mpf(F(3, 2) * mm[i] - 6 * tt[i]) * mpf(x)**i for i in range(1, 6))
    return a, (dd(F(1, 64)) if DD(F(1, 64)) >= 0 else None)
for label, fac5, fac4 in [("m5,t5 x2", 2, 1), ("m5,t5 x1.1", F(11, 10), 1), ("m4,t4 x2", 1, 2)]:
    mm = dict(m); tt = dict(t)
    mm[5] *= fac5; tt[5] *= fac5; mm[4] *= fac4; tt[4] *= fac4
    a, d64 = alpha_with(mm, tt)
    print(f"INFO sensitivity {label}: alpha = {float(a):.6f}, threshold g^2 = {float(1/(2*mp.sqrt(mpf(a)))):.4f}, d5(1/64) = {mp.nstr(d64, 6) if d64 is not None else 'outside domain'}")
