"""Exact maps from HTP/SHP and the symbolic four-jet construction HSQ."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
R=Path(__file__).resolve().parent
ink='#182432';blue='#164e75';teal='#087e83';purple='#7452a6';muted='#526475'
def canvas(title):
    f=plt.figure(figsize=(15,13),facecolor='white');a=f.add_axes([.03,.03,.94,.94]);a.set(xlim=(0,15),ylim=(0,13));a.axis('off')
    a.text(.2,12.6,title,fontsize=25,fontweight='bold',color=ink)
    return f,a
def panel(a,y,h):a.add_patch(FancyBboxPatch((.13,y),14.65,h,boxstyle='round,pad=.05,rounding_size=.08',facecolor='#f3f6fa',edgecolor='#d5dfe8'))
def save(f,stem):
    for ext in ['pdf','svg','png']:f.savefig(R/f'{stem}.{ext}',dpi=160,facecolor='white')
    plt.close(f)

f,a=canvas('Heat transport: multiplication, flags and actual evaluation')
panel(a,8.5,3.55)
a.text(.4,11.65,r'$\mathcal{E}=\{\sum a_nz^n:\ \sum |a_n|\sqrt{n!}\,h^n<\infty\ \mathrm{for\ every}\ h>0\}$',fontsize=19,color=blue)
a.text(.4,11.02,r'$T_t=e^{-t\partial_z^2},\qquad f\star_t g=T_t((T_{-t}f)(T_{-t}g))$',fontsize=21,color=ink)
a.text(.4,10.35,r'$f\star_t g=\sum_{n\geq0}\frac{(-2t)^n}{n!}f^{(n)}g^{(n)},\qquad z\star_t z=z^2-2t$',fontsize=21,color=teal)
a.text(.4,9.6,'The complete coefficient algebra keeps two descending support chains:',fontsize=16,color=ink)
a.text(.4,8.96,r'$\nu_0\geq\nu_2\geq\cdots,\qquad\nu_1\geq\nu_3\geq\cdots,\qquad a_n\ne0\Rightarrow\nu_n=1_L$',fontsize=21,color=blue)
panel(a,4.85,3.35)
a.text(.4,7.78,'Multiplication includes the mixed odd–odd contribution',fontsize=20,fontweight='bold',color=ink)
a.text(.4,7.05,r'$(\nu\circledast\mu)_0=(\nu_0\wedge\mu_0)\vee(\nu_1\wedge\mu_1)$',fontsize=24,color=purple)
a.text(.4,6.35,r'$(\nu\circledast\mu)_n=\bigvee_{r=0}^{n}\nu_r\wedge\mu_{n-r}\quad(n\geq1)$',fontsize=23,color=purple)
a.text(.4,5.55,r'$\boldsymbol{\Phi}(f,\nu)=(f,(1_K\otimes\nu_n)_n)\ \in\ \mathcal{E}\times\mathcal{F}(K_L)$',fontsize=21,color=blue)
panel(a,1.05,3.5)
a.text(.4,4.13,'The exact character identifies which divisor is transported',fontsize=19,fontweight='bold',color=ink)
a.text(.4,3.42,r'$\chi_{t,z}(f)=(T_{-t}f)(z),\qquad\chi_{t,z}(H_a)=H_{a-t}(z)$',fontsize=23,color=blue)
a.text(.4,2.69,r'$\chi_{t,z}(H_t)=H_0(z),\qquad H_t(z)=\chi_{t,z}(H_{2t})$',fontsize=25,color=teal)
a.text(.4,1.83,'Every entire function, time parameter and support label remains in these maps.',fontsize=16,color=ink)
a.text(.2,.58,'Proofs: HTP1–24, SHP1–28, HDT1–6. All series converge in the displayed coefficient space.',fontsize=12,color=muted)
a.text(.2,.2,'Kernel: Brad Rodgers & Terence Tao, arXiv:1801.05914v5. Full carrier: The Clankers, v11, def:lattice-split.',fontsize=11,color=muted)
save(f,'FULL_SUPPORT_HEAT_PRODUCT')

f,a=canvas('Four distinct actual roots: the complete supported receiver')
a.text(.2,12.06,'Symbolic layout for x > 0, y > 0; no numerical root is asserted. All formulas retain the original centres.',fontsize=13,color=muted)
panel(a,6.15,5.5)
cx,cy,dx,dy=7.5,8.85,4.0,1.45
a.plot([1,14],[cy,cy],color='#acb7c2',lw=1);a.plot([cx,cx],[6.48,11.15],color='#acb7c2',lw=1)
a.text(13.3,cy+.13,r'$\mathrm{Re}\,z$',fontsize=14,color=muted);a.text(cx+.2,10.96,r'$\mathrm{Im}\,z$',fontsize=14,color=muted)
coords=[(cx+dx,cy+dy),(cx-dx,cy-dy),(cx+dx,cy-dy),(cx-dx,cy+dy)]
a.plot([coords[j][0] for j in [0,2,1,3,0]],[coords[j][1] for j in [0,2,1,3,0]],color=blue,lw=1.7)
names=[r'$w_1=x+iy$',r'$w_2=-x-iy$',r'$w_3=x-iy$',r'$w_4=-x+iy$']
for i,((xx,yy),name) in enumerate(zip(coords,names),1):
    a.scatter([xx],[yy],s=90,color=teal,zorder=4)
    a.text(xx,yy+(.46 if yy>cy else -.53),name,fontsize=19,ha='center',color=blue)
    a.text(xx,yy+(-.47 if yy>cy else .3),rf'$D_{i}=\mathbb{{C}}[\epsilon_{i}]/(\epsilon_{i}^{{m}})$',fontsize=16,ha='center',color=purple,bbox=dict(facecolor='#f3f6fa',edgecolor='none',pad=2))
a.text(cx,cy+.35,r'$p_Q(z)=[z^4-2(x^2-y^2)z^2+(x^2+y^2)^2]^m$',fontsize=16,ha='center',color=ink,bbox=dict(facecolor='#f3f6fa',edgecolor='none',pad=2))
a.text(cx,cy-.45,r'$H_t=p_Q U_Q,\quad U_Q(w_i)=H_t^{(m)}(w_i)/(m!P_i(w_i))\ne0$',fontsize=16,ha='center',color=ink,bbox=dict(facecolor='#f3f6fa',edgecolor='none',pad=2))
panel(a,2.55,3.3)
a.text(.4,5.15,r'$G_L(\mathcal{O}(\mathbb{C}\setminus\mathbb{R})/(H_t))\ \longrightarrow\ G_L(\prod_{i=1}^{4}D_i)$',fontsize=22,color=blue)
a.text(.4,4.39,r'$[f]\ \longmapsto\ (\sum_{k=0}^{m-1}f^{(k)}(w_i)\epsilon_i^k/k!)_{i=1}^{4}$',fontsize=22,color=ink)
a.text(.4,3.65,r'$\Phi((b_i)_i,\lambda)=((b_i)_i,1_K\otimes\lambda)$',fontsize=22,color=teal)
a.text(.4,2.97,r'$\widehat q_i\widehat q_j=e\ (i\ne j),\qquad\sum_{i=1}^{4}\widehat q_i=1,\qquad\widehat q_i^2=\widehat q_i$',fontsize=21,color=purple)
a.text(.4,1.91,r'Every actual zero obeys $x^2\partial_t H_t(iy)>2H_t(iy)>0$.',fontsize=20,color=teal)
a.text(.4,1.35,'The receiver retains four arithmetic primes, 4m jet coordinates, and every lattice label.',fontsize=16,color=ink)
a.text(.2,.64,'Proofs: HSQ1–27; the shared-label injection has an exact module retract but no semiring retract.',fontsize=12,color=muted)
a.text(.2,.21,'Kernel: Brad Rodgers & Terence Tao, arXiv:1801.05914v5. Full carrier: The Clankers, v11, def:lattice-split.',fontsize=11,color=muted)
save(f,'FULL_SUPPORT_HEAT_QUARTET')
print('Rendered both exact heat-map and four-jet figures.')
