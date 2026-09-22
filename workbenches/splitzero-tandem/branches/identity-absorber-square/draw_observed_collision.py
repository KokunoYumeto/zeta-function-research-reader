"""Reproduce the symbolic diagram of OC5–OC17; no sampled arithmetic data."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

root=Path(__file__).resolve().parent
fig=plt.figure(figsize=(14,10),facecolor='#faf9f6')
ax=fig.add_axes([0,0,1,1]);ax.set(xlim=(0,14),ylim=(0,10));ax.axis('off')
ink='#182d43';blue='#176987';orange='#a34e25'
def box(x,y,w,h,title,lines,color=blue):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.1',facecolor='white',edgecolor=color,linewidth=1.5))
    ax.text(x+.2,y+h-.32,title,fontsize=16,color=color,weight='bold',va='top')
    for i,line in enumerate(lines):ax.text(x+.2,y+h-.86-.47*i,line,fontsize=14,color=ink,va='top')
def arrow(a,b,label=''):
    ax.annotate('',xy=b,xytext=a,arrowprops={'arrowstyle':'->','color':ink,'lw':1.6})
    if label:ax.text((a[0]+b[0])/2,(a[1]+b[1])/2+.17,label,ha='center',fontsize=13,color=ink)
ax.text(.5,9.55,'The observed collision retains the signed current',fontsize=23,color=ink,weight='bold')
ax.text(.5,9.13,r'$a=u^*u>0,\quad r=u^*v,\quad \Delta=(u^*u)(v^*v)-|u^*v|^2>0$',fontsize=16,color=ink)
box(.5,6.55,3.5,2.05,'Original family · OC2',[r'$F(s)=R+sP_e$',r'$F(s)^2=sF(s)$',r'$M(s)=C+F(s)$'])
box(5.15,6.55,3.65,2.05,'Observation · OC5–6',[r'$F_B(s)=(\epsilon v+su)u^*$',r'$F_B(s)^2=\lambda(s)F_B(s)$',r'$\lambda(s)=as+\epsilon r$'])
box(10,6.55,3.5,2.05,'Collision · OC9',[r'$s_*=-\epsilon r/a$',r'$\widetilde R^2=0,\quad\widetilde R\ne0$',r'$\eta\mapsto\widetilde R$'],orange)
arrow((4.1,7.5),(5.05,7.5),r'$J^\dagger(\cdot)J$')
arrow((8.9,7.5),(9.9,7.5),r'$s=s_*$')
box(.5,3.42,6.05,2.68,'Signed displacement · OC11',[
    r'$\mathrm{Im}\,s_*=\mathrm{tr}\,W_B(0)/(2a)$',
    r'$W_B(s_*)=W_B(0)+2\epsilon\,\mathrm{Im}(r)\,gg^*$',
    r'$W_B(s)=W_B(0)\quad(s\in\mathbb{R})$',
    'Real collision exactly when the original trace is zero.'],orange)
box(7,3.42,6.5,2.68,'Full operator · OC12–17',[
    r'$M_B(s)=C_B+F_B(s)$',
    r'$p_s(\zeta)=p_t(\zeta)-(s-t)q_t(\zeta)$',
    r'$q_t(\zeta)=u^*\mathrm{adj}(\zeta I-M_B(t))u$',
    'The original Hermitian part remains in every inverse.'])
box(.5,.86,13,2.07,'Exact resolvent receiver · OC14–17',[
    r'$G_s=G_t+\dfrac{(s-t)G_tu\,u^*G_t}{1-(s-t)u^*G_tu},\qquad G_t=(\zeta I-M_B(t))^{-1}$',
    r'$1-(s-t)u^*G_tu=0\quad\Longrightarrow\quad\ker(\zeta I-M_B(s))=\mathbb{C} G_tu$',
    'The displayed inverse requires a nonzero denominator; its zero defines the stated eigenspace.'])
ax.text(.5,.35,'Proof: Observed collision OC1–OC17. Incoming programme source: DF1–12, public edition 4ba9285.',fontsize=11,color=ink)
(root/'figures').mkdir(exist_ok=True)
for ext in ['png','svg']:fig.savefig(root/'figures'/('18_observed_collision.'+ext),dpi=160,facecolor=fig.get_facecolor())
plt.close(fig)
print('Rendered symbolic collision diagram.')

fig=plt.figure(figsize=(14,9),facecolor='#faf9f6')
ax=fig.add_axes([0,0,1,1]);ax.set(xlim=(0,14),ylim=(0,9));ax.axis('off')
ax.text(.5,8.55,'The collision returns the original current kernel',fontsize=23,color=ink,weight='bold')
ax.text(.5,8.10,r'$D=\mathbb{C}[\eta]/\eta^2,\quad b_0=\epsilon\sqrt{\Delta},\quad N_*=b_0hg^*,\quad H=\{g,h\}^{\perp}$',fontsize=17,color=ink)
box(.5,5.30,6.05,2.38,'Retained support · OSP22–24',[
    r'$\mathbb{C}\times D\ \longrightarrow\ \mathrm{End}(B)$',
    r'$(k,c+\ell\eta)\mapsto k(I-P)+cP+\ell N_*$',
    r'$[\tau]\mapsto I,\quad[e]\mapsto P,\quad[n]\mapsto P+nN_*$'])
box(7,5.30,6.5,2.38,'Unchanged observed space · OSP24–26',[
    r'$B\simeq H\oplus D\quad\mathrm{over}\ \mathbb{C}\times D$',
    r'$\|c+\ell\eta\|^2=|c|^2+\epsilon^2\Delta|\ell|^2$',
    'This module is projective over the retained support algebra.'])
box(.5,2.61,13,2.20,'Restriction of coefficients exposes the exact defect · OSP25–26',[
    r'$D\hookrightarrow\mathbb{C}\times D,\qquad c+\ell\eta\mapsto(c,c+\ell\eta)$',
    r'$\mathrm{Tor}^{D}_i(\mathbb{C},B)=\ker N_*/\mathrm{im}\,N_*\simeq H=\ker W_B(0),\qquad i\geq1$',
    'Orthogonal projection to H is the displayed isomorphism; the original metric is retained.'],orange)
box(.5,.42,13,1.65,'Measured support retains its own weights · OSP10–14',[
    r'$A=UU^*,\quad P=U(U^*U)^{-1}U^*=\dfrac{(a+d)A-A^2}{\Delta}$',
    r'$A-A^2=J^\dagger\Pi(I-P_B)\Pi J$'])
for ext in ['png','svg']:fig.savefig(root/'figures'/('19_observed_support.'+ext),dpi=160,facecolor=fig.get_facecolor())
plt.close(fig)

fig=plt.figure(figsize=(14,10),facecolor='#faf9f6')
ax=fig.add_axes([0,0,1,1]);ax.set(xlim=(0,14),ylim=(0,10));ax.axis('off')
ax.text(.5,9.55,'The collision has a cotangent and integral Frobenius receiver',fontsize=21,color=ink,weight='bold')
ax.text(.5,9.07,r'$\lambda=as+b,\quad a\ne0;\qquad b=\epsilon r\ \mathrm{in\ the\ complex\ observation}$',fontsize=16,color=ink)
box(.5,6.07,6.1,2.52,'Relative cotangent · complex fibre',[
    r'$\mathcal{A}=\mathbb{C}[s,z]/z(z-\lambda)$',
    r'$L_{\mathcal{A}/\mathbb{C}[s]}=[\mathcal{A}\ \overset{2z-\lambda}{\longrightarrow}\ \mathcal{A}]$',
    r'$\Omega^1_{\mathcal{A}/\mathbb{C}[s]}\simeq\mathbb{C}[s]/(\lambda^2)$',
    r'$\mathrm{disc}(1,z)=\lambda^2$'])
box(7.1,6.07,6.4,2.52,'Derived collision · both degrees retained',[
    r'$s_*=-b/a,\quad D=\mathbb{C}[\eta]/\eta^2$',
    r'$L\otimes^{\mathbf{L}}_{\mathbb{C}[s]}\mathbb{C}_{s_*}=[D\ \overset{2\eta}{\longrightarrow}\ D]$',
    r'$H^{-1}=\mathbb{C}\eta,\qquad H^0=\mathbb{C}$',
    'The degree −1 term survives derived specialization.'],orange)
box(.5,3.59,13,1.95,'Absolute node map · every base coefficient retained',[
    r'$x=z,\quad y=z-as-b;\qquad z=x,\quad s=(x-y-b)/a$',
    r'$xy=0,\qquad d[z(z-as-b)]=(2z-as-b)\,dz-az\,ds$'])
box(.5,.68,13,2.37,'Common integral family · every prime, including 2',[
    r'$\mathbb{Z}[a,a^{-1},b,s,z]/z(z-as-b)$',
    r'$\phi(a)=a^p,\quad\phi(b)=b^p,\quad\phi(z)=z^p,\quad\phi(s)=\dfrac{(as+b)^p-b^p}{a^p}$',
    r'$\phi(as+b)=(as+b)^p;\quad\mathrm{the\ shifted\ relation\ is\ preserved}$'])
ax.text(.5,.24,'Exact proofs and source comparisons: Observed cotangent and Frobenius. Complex and p-adic models share the integral source.',fontsize=10.5,color=ink)
for ext in ['png','svg']:fig.savefig(root/'figures'/('20_observed_cotangent.'+ext),dpi=160,facecolor=fig.get_facecolor())
plt.close(fig)
print('Rendered support and cotangent diagrams.')


