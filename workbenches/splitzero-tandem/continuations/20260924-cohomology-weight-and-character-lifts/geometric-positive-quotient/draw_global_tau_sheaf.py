"""Current multiplicative maps R3-R5; no source addition on tau is used."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
ROOT=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12})
fig,ax=plt.subplots(figsize=(13,9))
fig.patch.set_facecolor('#f7f9fc')
ax.set(xlim=(0,13),ylim=(0,9));ax.axis('off')
ink='#172a43';blue='#156f95';green='#28734e'
def box(x,y,w,h,colour):
 ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.06,rounding_size=.10',fc='white',ec=colour,lw=1.5))
def arrow(start,end,colour):
 ax.annotate('',xy=end,xytext=start,arrowprops={'arrowstyle':'-|>','lw':1.6,'color':colour})
ax.text(.5,8.53,'Global presence and the integer complement',fontsize=23,weight='bold',color=ink)
ax.text(.5,8.08,'Multiplicative maps only. No value of tau + tau is defined or used.',color=ink)
box(4.12,5.85,4.78,1.62,blue)
ax.text(6.51,6.96,r'$M=\mathbb{Z}\sqcup\{\tau\}$',fontsize=25,ha='center',color=blue)
ax.text(6.51,6.41,r'Global unit: $\tau$; integer-local unit: $1$.',ha='center',fontsize=11.5,color=ink)
box(.62,2.88,4.89,1.69,green)
box(7.48,2.88,4.89,1.69,blue)
ax.text(3.06,4.04,r'$B_\times=\{0,\tau\}$',fontsize=24,ha='center',color=green)
ax.text(3.06,3.49,r'$\chi(\tau)=\tau,\qquad\chi(n)=0$',fontsize=18,ha='center',color=green)
ax.text(9.92,4.04,r'$(\mathbb{Z},\cdot,1)$',fontsize=24,ha='center',color=blue)
ax.text(9.92,3.49,r'$r(\tau)=1,\qquad r(n)=n$',fontsize=18,ha='center',color=blue)
arrow((5.14,5.80),(3.42,4.65),green)
arrow((7.88,5.80),(9.60,4.65),blue)
ax.text(.92,5.28,'Only tau maps to tau',fontsize=12,color=green)
ax.text(9.60,5.28,'Keep every integer',fontsize=12,color=blue)
ax.text(.69,2.33,r'$\chi^{-1}(\tau)=\{\tau\},\qquad\chi^{-1}(0)=\mathbb{Z}$',fontsize=18,color=green)
ax.text(7.51,2.33,r'$r^{-1}(1)=\{\tau,1\}$',fontsize=18,color=blue)
ax.text(.62,1.60,'Both maps together give an exact return:',fontsize=14,weight='bold',color=ink)
ax.text(.62,1.08,r'$\tau\longmapsto(\tau,1),\qquad n\longmapsto(0,n)\quad(n\in\mathbb{Z})$',fontsize=23,color=ink)
ax.text(.62,.58,'Apply these maps pointwise to locally constant sections: tau is the unique global unit section.',fontsize=11.5,color=ink)
ax.text(.62,.18,'Complete proofs: ADDITION_RETRACTION_AND_MULTIPLICATIVE_CORE.md, R3–R5. The integer subsheaf is the zero fibre of chi.',fontsize=9,color=ink)
fig.savefig(ROOT/'global_tau_sheaf.png',dpi=160,bbox_inches='tight')
fig.savefig(ROOT/'global_tau_sheaf.svg',bbox_inches='tight')
plt.close(fig)
