"""Exact source reconstruction and positive-transfer compression diagram."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

base=Path(__file__).resolve().parent
fig,ax=plt.subplots(figsize=(14,10.5))
ax.set(xlim=(0,14),ylim=(0,10.5))
ax.axis('off')
def box(x,y,w,h,color):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.13',ec='#52627a',fc=color,lw=1.5))
def label(x,y,s,size=14,weight='normal',**kw):
    ax.text(x,y,s,ha='center',va='center',fontsize=size,fontweight=weight,**kw)
def arrow(x,y,X,Y):
    ax.annotate('',xy=(X,Y),xytext=(x,y),arrowprops=dict(arrowstyle='->',lw=1.6,color='#52627a'))

label(7,10.15,'The positive quotient and the complete source it comes from',21,'bold')
label(7,9.65,'All actual zeros and multiplicities; no numerical cutoff or assumed purity',13,color='#52627a')
box(.45,6.15,13.1,2.95,'#edf3fb')
label(7,8.8,'FULL-JET SOURCE RECONSTRUCTION',15,'bold')
label(7,8.28,r'$\mathcal{Q}=\mathcal{B}/\mathcal{I}\ \longrightarrow\ Q_{\rm line}^{\rm jet}\oplus Q_{\rm off}^{\rm jet}\ \longrightarrow\ C_{\rm rec}$',21)
label(7,7.72,r'$[F]\longmapsto([F]_{J_L},[F]_{J_O}),\qquad ([f],[g])\longmapsto[f-g]$',17)
label(7,7.13,r'$C_{\rm rec}=\mathcal{B}/(J_L+J_O),\qquad J_L\cap J_O=\mathcal{I}$',19)
label(7,6.57,'Compatible pairs reconstruct the full source; their higher jets remain.',13)
arrow(7,5.98,7,5.32)
label(9.55,5.65,r'$E:\ [F]\mapsto(F(\rho))_\rho$',15)

box(.45,2.62,6.15,2.55,'#eaf5ef')
box(7.38,2.62,6.15,2.55,'#fcf0e9')
label(3.52,4.78,'POSITIVE RECEIVER',15,'bold')
label(10.45,4.78,'RETAINED COMPLEMENT',15,'bold')
label(3.52,4.20,r'$H_{\rm line},\quad \Re\rho=\frac{1}{2}$',20)
label(10.45,4.20,r'$H_{\rm off},\quad \Re\rho\ne\frac{1}{2}$',20)
label(3.52,3.58,r'$T_n^*=nT_{1/n},\qquad W_L(x,x)=\|x\|^2$',17)
label(10.45,3.58,r'$W_O(x,y)=\sum_{\rho\ {\rm off}}m_\rho x_\rho\overline{y_{\rho^\#}}$',17)
label(3.52,2.98,r'$P_{\rm line}=\mathrm{s}\!-\!\lim_{R\to\infty}e^{-R D_a^*D_a}$',18)
label(10.45,2.98,r'$H_{\rm off}=\overline{\mathrm{ran}(D_a^*D_a)},\qquad a>1$',18)
label(3.6,5.58,r'$H=H_{\rm line}\oplus H_{\rm off}$',16)

box(.45,.62,13.1,1.5,'#f3f4f8')
label(7,1.82,'THE ORIGINAL ARITHMETIC FORM IS RECONSTRUCTED EXACTLY',14,'bold')
label(7,1.25,r'$W_L+W_O=A(0)+A(1)+\mathcal{A}_\infty(v)-P_{\rm hist}(v)$',20)
label(7,.83,'Gamma, powers of pi, endpoints, prime repetitions and finite trivial-divisor terms stay in PSC5.',12)
label(7,.2,'Proofs: PSC1–PSC8 and PTQ.  Integer n is the geometric cover degree; a is a coefficient parameter.',11,color='#52627a')
fig.savefig(base/'positive_quotient_source.png',dpi=150,bbox_inches='tight',facecolor='white')
fig.savefig(base/'positive_quotient_source.svg',bbox_inches='tight',facecolor='white')
plt.close(fig)
