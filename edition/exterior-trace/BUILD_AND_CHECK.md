# Build and check the source package

All paths below are relative to the extracted `zeta-integrated-sources` directory. The separate PDF is the reviewed publication artifact; rebuilding it can change PDF timestamps or font embedding without changing the mathematical source.

## Main reader

The complete 57-input TeX graph starts at `main.tex`. With a current TeX installation providing the packages named in its preamble, run from the extracted archive root:

```text
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The bound artifact has 454 pages. The final review covers the new chapter and its table-of-contents links; it is not a fresh visual or mathematical certification of every inherited page. Exact source hashes are in `EDITION_SOURCE_SELECTION.json`.

## New exact finite checks

The standalone finite checkers need Python and SymPy. Use the documented SymPy version 1.13.1 to reproduce the recorded checks. From the extracted archive root:

```text
python edition/evidence/diagonal-exterior/check_diagonal_exterior.py
python -O edition/evidence/diagonal-exterior/check_diagonal_exterior.py
python edition/evidence/exterior_trace_review/check_review_refinements.py
python -O edition/evidence/exterior_trace_review/check_review_refinements.py
python workbenches/tau-exterior-trace-delivery/check_exterior_trace.py
python -O workbenches/tau-exterior-trace-delivery/check_exterior_trace.py
```

The delivered checker has its own `CHECKS.md` and negative-control instructions. The original delivered records and the later independent replay logs are kept in different directories. The original upstream 24-method source replay is historical supplied evidence, not the independent 22-method exterior replay. Neither test suite estimates the actual large-k arithmetic norm.

## Formal modules

The current public Lean toolchain, Lake configuration, preparation scripts and workflows are retained in `formal/splitzero` and `.github/workflows`. The conormal-cyclic workflow is the trigger-corrected current version at the immutable public base, not the older reviewed PR version. It specifies the exact build and trust checks for `SplitZeroConormalTower.lean` and `SplitZeroCyclicDepth.lean` together with their inherited dependencies. The preparation step fetches and hash-checks pinned upstream sources; this package is not wholly offline.

The actual post-merge run and its complete log are recorded under `edition/evidence/review_pr21/postmerge_ci`. `PUBLISHED.json` is the earlier workflow-update receipt and truthfully says CI was pending at that moment; `CI_RECEIPT.json` records the later passing result. No local Lean execution was used for this publication preparation.

## Review evidence is not an input manifest

Files under `edition/evidence` include dated checks and reviews. Some historical receipts identify earlier reader artifacts or external reference sources that are not bundled here. In particular, the diagonal-exterior `CURRENT_READER.json` binds the historical 442-page reader, whereas `edition/evidence/current-reader/READER_INTEGRITY.json` binds this 454-page reader. Their scopes and original hashes are preserved. Only `EDITION_SOURCE_SELECTION.json` inventories this archive.

Public receipt derivatives replace private filesystem locations with package-relative locators where the exact object is included, and explicitly external evidence locators otherwise. The original hashes and resulting public hashes are recorded separately. The original source package's anonymous `/mnt/data` paths remain as historical container provenance. No mathematics is edited by those path substitutions.
