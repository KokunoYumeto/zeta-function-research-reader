"""Reproducible diagram of CBR and PHW maps; coordinates are schematic."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch
B=Path(__file__).resolve().parent
O=B/'figures';O.mkdir(exist_ok=True)
fig=plt.figure(figsize=(15,10),facecolor='white')
ax=fig.add_axes([.025,.04,.95,.9]);ax.set_xlim(0,15);ax.set_ylim(0,10);ax.axis('off')
def box(x,y,w,h,text,color='#eef4f8',size=13):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.10',facecolor=color,edgecolor='#637b8d',linewidth=1.2))
    ax.text(x+w/2,y+h/2,text,ha='center',va='center',fontsize=size,linespacing=1.6)
def arrow(a,b,label='',dy=.12):
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=15,color='#344c64',linewidth=1.5))
    if label:ax.text((a[0]+b[0])/2,(a[1]+b[1])/2+dy,label,ha='center',va='bottom',fontsize=11,color='#243b52')
ax.text(7.5,10,'The arithmetic quotient retains Frobenius; the full collision retains a residue',ha='center',va='bottom',fontsize=19,weight='bold')
box(.2,7.55,4.1,1.55,'Original signed frame cover\n'+r'$|G|=192,\quad G^{\rm ab}\cong C_2$'+'\n'+r'$[G,G]\ \mathrm{transitive\ on\ all\ 8\ states}$',size=13)
box(5.25,7.55,4.2,1.55,'Original infinity-path quotient\n'+r'$w^2=4-27A^2$'+'\n'+r'$A=1:\quad\mathbb{Q}(\sqrt{-23})$',size=14)
box(10.4,7.55,4.3,1.55,'Connes–Consani finite cover\n'+r'$\chi_{23}(u)=\left(\frac{u_{23}}{23}\right)$'+'\n'+r'$\mathrm{Mon}(C_p)=\chi_{23}(p),\quad p\ne23$',size=14)
arrow((4.4,8.3),(5.15,8.3))
arrow((9.55,8.3),(10.3,8.3))
box(.2,5.35,4.1,1.2,r'$p=2:\quad +1$'+'\nTwo circles, each length '+r'$\log 2$',color='#e8f3ee')
box(5.25,5.35,4.2,1.2,r'$p=5:\quad -1$'+'\nOne circle, length '+r'$2\log 5$',color='#f7edef')
box(10.4,5.15,4.3,1.55,'Prime-power trace coefficients\n'+r'$\mathrm{Tr}(T_p^k)$'+'\nTrivial projection retains the full\nsupported-zero Weil endpoints',size=12)
arrow((12.55,7.45),(12.55,6.8))
ax.plot([.2,14.7],[4.65,4.65],color='#c6cfd8',lw=1)
ax.text(7.5,4.42,'The actual heat collision:  '+r'$t=h-\frac{1}{8},\quad w^2=256t^2(9+64t)$',ha='center',fontsize=16,weight='bold')
box(.2,2.4,4.1,1.3,'Double-cover special fibre\n'+r'$\mathbb{C}[w]/(w^2)$'+'\n'+r'$w\ne0,\quad w^2=0$',color='#f5eef9')
box(5.25,2.4,4.2,1.3,'Two normalized special points\n'+r'$\mathbb{C}\oplus\mathbb{C}$'+'\n'+r'$c+dw\longmapsto(c,c)$',color='#eef4f8')
arrow((4.4,3.05),(5.15,3.05))
box(10.4,2.4,4.3,1.3,'Full signed collision\n'+r'$\mathscr{L}_0=\mathbb{C}[T]/(T^4)$'+'\n'+r'$\mathfrak{N}=(T),\quad\mathfrak{N}^4=0$',color='#e8f3ee')
box(.2,.3,9.25,1.35,'The character has trivial monodromy at '+r'$h=\frac{1}{8}$'+'\n'+r'$w=\pm16t\sqrt{9+64t}$'+' are separate analytic graphs.\nThe map of special fibres has kernel '+r'$\mathbb{C} w$'+' and a one-dimensional cokernel.',size=13)
box(10.4,.3,4.3,1.35,'Nonzero original residue\n'+r'$\delta=-\frac{T^3}{16}\frac{d}{dT}$'+'\n'+r'$[n_2]\longmapsto-\frac{3}{8} n_3$',color='#f5eef9',size=14)
arrow((12.55,2.3),(12.55,1.75))
fig.text(.5,.014,'Exact equations and maps: CBR1–CBR29; PHW4–PHW25. Boxes and arrows are schematic, not metric geometry. No positivity of the full Weil form is inferred.',ha='center',fontsize=10,color='#455968')
for ext in ['png','svg']:fig.savefig(O/f'34_class_field_holonomy.{ext}',dpi=180)
plt.close(fig)
print(str(O/'34_class_field_holonomy.png'))
