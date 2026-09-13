# Exact-head PR #25 review and bounded correction proposal

## Recommendation

Do not merge the actively edited draft yet. The principal written norm/window arguments and finite Lean interfaces are sound within their stated original-source premises. Correct the strict-positive eigenvalue claim, preserve zero multiplicities, repair the workflow triggers, and obtain the appropriate final exact-head checks. Relay the bounded review comment to the author rather than racing a branch update.

This review followed `bb29776518b7d7e6dfe704878e627f2b92e84e32`, then the author's repair `a02db96da0faff1aae32409c2719aab395a4aae9`, then `66fac5e7885a40cd4873e74b754907320f05b067`. All changed mathematical, Lean, audit, workflow and checker sources were read completely at the initial head, and all changed successor files were fetched and read completely. The inherited TodaVolume definition/proofs, preparation script, toolchain and lakefile were also read. The author incorporated main `952ef9fee1e1419b6858d920354de8fa99430b7d` into its branch; the resulting current-main delta has eleven added paths and no modification/deletion of a preceding main path. No branch change or local Lean execution was performed. The only authorized remote action was the bounded review comment linked below.

## Correctable findings

1. `RESEARCH_NOTE.md`, section 3: the generalized eigenvalues of `(F*G_iF,Omega)` are **nonnegative**, not necessarily strictly positive. The intended exact-quartet family itself supplies singular F at even tensor degrees. The complete parity proof and a portable exact regression are in `PROPOSED_REVIEW_COMMENT.md` and the three-file proposal. All q eigenvalues, including zeros, must remain in the determinant and AM-GM averages. This changes neither displayed block budget nor threshold four.
2. The new workflow's push branch filter excludes main, so a normal main merge would not run this same strict new workflow. Its PR filter also omits `AuditConsecutiveWindow.lean`. Add main and that audit path. Preserve the entire job body, strict flags, pins, transitive audit and the author's new arithmetic-source replay.

The local proposal changes exactly the note, checker and new workflow. It changes no Lean theorem and no existing main file. Its branch is active, so the files are suggestions for the author/parent, not an executable authorization to overwrite a moving head. The first proposal receipt is historical for a02; use `PROPOSAL_66_RECEIPT.json` and `proposed_66/` for the successor-compatible proposal.

## Written calculations and their limits

The analytic audit uses the supplied original density, not a replacement measure. The Joukowski ellipse gives the claimed bounded real strip and avoids the zeta pole for |T|>=10. Splitting at real part 1/4 makes the largest stated growth exponent 79/16, below 6. The inverse Dirichlet-series bound at real part 2, annular propagation and Cauchy derivative estimate give the local exponent 42. Using `g=h(g/h)` avoids dividing at selected zeros. Boundedness plus L1 translation continuity makes the positive twofold convolution continuous; restricting further convolution variables produces the original mass factor and its k>=3 lower envelope.

The two-sided norm envelope is correctly derived from the monic Legendre minimum and actual exponential moments: `(ell*n)^(2n) <= omega_n <= (U*n)^(2n)` for n>=k>=3. In the lower bound, `vartheta^(k-3)>=min(1,vartheta)^n`, the exponential cost is at least exp(-2an), `(2n)^(-B)>=2^(-nB)`, and `2c/3>=min(1,2c/3)^n`. The upper trial-polynomial bound is dominated by the stated U. No monotonicity of monic norms or normalization of mass is needed.

For n/2<=r<=2n, division of the envelopes gives `n*U^(1+n/r)*ell^(-n/r)*(1+r/n)^(1+n/r)`; the displayed constant `27*max(1,U)^3*max(1,ell^(-1))^2` bounds it. Both proposed length-q windows meet the conditions for k>=3. The first-degree source formula supplies the n=q-1 step without a previous singular inverse. Hence the two block budgets are each at least `2q*log(D_h*k)`, giving `4q*log(D_h*k)` in the same four-volume budget. This is compatible with the already published central-window proof's `4(q-1)` finite bound and identical limiting constant four. `COORDINATION.md` correctly identifies the shared threshold result and the additional comparable-window/first-degree composition.

The original source maps, full Taylor unit, shifted coordinate and its modulus-one leading phase, total mass, source relation subspaces, cyclic multiplicities, supported zero and external tau are retained. For the original quartet the measure is even at theta=0; the phase is not discarded in the deformation identities. The general-packet analytic norm envelope is not a claim to extend the dagger-specialized quotient identities to arbitrary packets. The original degree/dagger qualifications remain part of that interface.

No opposing upper arithmetic volume estimate is obtained. The analytic envelope, limiting argument and relation-block eigenvalue interpretation are written mathematics, not additional Lean declarations, zero-location computations or interval certificates.

## Finite formalization

The new declarations prove conditional algebraic interfaces, not the existence of the arithmetic data satisfying their hypotheses:

- `exact_step` expands the original Toda energy and retains the real phase square. `radius_step` bounds the two contraction factors and phase loss with explicit positive denominators.
- `exact_product` telescopes r+1 steps with all interior losses squared; its base case is the one-step identity. `product_bound` and `lower_bound_propagates` preserve the common nonnegative lower allowance. The natural-index offset differs from the prose's length-r notation but is consistent after substitution.
- `first_radius_step` uses the independent first-degree relation norm and transition. `norm_bound_forces_volume` clears only positive denominators and composes the actual supplied norm upper bound. `log_volume_forcing` applies the log only to positive data.
- `doubling_from_envelope` is the finite power consequence of the two explicit envelope premises. `canonical_norm_volume` constructs Lambda_j=w_j/V_(j+1), derives each local inequality from the supplied radius equation, then composes propagation and the norm bound. Its shifted volume indexing is correct. It does not assume its own endpoint conclusion.

The new sources contain no sorry, admit, custom axiom, unsafe/native decision escape or skipped local proof. CI compiles the inherited TodaVolume and all four new modules using `--trust=0 -DwarningAsError=true`. The original core blob, Lean 4.31.0 and mathlib revision remain pinned. The audit enforces the exact selected target set, rejects duplicates and permits only propext, Classical.choice and Quot.sound. The successor has ten targets, not nine.

## Observed execution evidence

At bb297, both new window runs failed. The failed log shows a multiplication-order mismatch in the division proof and an unnormalized natural-number cast of 2 in the logarithm proof. The a02 author patch changes exactly those proof steps; it does not relax a premise or conclusion. Both a02 window runs and all nine inherited workflows completed successfully. The read-back window log has nine accepted standard-axiom reports and seven normal/optimized finite methods.

At 66fac5e, both window runs **34728377778 / job 103646536376** and **34728375048 / job 103646529213** completed successfully with every step successful, including the added arithmetic-source replay. Both full logs were downloaded and independently passed the fetched ten-target audit. Each contains all ten reports with only the three allowed standard axioms. They record seven core methods in both modes, verified intentional negative-control failures, and the byte-pinned arithmetic and balanced checkers in both modes with identical output. The arithmetic record has 18 methods and the balanced record contains 12,017 checks. These are actual GitHub execution records, not local Lean replays. The final observation confirms all eleven current-head workflow runs completed successfully, including all nine inherited workflows; their earlier pending snapshots remain separate historical observations.

Fresh local diagnostics separately ran the fetched seven-method core and the proposed eight-method core normally and under optimization; every normal run passed and every intentional negative control exited 1. The added Gaussian rational fixture retains generalized spectrum `[0,19/4,83/10]`, a rank-two F with kernel `(13,0,2)`, and determinant ratio `2139/40`. These finite fixtures support the correction; the parity argument proves its necessity for the intended even-k quartet family.

No PR status, branch, main file, frozen E asset or Zenodo object was changed by this review. The approved [single author-facing comment](https://github.com/KokunoYumeto/zeta-function-research-reader/pull/25#issuecomment-5649747922) was posted and its exact body read back. The next action is to review the author's resulting head and its own CI; the present head still needs the two scoped corrections despite its successful checks.
