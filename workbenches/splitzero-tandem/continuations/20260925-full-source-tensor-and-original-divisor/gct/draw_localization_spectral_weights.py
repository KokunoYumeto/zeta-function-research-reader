from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

r = Path(__file__).resolve().parent
plt.rcParams.update({'font.family': 'DejaVu Sans', 'mathtext.fontset': 'dejavusans'})
fig = plt.figure(figsize=(17, 14), facecolor='#f8fafc')
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, 17); ax.set_ylim(0, 14); ax.axis('off')

def panel(y, h, title, formula, color='#e6eff9', size=19):
    ax.add_patch(FancyBboxPatch((.65, y), 15.7, h, boxstyle='round,pad=.08',
                              facecolor=color, edgecolor='#7a8ca2'))
    ax.text(.95, y+h-.38, title, fontsize=15, weight='bold', va='center')
    ax.text(8.5, y+(h-.65)/2, formula, fontsize=size, ha='center', va='center', linespacing=1.35)

ax.text(.65, 13.5, 'The actual localization row: what separates, and what survives',
        fontsize=22, weight='bold')
ax.text(.65, 13.08, 'Full coefficient kernel, every polynomial order, every original zero multiplicity — CLP2–CLP13',
        fontsize=12)
panel(10.55, 2.1, 'Actual geometric row and its full derivative matrix — CLP2, CLP5–CLP6',
      r'$0\longrightarrow J(-1)\longrightarrow A(-1)\longrightarrow Q(-1)\longrightarrow0$'
      +'\n'+r'$\mathsf{T}_r(\lambda-1)_{ij}=F_0^{(i-j)}(\lambda-1)/(i-j)!\quad(i\geq j);\quad0\quad(i<j)$'
      +'\n'+r'$F_0(s)=\frac{s(s-1)}{8}\pi^{-s/2}\Gamma(s/2)\zeta(s),\qquad t=L+1$', size=18)
panel(8.05, 2.13, 'At an original zero: the normal comparison is invertible — CLP7',
      r'$\lambda=\rho,\quad0<\Re\rho<1,\quad\mu=\rho-1$'
      +'\n'+r'$J(-1)/(L-\mu)^rJ\ \overset{\mathsf{T}_r(\mu)}{\longrightarrow}\ A(-1)/(L-\mu)^rA$'
      +'\n'+r'$\left(\mathsf{T}_r(\mu)^{-1}\right)_{ij}=\frac{1}{(i-j)!}\left(\frac{8\pi^{s/2}}{s(s-1)\Gamma(s/2)\zeta(s)}\right)^{(i-j)}_{s=\mu}$',
      color='#e1f2e9', size=18)
panel(5.42, 2.26, 'At a translated zero: the higher boundary retains the normal extension — CLP8–CLP9',
      r'$\lambda=\rho+1,\quad m=m_\rho,\quad d=\min(r,m)$'
      +'\n'+r'$0\longrightarrow Q(-1)[(t-\rho-1)^r]\ \overset{\beta^2}{\longrightarrow}\ J(-1)/(L-\rho)^rJ$'
      +'\n'+r'$\beta^2\left([F_0(s)/(s-\rho)^j]\right)=[F_0(s)(s-\rho)^{r-j}],\quad1\leq j\leq d$'
      +'\n'+r'$\mathrm{rank}\,\beta^2=d;\qquad\text{source and image character }a^{\rho+1}$',
      color='#fff0dc', size=17)
panel(2.87, 2.19, 'The coherent families have disjoint supports — CLP13',
      r'$\mathscr{C}_r=\mathrm{coker}\,\mathsf{T}_r(\lambda),\qquad\mathscr{C}^{+}_q=\mathrm{coker}\,\mathsf{T}_q(\lambda-1)$'
      +'\n'+r'$\mathrm{supp}\,\mathscr{C}_r=\mathscr{Z}\subset\{0<\Re\lambda<1\},\quad'
      r'\mathrm{supp}\,\mathscr{C}^{+}_q=\mathscr{Z}+1\subset\{1<\Re\lambda<2\}$'
      +'\n'+r'$\mathrm{RHom}_{\mathcal{O}}(\mathscr{C}_r,\mathscr{C}^{+}_q)=0='
      r'\mathrm{RHom}_{\mathcal{O}}(\mathscr{C}^{+}_q,\mathscr{C}_r)$', size=18)
ax.text(.85, 2.38, 'The degree-one spectral lift has an r-dimensional kernel at an original zero (CLP6–CLP7).', fontsize=13)
ax.text(.85, 1.98, 'The shifted boundary is a different lifting equation; the ordinary geometric boundary remains zero.', fontsize=13)
ax.text(.85, 1.58, 'Neither the full J(-1) nor its character quotients are replaced by the coherent normal family.', fontsize=13)
ax.text(.65, 1.05, 'Human sources: Connes–Consani, 0903.2024v3 §5 and 2609.00299v1; Deligne, Weil II §3.6.',
        fontsize=11, color='#43546b')
ax.text(.65, .64, r'The support remains $\tau\langle Z_1;\mathrm{no}\ Z_2\rangle$; these are operations on the reconstructed coefficient spaces.',
        fontsize=11, color='#43546b')
ax.text(.65, .25, r'No common arithmetic modulus or conclusion $\Re\rho=1/2$ is imposed by this diagram.',
        fontsize=11, color='#43546b')
for ext in ('png', 'svg'):
    fig.savefig(r / ('localization_spectral_weights.'+ext), dpi=150, facecolor=fig.get_facecolor())
plt.close(fig)
