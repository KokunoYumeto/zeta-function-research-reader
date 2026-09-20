# Native spectral action: complete finite calculation

The original outgoing arithmetic relation now has an exact trace-action description in the same attained quotient metric. The calculation starts at the native selfadjoint compression A and follows T(t) = A − tQ to the original multiplication operator M at t=1. It retains the full arithmetic characteristic polynomial, every original repeated root, the original S = k/2 + i u coordinate, and the physical jet injection.

## Complete proofs and checks

- NATIVE_SPECTRAL_ACTION.tex: complete SA1–43, 30,046 bytes; SHA-256 8a88c5c7a51d00f802646754427c80e3af668909f767a1b10e96104df6e61b47.
- verify_native_spectral_action.py: SHA-256 94c51edcd9948bf5c36f5a2d0b305753de7ec7bb4f87e236c441f3d5c2cad791.
- CHECKS_NORMAL.json and CHECKS_OPTIMIZED.json: both passed 600 exact symbolic checks and four deliberate-failure controls, with byte-identical SHA-256 84885a72b1e3e3a809d481969222dd43a58bdae976ea56621655236cf71c94f0.
- Python 3 in the existing environment, SymPy 1.13.1. All equality checks use explicit exceptions, so optimization does not disable them.
- No source rendering, PDF reading, compilation, or publication was performed. Figure data and complete proof locators are in FIGURE_SPEC.md for the parent task.
- SOURCE_FUNCTION_CLASS_CHECK.tex proves the coefficient discrepancy inside the human source's actual function class E^0, using x² exp(−x²) and its exact Fourier transform. SHA-256 901d544632856c44a4bf4b73f0b64096c9c729d25881c7bc0ca92b9af0503236.
- Independent full metric derivation: independent_metric_curvature/RANK_ONE_METRIC_CURVATURE.tex, MC1–MC35, SHA-256 355c050f66fa2676093291f455e5aef3b0ab6e350e35203de4ac64ddeed610ee. Its normal and optimized runs each pass 223 exact checks and 22 negative controls.
- Independent endpoint, multiplicity and phase proof: independent_metric_curvature/INDEPENDENT_ENDPOINT_CHECK.tex, EC1–EC15, SHA-256 6ea313e182d5707fb62805a925f9bcba762106dc0f3152a8d34a5a58ed45476f. Its normal and optimized checker runs each pass 239 exact checks and six negative controls. Both independent TeX files were read completely by the main derivation agent; no correction to SA32–SA43 was found.

## What is calculated

SA10–SA11 prove from polynomial products that the cyclic n-th trace derivative with divided differences of F' has coefficient (n−1)!, not n!. The statement of Connes–van Suijlekom's lemma has the extra factor; its repeated-node proof and subsequent second-derivative calculation are compatible with the corrected coefficient. This is a bounded coefficient correction, not a rejection of the paper.

SA13–SA17 give the exact determinant, resolvent and trace map:

    det(zI − T(t)) = (1−t) det(zI − A) + t chi_u(z).
    tr F(T(t)) − tr F(A)
      = − coefficient(z^−1) of F'(z) log(1+t kappa(z)).

Here kappa(z) is the actual scalar outgoing resolvent ell(zI−A)^−1 r. No common factor of the full polynomial is discarded. SA41 also calculates all derivatives at t=1 without requiring the original multiplication operator to be diagonalizable.

SA18–SA24 calculate what native parity and Q²=0 actually remove. For example, the quadratic holomorphic trace has no second derivative, but the quartic trace retains the term 2t²(ell A r)².

SA27–SA31 and SA42 give the exact connection to the existing arithmetic control:

    H(t) = tr(T(t)^dagger_G T(t)).
    H''(t) = 2 epsilon².
    H(t) − Re tr(T(t)²) = t² epsilon².
    L(t)² ≤ t² epsilon² = t² H''(t)/2.

L(t) counts the full aggregate displacement to the right of Re S = k/2, including algebraic multiplicities. The selfadjoint dilation uses the specified metric G direct-sum G and gives its own complete determinant, not an identification with the original characteristic polynomial.

SA38–SA43 give exact finite comparison-measure examples. They are explicitly not fabricated arithmetic zero packets. A parity-respecting example also shows why all holomorphic trace data alone do not determine the retained metric curvature; the actual coordinate change and mixed derivative are computed.

## Human source and reading coverage

Alain Connes and Walter D. van Suijlekom, Quadratic Forms, Real Zeros and Echoes of the Spectral Action, arXiv:2511.23257v1, original author LaTeX Araki-final-oct25.tex. Read directly for this subtask: the complete Section sect:sa, including lem:sa and prop:der-sa. Source hash 0357a6123b7b3a2ba2e058458f5267eef1c4ad6abb051af559015b86ae2aa111. Canonical routing record supplied by the parent's existing index: PUBUNIT-D7A365B74D8E7FFC9D79765B.

Programme predecessor: NATIVE_SECULAR_RECEIVER.tex, NS1–37. The metric and outgoing correction used here are derived again in SA1–SA7 rather than treated as an unnamed supplied object.

## Exact scope

This is a finite trace/resolvent/metric calculation. It does not prove a growing-degree estimate or decay of epsilon. The native arithmetic measure is retained, while the executable tests verify the finite identities on exact algebraic models rather than claiming numerical evaluation of that measure or kernel certification of the analytic paper.

The expanded checker includes a nonzero size-two Jordan endpoint at zero, and a four-dimensional comparison-measure quotient with characteristic and minimal polynomial (z²+1)². The latter retains both size-two nonreal Jordan blocks, the complete metric, epsilon²=3868/21 and the full algebraic-multiplicity aggregate L=4. The independent endpoint proof establishes its polynomial derivative formula for every polynomial degree and every derivative order, beyond the finite executable test list.
