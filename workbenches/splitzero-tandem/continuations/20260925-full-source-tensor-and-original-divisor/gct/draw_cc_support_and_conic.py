from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

r = Path(__file__).resolve().parent
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 12, 'mathtext.fontset': 'dejavusans'})
fig = plt.figure(figsize=(16, 12), facecolor='#f8fafc')
ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, 16); ax.set_ylim(0, 12); ax.axis('off')

def box(x, y, w, h, text, color='#e7eef8', size=13):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.12',facecolor=color,edgecolor='#536176',linewidth=1.2))
    ax.text(x+w/2,y+h/2,text,ha='center',va='center',fontsize=size,linespacing=1.65)

def arrow(a,b,label='',offset=(0,0)):
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=16,color='#334155',linewidth=1.5))
    if label: ax.text((a[0]+b[0])/2+offset[0],(a[1]+b[1])/2+offset[1],label,ha='center',va='center',fontsize=11,
                      bbox={'facecolor':'#f8fafc','edgecolor':'none','pad':3})

ax.text(.55,11.5,'Actual CC support maps and the descended conic',fontsize=22,weight='bold',color='#14243a')
ax.text(.55,11.05,'Two exact receivers; no metric or arithmetic coordinate is assigned to the parityless support.',fontsize=12,color='#334155')

ax.text(.6,10.5,'1. The coefficient sheaf on the three-point support',fontsize=16,weight='bold')
box(.7,8.55,4.5,1.35,'Chart +\n'+r'$V_+=S\oplus\mathbb{C}^2$'+'\nValue and integral lines retained',size=12)
box(10.8,8.55,4.5,1.35,'Chart −\n'+r'$V_-=S\oplus\mathbb{C}^2$'+'\nValue and integral lines retained',size=12)
box(6.25,8.55,3.5,1.35,'Generic overlap A\n'+r'$\tau\langle Z_1;\ \mathrm{no}\ Z_2\rangle$'+'\nA is a coefficient space',color='#e6f2ec',size=12)
arrow((5.35,9.25),(6.05,9.25),r'$r_+=\Sigma$',(0,.43))
arrow((10.65,9.25),(9.95,9.25),r'$r_-=R\Sigma$',(0,.43))
ax.text(8,8.05,r'$\Sigma f(u)=2\sum_{n\geq1}f(nu),\qquad Ra(u)=u^{-1}a(u^{-1}),\qquad R\Sigma f=\Sigma\widehat f$',ha='center',fontsize=14)
ax.text(8,7.52,'The two chart images coincide. Their cokernel is taken once.  [CSL1–CSL2]',ha='center',fontsize=12)

box(1,6.08,3.1,.82,r'$Q_H$',color='#e6f2ec',size=17)
box(6.05,6.08,3.9,.82,r'$Q_H\oplus Q_H$',color='#e6f2ec',size=17)
box(11.9,6.08,3.1,.82,r'$Q_H$',color='#e6f2ec',size=17)
arrow((4.25,6.49),(5.9,6.49),r'$q\mapsto(q,q)$',(0,.52))
arrow((10.1,6.49),(11.75,6.49),r'$(a,b)\mapsto a-b$',(0,.52))
ax.text(8,5.55,r'Section: $q\mapsto\frac{1}{2}(q,-q)$     Mirror: $R$, swap-with-$R$, $-R$ respectively',ha='center',fontsize=13)
ax.text(8,5.08,r'$\Sigma S=\overline{\Sigma S},\quad Q=Q_H=A/\Sigma S\cong\mathcal{B}/\mathcal{I},\quad N=0$'+'  [SSI1–SSI8; CSL10]',ha='center',fontsize=12)

ax.plot([.5,15.5],[4.62,4.62],color='#a6b2c2')
ax.text(.6,4.17,'2. The geometric Tate factor from the exact signed descent',fontsize=16,weight='bold')
box(.7,2.55,6.2,1.1,r'$[X:Y]\longmapsto[X^2-Y^2:i(X^2+Y^2):2XY]$'+'\nOver '+r'$\mathbb{Z}[1/2,i]$'+', with the full semilinear involution',size=12)
box(9.15,2.55,6.15,1.1,r'$\mathcal{C}:\ x^2+y^2+z^2=0$'+'\n'+r'$\phi^*\mathcal{O}_{\mathcal{C}}(1)=\mathcal{O}_{\mathbb{P}^1}(2)$',color='#f8eadc',size=14)
arrow((7.1,3.1),(8.95,3.1),'Exact descent',(0,.38))
ax.text(.85,1.93,r'At $2$: $(x+y+z)^2=0$; the doubled line is retained.  Specialization: $h_s\mapsto2h_\eta$.',fontsize=13)
ax.text(.85,1.37,r'Every $p$ and every $r\geq1$:  $\#\mathcal{C}(\mathbb{F}_{p^r})=1+p^r$,  $Z(\mathcal{C},s)=\zeta(s)\zeta(s-1)$,  $\Re s>2$.',fontsize=13)
ax.text(.85,.81,'The shift comes from H² = E(−1); this conic has H¹ = 0 in every geometric fibre.  [CD2–CD10]',fontsize=12)
ax.text(.55,.25,'Sources: Connes–Consani, arXiv:0903.2024v3 §5 and arXiv:2609.00299v1 §§3–4. Full proofs: CSL and CD.',fontsize=10,color='#475569')

for ext in ('png','svg'):
    fig.savefig(r/('cc_support_and_conic.'+ext),dpi=160,facecolor=fig.get_facecolor())
plt.close(fig)
