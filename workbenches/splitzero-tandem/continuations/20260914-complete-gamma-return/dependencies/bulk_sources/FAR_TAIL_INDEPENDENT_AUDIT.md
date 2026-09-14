# Independent original-source tail proof

Authoring scope: `/root/joint_schur_exact_audit/far_tail_check`, delegated by the joint-Schur mathematical audit task. No reader inputs, PDF builds, publication files, or upstream sources were changed.

The durable user provenance remains in the existing workspace logbook. This audit records the bounded mathematical calculation assigned to this agent: verify the proposed original Gamma far-tail estimate, verify the subsequent small-interval estimate, and prove their transfer to the complete high relation determinants without losing the original polynomial degree or Gamma constants.

The complete proof is `far_tail_independent.tex`, FTC1–26. Final SHA256:

`0a201492929cfa329070b45eba0f352ad6d90f2ffe47c900b7b24741452d95eb`

The proof includes:

- Original roots, all multiplicities, original relation dimensions q and q+1, and the exact coefficient matrix of P(S) -> P(c+iqz).
- Gamma upper and lower constants from Euler rotation and reflection, including a derivation of the reflection identity and the exact constant ratio.
- The original-root exterior expansion with its explicit absolute remainder.
- A full shifted-Legendre proof with the stated finite constants.
- The general far cutoff and angle estimate on the precise interval |y| > qB.
- The finite q >= 2 Rmax threshold and the uniform far bound 512q exp(-19q)/(59 sqrt(cos 1)).
- The inner bound with epsilon = 2^-10, including the retained extra numerator factor (2 epsilon^2)^l and an elementary certificate that beta < exp(-2).
- The complete central interval epsilon <= |z| <= 64. The annulus epsilon < |z| < 1 remains inside its original Gram matrix.
- Original-basis Gram congruences, determinant bounds, signed numerator-minus-denominator correction, both actual high endpoints, and original Gamma-convolution mass factor.
- Exact finite thresholds, including the stronger q >= 2048 Rmax threshold when the central Taylor proof requires tau_epsilon <= 1/4.

The polynomial estimate and tail integral were separately checked by the bounded `legendre_constant` child. That check confirmed the constants and made explicit D >= 0; here D = 2q+2s+2r-2 is automatically nonnegative.

The parent article `ORIGINAL_RELATION_BULK_CONTROL.tex` was read in its actual BRD22–42 span, with BRD13–21 and the coefficient/Gram definitions supplying the required dependencies. All Gamma constants, the paired-root estimate, finite degree factors, both exponential tail constants, BRD41a's one-sided interval, and BRD42's signs were verified.

One interval defect was reported to the parent: the original BRD32–33 wording used fixed F = {|y| > 64q} while allowing arbitrary B in its tail integral. For B > 64 this would omit the interval 64q < |y| <= Bq. The second checker independently identified the same defect. The parent repaired it by defining the precise moving region F_B = {|y| > qB}, retaining the fixed central denominator, and explicitly specializing B = 64 back to the original F. This final wording was independently reread and accepted. The independently checked B = 64 result was already correct.

Final parent source pinned after the cutoff repair:

`ORIGINAL_RELATION_BULK_CONTROL.tex`

SHA256 `4d6e3df419edcedbe7e66e6f802bdeca6e088d9036c5b4c17692517995ebcba9`

The complete BRD22–42 mathematical claim set and its determinant transfer are accepted. The final read was bounded to the repaired moving-cutoff paragraphs; this record does not claim that all unrelated new prose in the final file was reread. The complete independent Gamma and Legendre proofs remain in FTC1–26.

Validation performed: exact polynomial division for the 22/7-minus-pi integral, complete TeX environment nesting, and a tag inventory FTC1–26. This file makes no PDF compilation or visual-review claim.
