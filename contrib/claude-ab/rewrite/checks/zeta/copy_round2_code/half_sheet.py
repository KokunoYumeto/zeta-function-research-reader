#!/usr/bin/env python3
"""a = 1/2 sheet: zeros of zeta(s,1/2) = (2^s-1) zeta(s): nontrivial rho (100k, RH-verified range) and
s_k = 2 pi i k / log 2 (Re s = 0). Velocities c = s zeta(s+1,1/2)/zeta'(s,1/2) computed directly with Arb Hurwitz."""
import numpy as np, time
from flint import acb, arb, ctx, acb_series
from common import load_zeros, sieve_coeffs
ctx.prec = 80
g, zp, z1, c1 = load_zeros(('zeros_A.npz', 'zeros_B.npz', 'zeros_C.npz'))
rho = 0.5 + 1j * g
half = acb(0.5)
def cv(z): return complex(float(z.real.mid()), float(z.imag.mid()))
def vel(s):
    s_ = acb(s.real, s.imag)
    num = s_ * (s_ + 1).zeta(half)
    den = acb_series([s_, 1]).zeta(half)[1]
    return cv(num / den)
# (1) nontrivial zeros: closed form c1*(2^{rho+1}-1)/(2^rho-1), cross-checked directly on a sample
c_nt = c1 * (2.0**(rho + 1) - 1) / (2.0**rho - 1)
samp = [0, 1, 999, 49999, 99999]
print("direct Arb vs closed form (nontrivial):", max(abs(vel(rho[k]) - c_nt[k]) / abs(c_nt[k]) for k in samp))
# (2) imaginary-axis zeros
K = int(g[-1] * np.log(2) / (2 * np.pi))
t0 = time.time()
sk = 2j * np.pi * np.arange(1, K + 1) / np.log(2)
c_ax = np.array([vel(s) for s in sk])
print(f"imaginary-axis zeros: {K} (up to height {sk[-1].imag:.1f}), {time.time()-t0:.0f}s; |c|/sqrt(t) range {np.min(np.abs(c_ax)/np.sqrt(sk.imag)):.3f}..{np.max(np.abs(c_ax)/np.sqrt(sk.imag)):.3f}")
# closed-form check for the axis zeros: c(s_k) = s_k zeta(1+s_k)/(log2 zeta(s_k))
k0 = 7; s = acb(0, sk[k0].imag)
cf = cv(s * (s + 1).zeta() / (arb(2).log() * s.zeta()))
print("axis closed form check:", abs(cf - c_ax[k0]) / abs(cf))
np.savez('half_sheet.npz', g=g, c_nt=c_nt, sk=sk.imag, c_ax=c_ax)
# (3) sharp error and Bohr coefficients
a = 0.5
gam_all = np.concatenate([g, sk.imag]); c_all = np.concatenate([c_nt, c_ax])
o = np.argsort(gam_all); gam_all = gam_all[o]; c_all = c_all[o]
Scum = np.concatenate([[0], np.cumsum(c_all)])
Ma = lambda T: (T / (4 * np.pi) + 1j * T**2 / (4 * np.pi)) / a - 1j * T
Tmax = min(g[-1], sk[-1].imag) - 60
T = np.arange(2000.0, Tmax, 0.004)
E = Scum[np.searchsorted(gam_all, T, 'right')] - Ma(T)
ET = E / T
b, e = sieve_coeffs(64)
print(f"\nsharp E_1/2(T)/T on [2000,{Tmax:.0f}]: rms Re {np.sqrt(np.mean(ET.real**2)):.4f}, rms Im {np.sqrt(np.mean(ET.imag**2)):.4f}, mean {np.mean(ET):.2e}")
print("Bohr coefficients at log m: observed vs predicted -beta(m) m^{-1/2}/(2 pi a log m) [beta = b on odd m, 0 on even m]")
for m in range(2, 17):
    obs = np.mean(ET * np.exp(1j * T * np.log(m)))
    pred = 0.0 if m % 2 == 0 else -b[m] / (2 * np.pi * a * np.sqrt(m) * np.log(m))
    print(f"  m={m:2d}: obs {obs.real:+.6f}{obs.imag:+.6f}i   pred {pred:+.6f}")
# a=1 comparison amplitude at log 3 (should be half of the a=1/2 one)
for xi in [0.5, 0.9]:
    obs = np.mean(ET * np.exp(1j * T * xi)); print(f"  control xi={xi}: {obs.real:+.6f}{obs.imag:+.6f}i")
