# Handoff: exact gamma convolution for the arithmetic control

Base inspected: main `fa4be32f87a9a90f3c02a07f7790dea95a1e7b0f`.
Parallel work inspected: PR #22, head `811210d24b80813a08972ca23f919db015383137`.
Do not duplicate its trace/Gram/projection/filtration modules. Its inspected PR
still reported strict verification in progress; this handoff is not a new certificate.

## Source-derived input

The main-branch `theta_gamma_reference.tex` already proves the one-factor gamma
measure, literal mass, monic polynomial norms and arithmetic multiplier
(TG.2--TG.14). The delivered Toda note proves the canonical quotient determinant
and its exact finite control formula. This contribution extends those specific
objects; it does not claim the general Meixner--Pollaczek convolution theory as new.

## Bounded algebraic targets

1. **Addition and exact projection coefficient.** From the specified generating
   function or recurrence and orthogonality, prove
   `b_n^(k lambda)(sum t_i) = sum_(sum n_i=n) n!/(product n_i!) product b_n_i^lambda(t_i)`.
   The conditional projection of one product is
   `(product (2lambda)_(n_i))/(2k lambda)_n * b_n^(k lambda)`.
   Its normal squared norm is NOTE (16), with the literal reference mass to power k.
   This is a projection plus retained complement, not an algebra isomorphism.

2. **Finite arithmetic coefficient transform.** Write
   `c_j=int b_j w_h /(c_lambda j! (2lambda)_j)` and the formal series
   `A(z)=sum (2lambda)_j c_j z^j`. Then the sum-density multiplier coefficient is
   `[z^n]A(z)^k/(2k lambda)_n`. Each coefficient is a finite identity.
   Degree-N source and relation Grams use only c_0 through c_(2N).
   Do not infer pointwise positivity of a truncated expansion. Its finite moments
   agree exactly at the declared degree; the full density remains the positive one.

3. **Reference determinant.** With alpha=2k lambda and literal mass c_lambda^k,
   `D_n^Gamma(theta)=c_lambda^(kn) product_(j<n) j!(alpha)_j * cos(theta)^(-n(alpha+n-1))`.
   Differentiate using the source's original Toda identity. Retain both endpoint
   values n=0 and n=1 and all factors. The reference parameter does not change the
   original scaling centre S=k/2+iu.

4. **Same-quotient comparison.** For the original boundary-column map B and
   arithmetic source Gram M, the gamma representative changes by
   `R=Rgamma-B(B* M B)^(-1)B* M Rgamma`. Construct its quotient equation and
   boundary primitive using the existing quotient and section-change interfaces.
   Handle an empty boundary block without an inverse of a zero-size operator.

5. **Quotient-dimensional determinant bound.** A source inequality M<=C^k Mgamma
   implies G<=C^k Ggamma by evaluating on the reference least-norm representative.
   Hence detG/detGgamma<=C^(kq), where q is the actual quotient dimension.
   This one-sided bound does not bound the consecutive ratio T_(N-1)/T_(N+1).

6. **Exact recurrence factor.** For X_n=D_n/Dgamma_n and
   Y_n=B_n/Bgamma_n, retain T_N=X_(N+1)/Y_(N-q+1).
   Then `a_(N+1)=(N+1)(N+2k lambda) X_(N+2)X_N/X_(N+1)^2` at theta=0,
   and the source Toda volume ratio is the reference ratio times
   T_(N-1)/T_(N+1). This is an equality on the original canonical control.

## Analytic interfaces

The gamma convolution uses its actual Fourier transform and uniqueness of finite
measures. The arithmetic multiplier is |(2xi/h)/Gamma(lambda+it/2)|^2.
For a full quartet, lambda=1/4 and the explicit compact/tail constant in NOTE (21)
bounds it. For h=1 an alternate lambda=13/4 gives C=1024/sqrt(pi); the analytic
source is nonzero but its finite arithmetic quotient is zero.

The all-degree moment-tail bound is NOTE (36). It requires the stated multiplier
bound and the explicit gamma Laplace transform, not an assumed weight theorem.
The compact integral in the nonempty-packet bound still requires an actual
validated enclosure when numerical certification is wanted.

## Support and scope

All source quotients use the original relation map. Linear Hilbert projection
maps lift at their supplied labels; the normal component mapping to a supported
zero is retained through the complementary map. Gram and squared-modulus
observations have quadratic, not semiring-homomorphism, types. No new scalar
zero is adjoined at a tensor or conormal level. The original Taylor unit and
cochain theta primitives stay in the maps to arithmetic cohomology.

17 exact regression methods pass normally and under python -O. Both false controls
fail. The preceding Toda archive's 35 manifest records and its 24-method suite
were independently checked; both inherited normal and optimized runs completed.
The seed coefficients are numerical, not interval-certified. No new Lean run or
uniform RH-level upper estimate is asserted.
