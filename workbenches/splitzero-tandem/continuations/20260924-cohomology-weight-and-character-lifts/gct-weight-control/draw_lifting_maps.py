from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

root=Path(__file__).resolve().parent
fig,ax=plt.subplots(figsize=(13.8,13),dpi=180)
fig.patch.set_facecolor('#f4f6fa'); ax.set_facecolor('#f4f6fa')
ax.set_xlim(0,100);ax.set_ylim(0,100);ax.axis('off')

def txt(x,y,s,size=14,color='#192539',ha='left',weight='normal'):
    ax.text(x,y,s,fontsize=size,color=color,ha=ha,va='center',weight=weight)
def panel(y,h,title,color):
    ax.add_patch(FancyBboxPatch((2,y),96,h,boxstyle='round,pad=0.6,rounding_size=1.2',
                              facecolor='white',edgecolor=color,linewidth=1.5))
    txt(5,y+h-3,title,17,color,weight='bold')
def arrow(x,y,u,v,color='#354357'):
    ax.annotate('',xy=(u,v),xytext=(x,y),arrowprops=dict(arrowstyle='->',lw=1.8,color=color))

txt(3,97,'Which lifting map is being calculated?',23,weight='bold')
txt(3,93.3,r'Support: $\tau\langle Z_1;\mathrm{no}\ Z_2\rangle$.  All rows below act on specified coefficient spaces.',12)

panel(64,26,'1. Deligne’s actual localization cross', '#286855')
txt(8,81,r'$0\longrightarrow K_i\longrightarrow B_i\overset{\pi_i}{\longrightarrow}C_i\longrightarrow0$',19)
txt(11,75,r'$A_i\ \longrightarrow\ B_i\ \overset{\partial_i}{\longrightarrow}\ O_i$',18)
txt(57,81,r'$w(C_i)\leq i$',16)
txt(57,76.5,r'$w(K_i),w(O_i)\geq i+1$',16)
txt(8,69.5,r'$W_iB_i\simeq C_i,\qquad \partial_i(W_iB_i)=0$',18,color='#286855')
txt(8,66.3,'Deligne, Weil II §3.6; DC5–DC9. Proper geometric model, inertia, duality and twists retained.',10.5)

panel(34,27,'2. Constructed character-shifted original-zeta modules', '#244d88')
txt(8,52,r'$0\longrightarrow W(-1)\longrightarrow E\longrightarrow V\longrightarrow0$',18)
txt(8,46.8,r'$w_a(a^\rho)=2\operatorname{Re}\rho\in(0,2)$',16)
txt(55,46.8,r'$w_a(a^{\rho+1})\in(2,4)$',16)
txt(8,41.7,r'$\mathcal{D}^{\prime}_a(X)=aF_{a,W}X-XF_{a,V}=a\mathcal{D}_a(X)$',16)
txt(8,37.6,r'$X=-(\mathcal{D}^{\prime}_a)^{-1}(Y^{\prime}_a)$',17,color='#244d88')
txt(8,34.9,'ZTM2–ZTM5: full nilpotents; unique lift for all recovered characters; finite sums and algebraic direct sums.',9.5)

panel(5,26,'3. The unshifted whole analytic source', '#9a5630')
txt(8,22.8,r'$0\longrightarrow\mathcal{I}\longrightarrow\mathcal{B}\longrightarrow\mathcal{Q}\longrightarrow0$',19)
txt(8,17.5,r'$[F_0/(s-\rho)]\quad\overset{\delta_{\rho,1}}{\longmapsto}\quad[F_0]\ne0$',18)
txt(8,12.5,r'Both connecting lines carry $a^\rho$: the weights coincide.',16,color='#9a5630')
txt(8,8.4,r'$F_0(s)=\dfrac{s(s-1)}{8}\pi^{-s/2}\Gamma(s/2)\zeta(s)$',15)
txt(8,5.7,'GLB1–GLB8, ZLB1–ZLB11: this exact eigenfunction lift is not asserted to be the programme’s geometric lift.',9.5)
txt(3,1.8,'Diagram positions are schematic. They assign no coordinates, arithmetic or metric to the supporting datum.',10)

fig.savefig(root/'lifting_maps_and_weights.png',bbox_inches='tight',facecolor=fig.get_facecolor())
fig.savefig(root/'lifting_maps_and_weights.svg',bbox_inches='tight',facecolor=fig.get_facecolor())
plt.close(fig)
print(root/'lifting_maps_and_weights.png')
