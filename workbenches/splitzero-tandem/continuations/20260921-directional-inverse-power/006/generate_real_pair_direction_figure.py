"""Draw the original real tangent geometry and proved pole transition."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from flint import arb

B = Path(__file__).resolve().parent
C = json.loads((B/'independent/REAL_PAIR_DIRECTION_CONSTANTS.json').read_text(encoding='utf-8'))
assert C['status'] == 'CERTIFIED'
def midpoint(s): return float(arb(s).mid())
def complex_midpoint(s):
    r,i=s[:-1].rsplit(' + ',1)
    return complex(midpoint(r),midpoint(i))
Az,Ax,Bxi=(complex_midpoint(C[k]) for k in ['G_z','G_x','G_xi'])
J=np.array([[Az.real,Ax.real],[Az.imag,Ax.imag]])
angles=np.linspace(0,2*np.pi,800)
circle=np.vstack([abs(Bxi)*np.cos(angles),abs(Bxi)*np.sin(angles)])
ellipse=np.linalg.solve(J,circle)
vectors=[np.array([midpoint(v['v_z']),midpoint(v['v_x'])]) for v in C['degree3_resonance_line_vectors']]
colors=['#bc4f00','#7030a0','#007d78']
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'axes.titlesize':14,'axes.labelsize':11})
fig,axes=plt.subplots(1,3,figsize=(19,8.6))
fig.subplots_adjust(left=.05,right=.98,top=.81,bottom=.34,wspace=.32)
fig.suptitle('The same real singular point: exact resonance directions and the pole transition',fontsize=19,y=.985)
fig.text(.5,.925,r'$\Lambda(v)=G_zv_z+G_xv_x,\qquad \det\Lambda\in[-88.12638\pm6.25\times10^{-6}]\ne0$',ha='center',fontsize=13)
ax=axes[0]
ax.plot(ellipse[0],ellipse[1],color='#9aa2a7',lw=1.8,label=r'$|\Lambda(v)|^2=|G_\xi|^2$')
for k,(v,color) in enumerate(zip(vectors,colors),1):
    ax.plot([-v[0],v[0]],[-v[1],v[1]],color=color,lw=2.4,label=f'k={k}')
    ax.scatter([v[0]],[v[1]],color=color,s=28,zorder=5)
ax.axhline(0,color='#dddddd',lw=.8);ax.axvline(0,color='#dddddd',lw=.8)
ax.set(xlabel=r'Original direction component $v_z$',ylabel=r'Original direction component $v_x$',title='Original parameter plane',xlim=(-.064,.064),ylim=(-22,22))
ax.legend(loc='upper left',fontsize=9,framealpha=.95)
ax.grid(alpha=.12)
ax.text(.5,-.20,'Axes have different scales. The ellipse is the\nquadratic coefficient of the original zeroth moment.',ha='center',va='top',transform=ax.transAxes,fontsize=10)

ax=axes[1]
ax.plot(circle[0],circle[1],color='#9aa2a7',lw=1.8)
for k,(v,color) in enumerate(zip(vectors,colors),1):
    w=J@v
    ax.plot([-w[0],w[0]],[-w[1],w[1]],color=color,lw=2.4)
    ax.scatter([w[0]],[w[1]],color=color,s=30)
    ax.annotate(f'k={k}',w,xytext=(7,7),textcoords='offset points',color=color,fontsize=10)
ax.annotate('',xy=(Bxi.real,Bxi.imag),xytext=(0,0),arrowprops={'arrowstyle':'->','color':'#454545','lw':1.6})
ax.annotate(r'$G_\xi$',(Bxi.real,Bxi.imag),xytext=(8,-1),textcoords='offset points',color='#454545')
ax.axhline(0,color='#dddddd',lw=.8);ax.axvline(0,color='#dddddd',lw=.8)
ax.set_aspect('equal');ax.set(xlabel=r'$\operatorname{Re}\Lambda(v)$',ylabel=r'$\operatorname{Im}\Lambda(v)$',title='Exact image under the derivative',xlim=(-7.3,7.3),ylim=(-7.3,7.3))
ax.grid(alpha=.12)
ax.text(.5,-.20,r'$v_k=\Lambda^{-1}(G_\xi e^{ik\pi/4}),\quad k=1,2,3$'+'\nThe opposite ray is the same unoriented line.',ha='center',va='top',transform=ax.transAxes,fontsize=10)

ax=axes[2];q=np.linspace(.001,1,250)
ax.plot(q,5-q,color='#b72946',lw=2.5,label='Largest inverse singular value')
ax.plot(q,3+q,color='#216fa0',lw=2.5,label='Second inverse singular value')
ax.plot([1,1.6],[4,4],color='#7030a0',lw=3,label='Both poles, q ≥ 1')
ax.scatter([1],[4],color='#7030a0',s=35,zorder=5)
ax.set(xlabel=r'Approach exponent $q>0$',ylabel='Pole exponent in the actual path parameter',title='Turning toward any resonance line',xlim=(0,1.6),ylim=(2.85,5.2),yticks=[3,4,5])
ax.grid(alpha=.2);ax.legend(loc='upper right',fontsize=8.5)
ax.text(.5,-.20,r'$p(\tau)=p_*+\tau v+q_0\tau^{1+q}w$'+'\n'+r'$v$ resonant; $w$ transverse; $q_0\ne0$; $\tau>0$.',ha='center',va='top',transform=ax.transAxes,fontsize=10)
fig.text(.05,.095,'Degree D=3: other straight directions have poles (5,3); each displayed resonance line has (4,4).\nEvery inverse exterior rank 2, 3 and 4 has pole 8 throughout the transition, with the full original Gamma constants.',fontsize=12)
fig.text(.05,.034,'Proof: RPD3–5, RPD20–28 and RPD31. Tangent geometry uses certified interval midpoints; it is not a plot of a finite zero curve.\nOriginal period and metric: PCL1–16, WCF1–6 (pinned sources in the proof). Inclusion arithmetic: Fredrik Johansson, Arb, arXiv:1611.02831v1.',fontsize=9,color='#444444')
O=B/'figures_real_pair_direction';O.mkdir(exist_ok=True)
for suffix in ['png','svg']:fig.savefig(O/f'37_real_pair_directional_geometry.{suffix}',dpi=180,facecolor='white')
plt.close(fig)
print(str(O/'37_real_pair_directional_geometry.png'))
