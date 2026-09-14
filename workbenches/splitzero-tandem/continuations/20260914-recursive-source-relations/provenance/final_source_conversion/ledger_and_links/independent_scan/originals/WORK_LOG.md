# Independent ledger Markdown audit

## Scope and instructions

Read-only audit assigned by the ledger conversion scan parent: read the frozen ledger sources manifest, every packaged Markdown source and its referenced original; enumerate literal `^[` and footnote markers, classify exponent versus genuine note intent, and inspect the converter mechanism. No active source edits and no PDF build. All audit outputs are confined to this directory.

## Provenance

Existing task provenance located at `work/backpropagation_20260913/USER_DIRECTION_AND_OWNERSHIP.md`, with cumulative workflow history in `work/backpropagation_20260913/BUILD_LOG.md`. Parent has been asked for the complete established user transcript path; this subtask will link it rather than construct an incomplete replacement from inherited context.

Parent supplied the current scan task's extracted user-role provenance at `../USER_INPUTS_VERBATIM.md`. It is shared provenance for this bounded audit; the root logs above preserve the broader outcome context.

## Work performed

- Read the 12-entry frozen `sources_manifest.json` and `build_ledger.py` and `layout.lua`.
- Converter passes `--from=markdown+tex_math_single_backslash` to Pandoc. Lua filters transform `Str`, `Code`, and display `Math` after Markdown parsing; they do not intercept a `Note` node.
- An initial discovery command and a later unfiltered parent graph JSON print returned truncated output. No final finding depends on either truncated display. Final enumeration reads precisely the 24 manifest paths; the parent graph is parsed and filtered programmatically.
- All 24 source files exist and exactly match their manifest SHA-256 and byte counts. The first scan wrote a complete JSON receipt but terminal printing failed on a Unicode glyph; stdout encoding was corrected and the same read-only audit rerun.

## Remaining

None within the assigned Markdown/converter audit. Parent owns applying and verifying active source changes.

## Completed findings and evidence

- `SOURCE_SCAN.json` records all 24 sources, exact manifest hashes/bytes, and every literal `^[`, `[^`, TeX footnote command, and HTML footnote semantic marker. All files exist; all hashes and byte counts match. There are two `^[` occurrences per packaged/original corpus and no other source footnote markers.
- Both candidates are the exponent `[K:Q]` attached to base `2` in `formation.md:277` (columns 118 and 172), copied exactly in the original `AUDIT.md`. They are mathematical field-degree exponents. No genuine footnote was found.
- `PARSER_PROBE.json` contains actual non-building Pandoc AST probes for all 12 packaged sources. They reproduce two false Note nodes, fifteen false Superscript nodes, and two false Links targeting `k+1`. Every selected node has its exact source occurrence.
- The parent expanded this bounded audit to source mappings and proposals for the fifteen superscripts and two formula links. `CLASSIFICATION_AND_PROPOSALS.json` and `.md` contain all seventeen source-faithful inline-math proposals, old TeX snippets, exact source lines and checksums. No proposal has been applied by this audit.
- Every full old formula generated with the frozen Lua filter matches the frozen ledger TeX. Two repeated C_q identities have their two distinct source occurrences recorded. Every proposed formula parses as exactly one InlineMath node.
- Original inverse exponent parentheses, brackets, both `(k+1)` factors, operator words, signs, constants, and coordinate letters are preserved. The shorthand `L2` is kept literally as `\\mathrm{L2}`; the transcript's more explicit `L^2` is documented separately rather than silently substituted.
- A child performs a bounded transcript witness lookup in `transcript_witnesses/`. Transcript variants do not override the audited ledger's exact original source.
- No active source edits, converter rebuilds, TeX compilation, or PDF build were performed.
