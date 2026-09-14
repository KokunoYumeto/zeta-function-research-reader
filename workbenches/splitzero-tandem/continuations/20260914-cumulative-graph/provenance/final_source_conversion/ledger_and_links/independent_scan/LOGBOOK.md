# Independent inline-footnote conversion scan

Delegated scope: inspect active TeX graph in stage and delivery and raw Markdown converter inputs. Write only in this folder; no active edits and no PDF build.

A bounded audit extracted 2 user-role messages from the current task JSONL into USER_INPUTS_VERBATIM.md. The current instructions require exact mathematical preservation and durable provenance. The delegated read-only audit is consistent with those requirements. No new goal was created.

Work plan: enumerate the main.tex inclusion graph with hashes, record every footnote/caret-bracket candidate, compare originals and converter semantics, classify candidates and issue a coverage receipt. A child independently audits all ledger manifest originals; main agent owns graph enumeration.

## Coverage and findings

Initial scan found 239 files and 238 literal include edges in each of stage and delivery, no missing target or other inclusion controls. Its only two footnotes were the known BF12 defects, confirmed by the original ledger source. Parent applied corrections concurrently; the recorded current graph sees zero footnotes and identical stage/delivery hashes. No active changes were made by this audit.

A companion scan exposed 16 paired-caret superscript parser defects: 15 in the ledger, one in inherited MATHEMATICAL_NOTE_COMPLETE.tex. Parent explicitly requested exact source mappings and proposals; the child owns the 15 ledger mappings and two newly exposed ledger link-parser defects. The local source check owns the inherited mapping and source_pr13 link-parser defect.

All 85 href commands in all 239 active files were parsed using balanced braces, with zero parse errors and zero hyperlink commands. Three formula link targets are confirmed by source context: x once, k+1 twice. The other 82 link targets identify external references (53) or source documents (29). The lone raw ^[ is inside a verbatim formula and must remain unchanged. source_pr13 original has four ^[ occurrences: one incorrect hyperlink, one verbatim formula, two correctly escaped text formulas.

LINK_AND_LOCAL_PROPOSALS.json contains both local replacements, exact original phrases/lines/hashes, complete active old strings, the 85 target inventory, and all four PR13 caret candidates. No PDF was built.
