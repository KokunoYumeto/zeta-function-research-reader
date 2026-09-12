# Independent review of the cyclic sum metric and connection

Date: 12 September 2026. Reviewer: `paired_connection_calibration`.

## Reading scope and result

I read the complete working section `cyclic_sum_metric_connection_20260912.tex`, CM.1–19; all 983 lines of the delivered `Tau_Cyclic_Sum_Control/NOTE.tex`; the complete density continuation `nested_relative_frame_density_20260912.tex`; and NN.1–4 with their original source definitions. The delivered note was read as mathematical source material, including its original assumptions and source claims. Its administrative instructions were not adopted as instructions for this task.

The CM identities are mathematically correct within their stated finite-source and fixed-source limiting scopes. This audit found no sign, tensor-degree, mass, crossed-term, or minimum-comparison defect. I requested three explicit typing clarifications from the author: the norm defining the monic polynomials in the original coordinate `S`; the map `∂_N:I/I²→E`, which is independent of `N`; and the precise kernels of the source map into the conormal layer and its derivative observation. All three are now present and were reread in the complete final CM source: the fixed derivative is named `∂_I`, and both kernel preimages are explicit. Their formulas and justification are given below. No cumulative, source-note, frozen-edition, or publication-stage files were edited by this reviewer.

## The original cyclic source and annihilator: CM.1–2

At an ordered tuple of actual selected roots, the original local algebra has coordinates `s_i=ρ_i+z_i` and full powers `z_i^{m_{ρ_i}}=0`. Put

\[
\lambda=\sum_i\rho_i,\qquad D=\sum_i(m_{\rho_i}-1),\qquad N=M_{z_1+\cdots+z_k}.
\]

Every monomial of total degree greater than `D` vanishes. The coefficient of the retained top monomial `∏z_i^{m_{ρ_i}−1}` in `N^D1` is `D!/∏(m_{ρ_i}−1)!`, which is nonzero in the original complex coefficient field. Therefore the nilpotent order is exactly `D+1`. Taking the maximum over tuples with the same actual sum, and then the product over distinct sums, gives CM.1. This keeps collided sums and every multiplicity.

The vector `1` is invariant. Its annihilator for multiplication by `S` is the annihilator of the algebra element `S` itself, because `P(M_S)1=P(S)`. Thus `α:C_χ→E^{S_k}` is an injective unital algebra map. The original unit `U_k=υ_h^{⊗k}` is invertible and commutes with multiplication by `S`; its multiplication map gives the distinct, explicitly defined module injection `η=M_{U_k}α`. No coefficient of that unit is replaced.

The original Mellin transform of `V_kP` is `(∏v_h(s_i))P(S)`. The product is nonzero on an open set; hence vanishing of this analytic function forces `P=0`. Its critical-line image is precisely `Ψ(u,y)P(k/2+iu)` with the original factor `(2π)^{-k/2}` contained in `Ψ` and the signed coordinate Jacobian of absolute value one. Squared norm and full jet evaluation therefore give CM.2. The retained scalar source is a specified injection into the full original source; it has its own fixed constant relative frame.

## Original moments, crossed terms and finite Gram matrices: CM.3–5

For the dagger-stable packet, `\bar a=(-1)^d a` on the original line, so `\bar a a'` is real and equals `w'/2`. Original decay gives zero boundary terms after multiplication by every power of `t`. Thus

\[
\theta_0=0,\qquad
\theta_j=\frac12\int t^jw'(t)dt=-\frac j2\mu_{j-1}\quad(j\ge1).
\]

Consequently the formal series of these mixed moments is exactly `Θ(z)=−z Mcal(z)/2`. This is an identity of formal coefficients, with no convergence hypothesis required for CM.4.

For the original derivative at fixed relative coordinates,

\[
\Psi'=\frac1k\sum_i a'(t_i)\prod_{r\ne i}a(t_r).
\]

Squaring has `k` diagonal terms and `k(k−1)` ordered distinct-index terms, each carrying the original common factor `k^{-2}`. Multinomial expansion of `u^j=(Σt_i)^j` and absolute Fubini evaluation give, respectively,

\[
\frac1k\mathcal N(z)\mathcal M(z)^{k-1},\qquad
\frac{k-1}{k}\Theta(z)^2\mathcal M(z)^{k-2}
=\frac{k-1}{4k}z^2\mathcal M(z)^k.
\]

The fixed phase makes both mixed-factor integrals equal to the same real moment series. This proves the sign and coefficient of the second term of `B_{j,k}`. It vanishes at the unweighted zeroth coefficient; it is retained at higher coefficients. The mass array follows from the same multinomial calculation without derivatives. No evenness condition on the one-factor density is needed, and `μ_1` need not vanish.

For the original complex source powers `c_j(u)=(k/2+iu)^j`,

\[
(\Psi c_j)'=\Psi'c_j+\Psi c_j',\qquad
c_j'=ij(k/2+iu)^{j-1}\quad(j\ge1).
\]

Pairing this expression for columns `i,j` gives four terms. The two crossed terms use `⟨Ψ,Ψ'⟩=⟨Ψ',Ψ⟩=m_k'/2`, so they are precisely

\[
\frac12\int\overline{c_i}c_j'm_k'\,du,
\qquad
\frac12\int\overline{c_i'}c_jm_k'\,du.
\]

They are separate matrix contributions; their entries may have imaginary parts. Their polynomial moment rule is `∫u^r m_k'=−r M_{r−1,k}` for `r≥1`, with zero at `r=0`. These observations establish every coefficient in CM.5 from the original arrays.

Both finite forms are strictly positive. For the amplitude form, `m_k(u)>0` everywhere and a nonzero complex polynomial on the line has finitely many zeros. For the derivative form, a zero quadratic form gives an original `L²(du;H)` amplitude with zero weak derivative. Pairing with each vector in a countable dense subset of the separable fibre Hilbert space gives scalar distributional constants. Each such constant must vanish because it is in `L²(R)`. Therefore the whole amplitude vanishes, and injectivity of the original polynomial source forces the zero coefficient vector. This proves the stated strictness without replacing the derivative form by a scalar Fisher bound.

## The canonical representative and both retained forms: CM.6–7

The monic polynomials are in the original variable `S` and have

\[
\omega_j=\int_{\mathbb R}|p_j(k/2+iu)|^2m_k(u)du>0.
\]

This explicit norm was requested at the point of definition so that the variable is not confused with a monic polynomial in the real coordinate `u`. It is exactly the convention in delivered source equation (4.1).

In the original orthogonal polynomial coordinates, let `Ω=diag(ω_0,…,ω_N)` and let `B` have columns `b_j=[p_j]_χ` in the fixed remainder basis. The first `degχ` columns span that remainder space because the polynomials are monic in successively increasing degrees. Thus, for `N≥degχ−1`,

\[
K_N=B\Omega^{-1}B^*>0,\qquad G_N=K_N^{-1},\qquad
a_{\min}(x)=\Omega^{-1}B^*G_Nx.
\]

Direct multiplication gives `Ba_min=x`. If `Br=0`, then `a_min(x)^*Ωr=x^*G_NBr=0`. Therefore this representative is orthogonal to the exact cyclic relation kernel and is the unique minimum. Its norm is `x^*G_Nx`. Multiplication by the actual coefficient vectors of the monic `p_j` gives exactly `T_N` in CM.6. Its full arithmetic jet is `ηx`, including `U_k`.

Applying the complete derivative Gram from CM.5 to those same coefficient vectors gives `T_N^*H^∂T_N`, with all crossed terms retained. This proves both equalities in CM.7. The source norm, derivative norm and arithmetic inclusion have explicit matrix maps between them; none has been substituted for another.

## Actual exponential integrals and tilted information: CM.8–12

I checked the density section’s original-amplitude tail proof used here. Rotation of Euler’s gamma integral through the angle `sgn(τ)φ`, `0<φ<π/2`, gives

\[
|\Gamma(\lambda+i\tau)|\le e^{-\phi|\tau|}\Gamma(\lambda)(\cos\phi)^{-\lambda}.
\]

The small and large arcs vanish with the original principal power; the bound is uniform for `λ` in the compact interval `[1/8,3/8]`. The counting-function formula `ζ(s)=s/(s−1)−s∫_1^∞{x}x^{-s-1}dx` supplies the stated polynomial bound on `1/4≤Re s≤3/4`. Combining these with the original gamma argument `s/2` yields the exponent `φ|t|/2`. For large `|t|`, every factor of the original monic `h` has modulus at least `|t|/2`; on the complementary compact rectangle its entire quotient is bounded, including the selected full cancellations. Cauchy estimates on the radius-`1/8` circles then establish every derivative bound `|a^{(j)}(t)|≤C_{h,j,b}e^{-b|t|}` for every `b<π/4`.

For real `|θ|<π/2`, choose `|θ|<2b<π/2`. This gives absolute integrability of both defining expressions in CM.8. On every compact subset of the complex strip `|Re z|<π/2`, choose a single strictly larger `2b`; its remaining exponential margin also absorbs every polynomial factor from complex differentiation. Thus the integral formulas extend holomorphically to that open strip, with exactly the moments in CM.4 as derivatives at zero. No endpoint assertion at `|θ|=π/2` is used.

Integration by parts with this weighted decay gives

\[
\int e^{\theta t}\bar a a'\,dt=-\frac\theta2M(\theta).
\]

Applying the same `k` versus `k(k−1)` count as above therefore gives CM.9. This is a calculation of the original derivative `Ψ'` under an exponential measure. The multiplier in CM.10 gives a distinct, explicitly related derivative:

\[
a_\theta=e^{\theta t/2}a,\quad
a_\theta'=e^{\theta t/2}(a'+\theta a/2),\quad
\|a_\theta'\|^2=N(\theta)-\frac{\theta^2}{4}M(\theta).
\]

The negative coefficient results from the full crossed contribution `θ(−θM/2)` plus `θ²M/4`. The mass is `M(θ)`, not one. The last squared norm is positive: a zero derivative would make a nonzero `L²` function constant. The exponential multiplier is an onto isometry between the exact weighted and unweighted Hilbert spaces in CM.10, with the displayed inverse.

At the product level, `Ψ_θ=e^{θu/2}Ψ`. Thus `m_{k,θ}=e^{θu}m_k`, the line projection is unchanged on each fibre, and the normal component is exactly `e^{θu/2}n_k`. Moreover `∫\bar a_θ a_θ'=0`, either by differentiating its decaying squared modulus or by adding `θM/2` to the original weighted mixed integral. Therefore the complete product derivative has squared norm

\[
\int\|\Psi_\theta'\|^2du
=\frac1kM(\theta)^{k-1}\left(N(\theta)-\frac{\theta^2}{4}M(\theta)\right).
\]

Its exact line/normal decomposition has squared line norm

\[
\frac14\int e^{\theta u}\frac{(m_k'+\theta m_k)^2}{m_k}\,du
\]

and squared normal norm `∫e^{θu}||n_k||²du`. Multiplication by four proves CM.12. All integrals are finite, including the score quotient: its squared line norm is bounded by the full derivative energy through orthogonal projection. Here `m_k>0` everywhere, so it has no denominator zero.

Strict positivity of the normal integral follows from the actual FC zero argument, with its original zero orders. Multiplication by the nonzero real exponential leaves the zero set and the set of fibres with nonzero normal vector unchanged. Its exponential is positive in the integral. For an original quartet two-factor zero fibre at `u=0`, the normal vector remains exactly zero after tilting; the added derivative term is tangential. This is consistent with strictly positive integrated normal energy. The tilted identity consequently does not discard that exceptional fibre or the original mass.

## Fixed cyclic source under full relative enlargement: CM.13–15

For a fixed polynomial `P(S)`, its derivative coefficient is `ic_{P'}`. The term `Ψ ic_{P'}` lies in the original constant relative line. Every full relative frame contains that line; hence

\[
\begin{aligned}
\Pi_0d(P)&=\Psi\left(ic_{P'}+\frac{m_k'}{2m_k}c_P\right),\\
(\Pi_m-\Pi_0)d(P)&=(\Pi_m-\Pi_0)\Psi'c_P,\\
(I-\Pi_m)d(P)&=(I-\Pi_m)\Psi'c_P.
\end{aligned}
\]

These are actual maps of the same original derivative vector. Their ranges are respectively `ranΠ_0`, `ranΠ_m∩kerΠ_0`, and `kerΠ_m`, which are mutually orthogonal because the projections are nested. Subtracting the first from `d(P)` gives `n_k c_P=b_m(P)+r_m(P)`, and taking full original norms proves CM.14.

The complete density proof establishes `Π_m(u)→I` strongly on every fibre, using the original weighted exponential moment and the onto multiplier `q↦Ψ_u q`. Its global fixed-source conclusion uses the single fixed vector `Ψ'c_P∈K` and projection contraction as an integrable dominating function. Thus `r_m(P)→0` in `K`; the displayed exact subtraction gives `b_m(P)→n_k c_P` in the same space. The whole cyclic normal energy is the limit of the additional full-frame tangential energy.

For a finite fixed collection, Cauchy–Schwarz applied to pairings of convergent vectors gives entrywise and hence finite-dimensional matrix convergence of the restricted Gram arrays. All coefficients and original polynomials stay fixed. A sequence of changing canonical representatives `T_Nx` is outside this fixed-source conclusion, exactly as CM.15 states.

## Common degree, both minima, and their exact control difference: CM.16–18

The new bound `degχ−1≥k(d−1)` is valid for every nonempty monic original `h`, including `d=1`. For each `0≤q≤k(d−1)`, choose integers `0≤α_i<d` with `Σα_i=q`; such a choice is obtained by allocating at most `d−1` to each coordinate in order. The standard monomial `s^α` occurs in `S^q` with coefficient `q!/∏α_i!`. Replacing a nonstandard factor `s_i^d` using the original monic polynomial replaces it by terms of smaller degree in that coordinate and does not increase any other coordinate’s degree. Each reduction therefore strictly lowers total degree. Consequently no reduced nonstandard term of `S^q` can change the coefficient of this degree-`q` standard monomial. The remainder of `S^q` has total degree exactly `q`, while all smaller powers have smaller remainder degree.

The remainders `1,S,…,S^{k(d−1)}` are therefore independent. An annihilating polynomial of degree at most `k(d−1)` is impossible, proving the claimed lower bound for the exact `χ`. At every `N≥degχ−1`, an arbitrary target `y∈E` is reached by the monic multivariate remainder of `U_k^{-1}y`, whose total degree is at most `k(d−1)`. This explicitly proves full-source surjectivity at the same degree where the cyclic minimum is defined; it retains the full jet unit.

Both representatives in CM.16 are actual finite polynomial-source vectors and have jet `ηx`. Their difference is an actual vector in the original full boundary kernel. The full minimum is orthogonal to that entire boundary subspace. Thus its cross term with `Δ_Nx` vanishes, and polarization gives

\[
G_N=\eta^*G_N^{\rm full}\eta+\Delta_N^*\Delta_N.
\]

This is an equality of full forms in their stated coordinate bases. Substituting it into the cyclic control `A_χ^*G_N+G_NA_χ−kG_N`, and using `A_kη=ηA_χ`, yields exactly the second identity in CM.17. The linear map on the positive Gram difference is `E_N↦A_χ^*E_N+E_NA_χ−kE_N`; its sign is not replaced by positivity of `E_N`. For an actual eigenvector, applying `A_χx=λx` on each side of the form gives `(\bar λ+λ−k)x^*E_Nx`, exactly CM.18.

## The actual polynomial difference and its conormal derivative: CM.19

The original full polynomial source map `T_h^{(k)}` is injective by its analytic Mellin transform. Therefore the actual difference `Δ_Nx` has a unique original polynomial `Q_x` of total degree at most `N`, and `x↦Q_x` is linear. Its zero full jet says `U_k[Q_x]_I=0`. Since the actual unit is invertible, this is equivalent to `Q_x∈I`.

Fix univariate monic division in the order `s_1,…,s_k`. If `R_i,D_i` are respectively its remainder and quotient operators in variable `s_i`, then

\[
Q_{i,x}=D_iR_{i-1}\cdots R_1Q_x,
\qquad
Q_x=\sum_i h(s_i)Q_{i,x}+R_k\cdots R_1Q_x.
\]

The final term is zero because `Q_x∈I`. These operators are linear; each nonzero quotient has total degree at most `N−d`. Thus this is an actual fixed-order linear division, retaining every coefficient of the monic `h`. It also supplies the original top cochain primitive: put `φ_*` in position `i`, `F_h` in the other positions, apply `Q_{i,x}(D_1,…,D_k)`, and multiply by `(-1)^{i−1}`. The tensor differential contributes the same sign at that position, so their product is `+1` and the sum is exactly `Δ_Nx`.

The precise two maps are

\[
\kappa_N:C_\chi\to I/I^2,\qquad x\mapsto[Q_x]_{I^2},
\]

\[
\partial:I/I^2\to E,\qquad
[Q]_{I^2}\mapsto\left[\frac1k\sum_i\partial_{s_i}Q\right]_I.
\]

The latter is independent of the source degree `N`. The derivative of a product of two members of `I` lies in `I`, so it is well defined on `I/I²`. Applying its product rule to the fixed-order division gives

\[
\partial\kappa_N(x)=\frac1k\sum_i h'(s_i)[Q_{i,x}]_I.
\]

This depends only on the actual conormal class, even if another division is chosen. For the full analytic unit `U=∏v_h(s_i)`, the product rule yields `δ(UQ_x)=(δU)Q_x+UδQ_x`. The first summand has zero class in `E`; the second retains the full unit and all derivative coefficients. Mellin differentiation by the original average logarithm then gives

\[
J^{(k)}\mathscr L_k\Delta_Nx
=U_k\partial\kappa_N(x),\qquad
\mathscr L_k=\frac1k\sum_i\log x_i.
\]

There is no extra factor `i`: it occurs in the spectral derivative `∂_u=i Ucal_k L_k Ucal_k^{-1}` and is removed when expressing the arithmetic logarithmic observation itself. This checks the full constant and sign in CM.19.

For the source maps the exact kernel formulas are

\[
\ker\kappa_N=\{x:Q_x\in I^2\},\qquad
\ker(J^{(k)}\mathscr L_k\Delta_N)
=\kappa_N^{-1}(\ker\partial).
\]

These are the requested explicit preimages of the full conormal kernel; they do not identify a kernel in `C_χ` with a kernel in `I/I²`. The ordinary quotient of `Q_x∈I` is its supported zero, whereas the stated conormal class is taken before that quotient. The two maps and their commuting derivative calculation specify the exact relationship. External absence is preserved by the original linear split lift, independently of those supported classes.

## Exact non-even tilted calibration

The separate fixture uses the original amplitude `a(t)=(t+1)e^{-t²/2}`, without division by its mass, and `k=2`. Its script directly differentiates the original product and independently computes the original Gram arrays in `1,S,S²` at `S=1+iu`, including both nonzero complex crossed matrices. It also computes the original weighted product derivative and the derivative after the positive exponential multiplier separately.

Writing the original common factor explicitly, exact Gaussian moments give

\[
M(\theta)=\sqrt\pi e^{\theta^2/4}
 \left(\frac{\theta^2}{4}+\theta+\frac32\right),
\]

\[
N(\theta)=\sqrt\pi e^{\theta^2/4}
 \left(\frac{\theta^4}{16}+\frac{\theta^3}{4}
       +\frac{\theta^2}{2}+\frac\theta2+\frac54\right),
\]

\[
N(\theta)-\frac{\theta^2}{4}M(\theta)
=\sqrt\pi e^{\theta^2/4}
 \left(\frac{\theta^2}{8}+\frac\theta2+\frac54\right)>0.
\]

These values were computed independently by this reviewer and reproduced by the fixture’s direct calculation. At `θ=1`, the original weighted product derivative energy is `143πe^{1/2}/32`; the derivative energy of the tilted product is `165πe^{1/2}/64`; and the entire CM.12 right-hand side is `165πe^{1/2}/16`. They are distinct values connected by the exact multiplier and its derivative term.

The fibre computation retains

\[
b=1+u/2,\quad C=\sqrt{\pi/2},\quad
F=(b^2-1/4)^2+1/8,
\]

\[
m(u)=Ce^{-u^2/2}F,\qquad
\|n(u)\|^2=Ce^{-u^2/2}\frac{b^2}{8F}.
\]

The normal term is nonzero except at `u=-2`. Positive tilting leaves this zero fibre unchanged and preserves strictly positive integrated residual. The fixture thus checks the crossed terms and strict-information mechanism in a non-even density while retaining its mass. It does not identify this model with the arithmetic theta amplitude or assert an arithmetic asymptotic. The full fixture files and exact mode outcomes are recorded with the final review receipt.

## Final certification scope

CM.1–19 is approved within the explicitly proved finite-source comparisons, the open real-exponential parameter interval, and the fixed-source frame limit. The delivered cyclic note, the ND decay and density arguments used by CM, and the complete arithmetic difference map were read. The independent algebra spot-check agreed with the common-degree and conormal calculations. The final complete CM source has SHA256 `7f58291e609995d05f99249a19d8835d2e12c7c7c182b1890b9a4d158511bb3c`. All three typing clarifications are closed. The non-even tilted fixture passes 21 exact checks in ordinary and optimized Python, with independent reproduction of its original moment arrays, both full Grams and tilted product energies. Final source hashes and fixture receipts are pinned by the accompanying manifest.
