from pathlib import Path
import re
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

ROOT=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','mathtext.fontset':'dejavusans'})
fig,ax=plt.subplots(figsize=(15,14))
ax.set(xlim=(0,15),ylim=(0,14)); ax.axis('off')
fig.patch.set_facecolor('#f7f9fc'); ax.set_facecolor('#f7f9fc')

def box(x,y,w,h,s,c='#e6eef9',size=12.5):
    s=re.sub(r'\\mathcal ([A-Z])',lambda m:r'\mathcal{'+m.group(1)+'}',s)
    s=re.sub(r'\\mathbb ([A-Z])',lambda m:r'\mathbb{'+m.group(1)+'}',s)
    s=s.replace(r'\frac1m',r'\frac{1}{m}').replace(r'\frac{e^{\sigma t}}t',r'\frac{e^{\sigma t}}{t}')
    ax.add_patch(FancyBboxPatch((x-w/2,y-h/2),w,h,boxstyle='round,pad=.08',
                              facecolor=c,edgecolor='#425970',linewidth=1.2))
    ax.text(x,y,s,ha='center',va='center',fontsize=size,linespacing=1.4)
def arr(x,y,X,Y):
    ax.annotate('',xy=(X,Y),xytext=(x,y),arrowprops=dict(arrowstyle='->',lw=1.7,color='#344c63'))

ax.text(.35,13.55,'Deligne’s exact weight control and the arithmetic return map',fontsize=20,weight='bold')
ax.text(.35,13.08,'Finite-field theorem above; the proved original-zeta receiving map below. Every label names its proof.',fontsize=11.5)

box(3.78,11.6,6.55,1.9,
    'DP1–DP6: determinant weights → pointwise purity\n'
    r'$\mathcal F^{\otimes 2k}:\ (\operatorname{Tr}F_x^m)^{2k}\geq0$'+'\n'
    r'$w_{N(x)}(\alpha)\leq r+1/k\quad(\mathrm{every}\ k)$'+'\n'
    'Exterior powers + exact determinant sum → equality')
box(11.2,11.6,6.5,1.9,
    'DLM3, DLM10: primitive tensor square and dual\n'
    r'$P_{-j}^{\otimes2}(-j)\ \longrightarrow\ P_0(V^{\otimes2})$'+'\n'
    r'$|\alpha^2Q^j|\leq Q^\beta,\quad |\alpha^{-1}Q^{-j}|\leq Q^{(-\beta-j)/2}$'+'\n'
    r'$|\alpha|=Q^{(\beta-j)/2},\quad Q=N(s)$',c='#e5f2eb',size=12)
arr(3.78,10.57,3.78,9.88);arr(11.2,10.57,11.2,9.88)
box(7.5,9.1,13.9,1.4,
    'DW3–DW6: the pencil’s boundary cycles constrain every nonconstant constituent\n'
    r'$\mathcal G=\mathcal F\boxtimes\mathcal F\ (\mathrm{weight}\ 2\beta),\quad'
    r'\gamma\in 2\beta+\mathbb Z,\quad\gamma<2\beta+2\ \Longrightarrow\ \gamma\leq2\beta+1$'+'\n'
    'The strict inequality comes from DB/DBC: all-return positivity and boundary nonvanishing.',c='#fff0d8')
arr(7.5,8.3,7.5,7.85)
box(7.5,6.98,13.9,1.72,
    'DW7–DW8: product, complete Leray terms, and exact duality\n'
    r'$H_c^1\otimes H_c^1\hookrightarrow H_c^2(\widetilde V),\quad'
    r'w_q(\alpha)\leq\beta+1+2^{-k}\quad(\mathrm{every}\ k)$'+'\n'
    r'$V_{\rm mid}=\operatorname{im}(H_c^1\to H^1):\quad'
    r'\mathcal F^\vee(1)\ \Longrightarrow\ w_q(\lambda)\geq\beta+1$'+'\n'
    r'$|\lambda|=q^{(\beta+1)/2}\quad\mathrm{on}\ V_{\rm mid}$',c='#e5f2eb')
ax.text(7.5,5.85,'Hc⁰, Hc², every Tate factor, boundary sign and exceptional blowup term remain in the proofs.',ha='center',fontsize=10.7)
ax.plot([.45,14.55],[5.55,5.55],color='#8293a6',lw=1)
ax.text(.5,5.2,'DR1–DR3: after the complete source has supplied its arithmetic and norms',fontsize=13.5,weight='bold')
box(3.18,4.04,5.35,1.55,
    r'$A=\operatorname{End}(L),\quad N(a)=|L/aL|$'+'\n'
    r'$\mathcal D=\delta_0+\sum_{n\geq2}\delta_{\log n}$'+'\n'
    'Each branch uses its own recovered counter.',size=11.7)
box(10.7,4.04,7.45,1.55,
    r'$\mathcal R=\log_*\mathcal D=\sum_{p,m\geq1}\frac1m\delta_{m\log p}$'+'\n'
    r'$\mu_\sigma=t e^{-\sigma t}\mathcal R,\quad'
    r'\mathcal R=\frac{e^{\sigma t}}t\mu_\sigma\ (t>0)$'+'\n'
    r'$\mathcal D=\exp_*\mathcal R\quad(\mathrm{includes}\ \delta_0)$',size=13)
arr(5.97,4.04,6.85,4.04)
arr(10.7,3.19,10.7,2.67)
box(7.5,1.93,13.9,1.28,
    r'$\widehat\mu_\sigma(u)=-\zeta^{\prime}(\sigma+iu)/\zeta(\sigma+iu),\quad\sigma>1$'+'\n'
    'Deligne §2.1.9 uses precisely this all-prime-power measure. DR4 proves its boundary nonvanishing.',c='#eee8f8',size=14)
ax.text(7.5,.84,r'$\tau\langle Z_1;\mathrm{no}\ Z_2\rangle$ stays the support: no coordinate, metric, addition or numeric zero is placed there.',ha='center',fontsize=11)
ax.text(7.5,.41,'This diagram does not identify the two cohomology theories. Source: Deligne, Weil II §§1.3–3.3; current proof locators shown.',ha='center',fontsize=10)
for ext in ('png','svg'):
    fig.savefig(ROOT/f'deligne_weight_mechanism.{ext}',dpi=170,bbox_inches='tight')
plt.close(fig)
print(str(ROOT/'deligne_weight_mechanism.png'))
