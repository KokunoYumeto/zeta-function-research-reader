# Catalog reconstruction: findings and exact limits

This is a complete reconstruction of five existing historical registry inputs, not a new literature search or verification of every primary source. The inputs contain 48 bibliographic identity records, 63 literature-source records including later reading revisions, 156 literature-statement records, two author-acquisition/integration records, and 52 explicit source-to-bibliography mappings. Their source/statement chronology ends on 30 August 2026. All original record identifiers are retained in the public JSONL derivatives. Private paths, acquisition receipts and conversation details are excluded. Exact input file hashes appear in `CATALOG_VALIDATION.json`; the full path-bearing manifest remains private.

## What these records do and do not establish

The records provide many precise human attributions and statement locations. An inherited label saying “verified” means that the earlier registry recorded the specified verification. This reconstruction reads and checks the records; it does not repeat all of those primary-source verifications. A statement linked to a source is a recorded historical association, not evidence that every current manuscript uses that statement. A name mentioned in a title, named theorem, dependency list or bibliography is not automatically a proved mathematical dependency.

The 692-page September baseline and later work require a separate, manuscript-level attribution crosswalk. There is no Deligne bibliographic identity or terminal mapping in these five inputs. That is an exact finding about this bounded historical registry, not a finding that Deligne is absent from every manuscript or bibliography. It is therefore essential to join this reconstruction to the current source audit before describing the research program's provenance as complete.

## Revision-aware attribution

- Connes's survey *The Riemann Hypothesis: Past, Present and a Letter Through Time* has the resolved identifier arXiv:2602.04022 in `LITBIB-20260824-0004`. The older `LITSRC-20260824-0004` preserves its then-unresolved status and the extraction collision with arXiv:2501.06560. That collision must not be repeated as the survey's identity or presented as still unresolved.
- Conrey–Rubinstein–Snaith and Dehaye have historical “unread” identity/intake records, followed by content-reading revisions `LITSRC-20260826-0029` and `0030`. Preserve both chronology and later reading status. Do not let the old “unread” field erase the later reading or let later reading retroactively claim earlier access.
- Forrester's initially bounded reading `LITSRC-20260825-0013` was expanded by `LITSRC-20260826-0025`. Apostol/DLMF, Askey–Roy/DLMF, Lee, Connes–Consani, Mesland–Şengün and Blackadar also have explicit reading revisions. These are additional reading events, not separate newly authored human works.
- Connes–Consani's *Spectral triples and zeta-cycles* has both the arXiv identity and its published 2023 identity, `LITBIB-20260829-0040`, DOI 10.4171/LEM/1049. The earlier 2021 arXiv date must not be confused with the journal year.
- `LITSTMT-20260826-0079` has a later exact coordinate comparison in `LITSTMT-20260826-0083`. Earlier nonidentity does not establish absence of a relation.
- The action-amenability formulation in `LITSTMT-20260829-0148` is explicitly corrected by `0150`, with the precise Fell-bundle theorem supplied in `0149`. A public citation graph must carry that correction edge.

## Credits that should remain explicit

1. André Weil is the author of the 1952 work, originally pp. 252–265 and reprinted in *Collected Papers*, volume II, pp. 48–61. Denise Vella-Chemla is the author of the separately identified public French transcription dated December 2020. The catalog states that all fourteen original reprint pages were visually checked and controlled symbol-level comparisons. Credit the transcription as an access/edition contribution; do not silently call it the original scan or make the transcriber an author of Weil's theorems.
2. Jürgen Neukirch is the author of the English *Algebraic Number Theory* edition and Norbert Schappacher is its translator. Both roles are recorded in `LITBIB-20260828-0033`.
3. The chapter *Group C*-Algebras, C*-Correspondences and K-Theory* is by Bram Mesland and Mehmet Haluk Şengün. Roger Plymen and Mehmet Haluk Şengün are editors of the containing volume. The chapter citation must preserve those roles.
4. The DLMF references are human-authored chapters: T. M. Apostol, Chapter 25; A. B. Olde Daalhuis, Chapter 15; R. A. Askey and R. Roy, Chapter 5. An institutional link alone should not obscure those author credits.
5. Yuezhao Li's seminar notes carry the actually read induction-in-stages display. Dana P. Williams's *A Tool Kit for Groupoid C*-Algebras* is separately recorded as upstream framework whose official bibliographic metadata was checked. Do not assign Li's exact display to an unread Williams page.
6. Marc Yor's recorded role as Bourgade's thesis supervisor is distinct from his coauthorship of the Bourgade–Hughes–Nikeghbali–Yor paper.
7. Joël Merker's two records document acquisition/indexing of an 89-result arXiv author set. They expressly do not establish content-level reading or theorem-level use of all 89 works. Their acquisition count is not a claim of 89 dependencies.

## Unresolved identities and incomplete upstream chains

The public video creator is recorded as “Easy Riders.” The older evidence records an assertion that the creator is one of the three Grover–Mezzadri–Simm coauthors, but the name mapping remains unresolved in this registry. No personal identity has been inferred from voice, appearance, account details or local paths. Keep the public channel attribution and the three separately known paper authors until authoritative identification is obtained.

`LITSTMT-20260826-0073` corrects an overreach from an auto-caption transcript. Absence of displayed formulas from captions does not establish their absence from video frames. The earlier derivation recorded the recurrence and normalization as drawn from video material; exact video/frame attribution remains unresolved. An independent derivation from Killip–Nenciu does not remove the obligation to reconstruct the video contribution's provenance. Associate this correction with earlier video records `0068` and `0069`; do not repeat their stronger absence implication without it.

The terminal mapping preserves initials and differing recorded spellings. Examples include “J. Tolar”/“Jiri Tolar,” “J. S. Milne”/“James S. Milne,” “André Weil”/“Andre Weil,” and “N. C. Snaith”/“Nina C. Snaith.” The public name index retains these literal strings and roles; its 72 distinct strings are not a count of 72 distinct people. Initial expansion and diacritic correction need authoritative bibliographic evidence, not guesswork. One unresolved private human label in the configuration is retained only in private input provenance; no public identity is assigned to it.

`LITSRC-20260827-0031` explicitly records Titchmarsh, Macdonald and Hua as imported dependencies and reads ranges of Akemann–Vernizzi, Krattenthaler, Balantekin and Simm–Wei. `LITSRC-20260828-0032` explicitly names Diaconis–Shahshahani, Diaconis–Evans, Johansson, Forrester–Keating, Halász, Soshnikov, Akemann–Vernizzi, Balantekin, Titchmarsh, Keating–Snaith, Deaño–Simm, Serebryakov–Simm–Dubach, Tracy–Widom, Forrester–Witte and Claeys–Its–Krasovsky. These names/dependency lists are preserved, but this five-file slice does not resolve every one to its own complete terminal identity. The complete existing manuscript bibliography is a separate input for the coordinating bibliography audit.

Named results and historical mentions in the statement bodies likewise require role-sensitive treatment: a classical theorem name is a provenance lead, not proof of a particular consulted edition. Full statement bodies remain in `literature_statements.jsonl` so this distinction can be made without discarding the names.

## Actual Fourier, Mellin and orthogonal-polynomial references

| Human source | Exact recorded location or route | Recorded contribution and boundary |
|---|---|---|
| Walter Rudin, *Fourier Analysis on Groups*, Wiley Classics edition 1990, first publication 1962 | `LITSRC-20260824-0009`: printed pp. 1–3, 21–25, 29–30 | LCA convolution, Haar normalization, Fourier inversion and Fourier–Stieltjes uniqueness. Only those relevant pages were read. |
| André Weil, 1952 | `LITSRC-20260824-0008`: reprint pp. 52–55, 56–58, 58–59, 59–61 | Logarithmic Mellin/Fourier coordinates and conditions A/B; explicit formula (11), PF regularization and archimedean kernels; positivity/separating test; idèle-class distributions (12)–(13). Original and transcribed editions remain distinct. |
| A. P. Guinand, 1948 | `LITSRC-20260824-0007`: printed pp. 107–119, especially 108–115 | Cosine/Hankel transforms and explicit summation with boundary term. The record says the paper assumes RH throughout; no unconditional strengthening is imported. |
| Rowan Killip and Irina Nenciu, 2004 | `LITSRC-20260826-0020`: source lines 375–454, 565–777, 892–1021, 1607–1844 | Szegő recurrences, finite-support Verblunsky coordinates, CMV models, Haar laws, Toeplitz identity and Geronimus relations. Independently differentiated local recurrences are separate contributions. |
| Paul Bourgade, Ashkan Nikeghbali and Alain Rouault, 2009 | `LITSRC-20260826-0022`: lines 341–567, 648–823, 849–1101, 1105–1395, 1450–1613 | Deformed Verblunsky coordinate map, bijection, determinant factorization, independence/densities and Mellin–Fourier factorization. This prior art must be credited when discussing the coordinate construction. |
| Paul Bourgade, Chris Hughes, Ashkan Nikeghbali and Marc Yor, 2008 | `LITSRC-20260826-0021`: lines 234–520 and 601–929 | Independent beta/angle product decomposition and one-factor Mellin–Fourier transform; gamma/Barnes products. Random-matrix/zeta modeling remains distinct from individual-zero conclusions. |
| B. Winn, 2012 | `LITSRC-20260826-0026`: lines 372–603, 604–1170, 1172–1510 | Stereographic derivative-to-Cauchy-trace map, Fourier regularization, Laguerre Wronskians and Jack hypergeometric evaluation. The derivative-to-trace correspondence is prior human work. |
| Peter J. Forrester, 2022 | `LITSRC-20260826-0025`: lines 373–486, 581–966, 1001–1422, 1424–1593 | Jack hypergeometric duality, Cauchy-beta trace/density and moment formulas, Jacobi inverse-eigenvalue statistic. Fixed-size and asymptotic statements retain their separate hypotheses. |
| T. M. Apostol, DLMF Chapter 25 | `LITSRC-20260828-0036`, equation 25.11.25 | Hurwitz Mellin integral for Re(s)>1 and Re(a)>0; no unlocated display is credited for the Laurent constant. |
| Nick Simm and Fei Wei, arXiv:2409.03687v2 | `LITSRC-20260828-0032`: lines 553–909, 2196–2760 | Fourier estimates, microscopic determinant/Bessel interface, Jacobi/Toeplitz/Painlevé inputs and their named human dependency chains. Corrections in the catalog are explicitly version-specific. |

These are the sources actually identified in the assigned catalog, not a fresh claim that they exhaust the orthogonal-polynomial, transform or asymptotic literature required by the September manuscript. In particular, this pass has not verified a complete Riemann–Hilbert/Christoffel-function/equilibrium-measure bibliography for its later kernel calculations.

## Source-relative corrections must not become misattribution

The Grover–Mezzadri–Simm unequal-length parity correction `LITSTMT-20260827-0097` is recorded as an independent exact correction to the specified v1 display; equal-length formulas are retained. Do not attribute the corrected formula to the original source without disclosure. Simm–Wei corrections `0105` and `0107` similarly concern specified formulas/source-version evidence, not a claim that an entire human paper is invalid or that an unlocated proof is unknown globally. The Fekih-Ahmed domination issue is recorded with its exact range; standard Hurwitz inputs are instead attributed to Apostol/DLMF. Preserve the source's original statement and the separately proved correction.

## Fresh internal consistency flags for the mathematical owner

These flags concern the wording of inherited catalog records and do not accuse the cited human sources of error.

`LITSTMT-20260830-0155` defines the mapping torus by f(1)=α(f(0)), then calls t p+(1−t)α(p) a lift. Its endpoints are α(p) and p, so the stated boundary condition would require p=α²(p). A lift of p at zero satisfying the displayed convention is (1−t)p+tα(p). This mismatch requires comparison with the original source's mapping-torus convention and the Bott orientation before assigning a connecting-map sign. Merely swapping the lift without checking the orientation would not complete that comparison.

`LITSTMT-20260830-0153` describes multiplier/corona functoriality for a generic *-homomorphism too tersely. General multiplier extension needs the appropriate hypotheses or an explicit construction. The same record says the actual concrete map μ_P has an explicitly constructed multiplier extension, so the flag does not establish a defect in that concrete proof. Its theorem wording should point to the exact hypotheses and construction.

Four further wording points were identified in the same complete record review. `LITSTMT-20260828-0110` should retain the DLMF conventions at singular hypergeometric denominator parameters, in addition to Re(c−a−b)>0. `0119` needs a nonzero meromorphic germ for its finite-order factorization: the identically zero germ cannot equal z^k h with finite integer k and nonvanishing h. `0131` needs a continuation/removable-value convention or the relevant exclusions for its eta quotient: 1−2^(1−s) vanishes at s=1+2πin/log 2, n an integer; its recorded use at real 0<s<1 avoids these points. Finally, `0151` should not identify existence of a countable approximate identity with separability: a unital algebra has the constant approximate identity 1, while ℓ∞ is nonseparable (its uncountable set of binary sequences has pairwise sup-norm distance 1). The concrete application is recorded for separable ideals, so this is a correction to the general wording, not a disproof of the concrete application. Primary-source theorem wording remains for focused verification by the mathematical owner.

## Public packaging

The public derivative contains bibliographic facts, original registry formulations, exact published/source-edition locators, source IDs and correction edges. It does not contain the privately cached books, papers, extracted full texts or video transcripts. Existing rights restrictions remain. Attribution and public accessibility of metadata do not grant permission to republish a complete copyrighted source.
