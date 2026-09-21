"""Exact symbolic figure for PS/PB/ECC/OCQ; no sampled arithmetic zeros."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
B=Path(__file__).resolve().parent
O=B/'figures_prime_collision';O.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'mathtext.fontset':'dejavusans'})
fig=plt.figure(figsize=(14,12),facecolor='#f7f9fc')
ax=fig.add_axes([0,0,1,1]);ax.set_xlim(0,14);ax.set_ylim(0,12);ax.axis('off')
ink='#15283c';blue='#176893';red='#a64235';green='#236845'
def box(x,y,w,h,fc='#ffffff',ec='#cad6e2'):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.12,rounding_size=0.12',fc=fc,ec=ec,lw=1.3))
def txt(x,y,t,size=12,color=ink,ha='left',va='center',weight='normal'):
    ax.text(x,y,t,fontsize=size,color=color,ha=ha,va=va,weight=weight)
def arrow(x1,y1,x2,y2,color=blue):
    ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle='-|>',mutation_scale=14,lw=1.8,color=color))
txt(.55,11.55,'The defining prime and the original collision quotient',21,weight='bold')
txt(.55,11.15,'Exact arithmetic ideals and both original Hilbert metrics; every marked root keeps both signs.',11)
box(.45,7.05,13.1,3.55)
txt(.75,10.25,'POSITIVE ES WITNESSES',14,blue,weight='bold')
txt(.75,9.84,r'$p\equiv1\ (\mathrm{mod}\ 12),\quad 4/p=1/x+1/y+1/z,\quad p\nmid S$',14)
for x,title,roots,vals,smith in [
    (.75,'One denominator divisible by p', ['M: p','N: x','T: y','E: z'],['1','0 or 1','0 or 1','1'],'0,0,0,0,0,0,1,1  or  0,0,0,0,1,1,1,1'),
    (7.25,'Two denominators divisible by p',['M: p','N: x','T: pY','E: pZ'],['3','0','3','3'],'0,0,0,1,1,2,2,3')]:
    txt(x,9.36,title,12,weight='bold')
    for k,(root,val) in enumerate(zip(roots,vals)):
        xx=x+1.42*k;box(xx,8.26,1.18,.78,fc='#eef5fb')
        txt(xx+.59,8.79,root,11,ha='center')
        txt(xx+.59,8.47,'+   −',14,blue,ha='center')
        txt(xx+.59,8.05,val,12,green,ha='center')
    txt(x,7.68,'Branch ideal exponents above; full units retained in PS9.',9)
    txt(x,7.33,'Smith: '+smith,9)
txt(.8,6.68,r'$\Pi_P(C_0^2E_N)=C_0^2E\ \subset\ I=(E:O)$',19,green)
txt(8.1,6.68,'Least coefficient powers: 1 and 2.',12,green)
box(.45,3.08,13.1,2.95)
txt(.75,5.67,'THE SAME FOUR SIGNED COLLISION STATES',14,blue,weight='bold')
txt(.75,5.23,r'$(P,+),\ (P,-),\ (P+t,+),\ (P+t,-)$',16)
txt(.75,4.7,'Raw covariance eigenvalue orders',11,red)
txt(.75,4.29,r'$1,\quad |t|,\quad |t|^2,\quad |t|^3$',18,red)
arrow(5.4,4.65,7.0,4.65)
txt(6.2,5.07,r'$Z_t$',17,ha='center')
txt(7.35,4.96,'Retained jets, including the full kernel minimum',11,blue)
txt(7.35,4.49,r'$(f_0(P),\ \Delta_t f_0,\ f_1(P),\ \Delta_t f_1)$',16)
txt(7.35,4.0,r'$J_{b,t}=E_tH_b^{-1}E_t^*>0\quad (b=U,W)$',15)
txt(.75,3.47,r'$Z_t C_{b,t}Z_t^*=\mathrm{diag}(J_{b,t},J_{b,t})$',16,blue)
txt(8.9,3.47,'The same exact map at both receivers.',10)
box(.45,.8,13.1,1.8,fc='#edf6f1',ec='#a6cbbb')
txt(.75,2.27,'THE ACTUAL INDUCED ORIGINAL CONDUCTOR',14,green,weight='bold')
txt(.75,1.77,r'$\overline{\mathcal{T}}_t^{-1}=\pi_{U,t}\,(T_A\oplus T_A)^{-1}\,\iota_{W,t}$',18)
txt(8.1,1.8,r'$\|\wedge^j\overline{\mathcal{T}}_t^{-1}\|\leq\prod_{k=1}^j\gamma_k$',17,green)
txt(.75,1.19,'Squared inverse singular values: eigenvalues of J_W,t J_U,t⁻¹, each twice; finite at t = 0.',12)
txt(.55,.43,'Proofs: PS6–25, PB1–8, PES1–12, ECC31–43, OCQ1–11. Human sources: ES reader v69; Tao; DLMF Ch. 18; Jouve–Rodriguez-Villegas.',8)
txt(.55,.18,'Symbolic diagram. The one-divisible valuation-one row is permitted by the proved bound; its existence is not claimed. No arithmetic zero trajectory is depicted.',8)
for ext in ['png','svg']:
    fig.savefig(O/f'20_prime_and_original_collision.{ext}',dpi=170,facecolor=fig.get_facecolor())
plt.close(fig)
print(str(O/'20_prime_and_original_collision.png'))
