"""Reproduce exact diagrams for FOUR_CORNERS_OVER_Z.md; no sampled bound is claimed."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle

OUT = Path(__file__).resolve().parent / "figures"
OUT.mkdir(exist_ok=True)
INK = "#15283e"
BLUE = "#245eaa"
TEAL = "#11776e"
PURPLE = "#7444a5"
RED = "#b84143"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12,
                     "svg.fonttype": "none"})

def page(title, subtitle, height=10):
    fig, ax = plt.subplots(figsize=(14, height))
    fig.patch.set_facecolor("#fcfcfa")
    ax.set(xlim=(0, 14), ylim=(0, height))
    ax.axis("off")
    fig.subplots_adjust(left=.025, right=.985, bottom=.025, top=.975)
    ax.text(.2, height-.25, title, fontsize=22, weight="bold", color=INK, va="top")
    ax.text(.2, height-.95, subtitle, fontsize=12, color=INK, va="top")
    return fig, ax

def card(ax, x, y, w, h, title, rows, color=BLUE):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.08,rounding_size=0.1",
                               edgecolor=color,facecolor="white",linewidth=2))
    ax.text(x+.2,y+h-.25,title,fontsize=18,color=color,weight="bold",va="top")
    for i, row in enumerate(rows):
        ax.text(x+.2,y+h-.9-.43*i,row,fontsize=13,color=INK,va="top")

def save(fig, name):
    for ext in ("png","svg"):
        fig.savefig(OUT/(name+"."+ext),dpi=160,bbox_inches="tight",facecolor=fig.get_facecolor())
    plt.close(fig)

fig, ax = page("The original four roles, calculated over the integers",
    r"Each corner specifies both operations. Integer zero $e=0_{\mathbb{Z}}$ remains distinct from the programme's $\tau$.",11)
card(ax,.3,5.1,6.45,3.9,r"$\varepsilon$: identity for both",[
    r"$\varepsilon+x=x,\qquad \varepsilon x=x$",
    r"From $\mathbb{Z}$: $J=\{\varepsilon<a\}$.",
    r"Addition = maximum; multiplication = maximum.",
    r"Every integer maps to $a$.",
    r"From $G(\mathbb{Z})$: even $\tau$ maps to $a$."
],PURPLE)
card(ax,7.1,5.1,6.35,3.9,r"$\tau$: additive identity, product absorber",[
    r"$\tau+x=x,\qquad \tau x=\tau$",
    r"From $\mathbb{Z}$: $S=\mathbb{Z}\sqcup\{\tau\}$.",
    r"All integer sums and products remain.",
    r"$5+(-5)=e\ne\tau$.",
    r"This is the actual programme starting object."
],BLUE)
card(ax,.3,.85,6.45,3.9,r"$u$: sum absorber, multiplicative identity",[
    r"$u+x=u,\qquad ux=x$",
    r"From $\mathbb{Z}$: $B=\{c<u\}$; every integer $\mapsto c$.",
    r"Addition = maximum; multiplication = minimum.",
    r"From $G(\mathbb{Z})$: $C=\{t<c<u\}$.",
    r"$\tau\mapsto t$; every integer $\mapsto c$."
],TEAL)
card(ax,7.1,.85,6.35,3.9,r"$\Omega$: absorber for both",[
    r"$\Omega+x=\Omega,\qquad \Omega x=\Omega$",
    r"From $\mathbb{Z}$: $A=\mathbb{Z}\sqcup\{\Omega\}$.",
    r"All integer sums and products remain.",
    r"From $G(\mathbb{Z})$: $H=\mathbb{Z}\sqcup\{\tau,\Omega\}$.",
    r"Literal rule: $\tau\Omega=\Omega$."
],PURPLE)
ax.text(.35,.43,"Proof: FOUR_CORNERS_OVER_Z.md, Theorem Z1. Exact map conventions are part of the theorem.",
        fontsize=10.5,color=INK)
ax.text(.35,.16,"Original sources: HI-AI [1], §3; HI-AI [2], §§9–10. These are separate constructions, not four global points in one algebra.",
        fontsize=10,color=INK)
save(fig,"05_original_integer_square")

fig, ax = page("Isomorphic under multiplication; different when addition is retained",
    "The displayed bijections preserve the whole multiplication table and the multiplicative identity.",9)
card(ax,.5,4.6,5.4,2.65,r"$S=\mathbb{Z}\sqcup\{\tau\}$",[
    r"Integer multiplication unchanged.",
    r"$\tau x=\tau$ for every $x\in S$.",
    r"$\tau+1=1$."
],BLUE)
card(ax,8.0,4.6,5.4,2.65,r"$A=\mathbb{Z}\sqcup\{\Omega\}$",[
    r"Integer multiplication unchanged.",
    r"$\Omega x=\Omega$ for every $x\in A$.",
    r"$\Omega+1=\Omega$."
],PURPLE)
ax.add_patch(FancyArrowPatch((6.0,5.95),(7.85,5.95),arrowstyle="<->",mutation_scale=18,color=INK,lw=2))
ax.text(6.92,6.55,r"$n\mapsto n$",ha="center",fontsize=15,color=INK)
ax.text(6.92,5.35,r"$\tau\mapsto\Omega$",ha="center",fontsize=15,color=INK)
card(ax,.5,1.4,5.4,2.55,r"$B=\{c<u\}$",[
    r"Addition: maximum.",
    r"Multiplication: minimum.",
    r"Additive identity $c$; multiplicative identity $u$."
],TEAL)
card(ax,8.0,1.4,5.4,2.55,r"$J=\{\varepsilon<a\}$",[
    r"Addition: maximum.",
    r"Multiplication: maximum.",
    r"Common identity $\varepsilon$."
],PURPLE)
ax.add_patch(FancyArrowPatch((6.0,2.7),(7.85,2.7),arrowstyle="<->",mutation_scale=18,color=INK,lw=2))
ax.text(6.92,3.25,r"$c\mapsto a$",ha="center",fontsize=15,color=INK)
ax.text(6.92,2.05,r"$u\mapsto\varepsilon$",ha="center",fontsize=15,color=INK)
ax.text(.5,.78,"All four full algebras are pairwise nonisomorphic. No bijection preserves both operations.",fontsize=14,color=INK,weight="bold")
ax.text(.5,.25,"Proof: Theorem Z2, equations (Z10)–(Z12). Starting definitions: HI-AI [1–2]. Arrows denote monoid isomorphisms only.",
        fontsize=10.5,color=INK)
save(fig,"06_monoid_isomorphisms")

fig, ax = page("Integer value and state together recover every element",
    r"Exact image of $H$ in $A\times L$. Displayed integer sample: $-2,-1,0,1,2$; the formula covers every integer.",10)
cols=[r"$-2$",r"$-1$",r"$e=0$",r"$1$",r"$2$",r"$\Omega$"]
rows=[r"$\Omega$",r"$e$",r"$\tau$"]
x0,y0,w,h=1.7,3.6,1.75,1.0
for j,label in enumerate(cols):
    ax.text(x0+w*(j+.5),y0+3*h+.3,label,ha="center",fontsize=16,color=INK)
for i,label in enumerate(rows):
    y=y0+(2-i)*h
    ax.text(x0-.3,y+h/2,label,ha="right",va="center",fontsize=18,color=INK)
    for j in range(6):
        allowed=(i==0 and j==5) or (i==1 and j<5) or (i==2 and j==2)
        extra=(i==2 and j<5 and j!=2)
        color="#e8edf1"
        if allowed: color=("#efe4f8" if i==0 else "#dceee9" if i==1 else "#dce8fa")
        if extra: color="#f8e2df"
        ax.add_patch(Rectangle((x0+j*w,y),w,h,facecolor=color,edgecolor="white",linewidth=2))
        if allowed:
            val=cols[j] if i==1 else rows[i]
            ax.text(x0+w*(j+.5),y+h/2,val,ha="center",va="center",fontsize=17,color=INK)
        elif extra:
            ax.text(x0+w*(j+.5),y+h/2,"excluded",ha="center",va="center",fontsize=11,color=RED)
        else:
            ax.text(x0+w*(j+.5),y+h/2,"—",ha="center",va="center",fontsize=14,color="#7f8b97")
ax.text(6.8,7.38,r"Arithmetic coordinate $q(x)\in A$",ha="center",fontsize=16,color=INK)
ax.text(.4,5.1,r"State $\rho(x)\in L$",rotation=90,ha="center",va="center",fontsize=15,color=INK)
ax.text(.6,2.9,r"Exact image: $\{(n,e):n\in\mathbb{Z}\}\ \cup\ \{(e,\tau),(\Omega,\Omega)\}$.",fontsize=17,color=INK)
ax.text(.6,2.24,r"Supported zero $(e,e)$ and unsupported $\tau=(e,\tau)$ remain different.",fontsize=15,color=INK)
ax.text(.6,1.64,"Red cells exist in the larger fibre product. The original algebra excludes unsupported nonzero values.",fontsize=12.5,color=RED)
ax.text(.6,1.08,r"Exact condition: shared absorbed state, and $\nu_A(q(x))\leq\rho(x)$ (Section 8).",fontsize=13,color=INK)
ax.text(.6,.42,"Proof: equations (Z23)–(Z27), (Z31)–(Z33); Theorem Z5 gives the kernels. No finite sample replaces the general proof.",
        fontsize=10.5,color=INK)
ax.text(.6,.15,"Original sources: HI-AI [1–2]. Grey cells fail the common-quotient compatibility condition.",fontsize=10.5,color=INK)
save(fig,"07_integer_and_state")
print(str(OUT))
