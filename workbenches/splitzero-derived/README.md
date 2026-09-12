# SplitZero derived formalization workbench

The implementation extends the existing library in [`formal/splitzero`](../../formal/splitzero), based on the structural and synchronization PRs #4 and #5. It does not fork a new scalar construction, change the frozen manuscripts, or integrate with another owner's repository.

The [mathematical note](../../formal/splitzero/DERIVED_MATHEMATICS.md) gives the exact constructions, proofs, sources, and RH-oriented dependency map. Seven new Lean modules cover reverse reconstruction and intrinsic recovery, actual induced homology maps and their kernels, support-preserving quotient universal properties, the typed differential equation, a nonzero class becoming a nonzero boundary, and operator-balanced finite jets lifted through the original amplitude quotient.

The [audit target manifest](../../formal/splitzero/DERIVED_TARGETS.json) and [`SplitZero derived constructions` workflow](../../.github/workflows/splitzero-derived.yml) specify the acceptance criteria. The PR must identify a successful run at the exact source revision before it is described as validated. Python checker tests are not mathematical proofs.

The sequence toward the proposed arithmetic application is now explicit: operator-balanced theta complexes and their kernel/cone; an equivariant geometric comparison with the required spectral image; duality and two-sided weight bounds on that same image; spectral normalization. The completed algebraic units do not assume the missing global comparison or its purity. Deligne and Connes-Consani source-reading boundaries are recorded in the note. No attached source book, source corpus, or private session transcript is republished.
