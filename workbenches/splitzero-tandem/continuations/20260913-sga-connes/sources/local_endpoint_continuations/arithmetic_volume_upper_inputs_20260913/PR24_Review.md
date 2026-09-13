# PR #24: bounded mathematical and endpoint-interface review

## Outcome and revision

Reviewed exact PR head `dfcbba5cbf7fec8c9301fe242c13e741d762013e`, tree `b37c4ddcd4e2e92c52283c61d076737950a75f2d`. At intake it is open, draft, and mergeable. Its two commits add five files, with no modifications or deletions against merge base `fa4be32f87a9a90f3c02a07f7790dea95a1e7b0f`. Current main at intake was `3b07cac9427f0132cc74a33598435144544abb54`, thirty commits ahead of that merge base. This review is for the next cut only, not an instruction to alter or delay the current publication.

The core transfer, determinant, derivative, and control calculations are correct under the retained reflection-stable source hypotheses. They yield an exact finite calculation of the same canonical relation norms and control, not a uniform arithmetic estimate. Two useful next-cut actions are to make the reflection hypothesis explicit and to add a genuinely nonzero-phase public regression. The Gamma/endpoint join is compatible, with an important distinction between the finite input cutoff for the invariant answers and the larger input needed by a naive computation of every transfer entry.

PR: https://github.com/KokunoYumeto/zeta-function-research-reader/pull/24

## Findings requiring precise qualification

### 1. State dagger stability before doubling the original-root jets

`RESEARCH_NOTE.md:11` begins with a general nonempty packet of actual zeros with full orders. Lines 41--44 then use reflection to claim that `psi=i^(-q)chi(c+iu)` is real and `Pi=psi^2`. The Gamma source explicitly requires the original dagger stability for reflection statements. PR24 should state that same hypothesis, or restrict this construction to the intended complete reflection-stable quartet packets.

This is a necessary mathematical scope condition, not an optional normalization. For an illustrative single root `lambda=c+delta+i gamma`, with real nonzero delta, one has

    psi(u)=u-gamma+i delta,
    Pi(u)=(u-gamma)^2+delta^2,
    zeta=gamma-i delta,
    Pi'(zeta)=-2i delta != 0.

Thus Pi is not psi squared, and raw jets doubled at only the original root do not have kernel (Pi). This symbolic example asserts nothing about the existence of an off-line zeta zero; it exposes the missing premise in the stated general-packet implication. A dagger-stable full quartet has precisely the required property, so this does not invalidate the intended quartet calculation. It is a blocker to presenting the doubled-root statement as a theorem for unrestricted packets, not a counterexample to its reflection-stable version.

### 2. The public phase tests currently test phase zero twice

In `check_transfer_core.py:29`, the atomic weights are `w_j=2+(j*j+3*j) mod 7`, with nodes `j-9`, for `0<=j<=18`. They satisfy `w_j=w_(18-j)` because `(18-j)^2+3(18-j)` is congruent to `j^2+3j` modulo 7. All odd moments therefore vanish. The other phase fixture is the even Gaussian. With the same even relation polynomial, both cases in `test_phase_and_control` at line 102 have phase zero.

The test still checks a valid equality, but does not catch accidentally dropping the phase square or the nonzero boundary contribution in the derivative solve. The expanded twenty-method suite is not present in the PR, so its asserted asymmetric coverage cannot be independently credited here. Add an explicitly asymmetric positive atomic measure to the public core for the next cut.

A separate review-only fixture multiplies those positive weights by `10+node`, which remains positive on nodes -9 through 9. It verifies the additional-solve formula, the norm-gap formula, and the complete two-loss identity with nonzero exact phase

    -74546106783325497234077749 / 44411209934630298438578438.

No original checker or branch was edited. This closes the bounded mathematical check in the review; it does not change the published regression coverage.

### 3. Nonnegative gaps and fixed width are not additional strictness or asymptotics

The actual equation (10) correctly says `Delta_j>=0`; the title/body sometimes call the gaps positive. Strict positivity should not be inferred for every general real-root configuration: in the Gaussian fixture with psi=u, `Delta_0=0`. The intended off-line quartet has additional root information, but the norm identity itself proves nonnegativity. Likewise the transfer width is fixed at 2q only while h and k are fixed; q itself grows with tensor degree in the quartet target.

## Exact calculation reconstructed from the supplied source

Keep the actual source density

    w_h(t)=|(g/h)(1/2+it)|^2/(2pi),  g=2xi,
    m_(h,k)=w_h^{*k},  integral m_(h,k)=mu_h^k,
    c=k/2,  S=c+iu,
    dmu_theta=e^(theta u)m_(h,k)(u)du.

The actual polynomial inclusion, quotient, full Taylor unit, and equations involving J, eta, and the original cohomological quotient remain attached. The tilt has the supplied exponential-integrability domain; no evenness is imposed at nonzero tilt. In the reflection-stable setting, `Psi(chi)=i^q psi`, `Pi=psi^2`, and the unit factor has modulus one without being deleted from the source map.

### Raw jets and transfer

For width m=2q and complete root orders `r_a=2 ell_a`, raw derivative coordinates have kernel (Pi), multiplication block `zeta_a v_d+d v_(d-1)`, and the full factorial Vandermonde determinant. The factor d, nilpotent orders, row order, and factorials are all necessary. The S-to-u jet conversion contributes the literal factor i^d; it is not a divided-derivative convention.

If a linear combination of `Q_n,...,Q_(n+m-1)` lies in (Pi), write it as Pi H with degree H<n. Orthogonality gives the integral of `Pi |H|^2` equal to zero. Positivity almost everywhere of the actual source weight forces H=0. For n=0 the degree argument suffices. This establishes F_n invertibility, not a bound on its condition number.

The solve `F_n d_n=v_(n+m)` makes its residual divisible by Pi. Dividing gives a monic degree-n polynomial Qhat_n orthogonal for the original relation weight. Pairing with that degree-n quotient leaves only the Q_n term, proving

    nu_n=-(d_n)_0 omega_n=omega_n vartheta_n>0.

The shift companion matrix has determinant `(-1)^(m-1)(d_n)_0=-(d_n)_0`, because m is even. Hence `F_(n+1)=F_n K_n`, and multiplication transport by `F_n^(-1)X_Pi F_n` gives the stated conjugacy. No diagonalizability of the arithmetic action is assumed.

### Determinants, quotient volumes, and phase

Products of source and relation norms give

    D_n=product_(j<n) omega_j,
    B_n=product_(j<n) nu_j,
    det F_n/det V=B_n/D_n.

With `a=N-q+1`, the original Schur quotient is therefore

    V_N=D_(N+1)/B_a
       =(product_(j=a)^(a+q-1) omega_j) det V/det F_a.

The source-coordinate change is triangular with determinant of modulus one on the remainder basis. It does not replace the original quotient Gram or mass. The determinant ratio retains the literal relation norm before quotienting, not the zero image of the relation.

Differentiated monic orthogonality gives `Q_j'=-a_j Q_(j-1)` and `(log omega_j)'=b_j`. Consequently the entire derivative of F_n is an internal strictly triangular shift plus its actual boundary column:

    F_n'=F_n L_n-a_n v_(n-1)e_0^T.

The trace of L_n vanishes, so

    (log V_N)'=sum_(j=n)^(n+q-1) b_j
                +a_n e_0^T F_n^(-1)v_(n-1).

At n=0 the boundary term is omitted; no negative-index inverse is evaluated. The original cross term remains `i(sigma-(log V_N)')`, including its i. This is the phase solve tested independently in the asymmetric fixture. The real recurrence coefficient b_j is distinct from the source remainder vector also called b_N.

### Both source losses and the trace certificate

The polynomial `Z_j=psi Qhat_j-Q_(j+q)` has lower degree, and source orthogonality gives exactly

    Delta_j=||Z_j||^2=nu_j-omega_(j+q)>=0.

The first term is an original relation after the retained i^(-q) conversion. Z_j itself has quotient class `-[Q_(j+q)]`; its source norm is not assigned to external absence.

For n=N-q+1>=1, substituting the actual adjacent volume ratios into the previously established radius identity yields

    epsilon_N^2
      =Delta_(n-1)Delta_n/(nu_(n-1)omega_N)-phi_N^2.

Writing P=V_(N-1), M=V_N, Q=V_(N+1), and a=omega_(N+1)/omega_N shows that this is exactly PR23's retained identity

    epsilon_N^2
      =a(P-Q)^2/(4PQ)
       -a(2M-P-Q)^2/(4PQ)-phi_N^2.

The imbalance square has not ceased to exist because the gap form packages it differently. Equation (12) is the coarse upper bound obtained after both nonnegative losses are dropped. The independent asymmetric fixture verifies all three expressions agree. The first degree N=q-1 retains its separate formula and no inadmissible predecessor.

The inherited original-Gram trace bound applies only once its original G, arithmetic inclusion/extraction, invariance, orthogonal projection, and rank-two certificate hypotheses are supplied. PR24 provides a representation of the required scalar energy inputs, not a new construction of every arithmetic hypothesis or an assumption that the arithmetic operator is normal.

## Exact endpoint and Gamma joins

The four specified Gamma source/join files and the corrected PR23 endpoint note were read completely and copied byte-for-byte into the review's own `join_inputs` directory. No active-edition source was changed.

### Four endpoint transfer determinants

Use a window of degrees N=n,...,n+r-1 with n>=q and r>=1. Define `W_a=product_(j=a)^(a+q-1) omega_j` and set a=n-q. The ratio in the endpoint logarithm is exactly

    V_(n-1)V_n / (V_(n+r-1)V_(n+r))
      = W_a W_(a+1) det F_(a+r) det F_(a+r+1)
        / (W_(a+r) W_(a+r+1) det F_a det F_(a+1)).

The common raw Vandermonde determinant cancels twice upstairs and downstairs, without changing a single raw jet or root multiplicity. The smallest a may be zero, where F_0 and the empty relation determinant are valid. The norm contribution remains `(omega_(n+r)/omega_n)^(1/(2r))`. Thus PR24 supplies literal coordinates for the already-proved written Jensen endpoint bound, not a recurrence supremum or a newly selected metric.

### Determinant correction identity with the same Gamma relation

Construct `F_a^Gamma` from the Gamma reference polynomials using the same Pi, same raw jets, same row order, and same Vandermonde V. The same source-division argument applies to that positive reference. With the Gamma source's actual corrections `X_a=D_a/D_a^Gamma` and `Y_a=B_a/B_a^Gamma`, division of the two transfer identities proves

    det F_a / det F_a^Gamma = Y_a / X_a.

Also the quotient of the two consecutive norm products is `X_(a+q)/X_a`. Therefore at a=N-q+1,

    V_N/V_N^Gamma
      =(X_(N+1)/X_a)/(Y_a/X_a)
      =X_(N+1)/Y_a=T_N.

This reconstructs GD.31 and EG.4 exactly in the fixed-width coordinates. EG.3 then supplies the unchanged explicit Gamma rising-factorial contribution to the two endpoint norms. No arithmetic mass is set to one: the original coefficient c_(h,0)=mu_h/c_lambda and its kth power remain, and cancellation happens only in the displayed ratios. The matrices denoted T in operator transport must remain distinct from the scalar correction T_N.

A review-only Gaussian mass-seven versus Gamma-reference calibration (alpha=1, reference mass one, same psi=u^2+1) gives `det F_2/det F_2^Gamma=11/48=Y_2/X_2` and `V_3/V_3^Gamma=196/11=X_4/Y_2`. These are exact fixtures, not substituted arithmetic data.

### Finite input cutoff: invariant answers versus naive entry construction

GJ.5--8 prove that the actual degree-N Gram and its j-th derivative depend only on coefficients through 2N+j. EG.5 consequently gives cutoff 2(n+r) for the complete endpoint expression. PR24 does not invalidate that result.

However, an entry-by-entry construction of `F_a`, with a=N-q+1, uses source polynomials through degree N+q. A generic monic Q_d requires moments through 2d-1, so the naive transfer entries reach degree `2N+2q-1`, above the invariant volume cutoff 2N. The solve for vartheta_a uses Q_(N+q+1) and may naively reach `2N+2q+1`, although its norm invariant depends only on degree `2N+2`. The determinant and selected solve coordinate have exact cancellations enforced by the proved source/relation identities.

For example, with q=1, psi=u, N=1, moments m_0=1, m_1=0, m_2>0, and arbitrary m_3, the raw transfer matrix is

    F_1=[[0,-m_2],[1,-m_3/m_2]].

Its individual entry depends on m_3, but `det F_1=m_2` and `V_1=m_2/det F_1=1` do not. The next-cut implementation should state whether it computes higher-degree source jets or exploits the invariant cancellation. It should not assert that every raw F entry is itself determined by EG.5's shorter cutoff, or infer a computational/conditioning saving merely from width 2q.

### Cochain and support interface

The Gamma representative correction remains a literal original relation `chi P_x`. Its image under the source map is the boundary; the separate GD.32a/b formula supplies its actual cochain-degree k-1 primitive with both signs. The transfer norm helper does not replace this primitive or the quotient.

Likewise `C[S]/chi_1^2` is only the norm-helper algebra. The explicit maps to `C[S]/chi_2` and then `C[S]/chi_1`, their kernels, derivative compatibility, and the full multiplier derivative term remain. The stated X^6 -> X^5 -> X^3 example is consistent with the genuine conormal depth. Quotient-killed vectors go to supported zero e at the receiving label, not external tau. The h=1 arithmetic quotient remains zero-dimensional while the analytic source and its mass remain nonzero.

## Verification: reported, fetched, and newly executed are separate

There are zero GitHub check runs and zero Actions runs at this PR24 head. No CI execution is inferred from the author-written `VALIDATION.json`, the PR23 collaboration comment, or unrelated main-branch CI. The validation record names its earlier source commit and the public checker blob; the checker at the actual reviewed head exactly matches the published blob `53abdeda395040302d1f75c6b09e2ce7cce0d398` and SHA-256 `fcaef2ee4c972cb71255ed3365930b3a558edc2b66dce5567301b38aff7ed4aa`.

The entire five-file PR, including the eight-method checker, was read. Fresh review-local runs execute that unchanged public core normally and under `python -O`; all eight methods pass in about one second per mode, the JSON records are identical, and both deliberate-failure controls exit 1. The review environment is Python 3.13.9 and SymPy 1.13.1, distinct from the author's recorded Python 3.13.5/SymPy 1.14.0. Results are bound in `FRESH_CORE_RECEIPT.json`.

Eighteen additional bounded exact Gaussian/atomic/symbolic checks verify the displayed calibration, four-volume transfer telescope, two-norm ratio, Gamma determinant interface, nonzero-phase solve and both losses, the missing-reflection-hypothesis example, and the invariant cutoff cancellation. These are recorded in `INTERFACE_CHECK_RECEIPT.json`. They are fixtures, not actual zero data, quadrature enclosures, uniform estimates, or Lean proofs. No twenty-method expanded suite or preceding thirty-five-entry archive was supplied in this five-file PR, so those author-reported checks were not independently replayed here.

## Remaining estimate and next-cut boundary

For the fixed exact quartet, retain `q_k=[1+k(m-1)](k+1)^2` and the full multiplicity-correct lower contribution. The existing exterior result gives `L_(h,k)<=epsilon_(h,k,N)` and `L_(h,k)/(kq_k)>=delta/2`. The new formulas calculate the same allowance; they do not show that it is `o(kq_k)` along any admitted degree sequence.

The Gamma upper density/tail bounds retain their tensor costs and certify neither compact arithmetic quadrature nor uniformly conditioned inverses. One-sided `T_N<=C_h^(kq)` does not control the denominator in the endpoint ratio. The residual formula (14) is valid only after actual bounds on F, a candidate inverse, input enclosures, and `||I-YF||<1` have been established. Positivity/invertibility and the fixed-width reformulation do not supply those bounds.

Recommended next-cut scope: explicitly retain dagger stability, extend the public phase regression to a genuinely asymmetric fixture, and use the exact determinant/Gamma join above while distinguishing invariant cutoffs from naive raw-entry costs. No broader implementation or new uniform estimate is claimed by this review.

`PROPOSED_CORRECTION.patch` supplies a concrete, locally tested two-file proposal. The note states the exact annihilator identity and k>=1, then exhibits the induced quotient isomorphism and raw derivative map including i^d. The checker uses explicit positive asymmetric atomic weights, asserts the tested phase is nonzero, and verifies both the gap and full two-loss forms. Its eight methods pass normally and under `python -O`, with identical records and both negative controls failing. `PROPOSED_CORRECTION_RECEIPT.json` binds the proposed bytes; the proposal has not been applied to the PR or current publication.

All authored files and fresh-check outputs are confined to `integration_20260913_next/review_pr24`. The named active-edition files were only read and copied without modification. No main/branch/PR write, Zenodo action, local Lean, heavy build, subagent, broad filesystem scan, or unbounded wait was performed. This review stops at the pinned source and these bounded findings.
