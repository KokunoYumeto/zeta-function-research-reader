# Static TeX assembly audit

Audit date: 18 September 2026 (Europe/Berlin). Read-only source inspection; no TeX compilation and no mathematical source edits.

## Result

The twelve inspected additive fragments can be inserted into each of the three cumulative staging documents without a new label, explicit equation-tag, bibliography-key, environment, or macro-namespace conflict found by this static audit. All explicit references in their combined namespace resolve. The cumulative host preambles satisfy the macro dependencies. Citation coverage is complete after the specified new `human:dlmf1` entry is inserted.

The preceding balance and namespace findings do **not** certify that the raw fragments compile. Two preserved raw inputs have TeX syntax faults: LT6 writes an indexed diagonal matrix with the invalid double superscript `...^D^{-1}`, and the scalar reconstruction contains a form-feed byte followed by `rac{m^2}{8n^2}` in place of the fraction command. The accepted raw files and sealed snapshots retain those exact bytes. The assembly repairs only the rendered derivatives, with each repair recorded in `INSERTION_MANIFEST.json`. The later generated-edition check and exact preservation analysis are in `FINAL_INTEGRATION_CHECK.md` and `FINAL_INTEGRATION_CHECK.json`.

The inherited cumulative sources have one presentation ambiguity described below. The parent explicitly requires preservation of the inherited bytes and GEL tags. No repair of that inherited material is requested or performed.

## Fragment checks

Machine evidence is in `source_audit.json`, produced by `audit_sources.py`. Each file record contains the SHA256 of the exact bytes inspected. The sources changed during the audit, so those hashes, rather than elapsed time, determine whether this report applies to a later revision.

| Fragment | Labels | Explicit equation tags | Explicit references |
|---|---:|---:|---:|
| `transport/LRC_TRANSPORT_COMPLETE.tex` | 2 | 58 | 0 |
| `equilibrium/quantile/LRC11_LRC12_FULL_PROOF.tex` | 11 | 0 | 13 |
| `equilibrium/EQUILIBRIUM_NORM_PROOF.tex` | 2 | 54 | 0 |
| `attained_tail/gpa/GPA_ATTAINED_TAIL_PROOF.tex` | 1 | 28 | 0 |
| `attained_tail/ATTAINED_FIBRE_AND_PROFILE_PROPAGATION.tex` | 1 | 40 | 1 |
| `asymptotics/LRC_SCALAR_RECONSTRUCTION.tex` | 1 | 31 | 0 |
| `attained_tail/ALL_NONZERO_ROW_ENVELOPE.tex` | 1 | 22 | 0 |
| `PROFILE_COVARIANCE_BRIDGE.tex` | 1 | 19 | 0 |
| `joint_review/elliptic/ELLIPTIC_DERIVATIVE_PROOF.tex` | 0 | 0 | 0 |
| `joint_review/FINITE_COMPARISON.tex` | 0 | 0 | 0 |
| `RECEIVER_UPDATES.tex` | 1 | 12 | 0 |
| `forward_source_support_20260918/citation/prepared/WEIGHTED_CONDUCTOR_FORWARD_CITED.tex` | 1 | 36 | 0 |

All paths except the final WCF row are relative to `work/dual_web_intake_20260918`; the WCF row is relative to `work`.

- No duplicate labels or explicit equation tags occur within or across these fragments.
- Every `begin`/`end` environment is balanced and correctly nested. Braces, explicit TeX groups, and displayed-math delimiters balance.
- None contains a document class, package load, document wrapper, nested input, or bibliography environment. Preserve them as input fragments.
- Quantile references resolve within the quantile fragment. The attained-tail reference at line 212, `eqreview:powerexponential`, resolves to the equilibrium fragment at line 601 in its final citation revision.
- The environments used are `equation`, `gathered`, `cases`, `split`, `bmatrix`, and `aligned`; no theorem-environment definition is required by these fragments.
- The only macro definition introduced by the fragments is the scoped `providecommand` for `rank` in WCF, line 3. It does not override the host definition.

## Assembly requirements and presentation details

1. Retain a host preamble with `amsmath`, `amssymb` (or `amsfonts` with the required symbols), `mathrsfs`, and `hyperref` (or `url` if hyperlinks are otherwise unnecessary). The existing three cumulative drivers already have the required packages.
2. Retain the seven existing cited entries `human:globalization2026`, `human:splitzero2026`, `human:dlmf18`, `human:dlmf5`, `human:lyons2003`, `human:boyd-vandenberghe`, and `human:szego1975`. All seven are present in each cumulative document. Add the new `human:dlmf1` entry as described below. Do not append duplicate copies from the standalone transport bibliography.
3. Give the quantile and equilibrium fragments an appropriate assembly-owned section heading if they follow transport. Both begin with `subsection` at line 5. Without an intervening section, their subsections belong to transport's preceding section. This is a heading-level assembly matter; no mathematical text needs changing.
4. If the nearby transport standalone wrapper is reused or distributed as a buildable target, its preamble needs `mathrsfs`: `transport/TRANSPORT_STANDALONE.tex` loads only `amsmath,amssymb` and `hyperref`, while `LRC_TRANSPORT_COMPLETE.tex` uses `mathscr` beginning at line 550. This omission does not affect the cumulative drivers, which already load `mathrsfs`.
5. The added elliptic derivative fragment begins with `subsection`, and the finite-comparison fragment begins with `paragraph`. Their requested placement after PCB has the intended hierarchy and introduces no package, bibliography, or namespace dependency. Neither file contains explicit labels, tags, references, or citations.
6. `ALL_NONZERO_ROW_ENVELOPE.tex`, placed after LRS and before PCB, has label `sec:AER`, tags AER1 through AER22, balanced groups and three `gathered` environments. It adds no package, bibliography, or explicit-reference dependency. Its inspected SHA256 is exactly the accepted `122363522109e864d891f2190a62e4b7e708638cfc7892cda0927a6342a4f684`.
7. `RECEIVER_UPDATES.tex`, placed after finite comparison, is a balanced section fragment with label `sec:DRU` and tags DRU1 through DRU12. It introduces no citation or package dependency. Its latest inspected SHA256 is `030b939b47a529596004e77e2d913b9d4b85ea700729ba7b52410702f8d8d902` (169 lines); it changed while the root author finalized it, so the machine snapshot should be compared with the assembled pin.

## Final cited WCF and bibliography addition

The final WCF input is `sealed_inputs/01_WEIGHTED_CONDUCTOR_FORWARD.tex`, SHA256 `a21b1be2641978c992e9413090fd03fdfd974426043d02885594f51be6490841`. The original WCF was checked first; the final twelve-fragment inventory substitutes this derivative with additional citations. Its labels, equation tags, structural dependencies, and scope remain the same.

The supplied verifier was inspected and run without `--seal`, so it performed read-only checks. It returned PASS: six marked citation-only insertions total 1,821 bytes, and deleting exactly those spans restores original SHA256 `d86dcb3daf13c9b2d5a0aaa4d72cce35a1aff48066ad69c7d9846b9d097dc354` byte for byte.

The accompanying `BIBLIOGRAPHY_ADDITIONS.tex`, SHA256 `1e3c71468a97eade8e4a2a6e0341e4e19c44a6e4d1c7fb866f784d9fdfad35f5`, is a balanced integration snippet with one `bibitem` and no wrapper. Its two `WCF_BIB_APPEND` spans are unlabelled additions inside the existing `human:dlmf18` and `human:dlmf5` entries. They must not be pasted as freestanding bibliography entries. Insert the `WCF_BIB_NEW human:dlmf1` span once, assigning the parent's requested display label H25. Neither that key nor the H25 display label is occupied in any of the three cumulative hosts. Existing hyperref support covers every added URL.

The final equilibrium citation revision, SHA256 `68a875669b638bd099dda175df3345e49382b5fc07a232c1eb93f6393641dfc9`, cites `human:szego1975` at lines 409 and 716. That entry already has display label H24 in each host: 09 line 79338, 10 line 79505, 14 line 69712. No new Szego entry is needed.

## Cumulative namespace checks

The audited cumulative files are under `work/mixed_tail_continuation_20260917/full_receiver_build/staging`:

- `09_UPDATED_JOINT_NOTE.tex`
- `10_UPDATED_SIGNED_RETURN.tex`
- `14_CURRENT_KERNEL_AND_MULTIPLICITY_PROOFS.tex`

Each has one document class and one balanced document wrapper, balanced environments and braces, no duplicate labels, and no undefined local explicit references. None of the inspected new fragments collides with a cumulative label or explicit tag. The staging evidence is in `staging/audit_staging.json` and `staging/integration_namespace_audit.json`.

### Inherited GEL ambiguity retained exactly

The two distinct sections below both display equations numbered GEL1 through GEL13 in cumulative documents 09 and 10. Their LaTeX labels are distinct; this is a displayed-tag ambiguity, not duplicate label keys. Preserve all inherited bytes as instructed by the parent.

| Cumulative file | Earlier section | Later section |
|---|---|---|
| `09_UPDATED_JOINT_NOTE.tex` | `The exact Gamma ensemble and the leading growing return`, section heading line 4799, label `sec:GEL` line 4800; duplicate tags at lines 4808–5072 | `Uniform elliptic endpoint estimates with the original quarter shift`, heading line 70005, insertion label `GRBUILD:ELLIPTIC_UNIFORMITY_BODY:start` line 70002; duplicate tags at lines 70009–70314 |
| `10_UPDATED_SIGNED_RETURN.tex` | Same earlier title, heading line 4966, label `sec:GEL` line 4967; duplicate tags at lines 4975–5239 | Same later title, heading line 70172, insertion label `GRBUILD:ELLIPTIC_UNIFORMITY_BODY:start` line 70169; duplicate tags at lines 70176–70481 |

Document 14 contains no duplicate explicit equation tags. No added fragment uses a GEL tag.

## Limits

This is a lexical and manual assembly audit. It does not validate the mathematics, external bibliographic claims, plain-text references to equation names, page layout, line overflow, PDF hyperlinks, or successful engine compilation. Required mathematical checks belong to the proof auditors. This audit introduces no permission gate and no source changes.

All announced additions have now been received and inspected. The proposed bibliography placement is checked against the original cumulative sources; inspection of the actual assembled insertion is the assembling agent's final check. This audit does not claim that a future assembled derivative has already been compiled.
