"""Exact layer records and two-operation prime spectrum: AB2-AB4a, AB8."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

ROOT = Path(__file__).resolve().parent
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 11})
fig, ax = plt.subplots(figsize=(14, 11))
fig.patch.set_facecolor('#f7f9fc')
ax.set(xlim=(0,14), ylim=(0,11))
ax.axis('off')
ink, blue, green = '#172a43', '#156f95', '#25764d'

ax.text(.5, 10.55, 'The empty zero, the tau base, and the integer layer',
        fontsize=22, weight='bold', color=ink)
ax.text(.5, 10.12, 'Full integer values are retained. These four cases describe label availability.', color=ink)
cards = [
    (0.5, r'$0=\varnothing$', r'$Z_0$: absence', 'No carried parity', '#61748b'),
    (3.85, r'$\tau$', r'$Z_1$: presence', 'No carried parity', blue),
    (7.2, r'$n=2k\ne0$', r'$Z_1$ and $Z_2$', 'Carried parity: even', green),
    (10.55, r'$n=2k+1$', r'$Z_1$ and $Z_2$', 'Carried parity: odd', '#9b445b'),
]
for x, formula, layers, label, colour in cards:
    ax.add_patch(FancyBboxPatch((x, 8.15), 2.95, 1.52,
                 boxstyle='round,pad=.06,rounding_size=.10', fc='white', ec=colour, lw=1.5))
    ax.text(x+1.475, 9.24, formula, ha='center', fontsize=23, color=colour)
    ax.text(x+1.475, 8.78, layers, ha='center', fontsize=12, color=ink)
    ax.text(x+1.475, 8.39, label, ha='center', fontsize=11, color=ink)

ax.text(.5, 7.65, r'$D_2=\mathbb{Z}\setminus\{0\}\ \subset\ D_1=A\setminus\{0\},\qquad A=\mathbb{Z}\sqcup\{\tau\}$', fontsize=19, color=ink)
ax.text(.5, 7.15, r'$\iota(m+n)=\iota(m)+\iota(n),\qquad\iota(mn)=\iota(m)\iota(n)\qquad(m,n\in\mathbb{Z})$', fontsize=18, color=blue)
ax.text(.5, 6.68, 'Exact integer inclusion; proof for every finite arithmetic expression: AB4a.', color=ink)
ax.text(.5, 6.23, r'$1+1=2\quad\longrightarrow\quad\mathrm{even\ present}$', fontsize=17, color=green)
ax.text(7.0, 6.23, r'$1+(-1)=0\quad\longrightarrow\quad\mathrm{absence}$', fontsize=17, color='#61748b')
ax.text(.5, 5.78, 'The four-case observation preserves products. It cannot determine sums without the integer values.', fontsize=11, color=ink)

ax.plot([.5, 13.5], [5.43, 5.43], color='#c4cdda', lw=1)
ax.text(.5, 4.96, 'The prime ideals of these actual operations', fontsize=18, weight='bold', color=ink)
ax.text(.5, 4.53, 'Ideal = contains 0, closed under the specified addition, and absorbs multiplication by every element.', fontsize=10.7, color=ink)
ax.text(.5, 4.15, 'Prime = proper ideal with xy in the ideal only if x or y is in it. Complete proof: AB8.', fontsize=10.7, color=ink)

ax.add_patch(FancyBboxPatch((.65,1.50),7.15,2.10,boxstyle='round,pad=.09', fc='#eaf3f8',ec=blue,lw=1.3))
ax.text(.94, 3.21, r'$D(1)\cong\operatorname{Spec}\mathbb{Z}$', fontsize=17, color=blue)
ax.text(.94, 2.76, 'Every ordinary positive prime p occurs.', fontsize=11, color=ink)
ax.text(1.15, 2.04, r'$\{0\}$', fontsize=23, color=blue)
ax.text(4.85, 2.04, r'$p\mathbb{Z}$', fontsize=23, color=blue)
ax.annotate('', xy=(4.62,2.20), xytext=(2.24,2.20), arrowprops={'arrowstyle':'->','lw':1.5,'color':blue})
ax.text(3.4,2.38,'strict inclusion',ha='center',fontsize=10,color=ink)
ax.text(10.12, 2.04, r'$\mathbb{Z}\subsetneq A$', fontsize=23, color=green)
ax.annotate('', xy=(9.97,2.20), xytext=(6.12,2.20), arrowprops={'arrowstyle':'->','lw':1.5,'color':green})
ax.text(8.15,2.38,'strict inclusion',ha='center',fontsize=10,color=ink)
ax.text(11.20,3.17,'Additional closed point',ha='center',fontsize=12,color=green)
ax.text(11.20,2.78,r'$\tau\notin\mathbb{Z}$ makes this ideal proper.',ha='center',fontsize=10.5,color=ink)
ax.text(.5,1.03,'The blue region is the ordinary spectrum as an open subspace; the added point is in every point closure.',fontsize=10.6,color=ink)
ax.text(.5,.62,'This is the stated two-operation ideal spectrum, with tau as global unit. No analytic positivity is inferred.',fontsize=10.6,color=ink)
ax.text(.5,.21,'Proofs and all operation entries: ABSOLUTE_BASE_AND_INTEGER_LAYER.md, AB1–AB8. Diagram is exact, not a numerical sample.',fontsize=9,color=ink)
fig.savefig(ROOT/'absolute_base_and_integer_layer.png',dpi=160,bbox_inches='tight')
fig.savefig(ROOT/'absolute_base_and_integer_layer.svg',bbox_inches='tight')
plt.close(fig)
