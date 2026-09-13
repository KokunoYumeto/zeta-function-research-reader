# Independent review of the positive-form comparator supplement

**Final reviewed source: 24653 bytes, SHA-256 `105bc6884528e03b3f6aa15d9a7c34643c4bb3fb97c03451b3d3bf9499ef3dc9`. All RM.1–RM.35 finite identities pass. All requested domain/prose corrections are incorporated.** The earlier draft pins and findings below are retained as the exact review history; the terminal binding is in section 11.

Date: 2026-09-13. The complete source `workspace:/work/relation_moment_comparison_proof_20260913.tex` was read through all formulas RM.1–RM.31 and every intervening paragraph. Reviewed draft size: 21422 bytes; SHA-256: `8b638ead855aaccdcc5de46c274384313395a1156512e1e57ee9dc72aa266777`. The original delivered NOTE/RESEARCH_NOTE has a separate complete, source-pinned review at `work/relation_moment_independent_review_20260913.md`, SHA-256 `d4638ba723515cb151e9b04c8da99fd004f092bab48f1d80ebc25daa79d9b01f`.

This is a mathematical source review, not an execution receipt. No package test, Lean process, global-paper edit, or publication action was performed by this reviewer. The arithmetic construction of the concrete upper form is covered by the root's full arithmetic-comparison proof; this review verifies every finite map and inequality composing that actual form with the relation cost.

## Disposition and required source precision

The comparator quotient, its source map and adjoint, the contraction from the original new-column source, its exact kernel, the cost-action defect, the literal Gaussian matrices, and the rank refinement all pass independent derivation. RM.1–RM.19 reproduce the previously reviewed finite proof correctly, including the correction that zero cost gives a ratio of one and a zero logarithm.

The reviewed draft needs these small domain/prose edits:

1. Immediately after RM.16, replace “The integral is strictly positive away from \(x=a,b\)” by “The remainder in RM.15 is strictly positive on \([0,a]\setminus\{a,b\}\).” The integral itself is positive at the two nodes as well; the polynomial prefactor vanishes there.
2. Before RM.19, explicitly retain \(q\ge2\) together with \(t_1>0\), since it divides by \(q-1\). RM.17–RM.18 use the \(a,b\) defined for \(q\ge2\), with the degenerate equal-spectrum case already handled.
3. In RM.21, the displayed \(a_+,b_+\) formula likewise has domain \(q\ge2\). For \(q=1\), keep the exact upper-comparator determinant \(\det(1+Z_+)=1+t_1^+\); for \(q=0\), use the empty determinant separately.
4. The calibration paragraph saying “The operator formulas (RM.1)–(RM.25) retain \(i=j\) as well” is too broad as a formula-range assertion: RM.19 has \(t_1=0\) when \(i=j\) and its division is undefined. State that the original and comparator **maps** admit \(i=j\), while scalar formulas retain their stated dimension and positive-trace domains and zero cost is handled by the explicit zero case. The window formulas still require \(i<j\).

None of these changes affects the nonempty positive-dimensional endpoint application. They make the standalone statement correct on every claimed boundary. The exact comparator-excess identity proved in section 5 of this review is a useful additional completion of RM.24; it introduces no missing estimate.

## 1. RM.1–RM.10: original maps and action

Surjectivity of \(B_N\) follows because the remainders of the first \(q\) monic polynomials have an invertible triangular coefficient matrix in \(1,S,\ldots,S^{q-1}\). Hence \(K_N=B_NO_N^{-1}B_N^*\) is positive definite. Direct multiplication gives
\[
B_NR_N=I_E,\qquad R_N^*O_NR_N=G_N,
\qquad (\ker B_N)\perp_{O_N}\operatorname{im}R_N.
\]
The source embedding \(R_N:(E,G_N)\to\mathcal P_N\) is therefore an isometry onto the unique least-norm representatives, without any rescaling of \(\omega_n\).

For \(U=(\mathbb C^r,\Omega)\), the actual new-column map \(F:U\to E_i\) has \(F^\dagger=\Omega^{-1}F^*G_i\). The endpoint metric adjoint of the coordinate identity is \(T=K_iG_j\); composing before inversion gives
\[
Q=TI,
\qquad Q^{-1}=K_jG_i,
\qquad Z=(K_j-K_i)G_i=FF^\dagger,
\qquad G_iZ=G_i(K_j-K_i)G_i\succeq0.
\]
Thus \(Q=(I_E+Z)^{-1}\) and \(V_i/V_j=\det(I_E+Z)\), retaining all \(q\) eigenvalues including zeros. With
\(\mathsf H_N=K_NA^*G_N+A-kI_E\), cancellation in the stated original coordinates proves
\[
\mathsf H_iQ-Q\widehat{\mathsf H}_j=[A,Q],
\]
and conjugating the commutator through the inverse gives RM.5 exactly:
\[
[A,Z]=\widehat{\mathsf H}_j(I_E+Z)-(I_E+Z)\mathsf H_i.
\]

For \(\Phi=R_iF\), cyclicity yields \(t_1=\operatorname{Tr}(\Phi^\dagger\Phi)\), while expanding its squared trace gives all terms \(|b_n^*G_ib_m|^2/(\omega_n\omega_m)\) of RM.7. Removing the diagonal terms and grouping each unordered pair twice proves RM.8 with its exact factor \(1/2\). Determinant Grams on exterior quotient bases give the exact squared norm \(\mathcal A_2=\|\bigwedge^2\Phi\|_{\rm HS}^2\). Applying the unscaled alternating-tensor map in both domain and codomain multiplies both wedge Grams by \(2!\), which proves the stated relation between conventions rather than identifying them.

The actual column insertions satisfy \(N^*O_jL=0\), \(N^*O_jN=\Omega\), and \(L^*O_jL=O_i\). Consequently
\[
\mathfrak b=N-LR_iF,
\quad B_j\mathfrak b=F-B_iR_iF=0,
\quad \mathfrak b^*O_j\mathfrak b=\Omega+F^*G_iF.
\]
The column polynomial \(p_n-\sum_{\ell\le i}(R_ib_n)_\ell p_\ell\) is divisible by the full \(\chi\). Applying the original arithmetic realization and the displayed commuting quotient maps therefore gives the receiving represented zero with the original label, not source absence. The fibre \(p_R^{-1}(0_R)=\{0_R^\bullet,\tau\}\) explicitly records the two source values having that same amplitude.

## 2. RM.11–RM.19: cap, sharpness, and exact positive remainder

For \(q\ge2\), the exact identities
\[
qt_2-t_1^2=\sum_{\alpha<\beta}(\lambda_\alpha-\lambda_\beta)^2\ge0,
\quad t_1^2-t_2=2\sum_{\alpha<\beta}\lambda_\alpha\lambda_\beta\ge0
\]
prove \(0\le d\le t_1\), \(0\le b\le a\), and the displayed two-moment realization. An individual eigenvalue \(x\) satisfies
\[
qx^2-2t_1x+t_1^2-(q-1)t_2\le0,
\]
whose upper root is precisely \(a\). Hence the full actual spectrum lies in \([0,a]\).

For fixed \(s\ge1\), the interpolation polynomial in RM.12 is for \((s+x)^{-1}\). Its coefficients give the direct identity
\[
\frac1{s+x}-H_s(x)
=\frac{(a-x)(x-b)^2}{(s+x)(s+b)^2(s+a)}.
\]
Subtracting from \(1/s\) and integrating proves RM.14–RM.15 with the given sign. The quadratic coefficient is the strictly negative convergent integral
\[
c=-\int_1^\infty\frac{ds}{(s+a)(s+b)^2}.
\]
The two moment identities imply \(\operatorname{Tr}P(Z)=P(a)+(q-1)P(b)\), so the nonnegative remainder gives RM.16. Equality for \(a>b\) requires every eigenvalue to be \(a\) or \(b\); the first trace then forces exactly one \(a\). That spectrum is feasible for the two-moment problem, proving the claimed optimality. Equal variance gives \(Z=bI_E\), and dimensions one and zero have the independently stated exact determinants.

Expanding \((a-x)(x-b)^2\) proves RM.17. Finite spectral summation of the integral proves RM.18. On the proven spectral interval its denominator is at most \((s+a)^4\), so the remainder is at least \(C_3/(3(1+a)^3)\), with no action-commutation assumption. The full arithmetic action remains related by RM.5.

For \(q\ge2\), \(t_1>0\), the identity
\[
\mathcal A_2=(q-1)b(t_1-qb/2),\quad 0\le b\le t_1/q
\]
puts the last factor between \(t_1/2\) and \(t_1\), proving both bounds on \(b\) and RM.19. At \(\mathcal A_2=0<t_1\), all distinct eigenvalue pair products vanish, leaving exactly one positive eigenvalue; the determinant is \(1+t_1\). At \(i=j\), \(t_1=0\), so this formula is replaced by the established zero-cost result.

## 3. RM.20–RM.21: original-metric upper-form comparison

The concrete arithmetic upper construction supplies the same-coordinate dual-form inequality
\[
U_j\succeq K_j\succeq K_i.
\]
Retaining \(G_i=K_i^{-1}\), define
\[
D_+=U_j-K_i,
\quad Z_+=D_+G_i,
\quad \Delta=U_j-K_j.
\]
Then \(D_+\succeq D\succeq0\), and
\[
G_i(Z_+-Z)=G_i\Delta G_i\succeq0.
\]
Both endomorphisms are self-adjoint in the same original \(G_i\) metric. Order their eigenvalues decreasingly. For a self-adjoint \(X\), the top \(m\) eigenvectors span a subspace whose minimum Rayleigh quotient is \(\lambda_m(X)\). Every other \(m\)-dimensional subspace intersects the span of eigenvectors numbered \(m,\ldots,q\), since the two dimensions sum to \(q+1\); a nonzero vector in that intersection has quotient at most \(\lambda_m(X)\). These two facts prove the exact max–min formula stated in the source.

The form inequality applied inside that formula gives \(\lambda_m(Z_+)\ge\lambda_m(Z)\) for every retained coordinate index. Therefore
\[
\frac{V_i}{V_j}=\prod_{m=1}^q(1+\lambda_m(Z))
\le\prod_{m=1}^q(1+\lambda_m(Z_+))
=\det(U_jG_i).
\]
For \(q\ge2\), applying the proved two-trace optimization to \(Z_+\) then gives RM.21. For \(q=1\), its exact determinant is \(1+t_1^+\). This argument uses the original form order and a separately valid scalar bound; it does not assume an unsupported componentwise monotonicity of the optimized expression in two independently varied trace inputs.

Likewise \(Z\preceq Z_+\preceq a_+I_E\) proves \(Q\succeq(1+a_+)^{-1}I_E\). The required arithmetic input for \(K_i,G_i\) stops at degree \(2i\), while the explicit comparison measure determines its own upper kernel through degree \(2j\). For the displayed endpoint indices \(i\le q\), \(j\le2q\), those are respectively \(2q\) and \(4q\). The new traces of \(Z_+\) require no actual arithmetic moments beyond the first cutoff; the exact map proof can retain the actual high-column map \(F\) without needing to compute it as an input to this numerical upper certificate.

## 4. RM.22–RM.24: quotient form, adjoint, and actual contraction

Let \(E^\vee\) denote the fixed conjugate-dual coefficient space used by the positive dual form \(D_+\). Put
\[
\mathcal C_+=E^\vee/\ker D_+,
\qquad \langle[\alpha],[\beta]\rangle_+=\alpha^*D_+\beta.
\]
For a positive Hermitian matrix, diagonalization with nonnegative eigenvalues gives
\(\alpha^*D_+\alpha=0\) if and only if \(D_+\alpha=0\). Thus the displayed quotient inner product is positive definite and well-defined; its dimension is exactly \(\operatorname{rank}D_+\). No modification to \(G_i\) occurs in that argument.

The map
\[
J_+:\mathcal C_+\to E_i,\qquad J_+[\alpha]=D_+\alpha
\]
is well-defined and injective, with image \(\operatorname{im}D_+\). Its adjoint is
\[
J_+^\dagger v=[G_iv],
\]
because \(\langle J_+[\alpha],v\rangle_{G_i}=\alpha^*D_+G_iv=\langle[\alpha],[G_iv]\rangle_+\). Consequently
\[
J_+J_+^\dagger=D_+G_i=Z_+.
\]
For \(\Phi_+=R_iJ_+\), the exact isometry \(R_i\) implies
\(\Phi_+^\dagger\Phi_+=J_+^\dagger J_+\). Its nonzero eigenvalues equal those of \(Z_+\): on each positive eigenvalue \(\lambda\), the maps \(J_+\) and \(\lambda^{-1}J_+^\dagger\) are inverse. The remaining eigenvalues on either ambient space are zero and retain their multiplicities. Therefore
\[
\|\Phi_+\|_{\rm HS}^2=\operatorname{Tr}Z_+,
\qquad \|\bigwedge^2\Phi_+\|_{\rm HS}^2
=\sum_{\alpha<\beta}\lambda_\alpha(Z_+)\lambda_\beta(Z_+)
=\frac{(t_1^+)^2-t_2^+}{2}.
\]
This proves the full typed content of RM.23, including singular \(D_+\).

If \(\alpha\in\ker D_+\), then
\[
0\le\alpha^*D\alpha\le\alpha^*D_+\alpha=0,
\]
and \(D=F\Omega^{-1}F^*\) yields \(F^*\alpha=0\). In finite dimensions \(\operatorname{im}D_+=(\ker D_+)^\perp\), so every \(Fv\) belongs to that image. The equation \(D_+u=Fv\) therefore has a solution, and its entire solution set is one class modulo \(\ker D_+\). This proves that
\[
C:U\to\mathcal C_+,\qquad Cv=[u]\text{ with }D_+u=Fv
\]
is a well-defined linear map, \(J_+C=F\), and \(\Phi_+C=\Phi\). Its norm is calculated in the same quotient form. Set \(s=u^*D_+u=u^*Fv\ge0\). Cauchy–Schwarz in the literal \(\Omega\) metric gives
\[
s=|u^*Fv|\le\sqrt{u^*F\Omega^{-1}F^*u}\sqrt{v^*\Omega v}
\le\sqrt{s}\sqrt{v^*\Omega v}.
\]
If \(s>0\), dividing gives \(s\le v^*\Omega v\); if \(s=0\), that conclusion is immediate. Thus \(C\) is a contraction. Since \(J_+\) is injective, \(\ker C=\ker F\). Applying \(\bigwedge^2\) to the actual composition gives exactly the source diagram for the exterior areas; no admitted source pair is removed by that composition.

The zero case is complete: if \(D_+=0\), then \(D=0\), \(F=0\), \(\mathcal C_+\) is the zero Hilbert space, and each of \(J_+,C,\Phi_+\) is the unique typed zero map. Both comparator traces vanish and the determinant ratio is one. If \(r=0\), the original source is zero-dimensional even if \(D_+\ne0\); its contraction is the unique map from that zero space and the comparator excess remains present.

## 5. Exact comparator excess as the contraction defect

This is a directly proved extension of RM.24 which retains the full difference between the two cost maps. For every source class,
\[
C^\dagger[\alpha]=\Omega^{-1}F^*\alpha.
\]
It is well-defined because \(F^*\ker D_+=0\). To verify the adjoint formula, if \(Cv=[u]\), then
\[
\langle Cv,[\alpha]\rangle_+
=u^*D_+\alpha=(D_+u)^*\alpha=(Fv)^*\alpha
=v^*\Omega(\Omega^{-1}F^*\alpha).
\]
Now \(D_+\) applied to a representative of \(CC^\dagger[\beta]\) equals
\(F\Omega^{-1}F^*\beta=D\beta\). Hence
\[
\langle[\alpha],(I_{\mathcal C_+}-CC^\dagger)[\beta]\rangle_+
=\alpha^*(D_+-D)\beta
=\alpha^*\Delta\beta.
\]
This expression is independent of representatives because \(0\preceq\Delta\preceq D_+\) implies \(\ker D_+\subseteq\ker\Delta\). It proves the positive contraction defect in the quotient form and the exact original-metric pushforward
\[
J_+(I_{\mathcal C_+}-CC^\dagger)J_+^\dagger
=\Delta G_i
=Z_+-Z.
\]
Thus the comparator's additional positive cost is precisely the image of the contraction defect. Neither that cost nor the original source kernel is discarded.

For completeness, this construction is natural under an arbitrary invertible quotient-coordinate change \(P:E\to E'\). The matrices transform as
\[
D_+'=PD_+P^*,\quad G_i'=P^{-*}G_iP^{-1},\quad F'=PF.
\]
The induced map of positive-form sources is the isometry
\[
\widehat P:\mathcal C_+\to\mathcal C_+',\qquad
[\alpha]\mapsto[P^{-*}\alpha].
\]
Direct multiplication proves
\(\langle\widehat P[\alpha],\widehat P[\beta]\rangle_+'=\alpha^*D_+\beta\),
\(J_+'\widehat P=PJ_+\), and \(C'=\widehat PC\). This is the precise coordinate morphism, including any original derivative factorials in \(P\); no square root or new arithmetic metric is required.

## 6. RM.25: the complete cost-action defect

Since \(Z_+=Z+\Delta G_i\), substitute RM.5 and add the exact difference:
\[
[A,Z_+]=\widehat{\mathsf H}_j(I_E+Z_+)-(I_E+Z_+)\mathsf H_i+\mathcal E,
\]
where
\[
\mathcal E=[A,\Delta G_i]-\widehat{\mathsf H}_j\Delta G_i
+\Delta G_i\mathsf H_i.
\]
Use the original matrices
\(\widehat{\mathsf H}_j=A+K_jA^*G_j-kI_E\),
\(\mathsf H_i=A+K_iA^*G_i-kI_E\), and \(G_iK_i=I_E\). Expanding all terms gives
\[
\begin{aligned}
\mathcal E={}&A\Delta G_i-\Delta G_iA-A\Delta G_i
-K_jA^*G_j\Delta G_i+k\Delta G_i\\
&+\Delta G_iA+\Delta A^*G_i-k\Delta G_i\\
={}&\Delta A^*G_i-K_jA^*G_j\Delta G_i.
\end{aligned}
\]
The order of every noncommuting factor in RM.25 is therefore correct. The auxiliary symbol \(W_j\) defined just before this display is not used in the displayed calculation; this is harmless unused notation, not a mathematical error. No smallness or action-invariance assertion has been substituted for \(\mathcal E\).

## 7. RM.26–RM.27: literal Gaussian calculation

The complete independent core review reconstructs the original columns in basis \(1,S,S^2\), the exact \(K_3,K_6,G_3,F,\Omega\), and both cost matrices. The supplementary \(G_3\) and
\[
Z_{3,6}=\frac18\begin{pmatrix}-29&-35&84\\42&48&-126\\-21&-21&69\end{pmatrix}
\]
agree entry by entry with that independent computation, retaining \(\omega_n=7n!\), \(S=1+ix\), and quotient \((S-1)^3\).

One direct way to check its complete invariants is the actual source-Gram endomorphism
\[
\Omega^{-1}F^*G_3F=
\begin{pmatrix}27/8&0&105/4\\0&3/4&0\\7/8&0&55/8\end{pmatrix}.
\]
Its spectrum is \(3/4,(41\pm7\sqrt{34})/8\), including full multiplicities. The latter two have sum \(41/4\) and product \(15/64\), so
\[
t_1=11,\quad t_2=3365/32,\quad t_3=273947/256,
\quad \mathcal A_2=507/64,
\quad \det(I_E+Z)=5145/256.
\]
The three eigenvalues are distinct: the radical pair differs, and substituting \(3/4\) into their quadratic gives a nonzero value. Their positivity follows from \(41^2-49\cdot34=15>0\). Thus the actual spectrum cannot equal the two-value optimizer with repeated \(b\), proving strictness of RM.16 without using a decimal. The two-trace discriminant is nonzero, so the trace-only Jensen comparison is also strict. The dimension-two figures and determinant ratios in the supplement agree with the full original-coordinate matrices in the separate core review.

## 8. RM.28–RM.31: rank refinement with full zero directions

For \(W=\operatorname{im}F\subset E_i\),
\[
\langle v,Zv\rangle_{G_i}=\|F^\dagger v\|_\Omega^2
\]
proves \(\ker Z=\ker F^\dagger=W^{\perp_{G_i}}\). Hence
\(E_i=W\oplus^{\perp_{G_i}}W^{\perp_{G_i}}\). The map \(Z\) has image in \(W\); its restriction to \(W\) has zero kernel because an orthogonal direct summand meets its complement only in zero. It is therefore positive definite on the actual inherited metric of \(W\). This proves the complete decompositions
\[
Z=Z_W\oplus0_{q-\rho},\quad
Q=(I_W+Z_W)^{-1}\oplus I_{q-\rho},\quad
\det(I_E+Z)=\det(I_W+Z_W)\,1^{q-\rho}.
\]

Likewise, let \(\mathcal U=(\ker F)^{\perp_\Omega}\). Every source vector decomposes as a vector of \(\mathcal U\) plus a vector of \(\ker F\). Hence \(F|_{\mathcal U}:\mathcal U\to W\) is bijective, with its actual pulled-back Gram \(F^*G_iF\). It is not implicitly an isometry for the original \(\Omega\). If \(v\in\ker F\), then its original relation remains \(\mathfrak b v=Nv\) with exact norm \(v^*\Omega v\) and zero quotient observation. This proves the retained source-kernel statement, including the original new columns.

For a proved integer \(\rho\le R\le q\), take all \(\rho\) positive eigenvalues, and append exactly \(R-\rho\) zeros. Their two traces are still the same \(t_1,t_2\), so all feasibility inequalities needed for RM.30 hold. Applying the already proved scalar theorem to this \(R\)-entry list gives RM.31; the \(q-R\) remaining original zero eigenvalues each contribute the explicit factor one, as recorded by the full decomposition above. For \(R=1\), there is at most one nonzero eigenvalue, giving exact ratio \(1+t_1\); for \(R=0\), all eigenvalues are zero and the ratio is one.

To compare with the original dimension-\(q\) upper bound, the optimizer \(a_R,b_R,\ldots,b_R\) has the same exact first two traces as the original operator. Appending \(q-R\) zeros gives a feasible dimension-\(q\) positive spectrum. Its logarithmic determinant therefore cannot exceed the sharp dimension-\(q\) maximum already proved. This proves that the rank-refined estimate is at least as sharp, including equality cases, without asserting an unproved rank fact about the original packet.

Finally, positive order \(Z_+\succeq Z\) does not transport an upper bound on \(\operatorname{rank}Z\) to \(\operatorname{rank}Z_+\). The actual comparator source instead gives
\[
\operatorname{rank}Z_+=\operatorname{rank}D_+
=\dim\mathcal C_+,
\]
because \(G_i\) is invertible and \(\mathcal C_+\) is precisely the quotient by the radical. The supplementary note states this correct replacement explicitly.

## 9. Completion of this review

All RM.1–RM.31 identities have been checked with their original domains, metric adjoints, noncommuting factor order, kernels, multiplicities, and zero cases. The full new positive-form factorization is valid, including singular and zero comparators. The corrections listed above concern explicit domain statements and the integral-versus-remainder wording; they do not reveal a failed comparator identity. No source-specific arithmetic inequality has been inferred from the finite fixtures, and no inherited PR #25 estimate is certified by this review alone.

## 10. Complete revised-source read and RM.32–RM.35

The complete revised supplement, now through RM.35, was subsequently read again in full: 24627 bytes, SHA-256 `7a6aa23e5a250ff7c1d8cd7c4a642fa5ff866ffa4565c44be3013fb64135ec25`. All four corrections recorded against the first draft have been applied. The unused \(W_j\) definition has also been removed. The new RM.32–RM.34 reproduce exactly the contraction adjoint, quotient-form excess, and original-metric pushforward derived in section 5 of this review; every order, sign, source class, and nonzero/zero case agrees. The final domain wording for the finite-gap sentence should explicitly retain \(q\ge2\) when using \(a_+\); in dimension one its exact counterpart uses \(t_1^+\).

For the arithmetic join, the complete original source through AU.14 was read, including the whole AU.10–AU.13 comparison argument and its moment calculation, in `work/arithmetic_volume_upper_route_20260913.tex`, SHA-256 `21aaedc3585887fa7d2cb3e37e68d14415829a4b213566f7a08f4619835ef38b`. The earlier arithmetic source defines a full quartet of common multiplicity \(m\ge1\), \(\deg h=4m\), \(k\ge3\), \(w_h(t)=|(g/h)(1/2+it)|^2/(2\pi)\), and the original arithmetic mass \(\mu_h^k\). Its supplied lower-envelope statement AU.10 is
\[
m_{h,k}(u)\ge c_h\vartheta_h^{k-3}
e^{-\alpha(|u|+k-3)}(1+|u|+k-3)^{-B},
\]
with exactly
\[
\alpha=\pi/2,\quad B=42+2\deg h=42+8m,
\quad \vartheta_h=\int_{-1}^{1}w_h(t)\,dt>0.
\]
The revised RM source retains those same constants and makes the literal substitution
\[
a_k=c_h\vartheta_h^{k-3}e^{-\alpha(k-3)},\quad d_k=k-2>0,
\quad d\nu_{h,k}(u)=a_ke^{-\alpha|u|}(d_k+|u|)^{-B}\,du.
\]
Since \(1+|u|+k-3=d_k+|u|\), the density inequality in RM is exactly AU.10, without a lost additive constant or changed exponent. The complete proof of that inherited analytic lower envelope is carried by the arithmetic endpoint/upper-comparison closure, as explicitly stated by the supplement; this independent review verifies the exact use of it and its full finite morphism, rather than treating the Gaussian fixture as evidence for the envelope.

The comparison moments in AU.12 can also be checked directly, retaining their actual mass. For even \(n\), insert the positive identity
\[
(d_k+u)^{-B}=\frac1{(B-1)!}\int_0^\infty t^{B-1}e^{-(d_k+u)t}\,dt
\]
on the positive half-line. Tonelli applies to its nonnegative integrand, and repeated integration by parts gives \(\int_0^\infty u^ne^{-(\alpha+t)u}\,du=n!/(\alpha+t)^{n+1}\). Evenness then proves
\[
\nu_{k,n}=\frac{2a_kn!}{(B-1)!}
\int_0^\infty\frac{t^{B-1}e^{-d_kt}}{(\alpha+t)^{n+1}}\,dt
\quad(n\text{ even}),\qquad \nu_{k,n}=0\quad(n\text{ odd}).
\]
The bound \(\nu_{k,n}\le2a_kd_k^{-B}n!\alpha^{-n-1}\) proves all even absolute moments finite; odd absolute moments follow by the same positive-half-line integral. The measure is positive everywhere, so its polynomial Gram is positive definite and has its literal positive constant moment \(\nu_{k,0}\), which is not assigned the arithmetic mass.

In the original \(S\)-monomial coordinates, for \(c=k/2\), the comparator Gram entries are exactly
\[
(H_j^\nu)_{ab}
=\int(c-iu)^a(c+iu)^b\,d\nu_{h,k}(u)
=\sum_{r=0}^{a}\sum_{s=0}^{b}
\binom ar\binom bs c^{a+b-r-s}(-i)^ri^s\nu_{k,r+s}.
\]
The corresponding arithmetic Gram has the same formula with its original moments. Thus every phase, binomial coefficient, and power of \(k/2\) is retained. These entries need comparison moments through degree \(2j\) exactly as asserted.

For each coefficient vector \(v\), measure order gives
\[
v^*H_j^\nu v
=\int\left|\sum_{n=0}^jv_n(c+iu)^n\right|^2d\nu_{h,k}(u)
\le v^*H_j^m v.
\]
No metric replacement is used to invert this order. For an arbitrary positive definite form \(H\), direct expansion gives
\[
2\operatorname{Re}(\ell^*v)-v^*Hv
=\ell^*H^{-1}\ell-(v-H^{-1}\ell)^*H(v-H^{-1}\ell).
\]
The maximum over the original coefficient space is therefore \(\ell^*H^{-1}\ell\), attained uniquely at \(v=H^{-1}\ell\). Since the objective with \(H_j^m\) is at most the objective with \(H_j^\nu\) for every \(v\), taking the two maxima proves
\[
(H_j^m)^{-1}\preceq(H_j^\nu)^{-1}.
\]
For the original quotient monomial map
\(X_j=([S^0]_\chi,\ldots,[S^j]_\chi)\), composition by \(X_j\) and \(X_j^*\) preserves the order, proving RM.35:
\[
K_j=X_j(H_j^m)^{-1}X_j^*
\preceq U_j=X_j(H_j^\nu)^{-1}X_j^*.
\]

To check exact agreement with the monic-polynomial representation RM.1, let \(T_j\) be the invertible coefficient matrix whose \(n\)-th column contains the original monic polynomial \(p_n\) in the \(S\)-monomial basis. Then
\[
B_j=X_jT_j,\qquad O_j=T_j^*H_j^mT_j.
\]
Consequently
\[
B_jO_j^{-1}B_j^*
=X_jT_j(T_j^*H_j^mT_j)^{-1}T_j^*X_j^*
=X_j(H_j^m)^{-1}X_j^*.
\]
The cancellation is exactly this typed triangular-coordinate composite. It does not claim that \(T_j\) is unitary or discard the original norms. Since \(H_j^\nu\) is positive definite and \(X_j\) is surjective in the admitted range, \(U_j\) is positive definite as required. The difference \(D_+=U_j-K_i\) may still be singular; RM.22–RM.34 already handle that full case.

The revised arithmetic join therefore supplies the concrete matrix used in RM.20 and connects it to the original quotient form with all coordinates and constants retained. The only inherited analytic ingredient is exactly the lower-envelope estimate explicitly identified above, whose full proof is owned by the arithmetic closure. No bound on an omitted actual high-degree moment is introduced.

## 11. Terminal source binding

The final source is `workspace:/work/relation_moment_comparison_proof_20260913.tex`, 24653 bytes, SHA-256 `105bc6884528e03b3f6aa15d9a7c34643c4bb3fb97c03451b3d3bf9499ef3dc9`.

The final gap paragraph was read directly. It now states the derived gap \(Q\succeq(1+a_+)^{-1}I_E\) for \(q\ge2\), and separately states the dimension-one comparator determinant \(1+t_1^+\) and gap \(Q\succeq(1+t_1^+)^{-1}I_E\), followed by the empty determinant convention for \(q=0\). This is correct because \(0\le Z\preceq Z_+\) in dimension one bounds the unique cost eigenvalue by \(t_1^+\).

An exact byte comparison confirmed this paragraph is the only difference from the complete RM.1–RM.35 source read recorded in section 10: replacing the final paragraph by its preceding version occurs exactly once and reconstructs SHA-256 `7a6aa23e5a250ff7c1d8cd7c4a642fa5ff866ffa4565c44be3013fb64135ec25`. Thus the complete prior read plus the directly read final paragraph covers the exact final file, rather than relying on an author's report of unchanged material.

All requested finite source corrections are resolved in this final source. The complete comparator quotient, the original-source contraction and both its kernel and positive defect, the cost-action formula, arithmetic monomial-Gram composite, rank refinement, Gaussian calibration, and boundary cases have the proved dispositions above. The original incoming files remain unchanged, with their corrections documented separately. The inherited analytic source scope remains explicit; this review does not claim an RH conclusion or a new uniform original-trace bound.
