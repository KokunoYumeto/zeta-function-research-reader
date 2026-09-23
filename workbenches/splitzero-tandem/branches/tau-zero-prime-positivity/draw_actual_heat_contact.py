from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

O=Path(__file__).resolve().parent
fig=plt.figure(figsize=(15,11.2),facecolor='white')
ax=fig.add_axes([0,0,1,1]);ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis('off')
ink='#172e40';blue='#185e99';purple='#78377e';green='#176853'
def text(x,y,s,size=14,color=ink,ha='left',va='center'):
    ax.text(x,y,s,fontsize=size,color=color,ha=ha,va=va,linespacing=1.5)
def box(x,y,w,h,fc):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.012',facecolor=fc,edgecolor='#b7c6d0',lw=1))
def arrow(x1,y1,x2,y2):
    ax.annotate('',xy=(x2,y2),xytext=(x1,y1),arrowprops={'arrowstyle':'->','color':ink,'lw':1.7})
text(.04,.963,'Actual heat, the full arithmetic receiver, and the contact cancellation',21)
text(.04,.925,r'Original time and coordinate: $g_t(s)=16H_t(-2i(s-\frac{1}{2}))$,  $\partial_tg_t=\frac{1}{4}g_t^{\prime\prime}$',16)
box(.04,.69,.43,.185,'#edf5fa');box(.53,.69,.43,.185,'#eef7f3')
text(.065,.845,'Whole zero trace, every multiplicity',16,blue)
text(.065,.792,r'$Z_t(M_h)=\sum_\rho m_{\rho,t}M_h(\rho_t)$',20)
text(.065,.731,r'$t\geq0$: actual $C^\infty$ trace; right derivatives at $0$',14)
text(.555,.845,'Complete causal arithmetic distribution',16,green)
text(.555,.792,r'$\mathfrak{J}=\frac{1}{4}\{v^2\ell-v(\ell*\ell)\},\quad\ell=\alpha-\pi$',19)
text(.555,.731,r'$\pi=\sum_{n\geq2}\Lambda(n)n^{-1/2}\delta_{\log n}$',17)
arrow(.473,.792,.518,.792)
text(.5,.655,r'$\partial_t Z_t(M_h)|_{0+}=\langle\mathfrak{J},h(v)+h(-v)\rangle$',20,ha='center')
text(.5,.616,'The subtraction in alpha retains both endpoints and every Gamma constant.  [CH4–25; RT1–16]',12,ha='center')
box(.04,.333,.92,.236,'#f7f3f8')
text(.065,.535,r'At $\rho$:  $g_0(s)=(s-\rho)^m u(s)$,  $b=u^\prime(\rho)/u(\rho)$,  $x=w-(\rho-\frac{1}{2})$',16)
text(.065,.477,'Actual first variation',14,blue)
text(.065,.422,r'$\operatorname{PP}\left[H(\rho+x)\left(-\frac{m(m-1)}{2x^3}-\frac{mb}{2x^2}\right)\right]$',20)
text(.585,.477,'After adding the contact contribution',14,purple)
text(.585,.422,r'$\operatorname{PP}\left[-\frac{mb\,H(\rho+x)}{2x^2}\right]$',20)
arrow(.483,.421,.56,.421)
text(.065,.362,'Contact removes the splitting term; the full analytic-unit term remains.  [GC12–21; RT25, 28–29]',13)
text(.04,.285,r'One fixed compact test: $r=1/64$,  $F(s)=s(s-1)G_r(s-\frac{1}{2})$,  $H(s)=F(s)^2$',16)
text(.04,.245,r'$F(\rho)\neq0$ at every off-critical zero. Its actual global heat derivative receiver detects:',14)
box(.04,.111,.28,.099,'#edf5fa');box(.36,.111,.28,.099,'#f7f3f8');box(.68,.111,.28,.099,'#eef7f3')
text(.18,.174,r'$m\geq2$: triple pole at order $1$',14,ha='center')
text(.18,.137,'Every multiple off-critical zero',11,ha='center')
text(.5,.174,r'$m=1,\ b\neq0$: double pole at order $1$',13,ha='center')
text(.5,.137,'Full unit drift retained',11,ha='center')
text(.82,.174,r'$m=1,\ b=0$: finite order $n_\rho>1$',13,ha='center')
text(.82,.137,'Nonzero double pole at that order',11,ha='center')
text(.04,.073,'Exact meromorphic maps: RT20–27. Pole detection does not assign a sign to the complete Weil form.',12)
text(.04,.035,r'All maps retain the supported carrier: $(0,1_L)=e\neq\tau=(0,0_L)$.  [CH28–30; GC31–31a; RT30]',12)
fig.savefig(O/'actual_heat_contact.png',dpi=160,bbox_inches='tight')
fig.savefig(O/'actual_heat_contact.svg',bbox_inches='tight')
print(O/'actual_heat_contact.png')
