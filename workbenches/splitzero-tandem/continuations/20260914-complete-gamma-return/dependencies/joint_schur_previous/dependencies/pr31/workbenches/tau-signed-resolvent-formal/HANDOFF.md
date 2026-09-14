# Handoff: current source control and proper-source kernels

This work follows main `331ccd30185a98bfc8fde8102cf09b9c2add4d6b`, the complete ISM1–43 source-control chapter, and corrected PR30 head `aa6473075928b0316c49d50c163697c4ab98d004`. Preserve those sources and the original scalar, theta quotient, full jets, arithmetic unit and positive source forms. STATUS.md pins observed execution; RESEARCH_NOTE.md gives the complete mathematical construction; DEVELOPMENT.md retains failed proof elaborations and their repairs.

## Ready interfaces

`CanonicalSignedResolvent.canonical_properties` derives the traceless, original-metric-self-adjoint contrast from four **actual canonical residual sections**, allowing different relation dimensions. `canonical_tangent` ties its signed pairing to the four actual quotient-Gram tangents. `canonical_resolvent_interval` inserts the constructed finite Neumann polynomial and its exact `H^(L+1) X` remainder into the centered trace interval.

`SpectralResidual.residual_energy` proves the equality between the actual original-coordinate centered residual energy and its complete spectral variance. The diagonalization is supplied by two explicit equations for a `MetricFrame` that satisfies both inverse laws and `W*W=M`; it is not an independent replacement matrix. `signed_error` composes that equality with the proved weighted Hilbert–Schmidt inequality and the elementary geometric bound. `ResolventSeries.exists_stopping_degree` proves finite stopping for a fixed contraction constant and source-dependent error constant.

`RestrictedBoundary` constructs the natural isomorphism between the original quotient of full-source-boundary pullbacks by the smaller admitted boundaries and the kernel of the original quotient comparison. Both inverse total maps and the exact original quotient square are proved. Its image is tested against the receiving **supported zero**, `qf(y)=e qf(y)`, not external absence. A full-source primitive is not thereby a primitive in the proper admitted source. Noninjective transports are allowed; present empty inner faces remain distinct from global absence.

## Next quantitative input

Supply certified original arithmetic endpoint matrices and an explicit simultaneous diagonalization witness, or extend the proof to construct that witness from the generalized positive eigenproblem. The present module takes its defining equations as input; it does not claim a verified general numerical eigenvalue solver.

For an integrated endpoint certificate, preserve the exact signed integral of the finite center and certify its numerical integration error separately. The current source proves the nested-flag bound `Z_x <= 8q-6`; formalizing that bound and the compact-path integration step would provide a uniform-in-x error for each fixed endpoint pair. Do not replace uniformity over x for a fixed pair by uniformity over tensor degree k or over arithmetic packets. Neither the existence of the finite approximation nor auxiliary finite-field purity gives that latter bound.

For the proper-source diagram, instantiate the already specified full tensor theta primitive, its ordered insertions and both Koszul signs. Check admission into the proper boundary space rather than importing full-source exactness as proper-source exactness. The new quotient-kernel equivalence then tracks every retained class and every transition that kills one.

## Collaboration and publication

The development branch is `astra/signed-resolvent-checkin-20260914`; it preserves current main and PR30 ancestry. Only that branch was updated. This is an additive formalization contribution, not a new publication cut or a main merge. The user requested continuing repository check-ins; hourly notifications are set for substantive source, review and CI changes, without autonomous merges or publication.
