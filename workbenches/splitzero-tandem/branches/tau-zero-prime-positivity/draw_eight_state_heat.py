"""Reproduce the exact ESH35–ESH55 curves and collision diagram."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

P=Path(__file__).resolve().parent/'figures';P.mkdir(exist_ok=True)
plt.rcParams.update({'font.size':11,'axes.titlesize':13,'mathtext.fontset':'dejavusans'})
fig=plt.figure(figsize=(12,9),layout='constrained')
gs=fig.add_gridspec(2,2,height_ratios=[1,1.05])
ax=fig.add_subplot(gs[0,:]);h=np.linspace(0,.3,700);s=np.sqrt(1+64*h)
ax.plot(h,-2*(2-16*h),color='#146c94',lw=2.4,label=r'Marked root $R=1$: $-2\mu_1$')
ax.plot(h,-s*(s-3),color='#bc4b51',lw=2.4,label=r'Moving root $R_+$: $-2\mu_+$')
ax.plot(h,-s*(s+3),color='#713b8e',lw=2.4,label=r'Persistent root $R_-$: $-2\mu_-$')
ax.axhline(0,color='#333333',lw=1);ax.axvline(1/8,color='#333333',ls='--',lw=1)
ax.scatter([1/8,1/8],[0,-18],s=45,color=['#333333','#713b8e'],zorder=5)
ax.annotate(r'$-18$',(1/8,-18),xytext=(.145,-19),fontsize=12)
ax.set(xlim=(0,.3),ylim=(-34,7),xlabel=r'Chosen target path parameter $h$',ylabel=r'Sign-coordinate trace value $Q(T,T)$',title='The marked factor gains a positive direction; another factor loses one')
ax.set_xticks([0,1/8,1/4,.3],['0','1/8','1/4','0.3']);ax.grid(alpha=.2)
ax.legend(loc='lower left',fontsize=10)

ax=fig.add_subplot(gs[1,0]);ax.axis('off')
ax.set_title('All eight dimensions retained',pad=14)
rows=[['Parameter','Positive','Negative','Radical'],[r'$0\leq h<1/8$','6','2','0'],[r'$h=1/8$','4','1','3'],[r'$h>1/8$','6','2','0']]
table=ax.table(cellText=rows,cellLoc='center',colWidths=[.4,.2,.2,.2],bbox=[.02,.42,.96,.46])
table.auto_set_font_size(False);table.set_fontsize(11)
for (r,c),cell in table.get_celld().items():
    cell.set_edgecolor('#a0a0a0')
    if r==0:cell.set_facecolor('#e6edf0');cell.set_text_props(weight='bold')
    elif c==2:cell.set_facecolor('#fae6e5')
ax.text(.03,.30,r'Involution: $\#_\Sigma(T)=-T$, with scalar conjugation.',transform=ax.transAxes,fontsize=10)
ax.text(.03,.20,r'Infinity stays $\Theta^2=-1$: two positive states.',transform=ax.transAxes,fontsize=10)
ax.text(.03,.08,'The omitted infinity state is unramified.\nIt is separate from this finite-root collision.',transform=ax.transAxes,fontsize=10)

ax=fig.add_subplot(gs[1,1]);ax.axis('off');ax.set_title('The infinitesimal survives the vanishing trace',pad=14)
ax.text(.5,.85,r'$F_{1/8}(R)=(R-1)^2(R+2)$',ha='center',transform=ax.transAxes,fontsize=15)
ax.text(.5,.66,r'$\mathcal{L}=\mathbb{C}[T]/(T^4)$',ha='center',transform=ax.transAxes,fontsize=16)
ax.text(.5,.55,r'$\epsilon=R-1=T^2/6$',ha='center',transform=ax.transAxes,fontsize=13)
ax.annotate('',xy=(.5,.31),xytext=(.5,.48),xycoords='axes fraction',arrowprops={'arrowstyle':'->','lw':1.7})
ax.text(.53,.39,r'kernel $(T^2)/(T^4)$',transform=ax.transAxes,fontsize=11)
ax.text(.5,.23,r'$E_0=\mathbb{C}[T]/(T^2),\quad r_H=T/(2\sqrt{2})$',ha='center',transform=ax.transAxes,fontsize=14)
ax.text(.5,.08,r'$Q_{\mathcal{L}}(f,g)=2Q_{E_0}(\bar\pi_1f,\bar\pi_1g)$',ha='center',transform=ax.transAxes,fontsize=12)
fig.suptitle('The original eight-state completion along the exact marked-root heat path',fontsize=16)
for ext in ['png','svg']:fig.savefig(P/f'30_eight_state_heat.{ext}',dpi=180,bbox_inches='tight')
print('Rendered figure 30 from the proved derivative functions and full fibre algebras.')
