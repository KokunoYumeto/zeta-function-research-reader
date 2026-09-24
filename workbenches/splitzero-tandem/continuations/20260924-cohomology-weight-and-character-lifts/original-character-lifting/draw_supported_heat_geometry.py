"""Exact degree-four heat example and the actual theta support, THS19–25."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

R=Path(__file__).resolve().parent
fig=plt.figure(figsize=(15,12),facecolor='white')
ax=fig.add_axes([.03,.03,.94,.94]);ax.set_xlim(0,15);ax.set_ylim(0,12);ax.axis('off')
blue='#164e75';teal='#087e83';purple='#7452a6';ink='#182432';muted='#526475'
ax.text(.25,11.65,'Supported time-zero is a projection',fontsize=25,fontweight='bold',color=ink)
ax.text(.25,11.18,r'$e=(0,1_L),\quad\tau=(0,0_L),\quad\Phi(c,\lambda)=(c,1_K\otimes\lambda)$',fontsize=18,color=blue)
def panel(y,h):
    ax.add_patch(FancyBboxPatch((.12,y),14.7,h,boxstyle='round,pad=0.04,rounding_size=.08',facecolor='#f3f6fa',edgecolor='#d5dfe8',linewidth=1))
panel(7.45,3.25)
ax.text(.4,10.32,'Exact finite example: the polynomial $z^4$',fontsize=19,fontweight='bold',color=ink)
ax.text(.4,9.81,r'$q(U_{(t,1_L)}z^4)=z^4-12tz^2+12t^2$',fontsize=19,color=ink)
xs=[1.5,4.2,6.9,9.6,12.3]
for j,x in enumerate(xs):
    ax.text(x,9.26,f'Degree {j}',ha='center',fontsize=13,color=muted)
    ax.text(x,8.77,r'$1_S$' if j==4 else r'$\tau$',ha='center',fontsize=22,color=ink)
    ax.annotate('',(x,8.12),(x,8.53),arrowprops={'arrowstyle':'->','color':teal,'lw':1.6})
    value=r'$1_S$' if j==4 else (r'$e$' if j%2==0 else r'$\tau$')
    ax.text(x,7.79,value,ha='center',fontsize=22,color=teal)
ax.text(14.28,8.71,'input',ha='right',fontsize=12,color=muted)
ax.text(14.28,7.82,r'$U_e$ output',ha='right',fontsize=13,color=teal)
panel(3.8,3.35)
ax.text(.4,6.75,'The full map retains the changed support matrix',fontsize=19,fontweight='bold',color=ink)
ax.text(.4,6.18,r'$U_{(1,1_L)}U_{(-1,1_L)}=U_e\ne U_\tau=I_5$',fontsize=19,color=ink)
ax.text(.4,5.61,r'$\Phi(U_e)=(I_5,B_{1_L})$',fontsize=21,color=blue)
ax.text(.4,4.99,'Fixed-image labels keep the two parity chains:',fontsize=15,color=muted)
ax.text(.4,4.36,r'$\nu_0\geq\nu_2\geq\nu_4,\qquad\nu_1\geq\nu_3$',fontsize=21,color=teal)
ax.text(11.7,6.14,r'$B_{1_L}$',ha='center',fontsize=18,color=purple)
for i in range(5):
    for j in range(5):
        yes=j>=i and (j-i)%2==0
        ax.text(10.1+.7*j,5.65-.34*i,'1' if yes else '0',ha='center',fontsize=16,color=purple if yes else '#8794a1')
ax.text(11.5,3.97,r'$1=1_{K_L},\quad0=0_{K_L}$',ha='center',fontsize=13,color=purple)
panel(.8,2.7)
ax.text(.4,3.1,'The actual theta family already lies in this fixed image',fontsize=19,fontweight='bold',color=ink)
ax.text(.4,2.48,r'$\mathbf{a}(t)=((h_0(t),1_L),\tau,(h_1(t),1_L),\tau,(h_2(t),1_L),\ldots)$',fontsize=19,color=blue)
ax.text(.4,1.84,r'$(-1)^jh_j(t)>0\quad(t\in\mathbb{R}),\qquad U_{(0,\lambda)}\mathbf{a}(t)=\mathbf{a}(t)\quad(\lambda\in L)$',fontsize=19,color=teal)
ax.text(.4,1.22,'Every label is retained. The kernel positivity and convergent heat action prove this identity.',fontsize=14,color=ink)
ax.text(.25,.37,'Here q is the amplitude map. Proofs: THS3, THS9, THS16–25; full independent-label operator: HSL1–14.',fontsize=12,color=muted)
ax.text(.25,.02,'Original heat kernel: Brad Rodgers & Terence Tao, arXiv:1801.05914v5. Full carrier: The Clankers, v11, def:lattice-split.',fontsize=11,color=muted)
for ext in ('pdf','svg','png'):
    fig.savefig(R/f'SUPPORTED_HEAT_ZERO.{ext}',dpi=170,facecolor='white')
plt.close(fig)
print('Rendered the exact supported heat-operator figure.')
