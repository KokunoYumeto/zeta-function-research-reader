"""Exact symbolic maps and a proved singular-value function; no zero model."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch
B=Path(__file__).resolve().parent;O=B/'figures_reciprocity_057';O.mkdir(exist_ok=True)
# Reproduce the preceding figure with the newly proved arithmetic restriction.
old=(B/'generate_prime_collision_figure.py').read_text(encoding='utf-8')
old=old.replace("O=B/'figures_prime_collision'","O=B/'figures_reciprocity_057'")
old=old.replace("['1','0 or 1','0 or 1','1']","['1','0','0','1']")
old=old.replace('0,0,0,0,0,0,1,1  or  0,0,0,0,1,1,1,1','0,0,0,0,0,0,1,1')
old=old.replace('PS6–25, PB1–8, PES1–12, ECC31–43, OCQ1–11','OE1–18, ECC31–43, OCQ1–11')
old=old.replace('ES reader v69; Tao; DLMF Ch. 18; Jouve–Rodriguez-Villegas.','Elsholtz–Tao, arXiv1107.1010v6; ES reader v69; DLMF Ch. 18.')
old=old.replace('Symbolic diagram. The one-divisible valuation-one row is permitted by the proved bound; its existence is not claimed. No arithmetic zero trajectory is depicted.',
 'OE7–8 proves p does not divide S for every positive witness: the two Type I unit denominators have opposite quadratic characters. No zero trajectory is depicted.')
old=old.replace('20_prime_and_original_collision','20_prime_and_original_collision_current')
exec(compile(old,'reproduced_figure20','exec'),{'__file__':__file__})
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'mathtext.fontset':'dejavusans'})
fig=plt.figure(figsize=(14,13),facecolor='#f7f9fc');ax=fig.add_axes([0,0,1,1])
ax.set(xlim=(0,14),ylim=(0,13));ax.axis('off')
ink='#15283c';blue='#176893';red='#a64235';green='#236845'
def txt(x,y,t,size=12,color=ink,ha='left',weight='normal'):
    ax.text(x,y,t,fontsize=size,color=color,ha=ha,va='center',weight=weight)
def box(x,y,w,h,fc='#ffffff',ec='#cad6e2'):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.10',fc=fc,ec=ec,lw=1.3))
def arrow(x,y,X,Y):ax.add_patch(FancyArrowPatch((x,y),(X,Y),arrowstyle='-|>',mutation_scale=14,color=blue,lw=1.8))
txt(.55,12.52,'Signed arithmetic defects and the original conductor',21,weight='bold')
txt(.55,12.12,'All four marked roots and both factor signs are retained. Boxes show residue clusters, not Euclidean distances.',11)
for left,typ,labels,cluster in [(.65,'TYPE I',['M: p','N: x','T: y','E: pZ'],[0,3]),(7.3,'TYPE II',['M: p','N: x','T: pY','E: pZ'],[0,2,3])]:
    box(left-.15,8.2,6.05,3.28)
    txt(left,11.07,typ+' — exact residue-cluster structure',13,blue,weight='bold')
    for j,l in enumerate(labels):
        x=left+.67+j*1.4
        fc='#e8eefc' if j in cluster else '#f4efe5'
        box(x-.53,9.65,1.05,.91,fc)
        txt(x,10.24,l,11,ha='center')
        txt(x,9.90,'+   −',15,blue,ha='center')
        if j in cluster:
            ax.plot([x,x],[9.59,9.24],color=blue,lw=1.5)
    xs=[left+.67+j*1.4 for j in cluster]
    ax.plot([min(xs),max(xs)],[9.24,9.24],color=blue,lw=1.5)
    txt(left,8.90,'Mixed signs in the blue cluster:',11)
    txt(left,8.49,'cyclic defect R/(p); 8 integral sign operations' if typ=='TYPE I' else 'cyclic defect R/(p²); 4 integral sign operations',11,red)
box(.5,5.43,13,2.31)
txt(.8,7.36,'THE COMPLETE INTERSECTION, WITH ITS EXACT QUOTIENT MAP',13,blue,weight='bold')
txt(.8,6.89,r'$E\cap\Sigma_jE=\{R_0+\sigma Q:\ Q(r_j)\in f^{\prime}(r_j)R\}$',18)
txt(.8,6.40,r'$R_0+\sigma Q\ \longmapsto\ Q(r_j)\ \mathrm{mod}\ f^{\prime}(r_j)$',17,red)
txt(.8,5.88,'This arithmetic defect has length 1 or 2. The full signed affine coordinates are recovered by SGR5–7.',11)
box(.5,2.50,7.4,2.44,fc='#edf6f1')
txt(.8,4.57,'BOTH ORIGINAL GAMMA METRICS',13,green,weight='bold')
txt(.8,4.07,r'$\Gamma_{b,j}=D_j^*\Gamma_bD_j\quad(b=U,W)$',17)
txt(.8,3.52,r'$\Gamma_{W,j}^{-1}\Gamma_{U,j}=D_j^{-1}\Gamma_W^{-1}\Gamma_UD_j$',16)
txt(.8,2.95,'Every original inverse singular value is retained.',12,green)
plot=fig.add_axes([.63,.195,.30,.18]);nu=np.linspace(1,4,401)
large=np.sqrt(nu)+np.sqrt(nu-1);plot.plot(nu,large,label=r'$s=\sqrt{\nu}+\sqrt{\nu-1}$',color=blue,lw=2)
plot.plot(nu,1/large,label=r'$s^{-1}$',color=red,lw=2);plot.axhline(1,color='#999999',lw=.7)
plot.set(xlabel=r'Exact metric quantity $\nu\geq1$',ylabel='Singular value',ylim=(0,4));plot.legend(fontsize=10);plot.grid(alpha=.2)
txt(9.0,5.10,'ONE SIGN CHANGE: EXACT SPECTRUM',11,blue,weight='bold')
txt(.7,1.87,r'$\nu=\dfrac{(c_j^*H_bc_j)(v(r_j)^{\mathsf{T}}H_b^{-1}\overline{v(r_j)})}{|f^{\prime}(r_j)|^2}\geq1$',17)
txt(8.25,1.82,'Spectrum: s, 1, 1, 1, 1, 1, 1, 1/s',11)
txt(.7,1.10,'The curve is the proved universal function of the actual metric quantity ν, not a sampled programme spectrum.',11)
txt(.55,.60,'Proofs: OE7–18; SGR1–14. Human sources: Elsholtz–Tao, arXiv1107.1010v6, §2; original ES reader v69 and Tao attribution.',9)
txt(.55,.30,'A defect of the integral signed operation is not itself a singularity of the original complex conductor. The exact relation is displayed above.',9)
for ext in ['png','svg']:fig.savefig(O/f'21_signed_arithmetic_original_metrics.{ext}',dpi=170,facecolor=fig.get_facecolor())
plt.close(fig)
print(O/'21_signed_arithmetic_original_metrics.png')

fig=plt.figure(figsize=(14,10),facecolor='#f7f9fc');ax=fig.add_axes([0,0,1,1])
ax.set(xlim=(0,14),ylim=(0,10));ax.axis('off')
txt(.55,9.53,'Where the nonlinear escape goes',22,weight='bold')
txt(.55,9.10,'The exact ES collision path: (P; P+t, 2P, 2P(P+t)/(5P+7t)), with P ≠ 0 and both signs at each colliding root.',11)
box(.5,4.80,13,3.76)
txt(.8,8.18,'ACTUAL TWO-ROOT QUOTIENT',14,blue,weight='bold')
txt(.8,7.72,r'$Y=E_tM_*q,\qquad U_j=(m_j(P),m_j^{\prime}(P))^{\mathsf{T}}$',17)
headers=[.8,7.8,10.0]
for x,h in zip(headers,['Exact test','Order in |t|','Nonzero leading vector']):txt(x,7.14,h,11,weight='bold')
rows=[(6.65,r'$U_1\ne0$',r'$-1/2$',r'$U_1/\lambda$'),
      (6.18,r'$U_1=0,\ U_2\ne0$',r'$0$',r'$-P U_2$'),
      (5.71,r'$U_1=U_2=0,\ Z_\lambda\ne0$',r'$1/2$',r'$Z_\lambda$'),
      (5.24,r'$U_1=U_2=0,\ Z_\lambda=0$',r'$1$',r'$W_\lambda$')]
for y,test,order,lead in rows:
    txt(headers[0],y,test,15);txt(headers[1],y,order,16,red);txt(headers[2],y,lead,16,blue)
box(.5,2.00,13,2.23,fc='#edf6f1')
txt(.8,3.86,'THE COMPLETE COMPLEMENT RETAINS THE HIDDEN ESCAPE',13,green,weight='bold')
txt(.8,3.37,r'$f=M_*q=y_0+y_1(r-P)+(r-P)(r-P-t)(c+dr)$',18)
txt(.8,2.87,r'$c=f_2+(2P+t)f_3,\qquad d=f_3$',17)
txt(.8,2.36,'If U₁ = 0, the quotient is bounded but (c,d) has a nonzero |t|⁻¹ᐟ² term. Both original norms are exactly EQR4.',11)
txt(.7,1.40,'Rational sign involution, with the quotient fixed: pole order 3 if u₄ ≠ 0; 2 if u₄ = 0 and u₃ ≠ 0; otherwise 1.',11)
txt(.7,.98,'Every row retains both signs. Cancellation can occur at only one root label, and its next coefficient is proved nonzero.',11)
txt(.55,.50,'Proofs and full constants: EQR1–13. Human source of the polynomial: ES reader v69 with the original Tao/Fable attribution; original metrics: WCF.',9)
txt(.55,.23,'Exact case diagram, not an assertion that every exceptional stratum occurs for an original arithmetic period.',9)
for ext in ['png','svg']:fig.savefig(O/f'22_nonlinear_escape_complete_quotient.{ext}',dpi=170,facecolor=fig.get_facecolor())
plt.close(fig)
print(O/'22_nonlinear_escape_complete_quotient.png')
