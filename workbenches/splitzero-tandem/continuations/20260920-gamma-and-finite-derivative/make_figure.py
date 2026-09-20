"""Reproducible exact-formula diagram for results056 and058; no sampled curves."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

HERE = Path(__file__).resolve().parent
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 13,
                     'svg.fonttype': 'none'})
fig, ax = plt.subplots(figsize=(16, 11))
fig.patch.set_facecolor('#f6f7fa')
ax.set_xlim(0, 16); ax.set_ylim(0, 11); ax.axis('off')

def box(x, y, w, h, color):
    ax.add_patch(FancyBboxPatch((x, y), w, h,
                 boxstyle='round,pad=0.14,rounding_size=0.13',
                 linewidth=1.3, edgecolor=color, facecolor='white'))

def txt(x, y, s, size=13, color='#172b4d', **kw):
    ax.text(x, y, s, fontsize=size, color=color, va='top', **kw)

def arrow(x1, y1, x2, y2):
    ax.annotate('', xy=(x2,y2), xytext=(x1,y1),
                arrowprops={'arrowstyle':'->','lw':1.7,'color':'#385275'})

txt(.2, 10.9, 'Keep the original derivative error budget', 23, weight='bold')
txt(.2, 10.38, 'Arias de Reyna, arXiv:2201.00342v1: exact source correction and finite replacement', 14)
box(.25, 7.7, 7.15, 1.95, '#28657b')
txt(.45, 9.44, '056 — the first gamma inequality is proved', 16, weight='bold')
txt(.45, 8.97, r'$f^{\prime\prime}(t)=\int_0^\infty e^{-tu}K(u)\,du>0$', 17)
txt(.45, 8.39, r'$R(0)=1,\quad R(x)\downarrow\frac{2\pi}{3\sqrt{3}e^{4/3}}$', 17)
txt(.45, 7.94, 'Positive kernel; exact limit. Proof: 056, thm:gamma.', 11)
box(7.9, 7.7, 7.65, 1.95, '#b64e30')
txt(8.1, 9.44, '058 — global monotonicity is false as printed', 16, weight='bold')
txt(8.1, 8.94, r'$\left[\frac{H(2006)}{H(2000)}\right]^2<\frac{9328515625000}{12454264114047}<1$', 16)
txt(8.1, 8.22, 'Exact gamma recurrence and π > 3; no rounded gamma values.', 11)
txt(8.1, 7.94, 'Proof: 058, thm:ratio. This is not an RH counterexample.', 11)

box(2.8, 6.05, 10.3, .9, '#385275')
txt(7.95, 6.82, r'$m\in\{0,\ldots,3L-3\},\quad E_m=\epsilon_5(m)>0,\quad F_m>0$', 17, ha='center')
txt(7.95, 6.38, r'Original allowance: $\widetilde E_m=\min(4F_m,E_m)$', 15, ha='center')
arrow(5.6, 6.03, 3.9, 5.52); arrow(10.3, 6.03, 12.0, 5.52)
box(.65, 3.4, 6.3, 1.95, '#2b7f59')
txt(.9, 5.15, r'Certify $F_m<E_m$', 18, weight='bold')
txt(.9, 4.59, r'Output $U_m=0$', 17)
txt(.9, 4.04, r'$|F^{(m)}(p)|\leq F_m<\widetilde E_m$', 18)
box(8.55, 3.4, 6.3, 1.95, '#28657b')
txt(8.8, 5.15, r'Certify $E_m<2F_m$', 18, weight='bold')
txt(8.8, 4.59, r'Compute $P_J^{(m)}(p)$; then $\widetilde E_m=E_m$', 15)
txt(8.8, 4.04, r'$|F^{(m)}(p)-P_J^{(m)}(p)|<E_m/2$', 17)

txt(7.8, 3.04, 'The strict tests overlap and cover every positive pair.', 17, ha='center', weight='bold')
txt(7.8, 2.58, 'At E = F use computation; at E = 2F use zero. No equality test is required.', 13, ha='center')
txt(7.8, 2.17, 'Certified shrinking rational intervals eventually pass one test (058, prop:overlap).', 12, ha='center')
box(.65, .67, 14.2, 1.09, '#385275')
txt(.9, 1.57, 'One shared Taylor polynomial for all computed indices', 15, weight='bold')
txt(.9, 1.18, r'$M=1+\max\mathcal{C}$ when $\mathcal{C}\neq\varnothing$; choose $J\geq12$ using both original defJ bounds.', 13)
txt(.9, .87, 'The constants 316 and 632 stay fixed. Empty computed set: every output is zero.', 12)
txt(.3, .35, 'Exact proof diagram, not numerical derivative data. Full definitions and evaluation interface: 056 prop:taylor; 058 eq:eps5, eq:tilde, prop:overlap.', 10)
fig.subplots_adjust(left=.01, right=.99, top=.99, bottom=.02)
fig.savefig(HERE/'ARIAS_DERIVATIVE_REPAIR.png', dpi=150)
fig.savefig(HERE/'ARIAS_DERIVATIVE_REPAIR.svg', metadata={'Date':None})
plt.close(fig)
