"""Exact comparison diagram and retained cohomology of a contractible complex."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
OUT=Path(__file__).resolve().parent/"figures"
plt.rcParams.update({"font.family":"DejaVu Sans","svg.fonttype":"none"})
fig,ax=plt.subplots(figsize=(15,11))
fig.patch.set_facecolor("#fcfcfa")
ax.set(xlim=(0,15),ylim=(0,11));ax.axis("off")
fig.subplots_adjust(left=.025,right=.985,bottom=.025,top=.975)
ax.text(.25,10.75,"Which cohomology classes transfer?",fontsize=23,weight="bold",va="top",color="#183047")
ax.text(.25,10.05,"Every map below has its specified domain. Supported zero is retained before applying the additive quotient.",fontsize=12,color="#183047")
def box(y,h,title,rows,color):
    ax.add_patch(FancyBboxPatch((.4,y),14.0,h,boxstyle="round,pad=.1",fc="white",ec=color,lw=2))
    ax.text(.65,y+h-.27,title,fontsize=18,color=color,va="top")
    for i,row in enumerate(rows):
        ax.text(.65,y+h-.95-.53*i,row,fontsize=15,color="#183047",va="top")
box(7.0,2.4,"From the supported complex to a genuine free complex",[
    r"$L(V)=\mathbb{Z}[V],\quad E[v]=[0],\quad U(V)=(1-E)L(V),\quad r_v=[v]-[0]$",
    r"$L(d^{i+1})L(d^i)[v]=[0_{C^{i+2}}];\qquad D^i(r_v)=r_{d^iv},\qquad D^{i+1}D^i=0$",
    r"$\tau$ is killed in $L(V)$, but the supported symbol $[0]$ is a nonzero basis vector."
],"#245eaa")
box(3.5,2.9,"Exact comparison in every degree",[
    r"$0\ \longrightarrow\ K(C)\ \longrightarrow\ U(C)\ \longrightarrow\ C\ \longrightarrow\ 0$",
    r"$r_v\mapsto v;\qquad K(V)=\langle r_{v+w}-r_v-r_w\rangle_{\mathbb{Z}}$",
    r"$0\ \longrightarrow\ H^iK(C)\ \longrightarrow\ H^iU(C)\ \longrightarrow\ H^iC\ \longrightarrow\ 0$",
    r"Every cycle $z$ lifts to the cycle $r_z$. The short exact sequence need not split."
],"#157564")
box(.65,2.45,"A contractible input retains a nonzero cross-effect",[
    r"$C:\quad\mathbb{Z}\ \longrightarrow\ \mathbb{Z}^2\ \longrightarrow\ \mathbb{Z},\quad x\mapsto(x,0),\quad(x,y)\mapsto y$",
    r"$H^1(C)=0,\qquad H^1U(C)=\bigoplus_{x\ne0,\ y\ne0}\mathbb{Z}\,\{r_{(x,y)}-r_{(0,y)}\}$",
    r"These classes form the retained cross-effect; its additive quotient recovers the original complex."
],"#ad3545")
ax.text(.5,.15,"Proof: Chain comparison, complete kernel and cohomology calculations. Programme source: support_diagrams.tex, D1–D8.",fontsize=11,color="#183047")
for ext in ("png","svg"):
    fig.savefig(OUT/f"10_chain_comparison.{ext}",dpi=150,bbox_inches="tight",facecolor=fig.get_facecolor())
plt.close(fig)
