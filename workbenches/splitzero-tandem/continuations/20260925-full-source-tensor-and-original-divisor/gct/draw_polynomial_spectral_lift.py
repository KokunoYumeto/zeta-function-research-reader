from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

r = Path(__file__).resolve().parent
plt.rcParams.update({'font.family': 'DejaVu Sans', 'mathtext.fontset': 'dejavusans', 'font.size': 12})
fig = plt.figure(figsize=(16, 12), facecolor='#f8fafc')
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, 16); ax.set_ylim(0, 12); ax.axis('off')

def panel(x, y, w, h, text, size=17):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=.12',
                               facecolor='#e5f1e9', edgecolor='#52637a'))
    ax.text(x+w/2, y+h/2, text, ha='center', va='center', fontsize=size, linespacing=1.55)

ax.text(.6, 11.5, 'An actual spectral lifting obstruction vanishes', fontsize=22, weight='bold', color='#13263d')
ax.text(.6, 11.03, 'Continuous currents, algebraic currents, and their constructed quotient — no change of source', fontsize=13, color='#46566b')
panel(.9, 9.41, 14.2, 1.03,
      r'$0\longrightarrow D_c\longrightarrow D_a\longrightarrow D_\dagger\longrightarrow0$'
      +'\n'+r'$D_a\simeq R\Gamma(Y,\mathbb{D}_Y\mathscr{F}),\quad H^\bullet(D_\dagger)\ \mathrm{has\ invertible}\ P(L^\dagger)\quad(0\ne P\in\mathbb{C}[t])$', 16)
ax.text(.9, 8.92, 'The spectral complex retains both the equation and its homotopy:', fontsize=15, weight='bold')
ax.text(8, 8.38, r'$K_P(D)^k=D^k\oplus D^{k-1},\qquad d_P(x,y)=(dx,P(L)x-dy)$', ha='center', fontsize=20)
panel(.9, 6.91, 14.2, .94,
      r'$H^kK_P(D_\dagger)=0\quad\Longrightarrow\quad H^kK_P(D_c)\ \simeq\ H^kK_P(D_a)$'
      +'\n'+'Every algebraic spectral class has a unique continuous spectral class above it.', 17)
ax.plot([.6, 15.4], [6.55, 6.55], color='#adb7c5')
ax.text(.9, 6.12, 'The lift is constructed on the actual current complexes', fontsize=17, weight='bold')
ax.text(8, 5.53, r'$d_P(x,y)=0,\qquad d_P(\bar U,\bar V)=(\bar x,\bar y)$', ha='center', fontsize=19)
ax.text(8, 4.96, 'Choose algebraic lifts U,V of the quotient primitives. The corrected cocycle is', ha='center', fontsize=14)
panel(.9, 3.78, 14.2, .79,
      r'$(x,y)-d_P(U,V)=(x-dU,\ y-P(L)U+dV)\ \in\ K_P(D_c)$', 20)
ax.text(8, 3.38, 'The class is unique modulo continuous spectral boundaries. Representatives are not asserted to be unique.', ha='center', fontsize=12)
ax.plot([.6, 15.4], [3.05, 3.05], color='#adb7c5')
ax.text(.9, 2.64, 'Original-zero jets enter through the full source and its actual quotient', fontsize=16, weight='bold')
ax.text(8, 2.07, r'$F_0(s)=\frac{s(s-1)}{8}\,\pi^{-s/2}\Gamma(s/2)\zeta(s),\quad P(t)=(t-\rho)^m,\ m=m_\rho$', ha='center', fontsize=19)
ax.text(8, 1.52, r'$H^{-1}K_P(D_c)\simeq\ker P(L^{\prime}|Q^{\prime})\simeq H^{-1}K_P(D_a)$', ha='center', fontsize=19)
ax.text(.6, .96, 'Proof locators: CV4–CV8; CP4–CP9. Human setting: Connes–Consani 0903.2024v3 §5; Deligne, Weil II §3.6.', fontsize=10.5, color='#46566b')
ax.text(.6, .61, 'Here D denotes the global section complex; ρ is an actual nontrivial zero. Full multiplicities and endpoints remain in the proof.', fontsize=11, color='#46566b')
ax.text(.6, .28, r'The support remains $\tau\langle Z_1;\mathrm{no}\ Z_2\rangle$. This lift does not determine $\Re\rho$.', fontsize=11, color='#46566b')
for ext in ('png', 'svg'):
    fig.savefig(r / ('polynomial_spectral_lift.'+ext), dpi=160, facecolor=fig.get_facecolor())
plt.close(fig)
