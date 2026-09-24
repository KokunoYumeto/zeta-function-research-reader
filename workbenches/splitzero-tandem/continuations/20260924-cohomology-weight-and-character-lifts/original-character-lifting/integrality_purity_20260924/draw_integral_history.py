"""Reproducible diagrams using the original formulas and periods."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
HERE = Path(__file__).resolve().parent
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":12,
                     "mathtext.fontset":"dejavusans","svg.fonttype":"none"})
blue, orange, green, dark = "#155E9A", "#BB5319", "#14705B", "#202D3D"
def box(ax,x,y,w,h,title,body,color=blue):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.01",
        facecolor="#f5f8fc",edgecolor=color,lw=1.8))
    ax.text(x+w/2,y+h-.025,title,ha="center",va="top",weight="bold",color=color,fontsize=14)
    ax.text(x+w/2,y+h/2-.04,body,ha="center",va="center",fontsize=12,linespacing=1.7)
def arrow(ax,a,b):
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle="-|>",mutation_scale=17,color=dark,lw=1.6))
fig,ax=plt.subplots(figsize=(15,9))
ax.set(xlim=(0,1),ylim=(0,1)); ax.axis("off")
ax.text(.5,.98,"One complete arithmetic record, with its spectral observations",
        ha="center",va="top",fontsize=19,weight="bold",color=dark)
box(ax,.02,.65,.28,.24,"Full signed source",
    r"$1\to C_4\to G\to W\to1$"+"\n"+r"$R=\mathrm{End}(W),\quad \mathbf{1}_R=\mathrm{id}_W$"+"\n"+
    r"$\eta$: support; $\tau$: $Z_1$, no $Z_2$")
box(ax,.36,.65,.28,.24,"Every prime and repetition",
    r"$\mathcal{D}=\delta_0+\sum_{n\geq2}\delta_{\log n}$"+"\n"+
    r"$\mathcal{W}=\sum_{p,k\geq1}(\log p)\delta_{k\log p}$"+"\n"+"Unit atom and all weights retained")
box(ax,.70,.65,.28,.24,"Original function",
    r"$\mathcal{L}\mathcal{D}(s)=\zeta(s)$"+"\n"+
    r"$\mathcal{L}\mathcal{W}(s)=-\zeta'(s)/\zeta(s)$"+"\n"+r"$\mathrm{Re}\,s>1$, then continuation")
arrow(ax,(.30,.77),(.36,.77)); arrow(ax,(.64,.77),(.70,.77))
box(ax,.02,.28,.44,.26,"Actual quotient and full zero jets",
    r"$F_k(s)=\int_0^\infty k(u)u^{s-1/2}\,du/u$"+"\n"+
    r"$j_\rho(W_pq)=p^\rho e^{(\log p)t_\rho}j_\rho(q)$"+"\n"+
    r"$t_\rho^{m_\rho}=0$; every coefficient retained")
box(ax,.54,.28,.44,.26,"Faithful joint value observations",
    r"$t_{a,b}=a\log2+b\log3,\quad (a,b)\in\mathbb{Z}^2$"+"\n"+
    r"$\mathcal{T}(q)_{a,b}=\sum_\rho m_\rho F_q(\rho)e^{-\rho t_{a,b}}$"+"\n"+
    r"$\ker\mathcal{T}=\ker(F_q(\rho))_\rho$")
arrow(ax,(.84,.65),(.84,.58)); arrow(ax,(.84,.58),(.24,.58)); arrow(ax,(.24,.58),(.24,.54))
arrow(ax,(.46,.41),(.54,.41))
ax.text(.5,.19,"A hypothetical off-critical quartet has the exact absorption contribution",ha="center",fontsize=13)
ax.text(.5,.13,r"$-2m\left(e^{\beta t}+e^{(1-\beta)t}\right)\cos(\gamma t)$",ha="center",fontsize=21,color=orange)
ax.text(.5,.07,"It is a term in the same complete distribution, not a new prime event.",ha="center",fontsize=12)
ax.text(.5,.015,"Proofs IH1–IH6. Geometry: Connes–Consani (2026); scalar reconstruction: programme CG/TP/I26.\n"
        "No numerical off-critical zero is asserted. This diagram displays maps, not a proof of RH.",ha="center",fontsize=9,color=dark)
for ext in ["png","svg"]:
    fig.savefig(HERE/("INTEGRAL_HISTORY_AND_PURITY."+ext),dpi=170,bbox_inches="tight")
plt.close(fig)

fig=plt.figure(figsize=(15,11))
gs=fig.add_gridspec(2,2,left=.06,right=.97,top=.88,bottom=.12,wspace=.24,hspace=.45)
fig.suptitle("A point can return while its fibre retains a nontrivial return map",fontsize=19,weight="bold",y=.97,color=dark)
fig.text(.5,.925,r"Original curves $E_p=\mathbb{C}^{\times}/p^{\mathbb{Z}}$; both $\log p$ and $2\pi i$ retained",ha="center",fontsize=14)
ax=fig.add_subplot(gs[0,0])
for p,y,col in [(2,1,blue),(3,0,orange)]:
    times=np.arange(0,7)*np.log(p); times=times[times<=4.3]
    ax.hlines(y,0,4.3,color=col,lw=1)
    ax.scatter(times,np.full_like(times,y),c=col,s=48)
    for k,t in enumerate(times):
        lab="0" if k==0 else "$"+str(k)+r"\log "+str(p)+"$"
        ax.text(t,y+.11,lab,ha="center",fontsize=9)
ax.set(xlim=(-.12,4.4),ylim=(-.35,1.55),yticks=[0,1],yticklabels=[r"$E_3$",r"$E_2$"],
       xlabel=r"real logarithmic time $t$ (finite segment shown)")
ax.set_title("Individual returns; no shared nonzero real return",loc="left",fontsize=13,pad=17)
ax.text(.5,-.33,r"$a\log2=b\log3\ \Longrightarrow\ a=b=0$",transform=ax.transAxes,ha="center",color=green)
ax.spines[["top","right","left"]].set_visible(False)
ax=fig.add_subplot(gs[0,1])
for p,col,marker in [(2,blue,"o"),(3,orange,"x")]:
    for j in [0,1]:
        xx=np.arange(-2,3)*np.log(p)
        ax.scatter(xx,np.full_like(xx,2*np.pi*j),c=col,marker=marker,s=65,label="$p="+str(p)+"$" if j==0 else None)
ax.plot([0,0],[0,2*np.pi],color=green,lw=2,alpha=.7)
ax.annotate(r"$2\pi i$",xy=(0,2*np.pi),xytext=(.45,4.5),arrowprops={"arrowstyle":"->","color":green},color=green,fontsize=13)
ax.set(xlim=(-2.6,2.6),ylim=(-.65,7),xlabel=r"$\mathrm{Re}\,u$",ylabel=r"$\mathrm{Im}\,u$",
       yticks=[0,2*np.pi],yticklabels=["0",r"$2\pi$"])
ax.legend(loc="center left",fontsize=10)
ax.set_title("Common angular period remains",loc="left",fontsize=13,pad=17)
ax.text(.5,-.33,r"$\Lambda_2^{\log}\cap\Lambda_3^{\log}=2\pi i\,\mathbb{Z}$",transform=ax.transAxes,ha="center",color=green)
ax.spines[["top","right"]].set_visible(False)
ax=fig.add_subplot(gs[1,0]); ax.set(xlim=(0,1),ylim=(0,1)); ax.axis("off")
box(ax,.03,.55,.94,.37,"Same support, retained winding",
    r"$G=\{T^mJ^k:m\in\mathbb{Z},\ k\ \mathrm{mod}\ 4\}$"+"\n"+r"$\pi(T^mJ^k)=\eta$ for every $m,k$",green)
arrow(ax,(.5,.55),(.5,.38))
ax.text(.5,.30,r"$\eta\quad\longleftrightarrow\quad \tau\langle Z_1;\ \mathrm{no}\ Z_2\rangle$",ha="center",fontsize=16,color=green)
ax.text(.5,.11,"The support map is constant.\nThe complete stalk is still present.",ha="center",fontsize=12)
ax=fig.add_subplot(gs[1,1]); ax.set(xlim=(0,1),ylim=(0,1)); ax.axis("off")
box(ax,.03,.43,.94,.49,"One real prime cycle",
    r"$\nabla_\rho=d-\rho\,du,\qquad \rho=\beta+i\gamma$"+"\n"+
    r"$v\longmapsto p^\rho v$"+"\n"+r"$|p^\rho|^2-p=p^{2\beta}-p$",orange)
ax.text(.5,.25,r"Critical: $|p^\rho|^2=p$, although $p^\rho\ne1$",ha="center",fontsize=12)
ax.text(.5,.09,r"Angular cycle: $v\longmapsto e^{2\pi i\rho}v$",ha="center",fontsize=13)
fig.text(.5,.043,"Proofs PL3–PL6. Blue/orange points use exact logarithmic periods; axes retain their stated coordinates.\n"
         "Geometry: Alain Connes and Caterina Consani, arXiv:2606.06604v1 and 2609.00299v1.\n"
         "The display calculates return maps; it asserts no off-critical zeta zero and no RH conclusion.",ha="center",fontsize=9,color=dark)
for ext in ["png","svg"]:
    fig.savefig(HERE/("PRIME_CLOCK_LOOPS_AND_Z1."+ext),dpi=170,bbox_inches="tight")
plt.close(fig)
print("Wrote both figures as PNG and SVG.")
