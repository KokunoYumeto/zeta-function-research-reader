# Deligne mixed-control continuation

Drag **PROMPT.md** and **COMPLETE_CONTROL_WORK.tex** into the web session. The overview in **DELIGNE_USAGE_OVERVIEW.md** is also useful context.

The LaTeX reader contains every supplied proof body, the earlier AW calculation with its exact attribution and operator correspondence, and the complete original marked-product note with explicit corrections before its appendix. Exact individual TeX sources are in `sources`; independent reviews and build evidence are in `evidence`.

To reconstruct the flattened reader, run `python BUILD_READER.py` in this folder. Compile `COMPLETE_CONTROL_WORK.tex` with LuaLaTeX or pdfLaTeX; it has no external TeX file dependencies. Compilation here is a syntax check; no PDF edition is included in this handoff.
