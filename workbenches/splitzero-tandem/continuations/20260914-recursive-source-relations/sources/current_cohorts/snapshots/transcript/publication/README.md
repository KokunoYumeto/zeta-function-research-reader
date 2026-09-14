# Actual cohomology over the tau base

`actual-cohomology-proofs.pdf` is the complete mathematical proof volume. Its editable source is `actual-cohomology-proofs.tex` together with every file in `fragments/`. All thirteen full source contributions are retained; their hashes and the assembly changes are recorded in `BUILD_MANIFEST.json`.

The original mathematical files are preserved separately in `../proofs/`. The assembled copies namespace LaTeX labels by chapter, preserve the original equation tags, wrap long displays and provenance strings, and retain the distinction between the original script and calligraphic alphabets. A chapter's original local equation numbers belong to that chapter.

## Rebuilding

Use Python 3 and a standard TeX distribution with LuaLaTeX, Latin Modern fonts, `fontspec`, `unicode-math`, `mathrsfs`, `amsmath`, `amssymb`, `amsthm`, `mathtools`, `geometry`, `microtype`, `hyperref`, and the ordinary layout packages declared in the main TeX file.

Run from this directory:

```text
python rebuild.py
```

The script makes three LuaLaTeX passes and writes the new PDF and logs into `rebuild/`. It does not modify the delivered PDF or any proof source. No external mathematical file is needed to compile the assembled TeX body.

The proof volume is accompanied by the transcript audit and the original source closure in the surrounding delivery. Mathematical claims and limitations are stated in the individual full proofs; compilation and visual checks certify the artifact's integrity and presentation, not an unproved arithmetic weight estimate.
