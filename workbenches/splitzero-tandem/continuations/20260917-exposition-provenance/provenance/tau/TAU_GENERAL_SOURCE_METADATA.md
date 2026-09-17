# Tau/globalization: four general human-source records

Checked: 2026-09-17. Scope: source authentication, cited-result extraction, precise attribution and version control for the Bourne, Chajda–Eigenthaler–Länger, Deitmar and Lorscheid references in chapter 10. This is a bounded attribution audit; it is neither a new audit of the entire mathematical programme nor a novelty claim. Original project files and literature-cache files were not edited. No remote mutation occurred.

## Project source and evidence boundary

The dependent source read was `10_split_zero.tex`. SHA-256: `aaba1c0fcfdc5e8762b1f92e6e6ffed775931730e6427b0405c7f58a5fa463f7`.

The citations occur in its introduction (lines 183–198), conventions (204–221), blueprint comparison (447–449), ideal-induced quotient (606–637), localization/stalk comparison (732–738), Boolean/pointed-monoid comparison (759–766), source map (1214–1243), and bibliography (1298–1332). Line numbers refer to the pinned file above.

The retained primary-source PDFs were compared with the exact versioned arXiv downloads. The three comparisons returned HTTP 200 and byte equality.

| Cached PDF | Exact version | Bytes | PDF SHA-256 |
|---|---|---:|---|
| `Chajda_Eigenthaler_Laenger_Congruence_Kernels.pdf` | [arXiv:1901.05991v1](https://arxiv.org/pdf/1901.05991v1), 17 January 2019 | 123885 | `5178bfd86d615c8f451a779589e1aa162931b01ac1eea35db11e71b4ceb41145` |
| `Deitmar_Schemes_over_F1.pdf` | [arXiv:math/0404185v7](https://arxiv.org/pdf/math/0404185v7), 26 July 2006 | 178845 | `b61f5a5c88f224fa3d8c56120bcfcd7ba02eec58bec1da5e857f47b83b96ae09` |
| `Lorscheid_Geometry_of_Blueprints_I.pdf` | [arXiv:1103.1745v2](https://arxiv.org/pdf/1103.1745v2), 5 January 2012 | 360958 | `0538feb167cb5924b1b4e4b4f36bfe38f16afc37138b5199e88ad506641ed31b` |

The corresponding existing `.txt` files have SHA-256 values `5a4779e3ab807797dc3a52d08b4ff68e60c197f6879233618b69fed4138fc7bd`, `829fc2c2aa44f57c8156435b34926049cb86af93567d156aa994c2f4bc070058`, and `aa696853a9e527bd56ed52958b22e85a019e85685324a2ea6f9a83e0a3534196`. Extraction is available; formula typography should be checked against the PDF where necessary. These are 12-, 19-, and 51-page preprints respectively, not the final journal/book pagination.

## TG1. Samuel Bourne: ideal-induced congruence

**Authenticated bibliographic record.** Samuel Bourne, “The Jacobson Radical of a Semiring,” *Proceedings of the National Academy of Sciences of the United States of America* **37**(3) (1951), 163–170. DOI [10.1073/pnas.37.3.163](https://doi.org/10.1073/pnas.37.3.163). [PubMed record](https://pubmed.ncbi.nlm.nih.gov/16588996/); [journal archive record](https://www.jstor.org/stable/88060). The chapter's author, title, year, volume, pages and DOI are correct. The journal archive gives the issue date as 15 March 1951.

**Project role.** Lines 606–614 attribute the name and ideal-induced relation

\[
x\equiv_I y\quad\Longleftrightarrow\quad
\exists i,j\in I\;(x+i=y+j)
\]

to Bourne. Lines 616–637 then prove the project-specific calculation for the split-zero semiring, rather than attributing that calculation to the 1951 paper.

**Access and verification status.** Bibliographic identity is verified. The exact original page, definition/theorem number, original hypotheses and any predecessor attribution for this relation remain **unverified in primary text** in this pass. The public scan locator discovered through repository-location metadata is [PMC PDF](https://pmc.ncbi.nlm.nih.gov/articles/PMC1063325/pdf/pnas01564-0033.pdf). PMC and Europe PMC presented access challenges; the PNAS endpoint returned 403. An independent bounded helper obtained the same boundary. No access control was bypassed. Do not label this record “original definition read.”

**Claim-level consequence.** Retain the citation and the project's complete proof. Do not invent a page or strengthen “goes back to Bourne” to a verified priority claim. Bourne's [ICM 1950 abstract](https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM1950.1/ICM1950.1.ocr.pdf) authenticates the radical-theoretic programme but does not locate the requested relation.

**Backward references actually visible.** The journal archive lists Vandiver (1934; 1939), Jacobson (1943; 1945), Dubreil (1941), McCoy (1948), and von Neumann (1936). Their appearance does not show that the ideal-induced relation was taken from any one of them. This is a source-acquisition follow-up, not permission to assign the relation to Dubreil or another predecessor.

## TG2. Ivan Chajda, Günther Eigenthaler and Helmut Länger: ideals versus kernels

**Correct bibliographic record.** Ivan Chajda, Günther Eigenthaler and Helmut Länger, “Directly decomposable ideals and congruence kernels of commutative semirings,” *Miskolc Mathematical Notes* **21**(1) (2020), 113–125. DOI [10.18514/MMN.2020.2819](https://doi.org/10.18514/MMN.2020.2819). Verified against the [Hungarian Academy repository record](https://real.mtak.hu/111738/) and the first page of the [published paper](https://real.mtak.hu/111738/1/2819.pdf).

**Required correction.** Chapter 10 lines 1305–1311 incorrectly give *Mathematica Montisnigri* **47** (2020), 5–16. Replace that journal/volume/page tuple in the additive corrected bibliography; preserve the original archived bytes as provenance.

**Exact checked locus and version translation.** The locally used arXiv v1 has Definitions 1.1–1.2 and Example 1.4 on pp. 1–4. The final publication renumbers these as Definitions 1–2 and Example 2, with the relevant discussion on pp. 114–116. A citation saying only “pp. 1–4” must explicitly identify the arXiv version; for the published citation use “Definitions 1–2 and Example 2, pp. 114–116.”

**Statement and scope checked.** Their commutative semirings have an absorbing additive zero but need not have a multiplicative unit. An ideal contains zero, is closed under addition and under multiplication by arbitrary semiring elements. The paper explicitly shows that the zero-class does not determine a congruence: on the chain \(0<a<1\), equipped with join and meet, the diagonal congruence and the congruence with classes \(\{0\},\{a,1\}\) have the same zero-class. This supports the chapter's warning directly; the chapter's unital convention is a permitted specialization.

**Proof boundary.** The paper supplies general terminology and a counterexample. It does not supply the chapter's classification of all split-zero congruences or its arithmetic quotient identification. Those retain their project-source locators and proofs. Classification: the general warning is known explicitly; the split-zero application is separately proved in the project, with no novelty determination made here.

**Named source recursion.** Definition 1.1 explicitly cites Werner Kuich and Arto Salomaa, *Semirings, Automata, Languages* (Springer, Berlin, 1986; ISBN 3-540-13716-5). Definition 1.2 and the general kernel/ideal fact explicitly cite Jonathan S. Golan, *Semirings and Their Applications* (Kluwer, Dordrecht, 1999; ISBN 0-7923-5786-8). Golan is already in the chapter bibliography. Add Kuich–Salomaa to the provenance graph as an inherited definition source, while marking that this pass read the credit in CEL rather than independently checking the book. The paper's later direct-product argument credits G. A. Fraser and Alfred Horn; that later theorem is not invoked by the checked pp. 1–4 citation, so it is a contextual reference, not a claimed dependency of the split-zero classification.

The [Kuich–Salomaa publisher record](https://link.springer.com/book/10.1007/978-3-642-69959-7) independently confirms both full author names, 1986 copyright, *Monographs in Theoretical Computer Science. An EATCS Series*, volume 5, and DOI 10.1007/978-3-642-69959-7. Its later softcover/e-book issue dates do not replace the original 1986 publication year. This is primary metadata authentication, not full-book access.

## TG3. Anton Deitmar: localization and monoid spectra

**Authenticated bibliographic record.** Anton Deitmar, “Schemes over \(\mathbb F_1\),” in Gerard van der Geer, Ben Moonen and René Schoof (eds.), *Number Fields and Function Fields—Two Parallel Worlds*, Progress in Mathematics **239**, Birkhäuser Boston, 2005, 87–100. DOI [10.1007/0-8176-4447-4_6](https://link.springer.com/chapter/10.1007/0-8176-4447-4_6). The publisher authenticates the chapter metadata; its full typeset body was not accessed. The checked body is the exact arXiv v7 dated 26 July 2006. Cite that version for the checked numbering rather than implying the 2005 print body was compared page by page.

**Exact result and application.** In v7, §1.1, Lemma 1.2, constructs localization of a commutative unital monoid at a submonoid by pairs \((a,s)\), with

\[
(a,s)\sim(a',s')\iff\exists t\in S:\;ts'a=tsa',
\]

and proves its universal property. Section 1.2 defines prime ideals and the spectrum. Proposition 2.1(a), pp. 5–6, proves that the structure-sheaf stalk at \(\mathfrak p\) is \(A_{\mathfrak p}\); (b) recovers global sections as \(A\). The chapter cites this as a parallel for its own explicitly calculated stalks; that is the appropriate role.

**Convention translation with its exact map.** Deitmar allows the empty prime ideal. The project requires an ideal of a monoid with absorbing zero \(z\) to contain \(z\). For the same monoid \(A\), its pointed spectrum is therefore exactly \(\operatorname{Spec}_{\mathrm{Deitmar}}A\setminus\{\varnothing\}\), by the inclusion sending an ideal to itself. Indeed, if \(I\ne\varnothing\) and \(a\in I\), then \(z=az\in I\); conversely every pointed ideal is nonempty. Primality is unchanged. Basic opens restrict as \(D_{\mathrm{pointed}}(a)=D_{\mathrm{Deitmar}}(a)\cap\operatorname{Spec}_{\mathrm{pointed}}A\), so this inclusion identifies the topology with the subspace topology. Localization at each retained prime uses the identical multiplicative complement. A citation alone must not silently restore the deleted empty prime.

**Backward human lineage.** Deitmar's introduction expressly builds on Nobushige Kurokawa, Hiroyuki Ochiai and Masato Wakayama; it also names Kazuya Kato's fans and Jacques Tits's motivation. The first three names are independently confirmed by [their publisher record](https://ems.press/books/dms/250/4901): “Absolute derivations and zeta functions,” *Documenta Mathematica*, Extra Volume Kato (2003), 565–584, DOI 10.4171/DMS/3/15. Deitmar's bibliography prints incorrect initials “B. Kurokawa” and “A. Wakayama”; do not propagate those. Kato and Tits are historical/conceptual lineage here, not unseen proofs imported into the project's stalk argument.

## TG4. Oliver Lorscheid: blueprint comparison

**Authenticated bibliographic record.** Oliver Lorscheid, “The geometry of blueprints. Part I: Algebraic background and scheme theory,” *Advances in Mathematics* **229**(3) (2012), 1804–1846. DOI [10.1016/j.aim.2011.12.018](https://doi.org/10.1016/j.aim.2011.12.018). The [publisher record](https://www.sciencedirect.com/science/article/pii/S000187081100421X) and [author's institutional repository record](https://research.rug.nl/en/publications/the-geometry-of-blueprints-part-i-algebraic-background-and-scheme/) agree. Exact body checked: arXiv:1103.1745v2, 5 January 2012. The author's arXiv record calls v2 a slightly revised and extended version of the printed article; do not identify their pagination.

**Extracted comparison contract.** Sections 1.3–1.6 embed monoids, monoids with zero, semirings and rings as full subcategories of blueprints. For a semiring \(S\), the blueprint has its multiplicative monoid and all formal-sum relations valid in \(S\); preserving those relations is equivalent to preserving semiring addition. Sections 1.3 and 1.9 distinguish the pointed initial blueprint \(\{0,1\}\) with minimal pre-addition from the Boolean semiring, where \(1+1\equiv1\). Section 1.13 constructs localization and states its universal property, explicitly leaving elementary verification to the reader. Section 3.8 defines semiring schemes through affine covers. This supports the chapter's categorical language; it does not prove its specific spectrum or localization formulas.

**Exact structural bridge.** Let \(F\) be that minimal pointed blueprint and let \(B\) be the blueprint of the Boolean semiring. The identity of the carrier \(\{0,1\}\) defines a blueprint map \(F\to B\): it preserves multiplication and sends every minimal relation, generated by \(0\equiv\varnothing\), to a valid relation. A reverse unital zero-preserving map would be the same carrier identity and would have to preserve \(1+1\equiv1\). That relation does not hold in the minimal pre-addition: deleting zero terms preserves the count of occurrences of \(1\). Hence no such reverse map exists. This explicitly relates the two structures without assigning the project's support-totalization construction to Lorscheid.

**Limits of the citation.** In §3.8, equivalence with Toën–Vaquié's \(\mathbb N\)-schemes is presented as a desirable result, not proved there. Do not use this paper as a proof of that equivalence. The specific chapter claims checked here do not require it.

**Named source recursion.** Section 1.3 expressly attributes the pointed-monoid framework to Alain Connes and Caterina Consani, “Schemes over \(\mathbb F_1\) and zeta functions,” *Compositio Mathematica* **146**(6) (2010), 1383–1415, DOI [10.1112/S0010437X09004692](https://doi.org/10.1112/S0010437X09004692); metadata verified against the [publisher PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/6804644F3837A06EA306376E893CE22A/S0010437X09004692a.pdf/schemes_over_1_and_zeta_functions.pdf). Section 1.6 directs readers to Javier López Peña and Oliver Lorscheid, [*Mapping F1-land*](https://arxiv.org/abs/0909.0069), arXiv:0909.0069v1 (1 September 2009), for the comparison survey. These inherited credits should appear in the provenance graph without pretending this bounded pass audited every result in those papers.

Section 1.9 explicitly follows Paul Lescot, “Algèbre absolue,” *Annales des Sciences Mathématiques du Québec* **33**(1) (2009), 63–82. Its [author-hosted published PDF](https://lmrs.univ-rouen.fr/sites/lmrs.univ-rouen.fr/files/membres/u92/p29.pdf), p. 64, Definition 2.1, gives the Boolean operations. Its introduction credits Y. Zhu, *Combinatorics and characteristic one algebra*, preprint (2000); the latter's primary body was not located/read in this pass. Credit this explicitly as “Zhu, as reported by Lescot,” not as an authenticated first-publication claim. Lescot's acknowledgements credit Nikolai Dourov for replacing the notation \(F_1\) with \(B_1\); this is a naming credit, not authorship of the project's split-zero construction.

For López Peña–Lorscheid, the published bibliographic form reported by the same authors in reference 7 of their [2012 paper *Projective geometry for blueprints*](https://www.numdam.org/articles/10.1016/j.crma.2012.05.001/) is: “Mapping \(\mathbb F_1\)-land: an overview of geometries over the field with one element,” in *Noncommutative Geometry, Arithmetic and Related Topics*, Johns Hopkins University Press, 2011, pp. 241–265. This author self-citation and the versioned arXiv metadata were checked; the published book chapter itself was not read. The accompanying `TAU_GENERAL_RECURSIVE_SOURCES.bib` supplies the four corrected main records and eight recursive/historical records, with access/version boundaries in their notes. The Kato and Tits metadata are transcribed from Deitmar's checked bibliography; their original papers were not independently read. The Dourov naming credit appears in the Lescot note rather than as an invented separate publication.

## Corrections and completed handoff

1. Correct the CEL journal, volume and pages; state whether its locator uses the preprint or printed numbering.
2. Pin Deitmar v7 and Lorscheid v2 beside the published records. Their original chapter bibliography has no version pins.
3. Preserve the attributed human-source chain: CEL → Kuich–Salomaa/Golan; Deitmar → Kurokawa–Ochiai–Wakayama and historical Kato/Tits; Lorscheid → Connes–Consani, López Peña–Lorscheid and Lescot → Zhu. Distinguish an observed secondary credit from a primary theorem read.
4. Keep the Bourne original-page lookup explicitly incomplete. Metadata accuracy and the independently written project quotient proof do not authenticate an unread primary page.
5. Preserve the project-origin attribution separately. Nothing checked here establishes that these human authors invented the split-zero globalization functor, or that the project's construction is globally novel. The user-authorized Kokuno Yumeto / AI collaboration source records are handled by the parent provenance audit.

No blanket “all human sources audited” claim follows from this four-reference check. It produces concrete bibliography repairs and an explicit inherited-source frontier without halting any ongoing mathematical work.
