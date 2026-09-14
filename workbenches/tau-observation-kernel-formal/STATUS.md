# Observed strict original-observation verification

14 September 2026. The successful checked implementation is **`8e78bc7c240b04d297ade6afdadfd863e0c6db7b`**. GitHub Actions [run 34891954305](https://github.com/KokunoYumeto/zeta-function-research-reader/actions/runs/34891954305) completed with both jobs successful: [verify 104136565071](https://github.com/KokunoYumeto/zeta-function-research-reader/actions/runs/34891954305/job/104136565071) and [finite 104136565573](https://github.com/KokunoYumeto/zeta-function-research-reader/actions/runs/34891954305/job/104136565573). Both complete terminal logs were read after completion. The verify job completed at approximately 20:22:02 UTC.

This later status/README and concurrent-main source reconciliation changes none of the checked Lean sources, workflow, runner, finite tests or used formal dependencies. No subsequent unobserved run is claimed.

## Exact certificate

The runner individually compiled **33 local Lean modules**, including all four new modules and the complete used local dependency closure, with `--trust=0 -DwarningAsError=true`. The four new modules are:

- `SplitZeroObservationMetric`
- `SplitZeroObservedIterates`
- `SplitZeroObservedIteratesSupport`
- `SplitZeroResidueObservation`

The joint audit imported all four together with the inherited canonical signed-resolvent, boundary-socle and conormal modules. **All 56 selected transitive targets passed: 51 in the four new modules and five inherited proper-boundary/signed-trace targets.** Their axiom sets were subsets of `propext`, `Classical.choice` and `Quot.sound`. Counts include definitions and interface lemmas, not discoveries. This is not a new run of every historical audit.

The exact 33-source order, every dependency SHA-256, all 56 target names and each transitive axiom set are emitted in the public verification log and `.observation-kernel-logs/receipt.json`.

## Unchanged pins and source hashes

Lean **4.31.0**, compiler `68218e876d2a38b1985b8590fff244a83c321783`; Mathlib **`fabf563a7c95a166b8d7b6efca11c8b4dc9d911f`**. Original scalar Git blob **`ff991f7383922e71cdf0e4a3bc85e89e18f808ef`**, 7,366 bytes, SHA-256 `09f8ddf866687f93f384fd234975d1012dffdd6903782095901916607f042f48`. The new source hashes from the actual runner are:

| Source | SHA-256 |
|---|---|
| SplitZeroObservationMetric | `a1ef5765c3c0eebe9cbbb37a3a1812808d3025045b7bf99a0e4f4cc7e61222a8` |
| SplitZeroObservedIterates | `9587a9c6001bb3737756f811f1ed6bc231bac1bac3bc5fdaf011080c4a66251f` |
| SplitZeroObservedIteratesSupport | `d884a2773a44034b4ec4181ff74b36500cdf21bc3ce32c6e765cea6c362a83ed` |
| SplitZeroResidueObservation | `0145aac9efb60ff2288c97015fe46e35a6c165d1935cb690962a975dbac161b3` |

The separate Lean negative control was rejected at the actual equality `SplitZero.e = SplitZero.tau`: `rfl` failed because these original constructors differ. The workflow excludes missing-import, unknown-identifier and instance failures from that control's acceptance.

## Exact finite execution

The new **nine-method** suite passed normally and under `python -O`, with byte-identical success JSON. It constructs the original constrained sections for declared positive, non-diagonal complex matrix fixtures, retains all mixed Gram entries, tests the fixed-section correction and ordered denominator, preserves an explicit mass scaling, and includes the empty boundary image. Its polynomial fixtures include repeated factors, nontrivial observation annihilators, no observation rows, the original companion shift and a vector seen only after a later nilpotent iterate.

Five false formulas were rejected in each mode, with precisely the expected named JSON records: `omit-section-correction`, `diagonal-only`, `omit-denominator`, `one-step-closed`, and `always-faithful`. A generic crash was not accepted instead. The unchanged PR31 ten-method signed suite passed in both modes and its JSON records matched. The unchanged 24 derived/synchronization/tau-recovery checker unittests passed in each mode.

These are exact finite polynomial/matrix calibrations, not evaluations of actual zeta-zero packets, transcendental period coefficients, arithmetic moment intervals or a tensor-uniform estimate. No unchanged analytic delivery archive was independently extracted or rerun in this turn.

## Failures are retained

The two inspected failed candidates and their full-log diagnoses are documented in DEVELOPMENT.md. The first needed the scoped complex positive-order interface and explicit complete Gram rearrangements; the second needed the implicit source vector and membership-proof binders separated in the natural kernel diagram. The intervening residue-only push retained the first uncorrected metric error and is not presented as a distinct mathematical obstruction. All repairs keep the original statements, full cross terms and strict gates.

## Reproduction

From the checked implementation, with the unchanged toolchain installed:

```bash
cd formal/splitzero
python3 prepare.py
lake update
test "$(git -C .lake/packages/mathlib rev-parse HEAD)" = fabf563a7c95a166b8d7b6efca11c8b4dc9d911f
lake exe cache get
python3 ../../workbenches/tau-observation-kernel-formal/run_observation.py
```

The committed workflow gives the exact finite replays and negative-control commands. Its GitHub token permissions are read-only, credentials are not persisted, and the action/toolchain pins are unchanged.

## Mathematical scope

Checked: the constructed minimum observation section, full residual Gram and positivity, correction from a fixed section, the ordered scalar factors, the largest invariant observation kernel, finite determination from the original polynomial, its original SplitZero diagram/quotient actions, the concrete monic-residue annihilator characterization, and the conditional injectivity theorem from a literal Bezout witness.

Written, not additional Lean declarations here: the polynomial-gcd and primary-socle corollaries; explicit Bezout reconstruction coordinates; comparison of the resulting observation norm with the original metric; identification with the latest OCS coefficient matrices; the complete analytic construction of those period matrices. No actual-row injectivity, purity transfer, period integration or absolute common-kernel `kq` asymptotic is inferred from the finite certificate.

The branch preserves the complete checked PR31/PR30 ancestry and the current analytic main source without modifying their branch refs. LATEST_INTAKE.md records the concurrent main update and precise reading scope. No main merge was performed.
