# The total original counterfactual object and its amplification maps

This repository constructs one object from the actual tau-based Split-Zero programme and calculates its exact connection to Deligne's amplification argument. The original absolute base, represented zero, arithmetic scalar map, theta complex, full coherent kernel, complete zero jets, tensor operations and original source norms are retained.

Read [the cumulative proof manuscript](Tau_Split_Zero_Total_Counterfactual.pdf). The editable master is [tex/main.tex](tex/main.tex). Its opening chapters construct the object and all its maps, calculate the phase and arithmetic amplification, and give the detailed Deligne contradiction with primary references. The preceding proof increment and all later continuation proofs follow in full.

## The constructed object

For the offcritical open subset U of the critical strip, B_U consists of original functions F for which p(D)F belongs to Theta V for some monic polynomial with roots in U. The single tensor differential graded algebra is the direct sum of all algebraic tensor powers of [V -> B_U]. Its cochain injection into the original two-leg tau complex and its represented observation diagram are explicit.

The marked first cohomology is exactly the direct sum of full local quotients O_rho/(g) at actual offcritical zeros. Every nonzero such jet has an explicit nonzero original-source lift. Its arithmetic image exhausts every possible offcritical zero. The full background kernel and diagonal remain attached; neither is falsely used as that detector. Complete constructions and proofs are TO.1–10, CAU.1–37 and AG.1–38, including AG36a–e.

## The exact amplification calculation

The original arithmetic class survives tensoring with eigenvalue k rho. The positive phase space has generator -partial_r+k/2 and the exact connecting relation DR-RA=B. PAM.1–27 and PSC.1–64 compute B on the full primary block, with all nilpotents and the complete arithmetic source. The offending eigenvector has boundary norm at least k times its original real displacement times its lift norm.

The source and phase gluing differences can both tend to zero at a fully specified period. At the first polynomial cutoff they vanish identically. The full generator boundary nonetheless remains the explicit nonzero residue map f_chi,theta tensor ell. Its exact squared energy is epsilon_theta^2+(Im alpha)^2+omega_q/omega_(q-1). All maps connecting these assertions are proved.

AAM.1–36 calculates the same amplified control through the original four-window arithmetic volume. The norm-window factor and quotient-volume factor have an exact product equal to the control's geometric mean. The factor with vanishing relative size is accompanied by a forced growing factor. The proved comparison overhead has a positive limit on the amplified scale. Vanishing Gram matrices retain their inverse factors in the same control. The current estimates do not give an exhaustive contradiction, and no actual offcritical zero is certified here.

The coefficient-purity trace retract is retained and preserves the arithmetic dilation eigenvalue. Deligne's finite-field weight exclusion is not assumed for that arithmetic eigenvalue.

## Deligne and the recovered Weil II source

[The amplification note](total_object_sources/DELIGNE_AMPLIFICATION.md) proves the finite contradiction in Weil I, Lemma7.1 and paragraph7.3. Product varieties retain a nonzero eigenclass while dividing the fixed half-exponent error by the tensor degree. All embeddings, parity conditions and the finite choice of degree are given.

[The Weil II note](total_object_sources/WEIL_II_AMPLIFICATION.md) follows lemma1.8.1 back to corollary1.4.3: the excluded disc gives weight at most beta+2, and the invariant tensor injection improves it to beta+2/k. This is an upper boundary-weight bound. The two historical passages are identified separately.

[The recovered-source locator](total_object_sources/WEIL_II_SOURCE_LOCATOR.md) records the complete existing French and English S20 LaTeX exports, historical complete English math-mode source, published French scan, hashes and edition differences. The older English math-mode source has H0 in the denominator of1.8.1.1 where the current S20 text has H_c^2. Source originals were preserved.

## Complete source and provenance

[The original programme](original_programme/) contains the inherited821-page source cut and editable dependencies. [The source-ordered transcript](provenance/VISIBLE_TRANSCRIPT.md), full message records, both supplied attachments, five contiguous source audits and the independent5349-message capture comparison are retained. All67 user messages and148 readable assistant prose messages in the published parent chain were read in full. Redacted tool bodies and unembedded attachments are not claimed recovered.

The13 preceding proof modules are recorded in [the original manifest](provenance/PROOF_INPUT_MANIFEST.json). The18 added inputs are recorded in [the continuation manifest](provenance/CONTINUATION_INPUT_MANIFEST.json), each copied byte for byte. Complete authored sources and mathematical review receipts are in [total_object_sources/](total_object_sources/) and [continuation_sources/](continuation_sources/). The attributed AGT comparison uses the inherited EW nonlinear method and supplies its stated cross-pair reduction.

The frozen109-page preceding repository remains unchanged. This cumulative reader has224 pages at its current build. [Repository validation](build/REPOSITORY_VALIDATION.json) records31 proof input checks,261 labels,120 references and the exact PDF hash. Visual review is recorded separately under build/visual_qa; its receipt defines the precise edition checked. Historical receipts retain their original dates and scope.

## Rebuild

Run `python scripts/build_reader.py`. It needs XeLaTeX with the packages and fonts in tex/main.tex, and PyMuPDF for page metadata. The included TeX builds without network access or the original workspace. `assemble_continuation.py` preserves local collection provenance; it is not required for a standalone rebuild.

Run `python scripts/validate_repository.py` for input hashes, references and PDF checks. `python scripts/package_sources.py` creates Tau_Split_Zero_Total_Counterfactual_Source.zip alongside this repository, retaining the full source and named final receipts while omitting disposable build renders. Its target is distinct from the frozen preceding archive.
