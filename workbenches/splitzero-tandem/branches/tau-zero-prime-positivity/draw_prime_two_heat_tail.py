"""Exact support intervals and proved full-derivative bounds, PT7–PT40."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
P=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':13})
L=np.log(2);r=1/64;end=583/800;start=L+2*r
fig=plt.figure(figsize=(14,8.2),layout='constrained')
grid=fig.add_gridspec(3,2,height_ratios=[1,1.2,.65])
ax=fig.add_subplot(grid[0,0])
ax.plot([L-2*r,start],[1,1],color='#cd9d47',lw=12,solid_capstyle='butt')
ax.plot([start,end],[.55,.55],color='#af3d44',lw=12,solid_capstyle='butt')
ax.axvline(start,ls=':',color='#333');ax.axvline(end,ls=':',color='#333')
ax.text(L,.78,'Original prime-2 atom window',ha='center',fontsize=11)
ax.text(L,.23,r'$-\beta L^2h(a-L)=0$ for $a\geq L+2r$',ha='center',fontsize=13)
ax.set(xlim=(L-2*r-.008,end+.008),ylim=(.05,1.27),yticks=[],xlabel='Original translation a',title='The atom vanishes at the right edge')
ax.spines[['top','left','right']].set_visible(False)
ax=fig.add_subplot(grid[0,1])
ax.plot([start,end],[.7,.7],color='#af3d44',lw=14,solid_capstyle='butt')
ax.set(xlim=(start-.0004,end+.0004),ylim=(.2,1.3),yticks=[],xticks=[start,end],xticklabels=[r'$\log2+1/32$',r'$583/800$'],xlabel='Enlarged view of the same interval',title='The complete derivative is negative here')
ax.text((start+end)/2,1.03,r'$K_0(a)=-R_r(a)<0$',ha='center')
ax.text((start+end)/2,.30,r'$\dot K_{0+}(a)<-286628/27$',ha='center',fontsize=16,color='#af3d44')
ax.spines[['top','left','right']].set_visible(False)
ax=fig.add_subplot(grid[1,:]);ax.axis('off')
ax.text(.5,.93,r'$\dot K_{0+}(a)=\mathcal{A}(a)+\mathcal{C}_2(a)$',ha='center',fontsize=23)
ax.text(.25,.65,r'$\mathcal{A}(a)=\frac{1}{4}\int \mathcal{W}_\alpha(v)k(a-v)\,dv$',ha='center',fontsize=17)
ax.text(.75,.65,r'$\mathcal{C}_2(a)=-\frac{\beta}{2}\int [LW(v)+B(v)]k(a-L-v)\,dv$',ha='center',fontsize=16)
ax.text(.25,.38,r'$|\mathcal{A}(a)|<\frac{17068}{27}$',ha='center',fontsize=22,color='#216782')
ax.text(.75,.38,r'$\mathcal{C}_2(a)<-28120\beta<-11248$',ha='center',fontsize=21,color='#af3d44')
ax.text(.5,.11,r'$\dot K_{0+}(a)<\frac{17068}{27}-11248=-\frac{286628}{27}$',ha='center',fontsize=22)
ax=fig.add_subplot(grid[2,:]);ax.axis('off')
ax.text(.5,.83,r'$L=\log2,\quad\beta=L/\sqrt{2},\quad r=1/64,\quad k=b_r*b_r\geq0,\quad\int k=1$',ha='center',fontsize=15)
ax.text(.5,.47,r'$\dot{\mathbf{B}}=0,\qquad\dot{\mathbf{Z}}=\dot K_{0+}(a)\mathbf{e}_{1_L},\qquad\dot{\mathbf{D}}=-\dot K_{0+}(a)\mathbf{e}_{1_L}$',ha='center',fontsize=18)
ax.text(.5,.09,'Exact support intervals and proved bounds, not sampled zeros.  Original heat time and all Gamma terms retained.  PT7–PT40.',ha='center',fontsize=11)
fig.suptitle('A surviving mixed prime term controls the full infinitesimal heat response',fontsize=21)
for ext in ['png','svg']:fig.savefig(P/f'prime_two_heat_tail.{ext}',dpi=160)
print('Rendered prime_two_heat_tail.png and .svg')
