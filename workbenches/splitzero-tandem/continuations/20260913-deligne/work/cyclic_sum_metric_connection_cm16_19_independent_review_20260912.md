# Independent proof audit of CM.16–19

Date: 2026-09-12. Reviewer: `paired_checker_review`.

## Scope and result

I read the complete current `work/cyclic_sum_metric_connection_20260912.tex` and independently checked CM.16–19. I also read the complete source-note sections 3, 7 and 8 at `sources/web_cyclic_sum_delivery/Tau_Cyclic_Sum_Control/NOTE.tex`, including the original source inclusion, minimum comparison, thickened derivative maps and full unit-weighted conormal derivative.

The CM source snapshot reviewed has SHA256 `7f58291e609995d05f99249a19d8835d2e12c7c7c182b1890b9a4d158511bb3c`. The delivered source NOTE has SHA256 `2cdfd5b25631464f9500dc5fd07c4c8f5c927c8877eb1bf076307ec5dcbc2e8c`. CM.16–19 is mathematically correct in the revised snapshot. The initially undefined `partial_N` has been replaced by the explicitly typed, cutoff-independent `partial_I:I/I²→E`, and the final kernel statements have been replaced by their precise inverse images. I read those repairs in the revised source. No source edits were made by this reviewer.

An independent child reviewer, `cyclic_degree_spotcheck`, separately checked the leading-degree argument, both minima at the same cutoff, the unique boundary polynomial and fixed-order division, and found no mathematical defect. The full proof details of this audit follow.

## The original leading-degree calculation

Put `d=deg h≥1`, retaining its monic coefficients, and write

\[
h(s)=s^d+\sum_{j=0}^{d-1}h_js^j.
\]

The original product remainder basis consists of `s^α` with `0≤α_i<d`. For a monomial having `α_i≥d`, one reduction in variable `s_i` replaces

\[
s_i^{\alpha_i}\longmapsto
-\sum_{j=0}^{d-1}h_js_i^{\alpha_i-d+j}.
\]

Every resulting term has total degree at most the original degree minus one. Subsequent reductions never increase total degree. Thus every originally nonstandard monomial of degree `q` contributes only terms of degree strictly less than `q` to its full product remainder. This conclusion uses the original coefficients and does not alter the polynomial `h`.

For every integer `0≤q≤k(d−1)`, a tuple `0≤α_i≤d−1` with total `q` exists: distribute `q` successively into `k` slots, each of capacity `d−1`. In the original multinomial expansion of `S^q=(s_1+⋯+s_k)^q`, the standard monomial `s^α` has coefficient `q!/∏α_i!`, a nonzero complex number. No reduction of any originally nonstandard term can contribute to degree `q`, and no different standard term is that same monomial. Its coefficient therefore survives unchanged.

Consequently the remainder of `S^q` has total degree exactly `q`. If `P(S)` is nonzero of degree `q≤k(d−1)`, its highest nonzero coefficient multiplies this nonzero degree-`q` component. Remainders of its lower powers have smaller total degree and cannot cancel it. Hence `P(S)` cannot vanish in the full original algebra `E`.

The exact annihilator `χ` from CM.1 is monic and nonzero. Its degree must therefore exceed `k(d−1)`, proving

\[
\deg\chi-1\ge k(d-1).
\]

For `d=1`, the argument reduces to the nonzero remainder of `S^0=1`; the bound reads `degχ≥1`, with no empty or negative-degree exception required. Repeated roots and collided sums do not affect the leading-degree argument: it takes place in the original monic remainder basis before any decomposition into local root coordinates.

## Both canonical minima exist at the same cutoff

At `N≥degχ−1`, every class of `C_χ` has a scalar remainder of degree at most `N`. Thus the cyclic quotient map on `C[S]_{≤N}` is onto. Its original source Gram is positive definite because `m_k(u)>0` and a nonzero coefficient polynomial cannot vanish on a set of full real measure. The cyclic minimum and its linear representative map therefore exist uniquely.

For the full quotient, take any target `y∈E`. Since the full original Taylor unit `U_k` is invertible, form the original multivariate remainder `P_y=rem(U_k^{-1}y)`. Each individual exponent is less than `d`, and therefore its total degree is at most `k(d−1)≤N`. The original full jet formula gives

\[
J^{(k)}\mathcal T_h^{(k)}P_y=U_k[P_y]_I=y.
\]

This proves full surjectivity at the same `N`, with the unit included explicitly. The full polynomial source has positive definite original norm: its analytic transform is the nonzero entire product `∏v_h(s_i)` times its polynomial, and vanishing on the open set where that product is nonzero forces the polynomial to be zero. Thus the full minimum exists uniquely on all of `E` and is linear in `y`.

The scalar source inclusion uses the literal substitution `P(S)↦P(s_1+⋯+s_k)` and preserves total degree. Therefore both representatives appearing in `Δ_N` lie in precisely the same original full source of cutoff `N`.

## Exact orthogonal Gram and control differences

Let `D_N` denote the kernel of the full jet restricted to that original full source. The full minimum `R_N^full y` is orthogonal to `D_N`: for any `b∈D_N`, the affine line `R_N^full y+zb` represents the same target, and minimization of its squared norm for every complex scalar `z` forces the cross inner product to vanish.

The two representatives of `x∈C_χ` have full jets `ηx`, so `Δ_Nx∈D_N`. The orthogonal decomposition

\[
\mathcal R_Nx=R_N^{\rm full}\eta x+\Delta_Nx
\]

therefore yields the full sesquilinear identity, including mixed input vectors,

\[
G_N=\eta^*G_N^{\rm full}\eta+\Delta_N^*\Delta_N.
\]

The maps `A_k` and `A_χ` are multiplication by the same original sum in their respective algebras. Since multiplication by `U_k` commutes with multiplication by that sum, `A_kη=ηA_χ`. Taking the adjoint gives `η^*A_k^*=A_χ^*η^*`. Substitution into the definitions

\[
W_N=A_\chi^*G_N+G_NA_\chi-kG_N,
\qquad
W_N^{\rm full}=A_k^*G_N^{\rm full}+G_N^{\rm full}A_k-kG_N^{\rm full}
\]

proves CM.17 with exactly the coefficient `−k` and the two positive adjoint terms. No positivity of the control difference is inferred from the positive Gram difference.

For an actual eigenvector `A_χx=λx`, the first mixed term has coefficient `bar λ` and the second has coefficient `λ`. Hence the displayed difference evaluates to

\[
(\overline\lambda+\lambda-k)x^*(\Delta_N^*\Delta_N)x
=(2\operatorname{Re}\lambda-k)\|\Delta_Nx\|^2,
\]

which proves CM.18 without rescaling the eigenvector or losing the sign of the coefficient. This assertion concerns an actual eigenvector; it does not erase the nilpotent terms on generalized eigenvectors.

## The unique polynomial difference and its fixed-order division

Both representatives have unique original polynomial coordinates because the full analytic source map `mathcal T_h^(k)` is injective. Therefore `Q_x=(mathcal T_h^(k))^{-1}Δ_Nx` is uniquely specified, depends linearly on `x`, and has total degree at most `N`. The vanishing full jet gives `U_k[Q_x]_I=0`; invertibility of `U_k` gives `Q_x∈I`.

A concrete linear division procedure is available. Set `r_0=Q_x`. In the fixed order `i=1,…,k`, perform ordinary monic division in `s_i`, with coefficients in the polynomial ring of all other original variables:

\[
r_{i-1}=h(s_i)Q_{i,x}+r_i,
\qquad \deg_{s_i}r_i<d.
\]

Each quotient and remainder operator is coefficient-linear. Later divisions do not increase the already bounded degrees in earlier variables because each divisor involves only its own variable. The final remainder is the unique multivariate product remainder, and it is zero because `Q_x∈I`. Telescoping gives the original relation `Q_x=Σ_i h(s_i)Q_{i,x}`, linearly in `x`.

The same total-degree reduction argument shows `deg Q_{i,x}≤N−d`; a negative bound means that quotient is zero. This confirms that the procedure introduces no higher source degree. The conormal class `[Q_x]_{I²}` depends only on the uniquely specified polynomial, irrespective of which displayed division is used to compute coordinates.

The relation also has its original cochain primitive. In factor `i`, replace `F_h` by `φ_*`, apply `Q_{i,x}(D_1,…,D_k)`, and assign the primitive sign `(-1)^{i−1}`. The tensor differential contributes its own sign `(-1)^{i−1}`, giving the positive boundary `h(D_i)Q_{i,x}(D)F_h^{⊗k}`. Thus the sum is the actual polynomial-source boundary `mathcal T_h^(k)Q_x`, with both original signs accounted for.

## The fully typed derivative and all factors

Let `P=C[s_1,…,s_k]` and retain the original coefficient derivative `δ=k^{-1}Σ_i ∂_{s_i}`. The product rule proves `δ(I²)⊂I`. Consequently its restriction induces the well-defined map

\[
\partial_I:I/I^2\longrightarrow E=P/I,
\qquad [Q]_{I^2}\longmapsto[\delta Q]_I.
\]

This is a coefficient-linear map independent of `N`. It is also `E`-linear on this conormal domain: for `a∈P`, `Q∈I`, the term `(δa)Q` vanishes modulo `I`, so `[δ(aQ)]_I=[a]_I[δQ]_I`. This property concerns the conormal restriction and does not assert that differentiation descends on `P/I`.

Applying `δ` to the fixed-order relation gives

\[
\delta Q_x
=\frac1k\sum_i h'(s_i)Q_{i,x}
  +\sum_i h(s_i)\delta Q_{i,x}.
\]

Every term in the second sum vanishes modulo `I`. This proves the exact row in CM.19, including all plus signs and the original factor `1/k`. If another division gives different `Q_{i,x}`, differentiating the equality of the two expressions for `Q_x` proves equality of the resulting rows. Thus both the conormal class and its derivative are independent of the division presentation.

Let `U(s)=∏_i v_h(s_i)` be the full original entire product, whose complete Taylor class is `U_k`. Mellin differentiation gives

\[
J^{(k)}\mathscr L_k\mathcal T_h^{(k)}Q_x
=[\delta(UQ_x)]_I,
\qquad \mathscr L_k=\frac1k\sum_i\log x_i.
\]

The product rule is `δ(UQ_x)=(δU)Q_x+UδQ_x`. Since `Q_x∈I`, the first term has zero full Hermite class. The second has class `U_k partial_I κ_N(x)`, exactly as displayed. There is no extra factor of `i`: the displayed operator is the original Mellin logarithmic multiplication. The factor of `i` occurs only when this same map is expressed as a derivative in the real spectral coordinate `u`, where `∂_u mathscr U_k=i mathscr U_k mathscr L_k`.

Every local multiplicity and every Taylor coefficient of `U` remains in this computation. No division by a globally nonvanishing analytic amplitude is used; only its already proved invertible finite Taylor class enters the algebraic conclusion.

## Exact kernels of the actual source maps

The repaired source now states the correct typed preimages:

\[
\ker\kappa_N=\{x\in C_\chi:Q_x\in I^2\},
\qquad
\ker(J^{(k)}\mathscr L_k\Delta_N)
=\kappa_N^{-1}(\ker\partial_I).
\]

The second equality uses invertibility of `U_k`. Equivalently it is the set of `x` for which `δQ_x∈I`, since membership of `Q_x` in `I` is automatic. The original Gram kernel is still the more restrictive explicitly specified set `ker E_N=ker Δ_N={x:Q_x=0}`. These are maps with different codomains, and the displayed composition and preimages give their exact relationship. A nonzero relation can have a zero conormal class, and a nonzero conormal class can lie in `ker partial_I`; neither possibility is implicitly excluded.

The split quotient and the linear conormal derivative retain the source support label and their respective supported zeros. The observed nonzero derivative is computed from the original retained relation before the quotient, exactly as the source NOTE sections 7 and 8 require.

## Final audit result

The revised CM.16–19 arguments pass this independent proof audit. The degree bound is proved in the original monic multivariate coordinates; both minima exist at the same cutoff; the Gram and control differences have the correct complete terms; the canonical difference has a unique original polynomial and a linear fixed-order conormal division; and its arithmetic derivative has exactly the full factor `U_k/k` and the stated signs. The typed conormal map and kernel-preimage repairs are present in the reviewed source. This audit makes no claim about the remaining CM sections or a degree-asymptotic bound.
