"""Exact labelled diagram of the escaping cover and its retained trace form."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

root=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11})
fig,axs=plt.subplots(2,2,figsize=(14,10))
fig.patch.set_facecolor('#f9fafc')
for ax in axs.ravel(): ax.set_facecolor('#f9fafc')
r=np.linspace(-.7,.7,501)
axs[0,0].plot(-r*r,r,lw=3,color='#147d92')
axs[0,0].scatter([0],[0],s=75,color='#bc4749',zorder=4)
axs[0,0].set_xlim(-.52,.13);axs[0,0].set_ylim(-.76,.76)
axs[0,0].axvline(0,color='#9ca3af',lw=1);axs[0,0].axhline(0,color='#9ca3af',lw=1)
axs[0,0].set_xlabel(r'Original target $a$');axs[0,0].set_ylabel(r'Inverse root $r$')
axs[0,0].set_title(r'Two escaping sheets: $a=-r^2$',loc='left',fontweight='bold')
axs[0,0].text(.04,.94,r'$[X:Y:W:T]=[1:-6r^2:-52r^3:-2r]$',transform=axs[0,0].transAxes,va='top',fontsize=10,bbox={'facecolor':'#f9fafc','edgecolor':'none','alpha':.96,'pad':4})
axs[0,0].annotate(r'$\mathbb{C}[r]/(r^2)$',xy=(0,0),xytext=(-.37,.02),arrowprops={'arrowstyle':'->','color':'#374151'},color='#bc4749',fontsize=13)
a=np.linspace(-.6,.6,400)
axs[0,1].plot(a,2+0*a,color='#64748b',lw=2,label=r'Constant direction: $2$')
axs[0,1].plot(a,-2*a,color='#147d92',lw=3,label=r'Root direction: $-2a$')
axs[0,1].axvline(0,color='#9ca3af',lw=1);axs[0,1].axhline(0,color='#9ca3af',lw=1)
axs[0,1].axvspan(0,.6,color='#bc4749',alpha=.06)
axs[0,1].set_ylim(-1.4,2.7);axs[0,1].set_xlim(-.6,.6)
axs[0,1].set_xlabel(r'Original target $a$');axs[0,1].set_ylabel('Trace Gram eigenvalues in (1,r)')
axs[0,1].set_title('Trace-null at collision; signs survive nearby',loc='left',fontweight='bold')
axs[0,1].legend(loc='upper right',frameon=False,fontsize=10)
axs[0,1].text(-.53,-1.13,'Positive definite',color='#147d92');axs[0,1].text(.13,-1.13,'One negative direction',color='#bc4749')
for ax in axs[1]: ax.axis('off')
axs[1,0].set_title('Exact pullback to the earlier deformation',loc='left',fontweight='bold',pad=15)
lines=[
 (r'$r^2+a=0$',.88,18),
 (r'$a=-\lambda^2/4,\quad r=z-\lambda/2$',.71,15),
 (r'$z^2-\lambda z=0$',.53,18),
 (r'$\lambda=a_{\rm obs}t:\quad r^2=a_{\rm obs}^2t^2/4$',.34,14),
 ('Modulo t², the family is constant dual numbers.',.16,11),
 ('The class r remains nonzero; its square is zero.',.06,11)]
for text,y,size in lines: axs[1,0].text(.04,y,text,fontsize=size,va='center')
axs[1,0].annotate('',xy=(.43,.58),xytext=(.43,.63),arrowprops={'arrowstyle':'->','lw':1.5})
axs[1,1].set_title('Triple collision: keep the vanished class',loc='left',fontweight='bold',pad=15)
for text,y,size in [
 (r'$A_0=\mathbb{C}[u,v]/(u^2,uv,v^2)$',.88,15),
 (r'$j_0:A_0\longrightarrow B_0=\mathbb{C}[z]/(z^3)$',.67,14),
 (r'$u\longmapsto z^2,\qquad v\longmapsto0$',.47,15),
 (r'$\ker j_0=\mathbb{C}v\ne0$',.27,16),
 ('The image is dual numbers; the kernel is retained.',.09,11)]:
 axs[1,1].text(.025,y,text,fontsize=size,va='center',color='#bc4749' if 'ker' in text else '#172331')
fig.suptitle('The actual escaping fibre produces an infinitesimal boundary',x=.065,ha='left',fontsize=19,fontweight='bold')
fig.text(.065,.035,'Proof: ESCAPING_FIBRE_INFINITESIMAL_DERIVATION, EFI7–15, EFI23–40 and the observed-family pullback.\nOriginal map: Tao (21 July 2026), displayed polynomial; programme source 26_incompressible_fibre_heat.tex.\nThe plotted trace is the finite cover trace. Its equality with the arithmetic Weil pairing is not asserted.',fontsize=10,va='bottom',color='#374151')
fig.subplots_adjust(left=.07,right=.98,top=.89,bottom=.14,hspace=.4,wspace=.25)
out=root/'figures';out.mkdir(exist_ok=True)
fig.savefig(out/'25_escaping_trace.png',dpi=170)
fig.savefig(out/'25_escaping_trace.svg')
print('Rendered figure 25.')
