# Independent derivation of the native spectral transfer

20 September 2026. Scope: the complete mathematical argument in `../NATIVE_GAUSSIAN_TRANSFER.tex`, NG1–26, with particular attention to the finite characteristic comparison and the original full-root energy limit. This checks the mathematical maps and estimates. It does not assert a remote publication or certify unrelated programme claims.

## Finite characteristic comparison: NG4–9

The constants in NG6 are correct. Let `d_j=f(j+1)-f(j)`. The Vandermonde integral has exponent `sum_{i!=j} log|x_i-x_j|`, so the determinant convention gives `d_0=log|p_n(-a)|` with no extra factor two. Convexity yields

\[
\frac{d_{-2}+d_{-1}}2\le d_0\le\frac{d_0+d_1}2.
\]

For the positive shift the common subspace of `P_<n` and `(x+a)P_<n` is `(x+a)P_<n-1`. Their complementary vectors can be chosen as `1` and `(x+a)x^(n-1)`. Both changes of basis have determinant of absolute value one: their ordered degrees are `0,1,...,n-1` and `1,...,n` with monic leading coefficients. The common Gram determinant cancels. Each of the two attained one-dimensional metrics changes by a factor in `[ell,u]`; their ratio changes by a factor in `[ell/u,u/ell]`. Thus the logarithmic cost is precisely `Lambda=log(u/ell)`, with no factor `n` and no factor two.

For the negative shift the common subspace is `P_<n-1`. Their full sum consists of `F/(x+a)`, `deg F<=n`. Jensen for the convex function `z -> (a+z)^(-2)` gives

\[
(a+B_\zeta)^{-2}\|F\|_\zeta^2
\le\|F/(x+a)\|_\zeta^2\le a^{-2}\|F\|_\zeta^2.
\]

The resulting full rational-space comparison has lower constant `ell a^2/(a+B_lambda)^2` and upper constant `u(a+B_eta)^2/a^2`. Its logarithmic width is exactly NG5. It passes to both affine minima and proves NG9.

The reference Christoffel direction in the source is also correct. At the largest old zero, `p_(n+1)=-b_n p_(n-1)<0`, while the new monic polynomial is positive at large positive x. At consecutive old roots the signs alternate. Consequently `x_1<x'_1<...<x_n<x'_n`. Telescoping the increasing function `log(a+x)` over these interlaced roots bounds a successive slope gap by `log(1+B_eta/a)`. The lower averaged slope can be three half-gaps below `d_0`, whereas the upper averaged slope is only one half-gap above it. Combining with the two metric comparisons yields exactly NG6.

The common zero bound used here is justified for every displayed shifted measure. A decreasing reweighting lowers the x-mean, by its signed covariance. The positive shift of order one has mean at most the shift of order two; the latter is the original mean tested on the actual degree-n polynomial `(x+a)F`. Thus the stated degree-n hypothesis is sufficient.

## Original source density and full-root free energy: NG12–14

The pushforward under `x=y^2/q^2` has density

\[
q x^{-1/2}Q_k(q\sqrt x)^2\sigma(q\sqrt x)\,dx.
\]

Both signs of y are present. The source factors `B_q=2q exp(sqrt x) sigma(q sqrt x)` and `d omega=(1/2)x^(-1/2)exp(-sqrt x)dx` therefore multiply to exactly this density, with original mass intact.

The full root factor is `q^(2q) exp(q log x+O(k))` on any fixed positive compact interval. For determinant size n the constant contributes `2qn log q`. Since `n/q -> s/2`, the exponent divided by n gives the original potential

\[
V_s(x)=\frac\pi s\sqrt x-\frac2s\log x.
\]

The global upper estimate must instead use `(sqrt x+r_k)^(2q)`. Replacing `r_k` by a fixed epsilon gives the one-body potential `pi sqrt x/s-(4/s)log(sqrt x+epsilon)-t log(a+x)`. These coefficients, including the factor four before the regularized logarithm, are correct.

For fixed positive epsilon, the coefficient errors caused by `q/n -> 2/s`, by the Gamma upper factor, and by replacing `n^2` by `n(n-1)` are bounded by `o(1)(1+sqrt x)`. A fixed small subtraction `eta(1+sqrt x)` from the regularized potential absorbs them everywhere. The source measure `omega` is a probability, so integrating an upper bound on the entire exponent introduces no volume factor.

The compactification argument works on `[0,infinity]`. For fixed epsilon and eta small enough, the logarithmic kernel tends uniformly to minus infinity if either coordinate tends to infinity. It also tends to minus infinity on the finite diagonal. Its truncation from below is consequently continuous on the compact square, including the point at infinity. If `L_n` is an empirical probability, the removed n diagonal terms contribute at most `T/n` after division by `n^2`.

The assertion about decreasing maxima has the following exact justification. For decreasing continuous truncations `K_T`, choose maximizing measures `mu_T` in the compact space of probabilities. On a weakly convergent subsequence, every fixed truncation bounds the limiting maximal values by its integral against the weak limit. Let that fixed truncation decrease to the original kernel. The reverse bound follows by testing every fixed measure. The same argument applies to the monotone limits eta to zero and epsilon to zero. Measures charging zero or infinity have limiting energy minus infinity; a finite interior competitor excludes them. Thus these compact-space maxima are exactly the stated supremum over `(0,infinity)` at the final step. No endpoint region has been omitted.

The lower bound uses the *actual* equilibrium density on its fixed positive support. The logarithmic source error from the complete roots and Gamma factor is `O_h(k+log q)` per variable. For an arbitrary sequence `n/q -> s/2`, there is in addition an `o(n)` per-variable error from replacing `q/n` by its limit; this should be stated explicitly. For `n=floor(sq/2)` this additional error is only `O(1)`. Either version is `o(n^2)` after integration because `k/q -> 0`. Relative entropy against omega is finite, since the equilibrium density is bounded on a positive compact interval and vanishes as a square root at both edges. The pair logarithm is integrable there. Jensen therefore proves the lower bound in NG14 with the displayed constants.

## Convex slopes determine the zero law: NG15–20

The two directions of NG14 are sufficient. For any fixed epsilon>0 and n epsilon>=1,

\[
\frac{f_k(0)-f_k(-n\epsilon)}{n^2\epsilon}
\le\frac{f_k(1)-f_k(0)}n
\le\frac{f_k(n\epsilon)-f_k(0)}{n^2\epsilon}.
\]

The upper free-energy estimates at both signs, together with the lower estimate at zero, bound the lower and upper limits by the corresponding left and right secants of F. Their common limit exists: bounded energy controls `sqrt x+|log x|`; this supplies tightness, while `log(a+x)/sqrt x -> 0` supplies uniform integrability of the test function. Any limiting maximizer at t=0 is the unique EIQ minimizer. The two variational tests then prove differentiability at zero and identify its derivative with the equilibrium logarithmic moment. There is no differentiation of an asymptotic remainder here.

The zero measures have a common compact support because NG3 applies to the complete polynomials `Q_k(y)F(y^2/q^2)`. Consequently the logarithmic values at all a>=1 determine every moment by the convergent expansion at large a. Equality of polynomial moments then determines the measure on that compact interval. This proves the claimed reference law. NG6 changes these logarithmic values by only `O_h(k+log q)=o(q)`, so it transfers the law to the arithmetic relation measure. The same finite comparison transfers the source Jacobi law from the Gamma recurrence.

The relation block has dimension `d~sq`, and its divided counting measure is `s|y|rho_s(y^2)dy`. The full source block has density `h_0(y/(1+s))dy` of mass `1+s`. The off-diagonal block has rank at most one because only the last relation basis vector can leave the relation space on multiplication by y. Removing the two off-diagonal blocks is therefore a Hermitian rank-at-most-two change. Bounded-variation traces differ by at most `2 Var(f)/q`. Subtracting the relation contribution leaves exactly the probability in NG20. Formula NG19 also checks: `Q_k U_d-p_(N+1)` lies in the attained complement and its squared norm is `nu_d-omega_(N+1)` by orthogonality.

The argument works for every sequence `d/q -> s`, not only `d=floor(sq)`. State this explicitly when applying it to `N=2q`, where `d=q+1`. The `s=0` endpoint with d=0 or 1 follows directly from a finite-rank difference.

## Original observation metric and the four signs: NG21–26

The sign in NG21 is correct. Removing the degree-(N+1) source projection from `y L_N v` subtracts `p_(N+1) ell_N(v)` before taking its remainder. The result is the compressed multiplication, so `C_N=M-r_N ell_N`. Conjugating by the actual minimum section identifies its metric with G_N; no Euclidean change of metric is made.

Compression to the original attained observation complement loses `r_obs` dimensions. Its trace error against `g_t(y)=y^2 exp(-t y^2)` is bounded by `4r_obs/(exp(1)tq)`. The difference of the squared singular operator and the square of the selfadjoint compression has image in `span{Cu,v}` for a rank-one perturbation `uv*`, hence rank at most two. The total variation of `x exp(-t x)` on `[0,infinity)` is `2/(exp(1)t)`. This contributes `4/(exp(1)tq)`, proving NG23 exactly.

The denominator must be written `exp(1)t` or with upright Euler e: NG1 already uses italic e for the root multiplicity. Using the same symbol without distinction gives a false literal constant when m0>1.

For the independently proved five-orbit observation domain, `m0=1` and `|u|>=R_*`, the rank defect is `8k-16=o(q)`. The two low endpoints have s=0 and the two high endpoints have s=1. With unchanged signs `+,+,-,-`, NG26 therefore equals `2[-H'_0(t)+H'_1(t)]`. This is a proved observation statement only on that actual rank domain. The full compression law does not require a period restriction. The size-one orbit cannot be assigned this small-kernel estimate.

## Required finite-domain corrections

1. In NG1 state `k>=5`, `k=1 mod4`. CAI16–25 require k>=3, and the displayed NG24 rank formula fails at k=1. This does not change any limit.
2. Include the additional `o(n)` potential-coefficient error in the NG14 lower bound for arbitrary `n/q -> s/2`.
3. State the convergence for sequences `d/q -> s` to include `N=2q` directly.
4. Distinguish Euler `exp(1)` from the multiplicity e in NG23 and its preceding variation constants.

With these explicit repairs, I find the decisive NG6, NG12–15, NG20 and NG26 arguments mathematically sound. The direct positivity proof GM17 and the certified signed bound GM25 are available in `GAUSSIAN_EQUILIBRIUM_MOMENTS.tex`; their transfer through NG26 keeps the stated five-orbit domain.
