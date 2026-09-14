# Source reading, provenance, and scope

## New user material actually used

- `Pasted text(3).txt`: read its complete 644-line body, including the theta/Hochschild factorization, critical comparison kernel, Laplacian identities, augmented zero mode, heat-source limit, and curvature/action-hull continuation. Source-derived results are identified as such in the note. This run did not repeat its reported Lean execution or independently review the printed zero-mode claim against page images.
- `Deligne_FR.tex`: inspected the inline-work index and read the selected D022 ranges at file lines 31755–31849. This is a 49,653-line multi-work corpus, not a file containing only Weil II. The inspected inline-work list omits D032. D022 is *Poids dans la cohomologie des variétés algébriques*: the selected passage states geometric weight strictness, its relative version, and the Thom–Gysin shift. It does not endow the analytic circle quotients in this continuation with a geometric weight filtration.
- The previous six S20 ZIP parts were reassembled in order. The result has 216,580,466 bytes and SHA-256 `e2005bf31e1fcf362765f73c315c855e0f504f24f34d3a0ab188049da522b7c8`. The current `edition/source_language.ndjson` records at printed pp. 178, 203 and 206 were read. Page 206 contains the exact upper/dual-lower/image statements 3.3.4–3.3.6. We used those records, not the older zero-accepted salvage text. No OCR, PDF extraction, or claim of independently auditing the complete historical proof occurred.

The source inventory JSON records the exact bytes and selected page-record hashes. The source corpora are not redistributed in this package.

## GitHub coordination input

Read PR27 metadata and changed filenames, then the relevant source note via the GitHub connector:

- repository: `KokunoYumeto/zeta-function-research-reader`
- PR: 27
- inspected head: `a4a87844c257485ae6d669f5b3eb6d96b9e8b8d8`
- inspected base: `e4ee97cdce904d4b9bb5697d33095aaa00083f24`
- note: `workbenches/tau-specialization-curvature-formal/HOCHSCHILD_COMPARISON.md`

The PR was open and draft at the observed read. Its successful source checkpoint and Lean scope remain the contributor's reported/linked evidence; this continuation does not relabel it as a fresh local Lean run. Selected source comparisons agree with the uploaded report. No assertion of byte identity between the markdown report and pasted prose is made.

## Primary-source check

The arXiv abstract of Connes–Consani, *Hochschild homology, trace map and zeta-cycles*, arXiv:2207.10419, was checked. It expressly distinguishes the all-zero Laplacian realization and the critical-only sheaf realization. The analytical formulas used here are retained from the user's detailed comparison and proven explicitly where used. The abstract is not cited as a proof of the new estimates.

The general Fourier/Parseval ingredients and the use of matrix order through an identical constrained minimum are classical. The novel-to-this-continuation work is the explicit source-preserving composition, its constants, the all-period weighted identity, fixed-circle completion kernel, and finite Fourier truncation estimate; no global priority assertion is made.

## Local verification scope

`check_periodized.py` contains 16 passing exact finite regression methods. Normal and optimized JSON result records are identical. The separately run deliberately false controls reject omission of the zeroth-mode Gram and omission of the -k boundary term. They are tested failures, not excluded cases hidden from the suite.

`calibrate.py` was run at 40 and 60 decimal digits with different theta/frequency cutoffs. It evaluates the actual analytic seed h=1 and an explicitly declared Gaussian test. It supplies no interval rounding enclosure or full numerical tail certificate. The analytical error formulas are proven in the note, but their high-degree arithmetic input matrices have not been numerically enclosed here.

No new Lean execution and no opposing arithmetic asymptotic upper bound are claimed. Existing proof packages are not reported as freshly rerun merely because they remain on disk.
