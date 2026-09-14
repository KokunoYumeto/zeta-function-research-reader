# Split-Zero arithmetic cohomology

Start with [the accepted 1624-page public Split-Zero reader](https://zenodo.org/api/records/22739630/files/39-splitzero-recursive-source-relations-public-reader.pdf/content)
and its [complete editable source and build guide](workbenches/splitzero-tandem/continuations/20260914-recursive-source-relations/README.md).

Split-Zero arithmetic cohomology studies the original theta-function source of finite zero packets, explicit source relations, signed metric control, restricted support and boundary propagation. The construction retains zero multiplicities, original source masses, coordinates and quotient maps. The signed finite approximation converges for each fixed source pair; tensor-uniform arithmetic control remains an active calculation. No proof of the Riemann hypothesis or new Lean kernel verification is claimed.

The [research guide](CURRENT_RESEARCH.md) explains the construction and next
arithmetic calculation. The [public-derivation ledger](workbenches/splitzero-tandem/continuations/20260914-recursive-source-relations/PUBLIC_DERIVATION.md)
records locator-only presentation changes and exclusions. The public PDF was
rebuilt and reviewed as a derivative; it is not described as byte-identical to
the private delivery PDF. Complete mathematical source proofs remain preserved.
Raw private session records, reference-only literature and the raw owner ZIP
are not public payloads. Wrapper ZIPs are not duplicated as ordinary Git blobs.

The [preceding published R62 edition](https://doi.org/10.5281/zenodo.22738226) retains its PDF
preview and all 38 downloads. The [new published DOI 10.5281/zenodo.22739630](https://doi.org/10.5281/zenodo.22739630)
now provides [all 40 separate downloads](calculation_edition_20260914_recursive_source_relations/README.md). The public Split-Zero PDF
is the actual browser preview; the [matching source ZIP](https://zenodo.org/api/records/22739630/files/40-splitzero-recursive-public-sources.zip/content) is an offline download.

Later full-packet formal-boundary, global-ray-monodromy, graph, relation-tail and generator-limit continuations are separate subsequent intakes, not material integrated into this fixed edition. Existing working sources retain their independent proof and CI scopes; their Lean or CI results are not attributed to this public PDF.

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
The GitHub front and current DOI now share the accepted recursive source-relations public PDF/source cut. The preceding R62 DOI and all 38 earlier downloads remain unchanged. Independent working sources retain their own proof and CI scopes.


## PR29: original residue detection and signed metric transfer

[PR29](https://github.com/KokunoYumeto/zeta-function-research-reader/pull/29) is normally merged at
`baef5c29f2bc36101eb74e7fe95c2d8c9e44bb8c`. Its 21 complete contributed files are verified,
and all 14,416 prior leaves, including the DOI mirror, remain unchanged.
The [signed metric-transfer note](workbenches/tau-arithmetic-metric-transfer/RESEARCH_NOTE.md)
and [residue guide](workbenches/tau-residue-rigidity/README.md) calculate
residue detection using the actual source generator, original relation-valued
metric variation, and the signed arithmetic log transfer. All fourteen
reviewed premerge checks and all ten actual merge-push runs were successful.
At the 18:36:16 UTC observation, the two new workflows also had complete
log/source/axiom and negative-control reconciliation: [metric transfer](https://github.com/KokunoYumeto/zeta-function-research-reader/actions/runs/34774694650)
covered 35 strict modules and 60 selected transitive axiom targets;
[residue rigidity](https://github.com/KokunoYumeto/zeta-function-research-reader/actions/runs/34774694642) covered
28 modules and 34 selected targets. The other eight runs have successful
conclusion observations, not a newly claimed full-log or mathematical audit.
These finite identities do not establish a uniform arithmetic bound, and the
contribution remains outside the frozen R57 DOI edition.

## Marked-product and signed four-endpoint working continuation

[Source guide](workbenches/tau-marked-product-four-endpoint/README.md) · [complete mathematical TeX](workbenches/tau-marked-product-four-endpoint/NOTE.tex) · [HTML source](workbenches/tau-marked-product-four-endpoint/index.html) · [provenance and exact changes](workbenches/tau-marked-product-four-endpoint/PUBLIC_PROVENANCE.md)

The aim is to calculate the actual arithmetic/Gamma correction on one common
source and connect the complete tensor packet to an explicit external family.
The reason for retaining the source maps is that auxiliary purity alone does
not control the original theta-source norm. The new note constructs the
rank-d^k external family and its marked-fibre map, retains the cyclic parameter
defect, derives the signed integral and its full relation-valued derivatives,
and proves a finite midpoint error bound. Full mass, Taylor units, repeated-zero
jets, supported zero versus absence, and the ordinary four endpoint degrees
are retained.

The positive endpoint-shell operators each have trace 2q, rank q+1, and
spectrum 1, 2 with multiplicity q-1, 1. The trace is not a rank-2q assertion.
The sealed source is unchanged; this clarification makes the operator meaning
explicit in this guide. A uniform arithmetic upper estimate remains unproved.
No RH/GRH conclusion, faithful Frobenius/metric transfer, or programme-wide
failure theorem is claimed.

[Fresh finite-check receipts](workbenches/tau-marked-product-four-endpoint/checks/PUBLIC_REPLAY.json) record 14 tests
passing in both Python modes and the intended negative controls. They are not
Lean or interval certificates. The [complete source/hash ledger](workbenches/tau-marked-product-four-endpoint/PUBLIC_FILE_CHANGES.json)
retains the public-privacy changes and discloses exclusion of the unreviewed
integration patch; both mathematical scripts and the full note remain included.

No existing GitHub Pages site was verified. The HTML link above is a source
file, not a claimed rendered online reader; no hosting provider or configuration
was added. This HTML/TeX working edition creates no PDF solely for a preview and
does not replace the [historical 765-page R57 DOI edition at the marked-source publication checkpoint](https://doi.org/10.5281/zenodo.22736292),
its preview, any of its 36 downloads, or its reading links. Its rendered-reader
link belongs in a later frozen edition only after a real route is verified.

## Supplementary accepted research sources: finite certification and mixed control

These two source packages supplement the ongoing research. They are outside the
fixed 821-page R62 paper and are not silently assigned to the historical 765-page
DOI. The main Split-Zero reading front remains unchanged.

### Original theta moments and finite Hankel certification

[Read the unchanged 47-page paper](workbenches/splitzero-tandem/continuations/20260913-accepted-followups/original-theta-certification/Tau_Theta_Hankel_Complete_Proofs.pdf) · [Distribution and scope](workbenches/splitzero-tandem/continuations/20260913-accepted-followups/original-theta-certification/PUBLIC_DISTRIBUTION.md)
· [Source and reproduction guide](workbenches/splitzero-tandem/continuations/20260913-accepted-followups/original-theta-certification/README.md)

The original theta integral, its mass, signed summands and both factors of two
are retained through the moment and logarithmic-coefficient maps. The supplied
certificate reports positive lower endpoints for all 32 pivots and 32 leading
determinants of the original 16-by-16 H15 and first-shift matrices. It uses 33
even moments M0 through M64, N=20, L=4, 1024-bit ball integration and the
independent 2^4096 integer grid with 1,400 endpoint pairs. The
[TC proof](workbenches/splitzero-tandem/continuations/20260913-accepted-followups/original-theta-certification/proofs/TC.tex), [nine supporting proof bodies](workbenches/splitzero-tandem/continuations/20260913-accepted-followups/original-theta-certification/support_reader/main.tex),
[analytic tail/integration contract](workbenches/splitzero-tandem/continuations/20260913-accepted-followups/original-theta-certification/calculation/CERTIFIED_ORIGINAL_THETA_HANKEL.md)
and [exact replay source](workbenches/splitzero-tandem/continuations/20260913-accepted-followups/original-theta-certification/verify_exact_rational.py) remain complete.
The finite certificate does not establish all-dimension positivity or RH;
this publication step does not rerun its mathematical checks.

All 111 owner-archive files remain byte-exact. The full 114-file
[public distribution](workbenches/splitzero-tandem/continuations/20260913-accepted-followups/original-theta-certification/DERIVATIVE_MANIFEST.json) preserves the original proofs
and evidence with [disclosed provenance](workbenches/splitzero-tandem/continuations/20260913-accepted-followups/original-theta-certification/PUBLIC_PROVENANCE.json).

### Deligne mixed-control continuation

[Read the Markdown overview](workbenches/splitzero-tandem/continuations/20260913-accepted-followups/deligne-mixed-control/DELIGNE_USAGE_OVERVIEW.md) · [Complete editable LaTeX reader](workbenches/splitzero-tandem/continuations/20260913-accepted-followups/deligne-mixed-control/COMPLETE_CONTROL_WORK.tex)
· [Source guide](workbenches/splitzero-tandem/continuations/20260913-accepted-followups/deligne-mixed-control/README.md) · [Public derivation](workbenches/splitzero-tandem/continuations/20260913-accepted-followups/deligne-mixed-control/PUBLIC_DERIVATION.md)

The complete seven-body reader develops [coefficient-face attachment](workbenches/splitzero-tandem/continuations/20260913-accepted-followups/deligne-mixed-control/sources/MCF.tex),
[spectral-jet tensor and dual filtrations](workbenches/splitzero-tandem/continuations/20260913-accepted-followups/deligne-mixed-control/sources/MW.tex),
the [length-two relative extension](workbenches/splitzero-tandem/continuations/20260913-accepted-followups/deligne-mixed-control/sources/MRE.tex), and the
[singular boundary connection and exact period determinant](workbenches/splitzero-tandem/continuations/20260913-accepted-followups/deligne-mixed-control/sources/BC.tex).
Each coefficient records absence separately from a supported zero; the maps
attach those masks to the original theta complex, retaining its boundary
primitives and the proper-source V/W kernel.
The arithmetic extension remains nonsplit; the added diagonal splitting is
not substituted for the original arithmetic action. The connection keeps both
polar orders and the metric comparison uses the original theta-source Gram.

The earlier [AW1--23](workbenches/splitzero-tandem/continuations/20260913-accepted-followups/deligne-mixed-control/sources/AW.tex) is included in full: AW7 gives the
window spectra, AW14 the final (2q-1) log kappa bound, and AW13 the stronger
full-spectrum expression. [SP8--10](workbenches/splitzero-tandem/continuations/20260913-accepted-followups/deligne-mixed-control/sources/SP.tex) gives the complementary
projection-overlap/common-range refinement, not a replacement claim of novelty
or universal dominance. The same-source operator correspondence, original
masses and separately typed AW isometry remain explicit. PR29's existing
secants, relation-valued derivatives and signed trace-power controls retain
their attribution. The [original marked-product note](workbenches/splitzero-tandem/continuations/20260913-accepted-followups/deligne-mixed-control/sources/MARKED_PRODUCT_ORIGINAL_NOTE.tex)
is preserved, with errata stated outside it.

Actual inertia, Stokes/extension maps and growing-family arithmetic estimates
remain work to do; no uniform bound or RH conclusion follows. All 36 accepted
public files are retained, with six disclosed locator-only evidence derivatives.
This is a source-only edition: no PDF is supplied or created, and no fresh
compilation or visual QA is claimed. Use the direct Markdown/LaTeX links above
for reading; its ZIP is an offline source archive, not a preview. Existing
rights, notices, earlier publications and reader roles remain unchanged.


## Earlier published reader introduction (historical)

The following earlier introduction records its own fixed source cut and DOI;
its use of “current” belongs to that historical edition.

# Split-Zero cohomology and arithmetic weight control

Start with [the 821-page R62 Split-Zero paper](https://zenodo.org/api/records/22738226/files/37-splitzero-periodized-residue-continuation-821p.pdf/content),
[published DOI 10.5281/zenodo.22738226](https://doi.org/10.5281/zenodo.22738226), and
[all 38 separate downloads](calculation_edition_20260913_periodized_residue/README.md).
The pertinent PDF is the actual Zenodo browser preview; the matching
[public source ZIP](https://zenodo.org/api/records/22738226/files/38-splitzero-periodized-residue-public-sources.zip/content) is an offline download, not a preview.

The 821-page R62 Split-Zero reader develops periodized source recovery and density, finite-circle curvature with quotient compensation, the circle/critical-observation diamond, and residue-constituent derivative and curvature formulas. It keeps the original theta-function source, zero multiplicities, source mass, coordinate S=k/2+iu and least-norm quotient metric. The uniform arithmetic growth estimate remains an active unresolved problem; no RH proof or closure is claimed.

Periodized observations recover the specified arithmetic source and identify
the relevant completed spaces. The finite-circle formulas calculate curvature
with the compensating quotient terms; the observation diamond compares circle
and critical-line maps. Residue-constituent formulas track derivatives and
curvature without dropping multiplicities, full source mass, signs or
orientations. These calculations expose what the remaining uniform arithmetic
growth estimate must control; they do not supply that unresolved bound.

The [research guide](CURRENT_RESEARCH.md), [editable source/build guide](workbenches/splitzero-tandem/continuations/20260913-periodized-residue/README.md)
and [public-derivative ledger](workbenches/splitzero-tandem/continuations/20260913-periodized-residue/PUBLIC_DERIVATION.md) retain the
proof dependencies, 47 complete source witnesses and exact privacy disclosures.
The source contains 4,926 files. Mathematical texts, the PDF and nested delivery
archives keep their accepted bytes. The raw owner ZIP is not a public payload.

This fixed PDF/public-source cut ends at R62. Later holonomy, mixed-control (TA/AT/AW), and original-theta certification cuts are separate and excluded. Separately indexed GitHub working sources, including PR29 and the marked-product continuation, retain their own proof, finite-check and CI scopes; their presence in this repository does not confer certification by this DOI.

The [historical 765-page DOI](https://doi.org/10.5281/zenodo.22736292) and all its 36
downloads remain unchanged; this successor adds only PDF37 and ZIP38.
The [attempt log](ATTEMPTS.md), [research programmes](RESEARCH_PROGRAMMES.md)
and [participation guide](POLYCLANK_PARTICIPATION.md) retain earlier routes,
partial results and active problems. Overleaf confirmations remain historical
and timers remain paused.

