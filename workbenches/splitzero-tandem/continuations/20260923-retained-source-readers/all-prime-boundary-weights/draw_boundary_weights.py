from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle

out=Path(__file__).parent
fig,ax=plt.subplots(figsize=(12,8.8))
fig.patch.set_facecolor('#fafaf6')
ax.set_facecolor('#fafaf6')
ax.set_xlim(0,12);ax.set_ylim(0,9);ax.axis('off')
ax.text(.35,8.65,'Mixed tensor weights before the endpoint quotient',fontsize=19,weight='bold')
ax.text(.35,8.25,'The actual all-prime boundary: every place retains its evaluation / integral choice.',fontsize=11)
def box(x,y,w,h,text,color='#e9eef2'):
 ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.12',facecolor=color,edgecolor='#34495e',linewidth=1.3))
 ax.text(x+w/2,y+h/2,text,ha='center',va='center',fontsize=12)
box(.4,6.75,3.1,1.05,'Full tensor boundary\n'+r'$B^{\otimes r}=\mathrm{LC}(\Omega^r)$')
box(4.15,6.75,3.25,1.05,'Rational coinvariants\n'+r'$\mathrm{LC}(Z_r)$')
box(8.2,6.75,3.35,1.05,'Endpoint tensor quotient\n'+r'$\mathbb{C}^{\,2^r}$')
ax.annotate('',xy=(4.03,7.28),xytext=(3.65,7.28),arrowprops={'arrowstyle':'->','lw':1.5})
ax.annotate('',xy=(8.05,7.28),xytext=(7.53,7.28),arrowprops={'arrowstyle':'->','lw':1.5})
ax.text(.4,6.18,r'$Z_r:\quad m_p=m_\infty$ at every prime, where $m_v=\sum_{j=1}^r\varepsilon_{v,j}$.',fontsize=13)
ax.text(.4,5.74,r'On its $m$ component, the original idele action is exactly $|a|^m$.',fontsize=13)
ax.text(.4,5.2,'Tensor order two, with one named prime p',fontsize=15,weight='bold')
ax.text(.4,4.82,'The four balanced choices with one integral in each column:',fontsize=11)
x0,y0,w,h=1.55,2.1,3.65,1.0
for i in range(2):
 for j in range(2):
  y=y0+(1-i)*h
  ax.add_patch(Rectangle((x0+j*w,y),w,h,facecolor='#dce9e3' if i==j else '#f6d9a8',edgecolor='#34495e'))
  line='Endpoint value retained' if i==j else 'Mixed class survives in LC(Z₂)'
  second='also has mixed continuations' if i==j else 'value is erased by ℂ⁴ receiver'
  ax.text(x0+(j+.5)*w,y+.61,line,ha='center',fontsize=11,weight='bold')
  ax.text(x0+(j+.5)*w,y+.26,second,ha='center',fontsize=10)
for j in range(2): ax.text(x0+(j+.5)*w,4.33,'p-column = {'+str(j+1)+'}',ha='center',fontsize=12)
for i in range(2): ax.text(1.35,y0+(1-i+.5)*h,'∞-column\n= {'+str(i+1)+'}',ha='right',va='center',fontsize=12)
ax.text(9.25,3.43,'Each cell has\nmodulus character\n'+r'$|a|$'+'\n(weight 2).',ha='left',va='center',fontsize=12)
ax.text(.4,1.62,r'Example: $e_{\{\infty\}}\otimes e_{\{p\}}$ has prime eigenvalues $p\cdot p^{-1}=1$.',fontsize=12)
ax.text(.4,1.22,'At every other prime either one-element column is allowed; all those mixed choices remain.',fontsize=11)
ax.text(.4,.72,r'$H_j(\mathbb{Q}^{\times},B^{\otimes r})=\mathrm{LC}(Z_r)\otimes\Lambda^j\mathbb{C}^{(\mathrm{primes})}$.',fontsize=14)
ax.text(.4,.28,'BW6–14 prove these maps and weights. BW20–22 give the connecting map into the original test-space kernel.',fontsize=9.5)
fig.savefig(out/'BOUNDARY_WEIGHT_MAP.png',dpi=180,bbox_inches='tight')
fig.savefig(out/'BOUNDARY_WEIGHT_MAP.svg',bbox_inches='tight')
plt.close(fig)
