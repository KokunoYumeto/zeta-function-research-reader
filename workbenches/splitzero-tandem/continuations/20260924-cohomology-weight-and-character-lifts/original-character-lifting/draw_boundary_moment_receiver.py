from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
R=Path(__file__).resolve().parent;F=R/'figures';F.mkdir(exist_ok=True)
plt.rcParams.update({'font.size':11,'font.family':'DejaVu Sans','mathtext.fontset':'dejavusans'})
fig=plt.figure(figsize=(13,7.7),facecolor='white')
ax=fig.add_axes([.075,.43,.44,.43]);ax.set_facecolor('#f8fafc')
x=[-2,-1.5,-1.25,0];y=[2,1,0,0]
ax.scatter(x,y,s=100,color=['#b33b3b','#b33b3b','#2265a3','#2265a3'],zorder=4)
ax.axvspan(-1.5,-1.25,color='#d7c8ed',alpha=.6,zorder=1)
ax.set_xlim(-2.15,.13);ax.set_ylim(-.24,2.75)
ax.set_xticks(x);ax.set_xticklabels([r'$-2$',r'$-3/2$',r'$-5/4$',r'$0$'])
ax.set_yticks([0,1,2]);ax.set_ylabel('Negative directions in $K_{32}(t)$')
ax.set_xlabel('Original physical heat time $t$')
ax.grid(axis='y',alpha=.2)
ax.text(-1.37,2.60,r'$-3/2<t_*<-5/4$',ha='center',fontsize=11)
ax.text(-1.37,2.35,'First PSD boundary within this interval',ha='center',fontsize=8.5)
ax.set_title('Certified samples of the complete root trace',loc='left',pad=16,fontsize=13,fontweight='bold')
for xx,yy,label in zip(x,y,['(30, 2, 0)','(31, 1, 0)','(32, 0, 0)','(32, 0, 0)']):
    ax.annotate(label,(xx,yy),xytext=(0,12),textcoords='offset points',ha='center',fontsize=9)
ax.text(.5,-.30,'Inertias are (positive, negative, zero). No curve is inferred between samples.',transform=ax.transAxes,ha='center',fontsize=8)
ax2=fig.add_axes([.57,.28,.38,.60]);ax2.axis('off')
ax2.text(0,1,'A finite test detects every off-real zero',fontsize=13,fontweight='bold',va='top')
cards=[(.83,r'Actual zero $\zeta\notin\mathbb{R}\ \longmapsto\ \lambda_0=\zeta^{-2}$','Both sign partners and their multiplicities remain.'),(.60,r'$p_N(X)=a(X/\lambda_0)^N L_0(X)+\mathrm{conjugate}$','Interpolation cancels the retained nodes outside the target pair.'),(.37,r'$|\mathrm{tail}|\leq 4B^2V(r/|\lambda_0|)^{2N}$','This bounds the sum over ALL remaining roots.'),(.14,r'$Q_t(p_N)<0$ for a finite $N$',r'Rational coefficients and the full $\Phi$ map preserve the sign.')]
for yy,formula,caption in cards:
    patch=FancyBboxPatch((0,yy-.13),.99,.16,boxstyle='round,pad=.01',facecolor='#eef3f8',edgecolor='#c5d0de',transform=ax2.transAxes);ax2.add_patch(patch)
    ax2.text(.025,yy,formula,fontsize=11,va='center',transform=ax2.transAxes)
    ax2.text(.025,yy-.075,caption,fontsize=8.4,va='center',transform=ax2.transAxes)
    if yy>.2:ax2.annotate('',xy=(.5,yy-.19),xytext=(.5,yy-.14),arrowprops=dict(arrowstyle='->',color='#546274'),xycoords='axes fraction')
fig.text(.075,.18,r'New verified extension: $K_{64}(0)\succ0$',fontsize=16,fontweight='bold',color='#2265a3')
fig.text(.075,.135,r'All 64 pivots are positive; last conditioned pivot $\approx1.21406452042512\times10^{-226}$.',fontsize=10)
fig.text(.075,.087,r'Full criterion: all zeros are real $\Longleftrightarrow\ K_d(t)\succeq0$ for every finite $d$.',fontsize=12)
fig.text(.075,.04,'Proofs: ALM12–24; RWR5–17. Original heat kernel: Rodgers–Tao (1801.05914v5).\nIncoming witness: supplied session report and rational_witness.json; independent Arb reproduction retained.',fontsize=8,color='#4c5662')
for ext in ['png','pdf','svg']:fig.savefig(F/('BOUNDARY_MOMENT_RECEIVER.'+ext),dpi=180)
print('Rendered exact-result diagram and certified-sample plot.')
