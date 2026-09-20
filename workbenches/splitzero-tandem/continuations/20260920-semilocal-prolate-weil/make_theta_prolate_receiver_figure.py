"""Exact source-map diagram and a sampled plot of the proved PT10 bound.

No zeta zeros are sampled. The plotted input is explicitly truncated Hermite,
not the prolate eigenfunction. Floating-point plot samples are not certificates.
"""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from scipy.special import gamma, gammaincc, erfc

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "theta_prolate_figures"
OUT.mkdir(exist_ok=True)
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11,
                     "svg.fonttype": "none", "mathtext.fontset": "dejavusans"})
fig = plt.figure(figsize=(15, 10), layout="constrained")
gs = fig.add_gridspec(2, 2, height_ratios=[1.1, 1.0])
ax = fig.add_subplot(gs[0, :])
ax.set(xlim=(0, 15), ylim=(0, 5.3))
ax.axis("off")
ax.set_title("The original theta seed and the paper's weighted source",
             fontsize=18, loc="left", pad=10)

def box(x, y, width, height, title, lines, color):
    ax.add_patch(FancyBboxPatch((x, y), width, height,
        boxstyle="round,pad=0.06,rounding_size=0.10",
        facecolor=color, edgecolor="#46596c", linewidth=1.1))
    ax.text(x + .14, y + height - .26, title, fontsize=12, weight="bold",
            ha="left", va="top", color="#152f49")
    ax.text(x + width/2, y + height/2 - .14, "\n".join(lines),
            fontsize=12, ha="center", va="center", linespacing=1.8)

box(.10, 2.42, 4.40, 2.16, "Literal Hermite seed  [PT2, PT5]", [
    r"$H(x)=(\pi^2x^4-\frac{3}{2}\pi x^2)e^{-\pi x^2}$",
    r"$\phi_*=4H$"], "#edf4fa")
box(5.20, 2.42, 4.38, 2.16, "Original arithmetic source  [PT2]", [
    r"$f_0=\Theta\phi_*=8\sum_{n\geq1}H(nx)$",
    r"$\mathcal{M}f_0(s)=g(s)=2\xi(s)$"], "#eaf4ed")
box(10.28, 2.42, 4.40, 2.16, "Weighted author source  [PT4, PT6]", [
    r"$K=\frac{1}{8}U f_0,\quad (Uf)(u)=u^{1/2}f(u)$",
    r"$\widehat{K}(z)=\frac{1}{4}\Xi(z)$"], "#fff3df")
for left, right, label in [(4.53, 5.13, r"$\Theta$"),
                            (9.61, 10.20, r"$U/8$")]:
    ax.annotate("", xy=(right, 3.42), xytext=(left, 3.42),
                arrowprops={"arrowstyle": "->", "lw": 1.8, "color": "#314b65"})
    ax.text((left+right)/2, 3.68, label, ha="center", fontsize=12)
ax.text(.16, 1.72, r"$U:L^2(du)\longrightarrow L^2(du/u)$ is unitary;"
        r"   $\|K\|^2=\|f_0\|^2/64$.", fontsize=13)
ax.text(.16, 1.16, r"Scaling generators:  $UDU^{-1}=\frac{1}{2}-u\partial_u$;"
        r"   $-iu\partial_u=i(UDU^{-1}-\frac{1}{2})$.", fontsize=13)
ax.text(.16, .43, "Exact map, not an identification of metrics or of finite spectra."
        "\nConnes–Consani–Moscovici, arXiv:2511.22755v1, ku / emap / xih;"
        " receiver PT1–7.", fontsize=11, color="#314b65")

boundax = fig.add_subplot(gs[1, 0])
lam = np.linspace(1, 5, 321)
a = .25
B = (np.pi**2*lam**4 + 1.5*np.pi*lam**2)*np.exp(-np.pi*lam**2)
T = np.exp(-np.pi*lam**2)*(.5*np.pi*lam**3+1.5*lam)+.75*erfc(np.sqrt(np.pi)*lam)
Ia = (lam**(.5+a)-lam**(-.5-a))/(.5+a)
def J(nu):
    v = (nu+1)/2
    return gamma(v)*gammaincc(v, np.pi*lam**2)/(2*np.pi**v)
lattice = (B+T)*Ia
endpoints = 2*(np.pi**2*J(a+3.5)+1.5*np.pi*J(a+1.5)
               +lam**(a-.5)*T/(.5-a))
total = lattice + endpoints
boundax.semilogy(lam[1:], lattice[1:], color="#b87911",
                 label="Omitted Gaussian lattice tail")
boundax.semilogy(lam, endpoints, color="#3774ad",
                 label="Both Fourier endpoints")
boundax.semilogy(lam, total, color="#233d35", lw=2.3,
                 label="Sum: proved upper bound")
boundax.set_title("A concrete input with no unknown approximation error",
                  fontsize=12, loc="left")
boundax.set_xlabel(r"Cutoff $\lambda$")
boundax.set_ylabel(r"Bound for $\sup_{|\Im z|\leq 1/4}|\widehat K_\lambda-\Xi/4|$")
boundax.grid(alpha=.2)
boundax.legend(fontsize=9.3, loc="upper right")
boundax.text(.02, .04, r"$A_\lambda=H|_{[-\lambda,\lambda]},\ d_\lambda=0$"
             "\nTruncated Hermite input — not the prolate eigenfunction.",
             transform=boundax.transAxes, fontsize=10,
             bbox={"facecolor": "white", "alpha": .9, "edgecolor": "none"})

txt = fig.add_subplot(gs[1, 1])
txt.axis("off")
txt.set_title("All three errors survive the actual prolate transfer",
              fontsize=12, loc="left")
lines = [
    ("Interior error", r"$\lambda\,d_\lambda I_a(\lambda)$"),
    ("Omitted lattice tail", r"$[B(\lambda)+T(\lambda)]I_a(\lambda)$"),
    ("Lower and upper endpoints", r"$R_a(\lambda)$"),
]
for y, (label, formula) in zip([.86, .65, .44], lines):
    txt.text(.04, y, label, fontsize=12, weight="bold", color="#152f49")
    txt.text(.08, y-.09, formula, fontsize=16)
txt.text(.04, .18, "PT8–12 prove their sum is the uniform transform bound."
         "\nThe prolate discrepancy remains its actual norm."
         "\nNo Weil-minimum approximation or RH conclusion is shown.",
         fontsize=11, linespacing=1.6, va="top")
fig.suptitle("Exact constants and a complete finite theta-transfer bound",
             fontsize=21, weight="bold")
fig.savefig(OUT/"theta_prolate_receiver.svg")
fig.savefig(OUT/"theta_prolate_receiver.png", dpi=155)
plt.close(fig)
samples = {"sample_scope": "Floating point rendering of the proved PT10 bound; not interval certificates.",
           "input": "A_lambda equals H on [-lambda,lambda] and zero outside; d_lambda=0",
           "strip": {"max_abs_Im_z": a},
           "values": [{"lambda": float(lam[j]), "lattice": float(lattice[j]),
                       "endpoints": float(endpoints[j]), "sum": float(total[j])}
                      for j in [0, 80, 160, 240, 320]]}
(OUT/"BOUND_PLOT_SAMPLES.json").write_text(json.dumps(samples, indent=2)+"\n",
                                         encoding="utf-8")
print("Generated theta_prolate_receiver.svg/png and five labelled bound samples.")
