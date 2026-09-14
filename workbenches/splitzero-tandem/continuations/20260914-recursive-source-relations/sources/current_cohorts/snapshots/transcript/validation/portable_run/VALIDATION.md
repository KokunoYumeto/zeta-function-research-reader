# Transcript ledger validation

**PASS.** The five ledgers cover all 215 visible nodes in exact source order: 67 user messages and 148 assistant prose messages. There are no missing or unexpected source UUIDs.

| Lane | Visible nodes | Users | Assistants | Findings |
| --- | ---: | ---: | ---: | ---: |
| early_context | 51 | 15 | 36 | 34 |
| base_formation | 35 | 13 | 22 | 23 |
| typed_route | 34 | 12 | 22 | 30 |
| actual_tau | 43 | 14 | 29 | 14 |
| late_control | 52 | 13 | 39 | 14 |
| **Total** | **215** | **67** | **148** | **115** |

Each complete assigned segment was reconstructed exactly from the original UUID-keyed message strings and its header format. All five reconstructions match without whitespace normalization. Source text hashes were checked for all 5,349 retained messages.

The quote validation performed 211 checks: 209 literal nonempty source substrings and 2 exact empty-source checks. The latter preserve the visibly blank U0065 input in both its episode and finding. There are 197 distinct quote-kind/target/text tuples; repeated user quotations are checked separately. All 34 complete copied message bodies in the typed-route ledger are also exact.

All 1232 recorded locator/UUID/chain/role reference checks passed. The actual-tau ledger intentionally includes U0044 and U0045 in both a composite episode and individual steering episodes; stable UUID deduplication gives its 43 distinct covered nodes, and both episode records remain.

No whitespace fallback was needed. The script never changes case, punctuation, Markdown, TeX backslashes, or mathematical symbols. The detailed quote receipt records exact source offsets for literal matches and UUIDs for every match.

The two abbreviated quotations containing ellipses were replaced by their literal source excerpts by the early audit owner before this final run. No mathematical finding changed.

**Reading scope.** Full reading is recorded separately through the lanes' complete-read declarations, contiguous line/character windows, and explicit recovery of truncated tool output. Quotation matches alone are not used as evidence of a full read. The validator mechanically verifies provenance and coverage; it does not independently repeat the mathematical audit or prove a reader's cognition.

**Historical tool limit.** The transcript retains 2,600 explicitly redacted tool records. Their placeholders and metadata remain available, but their underlying historical execution results remain unavailable. This validation does not certify those missing outputs, linked attachment bodies, or historical test claims.

The 115 findings include completed calculations, valid scoped obstructions, repairs, and contextual entries. They are not 115 failures or abandoned calculations.

Reproduce from the repository root with:

    python -X utf8 work/tau_f1_transcript_audit_20260913/integration_validation/validate_ledgers.py

The copied validation/validate_ledgers.py has identical bytes and the same repository-root discovery when used in this output tree. Only the Python standard library is required.
