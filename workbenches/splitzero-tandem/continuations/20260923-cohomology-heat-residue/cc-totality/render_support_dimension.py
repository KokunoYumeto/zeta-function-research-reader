from pathlib import Path
import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
ROOT=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'mathtext.fontset':'dejavusans'})
fig=plt.figure(figsize=(11.5,8.3),layout='constrained')
gs=fig.add_gridspec(2,3,height_ratios=[1,1.5]);colors=['#2563a6','#bf4a22','#267052']
specs=[('Two-element lattice',[(0,0),(0,1)],[(0,1)],[r'$\tau=z_{0_L}$',r'$e=z_{1_L}$'],r'$|J|=1,\quad |J_{<}|=0$'),('Four-element chain',[(0,0),(0,1/3),(0,2/3),(0,1)],[(0,1),(1,2),(2,3)],[r'$\tau$',r'$z_u$',r'$z_v$',r'$e$'],r'$|J|=3,\quad |J_{<}|=2$'),('Four-element Boolean lattice',[(0,0),(-.6,.5),(.6,.5),(0,1)],[(0,1),(0,2),(1,3),(2,3)],[r'$\tau$',r'$z_{\{u\}}$',r'$z_{\{v\}}$',r'$e=z_{\{u,v\}}$'],r'$|J|=2,\quad |J_{<}|=2$')]
for idx,(title,xy,edges,labels,formula) in enumerate(specs):
    ax=fig.add_subplot(gs[0,idx]);ax.set_title(title,color=colors[idx],fontweight='bold',pad=16)
    for a,b in edges:ax.plot([xy[a][0],xy[b][0]],[xy[a][1],xy[b][1]],color=colors[idx],lw=2,zorder=1)
    for (x,y),label in zip(xy,labels):
        ax.scatter(x,y,s=65,c=colors[idx],zorder=2);ax.annotate(label,(x,y),xytext=(8,0),textcoords='offset points',va='center')
    ax.text(0,-.26,formula,ha='center');ax.set(xlim=(-1.05,1.35),ylim=(-.38,1.22));ax.axis('off')
ax=fig.add_subplot(gs[1,:]);bounds=[.25,1,2,4,8,12]
for title,color,base,extra,style in [('Two-element lattice',colors[0],1,0,'-'),('Four-element chain',colors[1],3,2,'-'),('Four-element Boolean lattice',colors[2],2,2,'--'),('Original integer module','#555555',0,0,':')]:
    for lo,hi in zip(bounds[:-1],bounds[1:]):
        y=base if lo<1 else int(math.log2(lo))+2+extra
        ax.plot([lo,hi],[y,y],color=color,lw=2.5,ls=style,label=title if lo==.25 else None)
        if lo>=1:ax.plot(lo,y,'o',color=color,ms=5)
        if hi<12:ax.plot(hi,y,'o',mfc='white',mec=color,ms=5)
ax.set_xscale('log',base=2);ax.set_xticks([.25,.5,1,2,4,8],['1/4','1/2','1','2','4','8'])
ax.set(xlim=(.25,12),ylim=(-.4,7.5),yticks=range(8),xlabel=r'Original archimedean bound $\lambda=e^{\delta}$ (logarithmic axis)',ylabel=r'$\mathbb{S}$-dimension')
ax.grid(axis='y',alpha=.2);ax.legend(loc='upper left',ncol=2,frameon=False)
fig.suptitle('Every support label changes the generator problem\nExact modules and maps: SRR1–8; dimension theorem: SRR6',fontsize=16,fontweight='bold')
for ext in ['png','pdf','svg']:fig.savefig(ROOT/('SUPPORT_DIMENSION.'+ext),dpi=180,bbox_inches='tight')
print('Rendered exact finite-lattice examples and proved step functions')
