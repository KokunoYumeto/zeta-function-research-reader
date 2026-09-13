# Independent machine QA: complete integrated reader

Result: **pass for the terminal candidate's machine checks**, with visual approval expressly outside this report. The checked terminal PDF is 512 pages, 4,146,598 bytes, SHA-256 `e32e7c2dd44d5359fcbf4329ec7cbf059e84b334435c1ddad3b177e8436be30a`.

The initial candidate was frozen before repair, and each later pin was explicitly supplied by the parent task. No report silently follows a mutable filename. The snapshots and reports distinguish:

| Snapshot | PDF bytes | SHA-256 |
| --- | ---: | --- |
| Initial, before layout repairs | 4,147,201 | `d4a31f7c7ce7ec06f42ddc2ebfa7ad39a6c1123d2e972df0df4e354d235254d9` |
| Intermediate first repair (`final_snapshot`) | 4,147,388 | `48ae2e14e07271b658c1710bfb17e4c59377fe4f4d4cb1f4248f1af2ed53d33f` |
| Terminal (`terminal_snapshot`) | 4,146,598 | `e32e7c2dd44d5359fcbf4329ec7cbf059e84b334435c1ddad3b177e8436be30a` |

All three contain 512 pages. The word `final` in the intermediate snapshot directory records its assignment at that time, not the terminal publication selection. Only the third pin is the terminal recommendation.

## Source preservation and completeness

The candidate build manifest was checked against actual bytes, not accepted solely on its boolean declarations. All 58 old non-main source inputs match their pinned baseline copies and the canonical copies read during snapshotting. The 59-input baseline includes the old main wrapper. The candidate's 65 declared inputs equal both its recursively reachable `input/include` closure and the inputs observed in the actual recorder file: no missing, unreachable or unrecorded project input.

The five added complete chapters occur in the actual PDF and its linked structure:

| Chapter | Starts on PDF page | Machine-observed proof coverage |
| --- | ---: | --- |
| Full-jet source/relation transfer | 455 | All 40 literal formula blocks found after whitespace normalization; 11 headings |
| Arithmetic endpoint bounds | 462 | AE.1--AE.48 all found; 17 headings |
| Balanced arithmetic norm windows | 472 | BV.1--BV.7 all found; 6 headings |
| Exact consecutive-window product | 475 | WP.1--WP.13 all found; 7 headings |
| Four-volume threshold | 480 | FV.1--FV.9 all found; 7 headings |

The AE source body's prior reversible reconstruction remains the separate proof-preservation evidence. The machine checks here bind the complete chapter bytes to the compiled dependency manifest, verify every new chapter label destination, and verify all 77 displayed tags and all 40 literal transfer blocks in extracted PDF text. They do not replace the mathematical review or assert that text extraction proves visual fidelity.

From the initial to terminal source cut, exactly four inputs changed: the main wrapper, confluent-transfer chapter, AE chapter, and window-product chapter. The baseline 58 non-main inputs and the balanced-window/four-volume chapters are unchanged. The new changes are the recorded reader-provenance qualification and typography/heading adapters. In the separately authorized AE repair, only four opaque 40/64-hex `texttt` literals received discretionary breakpoints; its converter's inverse reconstructs the exact original note.

## Labels, destinations, links, and text endpoints

- 1,685 source labels: no duplicates and none absent from the final auxiliary file.
- 1,436 source references resolve after correctly processing TeX comment-line continuations. The first parser pass's 18 apparent missing references were `%`-newline parser artifacts, not document defects.
- 3,045 named PDF destinations and 432 outline/bookmark entries resolve to actual pages.
- 2,221 internal link annotations resolve; no link rectangle lies outside its page box.
- All 492 TOC entries point to the same actual PDF page as their printed page number.
- All 148 URI annotations use HTTP(S). Their encoding and presence were checked; live external availability was not polled.
- All 512 pages extract text; no blank page or replacement-character page was found. The opening contains the revised title and explicitly historical earlier-edition model-use record. The final page retains the concluding bibliography through item 109 and the printed page number 512.

The initial and intermediate candidate also passed the structural link/closure checks. The terminal review is independently repeated, not inferred from them.

## Actual final log, separated from inherited diagnostics

All three terminal build-pass receipts have exit code zero, and their captured log hashes match the build record. The actual terminal `main.log` has **zero overfull boxes, undefined references, multiply-defined labels, missing-character diagnostics, or fatal errors**.

There are 40 warning/box diagnostics in that log. Thirty are byte-identical message blocks already present in the old baseline: 18 underfull notices and 12 package warnings. The remaining ten are new underfull notices only:

| Source | Final source lines | Underfull badness |
| --- | --- | --- |
| Confluent transfer | 51--57; 299--301; 452--456; 507--514 | 1466; 1354; 2035; 3039 |
| Arithmetic endpoint | 780--785; 863--867; 867--871 | 1033; 2799; 3240 |
| Window product | 199--200 | 1270; 1642; 1147 |

These are spacing diagnostics, not evidence of missing mathematics. Their appearance requires the separate visual judgment; this report does not approve or reject their visual appearance.

The initial repair candidates were four overfull boxes: transfer lines 51--57 (8.7234 pt), transfer lines 145--153 (27.09702 pt), AE lines 780--785 (186.61539 pt), and window-product lines 219--220 (29.99554 pt). All four are absent from the terminal log. The initial warning record remains preserved rather than overwritten by the repaired outcome. The parent also reported and corrected the CT heading/TOC spacing during its visual lane; this machine lane verifies the resulting destinations but makes no claim to have inspected those rendered pages.

## Evidence and boundary

`INITIAL_SNAPSHOT_RECEIPT.json`, `FINAL_SNAPSHOT_RECEIPT.json`, and `TERMINAL_SNAPSHOT_RECEIPT.json` bind the three immutable local snapshots. `MACHINE_QA_INITIAL.json`, `MACHINE_QA_FINAL.json`, and `MACHINE_QA_TERMINAL.json` contain the detailed structural checks. `DESTINATIONS_TERMINAL.json` records the complete resolved destination/TOC map. `TERMINAL_MACHINE_CHECKS.json` records thirteen passing terminal predicates and the source-cut comparison.

No PDF authoring, marker, TeX/PDF build, canonical promotion, remote change, or new mathematical calculation was performed in this QA lane. The narrow authored-source hash-break repair was separately requested and recorded in the AE chapter receipt. No visual-QA claim is made. Release or promotion still requires the parent task's independent visual approval of this exact terminal pin.
