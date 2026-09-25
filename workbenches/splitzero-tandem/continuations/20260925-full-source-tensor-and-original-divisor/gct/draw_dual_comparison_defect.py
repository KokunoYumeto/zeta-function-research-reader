from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

r=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','mathtext.fontset':'dejavusans','font.size':12})
fig=plt.figure(figsize=(16,12),facecolor='#f8fafc')
ax=fig.add_axes([0,0,1,1]);ax.set_xlim(0,16);ax.set_ylim(0,12);ax.axis('off')

def box(x,y,w,h,t,size=17):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.12',facecolor='#e5f1e9',edgecolor='#52637a'))
    ax.text(x+w/2,y+h/2,t,ha='center',va='center',fontsize=size,linespacing=1.5)

def arrow(a,b,label=''):
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle='->',mutation_scale=19,color='#334155',linewidth=1.7))
    if label:ax.text((a[0]+b[0])/2,(a[1]+b[1])/2+.20,label,ha='center',fontsize=12)

ax.text(.6,11.48,'Continuous and algebraic duals: the exact comparison',fontsize=22,weight='bold',color='#13263d')
ax.text(.6,10.98,'VSD0–VSD14: the sheaf cone, the full coefficient defect, and its polynomial operators',fontsize=13,color='#46566b')
box(.95,9.32,14.1,1.05,
    r'$\mathscr{D}_c\mathscr{F}\longrightarrow\mathbb{D}_Y\mathscr{F}\longrightarrow\mathscr{E}$'
    +'\n'+r'$\mathscr{E}=\mathrm{Cone}\left(i_*(A^{\dagger})^2\longrightarrow\mathscr{L}_{A^{\dagger}}[2]\oplus i_*W^{\dagger}\right),\quad\mathrm{arrow}=(g,-r^{\dagger})$',17)
ax.text(8,8.88,r'$E^{\prime}=\mathrm{Hom}_{\mathrm{cont}}(E,\mathbb{C}),\quad E^*=\mathrm{Hom}_{\mathbb{C}}(E,\mathbb{C}),\quad E^{\dagger}=E^*/E^{\prime}$',ha='center',fontsize=15)
ax.text(8,8.59,r'$\mathscr{L}_{A^{\dagger}}$'+' denotes the constant sheaf on Y with coefficient '+r'$A^{\dagger}$'+'.',ha='center',fontsize=10)
ax.plot([.6,15.4],[8.5,8.5],color='#adb7c5')
ax.text(.85,8.03,'All spectral polynomial data are already continuous',fontsize=17,weight='bold')
ax.text(8,7.45,r'$L F(s)=sF(s),\qquad E\in\{A,J,Q\},\qquad 0\ne P\in\mathbb{C}[t]$',ha='center',fontsize=17)
box(.95,5.96,14.1,1.03,
    r'$P(L^{\dagger}):E^{\dagger}\ \simeq\ E^{\dagger}$'
    +'\n'+r'$\ker P(L^{\prime})\simeq\ker P(L^*),\qquad\mathrm{coker}\,P(L^{\prime})\simeq\mathrm{coker}\,P(L^*)$',18)
ax.text(8,5.50,'Every finite-dimensional '+r'$L^*$'+'-invariant subspace of '+r'$E^*$'+' is contained in '+r'$E^{\prime}$'+'. [VSD13.11–VSD13.12]',ha='center',fontsize=14)
ax.text(8,5.08,'The nonzero defect carries a '+r'$\mathbb{C}(t)$'+'-vector-space structure. No discontinuous functional is differentiated.',ha='center',fontsize=12)
ax.plot([.6,15.4],[4.71,4.71],color='#adb7c5')
ax.text(.85,4.28,'The topology specifies which full receiver is obtained',fontsize=17,weight='bold')
box(.95,2.40,4.00,.97,r'$\mathscr{D}_{\mathrm{fin}}$'+'\nAll finite-support zero-jet functionals',14)
box(10.25,3.18,4.80,.92,r'$\mathcal{Q}^{\prime}_{\beta}$'+'\nEntire continuous strong dual',15)
box(10.25,1.51,4.80,.92,r'$\mathcal{Q}^{*}_{\sigma}$'+'\nEntire algebraic pointwise dual',15)
arrow((5.1,3.14),(10.04,3.62),'Strong completion [SDT7–SDT8]')
arrow((5.1,2.63),(10.04,1.96),'Weak completion [VSD10]')
ax.text(8,1.03,'Both routes retain the full original-zeta residue formula. The two topologies and completions are specified separately.',ha='center',fontsize=12)
ax.text(.6,.62,'Proof locators: VSD8–VSD10 and VSD13; original residue RD; strong topology SDT. Source setting: CC arXiv:0903.2024v3 §5.',fontsize=11,color='#46566b')
ax.text(.6,.28,'These are coefficient operations after arithmetic reconstruction. The support remains '+r'$\tau\langle Z_1;\mathrm{no}\ Z_2\rangle$'+'.',fontsize=11,color='#46566b')
for ext in ('png','svg'):fig.savefig(r/('dual_comparison_defect.'+ext),dpi=160,facecolor=fig.get_facecolor())
plt.close(fig)
