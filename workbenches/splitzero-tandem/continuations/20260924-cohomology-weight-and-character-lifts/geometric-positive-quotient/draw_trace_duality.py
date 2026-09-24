"""Exact schematic of the ramified trace and its full dual receiver."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

base=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','mathtext.fontset':'dejavusans','font.size':12})
fig,ax=plt.subplots(figsize=(13,10.6))
ax.set_xlim(0,13); ax.set_ylim(0,10.6); ax.axis('off')
ink='#14384b'; blue='#225f83'; green='#22674f'
def text(x,y,s,size=12,color=ink):
    ax.text(x,y,s,fontsize=size,color=color,va='center')
def panel(x,y,w,h,title):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.1',
        facecolor='#f5f8fa',edgecolor='#b8cad3'))
    text(x+.16,y+h-.3,title,13,blue)
def arrow(x1,y1,x2,y2):
    ax.annotate('',xy=(x2,y2),xytext=(x1,y1),
                arrowprops={'arrowstyle':'->','lw':1.6,'color':blue})

text(.3,10.24,'Ramified trace, full residue completion, and the dual comparison',18,blue)
text(.3,9.82,'Exact coefficient maps after the complete arithmetic reconstruction; no coordinate is assigned to tau.',10)
panel(.3,6.64,12.38,2.8,'A. The actual cover and its trace: every recovered integer n >= 1')
text(.64,8.51,r'$0\ \longmapsto\ 0$',18)
text(.64,7.95,'Local multiplicity n',11)
text(.64,7.5,r'$V_+\ \longrightarrow\ V_+:\ v\mapsto nv$',13)
text(4.1,8.51,r'$b_n(z)=z^n$',19)
text(4.1,7.95,'Interior fibre: n sheets, each multiplicity 1',11)
text(4.1,7.5,r'$A^{\oplus n}\longrightarrow A:\ (a_j)\mapsto\sum_{j=1}^n a_j$',13)
text(9.72,8.51,r'$\infty\ \longmapsto\ \infty$',18)
text(9.72,7.95,'Local multiplicity n',11)
text(9.5,7.5,r'$V_-\longrightarrow V_-:\ v\mapsto nv$',12)
text(.64,6.96,r'$\mathrm{Tr}_n\,b_n^*=n\,\mathrm{id}\qquad H^0=Z,\quad H^1=Q,\quad H^2=A$',15,green)

panel(.3,3.72,12.38,2.5,'B. The complete original-zeta receiver and the two different dual actions')
text(.64,5.19,r'$\mathcal{H}_{\mathrm{res}}$',21)
arrow(2.43,5.19,4.1,5.19); text(2.83,5.55,r'$\mathfrak{I}\;\cong$',14)
text(4.3,5.19,r'$Q^{\prime}_{\beta}$',21)
arrow(5.62,5.19,7.57,5.19); text(6.19,5.55,'inclusion',11)
text(7.8,5.19,r'$Q^*$',21)
arrow(8.85,5.19,10.48,5.19); text(9.26,5.55,'quotient',11)
text(10.66,5.19,r'$Q^{\dagger}$',21)
text(.64,4.63,r'$\mathfrak{I}\widehat{T}_n=\mathsf{U}_n^{\prime}\mathfrak{I},\quad\mathsf{U}_n^{\prime}=n(T_{1/n}^{Q})^{\prime}$',15)
text(6.84,4.63,r'$\mathfrak{I}\widehat{\mathsf{V}}_n=\mathsf{B}_n^{\prime}\mathfrak{I},\quad\mathsf{B}_n^{\prime}=(T_n^{Q})^{\prime}$',14)
text(.64,4.07,'The completion uses the exact residue seminorms, uniformly on bounded subsets of the original quotient.',10.4)

panel(.3,.91,12.38,2.37,'C. The additional algebraic-dual sector has an exact operator structure')
text(.64,2.51,r'$E^{\dagger}=E^*/E^{\prime},\quad E=A,J,Q$',17)
text(7.15,2.51,r'$L:F(s)\mapsto sF(s)$',17)
text(.64,1.91,r'$L^{\dagger}-\mu:E^{\dagger}\ \overset{\cong}{\longrightarrow}\ E^{\dagger}\quad(\mu\in\mathbb{C})$',17,green)
text(.64,1.37,'Every finite generalized L*-eigenvector in E* is already continuous; the full quotient remains retained.',11)
text(.32,.49,'Proofs: GTR2-GTR6, GTR10; SDT4-SDT8; VSD7-VSD13. Maps shown are exact; no positivity or weight bound is asserted.',9)
fig.savefig(base/'ramified_trace_duality.png',dpi=180,bbox_inches='tight',facecolor='white')
fig.savefig(base/'ramified_trace_duality.svg',bbox_inches='tight',facecolor='white')
print(base/'ramified_trace_duality.png')

