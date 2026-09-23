# Collision coefficients and their mixed-boundary receiver

This is the complete cumulative source extraction for the retained collision-prism results CFF1–35, CF1–67, DP1–43 and BCE1–45. It also includes the actual adelic inputs ABR, GBC1–20 and GSB1–22a, with the existing secondary-boundary diagram. The original source files, independent derivations and sealed standalone reader are retained in `collision_boundary/original_sources`.

The new results are SZ-20260923-968 (BCE1–28), SZ-20260923-969 (BCE29–41) and SZ-20260923-970 (BCE42–45). CFF's earlier identifiers remain unchanged. These are local coefficient and prism results; they do not identify the local complex with absolute syntomic cohomology or establish positivity of the original Weil pairing.

## Integration

Copy `46_collision_prismatic_boundary.tex` and the complete `collision_boundary` directory alongside the current cumulative `MAIN.tex` in `split_zero_rebuilt_20260922`.

Immediately before the existing bibliography, insert:

```tex
\input{46_collision_prismatic_boundary.tex}
```

Inside that bibliography insert:

```tex
\input{collision_boundary/bibliography.tex}
```

The extracted body is grouped so its coefficient macros cannot change earlier chapters. It does not invoke `\appendix`, replace the main bibliography, or alter any equation tag. All new bibliography keys have the prefix `BCE`. Figure paths are relative to the cumulative entry point. A final page break keeps these figures before the bibliography. The live `MAIN.tex` and sealed publication sources were not edited.

The following complete receiving inputs already occur in the cumulative manuscript:

- `45_boundary_tensor_weights.tex`: BW1–24, the original all-prime boundary and tensor weights. ABR, GBC and GSB use this precise input.
- `15_full_finite_support_recollement.tex`: FL1–15, the full finite support spectrum and integral cochain receiver used by CFF28–34.
- `11_mixed_extension_prime_trace.tex`, together with its cited full-base reconstruction, retains the earlier support-boundary conventions. This addition does not replace them.

The copied GSB source was compared byte-for-byte with its pinned public edition at commit `7bb431df02b42681b3c7335fbf272a3771f777ef`, file `workbenches/splitzero-tandem/research-self-audit/supporting_proofs/GLOBAL_SECONDARY_BOUNDARY_EVALUATION.tex`. Its references to earlier public receiving constructions and human sources remain intact. The source bank retains the integral collision algebra and the cotangent/residue predecessors explicitly used by DP and CFF.

## Preservation and validation

DP was converted in full from the sealed Markdown source. All 366 parsed mathematical expressions agree exactly between source and conversion apart from delimiter-adjacent whitespace introduced by the two parsers. Ordered equation tags agree for DP, CF, GSB and BCE. CFF's complete body and CF appendix are retained; only standalone document controls and appendix state were removed. Long filename typography is made breakable in the integrated copy. BCE's only reference changes are namespaced citation keys and the figure path.

`EXTRACTION_RECEIPT.json` binds the source files and records these transformations. `VALIDATION_SUMMARY.json` records compilation against a temporary copy of the current cumulative entry point. The added chapters have no unresolved references, duplicate labels or overfull boxes. Existing layout warnings elsewhere in the cumulative manuscript were not repaired by changing unrelated sources. Selected integration pages, including both BCE diagrams and the GSB diagram, were visually inspected. The separate 13-page BCE reader had already been inspected on every page.

`VALIDATION_MAIN.*` and `validation_render` are local integration checks, not publication payloads. Publish the sealed reader and complete retained source collection through the existing programme publication path. This extraction does not restore any withdrawn exploration or programme timeline.
