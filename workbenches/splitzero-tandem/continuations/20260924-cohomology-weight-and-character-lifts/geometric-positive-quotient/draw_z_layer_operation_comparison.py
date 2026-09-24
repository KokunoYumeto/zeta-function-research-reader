"""Reproduce the exact evaluation comparisons ZC4.3 and ZC6.1."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

ROOT = Path(__file__).resolve().parent
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
fig, ax = plt.subplots(figsize=(13.4, 10.8))
fig.patch.set_facecolor("#f6f8fb")
ax.set_facecolor("#f6f8fb")
ax.set_xlim(0, 13.4)
ax.set_ylim(0, 10.8)
ax.axis("off")

def box(x, y, equation, caption, colour):
    patch = FancyBboxPatch((x, y), 5.75, 0.99,
                          boxstyle="round,pad=0.05,rounding_size=0.10",
                          linewidth=1.2, edgecolor=colour, facecolor="white")
    ax.add_patch(patch)
    ax.text(x + 2.875, y + 0.64, equation, ha="center", va="center",
            fontsize=20, color=colour)
    ax.text(x + 2.875, y + 0.21, caption, ha="center", va="center",
            fontsize=10.5, color="#334155")

def arrow(x, y0, y1):
    ax.annotate("", xy=(x, y1), xytext=(x, y0),
                arrowprops={"arrowstyle": "-|>", "color": "#526174", "lw": 1.4})

ax.text(0.45, 10.35, r"Keeping $Z_0$, $Z_1$, $Z_2$: two exact evaluation differences",
        fontsize=21, weight="bold", color="#17243b")
ax.text(0.45, 9.94,
        r"$\tau$ carries $Z_1$ without parity; integer outputs retain their $Z_2$ state.",
        fontsize=12, color="#334155")

ax.text(0.45, 9.38, "1. Combine before multiplying, or multiply before combining",
        fontsize=15, weight="bold", color="#17243b")
blue, red = "#176b91", "#9f3d54"
box(0.45, 8.09, r"$(\tau+\tau)1$", "First add the two tau inputs", blue)
box(7.20, 8.09, r"$\tau1+\tau1$", "First multiply each tau input by integer 1", red)
arrow(3.325, 8.00, 7.64)
arrow(10.075, 8.00, 7.64)
box(0.45, 6.59, r"$\tau1=1$", r"Integer output: $Z_2$ odd", blue)
box(7.20, 6.59, r"$1+1=2$", r"Integer output: $Z_2$ even", red)
ax.text(6.70, 7.08, r"$\ne$", fontsize=25, ha="center", color="#17243b")
ax.text(0.45, 6.10,
        "Proof: ZC6.1. A rig identifies these procedures; an injective comparison cannot.",
        fontsize=11, color="#334155")

ax.plot([0.45, 12.95], [5.73, 5.73], color="#cbd5e1", lw=1)
ax.text(0.45, 5.30, "2. Retain Boolean absence and unchanged integer cancellation",
        fontsize=15, weight="bold", color="#17243b")
ax.text(0.45, 4.89, r"Using the shared scalar $0$ and the Boolean law $\tau+0=\tau$.",
        fontsize=12, color="#334155")
box(0.45, 3.55, r"$(\tau+1)+(-1)$", "First add tau and integer 1", blue)
box(7.20, 3.55, r"$\tau+(1+(-1))$", "First perform integer cancellation", red)
arrow(3.325, 3.46, 3.10)
arrow(10.075, 3.46, 3.10)
box(0.45, 2.05, r"$1+(-1)=0$", "Output: the shared scalar zero", blue)
box(7.20, 2.05, r"$\tau+0=\tau$", r"Output: $Z_1$ presence without $Z_2$", red)
ax.text(6.70, 2.54, r"$\ne$", fontsize=25, ha="center", color="#17243b")
ax.text(0.45, 1.55,
        "Proof: ZC4.3. In the completed table ZC5, the full defect is classified for every triple.",
        fontsize=11, color="#334155")
ax.text(0.45, 0.90,
        "These are evaluation diagrams, not identifications of tau with integer 0 or integer 1.",
        fontsize=11, color="#334155")
ax.text(0.45, 0.45,
        "Source comparison: Baez–Chaudhuri, arXiv:2506.23375v3, sections 3–6.\n"
        "Complete proofs: FULL_Z_LAYER_OPERATION_COMPARISON.md, ZC1–ZC10.",
        fontsize=9.7, color="#526174")

fig.savefig(ROOT / "z_layer_operation_comparison.png", dpi=170, bbox_inches="tight")
fig.savefig(ROOT / "z_layer_operation_comparison.svg", bbox_inches="tight")
plt.close(fig)
