from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from flint import arb,ctx
P=Path(__file__).parent
ctx.prec=768
data=json.loads((P/'ARITHMETIC_BALL_CERTIFICATES.json').read_text())
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'svg.fonttype':'none'})
fig=plt.figure(figsize=(17,10),facecolor='#fafbfd')
grid=fig.add_gridspec(1,2,width_ratios=[1.15,1],left=.075,right=.965,top=.84,bottom=.25,wspace=.23)
ax=fig.add_subplot(grid[0,0]); right=fig.add_subplot(grid[0,1]); right.axis('off')
for row,color in zip(data['rows'],['#122b46','#167fa4','#d18420','#8647a3','#297b4d']):
    x=[m['size']-1 for m in row['leading_minors']]
    y=[float(arb(m['real_lower']).log()/arb(10).log()) for m in row['leading_minors']]
    ax.plot(x,y,'o-',color=color,label=r'$\tau='+str(row['omega_imag'])+'$',lw=2,ms=6)
ax.set(xlabel=r'Degree $d$ (matrix size $d+1$)',ylabel=r'$\log_{10}$ of certified determinant lower bound',xticks=list(range(9)))
ax.set_title('Every plotted determinant is strictly positive',loc='left',fontsize=14,pad=14)
ax.grid(alpha=.18); ax.legend(frameon=False,ncol=2,loc='lower left')
ax.spines[['top','right']].set_visible(False)
right.text(0,1,'The complete form, at the original poles',va='top',fontsize=16,weight='bold',color='#122b46')
right.text(0,.87,r'$\omega=2+i\tau,\quad T_d(\omega)=(c_{j-i})_{0\leq i,j\leq d}$',fontsize=16,va='top')
right.text(0,.74,r'$L=\xi^\prime/\xi,\quad c_0=2\operatorname{Re}L(\omega)$',fontsize=16,va='top')
right.text(0,.61,r'$L\!\left(\frac{\omega+(1-\bar\omega)z}{1+z}\right)$'+'\n'+r'$\qquad=L(\omega)+\sum_{n\geq1}c_nz^n$',fontsize=17,linespacing=1.7,va='top')
right.text(0,.35,'45 leading-minor certificates\n40 positive two-mode margins\n768-bit ball arithmetic',fontsize=16,linespacing=1.6,color='#297b4d',va='top')
right.text(0,.105,'Exact coefficient identities: MP8–15\nFull-function certificates: WP24–27',fontsize=13,linespacing=1.6,va='top')
fig.text(.075,.94,'Complete-Weil matrices: certified finite positivity',fontsize=24,weight='bold',color='#122b46')
fig.text(.075,.885,'The full xi function evaluates every coefficient. No finite zero list replaces the tail.',fontsize=14,color='#415366')
fig.text(.075,.145,'Sylvester’s criterion proves positive definiteness through degree eight at each displayed pole.\n'
         'These determinants are basis-dependent; the plot makes no comparison of metric conditioning.\n'
         'The unrestricted degree criterion remains MP16–18. No RH conclusion follows from these finite tests.',
         fontsize=12,linespacing=1.6,color='#415366',va='top')
fig.text(.075,.025,'Source: ARITHMETIC_BALL_CERTIFICATES.json · Arb (F. Johansson); full-Weil derivation from Lagarias’s genus-one product.',fontsize=10,color='#415366')
for ext in ['svg','png']: fig.savefig(P/('FULL_WEIL_CERTIFICATES.'+ext),dpi=150,facecolor=fig.get_facecolor())
print('Wrote full-Weil scientific figure (SVG and PNG).')
