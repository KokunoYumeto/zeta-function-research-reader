# Complete independent review of IGO1–IGO28

Reviewer: `/root/intrinsic_gamma_completion/intrinsic_formula_review`.

Source read in full:
`intrinsic_order_20260914/INTRINSIC_EXTERIOR_GAMMA_ORDER.tex`.

Accepted source SHA256:
`a086f4f2ea260621f5e1a1ec5ca2d0ce8843b464634d35f9affba276a472920f`.

Result: **PASS for every claim and proof in this source. No repair is
required.** This is a mathematical source review, not a PDF layout review.
The earlier `INTRINSIC_FORMULA_REVIEW.md` contains independently derived
proofs of the Wronskian, degree, mixture, density factors, and translations;
this review additionally covers the actual complete final source.

## Source transforms and original relation

IGO1 retains the actual packet order, multiplicity, original centre, and
all root coordinates. Restricting the input source to `s in {1,k}` is
consistent with the stated two existing sources; it does not choose an
auxiliary order to achieve a desired asymptotic scale.

IGO2–IGO4 retain the full source mass. In particular, substitution of
`s=1`, `b=1/2`, `Gamma(1/2)=sqrt(pi)` into `M_s rho_b` gives precisely
`|Gamma(1/4+iy/2)|^2/(2pi)`. The beta substitution `u=exp(2x)` produces
the displayed factor 2. The resulting inverse Fourier coefficient is
`1/(2pi)`. Integrability of the first two derivatives of `sech(x)^v`
justifies integrability of its Fourier transform and Fourier inversion.
The contour displacement has the sign required to produce
`exp(-theta |y|)`; the zero-free cosh strip supports the analytic branch.
This proves all polynomial exponential moments on the stated open strip.
The characteristic identity extends holomorphically there and yields the
Laplace identity. The Euler product and beta limit supply the claimed
strict positivity. The original-line translation and its polynomial
inverse have triangular coefficient matrix with diagonal one.

The final source's added original-order recurrence is exact:
`k/4=l+1/4`, and the squared Gamma recurrence contributes `4^(-l)`.
The coefficient relative to sigma is
`M_k 2^(k/2-1-2l)/Gamma(k/2)`, whose exponent is exactly `-1/2`.
This is the displayed `beta_k`, retaining every polynomial factor.
The added convolution identity is exact for the full finite measures:
multiplication of the `k` characteristic functions produces
`M_1^k (cosh xi)^(-k/2)=M_k (cosh xi)^(-k/2)`.
The natural centres sum to `k/2=c`; translating the sum of `k` copies
of the fixed original line by `k(1/2-c)` produces that same centre.
These additions were read directly in the final bytes.

IGO5 is exactly the squared modulus of the complete original polynomial.
Its degree is `2q` and its leading coefficient one. The second-index
permutation proves evenness. Oddness of `k` and `delta>0` exclude real-line
zeros, so every factor is strictly positive. No coefficient other than the
proved odd zero coefficients is removed.

## Exterior measure and differential formulas

IGO6–IGO8 preserve the Heine factor `1/r!`, the full product masses, and
the phase `i^(r(r-1)/2)` of the original complex Vandermonde. The exterior
vector has exactly the stated squared modulus. Expansion of its two
determinants cancels the factor `1/r!` with the permutation multiplicity.
The Laplace moment determinant follows from the same expansion in the
real coordinate. All factors have the required exponential integrability.
Its positive definiteness follows from the strictly positive weighted
measure and the nonvanishing of a nonzero polynomial on an interval.

IGO9–IGO11 agree with the independent general derivation. Both triangular
Wronskian changes retain their determinant factors. The resulting exponent
is exactly `B=br+r(r-1)`. The top coefficient is the product of the leading
coefficients of `Q_j` and the Vandermonde of their degrees. It is strictly
positive, proving the exact degree `2qr`; the determinant parity is even.
Positivity on the real `z` line follows from the positive Gram determinant
and the full bijection `z=tan t`.

IGO12–IGO14 correctly apply the same formula with the literal relation
factor one. The source order is `2B=sr+2r(r-1)` and its original-source mass
coefficient includes `(2pi)^(-B)`. The distinct original and natural
centres are related by the proved affine map. The rank-zero measure is
separately the unit Dirac, so no density `rho_0` is used. The final
notation definition `dm_(0,a)=(2pi)^(a/2) rho_(a/2) dY` correctly
defines every produced target order without changing the two permitted
input source orders.

## Signed components and positive polynomial density

IGO15–IGO18 have the correct binomial signs and component orders. The
Gaussian convolution argument proves Fourier uniqueness for the finite
signed measures. All component-dependent centre translations are stated
explicitly. The top coefficient `a_(qr)=d_(qr)>0` forces the claimed
largest order, including both evaluated endpoint expressions. No
positivity of the individual signed coefficients is asserted.

IGO19–IGO21 have the exact Gamma ratio: `2^(2h)` cancels the product's
`4^(-h)` completely. The full density multiplier relative to original
source `dm_(0,2B)` is `M_s^r R(Y^2)/(2pi)^B`. The polynomial degree and
leading coefficient follow from the nonzero highest signed constituent.
The coordinate multipliers on the two complex lines use the correct
minus signs, since `Y^2=-(U-B)^2=-(T-rc)^2`.

IGO22–IGO23 establish positivity everywhere, not only equality of
measures. The coordinate Jacobian of `(u,Y) -> (u,Y-sum u)` is one.
On compact sets of `Y`, every polynomial factor is bounded by a fixed
polynomial in `u`; dropping the last coordinate's exponential decay
leaves the integrable bound `exp(-theta sum |u_j|)`. This proves finite
continuous fibre densities by dominated convergence. The displayed
distinct tuple with prescribed sum has nonzero Vandermonde and positive
remaining factors, and hence a neighbourhood of positive integrand.
Equality almost everywhere of the two continuous densities then gives
pointwise equality and positivity. The mass identities agree with the
characteristic function at zero and retain the entire relation Gram
determinant.

## Sum maps, adjoints, and exterior kernels

IGO24–IGO26 define the sum pullback as an isometry for the full pushforward
measure. Fibrewise Cauchy–Schwarz proves that the specified adjoint is
well defined on every `L^2` equivalence class and has norm at most one.
The adjoint identity has the correct conjugation convention for inner
products linear in the second variable. The Euclidean surface Jacobian
is `sqrt(r)`, and division by `|grad Sigma_r|=sqrt(r)` produces the stated
surface factor `r^(-1/2)`. The left inverse, closed range, orthogonal
projection, complete fibre-mean kernel, and Pythagorean identity follow
exactly. The rank-one and rank-zero cases are separately specified.

The symmetric kernel example is valid: the quadratic `A=sum y_i^2` has
finite second moment, and its conditional mean is square integrable by
the already proved contraction. On each sum fibre with `r>=2`, this
quadratic is nonconstant on a positively weighted open set. Its positive
conditional variance proves the displayed kernel vector is nonzero.

IGO27–IGO28 use the full complex exterior vector. Multiplication by that
vector maps symmetric functions to antisymmetric functions and preserves
the exact norm. Conversely, division is defined almost everywhere because
the original polynomial has no zero on the line and the diagonal has
zero product-source measure. The quotient is symmetric and its norm is
the required weighted norm. This proves surjectivity and unitarity onto
the complete antisymmetric subspace. The exterior adjoint contains
`conjugate(psi) v`, as required; substituting
`w=|psi|^2 product_i[M_s rho_b(y_i)]` into the sum adjoint proves the
formula and the precise kernel. Multiplication of the already constructed
nonzero symmetric fibre kernel produces a nonzero exterior kernel for
`r>=2`. The final source explicitly restricts the exterior density
formulas to `r>=1` and supplies the empty determinant and unit exterior
map for `r=0` separately.

Finally, the multiplication intertwiners follow pointwise, while the
displayed norm integral identifies exactly the transported domain of the
unbounded sum coordinate. The original centre `rc` and factor `i` give
the asserted intertwiner for the original complex sum. These conclusions
retain the lost fibre directions explicitly; no sum injectivity or
unproved recovery of those directions is assumed.

## Verification scope

The entire final source, including every displayed formula and its proof,
was read. The supplemental exact symbolic checks in
`verify_intrinsic_formulas.py` and `INTRINSIC_FORMULA_CHECKS.json` pass;
the general proofs, rather than those finite checks, support this receipt.
No conclusion about RH, mixed-boundary cancellation, or asymptotic control
beyond the source's actual statements is asserted by this review.
