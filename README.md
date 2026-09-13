# Split-Zero cohomology and arithmetic weight control

Start with [the complete 715-page Split-Zero paper](https://zenodo.org/api/records/22732414/files/33-splitzero-period-deligne-continuation-715p.pdf/content).
[Published edition, DOI 10.5281/zenodo.22732414](https://doi.org/10.5281/zenodo.22732414) ·
[All 34 separately downloadable files](calculation_edition_20260913_deligne/README.md) ·
[Editable source and build guide](workbenches/splitzero-tandem/continuations/20260913-deligne/README.md).

The paper studies the zeros of the Riemann xi function using its original theta-function
source and the least-norm representatives of finite arithmetic quotient classes.
It retains zero multiplicities, the source's full mass, the coordinate `S=k/2+iu`,
and the canonical quotient metric. The cumulative argument calculates endpoint and
relation-moment estimates, consecutive degree windows, Deligne cohomological
comparison maps and the complete polynomial-exponential period determinant.
The opposing arithmetic volume upper estimate remains unresolved; this is not
a claimed RH proof or disproof. The [research guide](CURRENT_RESEARCH.md) explains
the calculations, their motivations, and what remains unfinished.

The [public source ZIP](https://zenodo.org/api/records/22732414/files/34-splitzero-period-deligne-public-sources.zip/content) is an offline download; the readable preview is
the Split-Zero PDF above. Its [public-derivative ledger](workbenches/splitzero-tandem/continuations/20260913-deligne/PUBLIC_DERIVATION.md)
records private-workstation locator aliases and the omission of a reference-only
cache of copied literature pages. Mathematical texts, PDFs and nested delivery
archives retain their exact bytes. The [source commit](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/8572a3a05be6cbcb935b05262bafef9d686072ef/workbenches/splitzero-tandem/continuations/20260913-deligne)
and archive hashes identify the same 3,954-file public source selection.

This edition preserves every one of the preceding 32 downloads and adds the
715-page paper and its public source ZIP. The [512-page integrated reader](reader.pdf)
and [older 478/512-page DOI edition](https://doi.org/10.5281/zenodo.22731295)
remain separately readable and unchanged. No large wrapper ZIP is duplicated in Git.

The [attempt log](ATTEMPTS.md), [research programmes](RESEARCH_PROGRAMMES.md), and
[Polyclank participation guide](POLYCLANK_PARTICIPATION.md) record the motivations,
partial successes and unfinished routes. Overleaf confirmations remain historical;
timers remain paused.

## Current working sources


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
The later PR27 continuation and SGA/Hochschild SC/CC reader increment are outside the frozen 715-page PDF/source cut. The Zenodo preview and GitHub front now show the same 715-page Split-Zero paper.
