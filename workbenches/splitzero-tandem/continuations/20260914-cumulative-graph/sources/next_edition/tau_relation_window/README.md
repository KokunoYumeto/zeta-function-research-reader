# The exact relation-window spectrum and its arithmetic determinant bound

This folder supplies the complete AW1–AW23 calculation as a five-page readable PDF and editable LaTeX. It retains the original arithmetic and Gamma measures, their masses, the polynomial and relation flags, the full Taylor-unit observation, and the exact source-metric isometry. The full relative-eigenvalue bound and the one-dimensional nonlinear endpoint calculation are proved in the main text.

The editable entry point is `Tau_Relation_Window_Spectral_Transport.tex`; `proofs/AW.tex` contains the whole reading body and `originals/AW_original.tex` retains the accepted original byte-exactly. The only body layout change keeps the long section heading on two explicit lines; `evidence/LAYOUT.json` records its exact inverse. Document boundary and wrapper records are in `evidence/BODY_EXTRACTION.json`.

The complete independent written proof WS1–WS39 and its acceptance receipt are in `evidence/`. This includes the additional strictness calculation for the literal polynomial flags. The complete sealed 49-file Arithmetic Determinant Transport package, with its full AT proof, RV review and 29 inherited proof sources, is preserved under `dependencies/Tau_Arithmetic_Determinant_Transport`. Its historical source limitation remains stated in its own guide and in the dependency crosswalk.

Run `python build.py` with a LaTeX distribution to rebuild the main PDF. The build performs three pdfLaTeX passes. Every final page was visually inspected; the final compiler reports no warnings, all23 equation tags are present, and the complete body inverse was verified. No mathematical checker or Lean process was run for this artifact.

`SOURCE_GUIDE.json` provides the full reading and proof routes. `MANIFEST.json` lists every delivered payload except itself by relative path, byte count and SHA-256 hash.
