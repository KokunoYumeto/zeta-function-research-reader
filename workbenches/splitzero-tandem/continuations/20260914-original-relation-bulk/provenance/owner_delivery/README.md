# Original relation bulk control

Read [the complete 33-page PDF](Original_Relation_Bulk_Control.pdf). All 33 actual rendered pages passed visual review. The five complete proof bodies and their source pins are bound by `BUILD_VISUAL_RECEIPT.json`. The continuation prompt for this edition is `00_CONTINUE_THE_PROGRAMME.md`.

This separate reader contains the complete new analytic proofs. `Original_Relation_Bulk_Control.tex` is the main typed LaTeX file; its accepted proof bodies are under `sources/`.

`provenance/math_sources/` preserves the author files before document-wrapper and display preparation. The source-acceptance and display-change receipts identify the exact edition printed. Final PDF and page-review information will be recorded in `BUILD_VISUAL_RECEIPT.json`.

`dependencies/joint_schur_46/` is a complete byte-preserved copy of the accepted 46-page joint-Schur delivery, including its PDF, full source, exact calibration, inherited providers and provenance. Its original edition remains unchanged.

## Build

From this directory, with XeLaTeX and the standard packages declared in the main file, run:

```text
xelatex -interaction=nonstopmode -halt-on-error -file-line-error Original_Relation_Bulk_Control.tex
xelatex -interaction=nonstopmode -halt-on-error -file-line-error Original_Relation_Bulk_Control.tex
xelatex -interaction=nonstopmode -halt-on-error -file-line-error Original_Relation_Bulk_Control.tex
```

The additional passes resolve the contents and internal references. The complete source bundle retains the independent proofs and exact source provenance.
