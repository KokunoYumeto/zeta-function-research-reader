from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

root = Path(__file__).resolve().parent
fig, ax = plt.subplots(figsize=(12, 6.5))
fig.patch.set_facecolor('#f8fafc')
ax.set(xlim=(0, 12), ylim=(0, 6.5))
ax.axis('off')

def box(x, y, width, height, text, color):
    ax.add_patch(FancyBboxPatch((x, y), width, height,
                 boxstyle='round,pad=0.10', linewidth=1.5,
                 edgecolor=color, facecolor='white'))
    ax.text(x+width/2, y+height/2, text, ha='center', va='center',
            fontsize=13, color='#172033', linespacing=1.5)

def arrow(x1, y1, x2, y2, label, dy=0.16):
    ax.annotate('', xy=(x2,y2), xytext=(x1,y1),
                arrowprops=dict(arrowstyle='->', color='#475569', lw=1.7))
    ax.text((x1+x2)/2, (y1+y2)/2+dy, label, ha='center', fontsize=11)

ax.text(.2, 6.14, 'Two label records, one arithmetic observation',
        fontsize=20, weight='bold', color='#172033')
ax.text(.2, 5.65, r'$b=B_{\mathrm{Weil}}(a,a)$ uses the full original-zeta pairing; no sign is assumed.',
        fontsize=12, color='#475569')
box(.3, 4.0, 3.2, 1.0, r'$Z_1$ only: $\tau$'+'\n'+r'$U=[\tau]$', '#6d28d9')
box(.3, 2.25, 3.2, 1.0, r'$Z_1$ and odd $Z_2$: $1$'+'\n'+r'$f=[1]$', '#0369a1')
box(5.1, 4.0, 2.3, 1.0, r'$\mathcal{B}_C(aU,aU)=bU$', '#6d28d9')
box(5.1, 2.25, 2.3, 1.0, r'$\mathcal{B}_C(af,af)=bf$', '#0369a1')
box(9.55, 3.1, 1.7, 1.0, r'$b$', '#15803d')
arrow(3.65, 4.5, 4.95, 4.5, 'marked lift')
arrow(3.65, 2.75, 4.95, 2.75, 'marked lift')
arrow(7.55, 4.5, 9.40, 3.8, r'$\mathrm{ev}$', .25)
arrow(7.55, 2.75, 9.40, 3.35, r'$\mathrm{ev}$', -.35)
box(.3, .55, 7.1, .95,
    r'$Q=U-f\ne0,\quad Q^2=Q,\quad Qf=0$'+'\n'+r'$bU-bf=bQ$', '#b45309')
box(9.55, .55, 1.7, .95, r'$0$', '#b45309')
arrow(7.55, 1.0, 9.40, 1.0, r'$\mathrm{ev}(bQ)=0$')
ax.text(.3, .05, 'Exact maps: WEIL_UNIT_DIFFERENCE_LIFT.md, WU1 and WU4–WU8. The zero at right is a value, not a missing layer.',
        fontsize=10, color='#475569')
fig.savefig(root/'weil_unit_comparison.png', dpi=170, bbox_inches='tight')
fig.savefig(root/'weil_unit_comparison.svg', bbox_inches='tight')
plt.close(fig)
