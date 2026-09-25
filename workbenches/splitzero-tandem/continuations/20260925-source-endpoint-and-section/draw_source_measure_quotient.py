"""Exact full-source measure quotient; no numerical zero placement."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

base=Path(__file__).resolve().parent
fig, ax=plt.subplots(figsize=(12.6,9.1))
fig.patch.set_facecolor('#fbfcfe')
ax.set(xlim=(0,12.6),ylim=(0,9.1)); ax.axis('off')
ink='#183047'; blue='#12618a'; green='#176653'; amber='#95651a'
def box(x,y,w,h,title,subtitle,color):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.1',facecolor='white',edgecolor=color,lw=1.6))
    ax.text(x+w/2,y+h-.3,title,ha='center',va='center',fontsize=17,color=color)
    ax.text(x+w/2,y+.36,subtitle,ha='center',va='center',fontsize=10.8,color=ink)
def arrow(a,b,label,dx=0,dy=.22,color=blue,fs=11):
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=15,lw=1.6,color=color))
    ax.text((a[0]+b[0])/2+dx,(a[1]+b[1])/2+dy,label,ha='center',va='center',fontsize=fs,color=color)
ax.text(.3,8.73,'What each positive source pairing retains after the original quotient',fontsize=17.2,weight='bold',color=ink)
ax.text(.3,8.27,r'$\Gamma=\{\gamma\in\mathbb{R}:\zeta(1/2+i\gamma)=0\}$; original multiplicities and full source jets remain explicit',fontsize=11.5,color=ink)
box(.4,6.55,3.3,1.12,r'$\mathcal{I}=\Theta J$',r'actual complete summation image',amber)
box(4.67,6.55,3.3,1.12,r'$\mathcal{B}$',r'original entire-function source',blue)
box(8.94,6.55,3.3,1.12,r'$Q=\mathcal{B}/\mathcal{I}$',r'original full-jet quotient',green)
arrow((3.8,7.1),(4.55,7.1),'inclusion',dy=.26,color=amber,fs=8.5)
arrow((8.07,7.1),(8.82,7.1),'quotient',dy=.26,color=green,fs=8.5)
box(.4,3.97,3.3,1.35,r'$L^2(\mathbb{R}\setminus\Gamma,\mu)$',r'exact closure of the image of $\mathcal{I}$',amber)
box(4.67,3.97,3.3,1.35,r'$H_\mu=L^2(\mathbb{R},\mu)$',r'positive source completion',blue)
box(8.94,3.97,3.3,1.35,r'$L^2(\Gamma,\mu|_\Gamma)$',r'exact completed quotient',green)
arrow((2.05,6.42),(2.05,5.45),'dense image',dx=1.03,dy=0,color=amber)
arrow((6.32,6.42),(6.32,5.45),r'$j_\mu$: dense image',dx=1.25,dy=0,color=blue)
arrow((10.59,6.42),(10.59,5.45),r'kernel $N_\mu$',dx=1.0,dy=0,color=green)
arrow((3.8,4.64),(4.55,4.64),'inclusion',dy=.27,color=amber,fs=8.5)
arrow((8.07,4.64),(8.82,4.64),r'$h\mapsto h|_\Gamma$',dy=.32,color=green,fs=9)
ax.text(.4,3.20,r'$\inf_{G\in\mathcal{I}}\|j_\mu(F-G)\|^2=\sum_{\rho=1/2+i\gamma}m_\rho c_\rho|F(\rho)|^2,\quad \mu\{\gamma\}=m_\rho c_\rho$',fontsize=15,color=ink)
ax.text(.4,2.55,r'$\mu_0=(2/\pi)\,dt$: completed quotient is zero; original Fréchet quotient $Q$ is retained.',fontsize=12,color=ink)
ax.text(.4,2.05,r'$\mu_0+\sum m_\rho\delta_\gamma$: completion keeps the continuous and atomic observations in separate summands.',fontsize=11.7,color=ink)
ax.text(.4,1.46,r'Original $W=W_L+W_O$. The positive quotient returns $W_L$; the entire $W_O$ remains in the source comparison.',fontsize=11.8,color=ink)
ax.text(.4,.91,'Exact comparison diagram, not a zero-location plot. Full proofs: SPF0–SPF11 and SMC1–SMC9.',fontsize=10.5,color=ink)
ax.text(.4,.48,'Coefficient source: Connes–Consani, arXiv:0903.2024v3, §5. Earlier Mellin density: M9; exact source image: SSI.',fontsize=10.3,color=ink)
ax.text(.4,.10,'The support labels remain attached; no arithmetic value, addition, parity or coordinate is assigned to τ.',fontsize=10.3,color=ink)
fig.savefig(base/'source_measure_quotient.png',dpi=180,bbox_inches='tight',facecolor=fig.get_facecolor())
fig.savefig(base/'source_measure_quotient.svg',bbox_inches='tight',facecolor=fig.get_facecolor())
plt.close(fig)
