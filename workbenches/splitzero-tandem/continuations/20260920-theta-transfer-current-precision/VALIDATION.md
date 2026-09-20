# Validation of the complete source edition

The root read all six full derivations and independently reran the exact finite checkers:

- Native precision: 2,013 checks pass (89 identities, 1,703 PSD checks, 206 inequalities, 15 negative cases).
- Burnol transfer: 116 exact assertions pass in normal Python. No optimized-mode validation is claimed for this assertion-based checker.
- Moment-to-current composition: 1,008 checks pass (153 identities, 134 PSD checks, 708 inequalities, 13 negative cases).

The individual derivation tasks also report optimized runs for the two exception-based precision/composition checkers. Their unchanged full validation reports are included. These test matrices check identities and bounds; they do not replace arithmetic moments by synthetic data or locate zeta zeros.

All original proof files are hash-pinned in PROOF_IDENTITIES.json. Each cumulative successor reversibly appends all six complete proofs to its published predecessor; no earlier mathematical content is removed. The generated combined source receives a separate draft-mode syntax/reference check. Draft mode does not generate or visually inspect a PDF.

The scientific map diagram is generated from the displayed exact formulas, not measured native values. Its caption identifies the full definitions, parameter range, maps and human sources. Figure inspection and source-build results are recorded separately before publication.
