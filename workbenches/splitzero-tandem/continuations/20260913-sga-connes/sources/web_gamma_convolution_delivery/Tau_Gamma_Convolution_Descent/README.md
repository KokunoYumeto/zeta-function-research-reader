# Gamma convolution descent for arithmetic control

Read `index.html` for the full mathematical continuation, or `NOTE.tex` for the
editable LaTeX. `HANDOFF.md` gives bounded targets for the parallel formalization;
`PROGRAMME_STATE.md` records the exact next analytic estimate.

The contribution extends the repository's own gamma reference through the
spectral-sum map, retaining its mass, the arithmetic multiplier, all relative
polynomial directions, the original theta relations and their supported zeros.
It supplies exact all-k coefficients, source/quotient comparisons, explicit
reference determinants and a rigorous polynomial-moment tail bound.

Reproduce the finite checks with:

    python check_gamma_descent.py --json checks/normal.json
    python -O check_gamma_descent.py --json checks/optimized.json

`--fail-control` must exit unsuccessfully. SymPy 1.14.0 was used.
The numerical theta script is separate and does not use interval arithmetic.

The complete analytic statements have written proofs; no Lean certificate,
validated arithmetic quadrature, RH proof or remote publication is asserted.
