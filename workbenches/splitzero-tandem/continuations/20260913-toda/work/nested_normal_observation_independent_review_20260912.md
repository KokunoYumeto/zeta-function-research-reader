# Independent proof review of NN.1–22

The complete draft work/nested_normal_observation_20260912.tex was read, together with the original frame definitions and the full strictness/reconstruction argument FC.21–36 in output/split_zero_rh_tandem_2026-09-12/tex/sum_connection_stieltjes.tex. The companion fixed-source density argument was checked through work/nested_relative_frame_density_independent_review_20260912.md. No frozen or current cumulative source was edited, and no numerical tests were needed.

Reviewed NN draft SHA256: **b04d6bde65797899368e870578e029c62dc67d16c7f0b6ce805f63236b6b540f**.

Reviewed FC source SHA256: **fb453c93e3a08e3ed2aca04691e9401b13779be137eb07b2de55571df6b888cc**.

**Mathematical result:** the contractions, algebraic and metric limits, fixed-target divergence, changing actual metric transport, explicit arithmetic witness, and split-semimodule maps are correct. One opening notation clarification was sent to the author: specify all relative monomials in the \(k-1\) independent variables \(z_1,\ldots,z_{k-1}\), with \(z_k=-\sum_{i<k}z_i\). That is the existing FC.5 convention. Taking monomials in all \(k\) dependent variables instead would create a redundant frame and invalidate the inverse Gram notation. The proof below uses the explicitly independent FC frame.

## 1. Original source, normal map and finite transition

The coordinate change \((s_1,\ldots,s_k)\leftrightarrow(S,z_1,\ldots,z_{k-1})\), with \(s_i=S/k+z_i\) and \(z_k=-\sum_{i<k}z_i\), is linear and invertible. Thus the monomials \(\theta_\alpha S^n\) with \(\ell_\alpha+n\le m\) form the literal full total-degree source. On the integration line \(S=k/2+iu\), differentiation contributes \(inS^{n-1}\). The relative variables \(z_i=iy_i\) remain fixed under \(\partial_u\).

The derivative of \(A_mp=j_mC_mp\) is \(j_m'C_mp+j_mC_m'p\). The second term lies in \(\operatorname{ran}j_m\); therefore its complementary projection is zero, giving exactly \(\boldsymbol N_mp=(I-\mathbb P_m)\partial_u A_mp\). Projection onto the frame gives the displayed tangential map. This proves NN.2 with the original phase and derivative factor.

Literal coefficient padding gives \(C_\ell Q_{\ell m}=E_{\ell m}C_m\), \(j_\ell E_{\ell m}=j_m\), and \(A_\ell Q_{\ell m}=A_m\). The finite frame depends smoothly on \(u\), its Gram is invertible at each fibre, and the orthogonal projection is consequently strongly measurable. Its direct-integral action is a bounded self-adjoint projection of norm at most one. Nested frame ranges imply both products \(\mathbb P_\ell\mathbb P_m=\mathbb P_m\mathbb P_\ell=\mathbb P_m\).

The actual FC.24–26 argument proves that \(\boldsymbol N_m\) is injective on the complete admitted finite polynomial source, including \(h=1\). In particular \(H_m^N>0\), \(L_m^N\boldsymbol N_m=I\), and each source is nonzero because it contains \(1\). For \(r=\boldsymbol N_mp\),

\[
 (I-\mathbb P_\ell)r
 =(I-\mathbb P_\ell)(I-\mathbb P_m)\partial_uA_mp
 =\boldsymbol N_\ell Q_{\ell m}p.
\]

This proves the codomain and both formulas of NN.6. Since \(Q_{\ell m}\) and \(\boldsymbol N_\ell\) are injective, so is \(V_{\ell m}\). The orthogonal projection proves its norm bound. Substitution of \(L_\ell^N\boldsymbol N_\ell=I\) gives the exact cocycle and source square NN.7–8, including their identity-at-equal-level case.

The three projections \(\mathbb P_m\), \(\mathbb P_\ell-\mathbb P_m\), and \(I-\mathbb P_\ell\) are pairwise orthogonal and sum to the identity. Their decomposition of the single unchanged vector \(\partial_u(\Psi P)\) proves every equality in NN.9. These identities compare the actual normal images through \(V_{\ell m}\); no inclusion of those images by the ambient identity is needed.

## 2. Fixed-source decay and the algebraic colimit

The density argument provides the precise input needed here: for every fixed \(u\), the union of the full relative frame images is dense in \(L^2(d\mathbf y)\), and hence \(\Pi_m(u)\to I\) strongly. The argument uses the actual exponential moment of \(|\Psi(u,\cdot)|^2d\mathbf y\), together with its almost-everywhere nonvanishing, so it concerns the retained amplitude and every fibre. A fixed polynomial's derivative amplitude belongs to \(\mathscr K\), by the original differentiated Schwartz estimates. Consequently

\[
 \|(I-\Pi_m(u))\partial_u(\Psi P)(u)\|^2
 \le \|\partial_u(\Psi P)(u)\|^2
\]

has one integrable right-hand side independent of \(m\). Dominated convergence gives NN.4 exactly for the fixed polynomial once \(m\ge\deg P\). No assertion uniform in a changing polynomial source is used.

For the algebraic direct limit, a representative \(r\in\mathscr R_m^N\) corresponds to the polynomial with coefficient vector \(L_m^Nr\). The source square identifies later representatives with exactly the same polynomial. Every polynomial occurs, and a representative mapped to zero is \(\boldsymbol N_m0=0\). This proves the complex-linear isomorphism NN.10.

For each class, the norms of its later representatives decrease by the projection contraction and are bounded below by zero. Thus the limit in NN.11 exists. Passing to a common later level proves homogeneity and the triangle inequality, and the cocycle proves independence of representatives. The corresponding fixed polynomial has residual tending to zero by NN.4. Therefore the entire seminorm is zero. Its kernel is the entire algebraic limit, and the exact Hausdorff quotient is the zero vector space. The quotient is explicitly related to the nonzero polynomial algebraic limit by the zero linear map.

## 3. The derivative graph limit and reconstruction

Every graph pair has a unique coefficient vector because its normal component determines that vector. Hence NN.13 defines an injective transition and the source inclusions prove its cocycle. The two graph components are orthogonal, and their sum is the unchanged derivative amplitude. Both source presentations of the transition therefore have squared norm \(\|\partial_u(\Psi P)\|^2\), proving isometry.

Graph addition agrees under transitions and is an isometric bijection onto the indicated derivative image. This proves NN.14 and its completion as the closure of that image in the original \(\mathscr K\).

For completeness, the derivative image is injective in the polynomial source. If \(F=\Psi P\in L^2(du;\mathscr H)\) has zero weak \(u\)-derivative, then its pairing with any member of a countable dense subset of the separable Hilbert space \(\mathscr H\) is a scalar \(L^2(\mathbb R)\) distribution with zero derivative. Such a distribution is a constant, and its \(L^2\) norm forces that constant to vanish. Intersecting the corresponding countably many full-measure sets proves \(F=0\) almost everywhere. Each original amplitude factor has a discrete real zero set; after the invertible \((u,\mathbf y)\) coordinate map, their product vanishes only on a null union of affine hyperplanes. Thus the restriction of \(P\) to the full original real coordinate locus vanishes almost everywhere and is the zero polynomial. This also proves that every fixed nonzero polynomial has a strictly positive derivative norm.

The finite reconstruction map is exactly \(r=\boldsymbol N_mp\mapsto(\boldsymbol T_mp,\boldsymbol N_mp)\). Substitution proves NN.15. It induces a linear bijection between the two algebraic colimits; the already proved norms give its complete metric relationship. In particular, it is not a bounded map from the zero-seminorm limit to its nonzero derivative norm presentation, and the divergence argument below quantifies that fact at finite levels.

## 4. Original arithmetic observation and explicit witness

In NN.16, \(U=\prod_i v_h(s_i)\) denotes the original entire product before the derivative and full Hermite quotient are applied. Therefore \(\mathcal J^{\log}P=j_I(\partial_S^{\rm rel}(UP))\) is well-defined with every unit derivative and nilpotent order. Since \(\partial_S^{\rm rel}S=1\) and \(\partial_S^{\rm rel}z_i=0\), its literal columns agree with FC.34, including the \(n\) coefficient after the \(-i\mathscr U_k^{-1}\) source arrow. Coefficient inclusion and the finite inverse square then prove NN.17.

At any retained ordered tuple \(\boldsymbol\rho\), the polynomial \(P_\rho=S-\sum_i\rho_i\) vanishes at that tuple while \(\partial_S^{\rm rel}P_\rho=1\). The product rule gives

\[
 \bigl(\mathcal J^{\log}P_\rho\bigr)(\boldsymbol\rho)
 =(\partial_S^{\rm rel}U)(\boldsymbol\rho)\,0
   +U(\boldsymbol\rho)\,1
 =U(\boldsymbol\rho)\ne0.
\]

Full selected orders make every \(v_h(\rho_i)\) nonzero. This proof uses the constant coordinate of a full local algebra and remains valid for repeated roots. It also shows the observation is nonzero without assuming that the constant polynomial has a nonzero derivative jet.

For \(m_*\ge k(d-1)\), the complete remainder space is contained in the admitted source. Since multiplication by \(j_IU\) is invertible, the original map \(J_*\) is onto. The amplitude form \(H_{m_*}^0\) is positive definite because the amplitude is almost everywhere nonzero and the literal polynomial source is independent. Thus \(J_*(H_{m_*}^0)^{-1}J_*^*\) is positive definite. Its inverse \(G_*\) and the displayed minimum lift have exactly the stated original target metric: the lift maps to its target and is orthogonal to the kernel, so adding another lift adds the squared norm of a kernel vector. This proves NN.19 without a freely chosen target normalization.

For each finite normal image, substitute \(r=\boldsymbol N_mp\). The inverse, graph reconstruction, and fixed-target observation squared norm ratios have common denominator \(p^*H_m^Np\), and the three numerators in NN.20 respectively. The bijective substitution \(b=(H_m^N)^{1/2}p\) gives the maximum eigenvalues stated there.

Choose a fixed nonzero polynomial for the inverse and graph norms. Its amplitude and derivative norms are fixed positive constants, whereas the normal norm is positive at each finite level by FC.26 and tends to zero by NN.4. The corresponding ratios tend to infinity and bound the operator norms from below for every sufficiently large \(m\). For the arithmetic observation choose the single fixed polynomial \(P_\rho\) above. Its \(G_*\)-norm is fixed and positive, so the same argument proves divergence. This establishes all three limits to infinity, not merely an unbounded subsequence.

## 5. Changing actual minimum metrics

For \(m\ge m_*\), each earlier minimum lift is an admissible later lift with exactly the same amplitude. Taking the later minimum gives \(G_m\preceq G_*\). Both remain positive definite at each finite level. Define the displayed positive Hermitian matrix \(B_m=G_*^{-1/2}G_mG_*^{-1/2}\). Then \(0<B_m\preceq I\) and

\[
 q^*G_mq=(G_*^{1/2}q)^*B_m(G_*^{1/2}q).
\]

The two extremal eigenvalues of \(B_m\) bound this quadratic form by the corresponding multiples of \(q^*G_*q\). Applying the bound to \(q=\mathsf J_m^{\log}p\) and taking the same normal-norm Rayleigh supremum proves both sides of NN.21. The exact eigenvalue formula follows as in NN.20. The statement makes no unsupported inference about the changing-target norm: divergence in the fixed actual metric is compared through this explicit positive operator, whose eigenvalue asymptotics have not been assumed.

## 6. Split maps, the empty packet, and invariant sources

For \(G(V)=\{\tau\}\sqcup V\), supported vector addition and supported scalar action are the original operations, and the external scalar zero \(\tau\) acts by external absence. Casewise checking external and supported inputs proves the semimodule laws. A linear map gives an additive scalar-compatible \(G(f)\), including both the supported zero and external zero cases. Composition is literal composition on supported vectors.

NN.22 is exactly \(G\) of the zero Hausdorff quotient map. Its external fibre is the singleton \(\{\tau\}\), and its supported fibre is all polynomials, including their supported zero. If \(G(\mathcal J^{\log})\) factored through it, the supported zero polynomial would force the value at \(e_0\) to be \(e_E\), while \(P_\rho\) forces the same value to be a supported nonzero vector. This contradiction proves the exact factorization obstruction. For \(h=1\), \(E=0\), so the target observation is zero and its split lift does factor through that same map. The amplitude and normal strictness still satisfy FC.1–26, so the inverse and graph limits and divergence remain valid. No positive-dimensional target inverse is invoked in this case.

The invariant-source statement has the following exact metric proof. A fixed finite permutation group acts on the original variables with unit Jacobian in the retained relative measure; \(\Psi\), \(S\), the degree filtration and the derivative are invariant. Hence it acts unitarily on the original amplitude spaces, and the full finite projections commute with its Reynolds projection. On invariant vectors the invariant-frame projection equals the restriction of the full projection. Every source transition and normal/reconstruction map is therefore equivariant, and all the previous proofs restrict to the invariant source.

The jet map is equivariant because the same \(h\) is used in every factor and the full product unit \(U\) is invariant. Averaging a full preimage of an invariant target proves surjectivity onto \(E^{\mathrm{group}}\) without changing degree. The unique full minimum lift of an invariant target is itself invariant: applying any group element gives another lift with the same minimal norm, and uniqueness forces equality. Therefore the invariant-source minimum metric is precisely the restriction of the original full \(G_m\). This proves the metric statement in the final paragraph, rather than introducing an unrelated invariant target form. Finally \(P_\rho=S-\sum_i\rho_i\) is invariant, and its derivative jet is an invariant nonzero target by NN.18. Thus the same witness proves the invariant observation's nonvanishing and fixed-metric divergence.

No substantive mathematical gap was found. The independent-coordinate clarification and this explicit invariant minimum proof were communicated for incorporation into the final draft; the reviewed hash above records the exact initial version.

## Revised complete-source seal

The entire revised NN.1–22 draft was then reread at SHA256 **fc7e6656eaee1ab55dad868d6fbe16f5d43cced505fcb9be268f2a8bd8eb4bea**. Its opening frame definition now explicitly uses the \(k-1\) independent variables and retains \(z_k\) as dependent, resolving the notation issue. All the mathematical conclusions and proofs reviewed above remain correct. The invariant minimum argument is supplied in full in Section 6 of this report and was sent to the author for the cumulative source. There are no outstanding mathematical corrections to this reviewed version.

## Final bounded delta audit: NN.18a and the invariant minimum proof

The two subsequent additions and their surrounding contexts were read at final source SHA256 **9ec6dee3434116bbe014cdae3856eed3df3917ea2831d3279e09e244e3d558ab**. Both are correct. No source edit, test, additional agent or further extension was made in this delta review.

The new witness is in the nonempty-packet subsection, so \(d\ge1\). It is the literal original polynomial

\[
 P_{\rm rel}=\sum_{i=1}^k h(s_i)\in I,\qquad \deg P_{\rm rel}=d.
\]

It is nonzero, since its degree-\(d\) terms are the distinct monomials \(s_i^d\) with coefficient one. It is invariant under every permutation of the factors and belongs to the full invariant polynomial source at every degree \(m\ge d\). Its ordinary amplitude jet \(j_I(UP_{\rm rel})\) is zero. Applying the original derivative to the original product before quotienting gives

\[
 \begin{aligned}
 \mathcal J^{\log}P_{\rm rel}
 &=j_I\!\left((\partial_S^{\rm rel}U)P_{\rm rel}
             +U\,\partial_S^{\rm rel}P_{\rm rel}\right)\\
 &=\frac1k U_k\sum_{i=1}^k[h'(s_i)]_I .
 \end{aligned}
\]

The discarded term is exactly the one still containing the relation \(P_{\rm rel}\), and it vanishes only in the displayed original quotient. If \(d=1\), monicity gives \(h'=1\), so the sum is \(k\) and the result is \(U_k\ne0\). If \(d\ge2\), every \(h'(s_i)\) is already a full standard remainder, and its degree-\(d-1\) term is \(d s_i^{d-1}\). These are distinct standard basis monomials for different \(i\), so their sum cannot vanish. The lower-degree terms cannot cancel them. The complete arithmetic unit \(U_k\) is invertible, and multiplication by \(1/k\) is nonzero. Thus NN.18a is nonzero for every nonempty packet, including all repeated roots, without requiring simple-root point evaluations of \(h'\).

The asserted theta boundary is also the original one. In term \(i\), take the tensor with \(\phi_*\) in factor \(i\) and \(F_h\) in every other factor, multiply the primitive by \((-1)^{i-1}\), and apply the original tensor differential. Its Koszul sign is the same \((-1)^{i-1}\), giving a positive term with \(\Theta\phi_*=h(D)F_h\) in that factor. Summing gives exactly \(\mathcal T_h^{(k)}P_{\rm rel}\). This proves the claimed actual relation representative with both signs. Its invariant top-degree source is the displayed permutation-invariant polynomial. The separate \(h=1\) paragraph remains the zero arithmetic target; NN.18a does not assert nonvanishing there.

The final invariant-minimum paragraph now includes the requested proof. The permutations in the declared finite group preserve the original product measure and identical amplitudes, so their actions are unitary. They preserve the degree filtration and commute with the full jet map. The average with its literal factor \(1/|\mathfrak G|\) is consequently an invariant lift of an invariant target at the same admitted degree. Each group element maps the full minimum lift to another lift with exactly the same norm. Uniqueness forces every such group element to fix that lift. The full and invariant minima therefore coincide on invariant targets, with exactly the restrictions of \(G_m\) and \(G_*\) claimed in the text.

**Final status at the source hash in this subsection: no outstanding mathematical corrections.** The original reviewed NN.1–22 arguments, the new invariant supported-zero relation with nonzero conormal response, and the included invariant minimum proof are consistent with their exact source and target maps.
