from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

OUT=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'mathtext.fontset':'dejavusans'})
ink='#182e40'; blue='#176b91'; green='#247650'; orange='#ab5720'

def box(ax,x,y,w,h,txt,color=blue,size=13):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.009',
                              facecolor=color+'10',edgecolor=color,lw=1.6))
    ax.text(x+w/2,y+h/2,txt,ha='center',va='center',color=ink,fontsize=size,linespacing=1.7)

def arrow(ax,start,end,label='',color=ink,offset=(0,0)):
    ax.add_patch(FancyArrowPatch(start,end,arrowstyle='-|>',mutation_scale=16,lw=1.5,color=color))
    ax.text((start[0]+end[0])/2+offset[0],(start[1]+end[1])/2+offset[1],label,
            ha='center',va='center',color=color,fontsize=11)

def save(fig,name):
    fig.savefig(OUT/(name+'.png'),dpi=180,facecolor='white',bbox_inches='tight')
    fig.savefig(OUT/(name+'.svg'),facecolor='white',bbox_inches='tight')
    plt.close(fig)

fig=plt.figure(figsize=(15,10.5)); ax=fig.add_axes([0.025,0.025,.95,.95]);ax.axis('off')
ax.text(.02,.97,'The original classes and the exact closure step',fontsize=21,weight='bold',color=ink)
ax.text(.02,.929,r'$D=[P\,\longrightarrow\,A]$ keeps all endpoint and extra closed coefficients in $P$.',fontsize=13,color=ink)
box(ax,.02,.735,.20,.125,r'$Q=A/J$'+'\nOriginal full quotient')
box(ax,.365,.735,.24,.125,r'$\mathcal{H}_{\sigma,\delta}/J$'+'\nAlgebraic cohomology')
box(ax,.75,.735,.225,.125,r'$Q_{\sigma,\delta}$'+'\nHausdorff quotient',orange)
arrow(ax,(.232,.796),(.353,.796),'injective',offset=(0,.027))
arrow(ax,(.617,.796),(.738,.796),'quotient',offset=(0,.027),color=orange)
ax.text(.655,.69,r'kernel $C_{\sigma,\delta}/J$',fontsize=12,ha='center',color=orange)
ax.text(.02,.643,r'$\mathcal{H}_{\sigma,\delta}=L^2(u^{2\sigma-1}(1+(\log u)^2)^\delta\,du),\qquad C_{\sigma,\delta}=\overline{J}^{\mathcal{H}_{\sigma,\delta}}$',fontsize=15,color=ink)
box(ax,.02,.423,.445,.16,'Critical-line family only\n'+r'$Q\ \longrightarrow\ \prod_{N\geq1}Q_{1/2,N}$'+'\n'+r'common kernel $K_{\rm off}=I_{\rm line}/I$',orange)
box(ax,.535,.423,.44,.16,'All vertical weights and derivative orders\n'+r'$Q\ \hookrightarrow\ \prod_{0<\sigma<1}\quad\prod_{N\geq1}Q_{\sigma,N}$'+'\nEvery original zero jet is detected.',green)
ax.text(.02,.362,r'$\mathrm{Spec}(T_p\mid Q_{\sigma,\delta})\subseteq\{z:|z|=p^\sigma\}$',fontsize=16,color=ink)
ax.text(.02,.315,r'$Rb(u)=u^{-1}b(u^{-1})$ gives an isometry $Q_{\sigma,\delta}\to Q_{1-\sigma,\delta}$.',fontsize=14,color=ink)
ax.text(.02,.267,r'The paired radii multiply to $p$; this does not set either radius to $\sqrt{p}$.',fontsize=13,color=ink)
box(ax,.02,.111,.955,.105,r'$B_\zeta|_{K_{\rm off}\times K_{\rm off}}$ is nondegenerate.'+'\nThe exact original contour pairing still detects any nonzero class lost by the critical family.',green,13)
ax.text(.02,.04,'Proofs: VWR2–VWR8; WHR2–WHR10. Weighted spectral mechanism: Alain Connes (1998), §III and Appendix I.\nThese are coefficient maps; primitive Z₁/τ receives no addition, parity or numerical weight.',fontsize=10,color=ink)
save(fig,'FULL_VERTICAL_WEIGHT_RETURN')

fig=plt.figure(figsize=(15,10)); ax=fig.add_axes([.04,.58,.92,.39]);ax.axis('off')
ax.text(0,.96,'The off-critical observable retains the full arithmetic formula',fontsize=20,weight='bold',color=ink)
ax.text(.01,.73,r'$\Theta_{\rm off}(b)=F(0)+F(1)+A_\infty(b)-P_\zeta(b)-\sum_{\mathrm{Re}\,\rho=1/2}m_\rho F(\rho)$',fontsize=17,color=ink)
ax.text(.01,.55,r'$P_\zeta(b)=\sum_{n\geq2}\Lambda(n)\,[b(n)+n^{-1}b(n^{-1})],\qquad F=M_0b$',fontsize=15,color=ink)
ax.text(.01,.34,r'$A_\infty(b)=\frac{1}{2\pi}\int_{\mathbb{R}}F(\frac{1}{2}+it)\,[\frac{1}{2}\psi(\frac{1}{4}+\frac{it}{2})+\frac{1}{2}\psi(\frac{1}{4}-\frac{it}{2})-\log\pi]\,dt$',fontsize=15,color=ink)
ax.text(.01,.12,'All sums and integrals converge on the original test space A. Finite trivial-zero returns remain in VWR10.4.',fontsize=12,color=ink)

ax=fig.add_axes([.07,.22,.53,.30]);x=np.linspace(-2.05,2.05,6000)
def bump(x):
    y=np.zeros_like(x);take=np.abs(x)<.1
    y[take]=np.exp(1-1/(1-(10*x[take])**2))
    return y
y=bump(x-1)+bump(x+1)-bump(x-1.5)-bump(x+1.5)
ax.plot(x,y,color=blue,lw=2);ax.axhline(0,color=ink,lw=.7)
ax.scatter([-2,-1,0,1,2],[0,1,0,1,0],color=orange,zorder=3,s=45)
ax.set(xlim=(-2.05,2.05),ylim=(-1.25,1.25),xlabel='Original real source coordinate v',ylabel=r'$h_*(v)$')
ax.set_xticks([-2,-1.5,-1,0,1,1.5,2]);ax.grid(alpha=.16)
ax.set_title('An exact even Schwartz test with both endpoint conditions satisfied',fontsize=12,color=ink)
ax=fig.add_axes([.64,.22,.32,.30]);ax.axis('off')
ax.text(.01,.87,r'$h_*\in S,\quad b_*=\Sigma h_*\in J$',fontsize=16,color=ink)
ax.text(.01,.65,r'$b_*(1)=2$',fontsize=22,color=blue)
ax.text(.01,.43,r'$\Theta_{\rm off}(b_*)=0$',fontsize=20,color=green)
ax.text(.01,.12,'Thus a nonzero off-critical observable\ncannot be a scalar multiple of b(1).',fontsize=12,color=ink,linespacing=1.6)
fig.text(.06,.112,r'$h_*(v)=\varphi(v-1)+\varphi(v+1)-\varphi(v-3/2)-\varphi(v+3/2)$',fontsize=15,color=ink)
fig.text(.06,.062,r'Plot uses $\varphi(x)=\exp(1-1/(1-100x^2))$ for $|x|<1/10$, and zero elsewhere. Orange points are integers.',fontsize=11,color=ink)
fig.text(.06,.024,'Proof: VWR10. Sources: retained original explicit formula; Connes–Consani, On the Jacobian of Spec Z (2026), §8.\nThe plot is a proved source test, not a plot of zeta zeros or a claimed sign for the full Weil form.',fontsize=10,color=ink)
save(fig,'ORIGINAL_ARITHMETIC_CLOSURE_DEFECT')
print('Rendered two PNG/SVG mathematical figures.')
