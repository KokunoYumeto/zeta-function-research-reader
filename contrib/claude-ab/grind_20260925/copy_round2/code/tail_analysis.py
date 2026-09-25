#!/usr/bin/env python3
"""Round 2, target (2): velocity angle of each zero = its Gram offset.
Identity (RH + simplicity in range, Z real, sign Z'(gamma_n) = (-1)^{n+1}):
   arg zeta'(rho_n) = pi*S_n (mod 2pi),  S_n := n - 3/2 - theta(gamma_n)/pi,
   c1(rho_n) = rho_n |zeta(3/2+i gamma_n)|/|zeta'(rho_n)| * exp(i pi (S32_n - S_n)),  S32 := arg zeta(3/2+i gamma)/pi.
"""
import numpy as np, mpmath as mp
from common import load_zeros
g, zp, z1, c = load_zeros(('zeros_A.npz', 'zeros_B.npz', 'zeros_C.npz'))
N = len(g); n = np.arange(1, N + 1)
mp.mp.dps = 30
theta = np.array([float(mp.siegeltheta(mp.mpf(t))) for t in g])
S = n - 1.5 - theta / np.pi
S32 = np.angle(z1) / np.pi
rho = 0.5 + 1j * g
wrap = lambda x: (x + np.pi) % (2 * np.pi) - np.pi
d1 = wrap(np.angle(zp) - np.pi * S)
d2 = wrap(np.angle(c) - (np.angle(rho) + np.pi * (S32 - S)))
print(f"[identity] max |arg zeta'(rho_n) - pi S_n| (mod 2pi) over {N} zeros = {np.abs(d1).max():.2e}")
print(f"[identity] max |arg c1 - (arg rho + pi(S32 - S))| (mod 2pi)      = {np.abs(d2).max():.2e}")
print(f"[identity] max |Z'(gamma_n) - (-1)^(n+1)|zeta'||: {np.max(np.abs(1j*np.exp(1j*theta)*zp - ((-1.0)**(n+1))*np.abs(zp))):.2e}")
print(f"S_n range [{S.min():.3f}, {S.max():.3f}], std {S.std():.3f};  S32 range [{S32.min():.3f},{S32.max():.3f}]")
phi = np.arctan(1 / (2 * g))
sgn_pred = np.sign(np.sin(np.pi * (S - S32) + phi))
print(f"[sign rule] sign Re c1 == sign sin(pi(S-S32)+phi) for {np.mean(sgn_pred == np.sign(c.real))*100:.4f}% of zeros")
# ---- close pairs ----
mean_sp = 2 * np.pi / np.log(g / (2 * np.pi))
gap = np.diff(g); ng = gap / mean_sp[:-1]
tm = (g[:-1] + g[1:]) / 2
Sgap = np.arange(1, N) - np.array([float(mp.siegeltheta(mp.mpf(t))) for t in tm]) / np.pi - 1.0  # S(t_m) = N(t_m) - theta(t_m)/pi - 1 with N(t_m) = n (corrected in round 2)
for thr in [0.10, 0.05, 0.03]:
    idx = np.nonzero(ng < thr)[0]
    Sg = Sgap[idx]; fr = lambda lo, hi: np.mean(((Sg - lo) % 2) < (hi - lo))
    near0 = np.mean(np.abs(((Sg + 1) % 2) - 1) < 0.5)
    rec = c[idx].real / g[idx]
    print(f"\nclose pairs with normalized gap < {thr}: {len(idx)}")
    print(f"   S on the gap: mod-2 distance to 0 < 1/2 for {near0*100:.1f}% ; distance to 1 < 1/2 for {(1-near0)*100:.1f}%")
    print(f"   first member Re c1 < 0 for {np.mean(rec < 0)*100:.1f}% ; mean Re c1/gamma {rec.mean():+.3f}; min {rec.min():+.3f}; max {rec.max():+.3f}")
    straddle = np.mean(np.abs(Sgap[idx]) < 0.5)
    print(f"   pair straddles a Gram point with correct count (|S_gap|<1/2): {straddle*100:.1f}%")
    # predicted sign of the first member's horizontal velocity from S_gap: Re c1(rho_n) < 0 iff (S_gap - S32) mod 2 in (-1/2,1/2)
    pred_neg = np.abs(((Sgap[idx] - S32[idx] + 1) % 2) - 1) < 0.5
    print(f"   rule 'Re c1(first) < 0  iff  S_gap - S32 = 0 mod 2 (within 1/2)' correct for {np.mean(pred_neg == (rec < 0))*100:.2f}%")
# ---- the round-1 extremes ----
print("\nround-1 extreme negative excursions (first member n):")
for nn in [18859, 49527, 64901, 4765, 25095]:
    k = nn - 1
    print(f"  n={nn}: gamma={g[k]:.3f} norm.gap={ng[k]:.3f} S_n={S[k]:+.3f} S_gap={Sgap[k]:+.3f} S32={S32[k]:+.3f} arg(c1)/pi={np.angle(c[k])/np.pi:+.3f} Re c1/gamma={c[k].real/g[k]:+.3f}")
# ---- height dependence ----
print("\nheight dependence (close pairs, normalized gap < 0.10):")
idx = np.nonzero(ng < 0.10)[0]
for lo, hi in [(0, 10000), (10000, 30000), (30000, 50000), (50000, 75000)]:
    sel = idx[(g[idx] >= lo) & (g[idx] < hi)]
    Sg = Sgap[sel]
    print(f"  gamma in [{lo},{hi}): pairs {len(sel)}, std(S on gap) {Sg.std():.3f}, frac |S_gap mod 2 - 1|<1/2 (positive-spike type) {np.mean(np.abs((Sg % 2) - 1) < 0.5)*100:.1f}%, frac Re c1(first)>0 {np.mean(c[sel].real > 0)*100:.1f}%")
    selall = (g >= lo) & (g < hi)
    print(f"      all zeros in range: std(S_n) {S[selall].std():.3f}")
np.savez('tail_data.npz', S=S, S32=S32, theta=theta, Sgap=Sgap, ng=ng)
