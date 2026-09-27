#!/usr/bin/env python3
"""General-a velocity law at a=2: zeros of zeta(s,2)=zeta(s)-1, velocities c = rho zeta(rho+1,2)/zeta'(rho,2).
(1) residue identity by direct contour quadrature; (2) smoothed horizontal/vertical laws T/(4 pi a), T^2/(4 pi a) - T;
(3) Littlewood-type count/tilt (N2) at a=2."""
import numpy as np
from scipy.special import erfc
from flint import acb, ctx
ctx.prec = 64
import os
SP = os.path.join(os.environ.get('ZERO_DATA_DIR', 'data'), '')  # folder with the zero data (not published; zerodata.py regenerates it)
d = np.load(SP + 'onepoints_1100.npz'); rho = d['rho']; zp = d['zp']; z1 = d['z1']
a = 2.0
c = rho * z1 / zp
print(f"1-points found: {len(rho)}, beta range [{rho.real.min():.3f}, {rho.real.max():.3f}], gamma_max {rho.imag.max():.2f}")
Phi = lambda z: 0.5 * erfc(-z / np.sqrt(2))
def h(u, T1, T2, D): return Phi((u - T1) / D) - Phi((u - T2) / D)
def F2(s):
    s_ = acb(s.real, s.imag)
    v = s_ * ((s_ + 1).zeta() - 1) / (s_.zeta() - 1)
    return complex(float(v.real.mid()), float(v.imag.mid()))
def line_integral(sig, T1, T2, D, step=0.02):
    u = np.arange(T1 - 14 * D, T2 + 14 * D, step)
    s = sig + 1j * u
    H = h(-1j * (s - 0.5), T1, T2, D)
    Fv = np.array([F2(z) for z in s])
    return np.sum(Fv * H) * step * 1j / (2j * np.pi)   # (1/2 pi i) int F H ds, ds = i du
for (T1, T2, D) in [(100.0, 1000.0, 2.0), (150.0, 1050.0, 8.0)]:
    Hrho = h(-1j * (rho - 0.5), T1, T2, D)
    lhs = np.sum(c * Hrho)
    R = line_integral(3.4, T1, T2, D); L = line_integral(-1.75, T1, T2, D)
    rhs = R - L
    main = (T2 - T1) / (4 * np.pi * a) + 1j * ((T2**2 - T1**2) / (4 * np.pi * a) - (T2 - T1))
    print(f"[T1,T2]=[{T1},{T2}], D={D}: sum c H(rho) = {lhs:.6f}")
    print(f"      contour (1/2pi i)[int_(3.4) - int_(-1.75)] F H ds = {rhs:.6f}   |diff| = {abs(lhs-rhs):.2e}")
    print(f"      main terms (T2-T1)/(4 pi a) + i[(T2^2-T1^2)/(4 pi a) - (T2-T1)] = {main:.4f};  horizontal ratio {lhs.real/main.real:.4f}")
# (3) N2 at a=2: count and tilt vs (T/2pi)log(T/(2 pi e a)), (T/4pi) log a
for T in [300, 600, 1000]:
    sel = rho.imag <= T
    print(f"T={T}: N={sel.sum()} vs {(T/(2*np.pi))*np.log(T/(2*np.pi*np.e*a)):.2f};  sum(beta-1/2)={np.sum(rho.real[sel]-0.5):.3f} vs (T/4pi)log a={T/(4*np.pi)*np.log(a):.3f}")
