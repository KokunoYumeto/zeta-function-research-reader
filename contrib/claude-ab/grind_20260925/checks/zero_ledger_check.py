#!/usr/bin/env python3
"""Check of the split Mellin identity behind note 13_ (ledger of zeros and ones):

  2 zeta(s) M_S h(s) = int_1^oo Sigma h(u) u^{s-1} du + int_1^oo Sigma hhat(w) w^{-s} dw
                       + hhat(0)/(s-1) - h(0)/s,

for an even Schwartz h WITHOUT moment conditions, Sigma h(u) = 2 sum_{n>=1} h(nu),
hhat(xi) = int h(v) e^{-2 pi i v xi} dv.  Test function h(v) = (1+v^2) e^{-pi v^2},
hhat(xi) = (1 + 1/(2 pi) - xi^2) e^{-pi xi^2},
M_S h(s) = (1/2) pi^{-s/2} Gamma(s/2) + (1/2) pi^{-(s+2)/2} Gamma((s+2)/2).
Also: residues at s = 0 and s = 1, and the trivial-zero cancellation at s = -2.
claude-ab, model claude-opus-5-5 (Opus 5.5, max effort), 25 September 2026.
"""
import mpmath as mp
mp.mp.dps = 30
h = lambda v: (1 + v ** 2) * mp.exp(-mp.pi * v ** 2)
hh = lambda x: (1 + 1 / (2 * mp.pi) - x ** 2) * mp.exp(-mp.pi * x ** 2)
MS = lambda s: mp.pi ** (-s / 2) * mp.gamma(s / 2) / 2 + mp.pi ** (-(s + 2) / 2) * mp.gamma((s + 2) / 2) / 2
def Sig(f, u, N=200):
    return 2 * mp.nsum(lambda n: f(n * u), [1, mp.inf])
def rhs(s):
    a = mp.quad(lambda u: Sig(h, u) * u ** (s - 1), [1, 2, 4, mp.inf])
    b = mp.quad(lambda w: Sig(hh, w) * w ** (-s), [1, 2, 4, mp.inf])
    return a + b + hh(0) / (s - 1) - h(0) / s
for s in [mp.mpf(2), mp.mpc(0.3, 2.0), mp.mpc(-0.7, 1.0), mp.mpc(0.5, 14.0)]:
    L = 2 * mp.zeta(s) * MS(s)
    R = rhs(s)
    print("s = %-14s  2 zeta M_S h = %-40s  split formula = %-40s  |diff| = %s"
          % (mp.nstr(s, 4), mp.nstr(L, 15), mp.nstr(R, 15), mp.nstr(abs(L - R), 3)))
# residues
eps = mp.mpf("1e-12")
r0 = eps * 2 * mp.zeta(eps) * MS(eps)
r1 = eps * 2 * mp.zeta(1 + eps) * MS(1 + eps)
print("residue at s=0: %s  (predicted -h(0) = %s)" % (mp.nstr(r0, 12), mp.nstr(-h(0), 12)))
print("residue at s=1: %s  (predicted hhat(0) = int h = %s)" % (mp.nstr(r1, 12), mp.nstr(hh(0), 12)))
# M_S h has a pole at s=-2 (residue h''(0)/2), cancelled by zeta(-2)=0
rm2 = eps * MS(-2 + eps)
print("residue of M_S h at s=-2: %s ; h''(0)/2 = %s ; 2 zeta(s) M_S h(s) at s=-2+eps: %s (finite)"
      % (mp.nstr(rm2, 12), mp.nstr(mp.diff(h, 0, 2) / 2, 12), mp.nstr(2 * mp.zeta(-2 + eps) * MS(-2 + eps), 12)))
print("1 + 2 zeta(0) =", mp.nstr(1 + 2 * mp.zeta(0), 5))
