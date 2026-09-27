#!/usr/bin/env python3
"""ns51_sign_check.py -- certifies the sign kappa > 0 in Corollary 51.2': along the real segment the hydrodynamic
zero is the LARGER of the two real zeros that merge at x*.

Method: the evaluation G, G_alpha and the Krawczyk test are imported verbatim from certify_hydro_radius.py (the part
before its parameter block).  A chain of real x-intervals from 0 to x0 = X_c - 2^-8 is certified with real-centred,
real-symmetric alpha-boxes and consecutive consistency K_j in A_(j+1) (or conversely), starting from alpha = 0 at x = 0.
This is the analytic continuation of alpha_h along [0, x0] (unique along a path).  At x0 the two zeros in the fold box
A_F are enclosed by disjoint Krawczyk boxes; the hydrodynamic zero is the one met by the chain, and it is checked to be
the larger one.  Since the two real zeros are distinct on [x0, x*) (Delta > 0 there, Theorem 51.2) and both tend to
alpha*, the hydrodynamic zero is the upper one on the whole segment, i.e. alpha_h = alpha* + kappa sqrt(x* - x) + ...
with kappa > 0.
"""
import sys
src = open('certify_hydro_radius.py').read().split('# ------------------------------------------------------------------------------------------ parameters')[0]
exec(src)
XC = round(float(xc0) * 2**24) / 2**24
ETA = 2.0**-8
x0 = XC - ETA
N = 400
h = x0 / (2 * N)                      # half-width of each real x-cell
prev = None
ok = True
guess = acb(0)
for j in range(N):
    cx = h * (2 * j + 1)
    X = acb(arb(cx, h * (1 + 1e-9)))
    okj, A, K, c = krawczyk(X, acb(cx), guess, real_centre=True, need_slack=False)
    if not okj:
        ok = False; print("chain failed at cell", j, cx); break
    if j == 0 and not A.contains(acb(0)):
        ok = False; print("origin box does not contain alpha = 0"); break
    if prev is not None and not (A.contains(prev[1]) or prev[0].contains(K)):
        ok = False; print("consistency failed between cells", j - 1, j); break
    prev = (A, K)
    guess = acb(c.real.mid())
print(("PASS" if ok else "FAIL") + f"  real chain of {N} cells from x = 0 to x0 = X_c - 2^-8 = {x0!r} certified; hydro zero in {prev[1].real.str(12) if ok else '?'}")
# the two fold zeros at x0
AF = sqbox(acb(round(float(a0) * 2**24) / 2**24), 0.25)
r = (XC - x0) ** 0.5
AL0 = float(a0)
ok1, A1, K1, c1 = krawczyk(acb(x0), acb(x0), acb(AL0 + 1.34 * r), real_centre=True, need_slack=False)
ok2, A2, K2, c2 = krawczyk(acb(x0), acb(x0), acb(AL0 - 1.34 * r), real_centre=True, need_slack=False)
disjoint = ok1 and ok2 and not A1.overlaps(A2) and AF.contains_interior(A1) and AF.contains_interior(A2)
print(("PASS" if disjoint else "FAIL") + f"  two disjoint real zeros in A_F at x0: upper {K1.real.str(12)}, lower {K2.real.str(12)}")
# x0 lies in the last chain cell, so the hydrodynamic zero at x0 lies in prev K.  By (Fa)-(Fb) of the certificate, G(., x0)
# has exactly two zeros in A_F (x0 is on the boundary of the closed square X_F); they lie in K1 (upper) and K2 (lower).
# If prev K is inside A_F and disjoint from K2, the hydrodynamic zero is the upper one.
hydro_is_upper = ok and disjoint and AF.contains(prev[1]) and not prev[1].overlaps(K2) and prev[1].overlaps(K1)
print(("PASS" if hydro_is_upper else "FAIL") + "  the chain's hydrodynamic zero is the upper fold zero: kappa > 0 in Corollary 51.2'")
print("SIGN CERTIFIED" if (ok and disjoint and hydro_is_upper) else "NOT CERTIFIED")
