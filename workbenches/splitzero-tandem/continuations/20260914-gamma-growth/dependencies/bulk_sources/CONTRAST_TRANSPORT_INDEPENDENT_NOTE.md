# Independent projector-contrast calculation

Completed the full fragment `contrast_transport_independent.tex`, CTI1–CTI21. This is an independent mathematical proof, not a build or Lean check.

Current source SHA-256: `e28cd0b2d0e0804c78e4058c9b4f78f00f000c95d5a5aef5a994af7ff8bb9b73`. The earlier source hash `045ac0435e060488bfdf787d6ab3c9fd7da1630f3ca3fe7265e3e880558d4598` is preserved here for provenance. The sole change was adding the missing backslash to `operatorname{osc}` in CTI13; no mathematical expression changed. The parent independently read and accepted the complete CTI1–CTI21 proof before requesting that presentation correction.

For the exact original subspaces `P=polynomials of degree <=r-1` and `fP`, with monic degree `l` and `r>=l`, their intersection is `f polynomials of degree <=r-l-1`, of dimension `r-l`; their sum is the full ambient degree `<=r+l-1` space. For every positive original coefficient Gram M, the difference of its two orthogonal projectors has **rank exactly 2l and inertia exactly (l,l,r-l)**. Its spectrum is in `[-1,1]`, trace is zero, and the trace absolute value formed in that same metric is at most `2l`. The Euclidean singular-value norm of the non-Hermitian original coefficient matrix is not substituted for this metric quantity.

The proof supplies both full coefficient inclusion matrices, their Gram/projector formulas, the exact kernel, positive and negative subspaces, and the explicit metric isometry. For the bounded real logarithmic density derivative, it proves

`|Tr(DA)| <= (Tr|D|_M/2) osc(psi) <= l osc(psi)`

without requiring D and A to commute. It proves A is the actual compressed multiplication operator, then derives the log-determinant ratio derivative `Tr(DA)` directly by determinant multilinearity and rectangular trace cyclicity. Integration preserves the full determinant ratio.

CTI17–CTI21 instantiate the construction on the actual two bulk intervals with the original full quartet polynomial, Gamma mass, f coefficients and multiplicities. Every Gram is positive because the source is a positive density on intervals; finite mass by itself would be insufficient for arbitrary finite atomic support. All differentiation has an explicit compact dominating bound. Multiplication by the original chi gives the isometry back to the original relation spaces; the lifted projector difference has the same nonzero spectrum. The endpoint density comparison is proved with coefficient l times the exact bulk oscillation, while both original r-dimensional determinant factors remain present.

The fragment adds no claim about the omitted bulk complement or a tensor-uniform limit. Those estimates can use the exact transport inequality and the separately evaluated density oscillation. At r=l, the intersection is the zero space and all arguments still apply.
