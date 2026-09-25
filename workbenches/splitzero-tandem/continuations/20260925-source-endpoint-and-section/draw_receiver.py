"""Reproducible exact-map illustration for NHR4-NHR7; no sampled zero data."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

out = Path(__file__).resolve().parent
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
fig = plt.figure(figsize=(12, 9), facecolor="white")
ax = fig.add_axes((0.05, 0.39, 0.90, 0.54))
ax.set(xlim=(0, 10), ylim=(0, 5.6))
ax.axis("off")
fig.text(.05, .965, "Original zero jets in a unilateral Hardy receiver", fontsize=19, weight="bold")
fig.text(.05, .934, "Exact maps, arbitrary finite multiplicities; no assertion of an off-line zero", fontsize=11)

points = {"tl": (1.7, 4.2), "tr": (8.1, 4.2), "bl": (1.7, 1.8), "br": (8.1, 1.8)}
for key in ("tl", "bl"):
    x, y = points[key]
    ax.text(x, y, r"$E_+\subset Q'$", ha="center", va="center", fontsize=20, color="#204060")
for key in ("tr", "br"):
    x, y = points[key]
    ax.text(x, y, r"$\mathcal{N}^{\perp}\subset H^2$", ha="center", va="center", fontsize=20, color="#20634a")

def arrow(a, b):
    ax.annotate("", xy=b, xytext=a, arrowprops={"arrowstyle": "->", "lw": 1.6, "color": "#374151"})

arrow((3, 4.2), (6.6, 4.2)); arrow((3, 1.8), (6.6, 1.8))
arrow((1.7, 3.7), (1.7, 2.3)); arrow((8.1, 3.7), (8.1, 2.3))
ax.text(4.8, 4.43, r"$\mathcal{R}$: injective, conjugate-linear", ha="center", fontsize=12)
ax.text(4.8, 2.05, r"$\mathcal{R}$", ha="center", fontsize=16)
ax.text(.3, 3, r"$U_n'=(nT_{1/n})'$", ha="left", fontsize=12)
ax.text(8.4, 3, r"$W_n^*$", ha="left", fontsize=16)
ax.text(5, .93, r"$W_n^*g_{\rho,j}=n^{1-\bar\rho}\sum_{\ell=0}^{j}\binom{j}{\ell}(-\log n)^{j-\ell}g_{\rho,\ell}$", ha="center", fontsize=17)
ax.text(5, .28, "All j = 0, ..., m(rho)-1 survive.  Domain: 1/2 < Re(rho) < 1.", ha="center", fontsize=11)

ax2 = fig.add_axes((.05, .07, .9, .29))
ax2.set(xlim=(0, 12), ylim=(0, 3.8)); ax2.axis("off")
ax2.text(0, 3.45, "Why the cover is not an invertible positive dilation", fontsize=14, weight="bold")

def cells(x, y, vals, color):
    for i, v in enumerate(vals):
        ax2.add_patch(Rectangle((x+.58*i, y), .54, .55, facecolor=color, edgecolor="#536170", lw=.7))
        ax2.text(x+.58*i+.27, y+.275, v, ha="center", va="center", fontsize=13)

cells(.25, 2.2, ["a", "b"], "#e3edf5")
cells(3.2, 2.2, ["a", "a", "b", "b"], "#e5f3ed")
ax2.annotate("", xy=(3, 2.475), xytext=(1.6, 2.475), arrowprops={"arrowstyle": "->", "lw": 1.4})
ax2.text(2.3, 2.8, r"$W_2$", ha="center", fontsize=15)
ax2.text(6.2, 2.7, r"$W_2^*W_2=2I$", fontsize=16)
ax2.text(6.2, 2.0, r"$W_2W_2^*=2P_2\ne2I$", fontsize=16)
cells(.25, 1.05, ["1", "-1", "0", "0"], "#f6e8e1")
ax2.text(3.2, 1.3, r"$W_2^*(1,-1,0,0,\ldots)=0$", fontsize=15)
ax2.text(0, .3, "P2 averages each coefficient pair; the reverse-product defect is retained, not divided away.", fontsize=11)
fig.text(.05, .023, "Source: S. Waleed Noor, arXiv:1809.09577v4, §§1-5.  Calculation: NHR4.1-NHR4.2, NHR6, NHR7.1-NHR7.2.", fontsize=9)
fig.savefig(out / "original_jet_hardy_receiver.png", dpi=160)
fig.savefig(out / "original_jet_hardy_receiver.svg")
plt.close(fig)
