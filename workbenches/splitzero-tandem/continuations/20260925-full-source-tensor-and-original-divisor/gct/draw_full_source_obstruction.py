from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

r = Path(__file__).resolve().parent
plt.rcParams.update({'font.family': 'DejaVu Sans', 'mathtext.fontset': 'dejavusans'})
fig = plt.figure(figsize=(18, 15), facecolor='#f7f9fc')
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, 18)
ax.set_ylim(0, 15)
ax.axis('off')

def box(x, y, width, height, title, lines, color='#e7eef9', size=18):
    ax.add_patch(FancyBboxPatch((x, y), width, height, boxstyle='round,pad=.09',
                               facecolor=color, edgecolor='#8392a8'))
    ax.text(x+.3, y+height-.36, title, fontsize=14, weight='bold', va='center')
    ax.text(x+width/2, y+(height-.65)/2, '\n'.join(lines), fontsize=size,
            ha='center', va='center', linespacing=1.5)

ax.text(.7, 14.55, 'The complete source has two different obstruction components',
        fontsize=22, weight='bold')
ax.text(.7, 14.12, 'Actual strict source rows and multiplier actions; every zero multiplicity and the full kernel remain.', fontsize=12)
box(.7, 11.25, 16.6, 2.35, 'Original source and its translated normal source — FOD1; NEA1', [
    r'$F_0(s)=\frac{s(s-1)}{8}\pi^{-s/2}\Gamma(s/2)\zeta(s),\qquad F_+(\lambda)=\frac{(\lambda-1)(\lambda-2)}{8}\pi^{-(\lambda-1)/2}\Gamma((\lambda-1)/2)\zeta(\lambda-1)$',
    r'$\mathcal{Q}=\mathcal{B}/\mathcal{I},\quad \mathcal{Q}_+=\mathcal{B}/\mathcal{I}_+,\quad \mathcal{K}=\mathcal{I}\cap\mathcal{I}_+,\quad c=1-E(\lambda-1)$',
    r'$0\longrightarrow\mathcal{K}\longrightarrow\mathcal{B}\longrightarrow\mathcal{Q}\oplus\mathcal{Q}_+\longrightarrow0$'
], size=18)
box(.7, 7.55, 8.05, 3.15, 'Original component — FOD2–FOD5', [
    r'$e_{\rm low}:\quad0\to\mathcal{K}\to\mathcal{I}_+\to\mathcal{Q}\to0$',
    r'$\mathcal{K}\hookrightarrow\mathcal{I}\quad\Longrightarrow\quad e_0:0\to\mathcal{I}\to\mathcal{B}\to\mathcal{Q}\to0$',
    r'$\operatorname{Ann}_M(e_{\rm low})=\operatorname{Ann}_M(e_0)=\mathfrak{a}$',
    r'$c e_{\rm low}=e_{\rm low}\ne0,\qquad c e_0=e_0\ne0$'
], size=17)
box(9.25, 7.55, 8.05, 3.15, 'Normal component — FOD2–FOD5; NEA3', [
    r'$e_{\rm high}:\quad0\to\mathcal{K}\to\mathcal{I}\to\mathcal{Q}_+\to0$',
    r'$\mathcal{K}\hookrightarrow\mathcal{I}_+\quad\Longrightarrow\quad e_+:0\to\mathcal{I}_+\to\mathcal{B}\to\mathcal{Q}_+\to0$',
    r'$\operatorname{Ann}_M(e_{\rm high})=\operatorname{Ann}_M(e_+)=\mathfrak{a}_+$',
    r'$c e_{\rm high}=0,\qquad c e_+=0,\qquad e_+\ne0$'
], color='#e1f1e9', size=17)
ax.text(9, 7.1, 'The second row in each panel is the actual pushout along its displayed kernel inclusion.',
        ha='center', fontsize=11)
box(.7, 4.52, 16.6, 2.12, 'Exact full-divisor annihilators — FOD4; NEA3, NEA7', [
    r'$\mathfrak{a}=\{h\in M:\operatorname{ord}_{\rho}h\geq m_\rho\ \forall\rho\},\qquad\mathfrak{a}_+=\{h\in M:\operatorname{ord}_{\rho+1}h\geq m_\rho\ \forall\rho\}$',
    r'$M e_{\rm joint}\simeq M/\mathfrak{a}\oplus M/\mathfrak{a}_+,\qquad c\ \text{acts as}\ (1,0)$',
    r'$\mathfrak{a}_+=K_+\ \text{in NEA notation};\qquad \operatorname{Spec}_{\rm alg}(T|_{M e_+})=\{\rho+1\},\quad T[h]=[\lambda h]$'
], size=18)
box(.7, 1.57, 16.6, 2.43, 'Actual localization lift, with the original quotient retained — FOD6–FOD7; NEA10', [
    r'$\delta:D_G\to D_J[1],\qquad M\delta\simeq M/\mathfrak{a}_+,\qquad c\delta=0,\qquad c_{\mathcal{Q}}=1$',
    r'$f:\mathcal{Q}[k]\to D_G\quad\Longrightarrow\quad\delta f=0\quad\Longrightarrow\quad\widetilde f:\mathcal{Q}[k]\to D_F$',
    r'$\beta:\mathcal{B}\to\mathcal{I}_+,\quad F\mapsto cF,\qquad q_{\rm res}\beta=q,\qquad\ker q_{\rm res}=\mathcal{K}$'
], color='#e1f1e9', size=18)
ax.text(.7, 1.15, r'$M$: entire multipliers of polynomial growth on closed vertical strips. Spectrum above means algebraic non-bijectivity.', fontsize=11)
ax.text(.7, .82, r'Central postcomposition is used here. Conjugation fixes the equivariant boundary. No arithmetic purity follows from this alone.', fontsize=11)
ax.text(.7, .49, r'No addition, metric or coordinate is assigned to $\tau\langle Z_1;\mathrm{no}\ Z_2\rangle$. All operations act on reconstructed coefficients.', fontsize=11)
ax.text(.7, .17, 'Full proofs: FOD0–8 and NEA0–10. Inputs: GMS, CLP, CW. Human source settings: Connes–Consani §5; Deligne, Weil II §3.6.', fontsize=10, color='#43536a')
for ext in ('png', 'svg'):
    fig.savefig(r / ('full_source_obstruction.' + ext), dpi=150, facecolor=fig.get_facecolor())
plt.close(fig)
