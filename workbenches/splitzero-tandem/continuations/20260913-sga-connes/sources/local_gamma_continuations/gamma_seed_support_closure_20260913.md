# Complete Gamma seed support closure

All 90 members of the final seed manifest were checked against their exact bytes and SHA-256 hashes. The recommended support list contains **89 files, 6,494,916 bytes**: 88 original manifest members plus the original manifest. The two remaining original members are the complete GS.1–GS.40 and GS.41–GS.50 proof sources, already handled by `PROOFS`. **No original manifest member is excluded.**

Use `support_files` in `gamma_seed_support_closure_20260913.json` for the exact finite list. `included_support` supplies each original path relative to `work`, byte count, SHA-256, roles and byte-preservation requirement. `dependency_edges` records 316 explicit source, execution, build and review relationships.

| Retained material | Count |
|---|---:|
| Original executable scripts | 7 |
| Positive and mutant JSON outputs | 18 |
| Exact stdout and stderr files, including empty stderr | 36 |
| Replay / endpoint-transport validation receipts | 2 |
| Complete mathematical and implementation review | 1 |
| Original standalone wrapper | 1 |
| Final standalone PDFs | 2 |
| Render receipts and completed visual-review receipt | 3 |
| PNG images named by render receipts | 18 |
| Original 90-member handoff manifest | 1 |

## Required input and placement

The source-cost checker reads the default sibling `gamma_seed_intervals_20260913_normal.json` at lines 63 and 67–69 and rejects changed bytes. Its SHA-256 is `8688e782d2283c8c236678c75785a6170504b5317067f7bb91cc237e67b616d1`. Keep it beside `gamma_seed_intervals_20260913_source_costs_check.py`, whose sealed SHA-256 is `cd8a83921958727f85f36896c5794d8292358cdc56b3f017302324724b6fa63b`. An explicit `--input` may change the path, but the accepted data must have that identical hash. No source script in this family refers to `original_normal.json`; do not substitute or rename the actual default.

Preserve both complete original proof sources as sibling copies in public `work` through `PROOFS`. The replay scripts hash those original basenames, and the retained standalone wrapper inputs the source-cost fragment by its original basename. Preserve all QA subdirectory paths. Keep the JSON input and receipts byte-identical, including their original line endings.

Both final PDF files are retained because the original manifest and passed visual review refer directly to their exact bytes. All 18 PNGs remain because the render receipts enumerate their hashes, even where only a contact image was actually viewed. The render receipts retain their historical `pending actual viewing` text; the later passed visual-review receipt binds those exact receipts and records completed inspection.

## Sources outside the seed manifest

The complete review cites these three additional inputs. All exist and match its recorded hashes. The inherited H proof already supplies the first. The complete Gamma delivery must retain the other two under their existing `sources` locators. These are source-review dependencies; neither seed checker imports or executes them.

| Origin relative to workspace | Bytes | SHA-256 |
|---|---:|---|
| `work/toda_theta_input_tail_20260912.tex` | 23584 | `e50a11c51293017b1a433f3ed9b499947a953e6b2955f59f3c46f14ed26a409d` |
| `output/split_zero_rh_tandem_2026-09-12/sources/web_gamma_convolution_delivery/Tau_Gamma_Convolution_Descent/RESEARCH_NOTE.md` | 30605 | `886c82e2562d9b4846adb44640d28a34552e38eb2518a3cd47f90dbbedd95e5b` |
| `output/split_zero_rh_tandem_2026-09-12/sources/web_gamma_convolution_delivery/Tau_Gamma_Convolution_Descent/evaluate_seed_coefficients.py` | 2071 | `50986940edea09082d692746d261d672d0cf309ad4f49da9428760272c6f1dc8` |

## Exclusions and execution boundary

Only these seven unmanifested files are omitted. The original handoff already excludes all of them; exact hashes and sizes are retained in the JSON inventory for this local audit.
- `gamma_seed_intervals_20260913.aux`: Native standalone TeX build intermediate/log; generated again from retained complete TeX. Public render receipt preserves final log counts and PDF/PNG hashes.
- `gamma_seed_intervals_20260913.log`: Native standalone TeX build intermediate/log; generated again from retained complete TeX. Public render receipt preserves final log counts and PDF/PNG hashes.
- `gamma_seed_intervals_20260913.out`: Native standalone TeX build intermediate/log; generated again from retained complete TeX. Public render receipt preserves final log counts and PDF/PNG hashes.
- `gamma_seed_intervals_20260913_log.md`: Private lane continuity log; complete public mathematical review and execution/render receipts are retained.
- `gamma_seed_intervals_20260913_source_costs_standalone.aux`: Native standalone TeX build intermediate/log; generated again from retained complete TeX. Public render receipt preserves final log counts and PDF/PNG hashes.
- `gamma_seed_intervals_20260913_source_costs_standalone.log`: Native standalone TeX build intermediate/log; generated again from retained complete TeX. Public render receipt preserves final log counts and PDF/PNG hashes.
- `gamma_seed_intervals_20260913_source_costs_standalone.out`: Native standalone TeX build intermediate/log; generated again from retained complete TeX. Public render receipt preserves final log counts and PDF/PNG hashes.

The original render drivers require a native `.log` after rebuilding the corresponding standalone TeX. Their public receipts preserve final warning counts, PDF hashes and rendered image hashes; native build logs are not included. The original sealing script is retained as execution provenance. Its directory glob and visual attestation should not be rerun over a different public support set to replace the historical manifest or review.

This task read all seven scripts and the complete mathematical review, parsed existing public receipts, and checked file hashes and dependency paths. An independent read verified all 90 manifest members and 118 explicit receipt references, with no missing target. No checker, replay, renderer, build, sealing script or Lean run was executed. No cumulative-reader file was changed.

Inventory SHA-256: `c8201653f66065af0cb7f7eaf69de42a24e7c1457956ddf1fb8d7cad61940867`.
