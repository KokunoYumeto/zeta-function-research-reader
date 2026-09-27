# The split-zero programme around the Riemann zeta function — paper, version 3

LaTeX source of *The split-zero programme around the Riemann zeta function: its results, with proofs, and its bridges*, version 3 (27 September 2026). Prepared from an audit of the programme by Claude (Anthropic), model `claude-opus-5-5`. Programme: KokunoYumeto, developed with ChatGPT and Codex (OpenAI).

Version 3 is the text of version 2 with its framing corrected. It keeps every theorem, proof, figure and citation of version 2. Its only changes of content are two decimal renderings, (log 2)(log 3)/(4π) = 0.060598… and (log 2)(log 3)/(2π) = 0.121196…, and three updated statuses in the table of edges to the author's other workbenches. Appendix B, last subsection, lists every change.

Version 1 is Zenodo 10.5281/zenodo.22970703. Versions 1 and 2, with the audit notes they cite, are in the branch history at commit `a90d9e5b`, in `contrib/claude-ab/grind_20260925/` (`reader/` and `reader_v2/`). The check scripts cited in the paper are in `../../checks/zeta/`.

Build: `lualatex reader.tex` three times. The preamble uses fontspec and unicode-math with TeX Gyre Pagella, TeX Gyre Pagella Math, TeX Gyre Heros and DejaVu Sans Mono, with a luaotfload fallback list for rare glyphs. `fig/` holds the three figures.
