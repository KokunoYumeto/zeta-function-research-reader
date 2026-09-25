from pathlib import Path
import numpy as np
import mpmath as mp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

H=Path(__file__).resolve().parent
mp.mp.dps=35
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'mathtext.fontset':'dejavusans'})
ink='#173449'; blue='#176b91'; orange='#b35721'; green='#29784b'

fig=plt.figure(figsize=(15,11))
ax=fig.add_axes([.04,.59,.92,.37]); ax.axis('off')
ax.text(0,.99,'A global original-source test of the positive harmonic trace',fontsize=20,weight='bold',color=ink)
ax.text(.01,.84,r'$G(s)=(s-1)\zeta(s)e^{s^2},\qquad F_\dagger(s)=G(s)\overline{G(1-\overline{s})}$',fontsize=18,color=ink)
ax.text(.01,.69,r'$F_\dagger=M_0 b_\dagger,\qquad b_\dagger\in J=\Sigma S,\qquad F_\dagger(0)=F_\dagger(1)=\exp(1)/2$',fontsize=16,color=ink)
for x,c,txt in [(.01,blue,'Original zero evaluations\n'+r'$\sum_\rho m_\rho F_\dagger(\rho)=0$'),(.54,orange,'Harmonic return\n'+r'$\int_{\mathbb{R}}|G(1/2+it)|^2 W_{\rm off}(t)\,dt$')]:
    ax.add_patch(FancyBboxPatch((x,.34),.445,.24,boxstyle='round,pad=.012',facecolor=c+'10',edgecolor=c,lw=1.5))
    ax.text(x+.2225,.46,txt,ha='center',va='center',fontsize=15,color=ink,linespacing=1.7)
ax.text(.01,.19,'The original test is zero in Q. Every off-critical Poisson kernel would add a positive contribution.',fontsize=13,color=ink)
ax.text(.01,.065,'This tests the comparison map. It does not assert that an off-critical zero exists.',fontsize=13,color=ink)

ax=fig.add_axes([.075,.235,.405,.29])
t=np.linspace(-3,3,421)
y=np.array([float(abs((mp.mpc(.5,float(v))-1)*mp.zeta(mp.mpc(.5,float(v)))*mp.exp(mp.mpc(.5,float(v))**2))**2) for v in t])
ax.plot(t,y,color=blue,lw=2)
ax.fill_between(t,0,y,color=blue,alpha=.10)
ax.set(xlabel=r'Original critical-line coordinate $t$',ylabel=r'$|G(1/2+it)|^2$',ylim=(0,max(y)*1.12))
ax.grid(alpha=.18)
ax.set_title('Exact function; numerical samples of its graph',fontsize=12,color=ink)

ax=fig.add_axes([.565,.235,.365,.29])
x=np.linspace(-5,5,701);d=.2;gamma=2.
p=d/(np.pi*(d*d+(x-gamma)**2))
ax.plot(x,p,color=orange,lw=2)
ax.fill_between(x,0,p,color=orange,alpha=.10)
ax.set(xlabel=r'Critical-line coordinate $t$',ylabel=r'$d/[\pi(d^2+(t-\gamma)^2)]$',ylim=(0,1.8))
ax.grid(alpha=.18)
ax.set_title(r'Kernel example: $d=0.2,\ \gamma=2$',fontsize=12,color=ink)
ax.text(.5,.89,'Not asserted zeta-zero coordinates',transform=ax.transAxes,ha='center',fontsize=10,color=ink)

fig.text(.07,.095,'All actual off-critical zeros enter Woff with their full multiplicities. The proof treats the whole convergent sum.\nSource: Alain Connes, math/9811068v1, §VIII Lemma 3. Exact Gram repair: FGR1–FGR6.\nOriginal-zeta source test and full arithmetic return: the accompanying harmonic-sweep derivation.\nThe diagram concerns receiving coefficient spaces; it assigns no number, parity or addition to primitive Z₁/τ.',fontsize=11,color=ink,linespacing=1.6)
for ext in ['png','svg']:fig.savefig(H/('HARMONIC_ORIGINAL_SOURCE_TEST.'+ext),dpi=180,facecolor='white',bbox_inches='tight')
plt.close(fig)

fig,(ax1,ax2)=plt.subplots(1,2,figsize=(14,5.8))
N=np.arange(1,15)
c=[]
for n in N:
    k=np.arange(-int(n),int(n)+1,dtype=float)
    a=2.**(k-n);b=3.**(k-n)
    c.append(a@b/np.sqrt((a@a)*(b@b)))
ax1.plot(N,c,'o-',color=blue,label='Full finite-window inner product')
ax1.axhline(np.sqrt(24)/5,color=orange,ls='--',label=r'Limit $\sqrt{24}/5$')
ax1.set(xlabel='Window half-length N',ylabel='Inner product of unit vectors',ylim=(.96,1.001))
ax1.set_title('Same-side vectors do not become orthogonal')
ax1.grid(alpha=.18);ax1.legend(fontsize=10)
x=np.linspace(-6,6,400);d=.2
ax2.plot(x,np.exp(d*x)+np.exp(-d*x),color=blue,label=r'Original pair: $e^{dt}+e^{-dt}$')
ax2.plot(x,2*np.exp(-d*np.abs(x)),color=green,label=r'Harmonic pair: $2e^{-d|t|}$')
ax2.fill_between(x,2*np.exp(-d*np.abs(x)),np.exp(d*x)+np.exp(-d*x),color=orange,alpha=.15,label=r'Difference: $2\sinh(d|t|)$')
ax2.set(xlabel='Logarithmic test coordinate t',ylabel='Pair kernel; common oscillation omitted here')
ax2.set_title(r'Exact pair comparison at example $d=0.2$')
ax2.grid(alpha=.18);ax2.legend(fontsize=10)
fig.subplots_adjust(bottom=.25,top=.87,wspace=.32)
fig.text(.06,.08,'Left: abstract exponents 2 and 3, not zeta zeros; all Gram entries are required (FGR2).\nRight: the common factor in the full formula is m exp(t/2) b(exp(t)) exp(iγt); FGR6 retains it explicitly.\nThe graphs illustrate exact formulas. No off-critical zeta zero is assumed. Source: Connes (1998), §VIII; repair FGR1–FGR6.',fontsize=10.5,color=ink,linespacing=1.5)
for ext in ['png','svg']:fig.savefig(H/('FULL_GRAM_AND_PAIR_KERNEL.'+ext),dpi=180,facecolor='white',bbox_inches='tight')
plt.close(fig)
fig=plt.figure(figsize=(14,9));ax=fig.add_axes([.045,.035,.91,.93]);ax.axis('off')
ax.text(.01,.98,'The exact prime action keeps its original-source return',fontsize=21,weight='bold',color=ink)
ax.text(.02,.86,r'$T_p b_\rho=p^\rho b_\rho+R_{p,\rho},\qquad R_{p,\rho}=\Sigma h_{p,\rho}\in J$',fontsize=19,color=blue)
ax.text(.02,.76,r'$h_{p,\rho}=\int_0^{\log p}p^\rho e^{-\rho t}T_{\exp(t)}h_0\,dt\in S$',fontsize=17,color=ink)
ax.add_patch(FancyBboxPatch((.025,.51),.95,.15,boxstyle='round,pad=.012',facecolor=orange+'10',edgecolor=orange,lw=1.5))
ax.text(.5,.60,r'$(p-p^{2\beta})\|b_\rho\|^2=2\Re\!\left(p^{\overline{\rho}}\langle b_\rho,R_{p,\rho}\rangle\right)+\|R_{p,\rho}\|^2$',ha='center',fontsize=17,color=ink)
ax.text(.5,.54,'All norms and pairings here use the original measure du, on actual representatives.',ha='center',fontsize=12,color=ink)
ax.text(.02,.415,r'$(\beta-\frac{1}{2})\|b_\rho\|^2=-\Re\langle b_\rho,b_0\rangle,\qquad (L-\rho)b_\rho=b_0$',fontsize=19,color=ink)
ax.text(.02,.29,r'$\mathcal{H}_{\rm off}(b_\dagger)=2\sum_\rho m_\rho\left|\Re\langle b_\rho,b_0\rangle\right|$',fontsize=21,color=green)
ax.text(.02,.205,'Reflection cancels the signed pairings in pairs. The absolute-value sum retains every contribution.',fontsize=13,color=ink)
ax.text(.02,.10,'Proof: OPD1–OPD5, including the explicit source preimage, every endpoint term, and convergence.\nOriginal summation: Connes–Consani (0903.2024v3), §5. Harmonic trace: Connes (math/9811068v1), §VIII.\nThe Hilbert norm is not a norm on Q=A/J. No numerical weight or addition is assigned to primitive Z₁/τ.',fontsize=11,color=ink,linespacing=1.6)
for ext in ['png','svg']:fig.savefig(H/('ORIGINAL_PRIME_RETURN_IDENTITY.'+ext),dpi=180,facecolor='white',bbox_inches='tight')
plt.close(fig)
print('Rendered three mathematical figures and their SVG sources.')
