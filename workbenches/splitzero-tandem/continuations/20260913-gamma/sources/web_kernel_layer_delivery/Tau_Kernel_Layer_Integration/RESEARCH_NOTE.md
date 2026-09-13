# Full-jet interpolation kernels and the actual next relation layer

## Integration supplement — 12 September 2026

This supplement reviews the supplied **Coherent arithmetic interpolation and joint tensor boundary control** package and derives an additional finite-stage bridge. The source's canonical representative, original theta boundaries, full multiplicities, and support transport are retained. The new formulas below have written proofs and exact finite regression tests; they are **not new Lean certificates**.

The supplied ZIP has SHA-256 `a753df8341d05b2fccb6487b1dabc0044153a6c1abcf35092504aadb95c51d26`. All 29 entries of its manifest verified. Its note, handoff, and checker match the published Git blobs at PR #14, commit `3bff1b2bd87dfa2592f65c5ccc231f6ee9541dfc`. The source checker was independently rerun: nineteen tests passed normally and under optimized Python, with identical result records; the intentionally false twentieth test failed in both modes. See `SOURCE_REVIEW_RECEIPT.json`.

The comparison with PR #15 is limited precisely: its existing five-module receipt certifies its stated support-changing, relation-layer, finite-Krylov and rank-two interfaces. This supplement does not extend that receipt to the source's theta analytics, all-degree orthogonal-polynomial construction, or the new tensor-kernel calculations.

## 1. Source results retained, rather than reconstructed differently

Write the source polynomial degree as \(N\), to distinguish it from a moment matrix. Fix tensor degree \(k\ge1\), a nonempty packet polynomial \(h\) of degree \(d\), and \(N\ge k(d-1)\). The packet includes the complete orders of the selected actual zeros. Retain

\[
g=2\xi,\qquad E=E_h^{\otimes k},\qquad A=A_h^{(k)},\qquad
\mathcal J_N:\mathcal P_N^{(k)}\twoheadrightarrow E.
\tag{1}
\]

The last map is reduction modulo the original ideal
\((h(t_1),\ldots,h(t_k))\), followed by multiplication by the original local unit \(\upsilon_h^{\otimes k}\). Its kernel is \(\mathcal I_{k,N}\). The source map is

\[
\mathcal T(P)=P(D_1,\ldots,D_k)F_h^{\otimes k},\qquad
\mathcal M\mathcal T(P)=P(s_1,\ldots,s_k)\prod_i\frac{g(s_i)}{h(s_i)}.
\tag{2}
\]

Let \(\mathcal L_N=\mathcal T\mathcal I_{k,N}\), \(P_N=P_{\mathcal L_N}\), and let \(\sigma:E\hookrightarrow Q^{\widehat\otimes k}\) be the source arithmetic inclusion. Its canonical representative and forms are

\[
R_N=(I-P_N)s_h^{\otimes k},\qquad G_N=R_N^*R_N\succ0,
\qquad q^{(k)}R_N=\sigma,\quad J^{(k)}R_N=I,
\tag{3}
\]
\[
B_N=D^{(k)}R_N-R_NA,\qquad
W_N=A^*G_N+G_NA-kG_N.
\tag{4}
\]

The supplied note proves \(B_N(E)\subseteq\mathcal L_{N+1}\) and, with
\(\mathcal E_N=\mathcal L_{N+1}\cap\mathcal L_N^\perp\),

\[
Y_N=P_{\mathcal E_N}R_N,
\qquad C_N=(I-P_N)B_N,
\qquad W_N=-(Y_N^*C_N+C_N^*Y_N).
\tag{5}
\]

These are source results (source note, §§2–4 and 7–9), not claimed as discoveries of this supplement. Their finite-dimensional derivations check: the constrained minimum is over precisely the original ideal, the derivative increases total degree by one, and orthogonal projection removes only the admitted relation space. The source's exact sequence and packet naturality require full orders. Its total-degree statements require the threshold in (1). Its analytic function-space identities remain the stated analytic inputs, not consequences of a finite fixture.

The original coefficient square \(G(\mathbb Z)\to G(\mathbb C)\) over \(\mathbb Z\to\mathbb C\), with projections \(p_\mathbb Z,p_\mathbb C\), is unchanged. A vector in an admitted relation maps to the receiving fibre's supported zero, never to external absence \(\tau\).

## 2. Calculate the inverse interpolation metric by full-jet columns

Use exactly the source measure

\[
d\nu_h(t)=\left|\frac{g(1/2+it)}{h(1/2+it)}\right|^2\frac{dt}{2\pi}.
\tag{6}
\]

Let \(p_j^{(h)}(s)\) be its monic orthogonal polynomials, with the polynomial variable evaluated at \(s=1/2+it\), and retain their positive squared norms

\[
\kappa_j^{(h)}=\int|p_j^{(h)}(1/2+it)|^2d\nu_h(t)>0.
\tag{7}
\]

These are **not** the earlier theta-Krylov vectors \(u_j\), nor their norms \(\mathfrak h_j\). In particular they depend on \(h\); they are not assigned norm one. Existence through any finite degree follows from the source measure's positive-definite moment matrices. No limiting assertion is needed here.

Suppress \(h\) in notation. For a multi-index \(\alpha\), define

\[
p_\alpha=\prod_i p_{\alpha_i},\qquad
\kappa_\alpha=\prod_i\kappa_{\alpha_i},\qquad
a_j=\upsilon_h[p_j]_h\in E_h,\qquad
a_\alpha=\bigotimes_i a_{\alpha_i}\in E.
\tag{8}
\]

Every \(a_j\) is the full jet, including the local unit. Product orthogonality gives
\(\langle\mathcal T p_\alpha,\mathcal T p_\gamma\rangle=\kappa_\alpha\delta_{\alpha\gamma}\).
These polynomials form a basis of \(\mathcal P_N^{(k)}\), because the monic triangular basis change preserves total degree.

Set

\[
\boxed{K_N:=G_N^{-1}
=\sum_{|\alpha|\le N}\frac{a_\alpha a_\alpha^*}{\kappa_\alpha}.}
\tag{9}
\]

**Proof.** In this basis the source moment matrix is
\(\operatorname{diag}(\kappa_\alpha)\) and the full-jet matrix has columns \(a_\alpha\). Substitute into the source identity \(G_N^{-1}=J_NM_N^{-1}J_N^*\). A change of polynomial basis does not change that product. This proves (9) for the same canonical metric, not a newly selected metric.

Its representative has the explicit coefficient formula

\[
R_Nu=\sum_{|\alpha|\le N}\mathcal T(p_\alpha)
\frac{a_\alpha^*G_Nu}{\kappa_\alpha}.
\tag{10}
\]

In particular \(R_NK_N\) is an actual map from finite antidual coordinates into the original test-function space. It satisfies
\(J^{(k)}R_NK_N=K_N\) and \(q^{(k)}R_NK_N=\sigma K_N\).
The invertible coordinate change \(K_N\) is retained, not identified with the identity.

## 3. An explicit basis of the original next relation layer

Let \(\Sigma_{N+1}=\{\beta\in\mathbb N^k:|\beta|=N+1\}\). Define actual test functions

\[
\boxed{e_\beta=\mathcal T(p_\beta)-R_Na_\beta,
\qquad \beta\in\Sigma_{N+1}.}
\tag{11}
\]

They are in \(\mathcal E_N\). First, their full jets vanish by (3), so their numerator polynomials lie in the original ideal at degree at most \(N+1\); thus \(e_\beta\in\mathcal L_{N+1}\). Second, \(\mathcal T p_\beta\) is orthogonal to all degree-at-most-\(N\) polynomials and \(R_Na_\beta\) is orthogonal to \(\mathcal L_N\). Hence \(e_\beta\perp\mathcal L_N\).

Define

\[
\mathscr E_N:\mathbb C^{\Sigma_{N+1}}\longrightarrow\mathcal E_N,
\qquad c\longmapsto\sum_\beta c_\beta e_\beta,
\tag{12}
\]
\[
U_N=(a_\beta)_{\beta\in\Sigma_{N+1}},
\qquad D_N=\operatorname{diag}(\kappa_\beta)_{\beta\in\Sigma_{N+1}}.
\tag{13}
\]

The map \(\mathscr E_N\) is an isomorphism. Independence follows by taking the degree-\(N+1\) polynomial part of (11). For spanning, subtract from a relation its degree-\(N+1\) combination of the \(e_\beta\). The remainder is a relation of degree at most \(N\), hence belongs to \(\mathcal L_N\). An element of \(\mathcal E_N\) has no such remaining component.

Its Gram matrix and pairing with the representative are exactly

\[
\boxed{H_N:=\mathscr E_N^*\mathscr E_N
=D_N+U_N^*G_NU_N,\qquad
\mathscr E_N^*R_N=-U_N^*G_N.}
\tag{14}
\]

The cross terms vanish because the new-degree polynomials are orthogonal to the old polynomial space. In particular \(H_N\succ0\), and no original norm has been suppressed.

This identifies the existing quotient equivalence in coordinates:

\[
\mathbb C^{\Sigma_{N+1}}\xrightarrow{\mathscr E_N}\mathcal E_N
\xrightarrow{e\mapsto[e]}\mathcal L_{N+1}/\mathcal L_N.
\tag{15}
\]

The inverse quotient-to-layer map is the source's \([z]\mapsto(I-P_N)z\). For each nonzero coordinate vector, its class in this relative quotient is nonzero, and its image in the next admitted quotient is zero. At the split level this remains the next supported zero.

For an explicit theta primitive, form
\(p_\beta-\sum_{|\alpha|\le N}p_\alpha a_\alpha^*G_Na_\beta/\kappa_\alpha\).
Its full jet is zero. Fixed-order monic division expresses it as
\(\sum_i h(t_i)Q_{i,\beta}\), with \(\deg Q_{i,\beta}\le N+1-d\).
In the \(i\)-th cochain factor use the original \(\phi_*\) in place of \(F_h\), and multiply its primitive by \((-1)^{i-1}\). The differential supplies the same sign, producing the displayed relation with positive sign. This supplies the actual primitive, not just a dimension count.

## 4. Both boundary maps now have explicit coordinates

Define the matrix \(F_N:E\to\mathbb C^{\Sigma_{N+1}}\) by its rows

\[
(F_N)_\beta=\sum_{i:\beta_i>0}
\frac{a_{\beta-\mathbf e_i}^*}{\kappa_{\beta-\mathbf e_i}}.
\tag{16}
\]

Then

\[
\boxed{Y_N=-\mathscr E_NH_N^{-1}U_N^*G_N,
\qquad C_N=\mathscr E_NF_NG_N.}
\tag{17}
\]

The first equation is the actual orthogonal projection formula using (14).
For the second, multiply the finite expansion (10) by
\(s_1+\cdots+s_k\). Monicity implies that its degree-\(N+1\) coefficient at \(p_\beta\) is exactly \((F_N)_\beta G_Nu\). The term \(R_NAu\) has degree at most \(N\). Subtract \(\mathscr E_NF_NG_Nu\) from \(B_Nu\): the result has degree at most \(N\) and zero full jets, hence is in \(\mathcal L_N\). Projecting by \(I-P_N\) proves the equation.

Consequently the old quotient records

\[
\boxed{[B_Nu]_{\mathscr B^{(k)}/\mathcal L_N}
=[\mathscr E_NF_NG_Nu]_{\mathscr B^{(k)}/\mathcal L_N}.}
\tag{18}
\]

It becomes the supported zero under the next relation transition. The symbol
\(\mathscr B^{(k)}\) denotes the original product test-function space used by the source; no derivative on all of its \(L^2\) completion is defined here.

## 5. The control form is a top-degree full-jet endpoint

Define

\[
\boxed{V_N:=AK_N+K_NA^*-kK_N.}
\tag{19}
\]

Substituting (17) into the source boundary identity (5), and using
\(\mathscr E_N^*\mathscr E_N=H_N\), gives

\[
\boxed{W_N=G_N\bigl(U_NF_N+F_N^*U_N^*\bigr)G_N.}
\tag{20}
\]

Meanwhile direct multiplication of (4) by \(K_N\) on both sides gives
\(K_NW_NK_N=V_N\). Thus

\[
\boxed{V_N=U_NF_N+F_N^*U_N^*
=\sum_{|\alpha|=N}\sum_{i=1}^k
\frac{a_{\alpha+\mathbf e_i}a_\alpha^*
+a_\alpha a_{\alpha+\mathbf e_i}^*}{\kappa_\alpha}.}
\tag{21}
\]

This is a finite endpoint identity derived through the actual theta relation layer. It does not assume a small boundary, discard mixed terms, or replace the packet operator. It can also be obtained by finite Christoffel–Darboux telescoping. The standard scalar orthogonal-polynomial kernel and telescoping identities are recorded by NIST (n.d., §18.2(v)); the full-jet, original-layer identification (11)–(21) is proved here rather than imported from that scalar formula.

For this alternative telescoping proof, multiplication satisfies
\(s p_j=p_{j+1}+\beta_jp_j-(\kappa_j/\kappa_{j-1})p_{j-1}\), with
\(\operatorname{Re}\beta_j=1/2\). The imaginary part need not vanish for the packet-dependent measure. Only \(\beta_j+\overline{\beta_j}=1\) is needed. Interior adjacent terms cancel; (21) is the uncancelled total-degree boundary. The new tests include an asymmetric measure with a nonzero imaginary diagonal coefficient.

Regroup by \(\alpha\) and put \(b_\alpha=\sum_i a_{\alpha+\mathbf e_i}\).
Equation (21) factors through the two sets of columns \((a_\alpha)_{|\alpha|=N}\) and \((b_\alpha)_{|\alpha|=N}\). Therefore

\[
\boxed{\operatorname{rank}W_N=\operatorname{rank}V_N
\le\min\left\{d^k,\;2\binom{N+k-1}{k-1}\right\}.}
\tag{22}
\]

This sharpens the source's general next-layer bound
\(2\binom{N+k}{k-1}\) for this product-polynomial construction. It does **not** change the actual dimension of \(\mathcal E_N\), which remains
\(\binom{N+k}{k-1}\). The sharpening comes from the scalar summed derivative and regrouping its top-degree columns. For \(k=2,d=4,N=6\), the two structural bounds are 14 and 16 on a 16-dimensional packet; the exact regression tests cover this nonvacuous case. Neither rank bound is a small-eigenvalue estimate.

## 6. Estimate the same form without a second inversion

Since \(K_N\) is Hermitian positive definite,

\[
\boxed{-\epsilon G_N\preceq W_N\preceq\epsilon G_N
\quad\Longleftrightarrow\quad
-\epsilon K_N\preceq V_N\preceq\epsilon K_N.}
\tag{23}
\]

This is congruence by the specified invertible map \(K_N\). More explicitly, for \(u=K_N\lambda\),
\(u^*G_Nu=\lambda^*K_N\lambda\) and
\(u^*W_Nu=\lambda^*V_N\lambda\). This identifies the generalized Rayleigh quotients, including multiplicities of generalized eigenvalues. The original generator \(A\) is not replaced.

The source's same-metric reflection therefore still transfers an upper estimate to a lower estimate for precisely the original \(G_N\). Under the natural weight-\(k\) antidual action \(A^{\mathrm D}=kI-A^*\), the defect of the antidual metric \(K_N\) is \(-V_N\), not \(V_N\). The dual sign and weight are both retained.

The reflection map itself can be retained explicitly. If the source involution is \(j(u)=C\overline u\), its antidual involution is \(j^\#(\lambda)=C^T\overline\lambda\). From \(C\overline C=I\) and \(C^*G_NC=\overline{G_N}\), inversion gives \((C^T)^*K_NC^T=\overline{K_N}\). The control identity transports to \((C^T)^*V_NC^T=-\overline{V_N}\). Thus the two-sided equivalence retains the actual involution, not only spectral symmetry.

Equation (23) avoids the *second* inversion \(G_N=K_N^{-1}\) in the final inequality test. It does not eliminate the need to enclose moments, full-jet coefficients, or the conditioning of the first construction of \(K_N\).

A deterministic finite certificate can therefore work directly with
\(\widehat K,\widehat A\) and error bounds
\(\|K_N-\widehat K\|\le\eta_K\),
\(\|A-\widehat A\|\le\eta_A\), where \(\widehat K\) is Hermitian. Put

\[
\widehat V=\widehat A\widehat K+\widehat K\widehat A^*-k\widehat K,
\qquad
\eta_V=(2\|\widehat A\|+k)\eta_K
+2\eta_A(\|\widehat K\|+\eta_K).
\tag{24}
\]

Expanding both perturbations proves \(\|V_N-\widehat V\|\le\eta_V\).
Sufficient conditions, for \(\epsilon\ge0\), are

\[
\widehat K-\eta_KI\succ0,\qquad
\epsilon\widehat K\pm\widehat V
-(\epsilon\eta_K+\eta_V)I\succeq0.
\tag{25}
\]

No enclosure of the actual infinite arithmetic moments is asserted in this supplement.

## 7. The metric update and the univariate connection

The positive update from (9) and its inverse are

\[
\boxed{K_{N+1}=K_N+U_ND_N^{-1}U_N^*,}
\tag{26}
\]
\[
\boxed{G_{N+1}=G_N-G_NU_N(D_N+U_N^*G_NU_N)^{-1}U_N^*G_N.}
\tag{27}
\]

Equation (27) follows either by direct multiplication with (26), or from
\(R_{N+1}=R_N-Y_N\) and the orthogonal decomposition. The middle matrix is exactly the actual layer Gram matrix \(H_N\) in (14), not an unrelated auxiliary matrix. The lost Gram form is \(Y_N^*Y_N\).

For \(k=1\) and \(N=n+d\), (11) recovers the earlier monic theta vector:

\[
\boxed{e_{n+d+1}=u_{n+1},\qquad
\mathfrak h_{n+1}=\kappa_{n+d+1}^{(h)}
+a_{n+d+1}^*G_{h,n}a_{n+d+1}.}
\tag{28}
\]

Indeed the numerator of (11) is monic of degree \(n+d+1\), divisible by monic \(h\), and its quotient has degree \(n+1\) and leading coefficient one. Applying \(\mathcal T_h\) gives \(f_{n+1}\) plus an element of \(L_n\), orthogonal to \(L_n\). This uniquely identifies \(u_{n+1}\). Thus the packet-dependent polynomial construction is connected to the packet-independent original theta norm by an exact identity; those two norm families were not conflated.

## 8. Degree recursion and the remaining estimate

For \(A_j=a_ja_j^*/\kappa_j\), define finite matrix sums

\[
Q_{k,m}=\sum_{|\alpha|=m}\bigotimes_i A_{\alpha_i},\qquad
Q_{k,m}=\sum_{j=0}^m A_j\otimes Q_{k-1,m-j},\qquad
K_{k,N}=\sum_{m=0}^NQ_{k,m}.
\tag{29}
\]

These are finite degree convolutions; they do not assert convergence of an infinite generating series. They compute the product full-jet interpolation matrix using one-variable polynomial norms and jets, without inverting a total-degree moment matrix of dimension \(\binom{N+k}{k}\). The target dimension remains \(d^k\); no polynomial-time complexity or unconditional numerical stability is claimed.

In univariate packet inclusions, the source's exact equality
\(R_{H,n}\iota_{hH}=R_{h,n}\) remains in force. The packet-dependent polynomial bases used here need not themselves commute under inclusion. No extension of this univariate equality to different joint total-degree budgets is presumed.

Finally, on \(Av=k\rho v\), with \(v=v_0^{\otimes k}\), and \(\lambda=G_Nv\),

\[
\frac{\lambda^*V_N\lambda}{\lambda^*K_N\lambda}
=k(2\operatorname{Re}\rho-1).
\tag{30}
\]

The additional work is therefore the explicit layer basis, derivative-coordinate map, endpoint identity, and direct relative certificate for the same source-controlled object. It is not a proof of a uniform sublinear excess. No arithmetic block or nilpotent jet has been removed.

## Verification and literature scope

The independent new checker contains eighteen exact test methods. They cover the kernel basis change, repeated jets, two-variable layers, actual derivative-class coordinates, Gram updates, the original univariate theta vector, endpoint factorization, a nonvacuous improved rank bound, antidual signs, generalized characteristic polynomials, nonzero off-line *polynomial model* diagnostics, nonreal recurrence diagonals, fixed-order theta primitives, and deterministic matrix perturbation certificates. Normal and optimized result records agree. Both intentional-failure modes return failure.

These are finite regression tests, not proofs of the general analytic inputs and not Lean execution. The general finite identities have the written proofs above. The source's nineteen tests and this supplement's eighteen tests are separate suites, not counts of novel theorems.

The matrix-kernel and Christoffel–Darboux methods have established antecedents. NIST's general orthogonal-polynomial formulas supply the standard scalar comparison. Lasserre and Pauwels (2016) connect inverse moment matrices with orthogonal polynomials and the Christoffel function; only their abstract was examined here, so no theorem from that paper is used as a premise. No global priority claim is made for standard kernel or inverse-update identities.

### References

*Coherent arithmetic interpolation and joint tensor boundary control*. (2026, September 12). Zeta-function-research-reader research workbench, draft PR #14, commit `3bff1b2bd87dfa2592f65c5ccc231f6ee9541dfc`. https://github.com/KokunoYumeto/zeta-function-research-reader/pull/14

*Formalize support-changing relation layers and the Krylov boundary-control calculation*. (2026, September 12). Zeta-function-research-reader research workbench, draft PR #15, verified source commit `21970bbf4760d0bbca512a4a7996a2e38f968947`. https://github.com/KokunoYumeto/zeta-function-research-reader/pull/15

Lasserre, J.-B., & Pauwels, E. (2016). *Sorting out typicality with the inverse moment matrix SOS polynomial* [Preprint]. arXiv. https://arxiv.org/abs/1606.03858

National Institute of Standards and Technology. (n.d.). *Digital Library of Mathematical Functions*, §18.2(v), Christoffel–Darboux formula. https://dlmf.nist.gov/18.2#v
