"""Exact illustration of sections 4–5. No model for a metric on tau."""

from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

HERE = Path(__file__).resolve().parent
plt.rcParams.update({"font.size": 12, "mathtext.fontset": "dejavusans"})
fig = plt.figure(figsize=(13.5, 6.5), facecolor="#fcfbf8")
grid = fig.add_gridspec(1, 2, width_ratios=[1.25, 1], wspace=.24)
left = fig.add_subplot(grid[0]); right = fig.add_subplot(grid[1])
left.set_xlim(-.2, 5.8); left.set_ylim(-2.2, 2.7); left.axis("off")
left.set_title("Retain both directions of dilation history", loc="left", pad=18)
left.text(2.8, 2.2, r"$S_j=F_n^j(K\setminus F_nK),\quad j\in\mathbb{Z}$", ha="center")
for pos, j in enumerate(range(-2, 3)):
    left.add_patch(Rectangle((pos+.25, .85), .82, .8, facecolor="#e2eef2", edgecolor="#28677b", lw=1.5))
    left.text(pos+.66, 1.25, f"$S_{{{j}}}$", ha="center", va="center")
    if pos < 4:
        left.annotate("", (pos+1.29, 1.24), (pos+1.05, 1.24), arrowprops={"arrowstyle": "->", "color": "#28677b"})
left.text(.0, 1.25, "…", va="center"); left.text(5.25, 1.25, "…", va="center")
left.text(2.8, .5, r"$F_n:S_j\longrightarrow S_{j+1}$", ha="center")
left.text(2.8, .03, r"$\mu(S_j)=M(1-1/n)n^{-j},\quad M>0$", ha="center")
left.text(2.8, -.57, r"$D_n f=f\circ F_n$", ha="center", fontsize=17)
left.text(2.8, -1.1, r"$D_n^*D_n=D_nD_n^*=nI$", ha="center", fontsize=17)
left.text(2.8, -1.72, "No prefactor is inserted into the operator.\nThe original Haar mass M remains arbitrary.", ha="center", fontsize=11)

n = 3
angles = np.linspace(0, 2*np.pi, 1000)
right.plot(np.sqrt(n)*np.cos(angles), np.sqrt(n)*np.sin(angles), color="#126078", lw=3)
right.axhline(0, color="#b8b6af", lw=.8); right.axvline(0, color="#b8b6af", lw=.8)
right.scatter([0, 1], [0, 0], color="#b15a28", zorder=4, s=48)
right.annotate("0", (0, 0), (5, -17), textcoords="offset points", color="#9b4820")
right.annotate("1", (1, 0), (5, -17), textcoords="offset points", color="#9b4820")
right.set_aspect("equal"); right.set_xlim(-2.2, 2.2); right.set_ylim(-2.2, 2.2)
right.set_xticks([-np.sqrt(n), 0, np.sqrt(n)], [r"$-\sqrt{3}$", "0", r"$\sqrt{3}$"])
right.set_yticks([-np.sqrt(n), 0, np.sqrt(n)], [r"$-\sqrt{3}$", "0", r"$\sqrt{3}$"])
right.set_xlabel(r"$\operatorname{Re}\lambda$"); right.set_ylabel(r"$\operatorname{Im}\lambda$")
right.set_title(r"$\sigma(D_3)=\{\lambda:|\lambda|=\sqrt{3}\}$", pad=18)
right.text(.5, -.2, "Blue: full continuous spectrum; no L² eigenvectors.\nOrange: 0 and 1 are eigenvalues of the compression U₃.", transform=right.transAxes, ha="center", fontsize=10)
fig.suptitle("Covering index gives a common spectral radius", fontsize=20, y=.97)
fig.subplots_adjust(top=.80, bottom=.19, left=.035, right=.97)
fig.text(.035, .045, "Proof: accompanying note, §§4–6. Source setting: Connes–Consani (2609.00299); adelic dilation: Connes–Marcolli–Ramachandran (math/0501424).", fontsize=9)
fig.savefig(HERE / "clock_radius.png", dpi=160, facecolor=fig.get_facecolor())
fig.savefig(HERE / "clock_radius.svg", facecolor=fig.get_facecolor())
