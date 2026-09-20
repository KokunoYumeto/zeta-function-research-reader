"""Reproduce the exact precision-transfer diagram; no arithmetic samples."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

HERE=Path(__file__).resolve().parent
OUT=HERE/'figures'
OUT.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'svg.fonttype':'none'})
fig=plt.figure(figsize=(15,10),facecolor='#f7f8fa')
ax=fig.add_axes([0,0,1,1]);ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')
ax.text(.045,.951,'ARITHMETIC MOMENTS → COMPLEX CURRENT',fontsize=23,weight='bold',color='#182f46')
ax.text(.045,.909,'Exact finite precision transfer · original class, action, mass and quotient retained',fontsize=13,color='#35546b')
boxes=[
(.045,.57,'1  Actual source measure',[
 r'$h=d_\nu\min_b\{g_{n_b}\}>0,\quad H\preceq UI$',
 r'$g_t=\det L_t/(\mathrm{tr}\,L_t)^t$',
 'The density floor and mass are retained.']),
(.37,.57,'2  Scalar moment precision',[
 r'$\|H-\widehat H\|\leq d\varepsilon$',
 r'$\theta=d\varepsilon/h\leq 1/4$',
 r'$H_{\rm lo}=\widehat H-d\varepsilon I$']),
(.695,.57,'3  Proved positive bracket',[
 r'$(h/2)I\preceq H_{\rm lo}\preceq H\preceq UI$',
 r'$(1-2\theta)H\preceq H_{\rm lo}$',
 'No midpoint positivity is assumed.']),
(.045,.235,'4  Same quotient fibres',[
 r'$G_0=(JH_{\rm lo}^{-1}J^*)^{-1}$',
 r'$G=(JH^{-1}J^*)^{-1}$',
 r'$G_0\preceq G\preceq(1-2\theta)^{-1}G_0$']),
(.37,.235,'5  Same projected current',[
 r'$K=\ker\Lambda,\quad A=M_S,\quad x\ \mathrm{fixed}$',
 r'$|z-z_0|,\ |w-w_0|\leq6C\theta$',
 r'$|z_0|,\ |w_0|\leq C/2$']),
(.695,.235,'6  Complete complex product',[
 r'$|\overline{z} w-\overline{z_0}w_0|$',
 r'$\quad\leq6C^2\theta+36C^2\theta^2$',
 r'$\quad\leq\mathbf{15}\,C^2\theta$'])]
for x,y,title,lines in boxes:
    ax.add_patch(FancyBboxPatch((x,y),.26,.25,boxstyle='round,pad=0.016,rounding_size=0.012',
                 facecolor='white',edgecolor='#a9bdcc',linewidth=1.5))
    ax.text(x+.004,y+.208,title,fontsize=13,weight='bold',color='#183e5d')
    for j,line in enumerate(lines): ax.text(x+.004,y+.149-.058*j,line,fontsize=11.5,color='#182f46')
for start,end in [((.313,.69),(.348,.69)),((.638,.69),(.673,.69)),
                  ((.825,.545),(.175,.51)),((.175,.51),(.175,.508)),
                  ((.313,.36),(.348,.36)),((.638,.36),(.673,.36))]:
    if start==(.825,.545):
        ax.plot([.825,.825,.175],[.545,.518,.518],color='#147e83',linewidth=2)
    elif start==(.175,.51):
        ax.add_patch(FancyArrowPatch((.175,.518),(.175,.508),arrowstyle='-|>',mutation_scale=17,color='#147e83',linewidth=2))
    else: ax.add_patch(FancyArrowPatch(start,end,arrowstyle='-|>',mutation_scale=17,color='#147e83',linewidth=2))
ax.text(.045,.16,r'$W=(JJ^*)^{-1},\quad\overline{M}=2\sqrt{U/h}\,\|A\|_W,\quad C=\overline{M}\,U\|x\|_W^2$',fontsize=15,color='#182f46')
ax.text(.045,.11,'J includes the full physical unit and complex coordinate map. P and P₀ use G and G₀ on the same K.',fontsize=11.8,color='#35546b')
ax.text(.045,.074,'Full proofs: native precision; projection PD4–19; composition MC1–16. Human-source details in the caption.',fontsize=11,color='#35546b')
ax.text(.045,.039,'These are proved error bounds, not evaluated arithmetic moments, a growing-degree sign, or an RH conclusion.',fontsize=11,color='#35546b')
for ext in ('svg','png'):fig.savefig(OUT/f'moment_current_transfer.{ext}',dpi=140,facecolor=fig.get_facecolor())
print('Generated SVG and PNG from the exact precision-transfer formulas.')
