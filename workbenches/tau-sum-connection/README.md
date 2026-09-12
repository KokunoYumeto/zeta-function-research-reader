# Sum-fibre connection and conormal trace

Read RESEARCH_NOTE.md for the proofs and HANDOFF.md for bounded formalization targets. This is an add-only continuation of the spectral-sum workbench. The expanded conversation package also contains the LaTeX/HTML reader, full proof detail, source manifests and rerun logs, numerical theta-seed evaluation, and programme state.

Run from this directory with Python and SymPy installed:

    python check_sum_connection.py --json normal.json
    python -O check_sum_connection.py --json optimized.json
    python check_sum_connection.py --self-test-failure

The third command must fail. No dependencies, workflows, existing notes or formal sources are changed. The new scalar contraction retains the complete arithmetic mass and relative residual; it is not claimed to be the full Deligne-like weight estimate.
