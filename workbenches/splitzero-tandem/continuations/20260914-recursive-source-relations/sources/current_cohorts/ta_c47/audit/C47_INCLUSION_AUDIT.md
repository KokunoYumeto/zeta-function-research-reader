# C47 complete-body inclusion audit

This is a source and compatibility audit of the exact repository at `output/Tau_Theta_Hankel_Certification_2026-09-13/repository`. It changes no source, builds no PDF, and performs no mathematical replay. `audit_c47.py` writes its machine-readable findings only in this audit directory. The exact hashes, all labels and tags, environment usage, and collision locations are in `C47_INCLUSION_AUDIT.json`.

## Complete reader route

The complete 47-page object is a PDF concatenation, not a single TeX entry. `rebuild_pdfs.py` builds `Tau_Theta_Hankel_Certification.tex` with pdfLaTeX, builds `support_reader/main.tex` with LuaLaTeX, and concatenates the five-page TC component followed by the 42-page support reader. The latter has nine bodies. Therefore cumulative editable inclusion needs all **ten** bodies below; the recorded `complete_source_count: 9` applies only to the support reader.

1. `proofs/TC.tex` — TC1–TC28.
2. `support_reader/typed/WB.tex` — original workbench equations 1–23.
3. `support_reader/typed/WBR.tex` — WBR1–WBR41.
4. `support_reader/typed/CH.tex` — CH.1–CH.19 (retain the dot).
5. `support_reader/typed/TR.tex` — TR1–TR33, theta-tail and code review.
6. `support_reader/typed/TT.tex` — TT1–TT12.
7. `support_reader/typed/GF.tex` — GF1–GF13.
8. `support_reader/typed/TCReview.tex` — TR1–TR23, distinct error-control review.
9. `support_reader/typed/RootAcceptance.tex` — complete acceptance/replay/source chronology body, no explicit equation tags.
10. `support_reader/typed/GFR.tex` — GFR1–GFR30.

None of these bodies includes another file. None uses `\ref`, `\eqref`, `\pageref`, `\autoref`, `\cref`, or `\Cref`; most mathematical citations are literal prose references. None requires a non-ASCII character mapping. Do not embed the two whole document wrappers in the cumulative document: they contain their own preambles, title pages, document boundaries, pagination, and header settings.

## TeX compatibility

TC requires `amsmath`, `amssymb`, `amsthm`, theorem/lemma/proposition/proof environments, and the original definitions `\R=\mathbb R`, `\C=\mathbb C`, `\Q=\mathbb Q`. The support bodies require AMS mathematics, `mathrsfs` for `\mathscr`, `longtable`, `booktabs`, `array`, `calc` for the `\real` column expressions, `listings` for two TR code blocks and the GFR inline callback, `hyperref`, `xurl`, and the usual Pandoc `\tightlist` and `\passthrough` definitions. The two `\LTcaptype{none}` tables require counter `none`.

The exact 821/R62 preamble at `output/split_zero_rh_tandem_2026-09-12/current_source_20260913_periodized_residue/tex/main.tex` already supplies these packages, environments, macros, and counter except `listings` and TC's `\R`, `\C`, `\Q`. Add compatible definitions before including TC; do not unconditionally redeclare existing theorem environments or counter `none`. Preserve the original meanings if any later cohort already defines those short macros. `unicode-math` is in the standalone support-reader wrapper, but no body requires it; loading it into the existing 821 preamble would change global math setup unnecessarily.

Copying the support reader's `\lstset` configuration preserves the intended CLI/code presentation: `basicstyle=\ttfamily\footnotesize,breaklines=true,breakatwhitespace=false,columns=fullflexible,keepspaces=true,showstringspaces=false`. The bodies contain long source hashes and dimension-dependent tables, so a later cumulative render should inspect those tables and the long displayed formulas at the actual cumulative line width. This audit does not assert a successful cumulative compile or render.

## Labels and references

The ten bodies have 65 distinct TeX labels with no internal duplicates. A scan of every `.tex` in the exact 821 source tree found no collision with those 65 labels or TC's bibliography keys `workbench`, `flint`, `zhang`. Generic labels such as `scope` and `reproduction` can collide with other newly staged cohorts: namespacing all copied labels by cohort/body is a reversible cumulative adaptation if required by the final whole-tree scan. Retain its exact old-to-new mapping.

The 23 tags TR1–TR23 occur independently in both TR and TCReview. They are explicit displayed tags rather than duplicate TeX labels; preserving them is compatible with preserving the old proofs, but external cumulative references must say which review is meant. WB's plain numeric tags 1–23 also need a source-qualified citation in the larger reader. Preserve CH's dotted tag convention. Full tag-to-file-and-line data is recorded in JSON. Do not treat a theorem counter reset or source-wrapper section counter as a mathematical change.

## Dependency edges and propagation requirements

- TC's original-theta source and coefficient definitions depend on WB/WBR's original Fourier, theta and Mellin maps. TC10–TC13 and CH.10–CH.17 propagate actual moment enclosures to logarithmic coefficients and both finite LDL recursions. TC27 is about the original two dimension-16 matrices; its precise certificate cannot be replaced by historical rounded decimal replay data.
- GFR1–GFR9 derive explicit growth constants for precisely the original `F`; GF1–GF13 supply the whole product proof; WBR10 and TC16 then retain reciprocal zeros and all multiplicities. GFR is the later independent check of GF/TT. RootAcceptance's earlier statement that no independent GF acceptance is claimed is historical chronology and must not be presented as the final current review status.
- WB's undefined `nu_N` in its equation 16 is explicitly repaired by WBR's identity `nu_N:=u_N`, WBR16, and the consistent TC24 formula. A mathematically current earlier WB body should carry that exact identity in place with a provenance map to the sealed original; merely reproducing its old undefined symbol leaves current text stale.
- WBR23–WBR25 depend on the full original arithmetic packet. WBR explicitly requests cumulative inclusion of its entire original note, its entire proof, full replay, and both inherited dependency files. The exact inherited sources are `dependencies/dependencies/arithmetic_input.tex` (A1–A19) and `dependencies/dependencies/HOCHSCHILD_COMPARISON.md` (including H16–H25). Its literal `dependencies/...` prose paths are relative to the inherited workbench root, while the public C47 repository preserves that root beneath `dependencies/`. Retain or document that locator map in cumulative packaging.
- `dependencies/dependencies/MATHEMATICAL_NOTE.md` and `DERIVED_MATHEMATICS.md` preserve the full support-fibre/coequalizer arguments cited by WB. They are repository sources even though the ten printed bodies do not `\input` them. Deduplicate them against the TA staging by exact hash only, while preserving their source paths in provenance.
- WBR29–WBR40 retain the full nilpotent inverse, both reflected primary blocks, theta boundary representative, half-trace and critical observation defect. Any later packet/source refinement must recheck these downstream uses while retaining the original multiplicity and map data.
- WB and WBR explicitly describe their old numerical runs as exploratory. CH/TC and the root exact replay later provide actual finite integral enclosures and original-matrix positivity. Current text should link or incorporate those accepted refinements at the affected earlier claims; the old numerical files and historical statements remain provenance. This finite improvement does not establish positivity in every dimension.
- Preserve `calculation/` and the ordinary-Python exact rational replay (`verify_exact_rational.py` plus its referenced `reviews/` script), including the exact original certificate, fresh integration replay, API contract, exact endpoint receipts and 1,400-interval evidence. Their analytic input scope and optimization rejection remain part of the result.

`dependencies/TC_SOURCE_STAGING.json` is an earlier staging receipt whose `remaining_intake` still says the full GF proof is missing. GF and GFR are now present in the sealed final repository. Preserve that receipt as chronology, but use the final `MANIFEST.json`, support preservation record, and exact body inventory for current completeness.

## Source preservation

Preserve `originals/TC_original.tex` with `evidence/TC_EXTRACTION.json`; TC's removed `\maketitle` and bibliography paragraph break have recorded inverse reconstruction. Preserve all nine `support_reader/originals/` files and all `support_reader/conversion/` records. WB/GF have exact preamble/postamble/body extraction records; the seven Markdown proofs have their parsed conversion trees. The accepted typed files retain recorded line wrapping, command-hyphen, source-hash and table-column adaptations. Source SHA strings in historical review prose identify reviewed originals and may differ from the later typed body hash (notably GF's original line-ending adaptation); do not rewrite those historical pins to claim they identify the converted body.

## Audit log

2026-09-13: Read both TeX entry files, their reconstruction records, rebuild route, all body-level command/tag/label/environment usage, dependency source descriptions, and the exact 821 preamble. Compared the C47 labels and bibliography keys against every TeX file in that source tree. Recomputed pins for the distributed manifest and support-preservation record. Created only this audit directory's report and script. No original source file was modified; no PDF or Lean process was started.
