from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

out = Path(__file__).parent
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 10})
fig = plt.figure(figsize=(11.2, 8.0), layout='constrained')
gs = fig.add_gridspec(2, 2, height_ratios=[1, 1.25])
ax = fig.add_subplot(gs[0, 0])
n = np.array([1, 2, 4, 8, 16, 32, 64, 128])
ax.plot(n, 1/n, 'o-', color='#18568c', label=r'$\|a^{(N)}\|_2^2=1/N$')
ax.plot(n, np.ones_like(n), '--', color='#ad4b13', label=r'$m(a^{(N)})=1$')
ax.set_xscale('log', base=2)
ax.set_xticks(n, [str(x) for x in n])
ax.set_ylim(-.03, 1.12)
ax.set_xlabel(r'$N$ original integer coefficients, each $1/N$')
ax.set_title('The coefficient norm loses the mass', loc='left', fontweight='bold')
ax.legend(loc='center right', frameon=False)
ax.grid(alpha=.2)

ax = fig.add_subplot(gs[0, 1])
time = .15
x = np.linspace(-2, 2, 801)
kernel = np.exp(-x*x/(4*time))/np.sqrt(4*np.pi*time)
ax.plot(x, kernel, color='#ad4b13', lw=2.3)
ax.set_title('Supported zero still receives that mass', loc='left', fontweight='bold')
ax.set_xlabel(r'Original real position $y$')
ax.set_ylabel(r'$k_T(y)$')
ax.text(.04, .94, r'$T=0.15$'+'\n'+r'$\mathbb{H}_T\widehat{E}j(a^{(N)},0)=(k_Tv_{1_L},1)$',
        transform=ax.transAxes, va='top', fontsize=10)
ax.text(.05, .30, 'The same output for every N.\nThe retained mass is a separate coordinate.',
        transform=ax.transAxes, fontsize=9, bbox={'facecolor':'white','edgecolor':'none','alpha':.9})
ax.grid(alpha=.2)

ax = fig.add_subplot(gs[1, :])
ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis('off')
ax.text(0, .97, 'The exact map into a prime-boundary class', weight='bold', fontsize=12)
def box(x, y, w, h, title, body, color):
    patch = FancyBboxPatch((x, y), w, h, boxstyle='round,pad=.012',
                          facecolor=color, edgecolor='#34404b', lw=1)
    ax.add_patch(patch)
    ax.text(x+.018, y+h-.045, title, va='top', weight='bold', fontsize=10)
    ax.text(x+.018, y+h-.105, body, va='top', fontsize=10, linespacing=1.65)
def arrow(start, end, label, tx, ty):
    ax.add_patch(FancyArrowPatch(start,end,arrowstyle='-|>',mutation_scale=14,
                                lw=1.2,color='#34404b'))
    ax.text(tx,ty,label,ha='center',fontsize=9)
box(.02,.58,.30,.25,'Graph-completed source',
    r'$(a,0,m),\quad a_{-n}=a_n$'+'\n'+r'$\|a\|_2^2+|m|^2$', '#eef5fc')
box(.56,.58,.41,.25,'Original prime-boundary coordinates',
    r'$\ell_p\otimes(q_T(a),m)$'+'\n'+r'$q_T(a)=\sum_n a_n k_T(n)$', '#fdf1e8')
arrow((.33,.71),(.55,.71),r'$\beta\widehat{B}_{p,T}$',.44,.76)
box(.02,.10,.45,.25,'Gaussian integer weights',
    r'$a_n=e^{-\pi n^2x},\quad m=\vartheta(x)$'+'\n'+r'$x>0,\quad d_T=1/(4\pi T)$', '#eef5fc')
box(.56,.10,.41,.25,'Both moments evaluated',
    r'$\ell_p\otimes(\sqrt{d_T}\,\vartheta(x+d_T),\vartheta(x))$'+'\n'+
    'Original periodization of this class = 0.', '#fdf1e8')
arrow((.475,.23),(.55,.23),'MRT14',.515,.29)
arrow((.77,.57),(.77,.37),'Gaussian family',.86,.45)
ax.text(.02,.02, 'MRT18: the Mellin transform of the retained mass minus its marked zero term is '
        r'$2\pi^{-s/2}\Gamma(s/2)\zeta(s)$, $\Re s>1$.',fontsize=9)
fig.savefig(out/'SUPPORTED_ZERO_MASS_RECEIVER.pdf')
fig.savefig(out/'SUPPORTED_ZERO_MASS_RECEIVER.png',dpi=180)
plt.close(fig)
print('Retained-mass figure written; source MCB3, MCB17–18, MRT6–18.')
