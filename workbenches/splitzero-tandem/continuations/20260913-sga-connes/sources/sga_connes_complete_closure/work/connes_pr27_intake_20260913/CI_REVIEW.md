# PR27 immutable-source, CI, and finite-checker review

Review completed 2026-09-13. Repository: `KokunoYumeto/zeta-function-research-reader`.

## Result

The exact candidate has satisfactory observed CI and bounded finite-calibration evidence for its stated local/finite scope. Both current specialization runs succeeded; the push run checked the exact branch head, and the PR run checked a synthetic merge with an identical complete Git tree. Local normal/optimized replays passed, and substantive mathematical and audit corruptions were rejected. There is a future CI-trigger coverage gap to repair or explicitly track. This review does not approve the written analytic arguments or establish RH; those require the independent mathematical review assigned to the parent.

No Lean was executed locally. No packages were installed. No branch, PR, remote description, or publication was changed. All 41 downloaded repository files retain their original bytes. Only review scripts and isolated evidence/output files were written.

## Immutable provenance and complete diff proof

| Object | SHA |
|---|---|
| Base commit | `e4ee97cdce904d4b9bb5697d33095aaa00083f24` |
| Base tree | `7958ede8166c465770379b0fb23a4475ec49199f` |
| PR27 head commit | `a4a87844c257485ae6d669f5b3eb6d96b9e8b8d8` |
| Head tree | `335f0f6bb9cfd300359d453dea6d994eb44e7489` |
| PR synthetic merge commit | `59b5aadebcf91350430c0eba30ae6bae4087738d` |
| Synthetic merge tree | `335f0f6bb9cfd300359d453dea6d994eb44e7489` |

The API compare reports base equals merge-base, 13 commits ahead, zero behind, and exactly 16 added files with no modifications or deletions. Independently comparing the complete, non-truncated recursive base/head trees gives the same 16 additions. Every Git tree node was reconstructed and SHA-1 verified from its canonical child entries: 960 head nodes and 959 base nodes, including the two root trees above. Each of the 41 selected source files was downloaded by immutable Git blob, independently checked against its Git blob SHA-1, and given a byte count and SHA-256. Source integrity was checked again after finite execution. No inherited repository blob changed in the candidate.

`SOURCE_MANIFEST.json` records the actual tree hashes (not commit IDs), every file's SHA-1/SHA-256/length, and the exact tree diff. `evidence/compare.json`, `head_tree.json`, `base_tree.json`, and commit records retain the supporting API data. `CI_RECEIPT.json` contains the independent tree-hash recomputation result; `EVIDENCE_MANIFEST.json` hashes the downloaded/derived evidence files.

The 16 added paths are:

1. `.github/workflows/splitzero-specialization-curvature.yml`
2. `formal/splitzero/AuditLaplacianControl.lean`
3. `formal/splitzero/AuditSpecializationCurvature.lean`
4. `formal/splitzero/SplitZeroActionHull.lean`
5. `formal/splitzero/SplitZeroCurvatureRestriction.lean`
6. `formal/splitzero/SplitZeroLaplacianControl.lean`
7. `formal/splitzero/SplitZeroRelationCurve.lean`
8. `formal/splitzero/SplitZeroSpecializationChart.lean`
9. `workbenches/tau-specialization-curvature-formal/COORDINATION.md`
10. `workbenches/tau-specialization-curvature-formal/HOCHSCHILD_COMPARISON.md`
11. `workbenches/tau-specialization-curvature-formal/LAPLACIAN_PARABOLA.md`
12. `workbenches/tau-specialization-curvature-formal/RESEARCH_NOTE.md`
13. `workbenches/tau-specialization-curvature-formal/STATUS.md`
14. `workbenches/tau-specialization-curvature-formal/VALIDATION.json`
15. `workbenches/tau-specialization-curvature-formal/check_laplacian.py`
16. `workbenches/tau-specialization-curvature-formal/check_specialization.py`

The extra 25 inherited files comprise all other 12 workflows; the four repository-local transitive Lean modules; their two relevant audit files; four restriction-workbench checker/example scripts; and `prepare.py`, `lean-toolchain`, and `lakefile.toml`. Thus the selected workflow's local checker and import closure is present. Mathlib/toolchain binaries and the upstream scalar fetched by the preparer were not installed or locally materialized; their immutable pins and observed CI verification are recorded separately. The new modules' import closure does not import that upstream scalar.

## Actual current-head CI evidence

| Event | Run / job | Actual checked-out commit | Job completion UTC | Result |
|---|---|---|---|---|
| pull_request | 34735695035 / 103666603149 | `59b5aadebcf91350430c0eba30ae6bae4087738d` | 03:34:54 | success |
| push | 34735693215 / 103666609598 | `a4a87844c257485ae6d669f5b3eb6d96b9e8b8d8` | 03:35:26 | success |

Both runs report candidate head `a4a87844c257485ae6d669f5b3eb6d96b9e8b8d8` in API metadata. The checkout distinction above comes from the actual full job logs, not that metadata. The synthetic merge has exactly base/head as parents and the identical complete tree. The full decoded logs are retained as `evidence/job_103666603149.full.log` (51,266 bytes) and `job_103666609598.full.log` (51,081 bytes), with hashes in the receipts. The first was read end-to-end; all unique lines of the second were compared against it, and the full verification sections were proved byte-identical after removal of timestamp prefixes. Differences are checkout mechanics and runner-specific metadata, not tests, source-check commands, results, or audit reports.

Each run provides:

- Successful 17-method specialization and 10-method Laplacian suites; normal and `-O` stdout compared with `cmp`; both built-in deliberate negative controls nonzero in both modes with the intended diagnostic.
- Successful byte-pinned upstream scalar verification: Git blob `ff991f7383922e71cdf0e4a3bc85e89e18f808ef`, 7,366 bytes.
- Lean 4.31.0, reported release commit `68218e876d2a38b1985b8590fff244a83c321783`.
- Nine successful individual `lean --trust=0 -DwarningAsError=true` invocations: four inherited restriction modules and the five new modules. The loop accumulates failures and exits nonzero if any invocation fails.
- Four strict joint-import/audit invocations, with pipeline failure propagation and exact-target checker validation. `AuditLaplacianControl.lean` imports all five new modules, supplying joint import coverage.
- Exactly 71 unique printed declarations: 29 specialization/curvature, 9 Laplacian/intertwiner, 26 inherited restriction/certificate, and 7 inherited matrix-spectrum targets. Every reported transitive axiom belongs to `{propext, Classical.choice, Quot.sound}`. The extracted actual reports were independently matched to the audit files and reparsed locally; all passed.
- Inherited 16-method restriction suite, rational certificate example, and 13-check zero-mode calibration replayed normal/optimized with identical stdout. These replays retain cost spectrum `0, 19/4, 83/10`, return spectrum `1, 4/23, 10/93`, and rational combined enclosure `2.46119012317068` to `2.46119012317069`. The specialization workflow does not replay those inherited scripts' negative flags.

This is 38 selected new declarations plus 33 inherited declarations, not every declaration or the entire programme. Successful setup logs for pip, `lake update`, and cache retrieval are redirected and not separately uploaded; the observed successful shell steps establish that the prescribed commands and equality checks exited successfully, not an independently archived dependency manifest.

`STATUS.md` and `VALIDATION.json` explicitly preserve the older run 34735210715 / job 103665300994 at checkpoint `25960903723954d6118b1aa76a817cb6a7f452f0`. This review does not silently substitute that claim for current evidence: the current-head runs above were separately fetched and verified. The five module blobs, both checker blobs, and workflow blob stated by the checkpoint metadata agree with the corresponding exact-head values. The older full log was not needed or rereviewed.

## Other current-head checks: compact scope only

The exact-head API listing and `gh pr checks` agree on **11 total successful runs: two specialization and nine other runs**. Thus “ten other checks” is not the observed count. Full logs of these nine other runs were not rereviewed; their complete job/step metadata and workflow definitions were inspected.

| Workflow | Run | Job | Result |
|---|---|---|---|
| SplitZero tau recovery | 34735694961 | 103666602741 | success |
| SplitZero actual synchronization | 34735695001 | 103666603022 | success |
| SplitZero structural formalization | 34735694932 | 103666602807 | success |
| SplitZero derived constructions | 34735694928 | 103666602635 | success |
| SplitZero finite frontier | 34735694935 | 103666602686 | success |
| SplitZero boundary layer integration | 34735694967 | 103666603089 | success |
| SplitZero exterior trace collaboration | 34735695025 | 103666603132 | success |
| SplitZero conormal cyclic tower | 34735695046 | 103666603065 | success |
| SplitZero Toda volume integration | 34735695017 | 103666603037 | success |

The absent dedicated boundary-layer, consecutive-window, and restriction-certificate workflows have narrower change filters. Their absence is not a failed job. The specialization workflow does rerun the restriction/certificate and spectrum audits, but not the separate consecutive-window audit.

## Local finite replay and substantive negative evidence

`FINITE_RECEIPT.json` records all 18 bounded sequential subprocess runs, exit codes, stdout/stderr hashes, and runtime. `finite_output/` contains complete outputs. Existing Python 3.13.9 with SymPy **1.13.1** and mpmath 1.3.0 was used; CI separately ran pinned SymPy **1.14.0** and mpmath 1.3.0. This is a transparent cross-version replay, not an exact CI-environment reproduction. No install was attempted. Python bytecode writing was disabled and output working directories were separate from source.

- Both 17- and 10-method suites pass normal and optimized Python with byte-identical successful JSON and no stderr. Their method counts include four audit-parser methods in total; they are not 27 independent new mathematical theorems.
- Four invocations of the built-in `--negative` flags fail intentionally. These unconditional controls prove failure-path propagation, not sensitivity to mathematical errors.
- Independent audit mutations, in each mode: missing/empty target set, duplicated target, extra recognized target, `sorryAx`, `Lean.ofReduceBool`, custom axiom, and Lean error text, applied to each new parser. All 16 are rejected.
- Six independent in-memory algebraic source mutants, in each mode, each fail its specifically targeted existing test with one assertion failure and no execution error: reverse the relation-difference sign; remove the transported-action pole; corrupt the curvature-derivative factorial; corrupt the Gaussian coefficient; drop the centered-energy cross term; drop the Jordan-square term. Exact mutation anchors, targeted tests, and failure traces are retained in `review_negatives.py` and `finite_output/independent_negatives.*.stdout`. Original checker files were never edited.
- The actual 29+9 new CI reports from both jobs pass the original audit parser under both modes. An additional four bounded normal-mode subprocesses in `finalize_ci_receipt.py` independently replay the inherited 26/7-target parsers from both jobs; their outputs are in `finite_output/` and their exact scope is recorded in `CI_RECEIPT.json`.

The source fixtures are exact symbolic Gaussian polynomial/finite-jet calibrations. They neither sample zeta zeros nor certify Schwartz-space closure, coherent-sheaf globalization, curvature currents, heat limits, a uniform arithmetic upper-volume estimate, spectral simplicity, a positive invariant metric, or RH. Some individual assertions are elementary degree/normalization markers; passing them must not be inflated into an analytic theorem.

## Workflow review, pins, and recommendations

All 13 exact-head YAMLs were read completely in an independent static review. All 85 explicit `lake env lean` command templates contain `--trust=0`; 82 also specify warning-as-error. The three inherited original-core checks in structure line 44, synchronization line 44, and derived line 49 lack warning-as-error. Those exceptions are outside the new strict nine-source/four-audit commands; `lake build` commands are not themselves explicitly given these flags. Template counts are not loop-expanded execution counts.

All 13 workflows use checkout commit `3d3c42e5aac5ba805825da76410c181273ba90b1`, `persist-credentials: false`, and read-only contents permission. The elan script is commit-pinned to `0e36a07b9bbcc5381fa6250df109f9a4f94d7bac`; toolchain selects 4.31.0; `lakefile.toml` requires Mathlib `fabf563a7c95a166b8d7b6efca11c8b4dc9d911f`, with workflow equality check after update. There is no `pull_request_target`, publication/deployment step, explicit secret use, or privileged token scope in the reviewed YAMLs.

These are useful source pins, not a hermetic build. Runner image/system Python float, pip packages use version pins without artifact hashes, the pinned elan script invocation does not pin an elan binary version, toolchain/cache binary artifacts are not separately attested, and no committed Lake manifest is present. The full logs identify Ubuntu 24.04.5 / image 20260907.300.1 and runner 2.337.0 for these two runs.

Recommended follow-up (no workflow source was changed by this review):

1. **Cover the complete specialization dependency closure in triggers.** New workflow lines 9–19 enumerate only new Lean files and omit inherited restriction modules/audits, `prepare.py`, `lean-toolchain`, and `lakefile.toml`, although later steps rely on them. Both push and PR path filters omit `workbenches/tau-restriction-certificate-formal/**`, whose scripts are executed. A straightforward repair is `formal/splitzero/**` in the PR filter and addition of the inherited restriction-workbench glob to both filters. This is a real future validation gap, but does not invalidate either current run because their triggers did fire and full source trees were identical.
2. **Document or harden parser boundaries.** Both new parsers reject corrupt recognized records but ignore an appended axiom-free extra report and warning-only text. These probes were observed as accepted and explicitly recorded, not mislabeled successful rejection tests. They also cannot accept a required theorem using Lean's “does not depend on any axioms” form, so a future axiom-free target would fail closed. The actual logs have exactly the intended 71 reports, no unrecognized extras; shell exit checks and warning-as-error are the operational protection against compiler warnings/errors. These parser limitations therefore do not overturn current evidence.
3. Preserve the finite/selected-audit scope and the local/CI SymPy-version distinction in any integration summary. Do not claim this review rebuilt Lean locally or fully certified the written analytic continuation.

Primary evidence entry points: `SOURCE_MANIFEST.json`, `CI_RECEIPT.json`, `FINITE_RECEIPT.json`, `EVIDENCE_MANIFEST.json`, `evidence/`, and `finite_output/` beside this report.
