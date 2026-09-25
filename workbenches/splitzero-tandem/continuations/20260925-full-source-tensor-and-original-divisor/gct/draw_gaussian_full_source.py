from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

root = Path(__file__).resolve().parent
fig, ax = plt.subplots(figsize=(15, 11))
fig.patch.set_facecolor('#f7f9fc')
ax.set(xlim=(0, 15), ylim=(0, 11))
ax.axis('off')
ink, blue, green, orange = '#15253b', '#245dad', '#176b54', '#9a4c10'

def text(x, y, s, size=15, color=ink, ha='center', va='center'):
    ax.text(x, y, s, fontsize=size, color=color, ha=ha, va=va,
            linespacing=1.5)

def panel(y, h, title):
    ax.add_patch(FancyBboxPatch((0.35, y), 14.3, h,
                 boxstyle='round,pad=0.02,rounding_size=0.12',
                 facecolor='white', edgecolor='#ccd6e3', linewidth=1.2))
    text(0.65, y+h-0.28, title, 16, ha='left')

def arrow(x1, y1, x2, y2, label=None, dy=0.16, color=blue):
    ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle='-|>',
                 mutation_scale=18, linewidth=1.7, color=color))
    if label:
        text((x1+x2)/2, (y1+y2)/2+dy, label, 14, color)

text(7.5, 10.65, 'Gaussian approximation retains the original source', 23)
text(7.5, 10.22, r'$g_t(s)=e^{ts^2},\quad t>0,\qquad Q=\mathcal{B}/\mathcal{I},\quad \mathcal{R}=Q/N_O$', 17)

panel(6.88, 2.95, '1. Exact maps before taking a limit  ·  GAP2–GAP4')
text(2.05, 8.83, r'$Q$', 25)
text(7.45, 8.83, r'$\mathscr{C}=M/\mathfrak{a}$', 23)
text(12.85, 8.83, r'$Q$', 25)
arrow(2.75,8.83,5.7,8.83,r'$j$',0.26)
arrow(9.35,8.83,12.15,8.83,r'$b_t$',0.26)
text(7.5,8.22,r'$b_tj=m_{g_t}\ \longrightarrow\ 1_Q$',19,green)
text(7.5,7.68,'The two embeddings remain proper; no inverse Gaussian is inserted.',15)
text(7.5,7.22,r'$S_ta(u)=\frac{e^{t/4}}{2\sqrt{\pi t}}\int_0^\infty (u/v)^{-1/2}e^{-(\log(u/v)-t)^2/(4t)}a(v)\,\frac{dv}{v}$',16)

panel(3.62, 2.94, '2. The actual specialization square commutes  ·  GAP4–GAP5')
text(2.75,5.47,r'$\mathcal{R}$',24)
text(11.1,5.47,r'$H_{\infty,O}\ \subseteq\ H_O$',22)
text(2.75,4.43,r'$\mathcal{R}$',24)
text(11.1,4.43,r'$H_{\infty,O}\ \subseteq\ H_O$',22)
arrow(3.65,5.47,9.25,5.47,r'$\overline{\beta}_r$',0.25)
arrow(3.65,4.43,9.25,4.43,r'$\overline{\beta}_r$',0.25)
arrow(2.75,5.17,2.75,4.72)
text(1.64,4.96,r'$m_{g_t}$',16)
arrow(11.1,5.17,11.1,4.72)
text(12.85,4.96,r'$G_t^\#$',17)
text(7.5,3.92,r'$(G_t^\# y)_\rho=e^{t(1-\overline{\rho})^2}y_\rho,\qquad (\beta_rF)_\rho=\overline{d_r(\rho)}F(1-\overline{\rho})$',16)

panel(0.68, 2.61, '3. The topology and all endpoint data matter  ·  GAP5–GAP8')
text(0.8,2.39,r'$m_{g_t}\to1$ on $Q,\mathcal{R}$ and their strong duals:',16,green,ha='left')
text(0.8,1.95,'uniformly on bounded sets in each stated source topology.',15,ha='left')
text(0.8,1.41,r'$\mathcal{W}_M(g_th)\to\mathcal{W}_M(h)$ strongly, but $[g_t]$ has no limit in $Q$.',16,ha='left')
text(0.8,0.93,r'Endpoints: $(1,e^t,e^t,1)$; reflection factor: $d_t=e^{t(1-2s)}$.',16,ha='left')

text(7.5,0.3,'Maps and limits of constructed coefficient spaces; no coordinate or metric on the supporting datum.',12)
fig.savefig(root/'gaussian_full_source.png',dpi=170,bbox_inches='tight')
fig.savefig(root/'gaussian_full_source.svg',bbox_inches='tight')
plt.close(fig)
