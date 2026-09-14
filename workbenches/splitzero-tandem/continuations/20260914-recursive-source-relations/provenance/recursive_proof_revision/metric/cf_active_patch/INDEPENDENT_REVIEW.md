# Independent review of the current CF metric proof-site substitutions

Status: **PASS after the two type/domain corrections described below.**

This is a bounded mathematical review of the isolated derived ACM and HC proof bodies. The reviewer edited no mathematical source and ran no compilation. Compilation and cumulative integration belong to the patch author.

## Files read and accepted

The reviewer read the complete derived and original bodies of both files, the complete RMT1–22 dependency, both complete patch diffs, and the final changed passages after the author made the requested corrections and display-layout changes.

| File relative to this patch | SHA-256 |
| --- | --- |
| derived/tex/cohorts/cf/13_ACM.tex | 2ca5d662b84804295f3172f2a1a46518cda56b918a70648129293d88da8272c5 |
| derived/tex/cohorts/cf/31_HC.tex | e73bd05ee517cb07bc0ed37b293aa33e51b1f3c2ca8aacc80678b1dd7e8d4b94 |
| originals/tex/cohorts/cf/13_ACM.tex | 9c02ddb50343b9924203eb6504649a536921b0df1d667006bf7df74f6351bf07 |
| originals/tex/cohorts/cf/31_HC.tex | 312b5d36aa1d1c593ac91c3fce573ec1e604d933e6fe22465e0e5c5370ee458a |

The root RMT file and its metric/dependencies copy are byte-identical, both SHA-256 8110fbb1c5796ad36a75cf364b7744d5852419608b9e890d83b5fde5c0a9844f. Additional directly read source passages were HT1–HT7 in cumulative_source_v1/tex/cohorts/cf/30_HT.tex, PSC.28–PSC.35 in 15_PAM.tex, and ISM30–ISM43 in incoming_pr29_metric/incoming_source_metric_control.tex. In particular, the atomic measure and the source inequality were checked against their actual bodies rather than inferred from the new patch.

## Corrections found and verified

1. The first HC14b draft defined a padded relation map into H but directed the reader to substitute it into ACM4, whose displayed expression expects the unpadded relation map before coefficient inclusion. The accepted file now names B_N^AW: P_(N−q) → P_N, sets B_N^theta = I_N B_N^AW: P_(N−q) → H, and displays the full formula Q_N^theta = B_N^theta ((B_N^theta)^* M_x^theta B_N^theta)^−1 (B_N^theta)^* M_x^theta. Every multiplication is now well-typed. The negative relation domain is explicitly the zero space.
2. The first HC14a draft said N ≤ 2q when taking quotient minima over arbitrary v in E. The accepted file restricts this to q−1 ≤ N ≤ 2q. This is the actual surjectivity range of HT7, so the fibres exist and the positive quotient Gram is defined.

Both repairs are present in the accepted HC hash above. No outstanding mathematical correction was found within this bounded substitution review.

## ACM11a–16: complete propagation on the original path

The exact substitution is E_q = S_AW, O_q = S_SP, B_RMT = F_ACM, C_RMT = C_ACM, and U_RMT = U_ACM, W_RMT = W_ACM. The original reference convolution mass, arithmetic measure, ascending coefficients, full relation polynomial and relation-map inclusion are unchanged by ACM1–5. Consequently the trace pairing is the same signed derivative in both presentations. Its scalar density retains the required inverse metric v(U−W)M_x^−1v*.

The five simultaneous bounds are all retained: ordered relative spectrum, actual midpoint trace norm, overlap majorant, centered Hilbert–Schmidt expression, and the full-angle expression. The trace-zero identity permits both midpoint centering and trace-mean centering. In particular T_q ≤ S_SP has the correct direction: the latter bounds the trace norm from above. Both original q-entry angle lists are retained, including the designated zero and all additional zero angles; the 2q−1 concavity count agrees with RMT11.

The strict positivity argument has the required original moment structure. If F = 0, equality of the two crossed determinant ratios forces equality of their minimum sections. The constant representative is then orthogonal to chi P_q. The degree-q polynomial chi^{#_k}(S) = conjugate(chi(k−conjugate(S))) equals conjugate(chi(S)) on the original line, so this orthogonality contradicts the positive moment norm of chi. This establishes F > 0 and makes every denominator z_x positive. On the fixed compact path, the denominator is bounded away from zero. The only rank-stratified term is the intersection dimension, which is Borel; this does not obstruct any integral.

The formulas c_j(x) = (b_j−1)/(1−x+xb_j) preserve order, since their derivative with respect to b_j is positive. Their integrals are log b_j. Therefore ACM13 correctly retains the full ordered-spectrum sum before its (2q−1) log condition-ratio consequence. The derivative of H_a is exactly 1/(a sqrt(1−exp(−B/a))); its inverse is Psi_a(t) = 2a log cosh(t/2). Dividing each of the five derivative bounds by z_x gives precisely I_q, so all five controls propagate to the nonlinear coordinate.

For the finite signed construction, multiplication of the geometric sum by I−H_x^circ proves C_x−C_x^[p] = (H_x^circ)^(p+1) C_x. Every factor is a real function of the same positive relative operator D and is self-adjoint in M_x. Removing the trace mean preserves its pairing with U−W. The residual bound uses every eigenvalue and the valid inequality Tr((U−W)^2) ≤ 8q−6; thus e_p ≤ vartheta^(p+1) sqrt(K_D(8q−6)) tends to zero for the fixed source pair. ACM16 intersects additive, nonlinear and signed intervals with the correct signs. It makes no uniform-in-k assertion. The scalar source case has zero diameter and zero signed residual and returns the original endpoint exactly.

The final primitive is the original successive-monic-division primitive from ISM38–41. The two tensor signs multiply to +1. The proper-support residual is retained in the displayed quotient rather than erased by a full-source primitive. This matches the exact inclusion-induced relation in ISM42–43 and preserves the independent coefficient-face and outer-label data.

## HC9–11: signed Gamma interval

The new Gamma comparison has initial value F_0 = B_k^Gamma and final value B_k. Its source coordinate identification is y = u on S = k/2+iu and preserves the full chi of HT2 and the full convolution mass of ACM2. Thus beta_(p,Gamma)^− ≤ B_k ≤ beta_(p,Gamma)^+ is a literal application of the ACM bounds.

Writing T_k = 4q log(D_h k), the exact identity R_k = B_k−T_k gives the lower endpoint max(0, −T_k, beta^−−T_k), and the two upper bounds give min(Uhat_k, beta^+)−T_k. Likewise Delta_k^Gamma = B_k−B_k^Gamma gives HC10 after subtracting the same reference value. The signs in both intervals are correct; no positivity is imposed on the signed correction.

HC11 explicitly describes only the older coarse bound functions obtained by removing the beta entries. It does not assign the old positive quadratic width to the refined intersection. The refined intervals contain the actual endpoint for each fixed source because they intersect proved bounds on that same endpoint; the coarse-width calculation does not construct an arbitrary endpoint or a hypothetical arithmetic packet.

## HC14a–d and HC13a: actual source-phase transfer and energy budget

HC14a is the literal coefficient restriction from P_(2q+2) to H = P_(2q). Its continuous form and atomic form agree with HT3–HT7, including the complete source map, the relative variables, the 2pi/L mass factor, and u_r = (2pi r+theta)/L. The source sandwich is obtained by congruence restriction of PSC.33 before quotient minimization. Taking infima on the identical nonempty J_N fibres then proves the quotient sandwich in its corrected q−1 ≤ N ≤ 2q range.

The explicit corrected projections have codomain H and are orthogonal for M_x^theta. The same nested flags give the full spectra 0^[q], 1^[2], 2^[q−1], including the zero relation domain. Hence the derivative, all five pointwise controls, the nonlinear coordinate, and the signed finite residual transfer by the displayed substitution. HT6 proves positivity of every finite atomic moment Gram; the same chi^{#_k} proof is therefore valid at the atomic endpoint as well. In particular all nonlinear denominators remain positive throughout this actual path.

The source sandwich puts the eigenvalues of D_theta in [1−eta, 1+eta]. HC14 consequently has the valid improved factor 2q−1, and retains the stronger actual J_theta, ordered spectrum, nonlinear I_theta and signed center before taking that scalar consequence. HC14c uses the same residual exponent and constant as ACM15 with separately calculated source-phase operators.

For HC14d, U_(k,p)^ar is at least the actual positive B_k, so H_(2q−1)(U_(k,p)^ar) is within its positive domain. With the actual path quantities J_theta, I_theta, j_(r,theta), e_(r,theta) held fixed, the three displayed functions of their initial scalar are increasing: the additive and signed terms have slope one, and H_a and Psi_a are increasing. Substituting the proved upper bound for B_k therefore preserves each upper inequality. Their minimum is still an upper bound for B_(k,theta). Combining this with the unchanged weighted HC13 lower bound gives HC13a with all original w_N, derivative-source energies, phase metrics and boundary terms retained. No new energy estimate is assumed.

## Preservation of the averaged quotient paragraph

The complete paragraph beginning “For the averaged original phase metrics” and ending before the next subsection was compared directly. Its mathematical text, punctuation, spacing and line arrangement are character-for-character identical after CRLF-to-LF comparison. The original has 529 characters, including nine CR characters; the regenerated derived paragraph has 520 characters and LF line endings. The original file bytes remain separately preserved. This is text preservation with a recorded line-ending change, not a claim of byte identity for the regenerated paragraph.

The paragraph continues to use its already proved quotient-Gram comparison. The patch does not promote that average to an unproved original source measure, and does not apply the source-phase RMT substitution to the averaged quotient metrics.

## Scope

This receipt accepts the exact back-propagation into the stated current CF proof sites, after the two verified repairs. It does not claim a new audit of every earlier AW, EP, theta-source or Deligne proof, nor a uniform arithmetic estimate or an RH conclusion. All earlier proofs remain required parts of the cumulative source. Compilation is reported separately by the patch author.
