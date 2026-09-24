"""Reproducible diagram of the proved transfer-adjoint attempt, with no sampled zeros."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

base=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','mathtext.fontset':'dejavusans'})
fig,ax=plt.subplots(figsize=(12,8.6));ax.set_xlim(0,12);ax.set_ylim(0,8.6);ax.axis('off')
ax.text(6,8.25,'The positive-adjoint repair keeps an exact degree defect',ha='center',fontsize=18,weight='bold')
ax.text(6,7.82,'All actual nontrivial zeros and their multiplicities; no finite zero sample',ha='center',fontsize=11,color='#465568')

def box(x,y,w,h,title,lines,color):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.12',facecolor=color,edgecolor='#506074',lw=1.2))
    ax.text(x+w/2,y+h-.30,title,ha='center',va='top',fontsize=12,weight='bold')
    for yy,line in zip([y+h-.79-.46*i for i in range(len(lines))],lines):
        ax.text(x+w/2,yy,line,ha='center',va='top',fontsize=12)

box(.35,5.47,5.25,1.85,'Actual transfer and original Weil form',[
    r'$T_a x_\rho=a^\rho x_\rho,\quad U_a=aT_{1/a}$',
    r'$U_aT_a=aI,\quad W(T_ax,y)=W(x,U_ay)$'], '#eef5fc')
box(6.4,5.47,5.25,1.85,'Positive value space',[
    r'$\langle x,y\rangle=\sum_\rho m_\rho x_\rho\overline{y_\rho}$',
    r'$T_a^*=JU_aJ,\quad D_a=T_a^*-U_a$'], '#eef8f2')
ax.add_patch(FancyArrowPatch((5.75,6.37),(6.22,6.37),arrowstyle='->',mutation_scale=18,color='#506074'))
ax.text(6,6.65,'GTAH1',ha='center',fontsize=9)
box(.6,2.86,10.8,1.94,'Attempt: average both operators with the actual reflection',[
    r'$\widetilde T_a=(T_a+JT_aJ)/2,\quad\widetilde U_a=(U_a+JU_aJ)/2$',
    r'$\widetilde T_a^{\,*}=\widetilde U_a,\qquad\widetilde U_a\widetilde T_a=aI+\frac{1}{4}D_a^*D_a$'], '#fff5e8')
ax.add_patch(FancyArrowPatch((6,5.26),(6,4.96),arrowstyle='->',mutation_scale=18,color='#506074'))
box(.6,.56,10.8,1.73,'The same term controls inverse return',[
    r'$\widetilde T_a\widetilde T_{1/a}=I+\frac{1}{4a}D_a^*D_a$',
    r'$(D_a^*D_a x)_\rho=(a^{\mathrm{Re}\rho}-a^{1-\mathrm{Re}\rho})^2x_\rho$'], '#f7eef8')
ax.add_patch(FancyArrowPatch((6,2.67),(6,2.45),arrowstyle='->',mutation_scale=18,color='#506074'))
ax.text(6,.15,'Proofs: GTAH0–GTAH5. J exchanges ρ with 1−conjugate(ρ); a > 0. Original factors and full jets remain in the source.',ha='center',fontsize=8.8,color='#465568')
fig.savefig(base/'positive_transfer_defect.png',dpi=175,bbox_inches='tight',facecolor='white')
fig.savefig(base/'positive_transfer_defect.svg',bbox_inches='tight',facecolor='white')
plt.close(fig)
