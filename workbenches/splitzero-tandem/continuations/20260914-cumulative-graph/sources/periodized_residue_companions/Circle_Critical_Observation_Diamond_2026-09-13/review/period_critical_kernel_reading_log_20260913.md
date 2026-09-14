# Period/critical-kernel bridge: complete source reading and derivation log

Date: 2026-09-13. Owner: the bounded independent Deligne/SGA bridge subtask.

## Task and actual scope

The parent requested an exact bridge from SC1–37 to the retained PR27 critical quotient, beginning with the literal single packet k=1 and then deriving the strongest exact tensor result. The prescribed objects were the original arithmetic unit and weighted section, the factorwise critical-jet maps, the completed projective target, and the period curvature of the resulting kernel. The deliverable was the complete PC proof plus a standalone XD+SC+PC PDF, with the complete H1–42 analytic comparison note retained beside it. This local task performed no remote operation, global-paper edit, Lean execution, or numerical test.

## Completed readings and their scope

1. Read all SC1–37 in `work/sga_constituent_period_curvature_20260913.tex`, including full period determinant, invariant ideal, normal acceleration, Gram differentiation, dual orientation, moving metric, collision Tor, and adjacent-minor proofs.
2. Read all of the owner's `pr27_review/hochschild/USER_SOURCE_COMPARISON.md` and `MATH_REVIEW.md`, then every line of the retained 430-line `HOCHSCHILD_COMPARISON.md` H1–42. The retained note is at immutable PR27 revision a4a87844c257485ae6d669f5b3eb6d96b9e8b8d8 and has SHA256 0f5707281ee46ec411b1af5d25361cf23bb88c3689a0f3cd75f7fac5b951be13. Its complete copy is included in this companion.
3. Read the complete relevant original-source arguments A5–A13 in `arithmetic_input.tex`, including the theta primitive, jet section, actual strong-Schwartz domains, Euler inverse and cohomological source. Read the full unit and original-Gram proofs CT.1–CT.5 in `coherent_tensor_integration.tex`, and the full arithmetic unit/source and sum-polynomial arguments TVB.1–TVB.3 in `toda_cv_exact_bridge.tex`. The entire three source files are retained as dependencies rather than excerpted.
4. Read the original cyclic-sum definition and entire tuple nilpotence/minimal-polynomial proof in `work/20260913-toda-portable-3qilsrsz/package/build/source_cyclic_sum.tex`, covering the initial source construction through the relevant proof. The new PC text rederives that exact polynomial, including all equal-sum multiplicities.
5. The previously accepted XD1–26 proof is included unchanged. This subtask reread its introductory setup while matching SC constants; the full XD mathematical review and full prior XD/SC PDF review are inherited with their exact scope, not represented as a fresh complete XD reading here.

## Derivation and corrected exact types

PC1–PC8 prove chi_(h,1)=h by the literal variable isomorphism, recursively compute every inverse arithmetic-unit coefficient, and identify the retained polynomial source with the specific theta section by an explicit theta primitive. The descended map bar-J_h:Q→E_h is kept distinct from J_h:B→E_h. The source section intertwining follows from its polynomial relation and the surjectivity of eta_h.

PC9–PC15 prove the complete critical kernel and an explicit continuous retraction. The full phase i^(-j)/j! and local unit product survive derivative evaluation. The inverse unit is transported through iota_1^(-1) into the actual CRT ideal, whose identity is e_c=pi_c(e_0). The critical image is recovered with that exact identity, including empty-sector endpoints.

PC16–PC27 transport this kernel through the full period matrix. The rank-one defect is computed before restriction. The ideal basis proves the exact image, kernel and rank of the restricted defect. Direct Gram differentiation supplies the curvature and its order of vanishing, with both Wirtinger factors and the dual Chern orientation. The moving original-theta metric is connected by its full derivative cancellation.

PC28–PC41 prove the completed tensor comparison using the concrete factorwise continuous retraction. Root and the independent unit reviewer found the tensor carrier mismatch in the initial draft; the final text inserts iota_k:E^(tensor k)→E_h^(tensor k) and bar-alpha_k=iota_k^(-1)alpha_k. The original weighted map remains eta_k=eta_h^(tensor k)bar-alpha_k. The critical ideal's own identity is retained in alpha_(c,k). The full kernel is (chi_(c,k))/(chi_(h,k)), with the exact local injection x^r a_lambda(x) from C[x]/x^(m-r) into C[x]/x^m. This includes coincident critical and mixed sums and excess nilpotent jets. The original sum action and the full period curvature are then proved for that literal ideal, with all original theta masses and all empty/full endpoints.

## Independent mathematical closure

Root read the entire PC1–41 source and complete corrections, saving `period_critical_kernel_root_review_20260913.md`. The separately delegated arithmetic-unit reviewer read the entire initial proof, the entire corrected proof, and the last descended-map correction, saving `period_critical_kernel_unit_review_20260913.md`. Both accepted the mathematics. The precise accepted mathematical-source SHA256 is 93a9d828e86608699b83cf331f77f77ae5062505293f6f7e30e69db77af4c5f9.

The final source SHA256 is 7a7733e0d6910398b6de716604a82ef5287a55002e1874327490a70ccc3dd414. Its only subsequent changes are the two line-broken displays PC4/PC40 and the amsmath stack in PC30. The executable inverse delta reconstructs the exact accepted-source hash. No formula, hypothesis, proof statement, or map has otherwise changed; `review/LAYOUT_ONLY_DELTA.json` records this comparison.

## Actual PDF work and visual closure

The first build produced two overfull displays and an amsmath atop warning. Those three issues were repaired by the layout-only changes just described. The final wrapper was compiled twice with pdflatex, both actual commands returned zero, and the final log contains no overfull/underfull boxes, undefined references or controls, missing glyphs, or warnings. All 18 pages were rendered at 100 dpi with pdftoppm. Final rendered pages 11–18 were individually displayed and visually inspected: no clipping, overlap, missing symbols, or off-page formula tags remain. The eight new pages contain the entire PC proof, ending with the two endpoint cases and original supported Split-Zero maps.

Final pages 1–10 are both byte-identical PNG files and pixel-identical images to the prior completely viewed XD/SC edition. Their earlier visual receipt is retained verbatim; the present check reuses that precisely established identical material. No fresh inspection is claimed for those ten pages. The final visual receipt pins all 18 images, the PDF, source, and exact build evidence.

## Deliverables

`output/Period_Critical_Kernel_Bridge_2026-09-13/` contains the readable PDF, editable master, three complete proof bodies, five complete adjacent proof-dependency files, both PC mathematical reviews, the prior SC mathematical and visual reviews, this log, exact source provenance, and actual build/render evidence. The sibling final manifest inventories those files. The LC continuation remains separately owned and can be integrated by the parent without delaying the now-complete PC companion.
