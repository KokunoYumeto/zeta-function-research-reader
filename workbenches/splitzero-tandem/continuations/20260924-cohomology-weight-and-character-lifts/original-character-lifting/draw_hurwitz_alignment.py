from pathlib import Path
import json,numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
R=Path(__file__).resolve().parent;O=R/'hurwitz_intake'
d=json.loads((O/'HURWITZ_PATHS.json').read_text())
assert d['status']=='complete'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'axes.spines.top':False,'axes.spines.right':False})
fig=plt.figure(figsize=(13.2,8.3),facecolor='white')
gs=fig.add_gridspec(2,2,height_ratios=[1.8,1],left=.075,right=.97,top=.87,bottom=.14,hspace=.6,wspace=.27)
ax=fig.add_subplot(gs[0,:]);colors=['#126db0','#c35035','#16816e','#8056a1','#b17800']
for path,col in zip(d['paths'],colors):
    n=path['initial_index']
    points=list(reversed(path['branches'][0]['points']))+path['branches'][1]['points'][1:]
    xs=[float(p['t']) for p in points];ys=[float(p['z']['real']) for p in points]
    ax.plot(xs,ys,color=col,lw=2,label=f'Initial zero {n}')
    ax.scatter([0],[.5],s=44,color=col,zorder=5)
    ax.scatter([xs[0],xs[-1]],[ys[0],ys[-1]],s=28,color=col,zorder=4)
ax.axhline(.5,color='#66717c',linestyle='--',lw=1)
ax.axvline(0,color='#333333',linestyle=':',lw=1.3)
crossings=json.loads((O/'HURWITZ_CRITICAL_CROSSINGS_CERTIFICATE.json').read_text())
for case in crossings['cases']:
    tc=float(case['center_gamma_t_exact_decimals'][1])
    ax.scatter([tc],[.5],marker='*',s=110,color='#171717',edgecolors='white',linewidths=.6,zorder=7)
ax.text(.53,.08,'Black stars: certified interior crossings\n(path assignments remain numerical)',transform=ax.transAxes,fontsize=9,
        bbox=dict(facecolor='white',edgecolor='#d9dfe5',alpha=.96,pad=5))
ax.set(xlim=(-.52,1.02),xlabel=r'Shift $t$ in $F_t(s)=\zeta(s,1+t)$',ylabel=r'$\operatorname{Re}\rho_j(t)$')
ax.set_title('Five tracked branches meet the critical line at the same parameter',loc='left',fontweight='bold',pad=10)
ax.legend(loc='upper left',ncol=3,frameon=True,fontsize=9)
ax.text(.015,.04,r'$t=-\frac{1}{2}$: branches 1 and 3 reach $\operatorname{Re}s=0$;'+'\nbranches 2, 4 and 5 reach earlier Riemann zeros.',transform=ax.transAxes,fontsize=9,bbox=dict(facecolor='white',edgecolor='#d9dfe5',alpha=.96,pad=5))
ax.text(.5,.515,r'$t=0$',transform=ax.get_yaxis_transform(),fontsize=9) if False else None
bx=fig.add_subplot(gs[1,0]);rows=d['local_checks'];idx=np.arange(1,61);v=np.array([float(r['velocity']['real']) for r in rows])
bx.axhline(0,color='#444444',lw=1)
bx.vlines(idx,0,v,colors=np.where(v>0,'#126db0','#c35035'),lw=1)
bx.scatter(idx,v,c=np.where(v>0,'#126db0','#c35035'),s=13)
bx.set(xlabel='Initial zero index',ylabel=r'$\operatorname{Re}\rho_j^{\prime}(0)$',xlim=(0,61))
bx.set_title('First 60: 29 right, 31 left',loc='left',fontweight='bold',fontsize=11)
cx=fig.add_subplot(gs[1,1]);cx.axis('off')
cx.text(0,1,'What was checked',fontweight='bold',va='top')
cx.text(0,.79,'• 45-digit numerical continuation, with residual checks\n• Endpoints refined independently at 80 digits\n• All 60 signs agree with the saved interval calculation\n• Actual zeros also computed at '+r'$t=\pm10^{-4}$',va='top',linespacing=1.55,fontsize=10)
cx.text(0,.15,'The curves are numerical branch tracking.\nThey are not an all-zero theorem or a global interval certificate.',va='top',fontsize=9,color='#444444',linespacing=1.3)
fig.suptitle('The alignment in the shifted Hurwitz family',fontsize=19,fontweight='bold',x=.075,ha='left',y=.98)
fig.text(.075,.925,r'$\rho_j^{\prime}(0)=\rho_j\,\zeta(\rho_j+1)/\zeta^{\prime}(\rho_j)$'+'   •   original coordinates retained',fontsize=12)
fig.text(.075,.035,'Sources: programme shifted-Hurwitz note, thm:zero-motion; saved velocity certificate;\ncompute_hurwitz_paths.py / HURWITZ_PATHS.json; certified stars: HXC2–3 and retained interval checker.',fontsize=9,color='#444444',linespacing=1.4)
for ext in ['png','pdf','svg']:fig.savefig(O/f'HURWITZ_ALIGNMENT.{ext}',dpi=175)
plt.close(fig)
fig,ax=plt.subplots(figsize=(12,7));fig.subplots_adjust(left=.025,right=.975,bottom=.04,top=.88);ax.set(xlim=(0,12),ylim=(0,7));ax.axis('off')
fig.suptitle('Prime factors act on the whole shift family',fontsize=19,fontweight='bold')
nodes={'t':(2.2,5.3),'t/p':(5.7,6.3),'t/q':(5.7,4.3),'t/(pq)':(9.2,5.3)}
for label,(x,y) in nodes.items():
    ax.text(x,y,'$'+label+'$',ha='center',va='center',fontsize=17,bbox=dict(boxstyle='round,pad=.45',facecolor='#e9f2fa',edgecolor='#126db0'))
for a,b,label,dy in [('t','t/p',r'$V_p$',.15),('t','t/q',r'$V_q$',-.15),('t/p','t/(pq)',r'$V_q$',.15),('t/q','t/(pq)',r'$V_p$',-.15)]:
    x,y=nodes[a];u,v=nodes[b];ax.annotate('',xy=(u-.45,v),xytext=(x+.45,y),arrowprops=dict(arrowstyle='->',lw=1.8,color='#126db0'))
    ax.text((x+u)/2,(y+v)/2+dy,label,ha='center',va='center',bbox=dict(facecolor='white',edgecolor='none',pad=2))
ax.text(6,3.3,r'$V_pV_q=V_{pq}=V_qV_p,\qquad (V_pf)(t)=f(t/p)$',ha='center',fontsize=15)
ax.text(6,2.45,r'$\zeta(s,1+t)=\left[\prod_p(I-p^{-s}V_p)^{-1}\right](1+t)^{-s},\quad \operatorname{Re}s>1$',ha='center',fontsize=16,bbox=dict(boxstyle='round,pad=.65',facecolor='#f1f6f4',edgecolor='#16816e'))
ax.text(.65,1.36,r'At $t=0$: every prime fixes the parameter; scalar Euler factors are recovered.',fontsize=12)
ax.text(.65,.82,r'Full support: $\Phi_R(r,\lambda)=(r,1_K\otimes\lambda)$ retains every $\lambda\in L$.',fontsize=12)
ax.text(.65,.25,'Exact parameter diagram; it does not identify the parameter fixed point with a theorem about all zeros.\nProof: HURWITZ_PRIME_SCALING.tex. Human sources: Bost–Connes; Connes–Consani–Marcolli, Fun with F₁.',fontsize=9,color='#444444')
for ext in ['png','pdf','svg']:fig.savefig(O/f'HURWITZ_PRIME_FAMILY.{ext}',dpi=175)
plt.close(fig)
print('Both figures rendered from saved calculations and exact formulas.')
