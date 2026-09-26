#!/usr/bin/env python3
"""Referee v2, script r13.  Lemma 6.6 (version 2: C^1 fields) for the reader's map F.
 1. det DF = -2 identically; F^{-1}(-1/4, 0, 0) contains (0, 0, -1/4) and (+-1, -+3/2, 13/2).
 2. For a non-affine polynomial field V = (x y^2 + z, x^2 - y z, x y z) and U = DF^{-1} (V o F):
    div U = (div V) o F and DF . U = V o F, exactly (symbolically, then spot values at rational points).
 3. The escaping curve gamma(tau) = (1/z, -3z/2, 13 z^2/2), z = sqrt(1 - 8 tau): F(gamma(tau)) = (-1/4 + 2 tau, 0, 0)
    and gamma' = U(gamma) for V = (2, 0, 0).
"""
import sympy as sp
x, y, w, tau = sp.symbols('x y w tau')
F = sp.Matrix([(1 + x*y)**3*w + y**2*(1 + x*y)*(4 + 3*x*y), y + 3*x*(1 + x*y)**2*w + 3*x*y**2*(4 + 3*x*y), 2*x - 3*x**2*y - x**3*w])
X = sp.Matrix([x, y, w])
DF = F.jacobian(X)
ok = True
det = sp.simplify(DF.det()); ok &= det == -2
pts = [(0, 0, sp.Rational(-1, 4)), (1, sp.Rational(-3, 2), sp.Rational(13, 2)), (-1, sp.Rational(3, 2), sp.Rational(13, 2))]
ok &= all(sp.simplify(F.subs({x: a, y: b, w: c}) - sp.Matrix([sp.Rational(-1, 4), 0, 0])) == sp.zeros(3, 1) for a, b, c in pts)
print(("[PASS] " if ok else "[FAIL] ") + f"1 det DF = {det}; the three listed preimages of (-1/4, 0, 0)")
p, q, r = sp.symbols('p q r')
Vf = sp.Matrix([p*q**2 + r, p**2 - q*r, p*q*r])
divV = sum(sp.diff(Vf[i], v) for i, v in enumerate((p, q, r)))
VoF = Vf.subs({p: F[0], q: F[1], r: F[2]}, simultaneous=True)
adj = DF.adjugate()
U = adj * VoF / det
divU = sum(sp.diff(U[i], v) for i, v in enumerate((x, y, w)))
lhs = sp.expand(divU - divV.subs({p: F[0], q: F[1], r: F[2]}, simultaneous=True))
ok2 = lhs == 0 and sp.expand(DF * U - VoF) == sp.zeros(3, 1)
print(("[PASS] " if ok2 else "[FAIL] ") + "2 div U = (div V) o F and DF U = V o F identically for a cubic non-affine V")
z = sp.sqrt(1 - 8*tau)
gam = sp.Matrix([1/z, -3*z/2, 13*z**2/2])
Fg = sp.simplify(F.subs({x: gam[0], y: gam[1], w: gam[2]}, simultaneous=True))
V2 = sp.Matrix([2, 0, 0])
Ug = (adj * V2 / det).subs({x: gam[0], y: gam[1], w: gam[2]}, simultaneous=True)
ok3 = sp.simplify(Fg - sp.Matrix([sp.Rational(-1, 4) + 2*tau, 0, 0])) == sp.zeros(3, 1) and sp.simplify(gam.diff(tau) - Ug) == sp.zeros(3, 1)
print(("[PASS] " if ok3 else "[FAIL] ") + "3 F(gamma(tau)) = (-1/4 + 2 tau, 0, 0) and gamma' = U(gamma) for V = (2,0,0)")
print("ALL CHECKS PASS" if (ok and ok2 and ok3) else "SOME CHECKS FAILED")
