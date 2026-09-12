# Bounded exact-head merge-readiness review: PRs 14–18

12 September 2026. Repository: `KokunoYumeto/zeta-function-research-reader`.
This is an integration review, not a new proof audit of the entire reader. No local Git, source rewrites, remote mutations or Lean builds were performed. Previously audited sources were matched by exact SHA-256/Git blob; new PR17 public source and its finite checker were read directly. The current AGENTS instructions and `CURRENT_WORK.md` were read before review.

## Recommendations at the captured heads

| PR | Exact head | Recommendation | Validation scope |
|---|---|---|---|
| 14 | `3bff1b2bd87dfa2592f65c5ccc231f6ee9541dfc` | Integrate, with the small real-seed explanation supplied below. | Existing full source audit and 19-method normal/optimized finite replay match these exact bytes. No exact-head Actions runs returned; no new Lean or infinite theorem certificate. |
| 15 | `21970bbf4760d0bbca512a4a7996a2e38f968947` | Integrate independently of the failed PR16. | Exact-head boundary runs `34705607593` and `34705610528` and all four other inherited workflows are successful. Five new modules, 38 selected axiom-report targets; not the analytic theta specialization or RH. |
| 16 | `40346cbda35df1bc0242b8fdd449670d4af19a80` | Not ready at this head. Repair final module and reconcile three overlapping files with PR15, then read the new exact-head CI. | Dedicated PR and push boundary-integration runs fail in the sixth module; the 66-target audit step is skipped. Other four workflows and 25 Python tests pass. |
| 17 | `33b29f706008124886614ba4bd55bffc489df9e2` | Integrate after PR14; repeat the inherited full-quotient degree range locally for clarity. | Full 12.7 KB public note and 6 KB checker read; eight finite methods pass normally and with `-O`; both deliberate false controls fail as expected. No exact-head Actions runs returned and no Lean certification claimed. |
| 18 | `06cf51dc84bbae36298aa92cb6240a338b04cd6d` | Separate new draft; not a blocker to 14–17. | Head changed from the earlier reported `179cfce...`; latest captured head is draft, explicitly pending validation, with no Actions runs returned at capture. No source/Lean audit of this new head was performed. |

These are recommendations at stated snapshots, not claims of completed merges. The parent task owns final live-head readback, branch correction, retargeting, merges and publication.

## Dependency order and overlapping files

The initial main snapshot was `cc2bb03e7375df1887f70a459f1f538d54af3e0f`.
PR14's base is the already-integrated PR11 branch at `d37eade4f9e6a82c1a88aeff710a3b851a34eb49`.
PR15 and PR16 both independently branch from PR12 at `5d2772ea0a16d177ac3e01ff70394b90ba95a232`.
PR17 is directly based on PR14's exact head. PR18 is directly based on PR15's exact head.
The saved compare responses confirm the PR11 and PR12 base commits are common ancestors with the main snapshot.

Retarget to the intended integration branch/main; simply merging into the old stacked branch would not itself close the publication backlog. A sound order is PR14, PR17 and independent PR15, followed by repaired/reconciled PR16. PR18 stays separate until its own new exact-head evidence is ready.

PR15 and PR16 independently add different contents at three identical paths:

- `formal/splitzero/BOUNDARY_TARGETS.json` (38-target versus 66-target lists);
- `formal/splitzero/SplitZeroRelationLayer.lean`;
- `formal/splitzero/SplitZeroSupportChange.lean`.

The exact SHA-256 pairs are recorded in `overlapping_added_paths.json`. Preserve PR15's established declaration interfaces and dedicated check manifest; this is a coexistence repair, not permission to replace one contribution with the other. The parent assigned that repair separately. No other pair among 14–17 has a conflicting added path.

## Source audit reuse: PR14 and PR15

The existing audit `C:/Users/user/Documents/math/work/pr14_coherent_integration_review.md` has SHA-256 `3401b9d2de24248b41649b2939890fb4593527b3f69049f1c5ffd5db9d7869e1`.
The PR14 public note and checker exactly match its audited hashes, respectively `d3e808adea130c3e967b84a82def531e2984ce2c7a593bbc31cddf4504124ad0` and `4d7c78bd36037ee5dd7d69ade773c9860b979e6bb39a2e556df339666033773f`.
It already covers complete jets, constrained minimization, density, same-degree one-variable packet naturality and the tensor next-layer formulas. Do not incorrectly extend same-degree one-variable packet naturality to arbitrary nested joint packets without their additional projection map.

The one necessary exposition repair is public PR14 `RESEARCH_NOTE.md:236`: `D*=1-D` alone fixes only the real part of a complex diagonal. The source's actual real theta seed and real Gram–Schmidt family make that coefficient real; equivalently its actual spectral weight is even. The existing source audit supplies this argument in cumulative CT.8–CT.9. The local candidate adds that argument without changing equation (6.1) or any displayed equation.

The complete prior PR15 audit is `C:/Users/user/Documents/math/work/pr15_source_status_20260912.md`, SHA-256 `59411969feafe2b62f4475230373ad4eda4c5cef9aadb07dd8487e725905e70d`.
All five new module hashes in that audit match this exact PR15 download. Its independent API evidence verifies the exact-head successful run and job; it explicitly does not claim a fresh replay of inaccessible raw log contents. The live Actions snapshot agrees with success. The strict workflow uses the unchanged Lean 4.31.0 / Mathlib pins and selected axiom reports, not additional analytic axioms.

The supplementary existing audit `C:/Users/user/Documents/math/work/pr15_norm_volume_bridge_audit_20260912.md` has SHA-256 `c243310311da212f5d12303a8cbd282dcb42ed0bb7e0b4759d6cc092d5ea1e2c`. Its norm/quotient-norm dictionary and conjugated cross term are additional exact bridges, not a contradiction in PR15. Preserve the original measures and indices. An arbitrary supported morphism can have bottom target; the concrete nonexternal-zero applications use nonbottom receiving support, as the source audit already explains.

## PR16 exact failure

See `pr16_status/REVIEW.md` and its bound job/log receipts. The dedicated run [34706741599](https://github.com/KokunoYumeto/zeta-function-research-reader/actions/runs/34706741599), job `103588050409`, and push run [34706740298](https://github.com/KokunoYumeto/zeta-function-research-reader/actions/runs/34706740298), job `103588046433`, both fail at `formal/splitzero/SplitZeroBoundaryIntegration.lean:111:2`.
The proof simplification produces `{false,true}=empty` while the goal is `False`; compilation of the final module does not complete, so the new axiom-report stage is skipped. A same-head rerun alone is not an evidenced repair.

The PR body still names `d050a5...` and says pending. Until a repaired head passes, the public wording should say the actual head's final module fails compilation, with all analytic/spectral exclusions retained. Do not turn successful Python regressions or five compiled earlier modules into a claim that the full six-module/66-target integration is certified.

## PR17 bounded mathematical review

Exact note SHA-256: `551e3fe89b4409d5ed1eeacfaac4cb7d9c1291978127de1b4f989b272bd24a47`.
Exact checker SHA-256: `0e91d91c626106bf14bb68f44f2052400209f9185a299764d2ebc2f9e96cc4f2`.

The following displayed source structures were checked without changing their coordinates or measures:

- `RESEARCH_NOTE.md:23–57`: restriction through `C[S] -> E_h^tensor k`, the `SI-A` resolution, algebraic transpose (not Hermitian adjoint), Ext degree and cochain shift, resolvent residue pairing and characteristic-polynomial trace;
- lines 61–89: `S=s1+s2`, `r=s1-s2`, `Delta=r^2`, invariant ideal `(H0,Delta H1)`, retained diagonal nilpotents, filtered Hilbert series and the two original primitive signs;
- lines 93–121: actual arithmetic weight, Jacobian `1/2`, `Delta=-v^2`, complete relative-coordinate matrix weight, all-k Jacobian one, and degree-dependent exponential bounds;
- lines 125–137: invertible coordinate congruences and the Schur-complement isometry with its actual polynomial image retained;
- lines 141–171: raising/lowering commutators, primitive ladders, occupation multiplicities and retained nilpotent trace structure. The auxiliary decomposition Gram is explicitly not substituted for the arithmetic Gram;
- lines 175–181: Gaussian calibration is labelled a different measure, while arithmetic tensor estimates, purity and RH are not claimed.

The two cited primary Stacks entries were checked directly: [0AVV, affine pushforward](https://stacks.math.columbia.edu/tag/0AVV) supports the quasi-coherent affine-module description, and [0AWZ, finite pushforward right adjoint](https://stacks.math.columbia.edu/tag/0AWZ) supports the specified restriction-of-modules adjoint rather than a blanket assertion for all sheaves. The note's distinction is correct.

No blocking contradiction/type/sign/status error was found in this bounded review. This is not a fresh audit of all analytic source inputs, the expanded 24-method conversation suite, or Weil II. The finite replay here used SymPy 1.13.1; the source validation file preserves its earlier 1.14.0 run rather than pretending the runtimes are identical. All eight methods pass in both modes and both nine-test negative-control runs exit 1. Full outputs are in `pr17_finite_replay.json`.

The local candidate repeats the inherited `M>=k(d-1)` range when invoking full-quotient Gram/control inverses (`PR14 RESEARCH_NOTE.md:286–312`) and explicitly identifies the finite module `E` used by the resolution. This removes ambiguity about unsaturated lower-degree filtered pieces, without adding a new theorem hypothesis or altering an equation.

## Local candidates and integrity records

Candidates are under `reviews/corrections/workbenches/tau-coherent-interpolation/RESEARCH_NOTE.md` and `reviews/corrections/workbenches/tau-spectral-sum/RESEARCH_NOTE.md`.
`MINIMAL_CORRECTIONS_MANIFEST.json` binds original/corrected hashes and the exact diff. `MINIMAL_CORRECTIONS.diff` contains only the explanatory changes described above; all 69 PR14 and 30 PR17 displayed equation blocks are byte-identical. Original downloaded files remain untouched.

`merge_readiness_fetch_receipt.json` binds every fetched PR14–17 file to exact head/Git blob/SHA-256.
`pr18_bounded_metadata.json`, `pr18_bounded_checks.json` and `pr18_bounded_actions.json` are the separately captured moving-draft status. The review does not keep chasing PR18 or let it delay the already-reviewed backlog.
