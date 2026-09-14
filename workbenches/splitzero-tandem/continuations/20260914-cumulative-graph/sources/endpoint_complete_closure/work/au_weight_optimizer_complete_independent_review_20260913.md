# Complete independent proof review of the arithmetic determinant weight optimizer

The complete source `au_weight_optimizer_20260913.tex` was first read at SHA256 `4406cc2b12b4be184033c949e89ebe33be1a1de7e1569356a4eeb357bf9d5f54`, containing OW.1–OW.29 and OW.22a. Every displayed formula and its proof was examined, including the exact cofactor signs, boundary and interior cases, the exceptional segment, both scalar constructions, rational certificates and the original arithmetic quotient. No defect was found in those claims for their explicitly defined weight family. The stronger shared-moment estimate found during this independent review, and its complete exact-moment optimization, are proved below with their original constants and coordinate maps.

This review is mathematical source review. It does not execute the author's solver, mathematical fixture suite, compiler or renderer. The arithmetic-volume author owns those executions and their receipts. No sealed AU source, RF source or global reader file is edited by this review.

## The original source, polynomial chart and quotient coordinates

Retain k≥3 for the analytic comparison, c=k/2, g=2ξ, the same complete monic packet h, w_h(t)=|(g/h)(1/2+it)|²/(2π), m_k=w_h^{*k}, and μ_h=∫w_h. Its mass is ∫m_k=μ_h^k. The original polynomial chart is ΨP(u)=P(c+iu), with inverse f↦f((S−c)/i). It is a complex algebra isomorphism. Its source norm is exactly ∫|ΨP(u)|²m_k(u)du, using the unchanged density and its literal mass.

For the degree-q monic χ, define ψ=i^(−q)Ψχ. Taylor expansion at c gives ψ_j=i^(j−q)χ^(j)(c)/j! and ψ_q=1. Thus every coefficient phase and derivative factorial in OW.2 is correct. The operator equation Ψ(SP)=(c+iu)ΨP proves the original multiplication-by-S correspondence. At ζ=(λ−c)/i, the d-th raw derivative is (ΨP)^(d)(ζ)=i^dP^(d)(λ).

The coordinate map on coefficient columns of degree less than r is the upper triangular matrix L_r with entry `(L_r)_(n,j)=binom(j,n)c^(j−n)i^n` for 0≤n≤j<r, and zero below that range. Its diagonal entries are i^j, so det L_r=i^(r(r−1)/2) and |det L_r|=1. Denoting the u-chart and S-chart source Grams by H_u,H_S, one has H_S=L_(N+1)^*H_uL_(N+1). The monic remainder maps satisfy J_uL_(N+1)=L_qJ_S: division by χ and division by ψ give the same residue after applying Ψ, since Ψχ=i^qψ generates the same ideal as ψ. This proves the exact quotient-coordinate map rather than merely comparing its dimensions.

For a full-rank quotient map J and positive definite source Gram H, G=(JH^−1J^*)^−1 is the quotient Gram. Indeed x has the lift v=H^−1J^*Gx, for which Jv=x. For any w∈ker J, v^*Hw=x^*GJw=0. Every other lift v+w therefore has squared norm v^*Hv+w^*Hw, whose minimum is x^*Gx. Applying the invertible chart gives G_S=L_q^*G_uL_q and det G_S=det G_u. Thus the quotient volume is literally preserved by this proved chart, while the full phase matrix remains in its coordinate map.

## All signed cofactors and raw multiplicities: OW.3–OW.7

Let the distinct roots ζ_a retain their given order and complete lengths ℓ_a, with Σℓ_a=q≥1. The row `(a,d)` of E_N evaluates the raw d-th derivative, hence its entry in column j is j!ζ_a^(j−d)/(j−d)! for j≥d and zero otherwise. A polynomial has those complete jets zero precisely when it is divisible by every (u−ζ_a)^ℓ_a, equivalently by ψ, since the distinct factors are coprime. For N=q−1 no nonzero such polynomial exists, so Z=E_(q−1) is invertible. For N=q the kernel is one-dimensional and contains the literal monic coefficient column (ψ_0,…,ψ_q)^T.

Write Δ_j for the determinant retaining all columns except j in increasing order. Appending any row of E_q as its last row gives a zero determinant. Its cofactor expansion has signs (−1)^(q+j); removing the common factor (−1)^q proves that the column ((−1)^jΔ_j)_j is in the kernel. It is a multiple of the coefficient column. Its last coordinate is (−1)^q det Z, so every cofactor is exactly Δ_j=(−1)^(q−j)ψ_j det Z. A zero ψ_j therefore gives a zero minor without changing the number or order of columns or jets.

For the confluent determinant, temporarily separate the nodes within each prescribed cluster and take the ordinary Vandermonde determinant in the same row order. Successive divided differences in each cluster divide out precisely its within-cluster Vandermonde factors. The polynomial Taylor expansion shows that the limiting row of order d is the raw derivative row divided by d!. Multiplying by d! restores the original raw row. The remaining cross-cluster factors are (ζ_(a')−ζ_a)^(ℓ_aℓ_(a')) in the retained order. Therefore det Z equals the product of all d!, 0≤d<ℓ_a, times those ordered cross-cluster factors. This is also a polynomial identity after the stated cancellation, so no approximation of the arithmetic source is used.

A complete complex repeated-root check is ψ(u)=(u−(1+i))²(u−2)=u³−(4+2i)u²+(4+6i)u−4i, with the length-two root first. The raw determinant is (2−(1+i))²=−2i. The four minors in increasing omitted-column order are `(8,12−8i,4−8i,−2i)`. Their alternating column is `(8,−12+8i,4−8i,2i)=2i(−4i,4+6i,−4−2i,1)`. Thus the factor (−1)^q det Z=2i and all cofactor signs are retained in a genuinely complex, non-simple-root example.

Fix the original 0<b<π/2 and β_j=b^(2j)/(2j)!. With M_k=M_h(b)^k+M_h(−b)^k, all these β_j are positive. Cauchy–Binet expands det(E_q diag(τ_jβ_j)E_q^*) into the sum over the q-column sets, each with its retained minor, conjugate minor and diagonal product. Substituting the signed identity gives

`det A_q(τ)=|det Z|² Σ_(j=0)^q |ψ_j|² (∏_(l≠j)β_l)(∏_(l≠j)τ_l)`.

Thus a_j=|ψ_j|²∏_(l≠j)β_l=B_βη_j, with B_β=∏_(l=0)^qβ_l and η_j=|ψ_j|²/β_j. The Taylor coefficient formula gives exactly η_j=(2j)!|χ^(j)(c)|²/((j!)²b^(2j)); in particular η_q=(2q)!b^(−2q)>0. The signed cofactors have been proved before taking their squared moduli.

For the positive auxiliary cone, τ↦(s,t), s=Στ_j and t_j=τ_j/s, has inverse τ_j=st_j. Every determinant monomial has exactly q factors, so its value acquires s^q. This cancels the q log s in the original estimate. The map concerns auxiliary coefficients only; its domain and inverse do not change either source measure or quotient norm. Multiplying all a_j by B_β multiplies D_a and its maximum by B_β and leaves the maximizing auxiliary weights unchanged.

## Determinant concavity and every boundary case: OW.8–OW.13

For nonnegative a_0,…,a_q with a_q>0, define D_a(τ)=Σa_j∏_(l≠j)τ_l on the closed simplex τ_j≥0, Στ_j=1. Its continuous polynomial has a maximum on that compact set. Equal weights have positive value, so every maximizer has positive objective. Put I={j:a_j>0}, p=|I|, A=max a_j and S_a=Σa_j.

With v_i=√(a_i/a_q), i<q, the exact polynomial identity is D_a=a_q det M, where M=diag(τ_0,…,τ_(q−1))+τ_qvv^*. Rank-one expansion proves this at positive first q coordinates; polynomial identity extends it to the closed simplex. The matrix is positive semidefinite there. Its determinant is positive exactly when it is positive definite.

Along a real affine matrix line M+tE through the positive definite cone, differentiating M^−1M=I gives (M^−1)'=−M^−1EM^−1. The determinant derivative and trace identity give `(log det M)'=Tr(M^−1E)` and `(log det M)''=−Tr((M^−1/2 E M^−1/2)²)`. The latter Hermitian matrix has real eigenvalues, so equality occurs precisely when E=0. When p≥3, v has two nonzero components. A zero matrix increment forces the τ_q increment to be zero from the corresponding off-diagonal entry, then every other increment is zero from the diagonal. Hence log D_a is strictly concave on its convex positive-objective domain, which proves uniqueness of its positive maximum in this case.

A simplex point with at least two zero coordinates has D_a=0, because each monomial omits only one coordinate. At a positive boundary maximum exactly one coordinate τ_j vanishes, and a_j>0. The objective there is a_j∏_(i≠j)τ_i. Concavity of log x gives the product bound q^(−q), with equality precisely when every remaining coordinate is 1/q. Thus every positive boundary maximum must have τ_j=0 and τ_i=1/q for i≠j. Its gradient has active entries a_j/q^(q−1) and inactive entry (S_a−a_j)/q^(q−1).

The feasible path τ_j=ε, τ_i=(1−ε)/q has derivative (S_a−2a_j)/q^(q−1). It excludes this candidate when 2a_j<S_a. Conversely, when 2a_j≥S_a the inactive gradient is no larger than the active ones. Its scalar product with every feasible displacement is nonpositive. The supporting inequality for the concave log D_a therefore proves global maximality. This derivative is valid at the boundary because the candidate matrix is positive definite and remains so in a neighborhood. The value is a_j/q^q; its index must maximize the coefficient.

For p≥3 strict concavity makes this boundary maximizer unique, including the equality 2A=S_a. If 2A<S_a, every possible positive boundary maximum is excluded; compactness then gives an interior maximum, and strict concavity makes it unique.

For p=1 the objective is A times the product of the q complementary coordinates. Increasing their total mass increases the product, so the positive coefficient's own coordinate is zero, and the q others equal 1/q. This is the unique maximum. For p=2, with positive coefficients at j,l, the exact factorization is `(∏_(i≠j,l)τ_i)(a_jτ_l+a_lτ_j)`. At a fixed sum r=τ_j+τ_l, unequal coefficients maximize their linear factor only by assigning r to the complementary variable of the larger coefficient. Equality of the remaining q product factors then gives the unique boundary maximum. If a_j=a_l=A, the factor is Ar; the q factors r and the other q−1 coordinates have sum one. Their unique equal-product condition is r=1/q and every other coordinate 1/q, while the split between τ_j and τ_l remains arbitrary. This proves exactly the stated segment of maximizers.

The same exception is visible through the determinant map. With only a_q and a_j positive, a zero matrix increment has h_j=−(a_j/a_q)h_q and all other h_i=0. The simplex constraint is (1−a_j/a_q)h_q=0. Thus its only possible nonzero flat direction on the simplex occurs when the two coefficients are equal, and that direction changes their two weights by opposite amounts. The exact factorization identifies its full maximizing segment.

For q=1 the polynomial is a_0τ_1+a_1τ_0. It has value max(a_0,a_1), with the single complementary endpoint if they are unequal and the entire interval if equal. This handles the low-degree exception without applying a higher-dimensional uniqueness argument.

Finally, the determinant representation is related exactly to the original phase data. Monic remainder gives E_q=Z[I_q,−ψ_<q]. Writing B_0=diag(β_0,…,β_(q−1)) and z_i=−ψ_i√(β_q/β_i) yields A_q=ZB_0^(1/2)(diag(τ_<q)+τ_qzz^*)B_0^(1/2)Z^*. Here |z_i|²=η_i/η_q. The unitary diagonal entries U_ii=−ψ_i/|ψ_i| at nonzero coefficients, and U_ii=1 at zeros, give z=Uv exactly. Since diagonal τ commutes with U, the central matrix equals UMU^*. This proves the full congruence with every original coefficient phase retained.

## Interior stationarity, both scalar branches and the complete value

Assume q≥2 and 2A<S_a. With every τ_i>0 put P=∏τ_i and S=Σa_i/τ_i, so D_a=PS. Direct differentiation gives ∂_iD_a=P(S/τ_i−a_i/τ_i²). Euler's degree-q identity Στ_i∂_iD_a=qD_a determines the Lagrange multiplier, hence stationarity is exactly a_i=Sτ_i(1−qτ_i). At a_i=0 this forces τ_i=1/q. At a_i>0 it forces 0<τ_i<1/q.

Define y_i=1−qτ_i at positive coefficients. Then 0<y_i<1 and Σ_(i∈I)y_i=1: there are q+1−p zero-coefficient coordinates, each with weight 1/q. With c_*=S/q, the equations become a_i=c_*y_i(1−y_i). Conversely, any such positive y with sum one defines the original simplex weights τ_i=(1−y_i)/q on I and 1/q elsewhere; computing Σa_i/τ_i gives qc_* and verifies the original stationarity equations. Concavity proves global maximality, and uniqueness has already been proved.

Put t=4/c_*. Every quadratic equation requires 0<t≤1/A. Its smaller root is f_i(t)=(1−√(1−a_it))/2=a_it/[2(1+√(1−a_it))]. The rationalized expression has the same value at zero and no vanishing denominator. Each f_i increases continuously and strictly from zero to a value at most one-half. Let F=Σf_i.

If F(1/A)≥1, the intermediate value theorem and strict increase give exactly one t_*∈(0,1/A] with F(t_*)=1. Choosing every y_i=f_i(t_*) solves the full equations. If any solution has y_j>1/2, then every other y_i is strictly less than 1−y_j, because p≥3 supplies at least two other positive terms. The function x(1−x) is strictly increasing on (0,1/2), so a_j is strictly greater than every other coefficient. Thus a large root can occur only at the unique maximum A.

For that unique index j, the sum equation is Σ_(i≠j)f_i(t)=f_j(t). Division by f_j(t)>0 and the rationalized roots gives exactly H(t)=Σ_(i≠j)(a_i/A)(1+√(1−At))/(1+√(1−a_it))=1. For a_i<A, its logarithmic derivative is `[(1−a_it)^(-1/2)−(1−At)^(-1/2)]/(2t)<0`. Hence H strictly decreases on (0,1/A). Its endpoint values are H(0)=(S_a−A)/A>1 and H(1/A)=2F(1/A)−1.

If F(1/A)<1, two maximal coefficients would already contribute one to F, with the other positive terms increasing it further; the maximal index is therefore unique. The endpoint inequalities give the unique root of H in (0,1/A), and choosing y_j=1−f_j(t_*), y_i=f_i(t_*) otherwise gives a valid solution. If F(1/A)≥1, H has no root in the open interval, since its decreasing endpoint value is at least one. At equality, the maximal quadratic root is exactly one-half and the two descriptions meet at the already included smaller-root endpoint. These arguments prove existence, uniqueness and completeness of both branches.

There are q+1 original weight coordinates, so P=q^(−(q+1))∏_(i∈I)(1−y_i), including every zero coefficient's 1/q factor. Since S=qc_*=4q/t_*, multiplication gives d(a)=4∏_(i∈I)(1−y_i)/(q^qt_*), exactly as stated.

## Explicit zero-index reduction and rational three-coefficient solution

For p≥2 and z=q+1−p>0, put s=Σ_(i∈I)τ_i and τ_i=sσ_i on I. The exact factorization is D_a=(∏_(i∉I)τ_i)s^(p−1)D_(a|I)(σ). For a fixed s, the omitted-index product is at most ((1−s)/z)^z, with equality at equal omitted-index coordinates. The logarithmic derivative of (1−s)^zs^(p−1) vanishes only at s=(p−1)/q; its second derivative is strictly negative. Its endpoints give zero. Thus every maximum has τ_i=1/q at the zero coefficients, and the positive-index weights are exactly ((p−1)/q)σ_i. Its value is d(a)=(p−1)^(p−1)d_(p−1)(a|I)/q^q. At z=0, p−1=q and this factor is one. The p=1 case remains the separately proved boundary formula. This supplies the complete forward and inverse positive-index maps with the original q retained.

For three positive coefficients a,b,d satisfying all strict triangle inequalities, let Δ=2ab+2ad+2bd−a²−b²−d². The identity Δ=4ab−(a+b−d)² and 0<a+b−d<2min(a,b)≤2√(ab) prove Δ>0. The three positive-index weights σ_a=a(b+d−a)/Δ and its cyclic counterparts are positive and sum to one. For the quadratic objective aσ_bσ_d+bσ_aσ_d+dσ_aσ_b, each gradient equals 2abd/Δ; for example its a-coordinate is bσ_d+dσ_b=bd[(a+b−d)+(a+d−b)]/Δ. Euler's identity then gives value abd/Δ. Concavity proves maximality. The exact zero-index map gives τ_a=2a(b+d−a)/(qΔ) and its cyclic counterparts, and d(a)=4abd/(q^qΔ).

Several exact examples test the classification without numerical optimization. For q=3 and a=(7,2,1,1), the unique maximizer is (0,1/3,1/3,1/3), value 7/27; its inactive gradient is 4/9 and its active gradients 7/9. For a=(4,2,1,1), the same point has value 4/27 and all four gradients 4/9, but strict determinant concavity still makes it unique. For a=(0,5,0,5), the complete maximizing segment is τ_0=τ_2=1/3, τ_1+τ_3=1/3, with value 5/27.

For q=3 and a=(3,4,0,4), the all-small solution is τ=(10/39,8/39,1/3,8/39), y=(3/13,5/13,5/13) on the positive indices, c_*=169/10 and t_*=40/169. The square roots are respectively 7/13,3/13,3/13, so the smaller roots sum exactly to one. Its value is 64/351. For a=(4,3,0,3), the endpoint case has τ=(1/6,1/4,1/3,1/4), positive-index y=(1/2,1/4,1/4), t_*=1/4=1/A and value 1/6. For a=(19,10,0,10), the one-large solution is τ=(2/63,20/63,1/3,20/63), y=(19/21,1/21,1/21), c_*=441/2 and t_*=8/441; the smaller roots are 2/21,1/21,1/21, so H=1 exactly. Its value is 400/567. The endpoint sum in this case is 3/2−3/√19<1, while 19<10+10 proves it is an interior case. These examples retain the original fourth coordinate at a zero coefficient and test both scalar branches and their meeting point.

## Certified evaluation, equality handling and exact gain

For each monomial ∏_(l≠j)τ_l on the simplex, its q factors have total sum at most one, so their product is at most q^(−q). Therefore |D_a(τ)−D_ahat(τ)|≤q^(−q)Σ|a_j−ahat_j|. Evaluating this at a maximizing point for each list in turn proves the same bound for |d(a)−d(ahat)|. Each monomial is nonnegative, so d is coefficientwise monotone. Rational nonnegative coefficient boxes consequently enclose the value with width at most q^(−q) times their total coordinate width. An all-zero list has value zero. Any positive reference index can be placed last by a simultaneous permutation of coefficient and simplex coordinates, whose inverse restores the original ordering.

At a simplex candidate τ with D=D_a(τ)>0, let g_i=∂_iD_a and h=max_i g_i−qD. Euler's identity makes qD a convex combination of the g_i, so h≥0. For any positive-objective σ, concavity gives log D_a(σ)≤log D+g·(σ−τ)/D≤log D+h/D. Hence D≤d(a)≤D exp(h/D). If h<D, the power-series inequality exp x≤1/(1−x) for 0≤x<1 gives the rational upper certificate D²/(D−h). The argument holds at a boundary candidate because D>0 is exactly positive definiteness of its determinant representation. At every maximum, the active gradients equal qD and inactive gradients are no larger, so h=0.

For example, q=2 and a=(4,3,3), the equal-weight candidate has D=10/9, gradient (2,7/3,7/3), and h=1/9. Its exact rational certificate is [10/9,100/81]. The rational optimizer has value 9/8, which lies in that interval because 80≤81 and 729≤800 after cross multiplication. This checks the nonstationary gradient certificate as well as its zero-gap case.

Rational square-root brackets are obtained by squaring their nonnegative endpoints. Strict branch and trial comparisons are eventually determined as the brackets shrink. If the endpoint comparison remains equal, the smaller-root endpoint candidates converge to the proved endpoint optimizer. If a scalar trial is an exact root, its radical candidates converge to that optimizer instead of requiring an equality oracle. Positive auxiliary weights are mapped to the exact simplex by dividing by their positive sum, or by keeping zero-coefficient weights exactly 1/q and applying the proved positive-index map to the remaining budget. In a strict branch, the monotone scalar bracketing converges to the unique root; in an unresolved exact equality case, repeated radical refinement converges to its corresponding maximizing candidate.

At any of these limiting maximizers, D>0 and h=0. Both D and h are continuous polynomial/maximum functions of the candidate. Therefore eventually h<D and the rational width D²/(D−h)−D=Dh/(D−h) becomes smaller than any prescribed positive rational tolerance. Every returned interval is justified by its exact candidate and gradient, independently of any proposed numerical branch. The author's finite solver has an explicit round cap and reports failure if exhausted; this implementation limit does not replace the mathematical convergence argument or assert that a fixed cap works at every tolerance.

At equal weights D_eq=S_a/(q+1)^q. The monomial bound gives d(a)≤S_a/q^q and equal weights give the lower bound. Equality at the upper bound requires every term with a positive coefficient to attain its monomial maximum. The term omitting j attains this only at τ_j=0 and τ_i=1/q otherwise. Two distinct positive terms cannot have that same point, so upper equality holds exactly for one positive coefficient. If equal weights maximize, their interior gradient entries `(q+1)^(−(q−1))(S_a−a_i)` must all agree, so every coefficient is equal. Conversely equal coefficients give stationary equal weights, and determinant concavity proves maximality (or the direct constant linear polynomial for q=1).

Consequently the gain g(a)=log(d(a)/D_eq) satisfies 0≤g(a)≤q log(1+1/q)<1, with exactly those equality cases for the non-strict bounds. The final strict inequality follows from log(1+x)=∫_0^x(1+t)^−1dt<x for x>0. Testing the best boundary point gives g(a)≥max{0,q log(1+1/q)+log(A/S_a)}, and its second expression is the exact gain in the boundary regime. Testing equal positive-index weights in the exact reduction gives the additional lower bound q log(1+1/q)+(p−1)log((p−1)/p), with all original zero indices retained.

## The original arithmetic determinant bound and its precise scope

The positive comparison measure is the unchanged ν_k with density c_hϑ_h^(k−3)e^(−α(k−3))e^(−α|u|)(k−2+|u|)^(−B), where α=π/2 and B=42+2deg h, and ν_k≤m_kdu. The sealed arithmetic construction supplies this inequality and its positive constants. All finite polynomial moments exist. The positive almost-everywhere densities imply that every nonzero polynomial has positive squared norm, so the finite source Grams are positive definite. Their order is H_N^ν≤H_N; conjugating by H_N^−1/2 and inverting positive eigenvalues proves (H_N^ν)^−1≥H_N^−1, hence K_N^(ν,raw)≥K_N^raw after the same raw-jet map.

The already proved quotient formula and E_N=ZJ_N give det K_N^raw=|det Z|²/V_N, and the same identity holds for ν with its own literal mass. Weighted Cauchy–Schwarz at positive simplex τ gives H_q≤M_k diag(1/(τ_jβ_j)) from the separate moment inequalities ∫u^(2j)m_k≤M_k/β_j. Inverting and taking raw jets yields K_q^raw≥M_k^−1A_q(τ). Meanwhile K_(2q−1)^raw≤K_(2q−1)^(ν,raw). Taking determinants yields exactly OW.26 for C_k=log(V_q/V_(2q−1)). For q=1 both degrees are one, so C_k=0 and the same inequalities remain valid.

A boundary optimizer has positive determinant. Its convex mixtures with equal weights are positive simplex points; their raw matrices converge to the boundary matrix. Passing to the limit in their quadratic-form inequalities proves the same lower bound on the dual raw kernel. This uses no reciprocal of a zero boundary weight. Substituting det A_q=|det Z|²B_βd(η) then cancels the common raw determinant with K_(2q−1)^(ν,raw), giving U_opt=q log M_k−log B_β−log d(η)−log V_(2q−1)^ν. All source and comparison masses remain in their original factors.

For the stated source/relation determinant formula, the coefficient matrix with quotient monomials first and ψ times the relation monomials second is triangular with all diagonal entries one. Its determinant is one. In that basis the Schur complement of the relation Gram is precisely the least-lift quotient Gram proved above, so det H_(2q−1)^ν divided by det(B_(2q−1)^*H_(2q−1)^νB_(2q−1)) equals V_(2q−1)^ν. This retains the complete degree range and the same monic ψ.

Subtracting the equal-weight version gives U_eq−U_opt=g(η), so the improvement within this particular separate-moment family is absolutely less than one. For the complete quartet, the full root list is stable under u↦−u with each multiplicity retained, so monicity gives ψ(−u)=(−1)^qψ(u). At least one coefficient of the opposite parity is zero, while ψ_q=1. A nonzero root in the displayed list prevents ψ from being u^q, so a second coefficient is nonzero. Therefore η is neither an all-equal list nor a one-positive list, and both gain inequalities are strict. Dividing that bounded family improvement by q log k or q² gives zero for its stated growing q. This result concerns the solved family; the stronger moment estimates below have their own exact comparison maps and larger gains.

## Stronger shared-cosh bound found during the independent maps review

The independent maps reviewer identified the following improvement, which was checked directly here and sent to root and the arithmetic owner. It uses the same b, β_j, M_k, ψ, source measure and raw jets. For any coefficient column p=(p_0,…,p_q), pointwise Cauchy–Schwarz gives

`|Σ_(j=0)^q p_j u^j|² ≤ (Σ_(j=0)^q |p_j|²/β_j)(Σ_(j=0)^q β_j u^(2j))`.

Every term of the infinite cosh series is nonnegative on real u, so the finite second factor is at most cosh(bu). Tonelli and the convolution Laplace identity give ∫cosh(bu)m_k(u)du=(M_h(b)^k+M_h(−b)^k)/2=M_k/2, retaining both literal Laplace values. Hence the matrix inequality is H_q≤(M_k/2)diag(β_j^−1). Inversion and the unchanged raw-jet map yield K_q^raw≥(2/M_k)E_qdiag(β_j)E_q^*.

The cofactor polynomial is homogeneous and is defined for every positive auxiliary vector, including (1,…,1) off the unit simplex. Its determinant there is |det Z|²B_βΣη_j. Combining it with the same degree-(2q−1) comparison kernel gives

`C_k ≤ U_cosh := q log(M_k/2)−log B_β−log(Σ_(j=0)^q η_j)−log V_(2q−1)^ν`.

The improvement U_eq−U_cosh is exactly q log(2(q+1)). The improvement U_opt−U_cosh is q log(2(q+1))−g(η), lying between q log(2q) and q log(2(q+1)); equality at the lower endpoint requires a single positive coefficient, and equality at the upper endpoint requires all coefficients equal. For an admitted complete quartet both endpoints are strict. These comparisons alter the estimate used before optimization; they do not contradict the proved gain cap within the older family.

## Complete exact-moment diagonal family supplied by root

Root then supplied the larger family, independently checked here. Write μ_(2j)=∫u^(2j)m_k(u)du for 0≤j≤q, so μ_0=μ_h^k. Each is finite and strictly positive: the source has a positive density, and u^(2j) is positive off its finite zero set. For arbitrary a_j>0 define s(a)=Σ_(j=0)^q a_jμ_(2j). The same pointwise Cauchy–Schwarz inequality, now with a_j in place of β_j, integrates exactly to H_q≤s(a)diag(a_j^−1). Thus K_q^raw≥s(a)^−1E_qdiag(a_j)E_q^*.

The full auxiliary map is `a↦(s,t)`, with t_j=a_jμ_(2j)/s. It maps the positive cone bijectively to s>0 and the open simplex; its inverse is a_j=st_j/μ_(2j), whose actual cost is Σa_jμ_(2j)=s. All original moments, including μ_0, remain explicit. The signed cofactor calculation gives

`det(E_qdiag(a_j)E_q^*)/s^q = |det Z|²(∏_(j=0)^q μ_(2j)^−1) D_κ(t)`,

where κ_j=|ψ_j|²μ_(2j). Indeed each retained q-column product is s^q∏_(l≠j)t_l/μ_(2l); extracting the product of all q+1 inverse moments leaves the exact factor |ψ_j|²μ_(2j) at the omitted column. In particular κ_q=μ_(2q)>0, and its zero pattern is exactly that of ψ. The already fully proved optimizer classification, scalar construction and certificates apply to κ without changing the quotient dimension or deleting any zero coefficient.

At an interior optimizer choose s=1 and a_j=t_j/μ_(2j). At a boundary optimizer take positive simplex mixtures t^ε with equal weights and use a_j^ε=t_j^ε/μ_(2j). Their cost stays exactly one. The raw matrices E_qdiag(a_j^ε)E_q^* converge to the boundary raw matrix, whose determinant is positive because d(κ)>0. Passing to the limit in the raw-kernel inequality proves the boundary estimate without evaluating any divergent reciprocal source bound. Consequently the fully optimized exact-moment bound is

`C_k ≤ U_mom := Σ_(j=0)^q log μ_(2j)−log d(κ)−log V_(2q−1)^ν`.

The q+1 moments and the degree-q determinant are consistent: scaling the entire source density by r>0 multiplies each μ_(2j) and each κ_j by r, so d(κ) scales by r. The displayed source part therefore changes by q log r, as required for a q-dimensional determinant. This checks the literal mass count without changing the source density in the construction.

The β ray is contained in this exact family. Its true cost is S_q=Σ_(j=0)^qβ_jμ_(2j), and t_j=β_jμ_(2j)/S_q. Substitution into D_κ gives `(∏μ_(2j))B_β(Ση_j)/S_q^q`; hence its raw determinant lower bound is |det Z|²B_β(Ση_j)/S_q^q. The resulting estimate is U_β=q log S_q−log B_β−log(Ση_j)−log V_(2q−1)^ν, and U_mom≤U_β because d(κ) is the exact maximum over all such auxiliary rays.

Finally S_q<M_k/2 strictly. For every real u≠0, the omitted cosh terms starting at degree 2q+2 are positive because b>0; the source density is positive, and the full cosh integral is finite. Therefore integrating the positive remainder gives M_k/2−S_q>0. Thus U_β<U_cosh and the stronger family genuinely improves the original comparison. Every moment used has degree at most 2q. No asymptotic estimate of the comparison determinant or new zero information is assumed in this argument.
