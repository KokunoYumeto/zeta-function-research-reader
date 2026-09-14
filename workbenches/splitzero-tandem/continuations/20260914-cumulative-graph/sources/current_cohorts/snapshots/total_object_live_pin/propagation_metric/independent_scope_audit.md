# Independent metric propagation scope audit

Date: 2026-09-13. Auditor: `/root/metric_transitive_propagation/metric_scope_audit`.
Scope: read-only audit of the 341-page current cumulative TeX tree. This file is the auditor's sole owned output. No live mathematical source has been edited by this audit.

Source root: `output/tau_split_zero_counterfactual_continuation_20260913/tex`.

Initial source hashes:

| Source | SHA256 |
|---|---|
| modules/AW.tex | 9d1470feff3f6482c890a760da9f682b2944529de2443e40e1bd417c4d8c7b83 |
| modules/AT.tex | 9fa19a509edf91f5aa0a9cb4762485449196d0b1ff521f2445f791fa3290cc75 |
| continuation/ACM.tex | c2caa5a1bdd6fcc02794f4e112fd783cebb465048bd696002d417ca4b1550289 |
| continuation/SP.tex | 180cd8a83a59e692fc0fa16a6622794927360df42317dc9d0ec3bdd6dbd7cd1a |

## Mathematical dependency and sign audit

Every relevant arithmetic/reference four-endpoint correction is the same signed scalar
\[
 \Delta=F(1)-F(0),\qquad
 F(x)=\log\frac{V_{q-1}(x)V_q(x)}{V_{2q-1}(x)V_{2q}(x)},
 \qquad F'(x)=\operatorname{Tr}((U_x-W_x)C_x),
\]
on the common source `H=P_{2q}`, with its original increasing-power coefficients. Here `C_x=M_x^{-1}(M_1-M_0)` and the original relation and source flags give `U,W` spectrum `0^q,1^2,2^{q-1}`. The relation map in SP lands in H; AT/AW's relation map lands first in P_N. Their exact comparison is `B_SP=I_N B_AW`, already proved in ACM3–4. The original `q=1` zero relation domain and all repeated endpoints must remain.

The strongest proposed local metric refinement is valid:
\[
 a(x)=c_{q+2}-c_q+2\sum_{j=1}^{q-1}(c_{2q+2-j}-c_j),
 \quad t(x)=\tfrac12(c_{2q+1}-c_1)\|U_x-W_x\|_1,
\]
\[
 o(x)=\tfrac12(c_{2q+1}-c_1)
 \min\{4q-2s_x,\sqrt{(2q+1)(8q-4-2\operatorname{Tr}(U_xW_x))}\}.
\]
The independently checked finite-dimensional arguments give `|F'| <= a`, `|F'| <= t`, and `t <= o`. Thus
\[
 |\Delta|\le C_*:=\int_0^1\min(a,t)
 \le C_*^{\rm ov}:=\int_0^1\min(a,o)
 \le L_q(D)\le(2q-1)\log\kappa(D).
\]
This retains the exact common-source cross-pairing; it neither changes masses nor asserts that the isometry of AW preserves the arithmetic observation. The latter defect is AW12/ACM8, and QT retains its separate corrected, class-preserving commutator.

For any proved reference value B_ref the exact signs are `B_ref-C_* <= B_ar <= B_ref+C_*`. For an independently proved arithmetic interval `[L_ar,U_ar]`, the signed intersection is
\[
 \max\{L_{\rm ar}-B_{\rm ref},-C_*\}\le\Delta
 \le\min\{U_{\rm ar}-B_{\rm ref},C_*\}.
\]
Consequently `C_* >= max(0,B_ref-U_ar,L_ar-B_ref)`. The nonnegative lower bound here applies to the control C_*, not to the signed correction Delta.

## Genuinely affected source locations

| Source and initial location | Required propagation |
|---|---|
| AT18–22, beginning near line 313 | Strengthen the base theorem, both endpoint inequalities AT19, the pointwise trace AT20, its proof, and the quartet application AT22. Retain the old coarse estimate as an immediate weaker consequence. The condition-number lower consequence becomes `(4q log(delta k/(2 sqrt5))-B_ar)/(2q-1)`, with the sharper `C_*` inequality before weakening. |
| AW14/AW16/AW18, near lines 219,263,300 | Add the exact trace/overlap minimum to the strengthened theorem and quartet consequence while retaining L_q and its entire spectrum, isometry, observation defect, commutator, and q=1 angle formula. |
| SP10/SP13, near lines 151,183 | SP's overlap bound stays true; current integrated statement must contain the simultaneous AW/exact-trace control and its comparison to the SP envelope. SP's original metric operator is `T_x`; do not identify it with AW's source isometry T. |
| ACM9–13, near lines 114–195 | Preserve the actual AW/SP identity maps, then include the exact trace-norm minimum before the existing overlap minimum. No circular source dependency should be introduced. |
| QT26, near lines 460–480 | Replace the spectral-only symmetric interval by the stronger symmetric interval `[-C_*,C_*]` before intersecting with `[E-F,E+F]`. Keep QT's actual corrected commutator and relation-speed error. |
| reconstruction R8, near lines 310–345 | The exact four-factor identity stays unchanged; following prose must state the current joint control, not call the signed term uncalculated or cite only the old full-spectrum interval. |
| combined_restriction CR2–6, near lines 20–124 | Keep L_q defined, add C_* and C_*^ov, replace every inherited symmetric spectral endpoint in CR3–4 with C_*. Replace the left side in the compatibility CR6 with C_* and retain its nonnegative sign. Preserve CR5's exact arithmetic observation defect. |
| HC9–10, near lines 226–243 | Intersect the residual and signed intervals with the new control. Keep their older coarse versions as named predecessors if needed for HC11. The assertion of strictly positive width applies only to the old coarse interval; it cannot be carried onto the refined interval without evaluating the actual source data. |
| HC14 consequence, near lines 348–350 | The phase allowance is independently derived and should remain. The original arithmetic upper appearing in the consequence for phase energy should be replaced by the minimum of all proved arithmetic uppers, including B_Gamma+C_*^Gamma. |
| TW20, near lines 324–365 | Its exact arithmetic lower bound, with contraction, phase, control and trace residuals, is unchanged. Carry its entire literal lower side into the joint same-source interval rather than replacing it by its coarser first term. No new asymptotic for C_* follows. |
| CA14/CA21–24, near lines 163–180 and 280–344 | Re-run the finite source construction on the sigma interpolation explicitly, giving C_*^sigma. Insert it in CA14 and every endpoint in CA21; preserve the AGT nonlinear interval and all scalar error limits as valid consequences of the weaker envelope. |
| AAM24→AAM28→AAM29, near lines 326–447 | Add the new arithmetic upper `B_sigma+C_*^sigma`, retain the separate angle upper, and substitute the strengthened total upper in every later normalized/control bound. The exact maps, full phases, positive norm factors, and critical threshold remain. If the upper is called `all`, include the original Gamma control `B_Gamma+C_*^Gamma` and HC15's U_nu as well, with their existing exact definitions. |
| MP61,67,80, near lines 526,570,683 | The signed kernel identity, finite quadrature enclosure and final endpoint identity stay unchanged. Intersect the finite certified quadrature interval with the joint metric control; update the final inherited arithmetic upper to the same current bound. Do not convert an approximate numerical first-pair calculation into a certificate. |
| MP_ERRATA | Propagate changes to descriptions of the current refinement if the errata mention the obsolete arithmetic estimate, while preserving the original-source versus transformed-wrapper provenance. |

## Distinct Gram comparisons that remain unchanged

1. **CA sigma and original Gamma are different reference forms.** CA3 uses `sigma(y)=|Gamma(1/4+iy/2)|^2/(2pi)` with mass `sqrt(2pi)`. AT/AW/SP use the k-fold Gamma convolution with mass `(2pi)^(k/2)`. The comparison between them is not an identity. The same finite-matrix proof applies separately to `M_x^sigma=(1-x)H^sigma+xH_ar`; retain superscripts, all constants and both actual references. CA5–7's pointwise form/quotient bounds and CA12's asymmetric scalar enclosure do not become signed trace inequalities by symbol replacement.

2. **AGT angles.** AGT11 already bounds `|F'|` by `d_x sum sin(theta_l)` using the two projection differences. Since `U-W` is their signed sum, the trace-norm triangle gives `t(x) <= d_x sum sin(theta_l)`. Therefore the exact trace-norm control already retains this pointwise information. AGT19 remains a separate proved nonlinear endpoint enclosure and should stay in combined endpoints. Its same argument applies to sigma as CA17b already proves. A two-bound claim of 'all' that drops AGT19 is too narrow.

3. **Holonomy.** HC14's `2q log((1+eta)/(1-eta))`, its averaged `2q log(1/(1-eta^2))`, and MP79's two-endpoint allowance are not the old arithmetic-versus-Gamma AT18 estimate. Their Grams are phase/averaged quotient Grams. They must not be altered by a global `2q -> 2q-1` replacement. At fixed phase an additional common-source proof is available: PSC33 gives the full source sandwich `(1-eta)M <= M_theta <= (1+eta)M` at the required degree. Define the separate interpolation `(1-x)M+xM_theta` on `H=P_{2q}` and its actual flags. Then the generic AT argument proves `|B_theta-B_ar| <= C_*^theta <= (2q-1)log((1+eta)/(1-eta))`. This is a proved transfer through a newly specified same-source comparison, not an identification of phase and Gamma metrics. The averaged quotient estimate does not receive that improvement automatically: phase-averaged quotient minima are not the quotient of an averaged source without the retained relation correction.

4. **PAM/PSC energy.** PSC6 controls the four-volume in a fixed holonomy metric from the literal derivative energy. Its bound is not directly an arithmetic/Gamma signed correction. Combine it with the original arithmetic upper only through the proved phase-transfer map and allowance. PAM's boundary matrices, nonzero first-cutoff residual and source-period Gram constants are unchanged by AW/SP.

5. **TW/CA condition envelopes.** TW's pointwise density comparison and monic norm asymptotics, CA26–29's compulsory original-Gamma spectral spread, and AAM25's exact cost of the scalar angle upper all remain valid at their stated types. A lower bound on log kappa does not provide a lower bound on the signed correction or the exact joint control. AAM25's positive asymptotic applies to its named angle envelope, not the minimum including the new joint bound.

6. **FPK/LC/HG fixed-object limits.** FPK23–29, LC26–28 and FKG23 concern `N -> infinity` with fixed `h,k,chi`. Their complete constants, jets, logarithmic exponents and exact algebraic/Hilbert graph maps remain unchanged. They give no uniform moving-k error for q=[1+k(m-1)](k+1)^2. Only a statement connecting to the new finite bound is appropriate; rewriting the limit as a uniform counterfactual contradiction would be unsupported.

7. **AG/TO/CAU/MFC/CFA algebraic maps.** Their coefficient carriers, source inclusions, nilpotent tensor sum, complete Taylor unit and support kernels are inputs to the metric evaluation. No arithmetic endpoint inequality was found in AG that is changed by the finite trace refinement; its final assertion that all source metrics are determined by the original g is still exact. A cross-reference may connect the new bound, but the algebraic morphisms do not require a metric-driven rewrite.

8. Other search matches in BF, DC, OCQ, WBR, HK and SPC use the letter Delta or B for different spaces, maps, traces or boundary objects. No dependency on the arithmetic four-endpoint correction was found at those matches. Do not apply a textual replacement there.

## Acyclic proof placement

The parent proposes placing a complete independent strengthened finite-dimensional proof in AT18–22. This is safe if its derivation uses AT's existing determinant differentiation and flags only: prove spectra from the original nested subspaces, prove the finite projection-trace inequality, prove both trace-norm bounds, then integrate the ordered relative eigenvalues. AT must not cite AW/SP/ACM as premises. AW may continue to cite AT15 and give its independent spectra/isometry proof. SP and ACM can then cite AT, AW or reproduce the elementary arguments; downstream QT/CA/AAM/CR use the resulting bounds. This gives no circular theorem dependency even if chapters are printed in a historical order.

Status: scope audit complete; mathematical strategy passed with the reference-type, phase-transfer and historical-width qualifications above. Full changed-file and patch-manifest review remains to be performed when the parent's derived sources are ready.
