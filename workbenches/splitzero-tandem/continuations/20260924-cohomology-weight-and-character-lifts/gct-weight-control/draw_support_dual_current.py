from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

r=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','mathtext.fontset':'dejavusans','font.size':12})
fig=plt.figure(figsize=(16,12),facecolor='#f8fafc')
ax=fig.add_axes([0,0,1,1]);ax.set_xlim(0,16);ax.set_ylim(0,12);ax.axis('off')

def box(x,y,w,h,t,size=16):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.12',facecolor='#e5f1e9',edgecolor='#52637a'))
    ax.text(x+w/2,y+h/2,t,ha='center',va='center',fontsize=size,linespacing=1.6)

ax.text(.6,11.48,'Continuous support duality: the current realizes the maps',fontsize=22,weight='bold',color='#13263d')
ax.text(.6,10.97,'CSD0–CSD12: compactly supported tests, the positive Dirac sign, and both pole restrictions',fontsize=13,color='#46566b')
box(.95,9.30,14.1,1.0,
    r'$\mathscr{D}_c\mathscr{F}=\mathrm{Cone}\left(i_*A^{\prime 2}\ \longrightarrow\ \mathscr{T}_A^{\bullet}\oplus i_*V^{\prime}\right),\quad\mathrm{arrow}=(\delta,-r^{\prime})$'
    +'\n'+r'$\Gamma(U,\mathscr{D}_c\mathscr{F})=\left(\Gamma_c(U,\mathscr{K}^{\bullet})\right)^{\vee}$',18)
ax.text(8,8.87,'Every functional is continuous. The complex is obtained by transposing the actual test resolution. [CSD3–CSD4]',ha='center',fontsize=12)
ax.plot([.6,15.4],[8.5,8.5],color='#adb7c5')

ax.text(.85,8.06,'Local angular current',fontsize=17,weight='bold')
ax.text(8,7.53,r'$h_p=d\arg(z_p)/(2\pi),\quad d(h_p\mu)=\delta_p\mu,\quad d(h_p\mu,-\mu)=(0,r_p^{\prime}\mu)$',ha='center',fontsize=17)
ax.text(8,7.05,r'$i_p^*\mathscr{D}_c\mathscr{F}\simeq[\,A^{\prime}\longrightarrow A^{\prime}\longrightarrow V_p^{\prime}\,],\quad d=(0,r_p^{\prime}),\qquad i_p^!\mathscr{D}_c\mathscr{F}\simeq V_p^{\prime}[0]$',ha='center',fontsize=17)
ax.text(8,6.60,'The first complex has degrees −2, −1, 0. Point support is computed by the disk-to-puncture cone. [CSD5–CSD6]',ha='center',fontsize=12)
ax.plot([.6,15.4],[6.26,6.26],color='#adb7c5')

ax.text(.85,5.81,'Global comparison retains the opposite pole signs',fontsize=17,weight='bold')
box(.95,4.06,14.1,1.17,
    r'$d(\vartheta\mu)=\delta_0\mu-\delta_{\infty}\mu,\qquad\mu\longmapsto(\vartheta\mu;-\mu,+\mu)$'
    +'\n'+r'$d(\vartheta\mu;-\mu,+\mu)=(0;r_+^{\prime}\mu,-r_-^{\prime}\mu)$',18)
ax.text(8,3.59,r'$Q^{\prime}\longrightarrow Q^{\prime}\oplus Q^{\prime}:\ \mu\mapsto(\mu,-\mu),\qquad A^{\prime}\longrightarrow A^{\prime}\oplus A^{\prime}:\ \lambda\mapsto(\lambda,\lambda)$',ha='center',fontsize=16)
ax.text(8,3.15,'These are actual restrictions of the current comparison. They recover the full CDI support signs. [CSD7–CSD8]',ha='center',fontsize=12)
ax.plot([.6,15.4],[2.79,2.79],color='#adb7c5')

ax.text(.85,2.35,'Proper pushforward is adjoint to pullback on tests',fontsize=17,weight='bold')
ax.text(8,1.80,r'$b_{n*}c_{\lambda}=nc_{\lambda},\qquad b_{n*}\vartheta=\vartheta,\qquad b_{n*}\delta_p=\delta_p$',ha='center',fontsize=18)
ax.text(8,1.28,r'$B_n^{\prime}=(nT_n^{\prime},\ T_n^{\prime},\ \rho(n)^{\prime})\quad\mathrm{in\ degrees}\ (-2,-1,0)$',ha='center',fontsize=18)
ax.text(.6,.71,'The trace transpose '+r'$U_n^{\prime}$'+' is a different, explicitly compared map in GTR4–GTR5. All factors remain.',fontsize=12,color='#46566b')
ax.text(.6,.30,'Source setting: Connes–Consani arXiv:0903.2024v3 §5; sphere proof CSP; continuous dual CDI. No coordinate is assigned to '+r'$\tau\langle Z_1;\mathrm{no}\ Z_2\rangle$'+'.',fontsize=10,color='#46566b')
for ext in ('png','svg'):fig.savefig(r/('support_dual_current.'+ext),dpi=160,facecolor=fig.get_facecolor())
plt.close(fig)
