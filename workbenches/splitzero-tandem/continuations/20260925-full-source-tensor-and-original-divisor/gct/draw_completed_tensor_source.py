from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

r=Path(__file__).resolve().parent
fig,ax=plt.subplots(figsize=(16,10),facecolor='#f7f9fc')
ax.set(xlim=(0,1),ylim=(0,1)); ax.axis('off')
ink,blue,green='#19324c','#225a9d','#187062'
ax.text(.5,.97,'No additional kernel appears in the completed tensor source',ha='center',fontsize=23,color=ink)
ax.text(.5,.917,'CTS1–4: combine original-source spectral synthesis with the exact tensor map',ha='center',fontsize=15,color=ink)
def box(x,y,w,h,text,color=blue,size=17):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.01',ec=color,fc='white',lw=1.8))
    ax.text(x+w/2,y+h/2,text,ha='center',va='center',fontsize=size,color=color,linespacing=1.5)
def arrow(a,b,text='',dy=.035):
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=18,lw=1.8,color=blue))
    if text:
        vertical = abs(a[0]-b[0]) < .001
        ax.text((a[0]+b[0])/2+(.035 if vertical else 0),(a[1]+b[1])/2+dy,text,
                ha='left' if vertical else 'center',fontsize=16,color=blue)
box(.05,.69,.34,.12,'Original completed source\n'+r'$\mathcal{R}^{\widehat{\otimes}_{\pi} k}$')
box(.65,.69,.30,.12,'Rapid tuple receiver\n'+r'$\mathscr{H}_k$')
arrow((.40,.75),(.64,.75),r'$b_k$')
ax.text(.52,.68,'injective, continuous, dense image',ha='center',fontsize=12,color=green)
box(.05,.43,.34,.12,'Finite tensor of actual value blocks\n'+r'$K_j^{\widehat{\otimes} k}x$',size=16)
box(.65,.43,.30,.12,'Finite coordinate cutoff\nwith the Gaussian factors',size=16)
arrow((.22,.68),(.22,.56),r'$K_j^{\widehat{\otimes} k}$',dy=-.015)
arrow((.80,.68),(.80,.56),'cut off and multiply',dy=-.015)
arrow((.40,.49),(.64,.49),r'$b_k$')
ax.text(.5,.372,r'$K_j^{\widehat{\otimes} k}x\ \longrightarrow\ x$',ha='center',fontsize=24,color=green)
ax.text(.5,.323,'Convergence in the original completed projective topology. No sequence-topology replacement.',ha='center',fontsize=13,color=ink)
box(.05,.112,.90,.145,
    'All continuous positive product-transfer forms on the original source\n'
    r'Common radical $=\ \bigcap_{\mathrm{Re}\,\sum_a\lambda_a=k/2}\ker\varepsilon_{\boldsymbol{\lambda}}$'
    '\n= closure of the noncentered finite tensor blocks.',green,17)
ax.text(.5,.058,'Original Weil pairing retained: on reflected pairs, '+r'$W^{\otimes2}(u\pm v,u\pm v)=\pm2m_{\lambda}^{2}$',ha='center',fontsize=15,color=ink)
ax.text(.5,.006,'Proof: COMPLETED_TENSOR_SOURCE_SYNTHESIS.md, CTS1–5. Inputs: GSP4/7 and TWC2–10; original CC/Deligne provenance retained there.',ha='center',fontsize=10,color=ink)
fig.subplots_adjust(left=.02,right=.98,top=.97,bottom=.025)
for ext in ['png','svg']:
    fig.savefig(r/f'completed_tensor_source.{ext}',dpi=165,bbox_inches='tight',facecolor=fig.get_facecolor())
plt.close(fig)
