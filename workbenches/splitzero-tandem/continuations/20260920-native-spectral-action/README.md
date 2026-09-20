# The original arithmetic error bound as a trace curvature

The Split-Zero programme starts with the theta source whose Mellin transform is \(2\xi/h\), takes its quotient by the original theta relations, and measures finite polynomial classes using their least-norm source representatives. Here \(h\) contains the selected zeros with their complete orders. The quotient metric is the one obtained from that source; it is not chosen to improve a bound.

This edition calculates the trace response of the exact outgoing relation. In the coordinate \(S=k/2+iu\), write \(T(t)=A-tQ\). Here \(A\) is the attained selfadjoint compression, \(Q\) is its rank-one correction, and \(T(1)\) is the original quotient multiplication operator. The same arithmetic allowance already used in the programme is

\[
\epsilon^2=\operatorname{tr}(Q^{\dagger_G}Q)
=\tfrac12\,\frac{d^2}{dt^2}\operatorname{tr}(T(t)^{\dagger_G}T(t)).
\]

The proof computes the complete characteristic polynomial, every polynomial trace coefficient, all repeated-root endpoint terms, and the exact map back to the physical jets. The quadratic trace \(\operatorname{tr}(T(t)^2)\) has zero second derivative, but the retained-metric action above generally does not. Their exact difference and the mixed derivative are calculated, not discarded.

## Read the complete mathematics

- [All four complete proofs in one LaTeX document](COMPLETE_PROOFS.tex).
- [Main calculation, SA1–43](NATIVE_SPECTRAL_ACTION.tex).
- [Coefficient test inside the cited author's function class, FC1–4](SOURCE_FUNCTION_CLASS_CHECK.tex).
- [Independent metric, dilation and sharp-bound proof, MC1–35](RANK_ONE_METRIC_CURVATURE.tex).
- [Independent Jordan endpoint and multiplicity proof, EC1–15](INDEPENDENT_ENDPOINT_CHECK.tex).
- [Exact illustrated example and its full caption](FIGURE_CAPTION.md).
- [Machine-readable result and its programme use](RESULT_INDEX.json), [human source and point-of-use map](HUMAN_SOURCE_USE.json), and [validation scope](VALIDATION.md).

The contextual human source is Alain Connes and Walter D. van Suijlekom, [*Quadratic Forms, Real Zeros and Echoes of the Spectral Action*, arXiv:2511.23257v1](https://arxiv.org/abs/2511.23257v1), Section sect:sa. The source was read as original author LaTeX. SA10–11 and FC1–4 establish a bounded correction of its displayed cyclic coefficient; the source's repeated-node proof and later second derivative agree with the corrected value. The original author source has not been altered.

The three full cumulative manuscript successors are in [cumulative](cumulative/). Their preceding bodies, citations and proof sources are retained exactly; the insertion record identifies each predecessor and the complete added proof text.

These finite identities do not prove decay of \(\epsilon\), evaluate the remaining growing-degree arithmetic estimate, or settle RH. The figure and executable checks use explicitly identified finite comparison algebras, not invented arithmetic zeros. This is a GitHub source edition; it does not claim a new Zenodo or Overleaf deposit.
