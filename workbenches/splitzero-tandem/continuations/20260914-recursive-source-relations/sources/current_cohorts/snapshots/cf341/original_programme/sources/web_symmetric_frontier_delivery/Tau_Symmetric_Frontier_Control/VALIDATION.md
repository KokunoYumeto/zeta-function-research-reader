# Validation record

Python 3.13.5, SymPy 1.14.0.

- 22 named tests passed normally and under `python -O`.
- Success JSON files are byte-identical.
- Intentional false controls failed in both modes, with process exit status 1.
- No Python `assert` statement is used in the checker; unittest checks and explicit exceptions remain active under optimization.
- Input Git blob calculated from the mounted markdown: `4ec40c15397128552bc276ec903fe59c89657d4e`.
- That equals the pinned repository source read by the connector.

The tests cover finite algebra, not the arithmetic theta range, moment integration,
convergence, a uniform weight estimate, or an RH claim. No Lean execution was performed.
The Gaussian examples are declared calibration measures. Their literal mass is
retained by the equations and the exact mass-scaling regression.

Two initial display-fixture failures exposed a basis comparison that was missing
from the test expectation. The explicit matrix from `(1,s-1/2)` to `(1,s)` was
inserted and is retained in the note. No mathematical target was weakened.

GitHub write actions were not exposed in this turn; provider discovery returned
the installed GitHub connector without an additional write action. The add-only
patch is supplied for integration. No main branch, other-session branch, original
source, workflow, or dependency was changed.
