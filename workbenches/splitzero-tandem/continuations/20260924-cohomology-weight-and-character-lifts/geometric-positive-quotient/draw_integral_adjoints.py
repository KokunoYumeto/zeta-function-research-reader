"""Exact integral and infinitesimal maps, without numerical zero samples."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

root=Path(__file__).resolve().parent
fig,ax=plt.subplots(figsize=(18,12))
fig.patch.set_facecolor('#fbfaf7'); ax.set_facecolor('#fbfaf7')
ax.set_xlim(0,18); ax.set_ylim(0,12); ax.axis('off')
def text(x,y,s,size=17,**kw):
    ax.text(x,y,s,fontsize=size,ha='center',va='center',color='#18303d',**kw)
def box(x,y,w,h,color):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.12',facecolor=color,edgecolor='#536b78',linewidth=1.3))
def arrow(a,b):
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=18,color='#287381',linewidth=1.8))
text(9,11.6,'Integral counting, the adjoint, and a trace that retains an infinitesimal fibre',23,weight='bold')
text(9,11.05,r'Every prime $p$ is retained. These are operator coordinates; no coordinate or addition is assigned to $\tau$.',15)
box(.5,8.9,7.1,1.65,'#e8f3ef'); box(10.4,8.9,7.1,1.65,'#e9eef8')
text(4.05,10.1,r'$\mathcal{H}_{\mathbb{Z}}=\mathbb{Z}[b_n,n b_{1/n}:n\geq1]$',21)
text(4.05,9.58,r'$b_r^*=r b_{1/r},\qquad C_{a/b}=b\,b_{a/b}\quad (\gcd(a,b)=1)$',16)
text(4.05,9.12,'Smallest adjoint-stable ring containing the positive counts',14)
text(13.95,10.1,r'$\mathbb{Q}[\mathbb{Q}_{>0}^{\times}]$',23)
text(13.95,9.5,r'$\mathbb{Q}\otimes_{\mathbb{Z}}\mathcal{H}_{\mathbb{Z}}\ \simeq\ \mathbb{Q}[\mathbb{Q}_{>0}^{\times}]$',18)
arrow((7.8,9.95),(10.15,9.95)); text(8.95,10.32,'inclusion',15)
text(9,8.42,r'$\mathcal{H}_{\mathbb{Z}}\simeq\bigotimes_p B_p,\qquad B_p=\mathbb{Z}[F,V]/(FV-p),\quad F^*=V$',21)
box(.5,6.3,17,1.45,'#f4eddf')
text(9,7.31,r'$X=F+V,\qquad B_p\simeq\mathbb{Z}[X,F]/(F^2-XF+p),\qquad (F-V)^2=X^2-4p$',22)
text(9,6.65,'The trace map has rank two. Its two operator roots remain distinct until a branch fibre.',16)
arrow((9,6.15),(9,5.64));text(12.45,5.93,r'$A_p=\mathbb{Z}[\alpha]/(\alpha^2-p),\quad X=2\sigma\alpha$',16)
box(3.35,3.8,11.3,1.65,'#e6f1f2')
text(9,5.04,r'$B_{p,\sigma}\simeq A_p[\varepsilon]/(\varepsilon^2),\qquad \sigma\in\{+1,-1\}$',23)
text(9,4.48,r'$F=\sigma\alpha+\varepsilon,\quad V=\sigma\alpha-\varepsilon,\quad \varepsilon^*=-\varepsilon$',22)
text(9,3.99,r'$F+V=2\sigma\alpha$ while $\varepsilon\neq0$; imposing $F=V$ gives $2\varepsilon=0$ integrally.',16)
arrow((6,3.65),(4.2,3.0));arrow((12,3.65),(13.8,3.0))
box(.5,.87,7.5,1.92,'#e7edf5'); box(10,.87,7.5,1.92,'#f9eadc')
text(4.25,2.44,'Faithful indefinite receiver over the reals',17,weight='bold')
text(4.25,1.89,r'$\varepsilon\mapsto N\neq0,\quad N^2=0,\quad N^*J=-JN$',18)
text(4.25,1.35,r'$F_\sigma=\sigma\sqrt{p}\,I+N,\qquad F_\sigma^*JF_\sigma=pJ$',18)
text(13.75,2.44,'Every positive Hilbert star representation',17,weight='bold')
text(13.75,1.89,r'$E^*=-E,\ E^2=0\ \Longrightarrow\ \|Ev\|^2=0$',19)
text(13.75,1.35,r'$\mathbb{R}[\varepsilon]/(\varepsilon^2)\longrightarrow\mathbb{R},\quad\ker=(\varepsilon)$',20)
text(9,.44,'IAR1–IAR3; AT2–AT5. Actual zeta operators and every jet are retained in AT5. Positivity of the full Weil form is not inferred.',13)
fig.savefig(root/'integral_adjoints.png',dpi=170,bbox_inches='tight',facecolor=fig.get_facecolor())
fig.savefig(root/'integral_adjoints.svg',bbox_inches='tight',facecolor=fig.get_facecolor())
print(root/'integral_adjoints.png')
