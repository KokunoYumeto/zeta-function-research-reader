# Programme state — 12 September 2026

## Retained base

`G(Z) -> Z`, with infinite target, and its square to `G(C) -> C`, remain attached
to the absolute tau base. Coefficients, relations, quotient topology, generator
`D=-x d/dx`, Mellin exponent, factor `g=2 xi`, full jets, and support masks are not
changed. Relations become `e`-zeros at specified later supports; tau is absence.

## New results in this continuation

- An explicit isomorphism from the highest orthogonal polynomial degree to the
  actual next theta-relation layer: `b=Tplus-R F`. Its Gram is `Omega+F*G F`.
- Exact one-layer updates of representative, Gram, inverse Gram, and determinant.
- A highest-degree Christoffel--Darboux displacement for the actual inverse
  interpolation matrix. It carries the original `Y,Crel` maps and minus sign.
- A proved finite upper control `epsilon <= 2 sqrt(Gamma lambda)`, with both
  constants defined from the arithmetic recurrence and highest-layer jets.
- A signed cochain projector whose top cohomology is the ordinary symmetric
  tensor summand. It retains every repeated eigenline and the full complement.
- Exact orbit-sum matrices, including all orbit factorials, reducing target
  dimension `d^k` to `binomial(k+d-1,d-1)` on the selected summand.
- The highest relation-layer dimension on that summand is `p_at_most_k(M+1)`.
- A fully explicit degree-two nilpotent calibration: joint total degree four
  has excess `sqrt(7/2)` versus `sqrt(6)` for the contained degree-(2,2) family.
  A second calibration records nonmonotonicity, so this is not promoted to a
  universal convergence theorem.

## What has NOT been established

No uniform arithmetic sublinear tensor bound, RH/GRH, infinite trace-class result,
vanishing of the global balanced kernel, or universal geometric purity theorem.
No new Lean run. No arithmetic quadrature certificate. The actual trace contribution
of the symmetric complement is retained, not dropped. Auxiliary polynomial coordinate
changes and calibration masses are written explicitly.

## Files and execution

See VALIDATION.md, HANDOFF.md and check_frontier_control.py. The successful tests
are finite algebraic regressions. INTEGRATION.patch is add-only against the exact
read PR #14 head. Remote state is recorded separately; no remote write was made
by this continuation.
