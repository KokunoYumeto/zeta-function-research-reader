from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

out=Path(__file__).resolve().parent
plt.rcParams.update({"font.size":11,"font.family":"DejaVu Sans"})
fig=plt.figure(figsize=(11,6.1),constrained_layout=True)
gs=fig.add_gridspec(2,2,width_ratios=[1,1.35])
ax=fig.add_subplot(gs[0,0])
x=np.linspace(.025,1,700)
r=np.sqrt(np.pi*x)/8*np.exp(-1/(4*x))
ax.plot(x,r,color="#17628f",lw=2.4)
ax.set(xlabel="Original positive heat time t",ylabel="Both resonant moments",
       title=r"$r_t=\sqrt{\pi t}\,e^{-1/(4t)}/8$")
ax.grid(alpha=.2)
ax=fig.add_subplot(gs[1,0])
t=.25; z=np.linspace(-2.8,2.8,700)
ax.plot(z,np.exp(-z*z/(4*t))*np.cos(z/(2*t)),color="#925315",lw=2)
ax.axhline(0,color="grey",lw=.7)
ax.set(xlabel="Original real coordinate Z",ylabel="Adjoint cosine test",
       title=r"$e^{-Z^2/(4t)}\cos(Z/(2t)),\quad t=1/4$")
ax.grid(alpha=.2)
ax=fig.add_subplot(gs[:,1]);ax.axis("off")
def box(y,text,color):
    ax.text(.5,y,text,ha="center",va="center",transform=ax.transAxes,
            fontsize=11,bbox={"boxstyle":"round,pad=.7","facecolor":color,
                              "edgecolor":"#596875","linewidth":1})
def arrow(y1,y2,label=""):
    ax.annotate("",xy=(.5,y2),xytext=(.5,y1),xycoords="axes fraction",
                arrowprops={"arrowstyle":"->","lw":1.5,"color":"#596875"})
    if label:ax.text(.54,(y1+y2)/2,label,transform=ax.transAxes,va="center",fontsize=10)
box(.91,r"Original $\zeta$: $\mathrm{Res}_{s=1}\zeta=1$"+"\n"+
         r"$16H_0(i)=1$ with every factor retained","#edf4f8")
arrow(.83,.73,"ER4, ER7")
box(.65,r"$[H_t]=[1/16]\ne0$ in $\mathcal{S}'/N_t\mathcal{S}'$"+"\n"+
         r"$N_t I=H_t$ has no tempered solution","#fff2db")
arrow(.56,.46,"ER24–26")
box(.38,r"Retained source $(L_t,-4,0)$ or $(L_t,0,-4)$"+"\n"+
         r"in $\mathcal{S}'_{\rm even}\oplus\mathbb{C} B_+\oplus\mathbb{C} B_-$"+"\n"+
         r"Both map to $H_t$; their difference is retained.","#edf4f8")
arrow(.27,.18)
box(.10,r"$h_t=e^{-Z^2/(4t)}H_t(Z)\cos(Z/(2t))$"+"\n"+
         r"$\beta[(t_p-1)\otimes h_t]=\ell_p\otimes(H_t(0),r_t)$","#e7f2e9")
fig.suptitle("The original endpoint residue survives as an arithmetic prime-boundary coordinate",fontsize=14)
fig.savefig(out/"ENDPOINT_RESONANCE.pdf")
fig.savefig(out/"ENDPOINT_RESONANCE.png",dpi=180)
plt.close(fig)
