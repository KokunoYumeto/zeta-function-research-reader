from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

B = Path(__file__).resolve().parent
fig, ax = plt.subplots(figsize=(13,8), dpi=150)
ax.set(xlim=(0,13), ylim=(0,8)); ax.axis('off')
fig.patch.set_facecolor('#fbfaf6')
ax.set_facecolor('#fbfaf6')
def box(x,y,w,h,text,fc='#e5eef1',size=14):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.12',facecolor=fc,edgecolor='#375663',linewidth=1.2))
    ax.text(x+w/2,y+h/2,text,ha='center',va='center',fontsize=size,color='#183440',linespacing=1.5)
def arrow(x,y,xx,yy,label='',dy=.18):
    ax.annotate('',(xx,yy),(x,y),arrowprops={'arrowstyle':'->','lw':1.7,'color':'#375663'})
    ax.text((x+xx)/2,(y+yy)/2+dy,label,ha='center',va='bottom',fontsize=12)
ax.text(.2,7.7,'Supported zero is an identity on the original zero semilattice',fontsize=20,weight='bold',color='#183440')
box(.4,5.9,3.3,1.05,r'$M=\coprod_\lambda M_\lambda$'+'\nAll module fibres retained')
box(5.4,5.9,3.1,1.05,r'$eM=\{0_\lambda\}_\lambda$'+'\n'+r'$e|_{eM}=\mathrm{id}$')
box(10,5.9,2.5,1.05,r'$A=\{\tau,e\}$'+'\n'+r'$1_A=e=e^{-1}$')
arrow(3.85,6.65,5.2,6.65,r'$p_M:m\mapsto em$')
arrow(5.2,6.1,3.85,6.1,r'$i_M$',dy=-.38)
ax.text(.45,5.42,r'$p_M i_M=\mathrm{id}_{eM}$;  $i_M p_M=e\cdot(-)$;  $e\neq\tau$.   Proof: ZH1–ZH8.',fontsize=13)
ax.plot([.8,12.1],[4.45,4.45],color='#375663',lw=2)
for x,t,col,txt in [(1.3,'-1','#a64b3e','Nonreal zeros exist'),(6.2,'0','#8d6b2b','RH is the real-zero question'),(11.6,'0.2','#2c7160','All zeros real')]:
    ax.scatter([x],[4.45],s=100,color=col,zorder=3)
    ax.text(x,4.8,'$t='+t+'$',ha='center',fontsize=15,color=col)
    ax.text(x,3.96,txt,ha='center',fontsize=12,color=col)
ax.text(6.5,3.42,r'Actual heat group: $U_tq=e^{tu^2}q$,  $U_t^{-1}=U_{-t}$,  $U_0=\mathrm{id}$.',ha='center',fontsize=15)
ax.text(6.5,3.02,'The split lift fixes both zero labels at every time.  Proof: ZH9–ZH21.',ha='center',fontsize=12)
box(.5,.8,5.35,1.5,r'$C_0=\mathbb{C}[T]/(T^4)$,  $D(T)=-T^3/16$'+'\n'+r'$V_a(T)=T-aT^3/16$,  $V_a^{-1}=V_{-a}$'+'\nNonzero residue action; zero labels still fixed.',fc='#e8e3f0',size=14)
box(7.1,.8,5.2,1.5,r'$Q\geq0$,  $V_a^*QV_a=Q$,  $a\neq0$'+'\n'+r'$\Longleftrightarrow\quad\mathbb{C} T^3\subseteq\mathrm{rad}(Q)$'+'\nExact pairing consequence: ZH22–ZH24.',fc='#eee9db',size=14)
arrow(6.05,1.55,6.85,1.55)
ax.text(.35,.18,'Heat bounds: Rodgers–Tao (2018/2021), Platt–Trudgian (2020/2021).  No identification of Q with the full Weil pairing is claimed.',fontsize=10.5,color='#375663')
fig.subplots_adjust(left=.02,right=.98,top=.98,bottom=.02)
for ext in ['png','svg']:
    fig.savefig(B / ('supported_zero_heat_identity.'+ext),facecolor=fig.get_facecolor())
print('Saved supported_zero_heat_identity.png and .svg')
