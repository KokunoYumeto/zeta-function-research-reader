# Periodized/residue promotion script: complete static review

Scope: prepare and review the new local promotion workflow for the accepted R58--62 reader. This lane has not imported or executed the promotion module, and has not run stage, seal, preflight or promote. No current reader, immutable workspace, source package, source ZIP or mathematical source was edited. The only authored files are the new script and this review.

Reviewed script: `promote_cumulative_periodized_residue_reader_20260913.py`, 39,871 bytes, SHA-256 `58bcb006807a682abefa6545ddfcf8d1686191dc0e82bacbcecdaf08e22df19c`.

The script was adapted from the previously reviewed SGA/Connes promotion script. The complete predecessor was read before adaptation; the resulting program and all changed branches were read and its Python AST was parsed. Imports, constants, function/class declarations, and the guarded `main()` dispatch are the only top-level statements. Importing the module performs no filesystem operation. The CLI supports `preflight`, `stage`, `seal` and `promote`, with explicit final iteration, source-review and visual-review paths.

## Fixed source and package boundary

The old immutable workspace is v15, tied to the completed SGA/Connes promotion receipt. A new iteration must be greater than 15. The new exact package is `current_source_20260913_periodized_residue`; its ZIP is `Split_Zero_Cumulative_Periodized_Residue_2026-09-13_Source.zip`. Every package file remains the accepted fixed source cut except the documented current README and separately pinned acceptance evidence. The inherited README remains available under the new history directory. No later crosswalk suffix is copied into the fixed package.

The checks require 25 complete TeX proof bodies, 47 complete unique original source witnesses and the unique R62 conclusion marker. PDF hash, byte count and page count come from the actual build verification, compiler receipt and finished PDF. They are not hard-coded to the current iteration. Current v17 evidence has 821 pages, 25 bodies, 47 unique witnesses, 151 compiler inputs and empty required diagnostic arrays. The source-review file must accept the exact current PLAN; a previous edition's source review cannot substitute for it.

Stage requires completed source/build acceptance but deliberately does not read a pending visual receipt. Seal and promotion require complete visual acceptance, the same exact PDF, complete page renders and clean page geometry. The script imports only PyMuPDF lazily to inspect the finished PDF; it imports no builder and runs no mathematical checker or Lean command. Every compiled input and all raw witnesses are checked in the fixed source and again in the promoted current folder.

Private raw provenance retains its local publication role. The README states that separately pinned publisher copies are required for local execution locators and internal coordination evidence. It describes the complete original periodized/residue notes and PSA/PSD/RCX/FC/DC contributions without claiming new mathematical executions.

## Exact crosswalk transport

Let a byte word mean a finite sequence of bytes, with concatenation denoted here by `+`. Let `B` be the old v15 fixed SOURCE crosswalk, `N` the new fixed SOURCE crosswalk, and `C` the current working crosswalk. The admissible domain consists of triples for which `B` is an exact byte prefix of both `N` and `C`. These conditions are checked before any current mutation. The old receipt's `crosswalk_transport.fixed_cut` pins `B`; its `working_after` must agree with the old promotion's crosswalk `after` pin. Using `working_after` as the pin for `B` would be incorrect because the earlier promotion already retained a working suffix.

If `N` is a prefix of `C`, write the unique decomposition `C = N + S` and produce `N + S`, which is exactly `C`. Otherwise write the unique decomposition `C = B + S` and produce `N + S`. The decomposition is computed by a byte slice after the selected prefix length. Both branches retain every suffix byte in its original order, without decoding text or changing line endings. Empty `S` is valid. Occurrence of `S` as a substring elsewhere in `N` does not delete or alter it.

The result begins with `N`. On a second preflight, the first branch therefore applies and returns that result unchanged. If later work appends a byte word `H`, the same branch preserves the full remaining suffix `S + H`. An edit inside the mandatory old fixed prefix fails the domain check; a new fixed source that loses that prefix also fails. The prefix test establishes the exact allowed path relation, not independent authorship of the appended suffix. All other promotion candidates keep the generic exact-pin conflict checks.

The crosswalk is now an explicit candidate independently of the PLAN change list. Its special branch runs before generic allowed-pin acceptance, including when the current crosswalk equals the prior promotion's already-suffixed `after` pin. This closes the concrete data-loss route in the predecessor implementation.

For the checked source state, `B` has 41,377 bytes, `N` has 41,866 bytes, and the pre-existing suffix has 586 bytes. The derived working result has 42,452 bytes and SHA-256 `3d9782b4995f2a54dd16d89563d5359b0aeb0dbfdbba6672a02facc01876defe`. The actual transport records old fixed, old promoted, current-before, new fixed, retained suffix and current-after byte pins. These values describe a read-only byte comparison; no promotion was executed.

## Mutation and preservation review

All current targets pass path containment checks; frozen release directories, existing exact-source folders and root source ZIPs are rejected as current-file targets. Current conflicts are resolved before the backup directory is created. Before each write the exact preflight pin is rechecked; originals are copied to the backup; writes use sibling temporary files and atomic replacement followed by byte readback. Unrelated later files remain present because promotion performs no tree deletion.

The previous 715- and 765-page workspace/package PDFs and main TeX files, their completed promotion receipts, and both prior source ZIPs are checked before promotion and again afterwards. The fixed baseline I is separately verified. The old v15 fixed crosswalk is also checked again after promotion. Independent inspection confirmed the ten prior PDF/main/ZIP files match their recorded pins and that all 4,903 current v17 source paths satisfy stage naming restrictions without a manifest/history collision.

The independent crosswalk design receipt is `cumulative_periodized_crosswalk_design_review_20260913.json`, SHA-256 `53ff0444fe2a8f338d6b04bb8e6c9d8766f32343047533f6e84d12f931dc1a9c`. The complete independent code review is `cumulative_periodized_promotion_code_review_20260913_v17.json`, 7,337 bytes, SHA-256 `c461d31576112ba283bc4b0d1cc3030c73017ccde93d8ebcaef366a420735a7b`; it accepts the exact script pin above with no concrete code defect. Final source/visual receipt readiness belongs to the running parent workflow; older receipt schemas or pins cannot substitute for the required current acceptance.
