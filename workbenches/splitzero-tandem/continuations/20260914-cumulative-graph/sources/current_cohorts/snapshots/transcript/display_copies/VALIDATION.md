# Complete audit single-file validation

`COMPLETE_AUDIT.tex` is a self-contained LuaLaTeX source with one document class and one document environment. It includes the complete frozen ledger and every one of the 13 frozen proof chapters. No external content inputs remain.

- Output: 702,103 bytes; SHA-256 `be9394c8e738a8a5c16de73134a264d949e1273fc7d8d304e036f99e4f8da34f`.
- Frozen ledger document body: byte-for-byte identical.
- All 13 proof fragments: byte-for-byte identical, in the original order and groups.
- Original proof main document body: exactly recovered by replacing the marked inline expansions with their original input commands.
- All 15 frozen source file hashes: unchanged after final compilation.
- LuaLaTeX: two successful passes, exit code 0; no unresolved references, duplicate labels/destinations, missing glyph reports, or requested rerun.
- Validation output: 208 pages. The display copy has a combined contents list at both retained original contents calls, so its pagination differs from the frozen 206-page package. The mathematical bodies are unchanged.

The merged preamble and scoped fonts, margins, text sizes, counters, headings and hyperlinks are the only layout changes. Detailed original source hashes and exact-retention assertions are in `BODY_RETENTION_REPORT.json`; compilation details are in `COMPILE_VALIDATION.json`. The PDF in `build` is solely a local compilation artifact, not a requested delivery.
