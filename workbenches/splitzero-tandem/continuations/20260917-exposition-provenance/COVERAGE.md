# Exposition and provenance audit: coverage and remaining work

Human readability and accurate provenance are commitments of this programme. The companion explains its mathematics, credits the human sources it uses, and records the scope and limits of the source audit. See [the declaration source note](DECLARATIONS.md). This coverage record distinguishes source discovery, primary-source checking, and unresolved attribution.

## What was inspected

The first mechanical discovery baseline was the **692-page predecessor**, containing **19 logical files**. All **15 text/LaTeX files, 223,268 lines**, were scanned mechanically. Two foundation TeX files and seven canonical metadata files were also inspected, yielding 276 metadata records and 68 author-name strings. A recorded author-name string is neither a distinct-person count nor evidence that the programme used that person’s work.

The current files contain **zero citation-command occurrences** and **15 bibliography-item occurrences representing five distinct keys**: `SFB-current`, `SFB-connecting`, `QOT:gpa`, `QOT:pds`, and `QOT:current`. All five reference internal programme material. The separate foundation bibliography has **109 entries**, including scholarly and explicitly identified local/model-related sources. Historical notes do contain substantive human attribution; this discovery result does not negate it. The editorial work must connect that scattered attribution to the current claims.

The scanner found **412 marked source blocks**, representing **153 distinct body hashes** after explicit line-ending handling; 129 hash groups recur. These are exact text-body comparisons, not counts of independent results. **5,643 extracted occurrences** were checked against their exact source files, hashes, lines and original spellings; all marked blocks were rehashed. The extraction validation passed. This verifies extraction fidelity, not mathematical correctness or citation applicability.

[LEXICAL_CANDIDATES.csv](LEXICAL_CANDIDATES.csv) and [LEXICAL_CANDIDATES.json](LEXICAL_CANDIDATES.json) contain **4,396 current-file name/eponym candidates with 49 observed spellings**. Each row supplies only source filename, hash, line, column, observed spelling and an explicitly unresolved role. They contain no private prose. A Fourier, Gram or Schur occurrence is not automatically evidence of a particular publication dependency. A finite lexicon also misses unnamed results and variants.

## Transcript boundary

The acquired published parent chain covers 8–13 September 2026 and was acquired on 13 September at 15:15:44 UTC. Its prior verification records **5,350 nodes**, including the empty root, and **5,349 nonempty message records**: 67 user, 2,611 assistant, 2,654 tool and 17 system records. “Nonempty message record” concerns the message object; one attachment-only user record has empty textual content. The readable prose selection has **215 records: 67 user and 148 assistant**.

The published share redacts **2,600 tool payloads**. They were acquired as redacted records; their hidden content was not recovered. A mentioned attachment or sandbox file does not supply that file’s bytes. Completeness is limited to the acquired chain **as published**, not all sessions, branches, private messages or attachments. This inventory read the coverage and verification receipts; it did not reread all 5,349 messages.

A separate historical audit reports scanning those 215 visible records and six original snapshots. Its archive inventory reports **599 text objects, 427 distinct content hashes and 59,467,026 text bytes**, covering 47 selected ZIPs plus loose text in the selected multilingual archive. Those are sibling-receipt counts, not fresh validation by this inventory. Selected substantive passages have their own reading records. The scopes overlap and must not be added as if disjoint.

## Preserved predecessor reading route

The publisher’s recorded source commit is `de0644902496e1718879f4b625f9ff9faafc5ae5`. The [immutable source directory](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/de0644902496e1718879f4b625f9ff9faafc5ae5/workbenches/splitzero-tandem/continuations/20260917-root-sensitive-growing-degree) and [download release](https://github.com/KokunoYumeto/zeta-function-research-reader/releases/tag/rgc-growing-degree-2026-09-17-de064490) lead to the accepted edition. Its three recorded assets are:

| Asset | SHA-256 |
|---|---|
| [79-splitzero-growing-degree-reader.pdf](https://github.com/KokunoYumeto/zeta-function-research-reader/releases/download/rgc-growing-degree-2026-09-17-de064490/79-splitzero-growing-degree-reader.pdf) | `be77708317908a987cc4fcc54eac330100425b771a514d8c36e00250465b092e` |
| [80-splitzero-growing-degree-sources.zip](https://github.com/KokunoYumeto/zeta-function-research-reader/releases/download/rgc-growing-degree-2026-09-17-de064490/80-splitzero-growing-degree-sources.zip) | `2a72fcfebdba33390fda43071a43ea4dedfad8c6d929e2d58324b3fd2c83cbcc` |
| [81-splitzero-growing-degree-supplement-1.pdf](https://github.com/KokunoYumeto/zeta-function-research-reader/releases/download/rgc-growing-degree-2026-09-17-de064490/81-splitzero-growing-degree-supplement-1.pdf) | `96ff16e0ef3cb6b56e6be56030699f632ff00f7eabf19c521337b5de8b712f11` |

At the publisher handoff, [DOI 10.5281/zenodo.22802593](https://doi.org/10.5281/zenodo.22802593) remained the **680-page predecessor** and the matching 692-page Zenodo transition was pending. No newer DOI is asserted here. These publication facts are reported from the handoff and recorded release receipt; this inventory performed no fresh remote readback. The accepted successor and its verified publication are recorded in the update below.

## Remaining coverage

The old indexes describe a much wider corpus. Their August snapshots record **55,470 research-library file records / 10,100 publication units** and **251,407 local-work file records / 459 canonical publication units**. A 9 September historical navigation inventory contains 8,123 mixed-file path lines. These figures are routing metadata, not fresh inventories, full-reading claims, or proof that every relevant session was acquired. Library possession alone also does not establish research use.

- **P1: Historical branches and later web sessions outside the acquired 8–13 September chain.** The prior transcript receipt covers one published parent chain. A separate historical path inventory has 8,123 mixed-file navigation entries and is dated 9 September; it does not certify every session or branch. Next: Reconcile each programme-relevant export and its inherited history with source IDs, hashes and dates; identify missing branches and record them explicitly. Do not count duplicated inherited dialogue as independent evidence.

- **P2: Nested archives, binary-only records and embedded source-map payloads excluded from the selected historical archive scan.** The sibling historical inventory scanned 599 text objects with 427 hashes in 47 selected ZIPs plus loose text. It did not expand nested ZIPs, read PDFs, or decode the large loose source-map payloads. Next: Resolve referenced source bodies through the screened registry; recover only the exact dependency objects needed for provenance, with hash and edition checks. Keep private conversation material local.

- **P3: External predecessor archive and source-map lineage.** The publisher handoff states that the historical 326 MB archive and predecessor source map are not recursively embedded in CURRENT. Next: Follow the recorded reconstruction recipes and external hashes; classify each programme dependency as available, read, unresolved or inaccessible. Do not infer source coverage from the current proof payload being complete.

- **P4: Other relevant local research roots beyond the selected modern multilingual archive.** The canonical route enumerates general Chatnotes, Soc, Split Zero, Mock, globalization-NTE, globalization-CUE and CUE-Mellin roots. Its August snapshot reports 251,407 local file records and 459 canonical publication units. Next: Query the existing canonical source graph for actual links to the Split-Zero programme and inspect the returned dependency sources. Record unlinked material as outside the research-use boundary; mere library ownership is not a citation dependency.

- **P5: Human literature used after the legacy bibliography/source ledgers.** The three principal literature ledgers have latest dated entries on 30 August. The separate bibliography has 109 entries and was modified 12 September. The recorded research-library inventory has 55,470 file records and 10,100 canonical publication units. Next: Reconcile subsequent notes, source reviews, uploads and web citations against actual human works and editions; preserve author, translator, editor, exposé author, source-cites-source and direct-use roles separately.

- **P6: Unnamed mathematical dependencies, ambiguous eponyms and applicable theorem statements.** A finite name lexicon misses unnamed results, aliases and spelling variants. A name occurrence does not establish a paper used or an imported theorem. Next: Read the relevant derivations and source passages to attach each substantive use to its exact hypotheses and locator. Separate locally proved specialization, cited background, historical mention and actual imported result.

- **P7: Changing mathematical successor and public-entry integration.** The moving-cutoff successor is now accepted and published as the 726-page edition. This companion has been updated to its mathematical results, retaining predecessor locators explicitly. Source attribution for all newly encountered dependencies continues; mathematical acceptance does not by itself close that audit.

## Reproducibility and nonclaims

[COVERAGE.json](COVERAGE.json) records all 19 baseline file hashes, the bounded scan counts, input-evidence hashes, publication routes, prior transcript receipt scope and explicit remaining tasks. The private source map is identified solely for integrity; its original payload is not a public attachment. The screened public reconstruction is the distribution route.

Nothing here asserts that the entire corpus was read, that all intellectual debts have been found, or that every named method has been attributed. No private conversation passages, account locators, private source-map payloads or inferred personal authorship are published in these coverage files. The source-specific reading and attribution work must continue alongside the mathematical programme.


## Accepted successor and additional source discovery

The accepted **726-page edition** is published as [DOI 10.5281/zenodo.22803503](https://doi.org/10.5281/zenodo.22803503). Its immutable source commit is `be79088cb1fa4d79b31724856eefcdbd0839b8cc`. The publication owner verified all six new downloads, preserved all 78 earlier downloads, and verified the cumulative PDF as the default preview. These are publication-integrity checks, not a new mathematical proof audit. The exposition now explains the moving-cutoff advance and distinguishes its R726 references from the preserved R14 predecessor pagination.

Additional discovery inspected 708 files and 107 ZIPs across the selected programme roots: 1,102 text bodies, 460 distinct text hashes and 39,547,982 unique text bytes. Four hashes overlap the earlier selected archive inventory. The 1,976 bibliography-item occurrences and 1,106 text variants are not counts of distinct works. Two large tar archives remain outside that pass. The public expanded register preserves 163 selected historical bibliography entries whose text was read; its source corrections and verification limits remain attached.

Six readable web exports contain 134 response instances and 99 distinct response-content bodies after the stated exporter-date handling. The audit read 69 selected attribution paragraphs and recovered 19 typed source-use records. Older exports overlap the previously acquired chain; these counts must not be added as independent sessions. Raw conversation material is not included in the public companion.

The historical source-map pass recovered and mechanically searched 2,552 additional uniquely hashed text documents (241,968,238 bytes). It identified 1,045 bibliographic contexts. This is lexical discovery, not full mathematical reading. Its 106 embedded-text checksum discrepancies and 494 public-map restoration/hash-interpretation records require reconciliation; declared-original byte identity is not asserted for them. The public derivative applies transformations, so a different payload hash is not by itself evidence of corruption. Binary bodies and excluded objects are not counted as read papers. These overlapping inventories are kept separate.
