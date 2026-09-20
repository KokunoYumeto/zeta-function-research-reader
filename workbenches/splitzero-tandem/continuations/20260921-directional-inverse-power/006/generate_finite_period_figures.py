"""Reproducible scientific diagrams for FPZ, FUT and PRD; no sampled proof."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,FancyArrowPatch
B=Path(__file__).resolve().parent;O=B/'figures_finite_period_064';O.mkdir(exist_ok=True)
plt.rcParams.update({'font.size':12,'axes.titlesize':14,'figure.facecolor':'white','savefig.facecolor':'white'})
blue='#234f7b';red='#ab343e';green='#26715b'
def save(fig,name):
    fig.savefig(O/(name+'.png'),dpi=165,bbox_inches='tight')
    fig.savefig(O/(name+'.svg'),bbox_inches='tight')
    plt.close(fig)
c=json.loads((B/'FINITE_PERIOD_ZERO_CERTIFICATE.json').read_text(encoding='utf-8'))
cr=float(c['center']['real']);ci=float(c['center']['imag'])
fig,axes=plt.subplots(1,3,figsize=(15,5.2),gridspec_kw={'width_ratios':[1,1,1.2]})
ax=axes[0];ax.scatter([cr],[ci],s=70,c=red,zorder=3)
ax.annotate(r'$z_*$',(cr,ci),xytext=(8,7),textcoords='offset points',fontsize=16)
ax.set(xlim=(0,.016),ylim=(0,.012),xlabel=r'$\operatorname{Re}z$',ylabel=r'$\operatorname{Im}z$',title='Finite inverse period')
ax.grid(alpha=.2);ax.set_aspect('equal',adjustable='box')
ax.set_xticks([0,.004,.008,.012,.016]);ax.tick_params(axis='x',labelsize=10)
ax.text(.0007,.0107,r'$\delta=1/4,\quad\gamma=3$',fontsize=12)
ax.text(.0007,.0010,'Disk radius $10^{-14}$\nnot visible at this scale',fontsize=11)
ax=axes[1];ax.add_patch(Circle((0,0),1,facecolor='#e7f0f7',edgecolor=blue,lw=2))
ax.plot([-1,1,1,-1,-1],[-1,-1,1,1,-1],color=green,ls='--')
ax.set(xlim=(-1.5,1.5),ylim=(-1.5,1.5),xlabel=r'$\operatorname{Re}(z-c)/10^{-14}$',ylabel=r'$\operatorname{Im}(z-c)/10^{-14}$',title='Exact certified disk')
ax.set_aspect('equal');ax.text(0,.10,'Exactly one\nsimple zero',ha='center',va='center',color=red,fontsize=14)
ax.text(0,-1.38,'Root location within the disk is not drawn.',ha='center',fontsize=9)
ax=axes[2];ax.axis('off');ax.set_title('Complete-series certificate')
rows=[('Remainder in each $R$ entry',r'$<6.44\times10^{-98}$'),
      (r'Remainder in each $R\prime$ entry',r'$<2.92\times10^{-93}$'),
      ('Boundary error',r'$<8.01\times10^{-14}$'),
      ('Linear boundary term',r'$>4.34\times10^{-12}$'),
      ('Original symbol order',r'$v(z_*)=1$'),
      ('Complete first moment',r'$|\mu_1(z_*)|>13.80$')]
for j,(label,value) in enumerate(rows):
    y=.91-j*.145;ax.text(0,y,label,fontsize=11);ax.text(0,y-.064,value,color=blue,fontsize=14)
fig.suptitle('A finite zero of the original geometric conductor family',fontsize=18,y=1.03)
fig.text(.5,.015,'FPZ1–14 and FPR1–22. Original PCL coefficients; rigorous Arb enclosures (Fredrik Johansson).\nThe quartet is a geometric parameter choice; this figure does not identify it with zeta zeros.',ha='center',fontsize=10)
fig.tight_layout(rect=(0,.15,1,.93));save(fig,'28_certified_finite_period')

fig,axes=plt.subplots(1,3,figsize=(15,5.4),gridspec_kw={'width_ratios':[1.2,1,1]})
ax=axes[0];ax.axis('off');ax.set_title('Original fixed four-dimensional spaces')
ax.text(.5,.91,r'$\mathcal{P}_3\longrightarrow\mathcal{P}_3$',ha='center',fontsize=20)
ax.text(.5,.77,r'$c_0=a_{\rm amp}/2,\quad c_1=c_0-4$',ha='center')
ax.text(.5,.65,r'$s\in\{1,a_{\rm amp}\},\quad dm_s\ \mathrm{unchanged}$',ha='center')
ax.text(.5,.49,r'$\mu_0(z_*)=0,\quad\mu_1(z_*)\ne0$',ha='center',fontsize=16,color=red)
ax.text(.5,.34,r'$\mathrm{rank}=3,\quad\ker=\mathbb{C}\cdot1$',ha='center',fontsize=17)
ax.text(.5,.18,r'$\mathrm{image}=\mathcal{P}_2$',ha='center',fontsize=17)
ax.text(.5,.02,r'Actual new quotient: $\mathcal{P}_4/\mathcal{P}_0\to\mathcal{P}_3$'+'\nis invertible at this same period.',ha='center',fontsize=11)
ax=axes[1];ax.bar(range(1,5),[4,0,0,0],color=[red,blue,blue,blue]);ax.scatter([2,3,4],[0,0,0],color=blue,zorder=3)
ax.set(xticks=range(1,5),ylim=(-.3,4.8),xlabel='Inverse singular-value index',ylabel='Pole order in $|z-z_*|$',title='One singular value diverges')
for j,k in enumerate([4,0,0,0],1):ax.text(j,k+.18,str(k),ha='center',fontsize=15)
ax=axes[2];ax.bar(range(1,5),[4]*4,color=red)
ax.set(xticks=range(1,5),ylim=(0,4.8),xlabel='Exterior rank',ylabel='Pole order in $|z-z_*|$',title='Every inverse exterior rank')
for j in range(1,5):ax.text(j,4.15,'4',ha='center',fontsize=15)
fig.suptitle('The finite rank loss in the original Gamma metrics',fontsize=18,y=1.04)
fig.text(.5,.015,r'FPZ15–24: $|z-z_*|^{D+1}\|\bigwedge^r B_{D,s}(z)^{-1}\|\to\|\bigwedge^{D+1-r}B_*\|/|\alpha_*|^{D+1}$.'+'\nAll constants use the complete original moments and Gamma weights; the bars show proved orders, not samples.',ha='center',fontsize=11)
fig.tight_layout(rect=(0,.16,1,.93));save(fig,'29_finite_inverse_exterior')

fig,axes=plt.subplots(1,2,figsize=(13,5.6),gridspec_kw={'width_ratios':[1,1.2]})
ax=axes[0];theta=np.linspace(0,2*np.pi,200)
ax.plot(2**(1/3)*np.cos(theta),2**(1/3)*np.sin(theta),color='#bac4ce',ls='--')
roots=-2**(1/3)*np.exp(2j*np.pi*np.arange(3)/3)
for j,x in enumerate(roots):
    ax.scatter([x.real],[x.imag],s=75,color=blue);ax.annotate(r'$\ell='+str(j)+'$',(x.real,x.imag),xytext=(9,7),textcoords='offset points')
ax.axhline(0,color='#bbbbbb',lw=.7);ax.axvline(0,color='#bbbbbb',lw=.7)
ax.set(xlim=(-1.7,1.7),ylim=(-1.7,1.7),xlabel=r'$\operatorname{Re}(X/h-2)$',ylabel=r'$\operatorname{Im}(X/h-2)$',title='Three distinct boundary roots')
ax.set_aspect('equal')
ax=axes[1];ax.axis('off');ax.set_title('Exact return to the original centre')
ax.text(0,.88,r'$X=z(P+\kappa),\quad h=9/(\beta^2-9\eta)$',fontsize=14)
ax.text(0,.70,r'$X_\ell=h(2-2^{1/3}\omega_\ell),\quad\omega_\ell=e^{2\pi i\ell/3}$',fontsize=14)
ax.text(0,.52,r'$P_\ell(z)=X_\ell/z-\kappa-4-b_2/(3b_3)+O(z)$',fontsize=14)
ax.text(0,.33,r'$\operatorname{Disc}_P m_1=z^{26}[-108b_3^4C^4h^6+O(z^2)]$',fontsize=14,color=blue)
ax.text(0,.12,'No repeated root at any complex centre\nthroughout PRD14’s proved finite-period region.',fontsize=13)
fig.suptitle('The actual period moments exclude every repeated receiver root near infinite period',fontsize=16,y=1.02)
fig.text(.5,-.045,'PRD1–30: the displayed affine complex-plane coordinate has its exact inverse above.\nReal nonzero unit phase; all original moments retained. Finite complex zeros in FPZ lie outside that exclusion region.',ha='center',fontsize=10)
fig.tight_layout();save(fig,'30_actual_receiver_roots')

from mpl_toolkits.mplot3d.art3d import Poly3DCollection
fig=plt.figure(figsize=(13,6.4));ax=fig.add_subplot(121,projection='3d');tx=fig.add_subplot(122);tx.axis('off')
# Rows form an explicitly displayed orthonormal basis of the zero-mean
# real label space. This display metric is not an assigned Gamma metric.
H=np.array([[1,-1,0,0],[1,1,-2,0],[1,1,1,-3]],dtype=float)/np.sqrt([2,6,12])[:,None]
points=H.T
faces=[[points[k] for k in range(4) if k!=j] for j in range(4)]
ax.add_collection3d(Poly3DCollection(faces,alpha=.12,facecolor=blue,edgecolor=blue,lw=1.3))
for j,label in enumerate(['M','N','T','E']):
    p=points[j];ax.scatter(*p,color=red,s=45);ax.text(*(p*1.15),label,fontsize=16,ha='center')
ax.set(xlim=(-1,1),ylim=(-1,1),zlim=(-1,1),xlabel='$x_1$',ylabel='$x_2$',zlabel='$x_3$')
ax.set_xticks([-1,0,1]);ax.set_yticks([-1,0,1]);ax.set_zticks([-1,0,1])
ax.set_box_aspect((1,1,1));ax.view_init(elev=22,azim=36);ax.set_title('All four labels remain distinct')
tx.set_title('Exact label chart and retained scalar')
lines=[r'$p_j=e_j-\mathbf{1}/4,\quad q_j=Ke_j$',
       r'$x_1=(p_M-p_N)/\sqrt{2}$',
       r'$x_2=(p_M+p_N-2p_T)/\sqrt{6}$',
       r'$x_3=(p_M+p_N+p_T-3p_E)/\sqrt{12}$',
       r'$p=H^{\mathsf{T}}x,\quad q=K(p+\tau\mathbf{1})$',
       r'$\Theta(q_j)=(y_j,1/4),\quad\sum_jy_j=0$',
       r'$\widehat P(y_j,1/4)=(2iy_M,i/2)$']
for j,line in enumerate(lines):tx.text(0,.92-.125*j,line,fontsize=14)
fig.suptitle('The four labels and the scalar lost by the singular conductor',fontsize=17,y=.98)
fig.text(.5,.015,'FSR4–20. Exact orthonormal display coordinates on the real zero-mean label space; inverse map shown.\nThe original complex coordinates are recovered by K. Their full Gamma norms, including the scalar cross term, remain FSR20.',ha='center',fontsize=10)
fig.tight_layout(rect=(0,.12,1,.93));save(fig,'31_singular_four_labels')
print('Rendered four exact scientific diagrams, PNG and SVG; one bounded 3D tetrahedron.')
