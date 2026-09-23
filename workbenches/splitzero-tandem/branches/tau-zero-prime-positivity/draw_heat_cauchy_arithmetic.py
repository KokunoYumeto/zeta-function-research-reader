"""Reproducible exact formula diagram for HA1--HA23. No sampled zero set."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch

P=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'mathtext.fontset':'dejavusans'})
fig=plt.figure(figsize=(15,11),facecolor='white');ax=fig.add_axes([0,0,1,1]);ax.set(xlim=(0,15),ylim=(0,11));ax.axis('off')
def box(x,y,w,h,lines,color='#edf4fa',size=12):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.09',facecolor=color,edgecolor='#5d7080',linewidth=1.2))
    ax.text(x+w/2,y+h/2,lines,ha='center',va='center',fontsize=size,linespacing=1.65)
def arrow(x1,y1,x2,y2):
    ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle='-|>',mutation_scale=17,linewidth=1.4,color='#3c5265'))
ax.text(.55,10.5,'The actual heat pairing retains every endpoint',fontsize=22,weight='bold')
ax.text(.55,10.05,r'Original coordinates: $g_t(s)=16H_t(-2i(s-1/2))$,  $g_0=2\xi_R$,  $\mathrm{Re}\,z,\mathrm{Re}\,w>1$.',fontsize=14)
box(.55,8.18,4.15,1.45,r'$\partial_tg_t=\frac{1}{4}g_t^{\prime\prime}$'+'\n'+r'$L_t=g_t^\prime/g_t$'+'\n'+r'$\partial_tL_t=\frac{1}{4}(L_t^{\prime\prime}+2L_tL_t^\prime)$',size=15)
box(5.15,8.18,9.25,1.45,r'$K_t(z,w)=\sum_\rho m_\rho\,F_z^\#(\rho)F_w(\rho)=\frac{L_t(w)+\overline{L_t(z)}}{w+\overline{z}-1}$'+'\n'+r'$F_z(s)=1/(s-z),\qquad F^\#(s)=\overline{F(1-\overline{s})}$'+'\n'+'All zeros and multiplicities; real time in the fixed-pole zero-free interval.',size=13)
arrow(4.81,8.9,5.02,8.9)
ax.text(.55,7.66,'At time zero: three separately evaluated terms',fontsize=16,weight='bold')
box(.55,5.94,4.35,1.34,'Supported-zero endpoints\n'+r'$E=\frac{1}{w(\overline{z}-1)}+\frac{1}{\overline{z}(w-1)}$',color='#f9ecd7',size=14)
box(5.25,5.94,4.25,1.34,'Archimedean term\n'+r'$G=\frac{b(w)+\overline{b(z)}}{w+\overline{z}-1}$',color='#e7f3ee',size=14)
box(9.85,5.94,4.55,1.34,'Finite primes\n'+r'$P=\frac{\sum_{n\geq2}\Lambda(n)(n^{-w}+n^{-\overline{z}})}{w+\overline{z}-1}$',color='#f4eafa',size=13)
ax.text(7.5,5.45,r'$K_0=E+G-P,\qquad b(s)=-\frac{1}{2}\log\pi+\frac{1}{2}\psi(s/2)$',ha='center',fontsize=16)
box(.55,3.85,13.85,1.04,r'$\mathbf{B}_L=E\mathbf{e}_{1_L}+A(0)\sum_{\lambda\ne1_L}\mathbf{e}_\lambda,\quad\mathbf{Z}_L=K_0\mathbf{e}_{1_L},\quad\mathbf{D}_L=(P-G)\mathbf{e}_{1_L}+A(0)\sum_{\lambda\ne1_L}\mathbf{e}_\lambda$'+'\n'+r'$\mathbf{B}_L-\mathbf{Z}_L=\mathbf{D}_L$'+'   — each lower support coordinate remains present.',color='#f2f4f5',size=12)
ax.text(.55,3.33,'First heat response: a product of two distinct prime contributions',fontsize=16,weight='bold')
box(.55,1.38,4.1,1.45,r'$p^\alpha,\ q^\beta,\quad p\ne q$'+'\n'+r'$\Lambda(p^\alpha)=\log p$'+'\n'+r'$\Lambda(q^\beta)=\log q$',size=14)
box(5.15,1.38,9.25,1.45,r'$n=p^\alpha q^\beta:\quad(\Lambda*\Lambda)(n)=2\log p\log q$'+'\n'+r'$[n^{-s}]\,\dot{L}_0(s)=-\frac{1}{2}\log p\log q\log(p^\alpha q^\beta)$'+'\n'+r'$\dot{K}_0(z,w)=\frac{\dot{L}_0(w)+\overline{\dot{L}_0(z)}}{w+\overline{z}-1}$',size=14)
arrow(4.81,2.13,5.02,2.13)
ax.text(.55,.73,'The displayed mixed coefficient is exact. Its sign alone does not determine the sign of the full pairing.',fontsize=12)
ax.text(.55,.3,'Proofs: HA1–HA20; original heat source: Rodgers–Tao, arXiv:1801.05914v5, hoz / htdef. Full support: SZW33–34.',fontsize=10,color='#45525d')
fig.savefig(P/'heat_cauchy_supported_arithmetic.png',dpi=180)
fig.savefig(P/'heat_cauchy_supported_arithmetic.svg')
plt.close(fig)
print('Saved exact heat / full-support / mixed-prime diagram.')

import numpy as np
fig=plt.figure(figsize=(13,7),facecolor='white')
ax=fig.add_axes([0,0,1,1]);ax.set(xlim=(0,13),ylim=(0,7));ax.axis('off')
ax.text(.45,6.6,'A positive response of the original heat measure',fontsize=21,weight='bold')
ax.text(.45,6.16,r'Every real $t$, every $\sigma>1$, and $v=\sigma-1/2$: full proof HA24–HA26.',fontsize=13)
box(.45,4.65,12.05,1.06,r'$d\mu_{t,v}(u)=\frac{e^{tu^2}\Phi(u)\cosh(2vu)\,du}{\int_0^\infty e^{ty^2}\Phi(y)\cosh(2vy)\,dy}$'+'\n'+r'$\Phi(u)>0,\qquad L_t(\sigma)=2\,\mathbb{E}_{\mu}[u\tanh(2vu)]$',color='#e7f3ee',size=14)
plot=fig.add_axes([.075,.165,.32,.405])
xs=np.linspace(0,1.7,300)
plot.plot(xs,xs**2,label=r'$u^2$',linewidth=2.4,color='#8a3f83')
plot.plot(xs,xs*np.tanh(3*xs),label=r'$u\tanh(3u)$',linewidth=2.4,color='#167a83')
plot.set(xlabel=r'$u$',ylabel='function value',title=r'Exact functions shown at $v=3/2$')
plot.grid(alpha=.2);plot.legend(frameon=False,fontsize=11)
box(5.75,2.16,6.75,1.92,r'$\partial_t L_t(\sigma)=2\,\mathrm{Cov}_\mu(u^2,u\tanh(2vu))>0$'+'\n\n'+r'$K_t(\sigma,\sigma)>0,\qquad\partial_t K_t(\sigma,\sigma)>0$',color='#edf4fa',size=14)
ax.text(9.12,1.42,'Both functions increase strictly.\nThe double-integral covariance formula proves the sign.',ha='center',fontsize=12,linespacing=1.5)
ax.text(.45,.43,'Positive real diagonal values occur at negative heat times too; full matrix positivity also tests off-diagonal entries.',fontsize=11)
fig.savefig(P/'heat_real_diagonal_covariance.png',dpi=180)
fig.savefig(P/'heat_real_diagonal_covariance.svg')
plt.close(fig)
print('Saved actual heat covariance and real diagonal diagram.')
