# Verified mixed-support and boundary-kernel recovery

14 September 2026. The observed successful implementation is **`9102c2ee50b68ccac2e878d4ec45f6dd1b8c8e63`**. GitHub Actions [run 34786929823](https://github.com/KokunoYumeto/zeta-function-research-reader/actions/runs/34786929823) completed with both jobs successful: [verify 103803985110](https://github.com/KokunoYumeto/zeta-function-research-reader/actions/runs/34786929823/job/103803985110) and [finite 103803984984](https://github.com/KokunoYumeto/zeta-function-research-reader/actions/runs/34786929823/job/103803984984). The verify job finished at approximately 2026-09-13 22:37:19 UTC. Both complete decoded logs were read after completion.

This later status/failure-review update and concurrent publication-index reconciliation change none of that implementation's source, audit, workflow or formal dependency blobs. No later unobserved run is claimed.

## Exact verification scope

The recovered runner individually strictly compiled 43 local SplitZero modules, including its full used dependency closure and original synchronization. The boundary runner separately strictly compiled two new modules. Thus **45 distinct local sources** passed individual `--trust=0 -DwarningAsError=true` checks in this run. The nine completed new/recovered modules are:

- SplitZeroMetricResolvent
- SplitZeroCertifiedTraceBounds
- SplitZeroMetricResolventSupport
- SplitZeroMetricSandwich
- SplitZeroSourceProjectorContrast
- SplitZeroMixedSupportMetric
- SplitZeroCanonicalSourceContrast
- SplitZeroBoundarySocle
- SplitZeroBoundarySocleSupport

All selected transitive audits passed: 24 recovered resolvent targets, 32 recovered mixed-metric targets, and 21 new boundary targets, **77 targets across those nine modules**. The inherited 60-target arithmetic-metric/residue audit and original 73-target derived audit passed again. The 21 boundary reports passed once more in a joint import with canonical source contrast, synchronization homotopy and conormal derivatives. The allowed sets were subsets of `propext`, `Classical.choice`, and `Quot.sound`; `BoundarySocle.divide_intertwiner` reports no axioms. Counts include definitions and interface lemmas, not mathematical discoveries. This does not claim a rerun of every historical audit.

The new boundary implementation constructs its equivalence and inverse laws from actual quotient maps and cancellation hypotheses on the prequotient. The image theorem on the reconstructed total is the equality of v-action with the same fibre's e-action. The source cancellation hypothesis is never applied to the torsion quotient.

## Unchanged pins

Lean is **4.31.0**, compiler commit `68218e876d2a38b1985b8590fff244a83c321783`. Mathlib remains **`fabf563a7c95a166b8d7b6efca11c8b4dc9d911f`**. The original scalar source is Git blob **`ff991f7383922e71cdf0e4a3bc85e89e18f808ef`**, 7,366 bytes, SHA-256 `09f8ddf866687f93f384fd234975d1012dffdd6903782095901916607f042f48`.

The separate Lean negative control was rejected specifically at the proposed equality `(SplitZero.e : SplitZero.G ℤ) = SplitZero.tau`. The log shows `rfl` failed because those two original constructors are not definitionally equal. No missing import, identifier or instance was counted as that negative control's success.

## Nine completed source hashes

| Module | SHA-256 |
|---|---|
| SplitZeroMetricResolvent | `80f500fc813d4705ff30f39eb2084e1c74beb4d77078adb0208aa8e006720c0c` |
| SplitZeroCertifiedTraceBounds | `64b143c6830077f74fc2f5b5d3fb30fe33048207905e9dde6fe8bce08dbcd4d7` |
| SplitZeroMetricResolventSupport | `094554ecb0beb7daba2b61ebd21d408a501ebb1b472a5dfe49b81a1292d17f46` |
| SplitZeroMetricSandwich | `37b4c195a9155f74c8a406f6c8068d3d9ab953ac5a5aea52bf5586588083fd21` |
| SplitZeroSourceProjectorContrast | `9e2f314bba7f3dc21cd207af191662b5b48c5624434da4f356d6f7a8c8a28dd1` |
| SplitZeroMixedSupportMetric | `2e5c93e34a5e9407abde227492b0f3950fd1832bb0eb6281cc9a8855c2d51caf` |
| SplitZeroCanonicalSourceContrast | `2d95460c76156f2355f7489ef16fcb24d0a729bcd1f41eebafa4be9160119b91` |
| SplitZeroBoundarySocle | `177c92f4ebb55a574bf790dcb41e1b3331110f97b94b59c5a2d704c3e8da9c36` |
| SplitZeroBoundarySocleSupport | `76375427b7ad53a86e37ecfb1ea94e478164aea983de779171dc7177928b5e52` |

The complete source order, dependency hashes and axiom reports were emitted into the public verify log and `.mixed-metric-logs/receipt.json`; the new boundary records are `.boundary-socle-logs/receipt.json` and `.boundary-socle-logs/joint.json`.

## Finite job

The 11-method recovered source-resolvent suite, 15-method recovered mixed-metric suite, and nine new ordered lattice/socle cases passed normally and under `python -O`; their successful JSON outputs matched byte-for-byte. Twenty-four inherited checker unittests passed in each mode.

The three recovered false controls `diagonal-only`, `absent-join`, and `omit-boundary` and four new controls `nilpotent-zero`, `omit-jacobian`, `empty-absence`, and `diagonal-gram` were rejected in both modes. Each emitted `false_claim_accepted: false`; a generic crash was not accepted instead.

The new cases include (m,k)=(2,2), where the full socle has rank four and the sum-generated cyclic subspace rank three. The original top multinomial coefficient and the additional ordered direction are checked. The full mixed Gram fixture is [15], with genuinely nonzero cross terms. These are declared polynomial/matrix calibrations, not actual zeta-zero packets, certified arithmetic moments or finite-field purity computations.

## Independent uploaded-source replays

Separate local execution safely extracted both uploaded archives, verified all 86 Mixed Boundary and 28 Marked Product manifest entries, and replayed the unchanged supplied suites. The main mixed-boundary suite passed 18 methods; its tensor-cone suite passed 12 cases and its twist suite seven cases. The marked-product suite passed 14 methods. Both Python modes were used, matching output records where supplied, and the deliberate false controls failed. Exact script/archive hashes and times are retained in INTAKE.json. These local replays are not part of the Lean job or a proof that missing TeX text is present.

The real delivery gap MB20--MB44 and MB46--MB47, the parameter-ring qualification, and the three historical plus three new proof failures are documented in FAILURE_REVIEW.md. All three complete historical raw logs were read, not just their step summaries. The needed finite lattice/socle/action argument has an independent complete reconstruction in RESEARCH_NOTE.md; the missing full analytic/finite-field source remains outside this certificate.

## Concurrent-main and branch scope

The recovery starts from main **`8e28e155bcffe605af8fa6cce313e05cd692341a`** and preserves all 19 files and ancestry of the unfinished `astra/mixed-support-metric-recovery-20260913` contribution at **`fb60c6694093ee41648cf31d4be75bb69c145770`**. Neither that branch nor main was rewritten.

After the successful run, main advanced to **`35b7aeaff0b63b0db71f26c5b921cdbbec2507fb`**, changing only nine publication/index files. The final recovery branch preserves those exact files too. They do not alter the formal dependency closure, the source tests or the accepted MCF/SP/BC mathematical source. Against that inspected main snapshot, the final contribution has **29 added files and no inherited modification or deletion**. The archived publication and all other sessions' branch refs remain unchanged. No main merge was performed by this contribution.

## Reproduction

From the verified implementation commit with the inherited toolchain available:

```bash
cd formal/splitzero
python3 prepare.py
lake update
test "$(git -C .lake/packages/mathlib rev-parse HEAD)" = fabf563a7c95a166b8d7b6efca11c8b4dc9d911f
lake exe cache get
lake build
python3 ../../workbenches/tau-mixed-boundary-formal/run_boundary.py
python3 ../../workbenches/tau-mixed-metric-integration/run_mixed.py
python3 ../../workbenches/tau-mixed-boundary-formal/run_boundary.py --joint
python3 check_derived.py --prepare
lake env lean --trust=0 -DwarningAsError=true AuditDerived.lean > /tmp/derived.log
python3 check_derived.py /tmp/derived.log
```

The committed recovery workflow contains the finite replays and explicit forbidden equalities. Its permissions are read-only and its actions/toolchain dependencies are pinned.

## Mathematical boundary

The generic boundary-kernel equivalence, diagonal-power construction, induced quotient actions, original support naturality and mixed-source Gram identities are checked. Their concrete ramified primary/tensor formulas have the full written application and independent finite regressions. This is not a formalization of a general Tor derived functor, of the complete cubical derived tensor comparison, of analytic Stokes theory or of finite-field inertia/purity. Spectral nilpotents, character-twisted maps, and actual inertia are not identified without their separate comparisons. The original theta source, arithmetic action, quotient kernels and metric pairings remain attached; no opposing tensor-uniform arithmetic upper bound is asserted.
