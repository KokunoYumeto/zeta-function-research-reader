# Symmetric frontier delivery: complete proof review and continuation

The newly supplied `Tau_Symmetric_Frontier_Control_2026-09-12 (1).zip` was read and integrated on 12 September 2026. This review preserved the original archive and every staged source member, did not apply its patch to a shared branch, and did not edit the current cumulative `main.tex` or sealed earlier mathematical fragments.

## Edition, archive members, and revision record

The original archive is under the user-designated Noether Multilingual download directory. Its SHA256 is `a024ee4bbb4df9555bc6f94c2d74a2e90c077533ad2ce312863342b758539796`. The similarly named archive without ` (1)` is byte-identical; the duplicate suffix is therefore not a new mathematical revision.

Safe staging is at `sources/web_symmetric_frontier_delivery/Tau_Symmetric_Frontier_Control`. Every resolved member destination was checked against that intended root before extraction, and existing members were not overwritten. Exact archive locators, original sizes, and SHA256 values are in `sources/web_symmetric_frontier_delivery/LOCAL_STAGING_PROVENANCE.json`.

The complete `NOTE.tex`, `RESEARCH_NOTE.md`, `HANDOFF.md`, `PROGRAMME_STATE.md`, `VALIDATION.md`, checker, and reading/revision metadata were inspected. The eight-file additive patch was parsed and each reconstructed file compared byte-for-byte with the corresponding delivered source. No patch file modifies or deletes an earlier source. All eight comparisons pass.

The delivery is based on PR14 head `3bff1b2bd87dfa2592f65c5ccc231f6ee9541dfc`; its metadata explicitly records `remote_write: false`. It supplies an additive patch rather than a new published head. The source records two repaired display fixtures involving the exact matrix from `(1,s-1/2)` to `(1,s)`; the corrected matrix is preserved in the note and checker. No further revision history is present in the supplied archive.

- NOTE.tex SHA256: `734b6c935892ebd9d18b506f6b592f1ca3489afcb95d5c669a489f4ca04656cf`.
- RESEARCH_NOTE.md SHA256: `710ac0bc3d0f9fce403bf8db336ad93be0cdbf8ba63266dc3ab183154bd96d06`.
- Checker SHA256: `a486b13d0c1dfe073f40e33f7514e2f582e1c8e67cfc81bb039a883976f0b22e`.

The document's workflow statements were treated as source data, not new user instructions. The user's ongoing research and publication coordination determine the work scope.

## Complete proof review

The current cumulative CT.1–CT.26 and JD.1–JD.16 were used as the comparison baseline. An independent reviewer also read the complete PR10 global-retraction proof to verify the completed tensor topology used by the new source.

| Source | Verified mathematical content and exact scope |
| --- | --- |
| §§0–1 | Retains the infinite scalar target, represented zero and tau, original theta complex, generator, seed, full-order packet and arithmetic unit. Every polynomial relation remains an actual original theta boundary under the specified source map. |
| §2 | Orthogonalizes for `|g/h|² dt/(2pi)`, with literal polynomial norms and moment mass. The recurrence has coefficient `-omega_n/omega_(n-1)` and diagonal of real part `1/2`; its imaginary part remains. The source explicitly distinguishes these polynomials from the old `|g|²` seed-boundary polynomials through `T_h(hP)=Theta(P(D)phi*)`. The inverse Gram is the complete arithmetic-unit jet sum. |
| §3 | The actual relation graph `b=T_plus-RF` is an isomorphism onto the next orthogonal boundary layer. Highest-component extraction supplies its inverse. `Jb=0`, orthogonality, `b*b=Omega+F*GF`, and `b*R=-F*G` prove its Gram and projection. Fixed-order division supplies every original primitive and both Koszul signs. The representative, Gram, inverse-Gram and determinant updates follow from this same graph. |
| §4 | Total-degree recurrence pairs cancel with their actual norm ratios; the only surviving terms are the stated next-layer columns. Imaginary diagonal contributions cancel with their conjugates without being assigned zero. `Crel=b Omega^-1 Eplus*G` has the same target as the original `Y`, and their minus-sign cross form is exactly the displacement congruence. The finite `Gamma` upper bound follows from a matrix with nonnegative entries similar to a positive matrix, with the displayed exact row sums. It is a proved finite arithmetic inequality, not a claimed sublinear tensor estimate. |
| §4.6 | The source's AB/BA comparison correctly asserts equality of nonzero spectra. New FE.12–FE.19 strengthens it to an exact sequence, Hermitian support-space isometry, and the entire zero generalized eigenspace, including its possible size-two nilpotent extension. |
| §5 | Both permutation signs are correct: the Koszul action on odd top cochains contributes the permutation sign, and the signed chain average therefore has the ordinary symmetric top image. The unsigned chain average has the alternating top image. New SS.3–SS.7 proves the representation, differential equation, projector, and complementary summand explicitly. |
| §5.3, completion | The completion must be the completed projective tensor product used in the global-retraction source. PR10 supplies continuous `q,s,Lambda` and its tensor contraction. SS.1–SS.7 re-proves the completed comparison through the tensor homotopy and its permutation average. No blanket exactness assertion for arbitrary completed tensor products is used. |
| §5, support masks | At invariant labels the projectors split the original fibre. For arbitrary labels they first transport into the orbit-joined support. SS.1–SS.9 retains the exact original transport and its kernel; its sum is that transport, not an unproved identity on a different fibre. Zero amplitudes remain represented in their target support. |
| §6, orbit coordinates | Source and target orbit sums have their literal cardinality factors. The exact target Gram `D=I*I` and coefficient extraction `L=D^-1 I*` prove both inverse-kernel and metric compression. Invariance of the original metric is the reason those particular compression/inversion formulas hold. Partition-shell dimension follows from the onto full-jet map and the original relation graph, not a change of the quotient. |
| §6.6, finite trace wording | The numerical cycle trace and complement trace are correct for the finite packet. The sentence calling the symmetrizer a finite-rank cochain projector on the whole original complex is too broad: the symmetrizer on the infinite complex need not have finite rank. SS.8 constructs the exact finite projector `Pi_h=s sigma_h J_h`, with degree-zero part zero; `Pi_h^(tensor k) S_k` is the finite cochain projector supporting the asserted packet traces. Its inclusion/retraction are proved, and the whole symmetrizer and complementary cohomology remain present. |
| §7 | The declared Gaussian model retains its mass `sqrt(2pi)`, the stated `(1,x)` to `(1,s)` coordinate matrix, and full nilpotent generator. The positive example and nonmonotonic counterexample are both maintained. They are finite algebraic calibrations, not zeta packets. |
| §8 and evidence | No new uniform arithmetic estimate, Lean certificate, global purity theorem, or RH conclusion is asserted. The exact remaining upper estimate is on the original frontier matrices and their actual canonical metric. All theorem assertions accepted here have written proofs or an explicitly read earlier analytic proof; the finite checks are supplementary. |

## New complete proof fragments

`tex/frontier_energy_dissipation.tex`, FE.1–FE.25, SHA256 `856a8648f00ed023d52c5437f0b2085164bb943001e309ffe9c067230be89a0a`, contains:

- The original polynomial/jet/source definitions and a complete proof of the relation graph, its Gram, its derivative-layer map, and the total-degree displacement.
- Exact coordinates `U=G^(1/2)F Omega^(-1/2)`, `V=G^(1/2)Eplus Omega^(-1/2)`, with all inverse maps retained. The relative Gram loss is `UU*(I+UU*)^-1`; its eigenvalues are `lambda/(1+lambda)` for every positive frontier growth eigenvalue. The original derivative energy is exactly `chi=||V||HS²+||V U*||HS²`, and the determinant ratio retains every factor `(1+lambda)^-1`.
- The exact link to JD's accumulated determinant and energy identities, including the whole logarithmic remainder `sum int_0^lambda x/(1+x)^2 dx`.
- The complete smaller-border comparison: source coordinates are similar to `A0=J0K`, where `K=[U,V]*[U,V]`. The quotient `K^(1/2)` has exactly kernel `kerK` and intertwines with `H0=K^(1/2)J0K^(1/2)` on `rangeK`. A partial isometry identifies that Hermitian operator with the original relative form on `range[U,V]`, keeping both orthogonal complements.
- Every zero Jordan block of the border operator: if `Z0=ker(H0|rangeK)`, the exact extension map `z→J0K^(1/2)z` injects into `kerK`; there are `dimZ0` size-two blocks and `dimkerK-dimZ0` size-one blocks. The original supported chain `Lz→N0z→0` ends at represented zero, with neither intermediate support nor nilpotent data discarded.
- Finite determinant growth bounds from the original recurrence `Gamma` and from the actual derivative energy `chi`, retaining every positive denominator and the zero-departure case.

`tex/symmetric_spectral_cost.tex`, SS.1–SS.28, contains the complete signed cochain and completed-topology comparison, finite packet trace projector, unscaled orbit-coordinate maps, all occupancy multiplicities, full local nilpotent index and endpoint factorial, symmetric spectral departure, exact complementary tensor contribution, and symmetric determinant/energy dissipation.

For clarity, its new occupancy constants are `N=binom(k+d-1,d-1)`, `a=binom(k+d-1,d)`, `b=binom(k+d-1,d+1)`. With the full repeated list of offsets `delta_i`, the unweighted occupancy square sum is exactly `(a+b)sum delta_i²+b(sum delta_i)²`. The symmetric metric departure retains every strict triangular entry. The original symmetric layer bounds positive and negative inertia separately and preserves all repeated-eigenline amplification witnesses. The companion proof text, rather than these locators, is the mathematical deliverable.

The parent is independently developing the stronger holomorphic quartet-parity frontier calculation (`U*V=0` under its proved same-packet parity map). It is disjoint from this general-packet energy fragment. Another lane handles the further kernel-layer archive, incidence and filtered/Rees maps. No equality of homogeneous and orthogonal shell ranks is assumed here.

## Reproducible verification and evidence

- `scripts/validate_symmetric_frontier_delivery.py` verifies every staged source hash before and after execution, verifies both archive names have identical bytes, reconstructs all eight add-only patch files and compares them with the supplied source, then runs the original checker in four modes.
- Original source checker: **22 methods pass** normally and under `-O`, with byte-identical successful JSON. Both deliberate false controls produce **23 methods, one intended failure, no errors, exit 1**. Receipt: `checks/symmetric_frontier_fresh/validation_receipt.json`.
- `scripts/check_frontier_energy.py`: **34 exact Gaussian model records pass** normally and under `-O`. The original masses 7 and 11, nonconstant unit, nonzero imaginary recurrence diagonal, and repeated-root chain remain in the fixtures. Both deliberate negative runs have **34 passing records plus the intended false record**, and exit 1. These check the complete source relation Gram, rank, original layer factorization, relative loss, determinant, and both terms of `chi`.
- The independently derived singular-border checker has **102 passing records** in each positive mode. Six deliberately corrupted runs reject a false nilpotent square, an erased size-two zero block, and omission of the mixed `chi` term, normally and under `-O`. Scripts, receipts and proof report are included in the package.
- The independently derived symmetric occupancy checker has **938 passing records** normally and under `-O`. Both corrupted-orbit-coefficient controls fail. It retains all explicit occupancy combinatorics and local nilpotent endpoints; it does not certify arithmetic moments or global spectral claims.

Independent complete proof reviews are under `logbook/frontier_energy_review_20260912.md` and the packaged symmetric/Koszul and occupancy review files. Their exact final fragment hashes are also included in the integration manifest. All check counts are finite calibration records or test methods, not theorem counts.

The symmetric fragment compiled in an isolated wrapper with clean final TeX logs. This was syntax/layout-log validation, not a visual inspection claim. The cumulative build and actual visual PDF review remain with the parent. No PDF is claimed to contain these new fragments before that build succeeds.
