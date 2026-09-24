"""Render the exact GTZ and CGT maps; no sampled mathematics."""
from pathlib import Path
import re
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

base=Path(__file__).resolve().parent
plt.rcParams.update({"font.family":"DejaVu Sans","mathtext.fontset":"stix",
                     "font.size":14,"svg.fonttype":"none"})
fig=plt.figure(figsize=(17,11.6),facecolor="#fcfbf7")
ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,1); ax.set_ylim(0,1); ax.axis("off")
ink="#183844"; blue="#17678d"; green="#25735f"; orange="#a65a20"
ax.text(.05,.96,"The geometric Tate factor in the global zeta lift",
        fontsize=25,weight="bold",color=ink)
ax.text(.05,.922,"All arithmetic is already reconstructed.  The supporting datum "
        r"$\tau\langle Z_1;\mathrm{no}\ Z_2\rangle$ receives no new operation.",
        fontsize=14,color=ink)
def panel(x,y,w,h):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.012",
                facecolor="white",edgecolor="#becbd0",linewidth=1.2))
def arrow(a,b,label="",dy=.02,color=ink):
    ax.annotate("",xy=b,xytext=a,arrowprops={"arrowstyle":"->","lw":1.8,"color":color})
    if label: ax.text((a[0]+b[0])/2,(a[1]+b[1])/2+dy,label,
                     ha="center",va="center",color=color,fontsize=15)
panel(.045,.48,.91,.405)
ax.text(.066,.85,"A. The entire continuous lifting row",fontsize=18,weight="bold",color=blue)
xs=[.14,.47,.80]
ys=[.762,.615]
for y in ys:
    ax.text(.072,y,r"$0$",ha="center",va="center",fontsize=21)
    ax.text(.928,y,r"$0$",ha="center",va="center",fontsize=21)
    arrow((.088,y),(.107,y));arrow((.872,y),(.91,y))
ax.text(xs[0],ys[0],r"$\mathcal Q(-1)$",ha="center",va="center",fontsize=24)
ax.text(xs[1],ys[0],r"$\mathcal E_+=\mathcal B/(\mathcal I\cap\mathcal I_+)$",
        ha="center",va="center",fontsize=24)
ax.text(xs[2],ys[0],r"$\mathcal Q=\mathcal B/\mathcal I$",ha="center",va="center",fontsize=24)
arrow((.195,ys[0]),(.30,ys[0]),r"$j$")
arrow((.642,ys[0]),(.708,ys[0]),r"$\pi$")
ax.text(xs[0],ys[1],r"$\mathcal Q(-1)$",ha="center",va="center",fontsize=24)
ax.text(xs[1],ys[1],r"$\mathcal Q\,1\ \oplus\ \mathcal Q\,h$",ha="center",va="center",fontsize=24)
ax.text(xs[2],ys[1],r"$\mathcal Q$",ha="center",va="center",fontsize=24)
arrow((.195,ys[1]),(.32,ys[1]),r"$y\mapsto yh$")
arrow((.62,ys[1]),(.75,ys[1]),r"$\epsilon_0$")
for x in [xs[0],xs[2]]:
    ax.text(x,.69,r"$\Vert$",ha="center",va="center",fontsize=25)
arrow((xs[1],.731),(xs[1],.648),color=blue)
ax.text(.492,.69,r"$\Theta[F]=[F]_{\mathcal I}\,1+[F(s+1)]_{\mathcal I}\,h$",
        fontsize=17,va="center",color=blue)
ax.text(.069,.552,r"$M=\mathcal M_\infty(\mathbf C)\simeq\mathbf P^1(\mathbf C),"
        r"\quad h=c_1(\mathcal O(1)),\quad f_n^*h=nh\quad(n\ \mathrm{odd}).$",
        fontsize=19,color=ink)
ax.text(.069,.507,"GTZ4–GTZ5: continuous inverse; exact section; every zero jet and multiplicity retained.",
        fontsize=14,color=ink)
panel(.045,.09,.44,.34)
panel(.515,.09,.44,.34)
ax.text(.066,.391,"B. Ramified specialization at 2",fontsize=17,weight="bold",color=green)
ax.text(.066,.35,r"$\overline{\mathbf F}_2[\nu]/(\nu^2)$",fontsize=21,color=green)
ax.text(.066,.311,"The nonreduced fibre remains explicit.",fontsize=13,color=ink)
ax.text(.094,.25,r"$E(-1)$",fontsize=23,ha="center",color=ink)
arrow((.155,.26),(.25,.26),r"$\mathrm{sp}_2$",dy=.035,color=green)
ax.text(.345,.25,r"$\{(a,a)\}\subset E(-1)^2$",fontsize=21,ha="center",color=ink)
ax.text(.066,.196,r"$a\longmapsto(a,a),\qquad I:(x,y)\longmapsto(y,x)$",
        fontsize=18,color=ink)
ax.text(.066,.153,r"$\mathrm{image}(\mathrm{sp}_2)=H^2_{\bar\eta}{}^I$",
        fontsize=19,color=green)
ax.text(.066,.115,r"CGT7.  $E=\mathbf Q_\ell,\ \ell\ne2$.  The cokernel is zero.",
        fontsize=12.5,color=ink)
ax.text(.536,.391,"C. Every finite prime and repetition",fontsize=17,weight="bold",color=orange)
ax.text(.536,.334,r"$\mathrm{Tr}(F_p^m\mid H^\bullet_{\alpha=1})=1+p^m$",
        fontsize=22,color=orange)
ax.text(.536,.265,r"$\prod_p\frac{1}{(1-p^{-s})(1-p^{1-s})}=\zeta(s)\zeta(s-1)$",
        fontsize=21,color=ink)
ax.text(.536,.213,r"$\Re(s)>2,\qquad m\geq1,\qquad\mathrm{including}\ p=2.$",
        fontsize=18,color=ink)
ax.text(.536,.166,"CGT8–CGT10 retain both degrees and all local factors.",fontsize=12.5,color=ink)
ax.text(.536,.119,"The global analytic and geometric maps use the same +1 shift.",
        fontsize=12.5,color=ink)
ax.text(.05,.051,"Proofs: GTZ0–GTZ9 and CGT0–CGT12. Sources: Connes–Consani (2609.00299v1), "
        "Deligne, Weil II §3.6 and §6.2.9.",fontsize=12,color=ink)
ax.text(.05,.025,"The coefficient space Q is an input here. Its purity and the identification with "
        "the programme's full localization cross remain unproved.",fontsize=12,color=ink)
for item in fig.findobj(match=matplotlib.text.Text):
    item.set_text(re.sub(r"\\(mathcal|mathbf|mathbb|mathrm) ([A-Za-z])",
                         r"\\\1{\2}",item.get_text()))
for ext in ["png","svg","pdf"]:
    fig.savefig(base/f"cc_geometric_global_lift.{ext}",dpi=180,facecolor=fig.get_facecolor())
print("Rendered exact-map figure in PNG, SVG and PDF.")
