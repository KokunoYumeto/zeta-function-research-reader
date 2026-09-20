# Certified finite packets of the original theta heat flow

The Split-Zero source is the original theta function with Mellin transform $g=2\xi$. Under the multiplier $U_t f(x)=e^{t(\log x)^2/4}f(x)$, its Mellin transform is exactly $g_t(s)=16H_t(-2i(s-1/2))$, where $H_t$ is the de Bruijn–Newman heat flow. This edition puts the effective approximation of D. H. J. Polymath into those original coordinates, so that actual error bounds can enter the programme's moving-packet and exterior-factor calculations.

The full gamma/Stirling factors and their phases remain. A fixed holomorphic comparison function and an exact finite cutoff correction allow Cauchy estimates even across changes of the Riemann–Siegel cutoff. The proof then bounds every derivative, the complete exterior logarithmic derivative, multiplicity-weighted traces and their time derivatives. It supplies finite stopping and quadrature rules, and executes them on a nonempty packet.

For every $1023/4096\le t\le1025/4096$, there is exactly one zero of $g_t$, counted with multiplicity, in

$$
1/10<\Re s<9/10,\qquad507/4<\Im s<513/4.
$$

The proved count and exact reflection symmetry force this zero to be simple and lie on $\Re s=1/2$. The calculation also proves $|\rho'(t)|<1102$ and retains the full exterior factor $R_t=g_t/(s-\rho(t))$, with $|R_t'/R_t(\rho(t))|<2204$. These are deliberately broad, rigorously bounded positive-time statements—not a time-zero, negative-time, all-height or RH conclusion.

## Proofs, sources and checks

- [Complete integrated LaTeX](COMPLETE_PROOFS.tex), including the full independent remainder derivation.
- [Full receiver PMH1–10](POLYMATH_NATIVE_HEAT_RECEIVER.tex) and [corrected source remainder PMH11](SOURCE_REMAINDER_REPAIR.tex).
- [Independent complete remainder proof](INDEPENDENT_DERIVATION.tex) and [exact rational constant certificates](exact_certificates.py).
- [Finite source and contour checker](finite_receiver_checks.py), [root replay](checks/ROOT_REPLAY.json), [verification scope](VALIDATION.md) and [result/use index](RESULT_INDEX.json).
- [Exact coordinate illustration](figures/certified_packet.png), [caption](FIGURE_CAPTION.md) and [reproducible source](make_figure.py).
- [Three complete cumulative successors and reversible insertion records](CUMULATIVE_INSERTION.json).

The human source is [D. H. J. Polymath, arXiv:1904.12438v2](https://arxiv.org/abs/1904.12438v2), whose complete original author LaTeX was read. PMH11 identifies and repairs intermediate Gaussian-denominator, Stirling-factor and omitted-remainder issues in that version's proof of `RTN-prop`; it derives the unchanged final constants. An independent proof and exact rational certificates check that repair. The author source remains untouched. Arias de Reyna's Riemann–Siegel bounds are credited as read through Polymath, not falsely described as a direct reading of the 2011 original. [Fredrik Johansson's Arb paper](https://arxiv.org/abs/1611.02831v1) is credited for interval arithmetic.

This is a complete source edition. No new PDF, Zenodo deposit, Overleaf update or timer change is claimed.
