"""Exact finite heat comparison, with a proved rather than statistical band."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

HERE = Path(__file__).resolve().parent
OUT = HERE/"figures"
OUT.mkdir(exist_ok=True)
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":12})
fig, (ax, maps) = plt.subplots(1,2,figsize=(15,7),gridspec_kw={"width_ratios":[1,1.15]})
s=np.linspace(0,1/21,501)
lead=16*s/3
err=(1+6*s)*np.exp(3*s)-1
exact=2*np.exp(s)-np.exp(-s/3)-np.exp(-3*s)
ax.fill_between(s,lead*(1-err),lead*(1+err),color="#c3dce8",label="proved remainder band")
ax.plot(s,exact,color="#034d60",lw=2.8,label=r"$\Delta_s=2e^s-e^{-s/3}-e^{-3s}$")
ax.plot(s,lead,color="#9f423d",ls="--",lw=2,label=r"retained first term $16s/3$")
ax.set_xlabel(r"heat time $s$  ($0\leq s\leq 1/21$)")
ax.set_ylabel(r"unscaled trace difference $\Delta_s$")
ax.set_title("Exact comparison in the retained metric",pad=18)
ax.legend(loc="upper left",fontsize=10,frameon=False)
ax.grid(alpha=.2)
ax.set_xlim(0,1/21)
ax.set_ylim(0,.40)
ax.text(.5,-.22,
        "Mass 3 on [−1,1]; G = diag(3,1); quotient u²+1.\n"
        "A₁₂=1/3, A₂₁=1, Q₁₂=4/3; all other entries zero.\n"
        "t=1, ε²=16/3, ‖T‖²_G=3. Not arithmetic zero data.",
        ha="center",va="top",transform=ax.transAxes,fontsize=10)
maps.axis("off")
maps.set_xlim(0,1); maps.set_ylim(0,1)
def box(x,y,text,color="#f2f6f8",size=12):
    maps.text(x,y,text,ha="center",va="center",fontsize=size,
              bbox=dict(boxstyle="round,pad=.55",fc=color,ec="#4b6873"),linespacing=1.5)
def arrow(a,b):
    maps.annotate("",xy=b,xytext=a,arrowprops=dict(arrowstyle="->",lw=1.5,color="#4b6873"))
box(.5,.88,"Original quotient (C,G)\nT(t)=A−tQ,  Q²=0")
box(.23,.63,r"$\Phi_s(t)=\mathrm{tr}\,e^{-sT(t)^2}$"+"\n"+r"$f_s(S)=e^{s(S-c)^2}$",size=11)
box(.76,.63,r"$\Psi_s(t)=\mathrm{tr}\,e^{-sT(t)^{\dagger_G}T(t)}$",size=10)
arrow((.41,.79),(.23,.72));arrow((.59,.79),(.76,.72))
box(.5,.40,r"$\Delta_s(t)=\mathrm{Re}\,\Phi_s(t)-\Psi_s(t)$",color="#e7f1ed")
arrow((.23,.53),(.40,.46));arrow((.76,.54),(.60,.46))
box(.5,.19,r"$s\|T(t)\|_G^2\leq 1/7$"+"\n"+
    r"$L(t)^2\leq t^2\epsilon^2\leq 2\Delta_s(t)/s$",color="#e7f1ed")
arrow((.5,.34),(.5,.27))
maps.text(.5,-.03,"L(t) sums positive 2 Re(λ)−k for B(t)=k/2+iT(t),\n"
          "with every algebraic multiplicity retained.\n"
          "The two observations do not reconstruct the operator.",
          ha="center",va="top",fontsize=10)
fig.suptitle("Two finite heat traces recover the original arithmetic allowance",fontsize=18,y=.98)
fig.text(.5,.018,"Proof: NH24–26, NH32–36; HM9–19. Human context: Connes, arXiv:2402.13082v1, equation ft.",
         ha="center",fontsize=10)
fig.subplots_adjust(left=.07,right=.98,top=.87,bottom=.26,wspace=.24)
for extension in ("png","svg"):
    fig.savefig(OUT/("heat_gap."+extension),dpi=170,facecolor="white")
plt.close(fig)
