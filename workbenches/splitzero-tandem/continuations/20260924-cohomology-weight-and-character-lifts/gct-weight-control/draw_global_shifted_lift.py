from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

root = Path(__file__).resolve().parent
fig = plt.figure(figsize=(13.6, 11.6), dpi=180, facecolor='#f4f6fa')
ax = fig.add_axes([.04, .035, .92, .93])
ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis('off')

def text(x, y, s, size=14, color='#192539', weight='normal', ha='left'):
    ax.text(x, y, s, fontsize=size, color=color, weight=weight, ha=ha, va='center')

def box(y, h, title, color):
    ax.add_patch(FancyBboxPatch((1,y),98,h,boxstyle='round,pad=.6,rounding_size=1',
                              facecolor='white',edgecolor=color,lw=1.4))
    text(4,y+h-3,title,17,color,'bold')

text(2,98,'A continuous lift on the whole original source',23,weight='bold')
text(2,94,r'Support retained: $\tau\langle Z_1;\mathrm{no}\ Z_2\rangle$.  Coordinates below belong to coefficient functions.',11)
box(64,26,'1. Two full zero divisors, with every multiplicity', '#24558a')
text(5,80,r'Original: $\rho$,  $0<\operatorname{Re}\rho<1$',16,'#24558a')
text(54,80,r'Translated: $\rho+1$,  $1<\operatorname{Re}(\rho+1)<2$',14,'#835324')
text(5,74,r'$T_a|_\rho=a^\rho\exp((\log a)N_\rho)$',17,'#24558a')
text(54,74,r'$T_a|_{\rho+1}=a^{\rho+1}\exp((\log a)N_\rho)$',15,'#835324')
text(5,68.4,r'Source modulus weights: $(0,2)$',15,'#24558a')
text(54,68.4,r'Kernel modulus weights: $(2,4)$',15,'#835324')
text(5,65.3,r'$N_\rho^{m_\rho}=0$; full exponential retained. Modulus weights use $a>1$. Bands describe the full spectra.',10)

box(34,27,'2. The exact quotient map and its constructed inverse', '#286855')
text(5,52,r'$0\longrightarrow\mathcal{Q}(-1)\longrightarrow\mathcal{B}/(\mathcal{I}\cap\mathcal{I}_+)'
             r'\longrightarrow\mathcal{Q}\longrightarrow0$',20)
text(5,46,r'$\Phi[F]=([F]_{\mathcal{I}},[F]_{\mathcal{I}_+})$',17)
text(5,40.8,r'$\Phi^{-1}([f],[g])=[E_+f+(1-E_+)g]_{\mathcal{I}\cap\mathcal{I}_+}$',17,'#286855')
text(5,36.3,r'$E_+=1$ to every jet at $\rho$; $E_+=0$ to every jet at $\rho+1$.',13)

box(5,26,'3. Continuous source formula, with original factors', '#744978')
text(5,23,r'$F_0(s)=\dfrac{s(s-1)}{8}\pi^{-s/2}\Gamma(s/2)\zeta(s),\qquad F_{-1}(s)=F_0(s-1)$',17)
text(5,16.7,r'$k_{\mathrm{high}}(u)=\dfrac{1}{2\pi}\int_{\mathbb{R}}E_+(\frac{1}{2}+it)\,\mathcal{M}k(\frac{1}{2}+it)\,u^{-it}\,dt$',17)
text(5,10.7,'The separator is an entire multiplier, constructed by a convergent Gaussian Cauchy integral.',12)
text(5,7.2,'GSL3–GSL8 prove the estimates, full range, equivariance and unique continuous linear section.',11)
text(2,1.8,'Proof: GLOBAL_SHIFTED_ZETA_LIFT.md. Deligne comparison: Weil II §3.6, DC5–DC9. No RH conclusion is drawn.',10)
fig.savefig(root/'global_shifted_lift.png',bbox_inches='tight',facecolor=fig.get_facecolor())
fig.savefig(root/'global_shifted_lift.svg',bbox_inches='tight',facecolor=fig.get_facecolor())
plt.close(fig)
print(root/'global_shifted_lift.png')
