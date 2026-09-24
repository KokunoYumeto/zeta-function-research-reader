"""Reproduce IA2, IA3 and IA8, retaining the source elements and integer carry."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

ROOT = Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12})
fig,ax=plt.subplots(figsize=(14,10.5))
fig.patch.set_facecolor('#f7f9fc')
ax.set(xlim=(0,14),ylim=(0,10.5));ax.axis('off')
ink='#172a43';blue='#156f95';green='#27734c';gray='#65738a'
def box(x,y,w,h,colour):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.07,rounding_size=.10',fc='white',ec=colour,lw=1.4))
ax.text(.5,10.02,'Recovering the layers from the operations',fontsize=23,weight='bold',color=ink)
ax.text(.5,9.57,'The source algebra through the integer layer; tau remains presence without parity.',color=ink)
box(.55,6.73,7.50,2.38,blue)
ax.text(.85,8.67,r'$\{x:x+x=x\}=\{0,\tau\}$',fontsize=23,color=blue)
ax.text(.85,8.12,'Exactly the Boolean absence/presence base.',color=ink)
ax.text(.85,7.63,r'$D_2=\{x:x+x\ne x\}=\mathbb{Z}\setminus\{0\}$',fontsize=20,color=ink)
ax.text(.85,7.16,'The carried parity domain is recovered from addition.',fontsize=11,color=ink)
box(8.52,6.73,4.87,2.38,green)
ax.text(8.83,8.62,'Integer 1 is the unique x with',fontsize=13,color=ink)
ax.text(8.83,8.03,r'$x^2=x\quad\mathrm{and}\quad x+x\ne x$',fontsize=19,color=green)
ax.text(8.83,7.49,r'Multiplicative idempotents: $0,1,\tau$.',fontsize=11.5,color=ink)
ax.text(8.83,7.08,'Only 1 is not additively idempotent.',fontsize=11.5,color=ink)
ax.text(.55,6.12,r'$\{a:\ a(x+y)=ax+ay\ \mathrm{for\ all}\ x,y\}=\{0,\tau\}$',fontsize=21,color=blue)
ax.text(.55,5.63,'For nonzero integer n, the test x = y = tau gives n on the left and n+n on the right.',fontsize=11.7,color=ink)
ax.plot([.5,13.5],[5.27,5.27],color='#c4cdda',lw=1)
ax.text(.55,4.81,'An exact coordinate return at p = 2',fontsize=21,weight='bold',color=ink)
ax.text(.55,4.34,r'$n=r+2k,\quad r\in\{0,1\},\quad k\in\mathbb{Z}$',fontsize=21,color=blue)
ax.text(7.10,4.36,'Both coordinates belong to the integer layer.',fontsize=12,color=ink)
box(.6,2.24,5.92,1.57,green)
box(7.08,2.24,6.20,1.57,gray)
ax.text(.88,3.32,r'$1+1=2$',fontsize=22,color=green)
ax.text(.88,2.76,r'$(1,0)+(1,0)=(0,1)$',fontsize=21,color=green)
ax.text(7.37,3.32,r'$1+(-1)=0$',fontsize=22,color=gray)
ax.text(7.37,2.76,r'$(1,0)+(1,-1)=(0,0)$',fontsize=21,color=gray)
ax.text(.83,1.80,r'$(0,1)$ returns to 2: present, even.',fontsize=13,color=green)
ax.text(7.32,1.80,r'$(0,0)$ returns to 0: absent, no parity.',fontsize=13,color=gray)
ax.text(.55,1.22,'The same residue r = 0 has different full coordinates. No integer value or carry is discarded.',fontsize=12,color=ink)
ax.text(.55,.75,'Tau is a separate presence element, with no integer-coordinate pair and no count of instances.',fontsize=12,color=ink)
ax.text(.55,.27,'Complete proofs and all-prime formulas: INTRINSIC_ALGEBRA_AND_PRIME_COORDINATES.md, IA1–IA8.',fontsize=10,color=ink)
fig.savefig(ROOT/'intrinsic_algebra_and_prime_coordinates.png',dpi=160,bbox_inches='tight')
fig.savefig(ROOT/'intrinsic_algebra_and_prime_coordinates.svg',bbox_inches='tight')
plt.close(fig)
