# Independent bounded holonomy descent replay and patch review

The new twenty-two-method finite suite passes in ordinary and optimized Python, with byte-identical success records. All forty-two raw manifest rows match. All fifteen payloads in the integration patch are genuine file additions and reconstruct byte for byte to the delivered members. All forty-three raw files remain unchanged.

The supplied negative-control launcher has a material validation weakness: it raises an error even if a false formula is not rejected. The source was preserved, that defect was reported before repair, and a separate harness now rejects three actual target-mathematics mutations in both modes. Its zero exit remains reachable if a mutant equality unexpectedly survives. The new execution scope is exactly forty-four positive method invocations and six substantive negative invocations, in eight checker processes.

## Exact source, manifest, and isolation

The raw source is `workspace:/output/split_zero_rh_tandem_2026-09-12/sources/web_holonomy_descent_delivery/Tau_Holonomy_Descent_Control`. All local replay artifacts are under `workspace:/work/holonomy_descent_replay_20260913`.

The parent supplied the archive SHA-256 `f0506a27cd4c9012f43fa70c3d1f8f996bbb6db01b0eea2944b34dcf290ca8f0` and performed the safe extraction. This subtask's independent measurements concern the extracted forty-three-file tree. `MANIFEST.json` has SHA-256 `6d1f2799c840e34b8b144d864f7e088c06da8c024f3f7a7ce367d02cb57499c5`. Every one of its forty-two byte-count and SHA-256 rows agrees with the actual member; the only unlisted member is that manifest itself. The complete rows are recorded in `manifest_validation.json`.

The before-and-after snapshots agree for all forty-three files, including the manifest. Their complete byte counts and hashes are in `raw_snapshot_before.json` and `raw_snapshot_after.json`. The delivered checker was copied unchanged to `executable/check_holonomy.py`; its measured source and copy SHA-256 is `206da9776874d443fb4bc09dd21c0cc1dddbddc2e030f0c94570501b2697fea9`. The new controls are separate in `substantive_negative_controls.py`, SHA-256 `00b4502be5d5ffa2cfec584098d4e28682c047d7d52f517716d30fd0df4ba62b`. No source file or historical receipt was repaired in place.

## Pre-execution audit and the supplied negative-control defect

The complete delivered `scripts/check_holonomy.py`, `MANIFEST.json`, `VALIDATION.json`, and `HANDOFF.md` were read before execution. The checker imports only standard Python modules and SymPy. Its twenty-two cases are registered by the `@case` decorator; AST inspection confirms exactly twenty-two such functions. Equalities and order conditions use explicit `ArithmeticError` exceptions. There are no removable Python `assert` statements in either the unchanged checker or the separate new controls. None of these imports invokes a predecessor suite, a reader builder, or a browser.

The current delivered negative branches occupy lines 286–295. Their actual behavior is:

1. `erase-variance` constructs the literal mass-seven source matrices and compares their actual quotient mean with the quotient of their mean. The equality is false by `7/9`; it is a substantive formula check.
2. `support-is-absence` directly requires the fixed tuple equality `('ell',0)==('absent',)`. These fixed representations differ, but the branch does not evaluate or mutate the supported coefficient map. It cannot detect a regression in that map's implementation.
3. `omit-fourier-factor` computes the unscaled two-character Fourier matrix product and compares it with the identity. Its residual is the two-dimensional identity; it is a substantive formula check.

In addition, current line 300 is

```python
if args.negative:negative(args.negative);raise ArithmeticError('negative control did not reject')
```

Both statements following the colon are in the conditional body. Therefore, if a requested negative comparison returns without an exception, the following unconditional fallback exception still yields a failing process. A rule that accepts every nonzero exit cannot distinguish a rejected false formula from an undetected mutation followed by this guard. This is the precise harness defect; it does not turn the first and third branch computations into startup stubs.

The delivered historical logs actually end in the intended formula errors, including `Matrix([[7/9]])`, the support tuple error, and `Matrix([[1,0],[0,1]])`. They therefore record formula failures at their historical execution sites, rather than the fallback guard. Those logs have older source line locations (main at 278) than the delivered current script (main's negative branch at 300). They remain historical evidence and were neither overwritten nor represented as fresh executions of the current bytes.

The separate harness was implemented only after the defect was reported to the parent. It validates the unmutated target identity first, records all input and output matrices, then tests the deliberately mutated formula or support-map result. Rejection occurs at that final comparison with the prefix `MUTATION_REJECTED:<control>`. If the mutation is not detected, its function returns and `main` returns zero. There is no unconditional failure guard. The supplied negative CLI branches were not rerun; only the separate substantive controls were newly executed.

## Actual commands, runtime, and output counts

The actual interpreter is `runtime:python/python.exe`, Python 3.13.9. SymPy is exactly 1.14.0, imported from `workspace:/work/kernel_layer_replay_dependencies_20260912/sympy/__init__.py`. `PYTHONPATH` names that dependency directory and `PYTHONDONTWRITEBYTECODE=1`. The actual full Python version string, import location, and environment settings are in `runtime.json` and `execution_receipt.json`.

For each mode the positive command is the argument array `[PYTHON, OPT, REPLAY/executable/check_holonomy.py]`. Each negative command is `[PYTHON, OPT, REPLAY/substantive_negative_controls.py, --negative, NAME]`. `OPT` is absent in normal mode and the literal `-O` in optimized mode; `NAME` is one of the three names below. The complete absolute argument vectors, working directory, start/end timestamps, elapsed time, return code, and stdout/stderr path and SHA-256 are preserved for all eight actual child processes.

| Mode | Process | Seconds | Exit | Verified result |
| --- | --- | ---: | ---: | --- |
| normal | new suite | 35.30246070001158 | 0 | all 22 registered methods pass |
| normal | erase-variance | 0.41004269997938536 | 1 | actual false quotient interchange rejected |
| normal | support-is-absence | 0.3939400000090245 | 1 | actual support-map mutation rejected |
| normal | omit-fourier-factor | 0.4165477000060491 | 1 | actual Fourier-factor omission rejected |
| optimized | new suite | 35.5383240999945 | 0 | all 22 registered methods pass |
| optimized | erase-variance | 0.39000990000204183 | 1 | actual false quotient interchange rejected |
| optimized | support-is-absence | 0.3933847999724094 | 1 | actual support-map mutation rejected |
| optimized | omit-fourier-factor | 0.4269895000034012 | 1 | actual Fourier-factor omission rejected |

The run began at `2026-09-13T05:13:09.782137+00:00` and completed at `2026-09-13T05:14:23.072971+00:00`. Both suite stderr files are empty. Both suite output records list the same twenty-two names in the exact AST registry order and are byte-identical. Every negative stdout contains the actual exact fixture evidence, and every negative stderr reaches the intended mutation comparison; none contains a baseline failure, import failure, syntax failure, or startup refusal. The recorder requires the formula-specific error prefix rather than merely accepting exit one.

## Complete finite method inventory and executed scope

The quotient helper uses the actual matrices

\[
G=(JM^{-1}J^*)^{-1},\qquad C=M^{-1}J^*G.
\]

The remainder matrix `J=jmatrix(chi,N)` has column c equal to the coefficient vector of `S^c mod chi`; the relation matrix `B=bmatrix(chi,N)` has column c equal to the coefficient vector of the literal `chi S^c`. The finite moment helper constructs the exact Vandermonde Gram `V* diag(weights) V`. All entries used in the fixtures are exact rational or complex-rational numbers, together with exact finite Fourier square roots. Positivity is tested through exact leading principal minors for positive definiteness and all principal minors for positive semidefiniteness.

| Registered method | Actual finite fixture and calculation |
| --- | --- |
| `split_fibres_preserve_absence_and_supported_kernel` | Applies the actual zero coefficient map to a supported input with label `ell`, preserving its supported zero; checks that external absence stays absence and differs from that zero. |
| `finite_cover_full_laurent_basis` | For cover degrees 1 through 7 and exponents −17 through 17, verifies Euclidean reconstruction `n=ma+j`, `0≤j<m`; checks the retained carry when all pairs of basis powers multiply. |
| `character_projectors_complete_orthogonal` | For covers 2 and 4 and roots −1 and i, constructs all projectors with their `1/m`, checks sum identity, Hermitian idempotence, pairwise orthogonality, and the specified shift eigenvalues. |
| `fourier_inverse_retains_cover_factor` | For covers 2 and 4, checks both matrix unitarity identities and inverse reconstruction of the specified complex-rational vector using the exact `1/sqrt(m)` factor. |
| `phase_mean_filters_only_correlations_divisible_by_cover_degree` | For covers 2 and 4, checks each exact character mean for exponents −13 through 13, retaining the zero mode and precisely the multiples of m. |
| `shifted_sampling_refinement_keeps_sum_coordinate` | For m=1,...,6, theta=2/7, L=5/3, each phase and n=−4,...,4, verifies the shifted frequency identity in the explicitly stated units of `2 pi`. |
| `repeated_jet_quotient_and_original_relation` | Uses `chi=(S−1)²`, N=3, five points `1+i x`, x=−2,...,2, and weights 7,11,13,11,7. Checks source/quotient positivity, `JB=0`, `JC=I`, `B*MC=0`, and `C*MC=G`. |
| `exact_mean_variance_uses_original_boundary_columns` | Uses the two-phase nonunitary block fixture at q=2 and eta=1/3. Constructs each `X_j` from the original B, verifies `C−C_j=BX_j`, and checks the exact matrix variance decomposition and its positivity. |
| `sharp_quadratic_constant_with_literal_mass_seven` | For eta=1/7,1/3,3/4 and `M=7I2`, `J=(1,0)`, computes the two exact phase quotients and checks their mean is `(1−eta²)G`, retaining `G=7`. |
| `matrix_quadratic_comparison_under_nonunitary_coordinates` | At q=1,2,3 and eta=1/3, keeps the specified complex nonunitary triangular coordinate matrix and verifies both semidefinite quotient bounds. |
| `inverse_chord_and_inverse_mean_block` | At q=2, eta=2/5, checks the exact inverse chord residual, each positive block `[[K_j,I],[I,G_j]]`, and `mean(G_j)−mean(K_j)^−1` positive semidefinite. |
| `asymmetric_chord_bound` | Uses a=1/2, b=5/4, probability 1/3, `M=[[5,1],[1,3]]`, `J=(1,0)`, and proportional phases aM,bM. Checks the exact source mean and both quotient inequalities with `ab/(a+b−1)=5/6`. This proportional fixture does not independently establish sharpness in a general noncommuting family. |
| `equal_jet_cochain_split_and_contractible_complement` | Uses `chi=(S−1)²`, N=3, three specified relation perturbations of `2+3S`, checks common jets, average/reconstruction, and zero-sum deviations. The identity differential/contraction is represented by the identity matrix on the four-dimensional relation complement. |
| `degree_raising_map_commutes_with_actual_remainder` | For `(S−1)²` and `S³+2S+1`, uses N=q+1 and the actual degree-raising rectangular coefficient map, verifying `J_(N+1) U=A J_N`. It does not replace that source map by a cutoff endomorphism. |
| `unchanged_unit_and_theta_primitive` | Uses the repeated-jet fixture and literal invertible multiplication matrix `[[0,−1],[1,2]]`. Checks retained unit composition and that each column difference of canonical lifts is divisible by the original `chi`, with exact zero remainder. |
| `original_sampled_action_keeps_boundary_control_sign` | Uses seven points `1+i x`, x=−3,...,3, the original listed positive weights 2,3,5,7,11,13,17, k=2, and the sampled defect `B_s=D R_s−R_s A`. Checks `D*W+WD=kW` and the exact negative boundary-control sign in the coefficient Gram identity. |
| `finite_phase_interlaced_moment_identity` | Uses four phases, N=3, k=2, five shifted indices per phase, and weights `7/(1+a²)`. Checks the exact finite interlacing mean, retaining the factor 1/4, and the induced quotient-mean variance identity. |
| `residue_constituent_comparison_retains_unit_and_dual_factor` | Uses the q=2, eta=1/3 block quotient, the invariant column `(−1,1)`, unit `(1,0)`, residue row `(0,1)`, and both strictly positive coupling factors. Checks lower factor 8/9 and upper factor 9/8. |
| `translation_congruence_keeps_coefficient_but_not_trace_shift` | Uses `a=2/3+i/5`, the two-dimensional Pascal matrix, the full complex-rational metric `[[7,1+i],[1−i,5]]`, and transformed inclusion, unit, and dual residue. Checks exact coupling invariance and the full complex trace shift `2a`. |
| `further_sampling_quotient_retains_explicit_jet_kernel` | Uses `chi=(S−i)²(S−1)`, the full three-dimensional degree-two remainder basis, and evaluation at i. Shows the nonzero vector of `S−i` is killed, and the evaluation has rank one and kernel dimension two. |
| `holomorphic_schur_extension_retains_parameter_without_conjugating_it` | Uses the exact nonzero symbol z, eta=1/5, and the mass-seven two-dimensional matrix with off-diagonal `eta(z+1/z)/2`. Checks the holomorphic Schur expression and its substitutions at 2,2i,1+i, with stars only on fixed columns. |
| `phase_quotient_quadrature_has_its_own_retained_fourier_terms` | Uses eta=1/3 and the displayed Laurent polynomial quotient. The four-phase average equals its constant term; the two-phase mean differs by exactly `7 eta²/2=7/18`, so quotient quadrature is not silently treated as exact. |

These are finite regressions with the stated objects and ranges. They do not execute an all-phase integral, certify analytic tail bounds, prove the original arithmetic weighted-source constants, or establish an arithmetic volume upper bound. The parent owns the complete written seventy-three-equation proof review. The predecessor's sixteen-method suite, predecessor manifest audit, browser screenshots, and prior development-failure log are retained supplied history and are not included in this subtask's new execution count.

## Full exact calculations for the separate substantive controls

### Erasing the quotient-mean variance

Keep the original literal mass seven, `eta=1/3`, the quotient row `J=(1,0)`, and the original boundary column `B=(0,1)^T`. Define

\[
M=7I_2,\qquad
M_\sigma=7\begin{pmatrix}1&\sigma/3\\\sigma/3&1\end{pmatrix},
\qquad \sigma\in\{1,-1\}.
\]

Their equal-weight mean is M. Each phase matrix has the two positive eigenvalues `7(1−1/3)=14/3` and `7(1+1/3)=28/3`, so the displayed source metrics and their inverses remain in the required positive domain. Inverting the two-dimensional matrices gives

\[
M_\sigma^{-1}=\frac{1}{7(1-1/9)}
\begin{pmatrix}1&-\sigma/3\\-\sigma/3&1\end{pmatrix}.
\]

Thus the quotient metrics and canonical lifts are

\[
G=7,\quad C=\binom10,\qquad
G_\sigma=7(1-1/9)=56/9,\quad
C_\sigma=\binom{1}{-\sigma/3}.
\]

The actual difference is `C−C_sigma=B X_sigma`, where

\[
X_\sigma=(B^*M_\sigma B)^{-1}B^*M_\sigma C=\sigma/3.
\]

Therefore each phase variance is `X_sigma* (B* M_sigma B) X_sigma=7/9`, and the complete equal-weight identity is

\[
7=\frac12\left(\frac{56}{9}+\frac{56}{9}\right)
+\frac12\left(\frac79+\frac79\right).
\]

The separate harness first verifies that full identity and the actual boundary-column expressions. It then erases the variance and compares 7 with 56/9. The exact residual is 7/9, which triggers the formula-specific rejection in both modes.

### Collapsing a computed supported zero to absence

Let the actual coefficient linear map be `A0=[0]:C→C`, keep the supported input `x=('ell',7)`, the supported zero `z=('ell',0)`, and external absence `tau=('absent',)`. Define the supported lift by

\[
\widehat A_0(\tau)=\tau,\qquad
\widehat A_0((\lambda,v))=(\lambda,A_0v).
\]

The harness computes `A0[7]=[0]`, so the actual result is z. It separately checks `widehat A0(tau)=tau` and `widehat A0(z)=z`. The mutation is applied to that computed result: it replaces every supported image whose coefficient is zero by tau. Applied to x, the mutated function therefore returns tau while the correct supported lift returns z. The retained tag and label make these different elements. The failure occurs in comparing the results of the two actual map implementations, not in a startup assertion of a fixed tuple inequality.

### Omitting the Fourier cover factor

For cover degree `m=2`, retain

\[
W=\begin{pmatrix}1&1\\1&-1\end{pmatrix},\qquad
U=W/\sqrt2,\qquad
v=\binom{1/3}{2/3+i/7}.
\]

Direct multiplication gives `W*W=2I2`, hence `U*U=I2` and `U*(Uv)=v`. The harness verifies these exact baseline identities and records v and its full reconstructed value. The mutation omits the divisor `sqrt(2)` and uses W. Its alleged isometry then compares `W*W=2I2` with `I2`, leaving the exact residual `I2`. This final comparison produces the intended formula error in both modes.

Each control records these exact inputs and computed results before its final deliberately false comparison. Explicit arithmetic exceptions remain active under `-O`; no control relies on Python `assert` and none relies on an unconditional final exception.

## Independent line-anchored integration-patch verification

`INTEGRATION.patch` is 304893 bytes, SHA-256 `2a858e01f833145783e3e482e8b90af86c60d08089d1ea01a2bb941cb65d98be`. The independent `patch_audit/audit_patch.py` parses the actual byte grammar through a line-anchored state machine. It accepts only the specified unquoted ASCII paths under `workbenches/tau-holonomy-descent-control/`, regular new-file modes, all-zero old index, `--- /dev/null`, matching new-file headers, and contiguous insertion hunks whose old start/count are both zero. Hunk line counts are consumed exactly. Context, removal, unknown metadata, unsafe paths, binary sections, and unexplained trailing data are rejected by the parser.

Payload reconstruction removes exactly one leading plus from each added line. It splits only on literal LF, not on Unicode line separators. The three explicit no-final-newline markers remove precisely the serialization LF from the final payload line. Thus no line-ending, whitespace, character, or terminal-newline conversion is introduced. The reconstructed bytes were compared directly with raw member bytes and also used to compute each Git blob SHA-1, including its `blob <length>\0` prefix.

All fifteen files match in full. Their raw-relative paths are:

1. `COORDINATION.md`
2. `HANDOFF.md`
3. `INTAKE.json`
4. `NOTE.md`
5. `NOTE.tex`
6. `README.md`
7. `SOURCE_REVIEW.md`
8. `VALIDATION.json`
9. `checks/exact-normal.json`
10. `checks/exact-optimized.json`
11. `checks/negative-controls.json`
12. `index.html`
13. `reader.css`
14. `scripts/build_reader.py`
15. `scripts/check_holonomy.py`

All fifteen computed Git blob hashes match the declared index prefixes. The exact reconstructed payload total is 296600 bytes. The three files without a final newline are `INTAKE.json`, `VALIDATION.json`, and `checks/negative-controls.json`, and their absence of a terminal newline is preserved. The supplied patch receipt lists the same fifteen unique targets in a different order; order is not treated as a payload mismatch. There are no added/modified/deleted-count discrepancies, duplicate targets, or Windows case collisions.

The parser, its full row-by-row result `patch_audit/PATCH_AUDIT.json`, its separate review, and all fifteen reconstructed files are retained. The JSON report SHA-256 is `28627f1404a9fd9912898b90034f13723e43d46689f6e38a2a1a8116b1ef6485`; the parser SHA-256 is `9f4283c41c1e32d5e735b3dd5df91488d83bd9b9b32f93fb2624d98d9bfa9463`. The patch auditor rechecked the patch, supplied patch receipt, and fifteen payload members after its work: all seventeen inputs were unchanged. The supervising replay agent read the complete parser and inspected all fifteen compact comparison rows.

No `git apply`, isolated patch application, remote/current-tree mutation, reader build, browser inspection, or mathematical checker was performed by the patch audit. Byte reconstruction and comparison establish the requested payload equality without applying the patch anywhere.

The parser's original invocation is retained in `patch_audit/EXECUTION_PROVENANCE.json`: `python` followed by the absolute parser path, resolved at that time to the same miniconda Python executable. Its observed exit was zero and the execution tool reported 0.1464788 seconds. That tool supplied one combined output field, which is preserved in full; separate parser stdout/stderr and the parser's own interpreter-version string were not captured and are not asserted. This limitation does not affect the separately captured full stdout/stderr and exact runtime of all eight mathematical checker processes. The parser was not rerun merely to replace that historical receipt.

## Completed evidence and parent integration

The machine-readable execution entry point is `execution_receipt.json`. `code_audit.json` records the pre-execution inventory and negative-control distinction. `manifest_validation.json` and the two raw snapshots record exact member identity. `patch_audit/PATCH_AUDIT.json` records the independent add-only parser and all fifteen comparisons. All stdout/stderr files preserve complete outputs, with their actual argv and runtime pins in the execution receipt.

The finite replay and payload audit are complete. There is no failing positive method or mismatched payload. The supplied negative-launcher weakness and literal support assertion have been preserved and explicitly documented, while the separate six target-mutation executions supply substantive rejection evidence. Parent integration should retain that distinction and should not relabel predecessor sixteen-method executions, historical browser checks, or inherited analytic proofs as newly run here.
