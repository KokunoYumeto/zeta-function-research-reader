# Isolated next-phase graph reader: bounded dependency audit

Date: 2026-09-14. Scope: read-only audit of the complete PGS, PGD, sealed PGM v2, PGB and PGMB proof sources, the ten inputs in `source_snapshot/SOURCE_DEPENDENCIES.json`, and the accepted HCD proof. This report does not edit any source or cumulative edition and does not certify every assertion in the entire historical programme.

The five new proof bodies and all ten listed dependencies were read in full. The accepted raw HCD, exact original all-holonomy note, full PSD, complete original arithmetic-input chapter, full HCA and full LHT were also read. Each bounded tool output used for a full reading was checked for truncation; a combined QCV/QPS/index output was truncated and the two mathematical files were subsequently reread individually in full.

## Core proof closure

The ten-file list is not a complete standalone source closure. Four additional complete sources supply direct mathematical inputs to the new calculations:

1. `cumulative_source_v1/sources/holonomy_complete_closure/companion/originals/HCD.tex`: accepted continuous common-image holonomy descent. Its HCD2a–2c constructs the actual finite-source phase bound, HCD9–16 the minimum section and gap, and HCD17–28 the sampled Hilbert source, zero-weight convention, density and completed maps. PGB8–13 and PGB23–26 use these results.
2. `cumulative_source_v1/sources/holonomy_complete_closure/companion/originals/H_NOTE.tex`, SHA-256 `444f82a8fa420e6f471ef448442085f3a93acb137069e1505d155faab051b881`: H9–17 gives the half-density map, Zak transform and inverse, exact source mean and every sampling factor; H39–41 proves the weighted correlation estimate; H49a–g gives the matrix inverse strip and quadrature. These are the concrete definitions and maps invoked by HCD and PGB. HCD's zero-weight-corrected HCD18–28 must follow and govern the older H64 statement.
3. `cumulative_source_v1/sources/holonomy_complete_closure/companion/dependencies/finite_circle/proofs/PSD.tex`, SHA-256 `51102189bcc7a45610464143a5c0bee21c08059c317024e6e856bc7de993fe74`: PSD8–15 proves the original gamma-contour/zeta tail and the strict positivity of every convolution value for k at least two; PSD16–20 records the unchanged Fourier factors. The whole file also proves the discrete density and the sampled full-primary kernel. HCD explicitly declares this exact source a dependency.
4. `cumulative_source_v1/sources/holonomy_complete_closure/companion/dependencies/finite_circle/inherited/arithmetic_input.tex`, SHA-256 `a50b0fb587b644c4ea94dba45b2b423d038f2bfbe7fef188543939ba850e58d2`: A1–A10 proves the original source spaces, theta identities, two-ended continuous Euler inverses, full-jet iteration and original arithmetic section. This supplies the actual existence, domains, range and regularity behind QPS10, MBG3 and the half-density weighted columns.

The exact map dictionary in item 4 is

\[
 R_{\rm ref}=s_h,\qquad
 \varepsilon=j_h(h/g)=\upsilon_h^{-1},\qquad
 R_Z=R_h,\qquad J_Z=J_h,\qquad A=M_s.
\]

The equality of the section formulas follows by substituting this dictionary into A10 and QPS10: both are the same iterated Euler inverse applied to the same theta source `R_h(u)(D) phi_*`. A5–A7 establishes uniqueness and the two-ended estimates, so this comparison retains the original map rather than positing a new Hilbert vector with the desired Mellin transform. HCA5–6 names the same construction but refers back to AG/WBR; adding the whole HCA chapter alone would not supply the missing inverse proof.

The new finite algebra, completion and mixed-kernel calculations otherwise have their proofs in the five new sources themselves: PGS10–32 proves both Schur sections, the residual, consecutive transitions and signed endpoints; PGD3–31 proves all phase-density estimates from the original lower envelope and BT/TG inputs; PGM3–12 proves the exact mixed map, measurable fibre divisibility, its kernel and inverse; PGB3–26 proves the graph-to-average map, completion and its actual kernels; PGMB3–10 proves the three-term isometry and determinant decomposition. No additional unproved positivity or uniform-in-k bound is supplied by this audit.

## Additional assertions introduced by complete historical appendices

If the reader includes every listed dependency in full, it also prints assertions beyond those used to prove PGS–PGMB. Their original proof sources must be included or their exact existing dependency locators must be made explicit. The following list is a claim-to-source map, not permission to omit part of a source or to claim the missing proofs are supplied.

| Printed use | Proof required outside the initial ten files |
|---|---|
| QCV19 and QCV27 apply the gamma-greater-than-two restriction to every actual offcritical zero | Complete LHT1–18 source below; it proves the rational lower bound `Re g > 97/2052` on the entire closed low-height rectangle. PGS already declares gamma greater than two, but the complete QCV appendix makes the broader application. |
| QPS10/HCA5–6, source Euler inverses and theta-section regularity | The complete arithmetic-input source A1–A10 above supplies the proof at the exact same maps. HCA itself additionally introduces certified-Hankel, GF, TC, WBR and total-object dependencies beyond this core. |
| MBG35–37, actual sectorial period maps and transition | Complete FPB and SPG sources below. Their period construction is not used in PGS–PGMB, but MBG's last subsection explicitly uses it. The live FPB differs from the pinned historical copy; do not silently substitute either edition. |
| AT1, tau pushforward and full tensor cohomology | Original Tau Base note equations18–25 and46–48, explicitly declared by AT. |
| AT2–2a, full cyclic cohomology inclusion | Complete arithmetic-input and cyclic-sum sources, explicitly declared by AT. The finite annihilator and polynomial exact sequence are reproved in MBG23 and PGS3, but the full theta cohomology inclusion remains an earlier-source claim. |
| AT22, Gamma quartet lower bound | Complete Deligne-bound/Gamma-audit note named in AT's final source paragraph. The new PGS arithmetic decomposition does not use AT22. |
| CJ8, the regular radius product | Complete CV/TVB (or EP) proof at the named labels. CJ derives the first step directly and then uses that already proved regular identity. |
| TW20–21, preceding lower threshold and penalties | Complete HC/CJ/CV/TVB chain at the named labels; TW's density and norm comparison through TW19 does not need these later assertions. |
| AU32, central balanced-window lower estimate | Complete balanced-window/factor-four source named there. AU14–31 contains the upper comparison proofs internally. |
| TG18–21, original KL allowances and minimum-lift identities | Complete KL source at KL24/27/32. TG7–14 proves the Gamma recurrence used by PGD internally. |
| TG25–28, historical exponential-weight comparison | The explicitly cited Lubinsky–Mhaskar–Saff hypotheses and Hardy theorem; these claims are outside the new graph proof. The source contains a proof of its stated obstruction once Hardy's theorem is available, and gives primary literature locators. |
| Original endpoint NOTE14–29, local zeta lower mass | The note explicitly uses the zeta functional equation and vertical-strip Gamma estimate with DLMF locators. Its three-circles propagation, derivative argument and convolution lower envelope are fully written. BT's complete BI1–26 derives Binet and can support the required Gamma estimate; no assertion is made here that the note itself fully derives the functional equation. |
| Original endpoint NOTE38–42 | Full PR23 endpoint theorem and PR24 confluent transfer sources named with exact commits. These are historical endpoint applications; PGD22 uses the actual lower-envelope proof NOTE14–29. |

## Located additional full sources

All paths in this section are absolute and were verified by a read-only locator helper. LHT and HCA were then read completely by this audit. FPB and SPG are located and hashed, but not proof-audited in this bounded scan.

- LHT: `sources/phase_graph_20260914/reader_snapshot/originals/LHT.tex`, SHA `319478bb43ebf984edb0eff4fd0cb4aacfd588c6cac254b9b01a6f7686196f99`. Complete LHT1–18. A byte-identical snapshot is at `cumulative_source_v1/sources/current_cohorts/snapshots/total_object_live_pin/quartet_critical_values/low_height_theta.tex`.
- HCA: `sources/phase_graph_20260914/reader_snapshot/originals/HCA.tex`, SHA `54465acf93bbd3bb13f4670c258fbcaed7afab4d92de0dfba899617dd232db3f`. The full file includes HCA1–29a and its inserted refinements; HCA5–6 is the section use in QPS. A byte-identical cumulative snapshot is at `sources/current_cohorts/snapshots/total_object_live_pin/certified_hankel_attachment.tex`.
- Live FPB: `sources/phase_graph_20260914/reader_snapshot/originals/FPB.tex`, SHA `88f1e0b49c7d22226ade48bb5ed39fa150f67bf57fbffc63ee6657115b56090f`, complete FPB1–49. Historical cumulative FPB at `sources/current_cohorts/snapshots/total_object_live_pin/full_packet_formal_boundary/full_packet_formal_boundary.tex` has SHA `b7dce3dc82f5449a9d71a9e042cabfb25a9e041569ea44e8705339a6719e2fd0` and different bytes.
- SPG: `sources/phase_graph_20260914/reader_snapshot/originals/SPG.tex`, SHA `8c7947fddfa4ee9e05d69e85ea2a06610f8649b0a3433b74fcf9506031fbd7f0`, complete SPG1–46. SPG13–21 constructs Laplace integrals, exact gauges, Gamma factors and periods; SPG27–29 proves sector transitions; SPG30–32 and43–46 gives the actual theta and transported metric maps. No `*sectorial*` filename was found in the historical cumulative source. The live source is a subsequent-source intake and must be labelled as such.

## Rendering and cross-reference findings

- The raw TG20 source contains literal mojibake `\mathord{\textsf{Î”}}_N` in the displayed coefficient diagonal and its two congruence occurrences. A logged presentation-only replacement with `\Delta_N` must retain the original source and prove exact reversibility of the text replacement. The surrounding formula fixes its meaning as `diag(1,i,...,i^N)`; no mathematical matrix is changed.
- AT requires `\C`, `\cP`, `\Tr`, `\Ga`, `\ar` and theorem/proof environments supplied by its original wrapper. HCD declares `\C`, `\R`, `\av`, `\im` in its standalone preamble. The endpoint NOTE and H_NOTE are complete standalone documents; embedding must preserve proof bodies while extracting preambles and title/TOC commands in a recorded operation.
- Many links in the sources are literal equation names rather than LaTeX cross-reference commands. A clean compilation therefore cannot prove that all theorem dependencies are present. The named-use map above remains necessary even when no `undefined reference` warning occurs.
- BT and endpoint NOTE have several ordinary unprefixed section labels, as do historical standalone notes. The builder should namespace duplicated labels and transport each source's local `\ref`/`\eqref`/`\hyperref` through the same explicit bijection; no source label should be silently rebound to another chapter.

The core proof closure and the additional historical claims are recorded separately because they have different verified scopes. The report makes no claim that the broad Split-Zero/RH programme or the whole historical corpus has been completed.
