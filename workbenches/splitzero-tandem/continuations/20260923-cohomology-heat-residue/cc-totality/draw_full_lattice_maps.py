from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

root=Path(__file__).resolve().parent
plt.rcParams.update({'font.size':11,'font.family':'DejaVu Sans','svg.fonttype':'none'})
blue='#235c8c'; green='#24734b'; red='#a12632'; grey='#657080'
fig=plt.figure(figsize=(8.3,10.4))
ax=fig.add_axes([.035,.035,.93,.93]); ax.set(xlim=(0,10),ylim=(0,13)); ax.axis('off')
def label(x,y,t,**kw):
    ax.text(x,y,t,ha='center',va='center',**kw)
def arrow(a,b,color=blue,style='->',lw=1.4):
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle=style,mutation_scale=13,color=color,lw=lw))
label(5,12.65,'The whole lattice map and its prime fibres',fontsize=16,weight='bold')
label(5,12.13,r'$L=\{0<a<1\}$, with join and meet; $K=([0,\infty),\max,\cdot)$.',fontsize=11)
label(5,11.65,r'$G_L(\mathbb{Z})\ \longrightarrow\ \mathbb{Z}\times(K\otimes_{\mathbb{B}}L)$',fontsize=15)
label(5,11.12,r'$(r,\lambda)\ \longmapsto\ (r,\mathbf{1}_{\{j\leq\lambda\}})$',fontsize=14)
table=[(r'$\tau=z_0$',r'$(0;(0,0))$'),(r'$z_a$',r'$(0;(1,0))$'),
       (r'$e=z_1$',r'$(0;(1,1))$'),(r'$\widehat n\quad(n\neq0)$',r'$(n;(1,1))$')]
for j,(left,right) in enumerate(table):
    y=10.6-.43*j; label(3,y,left,color=blue); arrow((4,y),(5,y)); label(6.4,y,right)
ax.plot([.6,9.4],[8.7,8.7],color='#c6ced7',lw=1)
label(5,8.35,'Prime contraction: the complete fibres',fontsize=14,weight='bold')
label(2,7.85,r'$\mathrm{Spec}(K\otimes_{\mathbb{B}}L)$',fontsize=12)
label(7.15,7.85,r'$\mathrm{Spec}\,G_L(\mathbb{Z})$',fontsize=12)
left=[(2,7.2,r'$\mathfrak{p}_{11}=\{(0,0)\}$'),
      (2,6.3,r'$\mathfrak{p}_{22}=\{(u,0):u\geq0\}$'),
      (2,5.4,r'$\mathfrak{p}_{12}=\{0\}\cup\{u>v\}$')]
right=[(7.2,7.2,r'$P_{\{0\}}$'),(7.2,6.3,r'$P_{\{0,a\}}$'),
       (7.2,4.8,r'$Q_{(0)}$'),(6.4,3.8,r'$Q_{(2)}$'),(8,3.8,r'$Q_{(3)}$')]
for x,y,s in left+right:
    label(x,y,s,fontsize=11,bbox=dict(boxstyle='round,pad=.28',fc='white',ec='#c6ced7'))
for ya,yb in [(7.02,6.53),(6.1,5.62)]:arrow((2,ya),(2,yb),grey)
arrow((7.2,7),(7.2,6.55),grey); arrow((7.2,6.06),(7.2,5.04),grey)
arrow((7.1,4.57),(6.5,4),grey);arrow((7.3,4.57),(7.9,4),grey)
for start,end in [((4.0,7.2),(6.45,7.2)),((4,6.3),(6.35,6.3)),((4.05,5.4),(6.4,6.13))]:arrow(start,end,blue)
label(2.6,4.8,r'$\eta=(0)\in\mathrm{Spec}\,\mathbb{Z}$',color=green,fontsize=12)
arrow((4.0,4.8),(6.52,4.8),green)
label(3,4.15,'Each arithmetic prime has its\none original ring-prime preimage.',fontsize=10,color=green)
label(5,3.1,'Grey arrows: strict prime inclusion. Blue/green arrows: contraction.\nOnly primes 2 and 3 are drawn; every rational prime remains.',fontsize=10,color=grey)
ax.plot([.6,9.4],[2.6,2.6],color='#c6ced7',lw=1)
label(5,2.24,'The additional prime is retained',fontsize=14,weight='bold')
label(5,1.75,r'$(2,1)\in\mathfrak{p}_{12},\quad(2,1)\notin\mathfrak{p}_{11}\cup\mathfrak{p}_{22}.$',fontsize=13)
label(5,1.17,r'$\mathrm{Fr}_0^{-1}(\mathfrak{p}_{12})=\mathfrak{p}_{22},\qquad\mathrm{Fr}_t^{-1}(\mathfrak{p}_{ij})=\mathfrak{p}_{ij}\ (t>0).$',fontsize=12)
label(5,.45,'Proofs: ASL18–22, ASL31; LSP3–27. Tropical coefficients: Connes–Consani,\nGeometry of the Arithmetic Site, arXiv:1502.05580v1, Definition defnpt.\nFull lattice base: The Clankers, Split Support Geometry v11, def:lattice-split.',fontsize=9,color=grey)
for ext in ['pdf','svg','png']:
    fig.savefig(root/('FULL_LATTICE_PRIME_MAP.'+ext),dpi=170)
plt.close(fig)
print('Rendered exact full-lattice prime map.')
