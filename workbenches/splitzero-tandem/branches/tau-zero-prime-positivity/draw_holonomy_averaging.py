"""Reproducible illustration of HWA10–13 and HWA28–32."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

B=Path(__file__).resolve().parent
O=B/'figures';O.mkdir(exist_ok=True)
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False,'svg.fonttype':'none'})
fig,(ax,bx)=plt.subplots(1,2,figsize=(13.8,5.3),gridspec_kw={'width_ratios':[1,1.18]})
x=np.arange(8)
old=np.array([1,1,1,-1,1,1,-1,-1])
new=np.array([1,1/3,1/3,1/3,0,0,0,0])
ax.axhline(0,color='#888888',lw=.9)
ax.axvspan(-.5,.5,color='#efdfc4',alpha=.45)
ax.axvspan(.5,3.5,color='#d4e8f0',alpha=.45)
ax.axvspan(3.5,7.5,color='#eee4f0',alpha=.6)
ax.plot(x,old,'o',color='#a63c2f',ms=8,label='Original native trace')
ax.plot(x,new,'s',color='#16745d',ms=7,label='Average over 192 holonomy actions')
for j in range(8):
    if old[j]!=new[j]:ax.annotate('',xy=(x[j],new[j]),xytext=(x[j],old[j]),arrowprops={'arrowstyle':'->','color':'#66717a','lw':1})
ax.set(xticks=[0,2,5.5],xticklabels=['Constant\n1 dimension','Even, sum zero\n3 dimensions','Sign-odd\n4 dimensions'],yticks=[-1,0,1/3,1],yticklabels=['−1','0','1/3','1'],ylim=(-1.28,1.26),xlim=(-.5,7.5),ylabel='Exact eigenvalue')
ax.set_title('A. Full native form and its holonomy average\nHWA10–13; the odd radical is retained',loc='left',fontsize=12)
ax.legend(loc='lower left',fontsize=9,frameon=False)
t=np.linspace(0,2*np.pi,600)
pe=np.sin(2*t)
av=.5+np.sin(2*t)/6
change=.5-5*np.sin(2*t)/6
bx.axhline(0,color='#888888',lw=.9)
bx.plot(t,pe,color='#a63c2f',lw=2,label=r'$P_e=2\mathrm{Re}(\overline{A}B)$')
bx.plot(t,av,color='#16745d',lw=2,label=r'$\overline{P}_e=\frac{1}{2}(|A|^2+|B|^2)+\frac{1}{3}\mathrm{Re}(\overline{A}B)$')
bx.plot(t,change,color='#735b99',lw=1.7,ls='--',label=r'$K_e=\overline{P}_e-P_e$')
bx.set(xticks=[0,np.pi/2,np.pi,3*np.pi/2,2*np.pi],xticklabels=['0',r'$\pi/2$',r'$\pi$',r'$3\pi/2$',r'$2\pi$'],xlabel=r'Real unit-circle slice: $A=\cos\theta,\ B=\sin\theta$',ylabel='Exact endpoint quadratic value',ylim=(-1.15,1.53))
bx.set_title('B. Actual supported-zero endpoint comparison\nHWA28–32; every displayed pair has an admissible test',loc='left',fontsize=12)
bx.legend(loc='upper right',fontsize=8.5,frameon=False)
fig.suptitle('Holonomy gives a positive average and an explicit nonzero change',fontsize=16,y=1.01)
fig.text(.05,-.015,'Native trace: (5 positive, 3 negative). Average: (4 positive, 4 radical). The complete integrated Weil identity must retain the term −Kₑ.',fontsize=10)
fig.tight_layout()
for ext in ['png','svg']:
    fig.savefig(O/f'31_holonomy_endpoint_average.{ext}',dpi=180,bbox_inches='tight')
plt.close(fig)
print('Rendered figure31: exact native spectrum and actual endpoint comparison.')
