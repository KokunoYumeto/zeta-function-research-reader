"""Exact prism thickening and the full Frobenius non-descent coefficient."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch
root=Path(__file__).resolve().parent
fig,ax=plt.subplots(figsize=(18,11))
fig.patch.set_facecolor('#fbfaf7');ax.set_facecolor('#fbfaf7')
ax.set_xlim(0,18);ax.set_ylim(0,11);ax.axis('off')
def txt(x,y,s,size=18,**kw):
    ax.text(x,y,s,ha='center',va='center',fontsize=size,color='#20323b',**kw)
def box(x,y,w,h,c):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.13',facecolor=c,edgecolor='#567380',linewidth=1.4))
def arr(a,b):
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=20,color='#267788',linewidth=1.8))
txt(9,10.55,'A prism above the integral counting-adjoint relation',25,weight='bold')
txt(9,10.03,r'Fix any prime $p$, including $2$. Retain every other prime as a Laurent coordinate $U_q$.',17)
box(.5,7.4,17,1.95,'#e7f0f6')
txt(9,8.94,r'$C_p=\mathbb{Z}_p[F_p,V_p,U_q^{\pm1}:q\neq p],\qquad E=F_pV_p-p$',22)
txt(9,8.31,r'$A_p=\widehat{C_p}^{\,(p,E)},\qquad I=(E),\qquad\varphi(F_p)=F_p^p,\quad\varphi(V_p)=V_p^p,\quad\varphi(U_q)=U_q^p$',20)
txt(9,7.76,r'$\delta(E)\operatorname{mod} E=p^{p-1}-1$ is a unit; $A_p/I$ has no $p$-torsion.',19)
arr((9,7.2),(9,6.55));txt(12.8,6.85,r'quotient by the full ideal $(E)$',16)
box(.5,4.65,17,1.66,'#e7f3ed')
txt(9,5.87,r'$A_p/I\ \simeq\ \widehat{\mathcal{H}_{\mathbb{Z}}}^{\,p}$',25)
txt(9,5.31,r'$F_pV_p=p,\qquad F_q=U_q,\quad V_q=qU_q^{-1}\ (q\neq p)$',21)
txt(9,4.88,'The full integral algebra survives; the Frobenius lift does not descend to this quotient.',16)
box(.5,2.46,17,1.59,'#f8eddb')
txt(9,3.6,r'$\varphi(E)\operatorname{mod} E=p(p^{p-1}-1)\neq0$',25)
txt(9,3.07,'This is the exact retained defect, not an omitted term in a commuting square.',17)
txt(9,2.64,r'$F_p,V_p$ are counting-adjoint coordinates. The Frobenius lift is the distinct ring map $\varphi$.',16)
txt(9,1.9,r'$*\,U_q=qU_q^{-1},\qquad\varphi\,*\,U_q=qU_q^{-p},\qquad *\,\varphi U_q=q^pU_q^{-p}$',21)
txt(9,1.24,r'$*:(A_p,\varphi,I)\ \simeq\ (A_p,\varphi^{\prime},I),\qquad\varphi^{\prime}=*\varphi*,\quad\varphi^{\prime}(U_q)=q^{1-p}U_q^p$',20)
txt(9,.64,'The involution exchanges the two global Frobenius lifts; their distinction and every degree factor remain.',16)
txt(9,.21,'Complete proof: INTEGRAL_ADJOINT_PRISM_LIFT.md. No purity or RH conclusion is inferred.',13)
fig.savefig(root/'integral_prism_lift.png',dpi=170,bbox_inches='tight',facecolor=fig.get_facecolor())
fig.savefig(root/'integral_prism_lift.svg',bbox_inches='tight',facecolor=fig.get_facecolor())
print(root/'integral_prism_lift.png')
