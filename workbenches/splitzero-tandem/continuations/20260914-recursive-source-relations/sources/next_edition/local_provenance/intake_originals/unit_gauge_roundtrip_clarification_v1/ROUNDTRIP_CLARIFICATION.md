# Exact UG LaTeX re-reader clarification

The existing `latex_roundtrip_ordered_math_c_equal=false` flag is correct and remains unchanged. A fresh, read-only Pandoc LaTeX parse of the exact sealed generated TeX reproduces the complete sealed re-reader AST.

There are exactly 27 differing mathematical payloads, all the gauge note's original displays. For every one, the exact byte equation is:

`source payload = 0x0A || re-reader payload || 0x0A`.

Each source display has precisely one leading LF and one trailing LF that the LaTeX re-reader omits from its parsed payload. Every intervening byte is identical, including all interior whitespace, commands, signs, indices and tags. The mathematical node type and order are identical. No trimming or other transformation was applied to the source or generated TeX to establish this equation.

All 60 gauge inline mathematical payloads are exactly equal in the two ASTs. All 55 inline mathematical payloads of the complete independent review are also exactly equal, and that review's equality flag remains true. Thus the only discrepancy across the 142 mathematical payloads is the 54 boundary LF bytes absent from the secondary parser's 27 display payloads.

The generated TeX retains the complete original display payloads, including both boundary LF bytes. Each of its 142 recorded literal-emission spans was checked directly against the source AST payload and its inline/display delimiters. The JSON records every differing pair in full, its exact source and re-reader AST paths, source tags, payload hashes, and actual emitted TeX byte offsets.

The complete original/public source-and-prose byte inverse was rechecked for both sources. Both complete prepared-AST and writer-AST inverses were rechecked. Every original source, mapping, public source, generated TeX, wrapper and conversion receipt still matches the exact pins in the accepted full typing review. All pre-existing files in this conversion directory were hashed before and after the read-only checks and remained unchanged, including the existing reviews and final manifest.

This clarification adds evidence for the exact secondary-parser difference. It changes neither the accepted mathematical source nor the generated TeX, and does not assert exact equality of the differing re-reader payload arrays. No proof audit, fixture execution, Lean run, or PDF layout claim is added.

Accepted full typing review SHA-256: `79fdf2ad0bc20cb571fcdfc810042020b05b010285a2beb0f268b5e3d1879595`.

Exact clarification JSON SHA-256: `32d5372cf2c984bd70d02257da3cfbc7a7167af51a22421ac44e40dacf0044da`.
