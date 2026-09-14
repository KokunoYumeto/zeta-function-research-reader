# Joint Gamma Schur continuation

Read [the complete 46-page PDF](Joint_Gamma_Schur_Continuation.pdf). All 46 actual rendered pages passed visual review. The seven complete proof sections and every accepted mathematical source pin are bound by `BUILD_VISUAL_RECEIPT.json`. The continuation prompt is `CONTINUE_JOINT_SCHUR_PROGRAMME.md`.

The PDF prints the complete current joint-Schur note and the exact new continuation calculations. `sources/` contains its complete typed LaTeX. `Joint_Gamma_Schur_Continuation.tex` is the main file.

`provenance/math_sources/` retains the author sources before their standalone document wrappers were removed for inclusion. `provenance/display_changes/` records each preparation difference. `provenance/incoming/` retains the supplied package and original note. The full inherited Gamma, signed-return and original-degree proofs and the complete current receiving texts are retained under `dependencies/`; they are not replaced by abstracts.

The mathematical source pins and the source-preparation receipt identify the exact edition printed. The PDF visual-review receipt, added after compilation, identifies the reviewed final PDF.

## Build

Use XeLaTeX with the standard packages declared in the main file. From this directory run:

```text
xelatex -interaction=nonstopmode -halt-on-error -file-line-error Joint_Gamma_Schur_Continuation.tex
xelatex -interaction=nonstopmode -halt-on-error -file-line-error Joint_Gamma_Schur_Continuation.tex
xelatex -interaction=nonstopmode -halt-on-error -file-line-error Joint_Gamma_Schur_Continuation.tex
```

The extra passes resolve the complete contents and equation references. Mathematical authorship changes and display repairs have separate provenance records.

This source tree is a portable mathematical delivery. Local execution paths are confined to provenance receipts that identify the copied source files.
