from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

root = Path(__file__).resolve().parent
plt.rcParams.update({'font.family': 'DejaVu Sans', 'mathtext.fontset': 'dejavusans'})
fig = plt.figure(figsize=(18, 14), facecolor='#f8fafc')
ax = fig.add_axes([0, 0, 1, 1])
ax.set(xlim=(0, 18), ylim=(0, 14))
ax.axis('off')

def panel(y, h, title, lines, color='#e8eff8', size=18):
    ax.add_patch(FancyBboxPatch((.65,y),16.7,h,boxstyle='round,pad=.08',
                              facecolor=color,edgecolor='#90a2b8',linewidth=1))
    ax.text(.9,y+h-.31,title,fontsize=13,weight='bold',va='center')
    ax.text(9,y+(h-.36)/2,'\n'.join(lines),fontsize=size,
            ha='center',va='center',linespacing=1.36)

ax.text(.65,13.5,'The exact source of the defect and its continuous dual',fontsize=24,weight='bold')
ax.text(.65,13.08,'The restricted source splits; the quotient and its connecting map retain what was removed.',fontsize=13)
panel(10.37,2.2,'Original coefficients after arithmetic reconstruction — GDC0–2; AST',[
    r'$Q=A/J,\quad b_r=\beta_rq=D_r^*\mathsf{J}Eq,\quad N_O=\ker(P_OE),\quad A_O=q^{-1}N_O$',
    r'$\ker\beta_r=N_O,\quad\ker b_r=A_O,\quad R=Q/N_O\simeq A/A_O$',
    r'$R\ \overset{\overline{b}_r}{\longrightarrow}\ H_O\quad\mathrm{injective},\qquad \overline{b}_r([a])=b_ra$'
],size=19)
panel(7.28,2.55,'Primal inclusion and the retained connecting map — AST',[
    r'$\mathscr{P}_O=[\mathsf{A}_O^{-1}\ \overset{0}{\longrightarrow}\ i_*H^0]\ \longrightarrow\ '
    r'\mathscr{P}_r=[\mathsf{A}^{-1}\ \overset{+b_r}{\longrightarrow}\ i_*H^0]$',
    r'$\mathscr{P}_O\longrightarrow\mathscr{P}_r\ \overset{+\pi}{\longrightarrow}\ \mathsf{R}[1]\ \overset{\kappa_r}{\longrightarrow}\ \mathscr{P}_O[1]$',
    r'$\text{Stalk:}\quad\delta_{\rm SES}=+\overline{b}_r,\qquad\kappa_r=-\overline{b}_r$',
    r'$\text{Original specialization boundary:}\quad -b_r=\kappa_r\pi:A\longrightarrow H$'
],color='#e5f1e9',size=18)
panel(4.32,2.43,'Strong topology and the transposed triangle — GDC7,10; AST',[
    r'$R^{\prime}_{\beta}\simeq S_O=N_O^{\perp}=\overline{\sigma_r(\overline{H})}^{\,\beta},'
    r'\qquad q^{\prime}S_O=A_O^{\perp}\subset B=A^{\prime}_{\beta}$',
    r'$\mathsf{(A_O^{\perp})}[1]\longrightarrow\mathscr{E}_r\longrightarrow'
    r'\mathsf{((A_O)^{\prime}_{\beta})}[1]\oplus i_*\overline{H}\longrightarrow\mathsf{(A_O^{\perp})}[2]$',
    r'$\mathscr{E}_r=\operatorname{Cone}(-\delta_pa_r)[-1],\quad a_r=q^{\prime}\sigma_r$',
    r'$B/a_r\overline{H}\ \longrightarrow\ B/A_O^{\perp}\simeq(A_O)^{\prime}_{\beta}$'
],size=17)
panel(1.60,2.16,'The parameter changes the presentation by an explicit isomorphism — GDC3–4; AST',[
    r'$D_r=D_tV_{r,t},\quad \beta_r=V_{r,t}^*\beta_t,\quad r,t>1$',
    r'$\mathscr{P}_t\ \overset{(1_A,V_{r,t}^*)}{\longrightarrow}\ \mathscr{P}_r,\qquad'
    r'\mathscr{E}_r\ \overset{(1_B,\overline{V}_{r,t})}{\longrightarrow}\ \mathscr{E}_t$',
    r'$\beta_rQ=V_{r,t}^*(\beta_tQ),\qquad\sigma_r(\overline{H})=\sigma_t(\overline{H})$'
],color='#e5f1e9',size=18)
ax.text(.65,1.13,r'Both poles retain their two endpoint lines: $E_p[1]$ in the primal and $E_p^{\prime}[-1]$ in the dual.',fontsize=12)
ax.text(.65,.77,r'Sans-serif coefficients denote constant sheaves. No metric or coordinate is assigned to $\tau\langle Z_1;\mathrm{no}\ Z_2\rangle$.',fontsize=12)
ax.text(.65,.41,'The unseparated quotient is retained. These maps do not prove that the original attaching map vanishes.',fontsize=12)
ax.text(.65,.07,'Full proofs: GDC0–14; AST0–9 (cone signs: AST5.2a–b). Sources: Connes–Consani §5; Deligne, Weil II §3.6; ACD.',fontsize=11,color='#475569')
for extension in ('png','svg'):
    fig.savefig(root/('adjoint_source_topology.'+extension),dpi=150,facecolor=fig.get_facecolor())
plt.close(fig)
