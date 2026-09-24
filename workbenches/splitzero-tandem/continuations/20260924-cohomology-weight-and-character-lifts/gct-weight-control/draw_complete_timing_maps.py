from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

root = Path(__file__).resolve().parent
fig, ax = plt.subplots(figsize=(15, 10))
fig.patch.set_facecolor('#fafbfd')
ax.set(xlim=(0, 15), ylim=(0, 10))
ax.axis('off')

def box(x, y, w, h, text, color='#e8f0fa', size=12):
    ax.add_patch(FancyBboxPatch((x-w/2, y-h/2), w, h,
        boxstyle='round,pad=0.04', facecolor=color, edgecolor='#435970'))
    ax.text(x, y, text, ha='center', va='center', fontsize=size)

def arrow(x, y, X, Y):
    ax.annotate('', xy=(X,Y), xytext=(x,y),
        arrowprops={'arrowstyle':'->', 'color':'#435970', 'lw':1.6})

ax.text(7.5,9.6,'Whole timing first; arithmetic coordinates afterwards',
    ha='center',fontsize=20,weight='bold')
ax.text(7.5,9.13,'Exact receiving maps. The duration line is not a metric on the supporting point.',
    ha='center',fontsize=11.5)
box(3.6,7.95,6.0,1.35,'Complete absorption record '+r'$(E,t)$'+'\n'
    +r'$G_t=\{\sum_e a_e t(e):a_e\in\mathbb{Z},\ \mathrm{finite\ support}\}$'
    +'\nAll durations, event identities and multiplicities retained',size=11.6)
box(11.35,7.95,6.0,1.35,r'$G_t=\delta\mathbb{Z},\quad\delta>0$'+'\n'
    +r'$\delta=\min(G_t\cap V_{>0})$'+'\nExistence is equivalent to discreteness',color='#e6f3ec')
arrow(6.67,7.95,8.27,7.95)
ax.text(7.48,8.24,'discrete case\nGTQ2',ha='center',fontsize=10)
box(11.35,5.9,6.0,1.35,r'$t(e)=n\delta\ \longmapsto\ n$'+'\n'
    +r'$\operatorname{End}(G_t)\simeq\mathbb{Z},\quad\mathrm{id}\longmapsto1$'
    +'\nKeep absorption AND non-absorption positions',color='#e6f3ec')
arrow(11.35,7.21,11.35,6.66)
box(3.6,5.9,6.0,1.35,'Complete odd-refinement test history\n'
    +r'$c,\quad(1+3^{-1})c,\quad(2+3^{-2})c,\ldots$'+'\n'
    +r'$G_t=c\mathbb{Z}[1/3]$: no least positive duration',color='#fff0df')
arrow(3.6,7.21,3.6,6.66)
ax.text(3.6,4.82,'Every finite stage has a unit; the full history need not.',
    ha='center',fontsize=11.0)
box(7.5,3.6,13.8,1.45,'The full signed structure survives this refinement\n'
    +r'$G_D=D\times C_4,\quad J^2=\epsilon,\quad\epsilon^2=1$'+'\n'
    +r'$A_D(d,k)=(-d,2\chi(d)-k),\quad \chi(ac/3^r)=a\ (\mathrm{mod}\ 2)$',
    color='#edeafa',size=13)
box(4.0,1.66,6.0,1.2,r'$\eta\ \longmapsto\ \eta$'+'\n'
    +r'$\tau\langle Z_1;\mathrm{no\ exchanged}\ Z_2\rangle$'
    +'\nFixed support; no pointwise exchanged parity label',color='#f7efd9',size=11.5)
box(11.15,1.66,6.05,1.2,r'$(d,k)A_D(d,k)=\epsilon^{\chi(d)}$'+'\n'
    +'Every old winding and parity value is retained\nThe support is distinct from its section data',size=11.6)
arrow(5.2,2.82,4.2,2.34)
arrow(9.8,2.82,10.8,2.34)
ax.text(7.5,.53,'Proofs: GTQ1–GTQ8; OR1–OR7. Source comparison: Connes–Consani, arXiv:2609.00299v1, §§3–4.',
    ha='center',fontsize=10.1)
ax.text(7.5,.17,'The test history probes completeness → tick only; it is not asserted to be an admissible RH counterexample.',
    ha='center',fontsize=10.1)
for ext in ('png','svg'):
    fig.savefig(root/f'complete_timing_maps.{ext}',dpi=160,bbox_inches='tight')
plt.close(fig)
print(root/'complete_timing_maps.png')
