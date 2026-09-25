from pathlib import Path
import re
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

base=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'mathtext.fontset':'dejavusans'})
fig,ax=plt.subplots(figsize=(15,10.8))
ax.set_xlim(0,15);ax.set_ylim(0,10.8);ax.axis('off')
def box(x,y,w,h,text,color='#edf4f7',size=13):
    text=re.sub(r'\\(mathcal|mathscr) ([A-Za-z])',r'\\\1{\2}',text)
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.10',facecolor=color,edgecolor='#345466',linewidth=1.3))
    ax.text(x+w/2,y+h/2,text,ha='center',va='center',fontsize=size,linespacing=1.55)
def arr(p,q,label='',offset=(0,0),size=12):
    label=re.sub(r'\\(mathcal|mathscr) ([A-Za-z])',r'\\\1{\2}',label)
    ax.add_patch(FancyArrowPatch(p,q,arrowstyle='-|>',mutation_scale=16,linewidth=1.5,color='#224b65'))
    ax.text((p[0]+q[0])/2+offset[0],(p[1]+q[1])/2+offset[1],label,ha='center',va='center',fontsize=size)
ax.text(.25,10.42,'The actual boundary has a faithful Hardy receiver',fontsize=21,weight='bold')
ax.text(.25,10.03,'Exact source maps, full reflection, and the retained cover defect — ABH2–ABH6',fontsize=13,color='#345466')
box(.35,7.72,3.10,1.52,r'$x\in H_-$'+'\nActual left off-line\nboundary coordinates')
box(5.05,7.72,4.05,1.52,r'$\lambda_x(F)=\langle\beta_r F,x\rangle$'+'\n'+r'$\lambda_x\in R_\beta^\prime$'+'\nNo receiving kernel',size=13)
box(10.78,7.72,3.85,1.52,r'$\mathcal L_{r,t}x\in H^2$'+'\nTrace-class, injective\n'+r'$\mathcal L_{r,t}x\in\mathcal N^\perp$')
arr((3.58,8.45),(4.9,8.45),r'$\overline{H_-}\to R_\beta^\prime$',(0,.47),11)
arr((9.23,8.45),(10.65,8.45),r'$\mathcal H_t$',(0,.4))
box(.35,5.42,14.28,1.73,
    r'$\mathcal L_{r,t}x=-\sum_{\lambda\in\mathscr Z_+}m_\lambda d_r(\lambda)\overline{e^{t\lambda^2}}x_{\lambda^\#}g_\lambda$'
    +'\n'+r'$\lambda^\#=1-\overline{\lambda},\quad d_r(\lambda)=e^{-i\,\mathrm{Im}(\lambda)\log r}(r^{\mathrm{Re}(\lambda)}-r^{1-\mathrm{Re}(\lambda)})$'
    +'\n'+r'$\mathcal L_{r,t}=C_+B_{r,t}^*|_{H_-}$'+'   with the full reflected Gaussian and the proved domain of '+r'$C_+$',
    '#f2f6ed',14)
arr((7.48,7.63),(7.48,7.25))
box(.35,2.87,7.08,1.85,
    r'$W_n^*\mathcal L_{r,t}=\mathcal L_{r,t}T_n$'
    +'\n'+r'$W_n^*W_n=nI,\qquad W_nW_n^*=nP_n$'
    +'\n'+r'$nK-T_n^*KT_n=n\mathcal L_{r,t}^*(I-P_n)\mathcal L_{r,t}$'
    +'\n'+r'$K=\mathcal L_{r,t}^*\mathcal L_{r,t}$',size=13)
box(7.80,2.87,6.83,1.85,
    'Every cover scale is retained'
    +'\n'+r'$\|\mathcal L_{r,t}x\|^2=\sum_{j=0}^{\infty}n^{-j}$'
    +'\n'+r'$\times\|(I-P_n)\mathcal L_{r,t}T_n^j x\|^2$'
    +'\nAll observations vanish exactly when '+r'$x=0$', '#fff2df',13)
ax.text(.5,2.37,'The near-line estimate uses the actual boundary factor:',fontsize=13,weight='bold')
ax.text(.7,1.83,r'$\|g_\lambda\|^2\leq(2\sigma-1)^{-1},\qquad'
    r'|\Delta_r(\sigma)|\leq(r+1)\log r\,(\sigma-\frac{1}{2}),\qquad \sigma=\mathrm{Re}(\lambda)>\frac{1}{2}$',fontsize=15)
ax.text(.5,.95,'No lower bound on the distance of zeros from the line is assumed.\n'
    'Original source: Noor (arXiv:1809.09577v4), with the programme’s full zeta and boundary maps.\n'
    'This is an exact map diagram; it asserts neither an off-line zero nor lifting-obstruction vanishing.',
    fontsize=12,va='center',linespacing=1.65,color='#345466')
fig.savefig(base/'actual_hardy_boundary.png',dpi=180,bbox_inches='tight')
fig.savefig(base/'actual_hardy_boundary.svg',bbox_inches='tight')
plt.close(fig)
