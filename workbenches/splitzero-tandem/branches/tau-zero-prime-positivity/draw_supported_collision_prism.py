"""Exact maps from SG13--SG23 and EC9--EC41; diagram positions are schematic."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
P=Path(__file__).resolve().parent
plt.rcParams.update({'font.size':12,'mathtext.fontset':'dejavusans'})
def setup(size):
    fig,ax=plt.subplots(figsize=size)
    fig.patch.set_facecolor('#faf9f6');ax.set(xlim=(0,14),ylim=(0,size[1]));ax.axis('off')
    return fig,ax
def box(ax,x,y,w,h,label,color='#edf3f5',size=12):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.12',edgecolor='#536f81',facecolor=color))
    ax.text(x+w/2,y+h/2,label,ha='center',va='center',fontsize=size,linespacing=1.6)
def arrow(ax,xy0,xy1,label='',dy=.2):
    ax.annotate('',xy=xy1,xytext=xy0,arrowprops={'arrowstyle':'->','lw':1.6,'color':'#35596d'})
    ax.text((xy0[0]+xy1[0])/2,(xy0[1]+xy1[1])/2+dy,label,ha='center',va='center',fontsize=11)
fig,ax=setup((14,11))
ax.text(.15,10.55,'The collision prism retains its infinitesimal and its supported spectrum',weight='bold',fontsize=17)
ax.text(.15,10.1,r'$O=\mathbb{Z}_3,\quad C=O[\epsilon,T]/(\epsilon^2,T^2-6\epsilon),\quad a_C=3+\epsilon$',fontsize=14)
box(ax,.3,8.15,4.4,1.1,r'$C$'+'\n'+r'$\mathfrak{n}=(\epsilon,T),\quad\mathfrak{n}^4=0$')
box(ax,8.0,8.15,5.4,1.1,r'$D=C/(a_C)\cong(O/9)[T]/T^2$'+'\n'+r'$\mathfrak{d}=(3,T),\quad\mathfrak{d}^3=0$',color='#edf4ea')
arrow(ax,(4.88,8.7),(7.8,8.7),r'$\epsilon\mapsto-3,\ T\mapsto T$',.36)
ax.text(7,7.58,r'$\mathfrak{n}/a_C\mathfrak{n}\ \cong\ \mathfrak{d}:\quad[\epsilon]\mapsto-3,\ [T]\mapsto T$',ha='center',fontsize=14)
box(ax,.3,5.75,5.9,1.12,'Prism Frobenius on the divisor quotient\n'+r'$\overline{\Phi}:D\to C/3,\quad f_0+f_1T\mapsto\overline{f_0}$'+'\n'+r'$\ker\overline{\Phi}=\mathfrak{d}$',size=11)
box(ax,7.5,5.75,5.9,1.12,'Divided derivation on the same ideal\n'+r'$\overline{\partial}(f_0+f_1T)=\frac{3}{8}f_1T$'+'\n'+r'$\overline{\partial}(\mathfrak{d})=\mathfrak{d}^2=(3T)\ne0$',color='#fbefe4',size=11)
ax.text(.2,5.1,'Prime pullbacks, with the unsupported point retained (SG13–SG17)',weight='bold',fontsize=13)
ax.text(3.05,4.55,r'$\operatorname{Spec}G(C)$',ha='center',fontsize=14)
ax.text(10.65,4.55,r'$\operatorname{Spec}G(D)$',ha='center',fontsize=14)
for y,label in [(1.35,r'$P_\tau(C)$'),(2.55,r'$P_{\mathfrak{n}}(C)=\sqrt{(e_C)}$'),(3.75,r'$P_{\mathfrak{m}}(C)$')]:
    ax.plot(3.05,y,'o',color='#356f90',ms=8);ax.text(2.8,y,label,ha='right',va='center',fontsize=13)
for y,label in [(1.35,r'$P_\tau(D)$'),(3.75,r'$P_{\mathfrak{d}}(D)$')]:
    ax.plot(10.65,y,'o',color='#368a74',ms=8);ax.text(10.9,y,label,va='center',fontsize=13)
arrow(ax,(3.05,1.53),(3.05,2.37));arrow(ax,(3.05,2.73),(3.05,3.57));arrow(ax,(10.65,1.53),(10.65,3.57))
arrow(ax,(10.42,1.35),(3.29,1.35),r'$G(\pi)^*$',.23)
arrow(ax,(10.42,3.75),(3.29,3.75),r'$G(\pi)^*$',.23)
ax.text(6.8,2.55,'No point of this divisor quotient\npulls back to '+r'$P_{\mathfrak{n}}(C)$',ha='center',va='center',fontsize=11,color='#56616b')
ax.text(7,.66,r'$\mathfrak{m}=(3,\epsilon,T)$; vertical arrows mean inclusion of prime ideals.',ha='center',fontsize=11)
ax.text(7,.18,'Full proofs: SG1–SG23. Positions are schematic; all algebraic labels and maps are exact.',ha='center',fontsize=10)
fig.savefig(P/'supported_collision_prism.png',dpi=170,bbox_inches='tight');fig.savefig(P/'supported_collision_prism.svg',bbox_inches='tight');plt.close(fig)
fig,ax=setup((14,8.3))
ax.text(.2,7.88,'Two connecting maps detect different parts of the same extension',weight='bold',fontsize=17)
ax.text(.2,7.38,r'$0\longrightarrow N\overset{\kappa}{\longrightarrow}E\overset{\psi}{\longrightarrow}R\longrightarrow0,\qquad R=\mathbb{F}_3[T]/T^2$',fontsize=14)
ax.text(.2,6.93,r'$N=(O/3)a\oplus(O/9)b,\quad E=(O/9)c_1\oplus(O/9)c_2\oplus(O/3)w$',fontsize=13)
box(ax,.3,4.86,5.9,1.4,'Coefficient-3 connecting map\n'+r'$\beta:R\to N/3N$'+'\n'+r'$1\mapsto\overline{a},\quad T\mapsto0$')
box(ax,7.65,4.86,5.9,1.4,'Distinguished-divisor connecting map\n'+r'$\rho:R\overset{\sim}{\longrightarrow}N[3]$'+'\n'+r'$1\mapsto a,\quad T\mapsto-3b$',color='#edf4ea')
arrow(ax,(7.44,5.57),(6.42,5.57),r'$\mathrm{mod}\ 3N$',.35)
ax.text(7,4.19,r'$\beta(TR)=0,\qquad\rho(TR)=3N=\operatorname{im}A_N\ne0$',ha='center',fontsize=15)
box(ax,.3,2.3,13.25,1.18,r'$\operatorname{Ext}^1_C(R,N)\ \cong\ (N[3]/3N)\oplus N[3]\ \cong\ \mathbb{F}_3\oplus R$'+'\n'+r'$[(n,m)]\mapsto([n],n+m),\qquad E\mapsto(\overline{a},a)$',size=14)
ax.text(7,1.56,r'$\kappa\theta=3\,\mathrm{id}_E,\qquad\kappa\rho\psi=(3+\epsilon)\,\mathrm{id}_E$',ha='center',fontsize=13)
ax.text(7,.98,r'$A_H=5\kappa\,\frac{\theta-\rho\psi}{8},\qquad A_H\kappa=5\kappa A_N$',ha='center',fontsize=15)
ax.text(7,.35,'Full proofs: EC9–EC41. The factor 5 is retained; these finite modules carry no real order.',ha='center',fontsize=11)
fig.savefig(P/'collision_extension_connecting_maps.png',dpi=170,bbox_inches='tight');fig.savefig(P/'collision_extension_connecting_maps.svg',bbox_inches='tight');plt.close(fig)
print('Rendered two diagrams with exact maps and proof locators.')
