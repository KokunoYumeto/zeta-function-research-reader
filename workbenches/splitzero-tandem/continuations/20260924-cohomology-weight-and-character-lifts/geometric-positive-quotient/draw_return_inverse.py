"""Exact global measure comparison; no numerical zero samples."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

root=Path(__file__).resolve().parent
fig,ax=plt.subplots(figsize=(17,10))
fig.patch.set_facecolor('#fbfaf7')
ax.set_facecolor('#fbfaf7')
ax.set_xlim(0,17);ax.set_ylim(0,10);ax.axis('off')
def txt(x,y,s,size=17,**kw):
    return ax.text(x,y,s,fontsize=size,ha='center',va='center',color='#17252c',**kw)
def box(x,y,w,h,color):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.13',facecolor=color,edgecolor='#486270',linewidth=1.3))
def arrow(a,b,color='#276a78'):
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=18,color=color,linewidth=1.8))
txt(8.5,9.55,'The polarized return trace retains the complete original arithmetic history',23,weight='bold')
txt(8.5,9.02,r'$\mathscr{P}\mu=(d_2)_*(e^t\mu),\quad d_2(t)=2t,\qquad \mathscr{P}^{-1}\nu=(d_{1/2})_*(e^{-u/2}\nu)$',19)
txt(4,8.3,'Original arithmetic: every prime p, every k ≥ 1',16,weight='bold')
txt(13,8.3,'Polarized cohomology: both eigenvalue signs retained',16,weight='bold')
box(.55,6.45,6.6,1.3,'#e8f3f0');box(9.85,6.45,6.6,1.3,'#e8edf8')
txt(3.85,7.3,r'$\mathcal{R}=\sum_p\sum_{k\geq1}\frac{1}{k}\delta_{k\log p}$',21)
txt(3.85,6.72,'Primitive returns and all repetition coefficients',14)
txt(13.15,7.3,r'$\mathcal{R}_1=\sum_p\sum_{k\geq1}\frac{2p^k}{k}\delta_{2k\log p}$',21)
txt(13.15,6.72,r'From $\operatorname{Tr}(F_p^{2k})=4p^k$; odd traces cancel',14)
arrow((7.3,7.35),(9.65,7.35));txt(8.48,7.62,r'$2\mathscr{P}$',18)
arrow((9.65,6.8),(7.3,6.8));txt(8.48,6.5,r'$\frac{1}{2}\mathscr{P}^{-1}$',18)
arrow((3.85,6.2),(3.85,5.56));txt(4.75,5.9,r'$t\cdot$',17)
arrow((13.15,6.2),(13.15,5.56));txt(14.05,5.9,r'$u\cdot$',17)
box(.55,3.95,6.6,1.3,'#e8f3f0');box(9.85,3.95,6.6,1.3,'#e8edf8')
txt(3.85,4.8,r'$\mathcal{W}=\sum_p\sum_{k\geq1}(\log p)\delta_{k\log p}$',21)
txt(3.85,4.23,r'$\mathcal{D}=\exp_*\mathcal{R}$ retains the unit atom $\delta_0$',14)
txt(13.15,4.8,r'$\mathcal{W}_1=\sum_p\sum_{k\geq1}4p^k\log p\,\delta_{2k\log p}$',20)
txt(13.15,4.23,r'$\frac{1}{4}e^{-u/2}\cdot4p^k\log p=\log p$ at $u=2k\log p$',14)
arrow((7.3,4.85),(9.65,4.85));txt(8.48,5.12,r'$4\mathscr{P}$',18)
arrow((9.65,4.3),(7.3,4.3));txt(8.48,4.0,r'$\frac{1}{4}\mathscr{P}^{-1}$',18)
box(.55,1.27,15.9,1.94,'#fff0d8')
txt(8.5,2.84,'Exact transport into the original Weil form — endpoints, Gamma and support data remain',17,weight='bold')
txt(8.5,2.12,r'$W_\zeta(h)=H_h(0)+H_h(1)+A_\infty(h)-\frac{1}{4}\int_{(0,\infty)}e^{-3u/4}[h(u/2)+h(-u/2)]\,d\mathcal{W}_1(u)$',20)
txt(8.5,1.52,r'$\zeta(s)=\exp\!\left(\frac{1}{2}\int_{(0,\infty)}u^{-1}e^{-(s+1)u/2}\,d\mathcal{W}_1(u)\right),\quad \Re s>1$',18)
txt(8.5,.76,'PRI2–PRI7: all arrows are proved for complete locally finite measures. No finite range is substituted.',14)
txt(8.5,.35,'The unit atom records integer 1; it does not identify τ with that atom. Positivity of the full Weil form remains unproved.',13)
fig.savefig(root/'return_inverse.png',dpi=175,bbox_inches='tight',facecolor=fig.get_facecolor())
fig.savefig(root/'return_inverse.svg',bbox_inches='tight',facecolor=fig.get_facecolor())
print(str(root/'return_inverse.png'))
