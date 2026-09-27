# Figure for the Navier-Stokes paper: the two shear roots of I'_alpha(q) = 0 near the pole collision.
# Real roots alpha_h (hydrodynamic) and the partner for q^2 < q*^2, and the complex pair beyond.
import mpmath as mp, numpy as np
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
mp.mp.dps = 30
def F(a,q): return (mp.besseli(a-1,q)+mp.besseli(a+1,q))/2
qs = 0.7784728009903300761803564
xs=[]; ah=[]; ap=[]
alpha_star = mp.mpf('-0.569714080972361784438457668663')
grid = list(np.linspace(0.05, 0.70, 140)) + list(float(qs) - np.geomspace(0.078, 1e-6, 160))
for q in grid:
    q=mp.mpf(q)
    f=lambda a: F(a,q)
    assert f(alpha_star) < 0
    r1 = mp.findroot(f, (alpha_star, mp.mpf('-1e-12')), solver='illinois')
    r2 = mp.findroot(f, (mp.mpf('-0.9999'), alpha_star), solver='illinois')
    xs.append(float(q**2)); ah.append(float(r1)); ap.append(float(r2))
# complex pair beyond the collision
xc=[]; re=[]; im=[]
z = mp.mpc(-0.5697, 0.01)
for q in np.linspace(float(qs)+1e-4, 1.0, 120):
    q=mp.mpf(q)
    z = mp.findroot(lambda a: F(a,q), z)
    if abs(mp.im(z))<1e-12: z = mp.mpc(mp.re(z), 0.02)
    xc.append(float(q**2)); re.append(float(mp.re(z))); im.append(abs(float(mp.im(z))))
fig,ax=plt.subplots(1,1,figsize=(6.4,4.2))
ax.plot(xs,ah,color='C0',lw=1.8,label=r'hydrodynamic root $\alpha_h$')
ax.plot(xs,ap,color='C1',lw=1.8,label='first non-hydrodynamic root')
ax.plot(xc,re,color='C2',lw=1.8,label=r'$\mathrm{Re}\,\alpha$ of the complex pair')
ax.plot(xc,[r+i for r,i in zip(re,im)],color='C2',lw=1,ls='--',label=r'$\mathrm{Re}\,\alpha\pm\mathrm{Im}\,\alpha$')
ax.plot(xc,[r-i for r,i in zip(re,im)],color='C2',lw=1,ls='--')
ax.axvline(float(qs**2),color='0.5',lw=0.8,ls=':')
ax.plot([float(qs**2)],[-0.5697140809723618],'ko',ms=4)
ax.annotate(r'collision $(q_*^2,\alpha_*)$',xy=(float(qs**2),-0.5697),xytext=(0.66,-0.30),arrowprops=dict(arrowstyle='->',lw=0.7),fontsize=9)
ax.set_xlabel(r'$q^2=(k\rho_c)^2$'); ax.set_ylabel(r'$\alpha=-i\omega\rho_c/c$')
ax.set_xlim(0,1.0); ax.set_ylim(-1.05,0.05)
ax.legend(fontsize=8,loc='upper center',bbox_to_anchor=(0.5,-0.18),ncol=2,frameon=False)
fig.tight_layout(); fig.savefig('fig/fig_ns_collision.pdf'); fig.savefig('fig/fig_ns_collision.png',dpi=130)
print('hydro at q*-:',ah[-1],' partner at q*-:',ap[-1],' pair re at 1.0:',re[-1],'im',im[-1])
print('check alpha_h(0.05^2)~ -q^2/2:',ah[0], -0.05**2/2)
