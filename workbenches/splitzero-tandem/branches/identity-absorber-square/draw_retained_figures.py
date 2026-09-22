"""Reproduce exact class, filtration, contraction, and Frobenius diagrams."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
OUT=Path(__file__).resolve().parent/'figures'
plt.rcParams.update({'font.family':'DejaVu Sans','svg.fonttype':'none'})
fg='#183047';blue='#245eaa';green='#157564';red='#ad3545'
fig,axes=plt.subplots(1,2,figsize=(15,7.8),gridspec_kw={'width_ratios':[1,1.2]})
fig.patch.set_facecolor('#fcfcfa')
fig.subplots_adjust(top=.76,bottom=.21,left=.065,right=.97,wspace=.28)
fig.suptitle('The retained cross-effect has explicit independent classes',fontsize=22,color=fg,y=.97)
fig.text(.065,.86,r'$W=H^1U(\mathbb{Z}\longrightarrow\mathbb{Z}^2\longrightarrow\mathbb{Z})\ \cong\ (t-1)(u-1)\mathbb{Z}[t^{\pm1},u^{\pm1}]$',fontsize=17,color=fg)
ax=axes[0]
for a in range(-3,4):
    for b in range(-3,4):
        if a and b:
            ax.scatter(a,b,c=blue,s=45,zorder=3)
ax.axhline(0,color='#b1bac3',lw=1.5);ax.axvline(0,color='#b1bac3',lw=1.5)
ax.set(xlim=(-3.6,3.6),ylim=(-3.6,3.6),xticks=range(-3,4),yticks=range(-3,4),xlabel='first integer label a',ylabel='second integer label b')
ax.set_aspect('equal');ax.grid(alpha=.18)
ax.set_title('Finite sample of the full basis (a, b ≠ 0)',fontsize=13,pad=15)
ax.annotate(r'$w_{2,1}$',xy=(2,1),xytext=(.65,1.8),arrowprops={'arrowstyle':'->','color':fg},fontsize=15,color=fg)
ax.text(.5,-.14,r'$w_{a,b}=[r_{(a,b)}-r_{(a,0)}-r_{(0,b)}]$',transform=ax.transAxes,ha='center',fontsize=14,color=fg)
ax=axes[1];ax.axis('off')
rows=[('Every lattice label is a class',r'$w_{a,b}\longmapsto(t^a-1)(u^b-1)$',blue),
      ('Degree d of the augmentation filtration',r'$\mathrm{gr}_d W=\bigoplus_{i=1}^{d-1}\mathbb{Z}\,x^i y^{d-i}\quad(d\geq2)$',green),
      ('Exact scalar weight on that quotient',r'$[n](x^iy^{d-i})=n^d x^iy^{d-i}$',green),
      ('A different, torsion input retains more',r'$A=\mathbb{Z}/2,\ B=\mathbb{Z}/3:\quad W=\mathbb{Z}^2$',red)]
for k,(title,formula,c) in enumerate(rows):
    y=.96-k*.235
    ax.text(0,y,title,fontsize=14,weight='bold',color=c,transform=ax.transAxes)
    ax.text(0,y-.09,formula,fontsize=16,color=fg,transform=ax.transAxes)
ax.text(0,-.01,r'$F^dW=W\ (d\geq2),\quad \mathrm{gr}\,W=0,\quad \widehat W_I=0$',fontsize=15,color=red,transform=ax.transAxes)
fig.text(.065,.075,r'$x=t-1,\quad y=u-1$',fontsize=13,color=fg)
fig.text(.065,.03,'The dots index free generators, not points of an underlying geometric space. Proofs: Cross-effects, X1–X24; Chain comparison, Q42–Q46.',fontsize=10.5,color=fg)
for ext in ('png','svg'):fig.savefig(OUT/f'11_retained_cross_effect.{ext}',dpi=150,facecolor=fig.get_facecolor())
plt.close(fig)

fig,ax=plt.subplots(figsize=(15,10))
fig.patch.set_facecolor('#fcfcfa');fig.subplots_adjust(left=.025,right=.985,bottom=.025,top=.975)
ax.set(xlim=(0,15),ylim=(0,10));ax.axis('off')
ax.text(.3,9.75,'Keep the defect: its projector and its Frobenius',fontsize=23,weight='bold',color=fg,va='top')
def card(y,h,title,rows,c):
    ax.add_patch(FancyBboxPatch((.35,y),14.1,h,boxstyle='round,pad=.1',fc='white',ec=c,lw=2))
    ax.text(.6,y+h-.25,title,fontsize=18,color=c,va='top')
    for k,row in enumerate(rows):ax.text(.6,y+h-.92-.54*k,row,fontsize=16,color=fg,va='top')
card(5.55,3.3,'A chosen contraction gives the actual retained summand',[
    r'$dh+hd=1,\quad D=U(d),\quad H=U(h),\quad F_h=1-DH-HD$',
    r'$F_h^2=F_h,\quad DF_h=F_hD=0,\quad R_h=\mathrm{im}(F_h)\subset K(C)$',
    r'$F_h(r_v)=r_v-r_{dhv}-r_{hdv}$',
    r'$S=HDH,\qquad DS+SD=1-F_h:\quad U(C)\ \rightleftarrows\ (R_h,0)$'],blue)
card(1.15,3.8,'Frobenius on the completed mixed ideal',[
    r'$B=\widehat{\mathbb{Z}[t^{\pm1},u^{\pm1}]}_p,\quad J=(t-1)(u-1)B,\quad\phi(t,u)=(t^p,u^p)$',
    r'$\phi^*J=B\otimes_{B,\phi}J\ \overset{\Phi}{\longrightarrow}\ J,\quad b\otimes m\mapsto b\phi(m)$',
    r'$0\longrightarrow\phi^*J\overset{\Phi}{\longrightarrow}J\longrightarrow B/(Q_p(t)Q_p(u))\longrightarrow0$',
    r'$Q_p(T)=1+T+\cdots+T^{p-1},\quad\delta(J)\subset J$',
    r'$(B,(p))\longrightarrow(B/J,(p))\quad\mathrm{has\ kernel}\ J$'],green)
ax.text(.45,.48,'The upper summand retains cohomology. The lower cokernel measures Frobenius linearization on that retained object.',fontsize=12,color=fg)
ax.text(.45,.13,'Proofs: Homotopy defect, projector and deformation retract; Frobenius cross-effect, F1–F17. No cohomology equivalence is assumed.',fontsize=11,color=fg)
for ext in ('png','svg'):fig.savefig(OUT/f'12_retained_frobenius.{ext}',dpi=150,bbox_inches='tight',facecolor=fig.get_facecolor())
plt.close(fig)
