## Later working sources: arithmetic endpoint norms and exact window products

[Read the working-source guide](workbenches/tau-arithmetic-endpoint-bounds/README.md) · [Four-volume proof](workbenches/tau-arithmetic-endpoint-bounds/FOUR_VOLUME_THRESHOLD.md) · [Exact product](workbenches/tau-arithmetic-endpoint-bounds/window/WINDOW_PRODUCT_PROOF.md)

For the original theta-function source, the written proof bounds endpoint monic norm ratios by a fixed-packet constant times the degree, including balanced windows. Keeping every interior volume contraction twice yields a sharper exact product and necessary normalized four-volume growth of at least four for any exact off-line quartet packet. The remaining analytic question is an opposing arithmetic volume upper estimate; none is proved here.

These are later GitHub working proofs, not additions to DOI [10.5281/zenodo.22730756](https://doi.org/10.5281/zenodo.22730756). The [frozen 482-page main reader](reader.pdf), [424-page companion](calculation_edition_20260912e/26-splitzero-toda-continuation-424p.pdf) and [published source archives](calculation_edition_20260912e/README.md) remain unchanged. The guide states the degree-endpoint and dagger-stability qualifications and distinguishes written analytic arguments from finite checks.

## Frozen Toda--Gamma edition and its reading routes

[Published DOI 10.5281/zenodo.22730756](https://doi.org/10.5281/zenodo.22730756) · [Paired PDFs and source downloads](calculation_edition_20260912e/README.md)

# Arithmetic zeta packets: quotient volumes, Toda control and gamma convolution

This research edition studies a concrete finite part of the Riemann zeta
function's spectral data. A **packet** is a chosen finite collection of its
zeros, with every selected multiplicity retained. Its polynomial h divides
the completed function g=2xi. The original theta-function source has Mellin
transform g/h. Tensor products of this source represent sums of the selected
zero jets, including their full repeated-root structure.

The purpose is to calculate the cost of those spectral configurations in
the original arithmetic source norm. It is not to choose a favorable new
metric or to assert that an off-critical-line zero exists.

## What to read

- **Main research reader, 482 pages.** The complete literature-and-proof
  synthesis now includes Section 41 on arithmetic source/relation volumes
  and Section 42 on gamma convolution descent. The end of Section 42 proves
  the direct analytic generating-function map into the same Toda input.
- **Split-Zero/Toda companion, 424 pages.** A cumulative, more focused account
  of the source, its cohomological quotient and finite spectral controls,
  with 38 proof chapters and 18 complete source appendices. The new chapters
  calculate the separate source and relation curvature terms, certified
  theta-seed inputs, and an exact Gaussian calibration.
- **Separate full source ZIPs.** These retain the mathematical texts,
  formalization sources and scoped checking records for each reader.
  Earlier published PDFs and archives remain separate downloads.
- **Gamma and endpoint workbenches.** The delivered HTML/Markdown/LaTeX
  argument and its finite checker remain readable separately. The endpoint
  criterion and its gamma-coordinate substitution explain a finite-window
  way to choose one of the existing canonical representatives.

## The attempts, their motivation and their results

| Calculation | Why it was tried | What it establishes |
| --- | --- | --- |
| Exterior trace control | A single-vector bound can miss the combined displacement of many spectral directions. | The finite exterior calculation bounds their aggregate positive trace defect using the same rank-two allowance, with multiplicities and source factors retained. |
| Source and relation volumes | Relations vanish in the quotient, but their source norms still affect the least-norm representatives. | The determinant of the canonical quotient metric is exactly a source Hankel determinant divided by a relation Hankel determinant. |
| Two Toda flows | Both determinant sequences come from exponential deformation of the original arithmetic measure. | Their derivative formulas calculate the source/relation curvature and the original complex cross term. The finite upper estimate retains explicit nonnegative losses. |
| Gamma convolution descent | Computing a new high-dimensional convolution integral for each tensor degree is expensive. | A classical gamma reference, multiplied by the actual arithmetic amplitude, gives an exact all-tensor coefficient formula and an explicit tail majorant. Its relative-fibre component is retained. |
| Analytic generating-function map | The coefficient expansion and the Toda moment function appeared as separate descriptions of the same source. | They are linked by an explicit analytic map and inverse. A degree-N Gram matrix differentiated j times uses only the one-factor coefficients through degree 2N+j. |
| Endpoint degree selection | Bounding every recurrence coefficient in a whole degree window is stronger than selecting one useful canonical degree. | The written finite Jensen argument uses four endpoint quotient volumes and two endpoint polynomial norms. The gamma-coordinate version retains the exact reference and arithmetic correction factors. |

## The quantities are attached to explicit maps

At degree N the source is the original polynomial space, mapped to the cyclic
algebra C[S]/(chi). The relation columns are multiplication by the original
monic polynomial chi. The canonical representative is the unique least-norm
lift for the arithmetic moment matrix. Its correction from a reference lift
is a literal relation; its image is an actual theta boundary, with an explicit
tensor-cochain primitive. The quotient sends `(lambda_N,P)` to
`(lambda_N,[P]_chi)`: the fibre label remains even when the polynomial class
is zero. The unit, all signs, the centre k/2, the total mass and the
repeated-root orders remain in these formulas.

The gamma density is therefore a computational reference, not a substitute
for the zeta-derived measure. The arithmetic amplitude and its phase remain
in the multiplication map. The coefficient transform computes observations
of that same source and retains the orthogonal component removed by the sum
projection.

## Verification and the present quantitative boundary

Written proofs, exact finite regression checks, interval enclosures and Lean
checks have different stated scopes in the accompanying records. The gamma
delivery passed its 17 finite methods normally and under optimization;
independent fixtures also rejected altered mass, multiplicity, conjugation
and relation formulas. These are not interval certificates for arbitrary
arithmetic packets.

PR #22 supplies the checked finite original-Gram trace and projection
formalization: four modules and 50 selected transitive-axiom reports. The
exact reviewed revision was merged, and its three post-merge workflows
passed. PR #23 adds five strictly kernel-checked Toda modules and 30 selected
transitive-axiom reports. It has been merged; its exact source and checking
records accompany the edition. The Jensen/root assembly of its endpoint criterion
is a written proof, not an additional claimed Lean theorem.

The companion's certified numerical inputs concern the **unmodified analytic
seed h=1**, not a nonempty zero packet. This seed has nonzero mass while its
finite arithmetic quotient is zero-dimensional. The Gaussian example is an
explicit calibration, not zeta-zero data.

The outstanding quantitative problem is an upper estimate for the specified
arithmetic determinant/endpoint ratios as tensor and polynomial degrees
grow. The present identities do not prove that estimate. In particular, a
one-sided bound on individual positive correction factors does not bound
their consecutive ratios. No proof or disproof of the Riemann hypothesis is
claimed by this edition.


The exact current assets and retained previous downloads are listed in the [edition index](calculation_edition_20260912e/README.md). The immutable source commit is `a3f7aa023b59e2ecd4d0a590aad912f2ecd86ec7`.
