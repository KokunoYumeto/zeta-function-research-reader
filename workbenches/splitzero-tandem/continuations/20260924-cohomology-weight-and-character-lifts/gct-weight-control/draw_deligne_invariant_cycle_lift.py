from pathlib import Path
import re
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

root=Path(__file__).resolve().parent
fig,ax=plt.subplots(figsize=(15.8,10.5))
fig.patch.set_facecolor('#fafbfd')
ax.set(xlim=(0,15.8),ylim=(0,10.5)); ax.axis('off')

def box(x,y,w,h,label,color='#e8f2f8',size=14):
    ax.add_patch(FancyBboxPatch((x-w/2,y-h/2),w,h,boxstyle='round,pad=.06',
                 facecolor=color,edgecolor='#435970',linewidth=1.4))
    ax.text(x,y,label,ha='center',va='center',fontsize=size)

def arrow(x,y,X,Y,label='',dx=0,dy=0):
    ax.annotate('',xy=(X,Y),xytext=(x,y),arrowprops=dict(arrowstyle='->',lw=1.6,color='#435970'))
    if label:
        ax.text((x+X)/2+dx,(y+Y)/2+dy,label,ha='center',va='center',fontsize=13,
                bbox=dict(facecolor='#fafbfd',edgecolor='none',pad=2))

ax.text(7.9,10.08,'Deligne’s invariant-cycle quotient and its exact lift',ha='center',fontsize=22,weight='bold')
ax.text(7.9,9.55,'A proper family over the stated henselian trait; smooth total model and smooth geometric generic fibre.',ha='center',fontsize=11.8)
ax.text(7.9,9.18,r'$\mathbb{Q}_{\ell}$ coefficients; $N=\dim X^{\prime}$ is the total-model dimension; $I=\mathrm{Gal}(\bar{\eta}/\eta)$.',ha='center',fontsize=11.8)

box(7.9,7.86,7.25,1.22,r'$O=H^{2N-i-1}(X_s)^{\vee}(-N)$'+'\n'+r'weights $\geq i+1$', '#fff0d9')
box(2.43,5.62,4.35,1.38,r'$K=H^{i-1}(X_{\bar{\eta}})_I(-1)$'+'\n'+r'weights $\geq i+1$', '#fff0d9',13.5)
box(7.9,5.62,3.95,1.38,r'$B=H^i(X_{\eta})$'+'\n'+'all mixed weights retained', '#e8f2f8',13.5)
box(13.37,5.62,4.35,1.38,r'$C=H^i(X_{\bar{\eta}})^I$'+'\n'+r'weights $\leq i$', '#e6f3ec',13.5)
arrow(4.68,5.62,5.85,5.62)
arrow(9.95,5.62,11.14,5.62,r'$q$',dy=.32)
ax.text(4.0,4.43,r'$0\longrightarrow K\longrightarrow B\longrightarrow C\longrightarrow0$ is exact.',ha='center',fontsize=12)
arrow(7.9,6.39,7.9,7.16,r'$\partial$',dx=.32)
box(7.9,3.42,6.05,1.15,r'$A=H^i(X_s)$'+'\n'+r'$\mathrm{im}(A\to B)=\ker\partial$', '#e6f3ec',14)
arrow(7.9,4.06,7.9,4.85)
arrow(11.0,3.67,13.34,4.85,r'$\mathrm{sp}^{*}$',dx=.27,dy=-.13)

box(7.9,1.85,14.65,1.15,r'$q:W_iB\longrightarrow C$ is an isomorphism; '+r'$\partial(W_iB)=0$'+'\n'+
    r'Each invariant class has a unique lift in $W_iB$; its lift in $A$ is determined only modulo $\ker(\mathrm{sp}^{*})$.', '#eeeafa',13.7)
ax.text(7.9,.85,r'$\mathrm{coker}(\mathrm{sp}^{*})\simeq\mathrm{im}(\partial)/\partial K=0$. The full groups $K$ and $O$ have not been discarded.',ha='center',fontsize=13)
ax.text(7.9,.34,'Proof: DC. Human source: Deligne, Weil II §3.6, pp.212–214. This diagram does not identify the programme’s analytic receiver with this cohomology.',ha='center',fontsize=10.6)
for ext in ('png','svg'):
    fig.savefig(root/f'deligne_invariant_cycle_lift.{ext}',dpi=170,bbox_inches='tight')
plt.close(fig)
