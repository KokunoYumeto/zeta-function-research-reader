# Final visual-evidence allowlist: narrow independent review addendum

Date: 2026-09-13. This addendum reviews the exact final visual-evidence extension to the already reviewed H-to-Gamma edition. It retains the preceding complete workflow review and seal under `work/history/gamma_edition_pre_visual_20260913/`. The audit writes only its own files under `work/`; it performs no collection, staging, reader build, rendering, mathematical checker, portable replay, publication, or Lean execution and changes no file in the current reader package.

**Finding:** no missing actual-view input, source/PDF identity mismatch, wrapper-projection mismatch, or unauthorized change to the workflow was found. The exact 54-file extension contains the four complete original reviewer JSON/Markdown pairs, the aggregate JSON/Markdown pair, and all 44 page PNGs recorded as individually viewed. The existing collector already takes the four wrapper receipts from the aggregate's explicit component list and all 80 contact sheets from the renderer's explicit list. These mechanisms together retain the complete evidence for all recorded image-view actions without a directory sweep.

This review audits the provenance and actual bytes of the existing reviews. It does not claim that this auditor opened the images as a second visual reviewer. The evidence JSON explicitly records zero new image views. All 124 actually viewed image files were independently read, hashed, opened by the image-file decoder, and verified for file integrity. The actual PDF was independently hashed and its 478-page count read. Existing image-view claims remain attributed to the original four receipts.

## 1. Exact scope of the specification extension

The workflow remains byte-identical: SHA256 `d881c7ebdbfee984b8eead90cb78a1f4e90693c8748f4210d3dc4be55e8978f9`, 41,824 bytes. The preceding specification is exactly SHA256 `5780e4f4306365ef1a4e8775ae15522e78263b1d387808218caf2a3da0547081`; the preceding full review seal is exactly `00f524b5e37d2dfdba82ca49fc010707ba8af64fd702c3c2d2e250d4c7b12ff8`. Both are verified at their preserved historical paths. The history manifest also pins the complete previous review, previous static receipt, previous independent audit receipt, and preceding preparation handoff. All six historical hash/byte pairs were read and verified.

The revised specification is SHA256 `30cbb1e9ea4dbe4119e1a37443d5955daa5a152f13a95fda4b024551d7ea6f63`. Its `public_files` list equals the entire previous ordered list followed by exactly the 54 ordered entries in `work/gamma_visual_public_files_fragment_20260913.json`. The new entries are unique, have no case collision, and do not overlap any old explicit public entry. Exactly 44 have `exact=true`, and their paths equal the complete individually viewed PNG set. Exactly ten have `exact=false`, and their paths equal the complete five JSON/Markdown review pairs.

The earlier ordered `work_files` prefix is unchanged. The only added work entries are the six historical files, their `HISTORY.json`, the exact visual allowlist fragment, and the four audit/addendum/evidence/seal files for this bounded review. The sole additional top-level field is `preceding_review_history`, with exact value `work/history/gamma_edition_pre_visual_20260913/HISTORY.json`. Every other specification field is structurally equal to its preceding value. In particular the parent H identity, source archive, five proof names, 249 support members, 65-job description, mathematical source pins, runtime requirements, stage destination and replay settings remain unchanged.

The old seal continues to name its old specification and evidence revision. The new narrow seal names the revised specification and these final visual/source bindings, while also pinning the exact old specification, old seal, and history map. Neither the old seal nor the old full review is rewritten to imply it inspected a later revision. The audit additionally applies the unchanged public metadata transformation in memory to the preserved old specification and old seal and verifies that both retain their exact bytes even after that transformation.

## 2. Fixed reader and renderer identity

The actual reader PDF has SHA256 `9e79bd6cb4f95d845af0f637a1cb4fdcb56ddf32015f89430fa12c530b8b1680` and 478 physical pages. The current build receipt names this exact PDF and the complete 44 TeX input paths and 19 original source witnesses. Every one of those 44 input hashes and 19 witness hashes was independently compared to the current files. The current complete source audit's original and converted appendix pins and its matching TeX-input pins were also checked.

The final source audit is `build/source_audit_20260913i.json`, SHA256 `601ee113b5537ea844c7316dff64ca80ce021ea1659ee27795526042114907bd`. The final integration review is `logbook/gamma_final_integration_review_20260913.md`, SHA256 `f0957143f8849ac5a6904791a8d3f949e17efb8308926ad0c906807266f6f38a`. These are the current intake artifacts; the narrow seal pins their current bytes. The source audit identifies the same 478-page PDF, 43 proof chapters and 19 complete source appendices. This verification binds visual evidence to the actual completed reader rather than a previously rendered revision.

The renderer receipt is `build/qa/qa_receipt.json`, SHA256 `adb69fbbdc1ed42e0e333b289dd35dc92cb93deabd4dc915dd7d9109f2564008`. It names the same PDF, 478 rendered pages, 95 dpi, empty out-of-page-word and body-margin-crossing lists, and exactly 80 contact-sheet paths. It expressly does not assert visual approval. The aggregate approval is the separately supplied `build/qa/visual_review.json`, SHA256 `57929b33bc93d9f6b7767840133a9062b0014f28bc071a3b77a0f06cb6c719d4`. Its parsed content equals the aggregate logbook JSON, and the independent component audit also checked that those two aggregate files have identical bytes.

## 3. The complete raw-review-to-wrapper map

Each of the four collection wrappers contains the complete parsed original review as `original_review`, its exact original path and hash as `original_receipt`, the common PDF identity, its physical-page endpoints, and explicit contact/native-image records. The audit verifies equality of the entire embedded `original_review` object with the original JSON object. Thus the projection which extracts `original_review` is a left inverse of the wrapper construction on these four supplied records. No original observation, scope limitation, view mechanism, date, source locator, or original list order is discarded from that embedded object.

The common contact-record projection renames each reviewer's page-list field to `pages`, converts its already identified locator to a canonical package-relative path, and retains the exact image hash. The original families use `physical_pages`, `pages`, or `physical_pdf_pages`; these exact field choices are handled explicitly. Every projected contact record equals its wrapper record, in the same contact order.

The common native-record projection retains the exact `(canonical path, SHA256)` pair, then orders those pairs by their page-image path. For the second reviewer it first selects exactly `covered_page_images` entries whose `additionally_viewed_native` value is true. The other reviewers supply their explicit native-view arrays. No native-view flag is inferred from a render hash alone. The first review's original native array has a different order from its page-ordered wrapper; the audit records the exact permutation of raw indices. The original array order is still retained unchanged inside `original_review`. Hence this wrapper ordering does not alter or replace any viewing claim.

The original schemas yield the following exact coverage and native-view counts:

| Original component | Physical pages | Contact sheets | Additional individual pages |
|---|---:|---:|---:|
| `gamma_visual_pages_001_120_20260913` | 1–120 | 001–020 | 12 |
| `gamma_visual_pages_121_240_20260913` | 121–240 | 021–040 | 8 |
| `gamma_visual_pages_241_360_20260913` | 241–360 | 041–060 | 12 |
| `gamma_visual_pages_361_478_20260913` | 361–478 | 061–080 | 12 |

The four consecutive page lists are disjoint and concatenate exactly to the aggregate list `[1,2,...,478]`. Contact number `n` contains precisely physical pages `6(n-1)+1` through `min(6n,478)`, so contact 080 correctly contains four pages, 475–478. The concatenated contact-path list equals the renderer's ordered list. All four wrapper hashes and all four raw original hashes agree with their aggregate references.

The individual-page set is exactly:

`1, 8, 14, 24, 48, 53, 56, 86, 87, 88, 115, 120, 144, 183, 225, 234, 235, 237, 238, 240, 263, 274, 275, 282, 283, 284, 301, 302, 317, 318, 343, 344, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478`.

There are 44 distinct pages, exactly matching the aggregate's `individually_viewed_pages` list and the `exact=true` extension entries. The audit does not reclassify the other 434 pages as individually viewed. Their recorded full coverage is the stated contact-sheet coverage. Two original reviewers also list 238 individual render-file hashes for their complete ranges, regardless of whether those render files were individually opened. All 238 supplemental hashes were checked against current local files as provenance; that check makes no additional visual-view assertion and does not enlarge the 44-file native-image public list.

## 4. Complete retained view evidence and metadata correspondence

All 80 contact files and 44 actual native-view PNGs match their raw and wrapper hashes. Each is a decodable image with dimensions recorded in the independent evidence JSON. The 54 explicit public entries therefore fill the raw-review and actual-native-view portion of the visual evidence, while the unchanged collector supplies the four named wrappers and all 80 renderer-declared contact files. Every image which any raw review claims it actually viewed is present in this combined explicit/dynamic closure.

The audit reads all ten added text files in full. The Markdown reports' PDF identities, contact ranges, native-page lists, findings and declared limits agree with their JSON companions. A separate independent semantic cross-check also matched all 92 explicit Markdown image-table rows in the reports that contain such tables. The third review has a concise narrative and pins its full image details in the JSON companion; the aggregate narrative explicitly refers to the complete underlying receipts.

Generated review metadata receives the previously reviewed pathname-alias transformation in public copies. Every raw JSON remains valid under this exact transformation. For each wrapper/raw pair, the audit additionally verifies the commuting relation

`parse(alias(wrapper_bytes))["original_review"] = parse(alias(raw_review_bytes))`.

The aggregate's original SHA references continue to identify the original receipt bytes. The public manifest records their original/public hash pair; the wrapper's public transformed embedded review equals the public transformed raw review. The native/contact image bytes undergo no text transformation. This gives a concrete checkable relation between the original and public provenance records, without confusing a transformed public JSON hash with its original receipt hash.

The inherited physical-page 317–318 observation is preserved verbatim in the aggregate and in the third original review: a heading and the word “Let” occur before the formula continues on the following page. Both pages were individually inspected by that reviewer, and the complete source remains readable. The final records retain this minor inherited paragraph break; this audit neither erases it nor upgrades “no actionable defect” to a claim that no layout observation existed.

## 5. Evidence, seal and execution limits

The complete independent read-only program is `work/gamma_edition_final_visual_allowlist_audit_20260913.py`. It derives the workspace from its own location and contains no fixed local account path. It imports no collector/stager action and executes only the unchanged workflow's isolated pure alias function in memory. Its sole output is `work/gamma_edition_final_visual_allowlist_evidence_20260913.json`, recording every one of the 54 added original/public hash/size pairs, every wrapper/raw binding, all 124 image hashes and dimensions, the 238 supplemental render pins, the exact source/PDF/renderer/aggregate identities, prior history pins, and execution-scope fields.

The narrow seal is `work/gamma_edition_final_visual_allowlist_review_seal_20260913.json`. It pins the final modified specification, unchanged workflow, exact allowlist fragment, history map and six preserved history members, current static receipt, this full addendum and audit source/evidence, and the current final PDF/build/source/visual binding artifacts. It deliberately does not pin itself inside the specification or rewrite the preceding seal. The unchanged workflow will collect the four named new work artifacts with their actual hashes when the integration owner runs collection.

This bounded addendum is complete. The integration owner owns actual collection, staging, reader replay and checker execution. None of those actions is asserted by this addendum, and no new mathematical proof or verification result follows from this provenance audit.
