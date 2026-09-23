from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
P=Path(__file__).resolve().parent
plt.rcParams.update({'font.size':11,'mathtext.fontset':'dejavusans','axes.spines.top':False,'axes.spines.right':False})
fig=plt.figure(figsize=(12,8.4),layout='constrained')
gs=fig.add_gridspec(2,2,height_ratios=[1,1.13])
ax=fig.add_subplot(gs[0,:])
ns=np.array([1,2,3,4,5,6,7,10,15,30,31,60])
sp=np.array([any(n%p==0 for p in (2,3,5)) for n in ns])
mat=np.array([sp,~sp,ns%30!=0,np.ones(len(ns),bool)],int)
ax.imshow(mat,cmap=ListedColormap(['#eef0f3','#007f86']),vmin=0,vmax=1,aspect='auto')
ax.set_xticks(range(len(ns)),ns);ax.set_xlabel(r'Original basis index $n$; cutoff $D=5$')
ax.set_yticks(range(4),[r'Sparse support $\chi_5$',r'Least correction $\mathcal{M}_5$',r'Summed correction $\mathcal{K}_5$',r'Raw Fourier support'])
for i in range(4):
    for jn in range(len(ns)):ax.text(jn,i,'top' if mat[i,jn] else 'bottom',ha='center',va='center',color='white' if mat[i,jn] else '#36404a',fontsize=9)
ax.set_title('A. Two exact support corrections retained separately (PM15–23)',loc='left',fontweight='bold')
ax.set_xticks(np.arange(-.5,len(ns),1),minor=True);ax.set_yticks(np.arange(-.5,4,1),minor=True);ax.grid(which='minor',color='white',lw=2);ax.tick_params(which='minor',bottom=False,left=False)
bx=fig.add_subplot(gs[1,0])
r=1/64;a=np.log(2)
for y,c,lab,col in [(2,0,r'$f_r$: $[-1/64,1/64]$','#007f86'),(1,a,r'$(f_r)_a$: $[a-1/64,a+1/64]$','#b74c33')]:
    bx.plot([c-r,c+r],[y,y],lw=11,color=col,solid_capstyle='butt')
    bx.text(.08,y+.21,lab,fontsize=10)
bx.plot([a-2*r,a+2*r],[0,0],lw=11,color='#61509c',solid_capstyle='butt')
bx.text(.08,.23,r'Prime window $[a-1/32,a+1/32]$',fontsize=10)
bx.axvline(a,color='#b74c33',ls=':',alpha=.6);bx.axvline(0,color='#007f86',ls=':',alpha=.6)
bx.set_xlim(-.05,.86);bx.set_ylim(-.6,2.6);bx.set_yticks([]);bx.set_xticks([0,a],[r'$0$',r'$a=\log 2$']);bx.set_xlabel('Original logarithmic coordinate')
bx.set_title('B. Exact supports at one displayed separation',loc='left',fontweight='bold',fontsize=11)
cx=fig.add_subplot(gs[1,1]);cx.axis('off')
box=dict(boxstyle='round,pad=.5',fc='#f5f7fa',ec='#909ba5')
cx.text(.5,.86,r'$M_{f_r}(s)=s(s-1)\prod_{j\geq1}\frac{\sinh(r2^{-j}(s-1/2))}{r2^{-j}(s-1/2)}$',ha='center',va='center',bbox=box,fontsize=10)
cx.text(.5,.62,'Nonzero at every possible off-critical zero',ha='center',va='center',fontsize=10)
cx.annotate('',xy=(.5,.47),xytext=(.5,.56),arrowprops=dict(arrowstyle='->',lw=1.6))
cx.text(.5,.36,r'$K_r(a)=-T^2Y_r(a)-R_r(a),\quad R_r(a)>0$'+'\n'+r'$a>1/32,\quad T=\partial_a^2-1/4$',ha='center',va='center',bbox=box,fontsize=10)
cx.text(.5,.10,r'$\mathrm{RH}\ \Longleftrightarrow\ |K_r(a)|\leq K_r(0)$'+'\n'+'for every separation; the bound is unresolved',ha='center',va='center',fontsize=10)
cx.set_title('C. Complete all-zero arithmetic criterion (PW11–20)',loc='left',fontweight='bold',fontsize=11)
fig.suptitle('Supported prime operators and one fixed primitive test',fontsize=17,fontweight='bold')
for ext in ['png','svg']:fig.savefig(P/('primitive_prime_window.'+ext),dpi=180)
print('Rendered exact support masks, support intervals and proved maps.')
