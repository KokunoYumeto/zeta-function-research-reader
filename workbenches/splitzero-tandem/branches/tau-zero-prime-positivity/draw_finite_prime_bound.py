"""Plot the defined coefficient sum; the bounds are proved by exact rational checks."""
from pathlib import Path
import json,math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
P=Path(__file__).resolve().parent
cert=json.loads((P/'FINITE_PRIME_WINDOW_COEFFICIENT_CERTIFICATE.json').read_text())
lo=583/800;hi=math.log(256);d=1/32
items=[(row['n'],math.log(row['prime_base'])/math.sqrt(row['n'])) for row in cert['weights']]
events=sorted(set([lo,hi]+[math.log(n)+s*d for n,w in items for s in [-1,1] if lo<math.log(n)+s*d<hi]))
xs=[];ys=[]
for a,b in zip(events[:-1],events[1:]):
    mid=(a+b)/2
    y=sum(w for n,w in items if abs(math.log(n)-mid)<d)
    xs.extend([a,b]);ys.extend([y,y])
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':13})
fig=plt.figure(figsize=(13,8),layout='constrained');gs=fig.add_gridspec(2,1,height_ratios=[1.3,.85])
ax=fig.add_subplot(gs[0]);ax.plot(xs,ys,lw=1.5,color='#216782',label=r'$S(a)=\sum_{|\log n-a|\leq1/32}\Lambda(n)/\sqrt{n}$')
ax.axhline(223/125,ls='--',color='#bc6d30',label=r'Certified $S(a)<223/125$')
ax.axhline(81/25,color='#2e8662',lw=2,label=r'Proved $q/N>81/25$')
ast=(math.log(227)+math.log(241))/2
ax.plot(ast,sum(math.log(n)/math.sqrt(n) for n in [227,229,233,239,241]),'o',color='#ad3543')
ax.annotate('Exact maximizing packet:\n227, 229, 233, 239, 241',xy=(ast,1.783796246),xytext=(3.95,2.48),arrowprops={'arrowstyle':'->','color':'#ad3543'},fontsize=11)
ax.set(xlim=(lo,hi),ylim=(-.06,3.57),xlabel='Original translation a',ylabel='Coefficient sum and proved bounds',title='Every prime power in each original window is retained')
ax.set_xticks([lo,math.log(4),math.log(16),math.log(64),hi],[r'$583/800$',r'$\log4$',r'$\log16$',r'$\log64$',r'$\log256$'])
ax.legend(loc='upper left',fontsize=10);ax.grid(alpha=.17)
ax=fig.add_subplot(gs[1]);ax.axis('off')
ax.text(.5,.89,r'$K(a)=-R(a)-\sum_{|\log n-a|\leq1/32}\frac{\Lambda(n)}{\sqrt{n}}\,h_r(a-\log n)$',ha='center',fontsize=20)
ax.text(.5,.61,r'$0<R(a)<2^{-24}N,\qquad |h_r(u)|\leq N,\qquad N=\|f_r\|_2^2>24159387650$',ha='center',fontsize=17)
ax.text(.5,.34,r'$|K(a)|<\left(\frac{223}{125}+2^{-24}\right)N<q-\left(\frac{182}{125}-2^{-24}\right)N$',ha='center',fontsize=22)
ax.text(.5,.07,'Proofs: FP1–25 and FPC1–14.  The curve displays the defining finite coefficient sum; the proof uses rational enclosures.',ha='center',fontsize=11)
fig.suptitle('A strict full-Weil margin through log 256 for the unchanged fixed test',fontsize=21)
for ext in ['png','svg']:fig.savefig(P/f'finite_prime_bound.{ext}',dpi=160)
print('Rendered finite_prime_bound.png and .svg')
