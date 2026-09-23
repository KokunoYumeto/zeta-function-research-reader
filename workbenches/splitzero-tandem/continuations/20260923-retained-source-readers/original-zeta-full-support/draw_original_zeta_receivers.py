from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

p=Path(__file__).parent
r=json.loads((p/'FULL_ZETA_TRACE_RECEIPT.json').read_text())
plt.rcParams.update({'font.size':11,'font.family':'DejaVu Sans','mathtext.fontset':'dejavusans'})
fig=plt.figure(figsize=(12,8.4),layout='constrained')
gs=fig.add_gridspec(2,2,height_ratios=[1,1.12])
ax=fig.add_subplot(gs[0,:]);ax.set(xlim=(0,12),ylim=(0,3.8));ax.axis('off')
ax.set_title('Original zeta: the full multiplier and its inverse have specified domains',loc='left',fontweight='bold',pad=12)
def box(x,y,w,h,text,color):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.1',facecolor=color,edgecolor='#496176',lw=1.1))
    ax.text(x+w/2,y+h/2,text,ha='center',va='center',fontsize=12)
box(.2,1.45,4.6,1.12,r'$z_t\in\mathcal{O}(D_C),\quad z_0=\zeta$'+'\nOriginal meromorphic function','#edf4f9')
box(7.1,1.45,4.6,1.12,r'$h_t=16H_t(-2i(s-\frac{1}{2}))\in\mathcal{O}$'+'\nAuxiliary entire function','#edf4f9')
ax.annotate('',xy=(7,2.3),xytext=(4.9,2.3),arrowprops={'arrowstyle':'->','lw':1.7})
ax.text(5.95,2.6,r'$\times C(s)$',ha='center')
ax.annotate('',xy=(4.9,1.7),xytext=(7,1.7),arrowprops={'arrowstyle':'->','lw':1.7})
ax.text(5.95,1.19,r'$\times C(s)^{-1}$',ha='center')
ax.text(6,.64,r'$C(s)=s(s-1)\pi^{-s/2}\Gamma(s/2)$',ha='center',fontsize=14)
ax.text(6,.10,r'$D_C=[1]-\sum_{n\geq1}[-2n]$; every local unit, jet and support label is retained.',ha='center',fontsize=11)

ax=fig.add_subplot(gs[1,0]);ax.axis('off')
ax.set_title('Actual exceptional stalks',loc='left',fontweight='bold',pad=16)
rows=[['Point','Original $z_t$','Multiplier $C$'],['$1$','simple pole','simple zero'],['$-2n$','simple zero','simple pole'],['$0$','$-8H_t(i)$','$-2$']]
table=ax.table(cellText=rows,cellLoc='center',colWidths=[.17,.40,.40],bbox=[0,.32,1,.62])
table.auto_set_font_size(False);table.set_fontsize(11)
for (i,j),cell in table.get_celld().items():
    cell.set_edgecolor('#c4d0d9');cell.set_facecolor('#e9f1f6' if i==0 else '#ffffff')
ax.text(.02,.19,r'$\mathrm{Res}_1z_t=16H_t(i)=-2z_t(0)>0$',transform=ax.transAxes,fontsize=12)
ax.text(.02,.08,'The zero at $-2n$ has a nonzero twisted fibre.\nOrdinary evaluation and that fibre have different, explicit maps.',transform=ax.transAxes,fontsize=10)

ax=fig.add_subplot(gs[1,1])
vals=[sum(map(float,r[key]['display']))/2 for key in ['full_zeta_divisor_test','retained_completion_divisor_test','nontrivial_root_test']]
ax.barh([2,1,0],vals,color=['#a5463a','#306d9a','#46846b'],height=.54)
ax.axvline(0,color='#667788',lw=.8)
ax.set_yticks([2,1,0],[r'Full $\zeta$ divisor','Full $C$ divisor','Their sum'])
ax.set_xlim(-.10,.11);ax.set_xticks([-.09,-.06,-.03,0,.03,.06,.09]);ax.grid(axis='x',alpha=.18)
for y,v in zip([2,1,0],vals):ax.text(v+(.003 if v>0 else -.003),y,f'{v:+.6f}',va='center',ha='left' if v>0 else 'right',fontsize=10)
ax.set_title('One fixed test at physical time zero',loc='left',fontweight='bold',pad=16)
ax.set_xlabel(r'$F(s)=Z^{-1}+Z^{-3},\quad Z=-2i(s-\frac{1}{2})$',labelpad=12)
ax.spines[['right','top','left']].set_visible(False)
fig.suptitle('Every divisor contribution remains in the receiving equation',fontsize=17,fontweight='bold',x=.02,ha='left')
fig.savefig(p/'ORIGINAL_ZETA_RECEIVERS.png',dpi=170)
fig.savefig(p/'ORIGINAL_ZETA_RECEIVERS.pdf')
print('Wrote reproducible diagram with certified-value midpoints; proofs CF16, CF21, CF27 and OZ8–13.')
