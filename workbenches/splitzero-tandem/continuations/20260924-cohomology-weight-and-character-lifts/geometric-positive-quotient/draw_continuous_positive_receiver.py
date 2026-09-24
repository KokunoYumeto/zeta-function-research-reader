"""Exact maps in CFP/CPS; no numerical sample or assumed off-line zero."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

base=Path(__file__).resolve().parent
fig,ax=plt.subplots(figsize=(12.6,8.4))
fig.patch.set_facecolor('#fbfcfe')
ax.set(xlim=(0,12.6),ylim=(0,8.4));ax.axis('off')
ink='#183047';blue='#12618a';green='#176653';amber='#95651a'
def box(x,y,w,h,label,sub,color):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.1',
        facecolor='white',edgecolor=color,linewidth=1.6))
    ax.text(x+w/2,y+h-.30,label,ha='center',va='center',fontsize=17,color=color)
    ax.text(x+w/2,y+.36,sub,ha='center',va='center',fontsize=11,color=ink)
def arrow(a,b,label,dx=0,dy=.16,color=blue):
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=15,lw=1.6,color=color))
    ax.text((a[0]+b[0])/2+dx,(a[1]+b[1])/2+dy,label,ha='center',va='center',fontsize=11,color=color)
ax.text(.25,8.03,'All continuous positive transfer-adjoint forms on the original source',
    fontsize=18,weight='bold',color=ink)
ax.text(.25,7.60,r'$B(T_nF,G)=B(F,nT_{1/n}G)$ for every recovered integer $n$; all multiplicities retained',
    fontsize=12,color=ink)
box(.35,5.70,3.25,1.15,r'$N_O$',r'off-line values vanish; jets remain',green)
box(4.75,5.70,3.1,1.15,r'$Q=\mathcal{B}/\mathcal{I}$',r'original full zero-jet source',blue)
box(9.05,5.70,3.1,1.15,r'$R=Q/N_O$',r'actual specialization obstruction',amber)
arrow((3.7,6.3),(4.64,6.3),'inclusion',dy=.28,color=green)
arrow((7.96,6.3),(8.94,6.3),'quotient',dy=.28,color=amber)
box(3.65,2.65,5.30,1.80,r'$\mathcal{S}_L$',
    r'$\|x\|_k^2=\sum_{\rho=1/2+i\gamma}m_\rho(1+\gamma^2)^k|x_\rho|^2<\infty$'+'\n'
    +'for every integer '+r'$k\geq0$'+'; complete positive receiver',green)
arrow((1.98,5.59),(4.46,4.57),r'kernel $N_0$',dx=.50,dy=.26,color=green)
arrow((6.3,5.59),(6.3,4.56),r'$E_L$; kernel $N_L$',dx=1.38,dy=0,color=blue)
ax.text(.48,4.08,'Both images are dense\nfor every displayed seminorm.\nOriginal Fréchet topologies\nare retained separately.',
    fontsize=11,color=ink,linespacing=1.5)
ax.text(10.6,4.68,r'$\mathcal{P}(R)=\{0\}$',ha='center',fontsize=17,color=amber)
ax.text(10.6,3.94,'Every compatible continuous\npositive form on this exact\nquotient vanishes.',ha='center',
    fontsize=11,color=ink,linespacing=1.5)
ax.text(10.6,3.05,r'No conclusion $R=0$ is inserted.',ha='center',fontsize=10.5,color=amber)
ax.text(.4,1.87,r'$B_c(F,G)=\sum_{\rho\in\mathcal{Z}_L}m_\rho c_\rho F(\rho)\overline{G(\rho)},\qquad c_\rho\geq0$ with polynomial growth',
    fontsize=15,color=ink)
ax.text(.4,1.28,r'$W=W_L+W_O$ remains the original Weil form. The positive receiver returns $W_L$; the full $W_O$ is retained.',
    fontsize=12,color=ink)
ax.text(.4,.66,'Exact comparison diagram, not a zero-location plot. Full proofs: CFP and CPS1–CPS6; source quotient: AST1–AST5.',
    fontsize=10.5,color=ink)
ax.text(.4,.25,'Coefficient source: Connes–Consani, arXiv:0903.2024v3, §5. No operation or coordinate is assigned to τ.',
    fontsize=10.5,color=ink)
fig.savefig(base/'continuous_positive_receiver.png',dpi=170,bbox_inches='tight',facecolor=fig.get_facecolor())
fig.savefig(base/'continuous_positive_receiver.svg',bbox_inches='tight',facecolor=fig.get_facecolor())
plt.close(fig)

