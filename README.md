# Arithmetic zeta packets: endpoint norms, exact window products and gamma source control

[Published edition](https://doi.org/10.5281/zenodo.22731295) · [Research guide](CURRENT_RESEARCH.md) · [Exact 32-file inventory](calculation_edition_20260913_endpoint_gamma/ALL_ZENODO_FILES.json)

Start with [Split-Zero Cohomology and Arithmetic Weight Control, the current
478-page paper](calculation_edition_20260913_endpoint_gamma/30-splitzero-gamma-continuation-478p.pdf), which is the default Zenodo PDF preview.
It retains the complete cumulative source/cohomology calculations. The
separately readable [512-page integrated reader](reader.pdf) contains the broader
research synthesis. The
[edition page](calculation_edition_20260913_endpoint_gamma/README.md) pairs both PDFs with their exact source ZIPs.

The new calculations keep the original theta-function source, its full mass,
the coordinate `S=k/2+iu`, phases and zero multiplicities. They prove arithmetic
endpoint norm bounds, an exact degree-window product, and a four-volume growth
lower bound for any off-line quartet. An opposing arithmetic volume upper bound
has not been proved; no RH conclusion is claimed.

Read the [complete endpoint proof sources](workbenches/tau-arithmetic-endpoint-bounds/README.md),
[corrected confluent-transfer note](workbenches/tau-confluent-transfer/RESEARCH_NOTE.md),
and [Gamma companion source guide](workbenches/splitzero-tandem/continuations/20260913-gamma/README.md).
The [attempt log](ATTEMPTS.md), [research programmes](RESEARCH_PROGRAMMES.md),
and [Polyclank participation guide](POLYCLANK_PARTICIPATION.md) retain the
broader motivations and the distinction between completed and unfinished routes.

All 28 earlier downloads remain in the [32-file DOI record](https://zenodo.org/records/22731295#files).
The [previous frozen edition](calculation_edition_20260912e/README.md) is unchanged.
Written analytic proofs, finite checks, interval enclosures and strict Lean
results have their separately recorded scopes. Overleaf confirmations remain
historical, and timers remain paused. Source ZIPs are offline downloads.

## Current working sources

The working GitHub sources have advanced beyond the frozen DOI edition:

- [Canonical restriction and finite volume certificates](workbenches/tau-restriction-certificate-formal/RESEARCH_NOTE.md)
  compute how least-norm polynomial representatives change with degree and bound
  the resulting quotient-volume loss using finite matrix traces.
- [Specialization and curvature](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/a4a87844c257485ae6d669f5b3eb6d96b9e8b8d8/workbenches/tau-specialization-curvature-formal/RESEARCH_NOTE.md)
  interpolate those same representatives, retain the kernel and cokernel at the
  boundary, and turn determinant curvature into the finite trace certificate.
- [Theta source and Hochschild trace](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/a4a87844c257485ae6d669f5b3eb6d96b9e8b8d8/workbenches/tau-specialization-curvature-formal/HOCHSCHILD_COMPARISON.md)
  give the exact trace factorization, calculate which finite spectral blocks
  survive restriction to the critical line, and repair the boundary zero Fourier
  mode by retaining it before taking the explicit source-generated quotient.
- [Laplacian numerical-range bound](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/a4a87844c257485ae6d669f5b3eb6d96b9e8b8d8/workbenches/tau-specialization-curvature-formal/LAPLACIAN_PARABOLA.md)
  turns the original metric's measured action defect into a parabolic enclosure,
  without assuming an invariant metric or discarding repeated-zero jets.

PR26 and PR27 are merged working sources. The links for PR27 pin its reviewed
revision; its historical status files describe their original checkpoint.
Written analytic arguments and the selected Lean/finite checks have distinct
scopes. No uniform arithmetic upper estimate or RH conclusion is established.
These continuations are **not included in the frozen DOI PDFs or ZIPs**.
The published preview remains the current 478-page Split-Zero cohomology paper.
