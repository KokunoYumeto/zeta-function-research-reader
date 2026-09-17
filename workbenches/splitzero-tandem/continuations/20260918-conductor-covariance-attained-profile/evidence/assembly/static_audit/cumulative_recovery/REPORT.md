# Independent cumulative insertion-recovery audit

Audit time: 2026-09-17 22:48:23 UTC. All **233 checks passed**, with no failures. No source file was edited and no TeX compilation was performed.

The audit read the current `INSERTION_MANIFEST.json` (20,975 bytes; SHA256 `920950c9cf630f6bcb2c517333cfae1e88c80df808ab8a31526afbdc2a21574b`) and verified its recorded sizes and hashes against actual files. Every observed input remained byte-stable through the end of the audit. Its assertions of successful recovery were independently recomputed; the verifier does not import or execute the assembly implementation.

## Exact predecessor recovery

The predecessor directory is `work/mixed_tail_continuation_20260917/full_receiver_build/staging/`; the successor directory is `work/dual_web_intake_20260918/assembly/cumulative/`. Full absolute paths are recorded in `RECOVERY_AUDIT.json`.

| File | Predecessor bytes recovered | Successor bytes | Recovery result |
| --- | ---: | ---: | --- |
| `09_UPDATED_JOINT_NOTE.tex` | 3,366,040 | 3,585,384 | Every byte identical |
| `10_UPDATED_SIGNED_RETURN.tex` | 3,356,821 | 3,576,165 | Every byte identical |
| `14_CURRENT_KERNEL_AND_MULTIPLICITY_PROOFS.tex` | 2,957,454 | 3,176,798 | Every byte identical |

Measured SHA256 values:

| File | Recovered predecessor SHA256 | Current successor SHA256 |
| --- | --- | --- |
| 09 | `d0fbf7da7af46177628e09d3288f0253e36e6baf7b5d2bc6ecc69e8e3904d301` | `5c8c90779e890384567ecbcb4ce089e086fb615de524c44720671c328d9592d3` |
| 10 | `64c17d9ddf373462810515cb97621de8703c8d9e5dcf1cece5cce089159feaa2` | `b4ce8621c97191f25e4e04d085659f046abb8934362ad5e809446e8e5f2af44d` |
| 14 | `50e5071b8bc1e1325f401764e7fdd3cda50994601b6f2e1bf00627864d665571` | `8b7b185c31cb7f863dc857bc6978458522002974ddf2a76495fe8de619486cd8` |

For every file, the verifier removed the three recorded spans in descending successor-byte-offset order. It checked each payload's length and SHA256 before removal and compared the complete recovered bytes with the predecessor. A second check inserted the measured payloads into the predecessor at the recorded original offsets and reconstructed the complete successor exactly. Each successor's size increase is exactly 219,344 bytes. The inherited GEL material is included in this complete byte-preservation result; no inherited tag was changed.

## Inserted material and bibliography

| Shared payload | Bytes | SHA256 | Occurrences in each cumulative successor |
| --- | ---: | --- | ---: |
| `human:dlmf18` append, including inserted boundary newlines | 208 | `6c5d38f5dea764a7ed04dc92d688936ac06c16f1005b2d91a6d994b5e66902c9` | 1 |
| `human:dlmf5` append, including inserted boundary newlines | 206 | `fba98b35b4ebe544846e2aaf62c2e785ca639092b4b42ecdc2cb33c45c1812f0` | 1 |
| Common continuation including body, new reference and boundary comments | 218,930 | `56ba2e47c6b09bc037c7ebb49bb053e0ff96552a97be2788ae619915cd4a0e01` | 1 |

All three payloads are byte-identical across the three cumulative successors. The complete `DUAL_WEB_FULL_BODY.tex`, 217,998 bytes with SHA256 `eb3ca69c0cda569c8b7017d961295cd09642d5acd8996b856d279d15ea1bc6b4`, occurs exactly once in each cumulative successor and once in `DUAL_WEB_PROOF_SUPPLEMENT.tex`.

Each cumulative successor has exactly one `\bibitem[H25]{human:dlmf1}`, one bibliography item using display label H25, and one bibliography item using key `human:dlmf1`. Neither the key nor the label occurs as a bibliography item in any predecessor. The bibliography key multisets differ only by this one new entry.

The complete bibliography-entry intervals of all 29 inherited entries in 09, all 29 in 10, and all 27 in 14 recover byte-for-byte after removal of only the two supplied append payloads. Of these, 24, 24 and 22 entries respectively have `human:` keys. The marked append spans each occur exactly once inside their correct unique inherited entry.

The same H25 uniqueness and append-span placement checks pass for `DUAL_WEB_REFERENCES.tex` and `DUAL_WEB_PROOF_SUPPLEMENT.tex`. `DUAL_WEB_NEW_REFERENCES.tex` contains only one H25 item and does not repeat the inherited locator appends.

The independent bibliography inspection additionally confirms that all seven inherited entry byte strings copied into `DUAL_WEB_REFERENCES.tex` remain intact. Six entry intervals add one LF separator after the preserved bytes; the final `human:szego1975` interval is exact. The supplement embeds the entire 5,818-byte references file exactly once. The new entry content differs from its supplied source only by the H25 display-label assignment. See `bibliography_independent/REPORT.md` and its JSON audit for exact entry hashes and byte boundaries.

## Audit artifacts and limits

- `audit_recovery.py`: reproducible independent byte verifier.
- `RECOVERY_AUDIT.json`: 233 individual checks, complete absolute paths, measured hashes, insertion offsets, payload counts, and per-entry recovery hashes.
- `bibliography_independent/`: separate bibliography verifier and findings.
- `LOGBOOK.md`: assignment provenance and completed work record.

This is a static byte-preservation audit. Mathematical acceptance pins, formatting/control-character repairs, and rendered or compiled output are outside this subtask and remain with the parent audit.
