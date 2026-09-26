#!/usr/bin/env python3
"""F15: a non-trivial test of the global residue duality bound with the sharper constant
zeta(2)(1/pi + 8 pi/5) ~ 8.79.  F(s) = exp((s - rho1)^2), G(s) = exp((s - 1 + rho1)^2), so F(s)G(1-s) = 1 at s = rho1
and B_zeta(F,G) ~ 1/zeta'(rho1) (plus exponentially small contributions of the other zeros)."""
import mpmath as mp, numpy as np
mp.mp.dps = 30
r1 = mp.zetazero(1); g1 = r1.imag
F = lambda s: mp.exp((s - r1)**2)
G = lambda s: mp.exp((s - 1 + r1)**2)
def B(F, G):
    pts = [g1 - 10, g1 - 3, g1, g1 + 3, g1 + 10]
    I2 = mp.quad(lambda t: F(mp.mpc(2, t))*G(1 - mp.mpc(2, t))/mp.zeta(mp.mpc(2, t)), pts)
    Im1 = mp.quad(lambda t: F(mp.mpc(-1, t))*G(1 - mp.mpc(-1, t))/mp.zeta(mp.mpc(-1, t)), pts)
    return (I2 - Im1)/(2*mp.pi)
val = B(F, G)
res = mp.fsum(F(r)*G(1 - r)/mp.zeta(r, derivative=1) for r in [mp.zetazero(k) for k in (1, 2, 3)])
b = lambda H: max((1 + abs(t))*abs(H(mp.mpc(sg, t))) for sg in np.linspace(-2, 2, 9) for t in list(np.linspace(float(g1) - 6, float(g1) + 6, 1201)) + list(np.linspace(-float(g1) - 6, -float(g1) + 6, 1201)))
bF, bG = b(F), b(G)
c_sharp = mp.zeta(2)*(1/mp.pi + 8*mp.pi/5); c_crude = mp.zeta(2)*(1 + 4*mp.pi**2)/mp.pi
print("B_zeta(F,G) by the two contours      =", mp.nstr(val, 15))
print("sum of residues F(rho)G(1-rho)/zeta'(rho) (rho_1..rho_3) =", mp.nstr(res, 15))
print("b_{2,1}(F) b_{2,1}(G) =", mp.nstr(bF*bG, 6), "; bound with 8.79:", mp.nstr(c_sharp*bF*bG, 6), "; with 21.19:", mp.nstr(c_crude*bF*bG, 6))
ok = abs(val - res) < 1e-12 and abs(val) <= c_sharp*bF*bG
print("ALL CHECKS PASS" if ok else "SOME CHECK FAILED")
