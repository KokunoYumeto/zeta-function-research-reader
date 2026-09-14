# Complete passage-ledger volume

`ledger.pdf` is the readable 108-page passage-ledger volume. `ledger.tex` is its editable LaTeX source, and `ledger.md` is the complete assembled Markdown. This is the ledger volume for combination with the separate complete proof volume.

All twelve source snapshots are retained under `sources/`, with their original repository-relative paths and SHA-256 hashes in `sources_manifest.json`. They comprise the overview, acquisition coverage, five segment ledgers, three complete early passage appendices, the final supplementary continuation to the original web session, and the analytic-poles completion postscript after that unchanged continuation. No linked early passage appendix is omitted.

Seven long tables, containing 162 rows, are expanded into labelled entries. All original cell contents, quotations, source UUIDs and mathematical prose are retained. Display formulas are constrained to the available line width only when necessary; original mathematical expressions and all exact source snapshots remain unchanged. Unicode mathematical characters in prose use the mathematical font. Long hashes and paths have break opportunities, and each table-entry label stays with its first fields.

To rebuild from this directory:

```text
python build_ledger.py
```

The build uses only packaged relative paths. It requires Python, Pandoc, LuaLaTeX, the DejaVu text fonts and Latin Modern Math. It generates the layout filter and header, converts the complete Markdown to editable TeX, and runs LaTeX twice for contents and bookmarks. To regenerate only the Markdown and TeX, use `python build_ledger.py --tex-only`.

`BUILD_RECEIPT.json` records source hash validation, preserved source UUIDs and every expanded table. `QA_RECEIPT.json` records final rendering and independent preservation/visual checks. The final PDF has a contents page, 24 bookmarks and original transcript locators throughout.
