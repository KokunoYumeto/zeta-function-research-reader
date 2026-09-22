"""Reproducible exact-labelled illustration for NL8–NL16."""
from pathlib import Path
from fractions import Fraction
import json, math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

root=Path(__file__).resolve().parent
data=json.loads((root/'NON_EULERIAN_LENGTH_CHECKS.json').read_text())
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11})
fig,axes=plt.subplots(1,2,figsize=(14.5,6))
fig.patch.set_facecolor('#f9fafc')
for ax in axes:
 ax.set_facecolor('#f9fafc');ax.axhline(0,color='#526173',lw=1)
 ax.spines[['top','right']].set_visible(False)
atoms=[x for x in data['atoms'] if Fraction(x['product'])<=3]
xs=[math.log(float(Fraction(x['product']))) for x in atoms]
ys=[float(Fraction(d['log_multiplier']))*x for x,d in zip(xs,atoms)]
for x,y,d in zip(xs,ys,atoms):
 color='#b23d47' if y<0 else '#147d92'
 axes[0].vlines(x,0,y,color=color,lw=3);axes[0].scatter([x],[y],color=color,s=40)
 axes[0].annotate(d['product'],(x,y),xytext=(0,9 if y>=0 else -20),textcoords='offset points',ha='center',color=color)
axes[0].set_xlim(.30,1.18);axes[0].set_ylim(-.72,1.5)
axes[0].set_xlabel(r'Length $\ell=\log R$ (labels give exact $R$)')
axes[0].set_ylabel(r'Atom weight in $-F_1^{\prime}/F_1$')
axes[0].set_title(r'Separated endpoint: $F_1=\zeta-1$',loc='left',fontweight='bold',pad=18)
axes[0].text(.03,.94,r'$\nu_1\{\log(9/4)\}=-\log(3/2)$',transform=axes[0].transAxes,va='top',color='#b23d47')
ns=list(range(1,17));vals=[float(Fraction(data['first_jet_alpha'][str(n)])) for n in ns]
axes[1].bar(ns,vals,color=['#147d92' if v>=0 else '#b23d47' for v in vals],width=.64)
axes[1].set_xticks(ns);axes[1].set_ylim(-1.23,1.28)
axes[1].set_xlabel(r'Integer $n$');axes[1].set_ylabel(r'Exact first-jet coefficient $\alpha(n)$')
axes[1].set_title(r'Infinitesimal shift: $\dot\nu_0$',loc='left',fontweight='bold',pad=18)
for n in (6,10,15):
 v=vals[n-1]
 axes[1].annotate(data['first_jet_alpha'][str(n)],(n,v),xytext=(0,7),textcoords='offset points',ha='center',fontsize=10)
axes[1].text(.02,.055,r'$\dot\nu_0=\sum_n\alpha(n)[\delta_{\log n}-(\log n)\delta^{\prime}_{\log n}]$',transform=axes[1].transAxes,fontsize=11)
fig.suptitle('Support changes the arithmetic distribution',x=.065,ha='left',fontsize=18,fontweight='bold')
fig.text(.065,.08,'Left: all nonzero positive-length atoms with R ≤ 3; the atom (log 2)δ₀ is retained in the proof.\nRight: coefficients for n = 1,…,16, including products of distinct primes. Bars show coefficients, not the full distributions.\nProof: NON_EULERIAN_LENGTH_DERIVATION, NL8–NL16. Source: Secondary Note, first-log-jet-explicit.',fontsize=10,color='#374151',va='top')
fig.subplots_adjust(left=.065,right=.98,top=.82,bottom=.23,wspace=.23)
out=root/'figures';out.mkdir(exist_ok=True)
fig.savefig(out/'24_non_eulerian_lengths.png',dpi=170)
fig.savefig(out/'24_non_eulerian_lengths.svg')
print('Rendered figure 24.')
