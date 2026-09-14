# Publication content integrity

The thirteen assembled chapter bodies pass the independent content-retention check: **90,943 non-layout tokens and 256 explicit equation tags**, with complete paragraph and formula order preserved. No mathematical term, sign, constant, index, original alphabet command, displayed-equation body, or proof paragraph was dropped by the assembly transformations inspected here. This statement concerns retention of the selected complete sources; it does not certify the mathematical correctness of every source claim.

**PASS for the final repaired edition.** The review identified an actual loss of a source notation distinction in the initially inspected PDF. The publication owner repaired the shared font setup, and independent inspection of the final PDF confirms that the source's distinct script and calligraphic alphabets are restored. The final PDF is **98 pages, 719,145 bytes**, SHA256 `c42419d417ba87b0d6e3945d2664d96efa245c1136aae4f1cf992165a0e5a42a`.

## Independent method

`verify_integrity.py` reads the selected original sources and their assembled copies. It neither imports nor runs the publication builder and writes only inside this review directory. Each run saves the complete inspected sources, copied fragments, builder and manifests under a timestamped `snapshots/` directory. `INTEGRITY_RECEIPT.json` identifies those snapshots and pins every input hash.

1. Check each selected source and copy against the build manifest's SHA256 and check independently reconstructed pre-layout bodies against their recorded SHA256.
2. For the three standalone sources, extract the entire document body; retain every actual custom macro declaration; remove only the recorded presentation commands `\maketitle` and `\tableofcontents`. The remaining eleven declarations are checked separately below. Chapter wrappers and the shared table of contents replace the removed document presentation.
3. Undo the recorded injective label namespace and exact text-layout changes. Compare every remaining token in order. The tokenizer retains TeX control-word boundaries, prose word boundaries, grouping, signs, constants, indices, alphabet commands and comments. It ignores whitespace layout and recognizes only the explicit single-letter script grouping needed by the Unicode engine. It does not expand, simplify or substitute mathematical expressions.
4. Separately bind every explicit `\tag` to the complete unchanged outer display in which it occurs, preserving both tag multiplicity and order. This guards against a verifier that would merely erase tags and overlook an incorrect reference assignment.
5. Verify the explicit multiline force-equation patch independently: deleting only the added `aligned` wrapper, alignment markers, line breaks and spacing leaves **the same 89 mathematical tokens** on both sides.
6. For the two original Markdown chapters, compare every prose, code and full math atom after an independent Pandoc Markdown/LaTeX semantic roundtrip. Chapter 10 retains **1,459 atoms, including 105 full mathematical expressions**. Chapter 11 retains **357 atoms, including 38 full mathematical expressions**. Both ordered atom sequences agree exactly.
7. Check upstream provenance: eleven selected source files equal their current original files byte for byte. Chapters 2 and 4 were produced directly as output fragments; each matches the complete document-body tokens of its retained standalone TeX.

The check is stronger than merely replaying the builder, comparing source length, or counting equations. Sixteen substantive mutation controls all fail as intended: omission of a content token from each of thirteen chapters, reversal of the AT9 second-variation sign, interchange of tags AT8 and AT9 between their displays while retaining all formula bodies and the complete tag multiset, and replacement of the original theta-target `\mathscr B` by `\mathcal B`.

## Standalone extraction and actual notation finding

All **eight** custom commands in chapter 12 and **three** in chapter 13 survive exactly, including their replacement text. Chapter 3's `\tightlist` is supplied by the common preamble with equivalent behavior. The original theorem/proof bodies remain complete. The shared report class renumbers the two theorems of each final chapter as 12.1/12.2 and 13.1/13.2. No body contains an old numeric theorem/section reference broken by that presentation change. Chapter 3's literal Section 5/6 references still refer to manually numbered headings.

The builder's simple macro parser is not safe for arbitrary future preambles: synthetic braced optional defaults, unbraced declaration names and commented declarations expose limitations. Those forms do not occur among these actual declarations, so they did not cause a missing command here. The independent parser and exact declaration comparison avoid relying on the builder's parser for this conclusion.

**Concrete notation defect found:** the initial common preamble loaded `mathrsfs` before `unicode-math`. In chapter 13, the original theta-target notation `\mathscr B` and the different correction scalar `\mathcal B(t)` were consequently rendered as the same U+212C glyph. The initially extracted PDF text exhibits both as `ℬ`; the installed Unicode-math implementation aliases its default calligraphic and script alphabets. This is a rendered loss of a source distinction despite exact retention of the two different TeX commands. It is not a dropped proof or an algebraic identity between those objects.

The publication owner changed the common preamble to load `mathrsfs` after `unicode-math` and `\setmathfont`, restoring the separate original script alphabet. This review edits no publication or source file. The initial defect report and its inspected hashes remain in `macro_review/MACRO_REVIEW.md` and `macro_review/MACRO_RECEIPT.json`.

**Verified final repair:** on PDF page 94 (printed page 93), the theta-target B uses resource `/F76`, object 149, embedded Type1 font `/PPWDFG+rsfs10`. On PDF page 95 (printed page 94), the scalar correction B(t) uses resource `/F48`, object 49, embedded Type0 font `/WUOQUE+LatinModernMath-Regular`. Independent pypdf visitor and PyMuPDF span checks agree; the reviewer also viewed both existing 100 dpi page renders and confirmed visibly distinct forms. The RSFS font lacks a ToUnicode map and extracts a fallback Latin B, whereas the scalar extracts U+212C. Actual font resources, rather than extraction text alone, establish the repaired distinction. `macro_review/FINAL_FONT_RECEIPT.json`, SHA256 `866f0b29bb119a4742630d3b0cda3aff4ed1b8b4c5b78828d670eeff439985f8`, pins this evidence to the final PDF hash above.

## Equation tags and layout

Tags **AT8, AT9 and AT13** moved from inside their respective `split` environments to immediately after the same environment, still inside the same `\[ ... \]` display. Each tag's text is unchanged. Each full outer display has the identical ordered mathematical tokens after removal of the tag itself, and the three tags remain attached to the same first-variation, second-variation and window-projection formulas. All other explicit tags likewise retain their original contents and display binding.

The source-cutoff force equation remains complete: its left-hand side, both forcing/nonlinear terms, and the entire time-dependent dilation term survive with their original signs, viscosity, factors, arguments and variables. Only its line arrangement changes.

## Exact selected final source hashes

The machine receipt additionally pins every copied fragment and upstream proof file.

| Chapter | Selected source SHA256 |
|---|---|
| 01 | `6cce50f9097894769d69766c496e16c892d7a739fdb2df99e4aa20146cac05c4` |
| 02 | `73878f1aa0fd9cf59c3fbfc9479a577ad550a5385841668b54e14943fff02e94` |
| 03 | `9663dfe2b582764fb556873f0067ebdef26126669c91296c747ed8d79ce99028` |
| 04 | `44f5c9f391ad2edb9ac4992a08441b02d145c4fe259abfc5bc1a81bd2988d100` |
| 05 | `dc5845532e91edbff0ccc304db6a0d7d48b9e0a2574d02532ef58d5836441461` |
| 06 | `53678f46692e67d89f567676fa4eea76c11e17bce871989c8e9aa53f0bc9813f` |
| 07 | `9b296052c7bd9c17f1f158658fa5022d4efd47678a538aea5673c5f9e980010f` |
| 08 | `cf44640ec6e5b685a6a2afbf7db77a6118561479725260f0b32e212fbf0c4fe6` |
| 09 | `02880e71295c6f98f7e525c0dd474f509b02342521fbe579c505c6c0e04c8328` |
| 10 | `26f0afe272e44adf7e2c6d8bdf11300ce0315d0885e0f0859a4dada9909db28a` |
| 11 | `06feed8c3d8dce8155056c0ba4d41169886e6782ace17f021458d0f1e07081e3` |
| 12 | `24cf7ce5be6a43cc656641b516185df10b2e4d7824600ece657120d1c549deae` |
| 13 | `c79e76c087efd59871e3234ff44fb18964515dbd34f0318dffba6b3f1440f6ec` |

The review performs no PDF authoring, publication, remote operation, shared-master modification, or Lean run. Full-page visual quality assurance remains with the publication owner.

## Final retention receipt

`INTEGRITY_RECEIPT.json`, SHA256 `6d07e1ca150c799c5d205974df99d08d851e436fa6b049cdbc55a3edb6759a29`, pins the final PDF above, common TeX SHA256 `28107060f72d6f5075327ecedf621547cbac59a4fcf00734de53f1368e5bcd83`, builder SHA256 `d61e812d1bfe3105ffc4cc89c853f5445b45216759b2360e37babebd9a2b47df`, and the exact 13-chapter build manifest SHA256 `0dcecdb545f1406b26f3dffe24c7ab3d1bae95678511e632d007f37d7720bcb1`. The complete inspected byte snapshot is `snapshots/20260913T160200Z/`.

No unresolved source-retention or actual macro-preservation defect remains in this pinned edition. The previously identified font collision is repaired and independently verified. Future unsupported macro-parser inputs and the source12 standalone package omission retain the narrow scopes recorded above; neither caused dropped content in this volume.
