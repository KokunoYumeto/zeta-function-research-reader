# Exact validation — 20 September 2026

The standalone source is `BURNOL_ORIGINAL_THETA_TRANSFER.tex`.

- Exact algebra check: `python check_exact_transfer.py` passed all 116 assertions. It covers multiplicities 1 through 9; factorials, anti-triangular reversals and both jet inverses; a three-root complete divisor with multiplicities 3, 2, 1; every partial-fraction coefficient; original physical-unit conversion; polynomial degrees 0 through 12; and unchanged-fibre Gram/Schur identities at degrees 1 through 6.
- The checks explicitly use artificial exact algebraic data. They do not claim to verify zero locations, analytic convergence, or RH numerically.
- An independent mathematical derivation checked the complete local native and physical jet matrices, reciprocal coefficients, Gamma factors, factorials, bilinear versus Hermitian conventions, determinants, and multiplicity-two/three examples.
- The analytic map is proved in the standalone source: full Hilbert-domain multiplier; original-topology seminorm estimates on L_1; compactness; injection into the original strong theta quotient; and the exact all-degree polynomial-source correction.
- `pdflatex -interaction=nonstopmode -halt-on-error BURNOL_ORIGINAL_THETA_TRANSFER.tex` compiles successfully to 11 pages. Final compilation has no LaTeX warnings, undefined references, or overfull boxes. Publication rendering/visual QA remains root-owned; this is a compilation check only.
- The already established fixed-divisor collapse is explicitly received from `EXACT_CORPUS_RECEIVERS.tex`, RC7–RC8, through the identical relation columns and Schur matrix. It is not labelled a new result.

Frozen TeX SHA-256: `d4f96e03c3d506b9d384c7bc5a1f499a29d14aa88706937e84a195167f0040f8`.

Exact-check script SHA-256: `56b5c31fc15775ceee400a59e4d0b90938336a74de2d193a93ba408037ed1679`.

No publication, remote mutation, timeline creation, or change to another source file was performed by this derivation task.
