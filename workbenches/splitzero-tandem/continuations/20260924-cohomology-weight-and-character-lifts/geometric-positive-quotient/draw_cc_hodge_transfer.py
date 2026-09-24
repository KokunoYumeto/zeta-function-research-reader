from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

root = Path(__file__).parent
fig = plt.figure(figsize=(13.6, 9.4), facecolor="white")
ax = fig.add_axes([0.035, 0.025, 0.93, 0.94])
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis("off")

def box(x, y, text, color="#163956", size=15, width=None):
    ax.text(x, y, text, ha="center", va="center", fontsize=size,
            color=color, linespacing=1.65,
            bbox=dict(boxstyle="round,pad=.6", fc="#f7fafc", ec=color, lw=1.5))

def arrow(x1, y1, x2, y2, color="#163956"):
    ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle="-|>",
                                mutation_scale=18,lw=1.7,color=color))

ax.text(.5,.97,"One power expression, retained domains and three exact degrees",
        ha="center",va="top",fontsize=20,weight="bold")
ax.text(.5,.912,r"Every prime $p$; $L=\log p$; every integer $n\geq 1$.",
        ha="center",fontsize=14)
ax.text(.5,.874,r"Odd signed CC cases: multiply pullbacks by $\varepsilon_n$; retain translation by [−1] when $n\equiv3$ (mod 4).",
        ha="center",fontsize=11)

box(.13,.76,r"$E_p$"+"\n"+r"periods $L,\ 2\pi$",size=16)
box(.79,.76,r"$E_{p^n}$"+"\n"+r"periods $nL,\ 2\pi$",size=16)
arrow(.25,.765,.655,.765)
ax.text(.45,.799,r"$h_{p,n}([z])=[z^n]$",ha="center",fontsize=15)
ax.text(.45,.715,r"degree $n$;  $h^*=\mathrm{diag}(1,n)$",ha="center",fontsize=14)
ax.text(.45,.661,r"$\|h^*v\|_L^2=n\|v\|_{nL}^2$",ha="center",fontsize=16,color="#087d58")

box(.13,.475,r"$E_p$"+"\n"+r"periods $L,\ 2\pi$",size=16)
arrow(.715,.678,.259,.493,color="#9d4f12")
ax.text(.685,.55,r"$d([x'+i\theta'])=[x'/n+i\theta']$",ha="center",fontsize=12,color="#9d4f12",
        bbox=dict(fc="white",ec="none",pad=3))
ax.text(.50,.485,r"$C=d\circ h:\ (x,\theta)\mapsto(x,n\theta)$",ha="center",fontsize=13,color="#9d4f12")
ax.text(.50,.427,r"$C^*=\mathrm{diag}(1,n)$ on the SAME Hodge space",ha="center",fontsize=12,color="#9d4f12")
arrow(.13,.658,.13,.556,color="#9d4f12")
ax.text(.075,.605,r"$C$",ha="left",fontsize=14,color="#9d4f12")
ax.text(.5,.355,r"$G_L=\mathrm{diag}(2\pi/L,\ L/(2\pi))$",ha="center",fontsize=17)
ax.text(.5,.298,r"Exact return defect:  $(C^*)^\dagger C^*-nI=\mathrm{diag}(1-n,\ n^2-n)$",
        ha="center",fontsize=16,color="#9d4f12")
ax.text(.5,.25,r"For every $n>1$: one negative direction, one positive direction.",
        ha="center",fontsize=13)
ax.axhline(.204,xmin=.025,xmax=.975,color="#b1bec9",lw=1)
ax.text(.5,.158,r"Separate maps: on $\mathbb{P}^1$, degree $n$, $H^1=0$; on $E_p\to E_p$, degree $n^2$, $(F_n^*)^\dagger F_n^*=n^2I$.",
        ha="center",fontsize=13)
ax.text(.5,.107,"The square-root identity transfers across periods. Returning the period retains the full metric defect.",
        ha="center",fontsize=12)
ax.text(.5,.059,"Proofs CW2–CW5, CC_CANONICAL_WEIGHT_TRANSFER.md. Source: Connes–Consani, arXiv:2606.06604v1 and 2609.00299v1.",
        ha="center",fontsize=9)
ax.text(.5,.028,"Schematic of proved maps for all p,n; no sampled zeros, numerical interval search, or asserted RH purity.",
        ha="center",fontsize=10,color="#455764")
fig.savefig(root/"cc_hodge_transfer.png",dpi=180)
fig.savefig(root/"cc_hodge_transfer.svg")
plt.close(fig)
