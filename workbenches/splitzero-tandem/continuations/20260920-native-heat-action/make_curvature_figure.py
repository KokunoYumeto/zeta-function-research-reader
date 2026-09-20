"""Exact scalar-A boundary example for ID7; this is not arithmetic zero data."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

HERE = Path(__file__).resolve().parent
OUT = HERE / "figures"
OUT.mkdir(exist_ok=True)
s = np.linspace(0, 1.35, 700)
value = 16*s/27 * np.exp(-9*s/4) * (1-9*s/4)
plt.rcParams.update({"font.size": 11, "axes.titlesize": 13})
fig, ax = plt.subplots(figsize=(8.2, 4.7), layout="constrained")
ax.plot(s, value, color="#12617b", lw=2.4,
        label=r"$\Delta_s''(0)=\frac{16s}{27}e^{-9s/4}(1-9s/4)$")
ax.axhline(0, color="#555555", lw=.8)
ax.axvline(4/9, color="#a44626", ls="--", lw=1.4)
ax.scatter([4/9], [0], color="#a44626", s=36, zorder=4)
ax.annotate(r"$s=4/9$: curvature vanishes",
            xy=(4/9, 0), xytext=(.62, .018),
            arrowprops={"arrowstyle": "->", "color": "#a44626"},
            color="#873418")
ax.text(.04, .90, "Positive curvature", transform=ax.transAxes,
        color="#12617b")
ax.text(.67, .22, "Negative curvature", transform=ax.transAxes,
        color="#873418")
ax.set_xlabel("Heat time $s$")
ax.set_ylabel(r"Curvature in the path parameter: $\Delta_s''(0)$")
ax.set_title("The sharp boundary concerns curvature at $t=0$, not all $t$\n"
             r"$G=\mathrm{diag}(2,3),\quad A=\frac{3}{2} I,\quad "
             r"Q_{12}=\frac{2}{3},\quad\epsilon^2=\frac{8}{27}$", pad=13)
ax.grid(alpha=.16)
ax.legend(loc="upper right", frameon=False)
ax.set_xlim(0, 1.35)
for ext in ("png", "svg"):
    fig.savefig(OUT / ("heat_curvature." + ext), dpi=180)
plt.close(fig)
print("Rendered exact boundary example in PNG and SVG.")
