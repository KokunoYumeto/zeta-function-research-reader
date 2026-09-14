# Independent review of the actual-moment recursive propagation

Date: 2026-09-13. Outcome: **PASS at the corrected v3 pins below**.

This review extends INDEPENDENT_MATHEMATICAL_REVIEW.md and INDEPENDENT_SAMPLING_REVIEW.md. Those receipts record complete reads of the earlier AT, AW, SP, PSA and FC bodies and originals. I read the actual new proof paragraphs, theorem replacements and nonlinear endpoint formulas in all five sources, the complete revised R58 paragraph, and the complete RMT1--RMT18 dependency. I also read the complete independent RMT_ANGLE_SUBREVIEW.md and checked its explicit section, projection and angle derivation. I made no source edits.

## Accepted physical byte pins

| File below this directory | SHA-256 |
|---|---|
| staged/tex/next_edition/AT_complete.tex | 631a24454cc04c9224afd666afb7d055895552ed5f62a6e873d21f9caa11628b |
| staged/tex/next_edition/AW_complete.tex | 797f9661b1ccfa2de1f5ce726a855d60b8eb74e6abf6acee0d8bbaf84e798075 |
| staged/tex/tau_signed_projection_control.tex | cb1b198b261381981d0dbb1d5d5bb5fd994d1167186852cf7843fc9c881c64f1 |
| staged/tex/periodized_source_intake_proofs.tex | 758fca8acf534f958f0941debbd331e947f0055bf1762223090aaa7a2d9042b8 |
| staged/tex/periodized_curvature_control_bridge.tex | fd0b65e4790bc4b870473da7dffc17a5d340e9fe14992b87f28ec34b3044e155 |
| conclusion_replacements/R58_NEW.tex | 1967c3bf5ac605ad8b893d06eba0d5b91a1fd2f4a73910ead0c71e73dfcff405 |
| dependencies/recursive_metric_transport.tex | 034c7b72c44a02c2874e634124b94615575948203bb14fcdb3e5284f53f80e1b |

All five staged hashes were independently checked against PATCH_MANIFEST.json v3. R58_MAP.json now records physical file hashes: its new pin matches the row above and its old pin matches c79b1efcdac8e2757c4e97f502aac1a06229d9082050bdecd60197a9e56f8380. This resolves the metadata mismatch in the earlier sampling review. PSA now explicitly writes the trace of the square as \(\operatorname{Tr}((U-W)^2)\) and uses the prose “trace of the square”; both requested presentation repairs are present.

## Exact original-moment specialization

AT/AW/SP retain the original Gamma and arithmetic measures and the already proved identity of every source Gram and included relation map. Their RMT dictionaries identify \(x=t\), the metric derivative, both window operators, and now the scalar count \(a_{\rm RMT}=a_q\), where \(a_q=2q-1\). Thus the same four quotient determinants and the same signed derivative are used.

PSA/FC use the arithmetic measure \(m_{h,k}(y)\,dy\) and the actual finite positive atomic measure
\[
\sum_{|n|\le J}\frac{2\pi}{L}m_{h,k}(2\pi n/L)\,\delta_{2\pi n/L}.
\]
The previously reviewed Fourier calculation proves that its degree-\(2q\) Gram is exactly the restricted sampled source form. The zero atom retains its full weight; the unscaled zero vector and its \(L^{-1}\) metric have not been changed. The positivity needed at the atomic endpoint is already proved by the sampled source lower bound. The later angle calculation is therefore applied to two actual moment measures on the literal line \(S=k/2+iy\). No generic positive coefficient matrix is assigned this measure structure.

The complete two-positive-form proofs remain available separately. The new paragraphs specialize those finite identities and append the additional angle bound on their original moment source; they do not replace their earlier algebraic domain.

## Full angle count and strict positivity

For the original minimum sections \(R_N:E\to H\), the image \(K_N\) has dimension \(q\). For nested cutoffs \(i\le j\), \(R_i-R_j\) is a relation and \(R_j\) is orthogonal to it. Hence
\[
R_j=\Pi_jR_i,\qquad R_i^*MR_j=G_j,\qquad
G_i-G_j=(R_i-R_j)^*M(R_i-R_j)\succeq0.
\]
The isometric frames \(R_iG_i^{-1/2}\) and \(R_jG_j^{-1/2}\) have cross matrix \(G_i^{-1/2}G_j^{1/2}\). Its squared singular values are the \(q\) positive numbers \(\cos^2\theta_\nu\), and their determinant is \(V_j/V_i\). The projection-difference blocks have eigenvalues \(\pm\sin\theta_\nu\), with every common vector giving a zero angle.

The two crossed pairs are \((q-1,2q)\) and \((q,2q-1)\), so both full lists have length \(q\). For the second pair both minimum spaces lie in
\[
\mathcal P_{2q-1}\cap(\chi\mathcal P_0)^\perp,
\]
which has dimension \(2q-1\); their intersection therefore has dimension at least one. One distinguished zero angle is displayed separately. The other \(2q-1=a_q\) scalar costs retain every additional zero. Thus \(\mathcal B=0+\sum_{\nu=1}^{a_q}\lambda_\nu\) exactly. Concavity of \(z\mapsto\sqrt{1-e^{-z}}\) gives
\[
|\mathcal B'|
\le d\sum_{\nu=1}^{a_q}\sqrt{1-e^{-\lambda_\nu}}
\le a_q\sqrt{1-e^{-\mathcal B/a_q}}\,d.
\]
The stated coefficient retains the forced common direction; it does not assert that two \(q\)-element lists contain only \(2q-1\) geometric entries.

Strict positivity uses the actual moment measure. If \(\mathcal B=0\), both nonnegative crossed log determinant ratios vanish. For the first pair, positive semidefinite \(G_{q-1}-G_{2q}\) and determinant ratio one force equality of the two Grams, and the displayed squared-norm identity then forces equality of the sections. Thus \(1\perp\chi\mathcal P_q\). For
\[
\chi^{\#_k}(S)=\sum_j\overline{\chi_j}(k-S)^j
\]
one has \(\chi^{\#_k}(S)=\overline{\chi(S)}\) on the original line. Pairing \(1\) with \(\chi\chi^{\#_k}\in\chi\mathcal P_q\) would therefore give \(0=\int|\chi|^2\,d\mu_x\), contradicting the positive Gram of the nonzero polynomial \(\chi\). This proves \(\mathcal B(x)>0\) for the full closed path, including its atomic endpoint. Continuity and compactness justify the positive denominators on each fixed path; no uniform lower bound in tensor order is claimed.

## Three-bound integration and nonlinear interval

The former bounds \(E=S_{\rm AW}\) and \(O=S_{\rm SP}\), and the angle bound \(A=a_q\sqrt{1-e^{-\mathcal B/a_q}}\,d\), bound the same \(|\mathcal B'|\). Thus their pointwise minimum gives
\[
|\Delta\mathcal B|\le J^{(3)}=\int_0^1\min\{E,O,A\}\,dx
\le\mathcal J\le\mathcal L_q(D)\le(2q-1)\log\kappa.
\]
The new theorem statements AT18, AW14 and PSA25, and the actual applications AT19, AT22, AW18, FC13a and R58 use this stronger quantity at their original claim sites. In particular replacing \(-\mathcal J\) by \(-J^{(3)}\) in the quartet lower bound has the correct direction. SP13's generic proof is retained and its original-moment specialization is stated explicitly in SP13a--SP13c.

For \(\mathscr H_{a_q}(B)=2\operatorname{arcosh}(e^{B/(2a_q)})\), direct differentiation gives
\[
\mathscr H_{a_q}'(B)=
\frac1{a_q\sqrt{1-e^{-B/a_q}}}.
\]
Its increasing inverse on the positive range is \(2a_q\log\cosh(z/2)\), continuously extended at \(z=0\). Dividing each of the three inequalities by the same positive factor gives the printed minimum integral \(I\) and
\[
|\mathscr H_{a_q}(\mathcal B(1))-\mathscr H_{a_q}(\mathcal B(0))|
\le I\le\int_0^1d\,dx=\log\kappa.
\]
The maximum of the additive lower bound, zero and the inverse-coordinate lower bound, and the minimum of the two upper bounds, therefore give precisely AT19a, SP13c and PSA25a. FC13a and R58 point to this same actual-moment interval. The formula retains the original endpoint value inside the exponential, all \(a_q\) factors, the factor two in the argument, and the signed difference. There is no reversal of the direction of either comparison.

## Repairs found during this review and their verification

The first propagation cut reused \(a\) for the angle count, AT's spectral midpoint, AW's root in \(\chi=S-a\), and PSA's exponential source weight. In particular the q=1 AW sentence “gives \(a=1\)” conflicted with its retained arbitrary root \(a\), and PSA's later \(\kappa_{a,D}\) could refer to the new count instead of its actual source weight.

The corrected files consistently call the new angle count \(a_q=2q-1\). The original AT midpoint, AW root, and PSA source weight keep their original meanings. The exact RMT parameter dictionary is now explicit in AT/AW/SP, and PSA's source \(\kappa_{a,D}\) remains distinct from every nonlinear \(a_q\) factor. I checked the repaired formulas and their surrounding paragraphs, rather than only a replacement count.

For q=1, AW22 now explicitly uses \(a_q=1\). Its refined radius is \(I_{h,k}\); AW23 sets \(L=I_{h,k}/2\), while \(A_0=\operatorname{arcosh}(e^{\mathcal B(0)/2})\). This is the exact inverse of the preceding inequality for \(2\operatorname{arcosh}(e^{B/2})\). No factor two is missing. The prior \(\log(b_3/b_1)\) bound remains as the proved upper bound on \(I_{h,k}\).

Every empty sum and zero relation domain retains its previous meaning. At proportional moment forms, all eigenvalue differences vanish, so the two minimum integrals and the angle control vanish; the nonlinear interval returns the unchanged \(\mathcal B\). Strict positivity of that value follows from the actual moment argument, including q=1.

The dependency use is acyclic: the revised endpoint theorem uses RMT, which uses the earlier determinant derivatives, finite projection-trace arguments and full angle proof, rather than the revised endpoint theorem. This review accepts this corrected propagation cut; a later additional estimate requires its own bounded review.
