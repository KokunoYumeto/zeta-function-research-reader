from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

root = Path(__file__).resolve().parent
out = root / 'figures'
out.mkdir(exist_ok=True)
fig, ax = plt.subplots(figsize=(14, 8), dpi=160)
fig.patch.set_facecolor('#f8fafc')
ax.set_facecolor('#f8fafc')
ax.set(xlim=(0, 14), ylim=(0, 8))
ax.axis('off')

def box(x, y, w, h, title, lines, color):
    ax.add_patch(FancyBboxPatch((x, y), w, h,
        boxstyle='round,pad=0.14,rounding_size=0.12',
        facecolor='white', edgecolor=color, linewidth=2))
    ax.text(x+w/2, y+h-0.28, title, ha='center', va='top',
            fontsize=14, weight='bold', color=color)
    for i, line in enumerate(lines):
        ax.text(x+w/2, y+h-0.86-i*0.47, line,
                ha='center', va='top', fontsize=12, color='#172033')

ax.text(0.3, 7.73, 'One full mixed tensor, two different arithmetic receivers',
        fontsize=19, weight='bold', color='#14233c')
ax.text(0.3, 7.22,
        r'$H_0=B_0/(W\cap B_0),\quad W=\overline{E\mathcal{S}(\mathbb{A})_{0}};'
        r'\qquad \rho\neq1-\rho,\quad m=m_\rho=m_{1-\rho}$', fontsize=14)

box(0.35, 2.3, 5.4, 3.9, 'Retained original tensor', [
    r'$U_\rho\otimes U_{1-\rho}\ \subset\ H_0\otimes H_0$',
    r'$D^{[2]}=1+N_1+N_2$',
    r'$R_a^{[2]}=a\exp((\log a)(N_1+N_2))$',
    r'$v=u_{\rho,m}\otimes u_{1-\rho,m}\neq0$',
    'Every original nilpotent order is retained.',
    r'Full support: $(v,1_L)$.',
], '#2a5aa0')

box(8.2, 4.8, 5.3, 1.6, 'Convolution receiver', [
    r'$m_2(v)=0\in H[2],\qquad \alpha_a=R_{a^2}$',
    r'$(v,1_L)\longmapsto e=(0,1_L)\neq\tau$',
], '#92412d')
box(8.2, 1.95, 5.3, 2.0, 'Original duality contraction', [
    r'$\beta(f\otimes g)=Q(f,\overline{g})$',
    r'$\beta(v)=m(-1)^m c_\rho^2\neq0$',
    r'Action on the scalar target: $z\longmapsto az$.',
], '#17664e')

for target, label, ty in [((8.0, 5.45), r'$m_2$', 5.45),
                          ((8.0, 2.55), r'$\beta$', 2.8)]:
    ax.add_patch(FancyArrowPatch((5.95, 4.2), target,
        arrowstyle='-|>', mutation_scale=18, linewidth=2, color='#43536b'))
    ax.text(6.8, ty, label, fontsize=16, color='#283951')

ax.text(0.35, 1.40,
        r'$c_\rho=[(s-\rho)^m]M(s)\neq0,\quad '
        r'M(s)=2\zeta(s)\left['
        r'\frac{\pi^2\Gamma((s+4)/2)}{2\pi^{(s+4)/2}}'
        r'-\frac{3\pi\Gamma((s+2)/2)}{4\pi^{(s+2)/2}}\right]$',
        fontsize=12)
ax.text(0.35, 0.94,
        'The zero convolution value does not remove the mixed tensor or its nonzero duality value.',
        fontsize=12, color='#172033')
ax.text(0.35, 0.46,
        'Complete proofs: GDT13–27; full semiring tensor: GFT3, GFT8, GFT18.\n'
        'Human source: Connes–Consani–Marcolli, arXiv:math/0703392v1, tracepairing and fsharpinv.',
        fontsize=9, color='#43536b')
fig.subplots_adjust(left=0.015, right=0.995, bottom=0.015, top=0.995)
fig.savefig(out / 'global_mixed_tensor_receivers.svg')
fig.savefig(out / 'global_mixed_tensor_receivers.png')
plt.close(fig)

