# Quantitative original Gamma receiving sign check

Date: 2026-09-14. Scope: independent proof check of the receiving substitutions of QGT20, QGT22, QGT26 and QGT28. No receiver or provider source was edited.

The ongoing programme log is `baseline_20260914/TASK_LOG.md`; the existing session provenance is `logbook/USER_INPUTS_VERBATIM.md` at the workspace root. This review is also the durable work record for this bounded subtask. The parent handoff was:

> Bounded independent sign check for canonical receiver I am writing. Read QGT20,22,26,28 in C:\Users\[[user]]\Documents\math\work\backpropagation_20260913\root\joint_schur_intake\growing_w_20260914\q_scale_20260914\QUANTITATIVE_ORIGINAL_GAMMA_RETURN.tex and existing original H/arithmetic identities in growing_w_20260914\baseline_20260914\receiving\spans\LOW_REFINEMENT_RECEIVING_BODY.tex and growing_w_20260914\receiving\SIGNED_RETURN_RECEIVER.tex (targeted exact identity full surrounding proof). Derive exact sign-reversed H=−W+e0−eq−eq+1 intervals, with e0∈[−a0,b0], eq+eq+1∈[−b_k+,b_k−]; arithmetic Bar=B0+H+delta_sigma, delta∈[−a_k−,a_k+]. Determine q-scale consequences of QGT for fixed m≥2 and m=1 retaining source errors/asymmetric arithmetic constants (do not claim arithmetic o(q) if allowances only O(q log k)). Write proof check under baseline_20260914/receiving/review/QUANTITATIVE_RECEIVING_SIGN_CHECK.md. Do not edit receiver/provider files. Send exact original domains for conclusions. Original k,q only; no independent K choice.

## Sources read and exact domains

The complete QGT1–28 body was read from `q_scale_20260914/QUANTITATIVE_ORIGINAL_GAMMA_RETURN.tex`. The complete LRI1–4 body was read from `baseline_20260914/receiving/spans/LOW_REFINEMENT_RECEIVING_BODY.tex`. The original JSR1, BHR1–2, BHR8–10, WRC1–7, BHR12–15, GRI3–7 and JSR16–21 identities and surrounding proofs were read from `receiving/SIGNED_RETURN_RECEIVER.tex`. All these paths are relative to `work/backpropagation_20260913/root/joint_schur_intake/growing_w_20260914` in the current workspace.

The universal QGT estimates have the literal domain

\[
l,m\in\mathbb Z_{\ge1},\qquad k=4l+1,\qquad
e=1+k(m-1),\qquad q=e(k+1)^2=e(4l+2)^2=2n,
\]

on the original density

\[
\sigma(y)=\frac{|\Gamma(1/4+iy/2)|^2}{2\pi},\qquad y\in\mathbb R.
\]

In particular, the high ranks are exactly \(n=q/2\) and \(n+1\) in the parity Hankel product, corresponding to the original full-line ranks \(q,q+1\). QGT uses \(\mu_a=\int_{\mathbb R}|y|^{2a}\sigma(y)\,dy=m_{2a}\), whereas WRC uses the literal power moment index. Thus QGT's \(\mu_{q+l}/\mu_q\) is exactly WRC's \(\mu_{2q+2l}/\mu_{2q}\), with the same mass \(\sqrt{2\pi}\). The exact high product is

\[
Z_a=H_n^{(a)}H_{n+1}^{(a)}(H_n^{(a+1)})^2,
\qquad \rho_q+\rho_{q+1}=\log(Z_{q+l}/Z_q).
\]

The finite receiving estimates involving \(e_0,e_q,e_{q+1}\) additionally use the original complete quartet

\[
0<\delta<\tfrac12,\qquad \gamma>2,
\qquad k\ge2048\sqrt{\delta^2+\gamma^2},\qquad \epsilon=2^{-10}.
\tag{D1}
\]

This is precisely BHR1 with JSR1 retained. The original centre remains \(c=k/2\), the roots remain \(c+(2a-k)\delta+i(2b-k)\gamma\), and the original polynomial, source and remainder maps remain those of JSR1–15. No independent order has been selected. QGT itself needs no \(\delta,\gamma\) threshold; this extra threshold is required when transporting its scalar value to the original \(\chi\)-source through the proved finite source-error intervals.

For the arithmetic conclusions, retain the original arithmetic source of JSR16–21,

\[
w_h(y)=|v_h(1/2+iy)|^2/(2\pi),\qquad m_k=w_h^{*k},
\]

with its proved TW/DMR constants and hypotheses. The original deficits are taken at exactly \(N\in\{q-1,q,2q-1,2q\}\). No new source-envelope assumption or arithmetic estimate is introduced here. All asymptotic statements below hold as \(l\to\infty\) with the original quartet parameters and \(h\) fixed, and with the stated integer \(m\) fixed. For such fixed \(\delta,\gamma\), (D1) holds eventually.

## Exact sign transport

The two original identities, with their signs unchanged, are

\[
\mathcal H_k=-W_k+e_0-e_q-e_{q+1},\qquad
\mathcal B_k^{\rm ar}=\mathcal B_k^0+\mathcal H_k+\delta_k^\sigma.
\tag{S1}
\]

Their already proved finite source intervals are

\[
-a_0\le e_0\le b_0,\qquad
-b_k^+\le e_q+e_{q+1}\le b_k^-,\qquad
-a_k^-\le\delta_k^\sigma\le a_k^+,
\quad 0\le a_k^\pm\le D_k^\pm.
\tag{S2}
\]

Here WRC1 retains

\[
a_0=E_0+2L_1^{\rm tail},\quad b_0=a_0+\Delta_f,
\quad E_0=|\alpha_k^\chi|(\epsilon^{-2}-64^{-2})+2\delta_\chi,
\]

and BHR10 retains

\[
b_k^+=2E_\chi+2L_\Sigma,\qquad
b_k^-=b_k^++(2q+1)\Delta_f,\qquad E_\chi=lE_0.
\]

Every \(L_r^{\rm tail},\alpha_k^\chi,\delta_\chi,\Delta_f\) here has its BHR2/WRC1 definition. In particular the positive multiplication correction enters the lower \(\mathcal H_k\) error through \(b_k^-\), and the upper error through the separate scalar \(b_0\).

Define only the following abbreviations for these complete errors:

\[
S_k^-=a_0+b_k^-,\qquad S_k^+=b_0+b_k^+.
\tag{S3}
\]

From (S2), negation gives \(-b_k^-\le-e_q-e_{q+1}\le b_k^+\). Adding the low interval therefore proves

\[
-S_k^-\le e_0-e_q-e_{q+1}\le S_k^+.
\tag{S4}
\]

For any proved finite bounds \(L\le W_k\le U\), the order-reversing map \(x\mapsto-x\) gives \(-U\le-W_k\le-L\). Adding (S4) and then the arithmetic interval proves, without an independence assumption,

\[
-U-S_k^-\le\mathcal H_k\le-L+S_k^+,
\tag{S5}
\]

\[
\mathcal B_k^0-U-S_k^--a_k^-
\le\mathcal B_k^{\rm ar}
\le\mathcal B_k^0-L+S_k^++a_k^+.
\tag{S6}
\]

The outer version replaces \(a_k^\pm\) by their same-sign majorants \(D_k^\pm\). These formulas are interval consequences of the exact equalities, not assertions that the individual endpoint errors can be simultaneously attained.

## Substitution of the finite QGT bounds

For QGT20 the endpoints are

\[
L=\mathcal V_{q,l}-\mathcal U_{q,l}-E_{q,l},\qquad
U=\mathcal V_{q,l}+\mathcal U_{q,l}+T_{q,l}+E_{q,l}.
\]

Consequently the exact receiving substitution is

\[
-\mathcal V_{q,l}-\mathcal U_{q,l}-T_{q,l}-E_{q,l}-S_k^-
\le\mathcal H_k
\le-\mathcal V_{q,l}+\mathcal U_{q,l}+E_{q,l}+S_k^+,
\tag{S7}
\]

\[
\begin{split}
\mathcal B_k^0-\mathcal V_{q,l}-\mathcal U_{q,l}
-T_{q,l}-E_{q,l}-S_k^--a_k^-
&\le\mathcal B_k^{\rm ar}\\
&\le\mathcal B_k^0-\mathcal V_{q,l}+\mathcal U_{q,l}
+E_{q,l}+S_k^++a_k^+.
\end{split}
\tag{S8}
\]

This sign placement also follows directly from the full source equality

\[
W_k=\mathcal V_{q,l}+\xi_{q,l}-r_{q,l}-\varepsilon_{q,l},
\quad |\xi_{q,l}|\le\mathcal U_{q,l},\quad
-T_{q,l}\le r_{q,l}\le0,\quad|\varepsilon_{q,l}|\le E_{q,l}.
\]

In \(-W_k\), the term \(+r_{q,l}\) lies in \([-T_{q,l},0]\); it contributes only to the lower allowance. This exactly agrees with LRI4 when the retained high-determinant expression is used in place of the QGT centre.

For QGT22, application of (S5) gives

\[
\begin{split}
-\mathcal V^{\rm c}_{q,l}-p^+_{q,l}-\mathcal U_{q,l}
-T_{q,l}-E_{q,l}-S_k^-
&\le\mathcal H_k\\
&\le-\mathcal V^{\rm c}_{q,l}+p^-_{q,l}+\mathcal U_{q,l}
+E_{q,l}+S_k^+.
\end{split}
\tag{S9}
\]

The arithmetic substitution is

\[
\begin{split}
\mathcal B_k^0-\mathcal V^{\rm c}_{q,l}-p^+_{q,l}-\mathcal U_{q,l}
-T_{q,l}-E_{q,l}-S_k^--a_k^-
&\le\mathcal B_k^{\rm ar}\\
&\le\mathcal B_k^0-\mathcal V^{\rm c}_{q,l}+p^-_{q,l}+\mathcal U_{q,l}
+E_{q,l}+S_k^++a_k^+.
\end{split}
\tag{S10}
\]

In particular, the lower receiving error is \(p^+\), and the upper receiving error is \(p^-\). Interchanging them would be a sign error. The source identity \(-p^-\le\widetilde P-p^{\rm c}\le p^+\) becomes \(-p^+\le-(\widetilde P-p^{\rm c})\le p^-\).

For QGT26 put

\[
R_{q,l}=\mathcal U_{q,l}+\mathcal D_{q,l}.
\tag{S11}
\]

The symbol \(R_{q,l}\) here is only the explicitly displayed nonnegative error radius; it is distinct from every original relation ratio and from the original HC residual \(\mathcal R_k\). To avoid that possible collision in a receiving source, one may leave \(\mathcal U_{q,l}+\mathcal D_{q,l}\) written in full.

QGT26 and (S5) give

\[
-lq\mathcal C_\Gamma-R_{q,l}-S_k^-
\le\mathcal H_k
\le-lq\mathcal C_\Gamma+R_{q,l}+S_k^+.
\tag{S12}
\]

Writing the original \(\Delta_k^\Gamma=\mathcal B_k^{\rm ar}-\mathcal B_k^0\), the corresponding arithmetic inequality is

\[
-R_{q,l}-S_k^--a_k^-
\le\Delta_k^\Gamma+lq\mathcal C_\Gamma
\le R_{q,l}+S_k^++a_k^+.
\tag{S13}
\]

More precisely, the exact identity and QGT26 prove

\[
-R_{q,l}-S_k^-
\le\Delta_k^\Gamma+lq\mathcal C_\Gamma-\delta_k^\sigma
=\mathcal H_k+lq\mathcal C_\Gamma
\le R_{q,l}+S_k^+.
\tag{S14}
\]

All these finite evaluated intervals contain the retained exact-\(W_k\) interval WRC5: the difference between their lower endpoint and the WRC5 lower endpoint is \(W_k-U\le0\), and the corresponding upper difference is \(W_k-L\ge0\). Thus adding these intervals to the current exact intersection does not justify claiming a narrower intersection. They provide finite evaluated centres and errors.

## Fixed multiplicity at least two: the exact q-scale consequences

For each fixed \(m\ge2\), the original formula gives

\[
q=[1+(4l+1)(m-1)](4l+2)^2\ge64(m-1)l^3.
\]

Therefore \(l/\sqrt q\le[8\sqrt{m-1}\sqrt l]^{-1}\to0\) and \(l^2/q\le[64(m-1)l]^{-1}\to0\). By QGT16 and QGT25–27,

\[
R_{q,l}/q=O(l/\sqrt q+l^2/q+l/q)\longrightarrow0.
\]

BHR8–10 and WRC1 give \(b_k^\pm=O(1)\), \(a_0,b_0=O(k^{-1})\), hence \(S_k^\pm/q\to0\). Divide the two sides of (S12) by \(q\) after adding \(lq\mathcal C_\Gamma\). The squeeze theorem proves

\[
\frac{\mathcal H_k+lq\mathcal C_\Gamma}{q}\longrightarrow0,
\qquad
\frac{\Delta_k^\Gamma+lq\mathcal C_\Gamma-\delta_k^\sigma}{q}
\longrightarrow0.
\tag{S15}
\]

The finite arithmetic statement at that scale is exactly

\[
-\frac{a_k^-}{q}-\frac{R_{q,l}+S_k^-}{q}
\le\frac{\Delta_k^\Gamma+lq\mathcal C_\Gamma}{q}
\le\frac{a_k^+}{q}+\frac{R_{q,l}+S_k^+}{q}.
\tag{S16}
\]

The quantities \(a_k^\pm/q\) have not been proved to tend to zero. Their established outer bounds are of order \(\log k\). Dividing (S13) instead by \(q\log k\), and retaining JSR21, proves

\[
-(64m+245)
\le\liminf\frac{\Delta_k^\Gamma+lq\mathcal C_\Gamma}{q\log k}
\le\limsup\frac{\Delta_k^\Gamma+lq\mathcal C_\Gamma}{q\log k}
\le128m+490.
\tag{S17}
\]

The width of (S13), with the outer arithmetic allowances, divided by \(q\log k\), tends to \(192m+735\): the additional width \(2R_{q,l}+S_k^-+S_k^+\) is \(o(q)\). With the actual allowances \(a_k^\pm\), the corresponding upper limit is at most \(192m+735\). The constants are asymmetric and unchanged. Neither (S15) nor QGT28 proves \(\Delta_k^\Gamma+lq\mathcal C_\Gamma=o(q)\).

## Simple multiplicity: the exact q-scale consequences

For \(m=1\), the original degree is exactly \(q=(4l+2)^2\), so

\[
\frac l{\sqrt q}\longrightarrow\frac14,
\qquad \frac{l^2}{q}\longrightarrow\frac1{16},
\qquad \frac lq\longrightarrow0.
\]

QGT16 gives the exact limiting high uncertainty

\[
\frac{\mathcal U_{q,l}}q
=A\frac l{\sqrt q}
\left(\frac3{\sqrt2}+\sqrt{\frac12+\frac1q}\right)
\longrightarrow\frac A{\sqrt2}.
\tag{S18}
\]

Every term of QGT25 can be retained while dividing by \(q\). Its two quadratic terms contribute

\[
\frac{2Ml^2+4l^2\log2}{q}
\longrightarrow\frac M8+\frac{\log2}{4}.
\]

All remaining terms tend to zero after division by \(q\): the terms linear in \(l\) are \(O(l/q)\); \(2(n+1)l\log(1+1/n)\le2l(1+1/n)\) is also linear in \(l\); \((8l^3+l)/(6q)\), \((l^4+l^2/4)/q^2\), the rational \(p^-\) and \(p^+\), and the remaining displayed rational low-moment terms are bounded by their literal powers after using \(l\le\sqrt q/4\). More explicitly, \(p^-=O(q^{-1/2})\), \(p^+=O(q^{-1/2})\), \(l^3/q=O(q^{1/2})\), \(l^4/q^2=O(1)\), \(l^2/q=O(1)\), \(l^3/q^2=O(q^{-1/2})\), and \(l^4/q^3=O(q^{-1})\). LRI2 gives \(0<K_{q,l}=O(l/q^3)\), \(T_{q,l}=O(l^5/q^4)=O(q^{-3/2})\), and \(E_{q,l}=O(l/q^5)\). Thus

\[
\frac{R_{q,l}}q\longrightarrow
B_\Gamma:=\frac A{\sqrt2}+\frac M8+\frac{\log2}{4}.
\tag{S19}
\]

Here \(A=M/2+2C_{\rm partition}\) is exactly QGT12; the partition constant is QGT9's literal constant. No unidentified asymptotic coefficient was inserted into the original Gamma functional.

At \(m=1\), BHR8–10 and WRC1 give \(b_k^\pm=O(k)\), \(a_0,b_0=O(1)\), hence \(S_k^\pm/q\to0\). Equations (S12), (S14) and (S19) prove the finite-radius conclusion

\[
-B_\Gamma\le\liminf\frac{\mathcal H_k+lq\mathcal C_\Gamma}{q}
\le\limsup\frac{\mathcal H_k+lq\mathcal C_\Gamma}{q}
\le B_\Gamma.
\tag{S20}
\]

Exactly the same bounds hold for
\((\Delta_k^\Gamma+lq\mathcal C_\Gamma-\delta_k^\sigma)/q\), by its equality with the quotient in (S20). In particular these quantities are bounded; the present estimates do not identify their limits or prove that they tend to zero.

The arithmetic defect retains the original simple-multiplicity estimate

\[
\frac{\delta_k^\sigma}{kq}
=O_h\!\left((\log k/k)^{5/7}\right).
\]

Thus (S14) proves

\[
\frac{\Delta_k^\Gamma+lq\mathcal C_\Gamma}{kq}
=O_h\!\left((\log k/k)^{5/7}\right)+O(1/k).
\tag{S21}
\]

The equivalent bound at the \(q\) scale is only

\[
\frac{\Delta_k^\Gamma+lq\mathcal C_\Gamma}{q}
=O_h\!\left(k^{2/7}(\log k)^{5/7}\right)+O(1).
\tag{S22}
\]

Consequently a bounded full arithmetic residual at the \(q\) scale does not follow. The \(q\log k\) constants for \(m\ge2\) must not be transferred to this branch. The finite signed interval (S13) continues to apply with the original simple-multiplicity \(a_k^-\) and \(a_k^+\).

## Receiving verdict

The exact identities and all finite sign transports above are consistent with WRC3–7 and LRI1–4. The canonical receiver may insert (S7)–(S14) and their stated domains directly, retaining every original source error and asymmetric arithmetic allowance. For fixed \(m\ge2\), the new assertion is (S15); for \(m=1\), the proved assertion is the finite-radius bound (S20), together with the unchanged arithmetic rate (S21). No original source order, packet coordinate, low moment, high rank or arithmetic domain is replaced.

## Final QRI1–8 comparison and accepted pin

The parent subsequently requested a full comparison against the newly written `baseline_20260914/receiving/spans/QUANTITATIVE_RECEIVING_BODY.tex`, limited to QRI1–8. That full body was read, and its SHA-256 at acceptance is:

`9B82A76C55102278C72754C0B5AD3B660B6514D9D9A8C1BDE41A32AF521522E1`

**Status: accepted; no mathematical correction required.**

QRI1 is QGT20 with its exact source-sum centre. QRI2 is QGT22; its claimed containment follows because the difference of its lower endpoint from QRI1's lower endpoint is \(p^{\rm c}_{q,l}-p^-_{q,l}-\widetilde P_{q,l}\le0\), whereas its upper endpoint minus QRI1's upper endpoint is \(p^{\rm c}_{q,l}+p^+_{q,l}-\widetilde P_{q,l}\ge0\). QRI3 applies the map (S5), so its use of \(-\omega^+\) and \(-\omega^-\) correctly reverses both the \(p^\pm\) asymmetry and the one-sided \(T_{q,l}\) correction. QRI4 is exactly (S6), including both original arithmetic enclosures. QRI5 subtracts the unchanged HC threshold and intersects the lower bound with the independently proved nonnegative constraint; it is valid on the original HC domain intersected with (D1) and the original arithmetic source domain.

QRI6 is (S12) with its entire radius named \(\mathcal E_{q,l}^{\rm high}\). QRI7 agrees with (S15) and the bounded part of (S20). Its equivalent \(\mathfrak T_k\) assertion has the correct sign because \(\mathfrak T_k=-\mathcal H_k\). Every identity in QRI8 is exact, and its prose correctly retains the arithmetic defect at the left rather than claiming an unproved arithmetic \(o(q)\) conclusion. The finite source-error uses inherit exactly BHR1, namely (D1); the asymptotic uses keep the original fixed quartet and \(h\), with each stated multiplicity fixed. No independent order occurs in the body.

The explicit optional simple-multiplicity radius (S19) was also checked independently by a separate bounded algebra reviewer against QGT16, QGT21, QGT25 and the original LER13/LER17/LER20 expressions. That check confirmed every term and required no correction. QRI7 does not assert this extra radius, and its stated \(O(q)\) conclusion is already sufficient and correct.

This final comparison made no changes to QRI or to any receiver/provider source. The accepted-byte receipt is `QUANTITATIVE_RECEIVING_QRI_RECEIPT.json` beside this review.
