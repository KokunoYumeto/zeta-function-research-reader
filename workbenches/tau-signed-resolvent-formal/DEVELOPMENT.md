# Development and execution review

14 September 2026. This record concerns only the signed-resolvent continuation. It preserves the prior mixed-boundary failure review and the corrected PR30 status rather than rewriting them.

## The moving repository

The first and subsequent main checks in this turn returned `331ccd30185a98bfc8fde8102cf09b9c2add4d6b`. Its new source-control chapter, ISM1–43, was read in full. The pertinent targets selected were the signed finite resolvent and centered residual (ISM27–34, the fixed-pair stopping part of ISM37) and the proper-source boundary kernel (ISM42–43). The existing `Metric.sectionMap`, `SourceProjectorContrast`, `CanonicalSourceContrast`, `Homology.quotientKernelEquiv`, and original `Relations.quotientDiagram` were read before extending them.

The current main formal subtree was byte-identical by Git tree hash to the inherited formal base of PR30. Integration commit `e0be0f7d9b3a55a3ebe77762e8aceaf8b7179c04` has parents main331 and corrected PR30 head `aa6473075928b0316c49d50c163697c4ab98d004`; it retains both exact source sets. Only `astra/signed-resolvent-checkin-20260914` is updated. No main, PR30, publication, or other-session ref was changed.

PR30's correction is substantive for reporting: its recovered finite suites contain **nine and eight test methods**, not eleven and fifteen. The old higher counts in my preceding conversation summary were wrong. This continuation uses the actual unittest counts and retains the corrected source record.

## Four observed development failures

All four complete decoded verify logs were read after completion. All retrieved the repository, unchanged Lean toolchain and pinned Mathlib successfully. None was an arithmetic counterexample.

1. Run `34795420211`, job `103827441556`, commit `31f86c90d92b048197d086e38327c8a0789cc4bf`: finite ring identities needed the correct orientation of `sub_eq_zero`; finite-sum expansions needed explicit collection of scalar factors; the convergence target needed an explicit function expression. The weighted trace proof needed the `MatrixOrder` scoped instance, the specified complex inner-product field, current positive-matrix theorem names, and precise rewriting of matrix products. Warning-as-error also caught unused simp arguments and instances. These were proof/API repairs; no theorem conclusion or necessary positivity assumption was weakened.

2. Run `34795995375`, job `103829086209`, commit `d41ce288ed92bd58286cb5c4c870522c00d859e7`: `ResolventSeries` strictly compiled. The positive-factorization theorem supplies an existential proposition; constructing the data-bearing `MetricFrame` needed an explicit `Classical.choice` from a proved `Nonempty`, rather than an illegal elimination of `Exists` into `Type`. The Hermitian square lemma had an unused decidable-equality instance. `RestrictedBoundary` had a redundant `rfl` after its inverse-map rewrite had already closed the goal. The repairs retain the actual constructed isometry and both inverse laws.

3. Run `34796499693`, job `103830514750`, commit `696a25e9e930727fcb45907cab565fc79806d347`: `ResolventSeries`, `SignedTraceEnclosure`, and `RestrictedBoundary` all strictly compiled, as did their full used closure. The new canonical composition needed the second exponent in `pow_mul_comm`, an explicit additive rearrangement of the already proved residual identity, and omission of two unused instance binders. No commutation of the signed contrast with the resolvent was added.

4. Run `34796846287`, verify job `103831497469`, commit `c3f887cd849ac50a2787c571a161f0122eb4fbea`: all four preceding new modules, including `CanonicalSignedResolvent`, strictly compiled. The new `SpectralResidual` had one unused simp argument, one unused decidable-equality instance, and an equality-transport expression that needed unfolding of the named real-trace function. The repairs remove only the unused proof arguments and rewrite through the proved conjugation-trace equality. All simultaneous diagonalization equations and the actual centered variance remain. The joint inherited boundary, synchronization, conormal and homotopy closure compiled. The independent finite job `103831497314` passed: nine-, eight-, and ten-method suites, nine boundary cases, five false formulas per Python mode, and 24 inherited checker tests per mode.

The next candidate, `68a1752fc3916e7dd506bfcdbb29285a4f918169`, contains those spectral proof repairs and the full mathematical note. STATUS.md is the source of truth for the subsequently observed terminal execution; this development record does not predict its result.

## Local execution is separate

The active local container had no Lean/Lake executable and could not resolve GitHub's network host. Therefore the kernel executions above are GitHub Actions executions, not local Lean runs. Local SymPy 1.14.0 was available. The committed ten-method checker was independently run normally and with `python -O`; both completed successfully, in approximately 35.769 and 37.772 seconds, with identical success JSON. Its Git blob is `65aa4989a8ac4239e6a4394bf6fd2bdc2c45b331`, SHA-256 `429e76e908dd47a0cb3df6c6a74bdffd064481d54121478554653b7af9e860bb`.

Earlier foreground invocations exceeded the tool's 45-second limit while developing larger fixtures. Those timeouts are not reported as failed mathematical checks or as completed successful runs. The committed checker uses the fully executed non-diagonal complex q=1,2 fixtures, not an unexecuted large fixture. GitHub subsequently ran that exact committed checker in both Python modes, including all five negative formulas.

## Gates and scope

Every local source in the selected import closure is screened after removing nested comments and strings, then individually compiled with `--trust=0 -DwarningAsError=true`. The transitive axiom audit requires one report for every selected target and rejects unexpected axioms; the allowed standard set is `propext`, `Classical.choice`, `Quot.sound`. Counts include definitions and interface lemmas, not mathematical discoveries.

The separate negative Lean controls must fail at their proposed mathematical equalities, not at imports or instance synthesis. The finite controls require exactly five named JSON records with `false_claim_accepted: false`; a generic crash cannot satisfy the gate. No lint, kernel-trust or axiom gate was disabled.

The finite spectral calculations are declared polynomial/matrix calibrations, not actual zeta-zero packets or arithmetic moment integrations. The source's compact-path integral, the sharper nested-projector estimate `8q-6`, and a uniform-in-k arithmetic bound remain separately scoped. This continuation constructs the finite matrix error and the proper-boundary maps; it does not identify spectral nilpotents with inertia or claim a general derived-tensor formalism.
