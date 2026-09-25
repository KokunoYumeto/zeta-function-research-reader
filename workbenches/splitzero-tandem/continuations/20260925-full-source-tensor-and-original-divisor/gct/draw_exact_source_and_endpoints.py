from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

r=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','mathtext.fontset':'dejavusans','font.size':12})
fig=plt.figure(figsize=(16,12),facecolor='#f8fafc')
ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,16); ax.set_ylim(0,12); ax.axis('off')
def box(x,y,w,h,t,c='#e6eef9',size=13):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.13',facecolor=c,edgecolor='#52637a',linewidth=1.2))
    ax.text(x+w/2,y+h/2,t,ha='center',va='center',fontsize=size,linespacing=1.65)
def arr(x1,y1,x2,y2,t):
    ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle='<->',mutation_scale=16,color='#334155',linewidth=1.5))
    ax.text((x1+x2)/2,(y1+y2)/2+.35,t,ha='center',fontsize=13)

ax.text(.55,11.52,'The exact original source and the retained endpoint directions',fontsize=21,weight='bold',color='#13263d')
ax.text(.55,11.03,'All operations below act on the reconstructed arithmetic coefficient spaces.',fontsize=12,color='#46566b')
ax.text(.65,10.48,'1. A continuous inverse in the actual Schwartz space',fontsize=16,weight='bold')
box(.8,8.8,3.7,1.02,r'$S:\ f\ \mathrm{even\ Schwartz}$'+'\n'+r'$f(0)=0,\quad\int_{\mathbb{R}} f=0$')
box(6.1,8.8,3.65,1.02,r'$J=\Sigma S\subset A$'+'\n'+r'$J=\overline{J}$','#e5f1e9')
box(11.4,8.8,3.8,1.02,r'$\mathcal{I}\subset\mathcal{B}$'+'\nFull vanishing-jet ideal',size=13)
arr(4.7,9.3,5.9,9.3,r'$\Sigma$')
arr(9.95,9.3,11.2,9.3,r'$\mathcal{M}_0$')
ax.text(8,8.2,r'$\Sigma f(u)=2\sum_{n\geq1}f(nu),\qquad F(s)=\mathcal{M}_0b(s)=\int_0^\infty b(u)u^s\,du/u$',ha='center',fontsize=14)
box(.9,6.93,14.2,.72,r'$f_F(x)=\frac{1}{2\pi}\int_{\mathbb{R}}\frac{F(2+it)}{2\zeta(2+it)}x^{-2-it}\,dt,\qquad\Sigma f_F=b\quad(x>0)$','#fff0dd',size=16)
ax.text(8,6.47,r'$\frac{f_F^{(2r)}(0)}{(2r)!}=\frac{F(-2r)}{2\zeta^{\prime}(-2r)},\qquad f_F(0)=0,\qquad\int_{\mathbb{R}}f_F=0$',ha='center',fontsize=15)
ax.text(8,5.98,'The original trivial zeros determine the full even source jet.  [SSI2–SSI6; ESI2–ESI7]',ha='center',fontsize=12)
ax.text(8,5.52,r'$H^1(X,\Omega)=A/J\cong\mathcal{B}/\mathcal{I},\qquad\overline{J}/J=0$'+'  [SSI8; CS11; CSL10]',ha='center',fontsize=14)

ax.plot([.55,15.45],[5.17,5.17],color='#adb7c5')
ax.text(.65,4.72,'2. A different source quotient retains the prime endpoints',fontsize=16,weight='bold')
box(.9,3.2,6.35,1.0,r'$D_{\mathrm{null}}\cong D_{\mathrm{full}}\oplus V$'+'\n'+r'$V=\bigoplus_{p\ \mathrm{prime}}\mathbb{C}^2$','#e5f1e9',size=15)
box(8.0,3.2,7.1,1.0,'For each retained prime label p\nFourier: (c,d) → (−d,−c)\nDilation: + chart (c,ad); − chart (ac,d)',size=12)
ax.text(8,2.64,r'$\ell_p(F)=\sum_d v_p(d)\left(f_d(0),\ d^{-1}\int_{\mathbb{R}}f_d\right)$'+'  for '+r'$P_KF=\sum_d f_d\,1_{d\widehat{\mathbb{Z}}}$',ha='center',fontsize=14)
ax.text(8,2.08,r'$\widetilde{\Omega}\cong\Omega\oplus i_{+*}V_+\oplus i_{-*}V_-$',ha='center',fontsize=16)
ax.text(8,1.55,'H⁰ retains both prime-indexed copies and all four original endpoint lines; H¹ is unchanged.',ha='center',fontsize=12)
ax.text(8,1.05,'The closure quotient in panel 1 and the endpoint summands in panel 2 are different objects.',ha='center',fontsize=12,weight='bold',color='#334155')
ax.text(.55,.45,'Complete proofs: SSI0–SSI10, CS2A/CS11, CSL10, CSB0–CSB10. Source: Connes–Consani, arXiv:0903.2024v3 §5.',fontsize=10,color='#46566b')
ax.text(.55,.17,'Schematic of proved maps. It assigns no coordinate, vector, metric or arithmetic operation to '+r'$\tau\langle Z_1;\ \mathrm{no}\ Z_2\rangle$'+'.',fontsize=10,color='#46566b')
for ext in ('png','svg'):
    fig.savefig(r/('exact_source_and_endpoints.'+ext),dpi=160,facecolor=fig.get_facecolor())
plt.close(fig)
