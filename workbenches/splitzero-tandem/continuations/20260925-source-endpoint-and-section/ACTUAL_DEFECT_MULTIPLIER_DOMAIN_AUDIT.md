# Independent mathematical review of ADM0–ADM9

Reviewed file: `ACTUAL_DEFECT_MULTIPLIER_DOMAIN.md`.

Reviewed SHA256: `CEFA50CAADCB598DF0936191E98A1A6BEAF1495D932D86527CCA110519B9DB7E`.

Review date: 2026-09-25. Reviewer role: independent mathematical derivation and written-proof review in the current agent tree. This is an internal mathematical review, not an external human referee report.

## Coverage and outcome

The complete written ADM0–ADM9 proof was read. ADM0–ADM4 was checked against the common-domain and continuous-dual derivations; ADM5–ADM9 was checked against the actual AST source triangles, the accepted ACD/DCA current and cover maps, the GMS separator and module actions, and ECR1's original Gaussian embedding. The final ADM8 augmented-resolution induction and ADM9 finite interpolation paragraphs were reread after the last edits. No mathematical defect remains identified within this scope.

This receipt concerns the stated domains, topologies, maps, signs, kernels and algebraic derived categories. It does not independently reread all human literature underlying the earlier accepted programme theorems. It does not assert RH, vanishing of the actual adjoint defect, surjectivity of the dense specialization image, or a new purity theorem.

## ADM0–ADM1: original source and receiving objects

The support remains \(\tau\langle Z_1;\mathrm{no}\ Z_2\rangle\), with no new arithmetic, metric or coordinate assigned to it. The entire-source comparison retains the factor \(1/2\) in \(\Theta\), the factor \(1/\pi\) in its inverse, and
\[
F_0(s)=\frac{s(s-1)}8\pi^{-s/2}\Gamma(s/2)\zeta(s).
\]
The stated endpoint values and the expression at \(-2k\) are consistent with this full formula. The source ideal keeps every zero multiplicity. The subsequent value maps are explicitly quotient maps and do not replace that ideal by its reduced support.

The reflection \(\rho^\#=1-\overline\rho\) preserves imaginary part and multiplicity. Thus the stated \(D_r^*\mathsf J E\) coordinate is exactly \(\overline{d_r(\rho)}F(\rho^\#)\). The actual AST quotient \(\mathcal R\) and its original quotient topology are retained.

## ADM2–ADM4: common domain, topology and transpose

The tail estimate
\[
p_N((1-P_T)y)\le(1+T)^{-1}p_{N+1}(y)
\]
proves compactness of successive weighted Hilbert inclusions, the Montel property of the complete Fréchet intersection, and finite-coordinate density uniformly on bounded test sets. The fixed-multiplier estimate uses a nonnegative integer growth exponent, so every displayed \(p_{N+d_h}\) is defined.

The converse common-domain estimate is valid because
\[
|1+\rho^\#|\ge(1+|\Im\rho|)/\sqrt2.
\]
Together with the polynomial multiplier bounds, this proves the exact intersection of all maximal diagonal domains and equality of its graph topology with the \(p_N\) topology. The individual-operator core statement uses the two convergent graph-norm series and does not assume membership in every weighted domain.

The source estimate proves continuity \(E:Q\to H_\infty\); the bound \(|d_r|\le r-1\) gives continuity of \(\beta_r\). Finite full-jet isolators give every finitely supported value vector. The proof correctly keeps separate the quotient topology on \(\beta_rQ\), its \(H_\infty\) subspace topology and its Hilbert subspace topology.

The continuous-dual description follows from a bound by one increasing Hilbert norm. Its weighted sequence representation is unique. The tail estimate in ADM4.3 proves strong density of finite-coordinate functionals and of the embedded conjugate Hilbert space. The transpose is
\[
(\mathfrak m_h^\#)'\ell_z
=\ell_{(\overline{h(\rho^\#)}z_\rho)_\rho}.
\]
The conjugation belongs to the Riesz coordinate of the functional; the complex-linear transpose itself does not conjugate scalar multiplication. The stated transpose kernels and strong closures follow from the proved dense off-line image and AST's closed strong-dual embeddings. No new surjectivity or inductive-limit topology is asserted.

## ADM5: literal source and current triangles

The first coefficientwise exact sequence uses the same point space \(H_\infty\) on both sides and the original strict quotient \(A/A_O\). The second sequence retains \(H/H_\infty\); density is not used to replace this quotient by zero or to claim a quasi-isomorphism.

For the stated cone convention, a quotient class represented by \(a\) has cone lift \((a,-b_ra)\). Its point connecting component is therefore \(-\overline\beta_r\). The separately stated positive differentiate-a-lift boundary is \(+\overline\beta_r\). The full coefficient extension remains in the derived triangle.

The fine-resolution differentials \((-df,b_rf(p))\) and \(-d\omega\), followed by the literal compact-test transpose, agree with the ACD sign comparison \((-1,+1,-1)\). In the displayed current presentation this gives
\[
d^{-1}v=(-d_Tv,0),\qquad
d^0(u,\ell)=-d_Tu+\delta_pa_{r,\infty}\ell.
\]
Restriction to \(A_O\) kills the attaching map. Cancellation of the common point term and the already proved strict coefficient dual row give ADM5.5. This uses the concrete compact-test contractions, not exactness of continuous dualization on arbitrary complexes. The original endpoint characters and their degree shifts are retained.

## ADM6–ADM7: separator, translated action and full kernel

The full separator jets give identity on original \(Q\), \(\mathcal R\) and the reflected common domain. Translation gives zero on \(Q(-1)\), \(\mathcal R(-1)\) and \(H_\infty(-1)\). The calculation keeps \(h(s)\), \(h(s+1)\) and the coordinate map \((VF)(\lambda)=F(\lambda-1)\) distinct, with their exact intertwining equation.

The normal-ideal quotient is proved by the two explicit maps
\[
\mathcal I_+/(\mathcal I_+\cap\mathcal B_O)
\longrightarrow\mathcal R,
\qquad
[F]_{\mathcal B_O}\longmapsto[cF]_{\mathcal I_+\cap\mathcal B_O}.
\]
Both are well defined: \(c\mathcal B\subset\mathcal I_+\), \((c-1)\mathcal B\subset\mathcal I\subset\mathcal B_O\), and \(\mathcal B_O\) is an \(M\)-submodule. Their composites are identities modulo the displayed full intersection. Continuity follows from the quotient topologies. This proves strictness without a section.

The specialization route consequently retains the sign \(-\overline\beta_r\) and the same original image. It does not descend through \(\mathcal Q_+\) unless that image is zero: \(c\) acts as zero on the source normal quotient and as identity on \(\mathcal R\). The different source-return formula with \(c(s+1)\) lands in \(J\), exactly as claimed. ADM7.6 preserves both full normal kernels.

## ADM8: full-module contraction and action scope

The final text supplies the augmented base case: \(\epsilon a_{P^0}=0\) lifts through \(d^{-1}\). For \(j<0\), the identity
\[
d^j(a_{P^j}-H^{j+1}d^j)=0
\]
allows the next projective lift. Hence \(dH+Hd=a_P\). On the Hom complex with
\(Df=d_Yf-(-1)^nfd_P\), the specified \(Sf=(-1)^nfH\) gives
\(DS+SD=a_Y\): the terms containing \(d_YfH\) cancel, and centrality identifies \(fa_P\) with \(a_Yf\).

Taking \(a=1-c\) or \(a=c\) proves the four asserted full algebraic derived-Hom vanishings. The same homotopy proves that inclusion of either displayed normal kernel induces the stated derived-Hom equivalence with inverse induced by multiplication by \(c\). No finite-support hypothesis or continuous projective resolution is used.

The disk sheaf action uses the same coefficient multiplier in all form degrees. The sphere's finite cochain model separately uses \(h(s+1)\) in the top normal term. Since that last differential is zero, this is a valid cochain action, and at \(h(s)=n^s\) it has the required factor \(nT_n\). The weighted trace is retained with its own displayed factors. The quotient \(\mathcal R[1]\oplus\mathcal R(-1)[-1]\) carries the claimed action of \(c\); this does not imply that \(c\) is idempotent on the original entire-source complex.

## ADM9: exact cyclic-class comparison

ECR1's map \([h]\mapsto[e^{ts^2}h]\) is compatible with the full original-zero-jet ideal. Its composition with specialization has the displayed factor
\[
\overline{d_r(\rho)}e^{t(\rho^\#)^2}h(\rho^\#).
\]
For a finite off-line vector \(y\), prescribe precisely
\[
h(\rho^\#)
=\frac{y_\rho}{\overline{d_r(\rho)}e^{t(\rho^\#)^2}}
\]
on its support and zero jets at all remaining zeros. The existing full-jet isolators yield such an \(h\in\mathcal B\subset M\). All divisions occur at finitely many nonzero scalar values; no global inverse Gaussian in \(M\) is used. This proves the finite-coordinate image and the stated density. The kernel formula retains the quotient by the full jet ideal. No topology is introduced on the cyclic class module.

## Review corrections incorporated

The individual maximal-operator core proof now explicitly uses two graph-norm tails. Growth exponents in ADM2.1 are integer indexed. The augmented degree-zero start of the ADM8 induction is written out. ADM9 now states the finite prescribed values and explicitly excludes global Gaussian division. These changes make the written proofs explicit without changing the resulting maps or conclusions.

The scope of the final receipt is the exact SHA256 above. A subsequent mathematical edit requires review of the changed portion before this receipt applies to that edition.
