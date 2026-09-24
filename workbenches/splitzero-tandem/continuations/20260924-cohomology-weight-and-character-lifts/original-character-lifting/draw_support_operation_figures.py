from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle

R=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'mathtext.fontset':'dejavusans','pdf.fonttype':42,'svg.fonttype':'none'})
ink='#173248'; blue='#176b96'; teal='#137d72'; orange='#b86628'; pale='#edf5f8'
def canvas(title,subtitle):
    fig=plt.figure(figsize=(10,9),facecolor='white')
    ax=fig.add_axes([0,0,1,1]);ax.set_xlim(0,10);ax.set_ylim(0,9);ax.axis('off')
    ax.text(.4,8.62,title,color=ink,size=19,weight='bold',va='top')
    ax.text(.4,8.13,subtitle,color=ink,size=11,va='top')
    return fig,ax
def box(ax,x,y,w,h,text,color=blue,fs=12):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.08',facecolor=pale,edgecolor=color,linewidth=1.5))
    ax.text(x+w/2,y+h/2,text,ha='center',va='center',color=ink,size=fs)
def arrow(ax,start,end,color=teal):
    ax.add_patch(FancyArrowPatch(start,end,arrowstyle='-|>',mutation_scale=16,color=color,linewidth=1.7))
def save(fig,stem):
    for ext in ('pdf','svg','png'):fig.savefig(R/f'{stem}.{ext}',dpi=170,facecolor='white')
    plt.close(fig)

fig,ax=canvas('Loops retain their support basepoint',r'Exact example: $L=\{0<\alpha<1\}$, $D=0$, $\Lambda_D=\mathbb{Z}$, $e^a=1$, one coordinate.')
ax.text(.45,7.43,'All one-spheres, before any amplitude or support is discarded',weight='bold',color=ink,size=13)
rows=[(5.95,r'$\tau=(0,0)$',r'$\{\tau\}$','1 loop state'),(4.55,r'$z_\alpha=(0,\alpha)$',r'$\{\tau,z_\alpha\}$','2 loop states'),(3.15,r'$e=(0,1)$',r'$\{(-1,1),\tau,z_\alpha,e,(1,1)\}$','5 loop states')]
for y,base,states,count in rows:
    box(ax,.65,y,1.8,.75,base)
    arrow(ax,(2.6,y+.37),(3.0,y+.37))
    box(ax,3.15,y,5.2,.75,states,teal)
    ax.text(9.15,y+.37,count,ha='center',va='center',size=10,color=ink)
arrow(ax,(1.55,5.84),(1.55,5.4));arrow(ax,(1.55,4.44),(1.55,4.0))
ax.text(3.25,2.71,'Each state is a distinct elementary homotopy class.',color=ink,size=11)
ax.text(.5,2.08,'The complete zero-stage relation',color=ink,weight='bold',size=13)
ax.text(.65,1.63,r'$(b,\nu)\;\mathcal{R}\;(b^{\prime},\mu)\quad\Longleftrightarrow\quad\nu\leq\mu\quad\mathrm{and}\quad d_{\mathbb{R}/\mathbb{Z}}(b,b^{\prime})\leq1$',color=ink,size=15)
ax.text(.65,1.15,'Support may increase along an edge. The original distance bound remains.',color=ink,size=11)
ax.text(.45,.6,'Proof: SUPPORTED_DOLD_KAN_REVIEW.tex, sphere and directed-relation calculations.\nHuman source: Alain Connes and Caterina Consani, arXiv:2004.08879v1, lines 875–1231.',color=ink,size=9,va='top')
save(fig,'SUPPORT_BASEPOINT_LOOPS')

fig,ax=canvas('A returning zero is not an absent trace',r'Actual odd receiver at $d=3$: $A=-F_p^{-1}$, original blocks of dimension $q=(k+1)^2$.')
ax.text(.45,7.45,'Independent cyclic slots',color=ink,size=14,weight='bold')
for i in range(3):
    box(ax,.6+3.1*i,6.05,2.3,.8,fr'$(v_{i},\lambda_{i})$')
arrow(ax,(2.95,6.45),(3.6,6.45));arrow(ax,(6.05,6.45),(6.7,6.45))
ax.annotate('',xy=(1.75,6.95),xytext=(8,6.95),arrowprops=dict(arrowstyle='-|>',connectionstyle='arc3,rad=.2',color=teal,lw=1.7))
ax.text(4.9,7.02,r'returning corner $A$',ha='center',color=teal,size=11)
ax.text(.65,5.41,r'$\operatorname{Tr}(\mathcal{C}_3^n)=\tau\quad(3\nmid n)$',color=ink,size=17)
ax.text(.65,4.89,r'$\operatorname{Tr}(\mathcal{C}_3^{3m})=(3\operatorname{tr}(A^m),1_L)$',color=ink,size=17)
ax.text(.65,4.47,r'If the returning amplitude is zero, this is $e$, not $\tau$.',color=ink,size=12)
ax.plot([.45,9.5],[4.05,4.05],color='#bed1db')
ax.text(.45,3.69,'The exact synchronization retract',color=ink,size=14,weight='bold')
box(ax,.7,2.53,3.3,.72,r'$(\lambda_0,\lambda_1,\lambda_2)$',teal)
box(ax,6.05,2.53,3.2,.72,r'$\lambda_0\vee\lambda_1\vee\lambda_2$',orange)
arrow(ax,(4.15,2.9),(5.9,2.9));ax.text(5,3.16,r'$r$',ha='center',color=teal)
ax.text(.65,1.94,r'$rj=I,\qquad jr:(\lambda_j)_j\mapsto(\bigvee_j\lambda_j)_j$',color=ink,size=15)
ax.text(.65,1.39,r'Global synchronization gives trace $e$ also when $3\nmid n$.',color=ink,size=12)
ax.text(.65,.99,r'The cycle comparison retains $\Theta_3-\Theta_1$, with ghost $3\mathbf{1}_{3\mid n}-1$.',color=ink,size=12)
ax.text(.45,.55,'Proof: FLW7–17, FLW23–31. Every original metric entry and mass factor is retained.\nHuman source: Alain Connes and Caterina Consani, arXiv:2004.08879v1, lines 454–600.',color=ink,size=9,va='top')
save(fig,'FULL_SUPPORT_CYCLIC_TRACE')
print('Created two exact support-operation figures in PDF, SVG and PNG.')
