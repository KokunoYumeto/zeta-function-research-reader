# Deligne mixed-control continuation

Drag **PROMPT.md** and **COMPLETE_CONTROL_WORK.tex** into the web session. The overview in **DELIGNE_USAGE_OVERVIEW.md** is also useful context.

The LaTeX reader contains every supplied proof body, the earlier AW calculation with its exact attribution and operator correspondence, and the complete original marked-product note with explicit corrections before its appendix. Exact individual TeX sources are in `sources`; independent reviews and build evidence are in `evidence`.

To reconstruct the flattened reader, run `python BUILD_READER.py` in this folder. Compile `COMPLETE_CONTROL_WORK.tex` with LuaLaTeX or pdfLaTeX; it has no external TeX file dependencies. Compilation here is a syntax check; no PDF edition is included in this handoff.

## Public distribution

This is a disclosed public locator derivative. The complete LaTeX reader,
all seven proof sources, continuation prompt, overview and Python sources are
unchanged. Historical reviews and compilation evidence keep their original
claims and identities; they are not new executions. See PUBLIC_DERIVATION.md
and PUBLIC_DERIVATION.json. FOLDER_MANIFEST.json inventories this directory;
the manifest under history describes the original owner handoff.
