from pathlib import Path
from itertools import product
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
root=Path(__file__).resolve().parent
fig,ax=plt.subplots(figsize=(8.3,9.6))
ax.set(xlim=(0,10),ylim=(0,12));ax.axis('off')
def t(x,y,s,**kw):ax.text(x,y,s,ha='center',va='center',**kw)
def arr(a,b,color='#617c99'):
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle='->',mutation_scale=12,color=color,lw=1.3))
t(5,11.55,'Tensor sectors retained by the original operators',fontsize=16,weight='bold')
t(5,10.95,r'$A_p\ell_{ab}=\alpha_{ab}\ell_{ab},\quad\alpha_{ab}=(2a-k)\delta\log p+i(2b-k)\gamma\log p$',fontsize=11)
t(2.4,10.15,r'$\ell_{ab}$',fontsize=15,color='#235c8c')
t(7.6,10.15,r'$\ell_{k-a,k-b}$',fontsize=15,color='#235c8c')
t(2.4,9.7,r'$\alpha_{ab}$',fontsize=14)
t(7.6,9.7,r'$-\alpha_{ab}$',fontsize=14)
arr((3,9.5),(4.6,8.95));arr((7,9.5),(5.4,8.95))
t(5,8.65,r'$A_p^{[2]}(\ell_{ab}\otimes\ell_{k-a,k-b})=0$',fontsize=14)
t(5,8.08,r'$q=(k+1)^2$ independent vectors; uncentred exponent $k\log p$ is retained.',fontsize=10)
ax.plot([.3,9.7],[7.65,7.65],color='#c6ced7')
t(5,7.27,r'Nilpotent tensor block: $Re=\epsilon f$, $Rf=0$, $\epsilon>0$',fontsize=14,weight='bold')
t(5,6.8,r'$X_3=R\otimes I\otimes I+I\otimes R\otimes I+I\otimes I\otimes R$',fontsize=12)
words=[''.join(w) for w in product('ef',repeat=3)]
coords={}
for grade in range(4):
    row=[w for w in words if w.count('f')==grade]
    for i,w in enumerate(row):coords[w]=(5+(i-(len(row)-1)/2)*2,6.2-grade*.8)
for word,(x,y) in coords.items():
    for i,c in enumerate(word):
        if c=='e':
            nxt=word[:i]+'f'+word[i+1:]
            xx,yy=coords[nxt]
            arr((x,y-.12),(xx,yy+.15))
for word,(x,y) in coords.items():
    t(x,y,word,fontsize=12,bbox=dict(fc='white',ec='#aebdcb',boxstyle='round,pad=.22'))
for grade in range(4):
    t(.85,6.2-grade*.8,r'$r='+str(grade)+'$',fontsize=11,color='#52667b')
t(8.9,5,'Every arrow has\ncoefficient '+r'$\epsilon$'+'.',fontsize=10,color='#52667b')
t(5,3.1,r'$\ker X_3=\mathrm{span}\{ffe-fef,\ fef-eff,\ fff\}$',fontsize=13)
t(5,2.62,'Words denote the displayed tensor factors. The original orthonormal e, f\nand their tensor metric are retained; the three kernel vectors need not be orthogonal.',fontsize=10)
ax.plot([.3,9.7],[2.1,2.1],color='#c6ced7')
t(5,1.6,r'$\dim\ker R^{[t]}=\sum_{j=0}^{t}\binom{t}{j}(q-2)^{t-j}\binom{j}{\lfloor j/2\rfloor}$',fontsize=15)
t(5,.88,'Complete receiver proofs: OLR23–31. Lattice lifts: OLR16–17.\nSource locality: Connes–Consani, arXiv:2606.06604v1, Definition defnloc.\nThese local tensor sectors do not impose a purity theorem on the original object.',fontsize=9,color='#52667b')
fig.subplots_adjust(left=.015,right=.985,top=.985,bottom=.015)
for ext in ['pdf','svg','png']:fig.savefig(root/('ORIGINAL_TENSOR_SECTORS.'+ext),dpi=170)
plt.close(fig)
print('Rendered original tensor sectors.')
