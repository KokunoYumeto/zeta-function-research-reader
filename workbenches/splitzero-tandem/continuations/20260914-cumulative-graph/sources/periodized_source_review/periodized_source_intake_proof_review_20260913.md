# Independent review of the periodized-source intake proof

Date: 13 September 2026.

Final-version revalidation: the author repaired the representative sentence and added the explicit common-calculation cross-reference paragraph. I then reread the complete current PSA1–PSA29 source, SHA-256 `cb2a8387a5d7132cff142ff4ceec3f871bb5de6ef3343159bd52063ffbcbf327`. The indicated prose defect is now corrected. The mathematical review below applies to this complete current version; no unresolved defect remains within this review's assigned scope. The initial pins and counterexample are retained as the actual review history.

Final bounded domain clarification: I subsequently read the added paragraph requiring the common controlled degree D≥N+2 for the inverse observation extensions. It correctly records that D=2q+2 covers every endpoint N≤2q, and that the boundary identity uses smooth projected columns and requires source injectivity only at its representative degree N. This is exactly the domain argument proved in Sections 9–10 below. The final reviewed PSA source is SHA-256 `f4ce96183daf8fa7ec27c0f9d8b90d3fb69694caf2334cfa2e8987bffc5ab4c5`. Removing this one added paragraph reproduces the completely reread prior source hash `cb2a8387a5d7132cff142ff4ceec3f871bb5de6ef3343159bd52063ffbcbf327`; no further proof or execution change is being assumed.

Reviewed in full:

- `work/periodized_source_intake_proofs_20260913.tex`, PSA1–PSA29, SHA-256 `048365fbf6cdeb16f18f491d11df48c30998864e4adc4b0c5485c6afe68328fc`.
- `output/split_zero_rh_tandem_2026-09-12/sources/web_periodized_source_delivery/Tau_Periodized_Source_Control/NOTE.tex`, all 1,048 lines, including P1–P64 and P26a–P26b, SHA-256 `acf63a56d5f50cfaa23f57ee52a66df261ec241ce13fd81ccac39a3bbbddd3ff`.

This is a written proof review. No checker, mutation, numerical calibration, Lean run, or PDF build was executed in this lane. The complete density/completion proof is assigned to a separate reviewer; the critical comparison and its inherited source maps are assigned to the root. The execution-history paragraph is therefore treated here as a reported execution claim, not as independently verified execution evidence. PSA23–PSA25 and PSA27–PSA29 are the same common calculations as the root's FC1–FC23, not separate discoveries.

## Conclusion and the one required textual correction

The reviewed formulas have the stated constants, orientations, domains, and signs. In particular the Sobolev coefficient in PSA6, the sampled source factor 2π/L, the all-period zeta factor, the finite Fourier tail coefficient, the asymmetric source error, the fixed-remainder minimum, and both second-order boundary terms are correct.

The sentence immediately after the reference to P34–P37, “No extremal vector is changed,” is false if read literally. The constraint set and coefficient coordinates stay fixed; their minimizing representatives can change, and PSA19 correctly records that change. A concrete example is

J=(1,1), M=I₂, and M_L=diag(1,3/2).

These positive Grams obey (1−η)M≤M_L≤(1+η)M with η=1/2. Yet K=2, G=1/2, and C=(1/2,1/2)^T, while K_L=5/3, G_L=3/5, and C_L=(3/5,2/5)^T. The common affine constraint is p₀+p₁=v, and its unique minimizer has changed. Its difference (1/10,−1/10)^T belongs to ker J, as the actual argument requires.

Replace that sentence by: “The constraint set and coefficient coordinates are unchanged; the minimizing representatives may change and their difference is retained below.” This corrects the prose without altering any displayed theorem or its proof. The defect was reported to the parent as soon as identified.

## 1. Coordinate orientation, isometry, and the original generator

The ordered input coordinates are (r,z₁,…,z_(k−1)); the ordered output coordinates are (y₁,…,y_k), with y_i=r+z_i for i<k and y_k=r. Expanding the derivative matrix along its last row leaves the (k−1)-dimensional identity and gives sign (−1)^(k+1)=(−1)^(k−1). For k=1 this is the one-dimensional identity. Multiplying by the positive exponential Jacobian in y→x gives the absolute density exp(kr+∑z_i) dr d z. Thus PSA2 and PSA3 preserve the positive L² measure and separately retain the orientation sign.

Inserting the displayed inverse into the forward map cancels exactly the factor (x₁⋯x_k)^(1/2); in the other direction it recovers r=log x_k and z_i=log x_i−log x_k. The norm identity follows by the positive change of variables. Both compositions are identities on their corresponding L² equivalence classes.

A simultaneous change of every y_i leaves every z_i fixed and changes r by that same amount, so ∑∂_(y_i)=∂r in these coordinates. Differentiating the factor exp((kr+∑z_i)/2) contributes k/2. Therefore U_k D^(k)=(-∂r+k/2)U_k with the original D_i=−x_i∂_(x_i), and iteration gives ∂r^j U_k=(−1)^j U_k(D^(k)−k/2)^j. No averaging of the sum coordinate appears.

## 2. Weighted source regularity and the exact Sobolev constant

For the stated finite tensor source, each polynomial in D^(k) applied to F remains a finite sum of products of logarithmic derivatives of its original strong-Schwartz factors. Pulling the exponential r weight back through the isometry gives exp(2a|log x_k|)=max(x_k^(2a),x_k^(−2a)). Bounding that maximum by the sum leaves a finite sum of products of the original one-variable integrals, all finite by the stated source class. This proves PSA5 without extending it to arbitrary L² inputs.

For an H¹ function f with values in the Hilbert space K on [r,r+1], use its continuous absolutely continuous representative. There exists t₀ in this interval with ||f(t₀)||²≤∫_r^(r+1)||f(t)||²dt. Otherwise integrating the strict opposite inequality would be a contradiction. The fundamental theorem of calculus, ||a+b||²≤2||a||²+2||b||², and Cauchy–Schwarz on an interval of length at most one give

||f(r)||² ≤ 2∫_r^(r+1)||f(t)||²dt + 2∫_r^(r+1)||f′(t)||²dt.

For t in that interval, |t|≥|r|−1. Thus exp(−2a|t|)≤exp(2a)exp(−2a|r|). Apply this inequality to the two integrals with f=∂r^j ψ, and bound their weighted integrals by I_(a,j) and I_(a,j+1). The result is exactly

||∂r^jψ(r)||² ≤ 2 exp(2a)exp(−2a|r|)(I_(a,j)+I_(a,j+1)).

Taking square roots bounds every derivative by a constant times exp(−a|r|). For r in a fixed period interval, the series over translates r+mL is therefore uniformly summable in K for every derivative. It defines a smooth periodic K-valued function. Products of two translate sums are absolutely summable by the product of their two norm bounds, which justifies unfolding correlations. Polynomial r weights and repeated derivatives are integrable as well; integration by parts proves rapid Fourier decay, including Fourier derivatives. These observations justify all later Hilbert-valued Fourier and Mellin manipulations on this finite source.

## 3. Circle coefficients, the zeroth mode, and relative Fourier factors

The basis e_n(r)=L^(−1/2)exp(−2πinr/L) is orthonormal for the unscaled measure dr on one period. With the conjugate-linear first-slot convention, pairing e_n with P_Lψ inserts the phase exp(+2πinr/L). Unfolding all intervals gives exactly L^(−1/2)widehat ψ(2πn/L) for the plus-sign line transform. At n=0 this coefficient is L^(−1/2)widehat ψ(0), and multiplication by e₀ gives the constant function L^(−1)widehat ψ(0).

The augmented target keeps the unscaled vector widehat ψ(0); its metric must therefore be L^(−1) times the original K metric. The reconstruction rescales the vector by L^(−1/2) as it inserts the n=0 Fourier coefficient. Consequently its Gram contribution is exactly L^(−1) Z₀*Z₀, and PSA8 is the orthogonal decomposition of the full circle image. For the supplied Connes–Consani source map Eφ=(1/2)U₁Θφ, the Fourier coefficient is divided by 2 and its Gram by 4. The displayed seed value uses MΘφ_*(1/2)=2ξ(1/2), giving ξ(1/2)/sqrt L with no further factor.

For the tensor seed, take the additional plus-sign Fourier transform in z. The identity

u r + ∑_(i<k)t_i z_i = ∑_(i<k)t_i y_i + (u−∑_(i<k)t_i)y_k

shows that the full transform is the product of the k original Mellin amplitudes v_h(1/2+it_i), with t_k=u−∑_(i<k)t_i. The coordinate transformation has absolute determinant one, so no extra measure factor arises at this step. Plancherel in the k−1 retained relative variables contributes (2π)^(−(k−1)). The convolution of w_h=|v_h|²/(2π) contributes (2π)^(−k). Their ratio is exactly 2π, yielding PSA10. For k=1 the empty relative integral gives |v_h(1/2+iu)|²=2πw_h(u), the same identity.

The plus-sign transform sends ∂r to −iu and hence sends −∂r+k/2 to k/2+iu. Each polynomial column consequently has the literal factor P(k/2+iu). Circle Parseval adds the factor 1/L from the squared Fourier coefficient. Combining it with the preceding 2π proves every entry of PSA11, with all complex conjugates in the stated positions. The separate density review verifies the tail and positivity inputs used to conclude strict positivity for k≥2 at every L. The quantitative source inequality below independently supplies strict positivity for all k at its admitted L.

## 4. Correlations and the two exponential weights

The full periodized squared norm expands into pairs of translates. For translate indices m,n, substitute t=r+mL and put l=n−m. Summing m unfolds the real line; the remaining l term is ∫〈Ψc(t),Ψc(t+lL)〉dt. Absolute convergence was proved above. This gives M(L)=∑_l C(lL), with C(0)=M. Changing variables in the conjugate expression gives C(−s)=C(s)*, so the nonzero sum is Hermitian.

For s>0, write the original integrand as exp(−as) times the inner product of exp(−ar)Ψc(r) and exp(a(r+s))Ψc(r+s). Their two squared integrals are c*M_(a,−)c and, after t=r+s, c*M_(a,+)c. Hilbert-space Cauchy–Schwarz proves PSA13. The negative s calculation exchanges the two forms. Summing exp(−a|m|L) over m≠0 gives 2/(exp(aL)−1). Applying 2sqrt(xy)≤x+y to the two original nonnegative quadratic forms yields PSA14. Since this holds for every complex coefficient vector, it is exactly the stated Hermitian matrix order; no diagonal-entry approximation replaces complex cross-pairings.

## 5. All-period recovery and its limit at delta zero

For n>0 substitute u=2πn/L. Reversing the limits together with dL=−(2πn)u^(−2)du changes the integrand L^(−2−δ) dL to (2πn)^(−1−δ)u^δ du. This proves PSA15 with its exact exponent and coefficient. For n<0 the same substitution supplies the negative half-line. Each positive absolute index contributes once to each corresponding half-line, so the common lattice sum is ζ(1+δ), with no extra factor two multiplying the full real-line integral.

Tonelli applies to each nonnegative squared norm; summing and multiplying by (2π)^δ/ζ(1+δ) leaves the factor 1/(2π) in the original Plancherel convention. Equality of the quadratic forms for all c proves PSA16, including mixed matrix entries by the usual complex polarization identity. The weighted integrals are finite by the finite-source Fourier decay.

For a positive real v and 0<δ≤δ₀, write v^δ−1=∫₀^δ v^s log v ds. On 0<v≤1 its modulus is bounded by δ|log v|, and on v≥1 it is bounded by δv^δ₀|log v|. The slightly larger uniform bound in the note, δ|log v|(1+v^δ₀), is therefore valid. The Fourier Gram is bounded near u=0 and rapidly decaying at infinity, so the positive matrix integral L_(δ₀) is finite. Integrating the scalar bound against each quadratic form proves the two-sided matrix rate and convergence. The point u=0 is a Lebesgue null set and creates no missing term in this integral.

By contrast the retained circle zero mode is Z₀*Z₀/L. Inserting it into the L^(−1−δ)-weighted period integral would require ∫₀ L^(−2−δ)dL times that matrix, which diverges for any nonzero Z₀*Z₀. PSA8 gives its exact finite-L reconstruction. The averaging identity acts on source Grams before inverse compression; no interchange of averaging with the nonlinear constrained quotient construction is used.

## 6. The fixed-remainder minimum and its changing representative

Surjectivity of the monic remainder map J_N for N≥q−1 implies that J_N* is injective. Hence K_N=J_N M_N^(−1)J_N* is positive definite when M_N is positive definite. With G_N=K_N^(−1) and C_N=M_N^(−1)J_N*G_N, direct multiplication gives J_N C_N=I and C_N* M_N C_N=G_N.

For any vector v in E, every representative with J_N P=v has a unique decomposition P=C_N v+z with J_N z=0. The mixed pairing is C_N* M_N z=G_N J_N z=0. Expanding the squared norm therefore gives the full Pythagorean identity PSA18, including uniqueness of the minimizing representative because z* M_N z vanishes only for z=0.

If αM_N≤M_N′≤βM_N, then every representative in the same affine set satisfies P*M_N′P≥αP*M_NP≥αv*G_Nv. Taking the minimum gives the lower quotient inequality. For the upper inequality, evaluate the primed form on the original minimizing representative C_Nv: the primed minimum is at most (C_Nv)*M_N′(C_Nv)≤βv*G_Nv. Thus the factors pass unchanged to the quotient Gram. This argument does not assert that the original representative minimizes the primed form; the counterexample stated above explains the necessary wording correction.

Because both C_N and C_N′ are right inverses of J_N, their difference has every column in ker J_N. Monic division gives ker J_N=χP_(N−q) for N≥q, with the zero space when N=q−1. This proves PSA19 and its unique polynomial relation coefficient without changing coordinates. In the original tensor algebra, χ(S) annihilates the sum-cyclic generator 1, so χ(∑s_i)Q(∑s_i) is in the ideal generated by the h(s_i). Fixed-order monic division gives the actual Q_i coefficients. Replacing the i-th F_h by φ_* gives a cochain in which the preceding i−1 B slots have degree one. Its tensor differential therefore has sign (−1)^(i−1). Multiplication by the separately stated primitive sign (−1)^(i−1) produces +1, and h(D_i)F_h=Θφ_* gives the original relation. The quotient image is zero with the coefficient and support retained upstream.

## 7. Finite-cutoff tail: both lattice directions and the one-sided error

The source derivative identity in PSA4 gives the exact map underlying H_(p,N), including (−1)^p and the original-coordinate weight 1+(log x_k)². The sign has modulus one in the Gram, while remaining present in the map. The decay from Section 2 removes every integration-by-parts boundary term, so widehat(∂r^p ψ)(u)=(−iu)^p widehat ψ(u).

For u≠0, use the Bochner integral triangle inequality and weighted scalar Cauchy–Schwarz:

||widehat(∂r^p ψ)(u)|| ≤ ∫||∂r^pψ(r)||dr ≤ [∫(1+r²)^(−1)dr]^(1/2)[∫(1+r²)||∂r^pψ(r)||²dr]^(1/2).

The first squared factor is exactly π. Squaring and dividing by |u|^(2p) gives P60 and the inequality following PSA20. There is no Plancherel factor in this pointwise Fourier estimate.

For the circle Fourier coefficients the Gram factor is 1/L. Each omitted coefficient at u_n=2πn/L is bounded by π|u_n|^(−2p)H_(p,N)/L. Summing positive and negative n gives the exact coefficient (2π/L)(L/(2π))^(2p) times ∑_(n>J)n^(−2p). Since t↦t^(−2p) is decreasing, that sum is at most ∫_J^∞t^(−2p)dt=J^(1−2p)/(2p−1), for p≥1 and J≥1. Substitution yields exactly PSA21. The entire omitted Gram is positive because it is an orthogonal sum of positive coefficient Grams.

Polynomial inclusion into degree D pulls back the original, exponentially weighted, and derivative Grams to their corresponding smaller-degree forms. Therefore the two Rayleigh maxima at D bound all smaller-degree Rayleigh quotients. The explicit choices in P64 imply η_per≤η_P and η_tail≤η_T; hence η_per+η_tail<1 when the fixed positive budgets sum to less than one. Increasing the integer J to the prescribed maximum preserves this conclusion.

The lower source inequality combines M_N(L)≥(1−η_per)M_N with M_N(L)−M_N(L,J)≤η_tail M_N. The upper inequality uses the positive omitted Gram directly: M_N(L,J)≤M_N(L)≤(1+η_per)M_N. This proves the asymmetric PSA23 and strict positivity. The weakened symmetric bound follows because η_tail≥0. For k≥2 the separate positive-atom argument with J≥D also proves injectivity of the sampled degree-D polynomial space, but the quantitative source inequality already proves it for all admitted k.

## 8. Quotient determinants and the four-volume allowance

Apply Section 6 to PSA23. The quotient Gram G_N(L,J) is bounded below by αG_N and above by βG_N, where α=1−η_per−η_tail>0 and β=1+η_per. In a G_N-orthonormal frame the relative positive matrix has all q eigenvalues between α and β. Multiplying those eigenvalue inequalities yields α^q≤det G_N(L,J)/det G_N≤β^q; taking the real logarithm gives PSA24. This use of a frame only proves the invariant determinant inequality: the determinant ratio and all matrices remain recorded in the original fixed remainder basis.

Let ε_N=log det G_N(L,J)−log det G_N. Every ε_N belongs to [q log α,q log β]. The four-volume difference is ε_(q−1)+ε_q−ε_(2q−1)−ε_(2q). Its maximum is at most 2q log β−2q log α, and its minimum is at least the negative of that quantity. This proves PSA25 with the factor 2q, not 4q. Since β≤1+η_per+η_tail, the supplied total-error bound follows. If the two budgets are fixed independently of tensor degree, their positive denominator bound and finite numerator bound give a constant times q_k, whose quotient by q_k log k tends to zero. No growth estimate for the original Rayleigh maxima is required by that conclusion; they instead determine the chosen L(k) and J(k).

These are precisely the same source inequalities and determinant calculations developed in the root's FC extension. They are reviewed here as the common integrated proof, not counted as additional independent discoveries.

## 9. The finite image inverse and its full-jet quotient

Let Φ be the finite-cutoff source map of PSA26. The positive lower Gram estimate says ||Φc||²≥αc*M_Nc, so Φ is injective on its finite-dimensional coefficient domain. Its inverse on im Φ is well defined. In coefficient coordinates, (Φ*Φ)^(−1)Φ* sends Φc to c and hence is exactly that inverse on the stated domain. This formula does not require a bounded inverse on any completed infinite-dimensional source.

The composition J_NΦ^(−1) has kernel Φ(ker J_N) and is onto E because J_N is onto. Its quotient is therefore the actual full remainder space E, with nilpotent jet information retained. The minimizing lift is ΦC_N(L,J), and its Gram equals C_N(L,J)*M_N(L,J)C_N(L,J)=G_N(L,J), so the metric in PSA17 is the genuine quotient metric of this image.

At the one-degree extension, multiplication of coefficient polynomials by S intertwines J_(N+1) with A J_N. At the two-degree extension the analogous statement holds for S²−kS. Taking D=2q+2 covers all four endpoint degrees N≤2q and these two raises. The common source lower bound therefore proves every image inverse needed in the finite action diagram, on its correct degree-specific image.

## 10. Both Laplacian boundary terms and operator domains

On the Hilbert space of K-valued periodic functions, the Fourier basis identifies the H¹ derivative domain with the weighted sequence condition ∑(1+n²)||f_n||²<∞. The adjoint of ∂r on this domain is −∂r by integration by parts or its imaginary Fourier diagonal. Thus D_L=−∂r+k/2 has adjoint D_L*=∂r+k/2 and D_L*+D_L=k. The periodic H² domain corresponds to the weight 1+n⁴. On it D_L²−kD_L=∂r²−k²/4 has real Fourier diagonal −(2πn/L)²−k²/4 and is self-adjoint. The zero mode has value −k²/4. The finite projection onto |n|≤J preserves these domains and commutes with all the displayed derivatives.

Let r=V_(h,k)C_N(L,J). The coefficient difference S C_N(L,J)−C_N(L,J)A has zero remainder because J_(N+1)S C_N=A J_N C_N=A and J_(N+1)C_N A=A. It is a degree-at-most-(N+1) multiple of χ and hence has the actual monic theta primitive supplied by the same polynomial relation construction. Therefore B in PSA27 is the finite projection of this original boundary, with no discarded term.

Periodization and the finite projection commute with ∂r, and U_k intertwines the original generator as proved in Section 1. Consequently D_LR−RA=B. The minimizing-lift Gram identity gives R*R=G_N(L,J). Substituting RA=D_LR−B into A*R*R+R*RA−kR*R gives

R*(D_L*+D_L−k)R−B*R−R*B=−(R*B+B*R),

which proves PSA28 with its sign. All adjoint pairings are taken on smooth periodic representatives or their finite projections, so their domains are legitimate.

For the second-order relation, compute D_L²R=D_L(RA+B)=(D_LR)A+D_LB=RA²+BA+D_LB. Subtract kD_LR=kRA+kB and then subtract R(A²−kA). The result is exactly (D_L−k)B+BA. Both summands remain, proving PSA29. The first requires the differentiated original boundary and the second its arithmetic right action. Neither vanishes merely because the quotient image of B is zero.

If Av=ρv, then (L_(L,k)−ρ(ρ−k))Rv=((D_L−k)B+BA)v. The squared norm of the left side is the sum of |−(2πn/L)²−k²/4−ρ(ρ−k)|²||(Rv)_n||² over the admitted Fourier indices. Each scalar modulus is at least |Im(ρ(ρ−k))|, because the circle diagonal is real. Summation and taking nonnegative square roots proves the stated boundary lower estimate also after the finite projection. This provides no boundary upper estimate and does not replace the full arithmetic quotient by an invariant circle eigenspace.

## 11. Completion scope and reproducibility

The final completion paragraph refers to a separate proof of polynomial density for the actual positive sampled measure and its |χ|² weight. This review has read the raw P53–P58 statements but does not claim that the separate companion has been independently checked here. The finite-cutoff proof does not rely on interchanging this fixed-L infinite-degree completion with its degree-dependent L(k),J(k) construction. Its image inverse and fixed-remainder minimum were proved directly before taking any completion.

The common finite-cutoff and Laplacian formulas are analytically and algebraically correct, and the author has applied the one indicated prose repair in the fully reread final version pinned above. No raw source changes or verification runs were performed by this reviewer.
