# Independent review of the universal receiver, positive forms, and multiplicity trace

24 September 2026. Scoped review of POSITIVE_TRANSFER_UNIVERSAL_QUOTIENT.md at SHA256 b70a8f0edf765dcfb3259735eb4a8f90a31c649ad308f55d821dcf5cccdae930.

No repair was found necessary for the claims reviewed here.

## Coverage and scope

The independent proof verification in this review covers the definitions and constructions PTQ0–PTQ2, the complete universal property PTQ3, the complete bounded-positive-form classification PTQ4, and the complete multiplicity-weighted trace calculation PTQ8. The finite two-point orbit and sign convention PTQ5.3–PTQ5.4 were checked where used in PTQ8. The rest of PTQ5–PTQ11 is not certified as a separate complete proof audit by this review.

The source spaces, full divisor, multiplicities and operator formulas are the ones already read in GTAH0–GTAH7 and RTT0–RTT11 during this independent-review session. The corresponding source, residue and class-map checks are recorded separately in EXTENSION_CLASS_SOURCE_INDEPENDENT_AUDIT.md, EXTENSION_CLASS_INVOLUTION_AUDIT.md and POSITIVE_QUOTIENT_SOURCE_AUDIT.md. No new complete reading of their human-source bibliography is claimed. All coefficient operations follow the established arithmetic reconstruction; no operation or numerical coordinate is assigned to the support or its information layers.

## Universal receiver

The ranges in PTQ1 are supported off the line. Every finite off-line coordinate vector is the image of a finite vector after division by its finitely many nonzero defect coefficients. Their closure is therefore exactly \(H_{\rm off}\), without asserting a bounded reciprocal or a closed range. Dominated convergence in the original multiplicity-weighted square norm proves the strong exponential limits. Both coordinate subspaces reduce the specified original operators. On the retained coordinates the identity \(n^{\overline\rho}=n^{1-\rho}\) gives PTQ2.2, preserving the degree \(n\).

In the stated receiving category,
\[
B_n=A_n^*,\qquad B_nA_n=A_nB_n=nI
\]
imply \(A_n^*A_n=nI\). For the original coordinate vector \(\varepsilon_\rho\), the intertwiner gives
\[
A_nX\varepsilon_\rho=n^\rho X\varepsilon_\rho.
\]
Taking squared norms produces exactly
\[
n\|X\varepsilon_\rho\|^2
=n^{2\Re\rho}\|X\varepsilon_\rho\|^2.
\]
For any recovered \(n>1\), the two scalars differ off the line. Hence \(X\) kills each such coordinate and, by boundedness, all of \(H_{\rm off}\). The quotient factor is well defined by \(Yq_{\rm pos}x=Xx\), is unique because the quotient is onto, and is bounded by testing its unique line representative. Moreover \(X=XP_{\rm line}\) gives
\[
\|Y\|=\|X|_{H_{\rm line}}\|=\|X\|.
\]
The quotient intertwining identities follow by composing with the surjective quotient map. This is the required universal property in the explicitly stated bounded Hilbert category.

PTQ3's smaller-image observation is valid as well. The closed span of \(X(H)\) is invariant under \(A_n,B_n\), by the intertwining relations and boundedness. On its dense image the original degree identity gives \(B_nA_n=nI\), which extends continuously to that closed span. If \(B_n=A_n^*\) there, the same norm argument applies. No claim about arbitrary algebraic maps from the entire source or an untopologized Ext group follows.

## Classification of bounded positive forms

The equivalence of PTQ4.1 and PTQ4.2 uses \(U_nT_n=nI\) in one direction and \(U_n=nT_n^{-1}\) in the other. The coefficient \(n\) is real, so its location in the conjugate-linear argument causes no change.

For a positive semidefinite Hermitian form, Cauchy–Schwarz shows that a vector with zero diagonal value pairs to zero with every vector. Applying the degree identity to \(\varepsilon_\rho\) therefore kills every off-line row and column of the form.

For distinct retained zeros, put \(\delta=\Im\rho-\Im\eta\). A nonzero cross coefficient would force \(e^{i\delta\log n}=1\) for every recovered positive integer. Dividing the phases at consecutive integers gives
\[
e^{i\delta\log(1+1/n)}=1.
\]
If \(\delta\ne0\), then for sufficiently large \(n\),
\[
0<|\delta|\log(1+1/n)<2\pi,
\]
which is impossible for a real exponent whose complex exponential is one. Thus \(\delta=0\), and two retained zeros with that same frequency are the same complex point. Every distinct cross coefficient consequently vanishes. This uses the already reconstructed complete integer family.

The coordinate norm is \(\|\varepsilon_\rho\|^2=m_\rho\). Therefore
\[
c_\rho=\frac{B(\varepsilon_\rho,\varepsilon_\rho)}{m_\rho}
\]
is nonnegative and bounded uniformly by the bound of \(B\). Finite-coordinate expansion gives PTQ4.3, and the estimate
\[
\left|\sum_{\rho\in\mathscr Z_{\rm line}}
m_\rho c_\rho x_\rho\overline{y_\rho}\right|
\le C\|x\|_+\|y\|_+
\]
extends the identity to the complete Hilbert space. Conversely every displayed nonnegative bounded family defines such a form and satisfies the transfer-adjoint relation by direct substitution. The maximality under the bound \(B(x,x)\le\|x\|_+^2\) is precisely the coordinate inequality \(c_\rho\le1\). Pullback along any PTQ3 intertwiner satisfies the same relation, so it belongs to this classification.

This classification is for the stated value Hilbert space with one coordinate per distinct zero and its original weight \(m_\rho\). It is not a classification of unrestricted forms on full local jet algebras.

## Multiplicity trace

For a diagonal value observable, PTQ8 uses the stipulated weight
\[
\operatorname{tr}_\zeta(M_f)=\sum_\rho m_\rho f(\rho).
\]
This differs from the ordinary Hilbert operator trace on \(H\): the orthonormal vector at a distinct zero is \(\varepsilon_\rho/\sqrt{m_\rho}\), and its operator eigenvalue is only \(f(\rho)\). The factor \(m_\rho\) is instead exactly the trace of multiplication by a local germ on the original length-\(m_\rho\) algebra, where every diagonal entry is its value \(f(\rho)\). For a holomorphic germ it is also the coefficient of \((s-\rho)^{-1}\) in \(f(s)\zeta'(s)/\zeta(s)\). Arbitrary value observables here do not assert a global entire interpolation.

For nonnegative sequences the trace identities are extended nonnegative sums; for complex sequences they are used under absolute summability. No unbounded-operator product is needed to establish these coefficientwise identities. The projection partition proves PTQ8.2 in both stated domains.

The full zero count and the Gaussian \(e^{-t\gamma^2}\) make both sector sums finite. Reflection \(\rho\mapsto\rho^\#\) preserves \(\gamma\) and multiplicity, and every off-line orbit has exactly two distinct elements. This verifies the factor \(2m_\rho\) in PTQ8.3. Strict positivity of every weight proves its exact zero criterion without assuming either outcome.

The defect vanishes on line coordinates, and
\[
|n^\sigma-n^{1-\sigma}|\le n-1
\qquad(0<\sigma<1)
\]
proves absolute convergence in PTQ8.4. Reflection negates the difference and hence preserves its square, so the two orbit terms add. On a two-coordinate orbit the finite-dimensional multiplicity trace is \(m_\rho\operatorname{Tr}\); it gives zero on the exchange matrix and \(2m_\rho\) on the identity. Thus the comparison with PTQ5.4 is valid and does not remove either value direction.

The last paragraph of PTQ8 correctly keeps these diagonal observables outside the original holomorphic prime explicit formula. The reviewed results preserve the complete integer cover degrees, original multiplicities, and bounded-map domains; they assert no arbitrary source projector or vanishing of the original defect.
