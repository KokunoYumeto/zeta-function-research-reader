"""Exact map diagram for NS1--37; no sampled arithmetic zeros."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

OUT = Path(__file__).resolve().parent / "native_secular_figures"
OUT.mkdir(exist_ok=True)
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 13,
                     "svg.fonttype": "none", "mathtext.fontset": "dejavusans"})
fig, ax = plt.subplots(figsize=(14, 10.5))
fig.patch.set_facecolor("#f8fafc")
ax.set(xlim=(0, 14), ylim=(0, 10.5))
ax.axis("off")
navy, blue, red, green = "#142d4e", "#215c94", "#a63e35", "#24664e"

def box(x, y, w, h, title, lines, color=blue, steps=None):
    ax.add_patch(FancyBboxPatch((x, y), w, h,
        boxstyle="round,pad=0.13,rounding_size=0.08",
        linewidth=1.5, edgecolor=color, facecolor="white"))
    ax.text(x+.15, y+h-.23, title, color=color, fontsize=14,
            weight="bold", va="top")
    cursor=y+h-.67
    for j, (line, size) in enumerate(lines):
        ax.text(x+.15, cursor, line, color=navy,
                fontsize=size, va="top")
        cursor -= steps[j] if steps and j<len(steps) else .36

ax.text(.15, 10.23, "One outgoing relation controls both the spectrum and its error",
        fontsize=20, weight="bold", color=navy, va="top")
ax.text(.15, 9.78, "Exact maps for the original finite arithmetic packet; the attained metric G stays fixed.",
        fontsize=12, color=navy)
box(.25, 7.63, 5.90, 1.75, "Original source and quotient", [
    (r"$m=w_h^{*k},\quad \int m=\mu_h^k,\quad S=k/2+iu$", 15),
    (r"$C=\mathbb{C}[S]/(\chi),\quad M=(M_S-kI/2)/i$", 15),
    (r"$G=(EE^*)^{-1},\quad R=E^*G,\quad ER=I$", 15),
])
box(7.63, 7.63, 5.87, 1.75, "Attained self-adjoint compression", [
    (r"$A=EJ_LR=M+Q,\qquad A^*G=GA$", 15),
    (r"$Q=r\ell=\dfrac{i}{\omega_L}b_{L+1}b_L^*G$", 15),
    (r"$b_n=[p_n]_\chi,\quad Q^2=0$", 15),
], green, [.36,.48])
ax.annotate("", xy=(7.42,8.45), xytext=(6.34,8.45),
            arrowprops={"arrowstyle":"->","color":navy,"lw":2})
ax.text(6.9,8.76,"retain Q",ha="center",fontsize=11,color=navy)
ax.text(.25,7.30, "NS5–8: the correction is exactly the removed highest-degree multiplication term.",
        fontsize=12,color=navy)
box(.25,4.40,5.90,2.45,"Full secular determinant — no root dropped",[
    (r"$f(z)=\ell(zI-M)^{-1}r=P_f(z)/D_f(z)$",15),
    (r"$d(z)=\det(zI-A)=\chi_u(z)(1-f(z))$",15),
    (r"$d=I_fH_f,\quad I_f=\chi_u/D_f,\quad H_f=D_f-P_f$",13),
    ("H_f has simple real roots; I_f remains present.",12),
    ("An active and an invisible root can coincide.",12),
],blue)
box(7.63,4.40,5.87,2.45,"Original roots and every pole order",[
    (r"$\chi_u(z)=i^{-q}\chi(k/2+iz)$",15),
    (r"$f(z)=\sum_{\alpha}\sum_{j=0}^{e_\alpha-1}"
      r"\dfrac{c_{\alpha,j}}{(z-\alpha)^{j+1}}$",15),
    (r"$\operatorname{Im}\alpha\ne0\ \Longrightarrow\ p_\alpha=e_\alpha$",15),
    ("A nonreal original root is cancelled in d,",12),
    ("not erased from the original polynomial chi_u.",12),
],red,[.36,.60,.34,.30])
ax.annotate("", xy=(7.42,5.74), xytext=(6.34,5.74),
            arrowprops={"arrowstyle":"<->","color":navy,"lw":2})
ax.text(6.88,6.05,"NS14–21",ha="center",fontsize=10,color=navy)
box(.25,1.45,13.25,2.50,"The same correction gives the original arithmetic allowance",[
    (r"$\mathcal{C}=M_S+M_S^{\dagger_G}-kI"
      r"=-i(Q-Q^{\dagger_G}),\qquad X^{\dagger_G}=G^{-1}X^*G$",17),
    (r"$b_L^*Gb_{L+1}=0,\qquad"
      r"\epsilon_L=\|\mathcal{C}\|_G=\|Q\|_G"
      r"=\dfrac{\sqrt{(b_L^*Gb_L)(b_{L+1}^*Gb_{L+1})}}{\omega_L}$",17),
    (r"$|2\operatorname{Re}\kappa-k|\leq\epsilon_L"
      r"\quad(\kappa\in\operatorname{spec}M_S)$",17),
    ("NS29–32 retain the physical injection eta[P] = (jets of g/h) tensor k times P(sum s_j).",11),
    ("NS35–37 prove this finite bound. No decay of epsilon_L or convergence of zeros is asserted.",11),
],green,[.38,.65,.36,.27])
ax.text(.25,1.02,
    "Diagram of exact maps, not a plot of computed zeta zeros. Full proof: NATIVE_SECULAR_RECEIVER.tex, NS1–37.",
    fontsize=10.5,color=navy)
ax.text(.25,.63,
    "Human source: Connes–Consani–Moscovici, Zeta Spectral Triples, arXiv:2511.22755v1, Lemma key and eq:detDp.",
    fontsize=10.5,color=navy)
ax.text(.25,.25,
    "The complete caption states the domains, masses, repeated-root coefficients and source-to-quotient map.",
    fontsize=10.5,color=navy)
fig.subplots_adjust(left=.025,right=.99,top=.98,bottom=.025)
fig.savefig(OUT/"NATIVE_SECULAR_MAPS.png",dpi=160,facecolor=fig.get_facecolor())
fig.savefig(OUT/"NATIVE_SECULAR_MAPS.svg",facecolor=fig.get_facecolor())
plt.close(fig)
print(OUT)
