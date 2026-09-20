"""Reproducible exact-formula figures for the heat transport and volume bound."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
OUT = HERE/'figures'
OUT.mkdir(exist_ok=True)
plt.rcParams.update({'font.size': 12, 'font.family': 'DejaVu Sans', 'svg.fonttype': 'none'})

v = np.linspace(0.00001, 5, 700)
kappa = np.exp(v)
d = -np.expm1(-v)*np.exp(-v/np.expm1(v))
fig, ax = plt.subplots(figsize=(10.5, 6.0), layout='constrained')
ax.plot(v, v/np.e, color='#887b75', linestyle='--', label=r'Log-volume bound $v/e$')
ax.plot(v, d, color='#155b8b', lw=2.6, label=r'Sharp bound $d(e^v)=(1-e^{-v})e^{-v/(e^v-1)}$')
ax.fill_between(v, 0, d, color='#dcecf6')
ax.set(xlim=(0,5), ylim=(0,1.9), xlabel=r'Actual adjacent contraction $v=\log(V_N/V_{N+1})$',
       ylabel=r'Bound on $|\Psi_s(N+1)-\Psi_s(N)|$, for every $s>0$',
       title='One original degree step: no dimension multiplier')
ax.grid(alpha=.2)
ax.legend(loc='upper left', frameon=False)
fig.text(.5,-.035,'Exact formula curves, not arithmetic zero data. Complete proof: VH26–31; sharpness: VH30.',
         ha='center',fontsize=11)
for ext in ('png','svg'):
    fig.savefig(OUT/f'degree_volume_heat.{ext}',dpi=180,bbox_inches='tight')
plt.close(fig)

fig, ax = plt.subplots(figsize=(13,7.6), layout='constrained')
ax.set(xlim=(0,1),ylim=(0,1)); ax.axis('off')
def box(x,y,text,colour='#eaf2f7',size=13):
    ax.text(x,y,text,ha='center',va='center',fontsize=size,
            bbox=dict(boxstyle='round,pad=.65',fc=colour,ec='#355872',lw=1.2))
def arrow(a,b,label,offset=(0,0)):
    ax.annotate('',xy=b,xytext=a,arrowprops=dict(arrowstyle='->',lw=1.7,color='#355872'))
    ax.text((a[0]+b[0])/2+offset[0],(a[1]+b[1])/2+offset[1],label,
            ha='center',va='center',fontsize=12,color='#16394e')
box(.23,.82,'Original theta source\n'+r'$f_0=\Theta\psi,\quad \mathcal{M} f_0=2\xi$')
box(.76,.82,'Transported theta source\n'+r'$U_t f_0,\quad U_t=e^{t(\log x)^2/4}$')
arrow((.42,.82),(.55,.82),r'$U_t$',(0,.075))
box(.23,.52,'Original relation and quotient\n'+r'$V\ \overset{\Theta}{\longrightarrow}\ \mathcal{B}\ \longrightarrow\ Q$')
box(.76,.52,'Exact transported relation and quotient\n'+r'$V_t\ \overset{\Theta_t}{\longrightarrow}\ \mathcal{B}_t\ \longrightarrow\ Q_t$')
arrow((.43,.52),(.54,.52),'Invertible chain map',(0,.075))
arrow((.23,.72),(.23,.64),'Source',(-.07,0))
arrow((.76,.72),(.76,.64),'Source',(.07,0))
box(.25,.20,'Moving observation\n'+r'$\mathcal{H}_t=L^2(e^{-t(\log x)^2/2}dx)$'+'\n'+
    r'$\langle U_tF,U_tG\rangle_{\mathcal{H}_t}=\langle F,G\rangle_{\mathcal{H}_0}$', '#eaf5ef',12)
box(.75,.20,'Fixed observation\n'+r'$\mathcal{H}_0=L^2(dx)$'+'\n'+
    r'$K_t=\left[\int e^{t\Lambda_k/2}\overline{f_n}f_m\,d\mathbf{x}\right]$'+'\n'+
    r'$G_t=(E K_t^{-1}E^*)^{-1}$', '#fff3df',12)
arrow((.62,.43),(.32,.34),'Moving norm on transported lifts',(-.09,.02))
arrow((.8,.43),(.78,.35),'Finite admitted lifts',(.11,.015))
ax.set_title('One heat transport, two specified observations',fontsize=18,pad=18)
fig.text(.5,-.015,r'Real $t$ in the metric boxes; $\Lambda_k=\sum_{j=1}^k(\log x_j)^2$. '
         'The fixed-observation Gram retains every cross term.',ha='center',fontsize=11)
for ext in ('png','svg'):
    fig.savefig(OUT/f'theta_transport.{ext}',dpi=170,bbox_inches='tight')
plt.close(fig)
print('Two exact mathematical figures generated; visual inspection remains separate.')
