# PR #22 terminal independent review

## Outcome

Recommend merging the finite formalization at exact head `811210d24b80813a08972ca23f919db015383137` once the parent workflow resolves the remaining draft status. No mathematical, source-coverage, or CI blocker was found in this bounded review. This is not an approval of an analytic Toda estimate, the Riemann hypothesis, or source interfaces absent from these finite declarations.

PR: https://github.com/KokunoYumeto/zeta-function-research-reader/pull/22

The fresh before/after readbacks recorded an open draft PR, `mergeable=true`, `mergeable_state=clean`, with base `main` at `fa4be32f87a9a90f3c02a07f7790dea95a1e7b0f`. The exact head was stable across intake and the terminal evidence download. Current-base comparison is ahead by 20 commits, behind by zero, with that main commit as merge base. The resulting delta adds ten files; it modifies or deletes no existing file. In particular the inherited conormal workflow correction is already in current main, not a new PR #22 overwrite.

## Terminal CI and actual reports

All nine check runs, nine jobs, and every step in all nine jobs are `completed/success`; no source or audit step is skipped. Complete logs were freshly downloaded and hashed. The three critical logs are byte-identical to the prior pinned evidence.

| Run | Job | Workflow | Terminal proof-report evidence |
| --- | --- | --- | --- |
| 34721815033 | 103628992357 | Exterior, push | Exact head; all 4 new modules strict-checked; 50 exact raw axiom reports; every inherited audit passes |
| 34721817007 | 103628997564 | Exterior, PR | Test merge `ea88606764ba2a2875cb86ba073a3d33e061ac7e`; same 4 modules and 50 reports; every inherited audit passes |
| 34721817059 | 103628997656 | Conormal cyclic tower | Both conormal modules strict-checked; 29 exact raw reports; joint import and inherited audits pass |
| 34721817036 | 103629032739 | Structural formalization | 28 unique raw reports, standard axioms only; source/build steps pass |
| 34721817068 | 103628997731 | Actual synchronization | 19 synchronization reports with standard axioms only; structural 28-target audit passes |
| 34721817035 | 103628997638 | Tau recovery | Exact 87-target tau and 73-target derived report sets; structural 28-target audit passes |
| 34721817115 | 103628997927 | Derived constructions | Exact 73-target derived report set; structural 28-target audit passes |
| 34721817001 | 103628997561 | Finite frontier | Exact 40 frontier, 68 boundary-integration, 38 boundary, 87 tau, 73 derived report sets; structural 28-target audit passes |
| 34721816993 | 103628997452 | Boundary layer integration | Exact 68 boundary-integration, 38 boundary, 87 tau, 73 derived report sets; structural 28-target audit passes |

The exterior push and PR jobs each also contain the exact inherited sets of 29 conormal, 40 frontier, 68 boundary-integration, 38 boundary, 87 tau, and 73 derived declarations, followed by `PASS: 28 selected declarations; only standard axioms`. The conormal job contains those same inherited sets excluding exterior. The independent offline parser matches the complete reported declaration sets against the fetched manifests, checks duplicates in the raw exterior/conormal reports using the already-read strict parser, and checks all parsed dependencies are subsets of `propext`, `Classical.choice`, `Quot.sound`.

The exterior source hashes printed by both CI jobs exactly match the four reviewed files. All are compiled with `--trust=0 -DwarningAsError=true`, before selected audit execution. The pinned environment remains Lean 4.31.0 and Mathlib `fabf563a7c95a166b8d7b6efca11c8b4dc9d911f`. The external Mathlib cache is a dependency input; this review did not locally rebuild Lean or claim a fresh verification of every Mathlib source.

## Prior findings closed

The full source of all four new Lean modules, their original-Gram dependency, complete target manifest, checker and inherited strict parser, new workflow, inherited conormal workflow, rational checker, research note, and handoff were read.

1. The former strict-linter error in `control_selfadjoint` is repaired by omitting the unused `[Fintype n]` instance. Its mathematical statement and proof body are unchanged.
2. Filtration is now the fourth generated strict-source module and joint import. Its four public theorems are selected. The previous invalid `Complex.sum_re` simplification is replaced by the explicit real-part additive-homomorphism sum identity; unused `DecidableEq n` is omitted from `nested_difference`. Hypotheses and conclusions are preserved.
3. The final `zero_certificate`, `certificate_bound`, `original_gram_bound`, and supporting `control_selfadjoint` declarations are now directly included. There are 50 selected declarations, with all 42 earlier selections retained.
4. Push paths include main; PR and push paths cover `formal/splitzero/**`, the task workbench, and the workflow itself. Inherited dependency changes therefore trigger the dedicated checks.

The complete comment-stripped source scan finds no `sorry`, `admit`, new `axiom`, `unsafe`, `implemented_by`, or `native_decide` escape in any of the four modules. The actual exact selected reports contain no nonstandard axioms, including no `sorryAx`. Whole-file strict compilation and selected transitive reports are distinct evidence; neither is replaced by Python examples.

## Mathematical scope and hypothesis check

`SplitZero.TraceCertificate.original_gram_bound` at lines 201-235 concludes

    |2 Re tr(a) - w dim(d)| <= e.

Its actual data retain finite complex matrices; explicit inverse coordinates T and T-inverse with T* T=G; inclusion B and extraction L with LB=I; invariance AB=Ba; G-self-adjointness of BL; nonnegative real e; rectangular U:n-by-2 and V:2-by-n; GUV=A*G+GA-wG; tr(VU)=0; and det(VU)=-e^2. The proof transports A, B, L, U, and V together along that same coordinate isometry, and proves the compressed VU remains literally unchanged. It never replaces the original Gram by an unrelated metric.

The positive case derives H^3=e^2 H, tr(H)=0, and tr(H^2)=2e^2 from the literal two-coordinate factorization. It constructs (H^2 +/- eH)/(2e^2), proves Hermitian idempotence and trace one, and gets the bound from projection overlaps. The zero case uses Hermitian positivity, not nilpotence alone, to obtain H=0. There is no dimension multiplier in the resulting allowance. No normality or semisimplicity of A, invariant orthogonal complement, or orthogonality of an oblique arithmetic spectral projector is assumed. BL is explicitly the metric-orthogonal projection; an oblique CRT projector remains a distinct object in `projector_trace_comparison`.

`TraceFiltration.resolution_budget` and `gram_resolution_budget` conclude the total absolute projected control trace is at most 2e. They take a resolution of the identity by (Gram-)self-adjoint idempotents and signed trace-one control projections as hypotheses. `nested_difference` verifies a difference of nested orthogonal projections is a projection. These files do not construct the invariant arithmetic filtration, identify every quotient action, or connect the filtration resolution directly to a chosen U,V certificate in a single formal theorem. Those interfaces remain in the caller/written deductions, as the handoff states.

The current-base delta does not alter inherited theta/fullMultiplier definitions or claims. The newly added Lean files do not define or use `fullMultiplier` or a theta map. The inherited 87-target tau report continues to pass, but that is not a new analytic theta-map construction supplied by this PR.

Still outside this finite formalization: canonical arithmetic construction of G,U,V and their identities; construction of the actual spectral subspace and Gram coordinates for a given analytic packet; the complete exterior algebra/additive generator; p! source norm and completed tensor topology; Koszul/theta primitives; and the analytic allowance estimate uniform in tensor degree. Finite CI does not prove analytic Toda identities or RH. The selected external Deligne-reading claims and source archives were not independently re-audited here.

## Rational regressions and residual nonblocking observations

The source of the 244-line standard-library rational checker is unchanged from the previous completed finite replay. Its SHA-256 remains `84bef5607cba645e2dd1ae0523243e71dc14e966ebdb216c6085f2cba0106cdb`. Both terminal exterior jobs run all ten methods normally and with `python -O`, compare their JSON, and verify normal and optimized intentional-failure propagation. These are exact rational finite examples, not zeta-zero data or analytic interval estimates. No new local finite rerun was needed to establish terminal CI.

The previously noted test-05 name is still imprecise: its body demonstrates zero compressed trace defect with nonzero full control, not a genuinely zero Hermitian control permitting nontrivial Jordan action. This does not weaken any Lean theorem and is not a merge blocker. The research note's statement that filtration is not bundled in Lean predates the added finite filtration coverage; the new handoff explicitly distinguishes the now-checked projection budget from still-written quotient and monodromy constructions. This is a documentation consistency nit, not a proof gap.

## Evidence and action boundary

`terminal_evidence/FETCH_TERMINAL_RECEIPT.json` binds fresh PR, current-base comparison, all checks/runs/jobs and full logs. `terminal_evidence/TERMINAL_ANALYSIS.json` records independent offline parsing, source hash alignment and exact report coverage. `TERMINAL_REVIEW_RECEIPT.json` seals this report, scripts, and evidence receipts by SHA-256.

No local Lean, package build, Git operation, visible browser, remote write, PR draft change, merge, publication, canonical mathematical edit, usage reset, or child agent was performed. Review outputs are confined to this review directory. The parent workflow owns any authorized merge/publication mutation and must recheck the head immediately before acting.
