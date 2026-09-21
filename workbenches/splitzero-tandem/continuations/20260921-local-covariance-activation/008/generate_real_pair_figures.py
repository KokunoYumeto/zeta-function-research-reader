"""Reproducible diagrams of the exact real-pair certificate and return."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np
B=Path(__file__).resolve().parent
O=B/'figures_real_pair_005';O.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'svg.fonttype':'none'})
blue='#17668b';red='#ac3d47';green='#24745e'
fig=plt.figure(figsize=(14,8))
ax=fig.add_axes([.075,.39,.34,.45])
ax.add_patch(Rectangle((-1,-1),2,2,facecolor='#edf5f9',edgecolor=blue,lw=2))
ax.axhline(0,color='.7',lw=.7);ax.axvline(0,color='.7',lw=.7)
ax.scatter([0],[0],marker='+',color=red,s=90,zorder=3)
ax.set(xlim=(-1.12,1.12),ylim=(-1.12,1.12),aspect='equal',
       xlabel=r'$(z-z_c)/10^{-15}$',ylabel=r'$(x-x_c)/10^{-15}$')
ax.set_title('One exact root in this real rectangle',loc='left',fontweight='bold',pad=14)
fig.text(.07,.25,'Display offsets only; inverse coordinates:\n'+
         r'$z=z_c+10^{-15}X,\quad x=x_c+10^{-15}Y$'+'\n'+
         'The cross marks the center, not an exact root position.',fontsize=10)
fig.text(.07,.145,r'$z_c=0.022119477808661845132007916399\ldots$'+'\n'+
         r'$x_c=-1.466817440463494183975448871845\ldots$'+'\n'+
         'Exact terminating-decimal centers: RPZ4.',fontsize=10)
ax=fig.add_axes([.50,.19,.47,.66]);ax.axis('off')
items=[('The full infinite series is certified',17,blue),
       (r'$T(y)=y-PF(y),\quad F=(\Re d_1,\Im d_1)$',16,'black'),
       (r'$T(X)\subset\mathrm{int}(X),\quad\mathrm{Lip}_r(T)<1.829\,10^{-6}$',14,green),
       ('Geometric iteration proves existence and uniqueness.',11,'black'),
       (r'$u_*=1/z_*\in[45.20902385898\pm3.31\,10^{-12}]$',14,blue),
       (r'$a_*=\alpha(1+ix_*),\quad\alpha\in\mathbb{R}\setminus\{0\}$',15,'black'),
       (r'$d_1=d_4=0,\qquad d_2,d_3\ne0$',18,red),
       (r'$E_A=G G^\#,\quad G=f_1f_2$',17,'black'),
       (r'$\mu_0=\mu_1=0,\quad\mu_2=2|G_\xi|^2>0$',17,green)]
y=1
for txt,size,col in items:
    ax.text(0,y,txt,fontsize=size,color=col,va='top');y-=.112
fig.suptitle('A positive real period: exactly two conjugate factors vanish',fontsize=20,y=.965)
fig.text(.05,.035,'Proof: RPZ1–19 and RPCJ1–8. Full original matrix, unit and factor signs retained.\n'
         'Inclusion arithmetic: Fredrik Johansson, Arb, arXiv:1611.02831v1. This is a geometric coefficient member; no arithmetic zeta-zero identification.',fontsize=9)
for ext in ['png','svg']:fig.savefig(O/f'34_real_pair_certificate.{ext}',dpi=180)
plt.close(fig)

fig=plt.figure(figsize=(14,8.4))
ax=fig.add_axes([.07,.53,.38,.29])
ks=np.arange(1,5)
ax.bar(ks-.17,[5,3,0,0],.32,color=red,label='Inverse singular poles')
ax.bar(ks+.17,[5,8,8,8],.32,color=blue,label='Inverse exterior poles')
for k,v in zip(ks,[5,3,0,0]):ax.text(k-.17,v+.22,str(v),ha='center',color=red)
for k,v in zip(ks,[5,8,8,8]):ax.text(k+.17,v+.22,str(v),ha='center',color=blue)
ax.set(xticks=ks,ylim=(0,9.3),xlabel='Ordered singular index / exterior rank',ylabel='Exact pole exponent')
ax.legend(loc='upper left',bbox_to_anchor=(0,1.27),frameon=False,fontsize=10)
ax.spines[['top','right']].set_visible(False)
fig.text(.07,.405,r'$\tau=z-z_*,\quad\|\wedge^r B^{-1}\|\sim C_r|\tau|^{-p_r}$'+'\n'+
         r'$C_1=|R(2cb-R^2)|\rho_3/(c^4\rho_0)$'+'\n'+
         r'$C_2=\mu_2^2\rho_2\rho_3/(4c^4\rho_0\rho_1)$'+'\n'+
         r'$C_3=\|C_s\|/c^4,\quad C_4=c^{-4}$',fontsize=12,linespacing=1.8,va='top')
fig.text(.07,.135,'All constants are strictly positive.\nOriginal period: each constant gains '+r'$u_*^{2p_r}$'+'.\n'
         'Original Gamma mass, center and weights: RPCJ9; RPE5–9.',fontsize=10)
ax=fig.add_axes([.52,.13,.45,.72]);ax.axis('off')
lines=[('Both exact ways to retain all four labels',17,blue),
       ('Old source loses exactly two directions',13,red),
       (r'$T_A:\mathcal{P}_3\longrightarrow\mathcal{P}_1,\quad\ker T_A=\mathcal{P}_1$',16,'black'),
       (r'$\Theta_2q=(T_A\Phi_0q,[S^0]\Phi_0q,[S^1]\Phi_0q)$',14,'black'),
       ('The two saved scalars give an exact inverse (RPE21).',11,green),
       ('The actual order-two conductor is invertible',13,blue),
       (r'$T_A:\mathcal{P}_5/\mathcal{P}_1\;\longrightarrow\;\mathcal{P}_3$',19,'black'),
       (r'$x_a=[S^2\ell_a],\quad y_a=T_Ax_a$',17,'black'),
       (r'$a\in\{\mathrm{M},\mathrm{N},\mathrm{T},\mathrm{E}\}$',16,'black'),
       (r'$\det Y^{(2)}=-\frac{16}{29}\mu_2^4\ne0$',18,green)]
y=1
for txt,size,col in lines:
    ax.text(0,y,txt,fontsize=size,color=col,va='top');y-=.102
fig.suptitle('Degree three: the old inverse diverges; all four labels are retained',fontsize=19,y=.97)
fig.text(.05,.027,'Exact exponents: RPCJ14–23. Four distinct old marks, two-scalar inverse and full metric: RPE10–26.\n'
         'Human sources: ES reader v69 (The Clankers; underlying Alpöge/Fable/Tao example), and the cited DLMF Chapter 18 authors for the Gamma dictionary.',fontsize=9)
for ext in ['png','svg']:fig.savefig(O/f'35_real_pair_inverse_return.{ext}',dpi=180)
plt.close(fig)
fig=plt.figure(figsize=(14,8))
ax=fig.add_axes([.075,.35,.42,.48])
D=np.arange(1,101)
ax.plot(D,D+2,color=red,lw=2.5,label=r'First inverse singular pole: $D+2$')
ax.plot(D,D,color=green,lw=2.5,ls='--',label=r'Second inverse singular pole: $D$')
ax.plot(D,2*D+2,color=blue,lw=2.5,label=r'Exterior ranks $r\geq2$: $2D+2$')
ax.set(xlim=(1,100),ylim=(0,210),xlabel='Original degree cutoff D',ylabel='Exact pole exponent')
ax.legend(loc='upper left',frameon=False,fontsize=9)
ax.spines[['top','right']].set_visible(False)
ax.grid(axis='y',alpha=.18)
fig.text(.075,.18,'Each integer cutoff on this plot is certified.\nLines join integer values; there is no noninteger-cutoff claim.\n'
         'Coefficients retain all original Gamma weights and moments.\nExact constants: RPAC8–14.',fontsize=10,linespacing=1.6)
ax=fig.add_axes([.55,.16,.42,.69]);ax.axis('off')
rows=[('The complete resonance equation',17,blue),
      (r'$H_D=\frac{(i\lambda)^D}{c}U_D(\theta)$',20,'black'),
      (r'$H_D=0\ \Longleftrightarrow\ \theta=\cos\frac{k\pi}{D+1}$',19,red),
      (r'$k=1,\ldots,D$',15,'black'),
      (r'$\theta=\frac{\Re(A\overline{B})}{|A||B|},\quad\lambda=\frac{|B|}{|A|}$',18,'black'),
      ('At the certified original pair, for 1 ≤ D ≤ 100:',12,blue),
      (r'$|\theta-\cos(k\pi/(D+1))|>1.95\,10^{-5}$',16,green),
      ('All 5,050 interval comparisons pass.',13,green),
      ('For every D, the exact alternative on resonance is',11,'black'),
      (r'$(D+1,D+1,0,\ldots,0)$',19,red)]
y=1
for txt,size,col in rows:
    ax.text(0,y,txt,fontsize=size,color=col,va='top');y-=.099
fig.suptitle('The original real-pair inverse: every cutoff, both exact spectra',fontsize=20,y=.965)
fig.text(.05,.045,'Proof RPAC1–15. A finite certificate proves nonresonance through D=100; the all-degree formulas retain both cases.\n'
         'Original period and Gamma dictionary: PCL1–16 and WCF1–6. Inclusion arithmetic: Fredrik Johansson, Arb, arXiv:1611.02831v1.',fontsize=9)
for ext in ['png','svg']:fig.savefig(O/f'36_real_pair_all_cutoffs.{ext}',dpi=180)
plt.close(fig)
print('Rendered figures 34, 35 and 36 as PNG and SVG.')
