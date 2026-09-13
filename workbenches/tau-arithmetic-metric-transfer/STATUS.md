# Observed successful arithmetic-metric and residue integration

13 September 2026. The verified implementation commit is **`34636fb12b2180cc58c3cdff78231852b419dba1`** (tree `6f60eb36df4803446604ded707c971aabb8bcb51`). GitHub Actions **[run 34772920706, job 103765683307](https://github.com/KokunoYumeto/zeta-function-research-reader/actions/runs/34772920706/job/103765683307)** completed successfully at approximately **17:59:07 UTC**. The complete decoded job log was read after completion. This later status-only commit changes none of the verified source, workflow, checker, audit, or dependency blobs. It does not claim success for a later automatic run that has not been observed.

## Integration and preserved work

The starting and last-inspected main is `aea6471ac6cf36f7c5e660d8698dce6b0606196e`, containing merged PR28 and the R57 reader. This branch retains the entire main tree. Before this status file its diff was twenty added files and no modified/deleted main file; this status is the twenty-first addition. Main, the original reader/publication, dependency pins, and the other sessions' branch refs are unchanged. PR29 remains a draft and is not merged.

The complete eleven-file unfinished residue-rigidity contribution at `eed01119290bcac2f1c690be56ad20a71d929c35` was recovered with its commit ancestry. Its two coefficient modules had compiled; the actual source-generator theorem stopped at evaluation of multiplication in `Module.End`. Its missing definitional reduction is now repaired. The other recovered files are retained unchanged, including the written AV1--AV7 source-variation and AC1--AC5 adaptive-slope/coupling arguments and their exact checkers. The new note attributes that overlap explicitly.

## Strict Lean execution

All six modules passed separate `lake env lean --trust=0 -DwarningAsError=true` compilation:

- `SplitZeroMonicResidue`
- `SplitZeroResidueConstituent`
- `SplitZeroResidueSourceDetection`
- `SplitZeroMetricVariation`
- `SplitZeroArithmeticLogTransfer`
- `SplitZeroMetricVariationSupport`

The runner strictly rebuilt the complete used **35-file local SplitZero dependency closure**, not just the new modules. The combined import and **60 selected transitive axiom reports** passed: 34 recovered targets and 26 new targets. Every report used only `propext`, `Classical.choice`, and `Quot.sound`. Counts include definitions and interface lemmas, not mathematical discoveries. The unchanged **73-target derived audit** passed again. This is not a claim to have replayed every historical library audit.

The 35-file closure includes the original scalar, reconstruction, internal quotient, homology example, support-changing maps and adapter, quotient/source/period transports, residue support, synchronization homotopy, conormal derivative tower, Laplacian identities, tau base, and recovery. Its exact order, all source hashes, and all sixty reports were printed in the public job log and in the runner-generated `formal/splitzero/.metric-transfer-logs/receipt.json`.

### Exact six source identities

| Source | SHA-256 |
|---|---|
| `SplitZeroMetricVariation.lean` | `0a8e6a7814e6dbc8d21d114552799fbdff32b289578d7120d73f9c30446bd8e9` |
| `SplitZeroArithmeticLogTransfer.lean` | `0f73c942e59bfd05dd6758a4471cb90655d8679a43bec36e815402c2c43859fe` |
| `SplitZeroMetricVariationSupport.lean` | `cc6f5bbc6e9cbf7f32a354b8f3d786fc308def01670fb6be71e8fe786fd842ca` |
| `SplitZeroMonicResidue.lean` | `4c88f706693cb25d8d364d9b003a5b99777105153358f0ac63ee8fbe62ea6169` |
| `SplitZeroResidueConstituent.lean` | `b2e03ac14f244e1ff4b3cccee8275a026ace9c0cbe85e2a0df2279a8fd2e3154` |
| `SplitZeroResidueSourceDetection.lean` | `9cdb3fda6ca9002f2798b5da54b408d2c35cb8ef6abb928b6f5a7b7bf46cf610` |

Lean remains **4.31.0**, compiler `68218e876d2a38b1985b8590fff244a83c321783`. Mathlib remains **`fabf563a7c95a166b8d7b6efca11c8b4dc9d911f`**. The original scalar blob is **`ff991f7383922e71cdf0e4a3bc85e89e18f808ef`**, 7,366 bytes, SHA-256 `09f8ddf866687f93f384fd234975d1012dffdd6903782095901916607f042f48`. Original source/configuration preservation checks passed through the inherited helper. These pins are review gates, not a prohibition against inspecting and incorporating genuine future upstream corrections.

## Executed exact regressions

Each suite passed in normal and optimized Python, with byte-identical successful JSON records where emitted:

- Ten new exact metric-transfer methods: original polynomial-source positivity/mass and remainder maps; the actual boundary primitive; both secant identities; pencil gap; symbolic first and second source variations; both log-curvature terms; signed trace certificates in both directions and at equal metrics; cancellation of the common certificate scale; a nonzero original boundary with supported-zero observation.
- Ten recovered residue/source methods.
- Three recovered adaptive source-path/coupling methods.
- Twenty-four inherited checker tests.
- Seven inherited fail-closed parser cases.

The deliberately false boundary-loss equality, reversed signed-log formula, zero transverse rank, and wrong source-derivative sign were rejected in both Python modes. Forbidden `sorryAx` reports were rejected in both modes. The separate Lean attempt to identify the original `e` with `tau` failed specifically at that equality; missing modules, identifiers or instances were excluded as explanations of that negative control.

The new fixture uses the original coordinate `S=1/2+ix`, quotient `(S-1/2)^2+1`, and a Gaussian of literal mass seven weighted by `1`, `1+x^2`, and `1+2x^2`. It includes the first admitted source degree with no relation columns. For the displayed arithmetic/reference orientation the exact signed determinant ratio is **`1060928/561925`**. The common numerical certificate scale is **`100294/4521`**, and the tight displayed enclosure used orders **512 at all four endpoints**. The signed logarithm's decimal display is `0.6355308867715099`. Its two rational certificate endpoints are not identical; their machine-float displays round to the same number. That display is not a zero-width interval certificate. The checker independently compares the rational enclosure with a rational logarithm-series enclosure. These are declared finite polynomial calibrations, not arithmetic zero packets or certified evaluations of the theta integrals.

## Development failures and repairs

The recovered branch's run `34768496847` had already compiled the monic-residue and constituent modules but stopped in `observed_generator_power`. Adding the explicit definitional reduction after `pow_succ'` repairs that original-source theorem without weakening its action-intertwining input.

Our first run, `34771607181`, compiled `SplitZeroMetricVariation`, then exposed the reserved identifier `prefix` and an unnecessary inherited `Fintype` binder in the new logarithm module. The identifier became `partialLog`, and the unnecessary binder was omitted locally. The second run, `34772462215`, compiled both metric and signed-log modules, then required activation of Matrix notation for `*ᵥ` in the new supported-coordinate theorem. The third push run, `34772920706`, passed every step. No statement was weakened and no strict check was disabled. The failed development commits remain in history.

## Mathematical certificate boundary

The completed Lean results include the literal monic-remainder perfect pairing, exact rank-one constituent response, and bounded detection through powers of the actual source generator in the original supported quotient. They include exact canonical metric secants and source-pencil boundary losses, the signed four-endpoint trace-power enclosure, finite stopping orders, and quotient naturality/equality through the unchanged original `Relations.quotientDiagram`.

The arithmetic source-path calculus and integral identification retain their written-proof scope, with AV/AC attribution. The period invertibility and constituent-curvature arguments likewise retain their separate written scope. Positive spectral coordinate witnesses are explicit inputs; no automatic weighted eigensolver is claimed. Fixed-matrix certificate termination is not a uniform bound in tensor degree. No arithmetic moment enclosure, new RH theorem, or categorical impossibility result follows from these finite checks. The remaining quantitative target is the signed arithmetic source correction on the actual growing packet family.

## Reproduction

From the verified implementation checkout, with the inherited toolchain installer available:

```bash
cd formal/splitzero
python3 prepare.py
lake update
test "$(git -C .lake/packages/mathlib rev-parse HEAD)" = fabf563a7c95a166b8d7b6efca11c8b4dc9d911f
lake exe cache get
lake build
python3 ../../workbenches/tau-arithmetic-metric-transfer/run_metric_transfer.py
python3 check_derived.py --prepare
lake env lean --trust=0 -DwarningAsError=true AuditDerived.lean > /tmp/metric-derived.log
python3 check_derived.py /tmp/metric-derived.log
```

The committed read-only workflow additionally installs SymPy 1.14.0, runs all listed finite suites in both Python modes, compares their records, and checks every described negative control. Its exact commands remain in `.github/workflows/splitzero-arithmetic-metric-transfer.yml`.
