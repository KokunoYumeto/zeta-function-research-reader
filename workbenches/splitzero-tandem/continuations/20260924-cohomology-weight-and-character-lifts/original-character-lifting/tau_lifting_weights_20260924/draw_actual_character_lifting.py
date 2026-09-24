from pathlib import Path
import json
import sympy as s
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

H=Path(__file__).resolve().parent
checks=[]
def check(name, result):
    assert result, name
    checks.append(name)
t=s.symbols('t')
for m in range(1,5):
    for r in range(1,5):
        g=2+3*t-t**2+5*t**3+2*t**4
        v=s.series(1/(2*g),t,0,r).removeO()
        zeta=t**m*g
        size=m+r
        A=s.zeros(size)
        B=s.zeros(r)
        for n in range(1,size):A[n-1,n]=-n
        for n in range(1,r):B[n-1,n]=-n
        R=s.zeros(r,size)
        for n in range(size):
            for j in range(min(n,r-1)+1):
                R[j,n]=2*s.binomial(n,j)*s.factorial(n-j)*zeta.expand().coeff(t,n-j)
        L=s.zeros(size,r)
        for j in range(r):
            for k in range(j+1):L[m+j-k,j]=s.factorial(j)*v.coeff(t,k)/s.factorial(m+j-k)
        check(f'm={m},r={r}: full summation lift',R*L==s.eye(r))
        check(f'm={m},r={r}: original generators intertwine',R*A==B*R)
        delta=A**r*L
        check(f'm={m},r={r}: relation belongs to original kernel',R*delta==s.zeros(r,r))
        d=min(m,r)
        check(f'm={m},r={r}: full connecting rank',delta[m-d:m,:].rank()==d)
        chi=3+2*t+7*t**2-t**3+4*t**4
        ub=(-1)**m*chi*g.subs(t,-t)
        for j in range(r):
            actual=sum(delta[h,j]*s.factorial(h)*(-1)**h*ub*t**(m-1-h) for h in range(m))
            expected=(-1)**j*s.factorial(j)*t**(r-1-j)*chi/2
            check(f'm={m},r={r},j={j}: residue transport and every raw factorial',s.series(actual-expected,t,0,d).removeO().expand()==0)
y=s.symbols('y')
half=s.Matrix([[s.Rational(1,2),-s.Rational(1,2)],[s.Rational(1,2),s.Rational(1,2)]])
check('full supported Hom boundary retains minus half in both components',half*s.Matrix([-y,0])==s.Matrix([-y/2,-y/2]))
(H/'ACTUAL_CHARACTER_LIFTING_CHECKS_PRIVATE.json').write_text(json.dumps({'count':len(checks),'passed':checks,'scope':'Exact rational finite algebra checks of the full proved formulas, using formal zero germs and formal nonzero reflection germs. These are not numerical zeta-zero tests or substitutes for the analytic proofs.'},indent=2)+'\n',encoding='utf-8')

plt.rcParams.update({'font.family':'DejaVu Sans','mathtext.fontset':'dejavusans'})
def canvas(title):
    fig,ax=plt.subplots(figsize=(14,10.5))
    ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')
    ax.text(.5,.965,title,ha='center',va='top',fontsize=21)
    return fig,ax
def box(ax,x,y,w,h,txt,size=15,color='#edf4fc'):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.008',facecolor=color,edgecolor='#36536d',lw=1.3))
    ax.text(x+w/2,y+h/2,txt,ha='center',va='center',fontsize=size,linespacing=1.6)
def arrow(ax,a,b):ax.annotate('',xy=b,xytext=a,arrowprops={'arrowstyle':'->','lw':1.4,'color':'#36536d'})
def save(fig,name):
    fig.savefig(H/(name+'.png'),dpi=150,bbox_inches='tight')
    fig.savefig(H/(name+'.svg'),bbox_inches='tight');plt.close(fig)

fig,ax=canvas('The original restriction and its actual residue pushout')
ax.text(.5,.89,r'$Y=\chi\otimes Q^\prime,\quad E=\chi\otimes A^\prime,\quad V=\chi\otimes S^\prime,\quad U_a=a(T_{a^{-1}})^t$',ha='center',fontsize=16)
xs=[.18,.5,.82]
for yy,labels in [(.77,[r'$Y$',r'$E$',r'$V$']),(.54,[r'$C_\zeta=Y/DQ$',r'$E_{\rm res}=E/iDQ$',r'$V$'])]:
    ax.text(.025,yy,'0',ha='center',va='center',fontsize=17)
    ax.text(.975,yy,'0',ha='center',va='center',fontsize=17)
    for x,lab in zip(xs,labels):box(ax,x-.12,yy-.043,.24,.086,lab)
    for left,right in [(.035,.052),(.308,.372),(.628,.692),(.948,.968)]:arrow(ax,(left,yy),(right,yy))
for x,lab in zip(xs,[r'$q_C$',r'$r$',r'$\mathrm{id}_V$']):
    arrow(ax,(x,.713),(x,.598));ax.text(x+.028,.657,lab,ha='left',fontsize=14)
for yy in [.826,.596]:
    ax.text(.34,yy,r'$i$' if yy>.7 else r'$\bar i$',ha='center',fontsize=15)
    ax.text(.66,yy,r'$p=\Sigma^\prime$' if yy>.7 else r'$\bar p$',ha='center',fontsize=15)
ax.text(.5,.442,'Both rows are exact. The lower row is the pushout along the stated residue quotient.',ha='center',fontsize=12)
box(ax,.07,.254,.86,.136,r'$q(G)v=0,\quad\bar p e=v,\quad \bar i c_e=q(G)e$'+'\n'+r'$s(v)=e-\bar i\left((q(G)|_{C_\zeta})^{-1}c_e\right),\qquad \bar p s(v)=v,\quad q(G)s(v)=0$',17,color='#edf7ef')
ax.text(.5,.205,r'$\bar p^{-1}(V_{\rm lf})\simeq C_\zeta\oplus V_{\rm lf},\qquad U_a s(v)=s(U_a v)$',ha='center',fontsize=18)
ax.text(.04,.15,'The section is coherent on all polynomial-annihilated classes. The full kernel remains nonzero.\nIts faithful prime-dilation module lies in the first summand. The full supported cone is retained.\nNo arithmetic operation, parity or numerical weight is assigned to primitive Z₁ / τ.',va='top',fontsize=11.5,linespacing=1.45)
ax.text(.04,.045,'Complete proofs: RPC1–RPC6; independent check RQC0–RQC4. Original support: Connes–Consani 0903.2024v3 §5.\nAnalytic source: Meyer math/0412277v3. Geometric target: Deligne, Weil II §§3.6.1–3.6.3.',va='top',fontsize=10,linespacing=1.4)
save(fig,'ACTUAL_RESIDUE_PUSHOUT')

fig,ax=canvas('One lifting class, two precisely different receiving maps')
ax.text(.5,.889,r'$\zeta(\rho)=0,\quad m=\operatorname{ord}_\rho\zeta,\quad b=1-\rho,\quad N=G-b$',ha='center',fontsize=17)
box(ax,.06,.695,.88,.139,r'$A_j=\left.\partial_z^j M_{A,z}\right|_\rho,\quad S_j=\left.\partial_z^j M_{S,z}\right|_\rho,\quad NA_j=-jA_{j-1}$'+'\n'+r'$\Lambda_{\rho,0}=\frac{A_m}{2\zeta^{(m)}(\rho)},\quad\Sigma^\prime\Lambda_{\rho,0}=S_0,\quad N\Lambda_{\rho,0}=-\frac{mA_{m-1}}{2\zeta^{(m)}(\rho)}$',17)
ax.text(.5,.648,'Least generalized-character order of this lift: m + 1. All prime logarithms are retained in MCL7.',ha='center',fontsize=12)
box(ax,.12,.505,.76,.092,r'$\delta_N(S_0)\in Y/NY,\qquad (D\;\mathrm{mod}\;N)^{-1}\delta_N(S_0)=\left[\frac{\chi_\zeta(b)}{2}\right]\ne0$',17,color='#fff4e8')
arrow(ax,(.36,.495),(.25,.38));arrow(ax,(.64,.495),(.75,.38))
box(ax,.025,.233,.45,.139,'Actual residue pushout'+'\n'+r'$Y/NY\longrightarrow C_\zeta/NC_\zeta=0$'+'\n'+'The image vanishes; the character lifts.',14,color='#edf7ef')
box(ax,.525,.233,.45,.139,'Full supported derived comparison'+'\n'+r'$S_0\longmapsto-\delta_N(S_0)/2$'+'\n'+r'$(D\;\mathrm{mod}\;N)^{-1}(-\delta_N/2)=-\chi_\zeta(b)/4$',14,color='#fff4e8')
ax.text(.5,.174,r'$\chi_\zeta(b)=\pi^{b-1/2}\frac{\Gamma((1-b)/2)}{\Gamma(b/2)},\qquad 0<\Re b<1$',ha='center',fontsize=17)
ax.text(.04,.125,'This is the actual formula at every nontrivial zero, with its actual multiplicity. It is not a sample zero.\nThe full order-r classes, endpoints, extra copies and all cohomological degrees are in ORE4–ORE8.\nA longer-block lift exists. Deligne’s surjectivity theorem does not require a splitting with fixed block length.',va='top',fontsize=11,linespacing=1.45)
ax.text(.04,.034,'Proofs: MCL5–MCL10, ORE5.6–5.8, ORE8.8–8.10, RPC6–RPC8. Human sources: Connes–Consani, Meyer, Deligne.\nReproducible figure and exact factor checks: draw_actual_character_lifting.py. This figure does not assert RH.',va='top',fontsize=9.8,linespacing=1.4)
save(fig,'ACTUAL_SUPPORTED_CHARACTER_CLASS')
print(json.dumps({'checks':len(checks),'figures':['ACTUAL_RESIDUE_PUSHOUT.png','ACTUAL_SUPPORTED_CHARACTER_CLASS.png']}))
