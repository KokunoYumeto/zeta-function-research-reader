# Independent full review of arithmetic_amplification_match.tex

Date: 2026-09-13. Reviewer: `amplification_rate_review`.

Assignment received verbatim:

> AAM proof now written full at total_object/arithmetic_amplification_match.tex. Please fullread bounded adversarial check formulas AAM1–36 (about27k chars), particularly matrixcongruence tracefloor, exactgeomcontrolphaseweights, constantsrates, windowuppermin, fixedk degree ratios incl N^t and normalizedlift vsG→0. No edits; urgenterrors + finalreceipt/sourcehash if clear. Mathfullfile ready.

Read all of `work/rh_counterfactual_20260913/total_object/arithmetic_amplification_match.tex`, including all prose and proofs surrounding AAM.1–36.

Source SHA256 at the full read:

`24795CFB4E58906EEF30C20467EBF6361F6AB75998CF5FF77A8A0CA81BCB1DE2`

Final accepted stable source SHA256:

`8D4FE5196CB7D5893371D565DB8916A8C5C89CFC06AE64269462AEC9FE08534A`

The sole intervening change was the wording repair “both cosines” to “both hyperbolic cosines” noted below. A byte-preserving reversal of that exact ASCII phrase in the final source reproduces the original fully read SHA256 above. Thus the full mathematical review applies unchanged to the final source hash.

**Finding: pass; no mathematical error found.** No source edits made. No RH verdict is part of this review.

## Sources directly checked

The preceding bounded review read CA1–29, TW1–21, HT1–18, HC1–15, and CV.1–12 in full, with hashes recorded in `ARITHMETIC_AMPLIFICATION_RATE_REVIEW.md`. For the AAM degree-limit statements this review additionally read FPK.20–29, LC.24–28, and FKG.1–23, including its operator-convergence proof, original observation and primitive maps, algebraic quotient and Hilbert reduction, and the full quartet exponent calculation.

## AAM.1–8: original tensor packet and normalized control

The four roots in AAM.1 remain distinct because \(\delta\gamma\ne0\). Their nilpotent sum in each ordered local tensor factor has exact index \(1+k(m-1)\): the stated top multinomial coefficient is nonzero over \(\mathbb C\), and the next total degree forces some variable to exponent at least \(m\). Every independent real/imaginary sign count is realized, giving the stated complete cyclic polynomial and dimension. The parity values in AAM.5 agree with direct division of AAM.4 by \(kq_k\).

For the matrix congruence, direct multiplication gives

\[
G^{1/2}(AK+KA^*-kK)G^{1/2}
=G^{1/2}AG^{-1/2}+G^{-1/2}A^*G^{1/2}-kI
=G^{-1/2}(A^*G+GA-kG)G^{-1/2}.
\]

Thus the rank-two recurrence and trace calculation apply to exactly the normalized matrix of AAM.6. The complete primary space \(E_+\) is invariant under \(A\), so its image under \(G^{1/2}\) is invariant under \(G^{1/2}AG^{-1/2}\). The compressed trace is twice the real spectral trace minus \(k\) times its full dimension; this is exactly \(\mathcal L_k\), with all nilpotent multiplicities counted. Projection onto that subspace has trace pairing at most the positive eigenvalue of the trace-zero rank-two Hermitian matrix. This verifies AAM.8 without replacing the original quotient form.

## AAM.9–14 and AAM.29: endpoint weights and exact phase correction

The first and last weights are one; the \(q-1\) interior weights are two, so the sum is exactly \(2q\). Write \(\Phi_k\) as in AAM.12. Expanding each logarithm in AAM.11 gives

\[
\mathcal B_k=2\sum_Nw_N\log\varepsilon_{k,N}+\Phi_k-\Omega_k+P_k.
\]

Consequently

\[
\log\overline\varepsilon_k
=\frac{\mathcal B_k+\Omega_k-P_k-\Phi_k}{4q},
\]

which is precisely AAM.13's multiplicative identity, with no omitted phase factor. The trace floor supplies both the minimum and geometric-mean lower bounds. The threshold in AAM.14 follows by subtracting \(4q\log\mathcal L_k-\Omega_k\); the lower bound with both \(P_k\) and \(\Phi_k\) removed follows from the preceding equality and the same floor.

Replacing \(\mathcal B_k\) by the minimum of three valid upper functions remains valid, and AAM.29 retains the exact exponent \(4q\) for the geometric mean. Its next upper bound follows from

\[
\Omega_k\le4q\log(4q/e)+\mathcal E_k
\]

and nonnegativity of \(P_k,\Phi_k\). For the individual bound one isolates one nonnegative summand in AAM.14; the factor is exactly \(2w_N\), including both endpoint weights. No inequality reverses under any of these substitutions.

## AAM.15–23: exact arithmetic constants and amplification scales

The constants agree literally with TW8, including the powers of \(k\), \(k-2\), the original masses, and \(2^M\). The coefficient of \(k\) in \(\log(A_k/a_k)\) is
\(d_h=\alpha+\log(M_\alpha/\vartheta_h)\), while the logarithmic coefficient is \(p+1+B\). The actual even density proves \(M_\alpha>\vartheta_h\) by its strictly positive integral outside \([-1,1]\), hence \(d_h>\alpha>0\). This positivity is proved for the actual arithmetic constants and is not assumed for arbitrary positive inputs.

Because \(\log D_{2q}=O_h(\log q)\), \(\log q=O_h(\log k)\), and \(\mathcal L_k/(kq_k)\to\delta/2\), all four limits in AAM.20 follow with the displayed factors. In particular the last limit is \(4d_h/\delta\), not zero.

The two exact norm-window limits give \(\mathfrak n_k/q_k\to4/e\). Therefore

\[
\frac{\mathfrak n_k}{\mathcal L_k}\sim\frac8{e\delta k},
\qquad
\frac{\mathcal L_k}{k\mathfrak n_k}\to\frac{e\delta}{8}.
\]

The exact product identity then proves AAM.21's compensating lower growth for \(\mathfrak c_k\). Taking the logarithm of this positive ratio proves both limits in AAM.22. The finite lower estimate AAM.23 preserves the explicit TW error and the exact parity of the trace residual.

## AAM.24–30: actual finite upper functions

The spectral sum, angle inverse pair, and common-source constants match CA14 and CA17a–b. They act on the same four endpoint volumes. The interval inequality

\[
e^x/2\le\cosh(t+x)/\cosh t\le e^x\qquad(t,x\ge0)
\]

is valid: expansion gives the upper bound; \(\cosh(t+x)\ge e^{t+x}/2\) and \(\cosh t\le e^t\) give the lower. Substitution of the displayed half-arguments yields exactly AAM.25. Since \(q_k/\mathcal L_k\to0\), its constant deficit disappears after division by \(\mathcal L_k\). This is correctly stated as an upper-function overhead, not an asymptotic for the actual signed correction or the actual full spectral sum.

The independent HC8 upper function retains its coefficient \(2a\) on \(q_k^2\). Each remaining term divided by \(q_k^2\) tends to zero because \(k/q_k\to0\) and \(\log q_k/q_k\to0\). Hence AAM.27 and, after subtraction of the logarithmic threshold, AAM.30 have their stated constants. The minimum in AAM.28 keeps the more precise original spectrum instead of substituting its coarser scalar envelope.

## AAM.31–34: fixed-packet degree limits

FPK.25 and FPK.29 give the two complete reference asymptotics; LC.26 gives only the displayed leading logarithmic exponent for the actual measure. FKG.22 identifies their common coefficient as exactly \(\mathcal L_k\), and identifies the reference \(\log\log N\) coefficient as \((k+1)\ell_k^2\) for even \(k\) and zero for odd \(k\). AAM.31 does not assign that second coefficient to the actual mixed packet.

Subtracting the actual and original-Gamma leading logarithmic limits proves AAM.32. Exponentiation makes its \(N^{\pm\epsilon}\) formulation equivalent, with a threshold allowed to depend on the full fixed packet.

For fixed \(t>1\), the complete reference asymptotics give

\[
\log V_N-\log V_{\lfloor tN\rfloor}
\to\mathcal L_k\log t.
\]

The constants cancel, the difference of the \(\log\log\) terms tends to zero, and both remainder terms tend to zero. In contrast, for the actual measure the proved conclusion is only

\[
\frac{\log V_N-\log V_{\lfloor tN\rfloor}}{\log N}\to0.
\]

This follows by multiplying the leading-log limit at \(\lfloor tN\rfloor\) by \(\log\lfloor tN\rfloor/\log N\to1\). AAM.33 explicitly retains this weaker actual conclusion.

With \(\lfloor N^t\rfloor\), that logarithm ratio tends to \(t\), so the same subtraction gives \((t-1)\mathcal L_k\), exactly AAM.34. No error bound uniform in growing \(k\) is used in any of these steps.

## AAM.35–36: vanishing representatives and normalized lift

For each fixed packet, FKG.4–7 prove \(\|G_{k,N}^{\rm ar}\|\to0\), and FKG.8–9 retain the nonzero original arithmetic observation of every nonzero remainder. Expanding

\[
W=(A-cI)^*G+G(A-cI)
\]

gives the coefficient \(2\|A-cI\|\|G\|\) in AAM.35 by submultiplicativity. Its congruence is exactly AAM.6; thus the normalized operator retains the trace floor despite the unnormalized matrix limit. Positivity of \(G\) and \(\|G\|\to0\) force its smallest eigenvalue to zero, hence \(\|G^{-1/2}\|\to\infty\).

Finally direct substitution gives

\[
(RG^{-1/2})^*H_{k,N}(RG^{-1/2})
=G^{-1/2}GG^{-1/2}=I_{E_k}.
\]

Its operator norm in the actual source metric is exactly one, and its squared Hilbert–Schmidt norm is \(\operatorname{Tr}I=q_k\). Thus the statements in AAM.36 concern precisely the original finite source norm, not the Euclidean norm of its coefficient matrix.

The closing references to Deligne's separate finite-field calculation were not used to infer any arithmetic inequality in this review. All audited arithmetic comparisons above remain on their original domains.

## Minor prose note

Near AAM.25, “expanding both cosines into exponentials” can be changed to “expanding both hyperbolic cosines into exponentials.” The displayed functions and formulas are already correct. This is optional wording, not a mathematical defect.

The owner applied this wording change; its final hash and exact reverse-diff verification are recorded at the start of this receipt.

## Independent fixed-degree cross-check

The child reviewer `scale_crosscheck` independently read AAM.31–36 through the closing paragraph and returned: “PASS AAM31–36, read in full through closing paragraph; no errors found.” It separately confirmed the actual fixed-multiple logarithmic conclusion, the power-degree exponent \((t-1)\mathcal L_k\), the coefficient \(2\|A-cI\|\|G\|\), and the source-metric normalized-lift norms \(1\) and \(q_k\). No fixed-packet asymptotic is used uniformly in growing \(k\).
