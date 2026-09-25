"""Exact weighted-tail domain and raw subsampling; no numerical zero samples."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

out = Path(__file__).resolve().parent
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
fig, ax = plt.subplots(figsize=(12, 7.4), facecolor="white")
fig.subplots_adjust(left=.045, right=.97, top=.91, bottom=.07)
ax.set(xlim=(0, 12), ylim=(0, 8)); ax.axis("off")
fig.text(.045, .953, "The adjoint-domain test in the original source coordinates", fontsize=18, weight="bold")
ax.text(.1, 7.6, r"$\|a\|_\omega^2=\sum_{m\geq1}\frac{|a(m)|^2}{m(m+1)}$", fontsize=19)
ax.text(5.4, 7.6, r"$H_a(m)=m\sum_{r=m}^{\infty}\frac{a(r)}{r(r+1)}$", fontsize=19)
ax.text(.1, 6.25, r"$\Phi a\in\mathrm{dom}\,M^*\quad\Longleftrightarrow\quad H_a(m)=\ell+e_m,\quad e\in\ell^2$", fontsize=20)
ax.text(.1, 5.4, r"$a(m)=\ell+(m+1)e_m-me_{m+1},\qquad (\Phi a)^*(1)=-\ell$", fontsize=19)
ax.text(.1, 4.55, "The raw cover C2 retains ell and selects every second error coefficient:", fontsize=13, weight="bold")

def cells(x, y, labels, colors):
    for j, (label, color) in enumerate(zip(labels, colors)):
        ax.add_patch(Rectangle((x+1.04*j, y), .92, .7, facecolor=color, edgecolor="#475569"))
        ax.text(x+1.04*j+.46, y+.35, label, ha="center", va="center", fontsize=18)

cells(.25, 3.25, [r"$e_1$",r"$e_2$",r"$e_3$",r"$e_4$",r"$e_5$",r"$e_6$"],
      ["#f1f5f9","#d9ede5","#f1f5f9","#d9ede5","#f1f5f9","#d9ede5"])
cells(.25, 1.7, [r"$e_2$",r"$e_4$",r"$e_6$"], ["#d9ede5"]*3)
for src, dst in [(1,0),(3,1),(5,2)]:
    ax.annotate("", xy=(.25+1.04*dst+.46,2.46), xytext=(.25+1.04*src+.46,3.19),
                arrowprops={"arrowstyle":"->", "lw":1.25, "color":"#285841"})
ax.text(7, 3.65, r"$H_{C_2a}(m)=H_a(2m)$", fontsize=18)
ax.text(7, 2.65, r"$\|M^*\Phi C_2a\|^2$", fontsize=17)
ax.text(7, 1.95, r"$=|\ell|^2+\sum_{m\geq1}|e_{2m}|^2$", fontsize=17)
ax.text(.1, .6, "Adjoint-output norm contracts; the separate ambient operator norm remains ||C2|| = sqrt(2).", fontsize=12)
fig.text(.045, .023, "Proof: NAD1-NAD6.  Human source: S. Waleed Noor, arXiv:1809.09577v4, §§1-5.  All maps use the retained weights.", fontsize=9)
fig.savefig(out / "source_adjoint_domain.png", dpi=160)
fig.savefig(out / "source_adjoint_domain.svg")
plt.close(fig)
