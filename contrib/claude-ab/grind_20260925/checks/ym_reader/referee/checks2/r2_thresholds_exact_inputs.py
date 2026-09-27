# Referee check: thresholds of Corollary 3.5 / L17 of the YM reader with the independently computed norms
#   order 2: m(v2) = 134.0673186784, t(v2) = 19.7953312398   (closed forms in r2_order2_threshold.py)
#   order 3: m(v3) = 1203.1424168419, t(v3) = 127.2886523082, ||v3||_loc = 1965.1583644493  (r2_order3_run.py)
# each rounded UP to 4 decimals; orders 4-5 from F26 where used.
from fractions import Fraction as Fr
import mpmath as mp
mp.mp.dps = 40
m = {1: Fr(64, 3), 2: Fr(1340674, 10000), 3: Fr(12031425, 10000),
     4: Fr(17270702970768271, 341697152160), 5: Fr(1638684)}
t = {1: Fr(16, 3), 2: Fr(197954, 10000), 3: Fr(1272887, 10000),
     4: Fr(110695177857394584026401, 18025447358750832000), 5: Fr(190128)}
mW = {1: Fr(64, 3), 2: Fr(5834, 39), 3: Fr(336572872, 208845)}
tW = {1: Fr(16, 3), 2: Fr(137, 6), 3: Fr(225985217, 1253070)}
def make(N, mm, tt, resid_override=None):
    ell = {i: mm[i] + 4 * tt[i] for i in range(1, N + 1)}
    dl = {}
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i + j >= N + 1: dl[i + j] = dl.get(i + j, 0) + 3 * (mm[i] * tt[j] + mm[j] * tt[i])
    if resid_override: dl.update(resid_override)
    s = {i: Fr(3, 2) * mm[i] - 6 * tt[i] for i in range(1, N + 1)}
    return ell, dl, s
def ev(c, x): return sum(v * x**k for k, v in c.items())
def D(P, x):
    ell, dl, s = P; return (1 - ev(ell, x))**2 - Fr(8, 3) * ev(dl, x)
def d(P, x):
    ell, dl, s = P; Dx = D(P, x)
    return mp.mpf(3) / 2 * (1 + mp.sqrt(mp.mpf(Dx.numerator) / Dx.denominator)) + mp.mpf(ev(s, x).numerator) / ev(s, x).denominator
def root(P):
    lo, hi = Fr(0), Fr(1, 40)
    for k in range(1, 4001):
        x = hi * k / 4000
        if D(P, x) <= 0: lo, hi = hi * (k - 1) / 4000, x; break
    for _ in range(100):
        mid = (lo + hi) / 2
        if D(P, mid) > 0: lo = mid
        else: hi = mid
    return lo
def report(name, P):
    a = root(P); af = mp.mpf(a.numerator) / a.denominator
    extra = []
    for g2 in (Fr(4), Fr(15, 4), Fr(37, 10)):
        x = 1 / (4 * g2**2)
        if D(P, x) >= 0 and x <= a: extra.append(f"d({g2})={mp.nstr(d(P, x), 7)}")
    print(f"{name}: g^2 >= {mp.nstr(1/(2*mp.sqrt(af)), 10)}, d(alpha) = {mp.nstr(d(P, a), 8)}; " + ", ".join(extra))
    ell, dl, s = P
    assert all(v > 0 for v in ell.values()) and all(v > 0 for v in dl.values())
    assert all(v >= 0 for v in s.values()), "a coefficient 3/2 m_i - 6 t_i is negative"
print("coefficients (3/2)m_i - 6t_i with exact inputs:", {i: float(Fr(3, 2) * m[i] - 6 * t[i]) for i in (1, 2, 3)})
report("N=2, workbench inputs (reader's Cor. 3.5(b))", make(2, mW, tW))
report("N=2, exact inputs", make(2, m, t))
report("N=3, workbench inputs", make(3, mW, tW))
report("N=3, exact inputs (orders 1-3 all independently computed)", make(3, m, t))
report("L17 route: N=2 + ||v3||_loc = 944984/351 (workbench)", make(2, mW, tW, {3: Fr(944984, 351), 4: 6 * mW[2] * tW[2]}))
report("L17 route: N=2 exact + ||v3||_loc exact 1965.1584", make(2, m, t, {3: Fr(19651584, 10000), 4: 6 * m[2] * t[2]}))
m4 = dict(m); t4 = dict(t)
report("N=4, exact orders 1-3 + workbench order 4", make(4, m4, t4))
report("N=5, exact orders 1-3 + workbench orders 4-5", make(5, m, t))
mw5 = dict(m); tw5 = dict(t); mw5[2], tw5[2], mw5[3], tw5[3] = mW[2], tW[2], mW[3], tW[3]
report("N=5, all workbench inputs (Theorem 3.1)", make(5, mw5, tw5))
