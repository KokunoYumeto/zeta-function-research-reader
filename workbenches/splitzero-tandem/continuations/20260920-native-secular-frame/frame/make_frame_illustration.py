"""Exact two-real-dimensional section of the four-complex-dimensional receiver."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
P=Path(__file__).parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'svg.fonttype':'none'})
fig=plt.figure(figsize=(16,10),facecolor='#fafbff')
gs=GridSpec(2,2,figure=fig,height_ratios=[3.4,1.5],hspace=.28,wspace=.12)
cs=-60/431
ss,tt=np.meshgrid(np.linspace(-1,1,11),np.linspace(-1,1,11))
colors=['#287dac','#ac463c']
for k,c in enumerate([cs+1/500,cs]):
    ax=fig.add_subplot(gs[0,k],projection='3d')
    y4=-208*c*c/21*ss+4*(431*c+60)/21*tt
    ax.plot_wireframe(ss,y4,tt,color=colors[k],linewidth=.9,alpha=.65)
    # Literal coordinate projection forgetting the added moment; no metric identification.
    ax.plot_wireframe(ss,y4,np.zeros_like(tt),color='#202d46',linewidth=1,alpha=.7)
    for i in [0,5,10]:
        for j in [0,5,10]:
            ax.plot([ss[i,j]]*2,[y4[i,j]]*2,[0,tt[i,j]],color='#8c94a4',ls=':',lw=.8)
    if k==1:
        ax.plot(np.zeros(60),np.zeros(60),np.linspace(-1,1,60),color='#e09612',lw=4)
    ax.set(xlim=(-1,1),ylim=(-.4,.4),zlim=(-1.1,1.1))
    ax.set_xticks([-1,-.5,0,.5,1]);ax.set_yticks([-.2,0,.2]);ax.set_zticks([-1,0,1])
    ax.set_xlabel(r'$y_1=s$',labelpad=6)
    ax.set_ylabel(r'$\operatorname{Im} y_4$',labelpad=8)
    ax.set_zlabel(r'Added observation $m\beta=t$',labelpad=9)
    ax.view_init(elev=24,azim=-58)
    ax.set_box_aspect((1,.8,1))
    ax.set_title((r'$c=c_*+1/500$: the old output detects both directions'+'\nDark projection: rank 2 on this section' if k==0 else
                  r'$c=c_*=-60/431$: the old output loses one direction'+'\nDark projection: rank 1; the gold direction is invisible'),pad=16,fontsize=11)
ax=fig.add_subplot(gs[1,:]);ax.axis('off')
ax.text(.02,.98,'Exactly which section is drawn?',fontsize=17,fontweight='bold',va='top',color='#17233c')
ax.text(.02,.76,r'$\beta=\widetilde O(c)^{-1}(s,0,0,t)^T,\quad -1\leq s,t\leq1,\quad s,t\in\mathbb{R}$',fontsize=17,va='top')
ax.text(.02,.51,r'$O\beta=(s,0,0,i[-\frac{208c^2}{21}s+\frac{4(431c+60)}{21}t])^T,\qquad m\beta=t$',fontsize=17,va='top')
ax.text(.02,.23,r'At $c_*$: $\beta=tb/420$ has $O\beta=0$, while $m\beta=t$.  The added moment retains the entire lost line.',fontsize=13,va='top')
fig.suptitle('A regular eight-branch fibre can lose an observation — one moment recovers it',fontsize=21,fontweight='bold',x=.5,y=.975,color='#17233c')
fig.text(.5,.025,'Exact section and coordinate projection, not a metric-preserving embedding. Proof: ODD_FRAME_REPAIR.tex, OF9–20.\nReceiving map: Fable SE1–14. Null-vector interpolation: N. M. Temme, DLMF §3.3(i). Full caption accompanies this image.',ha='center',fontsize=10,color='#3d4760')
fig.subplots_adjust(top=.88,bottom=.1,left=.03,right=.97)
fig.savefig(P/'ODD_FRAME_REPAIR_ILLUSTRATION.svg',facecolor=fig.get_facecolor())
fig.savefig(P/'ODD_FRAME_REPAIR_ILLUSTRATION.png',dpi=155,facecolor=fig.get_facecolor())
print('Saved exact receiving-section SVG and PNG, 2480 x 1550.')
