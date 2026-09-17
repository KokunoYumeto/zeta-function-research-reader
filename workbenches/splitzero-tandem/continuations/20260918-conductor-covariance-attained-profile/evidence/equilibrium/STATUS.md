# Equilibrium and original-norm audit

Primary verdict for LRC11–15: **proved as written**, with the abbreviated arguments completed in this directory. The independent quantile audit proves a slightly stronger bound. The original mass, roots, Gamma shifts, both real half-lines and original monic fibres remain present.

The accepted local provider is `14_CURRENT_KERNEL_AND_MULTIPLICITY_PROOFS.tex`, SHA-256 `50e5071b8bc1e1325f401764e7fdd3cda50994601b6f2e1bf00627864d665571`, from `PROJECT_ROOT/work/mixed_tail_continuation_20260917/full_receiver_build/staging`. Relevant exact labels are EIQ1–33, ECL1–14, GRF1–5, GRE9–31, and RGC1–3. Their density, mass, endpoint, Euler and Robin conventions were read directly. No unavailable attachment package was used as evidence.

Dependencies: EIQ density and global Euler inequality → LRC11/LRC12 quantile bound → upper equilibrium monic bound; original Gamma density and mass + original opposite roots → full polynomial comparison → comparison on every unchanged affine fibre; arcsine logarithmic potential and entropy → lower equilibrium monic bound; endpoint equations and their exact derivatives → uniformity at h=1 through h=n. The lower and upper minima are not selected independently inside a claimed identity; inequalities hold first on the whole coefficient space and are then minimized on the same fibre.

Obligation matrix:

| Obligation | Verdict |
|---|---|
| LRC11, all real x and every quantile count, including endpoints | passed, independent proof |
| LRC12, original EIQ positive integral and derivative bounds | passed |
| LRC14, all complex polynomial directions of degree at most 2n | passed |
| Original Gamma mass and phase under the real-coordinate map | passed |
| Inner interval and both real half-lines | passed |
| LRC15 lower and upper constants, with full positive half-line | passed |
| Uniformity as alpha grows to infinity, including h=1 | passed, explicit common constants supplied |
| Scalar r=0,1 moments | passed for the stated M>=4 |
| Second intake equation (9) and (12) scalar ingredients | passed; separate power-exponential measure and shift -1/2 retained |
| Conductors, covariance sums, native allocation, arithmetic sign | outside this assigned proof; handled by sibling audits |

The second-intake scalar bounds require the root/Gamma comparison in its equation (8) separately. This audit verifies its exact Jensen, quantile, tail, parity and centre-shift ingredients, not an unseen package of GPA constants. A direct alternative from LRC14 and the retained-Gamma norms is available to the root reviewer if the GPA constants are unavailable.

No new numerical period evaluation, compilation, publication, or Lean certificate is claimed.
