"""Actual affine-coordinate contour geometry; no sampled zero is invented."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,Polygon
P=Path(__file__).resolve().parent
OUT=P/'figures';OUT.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11})
fig=plt.figure(figsize=(12,8.7),layout='constrained')
grid=fig.add_gridspec(2,2,height_ratios=[3.1,1.3])
verts=np.array([.1+126.75j,.9+126.75j,.9+128.25j,.1+128.25j])
center=.9+(126.75+15.5*1.5/32)*1j
half=1.5/64
radius=1/16
transform=lambda s:-2j*(s-.5)
for col,coordinate in enumerate(('s','z')):
    ax=fig.add_subplot(grid[0,col])
    f=(lambda s:s) if coordinate=='s' else transform
    poly=f(verts)
    ax.add_patch(Polygon(np.c_[poly.real,poly.imag],closed=True,facecolor='#eef4f8',edgecolor='#334e61',lw=1.7))
    critical=f(np.array([.5+126.75j,.5+128.25j]))
    ax.plot(critical.real,critical.imag,color='#207650',lw=2.5,label='Exactly one simple zero lies somewhere\non this open line segment')
    c=f(center)
    rr=radius if coordinate=='s' else 2*radius
    ax.add_patch(Circle((c.real,c.imag),rr,fill=False,ls='--',ec='#2566a6',lw=1.5))
    ends=f(np.array([center-half*1j,center+half*1j]))
    ax.plot(ends.real,ends.imag,color='#2566a6',lw=4)
    ax.plot(c.real,c.imag,'.',color='#2566a6')
    start=f(verts[0]+.2*(verts[1]-verts[0]))
    stop=f(verts[0]+.65*(verts[1]-verts[0]))
    ax.annotate('',(stop.real,stop.imag),(start.real,start.imag),arrowprops={'arrowstyle':'->','color':'#334e61','lw':2})
    ax.set_aspect('equal',adjustable='box')
    ax.set_xlabel('Re '+coordinate);ax.set_ylabel('Im '+coordinate)
    if coordinate=='s':
        ax.set(xlim=(-.06,1.08),ylim=(126.55,128.45))
        ax.set_xticks([.1,.5,.9]);ax.set_xticklabels(['1/10','1/2','9/10'])
        ax.set_yticks([126.75,127.5,128.25]);ax.set_yticklabels(['507/4','255/2','513/4'])
        ax.set_title('Original Mellin coordinate $s$\nOuter disk radius $1/16$')
    else:
        ax.set(xlim=(253.1,256.9),ylim=(-1.2,1.2))
        ax.set_xticks([253.5,255,256.5]);ax.set_xticklabels(['507/2','255','513/2'])
        ax.set_yticks([-.8,0,.8]);ax.set_yticklabels(['−4/5','0','4/5'])
        ax.set_title('Exact image $z=-2i(s-1/2)$\nOuter disk radius $1/8$')
    ax.grid(alpha=.15)
    ax.legend(loc='upper center',bbox_to_anchor=(.5,-.14),fontsize=9,frameon=False)
ax=fig.add_subplot(grid[1,:]);ax.axis('off')
ax.text(.01,.94,'An actual finite certificate, not an all-height or time-zero claim',weight='bold',fontsize=15)
ax.text(.01,.70,r'$1023/4096\leq t\leq1025/4096$     •     128 counterclockwise segments     •     Exact cutoff $N=K=4$',fontsize=12)
ax.text(.01,.46,r'Every boundary margin $>10^{-42}$     •     Winding number $1$     •     $|\rho\prime(t)|<1102$',fontsize=12)
ax.text(.01,.23,r'$g_t(s)=16H_t(z)$,     $\partial_s^j= (-2i)^j\partial_z^j$,     $|dz|=2|ds|$',fontsize=13)
ax.text(.01,.02,'Proofs PMH1–11; Polymath, arXiv:1904.12438v2, ab-cor and RTN-prop, with the complete corrected remainder proof.',fontsize=9)
fig.suptitle('The certified packet in both original coordinates',fontsize=19,weight='bold')
for ext in ('png','svg'):fig.savefig(OUT/('certified_packet.'+ext),dpi=170)
print('Exact affine contour geometry generated; no approximate root location is plotted.')
