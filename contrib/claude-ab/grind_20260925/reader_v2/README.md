# LaTeX source of the reader, version 2

*The split-zero programme around the Riemann zeta function: a reader of its results, with proofs*, version 2 (26 September 2026). Prepared by Claude (Anthropic), model `claude-opus-5-5` (Opus 5.5), at maximum reasoning effort.

Version 1 is in `../reader/` and is published on Zenodo as 10.5281/zenodo.22970703. Version 2 applies note `48_`, which covers a review of version 1 in both directions (four corrections, five stronger theorems, seventeen smaller items), and the outcome of its own referee pass (`../checks/zeta_reader_review/referee_v2/`). The additions include:
- a Carleman criterion in the angle |arg w| < π/4, so that the degrees {2^a3^b} are dense for t > (log 2)(log 3)/(4π);
- the extension of Proposition 2.8 to every q with φ(q) > 2.

Appendix B, last subsection, lists every change.

Build: `lualatex reader.tex` twice. The preamble is the same as in version 1: fontspec and unicode-math with TeX Gyre Pagella, TeX Gyre Pagella Math, TeX Gyre Heros and DejaVu Sans Mono, with a luaotfload fallback list for rare glyphs. `fig/` holds the three figures of version 1.
