"""Exact extension-class/source/residue maps; no sampled zero coordinates."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch

b=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','mathtext.fontset':'dejavusans'})
fig,ax=plt.subplots(figsize=(13,10));ax.set(xlim=(0,13),ylim=(0,10));ax.axis('off')
ax.text(6.5,9.65,'The actual extension class reaches the full original residue receiver',ha='center',fontsize=18,weight='bold')
ax.text(6.5,9.23,'Every actual zero and multiplicity; the two embeddings retain all jets',ha='center',fontsize=12,color='#465568')

def box(x,y,w,h,title,lines,color):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.12',facecolor=color,edgecolor='#56647a',lw=1.3))
    ax.text(x+w/2,y+h-.18,title,ha='center',va='top',fontsize=12,weight='bold')
    for i,line in enumerate(lines):ax.text(x+w/2,y+h-.65-i*.42,line,ha='center',va='top',fontsize=12)
def arrow(start,end,label=None,xy=None):
    ax.add_patch(FancyArrowPatch(start,end,arrowstyle='->',mutation_scale=17,color='#56647a',lw=1.2))
    if label:ax.text(*xy,label,ha='center',va='center',fontsize=11,color='#24384d')

box(.4,6.65,4.3,2,'Original extension-class module',[
    r'$\mathscr{N}_0=M e_0\cong M/\mathfrak{a}$',
    r'$h e_0\quad\longleftrightarrow\quad[h]_{\mathfrak{a}}$',
    r'$g_t(s)=e^{t s^2},\quad t>0$'],'#eef4fc')
box(8.3,6.65,4.3,2,'Actual entire source quotient',[
    r'$\mathcal{Q}=\mathcal{B}/\mathcal{I}$',
    r'$b_t(h e_0)=[g_t h]_{\mathcal{I}}$',
    r'$j([F])=F e_0$'],'#eef8f2')
arrow((4.85,7.85),(8.13,7.85),r'$b_t$ injective',(6.5,8.13))
arrow((8.13,7.2),(4.85,7.2),r'$j$ injective',(6.5,6.94))
ax.text(6.5,6.32,r'Both composites multiply by $g_t$; neither arrow is onto.',ha='center',fontsize=11,color='#465568')

box(7.3,3.95,5.05,1.55,'Positive value Hilbert space',[
    r'$H=\ell^2(\mathscr{Z},m_\rho)$',
    r'$E_0 b_t(h e_0)_\rho=g_t(\rho)h(\rho)$'],'#fff5e7')
box(.65,3.95,5.05,1.55,'Full strong residue space',[
    r'$\mathcal{H}_{\rm res}\cong\mathcal{Q}^{\prime}_{\beta}$',
    r'$\mathsf{S}_t=\mathsf{A} E_0 b_t$'],'#f4eef9')
arrow((10.5,6.17),(10.5,5.67),r'$E_0$',(11.0,5.94))
arrow((7.12,4.65),(5.86,4.65),r'$\mathsf{A}$',(6.5,4.98))
ax.text(6.5,3.57,"A is injective and anti-linear; the trace kernel is the value-vanishing ideal modulo a.",ha="center",fontsize=11)

box(.55,.75,11.9,2.05,'The source Gaussian factor stays in both exact observations',[
    r'$W_t(h,k)=\sum_{\rho}m_\rho e^{t\{\rho^2+(1-\rho)^2\}}h(\rho)\overline{k(\rho^\#)}$',
    r'$\mathfrak{d}_{a,t}(e_0,e_0)=\sum_{\rho}m_\rho e^{2t(\sigma^2-\gamma^2)}(a^{\sigma}-a^{1-\sigma})^2$',
    r'$\rho=\sigma+i\gamma,\quad\rho^\#=1-\overline{\rho},\quad a>1$'],'#f5f7fa')
ax.text(6.5,.27,'Proofs: ECR1-ECR6, RTT5-RTT6 and FOD4-FOD6. Original prime, Gamma, endpoint and finite trivial-divisor terms remain in ECR4.',ha='center',fontsize=9,color='#465568')
fig.savefig(b/'extension_class_receiver.png',dpi=180,bbox_inches='tight',facecolor='white')
fig.savefig(b/'extension_class_receiver.svg',bbox_inches='tight',facecolor='white')
plt.close(fig)
