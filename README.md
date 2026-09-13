# Split-Zero cohomology and arithmetic weight control

Start with [the complete 765-page Split-Zero paper](workbenches/splitzero-tandem/continuations/20260913-sga-connes/Split_Zero_Cohomology_and_Arithmetic_Weight_Control.pdf) and its [editable source and build guide](workbenches/splitzero-tandem/continuations/20260913-sga-connes/README.md).

The 765-page Split-Zero paper retains the original theta-function source, zero multiplicities, full source mass, the coordinate S=k/2+iu and the least-norm quotient metric. Through R57 it adds the explicit Hochschild comparison kernel, constituent curvature and Laplacian control to the endpoint, period and determinant calculations. A uniform arithmetic upper estimate is not established; no RH conclusion is claimed.

The source starts with the completed Riemann xi-function, divides out a selected finite zero packet with every zero order retained, and measures its inverse Mellin theta source in L². Polynomial relations are kept before taking the arithmetic quotient; the representative of each quotient class is the one of least norm in the specified source. This is the source of the metric used below, not a freely selected replacement metric.

The [research guide](CURRENT_RESEARCH.md) explains the calculations and remaining estimate. The [public-derivative ledger](workbenches/splitzero-tandem/continuations/20260913-sga-connes/PUBLIC_DERIVATION.md) records narrow historical locator aliases and a reference-only exclusion; mathematical texts, PDFs and nested delivery archives retain their owner bytes.

[The earlier 715-page DOI edition](https://doi.org/10.5281/zenodo.22732414) and [all 34 separate downloads](calculation_edition_20260913_deligne/README.md) remain unchanged. This GitHub source promotion does not claim a successor DOI; that link will be added after actual publication and readback. No wrapper ZIP is uploaded into ordinary Git blobs.

The [attempt log](ATTEMPTS.md), [research programmes](RESEARCH_PROGRAMMES.md) and [participation guide](POLYCLANK_PARTICIPATION.md) retain motivations, partial results and unfinished routes. Overleaf confirmations remain historical and timers remain paused.

## Current working sources

- [PR28: quotient, residue and period transport](workbenches/tau-split-integration/RESEARCH_NOTE.md) retains both transition defects in the original maps. Its eight actual merge-push workflows completed successfully; this is a status observation, not a newly performed full-log or analytic-proof review.



These working-source records retain their separately stated proof and CI scopes:

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
The SGA/Connes continuation is now included through R57 in the 765-page GitHub cut above. The frozen Zenodo edition remains the 715-page cut. Later work is not part of either fixed cut.
