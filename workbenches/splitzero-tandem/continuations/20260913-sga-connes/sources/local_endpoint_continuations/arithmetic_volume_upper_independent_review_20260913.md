# Independent review of the arithmetic central-volume upper estimate

Date: 13 September 2026. Scope: the complete new article `arithmetic_volume_upper_route_20260913.tex`, all of AU.1–33 and AU.40–49, including the inserted scalar argument; the complete independent scalar derivation `volume_comparator_review_20260913.md`; and the inherited arithmetic note at equations (26)–(37), especially its actual envelope (29) and original Laplace values (30)–(31). The broader arithmetic intake has its own independent review; this report checks the new composition and its new proofs rather than representing a second broad intake.

## 1. Finding and exact scope

The new finite matrix upper estimate, the scalar upper estimate, the explicit even-degree auxiliary determinant asymptotic with its finite error, and the monic family are mathematically valid. Every matrix inverse in the inequalities has the correct direction. The strongest low-degree-data estimate uses actual moments only through degree `2q`; its comparison measure uses explicit moments through degree `4q−2`. The scalar bound has leading order `q²` and does not give a contradiction with the central lower estimate of order `q log k`.

Two local type clarifications were reported to the author after the complete scalar argument was inserted. They are specified, with the exact maps repairing them, in item 14 below. Both are now incorporated and independently read in the final source. They do not change an inequality or a numerical constant. The final source seal at the end of this file records the checked bytes.

The independent fixture passes **112 exact rational/Gaussian-rational checks in normal Python and 112 in optimized Python**. It includes nonzero asymmetric moments, order-two raw derivative factorials, repeated nonreal roots, source and quotient chart congruences, every principal minor of the tested positive differences, and independent Cauchy and Legendre determinant calculations. These finite auxiliary calculations support the algebra audit; the written arguments below establish the general analytic estimates.

## 2. Original source and the unscaled chart: AU.1–2

The measure is the literal `k`-fold convolution of `w_h`, so Tonelli gives its mass `μ_h^k`. For `c=k/2`, substitution `ΨP(u)=P(c+iu)` and `Ψ⁻¹f(S)=f((S−c)/i)` gives inverse ring maps. The multiplication equation is `Ψ(SP)=(c+iu)ΨP`; differentiation gives `∂_u^d ΨP=i^d Ψ(P^(d))`. On degree `N`, the coefficient matrix has diagonal `i^j`, `0≤j≤N`, hence determinant of modulus one.

Write that matrix as `A_N`. With source Gram matrices explicitly labelled by chart, `H_N^S=A_N* H_N^u A_N`. If `J_N^S,J_N^u` are the respective monic remainder maps and `A_{q−1}` is the same chart on the quotient, then

\[
J_N^u A_N=A_{q-1}J_N^S,
\quad K_N^u=A_{q-1}K_N^S A_{q-1}^*,
\quad G_N^u=A_{q-1}^{-*}G_N^S A_{q-1}^{-1}.
\]

Thus the quotient determinants themselves agree for this unscaled chart. This proves the claimed equality of the volumes while retaining the multiplication observation and each derivative phase.

## 3. Cyclic degree, multiplicities, and the dagger relation: AU.3–4

For a tensor of `k` local rings of length `m`, let its nilpotent variables be `x_1,…,x_k`, with `x_i^m=0`. The largest total degree of a surviving monomial is `k(m−1)`. In the corresponding power of `x_1+⋯+x_k`, the coefficient of `x_1^(m−1)⋯x_k^(m−1)` is `(k(m−1))!/((m−1)!)^k`, which is a positive integer and therefore nonzero over `ℂ`. The next power vanishes. This proves local sum length `ℓ=1+k(m−1)`.

Every ordered sign pair may be chosen independently in each quartet factor, so every grid sum `(a,b)`, `0≤a,b≤k`, occurs. Its real and imaginary parts distinguish the grid positions because `δ,γ>0`. The direct product of the tensor-local factors therefore has exactly the cyclic annihilator and degree in AU.4. The transported roots `ζ_ab=(2b−k)γ−i(2a−k)δ` are conjugation-stable under `a↦k−a`, which proves that `ψ` is real monic.

The original roots are stable under `λ↦k−conj(λ)`. Comparing the roots and leading coefficients gives the coefficient identity `conj(χ)(k−S)=(-1)^qχ(S)`. On the real `u` line, `χ(c+iu)=i^qψ(u)` and `conj(χ)(c−iu)=(-i)^qψ(u)`. Their product is exactly `ψ(u)^2`. No parity assumption on `q` is required here.

## 4. Exact sequence and complete raw jets: AU.5–7

Monic division proves that the kernel of the remainder map is precisely the image of multiplication by `ψ`. The multiplication map is injective because `ℂ[u]` has no zero divisors. At `N=q−1`, its source is the zero vector space, and the remainder map is the identity in the chosen coordinates.

For each distinct centre, vanishing of the raw derivatives of orders `0,…,ℓ−1` is equivalent, by the polynomial Taylor formula, to divisibility by the corresponding factor of order `ℓ`. These coprime factors multiply, proving `ker E_N=ker J_N`. Applying the derivative map to the actual remainder proves the literal factorization `E_N=ZJ_N`. At degree below `q`, divisibility by a monic polynomial of degree `q` forces the polynomial to vanish, so the square matrix `Z` is invertible.

The confluent Vandermonde formula has the correct row-order sign and the factor `∏d!` for every cluster. Successive divided differences turn the ordinary Vandermonde rows into derivatives divided by their factorials, while removing the within-cluster Vandermonde factors. Multiplying back the derivative factorials yields AU.7. The independent fixture also checks multiplicity three, where `2!` is genuinely present rather than equal to one.

## 5. Least lifts and the central determinant orientation: AU.8–9

For `K=JH⁻¹J*`, surjectivity of `J` and positive definiteness of `H` imply `K>0`. For `G=K⁻¹` and `R=H⁻¹J*G`, direct multiplication gives `JR=I` and `B*HR=B*J*G=0`. Every lift is `Rx+By`, and expanding its quadratic form gives `x*Gx+y*B*HBy`. This proves the minimum property, without replacing the source norm.

The raw kernel is `E H⁻¹ E*=ZKZ*`, so its determinant is `|det Z|²/det G`. Taking the larger-source-degree determinant divided by the smaller-source-degree determinant gives

\[
\frac{\det\mathsf K_{2q-1}}{\det\mathsf K_q}
=\frac{V_q}{V_{2q-1}}.
\]

The order in AU.9 is therefore correct. In particular it is the larger raw kernel determinant that is in the numerator. The raw jet factors cancel at this ratio and remain present in the individual maps.

## 6. Actual lower envelope and its full positive moment integral: AU.10–12

The original note proves, for all real `u` and every `k≥3`,

\[
m_k(u)\ge c_h\vartheta_h^{k-3}
e^{-(\pi/2)(|u|+k-3)}(1+|u|+k-3)^{-B},
\qquad B=42+2\deg h=42+8m.
\]

Putting `a_k=c_h ϑ_h^(k−3)e^(−α(k−3))` and `d_k=k−2` gives exactly AU.11, because `1+|u|+k−3=d_k+|u|`. In particular `d_k≥1`, so there is no singularity at the origin. Pointwise domination gives a well-defined contraction between the two weighted `L²` spaces: equality of representatives in the larger-measure space also implies equality in the smaller-measure space. Polynomial multiplication, remainder and raw derivatives are the unchanged algebraic maps on the polynomial subspaces.

For `y>0`, integration by parts proves `∫₀∞t^(B−1)e^(−yt)dt=(B−1)!/y^B`. Substitute `y=d_k+u`, use Tonelli on the positive half-line, and evaluate `∫₀∞u^j e^(−(α+t)u)du=j!/(α+t)^(j+1)`. This yields AU.12 for even `j`. Odd moments vanish by symmetry, and are absolutely integrable by the same half-line integral. The estimate `ν_{k,j}≤2a_k d_k^(−B) j! α^(−j−1)` for even `j` proves finite moments directly. The comparison mass `ν_{k,0}` is never set equal to the arithmetic mass.

## 7. Positive-matrix comparison and the actual data cutoff: AU.13–15

The strictly positive comparison density gives `H_N^ν>0`, and domination gives `H_N^ν≤H_N`. Conjugation by `(H_N^ν)^(-1/2)` and inversion of positive eigenvalues proves `H_N⁻¹≤(H_N^ν)⁻¹`. Applying `E_N` and its adjoint gives `Kraw_N≤Kraw_N^ν`. Independently, minimizing the same affine quotient fibres proves `G_N^ν≤G_N`; these two directions agree under inversion and the fixed raw jet map.

Degree inclusion enlarges the set of source lifts, hence `V_{2q−1}≤V_q`. At degree `2q−1`, the raw kernel comparison bounds the first term of AU.9 from above and leaves its second, actual low-degree term unchanged. This proves both inequalities in AU.14. The actual Gram `H_q` has entries indexed by `i+j≤2q`; thus the highest actual moment used is exactly `2q`. The comparison Gram `H^ν_{2q−1}` reaches `i+j=4q−2`. No other step calls for a higher actual moment.

The coefficient matrix with the quotient monomials followed by `ψ,uψ,…` is square triangular with diagonal one, provided its columns fill the prescribed degree space. The Gram determinant is therefore unchanged. A Schur elimination of the relation Gram gives `V_N=det H_N/det(B_N*H_NB_N)`. At `N=2q−1` this is AU.15 and confirms the direction of the source/relation determinant upper bound.

## 8. Gamma coefficient transport: AU.16

Multiply the `k` generating functions in their original variable `z`. The product is `(1+z²)^(-kλ) exp((u_1+⋯+u_k) arctan z)`, so its coefficient of `z^l` is `b_l^(kλ)(u_1+⋯+u_k)/l!`. Integrating the finite derivative at zero gives

\[
\frac1{l!}\int b_l^{(k\lambda)}m_k
=c_\lambda^k\sum_{j_1+\cdots+j_k=l}
\prod_a(2\lambda)_{j_a}c_{h,j_a}.
\]

This verifies the factorial `l!`, the single factor `C_λ=c_λ^k`, and the absence of an extra multinomial in `d_l`. The monic degree-triangular expansion of `u^(i+j)` in the Gamma polynomials uses only orders at most `i+j`. Therefore coefficients through `c_{h,2q}` suffice for AU.14. At zero degree, `c_λ c_{h,0}=μ_h` and `C_λ c_{h,0}^k=μ_h^k`, so this conversion retains the source mass exactly.

## 9. Two-Laplace-value upper matrix and Cauchy–Binet: AU.17–20

For each `j`, `|u|^(2j)≤(2j)!b^(-2j)e^(b|u|)` follows from one nonnegative exponential-series term. Convolution gives `∫e^(±bu)m_k=M_h(±b)^k`. Weighted Cauchy–Schwarz gives `|Σa_ju^j|²≤(Στ_j)Σ|a_j|²|u|^(2j)/τ_j`, and integration yields the diagonal matrix majorant `H_q≤D_q(τ)` in AU.17.

Inversion reverses that inequality, so `Kraw_q≥(M_k Στ_j)^(-1) A_q(τ)`. Its determinant lower bound is the inverse contribution needed for the central upper bound. The factor on taking determinants is its `q`th power because the raw jet space has dimension `q`. This proves the sign and factor `q log(M_k Στ_j)` in AU.19.

Cauchy–Binet for `E diag(d_j)E*` gives `Σ_I |det E_I|² ∏_{j∈I}d_j`. Every summand is nonnegative, and the initial `q` columns give a strictly positive summand because they form `Z`. Thus `A_q(τ)>0` and its logarithmic determinant is defined. Common rescaling `τ↦sτ` contributes `q log s` in both terms and cancels, while neither source measure changes. Taking the infimum of a nonempty family of proved bounds is valid, whether or not an optimizer exists.

## 10. Interval comparison and Legendre kernel constants: AU.21–23

For `|u|≤T`, both factors in the comparison density are at least their values at `T`, so `ν_k(u)≥a_k(T)`. Hence `a_k(T)H_N^I(T)≤H_N^ν≤H_N`. All matrices are positive definite. After inversion and raw jet application, the order is exactly the chain in AU.23.

For completeness, Rodrigues and `j` integrations by parts give orthogonality to every lower-degree polynomial. Its leading coefficient is `(2j)!/(2^j(j!)²)`. The beta integral needed for the norm is

\[
\int_{-1}^1(1-x^2)^jdx
=2\,4^j\int_0^1t^j(1-t)^jdt
=\frac{2^{2j+1}(j!)^2}{(2j+1)!},
\]

where the last equality follows by repeated ordinary integration by parts. Thus `∫P_j²=2/(2j+1)`. On `[-T,T]`, the polynomial `P_j(u/T)` has squared norm `2T/(2j+1)`, and an order-`d` derivative contributes `T^(-d)`. The kernel denominator is consequently `2T^(1+d+e)`, as in AU.22, with conjugation on its second jet factor. Taking the determinant of multiplication by `a_k(T)^(-1)` gives `−q log a_k(T)`. The interval replacement is always at least as large an upper bound as the global envelope estimate because the two raw kernels have the displayed positive order.

## 11. Exact scaled chart in the scalar proof: AU.24–25

The root bound is `|ζ_ab|≤k sqrt(δ²+γ²)=kR_0`. For `D=max(1,2/b,2R_0)` and `T=Dq`, the roots of `χ_T=(iT)^(-q)χ(c+iTx)` have modulus at most `r=kR_0/(Dq)≤1/2`, because `q≥k`. The scaled chart has target measure `Tm_k(Tx)dx`, retaining mass `μ_h^k`, and relation multiplier `(iT)^q` exactly.

In the original `S` monomials its source coefficient matrix has diagonal `(iT)^j`, so its quotient determinant is `(iT)^(q(q−1)/2)`. The target quotient Gram is obtained by inverse congruence and has determinant `T^(−q(q−1)) V_N`, independent of the source degree `N`. This factor cancels in the central ratio, and the full raw derivative multiplier is `(iT)^d`. The estimates can thus be transported back as Hermitian inequalities as well as as determinant inequalities.

## 12. Coefficient and complete-remainder estimates: AU.26–27

Leibniz applied to `(x−1)^j(x+1)^j` proves the stated Legendre expansion. Submultiplicativity of the coefficient `ℓ¹` norm and the binomial coefficient identity give `||P_j||_coeff,1≤binom(2j,j)≤4^j`. In the orthogonal expansion of `f`, each Legendre coefficient is at most `sqrt((2j+1)/2)||f||_L²`. Summing and using the geometric series gives exactly `A_N=sqrt((2N+1)/2)(4^(N+1)−1)/3`.

For a repeated root list `z_1,…,z_q`, the formal inverse product has coefficients `h_j`. Multiplication with the elementary-symmetric generating polynomial proves that `Q_s=Σ_{j=0}^s h_j x^(s−j)` is the actual quotient in division of `x^(q+s)` by `χ_T`. All intermediate coefficients of degrees `q,…,q+s−1` vanish exactly. The remaining product therefore consists of its leading monomial of coefficient one and the negative remainder. The coefficient-norm subtraction of one is consequently valid.

Bounding the elementary and complete homogeneous coefficients gives `(1+r)^q Σ_{j≤s}binom(q+j−1,j)r^j−1`, which is bounded above by `((1+r)/(1−r))^q`. Degrees below `q` give coefficient norm one. Linearity proves AU.27 on the complete source degree range `≤2q−1`, retaining repetitions throughout. This proof does not require distinct roots or an inverse Vandermonde.

## 13. Scalar source norm and positive inverse comparison: AU.28–31

For a degree-below-`q` polynomial `v`, each monomial is bounded in absolute value by `max(1,|u/T|^(q−1))`. Squaring the coefficient-norm bound, replacing `max(1,y)` by `1+y`, and applying the original Laplace moment estimate yields AU.28 with its two distinct mass terms. The original source restricted to `[-T,T]` gives the lower norm factor `Ta_k(T)`. Combining the two estimates with AU.26–27 proves the bounded remainder map in AU.29.

Applied to a least lift of `x`, the remainder is already a lift at degree `q−1`, hence `G_q≤G_{q−1}≤C G_N`. Degree inclusion gives `G_N≤G_q`. Inversion after a positive congruence yields `K_q≤K_N≤C K_q`, so the determinant upper bound is exactly `q log C`. The source and quotient dimension exponents have not been interchanged.

For the displayed growth constant: `bT≥2q` makes the factorial ratio at most one; `M_k=∫2cosh(bu)m_k≥2μ_h^k` yields `U_k(T)≤3X^k`. Next `A_(2q−1)²≤(2q/9)256^q`. Finally, on `[0,1/2]`, the derivative of `log((1+r)/(1−r))` is at most `8/3`, yielding `log B_q(r)²≤(16R_0/(3D))k`. The factor `3·(2q/9)/(Dq)` is `2/(3D)`, which explains the literal `C_env=max(1,2/(3c_hD))`. Combining the unchanged factors gives every term of AU.31. The final article uses this distinct name for the envelope constant, avoiding a collision with degree-zero Legendre `A_N`.

## 14. Two local typing clarifications reported during review

First, before the scalar section, `H_N` denotes the `u`-monomial Gram and `J_N` is remainder modulo `ψ`. The scalar proof then applies `Ψ_T` and `rem_χ` to an `S` polynomial. Its norm symbols must explicitly be `H_N^S` and `H_{q−1}^S`, or it must explicitly restart its notation in that chart. The exact repair is the unscaled congruence in item 2 followed by the scaled congruence in item 11. In particular no numerical estimate or volume value changes. A complete typed insertion can introduce `H_N^S=A_N*H_NA_N`, `J_N^S=A_(q−1)⁻¹J_NA_N`, and `K_N^S=A_(q−1)⁻¹K_NA_(q−1)^(-*)`; the Hermitian inequality then returns to the earlier coordinates by congruence.

Second, the selector `s:E→P_(q−1)` is the right inverse of `J_(q−1)`. The composition `sJ_N:P_N→P_(q−1)` is the bounded remainder map. Its exact identities are `J_(q−1)s=I_E`, `J_(q−1)sJ_N=J_N`, and restriction to `P_(q−1)` equals the identity. Saying that the composition itself is a right inverse would conflate its source with the quotient source. These equations repair the wording at the required types.

Resolution verified in the final source: the coefficient chart is now named `𝕋_j`, all of `H_j^S,J_j^S,K_j^S,G_j^S` are introduced with the literal congruences, every source norm on `S` polynomials has the superscript `S`, and the least lift is `R_N^S`. The remainder paragraph now uses `π_(χ,N)` and states both `π_(χ,q−1)s=I` and `π_(χ,q−1)sπ_(χ,N)=π_(χ,N)`. The final step transports the Hermitian inequality from `K_j^S` to `K_j` by the specified congruence. Thus both findings are closed mathematically.

## 15. Literal upper-minus-lower gap: AU.32–33

The four-volume continuation supplies the central lower quantity `L_k=2(q−1)(log k+log(δ/(2C_h^bal)))`. Subtracting it from the explicitly displayed scalar upper quantity is exactly AU.32; this is a difference between proved bounds and does not assert the unknown volume's value. For fixed packet, `q=[1+k(m−1)](k+1)²`; therefore `k/q→0`, `log q/q→0` and `log k/q→0`. After division by `q²`, every term of the difference except `(αD+log256)` vanishes. This proves AU.33.

When divided by `q log k`, the leading upper term is `(αD+log256)q/log k`. It is asymptotic to `(αD+log256)k²/log k` for `m=1` and to `(αD+log256)(m−1)k³/log k` for `m>1`. Thus this scalar route leaves an explicitly calculated gap. The origin of its quadratic loss is identified in the full coefficient bound and the density's least value on the length-`2Dq` interval. The remainder map itself contributes only the proved order-`k` logarithmic cost.

## 16. Auxiliary source/relation identity and exact parity blocks: AU.40–42

For the explicitly stated auxiliary source `du` on `[-1,1]`, the mass is two. The relation `u^q` has `q` raw jets at the origin. The same triangular Gram elimination gives `V_N=D_(N+1)/B_(N−q+1)(q)`. Consequently its central ratio is exactly `D_(q+1)B_q(q)/(B_1(q)D_(2q))`, with `B_1(q)=2/(2q+1)`.

The monic Legendre norm is `2/(2j+1)·(2^j/binom(2j,j))²`, yielding AU.41 by multiplying consecutive monic norms. For `q=2s`, reorder the relation monomials by parity simultaneously in the rows and columns. The determinant incurs the square of the permutation sign, hence no sign change. Its even block entries are `2/(4s+2a+2b+1)=1/(2s+a+b+1/2)`. Its odd block entries are `1/(2s+a+b+3/2)`. The cross blocks vanish. The Cauchy numerator is `∏_(a<b)(b−a)²=∏_(j=0)^(s−1)(j!)²`, giving exactly AU.42.

## 17. Finite Legendre determinant error: AU.44

The central binomial bounds follow because the central coefficient is the largest among `2j+1` nonnegative binomial coefficients summing to `4^j`. They imply

\[
\frac{2^{1-2j}}{2j+1}
\le \frac{2}{2j+1}\left(\frac{2^j}{\binom{2j}{j}}\right)^2
\le 2^{1-2j}(2j+1).
\]

Multiplication for `0≤j<d` gives the central exponent `−d(d−1)log2` plus an error whose absolute value is at most `d log2+Σ log(2j+1)≤d log(4d)`. This proves AU.44 also at `d=1`.

## 18. Cauchy determinant integral and its finite error: AU.45

The logarithmic numerator is `2Σ_(i=1)^(s−1)(s−i)log i`. Writing `f(x)=(1−x)log x` gives

\[
2\sum_{i=1}^{s-1}(s-i)\log i
=s(s-1)\log s+2s\sum_{i=1}^{s-1}f(i/s).
\]

Here `f′=1/x−1−log x≥0`, `∫₀¹f=−3/4`, and `f≤0`. Monotonicity bounds the right-sum error between zero and `−∫₀^(1/s)f≤(log s+1)/s`. Hence the numerator differs from `s²log s−3s²/2` by at most `s log s+2s`.

The denominator is `s²log s+Σ_(a,b)log(2+a/s+b/s)`. Both partial derivatives lie between zero and `1/2`, so integrating the within-cell difference from the lower-left corner bounds the full sum error by at most `s` (indeed a smaller bound is possible but unneeded). With `F(t)=t²log t/2−3t²/4`, its double integral is `F(4)−2F(3)+F(2)=18log2−9log3−3/2`. Therefore

\[
\left|\log\mathcal C_s(2s)-9s^2\log(3/4)\right|
\le s\log s+3s.
\]

Changing the argument from `2s` to `2s+c` subtracts `Σ log(1+c/(2s+a+b))`, between `−cs/2` and zero. Applying the two shifts `1/2,3/2` and adding the previous errors gives `q log(q/2)+(7/2)q` at `q=2s`, exactly AU.45. The calculation is valid for `s=1`, since the empty numerator sum and the elementary integral bounds still apply.

## 19. Positive quadratic coefficient and the claimed finite constant: AU.43

Inserting the determinant estimates into the auxiliary ratio gives quadratic coefficient `3log2+(9/2)log(3/4)=(9/2)log3−6log2=(3/2)log(27/16)>0`. The linear contribution from the two determinant main terms is `−3q log2`, whose absolute value gives the corresponding term in the article's error display. The remaining terms are exactly the two `E_d` bounds, the AU.45 error, and `log((2q+1)/2)`.

For `q≥2`, the inequalities `q+1≤3q/2`, `4(q+1)≤8q`, `log(q/2)≤log(8q)` and `log((2q+1)/2)≤log(8q)` are valid. The constant multiples satisfy `3log2+7/2<3log16≤3log(8q)`. Summing gives at most `8q log(8q)`, hence the stated `12q log(8q)` is valid with room to spare. The estimate is finite for every even `q≥2`; it is stronger than a mere asymptotic statement. It concerns the stated auxiliary source only.

## 20. Monic family and all fibre maps: AU.46–47

The polynomial `ψ_t=∏(u−tζ_ab)^ℓ` is monic over `ℂ[t]`. The division algorithm over that ring proves spanning by `1,u,…,u^(q−1)`. If a nonzero multiple of a monic degree-`q` polynomial had degree below `q`, its leading coefficient would contradict monicity; thus those classes are linearly independent. The family is therefore free of rank `q` and every fibre has the same dimension.

At `t=1` it is the actual transported quotient; at zero it is `ℂ[u]/u^q`. For nonzero `t`, substitution `f(u)↦f(tu)` maps the `t` fibre to the `1` fibre because `ψ_t(tu)=t^qψ_1(u)`. Substitution by `u/t` is its inverse, with the opposite ideal relation. Differentiating gives the exact raw-jet multiplier `t^d` at order `d`. At zero, the proof uses the monic remainder basis, which stays a basis; it does not assert invertibility of separated evaluation rows when all centres coincide.

## 21. Fixed-source kernel path and determinant derivative: AU.48

For a fixed positive source Gram at each degree, the monic division algorithm expresses every coefficient of `J_N(t)` polynomially in `t`. Its first `q` columns remain `I_q`, so `J_N(t)` is surjective even at zero. Thus `K_N(t)>0` for every real `t`; its determinant and inverse are smooth there. The adjoint differentiates in the stated manner along this real parameter, giving `K_N′=J_N′H_N⁻¹J_N*+J_NH_N⁻¹(J_N′)*`.

The determinant multilinear derivative gives `(det K)′=det K·Tr(K⁻¹K′)`. Dividing by the positive determinant and subtracting the two degrees gives AU.48. This proves an exact source-dependent relation between the original fibre and the merged fibre. The estimate for Lebesgue measure at the merged fibre can only be transported using this actual changing kernel; the article makes no claim that the quadratic coefficient itself is invariant along the family.

## 22. Original representative and supported zero: AU.49

At each selected complete zero of `g`, division by the corresponding full factor of `h` leaves a nonzero local Taylor constant of `g/h`. A truncated Taylor series with nonzero constant is invertible by recursively solving its product coefficients. This multiplication therefore preserves the cyclic kernel of the tensor sum.

Successive monic division in the tensor variables gives a decomposition by the ideal generators `h(s_i)` plus a remainder in their product monomial basis. Since the original annihilator acts as zero and that basis is linearly independent, the remainder is zero. Applying the polynomial differential operators to the displayed tensor primitive and using the original identity `h(D)F_h=Θφ_0` gives the required representative difference. The sign `(-1)^(i−1)` in the primitive is cancelled by the tensor differential sign from the preceding `i−1` degree-one factors. Thus the supported relation is mapped to the supported zero at its existing label; the fibre map is explicitly given and does not change the external absence object.

## 23. Independent finite fixture and limits of its claims

Files:

- `check_arithmetic_volume_upper_independent_20260913.py`;
- `arithmetic_volume_upper_independent_checks_20260913.json`;
- `arithmetic_volume_upper_independent_checks_optimized_20260913.json`.

The source fixture is Lebesgue measure on `[-1,1]` plus positive atoms at `−2,1/3,5/4` with weights `1/7,2/5,3/11`. Its first moment is nonzero, so complex source-coordinate phases do not vanish through artificial evenness. The relation fixture `(u−i)²(u+i)²` tests repeated complex centres. A separate jet fixture `(u−i)³(u+i)³` tests raw order-two factorials and the scaled derivative phase. Every rational comparison matrix is tested using all principal minors, rather than floating-point eigenvalues.

The tests reconstruct the central ratio by both kernels and source/relation determinants, check the weighted diagonal majorant and Cauchy–Binet sum, and calculate exact auxiliary parity blocks and Legendre determinants at `q=2,4,6`. A symbolic monic family tests the quotient substitution identity and the determinant derivative through the merged fibre. No sampled arithmetic density, asymptotic claim, numerical Laplace enclosure, or Lean proof is inferred from these tests. Their normal and optimized output files are byte-identical because the explicit checks do not depend on Python assertions.

## 24. Source seal

**Final mathematical review status: pass.** No unresolved mathematical correction remains in the reviewed article. The final scalar proof and its surrounding type declarations were read again after the author incorporated item 14. The displayed gap AU.32 was split across lines without changing its terms, AU.31 uses an aligned display, the envelope prefactor is consistently `C_env`, and the final provenance refers to AU.24–33. These final changes preserve the proofs and constants checked above. This is a mathematical source review; the author's separate ten-page PDF visual review is not claimed here.

Sealed SHA-256 values:

- Article `arithmetic_volume_upper_route_20260913.tex`: `21aaedc3585887fa7d2cb3e37e68d14415829a4b213566f7a08f4619835ef38b`.
- Complete scalar derivation `volume_comparator_review_20260913.md`: `47ac2b43904ec43f3ce19d7c74ba760a29ce4d7a3e411132fe81ec0b27af6104`.
- Independent exact checker: `4af4be24807b203cd1233060b56808c45d05cad52fc7398683ce73c54aa17b37`.
- Normal receipt: `d28913a543027ca8890366aa181375fcd86186241ef8ed96c53f8f884952be0e`.
- Optimized receipt: `d28913a543027ca8890366aa181375fcd86186241ef8ed96c53f8f884952be0e`.

The original arithmetic `NOTE.tex` input at the cited envelope and Laplace equations is pinned by the intake manifest at `f776e7934f026342f48732a74f14d57470b8aae1cef76ebdee5f831bd49dedf8`. No primary source, original source packet, or primary article was edited by this review lane.
