"""Reproducible exact-map illustration of MR8--23; not a numerical plot."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

P=Path(__file__).resolve().parent
fig,ax=plt.subplots(figsize=(14,11),dpi=140)
ax.set(xlim=(0,14),ylim=(0,11));ax.axis('off')
ink='#162A3B';blue='#DDEEF8';green='#E1F0E6';gold='#FFF1D8'
def box(x,y,w,h,text,color=blue,size=14):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.12',
                facecolor=color,edgecolor=ink,linewidth=1.2))
    ax.text(x+w/2,y+h/2,text,ha='center',va='center',fontsize=size,color=ink,
            linespacing=1.7)
def arrow(a,b,label='',offset=(0,0)):
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=17,color=ink,linewidth=1.3))
    ax.text((a[0]+b[0])/2+offset[0],(a[1]+b[1])/2+offset[1],label,
            fontsize=12,ha='center',va='center',color=ink)

ax.text(.25,10.75,'The original kernel, with every source relation retained',
        fontsize=20,weight='bold',color=ink)
ax.text(.25,10.29,r'Exact finite maps: $S=k/2+iu$, $q=(k+1)^2$, $m=8k-16$, $r=q-m$, $d=N+1$.',fontsize=13,color=ink)
ax.text(.25,9.94,r'Original simple-packet five-orbit domain; $k\geq9$, $k=1\ (\mathrm{mod}\ 4)$, $N\geq q-1$.',fontsize=11,color=ink)
box(.3,7.8,4.3,1.9,'Original polynomial source\n'+r'$\mathcal{P}_N,\quad \|P\|_\mu^2=\int|P(k/2+iu)|^2d\mu$'+'\n'+r'$\ker E_d=\chi\mathcal{P}_{N-q}$',size=13)
box(8.5,7.8,5.1,1.9,'All original root values\n'+r'$E_dP=(P(v_{ab}))_{ab}$'+'\n'+r'$C_d=E_dH_d^{-1}E_d^*>0$',size=14)
arrow((4.75,8.75),(8.35,8.75),r'$E_d$',(0,.34))
ax.text(6.5,8.0,'Minimize in the entire source\nbefore restriction',ha='center',va='center',fontsize=12,color=ink)
box(.3,5.35,4.3,1.5,'Original kernel coordinates\n'+r'$x\in\mathbb{C}^m$',green)
box(8.5,5.35,5.1,1.5,'Actual invisible root values\n'+r'$\pi^T x\in\ker Z^T$',green)
arrow((4.75,6.1),(8.35,6.1),r'$\pi^T$  (ordinary transpose)',(0,.36))
arrow((11.05,7.65),(11.05,7.0),'',(.0,.0))
ax.text(11.05,7.28,r'$H_{K,N}=\overline{\pi} C_d^{-1}\pi^T$',ha='center',fontsize=13,color=ink,bbox={'facecolor':'white','edgecolor':'none','pad':3})
ax.text(.45,4.91,r'$Z=[M_A,\ S_kZ_k]$: the whole invariant image, not only the conductor columns $M_A$.',fontsize=13,color=ink)
box(.3,2.6,13.3,1.85,'',gold)
ax.text(6.95,4.08,r'$\det H_{K,N}=g_{\pi,Z}\,\dfrac{\det(Z^TC_d\overline{Z})}{\det C_d}$',ha='center',va='center',fontsize=16,color=ink)
ax.text(6.95,3.2,r'$=\dfrac{g_{\pi,Z}}{|V_\chi|^2}\,\dfrac{\sum_{|I|=|J|=r}z_I\overline{z_J}V_I\overline{V_J}\,B_{N+1-r}(\chi_I,\chi_J)}{B_{N+1-q}(\chi,\chi)}$',ha='center',va='center',fontsize=16,color=ink)
ax.text(.4,2.12,r'Every $I\ne J$ cross term remains. The numerator size is $n+m$, not $n=N+1-q$.',fontsize=13,color=ink)
ax.text(.4,1.63,r'Gamma receiver: $|\mathcal{R}\log\det H_K-\mathcal{R}\log\det H_K^\sigma|\leq 2mL_k^{\mathrm{form}}=o(kq)$.',fontsize=14,color=ink)
ax.text(.4,1.16,r'$\mathcal{R}f=f_{q-1}+f_q-f_{2q-1}-f_{2q}$. The $kq$ coefficient is not evaluated by this diagram.',fontsize=12,color=ink)
ax.text(.4,.58,'Proof: MR8–23. Human source: Akemann–Vernizzi, hep-th/0212051v2, Th and deg.\nOriginal programme inputs: OCF1–24, Toda (11)–(16), JM21–28. This is an exact-map schematic.',fontsize=10,color=ink,linespacing=1.6)
fig.savefig(P/'ORIGINAL_KERNEL_MAP.png',bbox_inches='tight',facecolor='white')
fig.savefig(P/'ORIGINAL_KERNEL_MAP.svg',bbox_inches='tight',facecolor='white')
plt.close(fig)
print('Figure sources and outputs ready.')
