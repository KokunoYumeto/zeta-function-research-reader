"""Exact structural diagrams for TS11--34; no sampled spectral data."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

OUT=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,
                     'mathtext.fontset':'dejavusans','pdf.fonttype':42})
def panel(ax,x,y,w,h,title,lines,color='#eaf2f8'):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.018',
                 fc=color,ec='#29465b',lw=1.1))
    ax.text(x+w/2,y+h-.045,title,ha='center',va='top',weight='bold')
    ax.text(x+w/2,y+h/2-.016,lines,ha='center',va='center',linespacing=1.5)
def arrow(ax,p,q,label='',dy=.018):
    ax.annotate('',q,p,arrowprops={'arrowstyle':'->','lw':1.5,'color':'#29465b'})
    if label: ax.text((p[0]+q[0])/2,(p[1]+q[1])/2+dy,label,
                     ha='center',va='center',fontsize=10)
def save(fig,name):
    fig.savefig(OUT/(name+'.pdf'),bbox_inches='tight')
    fig.savefig(OUT/(name+'.png'),dpi=165,bbox_inches='tight')
    plt.close(fig)

fig,ax=plt.subplots(figsize=(11,7.5)); ax.set(xlim=(0,1),ylim=(0,1)); ax.axis('off')
ax.text(.5,.98,'The actual supported-zero action and its computed metric defect',
        ha='center',va='top',fontsize=15,weight='bold')
panel(ax,.03,.63,.36,.24,'Original arithmetic source plane',
      '$f=af_c+bf_s$\n$G=\\mathrm{diag}(K_c,K_s)$\n$50<K_c,K_s<64$')
panel(ax,.61,.63,.36,.24,'Original even-source prime boundary',
      '$Uf=af_c+bf_s^{\\prime}$\n$(m_0,m_1)^T=M(a,b)^T$\n$\\mathcal{B}_p f=[(t_p-1)\\otimes Uf]$')
arrow(ax,(.40,.76),(.60,.76),'$U,\\ m,\\ \\mathcal{B}_p$',.04)
panel(ax,.03,.27,.36,.24,'Exact action in the source coordinates',
      '$E_T(a,b)^T=(a,c(T)a)^T$\n$c(T)=(\\kappa_T R-A)/B$\n$E_T^2=E_T$')
panel(ax,.61,.27,.36,.24,'Multiplication by supported zero',
      '$J_T(m_0,m_1)^T=(\\kappa_Tm_1,m_1)^T$\n$\\kappa_T=(4\\pi T)^{-1/2}$\n$T>0$', '#f6f0e3')
arrow(ax,(.21,.62),(.21,.52))
arrow(ax,(.79,.62),(.79,.52))
arrow(ax,(.60,.39),(.40,.39),'$E_T=M^{-1}J_TM$',.045)
ax.text(.5,.16,'$P_T$: the $G$-orthogonal projection onto $\\mathrm{im}(E_T)$',ha='center')
ax.text(.5,.105,'$N_T=E_T-P_T$,  $N_T^2=0$,  '
        '$\\|N_T\\|_G^2=(K_s/K_c)c(T)^2$',ha='center',fontsize=13)
ax.text(.5,.04,'$N_T=0$ exactly at $T_*=(R/A)^2/(4\\pi)$; theta time stays $t=1/32$.',ha='center')
save(fig,'SOURCE_ACTION')

fig,ax=plt.subplots(figsize=(11,7)); ax.set(xlim=(0,1),ylim=(0,1)); ax.axis('off')
ax.text(.5,.98,'The local geometric point and the full arithmetic module support',
        ha='center',va='top',fontsize=14,weight='bold')
ax.text(.035,.85,'$\\mathrm{Spec}\\,G_L(\\mathcal{O})$',fontsize=13)
for x,label in [(.32,'$Q_J^{\\mathcal{O}}$'),(.59,'$P_e^{\\mathcal{O}}$'),(.86,'$P_{(T-T_*)}^{\\mathcal{O}}$')]:
    ax.text(x,.80,label,ha='center',fontsize=14)
arrow(ax,(.37,.815),(.53,.815),'$\\subsetneq$',.045)
arrow(ax,(.66,.815),(.78,.815),'$\\subsetneq$',.045)
ax.text(.86,.71,'$H^j=\\mathcal{O}/(T-T_*)$',ha='center',color='#8b3d18')
ax.text(.035,.51,'$\\mathrm{Spec}\\,G_L(\\mathbb{Z})$',fontsize=13)
for x,label in [(.32,'$Q_J^{\\mathbb{Z}}$'),(.59,'$P_e^{\\mathbb{Z}}$'),(.86,'$P_{(p)}^{\\mathbb{Z}}$')]:
    ax.text(x,.46,label,ha='center',fontsize=14)
arrow(ax,(.37,.475),(.53,.475),'$\\subsetneq$',.04)
arrow(ax,(.66,.475),(.78,.475),'$\\subsetneq$',.04)
arrow(ax,(.32,.76),(.32,.51))
arrow(ax,(.59,.76),(.59,.51))
arrow(ax,(.84,.67),(.62,.52))
ax.text(.405,.64,'prime pullback\nunder integer constants',fontsize=10,ha='center')
ax.text(.855,.34,'every integer prime $p$',ha='center',fontsize=10)
ax.plot([.57,.90],[.395,.395],color='#b55b22',lw=4)
ax.text(.72,.27,'$\\mathrm{Supp}_{G_L(\\mathbb{Z})}\\mathrm{Res}\\,H^j=V(e)$',
        ha='center',fontsize=14,color='#8b3d18')
ax.text(.5,.17,'$J$ ranges over all proper meet-prime ideals of the original lattice $L$.',ha='center')
ax.text(.5,.10,'Horizontal arrows: prime inclusions. Downward arrows: the actual spectrum map.',ha='center',fontsize=10)
ax.text(.5,.045,'The restricted module retains all ordinary primes, even though the complex chart misses them.',ha='center',fontsize=10)
save(fig,'PRIME_SUPPORT')
