"""Exact operator completion, full zero jets, and the multiplicity trace."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

root=Path(__file__).resolve().parent
fig, ax=plt.subplots(figsize=(18,11))
fig.patch.set_facecolor('#fbfaf7')
ax.set_xlim(0,18); ax.set_ylim(0,11); ax.axis('off')
def text(x,y,s,size=19,**kw):
    ax.text(x,y,s,ha='center',va='center',fontsize=size,color='#20323b',**kw)
def box(x,y,w,h,color):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.13',
                 facecolor=color,edgecolor='#567380',linewidth=1.4))
def arrow(a,b):
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=20,
                               color='#267788',linewidth=1.8))
text(9,10.6,'The positive completion retains the multiplicity trace',25,weight='bold')
text(9,10.05,r'$A=\log p_0,\quad B=2\pi,\quad r\in\mathbb{Q}_{>0},\quad \mathbb{T}=\prod_{p\ \mathrm{prime}}S^1$',20)
box(.5,7.65,17,1.8,'#e7f0f6')
text(9,8.99,r'$U:\mathcal{H}_{\mathrm{geom}}^0\ \longrightarrow\ L^2(\mathbb{T},dm),\qquad Ue_r=\sqrt{ABr}\,z^{v(r)}$',23)
text(9,8.4,r'$\|\sum_r a_r e_r\|^2=AB\sum_r r|a_r|^2,\qquad dm=\prod_p d\theta_p/(2\pi)$',22)
text(9,7.89,r'Exact unitary; $F_p\mapsto\sqrt{p}\,z_p$, $V_p\mapsto\sqrt{p}\,z_p^{-1}$, $F_pV_p=p$.',18)
arrow((9,7.48),(9,6.9))
text(9,6.59,r'$\mathcal{A}=\mathbb{C}\otimes\mathcal{H}_{\mathbb{Z}}\quad\hookrightarrow\quad C(\mathbb{T}),\qquad \|a\|=\sup_{z\in\mathbb{T}}|\widehat a(z)|$',23)
text(9,6.07,'Faithful completion in the original geometric operator norm',17)
box(.5,3.65,8.1,1.8,'#f8eddb')
box(9.3,3.65,8.2,1.8,'#e7f3ed')
text(4.55,5.03,r'Full algebraic jet $J_{\rho,m}=\mathbb{C}[t]/(t^m)$',19)
text(4.55,4.47,r'$\pi_{\rho,m}(b_r)=r^\rho e^{(\log r)N}$',22)
text(4.55,3.94,'Every nilpotent coefficient remains in this action.',16)
text(13.4,5.03,r'Its exact trace: $\mathcal{T}_{\rho,m}(a)=m\chi_\rho(a)$',19)
text(13.4,4.47,r'$\mathcal{T}_{\rho,m}(f)=m f(z_\rho)$ on $\Re\rho=1/2$',21)
text(13.4,3.94,r'Positive and bounded for every multiplicity $m\geq1$.',16)
arrow((8.8,4.52),(9.08,4.52))
text(9,3.08,r'$\frac{1}{2\pi i}\oint_{|s-\rho|=\epsilon}h_a(s)\frac{\zeta^{\prime}(s)}{\zeta(s)}\,ds=m_\rho h_a(\rho)$',25)
text(9,2.45,'Original-zeta local residue; positive contour orientation; all other explicit-formula terms remain.',16)
text(9,1.87,r'$\rho=\sigma+i\gamma,\qquad a_{p,\rho}=F_p-\sqrt{p}\,e^{i\gamma\log p}b_1$',21)
text(9,1.3,r'$\mathcal{T}_{\rho,m}(a_{p,\rho}^{*}a_{p,\rho})=m(p^{1-\sigma}-\sqrt{p})(p^\sigma-\sqrt{p})<0\quad(\sigma\neq1/2)$',22)
text(9,.73,'This is an exact residue-block test. Positivity of the complete original Weil form remains unproved.',16)
text(9,.22,'Proofs: POSITIVE_COMPLETION_AND_ZERO_JETS.md, PCJ1–PCJ8 and PCJ10. No finite zero scan.',13)
fig.savefig(root/'positive_completion_trace.png',dpi=170,bbox_inches='tight',facecolor=fig.get_facecolor())
fig.savefig(root/'positive_completion_trace.svg',bbox_inches='tight',facecolor=fig.get_facecolor())
print(root/'positive_completion_trace.png')
