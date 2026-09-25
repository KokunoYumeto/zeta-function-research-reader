from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

r = Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','mathtext.fontset':'dejavusans','font.size':12})
fig = plt.figure(figsize=(16,12), facecolor='#f8fafc')
ax = fig.add_axes([0,0,1,1]); ax.set_xlim(0,16); ax.set_ylim(0,12); ax.axis('off')

def box(x,y,w,h,text,size=16):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.12',
                 facecolor='#e5f1e9',edgecolor='#52637a'))
    ax.text(x+w/2,y+h/2,text,ha='center',va='center',fontsize=size,linespacing=1.5)

ax.text(.6,11.48,'The geometric trace carries the residue degree factor',fontsize=22,weight='bold',color='#13263d')
ax.text(.6,10.98,'GTR0–GTR10: integer covers n ≥ 1, both endpoint stalks, all zero multiplicities',fontsize=13,color='#46566b')
box(.8,9.40,6.85,1.03,r'$z\mapsto z^n:\quad (a_1,\ldots,a_n)\mapsto\sum_{j=1}^n a_j$'+'\nInterior sheets: each has multiplicity 1.',15)
box(8.15,9.40,7.0,1.03,r'$(r_pv_p,v_p)\mapsto(nr_pv_p,nv_p)$'+'\nBoth poles: multiplicity n; both endpoint coordinates retained.',15)
ax.text(8,8.92,r'$\mathrm{Tr}_n\,u_n=n\,1_{\mathscr{F}}$'+'  on the entire coefficient sheaf. [GTR2.1–GTR2.4]',ha='center',fontsize=16)
ax.plot([.6,15.4],[8.52,8.52],color='#adb7c5')

xs=[6.8,10.0,13.4]
for x,txt in zip(xs,[r'$H^0=Z$',r'$H^1=Q$',r'$H^2=A$']):
    ax.text(x,8.03,txt,ha='center',fontsize=18,weight='bold')
rows=[(7.36,'Geometric pullback',[r'$1$',r'$1$',r'$n$']),
      (6.75,'Geometric trace',[r'$n$',r'$n$',r'$1$']),
      (6.14,r'Full pullback $B_n$',[r'$\rho(n)$',r'$T_n$',r'$nT_n$']),
      (5.53,r'Trace with inverse coefficients $U_n$',[r'$n\rho(n^{-1})$',r'$nT_{n^{-1}}$',r'$T_{n^{-1}}$'])]
for y,label,vals in rows:
    ax.text(.85,y,label,fontsize=14,va='center')
    for x,txt in zip(xs,vals):ax.text(x,y,txt,ha='center',va='center',fontsize=18)
ax.text(8,4.90,r'$U_nB_n=B_nU_n=n\,1,\qquad U_n^{\prime}=n(B_n^{-1})^{\prime}$',ha='center',fontsize=18)
ax.text(8,4.48,'The inverse in this formula acts on coefficients. For n > 1, the cover has no single-valued inverse. [GTR4]',ha='center',fontsize=12)
ax.plot([.6,15.4],[4.12,4.12],color='#adb7c5')

ax.text(.85,3.68,'Original-zeta residue → degree-minus-one transfer transpose',fontsize=17,weight='bold')
box(.95,2.08,14.1,1.08,
    r'$\iota(G)(F)=\sum_{\rho}\mathrm{Res}_{s=\rho}\frac{F(s)G(1-s)}{\zeta(s)}\,ds$'
    +'\n'+r'$\kappa^{\prime}\iota T_n=U_n^{\prime}\kappa^{\prime}\iota,\qquad U_n^{\prime}|_{Q^{\prime}}=nT_{n^{-1}}^{\prime}$',18)
ax.text(8,1.63,'Finite full-jet residues extend in the specified SDT strong topology; the original ζ remains the denominator.',ha='center',fontsize=12)
ax.text(8,1.13,r'$U_n^{\prime}\kappa^{\prime}\delta_{\rho,j}=n^{1-\rho}\sum_{h=0}^{j}\frac{(-\log n)^{j-h}}{(j-h)!}\kappa^{\prime}\delta_{\rho,h},\qquad\delta_{\rho,j}(F)=F^{(j)}(\rho)/j!$',ha='center',fontsize=16)
ax.text(.6,.61,'Proofs: GTR2–GTR5; RD2–RD5; SDT8. Source setting: Connes–Consani arXiv:0903.2024v3 §5; sphere construction CSP.',fontsize=11,color='#46566b')
ax.text(.6,.28,'All operations occur on the constructed coefficient receiver. The supporting datum remains '+r'$\tau\langle Z_1;\mathrm{no}\ Z_2\rangle$'+'.',fontsize=11,color='#46566b')
for ext in ('png','svg'):fig.savefig(r/('ramified_trace.'+ext),dpi=160,facecolor=fig.get_facecolor())
plt.close(fig)
