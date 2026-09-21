"""Reproducible diagrams of proved loci, bounds and original weighted poles."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch
import numpy as np
B=Path(__file__).resolve().parent
O=B/'figures_unit_phase_20260921';O.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'svg.fonttype':'none'})
blue='#166088';red='#b34545';green='#24745e'
fig,axs=plt.subplots(1,2,figsize=(13.2,6.7),gridspec_kw={'width_ratios':[1,1.1]})
ax=axs[0]
ax.add_patch(Circle((0,0),1,fill=False,edgecolor=blue,lw=2.4))
ax.axhline(0,color='.85',lw=.8);ax.axvline(0,color='.85',lw=.8)
ax.scatter([0],[0],s=32,color=red,zorder=4)
v=np.array([-.03099394451,.011074723404]);v=v/np.linalg.norm(v)*.7
ax.add_patch(FancyArrowPatch((0,0),v,arrowstyle='-|>',mutation_scale=18,color=red,lw=2))
fig.text(.08,.22,'The root stays inside this disk for every\n'+r'real unit phase $|x|\leq10^{-10}$.',fontsize=11)
ax.set(xlim=(-1.2,1.2),ylim=(-1.05,1.1),aspect='equal',xlabel=r'$\operatorname{Re}(z-c)/10^{-9}$',ylabel=r'$\operatorname{Im}(z-c)/10^{-9}$')
ax.set_title('Certified period disk and tangent direction',loc='left',fontweight='bold',pad=20)
fig.text(.08,.10,'Centre: the exact rational $c$ in FPZ4.\nBase root: $|z(0)-c|<10^{-14}$; marker is schematic.\nArrow shows tangent direction only; its length is arbitrary.',fontsize=9.5)
ax=axs[1];ax.axis('off')
ax.set_title('A simple singularity in the actual unit family',loc='left',fontweight='bold',pad=20)
lines=[(r'$a=\alpha(1+ix),\quad\alpha\in\mathbb{R}\setminus\{0\}$',18,blue),
       ('Every original matrix and Gamma weight is retained.',11,'black'),
       (r'$\mu_0(z,x)=(z-z(x))\,\mathcal{B}(z,x),\quad\mathcal{B}\ne0$',16,blue),
       (r'$|\mu_1|>14.01,\quad |\partial_z\mu_0|>1516$',15,green),
       (r'$|\partial_x\mu_0|>53.65$',15,green),
       (r'$z\,^{\prime}(0)\in[-.03099394451\pm5.37\times10^{-12}]$',12,'black'),
       (r'$\qquad+i[.011074723404\pm7.11\times10^{-13}]$',12,'black'),
       ('Fixed old degree-three spaces: rank 3 on the graph.',11,'black'),
       ('Actual order-one quotient: invertible on the graph.',11,'black')]
y=.94
for text,size,col in lines:
    ax.text(.01,y,text,fontsize=size,color=col,va='top');y-=.105
fig.suptitle('The original conductor singularity persists and moves',fontsize=20,y=.985)
fig.text(.04,.015,'UPP1–20; full infinite-series certificate. Arithmetic: Fredrik Johansson, Arb, arXiv:1611.02831v1.\nThis is the specified geometric family; no arithmetic zeta-zero identification is asserted.',fontsize=9)
fig.subplots_adjust(top=.85,bottom=.36,wspace=.25,left=.08,right=.97)
for ext in ['png','svg']:fig.savefig(O/f'32_unit_phase_graph.{ext}',dpi=180)
plt.close(fig)

fig,axs=plt.subplots(1,2,figsize=(13.2,7.0),gridspec_kw={'width_ratios':[1.1,1]})
ax=axs[0];ax.axis('off');ax.set_title('Every unit: exact finite-zero argument',loc='left',fontweight='bold')
ax.set_xlim(-.04,1.04)
boxes=[(r'Original unit $a=\alpha+i\chi\ne0$'+'\nAll four original factors $F_j(z)$',.81,blue),
       ('Complete coefficients $[z^2]F_j$ and $[z^4]F_j$\nExact quartics with the full unit denominator',.64,blue),
       ('Degree-19 residual algebra; explicit mod-101 inverses\nNo phase makes both coefficients vanish',.47,green),
       ('Even entire functions of exponential type\nEach factor has a nonzero finite complex zero',.30,green),
       ('Fixed old conductor: a finite singularity for every unit\nEvery inverse exterior norm diverges there',.13,green)]
for text,y,col in boxes:
    ax.add_patch(FancyBboxPatch((.01,y),.98,.12,boxstyle='round,pad=.012',fc='white',ec=col,lw=1.5))
    ax.text(.5,y+.06,text,ha='center',va='center',fontsize=10.5)
    if y>.2:ax.annotate('',xy=(.5,y-.035),xytext=(.5,y-.012),arrowprops={'arrowstyle':'->','color':col})
fig.text(.04,.145,'Both boundary phases also have nonzero fourth coefficient;\nthe guaranteed zero is therefore beyond $z=0$.\nThis argument alone does not certify its orbit or symbol order.',fontsize=10)
ax=axs[1]
ax.plot([1,2,3,4],[4]*4,'o-',color=blue,lw=2,ms=8,label='Vary period at fixed phase')
ax.plot([1,2,3,4],[4]*4,'s',mfc='none',mec=red,mew=2,ms=13,label='Vary phase at the fixed certified period')
ax.set(xlim=(.65,4.35),ylim=(0,5.2),xticks=[1,2,3,4],yticks=[0,1,2,3,4,5],xlabel='Exterior rank $r$',ylabel='Proved inverse pole order')
ax.grid(alpha=.18);ax.set_title('Certified degree-three conductor',loc='left',fontweight='bold')
ax.legend(loc='lower center',fontsize=9,frameon=False)
fig.text(.575,.115,r'$\lim |x|^4\|\bigwedge^r B_{3,s}(z_*,x)^{-1}\|$'+'\n'+r'$=\|\bigwedge^{4-r} B_{3,s}(z_*,0)\|/|\partial_x\mu_0(z_*,0)|^4>0$',fontsize=12)
fig.suptitle('Global finite zeros and two exact conductor singularity paths',fontsize=19,y=.98)
fig.text(.04,.015,'ANP1–32: exact coefficient elimination. GUC1–5: singularity for every unit. UPP17–20: original Gamma-metric exterior constants.\nOriginal period source: PCL1–10. ES marking and human provenance: canonical version-69 reader, FSR1–24.',fontsize=9)
fig.subplots_adjust(top=.86,bottom=.32,wspace=.30,left=.04,right=.97)
for ext in ['png','svg']:fig.savefig(O/f'33_unit_global_and_exterior.{ext}',dpi=180)
plt.close(fig)
print('Two figures rendered with their reproducible SVG sources.')
