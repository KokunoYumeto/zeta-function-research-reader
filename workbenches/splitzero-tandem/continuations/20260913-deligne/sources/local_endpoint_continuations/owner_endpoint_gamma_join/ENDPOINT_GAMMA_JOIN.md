# Endpoint degree selection in the actual gamma-corrected coordinates

This short calculation joins the complete written endpoint criterion in PR #23
(reported source revision `c720f40530eed2f5969dbabe94dfd3fddc0f507f`) to the
gamma convolution descent supplied on 13 September 2026. It uses the original
arithmetic source, the original polynomial relation, and the same canonical
quotient metric. It is a written substitution and finite-dependence proof,
not an additional Lean theorem or a uniform arithmetic estimate.

## Objects and the estimate being evaluated

Fix the original packet h and tensor degree k. Put alpha_k=2k lambda and keep
the source and reference Hankel determinants D_j and D_j^Gamma of GD.28.
Their positive quotient is X_j=D_j/D_j^Gamma. For the original relation chi,
of degree q>=1, let Y_j=B_j/B_j^Gamma and

\[
T_N=\frac{X_{N+1}}{Y_{N-q+1}},\qquad
V_N=\det G_N=V_N^\Gamma T_N,\qquad N\ge q-1.
\]

Here T_N is a positive scalar correction ratio, not the coordinate operator
also denoted T in the Toda calculation. Let n>=q and r>=1 be integers. The
endpoint criterion uses the actual quantities

\[
\mathcal A_{n,r}=\left(\frac{\omega_{n+r}}{\omega_n}\right)^{1/(2r)},
\qquad
\mathcal B_{n,r}=\log\frac{V_{n-1}V_n}{V_{n+r-1}V_{n+r}}.
\]

Its complete Jensen and telescoping proof gives

\[
\min_{0\le j<r}\epsilon_{h,k,n+j}
\le \mathcal A_{n,r}\sinh\left(\frac{\mathcal B_{n,r}}{2r}\right).
\tag{EG.1}
\]

No metric is selected here: the finite minimum is over the pre-existing
canonical representatives at degrees n through n+r-1.

## Exact reference and arithmetic factors at the endpoints

At the original observation theta=0, GD.28--29 gives

\[
\omega_j=c_\lambda^k j!(\alpha_k)_j\frac{X_{j+1}}{X_j}.
\tag{EG.2}
\]

Consequently,

\[
\boxed{
\mathcal A_{n,r}
=\bigl((n+1)_r(n+\alpha_k)_r\bigr)^{1/(2r)}
\left(\frac{X_{n+r+1}X_n}{X_{n+r}X_{n+1}}\right)^{1/(2r)}.
}
\tag{EG.3}
\]

The mass c_lambda^k is retained in EG.2 and cancels between the two specified
norms. The arithmetic mass mu_h^k was never assigned the value one. Each
rising factorial in EG.3 is the exact r-factor product, not a large-degree
approximation.

Substitution of V_N=V_N^Gamma T_N gives a second exact identity:

\[
\boxed{
\mathcal B_{n,r}
=\log\frac{V_{n-1}^\Gamma V_n^\Gamma}
               {V_{n+r-1}^\Gamma V_{n+r}^\Gamma}
+\log\frac{T_{n-1}T_n}{T_{n+r-1}T_{n+r}}.
}
\tag{EG.4}
\]

The reference quotient volumes in this expression are formed with the same
chi, using its two conjugate differential factors in GD.30. The roots,
their orders and the centre k/2 have not been changed. All ratios are
positive, so the real logarithms and the indicated positive roots exist.

Equations EG.3--4, inserted in EG.1, express the endpoint selection estimate
through an explicit reference factor, four source corrections X, and four
source-to-relation corrections T. A pointwise upper bound T_N<=C_h^(kq)
does not control the denominator in EG.4. Neither of these exact identities
supplies that missing quantitative estimate.

## Exact finite input count for the whole endpoint expression

The maximum source degree occurring in EG.1--4 is n+r: omega_(n+r) is its
highest monic polynomial norm, and V_(n+r) is its highest quotient metric.
Each defining source or relation Gram entry is the integral of a polynomial
of degree at most 2(n+r) against the original arithmetic sum measure.
The gamma coefficient theorem therefore proves that the complete endpoint
expression is determined by

\[
\boxed{c_{h,0},c_{h,1},\ldots,c_{h,2(n+r)},\quad k,\lambda,\chi.}
\tag{EG.5}
\]

The zeroth coefficient carries the original total mass. The higher
coefficients may have either sign. The finite coefficient-power formula
and the Schur complement give the actual endpoint values; an arbitrary
positive moment matrix cannot be inserted in their place. EG.5 gives a
finite route for each chosen window. It does not bound the conditioning
of the matrices or permit truncating the growing input count uniformly.

## Source roles

- [PR #23 endpoint proof at its supplied revision](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/c720f40530eed2f5969dbabe94dfd3fddc0f507f/workbenches/tau-toda-volume-formal/ENDPOINT_CRITERION.md): finite Jensen selection, four-volume telescope, two-norm telescope. The user supplied its complete proof, which was read and the telescopes checked. Current CI/source review is recorded separately.
- Tau Gamma Convolution Descent, GD.25 and GD.28--35: exact coefficient transform and source/reference determinant ratios. The full original note and independent finite/analytic review are retained in this edition.
- GJ.1--8 in the gamma chapter: the explicit analytic map from the same one-factor moment function to the coefficient series, and finite source/quotient derivative jets.

The new content here is their literal endpoint-coordinate substitution and
the maximum-degree input count. No additional theorem about zeta-zero
locations or a completed growing-window bound is claimed.
