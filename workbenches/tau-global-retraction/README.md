# Global theta retraction over the tau base

Additive continuation of the owner's SplitZero programme and tau-chain-descent PR #9.

The [research note](RESEARCH_NOTE.md) constructs a continuous left inverse of the **unchanged** theta map on the workbench's full test-function spaces. It uses arithmetic Mobius inversion on the position and Fourier exterior regions, an explicitly retained pair of cutoffs, and a proved strict-contraction inverse. Both source moments are restored by a displayed projection.

The result gives a closed, complemented theta image and a continuous contraction of the entire original cochain complex onto its arithmetic quotient. The construction is propagated through the original internal quotient and mixed-support synchronization. It extends the preceding finite-packet sections by an explicit theta boundary, preserving their Ext class and residue/Jacobian trace.

The note also calculates the global scaling cocycle, the continuous-dual sequence, completed tensor contractions, and the exact boundary terms in an auxiliary metric's covariance defect. It retains the common spectral kernel and the separate balanced analytic kernel.

## Files

- `RESEARCH_NOTE.md`: definitions, typed maps and written analytic proofs.
- `check_global_retraction.py`: twelve exact finite regression tests.
- `check-results.json`: actual successful local run.
- `VALIDATION.md`: source identity, run record and scope.

## Reproduce the finite checks

```sh
python check_global_retraction.py --json normal.json
python -O check_global_retraction.py --json optimized.json
cmp normal.json optimized.json
python check_global_retraction.py --deliberate-failure
python -O check_global_retraction.py --deliberate-failure
```

The final two commands must exit with status 1. These tests do not certify the analytic arguments or run Lean.

Base: `8f99b94d306c3b1aaa817d52c57fa6fd298d511c`. Only this new workbench is added; original mathematics, Lean modules, source books, licensing and existing workflows are untouched. Research draft for review, with no automatic merge. AI-assisted derivations under the owner's direction; no global-priority or RH/GRH claim.
