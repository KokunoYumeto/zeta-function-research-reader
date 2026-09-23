# An evaluated arithmetic pairing for the original endpoint test

**SZ-20260923-146.** The explicit original endpoint source at heat time `t=1/32` now has a proved arithmetic sign:

\[
50<\sum_\rho m_\rho F(\rho)^2<64.
\]

The test is `f=(D²−1/4)[exp(−8x²) H_(1/32)(x) cos(16x)]`, with the complete original theta density. The sum uses the original zeta zeros and their actual reflected Weil product. No zero list or assumption about their location is used: the value is enclosed from the original prime-power sum and full Gamma integral.

The same source has the two strictly negative prime-boundary coordinates in AP27. This evaluates the relation that was left open in ER37–40: the signs of those two linear moments do not determine this quadratic pairing. The invertible source filter and all original support labels remain in the calculation.

## Complete proof and reproduction

- **NOTE.pdf** is the illustrated proof reader.
- **ACTUAL_ENDPOINT_PAIRING.tex**, AP1–28, contains all definitions, the original-zeta receiving formula, finite-cutoff divisor/Gamma terms, source decomposition with its complete bounded residual, and the sign proof.
- **INDEPENDENT_TAIL_BOUNDS.md**, TB1–50, independently derives the original source tails, convolution formula, and every mathematical error bound used by the certificate.
- **certify_pairing.py** and **CERTIFICATE.json** give the interval computation. Run `python -B certify_pairing.py` with python-flint 0.9.0 and SymPy installed. It integrates the original finite source in ball arithmetic and includes the proved infinite-tail bounds. All final rational comparisons are checked.
- **draw_pairing.py** reproduces the exact-map and certified-interval figure using Matplotlib.
- Build with `lualatex NOTE.tex`, twice for links. The standalone proof needs no private proof file to compile.

The result closes this single test's previously unevaluated sign. It does not settle positivity for the full source space or RH. The previous endpoint paper is preserved; this is its mathematical successor.

## Human sources

Brad Rodgers and Terence Tao, [The de Bruijn–Newman constant is non-negative, v5](https://arxiv.org/abs/1801.05914v5), original TeX equations `hoz`, `sas`, `phidef`, `htdef`: source and coordinates, with the full original zeta multiplier kept in AP3.

Alain Connes, [Trace formula in noncommutative geometry and the zeros of the Riemann zeta function](https://arxiv.org/abs/math/9811068v1), Appendix II, (1)–(11), Theorems 1 and 6: original explicit-formula conventions. The Gaussian extension and finite-cutoff contributions are proved in AP4–6.

Fredrik Johansson and FLINT contributors, [original complex-integration documentation](https://raw.githubusercontent.com/flintlib/flint/master/doc/source/acb_calc.rst), integration contract and error control: the computation uses its returned enclosures, not only a requested tolerance.

The original algebraic prime receiver is [FR15–25, pinned source](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/ec73ac350d0cda3d95c0bd1361bede33166b4d34/workbenches/splitzero-tandem/continuations/20260923-original-zeta-return/NOTE.tex). AP27 explicitly evaluates its two coordinates on this test.
