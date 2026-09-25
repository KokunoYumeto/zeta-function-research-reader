from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
r=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','mathtext.fontset':'dejavusans','font.size':12})
fig=plt.figure(figsize=(16,10),facecolor='#f8fafc')
ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,16); ax.set_ylim(0,10); ax.axis('off')
def arr(x1,y1,x2,y2,t='',color='#334155'):
    ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle='->',mutation_scale=16,color=color,linewidth=1.5))
    ax.text((x1+x2)/2,(y1+y2)/2+.22,t,ha='center',fontsize=13,color=color)
def box(x,y,w,h,t):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.12',facecolor='#e5f1e9',edgecolor='#52637a'))
    ax.text(x+w/2,y+h/2,t,ha='center',va='center',fontsize=15,linespacing=1.6)
ax.text(.55,9.52,'The connecting map of the actual sheaf quotient',fontsize=22,weight='bold',color='#13263d')
ax.text(.55,9.05,'All rows use the original coefficient spaces. The cohomological degrees and arithmetic actions are retained.',fontsize=12,color='#46566b')
xs=[5.1,9.0,13.1]
for x,label in zip(xs,['Degree 0','Degree 1','Degree 2']): ax.text(x,8.5,label,ha='center',fontsize=15,weight='bold')
for y,label,terms in [(7.65,r'$D_J$', [r'$V_+\oplus V_-$',r'$J$',r'$J(-1)$']), (6.35,r'$D_{\mathscr{F}}$',[r'$V_+\oplus V_-$',r'$A$',r'$A(-1)$']), (5.05,r'$D_{Q}$',[r'$0$',r'$Q$',r'$Q(-1)$'])]:
    ax.text(.95,y,label,fontsize=20,ha='left',va='center')
    for x,t in zip(xs,terms): ax.text(x,y,t,ha='center',va='center',fontsize=19)
    arr(6.3,y,8.15,y,r'$r_+-r_-$' if label!=r'$D_{Q}$' else r'$0$')
    arr(9.7,y,12.12,y,r'$0$')
for x,t1,t2 in [(5.1,r'$\mathrm{id}$',r'$0$'),(9.0,r'$\mathrm{incl}$',r'$q$'),(13.1,r'$\mathrm{incl}$',r'$q$')]:
    arr(x,7.22,x,6.78); ax.text(x+.22,7.0,t1,fontsize=11)
    arr(x,5.92,x,5.48); ax.text(x+.22,5.7,t2,fontsize=11)
ax.plot([.55,15.45],[4.5,4.5],color='#adb7c5')
box(.9,2.95,14.2,1.02,r'$[a]\in H^1(D_Q)=Q\quad\longmapsto\quad[a]\in H^1(D_{\mathscr{F}})=A/J$'+'\n'+r'$\delta^1([a])=[d^1a]=0\ \in J(-1)$')
ax.text(8,2.48,'The lift is independent of the representative because changing a by J changes it by an actual boundary.',ha='center',fontsize=12)
ax.text(8,1.91,r'$0\longrightarrow J(-1)\longrightarrow A(-1)\longrightarrow Q(-1)\longrightarrow0$',ha='center',fontsize=18)
ax.text(8,1.4,'The degree-two quotient is the shifted zeta receiver. Its kernel remains the full original source image.',ha='center',fontsize=12)
ax.text(.55,.62,'Proofs: CSP4, CSP10 and CC_ACTUAL_WEIGHT_LIFT_COMPARISON.md. Original restrictions: Σ and RΣ.',fontsize=10,color='#46566b')
ax.text(.55,.32,'Schematic of the proved coefficient complexes; no operation is introduced on '+r'$\tau\langle Z_1;\ \mathrm{no}\ Z_2\rangle$'+'.',fontsize=10,color='#46566b')
for ext in ('png','svg'): fig.savefig(r/('actual_sheaf_lift.'+ext),dpi=160,facecolor=fig.get_facecolor())
plt.close(fig)
