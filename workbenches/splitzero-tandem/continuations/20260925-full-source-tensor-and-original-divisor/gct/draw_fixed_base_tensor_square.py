from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

r=Path(__file__).resolve().parent
fig,ax=plt.subplots(figsize=(16,10),facecolor='#f7f9fc')
ax.set(xlim=(0,1),ylim=(0,1)); ax.axis('off')
ink,blue,green,red='#19324c','#225a9d','#187062','#9b5132'
ax.text(.5,.966,'One fixed base: the two lifts remember the first boundary',ha='center',fontsize=23,color=ink)
ax.text(.5,.913,'FST1–6 · Actual coefficient square on the same sphere · Both poles and all endpoints retained',ha='center',fontsize=14,color=ink)
def box(x,y,w,h,text,color=blue,size=16):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.01',ec=color,fc='white',lw=1.8))
    ax.text(x+w/2,y+h/2,text,ha='center',va='center',fontsize=size,color=color,linespacing=1.5)
def arrow(a,b,text):
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=18,lw=1.8,color=blue))
    ax.text((a[0]+b[0])/2,(a[1]+b[1])/2+.035,text,ha='center',fontsize=18,color=blue)
box(.04,.715,.22,.12,r'$V=A\widehat{\otimes}A$'+'\nDegree −2')
box(.37,.715,.27,.12,r'$L=(H_\infty\widehat{\otimes}A)$'+'\n'+r'$\oplus(A\widehat{\otimes}H_\infty)$'+'\nDegree −1',size=14)
box(.75,.715,.21,.12,r'$M=H_\infty\widehat{\otimes}H_\infty$'+'\nDegree 0',size=15)
arrow((.27,.775),(.36,.775),r'$d_0$')
arrow((.65,.775),(.74,.775),r'$d_1$')
ax.text(.5,.656,r'$d_0(a\otimes a^{\prime})=(ba\otimes a^{\prime},-a\otimes ba^{\prime}),\qquad d_1d_0=0$',ha='center',fontsize=19,color=ink)
box(.04,.36,.44,.225,
    r'$H_L(a\otimes a^{\prime})=(ba\otimes a^{\prime},0)$'+'\n'
    r'$H_R(a\otimes a^{\prime})=(0,a\otimes ba^{\prime})$'+'\n'
    r'$d_1H_L=d_1H_R=b\widehat{\otimes}b$',green,17)
box(.53,.36,.43,.225,
    r'$H_L-H_R=d_0$'+'\nThe top detector is a boundary.\nIts two lifts differ by the first\nspecialization boundary.',red,18)
box(.04,.138,.44,.142,
    'Actual first specialization source\n'+r'$V/\ker d_0\ \longrightarrow\ \ker d_1$'+'\n'+r'$[x]\longmapsto d_0x$',blue,17)
box(.53,.138,.43,.142,
    'Hausdorff top receiver at each pole\n'+r'$M/\overline{\mathrm{im}\,d_1}$'+'\n'+r'$\simeq H_{\infty,L}\widehat{\otimes}H_{\infty,L}$',green,17)
ax.text(.5,.080,'Single-sphere angular pullback: '+r'$n(T_n\widehat{\otimes}T_n)$'+'  ·  Raw angular sign and all endpoint words: FST2, FST6.',ha='center',fontsize=14,color=ink)
ax.text(.5,.038,'Each pole has this local complex. The global model is '+r'$V\longrightarrow L\oplus L\longrightarrow M\oplus M\oplus V$'+'.',ha='center',fontsize=14,color=ink)
ax.text(.5,.002,'Proof: ACTUAL_FIXED_BASE_TENSOR_SQUARE.md. Inputs ACD6–8, ADM, TWC; CC and Deligne source provenance retained in the proof.',ha='center',fontsize=10,color=ink)
fig.subplots_adjust(left=.02,right=.98,top=.97,bottom=.025)
for ext in ['png','svg']:
    fig.savefig(r/f'fixed_base_tensor_square.{ext}',dpi=165,bbox_inches='tight',facecolor=fig.get_facecolor())
plt.close(fig)
