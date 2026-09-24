from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

r=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','mathtext.fontset':'dejavusans'})
fig=plt.figure(figsize=(17,13),facecolor='#f8fafc')
ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,17); ax.set_ylim(0,13); ax.axis('off')
def panel(y,height,title,text,size=19,color='#e6eff9'):
    ax.add_patch(FancyBboxPatch((.7,y),15.6,height,boxstyle='round,pad=.08',facecolor=color,edgecolor='#7a8ca2'))
    ax.text(1,y+height-.34,title,fontsize=15,weight='bold',va='center')
    ax.text(8.5,y+(height-.65)/2,text,fontsize=size,ha='center',va='center',linespacing=1.45)

ax.text(.7,12.55,'From separated families to the complete normal source',fontsize=22,weight='bold')
ax.text(.7,12.1,'The existing global separator acts on the actual full coefficient modules; no finite-block limit is assumed.',fontsize=12)
panel(9.4,2.2,'GSL supplies a continuous multiplier with all original zero jets retained',
      r'$E_+(\lambda)=1-E(\lambda-1),\qquad E_+|_{\mathcal{Q}}=1,\qquad E_+|_{\mathcal{Q}_+}=0$'
      +'\n'+r'$\mathcal{Q}=\mathcal{B}/\mathcal{I},\qquad\mathcal{Q}_+=\mathcal{B}/\mathcal{I}_+$'
      +'\n'+r'$F_0(\lambda-1)=\frac{(\lambda-1)(\lambda-2)}{8}\pi^{-(\lambda-1)/2}\Gamma((\lambda-1)/2)\zeta(\lambda-1)$',size=18)
panel(6.9,2.1,'The full normal row and its actual continuous reverse map',
      r'$0\longrightarrow\mathcal{I}_+\ \overset{\iota}{\longrightarrow}\ \mathcal{B}\longrightarrow\mathcal{Q}_+\longrightarrow0$'
      +'\n'+r'$m_{E_+}:\mathcal{B}\longrightarrow\mathcal{I}_+,\qquad F\longmapsto E_+F$'
      +'\n'+r'$\iota m_{E_+}=E_+|_{\mathcal{B}},\qquad m_{E_+}\iota=E_+|_{\mathcal{I}_+}$',color='#e1f2e9')
panel(4.05,2.47,'After the derived Hom functor from the complete original quotient',
      r'$\mathrm{RHom}_{M}(\mathcal{Q},\mathcal{I}_+)'
      r'\ \overset{\iota_*}{\longrightarrow}\ \mathrm{RHom}_{M}(\mathcal{Q},\mathcal{B})$'
      +'\n'+r'$\text{inverse up to homotopy: }(m_{E_+})_*;\qquad\delta S+S\delta=E_+-1$'
      +'\n'+r'$\mathrm{Ext}_{M}^{k}(\mathcal{Q},\mathcal{Q}_+)=0='
      r'\mathrm{Ext}_{M}^{k}(\mathcal{Q}_+,\mathcal{Q}),\qquad k\geq0$',size=18)
panel(2.0,1.62,'The original normal coordinate and source map retain their factors',
      r'$\lambda=s+1,\qquad E_+(s+1)=1-E(s)$'
      +'\n'+r'$a\longmapsto\frac{u^{-1/2}}{\pi}\int_{\mathbb{R}}'
      r'(1-E(1/2+it))\,\Theta a(1/2+it)\,u^{-it}\,dt\quad\in J(-1)$',size=18)
ax.text(.7,1.54,r'$M$ consists of entire multipliers with polynomial growth on each closed vertical strip.',fontsize=12)
ax.text(.7,1.15,'The reverse map is not a literal inverse on the source; the displayed homotopy proves its derived inverse.',fontsize=12)
ax.text(.7,.76,r'All endpoint values remain. No multiplier action, addition or metric is assigned to $\tau\langle Z_1;\mathrm{no}\ Z_2\rangle$.',fontsize=11)
ax.text(.7,.36,'Proof: GMS3–GMS5, GMS8; homotopy GMS4.7–4.9. Inputs: GSL4–6, CLP12–13. Human settings: CC §5; Deligne §3.6.',fontsize=10.5,color='#43546b')
for ext in ('png','svg'):
    fig.savefig(r/('global_multiplier_separation.'+ext),dpi=150,facecolor=fig.get_facecolor())
plt.close(fig)
