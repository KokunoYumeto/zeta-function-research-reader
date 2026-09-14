# Independent intrinsic exterior Gamma formula review

Reviewer: `/root/intrinsic_gamma_completion/intrinsic_formula_review`.
Scope: the Wronskian degree, signed Gamma decomposition, density scale,
original mass, and centre translations supplied by the parent. This receipt
reviews these formulas; it does not purport to review a final source file that
had not yet been written when the review began.

Assume `b > 0`, `M > 0`, integer `r >= 1`, and an even monic real polynomial
`W(y)` of degree `n = 2q`. Put `phi(t) = M (cos t)^(-b)`,
`g(t) = W(d/dt) phi(t)`, and `z = tan t`. All Laplace transforms below are
on the real interval `|t| < pi/2`; polynomial factors preserve convergence.

## 1. Exact Wronskian and top coefficient — accepted

The recurrence

`P_0 = 1`,
`P_(d+1) = b z P_d + (1+z^2) P_d'`

gives `phi^(d) = phi P_d(z)` by the chain rule. Therefore
`Q_0 = sum_d w_d P_d` and
`Q_(j+1) = b z Q_j + (1+z^2) Q_j'` give `g^(j) = phi Q_j`.

Let `H = det[g^(i+j)]_(0<=i,j<r)`. It is the Wronskian, with derivative
orders in rows, of `g,g',...,g^(r-1)`. Factoring a common function `phi`
out of all Wronskian columns gives `phi^r`: by the Leibniz rule the matrix
of derivatives of products is a lower triangular matrix, whose diagonal
entries are `phi`, times the matrix of derivatives of the `Q_j`.
Changing the independent variable from `t` to `z` gives the triangular
row matrix with diagonal entries `(dz/dt)^i`. Consequently

`H(t) = M^r (cos t)^(-B) D(tan t)`,
`B = br + r(r-1)`,
`D = Wr_z(Q_0,...,Q_(r-1))`.

Here `deg P_d = d` and its leading coefficient is the rising factorial
`(b)_d`, by induction. Thus

`deg Q_j = n+j`,
`lc(Q_j) = (b)_n (b+n)_j`.

For polynomials of distinct degrees `d_j`, the leading coefficient of
their Wronskian is the product of their leading coefficients times
`det[(d_j)_(falling i)] = product_(i<j)(d_j-d_i)`. This determinant
identity follows because the falling factorials are monic polynomials of
degrees `i`, so their evaluation determinant is the Vandermonde
determinant. Taking `d_j=n+j` proves

`deg D = nr = 2qr`,
`lc(D) = ((b)_(2q))^r product_(0<=j<r) j! (b+2q)_j > 0`.

Evenness is exact: `P_d` has parity `d`, `Q_0` is even, and `Q_j` has
parity `j`. Every determinant summand in `D` has total parity
`sum j - sum i = 0`. Write `D(z)=sum_(j=0)^(qr) d_j z^(2j)`.

If `W` is nonnegative and the source has positive density, the moment
matrix defining `H(t)` is positive definite: for any nonzero coefficient
vector its quadratic form is the integral of a nonzero polynomial's
squared modulus against the positive weighted source. This proves
`D(z)>0` on the real line. The original relation polynomial is strictly
positive there when its roots avoid `c+i R`.

## 2. Exact signed Gamma decomposition — accepted

At the imaginary argument `t=iu`, use
`cos(iu)=cosh u` and `tan(iu)=i tanh u`. For each `j`,

`(i tanh u)^(2j) = (-1)^j (1-sech^2 u)^j`.

Expanding this finite polynomial gives

`a_h = sum_(j=h)^(qr) (-1)^(j+h) binom(j,h) d_j`,
`H(iu) = M^r sum_(h=0)^(qr) a_h (sech u)^(B+2h)`.

The probability density with characteristic function `(sech u)^v` is

`rho_v(Y) = 2^v |Gamma(v/2+iY/2)|^2 / (4 pi Gamma(v))`.

The normalization is checked directly from the Fourier integral of the
Gamma product after the substitution `Y=2x`; the factor from `dY=2dx`
is essential. Uniqueness of Fourier transforms of finite signed measures
therefore gives the finite measure identity

`d nu(Y) = M^r sum_h a_h rho_(B+2h)(Y) dY`.

With original Gamma-source mass `M_s=(2pi)^(s/2)`, each summand has
source order `s_h=2B+4h` and coefficient

`M^r a_h / (2pi)^(B+2h)`

against that original source. Its coefficient is allowed to be signed.
The mass of the full measure is exactly

`nu(R) = H(0) = M^r D(0) = M^r sum_h a_h`.

Thus the finite signed mixture preserves the full mass of the exterior
relation measure. It does not claim that the component coefficients are
positive.

## 3. Exact polynomial density — accepted; no extra power of two

For integer `h >= 0`, the Gamma recurrence gives

`rho_(B+2h)(Y)/rho_B(Y)`
` = 2^(2h) Gamma(B)/Gamma(B+2h)`
`   times product_(j=0)^(h-1) [(B/2+j)^2 + Y^2/4]`
` = Gamma(B)/Gamma(B+2h)`
`   times product_(j=0)^(h-1) [Y^2 + (B+2j)^2]`.

The `4^h` from the density normalization cancels precisely the `4^(-h)`
from the product. There is no remaining power of two. Hence

`d nu(Y) = M^r rho_B(Y) R(Y^2) dY`,
`R(X) = sum_(h=0)^(qr) a_h Gamma(B)/Gamma(B+2h)`
`       times product_(j=0)^(h-1) [X+(B+2j)^2]`.

Since `a_(qr)=d_(qr)>0`, this polynomial has exact degree `qr` and
leading coefficient `d_(qr) Gamma(B)/Gamma(B+2qr)>0`.
Against the original source of order `2B`, the complete density multiplier
is `M^r R(Y^2)/(2pi)^B`. Omitting `(2pi)^(-B)` would change its mass.

If `W` is strictly positive on the real line, this density is positive
for every `Y`. For `r=1` this is immediate. For `r>=2`, express its
sum pushforward density as the integral in `y_1,...,y_(r-1)` with
`y_r=Y-sum_(j<r)y_j`. The coordinate Jacobian in this expression is one.
The positive source and relation factors are multiplied by the squared
Vandermonde. Distinct real tuples with prescribed sum exist, and an open
neighbourhood of any such tuple has strictly positive integrand, proving
the assertion. Consequently `R(Y^2)>0` for every real `Y`.

## 4. Original centres and rank-zero endpoint

The sum of the original coordinates `S_j=c+i y_j` is `S_sum=rc+iY`.
The natural coordinate for Gamma source order `2B+4h` is
`U_h=(B+2h)+iY`, so the required exact affine map is

`U_h = S_sum + (B+2h-rc)`.

These maps differ with `h`. The signed mixture formula on the common
real coordinate `Y` does not identify the different natural centres.

All density formulas above require `r>=1`. At `r=0`, the exterior
measure is the unit mass on the empty tuple and its sum pushforward is
the unit Dirac measure at zero; it must be supplied separately. In
particular, inserting `B=0` into `rho_B` is invalid.

Review conclusion: all formulas requested by the parent are accepted,
with the explicit centre translations and the separate rank-zero
endpoint retained. No order has been chosen to match an external scale;
the base order `2B=sr+2r(r-1)` and the full component orders are produced
by the stated exterior operation and the original relation polynomial.
