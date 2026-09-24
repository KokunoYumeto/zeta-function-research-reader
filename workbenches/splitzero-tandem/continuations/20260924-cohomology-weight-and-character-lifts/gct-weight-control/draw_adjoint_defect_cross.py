from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

root = Path(__file__).resolve().parent
plt.rcParams.update({'font.family': 'DejaVu Sans', 'mathtext.fontset': 'dejavusans'})
fig = plt.figure(figsize=(18, 15), facecolor='#f8fafc')
ax = fig.add_axes([0, 0, 1, 1])
ax.set(xlim=(0, 18), ylim=(0, 15))
ax.axis('off')

def panel(x, y, w, h, title, lines, color='#e6eef8', size=18):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.08',
                              facecolor=color,edgecolor='#91a1b4',linewidth=1))
    ax.text(x+.22,y+h-.35,title,fontsize=13,weight='bold',va='center')
    ax.text(x+w/2,y+(h-.35)/2,'\n'.join(lines),fontsize=size,
            ha='center',va='center',linespacing=1.35)

ax.text(.65,14.5,'One arithmetic defect, two exact specialization tests',fontsize=24,weight='bold')
ax.text(.65,14.08,'Original source, continuous transpose, both pole contributions and every cover branch retained.',fontsize=13)
panel(.65,11.60,16.70,1.98,'Original arithmetic and the constructed maps — ADC1; ACD0–1',[
    r'$F_0(s)=\frac{s(s-1)}{8}\pi^{-s/2}\Gamma(s/2)\zeta(s),\quad Q=A/J,\quad E:Q\to H=\ell^2(\mathscr{Z},m)$',
    r'$D_r=T_r^*-rT_{1/r},\quad a_r=q^{\prime}A_HD_r:\overline{H}\to A^{\prime},\quad b_r=\beta_rq=D_r^*\mathsf{J}Eq:A\to H$'
],size=18)
panel(.65,7.97,8.05,3.02,'Primal specialization — ADC8; ACD4–5',[
    r'$\mathscr{P}_r=[\mathsf{A}_D^{-1}\ \overset{+b_r}{\longrightarrow}\ i_*H^0]$',
    r'$A\ \overset{-b_r}{\longrightarrow}\ H,\qquad K_{-1}=0$',
    r'$\mathrm{Obs}_{-1}=b_rA=\beta_rQ$',
    r'$\operatorname{coker}\mathrm{sp}_{-1}=Q/Z_r$',
    r'$Q\ \overset{\beta_r}{\longrightarrow}\ \beta_rQ,\quad\ker\beta_r=Z_r$'
],size=18)
panel(9.3,7.97,8.05,3.02,'Continuous current dual — ADC3; ACD2–3',[
    r'$\mathscr{E}_r=\operatorname{Cone}(-\delta_pa_r)[-1]$',
    r'$\overline{H}\ \overset{a_r}{\longrightarrow}\ A^{\prime}\longrightarrow A^{\prime}/a_r\overline{H}$',
    r'$\mathrm{Obs}_i=0\quad\text{for every }i$',
    r'$\ker(K_0\to\operatorname{im}\partial_0)=a_r\overline{H}$',
    r'$D_c^{\rm raw}\mathscr{P}_r\simeq\mathscr{E}_r:\quad(-1,+1,-1)$'
],color='#e2f0e8',size=18)
ax.text(9,7.5,'The dual invariant-cycle quotient is zero before the attaching map is known to vanish.',
        ha='center',fontsize=13,weight='bold')
panel(.65,4.94,16.7,2.0,'Full sphere comparison — ACD6; four endpoint lines retained',[
    r'$R\Gamma(Y,\mathscr{P}_r)\simeq[A^{-1}\ \overset{(b_r,b_r)}{\longrightarrow}\ (H\oplus H)^0\ \overset{0}{\longrightarrow}\ A^1]$',
    r'$H^0(Y,\mathscr{P}_r)\simeq H\oplus(H/b_rA),\qquad H^0(Y,\mathsf{P})=Q\ni F\longmapsto(\beta_rF,0)$',
    r'$H^0(Y,\mathscr{E}_r)=\ker(a_r+a_r)\simeq\overline{H}\oplus C_{\rm crit}$'
],size=18)
panel(.65,1.85,16.7,2.56,'Genuine degree n covers — DCA3–7; ACD7–8',[
    r'$\Psi(f_{n*}\mathscr{E}_r)=(A^{\prime})^n,\quad \mathsf{F}_\Psi=T_n^{\prime}\Sigma_n,\quad \mathsf{L}_\Psi=\Delta T_{1/n}^{\prime}$',
    r'$\mathsf{F}\mathsf{L}=n\,1,\qquad \mathsf{L}_\Psi\mathsf{F}_\Psi=\Delta\Sigma_n=\sum_{j=0}^{n-1}\mathsf{t}^j$',
    r'$\mathrm{var}_n(x,[v])=e_0a_rx-(\mathsf{t}-1)v,\quad \mathsf{L}_\Phi x=(\overline{T}_nx,[(0,c,\ldots,(n-1)c)]),\ c=T_{1/n}^{\prime}a_rx$',
    r'$\beta_rT_n=U_n^*\beta_r:\ n^{\rho}=n^{1-\overline{\rho^{\#}}}\quad\text{on every nonzero image line}$'
],color='#e2f0e8',size=17)
ax.text(.65,1.30,r'Each pole retains $E_p[1]$ in the primal and $E_p^{\prime}[-1]$ in the dual; $\dim E_p=2$. $Z_r$ retains the full higher-jet kernel.',fontsize=12)
ax.text(.65,.91,r'No coordinate or metric on $\tau\langle Z_1;\mathrm{no}\ Z_2\rangle$. The displayed operations follow arithmetic reconstruction.',fontsize=12)
ax.text(.65,.52,'The cover factors are proved. They do not separate the source from this boundary image; weight vanishing remains unproved.',fontsize=12)
ax.text(.65,.16,'Complete proofs: ADC0–9, DCA0–12, ACD0–8. Source setting: Connes–Consani §5; Deligne, Weil II §3.6; Reich §§1,3.',fontsize=11,color='#475569')
for extension in ('png','svg'):
    fig.savefig(root/('adjoint_defect_cross.'+extension),dpi=150,facecolor=fig.get_facecolor())
plt.close(fig)
