# Complete-action coefficient and sign audit

## Scope and result

Read-only audit of LRC3 and Section 7 in the attachment. The covariance estimates LRC11–28 and the analytic transport upgrade are assigned to other reviewers; this audit checks what follows from their displayed conclusions and from the existing complete-action providers. This is a dependency audit, not acceptance of the new covariance proof.

The action signs, the coefficient +8 of q log a, the source-order cancellation, the prefix/tail endpoint signs, and the factor 4 in LRC30 agree with the supplied sources. Two presentation repairs are needed: define the polynomial h in O_actual,h(q), since the attachment only defines h as a parity index, and replace or resolve the WCF27 citation, which is absent from all three nominated comparison files. The exact action identity is directly available as TAC14/CAI15.

File abbreviations:

- ATT: PRIVATE_INPUT_ROOT/LOCAL_RECORD_09b0993e0db94f74/pasted-text.txt
- STAGE: PROJECT_ROOT/work/mixed_tail_continuation_20260917/full_receiver_build/staging/14_CURRENT_KERNEL_AND_MULTIPLICITY_PROOFS.tex
- FTR: snapshots/full_receiver/FULL_TAIL_RETURN_PROPAGATION.tex
- LRP: snapshots/low_return/LOW_RETURN_PROPAGATION.tex

All line numbers below refer to the files as read on 2026-09-18.

## Exact action and finite directed bounds

FTR lines 1620–1628 (TAC13) define

\[
\delta^{\rm ar}_{a,s}=\mathcal B_a^{\rm ar}-\mathcal B_a^{(s)},\qquad
\delta^{\rm ar}_{a,1}=\delta_a^\sigma,\qquad
\delta^{\rm ar}_{a,a}=\mathcal H_a+\delta_a^\sigma.
\]

FTR lines 1635–1645 (TAC14), repeated at STAGE lines 69514–69523, give the exact identity

\[
J_a=\mathcal B_a^{(s)}+\delta^{\rm ar}_{a,s}+W_a-P_{a,-}-P_{a,+}.
\]

The W term has coefficient +1. Both nonnegative penalty terms have coefficient -1. This is also CAI15, STAGE lines 53525–53535. The exact native/conductor/low-factor split is FTR lines 1510–1516 (TAC10), and its action substitution is FTR lines 1650–1656 (TAC15).

The monic norm comparison at STAGE lines 53739–53751 (CAI29) yields

\[
-E_{\rm hi}\le W_a-\mathcal W_q^\sigma\le E_{\rm lo},
\]

where the two errors are O_h(a+log q), by lines 53760–53768 (CAI30). The four literal Gamma norms give, with their endpoint ratio retained,

\[
\mathcal W_q^\sigma
=2\log\frac{(4q)!}{(2q)!}-4q\log2+
\log\frac{2q-1}{2(4q-1)}
\]

at STAGE lines 53770–53780 (CAI31). Define

\[
C(q)=4q\log q+(8\log2-4)q,\qquad
\eta_q=\frac1{16q}+\frac1{4q-2}.
\]

CAI32, STAGE lines 53782–53803, proves the finite signed interval

\[
C(q)-\log2-\eta_q\le\mathcal W_q^\sigma\le C(q)-\log2.
\]

CAI28, STAGE lines 53719–53729, proves

\[
0\le P_{a,-}+P_{a,+}\le\Pi_{h,a}
=(4q-1)\log(1+z_{h,a}),\qquad
\Pi_{h,a}=O_h(q/a^2)=O_h(1)
\]

on the present simple-quartet domain. Here z is the exact expression in CAI26, STAGE lines 53709–53712, and the source proves r_a<=a/3. This finite result requires a>=9 on the tensor class a=4l+1, which is automatic eventually in the asserted asymptotic regime.

Consequently, without selecting independent values of correlated factors,

\[
\begin{split}
\mathcal B_a^{\rm ar}+C(q)-\log2-\eta_q-E_{\rm hi}-\Pi_{h,a}
&\le J_a,\\
J_a&\le\mathcal B_a^{\rm ar}+C(q)-\log2+E_{\rm lo}.
\end{split}
\]

This is CAI34, STAGE lines 53815–53821, and proves CAI35, lines 53823–53828:

\[
J_a-\mathcal B_a^{\rm ar}
=4q\log q+(8\log2-4)q+O_h(a+\log q).
\]

The stronger exponential penalty bounds are unnecessary for LRC3.

## The +8 coefficient and its precise remainder

The stated LRC23 at ATT lines 994–1008 gives, at s=1,

\[
\mathcal B_a^{(1)}=C_Bq^2+O_{\rm actual}(q).
\]

Since q=(a+1)^2 exactly,

\[
4q\log q=8q\log(a+1)
=8q\log a+8q\log(1+1/a).
\]

For a>=1 the last term is nonnegative and at most 8q/a=8a+16+8/a. Therefore it is O(a). Keeping every term before absorbing permitted errors gives

\[
\begin{split}
J_a-\delta^{\rm ar}_{a,1}
={}&C_Bq^2+8q\log a+(8\log2-4)q\\
&+8q\log(1+1/a)+O_{\rm actual}(q)+O_h(a+\log q).
\end{split}
\]

Thus LRC3 has precisely the permitted O_actual,h(q) remainder. The coefficient (8 log 2 -4) of the monic window cannot be promoted to a determined q coefficient of J_a-delta without refining the O_actual(q) covariance remainder. This limitation is already emphasized at STAGE lines 53830–53837.

## Exact source-order sign and coefficient

CAI5 at STAGE lines 53367–53381 fixes

\[
\mathcal H_a=\mathcal B_a^{(1)}-\mathcal B_a^{(a)}.
\]

With l_a=(a-1)/4, LRC23 yields

\[
\begin{split}
\mathcal B_a^{(a)}-\mathcal B_a^{(1)}
&=l_a q(2C_B-4a_1)+O_{\rm actual}(q)\\
&=(C_B/2-a_1)aq+O_{\rm actual}(q),\\
\mathcal H_a
&=-l_a q(2C_B-4a_1)+O_{\rm actual}(q).
\end{split}
\]

The cancellation is exact before asymptotics:

\[
\mathcal B_a^{(a)}+\delta^{\rm ar}_{a,a}
=\mathcal B_a^{(a)}+\mathcal H_a+\delta_a^\sigma
=\mathcal B_a^{(1)}+\delta_a^\sigma.
\]

The source's older Gamma transition constant agrees exactly. At (alpha,beta)=(2,pi), ATT defines

\[
C_B=9-8\log2+F,\qquad
a_1=2(1-\log2)-\lambda/4.
\]

ECL14, STAGE lines 19004–19007, proves F=-lambda/2-3+L. Substituting without changing the original energy convention gives

\[
\begin{split}
2C_B-4a_1
&=18-16\log2+2F-8+8\log2+\lambda\\
&=4-8\log2+2\mathcal L
=2\mathcal L-4(2\log2-1)
=\mathcal C_\Gamma.
\end{split}
\]

The last equality is AMT48, STAGE lines 3819–3830. Thus C_B/2-a_1=C_Gamma/4>0 and the corresponding H term is negative. Existing AKS46, STAGE lines 7143–7149, already gives H_a=-l_a q C_Gamma+O(q) on the simple-quartet domain. This is an independent check of the sign and precision claimed in Section 7.

LRP lines 300–321 (LRP18) has exactly

\[
\Delta\mathcal C+\Delta\mathcal T+\Delta\Xi+\mathcal H_a
=-\Delta F_L.
\]

Here C denotes the complete transported conductor return from TAC10. If one writes the literal lower covariance C^- instead, its transport discrepancy R e^C must remain as an extra exact term; it can only be absorbed after an applicable error bound is proved. The attachment uses the correct unsuperscripted C in its final LRP18 display.

At ATT line 1175 the phrase that the aq terms in lower covariance and native return cancel should be read precisely: the common -16 C_partial aq and +16 C_partial aq cancel for both sources, while at s=a the remaining +(C_B/2-a_1)aq is canceled by H_a inside delta_ar,a. ATT lines 1196–1209 correctly state that second cancellation. The original signed delta_a^sigma survives.

## Endpoint signs and allocation coefficient

FTR lines 195–204 (FTR11) define

\[
\operatorname{pre}_R e=2e_{q+R}-e_q-e_{q-1},\qquad
\operatorname{tail}_R e=e_{2q-1}+e_{2q}-2e_{q+R}.
\]

Inserting -L_N<=e_N<=U_N gives exactly the two directed intervals in LRC29, ATT lines 1134–1150. FTR's existing table at lines 274–296 (FTR16) matches every sign and multiplicity. Repeated endpoints can make these bounds non-sharp but do not invalidate them. Their O_actual(q) order follows if the separate transport audit establishes O_actual(q) endpoint bounds at the actual ranks and cutoffs.

FTR lines 183–193 (FTR10) prove

\[
4\tau_K=\tau_L+\tau_b+\tau_{\rm rem}+\tau_s+\tau_A,
\qquad \tau_K+\tau_R=\tau_{\rm total}.
\]

These are exactly the tail forms of LRC30; no factor 4 is missing. The identification of the single-copy total tail with script T is TAC12, FTR lines 1598–1612. No individual allocation is evaluated by these identities.

## Definition and citation repairs

1. Define h explicitly before using O_actual,h(q). It is the original arithmetic quartet polynomial

   \[
   h(z)=\prod_{\zeta\in\{1/2\pm\delta\pm i\gamma\}}(z-\zeta),
   \qquad v_h=2\xi/h,\qquad
   w_h(y)=|v_h(1/2+iy)|^2/(2\pi),
   \]

   with arithmetic degree-a source w_h^{*a}. These definitions are CAI1, STAGE lines 53303–53316, at the stipulated simple quartet. The h in ATT line 636, r=2h+epsilon, is a variable parity half-degree and must not be read as this fixed polynomial. The h dependence in CAI35 comes from original arithmetic density constants, not from that parity index. The error constant is not claimed uniform as the fixed quartet/arithmetic datum changes.

2. ATT line 1175 cites WCF27, which was not found in any of the three nominated source files. The action identity needed here is explicitly TAC14, FTR lines 1635–1645, and CAI15, STAGE lines 53525–53535. This is a citation incompleteness, not an arithmetic sign defect.

## Original benchmark remains attached

The benchmark is L_{h,a}=delta q(a+1)/2, and the corresponding complete-action term is 4q log L_{h,a}; FTR lines 1646–1647 and 1756–1757, or STAGE lines 69525–69526 and 69635–69636. Because q=(a+1)^2,

\[
4q\log L_{h,a}=12q\log(a+1)+4q\log(\delta/2).
\]

Consequently the displayed LRC3, when compared to that benchmark, gives

\[
J_a-4q\log L_{h,a}
=C_Bq^2+\delta_a^\sigma-4q\log a+O_{\rm actual,h}(q).
\]

Both C_B q^2 and the signed arithmetic correction are retained. This audit assigns no value to delta_a^sigma, any kernel allocation, or the projected arithmetic pairing.

## Completed work and limits

- Read the complete attachment and the targeted exact source sections above.
- Derived the +8 coefficient directly from the factorial window and q=(a+1)^2.
- Checked the exact source cancellation and its identity with the older C_Gamma constant.
- Checked the directed endpoint signs, allocation factor 4, and benchmark conversion.
- No source edits, external publication, symbolic diagnostics, numerical claims, or Lean runs were made.
- The remaining independent review items are the covariance proof and the applicability of the new all-rank transport bounds; they belong to the parent and other assigned reviewers.
