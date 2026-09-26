#!/usr/bin/env python3
"""a = 2 (non-Eulerian) velocity spectrum from the certified zeros of zeta(s)-1 up to height 8000."""
import numpy as np
from fractions import Fraction as Fr
from scipy.special import erfc
from beta_coeffs import coeffs
import os
SP = os.path.join(os.environ.get('ZERO_DATA_DIR', 'data'), '')  # folder with the zero data (not published; zerodata.py regenerates it)
R, ZP, Z1 = [], [], []
for f in ['onepoints_1100.npz', 'onepoints_1100_4600.npz', 'onepoints_4600_8000.npz']:
    d = np.load(SP + f); R.append(d['rho']); ZP.append(d['zp']); Z1.append(d['z1'])
rho = np.concatenate(R); zp = np.concatenate(ZP); z1 = np.concatenate(Z1)
o = np.argsort(rho.imag); rho, zp, z1 = rho[o], zp[o], z1[o]
g = rho.imag; beta_re = rho.real
a = 2.0
c = rho * z1 / zp                                     # velocity d rho / da at a = 2
print(f"zeros of zeta(s,2): {len(rho)}, gamma_max {g[-1]:.2f}, beta in [{beta_re.min():.3f},{beta_re.max():.3f}]")
print(f"  fraction with beta > 1: {np.mean(beta_re>1)*100:.2f}%  (count up to T is ~ c T, vs N(T) ~ (T/2pi) log T)")
Ma = lambda T: (T / (4 * np.pi) + 1j * T**2 / (4 * np.pi)) / a - 1j * T
Ms, beta, gens = coeffs(2, Fr(8))
freqs = [(float(np.log(float(r))), r, float(beta[r])) for r in Ms[1:] if r <= 6]
# sharp error
Scum = np.concatenate([[0], np.cumsum(c)])
T = np.arange(1500.0, g[-1] - 60, 0.004)
Esh = Scum[np.searchsorted(g, T, 'right')] - Ma(T)
# H-weighted (analytic) smoothed error: window [T1, T] with Gaussian D; weights H(rho) = Phi((T - gamma + i(beta-1/2))/D) - Phi((T1 - ...)/D)
Phi = lambda z: 0.5 * erfc(-z / np.sqrt(2))
D = 1.0; T1 = 1000.0
gt = g - 1j * (beta_re - 0.5)                         # H(rho) = h(gamma - i(beta - 1/2))
low = np.sum(c * Phi((gt - T1) / D))                  # lower-edge constant  sum c Phi((gamma~ - T1)/D)
# sum_rho c [Phi((gt - T1)/D) - Phi((gt - T)/D)] = low - sum c Phi((gt - T)/D); split sum c Phi((gt-T)/D) = (zeros far above T: c) + local
Tg = T[::25]                                          # step 0.1 for the smoothed series
ctail = np.concatenate([np.cumsum(c[::-1])[::-1], [0]])   # ctail[k] = sum_{j>=k} c_j
W = np.empty(len(Tg), dtype=complex)
for i, t in enumerate(Tg):
    lo = np.searchsorted(g, t - 12 * D); hi = np.searchsorted(g, t + 12 * D)
    loc = np.sum(c[lo:hi] * Phi((gt[lo:hi] - t) / D))
    W[i] = low - (loc + ctail[hi]) - (Ma(t) - Ma(T1))
# Bohr coefficients
print("\nfrequency log r | beta(r) exact | pred sharp -beta r^-1/2/(2 pi a log r) | obs sharp E/T | pred H-smoothed (x e^{-D^2 l^2/2}) | obs H-smoothed W/T")
ETs = Esh / T; WT = W / Tg
for lam, r, bt in freqs:
    pred = -bt * np.exp(-lam / 2) / (2 * np.pi * a * lam)
    o_sh = np.mean(ETs * np.exp(1j * T * lam))
    o_sm = np.mean(WT * np.exp(1j * Tg * lam))
    print(f"  r={str(r):>6} lam={lam:.4f} beta={bt:+.4f} | pred {pred:+.5f} | sharp {o_sh.real:+.5f}{o_sh.imag:+.5f}i | predH {pred*np.exp(-D**2*lam**2/2):+.5f} | H {o_sm.real:+.5f}{o_sm.imag:+.5f}i")
for xi in [0.3, 0.55, 1.0]:
    print(f"  control xi={xi}: sharp {np.mean(ETs*np.exp(1j*T*xi)):.5f}  H {np.mean(WT*np.exp(1j*Tg*xi)):.5f}")
print(f"\nrms sharp E/T {np.sqrt(np.mean(np.abs(ETs)**2)):.4f}; rms H-smoothed W/T {np.sqrt(np.mean(np.abs(WT)**2)):.4f}; mean sharp {np.mean(ETs):.4f}")
np.savez(SP + 'sheet2.npz', rho=rho, c=c)
