from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

r = Path(__file__).resolve().parent
plt.rcParams.update({'font.family': 'DejaVu Sans', 'mathtext.fontset': 'dejavusans', 'font.size': 12})
fig = plt.figure(figsize=(16, 12), facecolor='#f8fafc')
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, 16); ax.set_ylim(0, 12); ax.axis('off')

def box(x, y, w, h, text, color='#e6eef9', size=15):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=.12',
                               facecolor=color, edgecolor='#52637a', linewidth=1.2))
    ax.text(x+w/2, y+h/2, text, ha='center', va='center', fontsize=size, linespacing=1.5)

def arrow(x1, y1, x2, y2, label=''):
    ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle='->',mutation_scale=16,
                                 color='#334155',linewidth=1.5))
    if label:
        ax.text((x1+x2)/2, (y1+y2)/2+.24, label, ha='center', fontsize=13)

ax.text(.6, 11.52, 'The derived sheaf retains its winding direction', fontsize=22,
        weight='bold', color='#13263d')
ax.text(.6, 11.04, 'CDW0–CDW10: an explicit comparison of complexes, including topology, naturality and orientation',
        color='#46566b')
box(.85, 9.45, 14.3, 1.04,
    r'$R\pi_*\mathscr{F}\ \simeq\ \Omega[0]\ \oplus\ j_{X!}(A\otimes\mathbb{C}[\vartheta])[-1]$'
    +'\n'+r'$\vartheta=\frac{1}{4\pi i}\left(\frac{dz}{z}-\frac{d\overline{z}}{\overline{z}}\right),\qquad\int_{|z|=1}\vartheta=1$',
    color='#e5f1e9', size=17)
ax.text(.9, 8.85, 'Strict map into the actual form resolution', fontsize=16, weight='bold')
box(1, 7.54, 6.6, .88, 'Pole chart\n'+r'$v_\pm\longmapsto(\mathrm{constant}(r_\pm v_\pm),v_\pm)$', size=14)
box(8.4, 7.54, 6.6, .88, 'Punctured chart\n'+r'$a\longmapsto\mathrm{constant}(a),\qquad a[\vartheta]\longmapsto a\vartheta$', size=14)
ax.text(8, 7.05, 'The winding sheaf has zero sections on either pole chart; the form need not extend through a pole.',
        ha='center', fontsize=12)
ax.plot([.6,15.4], [6.7,6.7], color='#adb7c5')
ax.text(.9, 6.25, 'The full source sequence survives in both internal degrees', fontsize=16, weight='bold')
for y, degree, terms in [(5.62, 'Degree 0', [r'$\Omega_J$', r'$\Omega$', r'$j_{X!}Q$']),
                         (4.76, 'Degree 1', [r'$j_{X!}J[\vartheta]$', r'$j_{X!}A[\vartheta]$', r'$j_{X!}Q[\vartheta]$'])]:
    ax.text(.9, y, degree, va='center', fontsize=13)
    for x, t in zip([4.2,8.2,12.3], terms):
        ax.text(x,y,t,ha='center',va='center',fontsize=19)
    arrow(5.5,y,6.9,y); arrow(9.5,y,10.9,y)
ax.text(8, 4.13, 'Each displayed row is exact, with a zero on each end. The internal differentials are zero.',
        ha='center', fontsize=12)
ax.plot([.6,15.4], [3.82,3.82], color='#adb7c5')
ax.text(.9, 3.35, 'Actual actions on the winding summand', fontsize=16, weight='bold')
ax.text(8, 2.8, r'$b_n:z\mapsto z^n\quad\Rightarrow\quad nT_n\qquad'
        r'w:z\mapsto-1/z\quad\Rightarrow\quad-R\qquad'
        r'\alpha:z\mapsto-1/\overline{z}\quad\Rightarrow\quad+R$',
        ha='center', fontsize=14)
box(.95, 1.25, 14.1, .96,
    r'$a[\vartheta]\in H^1(X,j_{X!}A[\vartheta])\quad\longmapsto\quad-a\in H^2(Y,\mathscr{F})$'
    +'\n'+r'$a[\vartheta]\longmapsto-[(1-E_+(s))(\Theta a)(s-1)]\quad\mathrm{in\ the\ GSL\ kernel}$',
    color='#e5f1e9', size=16)
ax.text(.6, .72, 'The minus sign uses the ordered Čech differential r₊−r₋ and positive complex integration. [CDW9.2–CDW10.8]',
        fontsize=11, color='#46566b')
ax.text(.6, .4, 'Sources: Connes–Consani, arXiv:0903.2024v3 §5 and arXiv:2609.00299v1 §§3–4; exact receiver proofs CSP and CDW.',
        fontsize=10, color='#46566b')
ax.text(.6, .14, 'Diagram of proved maps; no coordinate, metric or addition is assigned to '+r'$\tau\langle Z_1;\ \mathrm{no}\ Z_2\rangle$'+'.',
        fontsize=10, color='#46566b')
for ext in ('png','svg'):
    fig.savefig(r / ('derived_winding.'+ext), dpi=160, facecolor=fig.get_facecolor())
plt.close(fig)
