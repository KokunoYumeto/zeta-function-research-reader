"""Exact source, costalk and quotient comparison; no schematic zero positions."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
base=Path(__file__).resolve().parent
fig,ax=plt.subplots(figsize=(14,11.5))
ax.set(xlim=(0,14),ylim=(0,11.5));ax.axis("off")
def box(x,y,w,h,color):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.10",
                              ec="#52627a",fc=color,lw=1.5))
def text(x,y,s,size=15,bold=False,**kw):
    ax.text(x,y,s,ha="center",va="center",fontsize=size,
            fontweight="bold" if bold else "normal",**kw)
def arrow(x,y,X,Y):
    ax.annotate("",xy=(X,Y),xytext=(x,y),arrowprops=dict(arrowstyle="->",lw=1.5,color="#52627a"))
text(7,11.13,"The original source inside the supported defect receiver",20,True)
text(7,10.70,"Exact maps on the complete zero divisor, with every multiplicity retained",12,color="#52627a")
box(.4,8.15,13.2,2.15,"#edf3fb")
text(7,9.96,"AN ACTUAL RESTRICTED SOURCE AND ITS STRONG DUAL",14,True)
text(7,9.43,r"$0\longrightarrow J\longrightarrow A_O\longrightarrow N_O\longrightarrow0$",21)
text(7,8.93,r"$N_O=\ker(P_OE),\qquad A_O=q^{-1}N_O$",18)
text(7,8.47,r"$0\longrightarrow N_O^\prime\longrightarrow A_O^\prime\longrightarrow J^\prime\longrightarrow0$",21)
arrow(7,8.0,7,7.56)
box(.4,5.22,13.2,2.12,"#f5f0fa")
text(7,7.00,"THE SAME SOURCE IS RECOVERED FROM THE COSTALK",14,True)
text(7,6.47,r"$i^!\mathscr{E}_r=[\,\overline{H}\overset{a_r}{\longrightarrow} B\,],\qquad B=A^\prime_\beta$",20)
text(7,5.96,r"$a_r=q^\prime A_HD_r,\qquad\overline{\operatorname{im}a_r}^{\,\beta}=A_O^\perp$",19)
text(7,5.49,r"$H^1(i^!\mathscr{E}_r)=B/\operatorname{im}a_r,\qquad (H^1)_{\rm sep}\simeq (A_O)^\prime_\beta$",18)
box(.4,2.82,6.35,1.92,"#eaf5ef")
box(7.22,2.82,6.38,1.92,"#fcf0e9")
text(3.57,4.44,"SUPPORTED POSITIVE PART",13,True)
text(3.57,3.89,r"$H^0(i^!\mathscr{E}_r)=\overline{H_L}\simeq\overline{H_{\rm pos}}$",18)
text(3.57,3.29,r"$\mathscr{E}_r=i_*\overline{H_L}\oplus\mathscr{E}_r^O$",18)
text(10.41,4.44,"EXACT COST OF THE QUOTIENT",13,True)
text(10.41,3.90,r"$B\longrightarrow (A_O)^\prime_\beta$",21)
text(10.41,3.34,r"$\ker=A_O^\perp=\overline{\operatorname{im}a_r}^{\,\beta}$",18)
box(.4,.72,13.2,1.60,"#f3f4f8")
text(7,2.03,"ALL NONTRIVIAL SCALES GIVE ISOMORPHIC RECEIVERS",13,True)
text(7,1.54,r"$D_r=D_tV_{r,t},\qquad \mathscr{E}_r\simeq\mathscr{E}_t,\qquad r,t>1$",21)
text(7,1.04,r"$W=W_L+W_O$ remains; the full receiver also keeps both endpoint lines.",13)
text(7,.30,"Proofs: GDC1–GDC12, with RGR0–RGR12 and PTQ.  r is a coefficient parameter; integer n is a cover degree.",10,color="#52627a")
fig.savefig(base/"gysin_positive_receiver.png",dpi=150,bbox_inches="tight",facecolor="white")
fig.savefig(base/"gysin_positive_receiver.svg",bbox_inches="tight",facecolor="white")
plt.close(fig)
