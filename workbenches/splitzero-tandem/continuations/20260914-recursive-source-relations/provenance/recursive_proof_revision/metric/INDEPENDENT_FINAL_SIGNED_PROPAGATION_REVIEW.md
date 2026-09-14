# Independent review of the final signed metric propagation

Review date: 2026-09-13. Reviewer: independent mathematical review subagent. Verdict: **PASS for the bounded final delta at the physical-byte SHA-256 pins below.** No unresolved mathematical defect was found in that delta. The reviewer made no changes to the mathematical source files.

## Scope and preserved review history

This review follows the three earlier independent reviews in this directory: `INDEPENDENT_MATHEMATICAL_REVIEW.md`, `INDEPENDENT_SAMPLING_REVIEW.md`, and `INDEPENDENT_RMT_PROPAGATION_REVIEW.md`. Those reviews retain their original pins and findings. The comparison baseline for this pass is `history/accepted_three_control_cut`, whose five source hashes were checked against the accepted third review. They agree exactly.

The present pass reads every changed theorem/proof context in the five staged modules, the complete replacement R58, and the complete supplied dependencies RMT1–22 and ISM1–43. It checks the newly added exact trace norm, centered Hilbert–Schmidt estimate, five-entry minima in both endpoint coordinates, the finite constructed signed center and residual, and each earlier endpoint substitution. A line-diff inventory against the accepted cut confirms that all changed source lines fall inside the contexts read. This is a bounded proof review of the actual final delta; it does not claim a new independent rereading of every page of the full research program. The earlier source identifications and complete source proofs remain part of the preserved dependency closure.

The mathematical sources reviewed are:

| Local source | Final SHA-256 |
|---|---|
| `staged/tex/next_edition/AT_complete.tex` | `442259ac231ff586afe706f00d4bc17a7a6d87567c8013f9e62f215e52630fc7` |
| `staged/tex/next_edition/AW_complete.tex` | `9770b427a1c963fb4f572a7544b777b68f8d91b0370c68ee50392292d336d300` |
| `staged/tex/tau_signed_projection_control.tex` | `9a5a3c86a7aada96d92a40d092951e5db3dcd1c195d758d521b92a9d9b8dce88` |
| `staged/tex/periodized_source_intake_proofs.tex` | `899b3fa1eceaae7a911599c465158d24bfcf06dce55a69ace55d7ab57a635204` |
| `staged/tex/periodized_curvature_control_bridge.tex` | `d587b0c871f952d90063a2eaade1f04e3b7f09283fdaed85460a1dc700122825` |
| `conclusion_replacements/R58_NEW.tex` | `6863417dc5ff4921fc4ffcc03caa84a7abde6b59f479fa2230d1c23008e53f88` |
| `dependencies/recursive_metric_transport.tex` | `8110fbb1c5796ad36a75cf364b7744d5852419608b9e890d83b5fde5c0a9844f` |
| `dependencies/incoming_source_metric_control.tex` | `ce4b0968607fd06d7203ca498e66ce3dbe78e93e8eb3fe9079a106fa188ae0d8` |

Metadata pins are `PATCH_MANIFEST.json` = `2023d30254fd7fff18e802027b6ffa52e824181438bfc18d94db0b4b8c51c2eb`, `FINAL_SIGNED_DEPENDENCIES.json` = `fad630fcd6a030f049d26bbab326cc4714f04644506caeba26cc133d24187212`, and `conclusion_replacements/R58_MAP.json` = `2b22c7e4a1f7641991b316e4f82b0ddd52429ce92327bd9f42a4c2866ce1b03b`.

## Findings repaired before this verdict

The initial final-delta formulas were mathematically consistent, but their accompanying proof paragraphs had the following missing dependencies or undefined local notation. Each was reported to the editing agent and its repaired text was read.

1. AT19 already contained the signed branches. Its theorem proof now cites the independently constructed local AT19bb alongside both absolute branches of AT18.
2. AW14's proof of the five-entry minimum now includes both AW13c inequalities, as well as AW16, AW16a and the moment-angle bound.
3. AW22's division step now names all four generic inequalities and AW21, so it proves its actual five-entry nonlinear radius.
4. AW18 now derives the quartet maximum from both AW14 and AW17ab.
5. AW23 now states its derivation as the intersection of AW22 with AW17ab. Its enlarged interval is not attributed to AW22 alone.
6. The paragraph after PSA24f now includes both PSA24g inequalities in the five-entry minimum.
7. SP13c now invokes SP13eb for its signed branches and RMT13–22 for the complete intersection.
8. The paragraph after AT19a now assigns the inverse and nonlinear branches to RMT16–18 and the signed branches to RMT19–22/local AT19bb.
9. R58 now defines its newly used operator explicitly as \(C(x)=M(x)^{-1}(M^{(1)}-M^{(0)})\) before the Hilbert–Schmidt expression.

These repairs concern actual logical dependencies and symbol definitions. The accepted formulas did not need a sign, constant, dimension or endpoint change.

## Common source and operator verification

The finite Hilbert space is the unchanged \(H=\mathcal P_{2q}\), of dimension \(n=2q+1\), in the original ascending coefficient coordinates. Put \(M_x=(1-x)M_0+xM_1\), \(D=M_0^{-1}M_1\), and \(C_x=M_x^{-1}(M_1-M_0)\). Positivity of both endpoint forms proves positivity of every \(M_x\). The operator \(D\) is positive self-adjoint for \(M_0\); the operator \(C_x\) is self-adjoint for \(M_x\), since \(M_xC_x=M_1-M_0\) is Hermitian.

The maps in RMT/ISM have \(B_N:\mathcal P_{N-q}\to H\), whereas AW and PSA use the unpadded multiplication map with codomain \(\mathcal P_N\). Their exact relation is \(B_N^{\rm RMT}=I_NB_N^{\rm AW/PSA}\). Substitution in both relation-Gram formulas proves their equality, and substitution in the projection formulas proves equality as endomorphisms of \(H\). ISM proves \(\Pi_N=P_N-Q_N\), including the inverse parametrization \(\pi_\chi|_{\operatorname{ran}\Pi_N}\) of the minimum section. Thus the common signed endomorphism is exactly

\[
 A_x=\Pi_{q-1}+\Pi_q-\Pi_{2q-1}-\Pi_{2q}
 =U_x-W_x.
\]

For SP the equality is \((U_x,W_x,C_x)=(\mathcal R_x,\mathcal P_x,T_x)\). For AT it is \((M_x,D)=(M_*(t),D_*)\), with \(x=t\). For AW it is \((M_x,D)=(M(t),D)\). For PSA it is the original/sampled pair \((M^{(0)},M^{(1)})\) and \(D_{L,J}\). None of these substitutions changes a source mass or a relation coefficient.

The already established nested flags give each of \(U_x,W_x\) the full spectrum \(0^{[q]},1^{[2]},2^{[q-1]}\). Consequently the rank is \(q+1\), the trace is \(2q\), and the trace of its square is \(4q-2\). These are different quantities with their exact multiplicities retained. In particular

\[
 \operatorname{Tr}A_x=0,\qquad
 Z_x:=\operatorname{Tr}(A_x^2)=8q-4-2\operatorname{Tr}(U_xW_x).
\]

Both positive operators dominate their range projections. The two ranges have dimension \(q+1\) in \(2q+1\), so intersect in dimension at least one. The trace of the product of their range projections is at least that intersection dimension, by summing squared projected lengths. If positive operators \(S'\succeq S\) and \(T\succeq0\), then \(\operatorname{Tr}((S'-S)T)=\operatorname{Tr}(T^{1/2}(S'-S)T^{1/2})\ge0\). Applying this twice gives \(\operatorname{Tr}(U_xW_x)\ge1\), hence \(0\le Z_x\le8q-6\). The dimension-one quotient case gives the valid bound \(Z_x\le2\).

## The additional two bounds and both minima

Let \(d_x\) be the diameter of the complete ordered spectrum of \(C_x\). Subtracting the midpoint of its extreme eigenvalues changes no pairing with \(A_x\). In an \(M_x\)-orthonormal eigenbasis of \(A_x\), each diagonal entry of that centered \(C_x\) has absolute value at most \(d_x/2\). Multiplication by the absolute eigenvalues of \(A_x\) and summation proves

\[
 |\operatorname{Tr}(C_xA_x)|\le
 S_{\rm tr}(x)=\tfrac12d_x\|A_x\|_1.
\]

Alternatively subtract its trace mean. Expanding the square gives

\[
 \Sigma_x=\operatorname{Tr}\!\left((C_x-\operatorname{Tr}(C_x)I/n)^2\right)
 =\operatorname{Tr}(C_x^2)-(\operatorname{Tr}C_x)^2/n\ge0.
\]

Hilbert–Schmidt Cauchy–Schwarz in the same original metric therefore proves \(|\operatorname{Tr}(C_xA_x)|\le S_{\rm HS}(x)=\sqrt{\Sigma_xZ_x}\). All products and traces are of the original endomorphisms. The explicit algebra isomorphism \(T\mapsto M_x^{1/2}TM_x^{-1/2}\), with its displayed inverse, justifies the equivalent Hermitian calculation without changing either endpoint form.

The earlier full-spectrum estimate, the retained overlap estimate, these two estimates, and the actual moment-angle estimate all bound this identical signed derivative. Their pointwise minimum therefore bounds its absolute value, and integration proves the new \(J^{(5)}\) bound. The exact trace norm is retained even though its overlap majorant remains as another entry. The two-angle-list count remains \(a_q=2q-1\), with the forced zero explicitly retained geometrically and every additional zero retained in the scalar list.

For the actual measures, vanishing four-volume would identify the degree-less-than-\(q\) minimum section with the degree-\(2q\) minimum section. Thus \(1\perp\chi\mathcal P_q\). On the original line \(S=k/2+iy\), the polynomial \(\chi^{\#_k}(S)=\sum\overline{\chi_j}(k-S)^j\) equals \(\overline{\chi(S)}\). The asserted orthogonality would force \(\int|\chi|^2d\mu_x=0\), contradicting the positive Gram of the nonzero polynomial \(\chi\). This proves strict positivity on the specified continuous and sampled moment paths; it also justifies each denominator in the new five-entry nonlinear integral.

Writing \(f_x=a_q\sqrt{1-e^{-\mathcal B(x)/a_q}}\), its five entries are precisely \(d_x\) and the four generic numerators divided by \(f_x\). The derivative of \(2\operatorname{arcosh}(e^{B/(2a_q)})\) is \(1/f(B)\), so the chain rule proves the nonlinear radius. The retained inverse is \(2a_q\log\cosh(z/2)\) on \(z\ge0\). At \(q=1\), AW's \(A_0=\operatorname{arcosh}(e^{\mathcal B(0)/2})\) consequently has radius exactly \(\mathcal I_{h,k}/2\), as AW23 states.

## Constructed signed center and explicit residual

For each finite truncation \(\ell\ge0\), let the complete positive eigenvalues of \(D\) be \(b_1\le\cdots\le b_n\), and set

\[
 B_x^\circ=(1-x)I+xD,\quad
 \alpha_x=\frac{2(1-x)+x(b_1+b_n)}2>0,\quad
 H_x^\circ=I-B_x^\circ/\alpha_x,
\]
\[
 C_x^{[\ell]}=\alpha_x^{-1}\sum_{r=0}^{\ell}(H_x^\circ)^r(D-I),\quad
 R_x^{[\ell]}=(H_x^\circ)^{\ell+1}C_x,\quad
 E_x^{[\ell]}=R_x^{[\ell]}-\operatorname{Tr}(R_x^{[\ell]})I/n.
\]

The finite geometric identity, multiplied by \((B_x^\circ)^{-1}(D-I)\), gives \(C_x-C_x^{[\ell]}=R_x^{[\ell]}\) exactly. Every factor is a real function of \(D\), so its \(M_0\)-orthogonal eigenbasis also remains orthogonal for \(M_x=M_0B_x^\circ\). Thus every displayed operator is self-adjoint in the required original varying metric. ISM's explicitly constructed centered operator is \(Y_x^{[\ell]}=C_x^{[\ell]}-\operatorname{Tr}(C_x^{[\ell]})I/n\); it is not an assumed approximation.

Since \(\operatorname{Tr}A_x=0\), the exact derivative is

\[
 \mathcal B'(x)=\operatorname{Tr}(C_x^{[\ell]}A_x)
                    +\operatorname{Tr}(E_x^{[\ell]}A_x).
\]

Integrating Hilbert–Schmidt Cauchy–Schwarz on the second term proves

\[
 j_\ell-e_\ell\le\mathcal B(1)-\mathcal B(0)\le j_\ell+e_\ell,
\]
\[
 j_\ell=\int_0^1\operatorname{Tr}(C_x^{[\ell]}A_x)\,dx,\qquad
 e_\ell=\int_0^1\sqrt{\operatorname{Tr}((E_x^{[\ell]})^2)Z_x}\,dx.
\]

The center retains its sign. Each integral has a continuous finite-matrix integrand. To verify the stated decay constant, the eigenvalues of \(H_x^\circ\) are

\[
 h_j(x)=\frac{x(b_1+b_n-2b_j)}{2(1-x)+x(b_1+b_n)}.
\]

Their maximum absolute value is at most \(\vartheta=(b_n-b_1)/(b_n+b_1)<1\). The eigenvalues of \(C_x\) are \((b_j-1)/(1-x+xb_j)\), of absolute value at most \(|b_j-1|/\min\{1,b_j\}\). The residual eigenvalues are their products with \(h_j(x)^{\ell+1}\). Subtracting the trace mean from those real residual eigenvalues subtracts the nonnegative square of their sum divided by \(n\). Hence

\[
 \operatorname{Tr}((E_x^{[\ell]})^2)
 \le\vartheta^{2\ell+2}K_D,\qquad
 K_D=\sum_{j=1}^{n}\left(\frac{|b_j-1|}{\min\{1,b_j\}}\right)^2.
\]

Using the already proved \(Z_x\le8q-6\) and the interval length one yields exactly

\[
 0\le e_\ell\le\vartheta^{\ell+1}\sqrt{K_D(8q-6)}\longrightarrow0.
\]

The case \(D=cI\), \(c>0\), has \(H_x^\circ=0\), residual zero, and scalar \(C_x\); therefore \(j_\ell=e_\ell=0\), including \(\ell=0\). This agrees with cancellation of the four original quotient-determinant mass factors. These formulas establish convergence for each fixed actual pair; they do not insert a uniform tensor-order bound or an unevaluated assumption about \(Y\).

## Propagation through the earlier claims

AT19, AT19a, AW18, AW23, SP13c, PSA25a, FC13b and R58 use lower maxima and upper minima with the new entries \(\mathcal B(0)+j_\ell\mp e_\ell\). Each lower entry is separately at most the actual endpoint; each upper entry is separately at least it. Their intersection is therefore nonempty and contains that original endpoint. This is the exact reason the signed interval can be propagated alongside the absolute and nonlinear intervals.

AT22 retains the quartet parameters \(q=[1+k(m-1)](k+1)^2\), the original coefficient \(4q\), and the Gamma factor \(\delta k/(2\sqrt5)\). Substitution into the signed branch yields the additional lower bound \(4q\log(\delta k/(2\sqrt5))+j_\ell-e_\ell\); its maximum with the previously proved branch is valid. Rearranging the retained condition-number branch divides by the strictly positive \(2q-1\), preserving its displayed direction. No existence of the quartet or uniform control of its condition numbers is inferred.

The sampled applications use the literal inclusion \(I_{2q,D}:\mathcal P_{2q}\hookrightarrow\mathcal P_D\), with \(D=2q+2\), and the exact congruence restriction of both forms. The degree-\(2q\) quotient calculation therefore uses precisely the original and sampled moments; the two generator raises still use the full degree \(D\). The atomic measure retains \((2\pi/L)m_{h,k}(2\pi n/L)\) and the zero mode. The finite series order \(\ell_N\) is distinct from the original derivative order and the circle length. The full-spectrum sums are empty, with value zero, at \(q=1\); the coefficient in the sampled bound is still \(2q-1=1\).

ISM38–43 additionally retains the exact source comparison: successive monic division gives the coefficients of the tensor primitive, its two signs multiply to +1 at each differentiated degree-zero factor, and the proper-support residual is the specified kernel quotient of full boundaries admitted at that support modulo its own boundaries. The maps between the one-leg and two-leg complexes have the stated composites and preserve the diagonal kernel. The coefficient insertion/projection proof retains the active face and the empty-face outer label. Thus the metric refinements do not silently discard a proper-support residual.

## Provenance and scope of verification

Every final source hash above matches its row of `PATCH_MANIFEST.json`. For each of the five revised files, the original-copy physical hash also matches the original hash in that manifest and the current live source named there. Both full dependency copies match the current owner source bytes and `FINAL_SIGNED_DEPENDENCIES.json`. The R58 replacement and preserved old text match the physical-byte hashes in `R58_MAP.json`; the old text is `c79b1efcdac8e2757c4e97f502aac1a06229d9082050bdecd60197a9e56f8380`.

The editing agent reports two clean compilation passes for the five modules; compilation is its separate responsibility. This verdict rests on the mathematical review above and does not claim to be an independent compilation or a numerical evaluation of the exact center integrals. A numerical center must retain its integration error as expressly stated in the sources. The current artifacts prove finite source controls, their convergent signed residual, and their specified earlier substitutions; they do not prove the missing uniform arithmetic estimates for the entire RH program.
