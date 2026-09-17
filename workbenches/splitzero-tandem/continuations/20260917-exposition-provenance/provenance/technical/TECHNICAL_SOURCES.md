# Technical human-source and use ledger

Checked 2026-09-17. This is an additive attribution audit. It does not replace the accepted mathematical sources or certify the entire research programme.

## Scope and evidence levels

The historical use locators below refer to retained assistant records in the original web-session corpus. They identify passages actually read around the corresponding citation tokens, not proximity matches. The private corpus and raw conversation metadata are not a public bibliography. The public-facing credit sentences below contain no private conversation text, account identifiers, or personal attribution inferred from paths.

The inspected mathematical predecessor is `14_CURRENT_KERNEL_AND_MULTIPLICITY_PROOFS.tex` in the frozen 692-page edition, SHA-256 `9926c5b5670777548f15f3fd626a4237d2c10a26834f51ba2b466a3b3a349656`. Specific labelled calculations were inspected where stated; the entire 692-page proof was not re-audited here.

- **Verified-new / result extracted:** a primary source or author/institutional copy was opened and the stated formula or theorem locator was checked.
- **Verified-new / identity-only:** authors, title, publication and identifier were authenticated, but the full source result was not read.
- **Inherited use:** the archived citation and its mathematical context were recovered. This establishes use in the historical text, not correctness of every dependent proof.
- **Expository addition:** a modern reference supplied for an existing explicit calculation; this does not imply that the historical calculation consulted it.
- **Unresolved:** an exact theorem, version, name expansion or source-to-project arrow is not established by the available evidence. This is a bibliographic boundary, not a proposed conditional mathematical theorem.

No novelty or original-inventor claim is made. No source PDFs were added to the public bundle. Browser-accessed source extraction is available through the URLs below; no local PDF cache was retained by this worker.

## Directly recovered technical citations

|Historical locator|Human-source identification|Actual use|Status|
|---|---|---|---|
|A1721, reference 7|Stephen Boyd; Laurent El Ghaoui; Eric Feron; Venkataramanan Balakrishnan|Positive matrix certificates, exact Schur elimination including a zero-pivot condition|Inherited use; identity and strict/nonstrict formula locators checked|
|A2058, reference 3|Michael L. Overton; Robert S. Womersley; underlying principle credited to Ky Fan|Extremal trace on the particular rank-two additive exterior control|Inherited use; source identities checked; full original paper theorem not extracted|
|A2225, reference 2|Zlatko Drmač; backward credit to Åke Björck and Gene H. Golub|Principal-angle interpretation of an explicitly constructed source restriction|Inherited use; identity and abstract scope checked|
|A2225, reference 5|Russell Lyons|Exterior determinant / Cauchy–Binet mechanism and weighted degree-set generating polynomial|See subordinate `fourier_interpolation/VERIFIED_SOURCES.md` for exact source extraction|
|A2266, references 0 and 6|Bob Grone; Charles R. Johnson; Eduardo Marques de Sá; Henry Wolkowicz; backward credit to Jonathan M. Borwein, George P. H. Styan, Henry Wolkowicz, and problem proposer L. V. Foster|Optimal determinant bound using dimension, trace, and squared trace|Inherited use; Grone source formula and backward reference checked; 1982 solution identity checked|
|A2368, reference 3|Marco Hien; expressly credited source lineage includes Spencer Bloch, Hélène Esnault, Claude Sabbah and Takuro Mochizuki|Context for polynomial-exponential de Rham and rapid-decay period pairing; historical text supplies its own contours and proof|Inherited use; institutional preprint Theorem 5.3 checked; no wholesale application of Hien's theorem certified|
|A2559, reference 8|William N. Anderson, Jr.; George E. Trapp|Variational positive-operator background for averaging quotient forms|Inherited use; identity and abstract scope checked; exact finite constant is separately derived in the historical record|
|A2101, reference 5|Alexander I. Aptekarev; Amílcar Branquinho; Francisco Marcellán|Exponential deformation of orthogonality measures, recurrence coefficients and Toda dynamics|Inherited use; primary identity checked; exact theorem/formula number unresolved|
|A1959, reference 3; A1998, reference 3|Oliver Johnson; Andrew Barron|Convolution score as a conditional expectation and information residual|See subordinate `fourier_interpolation/VERIFIED_SOURCES.md` for exact extraction and mass-preserving translation|

### T01. Linear matrix inequalities and Schur complements

**Source:** Stephen Boyd, Laurent El Ghaoui, Eric Feron and Venkataramanan Balakrishnan, *Linear Matrix Inequalities in System and Control Theory*, SIAM Studies in Applied Mathematics 15 (1994), ISBN 0-89871-334-X. [Publisher DOI](https://doi.org/10.1137/1.9781611970777); [authors' authorized page](https://web.stanford.edu/~boyd/lmibook/); [full book](https://web.stanford.edu/~boyd/lmibook/lmibook.pdf).

**Exact extraction:** §2.1, pp. 7–8, equations (2.3)–(2.4), treats real symmetric positive-definite block matrices and the strict Schur-complement equivalence. Chapter 2 notes, printed p. 28, equation (2.41), includes the nonstrict version with the Moore–Penrose inverse and the required range condition `S(I-RR†)=0`. The zero-pivot/range condition must not be omitted. Author names and order were checked on the book's title page.

**Project edge:** A1721's error-aware inequalities are a use of this standard matrix method. Current AKS42, CEP25–27 and CTV7 retain their own quotient-minimization and determinant proofs. Citing the book supplies background; it does not transfer an arithmetic integral estimate or a uniform limiting bound. The complex-Hermitian version requires conjugate transposes, as retained in those project formulas. This check did not audit the numerical verifier.

**Public credit:** “We use standard positive-matrix and Schur-complement methods, as presented by Boyd, El Ghaoui, Feron and Balakrishnan; the arithmetic representative maps and retained mass factors are specified here.”

### T02. Extremal trace and Ky Fan's principle

**Source:** Michael L. Overton and Robert S. Womersley, “On the Sum of the Largest Eigenvalues of a Symmetric Matrix,” *SIAM Journal on Matrix Analysis and Applications* 13(1) (1992), 41–45. [Primary record](https://doi.org/10.1137/0613006). The 2006 online date is digitization, not the publication year.

**Backward credit:** the source explicitly attributes the extremal property to Ky Fan, “On a Theorem of Weyl Concerning Eigenvalues of Linear Transformations I,” *PNAS* 35(11) (1949), 652–655, [DOI](https://doi.org/10.1073/pnas.35.11.652), [primary journal deposit identity](https://pubmed.ncbi.nlm.nih.gov/16578320/). The original full theorem was not extracted in this pass; PMC access encountered a browser check.

**Project edge:** A2058 uses the principle on the programme's particular Hermitian rank-two control and gives the exterior-space eigenvalue calculation explicitly. This is established spectral linear algebra, not a newly discovered extremal-trace theorem. The arithmetic construction and estimates require the project proof independently.

**Identity warning:** DOI `10.1137/0613006` identifies Overton–Womersley, whereas Boyd–El Ghaoui–Feron–Balakrishnan has DOI `10.1137/1.9781611970777`. This disambiguation is not a finding that the archived A2058 citation itself was wrong.

### T03. Principal angles

**Source:** Zlatko Drmač, “On Principal Angles between Subspaces of Euclidean Space,” *SIAM Journal on Matrix Analysis and Applications* 22(1) (2000), 173–194. [Primary record](https://doi.org/10.1137/S0895479897320824). The paper's primary record describes real full-column-rank matrices, singular values of the cross-Gram matrix of orthonormal frames, and stability of the Björck–Golub algorithm. Metadata and abstract were checked; a numbered theorem was not extracted.

**Backward credit:** Åke Björck and Gene H. Golub, “Numerical Methods for Computing Angles Between Linear Subspaces,” *Mathematics of Computation* 27(123) (1973), 579–594, [journal DOI](https://doi.org/10.1090/S0025-5718-1973-0348991-3), [journal archive record](https://www.jstor.org/stable/2005662). The AMS PDF returned 403; no theorem-number claim is made.

**Project edge:** A2225 explicitly identifies its eigenvalues with squared singular values of the weighted source transport, then takes their logarithms for the four-volume term. Cite the angle interpretation to these authors. A numerical stability theorem over real Euclidean spaces does not by itself verify the programme's complex weighted maps, mass factors, or asymptotic estimates. Those need the displayed project comparison.

### T04. The two-trace determinant estimate and its earlier source

**Consulted source:** Bob Grone, Charles R. Johnson, Eduardo Marques de Sá and Henry Wolkowicz, “Improving Hadamard's inequality,” *Linear and Multilinear Algebra* 16(1–4) (1984), 305–322. [DOI](https://doi.org/10.1080/03081088408817634); [author-hosted published copy](https://www.math.uwaterloo.ca/~hwolkowi/henry/reports/PAPER17.pdf); [author bibliography](https://www.math.uwaterloo.ca/~hwolkowi/henry/reports/ABSTRACTS.html). Title-page spelling is Bob Grone; do not silently replace it with another name form.

**Exact locator:** §3, printed p. 313, equation (1.2), states the bound from dimension, trace and squared trace; p. 314 says those bounds are optimal with that data. Theorem 3.1 adds ordered diagonal information. The original p. 313 bound is explicitly credited there to reference [1], not claimed as the four authors' new result.

**Recursive source:** J. M. Borwein, G. P. H. Styan and H. Wolkowicz, “Some Inequalities Involving Statistical Expressions (L. V. Foster),” *SIAM Review* 24(3) (1982), 340–342, [primary record](https://doi.org/10.1137/1024072). The solving authors and Foster's distinct proposer role are retained. The 1982 full proof was not accessed.

**Project edge and exact notation:** in A2266 let `Z` be the positive cost operator in its stated metric, `t1=Tr Z`, `t2=Tr Z²`, dimension `q>1`. Put `m=t1/q`, `s²=t2/q−m²`, `a=m+s√(q−1)`, `b=m−s/√(q−1)`. Apply the source bound to the Hermitian representative of `I+Z`; its mean is `1+m`, variance is `s²`. The upper expression becomes exactly `(1+a)(1+b)^(q−1)`. The project separates `q=1` and the empty module. This checks the formula translation, not every source-specific trace calculation.

**Public credit:** “The optimal bound determined by dimension and the first two traces is the classical Borwein–Styan–Wolkowicz solution to Foster's problem, recalled by Grone, Johnson, Marques de Sá and Wolkowicz. We apply it to the explicit arithmetic cost operator.”

### T05. Rapid-decay periods and their human dependency chain

**Source:** Marco Hien, “Periods for flat algebraic connections,” *Inventiones mathematicae* 178(1) (2009), 1–22. [Published identity](https://doi.org/10.1007/s00222-009-0185-7). [Institutional full preprint](https://forschergruppe.app.uni-regensburg.de/Forschergruppe/Preprints2008/07-2008.pdf), DFG 07/2008: Theorem 5.3, printed p. 16; local duality Theorem 4.4 and Proposition 5.1. This institutional preprint has 23 numbered pages plus its cover; its numbering is not silently asserted to be the published version. [arXiv identity](https://arxiv.org/abs/0803.3463v1), submitted 24 March 2008, is independently identified, not byte-equated to that institutional copy.

**Result:** a smooth quasi-projective complex variety with a flat algebraic vector-bundle connection has the integration pairing between algebraic de Rham cohomology and rapid-decay homology of the dual connection, perfect in each degree.

**Backward credit:** Hien's introduction credits Bloch–Esnault for the curve pairing, Sabbah for the good-formal-structure conjecture, and Mochizuki for the algebraic proof and higher-dimensional good-lattice results. It distinguishes Grothendieck's trivial-connection comparison and Deligne's regular-singular comparison (Deligne, II.6.2). These roles must remain separate. This source is not authority for assigning all irregular-period work to Deligne.

**Project edge:** A2368 cites this literature as context while presenting its own contour comparison for `u≠0`, including coalescing critical points. No claim is made here that the full project family satisfies every hypothesis of every Hien comparison, or that this theorem proves a finite-field weight bound for it. The primary project proof remains the evidence for its exact arrows.

### T06. Shorted operators

**Source:** William N. Anderson, Jr. and George E. Trapp, “Shorted Operators. II,” *SIAM Journal on Applied Mathematics* 28(1) (1975), 60–71. [Primary record](https://doi.org/10.1137/0128007). The title page uses initials; full given names are corroborated by the same journal's cited coauthored records and the [1974 AMS meeting programme](https://www.ams.org/journals/notices/197401/197401FullIssue.pdf).

**Backward credit:** William N. Anderson, Jr., “Shorted Operators,” *SIAM Journal on Applied Mathematics* 20(3) (1971), 520–525, [primary record](https://doi.org/10.1137/0120053), explicitly gives the finite-dimensional generalized-Schur formula and maximum dominated positive operator supported in a specified subspace. The 1975 abstract distinguishes its Hilbert-space extension from that earlier finite-dimensional work.

**Project edge:** A2559's quotient-metric averaging discussion acknowledges this variational background and gives its finite Schur-complement proof and sharp calibration. Identity and primary abstract scope were checked. A numbered theorem of the 1975 paper was not extracted; no general infinite-dimensional theorem was silently substituted for the stated finite proof.

### T07. Orthogonality deformations and Toda equations

**Source:** Alexander I. Aptekarev, Amílcar Branquinho and Francisco Marcellán, “Toda-type differential equations for the recurrence coefficients of orthogonal polynomials and Freud transformation,” *Journal of Computational and Applied Mathematics* 78(1) (1997), 139–160. [Publisher record](https://doi.org/10.1016/S0377-0427(96)00138-0); [institutional preprint list, 96-04](https://www.mat.uc.pt/preprints/eng_1996.html); [Marcellán's institutional CV, item 64](https://memoria-investigacion-transferencia-hist.uc3m.es/InvestigaUc3m/2011-2012/carlos3/pdf/Matematicas_Francisco_Marcellan_Ingles.pdf). Given names were cross-checked against [Aptekarev’s institutional paper](https://keldysh.ru/papers/2017/prep2017_59_eng.pdf) and [Branquinho’s university profile](https://cmuc.mat.uc.pt/rdonweb/person/ppgeral.do?idpessoa=150).

**Project edge:** A2101 cites this paper for the established relationship between exponential measure deformation, recurrence-coefficient dynamics and Toda equations, then supplies its own monic-polynomial derivation for the two arithmetic measures. Identity and abstract scope were checked. A numbered source formula and a full backward genealogy to Toda/Freud were not verified in this pass; the eponyms alone are not inventor evidence.

## Supplemental mathematical tools and boundaries

The interpolation/Fourier/inverse-update worker's `fourier_interpolation/VERIFIED_SOURCES.md` records the exact directly inspected AKS20 confluent formula, OMR18 rank-one update and IRR27 rank-four update, with modern primary references. It also reconstructs the actual Johnson–Barron and Lyons edges listed above. Its seven bibliography entries are included in `TECHNICAL.bib`; the distinct worker report preserves its exact verification scope.

Saff and Totik: the publisher authenticates Edward B. Saff and Vilmos Totik, *Logarithmic Potentials with External Fields*, first edition (1997), [DOI](https://doi.org/10.1007/978-3-662-03329-6), distinct from the second edition (2024), [DOI](https://doi.org/10.1007/978-3-031-65133-5). In the inspected current source, EIQ explicitly states that its calculation does not import an external equilibrium theorem. No direct Saff–Totik citation/use chain was established in this bounded pass. Therefore they are not inserted as inherited dependencies in `TECHNICAL.bib`. They may be cited as further reading only with that status made explicit and an exact chapter selected after reading it.

## Search and validation boundary

Primary sources were preferred: SIAM, Springer, authors' university pages, institutional preprints, arXiv, and the journal deposit for Fan. Searches followed the exact identifiers inherited from historical reference objects, then one backward credit edge where material. Search-engine snippets were discovery aids; metadata assertions were checked against the primary pages described above. This is not a literature-completeness or novelty search.

The seven directly inspected historical citation contexts, plus supplied subordinate checks, cover the specified technical references. Unnamed standard results, all other historical turns and all current proof applications require the wider programme audit. No source corpus, accepted PDF, continuation prompt or remote repository was changed by this worker.
