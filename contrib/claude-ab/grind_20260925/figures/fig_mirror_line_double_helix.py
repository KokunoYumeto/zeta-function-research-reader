#!/usr/bin/env python3
"""Figure 17.1 for note 17_: the mirror line Re s = -1/2 as the Hurwitz one-line shift, and the chiral pair of
circles on the Clifford torus.

Left panel (s-plane, exact positions of the first six zeros from mpmath.zetazero):
  critical line Re s = 1/2 with the zeros rho_k; the mirror/shift line Re s = -1/2 with rho_k - 1 = A(rho_k);
  the nodal lines of the 2nd and 3rd Hurwitz jets (Z - 2, Z - 3); the line Re s = 3/2 where the zero velocity
  rho zeta(rho+1)/zeta'(rho) is read; the poles 0 and 1 and the pivot 1/2.
  One HYPOTHETICAL off-line pair (drawn dashed, labelled) shows the crossing rungs of item 3:
  mirror A(rho) = -conj(rho) versus shift rho - 1.  No such zero exists below height 3*10^12 (Platt-Trudgian 2021).
Right panel (stereographic image of the Clifford torus |z1| = |z2| = 1/sqrt2 in S^3):
  Gamma(psi) = (e^{i psi}, -e^{-i psi})/sqrt2, a (1,-1) curve: critical line with the pairing (s, s-1) for
  |psi| < pi/2 (psi = atan 2t), mirror line with the pairing (s, s+1) for pi/2 < psi < 3pi/2;
  D(phi) = (e^{i phi}, e^{i phi})/sqrt2, a (1,1) curve: the critical line with the pairing (s, 1 - conj s)
  as in 6.tex (half of D) and the mirror line with its own reflection s -> -1 - conj s (other half).
  The two curves meet exactly at t = +inf and t = -inf.

claude-ab, model claude-opus-5-5 (Opus 5.5, maximum reasoning effort), 25 September 2026.
"""
import os
import numpy as np
import mpmath as mp
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
gam = [float(mp.im(mp.zetazero(k))) for k in range(1, 7)]

plt.rcParams.update({"font.size": 9.5, "font.family": "DejaVu Sans"})
fig = plt.figure(figsize=(13.2, 6.4))
ax = fig.add_subplot(1, 2, 1)
ymax = 40
# vertical lines
for x, col, lw, ls, lab in [(0.5, "#2b6cb0", 2.0, "-", "critical line Re s = ½ (zeros ρ)"),
                            (-0.5, "#c05621", 2.0, "-", "Re s = −½: A(ρ) = ρ − 1 (first Hurwitz jet vanishes)"),
                            (-1.5, "#c05621", 0.9, ":", "Re s = −3/2, −5/2: nodal lines of the 2nd, 3rd jets"),
                            (-2.5, "#c05621", 0.9, ":", None),
                            (1.5, "#2f855a", 1.2, "--", "Re s = 3/2: zero velocity ρζ(ρ+1)/ζ′(ρ) is read here"),
                            (0.0, "0.55", 0.8, "-", None), (1.0, "0.55", 0.8, "-", None)]:
    ax.plot([x, x], [0, ymax], color=col, lw=lw, ls=ls, label=lab)
for g in gam:
    ax.plot(0.5, g, "o", color="#2b6cb0", ms=6, zorder=5)
    ax.plot(-0.5, g, "o", mfc="white", mec="#c05621", mew=1.6, ms=6, zorder=5)
    ax.annotate("", xy=(-0.47, g), xytext=(0.47, g), arrowprops=dict(arrowstyle="->", color="0.3", lw=1.0))
    for m in (2, 3):
        ax.plot(0.5 - m, g, "o", mfc="white", mec="#dd6b20", mew=0.8, ms=3.5, zorder=4)
ax.text(0.53, gam[0] - 1.6, "ρ₁ = ½ + 14.1347i", fontsize=8, color="#2b6cb0")
ax.text(-1.45, gam[0] - 1.6, "ρ₁ − 1 = A(ρ₁)", fontsize=8, color="#c05621")
# poles and pivot
ax.plot([0, 1], [0, 0], "x", color="k", ms=9, mew=2)
ax.text(0.02, 0.6, "pole 0", fontsize=8); ax.text(1.02, 0.6, "pole 1", fontsize=8)
ax.plot(0.5, 0, "D", color="#6b46c1", ms=5)
ax.text(0.33, -1.7, "pivot ½ (owner's τ: proposal)", fontsize=7.5, color="#6b46c1")
# hypothetical off-line pair at height 18 (clearly labelled)
b, h = 0.72, 17.6
for x in (b, 1 - b):
    ax.plot(x, h, "s", mfc="none", mec="#9b2c2c", ms=6, mew=1.2)
ax.annotate("", xy=(-b, h + 0.35), xytext=(b, h + 0.35), arrowprops=dict(arrowstyle="->", color="#9b2c2c", ls="--", lw=1))
ax.annotate("", xy=(b - 1, h - 0.35), xytext=(b, h - 0.35), arrowprops=dict(arrowstyle="->", color="0.35", lw=1))
ax.plot([-b, b - 1], [h + 0.35, h - 0.35], "s", mfc="none", mec="#9b2c2c", ms=4)
ax.text(-2.95, 3.0, "HYPOTHETICAL off-line zero β + iγ (β = 0.72), for illustration only:\n"
        "mirror A(ρ) = −β + iγ (dashed) and shift ρ − 1 = β − 1 + iγ (solid) differ;\n"
        "A(ρ) is the shift of the partner 1 − ρ̄. None exists below height 3·10¹².",
        fontsize=7, color="#9b2c2c", va="bottom",
        bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="#9b2c2c", lw=0.6))
ax.annotate("", xy=(0.25, h - 0.8), xytext=(-1.2, 7.4), arrowprops=dict(arrowstyle="->", color="#9b2c2c", lw=0.6))
ax.set_xlim(-3.0, 2.0); ax.set_ylim(-3, ymax)
ax.set_xlabel("Re s"); ax.set_ylabel("Im s")
ax.set_title("Mirror through the pole 0 = the Hurwitz one-line shift, exactly on Re s = ½", fontsize=10)
ax.legend(fontsize=7.2, loc="upper left", framealpha=0.95)

# right panel: Clifford torus, stereographic projection from (z1, z2) = (0, i)
ax3 = fig.add_subplot(1, 2, 2, projection="3d")
def stereo(z1, z2):
    x1, y1, x2, y2 = np.real(z1), np.imag(z1), np.real(z2), np.imag(z2)
    d = 1 - y2
    return x1 / d, y1 / d, x2 / d
u, v = np.meshgrid(np.linspace(0, 2 * np.pi, 60), np.linspace(0, 2 * np.pi, 60))
X, Y, Zc = stereo(np.exp(1j * u) / np.sqrt(2), np.exp(1j * v) / np.sqrt(2))
ax3.plot_surface(X, Y, Zc, color="0.85", alpha=0.18, linewidth=0, rasterized=True)
def curve(psi, kind):
    if kind == "Gamma":
        return stereo(np.exp(1j * psi) / np.sqrt(2), -np.exp(-1j * psi) / np.sqrt(2))
    return stereo(np.exp(1j * psi) / np.sqrt(2), np.exp(1j * psi) / np.sqrt(2))
p1 = np.linspace(-np.pi / 2, np.pi / 2, 400)
p2 = np.linspace(np.pi / 2, 3 * np.pi / 2, 400)
ax3.plot(*curve(p1, "Gamma"), color="#2b6cb0", lw=2.6, label="Γ, critical half: (s, s−1), Re s = ½")
ax3.plot(*curve(p2, "Gamma"), color="#c05621", lw=2.6, label="Γ, mirror half: (s, s+1), Re s = −½")
ax3.plot(*curve(p1, "D"), color="#2b6cb0", lw=1.3, ls="--", label="D, (1,1): critical line with (s, 1−s̄), as in 6.tex")
ax3.plot(*curve(p2, "D"), color="#c05621", lw=1.3, ls="--", label="D, other half: Re s = −½ with (s, −1−s̄)")
for psi, lab in [(np.pi / 2, "t = +∞"), (-np.pi / 2, "t = −∞")]:
    P = curve(np.array([psi]), "Gamma")
    ax3.scatter(*P, color="k", s=28, zorder=6)
    ax3.text(P[0][0], P[1][0], P[2][0] + 0.12, lab, fontsize=8)
for g in gam[:3]:
    ph = np.arctan(2 * g)
    ax3.scatter(*curve(np.array([ph]), "Gamma"), color="#2b6cb0", s=12)
    ax3.scatter(*curve(np.array([np.pi - ph]), "Gamma"), color="#c05621", s=12)
ax3.set_title("Clifford torus in S³ (stereographic): Γ is a (1,−1) curve, D a (1,1) curve;\n"
              "they meet only at t = ±∞; first three zeros marked near t = +∞", fontsize=9.5)
ax3.legend(fontsize=7, loc="upper left")
ax3.set_axis_off()
ax3.view_init(elev=28, azim=-60)
fig.text(0.01, 0.005, "claude-ab (Opus 5.5, max effort) · zeros from mpmath.zetazero · figures/fig_mirror_line_double_helix.py",
         fontsize=7, color="0.4")
fig.tight_layout()
for ext in ("png", "svg"):
    fig.savefig(os.path.join(HERE, "fig_mirror_line_double_helix." + ext), dpi=150, bbox_inches="tight")
print("saved")
