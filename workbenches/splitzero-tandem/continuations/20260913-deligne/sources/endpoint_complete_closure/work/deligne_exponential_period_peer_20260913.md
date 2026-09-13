# Independent review of the exponential-family quotient, connections, and periods

Review date: 13 September 2026. Reviewed source: `output/split_zero_rh_tandem_2026-09-12/sources/web_deligne_exponential_delivery/Tau_Deligne_Exponential_Comparison/NOTE.tex`, SHA-256 `919f4036a3b3e10fcef0b5bf1b1aff5c0e4fb4dfa311feea51d61ed7c546e9f2`.

## Scope and conclusion

I read Sections 5–9 completely, including the parameter connections, all of 6.1 and 6.2, the finite-field infinity chart, and the rank-one calibration. The first whole-file output had a small truncation; I then reread the complete relevant ranges in two bounded outputs. I also read `SOURCE_REVIEW.md` completely. This review verifies the new algebra, analytic convergence, period comparison, residue pairing, specialization maps, and the explicit local calculation at infinity. The parent independently verifies the inherited existence and domains of the maps `j_E`, `r_N`, and the actual Deligne source theorem and its hypotheses. No previously supplied checker was rerun, no existing source was edited, and no claim is made here to an independent rereading of all of Weil II.

The stated quotient and the fixed-nonzero-u period comparison are correct. The period proof handles nonproperness by fixed-contour tail estimates, which I give explicitly below. It does not require distinct critical points. I found no mathematical failure of the displayed statements within this scope. A small directional wording issue in Section 7 should be made index-exact: the residue Gram entry with indices a,b vanishes when a+b<q−1 and equals one when a+b=q−1; the phrase “below the first nonzero antidiagonal” can mean the opposite part of a displayed matrix.

I also prove a stronger exact determinant identity, including its comparison with the original arithmetic Gram determinants. The complete integration-ready TeX proof is `work/deligne_exponential_determinant_extension_20260913.tex`, equations XD1–XD26. It retains the full monomial Gamma-factor product and oriented complex determinant.

## 1. The polynomial-exponential quotient and arbitrary coefficient base change

Let D(P)=uP′+(χ−t)P, where χ is the original monic degree-q polynomial and q≥1. Over any coefficient algebra B obtained by base change, if P has degree a and nonzero highest coefficient b, D(P) has degree a+q and highest coefficient b. This remains true with zero divisors in B: the only degree-(a+q) contribution is the multiplication of b by the monic highest coefficient 1. Thus D is injective. Its image meets B[S] below degree q only at zero.

For a polynomial F of degree n≥q, subtract D(b S^(n−q)), with b the actual highest coefficient of F. Its degree strictly decreases. Repetition gives F=D(Q)+R with deg R<q; injectivity and the highest-degree argument make Q and R unique. The construction is B-linear because uniqueness compares the reductions of sums and scalar multiples. Hence the original presentation splits as coefficient modules, commutes with base change, has zero degree-zero cohomology, and has free degree-one cohomology with the stated q basis vectors. At u=t=0 its actual differential is multiplication by χ, so specialization is the literal cyclic quotient, including every repeated-root multiplicity.

Multiplication by S has commutator [D,M_S]=uI. In particular D(S)−S D(1)=u, and the image is not an ideal when u is invertible: ideal stability together with D(1),D(S) would put the nonzero class u[1] into zero. The exact alternative already provided in the note is its coefficient-module section and descending parameter connection; no missing ring structure is needed by the period proof.

## 2. Descending parameter connections and their signs

Direct application to a polynomial gives [D,∂t]=I and [D,−M_S/u]=−I. Their sum commutes with D, so ∇t=∂t−S/u acts on both terms as a chain endomorphism with the parameter Leibniz rule, and descends to the quotient. The only required reduction on the specified basis is S^q=t−∑c_a S^a, obtained from D(1). Thus the connection matrix is ∂t−A(t)/u with A(t)=A+t e_0 e_(q−1)^T, including q=1. Its regular scaled connection −u∇t has the stated reduction A(t), and then A at t=0.

For coefficient c_a, [D,∂_(c_a)]=−S^a and [D,S^(a+1)/((a+1)u)]=S^a. Thus ∂_(c_a)+S^(a+1)/((a+1)u) descends, with exactly the note's sign and denominator. The coefficient and t connections commute before passage to the quotient: the polynomial multiplication terms commute, and their cross-parameter derivatives vanish. Thus they are a flat connection in these parameter directions at fixed u≠0. The note does not assert that separate multiplication by every S power descends.

The source perturbation statements follow algebraically from the explicitly displayed inherited maps. Namely j_E(D+t r_N R j_E)=(A+tR)j_E and (D+t r_N R j_E)r_N−r_N(A+tR)=Dr_N−r_NA. The added term kills every original boundary in ker j_E. The metric variation is obtained by expanding A(t)^*G_N+G_NA(t)−kG_N, with original G_N held fixed. This review checks those substitutions; the parent's inherited-map audit supplies existence and domains.

## 3. Fixed-ray convergence, parameter differentiation, and boundary cancellation

Fix u≠0 and the one argument and oriented rays of (36a). Put d=q+1. For a compact parameter set K define

M_K = ∑_(a=0)^(q−1) sup_K|c_a|/(a+1) + sup_K|t|,
R_K = max(1,2dM_K), and α=1/(2d|u|).

The actual leading exponent on every ray is −r^d/(d|u|). For r≥1 the sum of the absolute values of all lower terms is at most M_K r^(d−1)/|u|. Therefore for r≥R_K the real part of the full exponent is at most −αr^d, uniformly on K and on every ray. A fixed number of parameter derivatives multiplies the integrand by a polynomial in S, with precisely the factors S^(a+1)/((a+1)u) and −S/u. Its tail is bounded by C r^L exp(−αr^d), with C,L fixed on K. The exact integrable majorant is given by

∫_0^∞ r^L exp(−αr^d) dr = α^(−(L+1)/d) Γ((L+1)/d)/d.

The finite interval is controlled by continuity. This proves absolute convergence, locally uniform convergence in all coefficient parameters, entire parameter dependence, and differentiation under the integrals at every finite order. It also proves that exp(Φ_t/u)P tends to zero at infinity on each ray for every polynomial P.

On an outward ray, the integral of d(exp(Φ_t/u)P) is −P(0), because Φ_t(0)=0. In Γ_j=−ℓ_0+ℓ_j the endpoint contributions are +P(0) and −P(0), so they cancel exactly. Thus periods annihilate the actual image of D. This proof uses no improper exchange of a parameter derivative and an unbounded integral, and no choice of critical-point thimbles. The straight coefficient path used subsequently is contained in a compact parameter set, so the same tail estimate applies throughout it.

## 4. The monomial matrix and continuation across repeated roots

For the monomial potential, substitute x=r^d/(d|u|) in each individual oriented ray integral. For 1≤l≤q, the factor is a_l=(d|u|)^(l/d) Γ(l/d)/d and the oriented phase is exp(ilθ_0)(ζ^(jl)−1), where ζ=exp(2πi/d). These are precisely all the factors in (36f).

For the matrix V_(jl)=ζ^(jl)−1, add the j=0 summand, which is zero. The finite root-of-unity sums give (V*V)_(lm)=dδ_(lm)+d. The rank-one all-ones matrix has eigenvalues q and zero, so det(V*V)=d^q(1+q)=d^d. This also proves nonsingularity when q=1. Hence

|det Π_mon|² = d^d ∏_(l=1)^q [(d|u|)^(l/d) Γ(l/d)/d]².

Parameter differentiation of the periods is justified by Section 3 above and gives Π′=ΠB along the fixed-ray coefficient path. The adjugate identity differentiates det Π without assuming Π is invertible. Thus det Π satisfies a scalar first-order equation and cannot vanish when its initial value is nonzero. Coincident critical points create neither a contour discontinuity nor a singularity of the coefficient matrices. The quotient-to-period map and the stated inverse therefore hold on every fibre with this fixed u≠0.

## 5. A root-free closed determinant formula

For 1≤m≤q and 0≤b<q perform ordinary monic division S^(m+b)=(χ−t)Q_(m,b)+R_(m,b), deg R<q. Then deg Q≤q−1, and twisted reduction is exactly R_(m,b)−u Q′_(m,b). Its correction has degree at most m+b−q−1≤b−1, so it contributes zero to diagonal entry b. Consequently the trace of the full twisted-reduction multiplication matrix for S^m equals Tr A(t)^m, while retaining the nonzero off-diagonal correction matrix.

Define F(c,t)=Tr Φ_t(A(t)), with the original primitive and all coefficients and denominators retained. The trace product rule dTr A^n=nTr(A^(n−1)dA), valid without diagonalization, gives

dF = ∑ Tr A(t)^(a+1) dc_a/(a+1) −Tr A(t) dt + Tr((χ(A(t))−tI)dA(t)).

The last term is exactly zero because χ(A(t))−tI=0 on the actual cyclic quotient. The first two terms are u times the connection-matrix trace one-form. The adjugate scalar ODE therefore integrates to

det Π(u,c,t)=det Π_mon(u) exp(F(c,t)/u).

This is valid with arbitrary repeated roots, and its proof never chooses roots, eigenvectors, or a semisimple decomposition. Its real-positive determinant consequence is

det(Π*Π)=|det Π_mon(u)|² exp(2 Re(F(c,t)/u)).

For the original arithmetic Gram G_N and V_N=det G_N, the exact comparison B_N=G_N^−1 Π*Π is G_N-positive and self-adjoint. Therefore

log det B_N = log |det Π_mon(u)|² + 2 Re(F(c,t)/u) − log V_N.

Taking the difference for the same u,c,t and two admitted degrees preserves exactly log(V_i/V_j). The complete typed source maps and proof are XD22–XD26 in the accompanying TeX. The identity explicitly computes the common singular exponential factor while retaining the original endpoint quantity; it supplies no new upper bound on that endpoint quantity.

## 6. Residue pairing, dual connection, and trace contraction

Use indices a,b from 0 to q−1. In the Laurent expansion of S^(a+b)/(χ−t), the coefficient of S^−1 vanishes for a+b<q−1 and equals 1 when a+b=q−1. Reversing the column order therefore gives a triangular matrix with diagonal entries 1; reversing q columns has sign (−1)^(q(q−1)/2). This proves the stated determinant without ambiguity about which side of the antidiagonal is meant.

The difference 1/(χ−t)−1/χ=t/(χ(χ−t)), multiplied by any two degree-below-q representatives, has order at most S^−2 at infinity. Its S^−1 coefficient is zero, so the pairing matrix is independent of t, as claimed. It can depend on the coefficients c_a; the word “constant” here is correctly read in the stated t direction. Multiplication by S on the ordinary quotient by χ−t is self-adjoint for this bilinear residue pairing, so A(t)^T S=S A(t). Substitution then verifies the duality between ∂t−A(t)/u and ∂t+A(t)/u exactly. This is the displayed t-horizontal duality; the note need not assert a coefficient-independent pairing in every parameter direction.

For an arbitrary polynomial f and v modulo χ, the residue of f v χ′/χ at a root λ of multiplicity ℓ_λ is ℓ_λ f(λ)v(λ), because χ′/χ=ℓ_λ/(S−λ)+a holomorphic function. In the local factor C[S]/((S−λ)^ℓ_λ), multiplication by f v is triangular in the ordered powers of S−λ with that same value on every diagonal entry. Its trace is therefore ℓ_λ f(λ)v(λ). Summing gives the full identity (42), including all nilpotent multiplicities. Substitution of the inherited antilinear reflection f↦f^(dagger_k) preserves this calculation. No trace of a larger tensor packet is substituted.

## 7. Split specialization and the derivative response

The exact specialization homomorphism C[u,t]→C sends represented u and t to represented scalar zero and preserves the external absence symbol under G. In the underlying coefficient complex, the specialized differential is multiplication by χ, so any relation differing by D(P) has the same image in C[S]/χ. This proves well-definedness of (44) on the supported quotient classes.

The family equality [χP]=t[P]−u[P′] is simply the zero class of D(P), with its two signs retained. The original derivative response is instead the literal polynomial identity ∂S(χP)=χ′P+χP′ followed by quotient modulo χ. This proves the displayed conormal map and its χ′ contribution, and connects it to the residue trace contraction without replacing the original relation-power tower by the parameter u.

## 8. The finite-field infinity chart and nonproper family issue

At a specified map of the original finitely generated coefficient ring to F_Q with p>d=q+1, all denominators retained in Φ are defined, the leading coefficient 1/(du) is a unit on u≠0, and degree is exactly d. In one variable the highest homogeneous term has no zero in P^0, so its projective zero locus is the empty smooth scheme. These are the note's direct hypotheses for the cited exponential-cohomology theorem.

Write w=1/S and b(w,u,t) exactly as in (47a). On the open b≠0 adjoin v with b v^d=1. The v derivative d b v^(d−1) has inverse v/d. Thus this is a finite étale cover of the chosen open chart. Over the boundary w=0, v is a unit and d(wv)/dw=v, so after a further open restriction the map x=w v is a relative étale coordinate over the parameter base. Since v^−d=b, x^−d=w^−d b equals the original entire potential divided by u. The μ_d action v↦ζv, x↦ζx preserves x^−d, so the cover and its descent action are retained.

This gives an actual local chart at every boundary point in which the exponential eigensheaf on x≠0 is the pullback of the fixed one-variable model L_ψ(x^−d), with the parameter direction a product. Thus the nonproper affine projection has a concrete boundary control after compactification by P^1, rather than an unsupported inference of lissity from fibre dimensions. Passing from this chart to the cited lissity theorem uses local acyclicity and the proper compactification argument; the parent separately verifies the exact cited Deligne passages. Nothing here provides a chart through u=0 or equates finite-field Frobenius with the characteristic-zero coefficient A.

## 9. Rank-one orientation check

For q=1 and χ=S−λ, the ray-difference contour for real u>0 is oriented from +i∞ to −i∞. The contour in (36m) is explicitly the opposite orientation. On that latter contour put S=iy to obtain i∫ exp(−y²/(2u)−i(λ+t)y/u)dy. Differentiating in h=λ+t and integrating the y derivative proves that this integral satisfies J′(h)=−hJ(h)/u; J(0)=i√(2πu). Therefore J(h)=i√(2πu)exp(−h²/(2u)), first for real h and then for all complex h by entire continuation justified by the Gaussian majorant. The displayed logarithmic derivative, real-parameter metric, and orientation sign are correct. This agrees with XD19 because F=Φ_t(A(t))=−(λ+t)²/2.

## Reproducibility and limits

This is an independent analytical and algebraic review, not a numerical experiment or a replay certificate. The raw NOTE remains untouched. The additional TeX contains the full new determinant proof and the strengthened fixed-ray estimates. No Lean, PDF build, global artifact edit, or remote mutation was performed in this review lane.
