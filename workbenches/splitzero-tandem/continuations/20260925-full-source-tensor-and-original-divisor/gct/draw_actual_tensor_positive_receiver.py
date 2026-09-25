from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
out=Path(__file__).resolve().parent
fig=plt.figure(figsize=(15,9),facecolor='#f7f9fc')
ax=fig.add_axes([0,0,1,1]);ax.set_xlim(0,15);ax.set_ylim(0,9);ax.axis('off')
blue='#163b65';teal='#146a63';rust='#965337';gray='#44505e'
def box(x,y,w,h,text,color=blue,size=13):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.12',linewidth=1.5,edgecolor=color,facecolor='white'))
    ax.text(x+w/2,y+h/2,text,ha='center',va='center',fontsize=size,color=color,linespacing=1.6)
def arrow(x,y,x2,y2,label='',dy=.18,color=blue):
    ax.add_patch(FancyArrowPatch((x,y),(x2,y2),arrowstyle='-|>',mutation_scale=15,linewidth=1.5,color=color))
    if label: ax.text((x+x2)/2,(y+y2)/2+dy,label,ha='center',va='bottom',fontsize=12,color=color)
ax.text(.5,8.6,'The actual specialization map under tensor powers',fontsize=23,color=blue,weight='bold')
ax.text(.5,8.18,'All coefficients are after complete arithmetic reconstruction. No coordinate or metric is placed on the supporting datum.',fontsize=12,color=gray)
box(.5,6.35,3.5,1.25,'Original source\nR = Q / N_O')
box(5.5,6.35,4.25,1.25,'Full rapid receiver\nH∞,O')
arrow(4.15,6.98,5.32,6.98,'b = β̄r')
ax.text(10.1,7.12,'(bF)ρ = δρ F(ρ#)',fontsize=16,color=blue)
ax.text(10.1,6.68,'δρ = conjugate(d_r(ρ))',fontsize=12,color=gray)
arrow(2.25,6.2,2.25,5.55,'',color=teal)
arrow(7.6,6.2,7.6,5.55,'',color=teal)
ax.text(3.02,5.87,'apply tensor construction',fontsize=11,color=teal)
ax.text(8.02,5.87,'apply tensor construction',fontsize=11,color=teal)
box(.5,4.25,3.5,1.2,'Original projective tensor source\nR completed tensor k',teal,13)
box(5.5,4.25,4.25,1.2,'Rapid tuples of actual zeros\nH_k ≅ (H∞,O) completed tensor k',teal,12)
arrow(4.15,4.85,5.32,4.85,'b_k',color=teal)
ax.text(10.1,5.07,'Exact character on both sides:',fontsize=12,color=teal)
ax.text(10.1,4.63,'n^(ρ₁# + ··· + ρk#)',fontsize=16,color=teal)
ax.text(.5,3.78,'TWC2–3: dense receiving map; its complete-source kernel is retained explicitly. Product multiplicity = mρ₁ ··· mρk.',fontsize=12,color=gray)
box(.5,.92,6.45,2.22,'Same-eigenvalue tensor\nExponent kρ; modulus n^(k Re ρ)\nAn off-line repeated coordinate is removed\nby the positive tensor projection.',rust,14)
box(7.35,.92,7.1,2.22,'Reflected pair (k = 2)\nExponent ρ + ρ# = 1 + 2i Im ρ; modulus n\nRetained defect coefficient: −δρ²\nThis pair survives the positive tensor projection.',teal,14)
ax.text(.5,.42,'TWC6 and TWC10: the complete positive receiver keeps exactly Re(ρ₁# + ··· + ρk#) = k/2. Transfer degree = n^k.',fontsize=12,color=gray)
ax.text(.5,.12,'Each statement concerns the actual off-line coordinates when present; the diagram does not assert that such zeros exist.',fontsize=11,color=gray)
fig.savefig(out/'actual_tensor_positive_receiver.png',dpi=160,facecolor=fig.get_facecolor())
fig.savefig(out/'actual_tensor_positive_receiver.svg',facecolor=fig.get_facecolor())
plt.close(fig)
