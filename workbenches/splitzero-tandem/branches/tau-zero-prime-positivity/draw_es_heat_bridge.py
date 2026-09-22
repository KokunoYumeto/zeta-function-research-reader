"""Exact-coordinate figures for ESQ and the shell heat lift."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from itertools import combinations

out=Path(__file__).resolve().parent/'figures'
out.mkdir(exist_ok=True)
plt.rcParams.update({'font.size':11,'figure.facecolor':'white','savefig.facecolor':'white'})
v=np.array([[-1,0,0],[1/3,0,2*np.sqrt(2)/3],[1/3,np.sqrt(2/3),-np.sqrt(2)/3],[1/3,-np.sqrt(2/3),-np.sqrt(2)/3]])
assert np.allclose(v@v.T,np.eye(4)*4/3-np.ones((4,4))/3)
fig=plt.figure(figsize=(12.4,5.3))
ax=fig.add_subplot(121,projection='3d')
faces=[v[list(c)] for c in combinations(range(4),3)]
ax.add_collection3d(Poly3DCollection(faces,facecolors='#46a8bc',alpha=.08,edgecolor='#496472',linewidth=1))
labels=[r'$r_\infty$',r'$r_0$',r'$r_+$',r'$r_-$']
for i,p in enumerate(v):
    f=-p/3
    ax.scatter(*p,s=48,color='#167e9c')
    ax.scatter(*f,s=28,color='#bd6250')
    ax.plot([p[0],f[0]],[p[1],f[1]],[p[2],f[2]],'--',color='#999999',linewidth=.8)
    ax.text(*(p*1.16),labels[i],fontsize=12)
ax.scatter(0,0,0,s=18,color='black')
ax.set(xlim=(-1.2,1.2),ylim=(-1.2,1.2),zlim=(-1.2,1.2))
ax.set_box_aspect((1,1,1));ax.view_init(22,35);ax.set_axis_off()
ax.set_title('The exact regular tetrahedron in the positive three-space',pad=12,fontsize=12)
ax.text2D(.04,-.02,r'Face centres: $f_j=-r_j/3$.  The line $\mathbb{R}E_{21}$ is orthogonal to this space.',transform=ax.transAxes,fontsize=10)
bx=fig.add_subplot(122);bx.axis('off')
bx.set_title('The four-dimensional map retains the extra direction',fontsize=12,pad=12)
rows=[(r'$w_j=\frac{1}{2} E_{21}+\frac{\sqrt{3}}{2}r_j$',.85,18),
      (r'$\langle w_i,w_j\rangle_G=\delta_{ij},\qquad E_{21}=\frac{1}{2}\sum_j w_j$',.66,17),
      (r'$W^{-1}A_hW=\frac{1}{4} I_4+\frac{2h-1/2}{4}\,\mathbf{1}\mathbf{1}^{\mathsf{T}}$',.44,16),
      ('The sum-zero space has eigenvalue 1/4.',.23,12),
      ('The uniform line has eigenvalue −1/4 + 2h.',.12,12)]
for t,y,sz in rows:bx.text(.03,y,t,fontsize=sz,transform=bx.transAxes)
fig.subplots_adjust(left=.01,right=.99,top=.88,bottom=.12,wspace=.04)
for ext in ['png','svg']:fig.savefig(out/f'27_tetrahedral_heat_frame.{ext}',dpi=160)
plt.close(fig)

h=np.linspace(0,.30,401);a=-.25+2*h
fig,(ax,bx)=plt.subplots(1,2,figsize=(12.4,5.4),gridspec_kw={'width_ratios':[1,1.18]})
ax.plot(h,a,color='#146f9f',label=r'ES eigenvalue $a=-1/4+2h$')
ax.plot(h,2*a,color='#ba604c',label=r'Reflected trace $q(r,r)=2a$')
ax.plot(h,4*a,color='#19926f',label=r'Shell eigenvalue $4a=-1+8h$')
ax.axhline(0,color='#888888',linewidth=.8);ax.axvline(1/8,color='#555555',ls='--',linewidth=1)
ax.axvspan(1/8,.30,color='#19926f',alpha=.06)
ax.set_xticks([0,1/8,1/4],['0','1/8','1/4']);ax.set_xlabel('Original heat parameter h')
ax.set_ylabel('Exact value');ax.set_xlim(0,.30);ax.grid(alpha=.18)
ax.set_title('One crossing, with all scale factors retained',fontsize=12)
ax.legend(loc='lower right',fontsize=9)
bx.axis('off');bx.set_title('The same lift on finitely or infinitely many orbits',fontsize=12)
rows=[(r'$\mathcal{H}=\ell^2(\mathcal{O})\otimes\mathbb{C}^2\otimes\mathbb{C}^3$',.88,17),
      (r'$\Psi(P_+)=Q_<,\qquad\Psi(P_-)=Q_>$',.72,16),
      (r'$H_h=4Q_<+(-1+8h)Q_>$',.55,18),
      (r'$\langle v,H_hv\rangle\geq\min(4,-1+8h)\,\|v\|^2$',.36,15),
      (r'for every $v\in\mathcal{H}$ and $h>1/8$.',.24,12),
      ('At h = 1/8: the negative-sector form vanishes;',.10,11),
      ('the two square-zero blades and their mixed products remain.',.03,11)]
for t,y,sz in rows:bx.text(.015,y,t,fontsize=sz,transform=bx.transAxes)
fig.subplots_adjust(left=.07,right=.99,top=.87,bottom=.13,wspace=.21)
for ext in ['png','svg']:fig.savefig(out/f'28_shell_heat_sign.{ext}',dpi=160)
plt.close(fig)
print('Wrote exact tetrahedral frame and shell heat figures.')

fig,(ax,bx)=plt.subplots(1,2,figsize=(12.4,5.4),gridspec_kw={'width_ratios':[1.1,1]})
ax.axis('off');ax.set_title('The actual test quotient and the ES form',fontsize=13)
texts=[(r'$f\in C_c^\infty(\mathbb{R};\mathbb{C})$',.87,17),
       (r'$L f=(M_f(0),M_f(1),M_f(\frac{1}{2}+\frac{i}{2}),M_f(\frac{1}{2}-\frac{i}{2}))$',.67,13),
       (r'$\mathcal{C}=P_{1/4}-P_0$',.48,18),
       (r'$\mathcal{C}(f,g)=(\widehat{J}Lf)^*G_{\rm ES}A_0(\widehat{J}Lg)$',.28,14),
       ('The quotient has signature (3, 1).',.12,12),
       ('The section, kernel and involution maps are explicit.',.03,11)]
for text,y,sz in texts:ax.text(.015,y,text,fontsize=sz,transform=ax.transAxes)
for start in [.80,.60,.41]:ax.annotate('',xy=(.45,start-.07),xytext=(.45,start),xycoords='axes fraction',arrowprops={'arrowstyle':'->','color':'#76838b'})
x=np.array([0,1]);width=.30
bx.bar(x-width/2,[-2,2],width,color='#207a9c',label=r'Endpoint change $\mathcal{C}$')
bx.bar(x+width/2,[2,-2],width,color='#b35e4d',label=r'Archimedean change $-\mathcal{C}$')
bx.axhline(0,color='#555555',lw=.9)
bx.set_xticks(x,[r'$f_-=S(1,1,0,0)$',r'$f_+=S(1,-1,0,0)$'])
bx.set_ylim(-3,3);bx.set_yticks([-2,-1,0,1,2]);bx.set_ylabel('Exact change on the same admissible test')
bx.set_title('The whole Weil form has zero change',fontsize=13)
bx.legend(loc='upper center',fontsize=10)
bx.text(.5,.02,r'$\Delta W=\mathcal{C}-\mathcal{C}=0$',ha='center',transform=bx.transAxes,fontsize=14)
fig.subplots_adjust(left=.04,right=.98,top=.85,bottom=.15,wspace=.20)
for ext in ['png','svg']:fig.savefig(out/f'29_actual_weil_correction.{ext}',dpi=160)
plt.close(fig)



