"""Original metric and trace forms at the collision, with exact scale b retained."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
root=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12})
fig,axs=plt.subplots(1,2,figsize=(14,6.5))
fig.patch.set_facecolor('#f9fafc')
for ax in axs: ax.set_facecolor('#f9fafc')
theta=np.linspace(-np.pi/2,np.pi/2,401)
axs[0].plot(theta,np.sin(2*theta),color='#147d92',lw=3)
axs[0].axhline(0,color='#9ca3af',lw=1)
axs[0].scatter([-np.pi/4,np.pi/4],[-1,1],color=['#bc4749','#147d92'],s=70,zorder=4)
axs[0].set_xticks([-np.pi/2,-np.pi/4,0,np.pi/4,np.pi/2],[r'$-\pi/2$',r'$-\pi/4$','0',r'$\pi/4$',r'$\pi/2$'])
axs[0].set_ylim(-1.3,1.3)
axs[0].set_xlabel(r'$x_\theta=\cos\theta\,g+i\sin\theta\,h$; parameter $\theta$')
axs[0].set_ylabel(r'$x_\theta^*W_*x_\theta/b=\sin(2\theta)$')
axs[0].set_title(r'Current survives: $W_*=i(N-N^*)$',loc='left',fontweight='bold',pad=18)
axs[0].annotate(r'$-b$',(-np.pi/4,-1),xytext=(12,-14),textcoords='offset points',color='#bc4749')
axs[0].annotate(r'$+b$',(np.pi/4,1),xytext=(12,5),textcoords='offset points',color='#147d92')
axs[1].axis('off');axs[1].set_title('The same infinitesimal has distinct exact receivers',loc='left',fontweight='bold',pad=18)
rows=[(r'$N=bhg^*,\quad N^2=0,\quad b=\varepsilon\sqrt{\Delta}>0$',.90,15),
 (r'$\mathrm{tr}(N^k)=0\quad(k\geq1)$',.71,16),
 (r'$\|N\|_{\mathrm{HS}}^2=b^2$',.54,18),
 (r'$\mathrm{Tr}_{\mathrm{alg}}((c_0+c_1r)^*(c_0+c_1r))=2|c_0|^2$',.34,13),
 (r'$\|c_0 I_S+c_1N\|_{\mathrm{HS}}^2=2|c_0|^2+b^2|c_1|^2$',.15,13)]
for t,y,s in rows:axs[1].text(.025,y,t,fontsize=s,va='center')
fig.suptitle('What vanishes, and what the original metric still measures',x=.07,ha='left',fontsize=19,fontweight='bold')
fig.text(.07,.075,'The plot uses the original orthonormal pair g,h; the vertical axis divides by the retained positive constant b.\nThe algebra involution fixes the generator, while its matrix image is not self-adjoint: F − F* = −iW.\nProof: INFINITESIMAL_SUPPORT_POSITIVITY_DERIVATION, ISP5–17 and the trace/Hilbert–Schmidt comparison.',fontsize=10,color='#374151')
fig.subplots_adjust(left=.075,right=.985,top=.81,bottom=.25,wspace=.26)
out=root/'figures';out.mkdir(exist_ok=True)
fig.savefig(out/'26_infinitesimal_forms.png',dpi=170)
fig.savefig(out/'26_infinitesimal_forms.svg')
print('Rendered figure 26.')
