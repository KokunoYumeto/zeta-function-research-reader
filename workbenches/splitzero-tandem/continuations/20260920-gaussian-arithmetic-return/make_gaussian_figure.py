from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.special import ellipk,ellipe
from scipy.optimize import brentq
from numpy.polynomial.legendre import leggauss
P=Path(__file__).parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'axes.spines.top':False,'axes.spines.right':False})
r=brentq(lambda r:r*ellipk(1-r*r)/ellipe(1-r*r)-.5,.15,.17,xtol=1e-15)
u=2/ellipk(1-r*r);v=4/ellipe(1-r*r)
gn,gw=leggauss(256);z=(gn+1)/2;ww=gw/2
w=z/(1-z); jac=1/(1-z)**2
def rho(x):
 x=np.asarray(x);out=np.zeros_like(x)
 mask=(x>u*u)&(x<v*v);t=x[mask]
 if len(t):
  integral=np.sum(ww[None,:]*jac[None,:]*np.sqrt(w)[None,:]/((t[:,None]+w[None,:])*np.sqrt((u*u+w)*(v*v+w))[None,:]),axis=1)
  out[mask]=np.sqrt((v*v-t)*(t-u*u))*integral/(4*np.pi*t)
 return out
axis=np.concatenate([np.linspace(-4,-.012,1100),[np.nan],np.linspace(.012,4,1100)])
full=np.arccosh(4/np.abs(axis))/(2*np.pi)
relation=np.abs(axis)*rho(axis*axis)
retained=full-relation
fig=plt.figure(figsize=(9.2,10.4),layout='constrained')
gs=fig.add_gridspec(3,1,height_ratios=[1.05,1.9,1.1])
ax=fig.add_subplot(gs[0]);ax.axis('off');ax.set_xlim(0,1);ax.set_ylim(0,1)
ax.text(0,1,'The Gaussian action in the original quotient',fontsize=17,weight='bold',va='top')
box=dict(boxstyle='round,pad=.55',facecolor='#edf4f7',edgecolor='#65869b')
ax.text(.25,.65,r'Full source: $\mathcal{P}_{\leq N}$'+'\n'+r'original metric $L^2(\mu_k)$',ha='center',va='center',bbox=box)
ax.annotate('',xy=(.68,.65),xytext=(.48,.65),arrowprops={'arrowstyle':'->','lw':1.8})
ax.text(.59,.79,'NG18–20',ha='center',fontsize=10)
ax.text(.83,.65,r'$\mathcal{V}_N\;\perp\;Q_k\mathcal{P}_{<d}$'+'\n'+r'$C_N$       relation Jacobi',ha='center',va='center',bbox=box)
ax.text(.03,.27,r'Gamma → arithmetic: the characteristic-value error is $O_h(k+\log q)=o(q)$ (NG6).',fontsize=11)
ax.text(.03,.09,'The complete $Q_k$ remains. The only coupling has rank ≤ 1 (NG19).',fontsize=11)
ax=fig.add_subplot(gs[1]);ax.plot(axis,full,color='#8195a3',ls='--',lw=1.6,label='Full source: $h_0(z/2)$, mass 2')
ax.plot(axis,relation,color='#bf7448',lw=1.6,label=r'Relation: $|z|\,\rho_1(z^2)$, mass 1')
ax.plot(axis,retained,color='#16587c',lw=2.5,label=r'Retained: $d\nu_1/dz$, mass 1')
ax.fill_between(axis,0,retained,color='#16587c',alpha=.11)
ax.set(xlabel='$z=y/q$ (spectral coordinate)',ylabel='Density',xlim=(-4.1,4.1),ylim=(0,1.1))
ax.set_title('The actual relation subtraction leaves a positive probability (NG20; GM17)',fontsize=12)
ax.legend(loc='upper right',fontsize=9,framealpha=.95)
ax.annotate('Integrable divergence at 0',xy=(-.025,1.02),xytext=(-3.9,.94),arrowprops={'arrowstyle':'->'},fontsize=9)
ax.text(.03,.06,r'Endpoints: $u\approx0.618688$, $v\approx3.864343$'+'\nCurve samples use the explicit integral; the sign proof is exact.',transform=ax.transAxes,fontsize=9,bbox=dict(facecolor='white',alpha=.88,edgecolor='none'))
ax=fig.add_subplot(gs[2]);ax.axis('off');ax.set_xlim(0,1);ax.set_ylim(0,1)
ax.text(0,.98,'Four original cutoffs, with their original signs',fontsize=13,weight='bold',va='top')
for i,(cut,sign,s) in enumerate([('q-1','+','0'),('q','+','0'),('2q-1','−','1'),('2q','−','1')]):
 ax.text(.14+.235*i,.65,sign+'  $'+cut+'$\n$s='+s+'$',ha='center',va='center',bbox=box,fontsize=13)
ax.text(.5,.29,r'At $t=1/1024$:  $I_0\leq 2/3$,   $I_1\geq (63/64)\,m(1)$,   $m(1)>10249/10000$',ha='center',fontsize=11)
ax.text(.5,.09,'$2(I_0-I_1)<-657061/960000$  (NG27; GM21–25)',ha='center',fontsize=15,color='#16587c',weight='bold')
fig.savefig(P/'GAUSSIAN_NATIVE_MECHANISM.png',dpi=190)
np.savez(P/'GAUSSIAN_FIGURE_SAMPLES.npz',coordinate=axis,full_source=full,relation=relation,retained=retained,u=u,v=v,r=r)
print('Figure written; samples are illustrations of the proved density, not a numerical proof.')
