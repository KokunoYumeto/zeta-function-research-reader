"""Exact equation diagram only: no sampled or invented native arithmetic data."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

HERE=Path(__file__).resolve().parent
OUT=HERE/'figures'
OUT.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':14,
                     'svg.hashsalt':'native-resolvent-rank-one-RR1-16'})
fig=plt.figure(figsize=(15,10),facecolor='white')
ax=fig.add_axes([0,0,1,1]);ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')
ink='#182632';accent='#176177';quiet='#52606a'

def text(x,y,s,size=16,ha='center',color=ink):
    ax.text(x,y,s,fontsize=size,ha=ha,va='center',color=color)
def arrow(x0,y0,x1,y1):
    ax.add_patch(FancyArrowPatch((x0,y0),(x1,y1),arrowstyle='-|>',
                  mutation_scale=16,linewidth=1.5,color=quiet))
def rule(y):ax.plot([.045,.955],[y,y],color='#cbd2d7',lw=.8)

text(.05,.958,'One scalar uncertainty, with the original complex phase',23,ha='left')
text(.05,.918,'Exact native-measure equations • SZ-20260920-026 • RR1–16',13,ha='left',color=quiet)
rule(.885)
text(.25,.842,'ACTUAL ARITHMETIC INPUT',13,color=accent)
text(.25,.798,r'$d\rho_b=s(x)\,d\nu_b(x),\quad b=0,1$',19)
text(.25,.751,r'$\mu_j^{(b)}=\int_0^\infty x^j\,d\rho_b(x)$',19)
text(.25,.709,'Both parity blocks; their full masses retained',12,color=quiet)
arrow(.46,.778,.53,.778)
text(.745,.842,'FINITE ORIGINAL-MOMENT MATRICES',13,color=accent)
text(.745,.793,r'$F^-=C^*(D+aH)^{-1}C$',19)
text(.745,.746,r'$F^+=C^*(D-\kappa ee^*+aH)^{-1}C$',18)
text(.745,.707,r'$\kappa=(e^*D^{-1}e)^{-1},\quad a=4j^2>0$',16)
rule(.669)
text(.5,.628,r'$F_n(a)=F^-+\lambda zz^*,\qquad z=(1,-a,\ldots,(-a)^n)^T$',22)
text(.5,.582,r'$0\leq\lambda\leq\gamma,\qquad F^+-F^-=\gamma zz^*$',21)
text(.5,.536,'Every matrix entry shares the same real scalar — not independent errors',14,color=quiet)
text(.5,.482,r'$u^*(F_n-F^-)v=\lambda\,\overline{f_u(-a)}f_v(-a)$',22)
ax.plot([.24,.76],[.428,.428],color=accent,lw=3)
ax.plot([.24,.76],[.428,.428],'o',color=accent,ms=7)
text(.24,.393,r'$0$',16)
text(.76,.390,r'$\gamma\,\overline{f_u(-a)}f_v(-a)$',17)
text(.5,.347,'Exact complex line segment; schematic placement, no numerical native values',12,color=quiet)
rule(.319)
text(.18,.271,'SAME SOURCE',12,color=accent)
text(.18,.226,r'$G^-\preceq G\preceq G^+$',20)
arrow(.34,.226,.40,.226)
text(.59,.271,'SAME OBSERVATION FIBRE',12,color=accent)
text(.59,.226,r'$Q_A(G)=(AG^{-1}A^*)^{-1}$',20)
text(.59,.184,r'$\min_{Az=u}z^*Gz=u^*Q_A(G)u$',16)
arrow(.80,.226,.86,.226)
text(.916,.269,'FULL',12,color=accent)
text(.916,.24,'CONDUCTOR',12,color=accent)
text(.916,.201,r'$A\mapsto\overline{C}A$',18)
text(.5,.135,r'$\log\frac{\det Q_1^-\det Q_2^-}{\det Q_3^+\det Q_4^+}'
                 r'\ \leq\ \log\frac{\det Q_1\det Q_2}{\det Q_3\det Q_4}'
                 r'\ \leq\ \log\frac{\det Q_1^+\det Q_2^+}{\det Q_3^-\det Q_4^-}$',22)
text(.05,.064,'Human source: Zimmerling–Druskin–Simoncini, arXiv:2407.21505v3, §§3–5.',11,ha='left',color=quiet)
text(.05,.038,'Complete native receiver: NATIVE_RESOLVENT_RANK_ONE.tex. Native moment values and growing-degree phase remain unevaluated.',11,ha='left',color=quiet)
fig.savefig(OUT/'native_resolvent_rank_one.svg',metadata={'Date':None,'Creator':'Exact native resolvent equation diagram'})
fig.savefig(OUT/'native_resolvent_rank_one.png',dpi=180,metadata={'Software':'Exact native resolvent equation diagram'})
plt.close(fig)
print('Created exact-equation SVG and PNG; not a numerical arithmetic experiment.')
