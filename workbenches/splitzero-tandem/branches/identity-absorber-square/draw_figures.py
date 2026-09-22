"""Exact algebra diagrams. No numerical or geometric identification is asserted."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "figures"
OUT.mkdir(exist_ok=True)
plt.rcParams.update({"font.family": "DejaVu Sans", "mathtext.fontset": "dejavusans",
                     "font.size": 14, "svg.fonttype": "none"})
INK, BLUE, TEAL, PURPLE = "#17283c", "#235ca5", "#126e68", "#7245a0"

def canvas(title, subtitle, size=(14, 10)):
    fig, ax = plt.subplots(figsize=size)
    fig.patch.set_facecolor("#fcfcfa")
    ax.set_facecolor("#fcfcfa")
    ax.set(xlim=(0, 14), ylim=(0, 10))
    ax.axis("off")
    ax.text(.4, 9.55, title, fontsize=23, weight="bold", color=INK, va="top")
    ax.text(.4, 8.9, subtitle, fontsize=12, color=INK, va="top")
    return fig, ax

def box(ax, xy, wh, title, lines, color=BLUE):
    x, y = xy
    w, h = wh
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=.12,rounding_size=.12",
                              ec=color, fc="white", lw=1.8))
    ax.text(x + .18, y + h - .2, title, fontsize=17, weight="bold", color=color, va="top")
    if lines:
        ax.text(x + .18, y + h - .67, "\n".join(lines), fontsize=13.2,
                color=INK, va="top", linespacing=1.55)

def arrow(ax, a, b, color=INK):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle="-|>", mutation_scale=17, lw=1.8, color=color))

def save(fig, name):
    fig.savefig(OUT / (name + ".png"), dpi=150, facecolor=fig.get_facecolor(), bbox_inches="tight")
    fig.savefig(OUT / (name + ".svg"), facecolor=fig.get_facecolor(), bbox_inches="tight")
    plt.close(fig)

fig, ax = canvas("Both absorber extensions coexist without losing arithmetic",
    r"Exact pushout in $\mathcal{W}$: maps preserve both identities; global zero absorption is not assumed.")
box(ax, (4.55, 6.9), (4.9, 1.3), r"$S=G(R)=R\sqcup\{\tau\}$",
    [r"$\tau\ne e=0_R,\quad \tau x=\tau\quad(x\in S)$"])
box(ax, (.45, 4.55), (5.6, 1.7), r"$H=S\sqcup\{\Omega\}$",
    [r"$\Omega+x=\Omega x=\Omega\quad(x\in H)$",
     r"In particular: $\tau\Omega=\Omega$"], PURPLE)
box(ax, (7.95, 4.55), (5.55, 1.7), r"$T=S\sqcup\{w\}$",
    [r"$w+x=w\quad(x\in T)$",
     r"$wr=w\ (r\in R),\quad w^2=w,\quad\tau w=\tau$"], TEAL)
arrow(ax, (5.15, 6.83), (3.6, 6.36))
arrow(ax, (8.8, 6.83), (10.2, 6.36))
box(ax, (3.2, 1.75), (7.6, 1.8), r"$P(R)=R\sqcup\{\tau,w,\Omega\}$",
    [r"All old operations retained; all displayed parts distinct.",
     r"Forced cross operations: $\Omega w=\Omega,\quad\Omega+w=\Omega$"], BLUE)
arrow(ax, (3.4, 4.4), (4.7, 3.68))
arrow(ax, (10.3, 4.4), (9.3, 3.68))
ax.text(7, 3.99, "All four arrows are inclusions.", ha="center", fontsize=12, color=INK)
ax.text(.45, .85, r"Why the product is forced:  $(\tau\Omega)w=\Omega(\tau w)=\Omega\tau=\Omega$.",
        fontsize=16, color=INK)
ax.text(.45, .22, "Proof: RECEIVERS.md, Theorems 1–2. Original definitions: HI-AI [1], §3; [2], §§9–10.\n"
        "The diagram represents algebra homomorphisms, not spatial or magnitude relations.",
        fontsize=10.5, color=INK, va="top")
save(fig, "01_common_receiver")

fig, ax = canvas("The order of the other two adjunctions changes the algebra",
    r"Uniform conventions: $U$ keeps the old additive identity; $E$ permits both old identities to become local.",
    size=(14, 10))
box(ax, (.5, 6.05), (3.55, 1.85), r"Start: $G(R)$",
    [r"$\tau\ne e$.", r"Original ring operations.",
     r"Supported elements: $r\in R$."])
box(ax, (5, 6.05), (3.7, 1.85), r"First adjoin $u$: $C_3$",
    [r"$t<c<u;\quad +=\max,\ \cdot=\min$",
     r"$\tau\mapsto t,\quad r\mapsto c$"], TEAL)
box(ax, (9.65, 6.05), (3.75, 1.85), r"Then $\epsilon$: $P_E$",
    [r"$\epsilon<u;\quad +=\max,\ \cdot=\max$",
     r"Original image:", r"$s\mapsto u$ for all $s\in G(R)$."], PURPLE)
arrow(ax, (4.18, 7), (4.84, 7))
arrow(ax, (8.84, 7), (9.5, 7))
box(ax, (.5, 3.35), (3.55, 1.85), r"Start: $G(R)$",
    [r"Same programme object.",
     r"Same original elements."])
box(ax, (5, 3.35), (3.7, 1.85), r"First adjoin $\epsilon$: $E_2$",
    [r"$\epsilon<c;\quad +=\max,\ \cdot=\max$",
     r"Every original $s$ maps to $c$."], PURPLE)
box(ax, (9.65, 3.35), (3.75, 1.85), r"Then $u$: $P_U$",
    [r"$\epsilon<u;\quad +=\max,\ \cdot=\min$",
     r"Original image:", r"$s\mapsto\epsilon$ for all $s\in G(R)$."], TEAL)
arrow(ax, (4.18, 4.3), (4.84, 4.3))
arrow(ax, (8.84, 4.3), (9.5, 4.3))
ax.text(.6, 2.5, "Same two final labels, different cross-product:", fontsize=18, color=INK, weight="bold")
ax.text(3.3, 1.72, r"$P_E:\quad\epsilon u=u$", fontsize=25, color=PURPLE, ha="center")
ax.text(10.6, 1.72, r"$P_U:\quad\epsilon u=\epsilon$", fontsize=25, color=TEAL, ha="center")
ax.text(.6, .88, "Every binary-operation-preserving map between the two final algebras is constant.",
        fontsize=14, color=INK)
ax.text(.5, .22, "Proof: RECEIVERS.md, Theorems 4–6; every arrow is the specified universal map, not an inclusion.\n"
        "Starting construction: HI-AI [1], §3. Identifications shown here are quotient outcomes, not changes to G(R).",
        fontsize=10.5, color=INK, va="top")
save(fig, "02_order_of_roles")

fig, ax = canvas("All quotients of the common receiver",
    r"$R$ is a nonzero commutative unital ring. $P(R)=R\sqcup\{\tau,w,\Omega\}$.")
box(ax, (.5, 6.5), (12.9, 1.65), r"An ideal $I\subseteq R$ gives $P(R/I)$",
    [r"Exactly $r\sim s$ when $r-s\in I$; $\tau,w,\Omega$ remain separate.",
     r"Every congruence that does not collapse all of $R$ is of this form."])
ax.text(.65, 5.97, r"When $I=R$, the supported ring becomes one element $c$. Exactly three further mergers follow:",
        fontsize=12.5, color=INK)
cards = [
    (.55,  r"$L_4$", [r"$\{\tau\}\mid R\mid\{w\}\mid\{\Omega\}$", "4 classes"], BLUE),
    (4.0, r"$L_3$", [r"$\{\tau\}\mid(R\cup\{w\})\mid\{\Omega\}$", "3 classes"], TEAL),
    (7.45, r"$E_2$", [r"$(\{\tau\}\cup R\cup\{w\})\mid\{\Omega\}$", "2 classes; both operations max"], PURPLE),
    (10.95, "Singleton", [r"One class", r"$P(R)$"], INK)
]
for x, title, lines, color in cards:
    box(ax, (x, 3.75), (2.5 if x == 10.95 else 2.95, 1.65), title, [], color)
    ax.text(x+.12, 4.63, lines[0], fontsize=10.3, color=INK, va="top")
    ax.text(x+.12, 4.05, lines[1], fontsize=10.2, color=INK, va="top")
for x1, x2 in [(3.6,3.88),(7.05,7.32),(10.53,10.82)]:
    arrow(ax, (x1,4.62),(x2,4.62))
ax.text(4.85, 3.1, r"$w=c$", color=TEAL, ha="center", fontsize=15)
ax.text(8.5, 3.1, r"$\tau=c=w$", color=PURPLE, ha="center", fontsize=15)
ax.text(12.15, 3.1, r"$\Omega=\tau$", color=INK, ha="center", fontsize=15)
box(ax, (.6, 1.1), (12.7, 1.23), "Faithfulness consequence",
    [r"If a homomorphism is injective on the original $R$, it is injective on all of $P(R)$."], BLUE)
ax.text(.5, .35, "Proof: RECEIVERS.md, Theorem 3 and Corollary 3.1; original constructions from HI-AI [1–2].\n"
        "Arrows are quotient maps; bars mark congruence classes. This does not depict a shape for the arbitrary ideal lattice.",
        fontsize=10.5, color=INK, va="top")
save(fig, "03_all_quotients")
fig, ax = canvas("All six orders give four different algebras",
    r"Exact receivers: every original $s\in G(R)$ maps to $a$. Addition is maximum in every displayed chain.")
rows = [
    [r"$O\ U\ E$", r"$\epsilon<a=u=\Omega$", "maximum", "2"],
    [r"$U\ O\ E$", r"$\epsilon<a=u<\Omega$", "maximum", "3"],
    [r"$U\ E\ O$", r"$\epsilon<a=u<\Omega$", "maximum", "3"],
    [r"$O\ E\ U$", r"$a=\epsilon=\Omega<u$", "minimum", "2"],
    [r"$E\ O\ U$", r"$a=\epsilon=\Omega<u$", "minimum", "2"],
    [r"$E\ U\ O$", r"$a=\epsilon<u<\Omega$", "min on {ε,u}; Ω absorbs all", "3"],
]
table = ax.table(cellText=rows,
    colLabels=["Order\n(left to right)", "Exact images of the labels", "Multiplication", "Size"],
    colWidths=[.19, .34, .39, .08], bbox=[.02, .26, .96, .53], cellLoc="center")
table.auto_set_font_size(False)
table.set_fontsize(14)
palette = ["#f1eafa", "#e7effb", "#e7effb", "#e5f3ef", "#e5f3ef", "#fff0db"]
for (row, col), cell in table.get_celld().items():
    cell.set_edgecolor("#d0d8e2")
    cell.set_linewidth(1)
    cell.get_text().set_color(INK)
    cell.set_facecolor("#dce5ef" if row == 0 else palette[row - 1])
    if row == 0: cell.get_text().set_fontweight("bold")
ax.text(.5, 1.94, r"$O$: adjoin literal $\Omega$;  $U$: adjoin $u$;  $E$: adjoin common identity $\epsilon$.",
        fontsize=15, color=INK)
ax.text(.5, 1.26, r"$U$ keeps the old additive identity. $E$ allows old identities to become local. $O$ keeps both.",
        fontsize=12.5, color=INK)
ax.text(.5, .36, "Proof: RECEIVERS.md, Theorem 7. Starting definitions: HI-AI [1], §3; [2], §§9–10.\n"
        "Equalities are forced images under the stated universal maps. They do not identify elements inside the original G(R).",
        fontsize=10.5, color=INK, va="top")
save(fig, "04_all_six_orders")
print(str(OUT))
