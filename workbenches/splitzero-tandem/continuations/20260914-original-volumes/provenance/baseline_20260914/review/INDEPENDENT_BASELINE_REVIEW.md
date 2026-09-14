# Independent mathematical acceptance of the original-packet baseline

Reviewed by `/root/baseline_final_review`, 14 September 2026. This review covers the complete new proof bodies BSL1–22 in `BASELINE_ORIGINAL_PACKET.tex` and HBL1–18 in `independent/HOMOGENEOUS_GAMMA_BASELINE.tex`. The corresponding receipt pins their exact bytes and all dependencies actually consulted. The review is mathematical; no PDF rendering, numerical experiment or formal verification is claimed.

**Decision: ACCEPT.** No mathematical correction is required in either new source. The leading positive coefficient applies to the canonical packet with `k=4l+1`, `e=1+k(m−1)` and `q=e(k+1)^2`, at fixed original `m,δ,γ` as `l→∞`. An independent source order `K=q+1` is not present in this proof and has not been inserted into its conclusions.

## 1. Exact source, relation and quotient maps: BSL1–5 and HBL1–8

For the original monic polynomial χ of degree q, the polynomial remainder map J_N is onto for N≥q−1 and has kernel exactly χP_(N−q). The displayed frame `(1,…,S^(q−1),χ,…,χS^(r−1))`, with r=N+1−q, is triangular with every diagonal coefficient equal to one. Consequently its squared determinant is one in the complex Hermitian Gram transformation. Its Schur complement is the minimum norm on the fixed remainder fibre. This proves det G_N = det H_N/det A_(χ,r), including the empty relation space r=0. Direct multiplication also verifies the inverse-kernel presentation `(J_N H_N^−1 J_N*)^−1` and the minimum section in BSL3.

For the homogeneous polynomial `(S−c)^q`, the translated monomial source and remainder frames are likewise related to the original frames by triangular matrices of determinant one. Evaluation on S=c+iy contributes the diagonal phases i^(q+j) to relation columns. These phases have squared modulus one. Thus HBL5 computes precisely the determinant of its own quotient; it does not identify the displaced and homogeneous remainder algebras.

The inherited monic norms are γ_j=√(2π)j!(1/2)_j=√(2π)(2j)!/4^j. The monic polynomials in the original S coordinate are i^j p_j((S−c)/i); their norms remain γ_j. The original source determinant is therefore the product of γ_j, with its mass retained. Substituting all four degrees q−1,q,2q−1,2q gives source coefficients −1 at q, −2 at q+1,…,2q−1, and −1 at 2q. The relation contribution has coefficients 0,−1,+1,+1 at ranks 0,1,q,q+1. These are exactly BSL4 and HBL7–8.

BSL5 gives the complete coefficient map T_(h,j)=binom(j,h)c^(j−h)i^h, which has |det T|=1. Hence its reference relation Gram is T* M_(q,r) T. The low reference determinant is μ_q, not one. At ranks q=2n and q+1, simultaneous even/odd row and column permutations produce H_n^(q)H_n^(q+1) and H_(n+1)^(q)H_n^(q+1). The vanished odd entries follow from the actual even density, and the two permutation determinants multiply to +1. All four factors of Z_q follow with their stated sizes.

## 2. Original-root comparison and full tails: BSL6–14

The threshold k≥2048√(δ²+γ²) and q≥k² imply |ζ_ab|/(qε)≤1/2, with ε=2^−10. Every bulk multiplier therefore has a bounded inverse on the two original compact intervals. In the convergent logarithm series the actual permutation `(a,b)↦(k−a,k−b)` cancels odd powers. The retained quadratic coefficient is

`e Re Σ ζ_ab²/(qz)² = k(k+2)(δ²−γ²)/(3qz²)`.

There is a factor two from log |χ|² and a denominator two from the second logarithm term; these cancel with the positive sign shown. The remaining even terms are bounded by `q Σ_(j≥2) t_ε^j/j ≤ qt_ε²/[2(1−t_ε)]`. Since δ²−γ²<0, the lower bulk bound uses ε^−2 and the upper bound uses 64^−2. Thus both b_− and b_+ have the correct signs and extrema.

The multiplier `χ(c+iy)/(iy)^q` intertwines the two specified maps from the same relation coefficient space into L²(B,dσ). Taking Hilbert Grams gives BSL8 on that space. No unstated comparison between quotient fibres is used. Multiplication by this bounded continuous multiplier and its inverse is justified at both closed bulk components, including their endpoints.

I checked the inherited full-vector tail proof at high ranks in CTR37–44 and BRD22–38, and the separate scalar proof LET10–16. The contour rotation gives `σ(y)≤C_U exp(−|y|)` with `C_U=Γ(1/4)²/(2π√cos 1)`. The reflection identity and the unrotated Euler bound give `σ(y)≥C_L exp(−π|y|)` with `C_L=π/Γ(3/4)²` and ratio C_U/C_L=(cos 1)^−1/2. The [1,2] bulk subsegment, full Jacobian dy=q dz and exact powers q^(2q+2s) are retained before comparison.

The Legendre coefficient estimate applies to every complex polynomial of degree r−1≤q at r=q,q+1. Its squared coefficient sum is bounded by r²8^(2q) on the inner segment, giving the exact κ_(I,r) used in BSL9. The far estimate integrates both tails with denominator q−D_s/64≥59q/64 and D_s≤5q, yielding the same κ_F. The polynomial threshold for f is inherited only where f occurs in the larger dependency; the χ-only forms in BSL have s=0. At scalar rank one, LET proves the positive integral estimate directly and does not invoke a high-rank projection argument outside its domain. Thus the BSL9 constants legitimately hold at all and only the required ranks 1,q,q+1.

For each positive bulk Gram, the full determinant is its bulk determinant multiplied by exp(t_H), where t_H is the stated positive log determinant. Both t_A and t_M lie in [0,L_r], so their difference belongs to [−L_r,L_r]. This explains why the error in BSL10 has one L_r on each side, rather than two; it is correct. The logarithm of the bulk determinant ratio lies in [r b_−,r b_+] after congruence. The interpolation formula BSL11 follows by determinant differentiation under a bounded integrand on a compact set. Its starting determinant is det M_(q,r) because the coefficient congruence has determinant modulus one.

Finally, summing η_q+η_(q+1)−η_1 gives exactly the lower value `(2q+1)b_−−b_+−(L_q+L_(q+1)+L_1)` and upper value `(2q+1)b_+−b_−+(L_q+L_(q+1)+L_1)`. In particular the low endpoint sign in BSL14 has been checked independently.

## 3. Homogeneous leading coefficient: HBL9–15 and BSL15–16

The factorial bounds from the monotone logarithm integral give `log γ_j=2j log j−2j+O(log q)` uniformly for q≤j≤2q. The two different endpoint sums each have q terms. Their integral errors are O(q log q), and the integrals of x and x log x over [1,2] are 3/2 and 2 log 2−3/4. Therefore their signed sum is exactly `−6q² log q+(9−8 log 2)q²+O(q log q)` to the claimed order.

For the literal Gamma determinant, the transformation t=q²x gives the unchanged source measure `dν(q²x)=B_q(x)dω(x)` and the exact power `q^(2as+2s(s−1))`. At (s,a)=(n,q),(n+1,q),(n,q+1),(n,q+1), these powers have exponents `(3/2)q²−q`, `(3/2)q²+3q`, `(3/2)q²`, `(3/2)q²`. Their sum is 6q²+2q. The sum of the four sizes squared, divided by q², tends to one. No n+1 correction or odd block has been dropped in obtaining the leading limit.

The moving α=a/s step is justified by convexity at three fixed exponents and the fixed-exponent GEL free-energy theorem. Both lower secant inequalities in HBL are in the correct direction; their small coefficients tend to zero while their fixed-point differences remain bounded. The upper bound followed by continuity gives the matching limsup. This does not differentiate an asymptotic error. The resulting energy is F(2,π), since q/s→2. The low μ_q has a positive constant lower bound and an upper bound 2C_U(2q)!, so log μ_q=O(q log q), as required.

The EIQ equilibrium at α=2,β=π has uK(κ)=2 and vE(κ)=4. Substituting β=π into its density coefficient β/(4π²x) gives exactly HBL14. The literal x↦r²x transport changes the functional by 6 log r−π(r−1)M. Maximization at r=1 proves πM=6. The equilibrium support identity then gives F=−ℓ/2−3+L, and evaluation at its right endpoint gives the one-dimensional formula HBL15 with the stated signs. Square-root endpoint behavior makes its endpoint logarithms integrable.

The original location errors satisfy |a_k|≤|δ²−γ²|/(3e) and d_χ≤2(δ²+γ²)²/(3e³k²ε⁴). Hence their combined determinant error is O(q/e), with exponentially small tails. Dividing by q² tends to zero on the canonical packet. This is the exact comparison that transfers the homogeneous coefficient to BSL16, rather than an identification of its source and target objects.

## 4. Strict positivity: HBL16–18

The arcsine competitor on [1,9] is a probability after the literal substitution x=5+4 cos θ. Its logarithmic energy is log 2: factoring the difference of cosines and joining the two half-angle integrals produces an interval of length π on which log |sin| has integral −π log 2, followed by the factor log 4. The single logarithmic moment is 2 log 2 from `5+4 cos θ=|2+exp(iθ)|²` and the absolutely convergent logarithm series. The square-root moment is `(6/π)E(√(8/9))`. The three integrals are finite, so this is an admitted competitor for the precise extended-energy supremum.

The competitor proves F(2,π)≥5 log 2−6E(√(8/9)), and therefore C_B≥9−3 log 2−6E(√(8/9)). The polynomial `P(z)=1−z/2−z²/8−z³/16` is positive on [0,1] and has `P(z)²−(1−z)=5z⁴/64+z⁵/64+z⁶/256≥0`. It is thus an upper bound for √(1−z). Integrating at z=(8/9)sin²t gives E≤265π/729. The displayed integral for 22/7−π is positive; the finite exponential sum at 7/10 is 12013/6000>2, so log 2<7/10. Consequently

`C_B ≥ 9−3 log 2−530π/243 > 9−21/10−11660/1701 = 769/17010 > 0`.

All coefficients and rational arithmetic in this bound were checked directly. No decimal evaluation of the equilibrium is used.

## 5. Full receiving maps and scales: BSL17–22

TWA26–30 retains the tensor-Gamma coefficient β_k and the actual polynomial f_l. Its multiplication map sends a remainder fibre bijectively to the specified product-jet fibre. All imaginary parts of χ-roots are nonzero because k is odd, whereas the roots of f_l are real, so the inverse Taylor multiplication used for this packet is valid. The four copies of q log β_k and of the full resultant determinant are present before their signed cancellation. TWA29–30 therefore gives B_0=B_σ+T_k with the positive sign in BSL18. The definition of δ_k^σ in TWA15 gives B_ar=B_σ+δ_k^σ, and subtraction gives Δ_Γ=δ_k^σ−T_k.

GEL19 supplies T_k/(lq)→C_Γ; TWA15 supplies δ_k^σ/(kq)→0 for the actual fixed packet. The exact degree q=e(k+1)² gives l/q→0 and k/q→0. Hence these two return terms are o(q²). The fixed original D_h>0 gives 4q log(D_hk)=o(q²). This proves all three limits in BSL19 with the same C_B; it does not equate the functions at finite k. The stated finite enclosures follow by adding their actual signed intervals to BSL14.

For the mixed receiver, Λ:E_χ→im Λ is onto, K=ker Λ, and `[I_K,S_*]` is invertible. Its Gram determinant is |det[I_K,S_*]|² det G_N; eliminating the kernel block gives exactly det(I_K*G_NI_K)det Q_N. The complete Schur factor and the original fixed frame therefore prove BSL20. At the four endpoints this same frame factor has total coefficient zero. BRU8–21 identifies the individual determinant ratios with the actual kernel and boundary row-contraction sums, including the asymmetric boundary denominator and all off-diagonal correlations. Thus BSL21 proves only their combined limit, which is exactly what its text states. Rank-zero and full-rank cases remain valid with the empty determinant convention.

Finally TWA5–10 has the exact identity `B_ar=4q log L_k−W_k^σ+S_k−τ_k^win`, with W_k^σ the explicit factorial window, distinct from the Gamma return W. This factorial window is O(q log q). TWA4–6 proves τ_k^win=O_h(k+log q). The exact polynomial formulas for q and L_k imply log q and log L_k are O(log k) at fixed packet. All three terms divided by q² tend to zero. Rearrangement therefore proves S_k/q²→C_B, with the signs in BSL22. No estimate on one individual contraction or phase is inferred from the combined sum.

## Scope retained by this acceptance

The q² leading coefficient and the previously proved kq Gamma difference coexist because k/q→0 on the actual packet. This review does not claim an o(q) free-energy error, an independently selected tensor order, an upper estimate annihilating the HC costs, or a resolution of RH. It certifies the complete new canonical baseline calculation and its actual original receiving maps. Any next construction must keep its own defined source, coefficient maps and degree identities. The reviewed proofs require no source changes.
