# Coherent tensor boundaries and complete arithmetic jets

This cumulative continuation integrates the complete PR #14 source with the original theta moment and kernel calculations, reconstructs additional historical Hurwitz and Laurent mathematics, and proves the next terminal-energy and joint-source density results. Every original arithmetic coefficient, complete zero multiplicity, spectral coordinate, support, supported zero and external zero remains attached to its declared map.

[Read the complete PDF](Split_Zero_Cohomology_and_Arithmetic_Weight_Control.pdf) · [Complete TeX](tex/main.tex) · [Source and verification manifest](PUBLIC_SOURCE_MANIFEST.json)

The earlier [109-page moment/resolvent edition](../20260912-moments/README.md) remains a separate, unchanged contribution. This **156-page** edition contains sixteen complete proof sections and seven full dated source appendices. The mathematical statements below are proved in the linked sections.

- [Coherent tensor interpolation](tex/coherent_tensor_integration.tex) identifies PR #14's full coefficient matrix with the arithmetic-unit kernel formula. It proves the original reflection, ordered tensor boundary signs, the extra projection for nested tensor packets, and its exact effects on both the Gram matrix and weight form. Actual signed inertia sharpens the tensor spectral bounds; the next-layer maps give the determinant and relative-energy constraints.
- [Joint boundary density](tex/joint_density_dissipation.tex) proves density for the actual total-degree boundary family. Its minimum representatives converge to supported zero while every full jet remains fixed. The complete graph relation and isometric quotient recover those jets. The absolute boundary-energy series sums to the original Gram matrix; the corresponding relative energy has infinite total sum. The same matrices give an accumulated determinant-cost inequality.
- [Terminal energy](tex/kernel_terminal_continuation.tex) proves the exact metric, scalar, determinant and transverse-energy step in the original polynomial packet, including critical/quadrature coincidences. Its rational presentation is related by an explicit isometry. Doubled Taylor algebras supply all coefficients needed to extract the terminal metric from the initial resolvent error and genuine operator tail.
- [The original tesserine channel and arithmetic volume](tex/research_conclusion.tex) are related by the exact formula `epsilon_m² = a_(d+m+1) (1-r_m)(1-r_(m+1))/r_(m+1)`, where `r_m = det G_m / det G_(m-1)` and the original fixed-section metric `G_-1` is retained. For a full four-point zero orbit with multiplicity `mu`, `mu² |c_-+|² <= epsilon_m²`, with the original character `c_-+ = 2(2 beta-1)`. The complete proof and Split-Zero character morphism retain the critical two-point orbit and its supported zero.
- [Historical full-cluster reconstruction](tex/historical_hurwitz_jets.tex) recovers the original compact probability measure from the complete local Hurwitz zero-cluster germ at any nontrivial zeta zero, retaining arbitrary multiplicity. It proves the completed-function residue defect, exact marked Laurent-jet maps and collision kernels. Two distinct prime characters recover the entire finite spectral algebra, with explicit primary kernels and the inverse original spectral coordinate.

The cumulative source retains the certified arithmetic incomplete-gamma moment series, explicit infinite tails, full confluent quadrature, initial-resolvent convergence, metric-departure formulas, historical packet ghost and support-diagram foundations. The [research-state section](tex/research_conclusion.tex) gives the current chain of exact maps and the remaining arithmetic energy calculation. No RH conclusion or missing quantitative estimate is assumed.

## Reproduce the reader and checks

Use XeLaTeX with the packages in `tex/main.tex` and Cambria, Calibri and Consolas fonts. The exact arithmetic checkers require SymPy; the certified interval moment calculation requires python-flint/Arb. From this package directory:

```text
python scripts/build_reader.py
python scripts/check_arithmetic_moments.py
python scripts/validate_pr14_delivery.py
python scripts/check_coherent_tensor_comparison.py
python -O scripts/check_coherent_tensor_comparison.py
python checks/terminal_energy_recurrence.py
python -O checks/terminal_energy_recurrence.py
python checks/terminal_energy_monotonicity.py
python checks/terminal_volume_energy.py
```

The original PR #14 ZIP and all its staged files are included, so the delivery validator can check the source bytes and rerun its deliberate failure controls without access to a private download directory. Public provenance supplies a repository-relative archive locator. The original source files and archive bytes are unchanged; metadata adaptations are recorded in the manifest.

The finite tests supplement the complete mathematical proofs. The monotonicity calibration has its explicitly specified positive measure and packet; its scope and exact relationship to the arithmetic moment construction are proved in the terminal section. The analytic density, infinite-tail, full-cluster and convergence claims have written proofs. No new Lean execution is claimed.

`build/build_receipt.json` pins the PDF and all TeX inputs. `build/qa/visual_review.json` records visual review of that exact PDF. The full source appendices and their original witnesses are provided under `build/` and `sources/`; independent proof reviews are under `logbook/`.
