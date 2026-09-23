"""Reproduce the exact node, retained differential and divided-Frobenius maps."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

out=Path(__file__).resolve().parent/'figures'
plt.rcParams.update({'font.family':'DejaVu Sans','svg.fonttype':'none'})
fig,ax=plt.subplots(figsize=(16,12))
fig.patch.set_facecolor('#fcfcfa')
fig.subplots_adjust(left=.025,right=.99,bottom=.025,top=.975)
ax.set(xlim=(0,16),ylim=(0,12));ax.axis('off')
ink='#183047';blue='#245eaa';green='#157564';red='#ad3545'
ax.text(.3,11.75,'A mixed differential survives between the two branches',fontsize=24,weight='bold',color=ink,va='top')
ax.text(.3,11.15,r'$A=\mathbb{Z}[t^{\pm1},u^{\pm1}]/(xy),\quad x=t-1,\quad y=u-1,\quad\kappa=x\,du=-y\,dt$',fontsize=19,color=ink)

def box(x,y,w,h,color):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.1',fc='white',ec=color,lw=1.8))
def arrow(x1,y1,x2,y2,color=ink):
    ax.annotate('',xy=(x2,y2),xytext=(x1,y1),arrowprops={'arrowstyle':'->','color':color,'lw':1.8})

box(.4,7.05,4.2,3.4,blue)
ax.text(.65,10.1,'The two Laurent branches',fontsize=16,color=blue,weight='bold')
ax.plot([.9,4.0],[8.15,8.15],color=blue,lw=2.5)
ax.plot([2.0,2.0],[7.6,9.5],color=green,lw=2.5)
ax.scatter([2.0],[8.15],s=70,color=red,zorder=3)
ax.text(2.6,7.82,r'$u=1$',fontsize=16,color=blue)
ax.text(2.16,9.1,r'$t=1$',fontsize=16,color=green)
ax.text(2.15,8.38,r'$(t,u)=(1,1)$',fontsize=13,color=red)
ax.text(.66,7.22,'Scheme diagram; omitted points at t=0 or u=0.',fontsize=10.5,color=ink)

box(5.0,7.05,10.5,3.4,blue)
ax.text(5.3,10.1,'Restriction to both branches has an exact nonzero kernel',fontsize=16,color=blue,weight='bold')
ax.text(5.3,9.35,r'$0\longrightarrow\mathbb{Z}\kappa\longrightarrow\Omega^1_{A/\mathbb{Z}}\longrightarrow T\,dt\oplus V\,du\longrightarrow0$',fontsize=20,color=ink)
ax.text(5.3,8.63,r'$T=\mathbb{Z}[t^{\pm1}],\quad V=\mathbb{Z}[u^{\pm1}],\quad\mathrm{Ann}_A(\kappa)=(x,y)$',fontsize=17,color=ink)
ax.text(5.3,7.95,r'$H^{-1}(L_{A/\mathbb{Z}})=0,\qquad \Omega^2_{A/\mathbb{Z}}=\mathbb{Z}\omega,\quad\omega=dt\wedge du$',fontsize=17,color=ink)
ax.text(5.3,7.35,'Proofs: N1–N2, equations N7–N11. The differential sequence has no A-linear section.',fontsize=11.5,color=ink)

box(.4,2.85,9.4,3.65,green)
ax.text(.7,6.12,'The full retained complex and divided Frobenius',fontsize=17,color=green,weight='bold')
ax.text(3.9,5.53,'degree 1',fontsize=12,color=ink)
ax.text(6.45,5.53,'degree 2',fontsize=12,color=ink)
ax.text(.75,4.9,r'source: $(\Omega^\bullet,pd)$',fontsize=15,color=ink)
ax.text(.75,3.64,r'target: $(\Omega^\bullet,d)$',fontsize=15,color=ink)
for yy in (4.9,3.64):
    ax.text(4.0,yy,r'$\mathbb{Z}\kappa$',fontsize=20,color=ink)
    ax.text(6.6,yy,r'$\mathbb{Z}\omega$',fontsize=20,color=ink)
    arrow(5.04,yy+.12,6.38,yy+.12)
ax.text(5.55,5.22,r'$p$',fontsize=17,color=ink)
ax.text(5.55,3.96,r'$1$',fontsize=17,color=ink)
arrow(4.43,4.73,4.43,4.06);arrow(7.02,4.73,7.02,4.06)
ax.text(4.62,4.36,r'$p$',fontsize=17,color=green)
ax.text(7.21,4.36,r'$1$',fontsize=17,color=green)
ax.text(7.93,4.92,r'$H^2=\mathbb{Z}/p$',fontsize=15,color=red)
ax.text(7.93,3.68,r'$H^2=0$',fontsize=15,color=ink)
ax.text(.75,3.13,r'$d\kappa=\omega,\qquad dF_i=pF_{i+1}d$',fontsize=17,color=green)

box(10.2,2.85,5.3,3.65,red)
ax.text(10.48,6.1,'Linearization retains more',fontsize=17,color=red,weight='bold')
ax.text(10.48,5.44,r'$\mathfrak{m}=(x,y),\quad Q_p(z)=\sum_{i=0}^{p-1}z^i$',fontsize=15,color=ink)
ax.text(10.48,4.83,r'$A/\phi(\mathfrak{m})\longrightarrow\mathbb{Z}\kappa$',fontsize=18,color=ink)
ax.text(10.48,4.29,r'$[a]\longmapsto p\,a(1,1)\kappa$',fontsize=17,color=ink)
ax.text(10.48,3.72,r'$\ker\cong T/(Q_p(t))\oplus V/(Q_p(u))$',fontsize=14.5,color=ink)
ax.text(10.48,3.19,r'$\mathrm{rank}_{\mathbb{Z}}\ker=2p-2,\quad\mathrm{coker}=\mathbb{Z}/p$',fontsize=15,color=red)

ax.text(.55,2.14,'The ring comes from the retained programme cross-effect by exact quotient maps:',fontsize=16,color=ink)
ax.text(.55,1.52,r'$W\cong jR\longrightarrow jR/j^2R\cong A,\qquad \ker=j^2R;\qquad(B,(p))\longrightarrow(B/jB,(p))$',fontsize=19,color=ink)
ax.text(.55,.92,'The right-hand map is a quotient of crystalline prisms. The differential calculation keeps its mixed classes and their maps.',fontsize=13,color=ink)
ax.text(.55,.36,'Proofs: Node cotangent, N6–N13, N21–N27, N31–N32. Human foundations: Illusie I, II 2.1.2 and III 3.2.4; prism sources in F3.',fontsize=11.8,color=ink)
for ext in ('png','svg'):
    fig.savefig(out/f'13_node_differentials.{ext}',dpi=150,facecolor=fig.get_facecolor())
plt.close(fig)
