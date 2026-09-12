# PR #23 merge and endpoint-note correction

## Verified merge and source preservation

PR #23 was merged at `f3648b18212f7e072437a6f9c62461e6b0a7c870`. Its ordered parents are current main `b32ca2128e0deb0eec6eafb860776a5d6a28dcbb` and reviewed PR head `c720f40530eed2f5969dbabe94dfd3fddc0f507f`.

The merged tree is `d136a217989e275d42d501d65a0b46b9b4f7dc53`, exactly the reviewed head's actual Git tree. Complete nontruncated tree entries, including paths, object types, modes, and hashes, agree. Relative to the main parent, the merge adds exactly fourteen files, modifies none, and deletes none. Inherited implementations and reviewed PR #22 bytes are unchanged.

Merge: https://github.com/KokunoYumeto/zeta-function-research-reader/commit/f3648b18212f7e072437a6f9c62461e6b0a7c870

## Two authorized wording corrections

The complete endpoint document was freshly read from main. One SHA-guarded contents update then committed precisely the two previously reviewed wording corrections at `3b07cac9427f0132cc74a33598435144544abb54`, whose sole parent is the merge above.

1. The geometric-mean endpoint bound is now described as never larger, and potentially strictly smaller, than the bound using the largest recurrence factor. Equal recurrence values need not produce a strict improvement.
2. The first exterior control norm is now described as at most epsilon, equal to epsilon for `1<=p<=q-1`, and zero for `p=q`. Its multiplicity and the exact second-exterior capacity formula are unchanged.

The correction changes only `workbenches/tau-toda-volume-formal/ENDPOINT_CRITERION.md`, with two added and two removed lines. The whole post-update document was read back and matched against the expected two byte-string replacements. Every other byte and every file mode is preserved; no Lean source, checker, manifest, workflow, or inherited object changed.

| Document version | Git blob | SHA-256 |
| --- | --- | --- |
| Before | `aa2f449a8829532672dc308282446ad3b24bb54f` | `61dd03044ad56b2baf3671fa217497b0f4749c1259f841cdc8491846abbd2e46` |
| Corrected | `09d658b1c50245b9e340722817bc9487f1ce409a` | `a9a8b080b3779f82388a8bd4338ada2564ceb2410a0734bd58700f65c7789c62` |

Correction: https://github.com/KokunoYumeto/zeta-function-research-reader/commit/3b07cac9427f0132cc74a33598435144544abb54

Corrected note: https://github.com/KokunoYumeto/zeta-function-research-reader/blob/3b07cac9427f0132cc74a33598435144544abb54/workbenches/tau-toda-volume-formal/ENDPOINT_CRITERION.md

## Post-merge CI

All four triggered main-merge jobs and the separate documentation-correction Toda job are now `completed/success`, as are all five check runs and every step in those jobs. Their complete logs were fetched and independently parsed; no CI rerun was requested or performed.

| Revision | Run | Job | Successful evidence |
| --- | --- | --- | --- |
| Merge | 34725346271 | 103638389909 | Toda: exact 30 new raw reports; inherited 50/29/40/68/38/87/73 reports; structural 28 pass |
| Merge | 34725346263 | 103638389976 | Exterior: exact 50 raw reports; inherited 29/40/68/38/87/73; structural 28 pass |
| Merge | 34725346270 | 103638389853 | Conormal: exact 29 raw reports; inherited 40/68/38/87/73; structural 28 pass |
| Merge | 34725346301 | 103638389915 | Frontier: exact 40/68/38/87/73 report sets; structural 28 pass |
| Correction | 34725439222 | 103638631191 | Toda: exact 30 new raw reports; inherited 50/29/40/68/38/87/73 reports; structural 28 pass |

Both Toda jobs check all five new modules and four inherited exterior modules individually with `--trust=0 -DwarningAsError=true`, then complete the inherited rebuild, combined import, and subsequent audits. The source hashes match the independently reviewed files. Every parsed dependency set is a subset of `propext`, `Classical.choice`, and `Quot.sound`; exact raw target coverage is checked with the unchanged fail-closed parser. The thirteen exact-rational methods and twenty-five inherited harness tests pass normally and under `python -O`, with deliberate-failure controls failing as intended. These remain finite calibrations, not arithmetic interval certificates.

Correction run: https://github.com/KokunoYumeto/zeta-function-research-reader/actions/runs/34725439222/job/103638631191

The previously frozen `CORRECTION_PRESERVATION_REVIEW.md` and its receipt accurately recorded that CI was pending at their creation. This final terminal review supersedes only that historical CI status; the frozen source-preservation facts and hashes remain unchanged.

## Research boundary is unchanged

The five Lean modules check the original weighted/unweighted relation correction, source/relation determinant calculation, two-loss scalar identity and bounds, finite telescopes/selection, and composition with the inherited original-Gram trace certificate. The selected thirty new declarations and inherited fifty exterior declarations are finite algebraic certificates.

The four-volume/two-norm endpoint-selection theorem retains its complete written Jensen proof and explicit nonnegative-root assembly. The two telescopes and finite-selection lemmas are Lean-checked; the full Jensen assembly is not a Lean theorem here. The candidate arithmetic asymptotic bounds remain unproved. No real-zero assertion or proof of the Riemann hypothesis is inferred from positivity, the Toda identities, determinant accounting, or finite CI.

The exact second-exterior allowance remains `epsilon*min(s,r_p,D_p-s)` under the stated spectrum and degree hypotheses. The zero exterior degree is a scalar line with zero additive control; a positive-radius two-direction spectrum requires dimension at least two. Those degenerate cases do not change the corrected formula's scope.

## Evidence and action boundary

The local evidence retains full before/after document bytes, the minimal API diff, Git commit/tree records, complete terminal CI logs, and independent parsing results. `MERGE_CONTINUITY.json` and `ANALYSIS_RECEIPT.json` record the machine-checkable continuity and audit facts; the final seal binds these and this report by SHA-256. Public derivatives should include the bounded review and receipts, not raw account metadata, downloaded logs, or local execution scripts.

The only remote mutation made by this follow-up was the explicitly authorized, SHA-guarded two-sentence endpoint correction. The parent workflow performed the PR merge. No local Lean, heavy build, PR #24 review/change, usage reset, or child agent was used.
