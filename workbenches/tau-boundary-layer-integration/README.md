# Tau boundary-layer integration

Additive formalization on verified PR #12, coordinated with the owner-supplied rank-two note and PR #13. The six new Lean modules preserve the existing scalar and reconstruction libraries.

- `../../formal/splitzero/SplitZeroSupportChange.lean`: support-changing total morphisms.
- `../../formal/splitzero/SplitZeroJointHomotopy.lean`: every classified homotopy on the actual four-mask chart.
- `../../formal/splitzero/SplitZeroRelationLayer.lean`: quotient transport, its one-dimensional kernel, and the orthogonal relation-layer equivalence.
- `../../formal/splitzero/SplitZeroOrthogonalControl.lean`: actual Gram minima, source-jet positivity, one-layer boundary contraction, and rank-one update.
- `../../formal/splitzero/SplitZeroRankTwoControl.lean`: rank-two factorization, eigenvector transfer, and scalar root calculation.
- `../../formal/splitzero/SplitZeroBoundaryIntegration.lean`: packet-projector commutator and supported quotient transport.

`MATHEMATICS.md` gives exact proofs, source attribution, and the remaining analytic and spectral-wrapper obligations. Execution status and the exact verified commit/run are recorded in the draft PR. The existence of these files is not itself a verification certificate.

The source is the owner's SplitZero programme. The contribution adds formal proofs and reuses Mathlib's quotient, orthogonal-projection, and Gram-matrix infrastructure. It is not a claim of mathematical priority for standard linear algebra.

Nothing is submitted to Sneed, and no main branch is merged.
