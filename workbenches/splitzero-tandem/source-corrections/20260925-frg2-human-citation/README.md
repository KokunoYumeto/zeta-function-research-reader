# Human-source correction for the Gamma-polynomial calculation

This edition repairs one point-of-use omission in the Split-Zero zeta programme's cumulative analytic papers. The density, recurrence and polynomial norms in **FRG2** belong to the classical Meixner–Pollaczek family. Earlier editions already contained the human-source bibliography and the exact comparison in HPS1–4, but FRG2 itself referred only to project notes. The added paragraph puts that credit beside the formula where it is used.

This is a citation correction, not a new mathematical result or an RH claim. The complete previous equations, arguments, source credits and historical edition notices remain. Deleting the explicitly marked citation inserts recovers every predecessor byte, as recorded in [the source comparison](CITATION_CHANGES.json).

## Read the corrected papers

- [Cumulative paper, 837 pages](accepted-cumulative/14_CURRENT_KERNEL_AND_MULTIPLICITY_PROOFS.pdf), with [complete LaTeX](accepted-cumulative/14_CURRENT_KERNEL_AND_MULTIPLICITY_PROOFS.tex). The added citation is on page 749.
- [Full receiving-proof supplement, 263 pages](accepted-supplement/FULL_RECEIVER_PROOF_SUPPLEMENT.pdf), with [complete LaTeX](accepted-supplement/FULL_RECEIVER_PROOF_SUPPLEMENT.tex). The added citation is on page 89.

Both PDFs were rebuilt with three XeLaTeX passes. Citation keys resolve, the new external source link is present, and the changed pages and following pages were visually inspected. This is a scoped citation/build check, not a fresh independent verification of every preceding theorem.

The same citation is integrated into the complete editable [joint note](accepted-joint-note/09_UPDATED_JOINT_NOTE.tex), [signed-return paper](accepted-signed-return/10_UPDATED_SIGNED_RETURN.tex), [later kernel-degree cumulative](later-kernel-cumulative/14_CURRENT_KERNEL_AND_MULTIPLICITY_PROOFS.tex), and [retained proof compilation](retained-proof-compilation/RETAINED_COMPLETE_PROOF_SOURCES.tex). These four sources were not separately rebuilt as PDFs for this citation-only edition. The retained compilation contains two inherited copies of the passage, both corrected.

## Human source and exact comparison

T. H. Koornwinder, R. Wong, R. Koekoek, R. F. Swarttouw and W. P. Reinhardt, *NIST Digital Library of Mathematical Functions*, Chapter 18, version 1.2.8 (15 September 2026): [weight and norms, 18.19.6–9](https://dlmf.nist.gov/18.19#E6), [recurrence, 18.22.8](https://dlmf.nist.gov/18.22#E8), [generating function, 18.23.7](https://dlmf.nist.gov/18.23#E7).

The comparison retains λ = s/4, x = y/2, φ = π/2, p(r,s;y) = r! Pᵣ⁽ˢ⁄⁴⁾(y/2;π/2), dy = 2 dx, the full mass Mₛ = (2π)^(s/2), and the original complex-coordinate phase. The complete TeX, including HPS1–4, gives the formulas without shorthand. This credit concerns the classical polynomial input; it does not attribute the programme-specific conductor or first-row bounds to the DLMF authors.

DLMF's source notes identify Mourad E. H. Ismail's *Classical and Quantum Orthogonal Polynomials in One Variable*, 2009 corrected reprint of the 2005 original, equations (5.9.1), (5.9.3), (5.9.8) and (5.9.9), for the relevant formulas. The leading coefficient also has DLMF's derivation from 18.20.10. Ismail's book was not independently read for this correction; that ancestry is explicitly source-reported.

## Preserved editions and the wider programme

The [837/263 predecessor](https://zenodo.org/records/22819902), [later kernel-degree source](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/914b9aab530b7e6c1d112a236b51fa527c9c0538/workbenches/splitzero-tandem/continuations/20260921-kernel-degree-steps/cumulative/14_CURRENT_KERNEL_AND_MULTIPLICITY_PROOFS.tex#L62558), and [retained-source witness](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/9104d852c6bc5b79e6fc4588c403128a40b7fda3/workbenches/splitzero-tandem/continuations/20260922-arithmetic-probe-mass/RETAINED_COMPLETE_PROOF_SOURCES.tex#L72180) remain unchanged. Their original dates are historical dates, not dates assigned to this correction.

The programme's more recent cohomology, positive-quotient and character-lifting work remains in the [three-task edition](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts). This citation edition does not replace that mathematics or imply that newer owner handoffs were included there. The [main repository](https://github.com/KokunoYumeto/zeta-function-research-reader) retains the full project description, sources, formalization and research reports.
