#!/usr/bin/env python3
"""Referee v2, script r01 (independent of the review's and the author's scripts).

Prop 3.11 of the zeta reader v2 (Carleman density criterion) for S = {2^a 3^b : a+b >= 1}.

Checks
 A. nu(x) = #{(a,b) != (0,0): a log2 + b log3 <= x} = kappa x^2 + O(x), kappa = 1/(2 log2 log3).
 B. Carleman sum C1(R) = sum_{log n < R} (1/log n - log n/R^2) = (4/3) kappa R + O(log R);
    reader's threshold t* = 1/(4 pi kappa) = log2 log3/(2 pi) = 0.12120.
 C. Jensen threshold 1/(4 kappa) = log2 log3 / 2 = 0.3807 (reader's section 9).
 D. The constants of the reader's step 3: int_{-pi/2}^{pi/2} sin^2 cos = 2/3;
    (1/(4 pi t)) int_0^R (1 - y^2/R^2) dy = R/(6 pi t).
 E. REFEREE'S ANGLE VERSION.  Carleman's formula applied to F(z) = L(z^{1/2}) (equivalently
    Nevanlinna's formula for the angle |arg w| < alpha = pi/(2k), here any 0 < k <= 2):
      zero side   C_k(X) = sum_{log n < X} (x_n^{-k} - x_n^k X^{-2k}),  x_n = log n,
      bound side  X^{2-k} / (pi t (4 - k^2))  (k < 2),   (log X)/(4 pi t)  (k = 2),
    using only the reader's growth bound log|L(u+iv)| <= v^2/(4t) + O(|u|) + O(log|v|).
    The constant rests on the identity (4-k^2) I1(alpha) + 2k sin^2(alpha) = 4/k,
    I1 = int_{-alpha}^{alpha} sin^2(phi) cos(k phi) dphi, alpha = pi/(2k), checked here.
    For the lattice C_k(X) X^{k-2} -> 4 kappa k/(4-k^2) and C_2(X) = 2 kappa log X + O(1),
    so the family is dense for t > 1/(4 pi kappa k); k = 2 gives t > log2 log3/(4 pi) = 0.06060.
"""
import math
import numpy as np
import mpmath as mp

L2, L3 = math.log(2.0), math.log(3.0)
kappa = 1.0 / (2.0 * L2 * L3)
ok_all = True
def report(name, cond, info=""):
    global ok_all
    ok_all &= bool(cond)
    print(("[PASS] " if cond else "[FAIL] ") + name + ("" if info == "" else ": " + info))

def lattice_logs(Xmax):
    xs = []
    amax = int(Xmax / L2) + 1
    for a in range(amax + 1):
        bmax = int((Xmax - a * L2) / L3) + 1
        b = np.arange(0, bmax + 1)
        x = a * L2 + b * L3
        x = x[(x <= Xmax) & (x > 0)]
        xs.append(x)
    return np.sort(np.concatenate(xs))

XMAX = 1600.0
xs = lattice_logs(XMAX)
print(f"lattice points with log n <= {XMAX}: {len(xs)}")

# A
rows = []
for x in (50, 200, 800, 1600):
    nu = np.searchsorted(xs, x, side="right")
    rows.append((x, nu, nu / (kappa * x * x), (nu - kappa * x * x) / x))
report("A  nu(x)/(kappa x^2) -> 1 with (nu - kappa x^2)/x bounded",
       abs(rows[-1][2] - 1) < 2e-3 and max(abs(r[3]) for r in rows) < 3,
       "; ".join(f"x={r[0]}: ratio {r[2]:.5f}, (nu-kx^2)/x {r[3]:.3f}" for r in rows))

# B
def C1(R):
    x = xs[xs < R]
    return float(np.sum(1.0 / x - x / R**2))
tstar = 1.0 / (4 * math.pi * kappa)
rat = [(R, C1(R) / ((4.0 / 3.0) * kappa * R), C1(R) - (4.0 / 3.0) * kappa * R) for R in (100, 200, 400, 800, 1600)]
report("B  C1(R)/((4/3) kappa R) -> 1; t* = log2 log3/(2 pi)",
       abs(rat[-1][1] - 1) < 0.01 and abs(tstar - L2 * L3 / (2 * math.pi)) < 1e-15 and abs(tstar - 0.12120) < 5e-6,
       "; ".join(f"R={r[0]}: {r[1]:.5f} (diff {r[2]:.2f}, diff/logR {r[2]/math.log(r[0]):.3f})" for r in rat) + f"; t* = {tstar:.6f}")

# C
tJ = 1.0 / (4 * kappa)
def jensen_ratio(R):
    # R^{-2} int_{x0}^{R} nu(x) dx/x = R^{-2} sum_n log(R/x_n)
    x = xs[xs <= R]
    return float(np.sum(np.log(R / x))) / R**2
jr = [(R, jensen_ratio(R) / (kappa / 2)) for R in (200, 800, 1600)]
report("C  Jensen: R^{-2} int nu(x)dx/x -> kappa/2, threshold 1/(4 kappa) = log2 log3/2",
       abs(jr[-1][1] - 1) < 0.01 and abs(tJ - 0.38075) < 5e-5,
       "; ".join(f"R={r[0]}: ratio {r[1]:.5f}" for r in jr) + f"; threshold {tJ:.5f}")

# D
mp.mp.dps = 30
arc = mp.quad(lambda p: mp.sin(p)**2 * mp.cos(p), [-mp.pi / 2, mp.pi / 2])
R, t = mp.mpf(1000), mp.mpf('0.2')
axis = (1 / (4 * mp.pi * t)) * mp.quad(lambda y: 1 - y**2 / R**2, [0, R])
report("D  step-3 constants: arc integral 2/3 and axis term R/(6 pi t)",
       abs(arc - mp.mpf(2) / 3) < 1e-25 and abs(axis - R / (6 * mp.pi * t)) < 1e-20,
       f"arc {mp.nstr(arc, 20)}, axis/(R/(6 pi t)) {mp.nstr(axis / (R / (6 * mp.pi * t)), 20)}")

# E1: the identity (4-k^2) I1 + 2k sin^2(alpha) = 4/k  (arc + ray constants of the angle formula)
worst = 0
for k in (mp.mpf('0.5'), mp.mpf('0.8'), 1, mp.mpf('1.3'), mp.mpf('1.5'), mp.mpf('1.8'), mp.mpf('1.95'), 2):
    al = mp.pi / (2 * k)
    I1 = mp.quad(lambda p: mp.sin(p)**2 * mp.cos(k * p), [-al, al])
    worst = max(worst, abs((4 - k**2) * I1 + 2 * k * mp.sin(al)**2 - 4 / k))
report("E1 (4-k^2) I1(alpha) + 2k sin^2(alpha) = 4/k for alpha = pi/(2k), 0.5 <= k <= 2", worst < 1e-25, f"max error {mp.nstr(worst, 3)}")

# E2: k = 2 directly in the z = w^2 plane: arc term O(1) and axis term (log R')/(8 pi t)
arc2 = mp.quad(lambda p: mp.sin(p / 2)**2 * mp.cos(p), [-mp.pi / 2, mp.pi / 2])
report("E2 k=2: arc integral int sin^2(psi/2) cos psi = 1 - pi/4 (bounded arc term)", abs(arc2 - (1 - mp.pi / 4)) < 1e-25, mp.nstr(arc2, 15))

# E3: lattice zero sums for the angle formula
def Ck(X, k):
    x = xs[xs < X]
    return float(np.sum(x**(-k) - x**k / X**(2 * k)))
out = []
for k in (1.0, 1.5, 1.9):
    # the main term 4 kappa k/(4-k^2) X^{2-k} grows; the remainder C_k - main term must stay bounded
    rem = [Ck(X, k) - 4 * kappa * k / (4 - k * k) * X**(2 - k) for X in (200.0, 400.0, 800.0, 1600.0)]
    out.append((k, rem, 1.0 / (4 * math.pi * kappa * k)))
C2 = [(X, Ck(X, 2.0) - 2 * kappa * math.log(X)) for X in (50.0, 200.0, 800.0, 1600.0)]
def rem_ok(k, rem):
    if k == 1.0:   # O(log X) remainder, as the reader states: remainder/log X stays bounded
        return max(abs(r) / math.log(X) for r, X in zip(rem, (200.0, 400.0, 800.0, 1600.0))) < 1.5
    return abs(rem[-1] - rem[-2]) < 0.05       # k > 1: bounded, converging remainder
report("E3 C_k(X) = 4 kappa k/(4-k^2) X^{2-k} + remainder (O(log X) for k = 1, converging for k = 1.5, 1.9); C_2(X) - 2 kappa log X converges",
       all(rem_ok(o[0], o[1]) for o in out) and abs(C2[-1][1] - C2[-2][1]) < 0.01,
       "; ".join(f"k={o[0]}: remainders " + ", ".join(f"{r:.4f}" for r in o[1]) + f" (X=200..1600), threshold t > {o[2]:.5f}" for o in out)
       + "; C2 - 2 kappa logX: " + ", ".join(f"{c[1]:.4f}@{int(c[0])}" for c in C2))

t2 = 1.0 / (8 * math.pi * kappa)
report("E4 angle threshold t > 1/(8 pi kappa) = log2 log3/(4 pi) = t*/2",
       abs(t2 - L2 * L3 / (4 * math.pi)) < 1e-15 and abs(t2 - tstar / 2) < 1e-15,
       f"t_angle = {t2:.6f} against the reader's t* = {tstar:.6f}")

print("ALL CHECKS PASS" if ok_all else "SOME CHECKS FAILED")
