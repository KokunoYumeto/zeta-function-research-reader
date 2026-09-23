from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

out=Path(__file__).parent
fig=plt.figure(figsize=(11,6.3),facecolor='white')
ax=fig.add_axes([.035,.43,.93,.52]);ax.axis('off')
ax.set_xlim(-.02,1.02)
def box(x,y,w,h,text,color):
    p=FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.012',facecolor=color,edgecolor='#263747',lw=1.2)
    ax.add_patch(p);ax.text(x+w/2,y+h/2,text,ha='center',va='center',fontsize=11,linespacing=1.45)
box(.01,.19,.30,.68,'Original source at t = 1/32\n'+r'$h(x)=e^{-8x^2}H_{1/32}(x)\cos(16x)$'+'\n'+r'$f=(D_x^2-1/4)h$'+'\nFull theta density retained','#edf3fb')
box(.41,.59,.56,.28,'Prime-boundary receiver (AP27)\n'+r'$(-J_2-\frac{1089}{4}C,\;-\frac{\sqrt{\pi/32}}{32}e^{-8})$'+'\nBoth coordinates are negative','#fff2e4')
box(.41,.12,.56,.29,'Arithmetic receiver (AP4–6, AP26)\n'+r'$K=A_\infty(k)-2\sum_{n\geq2}\Lambda(n)n^{-1/2}k(\log n)$'+'\n'+r'$k=f*f$'+'; full Gamma term and every prime power','#eaf7ef')
for y in [.74,.26]:
    ax.add_patch(FancyArrowPatch((.32,.53),(.395,y),arrowstyle='-|>',mutation_scale=16,lw=1.4,color='#263747'))
ax.text(.015,.01,'The two arrows are different proved maps of the same source. No support label is removed.',fontsize=10)
bx=fig.add_axes([.12,.105,.79,.23])
bx.axvline(0,color='#333333',lw=1)
bx.plot([50,64],[.55,.55],lw=13,color='#2c7a51',solid_capstyle='butt')
bx.plot([56.95,56.97],[.55,.55],'o',ms=7,color='#172e44')
bx.text(57,.89,r'Full original value: $50<K<64$',ha='center',fontsize=12)
bx.text(31,.06,r'$56.95<A_\infty(k_0)-P_{0,64}<56.97$'+'\n'+r'Full residual: $E_\Gamma<6.1$, $E_P<0.45$; tails retained',ha='center',fontsize=10)
bx.set_xlim(-5,72);bx.set_ylim(-.15,1.1);bx.set_yticks([]);bx.set_xticks([0,25,50,64])
bx.spines[['left','right','top']].set_visible(False)
fig.text(.5,.015,'Exact source and rational enclosure: AP1–28. Human sources: Rodgers–Tao, arXiv:1801.05914v5; Connes, math/9811068v1.',ha='center',fontsize=8)
fig.savefig(out/'PAIRING_MAP.pdf',bbox_inches='tight')
fig.savefig(out/'PAIRING_MAP.png',dpi=180,bbox_inches='tight')
