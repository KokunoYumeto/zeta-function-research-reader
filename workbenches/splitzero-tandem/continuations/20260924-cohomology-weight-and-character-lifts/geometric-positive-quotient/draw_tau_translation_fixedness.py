"""Diagram of proved maps only; drawing positions encode no source metric."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

root=Path(__file__).resolve().parent
fig,ax=plt.subplots(figsize=(12,7.4))
fig.patch.set_facecolor('#fafbfd')
ax.set(xlim=(0,12),ylim=(0,7.4))
ax.axis('off')
ink='#183044'; blue='#1c6c98'; green='#237050'
def arrow(a,b,label,y):
    ax.annotate('',xy=b,xytext=a,arrowprops={'arrowstyle':'-|>','lw':1.7,'color':blue})
    ax.text((a[0]+b[0])/2,y,label,ha='center',color=blue,fontsize=14)
def node(x,y,s):
    ax.add_patch(FancyBboxPatch((x-.65,y-.32),1.3,.64,boxstyle='round,pad=.05',fc='white',ec=blue,lw=1.4))
    ax.text(x,y,s,ha='center',va='center',fontsize=22,color=ink)
ax.text(.4,6.95,'Fixedness from the source bijections',fontsize=23,weight='bold',color=ink)
ax.text(.4,6.48,'An operation diagram. No radius, displacement, or pairing is assigned.',fontsize=12,color=ink)
node(2.1,5.35,r'$\tau$');node(9.75,5.35,r'$\tau$')
arrow((2.85,5.35),(9,5.35),r'$\widehat T_1$',5.65)
ax.text(5.9,4.75,'Forced: integer inputs already map onto all integer outputs.',ha='center',fontsize=12,color=green)
node(2.1,3.5,r'$0$');node(5.95,3.5,r'$1$');node(9.75,3.5,r'$2$')
arrow((2.85,3.5),(5.2,3.5),r'$n\mapsto n+1$',3.9)
arrow((6.7,3.5),(9,3.5),r'$n\mapsto n+1$',3.9)
ax.text(5.95,4.32,'The full integer amount changes: two steps retain 2.',ha='center',fontsize=13,color=ink)
for x,s in [(2.1,'E'),(5.95,'O'),(9.75,'E')]:
    ax.text(x,2.13,s,ha='center',fontsize=22,color=green)
    ax.annotate('',xy=(x,2.45),xytext=(x,3.10),arrowprops={'arrowstyle':'->','lw':1.2,'color':green})
    ax.text(x+.2,2.70,r'$\rho$',fontsize=13,color=green)
ax.text(5.95,1.55,'Orbit classes: one step exchanges E and O; two steps return the class.',ha='center',fontsize=12,color=green)
ax.text(.4,.95,'E and O are the integer orbit classes modulo steps of two.',fontsize=11,color=ink)
ax.text(.4,.59,'This auxiliary quotient does not change the intrinsic Z₀ label retained at integer zero.',fontsize=11,color=ink)
ax.text(.4,.21,'Proofs F0–F4: TAU_FIXEDNESS_FROM_INTEGER_TRANSLATIONS.md. All source integer amounts remain present.',fontsize=9.5,color=ink)
for suffix in ['png','svg']:
    fig.savefig(root/f'tau_translation_fixedness.{suffix}',dpi=160,bbox_inches='tight')
plt.close(fig)
