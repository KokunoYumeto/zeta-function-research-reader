# Human sources and mathematical credit

Audit date: 17 September 2026. This additive guide makes the programme's human mathematical dependencies legible. It accompanies the exposition and the detailed proof corpus. It does not replace them or claim that every source cited somewhere in the archive supplies a theorem used in the current argument.

The policy is to credit a checked treatment, the earlier work that treatment explicitly uses, and the exact programme step to which the result is applied. A reproduced proof still receives credit for its established mathematical ingredients. A name, an eponym, an acknowledgement, a bibliography entry, and a proved dependency have different evidential meanings. We do not manufacture an original-inventor claim from a familiar theorem name.

This work implements the programme's independent commitments to human-readable mathematics, fair credit and a clear provenance record. The audit makes its source-checking limits explicit and does not claim that all recursive attribution is finished.

## How to read the evidence

- **New: result checked.** The primary paper, author copy, or authoritative authored handbook was opened, and the stated result and locator were read in this audit.
- **New: identity checked.** A primary publication record authenticates author, title and edition. It does not authenticate an uninspected theorem body.
- **Source-reported predecessor.** The checked source explicitly identifies the earlier human work and, where available, its exact locator. That credit is retained; it is not relabelled as a direct reading of the earlier work.
- **Inherited check.** A pre-existing source or statement record documents an earlier check. This audit preserves that record and its revision history without claiming to have repeated the full source check.
- **Use established / use candidate.** The former has a recovered mathematical application or an exact comparison of formulas. The latter remains a contextual or further-reading connection until the application is identified.

Anonymous IDs such as `H01`, `INH-001`, and `A2225` identify audit records. They are not names or account identifiers. Public source URLs are given below; private conversation exports and machine paths are excluded.

## The immediate source spine

|ID|Human source and BibTeX key|Where it enters|Verification status|
|---|---|---|---|
|H01|Bernhard Riemann; `Riemann1859`|Theta integral, completed zeta, the original zero question|New: primary transcription and formulas read|
|H02|André Weil; `Weil1952Primary`; Denise Vella-Chemla, transcription role, `Weil1952VellaChemla2020`|Explicit formula, logarithmic Mellin convention and positivity formulation|New: full retained transcription read; original-scan authentication inherited|
|H03|Ralf Meyer; `Meyer2005`|Even Schwartz source, zeta summation, Poisson identity and closed-range theorem|New: result checked; exact source-to-programme dictionary below|
|H04|Alain Connes; `Connes1999` / inherited `connesSelecta1999`|Meyer's explicitly credited spectral predecessor; earlier programme spectral comparisons|New identity and introduction; inherited detailed application checks retained separately|
|H05|Walter Rudin; `Rudin1990Verified` / inherited `rudin1990`|Modern Fourier-analysis exposition, Fourier uniqueness/inversion and Plancherel background|New edition/section identity; result-level inherited records; Plancherel theorem body not newly read|
|H06|Tom H. Koornwinder, Roderick S. C. Wong, Roelof Koekoek, René F. Swarttouw, William P. Reinhardt; `DLMF18Current`|Meixner–Pollaczek, Laguerre, recurrence and Christoffel–Darboux formulas|New: handbook formulas and explicit predecessor notes read|
|H07|Gábor Szegő; `Szego1975`; Mourad E. H. Ismail; `Ismail2009`|Human predecessors expressly named for the H06 formulas|Source-reported exact book locators; books not independently read in full|
|H08|Richard A. Askey and Ranjan Roy; `DLMF5Current`; Frank W. J. Olver; `Olver1997`|Gamma identities and Stirling estimates|New: handbook formulas and source notes; predecessor book pages source-reported|
|H09|Carl de Boor; `deBoor2005DividedDifferences`|Confluent Newton/Hermite interpolation in AKS20|New: exact source and programme specialization checked|
|H10|William W. Hager; `Hager1989Inverse`; Jack Sherman, Winifred J. Morrison, Max A. Woodbury|Rank-one and rank-four inverse updates in OMR18 and IRR27|New: Hager equations and exact dictionary; earlier identities and priority limits retained|
|H11|Stephen Boyd, Laurent El Ghaoui, Eric Feron, Venkataramanan Balakrishnan|Positive matrices, Schur complements and range conditions|New: strict and nonstrict source formulas checked; project estimates remain project calculations|
|H12|Pierre Deligne, with the distinct roles of André Weil, Alexander Grothendieck, Bernard Dwork and Nicholas M. Katz|Finite-field weight theorem and the geometric analogy that motivated the programme|New: Weil I Theorem 1.6; Weil II identity. No automatic transfer to the analytic project spaces|
|H13|Christopher Deninger; `Deninger1998`|Cohomological/dynamical research programme and local regularized factors|New: exact local proposition and status of proposed global formula checked|
|H14|Oliver Lorscheid; `Lorscheid2012Blueprints`; Anton Deitmar; `Deitmar2006`|Historical blueprint/monoid-scheme route|New: Lorscheid definitions and predecessor attribution; Deitmar identity; application tracked historically|

The current Gamma/Schwartz calculations depend directly on H01–H11. Deligne's work deserves accurate and visible credit for the geometric programme and any actual geometric use. A theorem over a finite field does not become a theorem about the programme's analytic spaces merely because their formulas resemble one another.

## Exact source-to-result arrows

### H01. Riemann, and the predecessors he actually names

Bernhard Riemann, *Ueber die Anzahl der Primzahlen unter einer gegebenen Grösse* (November 1859), is read here in the [D. R. Wilkins transcription, December 1998](https://www.claymath.org/wp-content/uploads/2023/04/Wilkins-transcription.pdf). The transcription's pp. 1–5 contain the Euler product, theta transformation, completed function, and vertical-line inversion. Riemann expressly credits **Leonhard Euler** for the product, **Carl Gustav Jacob Jacobi**, *Fundamenta*, p. 184, for the theta transformation, and **Joseph Fourier** for inversion. His opening mentions **Carl Friedrich Gauss** and **Peter Gustav Lejeune Dirichlet** as earlier investigators; that mention alone is not an exact theorem-dependency claim.

Riemann writes `Π(z)=Γ(z+1)` and puts `s=1/2+it`. His `ξ(t)` therefore equals the modern entire `ξ_R(s)=s(s−1)π^(−s/2)Γ(s/2)ζ(s)/2` after this substitution. This variable change must be stated. The Jacobi book page and Fourier's original theorem were not independently read in this pass; their recursive credit is recovered from Riemann's explicit citations. Wilkins receives transcription credit, not authorship of the mathematics.

### H02. Weil's explicit formula: edition and recursion matter

André Weil's 1952 Lund article occupies pp. 252–265; the collected-work reprint is volume II, pp. 48–61. The separately credited [Denise Vella-Chemla transcription](https://denisevellachemla.eu/transc-Weil-1952.pdf), December 2020, has its own pagination. The complete retained text was read; the earlier 14-page original-scan authentication is inherited. Its exact sign-sensitive checks remain controlling evidence.

Collected-work pp. 52–55 contain the logarithmic Mellin convention, contour calculation and hypotheses (A), (B); pp. 56–58 give local terms and equation (11); pp. 58–59 give the positivity criterion; pp. 59–61 pass to idèles. The source explicitly uses **Albert Edward Ingham**, Chapter IV, Theorem D p. 49 and Theorem 26 pp. 71–72; **Erich Hecke** for the functional equation; **Laurent Schwartz**, volume II, equation (VII,7;18), for the distributional transform; and **Jacques Hadamard**'s argument as presented by **Edmund Landau**, volume II, pp. 14–15. These are preserved recursive credit, with direct earlier-page inspection still open. **Marcel Riesz** is the dedicatee, a different role.

The 1952 paper is not silently identified with Weil's distinct 1972 *Sur les formules explicites de la théorie des nombres*, cited by Connes. Citation titles and dates must remain distinct.

### H03–H04. The exact Meyer–Connes comparison

[Ralf Meyer, arXiv:math/0412277v3](https://arxiv.org/abs/math/0412277v3), §3, Definition 3.1, defines `Zf(x)=Σ_(n≥1) f(nx)`. Its equation (11) is the Poisson relation. Theorem 3.3 proves the closed-range assertion for the stated Schwartz spaces. The even Schwartz space with `f(0)=Ff(0)=0` is Meyer's `H_cap`. For the programme's identically defined space `V`, the identity map identifies `V=H_cap`, and its two-sided nonzero theta sum satisfies `Theta=2Z` by evenness. Multiplication by 2 preserves the image and closedness. The precise topology is the one specified in the source and retained in the programme.

Meyer's completed zeta is `π^(−s/2)Γ(s/2)ζ(s)`, with poles. Thus the programme's `g=s(s−1)ξ_Meyer` is `2ξ_R`. His dilation generator `x∂_x` has the opposite sign from the programme's `D=−x∂_x`. None of these factors or signs may be suppressed. This comparison gives credit for the actual source construction; further project assertions need their own proofs.

Meyer's §1 explicitly identifies [Alain Connes's spectral interpretation](https://arxiv.org/abs/math/9811068) as its predecessor. Meyer's reference [2], **Alexander Grothendieck**, *Produits tensoriels topologiques et espaces nucléaires* (1955), is part of his functional-analytic source chain. Meyer's other own papers have a distinct role in developing his representation framework. Source-reported ancestry is retained without claiming a fresh proof audit of each predecessor.

The inherited `connesSelecta1999` locators refer to a particular author edition. The newly opened 1998 arXiv manuscript has different PDF pagination. The two are not merged. Connes's general spectral interpretation does not itself prove a new arithmetic estimate or settle the Riemann hypothesis.

### H06–H08. The Gamma polynomials have an explicit classical name and dictionary

The current DLMF [Chapter 18](https://dlmf.nist.gov/18) names **T. H. Koornwinder, R. S. C. Wong, R. Koekoek, R. F. Swarttouw and W. P. Reinhardt**. They must be credited alongside the institution. The checked release is **1.2.8, 15 September 2026**. Existing citations to 1.2.7 remain historical edition records.

For the programme's original parameter `s>0`, write `M_s=(2π)^(s/2)` and retain its measure

`dm_s(y)=M_s 2^(s/2)/(4π Γ(s/2)) |Γ(s/4+iy/2)|² dy`.

The classical identification is exactly

`p_(n,s)(y)=n! P_n^(λ)(x;φ)`, where `λ=s/4`, `x=y/2`, `φ=π/2`.

[DLMF 18.23.7](https://dlmf.nist.gov/18.23#E7), whose source note cites **Mourad E. H. Ismail**, equation (5.9.3), yields

`Σ p_(n,s)(y)z^n/n! = (1+z²)^(−s/4) exp(y arctan z)`.

[DLMF 18.19.6–18.19.9](https://dlmf.nist.gov/18.19) cites Ismail (5.9.8)–(5.9.9). Substitute `dy=2dx` into its weight and squared norm. The programme's multiplier is `M_s 2^(s/2)/(2π Γ(s/2))` times the standard `dx` measure, and multiplication by `(n!)²` for the monic polynomial gives exactly

`∫ p_(n,s)(y)² dm_s(y)=M_s n! (s/2)_n`.

Thus the inherited Gamma polynomials are a precisely rescaled Meixner–Pollaczek family. This comparison preserves the original total mass, degree convention and variable. The programme's further coordinate `u_d(S)=p_(d,s)((S−c)/i)/sqrt(h_(d,s))` retains its `i^(−d)` leading phase; it is not erased by the comparison. No priority claim about Meixner or Pollaczek follows merely from the name.

For Laguerre calculations, the exact source chain is:

|Programme ingredient|Checked DLMF locator|Explicit human predecessor in that page's source note|
|---|---|---|
|Weight, squared norm, leading coefficient|Table 18.3.1, Laguerre row|Gábor Szegő, §2.4 item 2; (5.1.1), (5.1.8)|
|Rodrigues representation|18.5.5 and Table 18.5.1|Szegő (5.1.5)|
|Finite coefficient formula|18.5.12|Szegő (5.3.3)|
|Three-term recurrence|Table 18.9.1|Szegő (5.1.10)|
|Christoffel–Darboux and confluent diagonal|18.2.12–18.2.13|Szegő, Theorem 3.2.2 and (3.2.4)|

The handbook formulas were checked at [18.3](https://dlmf.nist.gov/18.3), [18.5](https://dlmf.nist.gov/18.5), [18.9](https://dlmf.nist.gov/18.9), and [18.2(v)](https://dlmf.nist.gov/18.2#v). Szegő's original book pages were not independently re-read in this pass. For the project's QOT/RGC formulas, set `x=αt`, `β=2q` without changing the measure. The source norm becomes exactly

`∫_0^∞ [L_ℓ^(β)(αt)]² t^β e^(−αt) dt = α^(−β−1) Γ(ℓ+β+1)/ℓ!`, for `α>0`, `β>−1`.

The programme's finite Jacobi matrix and its negative off-diagonal convention still require the displayed recurrence transformation and the retained next-degree term when estimating the rectangular multiplication operator. A handbook citation alone does not justify discarding that term.

[DLMF Chapter 5](https://dlmf.nist.gov/5) is authored by **Richard A. Askey and Ranjan Roy**. Its [§5.11 source note](https://dlmf.nist.gov/5.11) credits **Frank W. J. Olver**, *Asymptotics and Special Functions* (1997), pp. 87–88 and 293–295, for the displayed Stirling formulas. The [§5.5 identities](https://dlmf.nist.gov/5.5) supply recurrence, reflection and multiplication formulas with their exact argument conventions. Those formulas must be cited by equation, not by an undifferentiated institutional homepage. Elliptic-integral conventions in [§19.2](https://dlmf.nist.gov/19.2) have the additional human chapter author **B. C. Carlson**.

### H09–H11 and the other recovered technical authors

The full [technical source ledger](provenance/technical/TECHNICAL_SOURCES.md) supplies result locators and exact translations. Its checked modern sources include **Carl de Boor** for confluent interpolation; **William W. Hager** for inverse updates; **Boyd, El Ghaoui, Feron and Balakrishnan** for Schur complements; **Russell Lyons** for exterior determinant mechanisms; and **Oliver Johnson and Andrew Barron** for convolution-score projection. Classical mechanisms receive human credit even when the programme gives an independent proof.

Two especially material backward attributions are now explicit. The extremal eigenvalue-sum source is **Michael L. Overton and Robert S. Womersley**, DOI `10.1137/0613006`, who credit **Ky Fan**. The two-trace determinant estimate is recovered through **Bob Grone, Charles R. Johnson, Eduardo Marques de Sá and Henry Wolkowicz**, p. 313, equation (1.2); that page explicitly credits **Jonathan M. Borwein, George P. H. Styan and Henry Wolkowicz**'s solution to **L. V. Foster**'s problem. Proposing the problem and solving it are separate human contributions.

Other recovered exact identities are **Zlatko Drmač**, with the earlier **Åke Björck–Gene H. Golub** principal-angle algorithm; **William N. Anderson, Jr.–George E. Trapp** for shorted operators; and **Alexander I. Aptekarev, Amílcar Branquinho and Francisco Marcellán** for Toda-type orthogonality deformations. Where only a publisher identity or abstract was available, the ledger says so; it does not invent a theorem number.

### H12. Deligne's actual theorem and the people behind it

[Pierre Deligne, *La conjecture de Weil. I*](https://www.numdam.org/item/PMIHES_1974__43__273_0/), **Theorem 1.6, p. 276**, gives the Frobenius eigenvalue magnitude `q^(i/2)` for the stated smooth projective variety over `F_q`, with `ℓ` different from the characteristic. The source's §1.5 records **Alexander Grothendieck**'s cohomological trace formula. Its opening and §1.2 credit **Bernard Dwork**'s rationality theorem, Grothendieck's framework and **Nicholas M. Katz**'s lecture notes; the introduction distinguishes the recalled material from Deligne's original sections. **André Weil** receives credit for the conjectures and geometric programme.

These are mathematical roles, not interchangeable names. The official article record gives pp. **273–307**; the 273–308 range printed in some later references is not copied as if independently checked. The [Weil II primary record](https://www.numdam.org/item/PMIHES_1980__52__137_0/) authenticates Deligne, volume 52 (1980), pp. 137–252. Its bibliography is part of the recursive trail; the exact use of a Weil II theorem in each historical claim remains a separate audit item.

[Hodge II](https://www.numdam.org/item/PMIHES_1971__40__5_0/) and [Hodge III](https://www.numdam.org/item/PMIHES_1974__44__5_0/) were also checked at the stated construction and functoriality results: Hodge II §3.2, and Hodge III §8.2. These identify Deligne's mixed-Hodge-theoretic contribution. No mixed Hodge structure, finite-field model, or Frobenius action on a project object is certified solely by inserting those citations.

The [exposé-level SGA source record](provenance/SGA_SOURCE_ROLES.md) retains the precise backward citations. The historical SGA5 trail also requires **Luc Illusie**'s rédaction and the **Jean-Louis Verdier** pairing contribution. SGA4½ has contributions by **Jean-François Boutot, Illusie and Verdier** in addition to Deligne. The wider historical ledger retains those roles. A bibliography that says only “Deligne/Grothendieck” loses relevant human provenance.

The historical irregular-period reading includes **Spencer Bloch–Hélène Esnault**, with selected §5 reading recorded later, and contextual or abstract-level consultation of **Marco Hien** and **Claude Sabbah–Morihiko Saito**. The present audit also checks Hien's Theorem5.3 and its credited chain through Bloch–Esnault, Sabbah and **Takuro Mochizuki**. That comparison must not be confused with the proof used in the current polynomial period map: file03 PDE1–13 gives its own oriented-ray determinant proof using a differential equation and a Gamma/Fourier base point. No use of Hien's abstract theorem is asserted for that particular proof. The technical and historical ledgers preserve these different source roles.

### H13. Deninger's proved and proposed statements

[Christopher Deninger, *Some analogies between number theory and dynamical systems on foliated spaces*](https://ems.press/books/dms/246/4682), ICM 1998, pp. 163–186, §3, distinguishes regularized local-factor identities (Proposition 3.1) from the proposed global cohomological formula (3). The latter is a research programme, not an available proof of the Riemann hypothesis. The source uses a completion with the additional constant `2^(−1/2)`; it cannot be silently identified with Meyer's completion.

The preceding formalism follows the geometric trace idea associated with **Grothendieck**. The local-factor calculation also refers to the classical Hurwitz-zeta derivative identity associated with **Matyáš Lerch**. These backward credits are reported at their actual roles; the historical primary Lerch paper has not been independently authenticated here. The programme's own spaces, operators, pairings and estimates need an explicit map before any Deninger analogy becomes an application.

### H14. Blueprints and monoid schemes

[Oliver Lorscheid, arXiv:1103.1745v2](https://arxiv.org/abs/1103.1745v2), Definition 1.1 and §1.6, supplies the blueprint and extension-of-scalars framework. His explicit predecessors include **Kazuya Kato**, **Anton Deitmar**, and **Alain Connes–Caterina Consani**. The archived link `math/0404185` is [**Anton Deitmar, *Schemes over F1***](https://arxiv.org/abs/math/0404185v7), not an anonymous source; its abstract explicitly credits **Nobushige Kurokawa, Hiroyuki Ochiai and Masato Wakayama**'s approach. The corresponding definitions and exact historical use are source-specific. Later proposed cohomological, tropical, or analytic extensions are not treated as proved merely because they occur in an introduction.

## Complete inherited bibliography and catalog coverage

[INHERITED_REFERENCES.tex](provenance/inherited/INHERITED_REFERENCES.tex), [INHERITED_REFERENCES.json](provenance/inherited/INHERITED_REFERENCES.json), and [INHERITED.bib](provenance/inherited/INHERITED.bib) preserve **all 109 original bibliography keys and full citation detail**. Minor cross-document section references have been made self-contained; no bibliography item is discarded. They include the wider random-matrix, algebraic-geometric, operator-algebraic, fluid, gauge and complexity-theoretic branches. Their preservation does not label every item an immediate dependency of the current exposition.

The [human catalog](provenance/catalog/HUMAN_CATALOG.md), [machine catalog](provenance/catalog/HUMAN_CATALOG.json), and [catalog issues](provenance/catalog/CATALOG_ISSUES.md) retain all **48 bibliographic identity records, 63 source records, 156 statement records, two author-ingestion records, and 52 source mappings** from the inspected registry. Every complete statement object was read and matched to its source record. Source events are revision-aware. The registry's latest entries date to 30 August 2026; it cannot by itself certify the later 692-page continuation.

This broader credit includes, among others, **Rowan Killip–Irina Nenciu** for circular matrix models; **Paul Bourgade–Ashkan Nikeghbali–Alain Rouault** for deformed Verblunsky coefficients; **Peter J. Forrester** and **Brian Winn** for moment formulas; **Alexander Grover–Francesco Mezzadri–Nick Simm** and **Nick Simm–Fei Wei** for the specific recent derivative-moment sources; **Ian G. Macdonald**, **Christian Krattenthaler**, and the other exact terminal references for the combinatorial identities; and **Ruy Exel** for the universal crossed-product step. The catalog gives the precise source and statement arrows rather than relying on this short orientation list.

`REFERENCES.bib` contains the inherited 109 keys plus the checked core and technical additions. `rudin1990` and `Rudin1990Verified`, `connesSelecta1999` and `Connes1999`, and `weil1952` and `Weil1952Primary` are intentional edition/check aliases for the same respective works. Use one appropriate key per work in a particular rendered bibliography; the different verification records are retained for audit, not as different mathematical authorships.

## Remaining attribution work, recorded rather than concealed

1. Several earlier primary books and papers are currently identified through a checked source's explicit reference. The citation and human credit are already present; original-page checks remain open for Jacobi, the earliest Fourier/Plancherel/Mellin sources, some Weil predecessors, and parts of the matrix and information-theory histories.
2. Exact theorem bodies were unavailable for some primary publisher records. The technical ledger marks these identity-only checks. No unverified formula number is supplied.
3. A public channel alias does not identify which particular coauthor owns it. The inherited video credit preserves that uncertainty. Initials are retained wherever a full given name has not been authenticated; they are not silently expanded from guesses.
4. The historical Jensen route has an inherited citation to David W. Farmer. A complete backward chain for each Jensen/real-rootedness claim is not established by this bounded bibliography pass. The same applies to every unnamed cyclic-character projection or potential-theoretic statement. EIQ supplies its own calculation; no Saff–Totik dependency is invented from topic resemblance.
5. The reconstructed catalog exposes several precise statement-wording issues, including a reversed mapping-torus lift, an overbroad multiplier-extension phrase, and an incorrect equivalence between separability and a countable approximate identity. These concern the programme's recorded wording, not faults attributed to the cited human authors. The reversed-lift and multiplier wording findings have been sent to the mathematical and publication owners. Other catalogue issues remain in the correction register; no completed source-sensitive repair is claimed merely from this report.
6. This audit covers the source families and records specified above. Additional archival branches and recursive descendants remain visible in the wider attribution ledger. No global closure or novelty claim is made.

The published exposition should place a citation at the result's point of use, not merely append this guide. The guide makes those citations checkable and keeps the earlier human work visible behind them.


## Additional recovered source paths

The [attribution map](ATTRIBUTION_MAP.md) joins the tau lineage, exact moment–cumulant source, later web-use records and broader historical bibliography. The [unresolved register](UNRESOLVED_ATTRIBUTION.md) records the remaining checks. Carlson's [DLMF Chapter 19](https://dlmf.nist.gov/19) expressly credits L. M. Milne-Thomson's chapter in Abramowitz–Stegun for part of the Legendre-integral treatment and lists earlier sources individually. Chapter author, handbook editors, technical acknowledgements and mathematical predecessors retain their different roles.
