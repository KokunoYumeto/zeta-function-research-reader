# Verification boundary

The authoritative execution record is [PR26](https://github.com/KokunoYumeto/zeta-function-research-reader/pull/26): it gives the exact implementation SHA, completed run/job, transitive axiom reports and independent finite checks. A pending or failed run is not a certificate. Earlier failed proof-script attempts remain in history.

The four source modules are `SplitZeroRestrictionTransport`, `SplitZeroRestrictionSource`, `SplitZeroRestrictionLogCertificate`, and `SplitZeroRestrictionSpectrum`. The two audits select 26 and 7 named theorems. Both fail-closed checkers reject missing, duplicated, additional or unapproved axiom reports. Allowed axioms are only `propext`, `Classical.choice`, `Quot.sound`.

The unchanged dependency environment is Lean 4.31.0 and Mathlib fabf563a7c95a166b8d7b6efca11c8b4dc9d911f. Individual source checks use `--trust=0 -DwarningAsError=true`. The workflow also rebuilds the five immediate Toda/window dependencies, reruns PR25's ten-target audit and its seven exact tests, and imports them with the new restriction modules in one environment. It does not represent this as rerunning every historical library audit.

The 16-method independent checker uses exact finite source matrices and rational logarithm enclosures. The degree-64 display is independently checked against a rational logarithm enclosure and rounded outward. None of these are actual zeta-zero packets or interval evaluations of arithmetic moment integrals.

The uploaded restriction report was read in full. Its archive and its supplied 19-method checker were not independently opened/executed because the local runtimes failed. The parallel Gamma transcript supplies progress claims, not the full proofs of those results; they are not reclassified as this contribution's certificate.

Weighted spectral existence and the original arithmetic source/integral construction remain inherited mathematical inputs. The spectral module proves the trace and determinant comparison from explicit inverse coordinate maps. The final convergence of the adaptive upper/lower enclosure and the interval-coefficient extension are complete written consequences in RESEARCH_NOTE.md, not additional named Lean declarations.
