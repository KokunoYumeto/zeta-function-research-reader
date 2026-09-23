"""Reproduce the exact interval geometry and proved bounds of FC/FW."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
P=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'axes.titlesize':15})
fig=plt.figure(figsize=(15,10.2),layout='constrained')
gs=GridSpec(3,2,figure=fig,height_ratios=[1,0.60,0.85])
T=19/25; r=1/64; L=np.log(2); beta=L/np.sqrt(2); delta=2*L/T
ax=fig.add_subplot(gs[0,0]);x=np.linspace(-.994,.994,1400)
ax.plot(x,-.5*np.log1p(-x*x),color='#216782',lw=2.5,label=r'$v(x)=-\frac{1}{2}\log(1-x^2)$')
ax.axhline(beta,color='#c05640',ls='--',label=r'$\beta=\log 2/\sqrt{2}$')
for lo,hi in [(-1,1-delta),(-1+delta,1)]:ax.axvspan(lo,hi,color='#deb356',alpha=.3)
ax.set(xlim=(-1,1),ylim=(0,2.45),xlabel=r'$x=2(t-c)/T$',ylabel='Exact potential',title='Prime 2 is controlled by the boundary potential')
ax.text(0,1.68,r'$v(x)>\frac{1}{2}>\beta$'+'\non both shaded overlap strips',ha='center',fontsize=13)
ax.legend(loc='lower center',fontsize=10);ax.grid(alpha=.15)
ax=fig.add_subplot(gs[0,1]);n=np.arange(9);hn=np.array([sum(1/j for j in range(1,i+1)) for i in n])
ax.bar(n,hn,color=['#c05640','#c05640']+['#216782']*7,width=.62)
ax.axhline(1.5,color='#555',ls=':');ax.set(xticks=n,xlabel='Legendre degree n',ylabel=r'$H_n$',title='Both original moments control the two lowest modes')
ax.text(4.9,.67,r'$\mathcal{L}P_n=H_n P_n$'+'\n'+r'$\int f(x)e^{\pm Tx/4}\,dx=0$',ha='center',fontsize=14)
ax.grid(axis='y',alpha=.15)
ax=fig.add_subplot(gs[1,:]);ax.axis('off')
ax.text(.5,.84,r'$Q(F)>c_*\|F\|_2^2,\qquad c_*=\frac{11509}{600000}>\frac{1}{64},\qquad T=\frac{19}{25}$',ha='center',fontsize=20)
ax.text(.5,.35,r'$[K(a_i-a_j)]-c_*[h_r(a_i-a_j)]\succ0\quad (\mathrm{distinct}\ a_i,\ \max a_i-\min a_i\leq\frac{583}{800})$',ha='center',fontsize=17)
ax.text(.5,.02,'Full Weil form, both global endpoint moments, original radius r = 1/64.  Proofs: FC34, FW7.',ha='center',fontsize=11)
ax=fig.add_subplot(gs[2,:]);A=583/800;A3=np.log(3)-2*r
ax.axhspan(.80,1.15,xmin=0,xmax=1,color='#f4f5f6')
ax.plot([0,A],[1,1],color='#216782',lw=11,solid_capstyle='butt')
ax.plot([A,A3],[1,1],color='#2e8662',lw=11,solid_capstyle='butt')
ax.axvspan(L-2*r,L+2*r,color='#e1ad52',alpha=.6,ymin=.18,ymax=.79)
ax.axvspan(np.log(3)-2*r,np.log(3)+2*r,color='#eee',alpha=.75,ymin=.18,ymax=.79)
for p in [2*r,L-2*r,L,L+2*r,A,A3]:ax.plot([p,p],[.9,1.11],color='#333',lw=1)
ax.text(.32,1.23,'Full local matrix bound',ha='center',color='#216782')
ax.text(.9,1.23,r'Prime gap: $K(a)=-R_r(a)$',ha='center',color='#2e8662')
ax.text(L,.70,'Entire prime-2 window',ha='center',fontsize=11)
ax.text(A,.45,r'$A_*=583/800$',ha='center',fontsize=11)
ax.text(A3,.25,r'$\log3-1/32$',ha='center',fontsize=11)
ax.text(.27,.31,r'$|K(a)|<q-c_*N_r$ for $1/32\leq a\leq\log3-1/32$',ha='center',fontsize=12)
ax.set(xlim=(0,1.16),ylim=(.13,1.42),yticks=[],xlabel='Original translation a',title='The two-test margin continues to the next prime window (FW19–21)')
ax.spines[['top','right','left']].set_visible(False)
fig.suptitle('First-prime positivity with every interaction retained',fontsize=22)
for ext in ['png','svg']:fig.savefig(P/f'first_prime_bound.{ext}',dpi=160)
print('Rendered first_prime_bound.png and .svg')
