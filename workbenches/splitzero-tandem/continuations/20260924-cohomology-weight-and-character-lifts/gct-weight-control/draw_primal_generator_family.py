from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

r = Path(__file__).resolve().parent
plt.rcParams.update({'font.family': 'DejaVu Sans', 'mathtext.fontset': 'dejavusans'})
fig = plt.figure(figsize=(16, 12), facecolor='#f8fafc')
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, 16); ax.set_ylim(0, 12); ax.axis('off')

def box(y, h, formula, size=19):
    ax.add_patch(FancyBboxPatch((.8, y), 14.4, h, boxstyle='round,pad=.10',
                               facecolor='#e6eff9', edgecolor='#65768b'))
    ax.text(8, y+h/2, formula, ha='center', va='center', fontsize=size, linespacing=1.5)

ax.text(.65, 11.52, 'The original zeta divisor in an actual generator family', fontsize=22, weight='bold')
ax.text(.65, 11.06, 'Every parameter, jet order r >= 1, and zero multiplicity — GCF1–GCF7; PGF2–PGF7', fontsize=13)
box(9.55, 1.04,
    r'$\mathcal{I}/(L-\lambda)^r\mathcal{I}\ \longrightarrow\ \mathcal{B}/(L-\lambda)^r\mathcal{B}$'
    +'\n'+r'$R_r\ \overset{\mathsf{T}_r(\lambda)}{\longrightarrow}\ R_r,\qquad R_r=\mathbb{C}[h]/(h^r)$')
ax.text(8, 9.08, r'$\mathsf{T}_r(\lambda)_{ij}=F_0^{(i-j)}(\lambda)/(i-j)!\quad(i\geq j);\quad 0\quad(i<j)$', ha='center', fontsize=18)
ax.text(8, 8.55, r'$F_0(s)=\frac{s(s-1)}{8}\,\pi^{-s/2}\Gamma(s/2)\zeta(s),\qquad\det\mathsf{T}_r(\lambda)=F_0(\lambda)^r$', ha='center', fontsize=20)
ax.plot([.65, 15.35], [8.13, 8.13], color='#b3bdc9')
ax.text(.8, 7.7, 'The original meromorphic function is retained by the exact line-module map', fontsize=16, weight='bold')
box(6.30, 1.12,
    r'$\mathcal{O}\ \overset{\zeta}{\longrightarrow}\ \mathcal{O}(D)\ \overset{\mu_c}{\longrightarrow}\ \mathcal{O},\qquad \mu_c(g)=cg$'
    +'\n'+r'$D=[1]-\sum_{n\geq1}[-2n],\qquad c(s)=\frac{s(s-1)}{8}\pi^{-s/2}\Gamma(s/2)$', 18)
ax.text(8, 5.99, 'The middle module stays embedded in meromorphic functions; its frames retain the pole and trivial zeros.', ha='center', fontsize=12)
ax.plot([.65, 15.35], [5.60, 5.60], color='#b3bdc9')
ax.text(.8, 5.16, 'At an actual nontrivial zero: the whole family and its fibre retain different data', fontsize=16, weight='bold')
ax.text(8, 4.64, r'$x=\lambda-\rho,\quad m=m_\rho,\quad F_0(\rho+y)=y^m u_\rho(y),\quad u_\rho(0)\ne0$', ha='center', fontsize=18)
box(3.40, .87,
    r'$\mathscr{C}_{r,\rho}\ \simeq\ \mathbb{C}\{x,h\}/(h^r,(x+h)^m)$'
    +'\n'+r'$\mathrm{length}=mr,\qquad x^{m+r-1}=0,\qquad x^{m+r-2}\ne0$', 19)
ax.text(8, 2.97, 'The original map includes the full unit '+r'$u_\rho(x+h)$'+'; the proof retains its automorphism and inverse.', ha='center', fontsize=12)
box(1.65, .9,
    r'$0\longrightarrow K_{\lambda,r}\ \overset{\partial_{\lambda,r}}{\longrightarrow}\ R_r\ \overset{\mathsf{T}_r(\lambda)}{\longrightarrow}\ R_r\longrightarrow C_{\lambda,r}\longrightarrow0$'
    +'\n'+r'$\dim K_{\rho,r}=\dim C_{\rho,r}=\min(r,m),\quad K_{\rho,r}\simeq\mathrm{Tor}_1(\mathscr{C}_r,\mathbb{C}_\rho)$', 17)
ax.text(.65, 1.14, 'Human source setting: Connes–Consani 0903.2024v3 §5. Deligne, Weil II §3.6 supplies the distinct weight-lifting mechanism.', fontsize=10.5, color='#43546b')
ax.text(.65, .75, r'The support remains $\tau\langle Z_1;\mathrm{no}\ Z_2\rangle$; all displayed operations belong to the reconstructed coefficient spaces.', fontsize=11, color='#43546b')
ax.text(.65, .36, r'The calculation identifies the complete divisor and lifting boundary; these identities do not force $\Re\rho=1/2$.', fontsize=11, color='#43546b')
for ext in ('png', 'svg'):
    fig.savefig(r/('primal_generator_family.'+ext), dpi=160, facecolor=fig.get_facecolor())
plt.close(fig)
