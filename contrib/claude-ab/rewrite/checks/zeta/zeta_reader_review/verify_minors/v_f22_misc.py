#!/usr/bin/env python3
"""F22 verification (independent code).

Prop 6.2 for integers a >= 2: a has exact multiplicative order d modulo a^d - 1 and gcd(a, a^d - 1) = 1 (a in {2,...,30}, d <= 40).
Lemma 6.4 for real a > 1:
  - a #-closed set Z in the strip with a = 1.5 in which a reflected off-line pair returns together;
  - a collision a rho = a' rho' with real a, a' > 1 and rho/rho' irrational (so "rho/rho' in Q_{>0}" needs a, a' rational),
    while on the critical line (1/2 + i g)/(1/2 + i g') is real only for g = g'.
Lemma 6.6 with a non-affine V: for the reader's F (det DF = -2) and V = (x^2 + y, y w, x^3 - w), U = adj(DF) (V o F)/c;
  check exactly (rational arithmetic, symbolic derivatives) at random rational points: det DF = -2, Piola identity,
  div U = (div V)(F), and DF U = V(F).  Completeness under a polynomial automorphism is flow conjugation (no computation).
"""
import random
from fractions import Fraction
import sympy as sp
import mpmath as mp

random.seed(5)

def main():
    print("Prop 6.2 for composite bases")
    for a in range(2, 31):
        for d in range(1, 41):
            N = a ** d - 1
            if N <= 1:
                continue
            assert sp.gcd(a, N) == 1
            assert sp.n_order(a, N) == d, (a, d)
    print("  for every integer 2 <= a <= 30 and d <= 40 (N = a^d - 1 > 1): gcd(a, N) = 1 and ord_N(a) = d exactly")

    print("Lemma 6.4 with real a")
    a = mp.mpf(1.5)
    rho = mp.mpc(0.55, 1.0); rhos = 1 - mp.conj(rho)
    Z = [rho, rhos, a * rho, a * rhos, 1 - mp.conj(a * rho), 1 - mp.conj(a * rhos)]
    in_strip = all(0 < z.real < 1 for z in Z)
    closed = all(any(abs((1 - mp.conj(z)) - w) < 1e-25 for w in Z) for z in Z)
    ret = any(abs(a * rho - w) < 1e-25 for w in Z) and any(abs(a * rhos - w) < 1e-25 for w in Z)
    print("  a = 1.5, rho = 0.55 + i, rho# = 0.45 + i: Z = %s" % [mp.nstr(z, 4) for z in Z])
    print("  Z in the open strip: %s; Z = 1 - conj Z: %s; a*rho and a*rho# both in Z (pair returns together): %s; needs 1 - 1/a < Re rho < 1/a: %s < 0.55 < %s"
          % (in_strip, closed, ret, mp.nstr(1 - 1 / a, 4), mp.nstr(1 / a, 4)))
    assert in_strip and closed and ret
    a1, a2 = 2 * mp.sqrt(2), mp.mpf(2)
    r1 = mp.mpc(0.3, 0.3); r2 = a1 * r1 / a2
    print("  collision a*rho = a'*rho' with a = 2 sqrt2, a' = 2: rho = %s, rho' = %s (both in the strip: %s), rho/rho' = %s (irrational: 1/sqrt2)"
          % (mp.nstr(r1, 4), mp.nstr(r2, 6), 0 < r1.real < 1 and 0 < r2.real < 1, mp.nstr(r1 / r2, 10)))
    for g, g2 in ((14.1, 21.0), (5.0, 5.0)):
        rat = mp.mpc(0.5, g) / mp.mpc(0.5, g2)
        print("  on the line: (1/2 + %gi)/(1/2 + %gi) = %s (real only if g = g')" % (g, g2, mp.nstr(rat, 6)))

    print("Lemma 6.6 with a non-affine V")
    x, y, w = sp.symbols('x y w')
    X = [x, y, w]
    F = sp.Matrix([(1 + x * y) ** 3 * w + y ** 2 * (1 + x * y) * (4 + 3 * x * y),
                   y + 3 * x * (1 + x * y) ** 2 * w + 3 * x * y ** 2 * (4 + 3 * x * y),
                   2 * x - 3 * x ** 2 * y - x ** 3 * w])
    DF = F.jacobian(X)
    detDF = sp.expand(DF.det())
    print("  det DF =", detDF)
    assert detDF == -2
    c = detDF
    adj = DF.adjugate()
    V = lambda u: sp.Matrix([u[0] ** 2 + u[1], u[1] * u[2], u[0] ** 3 - u[2]])
    divV = lambda u: 2 * u[0] + u[2] - 1       # d/du0 (u0^2+u1) + d/du1 (u1 u2) + d/du2 (u0^3 - u2)
    VF = V(list(F))
    U = adj * VF / c
    divU = sum(sp.diff(U[j], X[j]) for j in range(3))
    piola = [sum(sp.diff(adj[j, i], X[j]) for j in range(3)) for i in range(3)]
    for trial in range(6):
        pt = {x: sp.Rational(random.randint(-9, 9), random.randint(1, 5)),
              y: sp.Rational(random.randint(-9, 9), random.randint(1, 5)),
              w: sp.Rational(random.randint(-9, 9), random.randint(1, 5))}
        Fp = [sp.nsimplify(f.subs(pt)) for f in F]
        lhs = divU.subs(pt)
        rhs = divV(Fp)
        pio = [p.subs(pt) for p in piola]
        flow = (DF.subs(pt) * U.subs(pt) - V(Fp))
        print("  point %s: div U = %s, (div V)(F) = %s, equal: %s; Piola %s; DF U - V(F) = 0: %s"
              % (tuple(pt.values()), lhs, rhs, sp.simplify(lhs - rhs) == 0, pio, all(sp.simplify(e) == 0 for e in flow)))
        assert sp.simplify(lhs - rhs) == 0 and all(p == 0 for p in pio) and all(sp.simplify(e) == 0 for e in flow)
    print("ALL F22 CHECKS PASS")

if __name__ == "__main__":
    main()
