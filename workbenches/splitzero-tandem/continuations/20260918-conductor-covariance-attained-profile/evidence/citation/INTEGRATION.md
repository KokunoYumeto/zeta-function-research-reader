# Insertion-only WCF citation derivative

This folder contains a prepared additive attribution repair, not a replacement for the accepted mathematical record. The original accepted WCF file remains unchanged. No PDF was built and no public service was changed.

## Receiver steps

1. Use `WEIGHTED_CONDUCTOR_FORWARD_CITED.tex` as the WCF fragment in the next additive compilation. It is the accepted source plus six marked citation-only spans. Every original byte, including equations, whitespace, phases, constants and previous citations, survives in order.
2. In the accepting bibliography, retain the complete existing `human:dlmf18` and `human:dlmf5` entries. From `BIBLIOGRAPHY_ADDITIONS.tex`, append each `WCF_BIB_APPEND` span's contents inside the matching existing entry; do not paste these unlabelled fragments as separate bibliography entries.
3. Insert the `WCF_BIB_NEW human:dlmf1` span as one new bibliography entry. The snippet deliberately assigns no `H` label. Use the accepting document's next available display label if that document requires labels, and first check whether it already defines `human:dlmf1`. If present, preserve that entry and merge only the verified locators rather than creating a duplicate key.
4. Preserve the existing `human:lyons2003` entry: the new projection citation uses the same arXiv v4 witness, adding Lemma 4.1, p. 12, rather than changing its attribution or phase conventions. The existing entry already identifies Section 4 and its version; adding this lemma/page to that entry is optional locator completion.
5. Run the verifier below. After actual integration, compile the receiving document and check resolved citations, bibliography and clickable destinations. This folder's structural check does not claim that a future receiver has been compiled.

```powershell
& 'LOCAL_ACCOUNT_ROOT/miniconda3/python.exe' -B -X utf8 'PROJECT_ROOT/work/forward_source_support_20260918/citation/prepared/verify_citation_derivative.py'
```

The six spans cover the forward Cauchy estimate, maximum modulus, finite Laurent removal, inverse Cauchy estimate, binomial coefficients and exterior projection lemma. They deliberately do not attribute the actual conductor matrix, inverse comparison, correction signs or four-endpoint inequalities to DLMF or Lyons.

`INSERTION_SPANS.json` records exact bytes, offsets and hashes. `CITATION_DERIVATIVE_MANIFEST.json` pins original, derivative, spans, bibliography additions, verifier and the inherited bibliography witness. Deleting only the explicit inserted spans must recover the accepted SHA-256 `d86dcb3daf13c9b2d5a0aaa4d72cce35a1aff48066ad69c7d9846b9d097dc354` byte for byte. `--seal` creates missing local receipts only and never overwrites a differing receipt or edits any source.

The source support and exact inspected-human-source boundaries are in the parent folder's `WCF_CITATION_COVERAGE.md`, `CITATION_ACTIONS.json` and `lyons/LYONS_SOURCE_CHECK.md`. The frozen 837/263-page edition and the mathematics owner's current proof are not touched by this handoff.
