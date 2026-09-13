# Gamma cumulative source integration review — 13 September 2026

The complete source integration passes the independent comparisons recorded below. The audited PDF has 478 pages and SHA-256 `9e79bd6cb4f95d845af0f637a1cb4fdcb56ddf32015f89430fa12c530b8b1680`. This review reads integration transformations and exact source data. It makes no new claim to have reread the historical 424 pages or to have visually examined all cumulative pages. No compiler, Pandoc, mathematical checker, Lean, or integration command was run.

## Complete authored bodies

The retained original standalone sources and the five integrated proof bodies were compared in full. For each standalone document, let B be every character between its unique document delimiters. The integration map removes the unique `\maketitle`, maps each original `\section` to `\subsection` and each original `\subsection` to `\subsubsection`, and encloses the entire result in a local group after a new reader section title. Every other character of B, including prose, hypotheses, environments, equations, signs, constants, labels and references, is compared for equality. The source-cost fragment is byte-identical without this map. The original full documents remain separately retained.

| Original source | Source SHA-256 | Complete fragment SHA-256 | Tags |
|---|---|---|---|
| `gamma_exact_coefficient_join_20260913.tex` | `270d7f89e6ac2b147fdbdb5d223125b3744239d43c5485c53740c47ed8d223ec` | `6830ccf4e3a24beae858ae38d46a254c1af350d47741178d63a830b796d005aa` | 59 |
| `gamma_seed_intervals_20260913.tex` | `579c934bc3e6abba27008de20385bc276e10c824a9f7944156a7781eeb7768e7` | `2748e87db064075532fce497435ad3f16bcb3aae3f85d80c646c553cbc6047a6` | 40 |
| `gamma_seed_intervals_20260913_source_costs.tex` | `ca1e162b24842e939dbece5bf12f02e76001baed8bf2bd61a0e02b490a1e7331` | `ca1e162b24842e939dbece5bf12f02e76001baed8bf2bd61a0e02b490a1e7331` | 10 |
| `gamma_finite_metric_transfer_20260913.tex` | `dabcf78af94fc090095f40d2a4e8eda3cf57fdc894ae2078a0a1b3b10afc4836` | `50c3ef9d4398d346fc6bd6b1b9ab4ed596d0d0df5fb6e7615880bb146c7eabdc` | 44 |
| `gamma_phase_fibre_transport_20260913.tex` | `9f6f62da311c0f6c76761ee74e234b3c77d9441e2136908857208e798ac81e76` | `b657394978bebe5745921a8acc24a35bf80875437b737d9d88f3745b80f3fda0` | 29 |

The exact local macro values are retained in their enclosing groups:

`tex/gamma_exact_coefficient_join.tex`: no local mathematical macro definitions.

`tex/gamma_seed_intervals.tex`: `\def\ii{\mathrm i}`, `\def\dd{\,\mathrm d}`, `\def\M{\mathcal M}`, `\def\F{\mathcal F}`.

`tex/gamma_seed_source_costs.tex`: no local mathematical macro definitions.

`tex/gamma_finite_metric_transfer.tex`: `\def\C{\mathbb C}`, `\def\R{\mathbb R}`, `\def\tr{\operatorname{Tr}}`, `\def\diag{\operatorname{diag}}`.

`tex/gamma_phase_fibre_transport.tex`: `\def\C{\mathbb C}`, `\def\R{\mathbb R}`, `\def\HH{\mathcal H}`, `\def\PP{\mathcal P}`, `\def\V{\mathcal V}`, `\def\diag{\operatorname{diag}}`.

The resulting tag sequences are GC.1–GC.59, GS.1–GS.40, GS.41–GS.50, GMT.1–GMT.42 including GMT.29a and GMT.29b, and GP.1–GP.29. The machine report retains every exact tag and line mapping. Full-body comparison also covers mathematical display environments outside ordinary inline/display delimiters; tag equality alone is not used as evidence of complete retention.

## Frozen H and complete earlier sources

All 946 files in `release_20260913h` agree in membership, byte count and SHA-256 with the final plan’s frozen H inventory. Each of the first 18 current source receipt rows equals its pinned predecessor. Every raw source matches its recorded source hash. Every one of the following complete generated appendices is byte-identical to its frozen H counterpart.

| Complete appendix | SHA-256 in both current and frozen H |
|---|---|
| `build/source_pr_8.tex` | `3dc1a74c95d80b658f8b99181a49c84c8c80a3790c6b0e64864eec85ff9a1548` |
| `build/source_pr_9.tex` | `0e3c4b3a54426943274887902a9aada603f6e627dc66d95a6bd8592f7f40ce36` |
| `build/source_pr_10.tex` | `1ab852994335134009a1f4667f1b079cdd326f8691843925f468555983cb184d` |
| `build/source_pr_11.tex` | `7041c607845a3435504bf2e7336bc8c0de573cc2bc4f4fbbd0f6f1317af9b40d` |
| `build/source_pr_13.tex` | `a2c21a6fefd80e80c8bbda36d057809a94ba081b7850d9f3d3737245174f10b5` |
| `build/source_pr_17.tex` | `3a81ec145df102984687e57a07989f5f855103f23ec34691a6a0c799e5ffc12b` |
| `build/source_derived_main.tex` | `ca367b14cb7dcc34de684d9c2e7e689fd0e4c33066979780393f0f699b417bff` |
| `build/source_pr_14.tex` | `4fa10db0c983f9aef88e829408ba18abcf60624ecf4d9d43984b5ec19b720316` |
| `build/source_kernel_layer.tex` | `6b117f87e10c0e78928c22d34ed69f7d6aa1bc676484127286a99e5ef42c180c` |
| `build/source_symmetric_frontier.tex` | `39bf28b2149790b483b4555791b1e4f6ec5c4e67bce52cadc5db36b606c9e238` |
| `build/source_spectral_sum_full.tex` | `36680c326ad7967d9fe7d386460674997c6d3074bad977f8aefd92ef7b011809` |
| `build/source_sum_connection.tex` | `290132218173f4e65a39d0ddb40df9608c0fb6abf78b0118b06e85a93880da7b` |
| `build/source_cyclic_sum.tex` | `d6eccaef9b9f29929435e7ed7ea2792b430b32b04d3d2b88031ce092a175e212` |
| `build/source_exterior_trace.tex` | `07db19308086c2100276e7a293911a12217e74bb5768a1eafdb0894272808780` |
| `build/source_toda_volume.tex` | `5b6415b2667fffc385ad7cf628f60cc3b1f884f0b838d8560ac5bfde1555d417` |
| `build/source_conormal_tower_pasted.tex` | `79870ac6665eb5b2661639f5a6da3878a0a13031a9f666a44a75d5b4282536b3` |
| `build/source_conormal_cyclic_pr21.tex` | `2ed17082b5d9cd8228e212647f103e9fb1d8a6e83f0f98d86ec08695f8af0e45` |
| `build/source_toda_parent_join.tex` | `f36d2fa44f9fa71bb76465ffeb659c2588a9dba09be61b0668c6393bbbbd2019` |

38 inherited TeX inputs outside the deliberately extended main and conclusion retain their exact hashes. The old conclusion and theorem crosswalk are each retained byte-for-byte as a prefix, followed by two newline bytes and their complete authored addition. The complete JSON report records every frozen H file, every configured source/support input, all 268 proposed/applied outputs, and the hashes of all 44 current TeX build inputs (main plus 43 proof inputs).

## Complete delivered Gamma source and its exact display map

The delivered ZIP and all 38 staged members match the final source pins and exact archive bytes; all archive CRCs pass. Both complete alternate witnesses remain unchanged. The reader includes the complete Markdown witness, SHA-256 `886c82e2562d9b4846adb44640d28a34552e38eb2518a3cd47f90dbbedd95e5b`. The original and prepared existing Pandoc trees have exactly the same ordered 223 Math nodes: 60 display and 163 inline nodes. This statement compares their full node payloads; it is not inferred from equal node counts.

Revision 03 changes only the final five-object display in the generated TeX. It adds an `aligned` wrapper, prefixes each of the five original lines with an alignment marker, and inserts a row separator between successive original lines. Its inverse removes precisely those wrapper tokens and alignment markers and replaces those row separators with the original newlines. The inverse recovers the following original character sequence exactly:

```tex
\[
\text{original split-supported polynomial source}
\longrightarrow\text{full gamma product fibre with arithmetic amplitude}
\longrightarrow\text{sum density and retained relative component}
\longrightarrow\text{exact all-tensor arithmetic coefficients}
\longrightarrow\text{the same source--boundary Toda determinant ratio}.
\]
```

There are four original `\longrightarrow` arrows, all in their original order and orientation. The current generated appendix equals the complete saved pre-layout appendix with this one replacement and no other changes. The exact original display SHA-256 is `d48e8fd0b396b343901d4eef27ac7abcd69b6c28b281245efc4b47aa791d8805`; the formatted display SHA-256 is `28153a8231ff5c7fe1eab5be9eec29682c53989a48072844ab1455ec090c1dc7`. This inverse equality concerns the generated TeX display. The separate 223-node equality concerns the original/prepared Pandoc trees; the two checks have distinct explicitly recorded inputs.

## The three recorded layout revisions

The revision receipts are linked by exact input/output PLAN SHA-256 values. Their saved `build_succeeded: false` values describe the prebuild repair state. The later current `BUILD_VERIFICATION.json` and build receipt record the successful 478-page build. This review verifies the latter’s PDF and all input hashes without rerunning it.

### Revision 1

Receipt SHA-256: `c81d40e7acba0723c246d60bd10281a0eeb8cf93fc03e5f5dd0dfb94e93b2e94`.

`layout.diff`

```diff
--- before/gamma_research_conclusion_addition_20260913.tex
+++ after/gamma_research_conclusion_addition_20260913.tex
@@ -42,12 +42,12 @@
 
 \paragraph{Result R39: certified original moments and signed coefficients.}
 Equations (GS.1)--(GS.40) prove the original theta derivative recurrence
-\[
+\begin{gather*}
  P_0(y)=8y^2-12y,\qquad
- P_{r+1}(y)=-2yP_r'(y)+(2y-\tfrac12)P_r(y),\qquad
+ P_{r+1}(y)=-2yP_r'(y)+(2y-\tfrac12)P_r(y),\\
  \mu_{2r}=2\int_1^\infty
  \left|\sum_{n\ge1}P_r(\pi n^2x^2)e^{-\pi n^2x^2}\right|^2dx.
-\]
+\end{gather*}
 Their fully specified positive square tail (GS.18) bounds the
 omitted infinite integer sum at every fixed order. At order two
 and three, the rigorous rational enclosures are
@@ -91,7 +91,7 @@
 $Q_1(k+1)-Q_1(k)=-13\rho/((13k+2)(13k+15))>0$.
 These are exact statements at every tensor degree for the specified
 source polynomial degrees. The analytic seed has the original zero
-arithmetic quotient $\C[S]/(1)$ throughout.
+arithmetic quotient $\mathbb C[S]/(1)$ throughout.
 
 \paragraph{Result R40: finite error propagation to the actual consecutive ratio.}
 The exact polynomial coefficient power and test expansion in
```

### Revision 2

Receipt SHA-256: `41012b47179638b0c4c2cd79d8678cf7a90406e9d03799ead40109e91cc66465`.

`layout.diff`

```diff
--- before/tex/main.tex
+++ after/tex/main.tex
@@ -12,6 +12,8 @@
 \endgroup
 \usepackage{amsmath,amssymb,amsthm,mathtools,mathrsfs}
 \usepackage{longtable,booktabs,array,calc}
+% Compatibility for the complete Pandoc uncaptioned Gamma source table.
+\newcounter{none}
 \usepackage{graphicx,xcolor}
 \usepackage{fancyhdr}
 \usepackage{fvextra}
```

### Revision 3

Receipt SHA-256: `5e2191fddb5f6de58cbecc7556315c5a24b4661d766490034d9992b0e2b690f4`.

`build_paper.py.diff`

```diff
--- before/scripts/build_paper.py
+++ after/scripts/build_paper.py
@@ -465,6 +465,9 @@
     import sys
     for witness in (PASTED_SPEC, PR21_MARKDOWN_SPEC, PARENT_JOIN_SPEC, GAMMA_MARKDOWN_SPEC):
         appendix, row = prepare_pasted_witness(sys.modules[__name__], witness)
+        if witness is GAMMA_MARKDOWN_SPEC:
+            from gamma_source_appendix_adapter import apply_gamma_source_layout
+            row = apply_gamma_source_layout(sys.modules[__name__], row)
         appended.append(appendix)
         rows.append(row)
     (BUILD / "source_appendices.tex").write_text("\n".join(appended), encoding="utf-8")
```

`gamma_source_appendix_adapter.py.diff`

```diff
--- before/scripts/gamma_source_appendix_adapter.py
+++ after/scripts/gamma_source_appendix_adapter.py
@@ -1,2 +1,35 @@
 """Pinned complete Gamma Markdown witness; importing is read-only."""
 GAMMA_MARKDOWN_SPEC = {'key': 'gamma_convolution', 'source': 'sources/web_gamma_convolution_delivery/Tau_Gamma_Convolution_Descent/RESEARCH_NOTE.md', 'provenance': 'sources/local_gamma_continuations/GAMMA_MARKDOWN_SOURCE_PROVENANCE.json', 'title': 'Gamma convolution descent and the original arithmetic coefficient correction', 'sha256': '886c82e2562d9b4846adb44640d28a34552e38eb2518a3cd47f90dbbedd95e5b', 'bytes': 30605, 'revision': '886c82e2562d9b4846adb44640d28a34552e38eb2518a3cd47f90dbbedd95e5b', 'revision_role': 'Complete delivered Markdown witness SHA-256; source-reported Git revisions retain their historical role', 'lean_source_blocks': 0, 'formal_status': 'Complete source witness. Finite checker records are separately retained. No new local Lean execution is claimed.', 'attribution': 'Complete original Gamma Convolution Descent Markdown note delivered on 13 September 2026. Its archive and alternate complete TeX note are retained byte-for-byte. The full local coefficient chapter proves the exact coordinate maps, finite derivative indices, cochain primitive and transform domains alongside this unmodified source witness. Source reports about remote revisions and computations retain the verification scope of their original receipts.'}
+
+
+def apply_gamma_source_layout(builder, row):
+    """Break the unchanged five-object source chain at its four arrows."""
+    import hashlib
+    import re
+    path = builder.ROOT / row['converted']
+    text = path.read_text(encoding='utf-8')
+    original = r"""\[
+\text{original split-supported polynomial source}
+\longrightarrow\text{full gamma product fibre with arithmetic amplitude}
+\longrightarrow\text{sum density and retained relative component}
+\longrightarrow\text{exact all-tensor arithmetic coefficients}
+\longrightarrow\text{the same source--boundary Toda determinant ratio}.
+\]"""
+    if text.count(original) != 1:
+        raise RuntimeError('Expected the unique full original Gamma five-object chain')
+    lines = original.splitlines()[1:-1]
+    wrapped = (chr(92)*2+chr(10)).join('&'+line for line in lines)
+    formatted = '\\[\n\\begin{aligned}\n'+wrapped+'\n\\end{aligned}\n\\]'
+    reconstructed = formatted.replace('\\begin{aligned}\n','').replace('\n\\end{aligned}','').replace('\\\\\n','\n').replace('&','')
+    if reconstructed != original:
+        raise RuntimeError('Gamma chain layout changed original mathematical tokens')
+    text = text.replace(original, formatted, 1)
+    path.write_text(text, encoding='utf-8')
+    row['reader_layout_refinements'] = [{
+        'scope': 'The complete final five-object chain in source section 10.',
+        'operation': 'Aligned rows at the four original rightward arrows; every original token remains in its original order.',
+        'original_display_sha256': hashlib.sha256(original.encode()).hexdigest(),
+        'formatted_display_sha256': hashlib.sha256(formatted.encode()).hexdigest(),
+        'inverse_layout_reconstructs_original_display': True,
+        'raw_source_and_prepared_Pandoc_math_nodes_changed': False}]
+    return row
```

In revision 01, expanding the intended field notation from `\C` to `\mathbb C` supplies the complex field already used in the complete proof; the original seed quotient is still `\mathbb C[S]/(1)`. The recurrence and moment integral retain every term, sign, coefficient and endpoint. Their surrounding display changes to `gather*`, with the spacing after the recurrence replaced by a line break. The exact equality comparison admits only these two replacements.

In revision 02, the added `none` counter supports the already generated uncaptioned longtable wrapper. No source table cell, caption, mathematical expression, or proof body is replaced. Removing its exact comment and declaration recovers the complete saved pre-revision main file.

The current builder was read in full. Its additions list the five complete proof inputs, import the Gamma witness, append that witness to the existing source loop, and apply the exact layout map only when the witness is `GAMMA_MARKDOWN_SPEC`. Existing source preparation paths remain identical. The current main input order is exactly the builder’s 43-item `REQUIRED` sequence.

## Build and visual scope

The current successful build receipt has zero LaTeX warnings, font warnings, missing characters, overfull boxes and undefined controls. Its underfull count is 70. This records existing compilation evidence, not a new compilation or visual acceptance. All-page visual approval remains false in this audit until the final exact-PDF QA receipt is supplied and bound.

The separately supplied complete proof reviews remain the evidence for the mathematics within the new chapters. This review establishes that those final complete bodies and the original source witnesses survive the cumulative integration.

## Independent exact-node review

The complete independent source-chain review and its comparison program were read. Its 33 comparison results pass, and every input pin and all 223 per-node payload hashes were recomputed here against the inspected sources. Its stronger comparison identifies exactly one changed generated Math node before the inverse (node 221), then proves strict ordered type-and-payload equality among all 223 original AST nodes, prepared AST nodes, alternate original NOTE.tex spans, and restored generated TeX spans. Its whole-file byte comparison also proves complete pre-layout file reconstruction. No whitespace is stripped from any mathematical payload.

The source receipt’s preliminary inline regex count of zero counts only backslash-parenthesis markup in Markdown; the complete AST and both TeX representations instead establish the actual 163 inline nodes. This audit uses the latter exact node count.

Independent review `work/gamma_chain_integration_review_20260913.md` SHA-256 `bad5a0284f1979c3d85b97d1f3323bd2eb6d96226409456ebfca929000afc0db`; receipt SHA-256 `399cd528041daf486b18e0d9c2532034856aeaf937a0e64aa352dd5d15a9ca6f`; comparison driver SHA-256 `15b0e54330ff4ba0cc16b7e4c8d29081a47d51fa39278db4297a1e6629643f31`. The complete review text and structured receipt are embedded in the machine report for packaging independence.

Machine-readable full record: `build/source_audit_20260913i.json`. Reproducible read-only comparison driver: `work/gamma_final_integration_audit_20260913.py`.

## Exact collector projection

The collector projection is appended to the complete machine audit. Every pre-existing rich-schema field and value remains unchanged. The scalar `pdf_sha256` is the independently checked `pdf.sha256`; `proof_fragments` is the integer 43. The `checks` array is exactly the 44 current TeX inputs, including `tex/main.tex`, with each `matches: true` supported by equality of its actual SHA-256 to both the current build receipt and the prior complete audit. The `sources` array is exactly the 19 current source-note rows. Each records its package-relative original path, actual original hash, `original_preserved: true`, converted path and actual converted hash. The converted hashes are checked against the 18 frozen-H comparisons and the separately audited Gamma conversion. No source, proof, build or visual receipt is modified.

The pre-projection complete audit SHA-256 is `e5ba06daa979e1506619a17c6b21d8c99e032411878b21046283d1a577fbde9d`; its full review SHA-256 is `da06193b652329ba43065f46ff5e7cd2a327ea08875bc6eae472d8e43f3d709e`. The read-only projection driver is `work/gamma_source_audit_projection_20260913.py`, SHA-256 `cb26b0dd9701563bc211c2270bb5c4f2ebe45c5febbbbaea4109ee814dcb1c42`. The inspected collector contract is `work/gamma_edition_workflow_20260913.py`, SHA-256 `d881c7ebdbfee984b8eead90cb78a1f4e90693c8748f4210d3dc4be55e8978f9`. This is a typed projection of verified source data, with the complete previous audit retained, and performs no compiler or mathematical-checker execution. Cumulative visual approval remains awaiting the separate final QA binding.

## Final exact-PDF visual evidence binding

The earlier pending-visual statements above record the source audit’s state before this final binding. The completed team review is now bound to this same 478-page PDF, SHA-256 `9e79bd6cb4f95d845af0f637a1cb4fdcb56ddf32015f89430fa12c530b8b1680`. The consolidated receipt `build/qa/visual_review.json` has SHA-256 `57929b33bc93d9f6b7767840133a9062b0014f28bc071a3b77a0f06cb6c719d4`; the render receipt has SHA-256 `adb69fbbdc1ed42e0e333b289dd35dc92cb93deabd4dc915dd7d9109f2564008`. The four complete original reviewer records were checked against their exact hashes and against their complete embedded values in the four typed wrappers. Their contact coverage is exactly physical pages 1 through 478, on all 80 renderer-declared contact sheets. The 44 additional native page inspections are 1, 8, 14, 24, 48, 53, 56, 86, 87, 88, 115, 120, 144, 183, 225, 234, 235, 237, 238, 240, 263, 274, 275, 282, 283, 284, 301, 302, 317, 318, 343, 344, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478.

This binding independently rehashes all 124 actually viewed image files (80 contacts and 44 page PNGs), matches the exact component PDF hashes and page ranges, and checks the 54-file public visual fragment. It does not constitute additional page viewing by this source-audit agent. All-page visual approval is attributed to the completed four-reviewer evidence; the source/proof conclusions remain supported by their separate full audits.

Recorded nonblocking observation: Inherited physical page317 has a heading followed by the word Let before its formula continues on318. Both pages were inspected individually; the complete source remains readable. This minor inherited paragraph break is recorded, not described as absent.

The pre-binding complete audit SHA-256 is `668ec47c98b5aed164a22bf300a35326545e137443570acc7ee66b224ee490af`; the pre-binding full review SHA-256 is `0e2ade2124c6fcef7f41b5fa7efc80a2c29c34e08b1c4b917be68b8b9902e8f3`. All existing source mathematics, original/full-body records and the exact 44-input/19-source collector projection remain unchanged. The earlier false visual flag is retained explicitly as historical data. No source, proof, build, render, raw reviewer record or frozen H file was edited. No compiler, renderer or mathematical checker was rerun. Binding driver `work/gamma_source_audit_bind_qa_20260913.py` has SHA-256 `ad18ddb4a631d6db327b8da4afb75468970c806c028111061500c5982a69f286`.
