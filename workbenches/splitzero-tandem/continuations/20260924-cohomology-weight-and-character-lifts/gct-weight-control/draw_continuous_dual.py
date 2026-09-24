from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

r=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','mathtext.fontset':'dejavusans','font.size':12})
fig=plt.figure(figsize=(16,12),facecolor='#f8fafc')
ax=fig.add_axes([0,0,1,1]);ax.set_xlim(0,16);ax.set_ylim(0,12);ax.axis('off')
def arrow(x1,y1,x2,y2,label=''):
    ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle='->',mutation_scale=16,color='#334155',linewidth=1.5))
    if label: ax.text((x1+x2)/2,(y1+y2)/2+.27,label,ha='center',fontsize=13)
def box(x,y,w,h,t,size=15):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.12',facecolor='#e5f1e9',edgecolor='#52637a'))
    ax.text(x+w/2,y+h/2,t,ha='center',va='center',fontsize=size,linespacing=1.5)
ax.text(.6,11.5,'The complete continuous dual and the original-zeta residue map',fontsize=21,weight='bold',color='#13263d')
ax.text(.6,11.02,'CDI0–CDI12, RD0–RD9, SDT0–SDT9: complete spaces, every zero multiplicity, exact degree factors',fontsize=12,color='#46566b')
xs=[3.6,8,12.8]
for x,d in zip(xs,['Degree −2','Degree −1','Degree 0']):ax.text(x,10.45,d,ha='center',fontsize=14,weight='bold')
for x,t in zip(xs,[r"$A'$",r"$A'$",r"$V_+'\oplus V_-'$"]):ax.text(x,9.67,t,ha='center',fontsize=22)
arrow(4.3,9.8,7.25,9.8,r'$0$')
arrow(8.7,9.8,11.6,9.8,r"$\lambda\mapsto(r_+'\lambda,-r_-'\lambda)$")
for x,t in zip(xs,[r"$H^{-2}=A'$",r"$H^{-1}=Q'$",r"$H^0=(\ker d)'$"]):ax.text(x,8.97,t,ha='center',fontsize=17)
ax.text(8,8.49,r"$d=r_+-r_-,\qquad Q=A/J,\qquad J=\Sigma S\ \mathrm{closed},\qquad Q'=J^\perp\subset A'$",ha='center',fontsize=14)
ax.plot([.6,15.4],[8.1,8.1],color='#adb7c5')
ax.text(.85,7.63,'Every support-map sign survives the transpose',fontsize=16,weight='bold')
ax.text(8,7.06,r"$\mathrm{difference}\ \mapsto\ (\lambda,-\lambda),\qquad\mathrm{sum}\ \mapsto\ (\lambda,\lambda),\qquad"
        r"\partial_{\rm loop}'(\lambda_+,\lambda_-)=-\lambda_++\lambda_-$",ha='center',fontsize=14)
box(.95,5.38,14.1,1.04,
    r'$\iota(G)(F)=\sum_{\rho}\mathrm{Res}_{s=\rho}\frac{F(s)G(1-s)}{\zeta(s)}\,ds$'
    +'\n'+r'$G\in\mathcal{Q}_{\rm fin},\qquad\iota:\mathcal{Q}_{\rm fin}\ \simeq\ \mathscr{D}_{\rm fin}\subset\mathcal{Q}^{\prime}$',size=17)
ax.text(8,4.94,'The sum is finite because G has finite full-jet support. Its denominator is the original ζ.',ha='center',fontsize=12)
ax.text(8,4.42,r'$\zeta(\rho+t)=t^m u_\rho(t),\quad P_{ij}=(-1)^j[t^{m-1-i-j}]\,u_\rho(t)^{-1},\quad\det P=u_\rho(0)^{-m}$',ha='center',fontsize=15)
ax.text(8,3.94,'The nonzero determinant retains every nilpotent order in each multiplicity-m block. [RD2–RD3; CDI9]',ha='center',fontsize=12)
ax.plot([.6,15.4],[3.61,3.61],color='#adb7c5')
ax.text(.85,3.15,'Arithmetic covariance retains the geometric factor',fontsize=16,weight='bold')
box(.95,1.6,14.1,1.08,
    r"$\iota(T_aG)=a(T_{1/a})'\iota(G),\qquad N_a^\vee=a^{-1}(T_{1/a})'$"
    +'\n'+r'$\iota(T_aG)=a^2N_a^\vee\iota(G),\qquad P(a^kT_aF,a^\ell T_aG)=a^{k+\ell+1}P(F,G)$',size=17)
ax.text(.6,1.02,r"$\Theta b(s)=\frac{1}{2}\int_0^\infty b(u)u^s\,du/u$"+' is the complete source comparison; the factor ½ is retained. [CDI6; RD7]',fontsize=12)
ax.text(.6,.6,r"$q':Q'_\beta\simeq J^\perp\subset A'_\beta,\qquad\overline{\mathscr{D}_{\rm fin}}^{\,\beta}=\mathcal{Q}'_\beta$"+'; SDT5–SDT8 prove the strong topology and residue completion.',fontsize=12,color='#46566b')
ax.text(.6,.28,'Source: Connes–Consani arXiv:0903.2024v3 §5; actual sphere/localization proof CSP. No operation is assigned to '+r'$\tau\langle Z_1;\mathrm{no}\ Z_2\rangle$'+'.',fontsize=10,color='#46566b')
for ext in ('png','svg'):fig.savefig(r/('continuous_dual.'+ext),dpi=160,facecolor=fig.get_facecolor())
plt.close(fig)
