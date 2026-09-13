# Failure review: proof, execution and source delivery are separate

This is the review for the recovery branch. It preserves the prior `tau-mixed-metric-integration/FAILURE_REVIEW.md` and its attributed history rather than rewriting that report.

## Three available historical failed runs

The user did not supply three exact UI trace IDs. The following are the three relevant recorded jobs recovered from the unfinished contribution; they are not asserted to be every possible failed session trace.

1. Run 34775074985, job 103771596758, commit 12a830194a4bc164e13f80a5222f686b2f667447: repository checkout, toolchain, and inherited closure/audit succeeded. The new resolvent proof used the deprecated `Matrix.mul_eq_one_comm`, needed explicit rearrangement of its secant identity, and an explicit metric parameter in a section-update rewrite. The recovered source repairs these with `mul_eq_one_comm`, an additive calculation, and specified parameters.
2. Run 34775645022, job 103773145903, commit bfe017b6e48cd0c9e8828f3ed9e5e5244016a172: the matrix proofs passed; the support interface was stopped by an unused `Fintype n` binder under warning-as-error. The recovered `omit [Fintype n] in` removes the unnecessary instance, not the conclusion or a necessary hypothesis.
3. Run 34777844699, job 103779125333, commit fb60c6694093ee41648cf31d4be75bb69c145770: the complete original closure and 60-target audit, and three resolvent modules with their 24-target audit, passed. The new source-sandwich file used the ambiguous identifier `gram` after opening both Matrix and MetricVariation. This recovery uses `MetricVariation.gram` explicitly. The old finite job succeeded.

The complete latest historical log and each new recovery failure log were read directly. The first two earlier diagnoses are retained from the recovered failure report and their repaired proofs were independently replayed in the new workflow. These are proof-script/API failures after successful syncing, not arithmetic counterexamples and not evidence that mixed support is inconsistent.

## New development history retained

Run 34785405481 at 099c21b... passed the repaired MetricSandwich and SourceProjectorContrast files. MixedSupportMetric then exposed (i) reversed finite double-sum order after Gram expansion and (ii) matrix-entry evaluation in a sum. The repairs are `Finset.sum_comm` and explicit `Matrix.sum_apply`/`Finset.sum_apply`. All off-diagonal terms stay. The finite job passed.

Run 34786149476 at f04110c... exposed definitional coercion differences between the quotient constructor and its linear `mkQ` map in the newly added BoundarySocle proof, plus a scalar-map reduction and explicitly unused lambda binder names. The repair makes the definitional changes explicit and retains the injectivity assumptions on the prequotient. No cancellation is asserted on the torsion quotient.

Run 34786546190 at eb3e6b3... strictly compiled BoundarySocle. Its support file then left one reflexive equality of same-label zero elements; `rfl` closes that exact remaining goal. The finite job passed. Subsequent observed final verification, if successful, is recorded in STATUS.md; no future run is predicted here.

The false-zero Lean control must fail at e=tau itself, not at imports or instance synthesis. All source checks keep `--trust=0 -DwarningAsError=true`; no lint or axiom check is disabled.

## A distinct real source-delivery defect

Both delivered ZIPs extract safely. The Mixed Boundary archive has 86 manifest entries and the Marked Product archive 28; all match their stated hashes. Yet Mixed Boundary NEW_BODY.tex and CONTINUATION.tex jump inside a proof from MB19 to an Airy display labelled MB45, then into the finite-field proof. Definitions/proofs MB20--MB44 and MB46--MB47 are absent. The cumulative entry includes NEW_BODY.tex and therefore does not repair the missing body. The exact hashes and local replay results are in INTAKE.json.

This is a content-completeness problem despite correct byte hashes. It does not invalidate the formulas in the separate markdown or the portions whose proofs remain. The original archives are not edited or blindly patched into main. RESEARCH_NOTE.md reconstructs the needed lattice, v-socle and action argument as an independent proof with explicit scope.

A source-level type clarification is also retained: for O=C[a][[v]], the v-kernel is free of rank m over C[a]; it is the family C[a] tensor E_rho, not an m-dimensional C-space until a is specialized. The quoted length similarly means rank of the finite C[a]-module (or its v-adic graded length over C[a]), not finite composition length over the unspecialized two-dimensional ring.

## Local execution

Unlike earlier sessions, archive extraction and exact SymPy execution worked in this turn. An initial 45-second invocation of the supplied main checker exceeded that tool timeout. Its full independent replay with a per-script 360-second limit completed, in both Python modes. That timeout is not a failed mathematical test. One update_ref tool attempt used the wrong schema key and was rejected before changing a ref; the corrected call uses branch_name. Neither event is hidden as a mathematical repair.
