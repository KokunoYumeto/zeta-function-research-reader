# Independent original-metric endpoint identity review

Full source reads: `work/rh_counterfactual_20260913/total_object/combined_original_metric_control.tex` (ACM1–13), the immutable baseline `output/split_zero_rh_tandem_2026-09-12/current_source_20260913_periodized_residue/build/endpoint_four_volume_threshold_source.tex` (all five sections), and `output/Deligne_Mixed_Control_Continuation_2026-09-13/sources/AW.tex` (AW1–23, including its complete proofs). The endpoint body was initially read through `output/split_zero_rh_tandem_2026-09-12/build/endpoint_four_volume_threshold_source.tex`; a later explicit SHA256 comparison established that this copy and the actual immutable baseline both have hash `eaddfd03f423bdc9715f10cbde97cd3ae5af09354efc054328c2aaef662d4623`.

The ACM sign, complete spectral formula, and overlap expression are correct. The following supplies the elementary determinant proof needed when propagating the result into the earlier endpoint calculation. All coordinates, polynomial coefficients, metrics, and quotient representatives remain those in the sources.

## 1. Original quotient determinant with the orientation retained

Let the original monic cyclic polynomial be \(\chi\) of degree \(q\geq1\). For \(N\geq q-1\), set \(r=N-q+1\), \(B_N:\mathcal P_{N-q}\to\mathcal P_N\), \(B_Nf=\chi f\), and let \(L_N:E=\mathbb C[S]/(\chi)\to\mathcal P_N\) send the original ordered remainder basis to \(1,S,\ldots,S^{q-1}\). Thus \(J_NL_N=I_E\). Retain the increasing-power coefficient bases throughout. The ordered matrix

\[
T_N=[B_N,L_N]
\]

has determinant \((-1)^{qr}\). Indeed \([L_N,B_N]\) has leading degrees \(0,1,\ldots,N\), with leading coefficient one in every column; its coefficient matrix is triangular with diagonal entries one. Moving its first \(q\) columns past its last \(r\) columns gives exactly the sign \((-1)^{qr}\). The case \(r=0\) gives the identity matrix and sign one.

For the unchanged positive Gram \(M_N(x)\), the minimum section and its Gram are

\[
R_N=L_N-B_N(B_N^*M_NB_N)^{-1}B_N^*M_NL_N,
\qquad G_N=R_N^*M_NR_N.
\]

When \(r=0\), the displayed subtraction is the zero relation term. Writing the original Gram in the \(T_N\) frame gives

\[
T_N^*M_NT_N=
\begin{pmatrix}
B_N^*M_NB_N&B_N^*M_NL_N\\
L_N^*M_NB_N&L_N^*M_NL_N
\end{pmatrix}.
\]

Subtracting the first block column times \((B_N^*M_NB_N)^{-1}B_N^*M_NL_N\) from the second block column is multiplication by a block triangular matrix of determinant one. The lower-right block becomes exactly \(G_N\), and the upper-right block becomes zero. Consequently

\[
\overline{(-1)^{qr}}\det(M_N)(-1)^{qr}
=\det(B_N^*M_NB_N)\det G_N,
\qquad
V_N=\det G_N=\frac{\det M_N}{\det(B_N^*M_NB_N)}.
\]

The determinant of the zero-dimensional relation Gram is one. The orientation has been retained before its two conjugate signs multiply to one.

## 2. Exact signed derivative in the common original source

Let \(H=\mathcal P_{2q}\), \(M_x=(1-x)M_\Gamma+xM_{\rm ar}\), \(\dot M=M_{\rm ar}-M_\Gamma\), and \(C_x=M_x^{-1}\dot M\). Set \(M_N=I_N^*M_xI_N\), where \(I_N:\mathcal P_N\hookrightarrow H\) is the literal coefficient inclusion. For any differentiable invertible matrix \(K(x)\), multilinearity of the determinant gives \((\det K)'=\operatorname{Tr}(\operatorname{adj}(K)K')\); since \(\operatorname{adj}(K)=\det(K)K^{-1}\), positivity gives \((\log\det K)'=\operatorname{Tr}(K^{-1}K')\).

Apply this to the two original determinant factors. Cyclicity of the finite rectangular trace and \(M_xC_x=\dot M\) give

\[
\begin{aligned}
\frac{d}{dx}\log\det M_N
&=\operatorname{Tr}(M_N^{-1}I_N^*\dot M I_N)
=\operatorname{Tr}(P_NC_x),\\
\frac{d}{dx}\log\det(B_N^*M_NB_N)
&=\operatorname{Tr}((B_N^*M_NB_N)^{-1}B_N^*I_N^*\dot M I_NB_N)
=\operatorname{Tr}(Q_NC_x),
\end{aligned}
\]

with

\[
P_N=I_NM_N^{-1}I_N^*M_x,
\qquad
Q_N=I_NB_N(B_N^*M_NB_N)^{-1}B_N^*I_N^*M_x.
\]

Thus

\[
(\log V_N)'=\operatorname{Tr}((P_N-Q_N)C_x).
\]

In particular, keeping the order of all four endpoints,

\[
\begin{aligned}
F'(x)&=\frac{d}{dx}\log\frac{V_{q-1}V_q}{V_{2q-1}V_{2q}}\\
&=\operatorname{Tr}\bigl((P_{q-1}+P_q-P_{2q-1}-P_{2q}
-Q_{q-1}-Q_q+Q_{2q-1}+Q_{2q})C_x\bigr)\\
&=\operatorname{Tr}((U_x-W_x)C_x),
\end{aligned}
\]

where \(Q_{q-1}=0\), \(U_x=Q_{2q-1}+Q_{2q}-Q_q\), and \(W_x=(P_{2q-1}-P_{q-1})+(P_{2q}-P_q)\). Therefore \(\Delta=F(1)-F(0)\) has exactly the sign in ACM7–11.

## 3. Back-propagation to the earlier central window

The earlier central quantity and its full endpoint remainder are

\[
C(x)=\log\frac{V_q(x)}{V_{2q-1}(x)},
\qquad
E(x)=\log\frac{V_{q-1}(x)}{V_q(x)}
+\log\frac{V_{2q-1}(x)}{V_{2q}(x)}.
\]

The exact factorization is \(F(x)=2C(x)+E(x)\). Each summand of \(E(x)\) is nonnegative: the minimum norm of any original quotient vector cannot increase when its source space increases; hence \(G_{N+1}\leq G_N\) as forms. Conjugating by \(G_N^{-1/2}\) gives a positive matrix with eigenvalues at most one, so \(\det G_{N+1}\leq\det G_N\). This argument changes no actual Gram; the conjugation only proves their determinant inequality.

Write \(C_0=C(0)\), \(C_1=C(1)\), \(E_0=E(0)\), and \(E_1=E(1)\). With the actual common-source integral

\[
I_{\rm ACM}=\int_0^1\min\{S_{\rm AW}(x),S_{\rm SP}(x)\}\,dx,
\]

the proved inequality \(|\Delta|\leq I_{\rm ACM}\) yields the exact propagated bound

\[
|2(C_1-C_0)+E_1-E_0|\leq I_{\rm ACM},
\]

and therefore

\[
C_0+\frac{E_0-E_1-I_{\rm ACM}}2
\leq C_1\leq
C_0+\frac{E_0-E_1+I_{\rm ACM}}2.
\]

Equivalently, \((F(0)-E_1-I_{\rm ACM})/2\leq C_1\leq(F(0)-E_1+I_{\rm ACM})/2\). The weaker difference bound is \(|C_1-C_0|\leq(I_{\rm ACM}+|E_1-E_0|)/2\). Nonnegativity of \(E_0,E_1\) does not determine the sign of \(E_1-E_0\), so it does not permit deleting that difference from the central estimate.

The baseline arithmetic lower estimate remains in its own original metric: for the full quartet and \(k\geq3\),

\[
C_1\geq2(q_k-1)\left(\log k+\log\frac{\delta}{2C_h^{\rm bal}}\right).
\]

Combining this exact existing lower estimate with the propagated upper estimate above is legitimate and retains \(E_0,E_1\). It produces no new uniform upper control of \(I_{\rm ACM}\).

## 4. Complete low-degree and overlap checks

For \(q=1\), the dimension is three; \(U,W\) have eigenvalues \(0,1,1\), and

\[
S_{\rm AW}=c_3-c_1=d,
\quad \mathcal L_1(D)=\log(b_3/b_1),
\quad S_{\rm SP}=\frac d2\min\{4-2s,\sqrt{3(4-2\operatorname{Tr}(UW))}\}.
\]

Here \(s\geq1\); on the actual original source, AW19–20 show \(s=1\), \(U-W=P_0-P_{\mathcal N}\), and \(\operatorname{Tr}(UW)=1+\cos^2\theta=2-\sin^2\theta\). Hence the SP expression is \(d\min\{1,(\sqrt6/2)\sin\theta\}\). The separately proved AW21 expression \(d\sin\theta\) is sharper in this special degree and remains available; the ACM pointwise minimum makes no claim to exhaust every known degree-specific estimate. Also the earlier central expression is exactly \(C(x)=\log(V_1/V_1)=0\), and the endpoint remainder is exactly \(E(x)=F(x)\); this verifies the central extraction at the repeated-endpoint edge case.

For \(q=2\), the dimension is five; \(U,W\) have eigenvalues \(0,0,1,1,2\). Their traces are four and their squared traces are six. Therefore

\[
\begin{aligned}
S_{\rm AW}&=c_4-c_2+2(c_5-c_1),\\
\mathcal L_2(D)&=\log(b_4/b_2)+2\log(b_5/b_1),\\
S_{\rm SP}&=\frac d2\min\{8-2s,\sqrt{5(12-2\operatorname{Tr}(UW))}\}.
\end{aligned}
\]

The range dimension three forces \(s\geq1\); both universal consequences are at most \(3d\), while their actual refined values need not be ordered.

In every degree, let \(P_U,P_W\) denote the orthogonal range projections and let \(E\) project onto their intersection. The complete spectra prove \(U\geq P_U\geq E\) and \(W\geq P_W\geq E\). Thus \(U-E,W-E\) are positive of trace \(2q-s\), and the trace-norm triangle inequality gives \(\|U-W\|_1\leq4q-2s\). Also

\[
\operatorname{Tr}((U-W)^2)=2(4q-2)-2\operatorname{Tr}(UW)
=8q-4-2\operatorname{Tr}(UW)\geq0.
\]

This establishes the nonnegative radicand as the exact squared Hilbert–Schmidt norm. Cauchy–Schwarz on all \(2q+1\) eigenvalues gives the stated square-root trace-norm bound. Finally \(\operatorname{Tr}(UW)\geq\operatorname{Tr}(P_UP_W)\geq s\): expand \(U=P_U+(U-P_U)\), \(W=P_W+(W-P_W)\), use nonnegative trace for products of positive operators, and observe that the restriction of both range projections to their intersection is the identity. Subtracting the midpoint of \(C_x\)'s extreme eigenvalues in the trace pairing is valid because \(\operatorname{Tr}(U-W)=0\), and yields the factor \(d/2\) in SP exactly.

No correction to the sign or formulas in ACM is required. The explicit central-window endpoint remainder and the complete determinant derivative proof are the necessary propagation material.

## 5. Accepted isolated baseline propagation

The added FV.M1–14, ERJ.32a–b, AU.31a–b and revised gap paragraph were independently read in `work/backpropagation_20260913/metric/baseline_patch`. The initial comma in the Gamma exponent was corrected. The AU introduction now preserves the original matrix entry's arithmetic degree-2q requirement while stating the signed entry's degree-4q requirement. The final FV.M13–14 replacement was read in full after regeneration and is accepted.

For the actual inclusion of declared top-degree complexes, the residual is exactly

\[
\ker[H^k(C_\lambda)\to H^k(C_{\rm full})]
=\bigl(dC_{\rm full}^{k-1}\cap C_\lambda^k\bigr)/dC_\lambda^{k-1}.
\]

The primitive map has domain \(\{\Xi:d\Xi\in C_\lambda^k\}\) and kernel \(C_\lambda^{k-1}+\ker d\): membership in its kernel means precisely that \(d\Xi=d\Xi_\lambda\) for a declared primitive, hence \(\Xi-\Xi_\lambda\in\ker d\). This proves both directions and retains tensor-slot cancellations. The one-leg injection \(V/W\to\mathscr B/\Theta W\) is explicitly limited to the unchanged top source and injective theta map, with the complete exact sequence proved. There is no tensor identification with a single \(V/W\).

The isolated patch uses \(E_0,E_1\) for the two arithmetic endpoint losses, whereas Section 3 of this receipt used subscripts 0 and 1 for interpolation endpoints. The patch's literal identity \(2C_k=\mathcal B^\Gamma+\Delta-E_0-E_1\) and its subsequent lower/upper inequalities are correct in that notation and retain both losses. The q=1 edge case belongs to the finite spectral formulas; the quartet growth estimates retain their stated k≥3 and q≥(k+1)^2 domains.

ERJ.32b's bound follows from \(1+\sum_j z_j\le\prod_j(1+z_j)\) for nonnegative \(z_j=g_j^{-s}-1\), giving the sum of all 2q inverse powers at most \(2q-1+\exp(s\mathcal B)\). Its individual eigenvalue lower bound follows by bounding each nonnegative \(-\log g_j\) by their sum. The AU congruence is correctly oriented: \(J_N^uT_N=T_{q-1}J_N^S\) gives \(K_N^u=T_{q-1}K_N^ST_{q-1}^*\), hence \(V_N^u=|\det T_{q-1}|^{-2}V_N^S=V_N^S\). The minimum of the independently proved upper bounds and the propagated nonnegative gap are valid.

Accepted source hashes, before subsequent layout-only changes:

- `build/endpoint_four_volume_threshold_source.tex`: `78f169cf790e593eb714ccdbc5d376ce1ab7e6a3424fa7f30c40a138649b1146`.
- `tex/endpoint_restriction_join.tex`: `50fb4709150cd32cad259f3cd138958f2ddf9bf32f925975a41105a7978dc972`.
- `tex/arithmetic_volume_upper_route.tex`: `363500876a972465589004a5c889d178a1f07fc5b0081bdc672454bf650daf47`.

Review result: PASS for the requested mathematical additions after these repairs. No shared source was edited by this reviewer.

## 6. Recursive full-angle propagation delta

Read in full the new `work/backpropagation_20260913/recursive_metric_transport.tex` (RMT1–18) and `work/backpropagation_20260913/metric/recursive_endpoint_specialization.tex` (FV.M15–18), followed by the actual replacements in FV.M11, ERJ.32a–b and AU.31a–b and their adjacent proof paragraphs. Unchanged previously accepted arguments were not redundantly re-reviewed.

Result: mathematical PASS. The explicit coordinate identity y=u preserves S=k/2+iu. The reference convolution constant and original arithmetic density agree exactly, so every common-source Gram, relation inclusion, quotient matrix, projection, and signed volume agrees. The positivity argument uses the polynomial chi times its full line-conjugate chi# in the degree-2q relation space; it is valid on the actual positive moment source, including q=1. The derivative of H_a(B)=2 arcosh(exp(B/(2a))) is exactly 1/(a sqrt(1-exp(-B/a))), and its inverse is exactly 2a log cosh(z/2). All three pointwise derivative estimates therefore propagate through the stated nonlinear coordinate. The interval intersections give the stated Blo/Bhi with the correct endpoint signs.

The endpoint specialization proves J≤I for the old two-bound integral, uses the actual moment domain for the full-angle argument, and retains the old generic signed-matrix proof. FV.M11 still subtracts both arithmetic losses E0+E1. The substitutions of Bhi into ERJ's joint upper bound and AU's central upper bound are valid; the previous inverse-power and congruence proofs apply to those same actual quantities. No uniform-in-order conclusion is inserted.

A notation clarification was sent for RMT10: write `Tr((U-W)^2)` explicitly instead of `Tr(U-W)^2`, because the intended and proved quantity is the trace of the operator square. This affects the display's parsing, not the surrounding mathematical derivation or the specialization formulas.

Delta-reviewed source hashes:

- RMT: `034c7b72c44a02c2874e634124b94615575948203bb14fcdb3e5284f53f80e1b`.
- Specialization: `d2a8c48b9ba05d67ddd4a85d06a7b2ede45fd7d69caa4991e4867113a0abda54`.
- Endpoint: `5e5719660038ef0a210ee98db17d8aead032c893d492cbbe968ace9bca36707c`.
- ERJ: `d28cce9c3d9c97661e783c4a5d718f185b9534ed2f4f238f657322fbd4c24511`.
- AU: `49775009fba50a77067a7ccca1a035ec965afe6bc914227dad75ca04dc31dddb`.

## 7. Earlier conclusion-site propagation delta

Read both `work/backpropagation_20260913/metric/ENDPOINT_CONCLUSION_REPLACEMENTS.json` and its Markdown counterpart in full. Checked every old string against the exact declared immutable conclusion, `output/split_zero_rh_tandem_2026-09-12/current_source_20260913_periodized_residue/tex/research_conclusion.tex`. Its SHA256 is `cec03014398811e5fa4788cb7b6f4816123c026d673a1a9a0398b7fded360e3b`, matching each record. Every old string occurs exactly once. Their first lines are 1436, 1483, 1595 and 1680 respectively; their final included lines are 1439, 1489, 1610 and 1683. Thus the recorded end_line values use the exclusive convention.

The four replacements are mathematically PASS. R44 preserves the original central lower bound and inserts the approved three-estimate integral and exact nonlinear Blo/Bhi. Both arithmetic endpoint losses remain in the four-volume and central equations. R45 substitutes the approved signed upper entry and takes the minimum with the complete older bounds; its positive asymptotic limit remains explicitly assigned only to the old scalar majorant. R47 inserts the approved joint upper bound and its inverse-power consequences with the same typed returns, while retaining all prior lower controls and central unit eigenvalues.

Two small presentation clarifications were sent to the author: document the exclusive end_line convention; state q=q_k before R44's new abbreviated endpoint definitions because its immediately preceding paragraph writes q_k. Neither changes a formula. This reviewer did not edit any conclusion file.

Reviewed artifact hashes:

- JSON: `e29aa39981d21c33ca2765eb143d498a69d911f31c0c09d90c23e7dbdde86c06`.
- Markdown: `4499e5bf5cfd94c96f6114bb0ac33005b05a148bb8cd02ea0a9955e65a1981bf`.

## 8. Sealed three-entry specialization after root's further refinement

The final small repairs are accepted. The positivity identity now explicitly includes the differently typed least sections into the common source before subtraction: \(G_i-G_j=(I_iR_i-I_jR_j)^*M_x(I_iR_i-I_jR_j)\). The polynomial spaces are defined explicitly, the spectral second moment is called the trace of the square, R44 explicitly sets q=q_k, and the conclusion artifact documents exclusive end_line values. Root's current RMT10 also explicitly writes the trace of the operator square.

The root RMT now retains five pointwise entries. The final endpoint specialization correctly retains its earlier three entries without identifying their minimum with the newer five-entry minimum. Its derivative estimates are proved and integrated directly, and the nonlinear derivative is likewise applied directly. Adding two further nonnegative admissible bounds can only decrease the pointwise minimum: J_five≤J_three and I_five≤I_three. Consequently the five-entry Blo is at least the three-entry Blo, while its Bhi is at most the three-entry Bhi, by monotonicity of the displayed inverse coordinate. The unchanged three-entry endpoint formulas therefore remain valid. The parent owns later integration of the additional entries; this receipt seals the requested three-entry source, not a claim that it already contains the later global tightening.

Final accepted pins:

- Root RMT observed for correspondence/inclusion only in this final delta: `49d50bebe33a0f4a45b041e6fe6145dbe8e36240d3a17dfc20c6d38249f88309`.
- Specialization: `14a1716a06f3d36ffeb1475e36f9647d2df8ebf321dfe0cde876604c4340e282`.
- Endpoint: `aaf08f2eacb540f2d880c221196468247c9b180d364f188666b527741604fc81`.
- ERJ: `d28cce9c3d9c97661e783c4a5d718f185b9534ed2f4f238f657322fbd4c24511`.
- AU: `49775009fba50a77067a7ccca1a035ec965afe6bc914227dad75ca04dc31dddb`.
- Conclusion replacements JSON: `ae55d33b085bea3880427dde6ec16f475895b29f239d595bd689de364be1a279`.
- Conclusion replacements Markdown: `319744aafffb8bbbb477b31a11c11336021ee5616edb4769885144b3b7c8d9a8`.

Final bounded review result: PASS. All former defects in this review are repaired, and the accepted source explicitly preserves the scope difference between the sealed three-entry specialization and root's newer five-entry refinement.

## 9. Superseding propagation of the full five-entry tuple

The parent expanded the final specialization after the preceding three-entry cut. The complete new FV.M15a proof, all five entries of FV.M15, the four divided entries plus d_x in its nonlinear integral, and the changed R44/R47 conclusion replacements were read in full. Mathematical result: PASS.

The additional exact trace-norm term is \(T_q=d_x\|U-W\|_1/2\). Midpoint centering proves \(|F'|\le T_q\), while the two already proved trace-norm majorants prove \(T_q\le S_{\rm SP}\). The additional centered Hilbert–Schmidt term is \(S_{\rm HS}=\sqrt{\Sigma_x\operatorname{Tr}((U-W)^2)}\), where \(\Sigma_x=\operatorname{Tr}(C_x^2)-(\operatorname{Tr}C_x)^2/(2q+1)\). The self-adjointness of C_x in M_x makes Sigma the exact squared norm of its trace-centered operator. Tr(U-W)=0 preserves F' under that centering, and finite Hilbert–Schmidt Cauchy–Schwarz proves the stated bound. Both adjoints and traces remain in the original metric.

The specialization now uses exactly the current RMT13 tuple \((S_{\rm AW},T_q,S_{\rm SP},S_{\rm HS},A_q)\), with all entries retained. Its nonlinear tuple is exactly \(d_x\) together with the first four entries divided by the common positive \(a\sqrt{1-e^{-F/a}}\). Hence the existing direct integration and inverse-coordinate proof gives the stronger Blo/Bhi, with both arithmetic endpoint losses still retained in FV.M11 and AU.31a. ERJ's existing joint budget and inverse-power argument continue to use the same strengthened upper endpoint. R44 reproduces the exact five-entry minimum and both new definitions; R47 now describes the five-entry result. No formula defect was found. This full five-entry propagation supersedes Section 8's limited three-entry scope while preserving that earlier review as version history.

After the author froze the final display wrapping, the nonlinear integral was re-read: it retains d_x and all four divided entries, with only brace sizing and an aligned row break changed. The entire specialization is embedded text-exactly in the endpoint source. All eight Markdown old/new code blocks match the corresponding JSON values after disregarding only terminal display-newline padding.

Final frozen five-entry pins:

- Specialization: `f27ae832f61c5aa040f398c405034380103670bdc803eaca613d2124fa3e2481`.
- Endpoint: `d7b88749db6c2974330181ad0f0ca98a08be7aa9adca0a02a040651bf56cdc38`.
- ERJ: `d28cce9c3d9c97661e783c4a5d718f185b9534ed2f4f238f657322fbd4c24511`.
- AU: `49775009fba50a77067a7ccca1a035ec965afe6bc914227dad75ca04dc31dddb`.
- Conclusion replacements JSON: `0284d3ab60aed50ace4b1985c662cc6ad817aca22ed510181a7d49ce6452d3d3`.
- Conclusion replacements Markdown: `2f5b22eab0bfe1560758cf04df6ac61424315afcaa428d56fbf2315cf944441c`.

Final full-five-entry result: PASS, with no outstanding mathematical defect in this bounded propagation.
