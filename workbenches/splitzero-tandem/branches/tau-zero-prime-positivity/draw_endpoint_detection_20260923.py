"""Reproducible exact-bound diagram; no sampled zeta zeros."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent
P=B/'receivers' if (B/'receivers').exists() else B
plt.rcParams.update({'font.size':11,'axes.titlesize':13,'figure.facecolor':'white','savefig.facecolor':'white'})
fig,ax=plt.subplots(1,3,figsize=(15.8,5.5),gridspec_kw={'width_ratios':[1,1.1,1.3]})
fig.suptitle('The endpoint-resonant test: all heights, retained time factor, exact global receiver',fontsize=16,y=.99)
a=ax[0];a.axvspan(0,1,color='#d9eef0');a.axvline(0,color='#175d72');a.axvline(1,color='#175d72');a.axvline(.5,color='#b27331',linestyle='--')
a.set_xlim(-.25,1.25);a.set_ylim(-2,2);a.set_xticks([0,.5,1]);a.set_yticks([]);a.set_xlabel(r'$\mathrm{Re}\,s$');a.set_ylabel(r'$\mathrm{Im}\,s$ — every height')
a.set_title('A. No missing zero in the strip')
a.annotate('',xy=(1.16,1.9),xytext=(1.16,-1.9),arrowprops={'arrowstyle':'<->','color':'#175d72'})
a.text(.5,.9,r'$M_{1/32}(s)\ne0$',ha='center',fontsize=14)
a.text(.5,.15,'Uniform in height\nincluding both boundary lines',ha='center',va='center',fontsize=10)
a.text(.5,-.75,r'$F(s)=s(s-1)M_{1/32}(s)$'+'\nOnly endpoint zeros in this strip',ha='center',va='center',fontsize=10)
a.text(.5,-1.55,'Proved: ERD27–28\nNo zeta zeros are plotted',ha='center',fontsize=9)
a=ax[1];tt=np.linspace(.006,.15,240)
logg=.5*np.log10(np.pi*tt)-1/(4*tt*np.log(10))
a.plot(tt,logg,color='#175d72',lw=2.2);a.axvline(1/32,color='#b27331',linestyle='--',lw=1)
a.set_xlabel('Original time $t>0$');a.set_ylabel(r'$\log_{10}[\sqrt{\pi t}\,e^{-1/(4t)}]$')
a.set_title('B. Every time jet vanishes at 0')
a.grid(alpha=.2)
a.text(.024,-7.1,r'$g_t=\sqrt{\pi t}\,e^{-1/(4t)}$'+'\n'+r'$M_t(s)=g_t\,e^{t(s-1/2)^2}$'+'\n'+r'$\qquad{}\times B(t,s-1/2)$',fontsize=10,va='top')
a.text(.024,-14.4,'The plotted factor is retained.\nNonzero at every $t>0$.\nEvery right time derivative\nat 0 is zero.',fontsize=10)
a.text(.024,-17.1,'Exact statement: ERD40–50',fontsize=9)
a=ax[2];a.axis('off');a.set_title('C. The positive test and the remaining bound')
boxes=[
(.88,'Original full source at $t=1/32$\n'+r'$50<q=K(0)<64$'+'\nAP1–28: full arithmetic certificate'),
(.56,r'$K(a)=\sum_\rho m_\rho F(\rho)^2 e^{a(\rho-1/2)}$'+'\nEvery original zero has $F(\\rho)\\ne0$\nFull Gamma and prime terms: EPM28–30'),
(.20,r'$\mathrm{RH}\ \Longleftrightarrow\ |K(a)|\leq q\quad(a\geq0)$'+'\nProved equivalence: EPM45–47\nThe uniform inequality remains unproved')]
for y,label in boxes:
    a.text(.5,y,label,transform=a.transAxes,ha='center',va='center',fontsize=11,bbox={'boxstyle':'round,pad=.65','fc':'#edf4f6','ec':'#175d72'})
for y1,y2 in [(.78,.66),(.44,.32)]:
    a.annotate('',xy=(.5,y2),xytext=(.5,y1),xycoords='axes fraction',arrowprops={'arrowstyle':'->','lw':1.6,'color':'#175d72'})
fig.subplots_adjust(top=.86,bottom=.14,wspace=.38)
for ext in ['png','svg','pdf']:
    fig.savefig(P/('endpoint_resonant_detection.'+ext),dpi=180,bbox_inches='tight')
print(P/'endpoint_resonant_detection.png')
