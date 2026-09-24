"""Exact schematic and clock table for proofs M2 and M4--M7."""
from pathlib import Path
from math import lcm
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, FancyArrowPatch

root=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12})
fig=plt.figure(figsize=(15,10),layout='constrained')
gs=fig.add_gridspec(2,1,height_ratios=[1.15,1])
ax=fig.add_subplot(gs[0]);ax.set_xlim(0,15);ax.set_ylim(-.3,5.2);ax.axis('off')
ax.set_title('Three covering circles over ONE prime orbit',loc='left',fontweight='bold',fontsize=18,pad=13)
ax.text(0,4.67,r'Exact example: $p=13$, $\mathbb{Q}(\zeta_7)$, $G=(\mathbb{Z}/7\mathbb{Z})^\times$, return $g\mapsto6g$',fontsize=14)
for x,pair in zip([2.5,7.5,12.5],[(1,6),(2,5),(3,4)]):
    ax.add_patch(Ellipse((x,3.22),3.2,1.05,fill=False,color='#b84735',lw=2.3))
    ax.text(x,3.25,rf'${pair[0]}\ \longleftrightarrow\ {pair[1]}$',ha='center',va='center',fontsize=18,color='#903b2f')
    ax.text(x,2.49,r'period $2\log 13$; degree $2$',ha='center',fontsize=12)
    ax.add_patch(FancyArrowPatch((x,2.24),(7.5,1.22),arrowstyle='->',mutation_scale=14,lw=1.4,color='#526478'))
ax.add_patch(Ellipse((7.5,.79),4.3,.85,fill=False,color='#286da8',lw=2.3))
ax.text(7.5,.81,r'$C_{13}=\mathbb{R}/(\log13)\mathbb{Z}$',ha='center',va='center',fontsize=16,color='#286da8')
ax.text(7.5,.08,r'Base period $\log13$. Positive time is $t=-\log\lambda$; its return is multiplication by $13$.',ha='center',fontsize=12)

bx=fig.add_subplot(gs[1]);bx.axis('off')
bx.set_title('Retain every earlier winding clock: exact refinement data',loc='left',fontweight='bold',fontsize=18,pad=12)
ns=list(range(1,10));ls=[];last=1
for n in ns:
    last=lcm(last,n);ls.append(last)
ratios=[None]+[ls[j]//ls[j-1] for j in range(1,len(ls))]
weights=['—']+[('0' if r==1 else rf'$\log {r}$') for r in ratios[1:]]
cell=[list(map(str,ns)),list(map(str,ls)),['—']+list(map(str,ratios[1:])),weights]
table=bx.table(cellText=cell,rowLabels=[r'New clock $N$',r'Total states $L_N$',r'$L_N/L_{N-1}$',r'$\log L_N-\log L_{N-1}$'],cellLoc='center',rowLoc='right',bbox=[.23,.38,.76,.54])
table.auto_set_font_size(False);table.set_fontsize(13)
for (row,col),cellobj in table.get_celld().items():
    cellobj.set_edgecolor('#ccd3da')
    if col==-1:cellobj.set_facecolor('#f0f3f6')
    else:
        n=ns[col]
        cellobj.set_facecolor('#d9eee6' if n in (2,3,5,7) else '#fff0ce' if n in (4,8,9) else '#f4f4f4')
bx.text(.02,.26,r'$S_N\cong\mathbb{Z}/L_N\mathbb{Z},\quad L_N=\operatorname{lcm}(1,\ldots,N),\quad \log L_N-\log L_{N-1}=\Lambda(N)$',fontsize=18,transform=bx.transAxes)
bx.text(.02,.14,'Green: first prime channel. Gold: refinement of an existing prime channel. Gray: no new independent state.',fontsize=12,transform=bx.transAxes)
bx.text(.02,.035,r'All clocks remain recorded. The compatible infinite system is $\widehat{\mathbb{Z}}$; no finite prefix isolates an unbounded integer.',fontsize=12,transform=bx.transAxes)
fig.suptitle('Prime monodromy and the complete stack of winding observations',fontsize=20,fontweight='bold')
fig.savefig(root/'prime_monodromy_history.png',dpi=165)
fig.savefig(root/'prime_monodromy_history.svg')
plt.close(fig)

cycles=[];unseen=set(range(1,7))
while unseen:
    g=min(unseen);orbit=[];x=g
    while x not in orbit:
        orbit.append(x);unseen.remove(x);x=6*x%7
    cycles.append(orbit)
assert cycles==[[1,6],[2,5],[3,4]]
assert ls==[1,2,6,12,60,60,420,840,2520]
(root/'MONODROMY_FIGURE_CHECKS.json').write_text(json.dumps({
    'purpose':'Exact checks of the displayed example and table, not a test of RH or a finite substitute for M3--M7.',
    'finite_cover_cycles':cycles,'N':ns,'lcm':ls,'ratios':ratios,
    'proofs':'PRIME_MONODROMY_STACKED_HISTORY.md M2, M4--M7',
    'source':'Connes--Consani, arXiv:2501.06560v1, mappingtorus and finite-cover theorem'
},indent=2),encoding='utf-8')
print('Wrote PNG, SVG and exact figure-data checks.')
