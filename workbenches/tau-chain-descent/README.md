# Tau-base chain descent

Additive research continuation of [PR #8](https://github.com/KokunoYumeto/zeta-function-research-reader/pull/8), pinned at `25689c5376166df37801229bc275ff5a896007d9`.

Read [RESEARCH_NOTE.md](RESEARCH_NOTE.md) for the complete derivations. This contribution uses the original split support and the actual finite packet maps in `../tau-base-cohomology/FINITE_OPERATOR_COMPARISON.md`.

The new calculation is the chain-level extension behind the finite spectral projector. Its class is the retained local unit `j_h(h/(2 xi))`. It determines a rank-one arithmetic scaling boundary and the same unit morphism used in the residue/Jacobian trace pairing. The original mixed-support synchronization resolves a concrete failure of homotopy naturality across the two source legs; the difference of the two synchronized homotopies remains an explicit degree-zero cycle.

The note supplies the equivariant derived roof, strict reflection for the specified section, finite-rank cochain Lefschetz traces, and tensor homotopies with signs. It does not prove RH, a weight bound, or a global spectral-synthesis theorem.

## Reproduction

With Python and SymPy installed, run from this directory:

```sh
python3 check_chain_descent.py --json results.json
python3 -O check_chain_descent.py --json results.optimized.json
cmp results.json results.optimized.json
```

The negative controls must return a nonzero exit status:

```sh
python3 check_chain_descent.py --deliberate-failure
python3 -O check_chain_descent.py --deliberate-failure
```

See [VALIDATION.md](VALIDATION.md) and [check-results.json](check-results.json). These are finite algebraic regression tests, not new Lean certificates or analytic proof verification.

No existing source, formal module, dependency pin, workflow, or frozen reader is changed. The owner's mathematical programme and its prior formalization remain the source; this continuation records AI-assisted derivations under that direction. No private transcript or source-literature corpus is included.
