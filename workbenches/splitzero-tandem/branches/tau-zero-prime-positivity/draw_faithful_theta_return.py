from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

P=Path(__file__).resolve().parent
fig=plt.figure(figsize=(12,12.6),facecolor='white')
ax=fig.add_axes([.035,.035,.93,.93]);ax.set_xlim(0,12);ax.set_ylim(0,13);ax.axis('off')
navy='#17334a';teal='#087e80';orange='#b45323';light='#eff7f8'
def box(x,y,w,h,color=light):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.12',facecolor=color,edgecolor=navy,lw=1.2))
def txt(x,y,t,size=13,**kw):
    for cmd in ['mathcal','mathbb']:
        import re
        t=re.sub(r'\\'+cmd+r' ([A-Za-z])',lambda m:'\\'+cmd+'{'+m[1]+'}',t)
    t=t.replace(r'\frac12',r'\frac{1}{2}').replace(r'\ne ',r'\neq ')
    ax.text(x,y,t,fontsize=size,color=navy,**kw)
def arrow(x,y,X,Y,color=teal):ax.add_patch(FancyArrowPatch((x,y),(X,Y),arrowstyle='-|>',mutation_scale=17,lw=1.8,color=color))
txt(6,12.75,'Original zeta: exact recovery and the heat return defect',18,ha='center',weight='bold')
txt(.15,12.08,'1. The original labelled theta input is recoverable',15,weight='bold')
box(.25,10.55,3.45,1.05);box(8.05,10.55,3.65,1.05)
txt(1.98,11.18,r'$F=(\phi,(c_\lambda)_{\lambda\ne 1_L})$',16,ha='center')
txt(1.98,10.78,r'$\phi\in\mathcal S_{\rm ev}(\mathbb R)$',14,ha='center')
txt(9.88,11.18,r'$(\Phi_\phi,(c_\lambda)_{\lambda\ne 1_L})$',15,ha='center')
txt(9.88,10.78,'Every lower coefficient retained',11,ha='center')
arrow(3.9,11.32,7.84,11.32);arrow(7.84,10.79,3.9,10.79)
txt(5.9,11.52,r'$\Phi_\phi=(D_u^2-1)w_\phi/16$',13,ha='center')
txt(5.9,10.32,'Green inverse + Möbius inversion',12,ha='center')
txt(6,9.85,r'$w_\phi(u)=8\int_{\mathbb R}e^{|u-v|}\Phi_\phi(v)\,dv$',16,ha='center')
txt(6,9.35,r'$a=8\int e^{-u}\Phi_\phi(u)\,du,\qquad b=8\int e^u\Phi_\phi(u)\,du$',15,ha='center')
txt(6,8.98,'Exact on the original even-Schwartz theta image.  TF9–15',11,ha='center')
ax.axhline(8.6,xmin=.02,xmax=.98,color='#bccbd4',lw=1)
txt(.15,8.13,'2. Multiplication keeps the embedded local modules and every jet',15,weight='bold')
txt(6,7.64,r'$C(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2),\qquad \zeta\longmapsto C\zeta$',16,ha='center')
rows=[(6.85,r'$s=-2m$',r'$h\mathcal O/h^2\mathcal O$',r'$[hy]\longmapsto\kappa_m y(0)$'),
      (6.02,r'$s=1$',r'$h^{-1}\mathcal O/\mathcal O$',r'$[h^{-1}y]\longmapsto y(0)/2$'),
      (5.19,r'$s=0$',r'$\mathcal O/h\mathcal O$',r'$[y]\longmapsto-y(0)$')]
for y,l,src,mapping in rows:
    box(.4,y-.26,11.15,.59,color='#f5f7fa')
    txt(.64,y,l,15);txt(3.3,y,src,16);txt(7.02,y,mapping,15)
txt(6,4.6,r'$\kappa_m=(-1)^m\,2m(2m+1)\pi^m/m!\quad(m\geq1)$',14,ha='center')
txt(6,4.23,r'$\tau_L=z_{0_L}\ne e_L=z_{1_L}$; lower zero labels remain separate.  UZ18–24, 44–46',11,ha='center')
ax.axhline(3.86,xmin=.02,xmax=.98,color='#bccbd4',lw=1)
txt(.15,3.4,'3. The actual heat curve leaves that theta image',15,weight='bold')
txt(6,2.91,r'$\Omega_t=[\zeta_t]\in\mathcal O(U)/(\zeta),\qquad U=\{0<\Re s<1\}$',16,ha='center')
txt(6,2.4,r'$\mathcal M_t(s)=\frac{\pi^{-s/2}\Gamma(s/2)}{2}\,\frac{\zeta_t(s)}{\zeta(s)}$',18,ha='center')
txt(6,1.89,'The full local jets map isomorphically to these principal parts.',12,ha='center')
box(.7,.65,10.6,.85,color='#fff4eb')
txt(6,1.17,r'$\Omega_0=0,\qquad\Omega_t\neq0$',17,ha='center')
txt(6,.84,'for every sufficiently small nonzero time; no RH assumption.  TF21–31',12,ha='center')
txt(6,.12,'Maps and domains are exact. The heat statement concerns the specified Gaussian source family.',11,ha='center')
fig.savefig(P/'faithful_theta_return.png',dpi=160,bbox_inches='tight')
fig.savefig(P/'faithful_theta_return.svg',bbox_inches='tight')
print('Saved faithful_theta_return.png and .svg')
