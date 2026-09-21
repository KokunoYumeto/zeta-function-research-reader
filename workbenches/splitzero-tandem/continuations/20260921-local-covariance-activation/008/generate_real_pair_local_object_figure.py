"""Reproducible schematic of exact local root-coordinate germs and maps."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
B=Path(__file__).resolve().parent;O=B/'figures_real_pair_local';O.mkdir(exist_ok=True)
fig=plt.figure(figsize=(14,8.7),facecolor='white')
gs=fig.add_gridspec(2,2,height_ratios=[1.6,1],left=.065,right=.95,bottom=.08,top=.84,hspace=.32,wspace=.33)
ax=fig.add_subplot(gs[0,0]);bx=fig.add_subplot(gs[0,1]);cx=fig.add_subplot(gs[1,:])
for a in [ax,bx]:
    a.set_xlim(-1,1);a.set_ylim(-1,1);a.set_aspect('equal');a.set_xticks([]);a.set_yticks([])
    for sp in a.spines.values():sp.set_visible(False)
    a.annotate('',xy=(1,0),xytext=(-1,0),arrowprops={'arrowstyle':'->','color':'#77808c','lw':1})
    a.annotate('',xy=(0,1),xytext=(0,-1),arrowprops={'arrowstyle':'->','color':'#77808c','lw':1})
ax.set_title('Complexified family: real root-coordinate slice',fontsize=13,pad=15)
ax.plot([-.91,.91],[0,0],color='#147b83',lw=3)
ax.plot([0,0],[-.91,.91],color='#a74652',lw=3)
ax.plot([-.78,.78],[-.78,.78],'--',color='#997220',lw=1.6)
ax.scatter([0],[0],s=75,c='#102334',zorder=5)
ax.text(.86,-.13,r'$\alpha$',fontsize=14);ax.text(.10,.90,r'$\beta$',fontsize=14)
ax.text(.20,.12,r'$\beta=0:\ v=1$',color='#147b83',fontsize=12)
ax.text(-.93,.40,r'$\alpha=0$'+'\n'+r'$v=1$',color='#a74652',fontsize=12)
ax.text(.14,-.42,r'$p_*:\ \alpha=\beta=0$'+'\n'+r'$v=2$',fontsize=12)
ax.text(-.87,-.91,r'$\alpha\beta\ne0:\ v=0$',fontsize=12)
ax.annotate(r'$\alpha=\beta\ne0$'+'\nspectral collision; '+r'$g_0\ne0$',xy=(.62,.62),xytext=(.99,.60),
            fontsize=10.5,color='#806015',arrowprops={'arrowstyle':'-','color':'#806015'},ha='left')
bx.set_title('Actual real parameters: '+r'$\beta=-\overline{\alpha}$',fontsize=13,pad=15)
bx.axvline(0,ls='--',c='#997220',lw=1.6,ymin=.08,ymax=.92)
bx.scatter([0],[0],s=75,c='#102334',zorder=5)
bx.text(.62,-.15,r'$\Re\alpha$',fontsize=13);bx.text(.10,.91,r'$\Im\alpha$',fontsize=13)
bx.text(-.93,.46,r'$g_0=-U_0|\alpha|^2>0$'+'\n'+r'$U_0<0;\ v=0$',fontsize=12)
bx.annotate('Only conductor zero:\n'+r'$\alpha=0,\ v=2$',xy=(0,0),xytext=(.20,-.56),fontsize=12,
            arrowprops={'arrowstyle':'->','color':'#102334'})
cx.axis('off')
cx.set_title('The exact comparison in the original Gamma metric (RQT3–16)',fontsize=14,pad=10)
boxes=[(.02,r'Old source $\mathcal{P}_D$',r'$I_N$'),(.39,r'Moving quotient $\mathcal{P}_{D+2}/K$',r'$q:\ I_N,\quad w:\ M=(I+ZZ^*)^{-1}$'),(.80,r'Target $\mathcal{P}_D$',r'$I_N$')]
for x,title,metric in boxes:
    cx.text(x,.67,title+'\n'+metric,transform=cx.transAxes,fontsize=12,ha='left',va='center',
       bbox={'boxstyle':'round,pad=.55','facecolor':'#eff4f7','edgecolor':'#7c93a5'})
cx.annotate('',xy=(.385,.67),xytext=(.24,.67),xycoords='axes fraction',arrowprops={'arrowstyle':'->','lw':1.6})
cx.text(.30,.88,r'$T_0$',transform=cx.transAxes,fontsize=14)
cx.annotate('',xy=(.795,.67),xytext=(.71,.67),xycoords='axes fraction',arrowprops={'arrowstyle':'->','lw':1.6})
cx.text(.735,.88,r'$\widetilde A$',transform=cx.transAxes,fontsize=14)
cx.text(.01,.22,r'$B=\widetilde A T_0$'+r'    $\operatorname{sv}(T_0)=(1,\ldots,1,d_1,d_2)$',transform=cx.transAxes,fontsize=14)
cx.text(.55,.22,r'$d_1d_2=|g_0|^{D+1}/\sqrt{\det(RR^*)}$',transform=cx.transAxes,fontsize=14)
fig.suptitle('Two branches, one coupled module, and the exact source-angle defect',fontsize=19,y=.98)
fig.text(.065,.925,'Schematic local coordinate germs, not a metric embedding or a numerical neighborhood. All original coordinates return through RLA9.',fontsize=10.5)
fig.text(.065,.026,'Proof: RLA6–18, RQT1–19. Original family and Gamma frames: PCL and WCF; certified root: RPZ1–19. Full human citations accompany the proof.',fontsize=10)
for ext in ['png','svg']:fig.savefig(O/f'38_real_pair_local_object.{ext}',dpi=180,facecolor='white')
plt.close(fig)
print('Created figure38 PNG and SVG.')
