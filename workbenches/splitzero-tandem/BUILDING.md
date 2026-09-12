# Building the contributed volume

The source package contains the exact seven mathematical fragments used by the 88-page contributed volume, its master TeX file, and the generated TeX of six previously public source notes. The source notes retain their own revision and attribution headings. This is a standalone paper source package, not a standalone Lean repository.

Use XeLaTeX with Cambria, Calibri, and Consolas installed. From the package root, run this command three times:

```text
xelatex -no-shell-escape -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=build -jobname=reader tex/main.tex
```

The result is `build/reader.pdf`. The provided PDF is hash-pinned separately; a rebuild may have different timestamps and therefore different bytes even when its pages agree. The seven generated files `build/source_appendices.tex` and `build/source_*.tex` are required compile inputs, not disposable build caches.

The original local conversion script is not included: it verifies private staging manifests at machine-specific absolute paths. No such manifests or private transcripts are needed for the public build. The six raw source notes and their relative-path `build/source_receipt.json` preserve the source chronology and byte identities alongside the generated appendix TeX.

Python 3 with SymPy and mpmath runs the five included finite checkers. Execute carrier assertions without `-O`; the carrier CLI deliberately refuses optimized execution. The other four checkers support both ordinary and optimized Python. They overwrite their named JSON receipts under `checks/`, so use a separate copy when preserving the supplied receipts. The checks cover finite identities and specified numerical test functions; they do not turn the analytic arguments into Lean proofs or certify RH.

Keep this volume identified as a separate contributed continuation. Its analytic proofs, finite checks, and quotations of earlier formal interfaces have distinct scopes. In particular, source-metric positivity, shrinking absolute Gram matrices, and finite algebra calibrations are not assertions of a completed relative arithmetic estimate.
