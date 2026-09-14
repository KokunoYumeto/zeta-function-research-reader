# Independent review of MFG1–25

**Verdict: PASS.** The complete proof and the two final prose deltas have been independently checked. The moving-denominator clarification identified in this review is installed and correct. There are no remaining mathematical issues in this review scope.

The result concerns an **exploratory Gamma comparison family** with independent order `K=4L+1`. The choice `L=q/4`, `K=q+1` is an admissible member of that family. This review does not identify it with the canonical order of the original packet or assert that the original tensor, exterior, or spectral-sum operation produces this order. The opening scope paragraph now states this explicitly. Transfer to the displaced packet and application to its original arithmetic/cohomology receiver remain outside MFG1–25.

## Sources actually inspected

The complete initial MFG source was read, with SHA256 `5203d192c86a5cfcd2e88b014b0ab7e69705adf36028c0ff84f4c3e2fa6383d7`. The final moving-`L=0` argument and exploratory-family paragraph were then read as deltas. The accepted final source is:

- `ACTUAL_MACROSCOPIC_GAMMA_RETURN.tex`: **`667e2bcb50821fdff31acbf659768ba89a64b89834194a790ff7a5980c5e4b22`**.
- `../equilibrium/MACROSCOPIC_MARKED_EQUILIBRIUM.tex`, KME1–25: `8ce2d8a2587fffdf3bff1fbddb68c7ad140cb1a1dddbbbfa2daf36762f44108c`.
- `../equilibrium/endpoint_existence.tex`, KEP1–20: `94a36d5eacafd7944a9dd2bdbafe1fbbd226ca139431d2651a9989d3a52504d0`.
- `../../equilibrium/GAMMA_ENSEMBLE_LEADING_RETURN.tex`, GEL1–19: `2014e7fefdcd963b70b00fb89d597e24c0826582a2541dd1ff44d63051979fc1`.

The equilibrium and endpoint providers were inspected for their exact objects, parameter maps, energy convention, support, entropy, and derivative statements. Their earlier accepted proof cuts were not recursively reopened. This is a proof review, not a claim of a new Lean run, numerical certificate, PDF build, or publication. The reviewer made no source edits.

## MFG1–6: original Gamma measure, full polynomial, and finite return

The packet identities imply that `q=e(k+1)^2` is divisible by four, so `L=q/4` is integral and gives exactly `K=q+1`. The coordinate remains `S=c+iy`, with `c=k/2`. Substitution in every factor of `f_L` gives

\[
|f_L(c+iy)|^2=\prod_{j=0}^{L-1}\bigl(y^2+(2j+1/2)^2\bigr).
\]

The full square pushforward is used in every `H_s^{(a;L)}`. Permuting both rows and columns into even and odd indices has squared permutation sign. The real matrices of sizes `q` and `q+1` give the four literal factors with `(s,a)=(n,q),(n+1,q),(n,q+1),(n,q+1)`. Thus MFG4 has both required copies of `H_n^{(q+1;L)}`.

The Gamma recurrence gives a factor `4` for each quadratic factor and hence

\[
\Phi_L(y)d\sigma(y)=4^L\frac{|\Gamma(L+1/4+iy/2)|^2}{2\pi}\,dy.
\]

Writing `alpha=L+1/4`, the autocorrelation and the literal change `y=2xi` give the mass multiplier `4^L 2^{1-2alpha}=sqrt(2)`. The tilted mass is therefore exactly `sqrt(2) Gamma(2alpha) (cos t)^(-2alpha)` on `|t|<pi/2`. Polynomial multiplication of the original Gamma density preserves the exponential integrability needed for differentiated integration on a smaller strip.

The generating function has monic coefficient polynomials. Integrating its two copies gives `sqrt(2) Gamma(2alpha)(1-zw)^(-2alpha)`. Comparison of the coefficients of `z^i w^j/(i!j!)` gives zero for unequal indices and the squared norm

\[
\sqrt2\,j!\,\Gamma(j+2L+1/2).
\]

Division by the `L=0` norm gives the stated product over `2L` consecutive half-integer shifts. The phase `i^j` has modulus one, and the monic change to the coordinate `S` has determinant one. The four source products cancel to precisely the negative ranges `a=q,...,2q-1` and `a=q+1,...,2q`. The low ratio retains the entire `Phi_L`. Consequently the finite signed expression MFG6 has the stated signs `P - log r + log(Z_L/Z_0)`.

## MFG7–13: discrete marked field and equilibrium interface

Under the literal substitution `t=q^2 x`, each factor contributes `q^2`; the residual product is exactly MFG7. Differentiating the proposed antiderivative in its upper limit verifies MFG8 and its zero initial value. Each sample `(j+1/4)/q` belongs to its original cell. Monotonicity places both the sampled sum and `q` times the integral between the same left and right sums. Their difference is bounded by their telescoping endpoint difference, giving MFG9 globally on `x>0` with its exact constant.

The field is `pi sqrt(x)-2 log(x)-2h_lambda(x)`. Differentiation gives `partial_x h=arctan(2lambda/sqrt(x))/(2sqrt(x))`; the complementary-angle identity gives both forms of MFG11. Thus the full polynomial correction is retained at positive limiting `lambda`.

MFG12 uses a single bounded-above kernel integral on all probability measures, avoiding subtraction of divergent integrals. Its field and sign convention agree exactly with KME1–3. MFG13 is KME5–6 under the explicit map `kappa=2lambda`, including the `1/(2pi x)` factor, both endpoint equations, and the lower Stieltjes endpoint. KME15 supplies the global variational inequality, KME16–17 the required positive compact support and finite absolute entropy. KEP20 identifies the zero endpoint with `uK=2`, `vE=4`.

## MFG14–18: exact ensemble and complete limiting argument

The density identity is exact: multiplying `B_q=2q exp(sqrt(x)) sigma(qsqrt(x))` by `domega=(1/2)x^(-1/2)exp(-sqrt(x))dx` gives the full square-pushforward density after `t=q^2x`. The reference measure has mass one. Expansion of both Vandermonde determinants gives `1/s!`; the three scale exponents are `2as`, `2s(s-1)`, and `2Ls`, exactly as in MFG14.

MFG16–17 agree with GEL4–5, including all constants and the original exponential `exp(-pi|y|/2)`. The polynomial factor in the global upper Gamma bound is absorbed using

\[
(1+4q^2x)^{1/4}\le(1+2q)^{1/2}e^{\sqrt x/2}.
\]

This yields the exponent `-(pi q/2-3/2)sqrt(x)` and the stated `C_q`.

For positive limiting `lambda`, the endpoint error in MFG9 divided by `q` is bounded by `O(1/q)R(x)`, with `R=1+sqrt(x)+|log x|`. The upper-limit derivative of `h` is bounded by `C+2sqrt(x)` when the upper limit remains in a fixed positive neighborhood of `lambda`. These two estimates prove MFG18 globally. The same field comparison at `L=0` follows directly by `phi=1`, `h=0` and does not require that positive-neighborhood argument.

The upper exponent has the exact form `sum_{i != j} K_{Q_s}` for `Q_s=sV_s/(s-1)`. The inequalities `Q_s >= V_lambda-epsilon R` hold eventually for each fixed sufficiently small positive `epsilon`. For the perturbed field, `r_epsilon=log(1+x)-Q_epsilon/2` tends uniformly to negative infinity at zero and infinity. At zero the coefficient remains positive because `epsilon<1`; at infinity `pi-epsilon>0`. The bound `K <= r_epsilon(x)+r_epsilon(y)` establishes continuous truncations at every compactified endpoint and every diagonal point.

For an empirical measure, removing the diagonal of the truncated kernel contributes exactly `sM`. Maximizing the continuous truncated energy over probabilities on the compact interval is legitimate. Its decreasing maximum converges to the untruncated supremum: weak subsequences of maximizers are controlled at every fixed truncation; monotone convergence applied after subtraction from a common upper bound gives the limiting inequality. A finite-energy probability on a compact positive interval gives a common finite lower bound, so the limiting measure cannot charge either added endpoint. This proves both directions of the equality of the limiting truncated supremum and `F(Q_epsilon)`.

The final perturbation limit is also valid. Uniform coercivity puts every pair with a coordinate outside a common compact interval at the truncated value `-M`. On the remaining compact square, `R` is bounded, so truncated kernels converge uniformly as `epsilon` decreases to zero. Hence the order of limits in the proof gives the claimed upper bound without assuming an unproved continuity theorem for minimizers of perturbed fields.

For the lower bound, the actual equilibrium density has finite logarithmic energy and finite absolute entropy relative to `omega`. Jensen after restriction and change of measure gives exactly `s(s-1)` times the pair logarithm, `as` times the logarithmic moment, the two `s`-weighted source terms, and the negative entropy term. All are integrable. Compact-uniform convergence and `q/s -> 2`, `a/s -> 2` give the value of the stated equilibrium functional. The signs and all multiplicities in this lower bound are correct. Together the two arguments prove MFG15.

## MFG19: moving denominators and all four high factors

The review identified that the originally cited GEL10 theorem was stated for fixed `a/s`, whereas three denominator blocks have moving exponents. The installed paragraph resolves this explicitly, using the proof already supplied: at `L=0`, set `phi_{q,0}=1` and `h_0=0`. Then `|V_s-V_0| <= o(1)R` follows immediately from the two parameter limits; the same compactified-kernel proof gives the upper bound, and Jensen against `rho_0` gives the lower bound. Thus each moving denominator has limit `F_0`, with no differentiation of an asymptotic error.

The numerator and denominator scale powers subtract exactly. Their residual new power is `2L(4n+1)=2L(2q+1)`. The sum of the four squared sizes is `4n^2+2n+1`, which divided by `q^2` tends to one. Adding the four asymptotics proves MFG19 with remainder `o(q^2)`.

## MFG20–22: source product and finite low-factor constants

`A''(v)=log v`, so the two integrations over the original rectangle give the displayed closed form for `Q(lambda)`. There are `4Lq` source factors. The first outer range uses left endpoints in the `s` direction, the second uses right endpoints, and both use the original midpoint `(j+1/2)/q` in the `t` direction. Both derivatives of `log(s+t)` are bounded by one. The per-cell error is at most `3/(2q)` after multiplication by `q^2`; two arrays of `2Lq` cells give the exact total bound `6L` in MFG21.

The full-source constants `C_L` and `C_U` retain the original Gamma mass. The ratio after `y=qz` is `q^(2L) A/B`; the two half-axis factors and two Jacobians cancel in this ratio. Restriction to `1<=z<=2` gives both lower bounds `C_L exp(-2pi q)`. Since every `(2j+1/2)/q <= 1/2`, the original residual polynomial is bounded above by `(1+z)^(2L)` on the entire positive axis.

With `D=2q+2L<=5q/2`, integration against `exp(-qz)` gives

\[
A\le\frac{C_U2^D}{q}\left(1+\frac{D!}{q^D}\right)
\le\frac{2C_U}{q}5^{5q/2},\qquad
B\le\frac{C_U}{q}4^q.
\]

Here `D/q>=2` justifies absorbing the `1` into the doubled power. Dividing the corresponding lower and upper bounds gives both endpoints of MFG22 with exactly their displayed logarithms of constants, signs of `log q`, and coefficients of `q`. The remaining low logarithm is `O(q)` uniformly over the stated range.

## MFG23–25: cancellation, exact comparison, and derivative interface

The scale contributions cancel with their integer coefficients:

\[
-4Lq\log q+2L(2q+1)\log q-2L\log q=0.
\]

The finite source error is `O(L)=O(q)` and the residual low error is `O(q)`. Continuity of the explicit `Q` then gives MFG23 for every positive limiting `lambda<=1/4`. This is a `q^2`-scale limit; it supplies no unproved `o(q)` remainder.

The identity MFG24 is exact on `y != 0`, with its stated domain. Under `y=q sqrt(x)`, division of the correction logarithm by `q` gives `h_lambda(x)-lambda log x`. Its contribution to the field is therefore exactly `-2[h_lambda(x)-lambda log x]`. This verifies the precise relation to the auxiliary power-weight calculation without discarding the polynomial marks.

KME24 supplies `F'_lambda=2 integral log(x+4lambda^2) rho_lambda(x) dx`, including the right derivative at zero and its continuity. Differentiation of the actual source rectangle gives `Q'=4 integral_1^2 log(s+2lambda) ds`. Their difference integrates to MFG25, since both `F_lambda-F_0` and `Q(lambda)` vanish at zero. KEP20 and GEL12 identify the zero logarithmic moment with `mathcal L`, so the derivative is exactly `2 mathcal L-4(2log2-1)=mathcal C_Gamma`. The imported strict sign is the established GEL18a result; no numerical sign inference is used here.

## Final acceptance and scope

The moving-`L=0` delta is mathematically complete. The exploratory-family paragraph correctly preserves the original canonical `k` source and the independent status of `K`. No equation changed in that scope delta. All MFG1–25 claims pass for the accepted final source hash above.

The proved output is the exploratory homogeneous-relation coefficient `Psi(lambda)=F_lambda-F_0-Q(lambda)` for the full polynomial `f_L`, including the exact choice `L=q/4`, and its derivative bridge at zero. This acceptance does not certify an operation deriving that choice from the original programme, a displaced-packet transfer theorem, or any arithmetic/cohomology conclusion absent from the reviewed proof.
