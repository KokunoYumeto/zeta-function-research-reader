"""Reproducible exact map and coefficient diagram for NI/FJ."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
B=Path(__file__).resolve().parent
fig,axs=plt.subplots(2,1,figsize=(12,12),gridspec_kw={'height_ratios':[1,1.05]})
fig.patch.set_facecolor('white')
for ax in axs:ax.set_xlim(0,12);ax.set_ylim(0,6);ax.axis('off')
def box(ax,x,y,w,h,title,body,color):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.08',facecolor=color,edgecolor='#35516b',linewidth=1.3))
    ax.text(x+w/2,y+h-.25,title,ha='center',va='top',fontsize=13,weight='bold')
    ax.text(x+w/2,y+h/2-.14,body,ha='center',va='center',fontsize=12,linespacing=1.6)
ax=axs[0]
ax.text(6,5.9,'Exact finite jets and every remaining zero',ha='center',va='top',fontsize=17,weight='bold')
box(ax,.35,3.75,11.3,1.2,'Original rational tests',r'$\mathcal{R}_\sigma=\mathrm{span}\{(s-\sigma)^{-j-1}:j\geq0\},\quad \sigma>1$','#eaf1f7')
box(ax,.35,1.25,5.25,1.55,'Finite jets kept exact',r'$j_SF\in\bigoplus_{a\in S}\mathbb{C}[v_a]/(v_a^{r_a})$'+'\n'+r'$\ker j_S=W\mathcal{R}_\sigma$','#e2f0ed')
box(ax,6.4,1.25,5.25,1.55,'Exterior values retained',r'$F|_{\mathcal{Z}\setminus S}\in\ell^2(\mathcal{Z}\setminus S,m)$'+'\n'+r'$Jh(\rho)=h(1-\overline{\rho})$','#f5e9e5')
for xx in [3,9]:ax.annotate('',xy=(xx,2.85),xytext=(6,3.65),arrowprops={'arrowstyle':'->','lw':1.8,'color':'#35516b'})
ax.text(6,3.15,'Joint image dense; arbitrary prescribed finite jets reached exactly',ha='center',fontsize=10.7,bbox={'facecolor':'white','edgecolor':'none','pad':3})
ax.text(6,.64,r'$\mathrm{ind}_{-}Q_H=\kappa_{\mathrm{ext}}+\mathrm{ind}_{-}(B_S+H)$',ha='center',fontsize=17)
ax.text(6,.12,'FJ1–FJ13: each exterior reflected pair contributes one negative direction, if it exists.',ha='center',fontsize=11)
ax=axs[1]
ax.text(6,5.95,'The same test in the first heat polynomial and the actual trace',ha='center',va='top',fontsize=16,weight='bold')
ax.text(6,5.2,r'$s-\rho=i\xi/2,\quad b_m=m(m-1)/2,\quad (f_0,f_1,f_2)=(tb_m/m,0,1)$',ha='center',fontsize=14)
box(ax,.35,2.8,5.25,1.65,'First Taylor polynomial',r'$-\frac{m(m-1)^2}{4}\,t^2$'+'\n'+r'Negative for $m\geq2$, $t\ne0$','#f8e6e3')
box(ax,6.4,2.8,5.25,1.65,'Next actual heat contribution',r'$+\frac{m(m-1)(2m-3)}{4}\,t^2$'+'\n'+r'$p_4/16$ in the original coordinate','#e1efe5')
for xx in [3,9]:ax.annotate('',xy=(6,1.95),xytext=(xx,2.65),arrowprops={'arrowstyle':'->','lw':1.8,'color':'#35516b'})
ax.text(6,1.5,r'Actual local trace: $\frac{m(m-1)(m-2)}{4}\,t^2+O(t^3)$',ha='center',fontsize=17)
ax.text(6,.82,'At m = 2 the displayed terms cancel. At m > 2 their sum is positive.',ha='center',fontsize=12)
ax.text(6,.28,'FJ15–FJ22: actual local cluster; the full arithmetic complement remains in FJ23–FJ25.',ha='center',fontsize=10.8)
fig.subplots_adjust(hspace=.12,left=.04,right=.96,top=.98,bottom=.035)
for ext in ['png','svg']:fig.savefig(B/f'finite_jet_exterior_heat.{ext}',dpi=170,facecolor='white')
print('Saved exact FJ diagram.')
