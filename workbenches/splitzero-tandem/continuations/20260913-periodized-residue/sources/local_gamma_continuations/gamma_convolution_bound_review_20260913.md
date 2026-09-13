# Independent arithmetic multiplier and tail review — 13 September 2026

The reviewed source is `Tau_Gamma_Convolution_Descent/NOTE.tex`, read directly and completely from the delivered ZIP. Its exact source is 34,859 bytes with SHA256 `7cf984d87de405b815250b44454c4ee27c8ab46574da245b377ebc6e49327fa2`. This review independently verifies the analytic multiplier and gamma shift in equations (17)–(23), the gamma determinants and metric comparison in (28)–(35), and the moment tail in (36). The source was not edited or extracted by this reviewer. The other sections were read for definitions and dependencies; this report does not claim a separate execution of the package checker or a numerical interval certification.

All displayed bounds in this scope pass. The quotient index domain must be carried into the integrated presentation: (31)–(33) concern `N >= q−1`; (34)–(35), which contain `V_(N−1)`, concern `N >= q`. The existing first-full-quotient endpoint at `N=q−1` remains separate. Equation (36) is an untilted moment bound. Section 8 below proves its explicitly tilted counterpart, including both shifted cosine factors, when a tilted Gram is intended. Neither clarification changes equation (36).

## 1. The arithmetic amplitude and the values at selected zeros

Write

\[
s=\tfrac12+it,\qquad
g(s)=s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),\qquad
h(s)=\prod_\rho(s-\rho)^{m_\rho},\qquad d=\deg h.
\]

Every selected multiplicity is the actual full order of its selected zero, as stipulated in the source. Since `g` is entire, `v_h=g/h` is entire. More explicitly, at a selected zero `rho` of order `m_rho`, write

\[
g(s)=(s-\rho)^{m_\rho}u_\rho(s),\quad u_\rho(\rho)\ne0,
\qquad h(s)=(s-\rho)^{m_\rho}\widetilde h_\rho(s),
\quad \widetilde h_\rho(\rho)\ne0.
\]

The extension has the actual value `v_h(rho)=u_rho(rho)/tilde h_rho(rho)`, which is nonzero. This constructs the value rather than leaving a quotient of two zeros. The function

\[
A_{h,\lambda}(t)=v_h(\tfrac12+it)\,\Gamma(\lambda+it/2)^{-1}
\]

is entire as a function of complex `t`, because reciprocal gamma is entire. For real `t` and `lambda>0`, the denominator is finite and nonzero. The amplitude is not identically zero. Its real zeros therefore form a discrete, hence countable, set. In particular, each real compact interval has a finite maximum of its squared modulus.

With `r_lambda(t)=|Gamma(lambda+it/2)|^2/(2pi)`, direct multiplication proves the exact pointwise identity

\[
|A_{h,\lambda}(t)|^2r_\lambda(t)
=\frac{|v_h(\tfrac12+it)|^2}{2\pi}=w_h(t).
\]

At `lambda=1/4`, `s(s−1)=−(t^2+1/4)` and
`pi^(−s/2)=pi^(−1/4) exp(−it log(pi)/2)`. Cancellation of the same finite gamma factor gives exactly the minus sign, phase and real factor of source (20):

\[
A_{h,1/4}(t)
=-\pi^{-1/4}(t^2+\tfrac14)e^{-it\log\pi/2}
\frac{\zeta(\tfrac12+it)}{h(\tfrac12+it)}.
\]

At a selected zero this formula is read through the extension just constructed. No pole is present there.

## 2. The zeta estimate and the exact constant 25

The elementary continuation identity can be proved without a growth conjecture. For `Re(s)>1`, absolute convergence permits

\[
\zeta(s)=s\int_1^\infty\lfloor x\rfloor x^{-s-1}\,dx
=\frac{s}{s-1}-s\int_1^\infty\{x\}x^{-s-1}\,dx.
\]

The last integral and all its complex derivatives converge locally uniformly for `Re(s)>0`: on a closed subregion `Re(s)>=eta>0`, its derivative integrands are bounded by a constant times `x^(−eta−1)(1+log(x))^j`. It therefore continues the equality to `Re(s)>0`, away from the displayed pole at `s=1`. This is also the Riemann specialization of the standard Euler–Maclaurin integral recorded in [DLMF 25.11.5](https://dlmf.nist.gov/25.11#E5); the derivation here supplies the specialization and all constants.

On `s=1/2+it`, `|s/(s−1)|=1` and the integral of `x^(−3/2)` from 1 to infinity is 2. Consequently, with `R=(t^2+1/4)^(1/2)`,

\[
|\zeta(\tfrac12+it)|\le1+2R
\le2(1+|t|),\qquad
|\zeta(\tfrac12+it)|\le4R.
\]

The first second-step inequality uses `R<=|t|+1/2`; the last inequality uses `R>=1/2`. Both hold at `t=0` as well.

For a nonempty packet define exactly the source radius

\[
T_h=\max\{1,2\max_\rho|\rho-\tfrac12|\}.
\]

For every real `|t|>=T_h`, the reverse triangle inequality, applied once for each multiplicity, gives

\[
|\tfrac12+it-\rho|
\ge |t|-|\rho-\tfrac12|\ge |t|/2,
\qquad |h(\tfrac12+it)|\ge(|t|/2)^d.
\]

Since `|t|>=1`, the bounds needed for the numerator are

\[
(t^2+\tfrac14)^2\le\frac{25}{16}|t|^4,
\qquad |\zeta(\tfrac12+it)|^2\le16|t|^2.
\]

Their product is `25 |t|^6`, not `16 |t|^6` or `25 |t|^6/16`. Division by the squared lower bound for `h` proves

\[
B_{h,1/4}(t)\le
\frac{25\,2^{2d}}{\sqrt\pi}|t|^{6-2d}.
\]

For `d>=3` the exponent is nonpositive. The compact maximum and this tail bound therefore give exactly the source constant

\[
C_h=\max\left\{
\sup_{|t|\le T_h}|A_{h,1/4}(t)|^2,
\frac{25\,2^{2d}}{\sqrt\pi}T_h^{6-2d}
\right\}.
\]

It is finite and strictly positive, and bounds the multiplier on the entire real line. For `d=3` the tail exponent is zero; the argument requires no decay of that quotient beyond boundedness. A full off-line nonreal quartet with common complete multiplicity `m` has four distinct members and `d=4m>=4`, so it is covered with the original `lambda=1/4`. The conclusion does not require placing any packet root on the integration line.

The compact supremum is a mathematically specified constant, not an executed certified enclosure. A later interval calculation for a particular packet must enclose the analytic extension on that compact set. This distinction does not affect the proved global inequality with the stated supremum.

## 3. Every gamma shift, and the empty seed bound

The gamma recurrence gives for each integer `L>=0`

\[
\Gamma(\tfrac14+L+it/2)
=\Gamma(\tfrac14+it/2)
\prod_{j=0}^{L-1}(j+\tfrac14+it/2).
\]

Each factor is nonzero for real `t`; for `L=0` the product is one. Hence the source amplitude equality (22) is exact and preserves its complex phase. For `|t|>=T_h>=1`, the squared modulus of the product is at least `(|t|/2)^(2L)`. The direct shifted tail bound is

\[
B_{h,1/4+L}(t)
\le\frac{25\,2^{2(d+L)}}{\sqrt\pi}
|t|^{6-2d-2L}.
\]

Thus an entirely explicit form of the compact/tail constant used by the note is

\[
C_{h,L}=\max\left\{
\sup_{|t|\le T_h}|A_{h,1/4+L}(t)|^2,
\frac{25\,2^{2(d+L)}}{\sqrt\pi}T_h^{6-2d-2L}
\right\},\qquad L\ge\max(0,3-d).
\]

This includes packet degrees one and two without changing `w_h`. For the empty packet `h=1`, the same tail calculation can use `d=0,T_1=1`; no maximum over an empty zero set is needed. The source supplies a stronger completely numerical constant for this case.

For `h=1,L=3`, compute the squared shift product without changing scale:

\[
\prod_{j=0}^2|j+\tfrac14+it/2|^2
=4^{-3}(t^2+\tfrac14)(t^2+\tfrac{25}4)(t^2+\tfrac{81}4).
\]

The exact multiplier is consequently

\[
B_{1,13/4}(t)
=\frac{64}{\sqrt\pi}
\frac{(t^2+\tfrac14)|\zeta(\tfrac12+it)|^2}
{(t^2+\tfrac{25}4)(t^2+\tfrac{81}4)}.
\]

Using the all-real `|zeta|^2<=16(t^2+1/4)` from section 2 gives

\[
B_{1,13/4}(t)
\le\frac{1024}{\sqrt\pi}
\frac{(t^2+\tfrac14)^2}
{(t^2+\tfrac{25}4)(t^2+\tfrac{81}4)}
\le\frac{1024}{\sqrt\pi}.
\]

Both factors in the denominator of the fraction are at least `t^2+1/4`, so the last inequality is valid for every real `t`, including zero. This confirms every power of 2 in (23). It is an estimate on the nonzero analytic seed; its finite spectral quotient remains the zero module.

## 4. Domination and strict positivity on each sum fibre

Fix one of the bounded references above, write `B=B_(h,lambda)` and `C=C_h>0`, and retain the actual gamma density and its convolution

\[
r_{\lambda,k}(u)
=\frac{c_\lambda^k}{c_{k\lambda}}r_{k\lambda}(u),
\quad c_\lambda=2^{1-2\lambda}\Gamma(2\lambda).
\]

For positive integer `k`, this density is finite and strictly positive at every real `u`. For `k>=2`, use the original fibre coordinates `t_1,...,t_(k−1)` with `t_k=u−sum_(i<k)t_i`. Substitution of `w_h=B r_lambda` in the convolution integral gives

\[
m_{h,k}(u)=\int_{\mathbb R^{k-1}}
\prod_{i=1}^k B(t_i)r_\lambda(t_i)\,d^{k-1}t.
\]

All factors are nonnegative, and the integrand is bounded by `C^k prod_i r_lambda(t_i)`. Thus the integral is finite for every `u` and

\[
0\le m_{h,k}(u)\le C^k r_{\lambda,k}(u),\qquad
B_{h,\lambda;k}(u)=m_{h,k}(u)/r_{\lambda,k}(u)\le C^k.
\]

For strict positivity, let `Z` be the discrete set of real zeros of `B`. In this fibre chart the set where some `B(t_i)=0` is a countable union of affine hyperplanes: `t_i=z` for `i<k`, or `sum_(i<k)t_i=u−z`, with `z in Z`. Each has Lebesgue measure zero; this remains true for `k=2`, where these hyperplanes are points in the one-dimensional fibre. Outside the union every factor, including each gamma density, is strictly positive. Its integral over the fibre is therefore strictly positive. This proves the source's pointwise assertion for every `u`, using the actual convolution representative, rather than merely almost everywhere as an abstract conditional expectation class.

For `k=1`, the same domination holds, and the actual isolated zeros of `B` remain. The pointwise convolution formula then has no relative fibre. The scalar equality `w_h=B r_lambda` connects the different admissible references to the same arithmetic measure, including all original masses.

## 5. Gamma source and relation determinants

Let `alpha_k=2k lambda` and keep `u=sum t_i`, not its average. The original gamma mass generating function is

\[
Z_{\lambda,k}^\Gamma(\theta)
=c_\lambda^k(\cos\theta)^{-\alpha_k},\qquad
\theta\in\mathbb R,\quad |\theta|<\pi/2.
\]

Its differentiated moments are finite on this domain. For every integer `n>=0`, set

\[
H_n(\theta)=c_\lambda^{kn}
\prod_{j=0}^{n-1}j!(\alpha_k)_j
(\cos\theta)^{-n(\alpha_k+n-1)},\qquad H_0=1.
\]

At `n=1` this is exactly `Z`. For `n>=1`, explicit differentiation gives

\[
\partial_\theta^2\log H_n
=n(\alpha_k+n-1)\sec^2\theta.
\]

The constant part of `H_(n+1)H_(n−1)/H_n^2` is
`n!(alpha_k)_n/((n−1)!(alpha_k)_(n−1))=n(alpha_k+n−1)`; the cosine exponent in that ratio is `−2`. The factors `c_lambda` cancel with exponent `k((n+1)+(n−1)−2n)=0`. Therefore

\[
H_{n+1}H_{n-1}/H_n^2
=n(\alpha_k+n-1)\sec^2\theta.
\]

The source's Hankel–Toda determinant identity, starting with determinants 1 and `Z`, consequently proves by induction that its actual gamma Hankel determinant is `H_n`. The division is valid because the gamma weight is positive on the whole real line: the integral of the squared modulus of a nonzero polynomial against its tilted weight is positive, so every finite moment Gram is positive definite. This also proves the required determinant positivity directly.

Taking consecutive determinant ratios now yields, with no omitted source mass,

\[
\omega_n^\Gamma(\theta)
=c_\lambda^k n!(\alpha_k)_n
(\cos\theta)^{-(\alpha_k+2n)},\quad n\ge0,
\]

\[
a_n^\Gamma(\theta)
=n(n+\alpha_k-1)\sec^2\theta,\quad n\ge1.
\]

For the relation determinant, write `chi(S)=sum_j chi_j S^j` and let `bar chi` mean conjugation of its coefficients. For real `u`,

\[
\overline{\chi(k/2+iu)}\chi(k/2+iu)
=\overline\chi(k/2-iu)\chi(k/2+iu).
\]

Differentiation under the tilted integral therefore identifies source (30) with the moment Gram for the weight
`|chi(k/2+iu)|^2 exp(theta u) r_(lambda,k)(u) du`. Its `n` relation columns are the images of the `n` independent degree-`<n` polynomial columns under multiplication by the same nonzero polynomial `chi`. They remain independent. The weight is positive except at finitely many real points; its Gram is positive definite. This proves that all nonempty denominators used for `Y_n` and `V_N^Gamma` are positive. Empty determinant indices mean one.

## 6. Exact lift map, Loewner comparison, and determinant exponent

Take a nonzero monic annihilator `chi` of degree `q>0`, and an integer `N>=q−1`. The original vector-space sequence is

\[
0\longrightarrow\mathcal P_{N-q}
\xrightarrow{M_\chi}\mathcal P_N
\xrightarrow{\pi}\mathbb C[S]/(\chi)\longrightarrow0.
\]

Here `P_j` is zero for `j<0`; the source has dimension `N+1`, the relation space has dimension `m=N−q+1`, and the quotient has dimension `q`. Let `B_chi` be the `(N+1)-by-m` relation matrix in the original bases. The arithmetic source Gram `M_h` is positive definite since `w_h^*k` is positive almost everywhere, and the tilted version remains positive definite for any fixed real admitted tilt. Multiplication by `chi` is injective, so `B_chi^* M_h B_chi` is invertible whenever `m>0`.

The gamma least-norm lift `R_N^Gamma` has type `C^q -> C^(N+1)` and satisfies `pi R_N^Gamma=I`. Define

\[
R=R_N^\Gamma-B_\chi(B_\chi^*M_hB_\chi)^{-1}
B_\chi^*M_hR_N^\Gamma.
\]

The correction lies in the original relation subspace, so `pi R=I`; multiplication by `B_chi^*M_h` gives zero exactly. Every other lift of a vector `u` is uniquely `Ru+B_chi v`. Its squared arithmetic norm is

\[
\|Ru+B_\chi v\|_{M_h}^2
=\|Ru\|_{M_h}^2+\|B_\chi v\|_{M_h}^2,
\]

because the displayed orthogonality makes both cross terms zero. Thus `R` is exactly the arithmetic least-norm lift, proving (32), its type and its uniqueness. At `N=q−1`, `m=0` and the correction is the zero map. The representative is then the unique degree-`<q` representative, although its gamma and arithmetic norms remain different.

For every source polynomial and every fixed admitted real tilt, pointwise domination from section 4 gives

\[
\|P\|_h^2\le C^k\|P\|_\Gamma^2.
\]

Apply this to `P=R_N^Gamma u`. The arithmetic minimum is no larger than the arithmetic norm of that representative. Hence for all quotient vectors `u`,

\[
u^*G_Nu\le C^k u^*G_N^\Gamma u,
\quad\hbox{and consequently}\quad G_N\preceq C^k G_N^\Gamma.
\]

Conjugation by the positive square root `(G_N^Gamma)^(−1/2)` produces a positive definite `q`-by-`q` Hermitian matrix with every eigenvalue at most `C^k`. Its determinant is `det G_N/det G_N^Gamma`; multiplying these `q` positive eigenvalues proves

\[
0<\frac{\det G_N}{\det G_N^\Gamma}\le C^{kq}.
\]

The source's determinant-line identity uses the same original polynomial and quotient bases on both sides. It gives

\[
\frac{\det G_N}{\det G_N^\Gamma}
=\frac{\mathfrak D_{N+1}/\mathfrak D_{N+1}^\Gamma}
{\mathfrak B_{N-q+1}/\mathfrak B_{N-q+1}^\Gamma}
=X_{N+1}/Y_{N-q+1}=T_N.
\]

This proves the exponent `kq` in (33). It does not arise by dividing an upper bound for `X` by an upper bound for `Y`; that operation would give no such ratio bound. Applying source domination on an arbitrary `n`-dimensional polynomial subspace or its `n`-dimensional relation image separately proves `0<X_n<=C^(kn)` and `0<Y_n<=C^(kn)`, including `X_0=Y_0=1`.

For the empty spectral quotient, `q=0` and `chi=1`. The source and relation spaces coincide; `B_n=D_n`, `B_n^Gamma=D_n^Gamma`, `X_n=Y_n`, and `V_N=V_N^Gamma=T_N=1`. The quotient Gram is the zero-dimensional Gram, whose determinant is one. Its unique lift has zero-dimensional domain. Thus the determinant inequality is the equality `1<=C^0=1`; no positive-dimensional inverse or nonzero spectral packet is introduced.

## 7. Exact substitution into the upper control

At `theta=0` and `N>=q`, all three quotient degrees `N−1,N,N+1` are in the complete-quotient domain. The arithmetic recurrence coefficient is

\[
a_{N+1}=\frac{\mathfrak D_{N+2}\mathfrak D_N}{\mathfrak D_{N+1}^2}.
\]

Inserting `D_j=X_j D_j^Gamma` and the gamma recurrence from section 5 proves

\[
a_{N+1}=(N+1)(N+\alpha_k)
\frac{X_{N+2}X_N}{X_{N+1}^2}.
\]

Similarly, division of `V_j=V_j^Gamma T_j` at `j=N−1,N+1` proves exactly

\[
\frac{V_{N-1}}{V_{N+1}}
=\frac{V_{N-1}^\Gamma}{V_{N+1}^\Gamma}
\frac{T_{N-1}}{T_{N+1}}.
\]

Substitution of these two equalities into the inherited Toda estimate yields source (35) with all factors unchanged. The larger polynomial source at degree `N+1` admits every representative from degree `N−1`, so the arithmetic quotient Gram decreases in the Loewner order. Its determinant is therefore nonincreasing, and the actual ratio `V_(N−1)/V_(N+1)` is at least one. This proves the nonnegative numerator in (35) directly on the original metric. It imposes no independent monotonicity on `T_N`.

The first-full-quotient endpoint `N=q−1` has no `q`-dimensional quotient at degree `N−1=q−2`. Formula (35) is therefore used only for `N>=q`; the earlier endpoint formula is retained as stated in the Toda work. The one-sided pointwise and determinant bounds above do not supply a lower bound on `T_(N+1)` and do not establish an asymptotic estimate on the consecutive correction ratio. No such estimate has been certified here.

## 8. All-degree moment tail, including the tilted form

Let `k>=1`, `r` be any integer `>=0`, `T>=0`, and `a,b>0` with `a+b<pi/2`. The exponential series with nonnegative terms proves for every `x>=0`

\[
x^r\le r!a^{-r}e^{ax}.
\]

On `x>T`, multiplication by `1<=e^(b(x−T))` gives

\[
\mathbf1_{x>T}x^r\le r!a^{-r}e^{-bT}e^{(a+b)x}.
\]

The `r=0` case uses `0!=1` and is included. Apply this inequality with `x=|u|`, then use `m_(h,k)<=C^k r_(lambda,k)` to obtain

\[
\int_{|u|>T}|u|^r m_{h,k}(u)\,du
\le C^k r!a^{-r}e^{-bT}
\int_{\mathbb R}e^{(a+b)|u|}r_{\lambda,k}(u)\,du.
\]

For any real `u`, `exp(c|u|)<=exp(cu)+exp(−cu)` with `c=a+b`. Both moment generating functions have their original gamma mass. Their sum is exactly
`2 c_lambda^k (cos(a+b))^(−2k lambda)`. Therefore

\[
\int_{|u|>T}|u|^r m_{h,k}(u)\,du
\le 2 C^k c_\lambda^k r!a^{-r}e^{-bT}
(\cos(a+b))^{-2k\lambda}.
\]

This proves every constant and every domain in source (36), including `T=0` and `k=1`. For a finite polynomial `P(u)=sum_j p_j u^j`, absolute values and the triangle inequality yield the tail bound obtained by summing `|p_j|` times this expression at `r=j`. A relation entry contains the finite polynomial `|chi(k/2+iu)|^2` times its original source monomials; its degree and coefficients are retained in that finite sum.

For completeness, a fixed real tilt is handled without treating an exponential as a polynomial. If `|theta|+a+b<pi/2`, the same proof multiplies the integrand by `exp(theta u)`. With `c=a+b`,

\[
e^{\theta u+c|u|}\le e^{(\theta+c)u}+e^{(\theta-c)u}.
\]

Integration gives the proved tilted tail

\[
\begin{aligned}
\int_{|u|>T}|u|^r e^{\theta u}m_{h,k}(u)\,du
\le{}&C^k c_\lambda^k r!a^{-r}e^{-bT}\\
&\cdot\left[(\cos(\theta+a+b))^{-2k\lambda}
+(\cos(\theta-a-b))^{-2k\lambda}\right].
\end{aligned}
\]

At `theta=0` the bracket is exactly the factor `2(cos(a+b))^(−2k lambda)` in (36). Summation against the actual polynomial coefficients gives a tail enclosure for each tilted source or relation Gram entry. The source's compact interval quadrature is a separate computation: these formulas bound the omitted tails and do not certify a floating-point compact calculation or its rounding error. The specific empty-seed constant `1024/sqrt(pi)` is available without any zero-location input; a nonempty packet additionally requires an enclosure of its specified compact supremum when a numerical certificate is requested.

## Disposition

The arithmetic multiplier constants, gamma shifts, positivity and domination, gamma determinant formulas, exact least-norm representative map, quotient Loewner bound with exponent `kq`, and all-degree tail pass this independent proof review. The report supplies the missing explicit shifted compact/tail formula and a complete fixed-tilt version of the tail. The integrated text should retain the quotient index domains and the distinction between a specified compact supremum and a numerically enclosed one. There is no analytic or asymptotic RH certificate in this review, and no such certificate is inferred from the package's finite checker.
