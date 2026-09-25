#!/usr/bin/env python3
"""Theorem A_a by direct contour quadrature: sum over zeros of zeta(s,a) of c*H(rho)
vs (1/2 pi i)[int_(c0) - int_(-b)] F_a H ds, F_a(s) = s zeta(s+1,a)/zeta(s,a); a = 1/2 and a = 2."""
import numpy as np
from scipy.special import erfc
from flint import acb, ctx
ctx.prec = 64
SP = 'data/'
Phi = lambda z: 0.5 * erfc(-z / np.sqrt(2))
def h(u, T1, T2, D): return Phi((u - T1) / D) - Phi((u - T2) / D)
def Fa(s, a):
    s_ = acb(s.real, s.imag); A = acb(a)
    v = s_ * (s_ + 1).zeta(A) / s_.zeta(A)
    return complex(float(v.real.mid()), float(v.imag.mid()))
def line(sig, a, T1, T2, D, step=0.05):
    u = np.arange(T1 - 14 * D, T2 + 14 * D, step); s = sig + 1j * u
    H = h(-1j * (s - 0.5), T1, T2, D)
    return np.sum(np.array([Fa(z, a) for z in s]) * H) * step / (2 * np.pi)
# a = 1/2
d = np.load(SP + 'half_sheet.npz')
rho = np.concatenate([0.5 + 1j * d['g'], 1j * d['sk']]); cc = np.concatenate([d['c_nt'], d['c_ax']])
for (T1, T2, D) in [(100.0, 1000.0, 2.0)]:
    lhs = np.sum(cc * h(-1j * (rho - 0.5), T1, T2, D))
    rhs = line(3.0, 0.5, T1, T2, D) - line(-1.75, 0.5, T1, T2, D)
    main = (T2 - T1) / (4 * np.pi * 0.5) + 1j * ((T2**2 - T1**2) / (4 * np.pi * 0.5) - (T2 - T1))
    print(f"a=1/2 [{T1},{T2}] D={D}: zeros {lhs:.6f} | contour {rhs:.6f} | |diff| {abs(lhs-rhs):.2e} | main terms {main:.3f}")
# a = 2, high window with the new data
d = np.load(SP + 'sheet2.npz'); rho, c = d['rho'], d['c']
for (T1, T2, D) in [(5000.0, 7500.0, 2.0)]:
    lhs = np.sum(c * h(-1j * (rho - 0.5), T1, T2, D))
    rhs = line(3.4, 2.0, T1, T2, D) - line(-1.75, 2.0, T1, T2, D)
    main = (T2 - T1) / (4 * np.pi * 2) + 1j * ((T2**2 - T1**2) / (4 * np.pi * 2) - (T2 - T1))
    print(f"a=2 [{T1},{T2}] D={D}: zeros {lhs:.6f} | contour {rhs:.6f} | |diff| {abs(lhs-rhs):.2e} | rel {abs(lhs-rhs)/abs(lhs):.1e} | main {main:.3f}")
