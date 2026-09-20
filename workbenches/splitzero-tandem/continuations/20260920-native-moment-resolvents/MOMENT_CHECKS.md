# Exact finite-check and proof-validation receipt

Date: 2026-09-20.

Command: `python verify_moment_enclosures.py`

Exit status: 0. All arithmetic is exact rational, Gaussian-rational, or symbolic. The script completed 592 positive-semidefinite checks, together with the displayed matrix and polynomial identity tests.

Checked both parity test blocks, target degrees 0–2, auxiliary degrees n and n+1, and poles 1, 4, 9, 16. The tests cover:

- Complementary native-moment formulas for the Stieltjes and x-resolvents.
- Exact residual matrix identities before choosing a coefficient vector.
- Monotone lower and upper bounds under auxiliary-degree enlargement.
- Exact shifted-moment pole-rate certificate and complete finite Stieltjes weight sum.
- Positive quadratic-denominator variational lower bound and both orderings of the correctly signed partial-fraction upper bound.
- Original-form complex coefficient congruence, nontrivial retained physical-unit matrix, fixed observation kernels, complete conductor fibre, and both signed four-endpoint determinant bounds.
- Symbolic reciprocal-polynomial error cancellation through degree 6.
- Independent checks of the root RR6–11 rank-one formulas on both parity test blocks, target degrees 0–2, r=n+1 and n+2, and poles 4 and 16.

The finite atomic measures are test instances for universal identities only. They are explicitly not the native arithmetic measure. No native moment, period, unit phase, observed current sign, or arithmetic asymptotic was assigned a numerical value.

The standalone proof is `NATIVE_RESOLVENT_MOMENT_ENCLOSURES.tex`. Local repeated `pdflatex -interaction=nonstopmode -halt-on-error -jobname=moment_enclosures_math_check NATIVE_RESOLVENT_MOMENT_ENCLOSURES.tex` validation exited 0 and produced a 10-page private check output. The final log has no undefined references and no overfull boxes. One bibliography underfull-box notice remains. This validation is not publication or packaging.

Independent review of the complete root rank-one proof is recorded in `ROOT_RANK_ONE_REVIEW.md`. No mathematical defect was found and no root file was modified.

The remaining input boundary is explicit: actual native moments must be supplied exactly or enclosed with certified errors to obtain numerical values of the matrix bounds. The proof provides finite stopping certificates and native fixed-pole convergence, but does not assert an unproved auxiliary-depth complexity rate or numerical phase value.
