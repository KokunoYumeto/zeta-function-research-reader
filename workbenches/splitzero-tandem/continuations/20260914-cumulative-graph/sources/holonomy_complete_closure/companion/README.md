# Holonomy descent and generator control

This folder contains the complete 46-page companion, its editable LaTeX, the original proof sources, and the full supporting mathematical sources and review evidence.

Open `Holonomy_Descent_and_Generator_Control.pdf` to read the volume. The editable entry point is `Holonomy_Descent_and_Generator_Control.tex`; the seven complete bodies are in `proofs/`. Original supplied and accepted text is retained in `originals/`.

| Body | Pages | Full content |
| --- | --- | --- |
| H | 3–14 | Original all-holonomy source note, H1–66 and H49a–g |
| HG | 15–20 | Generator control, HG1–25 and HG11a |
| HD | 21–23 | Degree cost and exact supported-zero inverse images, HD1–10 |
| CQ | 24–29 | Shifted density, full sampled quotient and primary kernel, CQ1–29 |
| HDI | 30–34 | Exact inverse domain, source weights and sharp source realization, HDI1–24 |
| HCD | 35–42 | Continuous cochain descent, minimum metric and weighted relation gap, HCD1–29 with source estimates |
| CR | 43–46 | Continuous relation completion and canonical fixed-packet degree limit, CR1–14 and CR12a–c |

`SOURCE_GUIDE.json` gives each complete source and reader hash, all 213 numbered formulas, and the exact correction crosswalk. `dependencies/` contains the full preceding proofs, including PSD, PSA, the original periodized source, and the complete finite-circle source closure. The supplied historical evidence is in `evidence/supplied_holonomy/`; the complete current independent reviews and actual saved execution receipts are in `evidence/current_reviews/`. The continuous-completion independent review includes its full additional projection-gap and finite averaged-positivity proofs.

The original H49c inverse wording is corrected explicitly by HDI4–8: the inverse is defined on the selected closed strip with its proved strict bound, and extends to a neighborhood of that strip. The original arithmetic source, its leading coefficient, all masses, phases, multiplicities and coefficient frames are retained. The CQ, HDI and HCD proofs overlap; each is complete and retains the exact map for its particular receiving complex.

The raw CR note records its historical review status. This edition also includes the completed independent review and root acceptance. The fixed-packet limit in CR fixes the packet and tensor degree while the polynomial cutoff increases; it supplies no tensor-degree rate or Riemann-hypothesis conclusion.

The source bodies are preserved in full. CQ excludes only its private delegated-task and machine-context paragraphs. Its mathematical text remains complete. Every prose formula conversion and layout transformation has an exact inverse record under `evidence/typography/`; the untouched source versions are also available. Private transcripts, user-provenance logs, raw intake metadata, scans and historical reader screenshots are outside this deliverable.

To rebuild, install a LaTeX distribution containing the packages in the main preamble and run `python build.py` from this folder. The build performs three pdfLaTeX passes. It runs no mathematical checker or Lean process. `MANIFEST.json` covers every delivered payload except itself, using relative paths, byte counts and SHA-256 hashes.

The complete independent completion review is also supplied as readable LaTeX at `proofs/support/CR_independent_typed_review.tex`, with its exact source-to-typing map in `evidence/typography/CR_INDEPENDENT_FULL_TYPED_REVIEW.json`. `SUPPORT_GUIDE.json` specifies its full next-edition witness route. Its five-page scratch rendering was individually inspected; the portable wrapper reproduces every accepted page image exactly. To compile this supporting body separately, run `pdflatex CR_independent_review_witness.tex` twice inside `proofs/support/`. It retains every proof paragraph and all 216 original code spans, with 206 mathematical spans typeset and 10 provenance spans preserved. The 46-page companion is unchanged.
