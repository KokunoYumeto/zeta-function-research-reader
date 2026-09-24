"""Reproduce the exact residue and support-dual comparison diagram."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

base=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'mathtext.fontset':'dejavusans'})
fig,ax=plt.subplots(figsize=(13,9.4));ax.set_xlim(0,13);ax.set_ylim(0,9.4);ax.axis('off')
blue='#245775';dark='#183849';green='#23695c'
def panel(x,y,w,h,title):
 ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.12',facecolor='#f4f8fb',edgecolor='#bacbd4'))
 ax.text(x+.15,y+h-.28,title,color=blue,weight='bold',fontsize=12,va='top')
def txt(x,y,s,size=13,color=dark):ax.text(x,y,s,fontsize=size,color=color,va='center')
def arrow(x1,y1,x2,y2):ax.annotate('',xy=(x2,y2),xytext=(x1,y1),arrowprops={'arrowstyle':'->','color':blue,'lw':1.6})
txt(.25,9.06,'Original-zeta residues retain every multiplicity coordinate',17,blue)
txt(.25,8.65,'Actual coefficient dual and support maps · full original zero divisor · proofs RD1–RD7',10)
panel(.3,5.72,12.35,2.35,'A. A separating dual receiver, with its topology specified')
txt(.65,7.18,r'$\mathcal{Q}_{\mathrm{fin}}$',19);arrow(2,7.18,3.5,7.18)
txt(2.38,7.51,r'$\iota\;\cong$',14)
txt(3.6,7.18,r'$\mathcal{D}\subset\mathcal{Q}^{\prime}$',19);arrow(6.2,7.18,8.3,7.18)
txt(6.65,7.51,r'$\kappa^{\prime}$',14)
txt(8.45,7.18,r'$H^1(Y,\mathscr{F})^{\prime}$',19)
txt(.65,6.59,r'$\iota(G)([F])=\sum_{\rho}\mathrm{Res}_{s=\rho}\,\frac{F(s)G(1-s)}{\zeta(s)}\,ds$',16)
txt(.65,6.07,'D contains every derivative functional; its weak closure is the entire continuous dual.',11)
panel(.3,2.74,6.06,2.58,'B. Exact local matrix, for every multiplicity m')
txt(.65,4.62,r'$\zeta(\rho+t)=t^m u_\rho(t),\quad u_\rho(0)\neq0$',14)
txt(.65,4.01,r'$B_{ij}=(-1)^j[t^{m-1-i-j}]\,u_\rho(t)^{-1}$',15)
txt(.65,3.43,r'$\det B=u_\rho(0)^{-m}\neq0$',17,green)
txt(.65,2.99,'Higher jets survive; no zero simplicity is assumed.',10)
panel(6.77,2.74,5.88,2.58,'C. Arithmetic and the normal degree factor')
txt(7.05,4.65,r'$\iota T_n=n(T_{1/n})^{\prime}\iota$',17)
txt(7.05,4.04,r'$\mathcal{R}(n^kT_nx,n^\ell T_ng)=n^{k+\ell+1}\mathcal{R}(x,g)$',12)
txt(7.05,3.45,r'Normal action: $nT_n$; its contragredient:',11)
txt(7.05,3.03,r'$n^{-1}(T_{1/n})^{\prime}$',16)
panel(.3,.66,12.35,1.69,'D. The two support orientations stay visible under transposition')
txt(.65,1.55,r'$H^1:\ (x_+,x_-)\mapsto x_+-x_-\quad\Longrightarrow\quad\lambda\mapsto(\lambda,-\lambda)$',15)
txt(.65,.99,r'$H^2:\ (a_+,a_-)\mapsto a_++a_-\quad\Longrightarrow\quad\lambda\mapsto(\lambda,\lambda)$',15)
txt(.3,.3,'These are proved dual maps. Positivity and Deligne weight separation are not asserted. Sources: RD1–RD9; CSP7–CSP8.',9)
fig.savefig(base/'original_zeta_residue_dual.png',dpi=180,bbox_inches='tight',facecolor='white')
fig.savefig(base/'original_zeta_residue_dual.svg',bbox_inches='tight',facecolor='white')
print(base/'original_zeta_residue_dual.png')
