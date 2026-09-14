# Verified signed source resolvents and proper-boundary kernels

14 September 2026. **Observed successful implementation: `04ef2f962d69186ef48f07679a339b57486ef471`.** GitHub Actions [run 34797644407](https://github.com/KokunoYumeto/zeta-function-research-reader/actions/runs/34797644407) completed with both jobs successful: [verify 103833747257](https://github.com/KokunoYumeto/zeta-function-research-reader/actions/runs/34797644407/job/103833747257) and [finite 103833747401](https://github.com/KokunoYumeto/zeta-function-research-reader/actions/runs/34797644407/job/103833747401). The verify execution finished at approximately **2026-09-14 02:04:04 UTC**; the finite execution finished at approximately 02:02:33 UTC. Both complete decoded job logs were read after completion, including the final source hashes, all axiom reports and the actual negative-control diagnostics.

This status and the accompanying workbench README are a subsequent documentation-only addition. They change none of the verified Lean sources, runner, audit configuration, checker, workflow or formal dependency blobs. A later run is not claimed successful unless separately observed.

## Exact kernel-check scope

All **five new Lean modules** passed individual `--trust=0 -DwarningAsError=true` checks:

| Module | Selected transitive audit targets | SHA-256 |
|---|---:|---|
| SplitZeroResolventSeries | 17 | `839af3660892ab0b9957b4c188725f91efa6f92199f9a0685c7848a36f8d42bc` |
| SplitZeroSignedTraceEnclosure | 10 | `fa3278f4e5dfff2484ec6955063222be79ee59fa101782f779bd0e90c187fb1b` |
| SplitZeroRestrictedBoundary | 15 | `ac2f15917a4e1866fe8ae78a8f2276ec5684455e654af133b9b89bcd76e8f6e3` |
| SplitZeroCanonicalSignedResolvent | 7 | `006831fee20b6b095ca092ee2c81038c1119b18fbc6d310ce34525f098c47317` |
| SplitZeroSpectralResidual | 11 | `54b259c4af02019d4c41aa7a1dca839175dd28b97f190e74593f98f69f9ee82b` |

The runner strictly compiled **33 distinct local sources**, including the complete local import closure actually used by these modules and the joint original boundary-socle, synchronization, conormal and homotopy imports. It then checked **60 selected new targets** in the combined environment, requiring exactly one report for each expected target. Every transitive axiom set was a subset of `propext`, `Classical.choice`, and `Quot.sound`. The two relation-diagram constructions report only `propext` and `Quot.sound`. These counts include definitions and interface lemmas; they are not counts of new mathematical discoveries.

The 33 sources, in execution order, were: ResolventSeries, QuotientVolume, WeightedQuotientVolume, MetricVariation, SourceProjectorContrast, SignedTraceEnclosure, the original SplitZero, Extension, Fibres, Reconstruction, Homology, InternalQuotient, RestrictedBoundary, MetricVariationSupport, MetricSandwich, MetricResolvent, MetricResolventSupport, MixedSupportMetric, CanonicalSourceContrast, CanonicalSignedResolvent, SpectralResidual, BoundarySocle, BoundarySocleSupport, Presentation, Maps, Synchronization, SupportChange, RelationLayer, RelationLayerIntegration, ConormalTower, TauChart, TauDual, TauHomotopy. All abbreviated names except the original scalar have the `SplitZero` prefix.

This run does **not** claim to rerun every historical audit. In particular the older separate 60-target arithmetic-metric and 73-target derived Lean audits are not counted as executions in this workflow. Their used source modules were compiled where present in the current closure. The current 60 targets are the five new modules' selected declarations.

The complete receipt, including all 33 source SHA-256 values and all 60 axiom sets, was emitted twice into the public verify log and written on the runner to `formal/splitzero/.signed-resolvent-logs/receipt.json`.

## Original pins remain unchanged

Lean **4.31.0**, compiler commit `68218e876d2a38b1985b8590fff244a83c321783`; Mathlib **`fabf563a7c95a166b8d7b6efca11c8b4dc9d911f`**. The original scalar is Git blob **`ff991f7383922e71cdf0e4a3bc85e89e18f808ef`**, 7,366 bytes, SHA-256 `09f8ddf866687f93f384fd234975d1012dffdd6903782095901916607f042f48`. The workflow explicitly checks both toolchain and Mathlib revision and runs the unchanged scalar preparation.

Source-token screening removes nested comments and strings before rejecting forbidden proof shortcuts. Every local module is then individually kernel-checked. No lint, trust, axiom or failure gate was disabled during debugging.

## Two Lean negative controls

The proposed proof of `(SplitZero.e : SplitZero.G ℤ) = SplitZero.tau` was rejected at that exact equality: the log reports `rfl` failed. This is an intended negative control, not a substitute for the existing theorem distinguishing the constructors.

The false finite-series claim `partialSum (1/2 : ℚ) 1 0 = 2` was rejected after `norm_num` reduced its goal to `False`. For L=0 the actual partial sum is 1, not the infinite geometric value 2. Both controls imported the completed spectral module first. An unknown module, unknown identifier or failed instance synthesis would have failed the control gate rather than being accepted as the intended rejection.

## Exact finite job

The inherited source-resolvent suite passed **9 test methods**, the inherited mixed-metric suite passed **8 test methods**, and the new signed-source suite passed **10 test methods**, normally and under `python -O`. Successful JSON outputs matched byte-for-byte. In this final run the new suite took 25.296 seconds normally and 25.370 seconds in optimized mode.

The unchanged boundary suite passed its **nine full ordered lattice/socle cases** in both modes, with matching JSON. The inherited derived/synchronization/recovery checker harness passed **24 unittest methods** per mode.

The new five deliberately false formulas, `wrong-power`, `uncentered`, `diagonal-only`, `unweighted`, and `proper-zero`, were rejected in each Python mode. The workflow requires exactly those five named JSON records, each with `false_claim_accepted: false`, and identical records in both modes. A generic crash cannot satisfy the gate. The older seven finite negative formulas are not claimed as rerun by this particular workflow.

The new checker constructs non-diagonal complex source forms, the actual polynomial relation columns for its declared fixtures, the canonical sections and all four source projectors. It retains the L+1 residual power, the subtracted scalar mean-square, the mixed projector cross term, source-mass scaling, and a class that is a boundary only in the larger source. Its repeated-root polynomial fixtures are **not actual zeta-zero packets**, and these executions do not certify arithmetic moment or path integrals.

Checker Git blob: `65aa4989a8ac4239e6a4394bf6fd2bdc2c45b331`; SHA-256: `429e76e908dd47a0cb3df6c6a74bdffd064481d54121478554653b7af9e860bb`.

## Local replay and development history

The same committed checker was independently executed locally under SymPy 1.14.0. A fresh bounded normal replay completed all ten methods in 33.679 seconds with exit 0; the optimized replay completed all ten methods in 37.772 seconds with exit 0. Both negative-mode executions completed with the intended exit 1 and the same five false-claim records. Successful stdout and negative stdout comparisons matched across modes. Earlier foreground invocations that exceeded the local 45-second tool limit are **not** counted as completed checks.

Lean/Lake were unavailable in the local runtime and its direct GitHub network lookup failed. The kernel executions above are GitHub Actions executions, not local Lean runs. `DEVELOPMENT.md` and `FINAL_DEVELOPMENT.md` retain the five failed development candidates and their exact proof/API or documentation-syntax repairs. All five complete historical verify logs and this terminal successful log were read. The failures were not hidden or reclassified as arithmetic counterexamples.

The corrected PR30 history is preserved: the recovered suites contain **9 and 8 methods**, not the erroneous 11 and 15 stated in my older conversation summary and historical PR body. The present counts come from the executed unittest output.

## Repository and collaboration scope

This contribution read and preserved main **`331ccd30185a98bfc8fde8102cf09b9c2add4d6b`**, including its recursive-source-relations continuation. Its mathematical source is the complete ISM1–43 chapter, Git blob `b23bfcba6ec2dfcf35340a7d27c6f0a3145e83ea`, not merely publication metadata.

Integration commit **`e0be0f7d9b3a55a3ebe77762e8aceaf8b7179c04`** has parents that main snapshot and corrected PR30 head **`aa6473075928b0316c49d50c163697c4ab98d004`**. The inherited formal base was compared by tree hash before carrying PR30's additive formalization into this branch. Main was rechecked after the successful run and remained at the same snapshot. Only **`astra/signed-resolvent-checkin-20260914`** was updated. Main, PR30's branch, publication files and other sessions' branch refs were not changed. The final additive diff is recorded in the pull request.

The user's continuing-check request is implemented as an hourly condition watch for material source, review or CI changes. It does not perform autonomous merges, publication or unobserved formalization.

## Reproduction

From the checked implementation revision:

```bash
cd formal/splitzero
python3 prepare.py
test "$(cat lean-toolchain)" = leanprover/lean4:v4.31.0
lake update
test "$(git -C .lake/packages/mathlib rev-parse HEAD)" = fabf563a7c95a166b8d7b6efca11c8b4dc9d911f
lake exe cache get
python3 ../../workbenches/tau-signed-resolvent-formal/run_signed.py
```

The committed `splitzero-signed-resolvent.yml` gives the exact finite replays, mode comparisons and both types of negative controls. It uses read-only repository permissions and pinned checkout/toolchain dependencies.

## Mathematical boundary of this certificate

The implementation constructs the finite source resolvent, proves its exact centered spectral residual, proves the weighted trace inequality rather than assuming it, and attaches the interval to the original canonical source projectors. It constructs the natural proper-boundary quotient-kernel equivalence, both inverse total maps and the original quotient square; the exact image is characterized by the receiving supported-zero equality.

The simultaneous spectral diagonalization is supplied through explicit equations for an isometry of the original metric; this contribution does not construct a general generalized-eigenvalue solver. The scalar contraction bounds and finite stopping are for fixed endpoint data. The source's sharper nested-projector estimate `8q-6`, integration over the full source path, certified arithmetic moments and a uniform-in-tensor-degree upper bound remain separately scoped. Full-source theta primitives are not assumed admitted in every proper support. Nothing in this certificate identifies spectral nilpotents with inertia or proves a general tensor-derived/six-functor formalism.
