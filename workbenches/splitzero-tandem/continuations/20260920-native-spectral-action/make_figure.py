"""Reproduce the exact finite comparison in SA38--SA43, without zeta sampling."""
from pathlib import Path
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

HERE = Path(__file__).resolve().parent
OUT = HERE / "figures"
OUT.mkdir(exist_ok=True)
t = np.unique(np.r_[np.linspace(0, 1, 801), .25, .5])
J = 2/3 - 8*t/3
H = J + 16*t*t/3
L = 2*np.sqrt(np.maximum(0, (4*t-1)/3))
allowance = 4*t/np.sqrt(3)
plt.rcParams.update({"font.size": 12, "svg.fonttype": "none"})
fig, (left, right) = plt.subplots(1, 2, figsize=(13.8, 7.0))
fig.subplots_adjust(left=.075, right=.975, bottom=.24, top=.74, wspace=.24)
fig.suptitle("The metric retains what the quadratic eigenvalue trace loses", fontsize=18, y=.97)
fig.text(.5, .91, "Exact finite algebra example — not an arithmetic zero packet",
         ha="center", fontsize=13, color="#8a3c19")
fig.text(.5, .85,
         r"$G=\mathrm{diag}(3,1),\quad A_{12}=1/3,\ A_{21}=1,\quad Q_{12}=4/3$"
         "\nAll other entries of A and Q are zero. "
         r"$T(t)=A-tQ,\quad Q^2=0,\quad \epsilon^2=16/3.$",
         ha="center", fontsize=12)
left.plot(t, H, color="#126782", lw=2.6, label=r"$H(t)=\mathrm{tr}(T^{\dagger_G}T)$")
left.plot(t, J, color="#a44a3f", lw=2.6, label=r"$J(t)=\mathrm{tr}(T^2)$")
left.fill_between(t, J, H, color="#94c9d7", alpha=.28)
left.annotate(r"$H-J=16t^2/3$", xy=(.7, .15), xytext=(.29, 1.75),
              arrowprops={"arrowstyle":"->", "color":"#333"}, fontsize=12)
left.set_title("Same operator, same original metric")
left.set_ylabel("Exact trace")
left.set_ylim(-2.3, 3.8)
left.legend(loc="lower left", fontsize=11)
right.plot(t, allowance, color="#6b4c9a", lw=2.7, label=r"$t\epsilon=4t/\sqrt{3}$")
right.plot(t, L, color="#26734d", lw=2.4, label=r"$L(t)=2\sqrt{\max(0,(4t-1)/3)}$")
right.axvline(.25, color="#777", ls=":", lw=1.4)
right.plot([.25], [0], "o", color="#26734d")
right.plot([.5], [2/np.sqrt(3)], "o", color="#111")
right.annotate("Double root at t = 1/4", xy=(.25, 0), xytext=(.36, .31),
               arrowprops={"arrowstyle":"->"}, fontsize=11)
right.annotate("Equality at t = 1/2", xy=(.5, 2/np.sqrt(3)), xytext=(.06, 1.8),
               arrowprops={"arrowstyle":"->"}, fontsize=11)
right.set_title(r"Full spectrum in $S=c+iu$; $L(t)\leq t\epsilon$")
right.set_ylabel("Aggregate displacement to the right of Re S = c")
right.set_ylim(-.08, 2.55)
right.legend(loc="upper left", bbox_to_anchor=(0, -.19), fontsize=10)
for ax in (left, right):
    ax.set_xlabel(r"Original perturbation parameter $t$")
    ax.set_xlim(0, 1)
    ax.set_xticks([0, .25, .5, .75, 1])
    ax.grid(alpha=.2)
fig.text(.065, .075,
         r"$p_t(z)=z^2-1/3+4t/3$ retains both roots and their multiplicities."
         "\nSA27–31, SA38–39, SA42–43. Curves evaluate the displayed exact formulas.",
         fontsize=11)
fig.text(.065, .015,
         "Source context: Connes–van Suijlekom, arXiv:2511.23257v1, § sect:sa. "
         "Full finite proofs accompany this figure.", fontsize=10)
fig.savefig(OUT/"metric_trace.png", dpi=155)
fig.savefig(OUT/"metric_trace.svg")
plt.close(fig)
(OUT/"FORMULAS.json").write_text(json.dumps({
    "example_status":"Exact mass-three uniform comparison measure on [-1,1]; not arithmetic zeros",
    "G":[[3,0],[0,1]],"A":[[0,"1/3"],[1,0]],"Q":[[0,"4/3"],[0,0]],
    "H":"2/3-8*t/3+16*t^2/3","J":"2/3-8*t/3",
    "L":"0 for 0<=t<=1/4; 2*sqrt((4*t-1)/3) for 1/4<t<=1",
    "allowance":"4*t/sqrt(3)", "full_characteristic":"z^2-1/3+4*t/3",
    "original_coordinate":"S=c+i*u", "epsilon_squared":"16/3",
    "proof":"NATIVE_SPECTRAL_ACTION.tex: SA27–31, SA38–39, SA42–43"
}, indent=2)+"\n",encoding="utf-8")
print("Rendered exact two-panel comparison.")
