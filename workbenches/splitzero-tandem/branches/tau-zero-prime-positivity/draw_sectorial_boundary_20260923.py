from pathlib import Path
import json, math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import mpmath as mp
B=Path(__file__).resolve().parent
P=B/'receivers' if (B/'receivers').is_dir() else B
plt.rcParams.update({'font.size':10,'axes.titlesize':12,'figure.facecolor':'white','mathtext.fontset':'dejavusans'})

fig,(ax,bx)=plt.subplots(1,2,figsize=(12.2,4.8),gridspec_kw={'width_ratios':[1,1.45]})
x=np.linspace(-1.2,2.2,500);edge=np.maximum(abs(x),abs(x-1))
ax.fill_between(x,edge,3.1,color='#cfebdf')
ax.plot(x,edge,color='#217761',lw=2)
ax.axvline(.5,color='#22466b',ls='--',lw=1)
ax.set(xlim=(-1.2,2.2),ylim=(0,3.1),xlabel=r'$\sigma=\Re s$',ylabel=r'$\gamma=\Im s$',title='Exact domain of endpoint dominance')
ax.text(.5,2.6,r'$\mathcal{W}:\ \gamma>\max(|\sigma|,|\sigma-1|)$',ha='center',fontsize=10)
ax.text(.5,1.85,'On each compact subset:\nraw lateral branches have no zeros\nfor sufficiently small positive t',ha='center',fontsize=9)
ax.text(.5,.18,'Boundary equality is excluded',ha='center',fontsize=9)
ax.grid(alpha=.18)
bx.axis('off');bx.set_title('Exact return with both endpoint sectors retained')
lines=[(.91,r'$A(s)=\pi^{-s/2}\Gamma(s/2),\quad K_t=\sqrt{\pi/t}$'),
(.78,r'$E_0=e^{-s^2/t},\qquad E_1=e^{-(s-1)^2/t}$'),
(.62,r'$f_+=A^{-1}(J_t+2iK_tE_1)$'),
(.49,r'$f_-=A^{-1}(J_t-2iK_tE_0)$'),
(.33,r'$u_t=A^{-1}J_t\longrightarrow\zeta\quad (\Im s>0)$'),
(.17,r'$\mathcal{P}_t f_+=\mathcal{P}_t f_-=\mathcal{P}_t u_t=\zeta_t$'),
(.01,'The differential filter kills the endpoint modes;\nthe augmented inverse retains their initial data.')]
for y,txt in lines:bx.text(.5,y,txt,ha='center',va='center',fontsize=11 if y>.02 else 9)
fig.tight_layout(pad=1.6)
for ext in ['png','svg']:fig.savefig(P/('sectorial_endpoint_return.'+ext),dpi=190,bbox_inches='tight')
plt.close(fig)

mp.mp.dps=75
rho=mp.zetazero(1);nonzero=mp.mpc('.5',3)
ds=[mp.mpf(str(x)) for x in np.logspace(-7,-5,22)]
rows=[]
for s,name in [(rho,'first_zero'),(nonzero,'nonzero_point')]:
    A=mp.pi**(-s/2)*mp.gamma(s/2)
    for d in ds:
        N=int(mp.ceil(mp.sqrt(220/(mp.pi*d))))
        Z=mp.fsum(mp.exp(-mp.pi*d*n*n-s*mp.log(n)) for n in range(1,N+1))
        sector=mp.gamma((1-s)/2)*(mp.pi*d)**((s-1)/2)/2
        I=2*mp.sqrt(d)*A*Z;S=2*mp.sqrt(d)*A*sector
        leading=abs(2*A*mp.zeta(s))*mp.sqrt(d) if name=='nonzero_point' else abs(-2*mp.pi*A*mp.zeta(s-2))*d**mp.mpf('1.5')
        rows.append({'point':name,'d':float(d),'N':N,'I':float(abs(I)),'sector':float(abs(S)),'residual':float(abs(I-S)),'leading_residual':float(leading),
                     'leading_sector':float(abs(mp.pi**(-mp.mpf('.5'))*mp.gamma(s/2)*mp.gamma((1-s)/2))*d**(mp.re(s)/2))})
fig,axs=plt.subplots(1,2,figsize=(12.2,4.7))
for ax,name,title in zip(axs,['first_zero','nonzero_point'],[r'Numerical sample: first zero $\rho\approx\frac{1}{2}+14.134725i$',r'Numerical sample: $s=\frac{1}{2}+3i$, $\zeta(s)\ne0$']):
    rr=[r for r in rows if r['point']==name];d=np.array([r['d'] for r in rr])
    ax.loglog(d,[r['I'] for r in rr],color='#22466b',lw=2,label=r'Full moment $|I_d|$')
    ax.loglog(d,[r['sector'] for r in rr],color='#ce8830',lw=2,ls=':',label=r'Retained sector $|\mathcal{S}_d|$')
    ax.loglog(d,[r['residual'] for r in rr],color='#208768',lw=2,label=r'Residual $|I_d-\mathcal{S}_d|$')
    ax.loglog(d,[r['leading_residual'] for r in rr],color='#8d4f96',ls='--',lw=1.2,label='Full leading residual coefficient')
    ax.set(title=title,xlabel=r'$d=1/(4\pi T)>0$',ylabel='Absolute value of the full formula')
    ax.grid(which='both',alpha=.17);ax.legend(fontsize=8,loc='best')
fig.tight_layout(pad=1.5)
for ext in ['png','svg']:fig.savefig(P/('gaussian_boundary_zero_detector.'+ext),dpi=190,bbox_inches='tight')
plt.close(fig)
out={'precision_digits':75,'sampling':'Numerical illustration, not a zero enclosure or proof of positivity. Series truncated at N=ceil(sqrt(220/(pi*d))). Exact limiting rates and coefficients are GAB32–40.',
     'rho_real':str(mp.re(rho)),'rho_imag':str(mp.im(rho)),'nonzero_point':'1/2+3i','rows':rows}
(P/'GAUSSIAN_BOUNDARY_FIGURE_DATA.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({'figures':['sectorial_endpoint_return','gaussian_boundary_zero_detector'],'samples':len(rows)}))
