"""Exact source and residue diagrams for SZW and EHM."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

B=Path(__file__).resolve().parent; O=B/'figures';O.mkdir(exist_ok=True)
plt.rcParams.update({'font.size':12,'svg.fonttype':'none'})
def box(ax,x,y,w,h,text,color='#edf4f6',size=12):
    from matplotlib.patches import FancyBboxPatch
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.01',fc=color,ec='#71828c',lw=1))
    ax.text(x+w/2,y+h/2,text,ha='center',va='center',fontsize=size)
def arrow(ax,a,b,label='',above=True):
    ax.annotate('',xy=b,xytext=a,arrowprops={'arrowstyle':'->','lw':1.5,'color':'#546b76'})
    if label:ax.text((a[0]+b[0])/2,(a[1]+b[1])/2+(.023 if above else -.045),label,ha='center',fontsize=10)

fig,ax=plt.subplots(figsize=(14,7.5));ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')
ax.text(.5,.97,'Supported zero is retained before taking the Weil trace',ha='center',fontsize=19,weight='bold')
box(ax,.02,.65,.26,.2,r'$G(\mathbb{Z})=\{\tau\}\sqcup\mathbb{Z}^{\bullet}$'+'\n'+r'$e=0^{\bullet}\ne\tau$'+'\n'+r'$(\tau)\subsetneq(e)\subsetneq(p)$',size=15)
box(ax,.37,.65,.27,.2,r'$\Theta_e\phi(x)=\sum_{n\in\mathbb{Z}}\phi(nx)$'+'\n'+r'$n=0:\ \phi(0)$'+'\n'+r'$\Theta_e\phi(x)=x^{-1}\Theta_e\widehat\phi(x^{-1})$',size=12)
box(ax,.73,.65,.25,.2,r'$\left(\phi(0),\int\phi\right)$'+'\n'+r'$=\left(M_f(0),M_f(1)\right)$'+'\n'+r'$-M_f(0)/s+M_f(1)/(s-1)$',size=12)
arrow(ax,(.29,.75),(.36,.75),'full sum')
arrow(ax,(.65,.75),(.72,.75),'Mellin')
ax.text(.5,.56,r'$\phi=J_\theta f,\quad \phi(x)=\int e^{v/2}f(v)e^{-\pi e^{2v}x^2}\,dv,\quad Z_\phi(s)=\Lambda(s)M_f(s)$',ha='center',fontsize=14)
box(ax,.02,.22,.44,.23,'Each lower fixed label stays distinct\n'+r'$c/(\varepsilon+iu)+c/(\varepsilon-iu)\to2\pi c\delta_0(u)$'+'\n'+r'$c/s-c/s=0$'+'\nBoundary distribution survives; meromorphic finite part vanishes.',color='#f1eaf6',size=12)
box(ax,.53,.22,.45,.23,'Full label-resolved trace identity\n'+r'$\boldsymbol{B}_L-\boldsymbol{Z}_L=\boldsymbol{D}_L$'+'\n'+r'$B_L=(H(0)+H(1))e_1+H(0)\sum_{\lambda<1}e_\lambda$'+'\n'+r'$D_L=(P_{\rm fin}-A_\infty)e_1+H(0)\sum_{\lambda<1}e_\lambda$',color='#e5f2eb',size=12)
ax.text(.5,.10,'SZW1–4: prime and arithmetic maps. SZW6–23: full theta, actual tests and boundary maps.\nSZW33–42: retained labels, scalar observations and minimal Fourier closure.',ha='center',fontsize=11)
fig.tight_layout()
for ext in ['png','svg']:fig.savefig(O/f'32_supported_zero_weil.{ext}',dpi=180,bbox_inches='tight')
plt.close(fig)

fig,ax=plt.subplots(figsize=(14,7.4));ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')
ax.text(.5,.96,'Holonomy survives where the infinitesimal trace vanishes',ha='center',fontsize=19,weight='bold')
box(ax,.025,.64,.29,.20,'Two actual heat meridians\n'+r'$h_c=1/8:\quad g_c=(a_+a_-)(b_+b_-)$'+'\n'+r'$h_d=-1/64:\quad g_d=(b_+\ c_-\ b_-\ c_+)$'+'\n'+r'$\langle g_c,g_d\rangle=D_8$',size=12)
box(ax,.365,.64,.29,.20,'Whole colliding local algebra\n'+r'$\mathcal{L}_0=\mathbb{C}[T]/(T^4)$'+'\n'+r'$\epsilon=T^2/6,\quad\mathfrak{N}=(T)$'+'\n'+r'$Q(f,g)=4\overline{f(0)}g(0)$',size=13)
box(ax,.715,.64,.26,.20,'Original dual-number receiver\n'+r'$E_0=\mathbb{C}[r_H]/(r_H^2)$'+'\n'+r'$r_H=T/(2\sqrt{2})$'+'\n'+r'$\ker(\mathcal{L}_0\to E_0)=(T^2)$',size=12)
arrow(ax,(.32,.74),(.36,.74),'collision')
arrow(ax,(.66,.74),(.71,.74),'quotient')
box(ax,.025,.27,.43,.23,'One pair flip cannot extend regularly\n'+r'$t=h-1/8,\quad\beta(\beta+3)=16t$'+'\n'+r'$S_b(T)=(1-2\epsilon/\beta)T$'+'\n'+r'$\left.tS_b(T)\right|_{t=0}=-T^3/16\ne0$',color='#f5e8e5',size=14)
box(ax,.53,.27,.445,.23,'The residue defines an exact nonzero map\n'+r'$\delta=-\frac{T^3}{16}\frac{d}{dT},\quad\delta^2=0$'+'\n'+r'$\mathfrak{N}/\mathfrak{N}^2\ \longrightarrow\ \mathfrak{N}^3$'+'\n'+r'$[n_2]\mapsto-\frac{3}{8}n_3$',color='#e5f2eb',size=14)
arrow(ax,(.46,.38),(.525,.38),'residue')
ax.text(.5,.12,r'$n_1=T^2/2,\quad n_2=3T+T^3/6,\quad n_3=T^3/2;\qquad Q(\delta f,g)=0\ \text{while}\ \delta(T)\ne0.$',ha='center',fontsize=14)
ax.text(.5,.045,'EHM23–34 prove the meridians and full local algebra. EHM42–47 prove the pole, residue and exact filtration map.',ha='center',fontsize=11)
fig.tight_layout()
for ext in ['png','svg']:fig.savefig(O/f'33_holonomy_infinitesimal_residue.{ext}',dpi=180,bbox_inches='tight')
plt.close(fig)
print('Rendered figures32–33 with exact supported-zero and collision maps.')
