"""Reproducible diagram of RD18--RD31; positions are schematic."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
P=Path(__file__).resolve().parent
fig,ax=plt.subplots(figsize=(13,8.3))
fig.patch.set_facecolor('#faf9f6')
ax.set(xlim=(0,13),ylim=(0,8.3));ax.axis('off')
def box(x,y,w,h,text,fc='#eef3f6',size=12):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.15',facecolor=fc,edgecolor='#62788b',linewidth=1.2))
    ax.text(x+w/2,y+h/2,text,ha='center',va='center',fontsize=size,linespacing=1.6)
def arrow(a,b,label='',dy=.2):
    ax.annotate('',xy=b,xytext=a,arrowprops={'arrowstyle':'->','color':'#254d69','lw':1.8})
    ax.text((a[0]+b[0])/2,(a[1]+b[1])/2+dy,label,ha='center',fontsize=11)
ax.text(.1,7.92,'What detects the infinitesimal, and where its trace vanishes',fontsize=18,weight='bold')
ax.text(.1,7.48,r'Exact collision maps (RD16–RD20): $C_0=\mathbb{C}[T]/(T^4)$,  $D(T)=-T^3/16$',fontsize=13)
box(.15,5.46,3.68,1.42,'Perfect residue pairing\n'+r'$Q_{\rm res}(f,g)=i[T^3](f^*g)$'+'\nInertia (2, 2, 0)')
box(8.1,5.46,4.5,1.42,'Regular trace pairing\n'+r'$Q_{\rm tr}(f,g)=4\overline{f_0}g_0$'+'\nInertia (1, 0, 3)',fc='#edf4eb')
arrow((4.02,6.18),(7.9,6.18),r'$Q_{\rm tr}(f,g)=Q_{\rm res}(f,Kg)$',.46)
ax.text(5.93,5.58,r'$K=-4iM_{T^3}$',ha='center',fontsize=13)
box(3.9,4.12,4.1,.87,r'$\ker K=(T),\quad \operatorname{im}K=\mathbb{C}T^3$'+'\n'+r'$K^2=0,\quad D\ne0$',fc='#fbefe7',size=12)
ax.text(.1,3.48,'Full Weil packet (RD25–RD31): original amplitude and reflection retained',fontsize=13,weight='bold')
box(.15,1.8,3.6,1.13,r'$E_h=\mathbb{C}[s]/(d^m)$'+'\n'+r'$U=M_{j_h(2\xi/h)}$')
box(7.85,1.8,4.73,1.13,r'$B_h(f,g)=Q_h(Uf,K_hUg)$'+'\n'+r'$K_h=-iM_{h^\prime}$',fc='#edf4eb')
arrow((3.94,2.36),(7.66,2.36),'Jacobian trace map',.3)
ax.text(6.3,1.22,r'$\operatorname{rad}B_h=\operatorname{Ann}(h^\prime)=(d)/(d^m)=H^{-1}(L_{E_h/\mathbb{C}})$',ha='center',fontsize=14)
ax.text(6.3,.6,r'Supported endpoints:  $\Delta Z=0\ \Longrightarrow\ \Delta\mathbf{B}_L=\Delta\mathbf{D}_L$',ha='center',fontsize=13)
ax.text(6.3,.15,'Every lower support coordinate remains present; its endpoint change is compensated.',ha='center',fontsize=11,color='#344a5b')
fig.savefig(P/'collision_residue_duality.png',dpi=180,bbox_inches='tight')
fig.savefig(P/'collision_residue_duality.svg',bbox_inches='tight')
plt.close(fig)
