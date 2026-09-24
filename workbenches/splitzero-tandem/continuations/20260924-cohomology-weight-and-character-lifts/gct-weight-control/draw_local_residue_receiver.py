from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

root = Path(__file__).resolve().parent
plt.rcParams.update({'font.family': 'DejaVu Sans', 'mathtext.fontset': 'dejavusans'})
fig = plt.figure(figsize=(18, 15), facecolor='#f7f9fc')
ax = fig.add_axes([0, 0, 1, 1])
ax.set(xlim=(0,18), ylim=(0,15))
ax.axis('off')

def box(x,y,w,h,title,lines,color='#e8eef9',size=17):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.08',facecolor=color,edgecolor='#8491a8'))
    ax.text(x+.24,y+h-.35,title,fontsize=13,weight='bold',va='center')
    ax.text(x+w/2,y+(h-.65)/2,'\n'.join(lines),fontsize=size,ha='center',va='center',linespacing=1.6)

ax.text(.7,14.55,'Where the original residue pairing lives',fontsize=24,weight='bold')
ax.text(.7,14.12,'Exact local specialization, dual arrows and global cochain receiver; every source kernel is retained.',fontsize=13)
box(.7,11.72,16.6,1.92,'Original source — LVD1, LVD6; LNC1',[
    r'$0\longrightarrow J\longrightarrow A\ \overset{q}{\longrightarrow}\ Q\longrightarrow0,\qquad F_0(s)=\frac{s(s-1)}{8}\pi^{-s/2}\Gamma(s/2)\zeta(s)$',
    r'$P=\ker(\mathsf{A}_D\to i_*Q)[1],\qquad F[1]=P\oplus i_*E[1],\qquad E=\mathbb{C}^2\ \text{at each pole}$'
],size=18)
box(.7,8.36,8.05,2.8,'Actual local arrows — LVD2–4',[
    r'$P:\quad A\ \overset{q}{\longrightarrow}\ Q\ \overset{0}{\longrightarrow}\ A$',
    r'$D_cP:\quad A^{\prime}\ \overset{0}{\longrightarrow}\ Q^{\prime}\ \overset{q^{\prime}}{\longrightarrow}\ A^{\prime}$',
    r'$\text{arrows: can, var;}\quad\Psi=R\psi[-1],\quad\Phi=R\phi[-1]$',
    r'$T=1,\qquad \operatorname{coker}(J\to A)=Q$'
],size=17)
box(9.25,8.36,8.05,2.8,'Actual global pairing — LVD5, LVD7',[
    r'$K=[W_0\ \overset{-r}{\longrightarrow}\ A\ \overset{0}{\longrightarrow}\ A]$',
    r'$K^{\vee}=[A^{\prime}\ \overset{0}{\longrightarrow}\ A^{\prime}\ \overset{+r^{\prime}}{\longrightarrow}\ W_0^{\prime}]$',
    r'$\mathfrak{w}^{0}=q^{\prime}\mathcal{W}\overline{q},\quad\mathfrak{w}^{-1}=\mathfrak{w}^{1}=0$',
    r'$H^0(\mathfrak{w})=\mathcal{W}:\overline{Q}\to Q^{\prime}$'
],color='#e1f0e8',size=17)
ax.text(9,7.9,r'The global map is nonzero. Every sheaf map $\overline{P_{\rm full}}\to D_*P_{\rm full}$ induces zero on this $H^0$.',ha='center',fontsize=11)
box(.7,5.24,16.6,2.12,'Constructed Gysin receiver — RGR3–7',[
    r'$a=q^{\prime}\mathcal{W}:\overline{Q}\to A^{\prime},\qquad \mathfrak{o}=\mathrm{Gys}\circ i_*a:i_*\overline{Q}\to\mathsf{A}^{\prime}_D[2]$',
    r'$\mathscr{E}_{\mathcal{W}}=\operatorname{Cone}(-\delta_p a)[-1],\qquad\mathsf{A}^{\prime}_D[1]\to\mathscr{E}_{\mathcal{W}}\to i_*\overline{Q}\ \overset{\mathfrak{o}}{\longrightarrow}\ \mathsf{A}^{\prime}_D[2]$',
    r'$\Psi\mathscr{E}_{\mathcal{W}}=A^{\prime},\quad\Phi\mathscr{E}_{\mathcal{W}}=\overline{Q},\quad\mathrm{can}=0,\quad\mathrm{var}=a$'
],size=18)
box(.7,2.12,16.6,2.56,'The local quotient and the earlier normal lift are related by explicit maps — LNC8–10; FOD7',[
    r'$Q=H^1_p(F)\ \overset{+1\ (p=0),\ -1\ (p=\infty)}{\longrightarrow}\ H^1(Y,F)=Q$',
    r'$0\to J(-1)\to A(-1)\to Q(-1)\to0\quad\overset{(\mathcal{V}F)(\lambda)=F(\lambda-1)}{\longrightarrow}\quad e_+$',
    r'$c_Q=1,\quad q\,c_A=q,\qquad c e_+=0,\qquad \delta f=0\ \text{for }f:\mathcal{Q}[k]\to D_G\text{ in }D(M)$',
    'The separator preserves the local quotient and annihilates the specified normal class.'
],color='#e1f0e8',size=17)
ax.text(.7,1.56,r'$\mathcal{W}(\overline{G})(F)=\sum_\rho m_\rho F(\rho)\overline{G(1-\overline{\rho})},\quad\ker\mathcal{W}=\overline{N_0}$; full higher jets remain in $Q$.',fontsize=13)
ax.text(.7,1.12,r'Positive-circle and positive-quotient signs. $\mathsf{A}_D$ means the constant sheaf; $r=r_+-r_-$; $W_0=V_+\oplus V_-$.',fontsize=12)
ax.text(.7,.71,r'No coordinate or metric is assigned to $\tau\langle Z_1;\mathrm{no}\ Z_2\rangle$. These are post-reconstruction coefficient maps.',fontsize=12)
ax.text(.7,.30,'Complete proofs: LVD0–9, LNC0–11, RGR0–12. Sources: Connes–Consani §5; Reich §§1,3; Deligne, Weil II §3.6.',fontsize=11,color='#43536a')
for ext in ('png','svg'):
    fig.savefig(root/('local_residue_receiver.'+ext),dpi=150,facecolor=fig.get_facecolor())
plt.close(fig)
