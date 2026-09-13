# Canonical restriction transport and an adaptive trace certificate

## Source and scope

This continuation uses the owner-delivered **Tau Endpoint Restriction Control** report and the actual main/PR25 constructions. At intake main was `952ef9fee1e1419b6858d920354de8fa99430b7d`; PR25 was open at its checked head `66fac5e7885a40cd4873e74b754907320f05b067`. The review branch starts at that exact head. No historical source, dependency pin, arithmetic scalar implementation, frozen publication, main branch or parallel session's branch is changed.

The mathematical restriction report was read in full. The current runtime could not open the uploaded ZIP, so its manifest verification and reported 19-method suite are not represented as independently executed here. The new checker reconstructs the declared polynomial fixtures independently. The separate progress transcript reports further Gamma/error-control work and an upper-volume bound using moments through degree 2q. Those full proofs were not supplied in that transcript and are not certified by this contribution.

The return-map and sharp-gap certificate below are from the supplied report. The adaptive trace-only certificate, its terminating finite search, and its connection to the corrected per-block factor-four consequence are deductions in this continuation. The general logarithm-series and finite-dimensional spectral mechanisms are classical. No priority claim about those general mechanisms is made.

## 1. Keep the source and the two different transports

Fix the original nonempty cyclic arithmetic algebra

\[
 E=\mathbb C[S]/(\chi_{h,k}),\quad q=\deg\chi_{h,k},\quad A=M_S.
\]

Keep the original source map \(\mathcal V\), with \(g=2\xi\), measure \(m_{h,k}=w_h^{*k}\), and full-jet injection \(\eta\). Its observation is \(J^{(k)}\mathcal V=\eta\pi_\chi\). The multiplier \(\upsilon_h^{\otimes k}\) in \(\eta\) is not removed. The initial arithmetic quotient and all supported labels remain upstream.

For the unscaled monic orthogonal polynomials, set

\[
 B_N=[b_0,\ldots,b_N],\quad b_j=[p_j]_\chi,\quad
 O_N=\operatorname{diag}(\omega_0,\ldots,\omega_N),\quad \omega_0=\mu_h^k.
\]

For every admitted degree \(N\ge q-1\),

\[
 K_N=B_NO_N^{-1}B_N^*,\qquad G_N=K_N^{-1},\qquad
 R_N=O_N^{-1}B_N^*G_N. \tag{1}
\]

Thus \(B_NR_N=1\), \(R_N^*O_N=G_NB_N\), and \(R_N^*O_NR_N=G_N\). The middle identity shows orthogonality to the actual kernel of the original observation, rather than to a chosen unrelated subspace. For a positive source matrix it proves the least-norm characterization by expanding the norm of \(R_Nu+z\), \(B_Nz=0\).

For \(i\le j\), the forward quotient map is the identity on coordinates, but has type \((E,G_i)\to(E,G_j)\). Its metric adjoint is

\[
 T_{i,j}=K_iG_j:(E,G_j)\longrightarrow(E,G_i). \tag{2}
\]

Indeed \(G_iT_{i,j}=G_j\). If \(L_{i,j}\) is coefficient padding and \(P_{i,j}\) is the orthogonal cutoff in the larger monic source, direct substitution into (1) gives

\[
 L_{i,j}R_iT_{i,j}=P_{i,j}R_j. \tag{3}
\]

The raw cutoff identity behind this proof is
\(P_{i,j}O_j^{-1}B_j^*=L_{i,j}O_i^{-1}B_i^*\): it follows from diagonal orthogonality and literally retaining the first coordinates. The formal `source_restriction` theorem takes that raw identity, not (3), as input.

The reverse maps satisfy

\[
 T_{i,j}T_{j,l}=T_{i,l},\qquad
 T_{i,j}^{-1}=K_jG_i,\qquad
 \det G_i\det T_{i,j}=\det G_j. \tag{4}
\]

These are matrix identities without a commutation hypothesis on the different Grams. Writing \(H_{i,j}=1-T_{i,j}\) gives the noncommutative deficit law

\[
 H_{i,l}=H_{i,j}+T_{i,j}H_{j,l}. \tag{5}
\]

It does not imply additive or pointwise multiplicative identities for individually sorted eigenvalues.

The arithmetic action is also retained. Put
\(\mathsf H_N=K_NA^*G_N+A-kI\). Cancellation of the two equal middle terms \(K_iA^*G_j\) proves

\[
 AT_{i,j}-T_{i,j}A=\mathsf H_iT_{i,j}-T_{i,j}\mathsf H_j. \tag{6}
\]

Consequently the return eigenspaces need not be arithmetic invariant subspaces. None is substituted for the full generalized eigenspaces in the exterior trace argument.

## 2. The missing polynomial part is a retained original relation

Let \(X=L_{i,j}R_i\), \(R=R_j\), \(P=P_{i,j}\), \(T=T_{i,j}\). Then

\[
 d=X-R=X(1-T)-(1-P)R. \tag{7}
\]

Applying the original quotient map to the two right-hand terms yields \(1-T\) in both cases. Therefore \(B_jd=0\). Monic division puts the difference in \(\chi\mathcal P_{j-q}\), with the existing theta primitive; after the original internal quotient it is the receiving fibre's supported zero, not external absence.

From the dual identity in (1),
\(R^*O_jX=G_jB_jX=G_j\) and \(R^*O_jR=G_j\). Adjoint symmetry gives the reverse cross Gram. Expansion now proves

\[
 d^*O_jd=G_i-G_j. \tag{8}
\]

Thus both the original relation and its full source norm are retained. Applying the source's quotient-killing map to (8) is not a way to compute that norm; the norm precedes the quotient.

## 3. Weighted spectral comparison, not a replacement metric

Since \(K_j\succeq K_i>0\), the return map is positive and self-adjoint for the original \(G_j\)-pairing. Its eigenvalues satisfy \(0<g_a\le1\). A weighted spectral basis gives explicit inverse coordinate maps \(U,V\), \(UV=VU=I\), with

\[
 H=1-T=U\operatorname{diag}(x_a)V,\qquad x_a=1-g_a\in[0,1). \tag{9}
\]

The `RestrictionSpectrum` interface retains these inverse maps; it does not presume Euclidean normality. It verifies, from that witness,

\[
 \operatorname{Tr}(H^m)=\sum_a x_a^m,
 \quad\det(1-H)=\prod_a(1-x_a)>0,
 \quad-\log\det(1-H)=\sum_a-\log(1-x_a). \tag{10}
\]

Together with (4), the last value is exactly \(\log(V_i/V_j)\). The formal code uses the real part of the complex determinant only after proving it equals this positive real product. It does not use a complex logarithm branch.

The source's positive/self-adjoint spectral theorem supplies the existence of (9) in this arithmetic instance. The new code verifies its inverse-coordinate trace and determinant transport, but does not claim a fresh formalization of the full analytic moment construction or an automatic weighted spectral decomposition routine.

## 4. The supplied sharp certificate is obtained from the logarithm series

For \(x\in[0,1)\), define

\[
 P_p(x)=\sum_{m=1}^p\frac{x^m}{m},\qquad
 R_p(x)=-\log(1-x)-P_p(x)=\sum_{m=p+1}^\infty\frac{x^m}{m}. \tag{11}
\]

The formal proof invokes Mathlib's proved logarithm series and explicitly shifts its summation index. It does not assume this tail formula as a new axiom.

For \(0\le x\le r<1\), \(r>0\), comparison of the nonnegative terms after dividing out \(x^{p+1}\), or cross-multiplying when \(x=0\), gives

\[
 R_p(x)\le\frac{R_p(r)}{r^{p+1}}x^{p+1}. \tag{12}
\]

For \(s_m=\operatorname{Tr}(H^m)\), \(P_p=\sum_{m=1}^p s_m/m\), and \(\mathcal L=\log(V_i/V_j)\), sum (12) over the actual finite spectrum:

\[
 P_p\le\mathcal L\le P_p+\frac{R_p(r)}{r^{p+1}}s_{p+1}. \tag{13}
\]

This is the report's certificate with \(r=1-g_0\), supplied by the original matrix inequality \(K_i\succeq g_0K_j\). At \(g_0=1\), positivity forces \(H=0\), and all losses are zero. The coefficient in (13) is not silently used at \(r=0\).

## 5. New adaptive certificate: the trace moments certify the stopping condition

There is a second finite enclosure that does not require a separately estimated \(g_0\). If \(p\ge1\) and \(s_p<1\), then

\[
 \boxed{P_p\le\mathcal L\le
 U_p:=P_p+\frac{P_{2p}-P_p}{1-s_p}.} \tag{14}
\]

**Proof.** For every \(x\in[0,1)\), reindex the nonnegative tail:

\[
 R_{2p}(x)=\sum_{n\ge0}\frac{x^{n+2p+1}}{n+2p+1}
 \le x^p\sum_{n\ge0}\frac{x^{n+p+1}}{n+p+1}
 =x^p R_p(x).
\]

Each \(x_a^p\le\sum_bx_b^p=s_p\). Summing and retaining the nonnegative tails gives

\[
 \mathcal L-P_{2p}\le s_p(\mathcal L-P_p).
\]

Division by \(1-s_p>0\) proves the upper bound; the lower bound is the partial-sum inequality in (11). This proves (14) without setting any spectral mode, phase or arithmetic coefficient to zero.

For every fixed finite restriction, \(s_p\to0\); hence the stopping test \(s_p<1\) eventually succeeds. Also \(P_p\to\mathcal L\), so
\((P_{2p}-P_p)/(1-s_p)\to0\). Thus the two sides of (14) converge to the same original volume loss. The code checks the stopping-existence theorem; the final convergence assertion follows by the displayed limits and is stated here as a written consequence.

Evaluation of (14) uses only matrix multiplication, trace, finite sums and one real division. No matrix logarithm or computed eigenvectors enter the certificate. When the entries of the supplied finite matrix are rational (or exact complex rationals), the output is rational. Actual arithmetic matrices require certified input enclosures; a high-precision floating evaluation is not an exact input.

The criterion has not erased conditioning. If \(g_{\min}\) is small, obtaining \(s_p<1\), or obtaining a comfortably positive denominator, can require many powers and high precision. Fixed-pair termination is not uniform control as \(k\to\infty\).

### Robust use with uncertain trace moments

Suppose certified upper bounds \(\bar s_m\ge s_m\ge0\) are available through order \(2p\), and \(\bar s_p<1\). Then

\[
 \mathcal L\le\sum_{m=1}^p\frac{\bar s_m}{m}
 +\frac{\sum_{m=p+1}^{2p}\bar s_m/m}{1-\bar s_p}. \tag{15}
\]

Indeed the first prefix, the positive tail block, and reciprocal denominator in (14) are separately bounded in the required direction. In implementing (15), sum the tail block directly: subtracting two independently bounded prefixes is not generally a valid bound. This interval extension is proved here, not counted as an additional Lean theorem.

## 6. Reconcile the source's older threshold with the current work

The delivered restriction report uses the earlier threshold-two implication. That argument is valid but weaker than the current shared continuation. For a packet **consisting exactly** of a hypothetical off-line quartet, all multiplicities remain in

\[
 q_k=[1+k(m-1)](k+1)^2,\qquad L_{h,k}\ge\delta kq_k/2.
\]

PR25's reviewed analytic norm estimate and checked finite propagation give, with one fixed \(D_h>0\), each of the original blocks

\[
 (i,j)=(q_k-1,2q_k-1),\quad(q_k,2q_k)
\]

a lower bound

\[
 \log(V_i/V_j)\ge2q_k\log(D_hk). \tag{16}
\]

Therefore **in each block**

\[
 \prod_{a=1}^{q_k}g_a\le(D_hk)^{-2q_k},\qquad
 \min_a g_a\le(D_hk)^{-2}. \tag{17}
\]

For the corresponding actual nonzero eigenvector \(v\), (3) and the retained Gram imply

\[
 \frac{\|P_{i,j}R_jv\|^2}{\|R_jv\|^2}=g_a,
 \qquad
 \frac{\|(1-P_{i,j})R_jv\|^2}{\|R_jv\|^2}=1-g_a. \tag{18}
\]

This strengthens the report's single-mode order-\(k^{-1}\) consequence to an order-\(k^{-2}\) squared restriction factor in **each** block. It is not a bound on every direction; the direction need not be \(A\)-invariant. The low-degree part carries coordinate \(g_av\), not \(v\); inversion uses the literal return inverse in (4).

The total lower cost is the shared factor-four condition. In (14), apply independent stopping degrees to the two original loss matrices. Their computed bounds add to an upper certificate for exactly that total. A contradiction would require an arithmetic bound strictly below the forced lower cost. No such upper arithmetic growth estimate is proved here.

There is an explicit complexity warning under the same hypothesis. If a stopping margin \(s_p\le\theta<1\) is required and \(D_hk>1\), (17) forces

\[
 p\ge\frac{\log\theta}{\log(1-(D_hk)^{-2})}.
\]

Thus even a single forced weakly restricted mode can demand order \(k^2\) powers for a fixed margin. This is a consequence to retain in numerical planning, not a reason to replace the source metric.

## 7. Finite verification and remaining formal scope

The independent checker uses the literal mass-seven Gaussian source and the quotients \((S-1)^2\), \((S-1)^2+1\), \((S-1)^3\), plus a noncommuting complex weighted-column fixture. It verifies the original representative formulas, restriction identity, relation Gram, action defect, two-metric composition, coordinate covariance, Cauchy--Binet degree marker, source spectra and exact rational upper enclosures. These fixtures are not claimed zeta packets.

The mass-seven repeated-root example has return spectra \(\{2/3,2/5\}\) and \(\{4/5,2/5\}\). Both the source's sharp certificate and the adaptive certificate are checked against rational logarithm enclosures, not floating-point comparisons. The nilpotent arithmetic generator is retained.

The new Lean files isolate: matrix transport; original weighted source and relations; sharp/adaptive log-series inequalities and finite stopping; and inverse-coordinate spectral-to-matrix comparison. The input analytic moment formulas, weighted spectral existence in the actual source, monic division and theta primitives remain at the previously stated source scope. The same scalar, quotient, support and homology implementations are inherited, not redefined.

All successful executions must be identified by exact head SHA and completed CI job. Early elaboration/linter failures remain in branch history. They are not certificates. `STATUS.md` and the PR record identify the final successful scope when available.

## References and source locators

The supplied *Tau Endpoint Restriction Control* report, sections 2--7, is the source for (1)--(4), (6)--(13) and the mass-seven calibration. Its archive was not independently opened by this runtime.

The current shared arithmetic continuation is `workbenches/tau-arithmetic-endpoint-bounds/FOUR_VOLUME_THRESHOLD.md` at main `952ef9fee1e1419b6858d920354de8fa99430b7d`. PR25 at `66fac5e7885a40cd4873e74b754907320f05b067` supplies the per-block extension and checked finite propagation.

The Mathlib Community. (n.d.). *Analysis.SpecialFunctions.Log.Deriv: hasSum_pow_div_log_of_abs_lt_one*. Mathlib revision `fabf563a7c95a166b8d7b6efca11c8b4dc9d911f`. The actual pinned source was read; the extension here uses its positive logarithm series.
