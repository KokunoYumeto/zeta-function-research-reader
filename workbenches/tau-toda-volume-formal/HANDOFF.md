# Toda formalization and bounded analytic collaboration

## Coordination

Based on PR #22 at 811210d24b80813a08972ca23f919db015383137, including corrected main fa4be32f87a9a90f3c02a07f7790dea95a1e7b0f. All files are additive. Do not recreate the original scalar, relation quotients, conormal derivative, or rank-two trace certificate. The PR body records the exact completed strict run; this handoff alone is not execution evidence.

## Formal interfaces

1. `QuotientVolume.residual`: C-B H B*C. Proved orthogonality, Gram identity, determinant factor/ratio, and unchanged observation J when JB=0. Polynomial-column construction and arithmetic moments remain the source's input.
2. `TodaVolume.two_losses`: exact rational identity with volumes P,M,Q and phase z. Both squares remain. The upper equality case is exactly 2M=P+Q and z=0 for a>0. The endpoint uses its separate identity.
3. `TodaTrace.original_gram_volume`: obtains the invariant trace allowance from the inherited original-Gram factorization and composes it with the exact energy relation. No orthogonal spectral complement or normal arithmetic action is assumed.
4. `VolumeWindow.exists_log_step` and `exists_control_step`: an endpoint log-volume budget selects a step inside the original finite degree window; it does not assert that the required arithmetic budget is available.

## New analytic target passed back

For N_j=N_0+2j, j<r, N_0>=q, if sqrt(a_(N_j+1))<=A and B=log(V_(N_0-1)/V_(N_0+2r-1)), then some canonical step has epsilon<=A sinh(B/(2r)). The proof uses the checked telescope/selection and the supplied local bound. A small endpoint budget can therefore select the degree rather than uniformly estimating every step. For the fixed quartet q_k=[1+k(m-1)](k+1)^2, the necessary target is A*sinh(B/(2r))=o(k*q_k). Sufficient but unproved inputs are r comparable to q_k, A=O(q_k), B=o(q_k log k).

Retain g=2xi, omega_0=mu_h^k, the arithmetic Taylor unit, both Gram cross terms, original relation depth chi_r (not chi_1^r), nonempty-packet inverses, and both cochain signs. The h=1 arithmetic module has dimension zero and determinant one, not zero analytic mass.

## Next bounded formal work

The present certificate does not include differentiation under arithmetic integrals, the full Hankel-Toda identity, the curvature identity as a theorem about derivatives, or the analytic asymptotic estimate. The actual polynomial least-norm map must be instantiated into the constructed finite Schur theorem. The full arithmetic rank-two radius must be connected to the volume energy using the exact phase identity, not introduced as an axiom.

## Source scope

Complete pasted Toda/exterior notes read; local runtime failure prevented ZIP manifest/test replay and six-part Deligne reassembly. Independently read original Weil II pp.156,158,203 via the author-hosted scan. Definition 1.3.5 and the estimates preceding 3.2.13 are relevant; their finite-field hypotheses are not transferred by a name change.
