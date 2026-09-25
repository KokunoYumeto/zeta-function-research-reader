from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch

base=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'mathtext.fontset':'dejavusans'})
fig=plt.figure(figsize=(15,10.4),facecolor='white')
ax=fig.add_axes([0,0,1,1]); ax.set(xlim=(0,15),ylim=(0,10.4)); ax.axis('off')
navy='#19354a';teal='#176b74';orange='#a75520';muted='#52616c'
def box(x,y,w,h,title,lines,color):
    ax.add_patch(FancyBboxPatch((x,y-.16),w,h+.16,boxstyle='round,pad=0.12,rounding_size=0.12',edgecolor=color,facecolor='#f6f9fa',linewidth=1.5))
    ax.text(x+.16,y+h-.30,title,color=color,weight='bold',fontsize=13,va='top')
    for k,line in enumerate(lines):ax.text(x+.16,y+h-.74-.35*k,line,color=navy,fontsize=12,va='top')
def arrow(a,b,label='',offset=(0,0)):
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=15,color=muted,linewidth=1.4))
    if label:ax.text((a[0]+b[0])/2+offset[0],(a[1]+b[1])/2+offset[1],label,ha='center',va='center',color=muted,fontsize=11)
ax.text(.55,9.95,'The original-zeta receiver of the actual specialization defect',fontsize=20,weight='bold',color=navy)
ax.text(.55,9.5,'Exact maps after complete arithmetic reconstruction; no coordinate or arithmetic operation is assigned to '+r'$\tau$.',fontsize=12,color=muted)
ax.text(.55,8.9,'A. The original source and its faithful energy test',fontsize=15,weight='bold',color=teal)
box(.65,6.9,3.1,1.6,'Full source quotient',[r'$Q=\mathcal{B}/\mathcal{I}$','All nontrivial-zero jets retained',r'$\ker E=N_0$'],teal)
box(5.05,6.9,3.55,1.6,'Actual boundary',[r'$\beta_r=D_r^*JE:Q\longrightarrow H_O$',r'$\ker\beta_r=N_O$',r'$\mathcal{R}=Q/N_O$'],teal)
arrow((3.89,7.68),(4.9,7.68),r'$\beta_r$',(0,.28))
box(9.7,6.9,4.5,1.6,'Exact Gaussian energy',[r'$q_r(\sigma)=(r^\sigma-r^{1-\sigma})^2$',r'$\mathcal{E}_r(t)=\sum_\rho m_\rho q_r(\sigma)e^{2t(\sigma^2-\gamma^2)}$',r'$\mathcal{E}_r(t)=0\ \Longleftrightarrow\ \beta_r=0$'],teal)
arrow((8.74,7.68),(9.55,7.68),'test',(0,.28))
ax.text(.7,6.45,'OZD0, OZD6: the trace has a proved receiving map and exact kernel; this is not a zero seminorm on a chosen quotient.',fontsize=11,color=muted)
ax.text(.55,5.95,'B. Original functional equation: exactly what cancels',fontsize=15,weight='bold',color=orange)
box(.65,3.8,6.35,1.7,'Antisymmetric component',[r'$L_-=\frac{1}{2}\log|\chi(s)|$',r'$\chi(s)=\pi^{s-1/2}\Gamma((1-s)/2)/\Gamma(s/2)$',r'$\frac{1}{4\pi}\int\log|\chi|\,\Delta\phi_-=-\phi_-(1)+\sum_{k\geq1}\phi_-(-2k)$'],orange)
box(8.0,3.8,6.15,1.7,'Symmetric component',[r'$L_+=\frac{1}{2}(\log|\zeta(s)|+\log|\zeta(1-\overline{s})|)$',r'$\phi_+=\frac{1}{2}(\phi+\phi\circ\mathsf{R})$',r'$\mathsf{R}(x,y)=(1-x,y)$'],teal)
arrow((3.8,3.48),(3.8,2.96))
arrow((11.1,3.48),(11.1,2.96))
box(.65,1.6,6.35,1.2,'Cancels the corresponding original divisor terms',[r'$+\phi_-(1)-\sum_{k\geq1}\phi_-(-2k)$','All poles, trivial zeros and signs are retained.'],orange)
box(8.0,1.6,6.15,1.2,'Retains the actual boundary energy',[r'$\mathcal{E}_r(t)=\frac{1}{2\pi}\int L_+\Delta\phi_++\phi_+(1)-\sum_{k\geq1}\phi_+(-2k)$',r'$\phi_+(1)=\frac{(r-1)^2}{2}(e^{2t}+1)$'],teal)
ax.text(.65,.99,r'$\phi(x,y)=\eta(x)q_r(x)e^{2t(x^2-y^2)}$,  '+r'$\eta(1-x)=\eta(x)$,  '+r'$\eta=1$ near $[0,1]$; every integral uses $dx\,dy$.',fontsize=12,color=navy)
ax.text(.65,.55,'OZD1–OZD5 prove global convergence, every cutoff derivative, and the complete original-zeta divisor identity.',fontsize=11,color=muted)
ax.text(.65,.21,'Diagram of proved maps and identities, not a plot of assumed off-line zeros. Original weight-separated vanishing is not asserted.',fontsize=10,color=muted)
fig.savefig(base/'original_divisor_receiver.png',dpi=190)
fig.savefig(base/'original_divisor_receiver.svg')
print(base/'original_divisor_receiver.png')
