#!/usr/bin/env python3
"""ref_fold_patch_independent.py -- independent re-verification of the fold patch (F0)-(Fc) of certify_hydro_radius.py
(note 51_, Theorem 51.2), with the mpmath.iv evaluator of ivG.py (36 terms, independent tail bound) and a finer,
different discretization: 128 segments per edge of boundary(A_F) and of boundary(X_F) (the certificate uses 64).
Every boundary point is an exact binary number, so the segment boxes cover the two square boundaries exactly.

Also (non-rigorous, mpmath): the zero of the discriminant Delta(x) = 2 p_2 - p_1^2 in X_F computed from contour
integrals p_k = (2 pi i)^(-1) oint alpha^k G_alpha/G d alpha, compared with x* = q*^2/4.
"""
import time, pickle
import mpmath
from mpmath import iv, mp
import ivG

mp.dps = 40
T0 = time.time()
D = pickle.load(open('cells_dump.pkl', 'rb'))
XC = mpmath.mpf(D['XC']); ETA = mpmath.mpf(D['ETA']); AL0 = mpmath.mpf(D['AL0']); RHO = mpmath.mpf(D['RHO_F'])
res = []
def check(name, ok, extra=""):
    res.append((name, bool(ok))); print(("PASS" if ok else "FAIL") + "  " + name + (("  " + extra) if extra else ""), flush=True)

def square_pts(cr, ci, h, n):
    """counterclockwise corner-and-edge points (exact binary numbers when cr, ci, h are dyadic and n a power of 2)."""
    corners = [(cr + h, ci - h), (cr + h, ci + h), (cr - h, ci + h), (cr - h, ci - h)]
    pts = []
    for e in range(4):
        (x1, y1), (x2, y2) = corners[e], corners[(e + 1) % 4]
        for k in range(n):
            pts.append((x1 + (x2 - x1) * k / n, y1 + (y2 - y1) * k / n))
    return pts
def seg(p, q):
    return iv.mpc(iv.mpf([min(p[0], q[0]), max(p[0], q[0])]), iv.mpf([min(p[1], q[1]), max(p[1], q[1])]))
def ptv(p):
    return iv.mpc(p[0], p[1])

# ---- (F0) certified collision (certify_collision.py) inside A_F x X_F
q0 = mpmath.mpf('0.778472800990330076180356446189'); a0 = mpmath.mpf('-0.569714080972361784438457668663')
qb = iv.mpf([q0 - mpmath.mpf('1e-20'), q0 + mpmath.mpf('1e-20')])
xb = qb * qb / 4
ab = iv.mpf([a0 - mpmath.mpf('1.5e-10'), a0 + mpmath.mpf('1.5e-10')])
check("(F0) the certified collision box lies in int(A_F) x int(X_F)",
      XC - ETA < xb.a and xb.b < XC + ETA and AL0 - RHO < ab.a and ab.b < AL0 + RHO)

NE = 128
# ---- (Fa) G != 0 on boundary(A_F) x X_F
bA = square_pts(AL0, mpmath.mpf(0), RHO, NE)
NX = 4
xsubs = []
for i in range(NX):
    for j in range(NX):
        xsubs.append(iv.mpc(iv.mpf([XC - ETA + 2 * ETA * i / NX, XC - ETA + 2 * ETA * (i + 1) / NX]),
                            iv.mpf([-ETA + 2 * ETA * j / NX, -ETA + 2 * ETA * (j + 1) / NX])))
okA = True; minabs = None
for k in range(len(bA)):
    sb = seg(bA[k], bA[(k + 1) % len(bA)])
    for xs in xsubs:
        g, _ = ivG.G_Ga(sb, xs, deriv=False)
        if ivG.contains_zero(g):
            okA = False
        lo = max(0, min(abs(g.real.a), abs(g.real.b)) if g.real.a * g.real.b > 0 else 0,
                 min(abs(g.imag.a), abs(g.imag.b)) if g.imag.a * g.imag.b > 0 else 0)
        minabs = lo if minabs is None or lo < minabs else minabs
check(f"(Fa) G != 0 on boundary(A_F) x X_F ({len(bA)} segments x {len(xsubs)} x-boxes)", okA, f"min |G| >~ {mpmath.nstr(minabs, 4)}  [{time.time()-T0:.0f}s]")

# ---- winding numbers from enclosures: each segment enclosure excludes 0 (so the arg change on it is < pi) and the
#      endpoint ratio has positive real part; the principal args are summed in interval arithmetic
def winding(vals, boxes):
    tot = iv.mpf(0); ok = True
    for k in range(len(vals)):
        if ivG.contains_zero(boxes[k]):
            ok = False
        r = vals[(k + 1) % len(vals)] / vals[k]
        if not (r.real.a > 0):
            ok = False
        tot += iv.atan2(r.imag, r.real)       # principal argument (Re r > 0 checked above)
    return ok, tot / (2 * iv.pi)
xpt = iv.mpc(XC, 0)
vals = [ivG.G_Ga(ptv(p), xpt, deriv=False)[0] for p in bA]
boxes = [ivG.G_Ga(seg(bA[k], bA[(k + 1) % len(bA)]), xpt, deriv=False)[0] for k in range(len(bA))]
okb, w = winding(vals, boxes)
check("(Fb) winding number of G(., XC) along boundary(A_F) is 2", okb and w.a > 1.5 and w.b < 2.5, f"winding in [{mpmath.nstr(w.a, 8)}, {mpmath.nstr(w.b, 8)}]")

# ---- (Fc) two separated zeros on boundary(X_F) and the winding of Delta
def newton(al, x):
    for _ in range(80):
        g, ga = ivG.point_G_Ga(al, x, N=120)
        st = g / ga
        if abs(st) > 0.05:
            st = st * 0.05 / abs(st)
        al -= st
        if abs(st) < mpmath.mpf('1e-30'):
            break
    return al
def krawczyk(X, x0, guess):
    c = newton(guess, x0)
    cv = iv.mpc(c.real, c.imag)
    _, ga0 = ivG.point_G_Ga(c, x0, N=120)
    Yp = 1 / ga0; Y = iv.mpc(Yp.real, Yp.imag)
    Gc, _ = ivG.G_Ga(cv, X, deriv=False)
    YG = Y * Gc
    base = max(abs(YG.real.a), abs(YG.real.b), abs(YG.imag.a), abs(YG.imag.b))
    for fac in (2, 3, 5, 8, 13, 21, 34):
        rho = max(base * fac, mpmath.mpf('1e-25'))
        A = iv.mpc(iv.mpf([c.real - rho, c.real + rho]), iv.mpf([c.imag - rho, c.imag + rho]))
        _, GaA = ivG.G_Ga(A, X)
        K = cv - YG + (1 - Y * GaA) * (A - cv)
        if ivG.contains_interior(A, K):
            return True, A, K
    return False, None, None
AFbox = iv.mpc(iv.mpf([AL0 - RHO, AL0 + RHO]), iv.mpf([-RHO, RHO]))
def disjoint(A1, A2):
    return A1.real.b < A2.real.a or A2.real.b < A1.real.a or A1.imag.b < A2.imag.a or A2.imag.b < A1.imag.a
def two_roots(X, x0):
    r = mpmath.sqrt(XC - x0)
    ok1, A1, K1 = krawczyk(X, x0, AL0 + mpmath.mpf('1.34') * r)
    ok2, A2, K2 = krawczyk(X, x0, AL0 - mpmath.mpf('1.34') * r)
    if not (ok1 and ok2) or not disjoint(A1, A2) or not (ivG.contains_interior(AFbox, A1) and ivG.contains_interior(AFbox, A2)):
        return False, None, None
    return True, K1, K2
bX = square_pts(XC, mpmath.mpf(0), ETA, NE)
okc = True; dv = []; db = []
for k in range(len(bX)):
    p = bX[k]; q = bX[(k + 1) % len(bX)]
    o1, K1, K2 = two_roots(ptv(p), mp.mpc(p[0], p[1]))
    o2, S1, S2 = two_roots(seg(p, q), mp.mpc((p[0] + q[0]) / 2, (p[1] + q[1]) / 2))
    if not (o1 and o2):
        okc = False; print("   failure at", p); break
    dv.append((K1 - K2) ** 2); db.append((S1 - S2) ** 2)
if okc:
    okw, wD = winding(dv, db)
    check(f"(Fc) on boundary(X_F) ({len(bX)} segments) the two zeros are separated and wind(Delta) = 1",
          okw and wD.a > 0.5 and wD.b < 1.5, f"winding in [{mpmath.nstr(wD.a, 8)}, {mpmath.nstr(wD.b, 8)}]  [{time.time()-T0:.0f}s]")
else:
    check("(Fc) discriminant winding", False)

# ---- non-rigorous: locate the zero of Delta in X_F from contour-integral power sums, compare with x*
mp.dps = 30
def Delta(x):
    def integrand(t, k):
        al = AL0 + RHO * mp.expj(t) * 1          # circle of radius RHO about AL0 (contains the same two zeros)
        g, ga = ivG.point_G_Ga(al, x, N=80)
        return al ** k * ga / g * RHO * 1j * mp.expj(t)
    p1 = mp.quad(lambda t: integrand(t, 1), [0, mp.pi / 2, mp.pi, 3 * mp.pi / 2, 2 * mp.pi]) / (2j * mp.pi)
    p2 = mp.quad(lambda t: integrand(t, 2), [0, mp.pi / 2, mp.pi, 3 * mp.pi / 2, 2 * mp.pi]) / (2j * mp.pi)
    return 2 * p2 - p1 ** 2, p1
xstar = (mp.mpf('0.778472800990330076180356446189') ** 2) / 4
xz = mp.findroot(lambda x: mp.re(Delta(x)[0]), (xstar - mp.mpf('1e-3'), xstar + mp.mpf('1e-3')), solver='anderson')
d0, p1z = Delta(xz)
print(f"   (N) zero of Delta: x = {mp.nstr(xz, 20)}, x* = {mp.nstr(xstar, 20)}, |diff| = {mp.nstr(abs(xz - xstar), 3)}; p_1/2 there = {mp.nstr(p1z / 2, 15)}")
dd = mp.diff(lambda x: Delta(x)[0], xstar)
print(f"   (N) Delta'(x*) = {mp.nstr(dd, 12)}  (predicted -4 kappa^2 = -16 F_q/(q* F_aa) = -7.186435...)")
n = len(res); npass = sum(ok for _, ok in res)
print(f"\nsummary: {n} checks, {npass} PASS, {n - npass} FAIL  [{time.time()-T0:.0f}s]")
