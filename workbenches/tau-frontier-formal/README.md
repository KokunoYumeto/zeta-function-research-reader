# Finite frontier formalization and integration with the completed Codex work

This is an additive contribution to the owner's SplitZero/theta workbench.
The five new Lean source files passed together at
`beb6535b75c81a4075ffbe680362c741cfe15d45`, run 34711164173,
job 103600099708. The completed job and full log were read back.

That run checked every new file separately with
`--trust=0 -DwarningAsError=true`, accepted all 40 selected new transitive
axiom reports, and rechecked the prior 38 boundary, 87 tau, 73 derived and
28 structural targets. The eighteen inherited checker tests passed normally
and under `python -O`. These are checking-harness tests, not the source's
22 mathematical regression methods. Only propext, Classical.choice and
Quot.sound occur in the accepted reports.

## Integration snapshot

While this contribution was being checked, PR #16 completed and was merged.
The exact new main snapshot is
`fd414804b9bae5f7e8e5714d94b3be43f412d30d`, containing Codex's final PR #16
head `566083775551a7ecc9a5884b16a8b9b927adc2f0`, as well as the merged PR #17
spectral-sum research note. The earlier coordination paragraph in RESEARCH_NOTE
records a development snapshot; its mention of a failed #16 run is historical,
not the final status. The final #16 receipt reports its successful 66-target
check at run 34710753565/job 103598989742.

The integration commit imports that pinned main snapshot into this PR branch,
retaining all of its files. Our five source blobs, target manifest, checker and
mathematical note are byte-identical to the successful baseline. The added
workflow now checks Codex's six modules and 66 targets, the five new frontier
modules and 40 targets, and all inherited audits in the same workspace. It also
checks a combined import of both developments. The final PR validation record
identifies the completed combined run; a pending run is not a certificate.
Main itself and both other-session branches were not modified by this work.

## Mathematics and source scope

The modules cover the finite cross estimate; the raising/lowering cancellation
and k-1 incidence cost; explicit primal/kernel and invariant-coordinate identities;
signed finite-group averaging on the original cochain windows; and the actual
linear equivalence between projected-subcomplex homology and the selected part
of the original homology. See RESEARCH_NOTE.md for complete bounded proofs and
the precise hypotheses still needed from the analytic theta construction.

The source is the owner's complete Symmetric Frontier Control markdown and the
preceding Kernel Layer Integration supplement. The local execution service failed
before the newest ZIP could be opened. Its manifest and reported 22-test suite
were not independently rerun here. No private transcript is republished.

The original scalar, e/tau distinction, arithmetic quotient, dependency pins,
analytic normalization and full spectral jets are unchanged. The toolchain is
Lean 4.31.0 and Mathlib fabf563a7c95a166b8d7b6efca11c8b4dc9d911f.
The polynomial degree-shift realization, completed tensor permutation action,
and uniform sublinear arithmetic estimate remain separate instantiations.
