# Original tau-base cohomology: complete transcript audit and continuation

This repository contains the full published source, a 115-finding passage audit, and thirteen chapters of completed mathematical calculations on the original tau-base construction. It retains the absolute pointed base, its actual derived pushforward, its separate generic-stalk comparison, the original theta complex, the right adjoint, full support masks, arithmetic jets, units, and tensor actions.

## Read the result

- [Complete reading edition](Tau_Base_Transcript_Audit_and_Completed_Proofs.pdf).
- [Editable proof volume](publication/actual-cohomology-proofs.tex) and its local fragments.
- [Full passage ledger](PASSAGE_AUDIT.md); [editable ledger volume](ledger_publication/).
- [Concrete supplementary continuation](SUPPLEMENTARY_WEB_CONTINUATION.md), with its [analytic-pole completion postscript](CONTINUATION_POSTSCRIPT_ANALYTIC_POLES.md), addressed to the original web session; the delivery receipt is retained separately.

The completed proof chapters cover typed source maps and the actual eigenline lift, the restriction fibre and adjoint extension, the full reversed-support dual, the finite/global theta cocycles, full-jet grading and its theta lift, raw Mellin relations, source moment constants, the complete resonant circle resolvent, original cutoff-to-theta scaling, retained physical comparisons, viscosity/clock transport, and the coordinated arithmetic determinant and relation-window spectral calculations. Every chapter retains its complete statements and proofs. The two coordinated determinant chapters are identified as companion work rather than newly attributed to this audit.

The original arithmetic growth estimate remains open. The delivered continuation starts with the now-calculated signed density trace and relative source spectrum. Its postscript carries forward the newly completed analytic pole extension, period determinant and endpoint quotient; the quantitative theta-Gram contribution of those maps remains to be calculated. The global balanced-kernel calculation retains its stated scope. No theorem here assumes those missing estimates or declares the entire original program unsuccessful.

## Exact coverage and provenance

Source: <https://chatgpt.com/share/6aa6bc6e-98cc-83eb-9343-e811c26d6631>.

The raw published page contains 5,350 mapping nodes, 5,350 linear nodes and the same 5,350-node current parent chain, in exactly the same order. All 5,349 message texts roundtrip literally. Five readers covered all 215 visible records: 67 user turns and 148 assistant prose records. Independent verification reconstructs each entire assigned segment from the original UUID message bodies and checks the exact ordered union. The ledger has 115 findings. Its 211 quotation checks comprise 209 nonempty literal quotations and two exact empty-text references to the attachment-bearing U0065; no whitespace normalization is used. All 1,232 tested source references pass.

The share explicitly redacts 2,600 tool payloads. Neither those hidden contents nor linked attachment bodies absent from the page are claimed recovered. The complete published source, including redaction markers and attachment metadata, remains in [sources](sources/). A filename or a redacted command is not treated as proof that a calculation ran.

[Coverage](sources/COVERAGE.md), [transcript verification](sources/TRANSCRIPT_VERIFICATION.json), and [independent validation](validation/) give the exact checks. The source-pin manifests and final manifest record editions and hashes. [Provenance](provenance/) preserves task instructions, exact local user inputs, forwarded steering and the durable work log.

Original source snapshots remain unchanged. Corrected source-map editions preserve the earlier version under their local provenance directory. The corrected remote power-map edition is retained alongside the exact original accepted bytes. Publication records identify rendering transformations and the explicit even-Schwartz-domain and global-boundary clarifications.

## Complete dependencies

[Determinant transport dependencies](dependencies/determinant_transport/) include the companion proof and its complete 29-file mathematical source closure: original tau base and support constructions, arithmetic input and cyclic sum maps, theta source and periodization, Gamma measure and convolution, and complete independent proofs.

[Independent reviews](dependencies/independent_reviews/) retain the full Gamma, purity, determinant and relation-window proofs. [Remote coordinated sources](dependencies/remote/) retain scaling/exponential flow, corrected power-map domain, reflection-weight transport, Taylor-unit formal gauge, and their dependencies and checks. These are complete mathematical source files. A dependency inventory does not mean every inherited numerical fixture was rerun; current and inherited checks are identified separately.

## Reproduce

Use Python 3 and BeautifulSoup for extraction; the transcript verifier itself uses the standard library. Run the packaged transcript verifier from this repository:

    python reproduce/verify_transcript.py

    python -X utf8 reproduce/verify_audit.py

The portable audit rerun writes a separate receipt under validation/portable_run, preserving the original execution receipt. The path-only changes in the portable scripts are documented under reproduce. Build commands and dependencies for both editable volumes are recorded in their publication directories. The final reading edition concatenates the already visually checked ledger and proof volumes without scaling pages or altering mathematical text. Page labels and bookmarks identify both parts.

Finite algebra, sign and high-precision numerical checks supplement full proofs. No Lean run was performed. Source/sign validation includes every tensor-adjunction incidence sign through eight factors and a missing-sign mutation. The finite-cocycle check includes 54 high-precision cases and omitted-factor/reversed-orientation mutations. Mathematical review receipts and final visual QA are preserved in validation.

This audit task did not edit the shared cumulative master or independently publish remotely. Integration and web-session delivery are coordinated through their designated owners; receipts record what was actually delivered.
