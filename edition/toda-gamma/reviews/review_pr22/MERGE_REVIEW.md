# PR #22 merge and exact-commit post-merge CI readback

## Actual merged result

PR #22 is closed and merged, not merely approved or ready. GitHub records merge time `2026-09-12T23:05:09Z` and merge commit `b32ca2128e0deb0eec6eafb860776a5d6a28dcbb`. The reviewed head is unchanged at `811210d24b80813a08972ca23f919db015383137`. The latest main-ref observation points to the merge commit.

- Merge Git tree: `dc3feee138475fcad0c782087845ee44137ce208`.
- Actual first parent: `199d2bbfbf551de8272e573a9ce90bd5f1005988`, the already-published mirror.
- First-parent Git tree: `07b6b906dd40b41894d991d54bb6dd167ae37f23`.
- Second parent: the exact reviewed PR head `811210d24b80813a08972ca23f919db015383137`.

The PR API's `base.sha` still reported the older `fa4be32f87a9a90f3c02a07f7790dea95a1e7b0f`. This is distinct from the authoritative merge commit's first parent and live main ref. No conclusion about the merge base was inferred from that stale metadata field.

Full, nontruncated recursive Git trees were fetched for the actual first parent and merge. Every one of the 2,967 preexisting leaves has the identical path, object type, file mode and blob/submodule object ID in the merged tree. The merged tree has 2,977 leaves: precisely ten additions, all matching the reviewed PR's Git blob IDs. No preexisting reader, formal source, publication artifact or other tracked leaf was replaced, deleted or changed in this merge.

## Separate post-merge CI result

All three workflows actually triggered for exact merge commit `b32ca2128e0deb0eec6eafb860776a5d6a28dcbb` are now terminal successes. Every job step completed successfully; none was skipped. This is fresh post-merge evidence, separate from the nine successful premerge-head checks.

| Workflow | Run | Job | Terminal result |
| --- | --- | --- | --- |
| Exterior trace collaboration | 34724472394 | 103636068646 | completed/success |
| Conormal cyclic tower | 34724472442 | 103636069009 | completed/success |
| Finite frontier | 34724472427 | 103636068718 | completed/success |

The complete terminal logs were downloaded and hashed. An independent offline analysis verifies:

- Exterior has exactly the 50 selected raw declaration reports and matches all four reviewed source hashes. Its inherited reports exactly cover conormal 29, frontier 40, boundary integration 68, boundary 38, tau 87, and derived 73, plus the structural 28-target PASS.
- Conormal has exactly its 29 selected raw reports and the same inherited report sets excluding exterior.
- Frontier has exact 40/68/38/87/73 target sets and the structural 28-target PASS.
- Every parsed axiom dependency is within `propext`, `Classical.choice`, and `Quot.sound`; no `sorryAx` or CI error marker occurs.

These are successful finite-source/kernel-check and selected transitive-axiom reports. They do not establish an analytic Toda estimate or RH and do not expand the mathematical scope stated in the sealed premerge review.

## Evidence

`MERGE_RECEIPT.json` separates the actual merge facts from latest exact-merge CI state and binds the final full API/log snapshot. `MERGE_TREE_CONTINUITY.json` binds both full trees and the complete preexisting-leaf preservation check. `POSTMERGE_CI_ANALYSIS.json` records exact target-set verification and source/log hashes. `MERGE_REVIEW_SEAL.json` seals these receipts, this report, and the supporting read-only scripts.

No remote mutation, rerun, local Lean/build, usage reset or browser operation was performed by this readback. The bounded wait ended with all observed exact-merge workflows successful.
