# Validation

The new written arguments use the original theta/Mellin identities and explicitly specified inverse ODE. They have not been Lean-checked. Prior PR #12's successful certificate is used only at its stated coefficient/retraction/topological interfaces.

Fresh local checks: nineteen unittest methods passed with exact SymPy rational/complex arithmetic, normally and under `python -O`. The resulting JSON files agree byte for byte. An intentionally false extra test failed with exit status 1 in both modes. No Python assert statement is used as a mathematical check.

The fixtures are explicitly finite discrete measures and polynomial multipliers. They include a nontrivial local unit, repeated-root jets, nested packet maps, two-variable total-degree relations, same-metric reflection, a nonzero off-line model defect, source-preserving Gram changes, and the Koszul boundary signs. The off-line fixture is not an arithmetic zeta counterexample.

The checks do not certify infinite integrals, gamma bounds, polynomial density, analytic source-space mapping, a uniform arithmetic upper estimate, or RH. Those analytic conclusions that are stated in the note have written proofs with their inputs identified.

The actual uploaded Deligne TeX excerpts were read directly. No OCR or PDF extraction was used. External gamma input: DLMF 5.11.9. Other orthogonal-polynomial and inverse-moment references were checked for context/priority, not imported as unread theorems.

No private source literature, transcript, credential, or font file is published in the GitHub contribution.
