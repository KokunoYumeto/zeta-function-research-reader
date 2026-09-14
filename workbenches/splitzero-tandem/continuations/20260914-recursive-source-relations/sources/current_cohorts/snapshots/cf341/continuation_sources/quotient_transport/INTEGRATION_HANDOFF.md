# Quotient transport: complete source proof handoff

## Main includable module

Include quotient_transport.tex after the original AT/AW definitions and CR7
(it repeats all local definitions needed for its new proofs).
It begins with a section, has no preamble, uses only amsmath, amssymb and
mathrsfs, and introduces QT.1 through QT.28 and unique qt-prefixed labels.

Final main-module SHA256:
DFB27E5CE1CA1F6822957294F85F04E4F21E78DDC2584355D0005BA356C926E9.

The new complete proofs give:

1. The exact, invertible, original-arithmetic-observation-preserving
   repair X=Q_F T+Pi, its attained minimum distance from the prescribed
   source isometry T, and its original energy and determinant.
2. The full original-G quotient action a=JTR of the nearest
   relation-preserving repair, retaining the exact Taylor unit.
3. The attained minimum window-intertwining defect over every map
   preserving the original observation; its positive original chi-moment
   floor. No invertible relation-preserving exact intertwiner exists.
4. The square-zero operator left by the exact repaired conjugation.
5. Its signed correction paired with the actual relation-valued
   minimum-lift derivative; an interval that can be intersected with AW.
6. The literal two-term cochain map and its explicitly computed
   homotopy to the identity, with supported fibres and external tau kept.

## Exact input sources

The paths below are relative to the workspace root, not downloads or
new substitute models.

- output/tau_split_zero_counterfactual_reconstruction_20260913/proof_inputs/AT.tex
  SHA256 9FA19A509EDF91F5AA0A9CB4762485449196D0B1FF521F2445F791FA3290CC75.
- output/tau_split_zero_counterfactual_reconstruction_20260913/proof_inputs/AW.tex
  SHA256 9D1470FEFF3F6482C890A760DA9F682B2944529DE2443E40E1BD417C4D8C7B83.
- output/tau_split_zero_counterfactual_reconstruction_20260913/tex/combined_restriction.tex
  SHA256 A7CE5FCC13BC554DDB3044B4EAF9F7EAF735E84DA0B7A8E7D7C9DB52D075C44A.
- output/tau_split_zero_counterfactual_reconstruction_20260913/original_programme/tex/gamma_endpoint_window_bridge.tex
  SHA256 400541CDCB35D44C0F7E68F5DB1107DF4FCF707D0BE83B5A8A970D8EC9C73160.

The last source already proves principal angles and nonlinear
all-dimensional endpoint bounds in EW.25--EW.35c. Those results are
not claimed as new work here.

## Validation

- Parent read every QT.1--QT.28 proof and accepted the algebra.
- Independent reviewer read every QT.1--QT.28 proof and found no error.
  A wording clarification about the real trace after QT.24 was applied.
- compile_check.tex: six-page draft-mode pdflatex compile; no warnings,
  overfull/underfull boxes, undefined controls, or unresolved references.
  No public PDF was produced.
- check_transport.py and checks.json: twelve finite polynomial-coordinate
  cases, including q=1 and repeated roots, all pass. Maximum residual is
  3.6503578134672255e-11. Those finitely supported positive test measures
  check algebra only; they are explicitly not arithmetic source replacements
  and do not certify any zeta zero.

## Final closest-unitary supplement

Include review/unitary_repair_coefficient_review.tex after the main module.
It begins with a section, has no preamble, and preserves all VR1--VR33
formulas and complete proofs. Its literal prose mathematics and all local
symbol definitions have been corrected and fully read in the final TeX.

Final supplement SHA256:
800935E3CB8B7AABF8B24DBA9FE249C4194CAAB5E86E7863220B8347EA6B9B25.

It gives the unique closest original-observation-preserving unitary
I_K plus polar(D), its exact attained costs, the positive triangular
quotient block forced by the actual AW phases, its determinant cost bound,
and the full coefficient-equivariance calculation retaining nilpotents
and the actual Taylor unit.

The supplement was independently authored and reviewed by the
review_transport_blocks agent. This agent and the coordinating parent
read and accepted its full mathematical proofs. The twelve independent
numerical checks also verify its closest-unitary costs, positive
determinant, prescribed triangular phases, and determinant cost bound.

combined_compile_check.tex includes both modules in order: eleven pages,
zero LaTeX warnings/errors, undefined controls/references, or
overfull/underfull boxes after the second draft-mode compile. No PDF
produced. All files are final and stable for inclusion.
