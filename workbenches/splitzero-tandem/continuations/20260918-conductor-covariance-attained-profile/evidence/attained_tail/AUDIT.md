# Attained native-tail audit

**Primary verdict: proved as written.** This applies to the submitted mathematical statements on their retained original simple-quartet, source-order, fixed-period, full-conductor and root-comparison domain. The additive proof supplies the omitted finite constants and analytic details. It also proves the stronger envelope from every integer row \(r=2\), and, combined with the independently audited covariance total, a full-row weighted \(L^1\) error \(O_{\mathrm{actual}}(q\log q)\). Incoming build and diagnostic claims are not treated as locally executed evidence.

## Claim card

The unchanged data are \(k=4l+1\ge9\), \(j=k+4\), \(q=(j+1)^2\), \(q'=(j-7)^2\), \(\Delta=16j-48\), \(0\le v\le80\), \(L=q-v\), \(m=\Delta-v>0\), and \(s=1,j\). The quartet has \(0<\delta<1/2\), \(\gamma>2\); its period, logarithm branch, all \(a_{ab}\), and all derivatives \(\mu_h=E_A^{(h)}(0)\) are fixed. Source centres are \(c=j/2\) and \(c'=j/2-4\). The original Gamma measure, mass and complex-linear functional convention remain.

The row is the original attained minimum ratio
\[
\gamma_{r,s}=\log\frac{\min_z\|u_r+\sum_{t<r}z_tu_t\|_{s,c'}^2}
{\min_{P\ {\rm monic},\,\deg P=m+r}\|\chi_-P\|_{s,c'}^2},
\qquad u_r=\mathcal T_A(\chi_jS^r)/[\mu_v\binom{q+r}{v}].
\]
The finite envelope is the complete ATA17 expression. On \(j\ge257\) and \(j\sqrt{\delta^2+\gamma^2}\le2^{-33}q\), it bounds this row above and has centre \(\Delta\mathfrak f(r/q)\) with uniform error \(O_{\mathrm{actual}}(q/r+\log q)\). The submitted range \(R_j<r\le q+32j\) is valid; the audit strengthens it to \(2\le r\le q+32j\). The two exceptional degrees use NIB exactly. No claim evaluates \(\mathfrak f(0)\).

## Additive artifacts

- ATTAINED_FIBRE_AND_PROFILE_PROPAGATION.tex, ATA1–40: actual fibre bijection, complete projection slack, translation/conductor estimate, finite endpoint, discrepancy, weighted profile, correlated determinant, sublinear row sets, proper-source displacement.
- ALL_NONZERO_ROW_ENVELOPE.tex, AER1–22: envelope for every \(r\ge2\), uniform parity/dilation estimates without small-displacement assumptions, quantitative full-row profile and cumulative convergence.
- gpa/GPA_ATTAINED_TAIL_PROOF.tex, ATG1–28: both root/Gamma comparisons in every coefficient direction, all \(b^\pm\), inner-region terms, masses and rate-change constants.
- ../equilibrium/EQUILIBRIUM_NORM_PROOF.tex, EQ1–54: equilibrium and finite norm proof, particularly EQ43–54 for the power-exponential \(H^\pm\).
- ../asymptotics/LRC_SCALAR_RECONSTRUCTION.tex, LRS24: the same actual total is \(16C_\partial jq-128q\log j+O_{\rm actual}(q)\).
- ../PROFILE_COVARIANCE_BRIDGE.tex, PCB1–8: Robin derivatives, the \(\psi/\mathfrak f\) relation, and \(2\int_0^1\mathfrak f=C_\partial\).

These pieces form part of the cumulative proof repository. Every newly invoked companion implication was reconstructed and reviewed during this intake. Exact companion equation locators appear in the TeX.

## Dependency graph

1. NTG1–3 and NIB1–9 define actual relations, monic fibres, source and row ratio.
2. ATA6–8 proves the coefficient bijection and full old-Gram projection; ATA9–15 derives translation bounds from the recurrence with all mass factors.
3. ATG3–28 proves all-direction root/Gamma comparisons; EQ38–54 proves finite power-exponential endpoints and their centre.
4. AER11–14 integrates exact Robin derivatives across both root counts, retaining the \(v\)-displacement and full conductor. This proves the envelope independently of the native total.
5. PCB1–8 identifies its integrated mass. Pre-existing HJR25–26 then proves ATA23–25. Independently proved LRS24 sharpens this to AER16–20.
6. NTG14–15 and NTG23–25 turn the row estimate into the complete graph determinant, retaining \(\Omega_{R'}^{-1}\) and all cross pairings.
7. Original FTR/PRD/STF quotient maps propagate identical rows to actual allocations and CPQ quantities.
8. PRD22 gives all four degree-\(k\) displaced cutoffs. ATA36–39 expands and bounds each actual one-copy interval.

No row profile is used in the proof of HJR26 or LRS24. The total determines the accumulated deficit only after the independently proved envelope and mass identity.

## Obligation matrix

| Obligation | Status | Exact evidence |
|---|---|---|
| Monic affine domain before conductor | Passed | ATA5–7: inverse \(p_t=z_t\ell_r/\ell_t\), all \(\ell_t\ne0\). |
| Full preceding-relation subtraction | Passed | ATA8 explicitly uses \(G_{<r}^{-1}\). |
| Complete lower-ideal minimum | Passed | NTG8, SLC7–10; positive signed cofactor ratio retained. |
| Original mass and phases | Passed | ATA2,9–15, ATG7–13; \(\beta_s\) cancels only in matched ratio. |
| Shift under the two centres | Passed | \(z_{ab}=-i(\beta_{8,a,b}-4)\), ATA15. |
| Polynomial conductor norm for both orders | Passed | ATA10–15: Cauchy coefficient and full triangular Frobenius bounds, \(s\ge1\). |
| Both root counts, all coefficients, inner region | Passed | ATG14–19; no extremizer-only restriction. |
| Explicit \(b^\pm\) and size | Passed | ATG3,25,27–28; no hidden mass. |
| Square-coordinate shift \(-1/2\) | Passed | EQ38–43, AER2; power-exponential reference. |
| Jensen, quantiles, full exterior | Passed | EQ38–43 and exact EIQ providers; all \(x>0\) retained. |
| Moving parity including \(b=2\) | Passed | EQ45–54, AER5–10; no smallness assumption. |
| Root-count integration | Passed | AER11–14 works even for large \(\Delta/r\). |
| Exact mass | Passed | PCB1–8, original ECL16 coefficient. |
| Finite discrepancy and original total | Passed | HJR25–26, ATA21–25; sums explicitly end at \(q\). |
| Quantitative full-row \(L^1\) | Passed | LRS24 + AER16–20; row zero is an atom; row one uses NIB. |
| Trial slack | Passed | ATA18,25; stronger AER20 only for \(r\ge2\). |
| Correlated determinant | Passed | NTG23–25, ATA26–29. |
| Every \(o(q)\)-row set | Passed | ATA30–34, AER22; monotone integrable profile, exact quotient maps. |
| Proper-source displacement | Passed | PRD22, ATA35–39; two low intervals length \(b\), two high length \(2b\). |
| High-side coefficient | Passed | \(4b(16k-48)\mathfrak f(1)\); no extra four-copy multiplier. |
| Allocation split, signed flags, own source value, arithmetic sign | Out of scope | Expressly not consequences. |
| 329 checks, controls, three-pass PDF build | Not locally verified | Reported input state; source script and full claimed package unavailable in supplied paths. |

## Exact original providers checked

The authoritative ORIGINAL_NATIVE_TAIL_GRAM.tex was read at NTG1–3,8,10–25. NTG8 is the full monic minimum; NTG14–15 the determinant ratio; NTG20,22 the original conjugation, frame and phase; NTG23–25 the full old/later minimum. SZEGO_LOWER_GRID_CONTROL.tex was read at SLC1–21, including phase map SLC7, norm SLC10 and coefficient calculation SLC16–21.

In full_receiver_build/staging/14_CURRENT_KERNEL_AND_MULTIPLICITY_PROOFS.tex, HJR25 is at line 24454 and HJR26 at lines 24461–24466. The lower endpoint is exactly the maximum with zero of the outer return minus original OAR/FEX/PEC errors, including \((v-t_0)\mathcal L_s\). HJR21–22 gives weights one at \(r=0,q\) and two between.

NIB14–20 was read at lines 65426–65610. NIB14 is finite for every \(r\ge0\); NIB15 gives \(O(j\log j)\) on fixed linear ranges; NIB18–20 gives the old prefix. The submitted larger-prefix estimate correctly absorbs \(j^3/\log j\) into \(j^3\log\log j/\log j\) eventually.

PRD1–10 and PRD19–29 were read, particularly PRD22 at line 68734. The independent proper source remains degree \(k\), order \(1\) or \(k\), centre \(k/2-4\), and native cutoff \(N-v\). Its low shifts are \(b=8k+24\), high shifts \(2b\). Telescoping gives precisely the four intervals \(0,\ldots,b-1\); \(1,\ldots,b\); \(Q,\ldots,Q+2b-1\); \(Q+1,\ldots,Q+2b\). The condition \(2b\le32k\) puts both high intervals inside the separately guarded degree-\(k\) envelope.

## Source and execution scope

The supplied pasted-text.txt and CURRENT_STATE(2).json were read in full. A bounded filename search did not locate the linked ATTAINED_TAIL_PROFILE.tex or Tau_Correlated_Tail package; root separately confirmed its bounded Noether/Downloads search. The proof was reconstructed from the received text and accessible originals. The incoming status file records what the web session reported, not a local certificate.

The human generating-function source is DLMF 18.23.7 with the exact Meixner–Pollaczek dictionary. The existing local receipt mixed_tail_continuation_20260917/low_return/SOURCE_USE_REGISTER.md pins the primary-source read, human authors, release and Ismail trail; LRP3 gives the formula. ATA10 also derives it from the original recurrence. This audit does not claim a new reading of Ismail's book. ATA cites DLMF and Boyd–Vandenberghe at use; ATG cites original human Gamma, Legendre and Laguerre providers at use and derives every needed estimate.

Bounded rg and line-range reads inspected exact providers. Additive files were written only under this intake. This subtask performed no Lean, Lake, Elan, huge cumulative compile, remote publication, or frozen-source mutation. Structural checks and file hashes are not substitutes for the displayed mathematical proofs.

## Remaining gap

No implication remains missing for the audited envelope, integrated profile, graph determinant, sublinear-set control, or directed displacement correction. These do not determine the directional split, signed eight-flag leading coefficient, proper-source standard-window value, signed arithmetic/Gamma correction beyond its proved scope, or transferred sign of \(\Lambda_{AI}\). The complete action retains its exact cancellations.
