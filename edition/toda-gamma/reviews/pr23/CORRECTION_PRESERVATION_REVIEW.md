# PR #23 merge and two-sentence correction: preservation receipt

PR #23 merged at `f3648b18212f7e072437a6f9c62461e6b0a7c870`, with ordered parents `b32ca2128e0deb0eec6eafb860776a5d6a28dcbb` and reviewed head `c720f40530eed2f5969dbabe94dfd3fddc0f507f`. Its actual tree `d136a217989e275d42d501d65a0b46b9b4f7dc53` exactly matches that reviewed head, including all paths, object types, file modes, and blob hashes. The merge adds fourteen files to its main parent and modifies or deletes none. Inherited implementations are unchanged.

One authorized SHA-guarded contents update then produced correction commit `3b07cac9427f0132cc74a33598435144544abb54`, whose sole parent is that merge. Only `workbenches/tau-toda-volume-formal/ENDPOINT_CRITERION.md` changed, by two sentence replacements:

- The geometric-mean endpoint bound is never larger, and potentially strictly smaller, than the bound obtained using the largest recurrence factor.
- The first exterior operator norm is at most epsilon: it equals epsilon for `1<=p<=q-1` and is zero for `p=q`.

The complete before and after documents were read. The independent byte comparison confirms the after document is precisely those two replacements, with every other byte preserved. The Git commit records two added and two removed lines in one file. No Lean source, checker, manifest, workflow, inherited object, or file mode changed.

Before blob: `aa2f449a8829532672dc308282446ad3b24bb54f`.

Before SHA-256: `61dd03044ad56b2baf3671fa217497b0f4749c1259f841cdc8491846abbd2e46`.

Corrected blob: `09d658b1c50245b9e340722817bc9487f1ce409a`.

Corrected SHA-256: `a9a8b080b3779f82388a8bd4338ada2564ceb2410a0734bd58700f65c7789c62`.

The premerge terminal review remains valid for the unchanged finite Lean/checker bytes. Separate post-merge and correction CI jobs were triggered; they were still running when this stable preservation receipt was prepared. This receipt does not claim their terminal success and does not depend on live CI snapshots. Final remote CI evidence will be recorded separately.

The written Jensen endpoint theorem and exact second-exterior capacity formula are unchanged. The Jensen/root assembly is not newly formalized in Lean, and arithmetic asymptotic estimates remain unproved. No real-zero conclusion follows merely from these finite certificates.

Only the authorized endpoint correction was written remotely by this follow-up; the parent workflow performed the merge. No local Lean, heavy build, PR #24 review/change, usage reset, or child agent was used.

Corrected source: https://github.com/KokunoYumeto/zeta-function-research-reader/blob/3b07cac9427f0132cc74a33598435144544abb54/workbenches/tau-toda-volume-formal/ENDPOINT_CRITERION.md
