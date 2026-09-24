"""Exact full-L parity receiver and its ordinary prime distinction, HFP."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
R=Path(__file__).resolve().parent
fig=plt.figure(figsize=(15,13),facecolor='white');a=fig.add_axes([.03,.03,.94,.94]);a.set(xlim=(0,15),ylim=(0,13));a.axis('off')
ink='#182432';blue='#164e75';teal='#087e83';purple='#7452a6';muted='#526475';red='#9b3850'
a.text(.2,12.6,'A prime distinguishes the actual theta lift from its synchronization',fontsize=23,fontweight='bold',color=ink)
a.text(.2,11.96,r'$\mathcal{A}_L\ \longrightarrow\ L[C_2]\ \longrightarrow\ \mathcal{P}(C_2),\qquad (f,\nu)\longmapsto(\nu_0,\nu_1)$',fontsize=23,color=blue)
a.text(.2,11.35,r'Full lattice product: $(a,b)(c,d)=(a\wedge c\vee b\wedge d,\ a\wedge d\vee b\wedge c)$',fontsize=19,color=ink)
a.text(.2,10.79,r'$\chi:L\to\mathbb{B}$ is a stated receiver map; all labels remain in the preceding full-L construction.',fontsize=15,color=muted)
labels=[('Neither parity',r'$\varnothing$',(0,0),True),('Even only',r'$\{0\}$',(1,0),False),('Odd only',r'$\{1\}$',(0,1),False),('Both parities',r'$\{0,1\}$',(1,1),True)]
for i,(title,math,bits,member) in enumerate(labels):
    x=.2+i*3.7
    a.add_patch(FancyBboxPatch((x,7.55),3.35,2.55,boxstyle='round,pad=.05,rounding_size=.08',facecolor='#faedf0' if member else '#eaf5f3',edgecolor=red if member else teal,lw=1.5))
    a.text(x+1.675,9.62,title,ha='center',fontsize=18,fontweight='bold',color=ink)
    a.text(x+1.675,8.99,math,ha='center',fontsize=30,color=red if member else teal)
    a.text(x+1.675,8.37,rf'$({bits[0]},{bits[1]})$',ha='center',fontsize=23,color=ink)
    a.text(x+1.675,7.84,'in the prime' if member else 'outside the prime',ha='center',fontsize=14,color=red if member else teal)
a.text(.25,6.96,r'$\mathfrak{p}_{\mathrm{mix}}=\{\varnothing,C_2\},\qquad\{1\}\cdot\{1\}=\{0\},\qquad C_2\cdot A=C_2\quad(A\ne\varnothing)$',fontsize=22,color=purple)
a.text(.25,6.33,'This is an ordinary semiring prime ideal. It is not a downward or subtractive ideal.',fontsize=16,color=ink)
a.add_patch(FancyBboxPatch((.2,1.6),14.45,4.17,boxstyle='round,pad=.05,rounding_size=.08',facecolor='#f3f6fa',edgecolor='#d5dfe8'))
a.text(.5,5.32,'The two original lifts have the same function and different prime membership',fontsize=18,fontweight='bold',color=ink)
a.text(.5,4.6,r'$\mathbf{H}_t=(H_t,(1_L,0_L,1_L,0_L,\ldots))\quad\longmapsto\quad\{0\}\notin\mathfrak{p}_{\mathrm{mix}}$',fontsize=21,color=teal)
a.text(.5,3.85,r'$J\mathbf{H}_t=(H_t,(1_L,1_L,1_L,1_L,\ldots))\quad\longmapsto\quad C_2\in\mathfrak{p}_{\mathrm{mix}}$',fontsize=21,color=red)
a.text(.5,3.13,r'$\mathbf{H}_t^{\star_t k}=(T_t(H_0^k),(1_L,0_L,1_L,0_L,\ldots))\qquad(k\geq1)$',fontsize=21,color=blue)
a.text(.5,2.4,'Every tensor power keeps the same distinction. Inverting J removes this prime.',fontsize=17,color=ink)
a.text(.25,.96,'Proofs: SHP17–28, HTK24–32 and the complete HFP prime-spectrum calculation.',fontsize=12,color=muted)
a.text(.25,.57,'The diagram shows the exact four-element parity receiver, not an exhaustive picture of the full spectrum.',fontsize=12,color=muted)
a.text(.25,.18,'Kernel: Brad Rodgers & Terence Tao, arXiv:1801.05914v5. Full carrier: The Clankers, v11, def:lattice-split.',fontsize=11,color=muted)
for ext in ['pdf','svg','png']:fig.savefig(R/f'HEAT_FLAG_PRIME_SPECTRUM.{ext}',dpi=160,facecolor='white')
plt.close(fig)
print('Rendered the exact parity-prime comparison.')
