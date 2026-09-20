"""Exact equation diagrams; no synthetic zeros, rescaled axes or sample data."""
from pathlib import Path
import re
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
P=Path(__file__).parent/'figures';P.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':15,'mathtext.fontset':'dejavusans','svg.fonttype':'none'})
ink='#172536';blue='#145A86';orange='#9C491B';green='#1A6957'
def base(title,subtitle):
 f=plt.figure(figsize=(17,10),facecolor='white');ax=f.add_axes([0,0,1,1]);ax.set(xlim=(0,17),ylim=(0,10));ax.axis('off')
 ax.text(.6,9.45,title,fontsize=25,color=ink,weight='bold',va='center')
 ax.text(.6,8.9,subtitle,fontsize=13,color=ink,va='center')
 return f,ax
def box(ax,x,y,w,h,lines,color=blue,size=17):
 ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.12,rounding_size=0.10',facecolor='#F5F8FA',edgecolor=color,lw=1.5))
 for j,line in enumerate(lines):ax.text(x+w/2,y+h-(j+1)*h/(len(lines)+1),line,ha='center',va='center',fontsize=size,color=ink)
def arrow(ax,a,b,label='',offset=(0,.18),color=blue):
 ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=18,lw=1.5,color=color,connectionstyle='arc3'))
 if label:ax.text((a[0]+b[0])/2+offset[0],(a[1]+b[1])/2+offset[1],label,ha='center',va='bottom',fontsize=15,color=color)
def foot(ax,loc):ax.text(.6,.22,loc,fontsize=10,color='#425466',va='bottom')
def save(f,name):
 for t in f.findobj(matplotlib.text.Text):
  val=t.get_text().replace(r'\pmod4',r'\ (\mathrm{mod}\ 4)').replace(r'\pmod5',r'\ (\mathrm{mod}\ 5)')
  val=re.sub(r'\\(ge|le)(?![A-Za-z])',lambda m:'\\'+m[1]+'q',val)
  val=re.sub(r'\\(mathcal|mathsf|mathscr|mathbb)\s+([A-Za-z])',lambda m:'\\'+m[1]+'{'+m[2]+'}',val)
  for old,new in [(r'\underline G',r'{G_{N,J}}'),(r'\underline Q',r'{Q_{N,J}}'),(r'\underline B',r'{B_{N,J}}'),(r'\underline\rho',r'{\rho_{N,J}}')]:val=val.replace(old,new)
  t.set_text(val)
 f.savefig(P/(name+'.svg'),metadata={'Creator':'Reproducible programme equation diagram'})
 f.savefig(P/(name+'.png'),dpi=150)
 plt.close(f)

f,a=base('Original mixed action: recovery controls both directions',r'Original domain: $k\equiv1\pmod4$, $k\ge77$; $q=(k+1)^2$; $r=8k-16$. The period and full root grid are retained.')
box(a,.7,6.6,5.8,1.5,[r'$K=\ker\Lambda\quad(\dim K=r)$',r'kernel metric $H_K=I^*G_NI$'])
box(a,10.5,6.6,5.8,1.5,[r'$B_k=\operatorname{im}\Lambda$',r'quotient metric $Q_N=(\Lambda G_N^{-1}\Lambda^*)^{-1}$'],size=16)
arrow(a,(6.7,7.75),(10.3,7.75),r'$B=\Lambda A I$')
arrow(a,(10.3,6.9),(6.7,6.9),r'$C=J_K A L$',offset=(0,-.43),color=orange)
box(a,.7,3.85,7.35,1.9,['The complete original observation stack',r'$\mathcal O_d=(\Lambda,\Lambda A,\ldots,\Lambda A^d)^{\mathsf T}$',r'$\mathcal R_{d,N}\mathcal O_d=I,\qquad d\le80$'])
box(a,8.7,3.85,7.6,1.9,['The two directions cancel in the weight',r'$\widetilde C+\widetilde B^*=R_N,\quad\operatorname{rank}R_N\le2$',r'$\operatorname{rank}B\ge k-18,\quad\operatorname{rank}C\ge k-20$'],color=orange,size=16)
box(a,.7,1.05,15.6,2.05,[r'$p=\lceil r/d\rceil,\qquad b_N=[C_{d,N}\Vert W_d\Vert(\sum_{j<d}\Vert T\Vert_{H_K}^{2j})^{1/2}]^{-1}$',r'$\sigma_p(\widetilde B)\ge b_N,\quad\sigma_{p-2}(\widetilde C)\ge b_N,\quad\sigma_{2p-2}([A,P_K])\ge b_N$',r'$W_d$ retains every feedback block; $C_{d,N}$ retains the complete original recovery cost.'],color=green,size=17)
foot(a,'DO6–23; DC24–35; DQ1–12. Singular values use the original stated metrics. No projected current sign is assigned.')
save(f,'01_original_mixed_action')

f,a=base('Sixteen cofactor products recover the full conductor class',r'$R=S/(Q)$; $B$ is the original cyclic invariant image; $A_c=\prod_{a=1}^{4}g^aQ$; conductor $=A_cR$, including the vertex.')
box(a,.7,6.75,5.3,1.25,[r'$J_d=B_d/(A_cR)_d$','original graded source'],size=18)
box(a,10.1,6.75,6.2,1.25,[r'$\bigoplus_{i=1}^{4}\bigoplus_{r=1}^{4}(R/B)_{d+4r}$'],size=18)
a.text(13.2,8.25,'All sixteen original targets',ha='center',fontsize=14,color=ink)
arrow(a,(6.2,7.32),(9.9,7.32),r'$[f]\mapsto([x_i^{4r}f])_{i,r}$')
a.text(8.45,6.2,'Injective in every degree',ha='center',fontsize=20,color=green,weight='bold')
box(a,.7,4.3,15.6,1.3,[r'On $x_i\ne0$: the powers $1, x_i^4, x_i^8, x_i^{12}, x_i^{16}$ carry all five characters',r'$0,\ 4i,\ 3i,\ 2i,\ i\pmod5$. They generate the entire local module over the invariants.'],size=16)
box(a,.7,1.5,7.35,2.0,['Four one-step products',r'Six line gates + four plane gates $g_\nu(1/u)$','First nonzero order: 0; at most one gate: 1.',r'All are nonzero for fixed $|u|\ge R_{\rm prop}$.'],color=orange,size=15)
box(a,8.7,1.5,7.6,2.0,['Good coefficient specialization',r'$X_d$ is split over the fixed coefficient ring $\mathcal O$.',r'$\ker(X_d\otimes_{\mathcal O}T)=0$ for every $\mathcal O$-algebra $T$.',r'$F(Xv)=X^{(p)}F(v)$ is the exact Frobenius pullback.'],color=green,size=15)
a.text(.8,.86,'A preceding grid-evaluation kernel is retained. The proper-source target minimum is retained.',fontsize=14,color=ink)
foot(a,'CP1–20 and CP17a; independent CR1–26. Exact coefficient maps; no identification with arithmetic Frobenius or a Hermitian isometry.')
save(f,'02_cofactor_recovery')

f,a=base('One native truncation controls the original metric receivers',r'$\epsilon=L_N^{\sharp}/(2J)<1$, $J>L_N^{\sharp}/2$, $\kappa=(1-\epsilon)^{-1}$. Every truncated integral uses the original measure.')
box(a,.7,6.75,4.45,1.25,[r'$H^{[J]}\preceq H\preceq\kappa H^{[J]}$','original polynomial source'],size=16)
box(a,6.2,6.75,4.4,1.25,[r'$\underline G\preceq G_N\preceq\kappa\underline G$','full polynomial quotient'],size=16)
box(a,11.7,6.75,4.6,1.25,[r'$\underline Q\preceq Q_N\preceq\kappa\underline Q$','full observation quotient'],size=16)
arrow(a,(5.3,7.3),(6.05,7.3),'')
arrow(a,(10.75,7.3),(11.55,7.3),'')
box(a,.7,4.25,15.6,1.6,[r'The fixed original map is $B=\Lambda M_SI$; its source metric is $I^*G_NI$.',r'$\sqrt{1-\epsilon}\,\sigma_j(\underline B)\le\sigma_j(B_N)\le(1-\epsilon)^{-1/2}\sigma_j(\underline B)$'],color=green,size=18)
box(a,.7,1.4,7.35,2.0,['Actual reverse action',r'$C_N+B_N^*=R_N,\quad\operatorname{rank}R_N\le2$',r'$\sigma_{j-2}(C_N)\ge\sqrt{1-\epsilon}\,\sigma_j(\underline B)$','The metric-dependent reverse block is kept.'],color=orange,size=16)
box(a,8.7,1.4,7.6,2.0,['Inherited period metric P',r'$\rho_N^2=\lambda_{\max}(Q_N^{-1/2}P Q_N^{-1/2})$',r'$\sqrt{1-\epsilon}\,\underline\rho\le\rho_N\le\underline\rho$','This is the exact factor in the recovery transfer.'],size=16)
foot(a,'TR1–10 → MS1–8 → DQ/PM. Human multiplier source: Aptekarev, López Lagomasino, Martínez-Finkelshtein (2014), through the proved native receiver.')
save(f,'03_native_metric_brackets')

f,a=base('The complete source kernel and its signed endpoint correction',r'$\phi(x)=(4\pi^2x^4-6\pi x^2)e^{-\pi x^2}$; $f_s(x)=x^{-s}\int_x^{\infty}\phi(y)y^{s-1}dy$; $g_s=f_s/\Phi(s)$.')
box(a,.7,6.35,15.6,1.75,[r'$\mathscr K_T(z,w)=\int_{e^{-T}}^{\infty}g_z(x)g_w(x)dx=E_T(z+w-1)+\mathscr F(z,w)-\mathscr B(z,w;T)$',r'$\Gamma_Z(T)=\mathsf U_Z^*\mathsf K_T\mathsf U_Z$',r'Every primary derivative slot, the full arithmetic unit and both regular cross sums are retained.'],size=17)
box(a,.7,3.55,7.35,1.95,['Full physical action identity',r'$W=\mathsf U_Z^*(\epsilon g^*g-\ell^*h_T-h_T^*\ell)\mathsf U_Z$',r'One endpoint row and both source cross rows.',r'Finite relative spectrum: $\lambda^3-p_T\lambda+\det M_T=0$.'],color=orange,size=15)
box(a,8.7,3.55,7.6,1.95,['After the complete left-block minimum',r'$\log\det Q_+(T)=D_0(T)$',r'$\quad-e^{-2\delta T}T^{4m-2}C_m(T)$',r'$\quad+O_Z(e^{-2\delta T}T^{4m-3}),\qquad C_m(T)>0$'],color=green,size=16)
box(a,.7,1.0,15.6,1.6,['The exact original native receiver still performs the theta map and the entire polynomial minimum:',r'$u^*H_N^{(1)}u=\min_{P\in\mathbb C[S]_{\le N-\deg h_Z}}\Vert\Theta(\psi_u+P(D)\phi_*)\Vert_{L^2(dx)}^2$'],size=18)
foot(a,'SK1–33. Human sources: Askey–Roy, DLMF5.12.1; Paris,8.17.1/4; Roy–Olver–Askey–Wong–Reinhardt,1.14.7/37. No source-metric substitution.')
save(f,'04_full_source_kernel')
print('Created four exact equation diagrams as SVG and PNG:',P)
