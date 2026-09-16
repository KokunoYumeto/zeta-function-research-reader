# Uniform canonical-band review and a concentrated penalty certificate

16 September 2026. Additive continuation of PR37. The original two-band Jensen proof and its checker are unchanged.

## 0. Provenance, scope, and result

The user supplied `Pasted markdown(20260916-165456).md` (file ID `file_00000000bb7882308ddd473a49e00200`), the UCB full-band continuation. The entire supplied Markdown was read, including its small-rank patch, monic-norm comparison, rate derivative, finite guards, minimum localization, and penalty receiver. Its linked `UNIFORM_CANONICAL_BAND.tex`, PDF, and 40-payload ZIP were not available as inspected proof artifacts in this review. In particular, the exact separately defined `C_EIQ` and its author's 134+9 checks are not relabelled as independently replayed. Both local execution interfaces failed before running commands. External Wolfram evaluations did run, with scope recorded below.

The arithmetic inputs remain the existing original-source AMT bounds, the paired-root full-form comparator on the stated degree band, and the exact untilted radius identity. The equilibrium input remains the supplied EIQ measure for `V_{a,b}(x)=b sqrt(x)-a log(x)`, with support `[u^2,v^2]`, bounded density on compact positive parameter rectangles, and `D=V-2P-lambda >= 0`, with equality on the support. No entire cumulative source audit is claimed.

Relative to those stated inputs, the new note's headline conclusions follow:

\[
 \log\min_{q-1\le N\le2q-1}\epsilon_N
   =q a_1+O_h(k+\log q),\qquad
 \log(\mathcal P_-+\mathcal P_+)=-2q a_1+O_h(k+\log q).
\]

Here `q=[1+k(m-1)](k+1)^2` and

\[
 a_1=\log\frac{(u_*+v_*)\sqrt{v_*^2-u_*^2}}{16},\quad
 u_*K(\kappa_*)=2,\quad v_*E(\kappa_*)=4.
\]

The validated sharp constant is larger than PR37's independent coarse lower exponent: `a_1 = 0.06651895202027...`, whereas `log(50000/45927)/2 = 0.04248491300504...`. The UCB proof uses stronger equilibrium/root-comparison inputs and an eventual domain; PR37's explicit two-band finite bound remains a separate fallback, not a false result to delete.

This continuation supplies an independent quantile argument for the needed uniform single-norm error, a tighter finite sum of the actual penalties, and a relative tail certificate. The penalty mass is concentrated in a final `O_h(k+log q+log(1/eta))` strip at any prescribed relative tolerance `eta`. This does not say the final row alone dominates, identify the exact minimizer, or supply an RH upper allowance.

## 1. Original quotient and adjacent factors

Keep the original arithmetic source, complete unit, multiplicities, quotient map, source mass, and polynomial coordinate. With the UCB notation,

\[
 \nu_r=\min_{\deg P=r,\ P\text{ monic}}\|\chi P\|_{\rm ar}^2,
 \quad T_r=\nu_r/\omega_{q+r},\quad
 d_{q+r}=T_r^{-1},\quad
 \beta_n=\omega_n/\omega_{n-1}.
\]

The exact identity is

\[
 \epsilon_{q+r-1}^2
 =\beta_{q+r}(T_r-1)
 \begin{cases}1&r=0,\\1-T_{r-1}^{-1}&r\ge1.\end{cases}
\]

At `r=0`, the earlier observation is the isomorphism `J_{q-1}`. There is no inverse at `q-2`. Total parity, not separate vanishing of the kernel/boundary pairings, is used. The original component identity `z_B=-z_K` remains compatible with a nonzero mixed pairing.

## 2. Small relation rank: the new patch is valid

For `Y=4q/pi` and `0<eta<1`, the exact monic Legendre minimum on an interval of length `H` is

\[
 \int_I |P|^2\,dy\ge
 \frac{H^{2r+1}}{(2r+1){2r\choose r}^2}.
\]

It holds for every complex monic polynomial: the shifted Legendre minimizer is monic, orthogonal to all lower degrees, and the residual contributes a nonnegative squared norm. The original Gamma lower density on `[Y(1-eta),Y(1+eta)]` therefore gives UCB(2). The minimum of `2q log y-(pi/2)y` is at the lower endpoint; the retained cost is `2q[-log(1-eta)-eta]`.

For `eta=1/10` and `0<=r<=q/100`, the rational margin is exactly

\[
 \frac37-\frac1{90}-\frac3{50}-\frac1{5000}-\frac13
 =\frac{7537}{315000}>0.
\]

Using `binom(2r,r)<=4^r` and the stated factorial upper bound gives the supplied conservative prefactor `c_0 q^{-3/2}`, with `c_0=c_Gamma/(60 e sqrt(6 pi))`. Thus

\[
 \log(\nu_r^0/\gamma_{q+r})\ge
 q/3-(3/2)\log q+\log c_0.
\]

The exponent exceeds `2a_1`. This genuinely covers `r=0`, `r=1`, and all small positive `r/q`; it does not import a fixed-positive-ratio equilibrium estimate into a degenerating parameter range.

## 3. Independent proof of the uniform bulk monic-norm estimate

This proves the order and mechanism needed by UCB(5), without pretending to have read the linked detailed formula for its particular `C_EIQ`.

Fix a positive compact parameter rectangle and its supplied EIQ equilibrium probability `mu`, supported on `[A,B]`. Put `W=B-A`, `cap=W/4`, and let its density be bounded by `M`. The density vanishes continuously at the endpoints in this one-cut family. Write `P_mu(x)=integral log|x-y| dmu(y)` and `D=V-2P_mu-lambda`. The original Gamma remainder is

\[
 \mathfrak r(y)=\sigma(y)e^{\pi y/2}\sqrt y/\sqrt2.
\]

It need not be bounded below at zero. What is required, and follows from the original Gamma envelopes, is `r(q sqrt x)>=r_->0` on the equilibrium support for `q>=1000`, and `r(y)<=r_+` for every positive `y`. If `u_min` is the minimum of the positive square-root support endpoint on the rectangle, safe choices are

\[
 r_-=(c_\Gamma/\sqrt2)
       \sqrt{\frac{1000u_{\min}}{1+1000u_{\min}}},\qquad
 r_+=C_\Gamma/\sqrt2.
\]

### Lower norm

Let `nu` be the arcsine probability on `[A,B]`. For every monic degree-`j` polynomial `p`,

\[
 \int\log|p|\,d\nu\ge j\log\operatorname{cap}.
\]

This follows rootwise from the circle Jensen formula, including complex roots and roots on the interval. Since the equilibrium measure is supported on the same interval, Fubini and the arcsine potential give

\[
 \int V\,d\nu=2\log\operatorname{cap}+\lambda.
\]

The arcsine entropy is `integral log(dnu/dx) dnu = -log(pi cap)`. Probability Jensen applied to `|p|^2 exp(-jV)/(dnu/dx)` proves

\[
 h_{j,q}(a,b)\ge r_-\pi\operatorname{cap}\,e^{-j\lambda}.
\]

### Upper norm and quantile uniformity

Take the `j` midpoint quantiles `x_i` of `mu` and `p_j(x)=product_i(x-x_i)`. Their empirical CDF differs from the equilibrium CDF by at most `1/j` (the sharper `1/(2j)` is unnecessary). For fixed `x`, clip the logarithm at `delta=1/j`:

\[
 f_{x,\delta}(y)=\log\max\{|x-y|,\delta\}.
\]

On `[A,B]` it has total variation at most `2 log(1+W/delta)`. Integration by parts against the CDF error yields

\[
 \sum_i f_{x,\delta}(x_i)
 \le j\int f_{x,\delta}\,d\mu+2\log(1+jW).
\]

Moreover,

\[
 \int(f_{x,\delta}-\log|x-y|)\,d\mu(y)
 \le M\int_{-\delta}^{\delta}\log(\delta/|s|)\,ds
 =2M\delta.
\]

Since each unclipped nodal logarithm is no larger than its clipped version,

\[
 |p_j(x)|^2e^{-jV(x)}
 \le e^{4M}(1+jW)^4e^{-j\lambda}e^{-jD(x)}.
\]

This holds on the entire positive half-line, not merely inside the support. As `j>=1` and `D>=0`, its integral is bounded by

\[
 h_{j,q}(a,b)\le r_+J_*e^{4M_*}(1+jW_+)^4e^{-j\lambda},
\]

where `J_*` uniformly bounds `integral exp(-D) dx`, `M_*` the density bound, and `W_+` the support length. All are finite on the positive compact rectangle. For an explicitly crude bound on `[1,250] x [1,400]`, let `B_max` bound the support's right endpoint and `Lambda_*` bound `|lambda|`; then

\[
 J_*\le e^{\Lambda_*}(1+B_{\max})^2[1+2\Gamma(506)].
\]

Indeed `P_mu(x)<=log(x+B_max)`, so the small interval is integrable and the large tail is bounded by `x^252 exp(-sqrt x)`. This covers the whole region near zero as well as infinity.

### The square substitution and a separate finite constant

For `r=2j+eps`, evenness of the reference measure makes the monic minimizer have that same parity. Substituting `y=q sqrt x` gives exactly

\[
 \nu_r^0=\sqrt2 q^{2(q+r)+1/2}
 h_{j,q}((q+\varepsilon-3/4)/j,\pi q/(2j)).
\]

The quarter shift and the two half-lines have not disappeared. For `q>=1000`, `q/100<r<=q`, both these parameters and `(2q/r,pi q/r)` belong to `[1,250] x [1,400]`.

Let `L_a,L_b` bound the absolute Robin derivatives on the rectangle. The parameter replacement costs at most

\[
 C_{\rm par}=(401/4)L_a+50\pi L_b+\Lambda_*/2
\]

in `j lambda`, because `j|a-2q/r|<=401/4`, `j|b-pi q/r|<=50pi`, and `|j-r/2|<=1/2`.

The preceding two norm bounds yield `|log h+j lambda|<=C_norm+4log(q+1)` for an explicit constant made from `r_-,r_+,J_*,M_*,W_+` and the minimum capacity. Stirling cancellation is exact up to its positive remainder:

\[
 \log(\nu_r^0/\gamma_{q+r})
 =2(q+r)(1-\log(1+r/q))+\log h
 -\tfrac12\log(1+r/q)-\log(2\pi)-R_{q+r},
 \quad0<R_n<1/(24n).
\]

Thus a independently specified safe bulk error is

\[
 \widehat E_0(q)=C_{\rm norm}+C_{\rm par}
 +\tfrac12\log2+\log(2\pi)+1/48+4\log(q+1).
\]

This is an alternative finite constant, not a silent assertion about the unseen UCB15--19 definition of `C_EIQ`. It proves the same uniform `O(log q)` conclusion from the supplied equilibrium inputs.

## 4. The profile derivative, positivity, and the sharp constant

Put `s=sqrt(1-kappa^2)` (not a source order) and use the actual endpoint relation

\[
 1+t=E(\kappa)/(sK(\kappa)).
\]

The displayed profile simplifies exactly to

\[
 \psi(t)=\log\frac{1+s}{E(\kappa)}
             +t\log\frac{\kappa}{E(\kappa)}.
\]

With `f=log(kappa/E)` and `g=log((1+s)/E)`, the classical derivative formulas give

\[
 f'(\kappa)=K/(\kappa E),\qquad
 g'(\kappa)+t f'(\kappa)=0.
\]

Therefore `dpsi/dt=f`, exactly as in UCB. The modulus increases with `t`: one has `sK<E<K`, and differentiation of `log(1+t)` with respect to `s` gives

\[
 \frac{d}{ds}\log(1+t)
 =\frac{(1+t)+(1+t)^{-1}-(s+s^{-1})}{1-s^2}<0.
\]

For completeness, `E>sK` follows by pairing theta with `pi/2-theta` in their defining integrals. If their radicands are `x,y`, then `xy>=s^2` and

\[
 \sqrt x+\sqrt y-s(1/\sqrt x+1/\sqrt y)
 =(\sqrt x+\sqrt y)(1-s/\sqrt{xy})\ge0,
\]

strictly on a set of positive measure. Also `E<K` is immediate. Since `E(kappa)>1>kappa` for `0<kappa<1`, `psi'<0`; since `f'(kappa)>0`, the profile is convex. On `0<t<=1`,

\[
 \psi(t)\ge a_1+c_1(1-t),\qquad
 c_1=\log(E(\kappa_*)/\kappa_*)>0.
\]

Its limiting values are `psi(0)=log(4/pi)` and `psi(infinity)=0`; the latter also follows from the expansion in Section 7. Hence it is positive at every finite positive argument.

An independent exact-rational computation encloses

\[
 0.06651895202027<a_1<0.06651895202028,
 \quad0.04748604398475<c_1<0.04748604398476.
\]

The bulk formula, small-rank patch and original AMT transfer then give the claimed minimum rate and `O_h(k+log q)` localization. They do not prove exact finite minimization at `r=q`. The transfer retains both adjacent factors through the global lower bound on all `T_r`, exactly as in UCB(8)--(11).

## 5. A sharper finite penalty bound

Use either UCB's certified finite bulk error or the alternative one above, consistently throughout. Set

\[
 r_0=\lfloor q/100\rfloor,\quad
 C_k=E_0(q)+B_k,\quad
 s_k=q/3-(3/2)\log q+\log c_0-B_k,
\]
\[
 m_k=\min\{s_k,2qa_1-C_k\},\quad
 z=e^{-2c_1}\in(0,1).
\]

Impose the original root-comparison domain, `q>=1000`, and `m_k>=log2`. For the bulk,

\[
 T_r^{-1}\le e^{C_k-2qa_1}z^{q-r}
 \quad(r_0<r\le q),
\]

while `T_r^{-1}<=e^{-s_k}` on the small-rank block.

The exact coefficients of the combined penalty, indexed by `r=0,...,q`, are

\[
 c_0^{\rm wt}=3,\quad c_r^{\rm wt}=4\ (1\le r\le q-2),
 \quad c_{q-1}^{\rm wt}=3,\quad c_q^{\rm wt}=1.
\]

Do not confuse `c_0^{wt}` with the small-rank constant `c_0`. The small block's total coefficient is `4r_0+3`. Since `-log(1-x)<=x/(1-e^{-m_k})` for `0<=x<=e^{-m_k}`, summing the actual coefficients gives

\[
\begin{split}
 \mathcal P_-+\mathcal P_+\le{}&
 (4r_0+3)\frac{e^{-s_k}}{1-e^{-s_k}}\\
 &+\frac{e^{C_k-2qa_1}}{1-e^{-m_k}}
 \left[1+3z+\frac{4z^2(1-z^{q-r_0-2})}{1-z}\right].
\end{split}
\tag{PT1}
\]

In particular the bracket is bounded by

\[
 C_{\rm geo}=\frac{(1+z)^2}{1-z},\qquad
 40.2398920641<C_{\rm geo}<40.2398920642.
\tag{PT2}
\]

This replaces a `4q-1` worst-row factor by a geometric-series constant in the bulk. The small-rank contribution has strictly faster exponential decay. Keep the intersection with UCB's original finite bound and PR37's weaker-input bound; no stronger finite bound is asserted outside its guards.

The lower bound `P_total>=T_q^{-1}>=exp(-2qa_1-C_k)` stays. Each individual penalty has the same logarithmic rate: `P_+` contains the final row; `P_-` contains `T_{q-1}^{-1}`, whose logarithm differs at the profile level by a bounded quantity. Thus both log penalties are `-2qa_1+O_h(k+log q)`; neither is identically zero.

## 6. Penalty concentration near the upper endpoint

Let `P_far(d)` retain the original combined-penalty terms with `q-r>=d`. For integers `2<=d<=q-r_0`, PT1 and the same geometric sum give

\[
 \frac{P_{\rm far}(d)}{P_{\rm total}}
 \le
 (4r_0+3)\frac{e^{2qa_1+C_k-s_k}}{1-e^{-s_k}}
 +\frac{4e^{2C_k}z^d}{(1-z)(1-e^{-m_k})}.
\tag{PT3}
\]

The first term tends to zero exponentially since `1/3>2a_1`. Given `0<eta<1`, once it is at most `eta/2`, it suffices to choose

\[
 d\ge\max\left\{2,
 \left\lceil\frac{2C_k+\log\bigl(8/[\eta(1-z)(1-e^{-m_k})]\bigr)}{2c_1}\right\rceil\right\},
\]

with the stated finite `d<=q-r_0` guard. Then the final `d` rows retain at least `1-eta` of the complete penalty. Since `C_k=O_h(k+log q)`, this strip has width `O_h(k+log q+log(1/eta))`, not `O(q)`.

This is an upper bound on the required strip, not a claim that the last term alone is asymptotically dominant. The arithmetic comparison still has `O_h(k)` uncertainty and does not control individual adjacent fluctuations finely enough for such a claim.

## 7. The next degree regime: a reference-profile fact, not an arithmetic extension

The same exact profile has a useful large-`t` description. Put `L=log(4/s)`, `s=kappa'`. The standard complete-elliptic expansions give

\[
 K=L+O(s^2L),\quad
 E=1+\tfrac12s^2(L-\tfrac12)+O(s^4L),
 \quad1+t=\frac{1+O(s^2L)}{sL}.
\]

The exact simplification

\[
 \psi(t)=\operatorname{arctanh}s+(1+t)\log(\kappa/E)
\]

then yields

\[
 \psi(t)=\frac{s}{2}-\frac{s}{4L}+O(s^3L),\qquad
 \psi(t)\sim\frac{1}{2t\log t},\qquad
 u_t=2/K\sim\frac2{\log t}.
\tag{PT4}
\]

These are statements about the explicit reference equilibrium function. They DO NOT extend UCB's arithmetic comparison to `t=t_k -> infinity`. The compact positive parameter rectangle used in its norm estimate degenerates in that limit. Furthermore, in the original `y=q sqrt(x)` coordinate the inner equilibrium scale is `q u_t ~ 2q/log t`. It approaches the actual packet radius `R_k` when `log t` is of order `q/R_k`. Exactly there, a homogeneous replacement of the actual root polynomial requires a new, root-sensitive estimate. Full `chi`, both half-lines, and the adjacent factors must remain; polynomial recurrence prefactors cannot be ignored either.

The actionable next analytic theorem is therefore uniform control in a growing-degree/root-sensitive regime, or a different proved same-class comparison. Improving an allocation that cancels from `J_action=B_ar+W_ar-P_total` cannot lower this particular certificate. This is a limitation of a specified canonical-band strategy, not a no-go theorem for RH or the full tau construction.

## 8. Execution and formal scope

Two remote Wolfram evaluations succeeded. The first returned an exactly zero symbolic derivative residual, the exact rational small-rank margin, nine exact shifted-Legendre norm identities (`r=0,...,8`), and separately labelled high-precision diagnostic constants. The second used rational/integer arithmetic to prove eight inequalities: two signs bracketing the unique elliptic endpoint ratio, both stated endpoints for `a_1`, both for `c_1`, and both for `C_geo`. It used 4096 elliptic-series terms, directed rounding at `10^80`, explicit geometric tails, alternating Machin arctangent bounds for pi, and 20-term positive logarithm series with remainders. Its algorithm is preserved in `verify_ucb_constants.wl`.

Those are fresh checks, not a replay of the supplied 134 algebraic checks or nine certificate checks. They concern universal constants and finite identities, not an actual hypothetical zero packet, its period, or its arithmetic Gram integrals. No new Lean execution, GitHub Actions success, PDF build, linked-archive verification, or full-library audit is asserted. The existing SplitZero support and boundary interfaces remain unchanged; a vanished coefficient observation does not become external absence, and neither an integration-band restriction nor an arcsine comparison replaces the arithmetic quotient.

## References

National Institute of Standards and Technology. (n.d.). *Digital Library of Mathematical Functions*, Sections 19.4 and 19.12. https://dlmf.nist.gov/19.4 ; https://dlmf.nist.gov/19.12 . Derivative identities and complete-elliptic expansions only; the monic-norm and penalty arguments above are displayed explicitly.

Incoming user source: `Pasted markdown(20260916-165456).md`, equations (1)--(16). Original arithmetic comparisons: AMT/TW and the paired-root comparator retained there. Repository baseline: `1efd53337561d8f67cf0ac1d119acdaa222644c3`; preceding standalone bound: PR37 implementation `6a34ac7d911a5be3a2b030008e955ff35f8e0dad`.
