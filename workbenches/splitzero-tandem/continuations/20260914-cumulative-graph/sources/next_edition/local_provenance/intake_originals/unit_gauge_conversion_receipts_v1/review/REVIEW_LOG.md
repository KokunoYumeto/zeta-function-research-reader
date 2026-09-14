# Independent UG typing review

Task: review the accepted original UG note and complete independent mathematical review as typed source conversions; preserve all original math and paragraphs except explicitly identified internal ownership prose. Do not edit originals, run fixtures, or run Lean. Parent owns source conversion.

Read both complete accepted original sources. Parsed all original nodes independently with Pandoc markdown+tex_math_single_backslash+tex_math_dollars. Recorded original ASTs and full Code/Math inventories. Awaiting proposed typing mappings.

## Independent typing decisions before inspecting the proposed mappings

- The gauge note has 62 original inline Code nodes, of which 60 are mathematical; its two nonmathematical literals are the preceding tau-source SHA-256 and `tex/arithmetic_input.tex`. It has 27 original display Math nodes, with exactly UG1 through UG19 as its explicit tags. It has no raw nodes or fenced code blocks.
- The complete review has 59 original Code nodes, of which 55 are mathematical. Its four nonmathematical literals are two occurrences of the accepted gauge filename, one relative source filename, and the accepted gauge hash. It has no original Math, raw nodes, or fenced code blocks.
- The full Taylor jet unit is upsilon_h and the polynomial representative is nu. UG2 fixes their distinct types and forbids conflating them in source transcription. The target special-fibre multiplier is M_{upsilon_h}; the localized cochain multiplier is nu.
- Preserve the operator factorization D_M=M_h(I+HE), inverse (I+HE)^{-1}H, minus derivative term in the gauge, and ordered inverse-homotopy conjugation M_nu K M_{nu^{-1}}.
- In the tensor signs degree x means |x|, with the signed tensor convention explicitly given. Preserve the root note truncation exponent n_i+1 and the independent review exponent n_i separately; they are different original presentations and neither should be altered to match the other.
- The original tau-base NOTE.md, SHA d03e71ad18f187bd89880cb8ca6fc9c5d6f260b3de8e8e5702c27db97e7b63c3, defines \mathbf F_{1,\tau} (line 18), the structural map from this exact base (line 33), and K_{\tau,r}(W) (line 530). The source shorthand F_(1,tau) should therefore be typed as \mathbf F_{1,\tau}, and K_(tau,k)(L_k) as K_{\tau,k}(L_k); parentheses delimit ASCII subscripts. No object replacement is involved.
- The review's arbitrary-packet reflected polynomial must retain both conjugations, the sign (-1)^d, and first domain E_{h^dagger}. The note itself retains the reflection-stable restriction, and the historical review plus its final acceptance remain complete.

Final acceptance: all 115 inline mathematical Code conversions, 27 unchanged original display formulas, 142 complete emitted mathematical payload spans, complete original/public byte inverse, all headings and blocks, and both complete adapter AST inverses independently checked. Six precisely identified ownership wording edits retained all surrounding source and scope text. Acceptance JSON SHA 79fdf2ad0bc20cb571fcdfc810042020b05b010285a2beb0f268b5e3d1879595. No source, checker, fixture, Lean, or PDF mutation/run in this review.
