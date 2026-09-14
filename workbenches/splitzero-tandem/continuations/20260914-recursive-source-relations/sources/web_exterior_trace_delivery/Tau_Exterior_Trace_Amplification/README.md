# Exterior trace amplification

Open **index.html** for the self-contained MathML reader. **NOTE.tex** and **RESEARCH_NOTE.md** contain the derivation. **HANDOFF.md** supplies bounded targets for the parallel formalization session; **PROGRAMME_STATE.md** records the exact new growth criterion and what is still unproved.

Main result: on the original canonical cyclic arithmetic metric, exterior control keeps the same rank-two allowance. The determinant line of all positive-defect generalized eigenspaces gives an exact sum bound. For a full nonreal quartet it forces a cubic lower bound on any candidate control excess. The corresponding subcubic upper estimate remains an analytic research target, not a theorem of this package.

The original tau-base, infinite quotient, supported e, full multiplicities and units, source relations, factorials and cochain signs remain in the displayed maps.

Run exact regression checks:

```sh
python check_exterior_trace.py --json checks/fresh-normal.json
python -O check_exterior_trace.py --json checks/fresh-optimized.json
python check_exterior_trace.py --fail-control
```

The last command is expected to exit with status 1. SymPy is required. These are finite algebraic regression checks, not Lean certificates or tests of actual off-line zeta zeros.

No remote repository was changed. Source scope and corrections are in **SOURCE_REVIEW.md**.
