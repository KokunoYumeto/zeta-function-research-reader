# Split-Zero cohomology and arithmetic weight control

Start with [the complete 715-page Split-Zero paper](workbenches/splitzero-tandem/continuations/20260913-deligne/Split_Zero_Cohomology_and_Arithmetic_Weight_Control.pdf).
Its [editable source and build guide](workbenches/splitzero-tandem/continuations/20260913-deligne/README.md)
include the full cumulative argument and original source witnesses, through the
13 September Deligne endpoint continuation. The [research guide](CURRENT_RESEARCH.md)
explains where this cut fits among the working calculations.

The paper studies the Riemann xi function through its original theta-function
source, finite zero packets, and the least-norm representatives of their
arithmetic quotient classes. It retains zero multiplicities, the source's full
mass, the coordinate `S=k/2+iu`, and the canonical quotient metric. The new
chapters calculate endpoint and relation-moment estimates, consecutive degree
windows, cohomological comparisons with Deligne's constructions, and the complete
polynomial-exponential period determinant. The opposing arithmetic volume upper
bound remains unresolved; the paper does not claim an RH proof or disproof.

This source release is an [explicit public derivative](workbenches/splitzero-tandem/continuations/20260913-deligne/PUBLIC_DERIVATION.md):
mathematical texts, PDF and delivery archives retain their exact bytes; private
workstation prefixes in historical evidence are aliased, and a reference-only
cache of copied literature pages is replaced by bibliographic/hash provenance.
Every change is recorded. Historical checks keep their original scope; source
publication is not a new Lean or analytic verification.

The [512-page integrated reader](reader.pdf) remains separately readable.
[DOI 10.5281/zenodo.22731295](https://doi.org/10.5281/zenodo.22731295) is the older
frozen 478/512-page edition, with [its exact PDFs and source ZIPs](calculation_edition_20260913_endpoint_gamma/README.md).
It does **not** contain the new 715-page cut. Its 32 downloads and all older
source releases remain unchanged. The new large source ZIP is kept outside
ordinary Git files; a successor DOI is not claimed here before verification.

The [attempt log](ATTEMPTS.md), [research programmes](RESEARCH_PROGRAMMES.md),
and [Polyclank participation guide](POLYCLANK_PARTICIPATION.md) retain the
motivations, partial successes and unfinished routes. Overleaf confirmations
remain historical and timers remain paused.

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
The frozen DOI preview remains its 478-page Split-Zero cohomology paper; the current GitHub front is the 715-page cut above.
