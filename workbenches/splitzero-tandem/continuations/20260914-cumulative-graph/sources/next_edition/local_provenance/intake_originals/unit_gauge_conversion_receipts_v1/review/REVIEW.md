# Independent acceptance of the complete UG source typing

Status: accepted. This review addresses source transcription and complete source transport. It does not repeat the accepted mathematical proof audit, execute algebra fixtures or Lean, or certify a PDF layout.

Both complete original sources were read before the proposed mappings. Every mathematical inline Code node was then compared individually with its surrounding source paragraphs and original formulas. The original arithmetic unit note has 62 Code nodes: all 60 mathematical nodes are typed, and the hash and relative source path remain literal. Its complete independent review has 59 Code nodes: all 55 mathematical nodes are typed, and four filename/hash literals remain literal. The note's 27 original display Math nodes remain unchanged in full, including all UG1–UG19 tags. The resulting 142 mathematical payloads appear in order at the exact verified UTF-8 spans of the generated TeX.

## Exact notation and domain checks

The distinct objects in UG2 retain their original notation and types: `upsilon_h` is typed as \(\upsilon_h\), the full jet-algebra unit, while `nu` is typed as \(\nu\), its degree-below-d Hermite polynomial representative. The special-fibre multiplier remains \(M_{\upsilon_h}\); the cochain gauge remains multiplication by \(\nu\) in the localized coefficientwise formal ring. The spelling `Bhat_nu` becomes \(\widehat B_\nu\), preserving UG4's coefficientwise denominator convention.

The ordered inverse remains \((I+HE)^{-1}H\), with \(D_M=M_h(I+HE)\). Neither operator order nor signs are changed. The gauge expression retains the term \(-u\nu'/\nu\). The inverse up to homotopy remains \(rM_{\nu^{-1}}\), and its conjugated homotopy remains \(M_\nu K M_{\nu^{-1}}\). The degree-one retraction referred to as `r1` is typed as the same \(r^1\) defined by UG10.

The reflected polynomial retains both conjugations and the factor \((-1)^d\). The historical review's arbitrary-packet first domain remains \(E_{h^\dagger}\), while the accepted note's reflection-stable packet restriction remains intact. The complete historical clarification and its final resolved acceptance are both retained.

The signed tensor homotopy keeps every preceding \(P_i\), subsequent identity, and Koszul sign in the source order. The review's `degree x` is typed as \(\deg x\), denoting its unchanged cochain degree. The note's rectangular truncation exponent remains \(n_i+1\); the review's separately written exponent remains \(n_i\). The complete tensor unit remains \(M_{\upsilon_h}^{\otimes k}\), and the map \([P]\mapsto P(\sum A_i)1\) retains its original sum expression. The residue-dual multiplier retains its inverse-transpose exponent \(-T\).

The controlling tau-base source defines \(\mathbf F_{1,\tau}=\{\tau,1\}\), its structural map \(\jmath_R\), and the right-adjoint object \(K_{\tau,r}(W)\). Accordingly `F_(1,tau)` and `K_(tau,k)(L_k)` are typed as \(\mathbf F_{1,\tau}\) and \(K_{\tau,k}(L_k)\). The ASCII parentheses delimit the subscript; the original strings and exact byte positions remain in the mapping ledger. These spellings name the same original base and right-adjoint object, with the structural map and support-preserving lift unchanged. The same delimiter interpretation yields \(M_{\upsilon_h}^{-T}\), \(p^{\pm A_h}\), and \(Q^{\otimes k}\) from the source's ASCII grouped exponents.

## Complete source preservation

The audit independently reconstructed each public source from its original bytes and declared edits, and independently applied the reverse byte edits to recover each entire original. Every undeclared byte is preserved. The only prose edits are one ownership reference in the note and five ownership/reporting references in the review. They retain every mathematical, verification, source and scope statement. No paragraph or heading is omitted. In particular the separate analytic continuation, the fact that fixtures were not rerun by the mathematical reviewer, the accepted original source hash, and the resolved final acceptance remain present.

Both original and public Markdown trees were reparsed independently with the exact Markdown reader configuration. Their complete literal-node sequence equals the original sequence with precisely the declared Code-to-Math substitutions. The original/public block counts and complete heading nodes are equal. The prepared AST and writer AST transformations were each independently reversed and compared against their entire input trees. Finally, all 142 emitted TeX mathematical payload spans were compared directly with their source Math payloads, including inline/display delimiters and source order.

The gauge TeX re-reader records an ordered Math comparison difference caused by its own LaTeX parsing representation. This review does not treat that re-reader result as literal equality. Acceptance rests on the independently verified exact original/public AST transport and emitted UTF-8 payload spans; the source mathematics has not been rewritten to force a secondary parser's representation.

The original two accepted source files remain byte-identical to their pre-conversion hashes. The exact machine-readable evidence, including every accepted Code mapping and final source/output pin, is in `INDEPENDENT_TYPING_ACCEPTANCE.json`. The read-only audit implementation is `check_complete_typing.py`; it writes only into this review directory.

## f1_unit_gauge pins

- original_source: 14920 bytes; SHA-256 `9ded2486160b76bf65f92d44b73cdd0c59a3ca7e5334f88682e10592d5a45b2f`.
- mapping: 20426 bytes; SHA-256 `54dafcbf70df6c5779cb94cec6975d72ea13f857bd648c2e57394eebfd7c7777`.
- public_source: 15174 bytes; SHA-256 `b0d60706b6250e4c8c0ede3db0b847852af20299076518ebd76bc43775ad3e9c`.
- converted_tex: 16432 bytes; SHA-256 `9a29d0a8f8b181be0ea8112cbf8eaaa9a9a52a5c42dff0c9dbf1541724a3e898`.
- wrapper: 648 bytes; SHA-256 `10e636835fc123ba294516f9c37b198c4ac93103916b0a07a1e0858fafdd76c9`.
- conversion_receipt: 261489 bytes; SHA-256 `92f3c627c2d0e23749f2d4f5143fc01a5334ac197277bb740e254b7b2f4e3142`.

## f1_unit_gauge_review pins

- original_source: 9691 bytes; SHA-256 `e32e978870e65ea375040762432a3cfe479068ebe6cfd800086a2d35d55da6d0`.
- mapping: 20098 bytes; SHA-256 `927f6021226041e53ba113935033f022ded6c56a20dd9871a80de416d97d25ca`.
- public_source: 9897 bytes; SHA-256 `5cc96c73e8fabda87d87a5a58184f059361a38210a9696cf498caba911423316`.
- converted_tex: 10832 bytes; SHA-256 `2ab0f77b6918b10dc2afdba0cdc5db2ef13b3626758d9c7e41e8c159202ec526`.
- wrapper: 665 bytes; SHA-256 `eb53ff9ad85e3dbcad2a1774bbc53807723092328ed4ce722cfd86f95c8130a8`.
- conversion_receipt: 148761 bytes; SHA-256 `30362e283c6272e5a43b9de9d18c203771e2d692bc43dd52b9a8a9d280b83685`.
