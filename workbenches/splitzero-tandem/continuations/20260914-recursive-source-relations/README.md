# Split-zero cohomology and arithmetic weight control

Attribution: KokunoYumeto.

[Read the cumulative paper](Split_Zero_Cohomology_and_Arithmetic_Weight_Control.pdf). This 1,624-page edition develops the split-zero arithmetic cohomology programme: the original theta-function source and its quotients, labelled support and coefficient diagrams, spectral packets and their full jet orders, boundary and monodromy comparisons, and the metric and determinant estimates used to connect these constructions. Later corrections are carried into the affected earlier proofs and their downstream uses. The source chronology retains earlier attempts and explains their scope; a historical claim is not a new certification.

The complete editable reader starts at [tex/main.tex](tex/main.tex). Its current build uses 240 pinned source files in `tex/` and `build/`, including the corrected prepared PR13 source. The default build does not rerun the historical converter and cannot silently regenerate its superseded text.

## Build and verify

From this directory, with Python, PyMuPDF and XeLaTeX installed, run:

```text
python scripts/build_paper.py
```

The declared TeX packages and fonts must be available locally. Compilation needs no network connection or external research workspace. The builder checks the source pins before compiling and checks the compiler's actual input list afterward. A rebuild creates its own PDF and build receipt; it does not inherit visual acceptance for changed bytes.

To verify the downloaded, accepted publication package without rebuilding:

```text
python scripts/verify_public_edition.py
```

## Sources and provenance

[CURRENT_SOURCE_MANIFEST.json](CURRENT_SOURCE_MANIFEST.json) inventories this public package. [PUBLIC_DERIVATION.md](PUBLIC_DERIVATION.md) explains its relation to the sealed source edition; [PUBLIC_DERIVATION.json](PUBLIC_DERIVATION.json) gives every retained, transformed and omitted source-file identity. Original mathematical documents and revision evidence remain in `sources/`, `history/` and `provenance/`.

[The mathematical conversation and calculation companion](sources/public_mathematical_companion/PUBLIC_MATHEMATICAL_CONTENT.md) retains the selected visible mathematical responses, inputs and documentary calculation sources with exact source-interval mappings. Private reasoning and account/transport data are not included. The companion is historical mathematical evidence, not a claim that every calculation is correct or current.

This is a separately identified public derivative. Five nonmathematical source locators and one explanatory locator note differ from the sealed workstation edition; no formula or proof expression was changed for publication. Machine-specific paths in supporting provenance have public aliases. Private conversation captures, personal instructions, reference-only full-page literature extracts, and superseded PDFs containing private locators remain private. Their retained mathematical successors and precise source hashes are recorded rather than silently discarded.

The current PDF has its own source, page-render and visual-review bindings. This publication work supplies no new Lean execution or independent proof of the Riemann hypothesis.

## Lossless historical QA storage

The complete historical page-comparison JSON is stored as [gzip](provenance/final_pdf_qa/final_corrected_8bbd9da0/CROSS_PAGE_RENDER_TRANSFER.json.gz), with exact original/decompressed byte and SHA-256 identities in [PUBLIC_REPRESENTATIONS.json](PUBLIC_REPRESENTATIONS.json). No field or mathematical content was removed. Historical acceptance receipts keep their original scope and hashes. Verify exact decompression with `python scripts/verify_public_representations.py`. The accepted PDF and all current compiler inputs are unchanged.
