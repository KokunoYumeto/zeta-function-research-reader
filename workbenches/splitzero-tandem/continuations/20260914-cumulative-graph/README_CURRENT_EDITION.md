# Split-Zero cohomology and arithmetic weight control

## What this edition investigates

This cumulative research manuscript studies how the Riemann zeta function's theta-function source, finite zero-jet algebras and their original relations interact with cohomology and source norms. Its Split-Zero construction keeps a coefficient that is present but zero distinct from a coefficient that is absent. The calculation preserves those distinctions, full zero multiplicities and the original source-to-quotient maps while testing a tensor-amplification strategy inspired by Deligne's work on weights.

The mathematical target is a specific arithmetic determinant expression at four polynomial degrees. The question is whether the geometry and original source relations can control that expression as tensor degree grows. The manuscript does not claim to have found an off-critical-line zero or settled the Riemann hypothesis.

## What was tried, and what it produced

- **Retain the phase defect as a second source component.** The purpose is to keep information lost by the unweighted completion. The resulting completed graph quotient is explicitly nonzero. Its map to the old completion, and the kernel of that map, are both calculated.
- **Separate the sum-coordinate observation from the full tensor observation by an explicit projection.** The remaining mixed component is proved injective for tensor degree at least two. Its original squared norm survives the polynomial-degree limit and becomes a strict subtraction in an endpoint inverse.
- **Keep correlations between the original relation rows.** Exact Schur-complement formulas retain a second negative correction and provide finite lower and upper bounds that improve as more rows are included.
- **Return the graph calculation to the original arithmetic metric.** A signed determinant calculation carries the graph bounds back into the existing four-endpoint equations. This return cost is retained; an improved graph bound is not treated as a free improvement of the arithmetic bound.
- **Compare the generators in their actual metrics.** The comparison computes the entire commutator error, including nilpotent terms and the complex period parameter, instead of treating the metric change as if it commuted with the generator.

## Current result and remaining calculation

The edition supplies explicit maps, full written proofs and finite formulas for the source, mixed quotient, relation correlations and signed arithmetic return. It incorporates these into the earlier receiving statements rather than leaving them as detached appendices. The current four-volume lower estimate is retained.

What remains is an upper growth estimate for the same original arithmetic determinant expression as the tensor degree increases. The proved convergence at fixed tensor degree does not supply that separate estimate. Deligne's cited tensor and cohomological injections are genuine ingredients of the comparison programme; no unconstructed Frobenius comparison is claimed to control the theta-source metric.

## Reading and verification scope

The cumulative Split-Zero PDF is the intended front paper. The accompanying source package retains complete proof bodies and their build dependencies. Earlier mathematical and formalization contributions retain their own stated verification scope; written analytic arguments are not represented as Lean kernel checks. Finite test records are identified as such and do not certify the remaining analytic estimate.

This is the source cut assembled on 14 September 2026; the inherited manuscript title page retains its 13 September date. This introduction does not itself indicate that the cut has been published. Publication and download links belong in the final verified edition record.

## This local built edition

Attribution: KokunoYumeto.

[Read the cumulative PDF](Split_Zero_Cohomology_and_Arithmetic_Weight_Control.pdf) (1,929 pages). The exact PDF and all 279 compiler inputs are bound by the current build and visual-review records. This is a local verified package, not a claim that a remote upload has occurred.

[Complete source](tex/main.tex) · [Source manifest](CURRENT_SOURCE_MANIFEST.json) · [Derivation record](PUBLIC_DERIVATION.md) · [Machine-readable lineage](PUBLIC_DERIVATION.json).

Run `python scripts/verify_public_edition.py` for local file/build/PDF bindings. Run `python scripts/build_paper.py` with Python, PyMuPDF and XeLaTeX for the fixed-source rebuild; historical assemblers are not replayed. A rebuild produces a new runtime receipt and requires its own PDF review.

The inherited 1,624-page reader and superseded records remain under clearly labelled history. New raw FLS/log/auxiliary outputs stay private; the complete TeX sources and current successful build receipt remain public.
