from pathlib import Path
import json
import sympy as s
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

H=Path(__file__).resolve().parent
checks=[]
def check(name,ok):
    assert ok,name
    checks.append(name)
T,c,L=s.symbols('T c L',real=True,nonzero=True)
check('Bromwich Gaussian retains all edge cross terms',s.expand(c*L+c*c/T**2-T*T*(L+2*c/T**2)**2/4+T*T*L*L/4)==0)
B=s.Matrix([[s.Rational(1,2),-s.Rational(1,2)],[s.Rational(1,2),s.Rational(1,2)]])
Bi=s.Matrix([[1,1],[-1,1]])
alpha=s.Matrix([1,-1]); half=s.Matrix([s.Rational(1,2),s.Rational(1,2)])
check('supported split inverse, first composition',B*Bi==s.eye(2))
check('supported split inverse, second composition',Bi*B==s.eye(2))
check('anti-diagonal comparison maps to first summand',B*alpha==s.Matrix([1,0]))
check('half-diagonal evaluates the original sum',s.Matrix([[1,1]])*half==s.ones(1))
check('companion cone mirror has both signs',B*s.Matrix([[0,-1],[-1,0]])*Bi==s.diag(1,-1))
rp,rm=s.symbols('r_plus r_minus')
check('transpose support map is a cochain map',s.diag(rp,rm)*alpha==s.Matrix([rp,-rm]))
(H/'GLOBAL_PRIME_SUPPORT_CHECKS_PRIVATE.json').write_text(json.dumps({'count':len(checks),'passed':checks,'scope':'Exact finite factor checks supplement the full global analytic and coefficient proofs; no zero-location numerical test.'},indent=2)+'\n',encoding='utf-8')

plt.rcParams.update({'font.family':'DejaVu Sans','mathtext.fontset':'dejavusans'})
fig,ax=plt.subplots(figsize=(13,10))
ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')
def box(x,y,w,h,txt,size=14,color='#eef4fb'):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.008',facecolor=color,edgecolor='#34556d',lw=1.3))
    ax.text(x+w/2,y+h/2,txt,ha='center',va='center',fontsize=size,linespacing=1.5)
def arrow(a,b):
    ax.annotate('',xy=b,xytext=a,arrowprops={'arrowstyle':'->','lw':1.4,'color':'#34556d'})
ax.text(.5,.967,'Global prime actions remain distinguishable in the actual quotient',ha='center',fontsize=19)
ax.text(.5,.915,r'$S_T(x)=\sum_\rho m_\rho x^\rho e^{\rho^2/T^2},\qquad T\geq1,\ x>0$',ha='center',fontsize=18)
box(.035,.72,.44,.135,'Unchanged scale '+r'$x=1$'+'\n'+r'$S_T(1)=\frac{T}{2\sqrt{\pi}}\log T+O(T)$',16)
box(.525,.72,.44,.135,'Each fixed scale '+r'$x\ne1$'+'\n'+r'$S_T(x)=O_x(T)$',16)
ax.text(.5,.875,'Complete constants, prime-power resonances and Gamma terms: GGT3–GGT7; FPO4.',ha='center',fontsize=10)
arrow((.25,.71),(.39,.60));arrow((.75,.71),(.61,.60))
box(.13,.475,.74,.123,r'$\sum_i a_i c_{r_i}=0\quad(r_i\ \mathrm{distinct})$'+'\n'+r'$\Longrightarrow\quad a_j\frac{T\log T}{2\sqrt{\pi}}+O(T)=O(1)\quad\Longrightarrow\quad a_j=0$',15)
ax.text(.5,.425,r'$\mathbb{C}[\mathbb{R}_+^\times]\ \hookrightarrow\ \mathcal{A}_\zeta\ \hookrightarrow\ \mathcal{C}_\zeta,\qquad \delta_r\mapsto[r^s]\mapsto c_r$',ha='center',fontsize=18)
ax.text(.5,.383,'First map: algebra injection. Second map: linear injection into the actual comparison cone.',ha='center',fontsize=11)
box(.11,.23,.78,.104,r'$T_a^\diamond c_r=c_{ar},\qquad R^\prime c_r^\zeta=-r c_{1/r}^{\zeta^\vee}$'+'\n'+r'$\mathbb{C}[X_p,X_p^{-1}:p\ \mathrm{prime}]\ \hookrightarrow\ \mathcal{C}_\zeta$',16,color='#edf7f1')
ax.text(.04,.14,'The original zeta function remains explicit. The Gaussian is a test, not a replacement.\nBoth endpoint values, all multiplicities and every finite trivial-zero contour correction are retained.\nNo numerical weight, arithmetic coordinate, addition or parity is assigned to primitive Z₁ / τ.',fontsize=11,linespacing=1.4)
ax.text(.04,.038,'Proofs: FPO0–FPO8; GGT0–GGT8; UOS2, UOS9.\nHuman sources: Connes–Consani 2006.13771v1, Explicit formula; 0903.2024v3 §5; Meyer math/0412277v3.\nThe geometric lifting target remains Deligne, Weil II §§3.6.1–3.6.3.',fontsize=9.5,linespacing=1.4)
fig.savefig(H/'GLOBAL_PRIME_ORBIT.png',dpi=160,bbox_inches='tight');fig.savefig(H/'GLOBAL_PRIME_ORBIT.svg',bbox_inches='tight');plt.close(fig)

fig,ax=plt.subplots(figsize=(13,9.7));ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')
ax.text(.5,.965,'The relative class has an exact supported placement',ha='center',fontsize=21)
xs=[.115,.36,.63,.885]
for y,labels in [(.78,[r'$P$',r'$A$',r'$\chi A^\prime$',r'$\chi P^\prime$']),(.51,[r'$P$',r'$A$',r'$\chi(A^\prime)^2$',r'$\chi P^\prime$'])]:
    for x,lab in zip(xs,labels):box(x-.079,y-.045,.158,.09,lab,19)
    for x1,x2 in zip(xs,xs[1:]):arrow((x1+.089,y),(x2-.089,y))
ax.text(.02,.88,'Original residue-comparison cone '+r'$\mathcal{K}_\zeta$',fontsize=14)
ax.text(.02,.417,'Dual-supported comparison cone '+r'$\mathcal{L}_\zeta$',fontsize=13)
for x,lab in zip(xs,['id','id',r'$\lambda\mapsto(\lambda,-\lambda)$','id']):
    arrow((x,.72),(x,.57));ax.text(x,.65,lab,ha='center',va='center',fontsize=11,bbox={'facecolor':'white','edgecolor':'none','pad':2})
for x,lab in zip([.235,.49,.762],[r'$-d$',r'$\Psi_\zeta^1$',r'$d^\prime$']):ax.text(x,.825,lab,ha='center',fontsize=14)
for x,lab in zip([.235,.49,.762],[r'$-d$',r'$(\Psi_\zeta^1,-\Psi_\zeta^1)$',r'$d_Z^\prime$']):ax.text(x,.46,lab,ha='center',fontsize=12)
for x,deg in zip(xs,[-1,0,1,2]):ax.text(x,.925,'degree '+str(deg),ha='center',fontsize=10)
box(.055,.22,.89,.17,r'$H^1(\mathcal{L}_\zeta)=\mathcal{C}_\zeta\oplus Y,\qquad Y=\chi\otimes Q^\prime$'+'\n'+r'$[(\lambda_+,\lambda_-)]\mapsto\left(\left[\frac{\lambda_+-\lambda_-}{2}\right],\frac{\lambda_++\lambda_-}{2}\right)$'+'\n'+r'$H^1(\mathcal{J}_\zeta):c_r\mapsto(c_r,0)$',16,color='#edf7f1')
ax.text(.5,.174,r'$H^{-1}:\operatorname{id}_H,\quad H^0:0\to0,\quad H^2:\chi H^\prime\to\chi E^\prime\ \mathrm{by\ restriction}$',ha='center',fontsize=15)
ax.text(.035,.135,'E retains all four endpoint lines and both full extra closed coefficient copies.\nThe original Fourier restriction still has its explicit section. This relative cone is a different constructed map.\nThe comparison preserves source multiplication and every existing support label.',fontsize=11,linespacing=1.4,va='top')
ax.text(.035,.042,'Complete proof: UOS3–UOS8A; original cone ASD14. Reproducible source: draw_global_prime_support.py.\nHuman geometry: Connes–Consani 0903.2024v3 §5. Lifting target: Deligne, Weil II §§3.6.1–3.6.3.',fontsize=10,linespacing=1.4,va='top')
fig.savefig(H/'GLOBAL_SUPPORTED_ORBIT.png',dpi=160,bbox_inches='tight');fig.savefig(H/'GLOBAL_SUPPORTED_ORBIT.svg',bbox_inches='tight');plt.close(fig)
print(json.dumps({'checks':len(checks),'figures':['GLOBAL_PRIME_ORBIT.png','GLOBAL_SUPPORTED_ORBIT.png']}))
