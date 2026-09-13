# Confluent transfer for the arithmetic source–relation volume

[Read the complete public proof](RESEARCH_NOTE.md) and [the formalization handoff](HANDOFF.md).

The new map uses a 2q-by-2q matrix of raw jets of consecutive source orthogonal polynomials to calculate the actual relation norms, quotient determinant ratios, and retained phase of the canonical arithmetic control. It does not replace the original e/tau construction, arithmetic unit, theta relations, canonical metric, action or trace.

Run `python check_transfer_core.py --output core.json` and `python -O check_transfer_core.py --output core-optimized.json`. The public core contains eight test methods over exact declared finite fixtures. `--negative-control` must fail. These computations are not a new Lean certificate or an enclosure of actual arithmetic moments.

This is an add-only analytic workbench alongside the parallel formalizations. No dependency pin, inherited source, existing workflow or other-session branch is changed. The remaining asymptotic estimate is explicitly retained in the proof note.
