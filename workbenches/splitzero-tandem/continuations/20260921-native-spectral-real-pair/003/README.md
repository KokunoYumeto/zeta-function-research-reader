# SZ-20260921-003 — Native singular directions and the original conductor

21 September 2026. The 79-page reader contains 13 complete proof parts. Compile COMPLETE_NATIVE_SPECTRAL_READER.tex with LuaLaTeX. All new source notes and both illustrations accompany it.

The original observation has kernel \(K\), of dimension \(m=8k-16\), inside \(E=\mathbb C[S]/(\chi)\), of dimension \(q=(k+1)^2\). The degrees \(q-1,q,2q-1,2q\), their signs \(+,+,-,-\), physical coordinate, full invariant columns \(Z=[M_A,S_kZ_k]\), and attained metrics are retained.

## Results proved in this edition

- **OR1–25: complete conductor root geometry.** Every root of \(d_A=\mathcal U_A1\) satisfies \(|y|<q/r_*\); at most \(O_A(q^{1/8})\) lie outside \(q^{7/8}/8\); their total modulus is \(O_A(q\log q)\). The reciprocal rescaling converges to \(E_A(-iz)/z^v\) with explicit error and multiplicity-preserving root correspondence. Proof: COMPLETE_CONDUCTOR_ROOT_GEOMETRY.tex, OR7–21.
- **KF1–55: transport of the actual invariant kernel.** Its fixed low-degree intersection has a proved angle bound. Removing it and applying the complete conductor changes the four-cutoff determinant by an explicit \(o(kq)\) error. The actual subspace and transformed graph metric remain. Proof: ACTUAL_KERNEL_FILTRATION_AND_GRAPH.tex, KF25–32 and KF37–55.
- **CG1–32: the full graph-volume correction is below the required scale.** Uniformly over all relation polynomials of degree at most \(q\),
  \[
  \left|\log\frac{\|\chi'd_Ah\|_{\sigma,c'}^2}{\|\chi h\|_{\sigma,c}^2}\right|=O_A(\log q).
  \]
  The full conductor quotient consequently satisfies
  \[
  |\log\det Q_N^U-\log\det Q_N^d|=O_A(q\log q)=o(kq).
  \]
  Its low-cutoff changes vanish exactly. The original kernel's remaining graph effect is
  \[
  \mathcal G_K=-\Delta_{R,2q-1}-\Delta_{R,2q}+o(kq),\qquad
  \Delta_{R,N}=\log\frac{\det[A_R(Q_N^U)^{-1}A_R^*]}
                              {\det[A_R(Q_N^d)^{-1}A_R^*]}.
  \]
  The exact \(A_R\) uses every original invariant column and has kernel \(\overline K\). Proof: COMPLETE_CONDUCTOR_GRAPH_METRIC.tex, CG22–32.
- **S1–45: the unique small singular direction at all four cutoffs.** The supplied proof gives
  \[
  \log s_{q,N}=-q\log(q/k)+q[I(\delta,\gamma)/2-\psi(s)-J(s)]+o_h(q).
  \]
  Adjacent odd/even cutoffs have the same coefficient. The exact inverse isolates one potentially unbounded rank-one term, while every other singular value has an explicit lower bound \(\exp[-O_h(k+\log q)]\). This asymptotic retains the NG full-reference zero law and written monic-profile input H4–5 at their original scope. Proof: NATIVE_SMALLEST_SINGULAR_PROOF.tex, S11–45; profile derivation: RETAINED_PROFILE_PROOF.tex.
- **LS1–17: the explicit surviving line reaches the original observation.** Its class is \(u=[(Q_k-Q_k(0))/y]\). LS4–5 prove the finite projector and full heat-tail errors. Its actual observed fraction is
  \[
  1-\theta_{K,N}=(\Lambda u)^*Q_N(\Lambda u)/(u^*G_Nu).
  \]
  The exact conductor response is
  \[
  (\mathcal T_A\widehat u)(\eta)=-iQ_k(0)\sum_j a_j/(\eta-c+b_j).
  \]
  The rational numerator has degree \(J-v-1\); LS17 proves an explicit positive detection bound. LS10–12 retain the full Schur resolvent and memory equation connecting this to the observed action's own heat. Proof: LATE_HEAT_ORIGINAL_KERNEL_RECEIVER.tex.
- **NE1–16: every original eigenclass has a nonzero adjoint residual.** The Hermitian action-boundary norm satisfies \(\kappa_N\ge e\delta(k+1)^3/2\). NE10 gives a positive residual bound and NE13–14 gives the complete fixed-kernel mixed-phase identity in the two actual boundary rows. Proof: NATIVE_EIGENCLASS_BOUNDARY.tex; the finite source argument is included in EIGENCLASS_PHASE_SOURCE.tex.

The general-family and four spectral-resolution notes supply complete additional proofs of fixed-flag determinant calculus, rank changes with their exact minimum correction, spectral pencils, finite unit certificates and the ES trace receiver.

## Verification and citations

The spectral-resolution replay passed 3434 exact checks and 19 negative controls, with ordinary/optimized agreement. The boundary proof passed 832 exact checks and 3 negative controls. The singular/root identities passed 109 checks; an independent directed interval computation reproduced all five rational enclosures. The late-heat receiver passed 32 checks including 4 negative controls; conductor detection passed 60; the graph identities passed 81. Finite auxiliary examples do not estimate an unknown zeta period. The asymptotic estimates have written proofs and retain their stated imported inputs.

Human sources are credited in the proofs: J. L. W. V. Jensen; R. A. Askey and R. Roy; T. H. Koornwinder, R. Wong, R. Koekoek and R. F. Swarttouw, with W. P. Reinhardt; and B. C. Carlson. The related Hanyga reference is identified as related literature; no unproved import from it enters these finite arguments.

The previous kernel proof is [MR1–23, pinned complete source](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/5992ad50c0f2a06921f1fcaded7b4e38097c0739/workbenches/splitzero-tandem/continuations/20260920-original-kernel-mixed-determinants/ORIGINAL_KERNEL_MIXED_DETERMINANT.tex#L36). The original equilibrium is [EIQ1–33, complete public proof](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/5992ad50c0f2a06921f1fcaded7b4e38097c0739/workbenches/splitzero-tandem/continuations/20260920-original-kernel-mixed-determinants/providers/09_INPUT_CUMULATIVE_PROOFS.tex#L4381). Further precise public proof links appear at their uses in the reader. Every new in-scope proof accompanies this edition.

**Still being calculated:** the two actual invariant-covariance returns in CG32, the original kernel allocation at order \(kq\), the late-heat fractions, and fixed-kernel complex signs. No RH conclusion is asserted. Complete actions and attained metrics remain in the next calculation.
