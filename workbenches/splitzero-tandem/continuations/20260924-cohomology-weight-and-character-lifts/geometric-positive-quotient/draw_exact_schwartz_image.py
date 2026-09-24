"""Reproduce the exact source, endpoint, and cohomology maps, SSI1–SSI10."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

base=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,
                     'mathtext.fontset':'dejavusans','svg.fonttype':'none'})
fig=plt.figure(figsize=(13.2,8.7),facecolor='white')
ax=fig.add_axes([.035,.045,.93,.91]);ax.set_xlim(0,13);ax.set_ylim(0,8.4);ax.axis('off')
blue='#234f7c';green='#237766';gray='#424a55'
ax.text(0,8.15,'Exact source lift, with every endpoint retained',fontsize=20,weight='bold',color=blue)
ax.text(0,7.72,'Original zeta coefficients • complete zero multiplicities • no image closure required',fontsize=11.8,color=gray)

def box(x,y,w,h,color):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.07,rounding_size=0.07',
                              facecolor=color,edgecolor='#cad1d8',linewidth=1))
def arrow(p,q,label,offset=.16):
    ax.annotate('',xy=q,xytext=p,arrowprops={'arrowstyle':'->','lw':1.7,'color':blue})
    ax.text((p[0]+q[0])/2,(p[1]+q[1])/2+offset,label,ha='center',va='bottom',fontsize=13,color=blue)

box(.08,4.44,12.79,2.84,'#f5f8fc')
ax.text(.32,6.99,'The actual commuting maps  |  SSI1–SSI6',fontsize=12,weight='bold',color=blue)
ax.text(1.1,6.18,r'$S$',fontsize=24,ha='center')
ax.text(6.0,6.18,r'$J\subset A$',fontsize=24,ha='center')
ax.text(11.2,6.18,r'$I\subset\mathcal{B}$',fontsize=24,ha='center')
arrow((1.65,6.36),(4.85,6.36),r'$\Sigma f(u)=2\sum_{n\geq1}f(nu)$')
arrow((7.1,6.36),(9.95,6.36),r'$\mathcal{M}_0 b(s)=\int_0^\infty b(u)u^s\,du/u$')
ax.text(.43,5.7,r'$S:$ even Schwartz $f$,  $f(0)=0$,  $\int_{\mathbb{R}}f=0$',fontsize=12.5)
ax.text(.43,5.28,r'$I:$ $F^{(j)}(\rho)=0$ for every original nontrivial zero,  $0\leq j<m_\rho$',fontsize=12.5)
ax.text(.43,4.8,r'Both displayed maps are topological isomorphisms onto their images;  $J=\overline{J}$.',fontsize=12.3,color=green)

box(.08,1.84,6.22,2.23,'#f3faf7')
ax.text(.32,3.77,'Inverse and source jets  |  SSI5–SSI7',fontsize=12,weight='bold',color=green)
ax.text(.35,3.28,r'$H(s)=F(s)/(2\zeta(s))$',fontsize=15)
ax.text(.35,2.76,r'$f(x)=\frac{1}{2\pi}\int_{\mathbb{R}}H(2+it)x^{-2-it}\,dt$',fontsize=14.5)
ax.text(.35,2.21,r'$\frac{f^{(2r)}(0)}{(2r)!}=\frac{F(-2r)}{2\zeta^\prime(-2r)}\quad(r\geq1)$',fontsize=15)

box(6.6,1.84,6.27,2.23,'#f5f8fc')
ax.text(6.86,3.77,'Ordinary cohomology  |  SSI8, SSI10',fontsize=12,weight='bold',color=blue)
ax.text(6.87,3.23,r'$H^1(X,\Omega)=A/J\ \simeq\ \mathcal{B}/I$',fontsize=16)
ax.text(6.87,2.69,r'$\overline{J}/J=0$',fontsize=17,color=green)
ax.text(6.87,2.2,'All zero jets remain; four endpoint lines remain in H⁰.',fontsize=11.5)

ax.text(.1,1.31,r'At the endpoints:  $\int_0^\infty f(x)\,dx/x=-F(0)$,   $\int_0^\infty f(x)\log x\,dx=F(1)/2$.',fontsize=13)
ax.text(.1,.8,'The vanished quotient is the image-versus-closure difference. The Deligne weight-separation goal remains open.',fontsize=11.6,color=gray)
ax.text(.1,.30,'Proofs: EXACT_SCHWARTZ_SUMMATION_IMAGE.md, SSI0–SSI10; independent check, ESI0–ESI10.\nSource construction: Connes–Consani, arXiv:0903.2024v3, §5. This figure displays maps, not numerical samples.',fontsize=9.4,color=gray)
for ext in ['png','svg']:
    fig.savefig(base/f'exact_schwartz_image.{ext}',dpi=180,facecolor='white')
print('Created exact_schwartz_image.png and .svg')
