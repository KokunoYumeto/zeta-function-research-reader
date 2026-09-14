# Final macro and alphabet preservation refresh

The concrete M1 notation defect in the initial edition is repaired in the final PDF. The script theta target and calligraphic scalar correction now use distinct embedded fonts and visibly distinct glyphs. All 11 actual copied custom declarations still match exactly; all three source hashes and all three fragment hashes agree with the refreshed BUILD_MANIFEST. No unresolved macro, environment, mathematical alphabet or existing internal-reference defect remains in the bounded proof03/proof12/proof13 review.

## Exact final edition

- PDF: `output/tau_f1_transcript_audit_2026-09-13/publication/actual-cohomology-proofs.pdf`
- PDF SHA256: `c42419d417ba87b0d6e3945d2664d96efa245c1136aae4f1cf992165a0e5a42a`
- PDF bytes/pages: 719145 bytes; 98 pages.
- Main TeX SHA256: `28107060f72d6f5075327ecedf621547cbac59a4fcf00734de53f1368e5bcd83`
- Builder SHA256: `d61e812d1bfe3105ffc4cc89c853f5445b45216759b2360e37babebd9a2b47df`

The publication owner changed the common load order to `unicode-math`, `\setmathfont{Latin Modern Math}`, then `mathrsfs` (main TeX lines 8–10). Therefore the final `mathrsfs` declaration installs the separate RSFS alphabet for `\mathscr` after Unicode setup. The calligraphic alphabet remains in Latin Modern Math. The three source files and their proof-body tokens were not rewritten for this correction.

## Actual chapter 13 glyph instances

This check directly inspected the final PDF identified above, using both PyMuPDF spans and pypdf text/font callbacks. It also viewed the owner's already rendered full pages 94 and 95 at 100 dpi. No new render or PDF was created in this lane.

| Actual occurrence | PDF page / printed page | Font resource and PDF object | Embedded font |
|---|---|---|---|
| `\mathscr B` in `Q=\mathscr B/\Theta V`, and the original two-term complex | 94 / 93 | `/F76`, object 149 | `/PPWDFG+rsfs10`, Type1, embedded |
| `\mathcal B(t)` in AW5 and the correction in AW6 | 95 / 94 | `/F48`, object 49 | `/WUOQUE+LatinModernMath-Regular`, Type0, embedded |

For the first target the span box in PDF points is `(229.528, 458.475, 242.658, 469.384)`; the second target in the complex occupies `(147.190, 494.388, 157.095, 505.297)`. The scalar correction's span is `(210.183, 102.672, 242.605, 113.581)` on page 95. Every displayed example uses a 10.90909-point font. The two script-space occurrences are visibly the more elaborate RSFS B; the scalar correction is the distinct calligraphic B. Neither example is clipped or overlapped.

The RSFS resource lacks `/ToUnicode`, so both text extractors return the Latin fallback `B` for that font's B glyph. The Latin Modern Math resource has `/ToUnicode` and returns U+212C `ℬ` for the scalar correction. Thus decoded text alone is not the preservation test: the exact font objects, embedded font programs, span locations and inspected existing renderings establish the repair. A fallback extraction of plain `B` must not be interpreted as the PDF having silently changed `\mathscr B` into ordinary mathematical italic B.

Viewed render hashes:

- `page-94.png`: `c37ef037c9760858731a16175c66f3ae2dedadbb76d31f59859923803ef45fda`
- `page-95.png`: `88a7ad1db8072f54fbd7bbde8f92a260333c526356a1f516d90e0ae0423a0a4d`

Both are in `work/tau_f1_transcript_audit_20260913/publication/renders/c42419d417ba` and are preserved by the publication owner. This targeted inspection does not claim full 98-page visual QA, which belongs to the other review lanes.

## Remaining scope observations

The original theorem declarations remain equivalent environments with changed numbering: 1 and 2 become 12.1/12.2 or 13.1/13.2. Refreshed extracted-text lines 4568, 4745, 4892 and 4970 confirm those exact headings. The source12/source13 section numbers 1–5 remain suppressed. Their bodies contain no reference depending on the old theorem or section numbers. Chapter03's literal Section 5/Section 6 and A.1–A.4 headings are retained. These observations are real presentation changes, not unresolved reference errors.

Source12's original standalone preamble still omits its `\mathscr` dependency. The final common setup supplies the intended script alphabet. This pre-existing standalone source issue was never an extraction omission and is outside the read-only publication preservation check.

The parser controls documented in `MACRO_REVIEW.md` still describe limitations for unbraced command names, brace-bearing optional defaults, TeX comments and conditional definitions. Those shapes are absent from the three actual sources. The parser's support for ordinary braced stars and simple optional defaults was demonstrated; those hypothetical limits do not imply a missing actual declaration.

## Separate receipts retained

- Initial finding and source pins remain in `MACRO_REVIEW.md` and `MACRO_RECEIPT.json`. The latter is unchanged, SHA256 `31c6e0fbe53962e0fb54ab777443ebb3ca71af8802b335189b70428725963451`.
- Repaired macro/preamble/source/fragment receipt: `MACRO_RECEIPT_REPAIRED.json`, SHA256 `d3803b7cd22d1a10377f30ee22366c3e2c56f761be2d7a58d3d23ecf36e7327d`.
- Final exact PDF/font/span/render receipt: `FINAL_FONT_RECEIPT.json`, SHA256 `866f0b29bb119a4742630d3b0cda3aff4ed1b8b4c5b78828d670eeff439985f8`.
- Independent original theorem/reference scope review: `theorem_scope/REPORT.md`, SHA256 `e0cd3f07b5e787f04ca42a382fb408ac0db7aa24fbd82999d0107cc58a2e80bb`.

The refresh used the PDF skill in read-only mode; no artifact authoring marker applies. Two local receipt-script issues (an argument-name collision and console encoding) were repaired only inside this owned directory before the successful final runs. No originals, publication files, remote state, TeX builds or Lean sessions were changed by this lane.
