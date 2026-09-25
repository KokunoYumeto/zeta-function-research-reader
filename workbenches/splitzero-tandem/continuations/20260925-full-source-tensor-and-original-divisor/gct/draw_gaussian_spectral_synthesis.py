from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch

root=Path(__file__).resolve().parent
fig=plt.figure(figsize=(16,11),facecolor='#f7f9fc')
ink,blue,green='#15253b','#245dad','#176b54'
fig.text(.5,.965,'Recovering the complete source by Gaussian contour lifts',ha='center',fontsize=23,color=ink)
fig.text(.5,.928,'GSP2–GSP8 · Original quotient topology · Every zero multiplicity retained',ha='center',fontsize=15,color=ink)
ax=fig.add_axes([.06,.43,.40,.43])
ax.set_xlim(-2.8,2.8); ax.set_ylim(-3.5,3.5)
ax.add_patch(Rectangle((0,-3.5),1,7,color='#ddebdc',alpha=.75))
ax.axvline(0,color='#8993a2',lw=.8); ax.axhline(0,color='#8993a2',lw=.8)
for x1,y1,x2,y2 in [(-2,-2.7,2,-2.7),(2,-2.7,2,2.7),(2,2.7,-2,2.7),(-2,2.7,-2,-2.7)]:
    ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle='-|>',mutation_scale=17,lw=2,color=blue))
ax.text(.5,.8,'Complete actual\nnontrivial divisor\nis in this strip',ha='center',va='center',fontsize=13,color=green)
ax.text(0,2.9,r'$+T_j$',ha='center',fontsize=15)
ax.text(0,-3.2,r'$-T_j$',ha='center',fontsize=15)
ax.text(2.15,0,'upward',rotation=90,va='center',fontsize=12,color=blue)
ax.text(-2.35,0,'downward',rotation=90,va='center',fontsize=12,color=blue)
ax.set_xticks([-2,0,1,2]); ax.set_yticks([])
ax.set_xlabel(r'$\mathrm{Re}\,\lambda$ · spectral parameter',fontsize=13)
ax.set_title('Positive contour orientation; heights avoid every zero',fontsize=14,pad=12)
for sp in ax.spines.values(): sp.set_visible(False)
fig.text(.26,.354,'Schematic height scale; no zero locations are plotted.\nThese are coefficient coordinates, not coordinates on the support.',ha='center',fontsize=11,color=ink)

txt=fig.add_axes([.51,.42,.46,.45]);txt.axis('off')
def put(y,s,size=16):txt.text(0,y,s,fontsize=size,color=ink,va='top',linespacing=1.6)
put(.99,r'$g_t(\lambda)=e^{t\lambda^2}$',20)
put(.86,r'$K_j=\frac{1}{2\pi i}\int_{\Gamma_j}g_{1/j}(\lambda)(\lambda-L)^{-1}\,d\lambda$',18)
put(.69,r'$K_j\longrightarrow 1_{\mathcal{Q}}$',23)
put(.57,'Convergence is uniform on bounded source sets.\nEach contour retains all jets of every enclosed zero.',14)
put(.39,r'$\overline{\bigoplus_\rho\mathcal{Q}_\rho}=\mathcal{Q}$',21)
put(.24,r'$\overline{J_L+J_O}=\mathcal{B}$',21)
put(.10,'The reconstruction quotient has zero Hausdorff quotient;\nits algebraic classes are still retained.',13)

bot=fig.add_axes([.055,.075,.89,.25]);bot.axis('off')
bot.add_patch(Rectangle((0,0),1,1,facecolor='white',edgecolor='#cdd7e2'))
bot.text(.025,.87,'The actual lift and the exact equivariance defect',fontsize=17,color=ink)
for x,label in [(.08,r'$\mathcal{Q}$'),(.28,r'$\mathcal{B}$'),(.48,r'$\mathcal{Q}$')]:
    bot.text(x,.62,label,fontsize=24,color=blue,ha='center',va='center')
for x1,x2,label in [(.12,.24,r'$\mathcal{L}_t$'),(.32,.44,r'$q$')]:
    bot.add_patch(FancyArrowPatch((x1,.62),(x2,.62),arrowstyle='-|>',mutation_scale=15,lw=1.7,color=blue))
    bot.text((x1+x2)/2,.73,label,fontsize=15,color=blue,ha='center')
bot.text(.65,.61,r'$q\mathcal{L}_t=m_{g_t}$',fontsize=22,color=green)
bot.text(.055,.29,r'$\mathfrak{a}_t(h;x)=\mathcal{L}_t(hx)-h\mathcal{L}_t x\ \in\ \mathcal{I}$',fontsize=18,color=ink)
bot.text(.62,.29,r'$\mathfrak{a}_t(s;x)=-F_0\,\lambda_t(x)$',fontsize=18,color=ink)
bot.text(.025,.065,'Full original factor: '+r'$F_0(s)=\frac{s(s-1)}{8}\pi^{-s/2}\Gamma(s/2)\zeta(s)$'+'  ·  GSP1.5–1.8 and GSP8.4–8.8',fontsize=13,color=ink)
fig.text(.5,.025,'Proof: GAUSSIAN_SPECTRAL_SYNTHESIS.md. Inputs: RZ3–7, S3, GAP1–2; human-source provenance retained there.',ha='center',fontsize=11,color=ink)
for ext in ['png','svg']:
    fig.savefig(root/f'gaussian_spectral_synthesis.{ext}',dpi=170,bbox_inches='tight',facecolor=fig.get_facecolor())
plt.close(fig)
