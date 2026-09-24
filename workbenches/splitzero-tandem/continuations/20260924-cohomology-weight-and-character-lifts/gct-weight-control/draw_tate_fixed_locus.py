"""Illustrate the proved Tate fixed locus; p=3 is a geometric drawing choice."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

root=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'mathtext.fontset':'dejavusans'})
fig,axes=plt.subplots(1,2,figsize=(13.5,7.4),gridspec_kw={'width_ratios':[1,1.16]})
fig.subplots_adjust(left=.065,right=.975,bottom=.24,top=.78,wspace=.30)
fig.suptitle('The sign-adjusted involution on the paper’s Tate curve',fontsize=19,y=.965)
fig.text(.5,.9,r'$E_p=\mathbb{C}^{\times}/p^{\mathbb{Z}},\quad \kappa[z]=[1/\bar z],\quad \sigma[z]=[-1/\bar z]$',ha='center',fontsize=17)
t=np.linspace(0,2*np.pi,721);p=3
ax=axes[0]
for radius,color,label,style in [(1,'#156e84',r'$|z|=1$  even degree','-'),
                               (np.sqrt(p),'#b85721',r'$|z|=\sqrt{p}$  odd degree','-'),
                               (p,'#156e84',r'$|z|=p\sim |z|=1$','--')]:
    ax.plot(radius*np.cos(t),radius*np.sin(t),color=color,ls=style,lw=2.6,label=label)
ax.set_aspect('equal');ax.set_xlim(-3.4,3.4);ax.set_ylim(-3.4,3.4)
ax.set_xticks([]);ax.set_yticks([])
ax.set_title('Annulus representatives (drawing: p = 3)',fontsize=13,pad=14)
ax.legend(loc='lower center',bbox_to_anchor=(.5,-.23),frameon=False,fontsize=11)
for sp in ax.spines.values(): sp.set_visible(False)
ax.annotate('',xy=(p,0),xytext=(1,0),arrowprops={'arrowstyle':'<->','color':'#555','lw':1.2})
ax.text(2,-.4,'deck factor p',ha='center',fontsize=10)

ax=axes[1]
ax.set_xlim(-.06,1.06);ax.set_ylim(-.08,1.08)
ax.set_xticks([0,.5,1],[r'$0$',r'$1/2$',r'$1\sim0$'])
ax.set_yticks([0,.5,1],[r'$0$',r'$1/2$',r'$1\sim0$'])
ax.set_xlabel(r'$u=\log|z|/\log p\quad (\mathrm{mod}\ 1)$',labelpad=10)
ax.set_ylabel(r'$v=\arg(z)/(2\pi)\quad (\mathrm{mod}\ 1)$')
ax.set_title('Exact maps on the quotient coordinates',fontsize=13,pad=14)
ax.axvline(0,color='#156e84',lw=3);ax.axvline(1,color='#156e84',lw=3,ls='--')
ax.axvline(.5,color='#b85721',lw=3)
ax.axhline(0,color='#999',lw=1,ls=':');ax.axhline(1,color='#999',lw=1,ls=':')
x,y=.21,.24
ax.scatter([x,1-x,1-x],[y,y,y+.5],color=['#333','#9b3e80','#276530'],s=45,zorder=4)
ax.annotate('',xy=(1-x,y),xytext=(x,y),arrowprops={'arrowstyle':'->','color':'#9b3e80','lw':1.8})
ax.annotate('',xy=(1-x,y+.5),xytext=(x,y),arrowprops={'arrowstyle':'->','color':'#276530','lw':1.8,'connectionstyle':'arc3,rad=-.22'})
ax.text(.47,.13,r'$\kappa:(u,v)\mapsto(-u,v)$',color='#9b3e80',ha='center',fontsize=11)
ax.text(.13,.87,r'$\sigma:(u,v)\mapsto(-u,v+1/2)$',color='#276530',fontsize=11)
ax.text(.075,.32,'sample point',fontsize=10)
ax.text(.54,.96,'fixed circle',color='#b85721',rotation=90,fontsize=11,va='top')
fig.text(.065,.11,'Proof: C4–C5 in TAU_TWISTOR_TATE_AND_WEIL.md.  The even/odd labels are the parity of the lifted integer n in |z|² = pⁿ.',fontsize=10)
fig.text(.065,.074,'For z = pˢ with 0 < Re(s) < 1, κ-fixedness forces n = 1 and hence Re(s) = 1/2.  This does not assert fixedness of all zeta zeros.',fontsize=10)
fig.text(.065,.038,'Sources: Connes–Consani, arXiv:2609.00299v1 (twistor sign) and 2606.06604v1 (Tate quotient).  No metric at τ is assumed.',fontsize=10)
fig.savefig(root/'tate_fixed_locus.png',dpi=180)
fig.savefig(root/'tate_fixed_locus.svg')
plt.close(fig)
