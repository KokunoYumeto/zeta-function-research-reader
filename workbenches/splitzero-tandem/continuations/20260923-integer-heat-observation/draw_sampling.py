"""Reproducible sampled illustration of the proved heat-observation maps."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
H=Path(__file__).resolve().parent
T=1/8
def k(x,t=T):return np.exp(-np.asarray(x)**2/(4*t))/np.sqrt(4*np.pi*t)
xi=np.linspace(0,1,1201);l=np.arange(-24,25)
integer=np.sum(k(l)[:,None]*np.exp(-2j*np.pi*l[:,None]*xi),axis=0)
half=np.sum(k(l+.5)[:,None]*np.exp(-2j*np.pi*l[:,None]*xi),axis=0)
sizes=np.array([2,4,8,16,32,64,128]);ri=[];rh=[];qn=[]
for N in sizes:
    n=np.arange(1,N+1);a=(-1.)**n
    gram=k(n[:,None]-n[None,:],2*T);line=a@gram@a
    sample_m=np.arange(-24,N+25)
    ri.append(np.sum((k(sample_m[:,None]-n[None,:])@a)**2)/line)
    rh.append(np.sum((k(sample_m[:,None]+.5-n[None,:])@a)**2)/line)
    qn.append(np.sum(gram)/N**2)
circle=np.sum(np.exp(-8*np.pi**2*T*l*l))
plt.rcParams.update({'font.size':11,'axes.titlesize':12,'svg.fonttype':'none'})
fig=plt.figure(figsize=(7.2,7.6),layout='constrained')
grid=fig.add_gridspec(2,2)
axs=[fig.add_subplot(grid[0,0]),fig.add_subplot(grid[0,1]),fig.add_subplot(grid[1,:])]
axs[0].plot(xi,np.real(integer),label=r'$V_T(\xi)$: integer',color='#12698c')
axs[0].plot(xi,np.abs(half),label=r'$|V_{T,1/2}(\xi)|$',color='#b94b3d')
axs[0].scatter([.5],[0],color='#b94b3d',zorder=3)
axs[0].set(xlabel=r'Fourier coordinate $\xi$',ylabel='Sample multiplier',title=r'Original Gaussian, $T=1/8$')
axs[0].legend(loc='upper center',fontsize=9)
axs[1].loglog(sizes,ri,'o-',label='Integer samples',color='#12698c')
axs[1].loglog(sizes,rh,'s-',label='Half-integer samples',color='#b94b3d')
axs[1].set(xlabel=r'Coefficients $N$ (even)',ylabel='Sample square sum /\nline norm squared',title=r'Same coefficients $a_n=(-1)^n$')
axs[1].legend(fontsize=9)
axs[2].loglog(sizes,qn,'o-',label='Line norm squared',color='#12698c')
axs[2].loglog(sizes,np.full(len(sizes),circle),'--',label='Circle norm squared',color='#b94b3d')
axs[2].set(xlabel=r'Number of coefficients $N$',ylabel='Actual norm squared',title=r'Same coefficients $a_n=1/N$')
axs[2].legend(fontsize=9)
for ax in axs:ax.grid(alpha=.18)
fig.savefig(H/'sampling.png',dpi=180)
fig.savefig(H/'sampling.svg')
print('Rendered sampling.png and sampling.svg; finite numerical samples, not interval certificates.')
