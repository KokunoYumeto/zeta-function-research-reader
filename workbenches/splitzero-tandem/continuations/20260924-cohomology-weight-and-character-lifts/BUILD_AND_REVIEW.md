# Build, source preservation and review scope

This record accompanies the three complete readers in the **Split-Zero cohomology and zeta-function research programme**. The edition preserves programme proofs, editable LaTeX, Markdown where available, and reproducible figure sources. It does not redistribute human-author archives solely because they are accessible on arXiv, and it excludes private correspondence and verbatim conversation corpora.

## What the mathematical checks establish

Review here means a recorded AI mathematical check of the identified source passages. It is not human peer review, a proof-assistant kernel check, a proof of RH, or automatic validation of subsequent claims that use the checked result. A compilation check establishes that the document builds, not that its mathematics is true.

The **owner** is the AI task that produced the contribution. Its **root** is that task's coordinating agent; an independent check is a separately delegated AI review. A **publication-stage** check is performed while integrating the three contributions into this edition. These roles are reported separately so an author check, another AI's check and a document-build check are not conflated.

### Geometric weight control

The cumulative contribution reconstructs Deligne's argument and supplies the programme's geometric coefficient, localization, cover and continuous-dual calculations. Its accepted final batch comprises **ADC0–ADC9, DCA0–DCA12 and ACD0–ACD8**, after the earlier LNC/LVD/RGR batch. The owner records complete readings of these three new arguments and independent checks of their final maps, full-sheet corrections, topology and dual signs. The exact incoming versions were:

| Source proof | Incoming SHA-256 | Recorded scope |
| --- | --- | --- |
| `CC_ADJOINT_DEFECT_INVARIANT_CYCLE_CROSS.md` | `9ac7f6bf9ab3e5ee78ab1fac4f26a403a4c956f5f0616e53c5d198c017116373` | ADC0–ADC9, including the full-sheet and continuous-dual comparisons and endpoint maps |
| `CC_ADJOINT_DEFECT_COVER_ACTIONS.md` | `57dd9dc63240deb26ac233d5bf7e67e83798d4447b88ef0d6689293649fdaecb` | DCA0–DCA12, including finite-branch topology, cut homotopies, compositions, source extension and endpoint factors |
| `CC_ADJOINT_DEFECT_CONTINUOUS_DUAL.md` | `1373884c33e74aea9c0d48404152b16812b434b6cc4760227c8596666e919fda` | ACD0–ACD8, including the strong coefficient dual, fine resolution, signs, local/global source maps and sphere orientation |

These are incoming mathematical-review identifiers, not assertions that the publication derivative has unchanged bytes. Portable links, point-of-use citations and typesetting can change a published file's hash. The edition's current hashes belong to [MANIFEST.json](MANIFEST.json) and the geometric [proof-input manifest](gct-weight-control/proof_inputs.json).

The additional publication-stage mathematical check covered the preceding **LNC0–LNC11, LVD0–LVD9 and RGR0–RGR12**, together with selected dependencies. That is not a new full independent audit of every part of the cumulative reconstruction. The latest cross proves the specific source and comparison maps; it does not prove the arithmetic obstruction vanishes. A current-side quotient can vanish independently of the primal defect.

The publication-stage reviewer also read the complete **ADC0–ADC9, DCA0–DCA12 and ACD0–ACD8** texts and their receipt, verified the three incoming hashes above, and found no concrete mathematical defect in the checked new derivations. A separate componentwise check verified DCA3, DCA6 and DCA7 for every positive integer cover degree, including both residual homotopies, variation signs and the degree-one case. It did not use numerical sampling as proof. This coverage concerns these supplied derivations and covariance identities, not a fresh proof of every imported arithmetic or analytic foundation or a new complete reading of all cited human papers.

The [Deligne reading log](gct-weight-control/DELIGNE_FULL_READING_LOG.md) distinguishes the complete 116-page French transcription reading, the separately attributed peer reading of the original published pages, and upstream SGA or other references that were not newly reconstructed in full. Formula-level source discrepancies and unresolved checks are retained. The transcription is not described as Deligne-authored TeX.

### Positive quotient and source reconstruction

The [PTQ review](geometric-positive-quotient/POSITIVE_TRANSFER_UNIVERSAL_QUOTIENT_REVIEW.md) explicitly covers **PTQ0–PTQ4 and PTQ8**, plus **PTQ5.3–PTQ5.4** where used in the trace calculation. It does not claim a separate complete audit of all PTQ5–PTQ11. Its incoming proof hash is `b70a8f0edf765dcfb3259735eb4a8f90a31c649ad308f55d821dcf5cccdae930`.

The [PSC review](geometric-positive-quotient/POSITIVE_QUOTIENT_SOURCE_AUDIT.md) covers **PSC0–PSC9** at accepted incoming hash `2d188377c6b694e363e5b32a331a8af2ef4562d2cb8aab272d0ce1149b6f1171`. It records the corrections to the precise topology of the source fibre product and to the separator comparison in PSC6. Its source and dependency readings are listed in that review, rather than generalized into a claim that the whole bibliography was reread.

The Hilbert-space classification is for the specified value space, including the multiplicity convention; it is not a classification of unrestricted forms on full local jet algebras. The original complementary Weil contribution remains in the source calculation. Positivity after quotienting does not prove its vanishing.

The received **RGR0–RGR12** and **GDC0–GDC14** have the [complete GDC verification](geometric-positive-quotient/GYSIN_DEFECT_ROOT_VERIFICATION.md). The incoming GDC hash is `5d0f471b3250e4ee894caca68232c556d64a137a49a9fe25a641db61b94f79ab`; the verification hash is `a3c47e1cfac228e1c23dee2d121cb66b4eb9d109e95334c66f4705eff828d473`. The owner records reading every section and formula, followed by verification of the strengthened restriction topology, scale bounds, and restoration of both endpoint lines. A separate reviewer read the complete RGR argument and independently derived the scale ratio, strong annihilator and strong-open restriction results. That initial receipt did **not** claim a complete independent audit of the final written GDC text. The later accepted [AST0 record](geometric-positive-quotient/ADJOINT_DEFECT_SOURCE_TOPOLOGY_COMPARISON.md) supplies that additional full GDC0–GDC14 reading and check, including the final repaired text and a separate GDC7/SDT4 constituent check. This strengthens the recorded coverage without changing what the earlier receipt established. The proof gives the actual closure and quotient comparison; it does not prove the original Gysin defect vanishes.

The final source extension adds **AST0–AST9, CFP0–CFP12 and CFPA, and CPS0–CPS8**. It closes the earlier restriction to forms bounded for a selected value Hilbert norm: CFP classifies all jointly continuous positive transfer forms on the actual original Fréchet source. CPS calculates their common radical and positive completion and proves that the actual specialization quotient \(R=Q/N_O\) has only the zero compatible positive form. It does not prove \(R=0\), identify the generated positive topology with the original source topology, or remove the complementary original Weil term.

| Final incoming source | Incoming SHA-256 | Recorded mathematical check |
| --- | --- | --- |
| `ADJOINT_DEFECT_SOURCE_TOPOLOGY_COMPARISON.md` | `1b38252f2816901d49e87e212db102833c8d6ce5d7a90a655f62860d50b0c89e` | Actual specialization source and topology, including AST0's complete final GDC reading |
| `CONTINUOUS_POSITIVE_TRANSFER_FORMS.md` | `ce8da36c1c6a61acbd2a083751cd86597b4dbb8d2940892592a458f242034d1e` | Complete owner-root verification of CFP0–CFP12 and CFPA, following a separately derived source proof |
| `POSITIVE_SOURCE_COMPLETION_AND_SPECIALIZATION.md` | `d6eed5950b21e72365741b7da81955f41f89beff67d6004f9d5c7b3609fd79b0` | Independent full CPS0–CPS8 review; not a new independent reconstruction of every ancestor |

The included [CFP root verification](geometric-positive-quotient/CONTINUOUS_POSITIVE_FORMS_ROOT_VERIFICATION.md) and [CPS independent review](geometric-positive-quotient/CONTINUOUS_POSITIVE_FORMS_INDEPENDENT_REVIEW.md) give their exact scope and dependencies. These hashes identify the incoming mathematical texts. Point-of-use classical citations and portable links in the publication derivatives change their byte hashes, recorded in the final manifest; they do not convert an author-root check into a second complete independent CFP audit.

A further **publication-stage independent check** subsequently read the complete incoming CFP0–CFP12/CFPA and CPS0–CPS8 texts at the two hashes above and checked their new displayed derivations. It found no concrete mathematical defect. Its checks include CFP2's continuous action, CFP3–CFP4's source integral and annihilator, CFP5–CFP8's spectral support, one-dimensional receiving fibres and polynomial weight bounds, CFPA's positive Fourier-measure argument, and CPS1–CPS7's radical, completion and specialization calculations. It identified one internal reference correction in CPS5: the strict strong-dual row is AST3.5, while AST2 proves its kernel identification. The previous source reconstruction, exact isolators, classical zero count and functional equation, specialization identification, and AST/GDC strong-dual topology remain named dependencies; this check is not a new complete independent audit of those ancestors. In particular, it does not turn \(\mathscr P(Q/N_O)=\{0\}\) into \(Q/N_O=0\).

### Original-character lifting

The accepted character-lifting reader includes **MCL0–MCL11, ORE0–ORE10, RPC0–RPC8 and SCT0–SCT6**, together with the **RQC0–RQC4** residue-pushout check and **OEC0–OEC5** original-extension sign check. The included [pushout check](original-character-lifting/tau_lifting_weights_20260924/ACTUAL_RESIDUE_PUSHOUT_INDEPENDENT_CHECK.md) records a full RPC0–RPC7 reading; its stated scope is not silently extended to RPC8. The [sign check](original-character-lifting/tau_lifting_weights_20260924/ORIGINAL_RESTRICTION_EXTENSION_SIGN_CHECK.md) records a complete ORE0–ORE10 reading but verifies specifically ORE5.5–ORE5.8 and ORE8.8–ORE8.10 against the original Mellin lifts.

No completed additional publication-stage independent audit of this entire cumulative reader is claimed. The supplied source-level checks remain evidence for their stated passages, not certification of every older section or a transferred purity theorem. The full original target, the specified quotient, the Gamma germ, multiplicities and the supported contribution at −1/2 remain distinct through their calculated maps.

## Classical-source attribution

The source notes and [RESULTS.json](RESULTS.json) identify Deligne, Connes–Consani, Meyer and Reich at their points of use. The publication pass also adds explicit classical attribution for Hahn–Banach extension, the Fréchet open-mapping theorem, the zero-count input and the Guinand–Weil formula. The inspected Fréchet reference states its extension rather than proving it in full. The older Guinand and Weil papers are credited through an inspected Connes author-TeX witness; no new complete reading of those originals is claimed.

The final independent reviewer also compared the full arithmetic formula with the author TeX of [Connes–Consani, *Spectral Triples and Zeta-Cycles*, arXiv:2106.01715v1, §§2.1.1–2.1.2](https://arxiv.org/abs/2106.01715v1), lines 215–270 of `Spectraltriples.tex`. The precise convention change is \(F(x)=h(\log x)\) and \(A(s)=\widehat F((s-1/2)/i)\). Both endpoints, the prime-power factor \((\log p)p^{-m/2}\), and the positive archimedean term agree with the retained formula \(W=A(0)+A(1)+\mathcal A_\infty-P_{\rm hist}\). This is a completed publication-stage source comparison, not a retrospective claim that the earlier derivation had cited this witness. The reading was of those sections, not the whole paper; Guinand's and Weil's original articles are not described as newly inspected. The programme's separate finite-divisor cutoff retains its original pole and trivial-zero terms.

ADC8 and ACD1 also cite the complex Hilbert-space Riesz representation theorem and its conjugate-dual convention: [Tao, *245B, Notes 5: Hilbert spaces*, Theorem 1 and Remark 2](https://terrytao.wordpress.com/2009/01/17/254a-notes-5-hilbert-spaces/). Both passages were inspected for this attribution. The programme's particular source and dual maps remain its own calculations, not formulas attributed to that exposition.

CFPA's positive Fourier-measure theorem is classical **Bochner theory**, even though the appendix reproduces its proof for the subsequent source calculation. The publication pass verified [Tao, *245C, Notes 2: The Fourier transform*, Theorem 57 and the Fourier-inversion display (11)](https://terrytao.wordpress.com/2009/04/06/the-fourier-transform/comment-page-2/); it does not claim a complete reading of that lecture or Bochner's original paper. The passage from a positive functional on compactly supported continuous functions to a Radon measure uses the **measure form of Riesz representation**, [Tao, *245B, Notes 12: Continuous functions on locally compact Hausdorff spaces*, Theorem 24](https://terrytao.wordpress.com/2009/03/02/245b-notes-12-continuous-functions-on-locally-compact-hausdorff-spaces/), inspected by the publication coordinator. This is a different result from the Hilbert-space Riesz theorem above. The weak-star subnet of finite measures uses **Banach–Alaoglu**, [Tao, *245B, Notes 11*, Theorem 3](https://terrytao.wordpress.com/2009/02/21/245b-notes-11-the-strong-and-weak-topologies/); the coordinator also inspected the stated sequential version in Theorem 4. These are named-passage checks, not new complete readings of the lectures. Applying these classical results to the retained original-zeta source and deriving the CFP/CPS classification are the programme-specific calculations.

Programme identifiers such as PTQ, PSC or ADC locate a calculation in this edition. They do not replace the human mathematical provenance on which that calculation depends.

## Rebuild the readers

Run from each reader's own directory so relative proof and figure dependencies resolve:

| Reader | Source reconstruction | PDF engine |
| --- | --- | --- |
| Geometric weight control | `python build.py` checks the source-part hashes and rebuilds the cumulative Markdown and LaTeX with Pandoc | LuaLaTeX, `RECONSTRUCTION_AND_WEIGHT_FULL.tex` |
| Positive quotient | Complete included `CUMULATIVE_ALGEBRA.tex` and its included proof bodies | XeLaTeX |
| Original-character lifting | Complete included `FULL_LATTICE_CC_READER.tex` and its included proof bodies | pdfLaTeX |

Run the engine three times to resolve contents and cross-references. The geometric publication preamble specifies DejaVu Serif Condensed, Segoe UI and DejaVu Sans Mono, together with explicit Unicode mappings and the Connes–Consani source macro. Install these fonts or retain a documented replacement that covers the same glyphs before compiling. The publication repairs include source line endings and math-mode spacing, portable source links, missing macro definitions and glyph coverage; those repairs are not new mathematical hypotheses.

The final payload hashes and reader files are listed in [MANIFEST.json](MANIFEST.json). [PROOF_LOCATORS.json](PROOF_LOCATORS.json) gives exact source lines and headings, including historical and review sections. Its index status does not imply that every indexed assertion has received a fresh mathematical review.

### Recorded geometric reader build and visual check

The final `RECONSTRUCTION_AND_WEIGHT_FULL.pdf` has **774 pages**, SHA-256 `d2073d2175c7b29af6aea17d7978d2628a22ee0f69d09ca0aaeec347e02e537c`, and was built in three successful LuaLaTeX passes. All **63 proof-input hashes** matched the included source manifest. The all-page word-bounding-box scan found no off-page or side-edge-crossing words. No missing glyphs, undefined references or multiply defined references remained.

Every new ADC/DCA/ACD page, **513–550**, was inspected, together with representative earlier pages and detailed renders of repaired displays. This was not visual inspection of all 774 pages. The reflowed displays include DP8.1, RD8.3, CSD1.1 and GMS1.2; the part separator at page 540 remains intentional. Horizontal-box warnings remain, including small contents-table overflows and margin-intruding displays, but the completed checks found no clipping. Source-hash agreement establishes preservation, not an independent mathematical proof.

### Recorded positive-quotient reader build and visual check

The final publication copy of `CUMULATIVE_ALGEBRA.pdf` has **466 pages**, SHA-256 `ebb2a2dcb9d2896bb5972e26552f78775f77bf57173af2661b708e9e6b0af8d1`. The accepted incoming reader had 464 pages; publication citation additions account for the two extra pages. All three XeLaTeX passes succeeded. The full 466-page text/link privacy and word-bounding-box checks found no private locators, off-page words or side-edge-crossing words. No missing glyphs, undefined references or citations, or duplicate labels remained.

The final log retains **one inherited 2.155-point overfull paragraph, nine underfull horizontal boxes and two `unicode-math` command-selection warnings**. There are no vertical-box warnings. Every final appended page, **408–466**, was inspected through contact sheets; detailed renders of pages 408, 417, 440, 450, 453, 456, 461, 462 and 466 were checked. No clipping was found. The entry pages include AST at 440, CFP at 448, CFPA at 456 and CPS at 459; CPS4 is on page 461. This is not a claim of detailed visual inspection of all 466 pages.

The preceding RGR/GDC extension occupies pages **384–407**. Its publication worker inspected every appended page through contact sheets, plus detailed renders of pages 384, 400, 405 and 407 and the figure. All **726 math spans** in those four new Markdown files matched the accepted incoming texts exactly after publication link and citation repairs. The final CFP/CPS intake preserves that prior publication derivative; all 21 newly received source/figure files are accounted for, with incoming and publication hashes recorded in the build audit. Formula-preserving citation and link repairs, including CPS5's AST3.5 locator, are not new mathematical claims. Hash agreement establishes preservation, not an independent proof of the contents.

### Recorded original-character reader build and visual check

The final `FULL_LATTICE_CC_READER.pdf` has **1,148 pages**, SHA-256 `7903f97ab2117e516c7800815df2559db676eb8b3b5f4ba4bab1a7a912d8438c`, and was built in three successful pdfLaTeX passes. An all-page word-bounding-box scan found no off-page words and no words within 15 points of the side edges. No missing glyphs, undefined references or citations, duplicate labels, or vertical-box warnings remained.

The TeX log still reports **360 overfull horizontal boxes, 22 underfull horizontal boxes, seven mathematical-token bookmark warnings and one legacy `atopwithdelims` warning**. These remaining diagnostics are disclosed; a clean word-boundary scan is not a claim of exhaustive visual perfection. The publication worker inspected pages 1, 2, 410, 475, 1018, 1058, 1104, 1116, 1127, 1134, 1136, 1141 and 1148. This is selected-page visual review, not visual review of all 1,148 pages.

The latest proof entry pages are MCL at 1104, ORE at 1116, RPC at 1127, RQC at 1134, SCT at 1136 and OEC at 1141. Source-level locators remain the authoritative reference for individual numbered statements.

## Result status

The edition integrates actual internal geometric and analytic calculations. It does **not** report an RH proof or disproof, numerical arithmetic weight separation for the full original object, or a new P-versus-NP implication. It claims no new Lean execution. Those limits concern the results themselves; they do not erase the proved comparisons or the earlier work preserved alongside them.
