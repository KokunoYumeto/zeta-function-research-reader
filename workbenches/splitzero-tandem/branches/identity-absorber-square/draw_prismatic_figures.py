"""Exact algebra diagrams for the base extension and prismatic comparison."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

OUT=Path(__file__).resolve().parent/"figures"
OUT.mkdir(exist_ok=True)
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":13,"svg.fonttype":"none"})
INK="#183047"; BLUE="#245eaa"; GREEN="#157564"; RED="#ad3545"

def page(title,sub,h):
    fig,ax=plt.subplots(figsize=(15,h))
    fig.patch.set_facecolor("#fcfcfa")
    ax.set(xlim=(0,15),ylim=(0,h)); ax.axis("off")
    fig.subplots_adjust(left=.025,right=.985,bottom=.025,top=.975)
    ax.text(.2,h-.25,title,fontsize=22,weight="bold",color=INK,va="top")
    ax.text(.2,h-.93,sub,fontsize=12,color=INK,va="top")
    return fig,ax
def box(ax,x,y,w,h,head,rows,color=BLUE):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=.08",fc="white",ec=color,lw=2))
    ax.text(x+.2,y+h-.25,head,fontsize=18,color=color,va="top")
    for i,row in enumerate(rows):
        ax.text(x+.2,y+h-.92-.52*i,row,fontsize=14,color=INK,va="top")
def arrow(ax,start,end,label,at):
    ax.add_patch(FancyArrowPatch(start,end,arrowstyle="-|>",mutation_scale=18,color=INK,lw=1.6))
    ax.text(*at,label,fontsize=14,color=INK,ha="center")
def save(fig,name):
    for ext in ("png","svg"):
        fig.savefig(OUT/f"{name}.{ext}",dpi=150,bbox_inches="tight",facecolor=fig.get_facecolor())
    plt.close(fig)

fig,ax=page("What the monoid ring adds","Exact coordinates; integer zero e and unsupported tau remain separate in the source.",10.7)
box(ax,.35,6.35,6.35,2.55,r"$\Gamma(S)\cong\mathbb{Z}\times\Lambda$",[
    r"$[e]\mapsto(1,0),\quad[n]\mapsto(1,[n])\quad(n\ne0)$",
    r"$\Lambda=\mathbb{Z}[\mathbb{Z}\setminus\{0\},\,\cdot]$",
    r"First projection = induced support observation."])
box(ax,8.0,6.35,6.45,2.55,r"$\mathbb{Z}$: original integer addition",[
    r"$(k,v)\mapsto\operatorname{ev}(v),\quad[n]\mapsto n$",
    r"$\ker=\mathbb{Z}\times\ker(\operatorname{ev})$",
    r"The relation $e+e=e$ kills the support factor."],GREEN)
arrow(ax,(6.85,7.65),(7.8,7.65),"quotient",(7.33,8.0))
box(ax,.35,2.85,6.35,2.6,r"$\Gamma(H)\cong\mathbb{Z}^2\times\Lambda$",[
    r"$[\tau]=(1,0,0),\quad[e]=(1,1,0)$",
    r"$[n]=(1,1,[n])\quad(n\ne0)$",
    r"$\Gamma q(k,l,v)=(k,v),\quad\Gamma\rho(k,l,v)=(k,l)$"])
box(ax,8.0,2.85,6.45,2.6,r"$\Gamma(A)\times_{\Gamma(D)}\Gamma(L)$",[
    r"$=\{((k,v),(k,l)):k,l\in\mathbb{Z},\ v\in\Lambda\}$",
    r"$\Gamma(A)=\mathbb{Z}\times\Lambda,\quad\Gamma(L)=\mathbb{Z}^2$",
    r"Both maps to $\Gamma(D)=\mathbb{Z}$ read off $k$."],GREEN)
arrow(ax,(6.85,4.15),(7.8,4.15),r"$\cong$",(7.33,4.48))
ax.text(.55,1.9,r"The source had no element with observations $(n,\tau)$ for $n\ne0$.",fontsize=16,color=INK)
ax.text(.55,1.28,r"The ring has $[n]-[e]+[\tau]=(1,0,[n])$, mapping to exactly $([n],[\tau])$.",fontsize=16,color=INK)
ax.text(.55,.45,"Proofs: Four corners over the integers, Theorems Z7–Z8, equations Z37–Z49. Source definition: HI-AI, 11.tex.",fontsize=11,color=INK)
save(fig,"08_monoid_base_extension")

fig,ax=page("The prismatic bridge and the addition obstruction","Fix a prime p. Brackets denote a monoid basis element; p without brackets is an integer scalar.",12.3)
box(ax,.35,7.7,7.0,3.05,"Canonical monoid Frobenius",[
    r"$B_S=\mathbb{Z}_p\times\widehat{\Lambda},\quad I=(p)$",
    r"$\phi([n])=[n^p],\qquad\delta([n])=0$",
    r"$r=[p]-p\cdot1,\quad \delta(r)\equiv p^{p-1}-1\ (\mathrm{mod}\ r)$",
    r"The remainder is a unit: $(r,\delta(r))=B_S$."])
box(ax,8.0,7.7,6.45,3.05,"Arithmetic evaluation",[
    r"$\epsilon(k,v)=\operatorname{ev}(v)\in\mathbb{Z}_p$",
    r"$\phi_{\mathbb{Z}_p}(x)=x$",
    r"$\delta_{\mathbb{Z}_p}(p)=1-p^{p-1}\ne0$",
    r"$\epsilon$ is a ring map, but not a $\delta$-map."],RED)
box(ax,.35,4.3,14.1,2.65,"Positive bridge through Witt vectors",[
    r"$(B_S,(p),\phi)\ \longrightarrow\ (W(\mathbb{Z}_p),(p),F)\ \longrightarrow\ \mathbb{Z}_p$",
    r"$[n]\mapsto\langle n\rangle,\quad \mathrm{ghost}_j(\langle n\rangle)=n^{p^j};\qquad w_0(\langle n\rangle)=n$",
    r"First arrow: prism morphism. Second: ring projection. For $p=2$, $\langle1\rangle+\langle1\rangle$ begins $(2,-1)$."],GREEN)
box(ax,.35,.85,14.1,2.8,"A conjugate Frobenius family preserves the original addition",[
    r"$x_\ell=[\ell]\ (\ell\ \mathrm{prime}),\quad t=[-1],\quad t^2=1$",
    r"$\Psi_p(x_\ell)=(x_\ell-\ell)^p+\ell;\quad\Psi_p(t)=t\ (p\ \mathrm{odd}),\quad -1\ (p=2)$",
    r"$\sigma(x_\ell)=x_\ell-\ell,\quad\sigma(t)=-t:\qquad\Psi_p=\sigma\phi_p\sigma^{-1}$.",
    r"$\epsilon\Psi_p=\epsilon$; the maps commute across primes. Translation uses the chosen integer addition."],GREEN)
ax.text(.45,.3,"Full proof: Prismatic comparison. Definitions: Bhatt–Scholze, arXiv:1905.08229v4, Section 2; Bhatt–Lurie, 2201.06120v1.",fontsize=11,color=INK)
save(fig,"09_prismatic_bridge")
