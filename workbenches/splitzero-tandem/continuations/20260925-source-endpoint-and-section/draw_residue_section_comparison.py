from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch

b=Path(__file__).resolve().parent
fig,ax=plt.subplots(figsize=(15,10.3))
fig.patch.set_facecolor('#f7f8fa');ax.set(xlim=(0,15),ylim=(0,10.3));ax.axis('off')
def box(x,y,w,h,title,rows,color):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.12',fc=color,ec='#567084',lw=1.3))
    ax.text(x+.18,y+h-.25,title,fontsize=13,fontweight='bold',va='top',color='#102c44')
    for dy,txt,size in rows:ax.text(x+.18,y+h-dy,txt,fontsize=size,va='top',color='#102030')
ax.text(.4,9.97,'Same full source; different choices of the observed subspace',fontsize=20,fontweight='bold',color='#102c44')
ax.text(.4,9.48,r'$E=\mathcal{B}+\mathbb{C} h_t=\mathcal{B}+\mathbb{C} j_t,\quad g_t=e^{ts^2},\quad F_0=\frac{s(s-1)}{8}\pi^{-s/2}\Gamma(s/2)\zeta(s)$',fontsize=17)
box(.4,5.92,6.6,2.87,'Original full-zeta section  [NCI; NPE10]',[
(.65,r'$h_t=8g_tF_0/s,\quad \alpha=\widetilde{\Lambda}(h_t)$',17),
(1.24,r'$\delta_{n,t}=8F_0\eta_{n,t}$',17),
(1.82,r'$\overline{\mathrm{span}\{\delta_{n,t}\}}=I$',18),
(2.38,r'Stable part of $\alpha=0$: $\{(\Lambda,0):\Lambda\in I^\perp\}$',13)],'#e4f0e9')
box(7.75,5.92,6.6,2.87,'Gaussian section  [NJS3–8; RSS1]',[
(.65,r'$j_t=g_t/s,\quad \beta=\widetilde{\Lambda}(j_t)$',17),
(1.24,r'$\eta_{n,t}=g_t(n-n^{1-s})/s$',17),
(1.82,r'$\overline{\mathrm{span}\{\eta_{n,t}\}}=\mathcal{B}$',18),
(2.38,r'Stable part of $\beta=0$: $\{0\}$',14)],'#fff0df')
box(.4,3.17,13.95,2.14,'The actual original sector survives as a graph  [NJS1, 6–7; SSR1–6]',[
(.66,r'$k_t=j_t-h_t=\frac{g_t(1-8F_0)}{s},\qquad \beta=\alpha+\Lambda(k_t)$',18),
(1.20,r'$\{(\Lambda,0)_h:\Lambda\in I^\perp\}\ \longleftrightarrow\ \{(\Lambda,\Lambda(k_t))_j:\Lambda\in I^\perp\}$',18),
(1.72,r'$M_t\widetilde{\Lambda}=H_h\Lambda-\overline{\alpha}/(1-z)=H_j\Lambda-\overline{\beta}/(1-z)$',16)],'#e8e8f6')
for x in [3.7,11.05]:
    ax.add_patch(FancyArrowPatch((x,5.79),(x,5.46),arrowstyle='-|>',mutation_scale=16,color='#375c77',lw=1.4))
box(.4,.63,13.95,1.93,'Complete polynomial family in the same E  [RSS2–5]',[
(.65,r'$P(0)=1,\quad h_{P,t}=g_tP/s:\qquad\overline{\mathrm{span}\{P\eta_{n,t}\}}=P\mathcal{B}$',18),
(1.22,r'$P\mathcal{B}=\{F:F^{(j)}(a)=0,\ 0\leq j<\mathrm{ord}_aP\}$; full finite jets and exact quotient maps retained.',14)],'#e6eef5')
ax.text(.42,.14,'Closures are in the original strip topology; all cover degrees n >= 2 are retained. This is a diagram of proved maps.',fontsize=10,color='#334e68')
fig.subplots_adjust(left=.02,right=.985,bottom=.015,top=.995)
fig.savefig(b/'residue_section_comparison.png',dpi=160)
fig.savefig(b/'residue_section_comparison.svg')
plt.close(fig)
