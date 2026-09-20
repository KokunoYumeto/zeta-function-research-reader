from pathlib import Path
import re,json,subprocess,shutil
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch

P=Path(__file__).parent
fig,ax=plt.subplots(figsize=(10.2,12.8));ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis('off')
colors={'ink':'#18334a','blue':'#e5eff7','gold':'#fff0ce','green':'#e4f0e7','red':'#f7e6e2'}
def box(x,y,w,h,text,color,size=13):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.013',linewidth=1,edgecolor=colors['ink'],facecolor=colors[color]))
    text=re.sub(r'\\le(?![a-zA-Z])',r'\\leq ',text)
    text=re.sub(r'\\ge(?![a-zA-Z])',r'\\geq ',text)
    ax.text(x+w/2,y+h/2,text,ha='center',va='center',fontsize=size,color=colors['ink'],linespacing=1.6)
def arrow(x,y,X,Y):ax.add_patch(FancyArrowPatch((x,y),(X,Y),arrowstyle='-|>',mutation_scale=14,color=colors['ink']))
ax.text(.5,.975,'The original determinant retains both spectral extremes',ha='center',va='top',fontsize=17,weight='bold',color=colors['ink'])
box(.05,.81,.90,.11,'Original quotient and its attained metric\n'+r'$E=\mathbb{C}[y]/(Q),\quad G_N,\quad M=C_N+r_N\ell_N$'+'\n'+r'$C_N^{\dagger}=C_N,\quad\ell_Nr_N=0$', 'blue')
arrow(.5,.805,.5,.758)
box(.05,.59,.90,.16,'EXACT FINITE IDENTITY  (SD5)\n'+r'$\det(M^{\dagger}M+a^2 I)$'+'\n'+r'$=|Q(ia)|^2+a^2|p_N^C(ia)|^2 A_aB_a$'+'\n'+r'$A_a=r_N^{\dagger}(C_N^2+a^2I)^{-1}r_N$'+'\n'+r'$B_a=\ell_N(C_N^2+a^2I)^{-1}\ell_N^{\dagger}$','green',13)
arrow(.3,.585,.3,.525);arrow(.7,.585,.7,.525)
box(.05,.39,.43,.13,'Full original roots\n'+r'$\prod_{j=1}^{q}s_j(M)^2=|Q(0)|^2$'+'\n'+'Every multiplicity remains.\nThe product is independent of N.','blue',12)
box(.52,.39,.43,.13,'Original boundary term\n'+r'$\kappa_N=\Vert r_N\Vert_{G_N}\Vert\ell_N^{\dagger}\Vert_{G_N}$'+'\n'+r'$J_k^{\mathrm{action}}=\sum_Nw_N\log\kappa_N^2$'+'\n'+'The action enters through this term.','gold',12)
arrow(.3,.38,.3,.322);arrow(.7,.38,.7,.322)
box(.05,.15,.90,.16,'PROVED SPECTRAL CONSEQUENCES  (SD11–12, SD21–22)\n'+r'$|s_1(M)-\kappa_N|\le Bq,\qquad\kappa_N\ge q^2/(192B)$'+'\n'+r'$s_j(M)\le Bq\quad(j\ge2)$'+'\n'+r'$s_q(M)/q\le q^{-A}\quad\mathrm{for\ every\ fixed}\ A>0$'+'\n'+'The lower bound for kappa and the inverse-power bound hold eventually.','red',13)
ax.text(.5,.095,'Why the small values are forced: the determinant fixes the product,\nwhile the proved Gaussian bulk remains at scale q.',ha='center',fontsize=11,color=colors['ink'],linespacing=1.5)
ax.text(.5,.022,'All adjoints and norms use G_N.  a > 0; q−1 ≤ N ≤ 2q−1.\nB = 5 max{1, C_mult(h)}.  Fixed original h, δ, γ and m₀.\nExact identities and bounds, not a simulated spectrum. No effective k threshold is claimed.',ha='center',fontsize=9.5,color=colors['ink'],linespacing=1.5)
fig.savefig(P/'SPECTRAL_DETERMINANT_MECHANISM.png',dpi=170,bbox_inches='tight',facecolor='white');plt.close(fig)
