from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

base=Path(__file__).resolve().parent
fig,ax=plt.subplots(figsize=(15,10.4))
fig.patch.set_facecolor('#f7f8fa');ax.set_facecolor('#f7f8fa')
ax.set(xlim=(0,15),ylim=(0,10.4));ax.axis('off')
def box(x,y,w,h,title,lines,color='#e8eef6'):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.12',ec='#52677c',fc=color,lw=1.2))
    ax.text(x+.18,y+h-.25,title,fontsize=13,fontweight='bold',va='top',color='#102c44')
    for dy,text,size in lines:
        ax.text(x+.18,y+h-dy,text,fontsize=size,va='top',color='#102030')
def arrow(x1,y1,x2,y2,label='',dy=.1):
    ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle='-|>',mutation_scale=14,lw=1.3,color='#315a77'))
    if label:ax.text((x1+x2)/2,(y1+y2)/2+dy,label,fontsize=11,ha='center',va='bottom',bbox={'facecolor':'#f7f8fa','edgecolor':'none','pad':1.5})
ax.text(.35,10.08,'The endpoint extension and the complete cover ideal',fontsize=21,fontweight='bold',color='#102c44')
ax.text(.35,9.61,'Exact source maps, all recovered cover degrees, every original nontrivial-zero multiplicity',fontsize=12,color='#334e68')
box(.4,6.6,14.15,2.62,'1. Retain the pole before taking a quotient  [NPE1–3]',[
(.68,r'$h_t(s)=8e^{ts^2}F_0(s)/s,\quad F_0(s)=\frac{s(s-1)}{8}\pi^{-s/2}\Gamma(s/2)\zeta(s),\quad \mathrm{res}_0h_t=1$',17),
(1.30,r'$0\longrightarrow\mathcal{B}\longrightarrow E=\mathcal{B}\oplus\mathbb{C}h_t\longrightarrow\mathbb{C}_{\chi}\longrightarrow0,\quad\chi(n)=n$',17),
(1.96,r'$U_nh_t=nh_t-\delta_{n,t},\qquad\delta_{n,t}=8e^{ts^2}F_0(s)(n-n^{1-s})/s,\quad\delta_{n,t}(0)=n\log n$',15)])
box(.4,3.69,6.85,2.05,'2a. Endpoint observation retains the extension',[
(.69,r'$f=c/s+a_0+\cdots\ \longmapsto\ (a_0,c)$',16),
(1.16,r'$U_n:(a_0,c)\longmapsto(na_0-n\log n\,c,\ nc)$',15),
(1.67,'Nonzero square-zero part for n > 1  [NPE4]',12)],'#fff0df')
box(7.7,3.69,6.85,2.05,'2b. Full original-ideal pushout splits uniquely',[
(.69,r'$E/I\simeq Q\oplus\mathbb{C}_{\chi},\quad Q=\mathcal{B}/I$',17),
(1.16,r'$[F+ch_t]\longmapsto([F],c)$',16),
(1.67,'All zero jets remain in Q; residue remains  [NPE3]',12)],'#e3f1eb')
arrow(3.75,6.49,3.75,5.84,r'Laurent coefficients',.10)
arrow(11.1,6.49,11.1,5.84,r'quotient by the full $I$',.10)
box(.4,.6,14.15,2.45,'3. The complete discrepancy recovers exactly the original source quotient  [NCI2–7]',[
(.72,r'$\overline{\mathrm{span}\{\delta_{n,t}:n\geq2\}}^{\mathcal{B}}=\overline{F_0\mathcal{B}}^{\mathcal{B}}=I,\qquad F_0\mathcal{B}\subsetneq I$',20),
(1.38,r'$\mathscr{W}_n^*\mathcal{H}_t\Lambda=\mathcal{H}_tU_n^{\prime}\Lambda\ (\mathrm{all}\ n\geq2)\quad\Longleftrightarrow\quad\Lambda\in I^{\perp}$',18),
(1.98,'Global closure in the original strip topology; no finite-height test or assumed purity.',12)],'#e8e8f7')
ax.text(.45,.13,'All displayed numbers and coordinates belong to the reconstructed coefficient system. No coordinate or addition is assigned to tau.',fontsize=10,color='#334e68')
fig.subplots_adjust(left=.02,right=.985,bottom=.015,top=.995)
fig.savefig(base/'endpoint_cover_ideal.png',dpi=160)
fig.savefig(base/'endpoint_cover_ideal.svg')
plt.close(fig)
