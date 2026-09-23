"""Reproducible exact-bound and exact-map figures for OZG and OZR."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

root=Path(__file__).resolve().parent
if (root/'receivers').is_dir():root=root/'receivers'
plt.rcParams.update({'font.size':12,'svg.fonttype':'none'})
fig,ax=plt.subplots(figsize=(11,5.6),layout='constrained')
m=np.arange(1,33,dtype=float);R=2*m+.5
lower=np.log(4*m*m*(2*m+1)**2)+(1/8)*R**2-R
upper=lower+R/32
ax.fill_between(m,lower,upper,color='#c65c44',alpha=.42,label='Proved enclosure for $\\log d_m$')
ax.plot(m,lower,color='#8f362b',lw=1.8)
ax.plot(m,upper,color='#8f362b',lw=1.8)
ax.axhline(0,color='#586574',lw=.8)
ax.set(xlabel='Trivial-zero index $m$',ylabel='$\\log d_m(1/8,1)$',xlim=(1,32))
ax.set_title('Positive Gaussian test time: the retained trivial-zero terms grow',pad=14,weight='bold')
ax.text(.04,.93,r'$r=1/64,\quad\epsilon=1/8,\quad a=1,\quad R_m=2m+1/2$',transform=ax.transAxes,va='top')
ax.text(.04,.83,r'$d_m=4m^2(2m+1)^2e^{\epsilon R_m^2-aR_m}G_r(R_m)^2$',transform=ax.transAxes,va='top')
ax.text(.04,.73,r'$1\leq G_r(R)\leq e^{rR}$',transform=ax.transAxes,va='top')
ax.text(.04,.63,'The band uses exact upper and lower bounds.\nNo infinite-product truncation is used.',transform=ax.transAxes,va='top',fontsize=11)
ax.grid(alpha=.15);ax.legend(loc='lower right')
fig.text(.5,-.025,'OZG11–17: log-growth limit = epsilon; the cutoff sum has the same leading growth.',ha='center',fontsize=10)
for ext in ['png','svg']:fig.savefig(root/f'gaussian_trivial_zero_growth.{ext}',dpi=190,bbox_inches='tight')
plt.close(fig)

fig,ax=plt.subplots(figsize=(11,6.1));ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')
ax.text(.5,.96,'Original zeta: invertible transport and the full trace return',ha='center',weight='bold',fontsize=17)
box={'boxstyle':'round,pad=.6','facecolor':'#edf3f7','edgecolor':'#597b96'}
ax.text(.04,.78,r'$f(z)$',ha='left',va='center',bbox=box,fontsize=18)
ax.text(.48,.78,r'$\widetilde f(s)=e^{\chi(s)}\,\dfrac{C(\varphi(s))}{C(s)}f(\varphi(s))$',ha='left',va='center',bbox=box,fontsize=16)
ax.annotate('',xy=(.46,.8),xytext=(.16,.8),arrowprops={'arrowstyle':'->','lw':1.8,'color':'#285e80'})
ax.annotate('',xy=(.16,.72),xytext=(.46,.72),arrowprops={'arrowstyle':'->','lw':1.8,'color':'#285e80'})
ax.text(.30,.86,'OZR4–6',ha='center',fontsize=11)
ax.text(.30,.65,'explicit inverse',ha='center',fontsize=11)
ax.text(.5,.53,r'$C(s)=\frac{1}{2}s(s-1)\pi^{-s/2}\Gamma(s/2)$',ha='center',fontsize=17)
ax.text(.5,.39,r'$\widetilde Q_{\rm div}=\widetilde R^{\rm fp}+E_C^{\rm fp}$',ha='center',fontsize=18)
ax.text(.5,.28,r'$\widetilde Q_{\log}=\widetilde R^{\rm fp}+E_C^{\rm fp}+2a$',ha='center',fontsize=18)
ax.text(.5,.18,'Cauchy tests: signed original divisor + fixed-factor divisor + infinity term',ha='center',fontsize=12)
ax.text(.5,.07,r'Every local jet is retained; $e\neq\tau$.  OZR7–12, OZR19–36.',ha='center',fontsize=12)
fig.tight_layout()
for ext in ['png','svg']:fig.savefig(root/f'original_zeta_regular_transport.{ext}',dpi=190,bbox_inches='tight')
plt.close(fig)
print('Two figures rendered in PNG and SVG.')
