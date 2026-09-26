# LaTeX source of the reader

*The split-zero programme around the Riemann zeta function: a reader of its results, with proofs.* Prepared by Claude (Anthropic), model `claude-opus-5-5` (Opus 5.5), at maximum reasoning effort, 22–26 September 2026.

Build: `lualatex reader.tex` twice. The preamble uses fontspec and unicode-math with TeX Gyre Pagella, TeX Gyre Pagella Math, TeX Gyre Heros and DejaVu Sans Mono (all in TeX Live), and a luaotfload fallback list (TeX Gyre Pagella Math, STIX, DejaVu Serif, FreeSerif) for rare glyphs.

Files: `reader.tex` (preamble and title page); `sec0_front.tex` to `sec9_open.tex` (the sections); `appA_catalogue.tex`, `appB_corrections.tex`, `appC_verification.tex` (appendices); `refs.tex` (bibliography); `fig/` (the three figures, made by the scripts in `figures/` of the audit notes archive; the mirror-line figure was re-rendered with neutral labels).
