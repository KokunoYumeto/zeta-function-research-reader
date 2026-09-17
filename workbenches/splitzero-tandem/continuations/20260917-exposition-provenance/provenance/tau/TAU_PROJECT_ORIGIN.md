# The project origin of the tau construction and its human mathematical sources

Checked 17 September 2026. This is an additive provenance and exposition report. It does not replace the frozen research sources, declare historical drafts correct in every respect, establish priority, or claim novelty. The accompanying `TAU_HUMAN_DEPENDENCIES.md` traces the larger semimodule bibliography beyond the two original notes.

## 1. What may be credited, and to whom

The globalization-semiring notes belong to the AI-assisted programme publicly credited as **KokunoYumeto / The Clankers**. This identifies project provenance without asserting novelty. The monthly collection also describes both earlier notes as belonging to the originating split-zero programme by Kokuno Yumeto.

The two original Zenodo records have different **deposited creator fields**, which must not silently be rewritten:

| Exact public source | Deposited date and creators | What it supplies here |
|---|---|---|
| [A Note on the Globalization Semiring G(Z)](https://doi.org/10.5281/zenodo.18976982) | Record date 12 March 2026; creators `ChatGPT, 5.4` and `Gemini, 2.5 DeepThink`; the TeX author field is empty | The original external-zero construction, its explicit two-coordinate model, arithmetic quotient and support geometry |
| [A Secondary Note on Split-Zero Globalization: Semimodule Classification, Multiplicative Reconstruction, and All-Orders Zeta Deformation](https://doi.org/10.5281/zenodo.19120905) | Record date 20 March 2026; creator `The Clankers`; PDF title page prints **29 April 2026**, because the deposited TeX uses `\date{\today}` | The general-ring formulation, support character, universal ring quotient, support-diagram formulation and subsequent calculations |
| [Monthly Mathematics Conjectures: Open Problems, Evidence, and Complete Results](https://zenodo.org/records/21849161), chapters 10 and 10A | A later cumulative project edition, not the source of an invented earlier priority date | Corrected formulations and expanded human-source attribution; its bibliography expressly credits the originating programme by Kokuno Yumeto |

Project attribution:

> The split-zero construction used in this programme was developed in KokunoYumeto's project with AI assistance and documented in the two Zenodo notes cited below. The first record lists ChatGPT 5.4 and Gemini 2.5 DeepThink as creators; the second uses the collective credit “The Clankers.” These are project-provenance citations. The mathematical background is credited separately to the human authors whose work supplies it, including Jonathan S. Golan, Anton Deitmar, Oliver Lorscheid and Jürgen Neukirch. The support-diagram extension is also situated explicitly in the Clifford and Płonka traditions and the inverse-semimodule literature. No claim of global novelty is made.

Do not replace these human ancestors with a citation to an AI system. Conversely, do not attribute the project's exact choices to a human paper merely because that paper develops related background. A use-source arrow needs its precise role.

## 2. A complete elementary explanation of the construction

Let \(R\) be a nonzero commutative ring with identity. Write \(r^\bullet\) for a tagged copy of \(r\in R\), and introduce one new element \(\tau\). Define

\[
G(R)=\{\tau\}\sqcup\{r^\bullet:r\in R\},\qquad e_R=0_R^\bullet.
\]

The tag changes no ring coordinate. It prevents the two different elements \(e_R\) and \(\tau\) from being mistaken for one another. All operations are:

\[
r^\bullet\oplus s^\bullet=(r+s)^\bullet,
\quad r^\bullet\oplus\tau=\tau\oplus r^\bullet=r^\bullet,
\quad\tau\oplus\tau=\tau;
\]
\[
r^\bullet s^\bullet=(rs)^\bullet,
\quad r^\bullet\tau=\tau r^\bullet=\tau,
\quad\tau^2=\tau.
\]

The semiring zero is \(\tau\); its unit is \(1_R^\bullet\). A cancellation such as \(r^\bullet\oplus(-r)^\bullet=e_R\) produces a **present coefficient whose value is zero**. It does not produce the external zero \(\tau\). This is the elementary reason for retaining both elements. [Original note, Definition 1.1 and Proposition 1.2; secondary note, Proposition 2.1.]

Here is a complete verification of the semiring assertion without an analogy. Let \(\mathbb B=\{0,1\}\) have join as addition and ordinary Boolean multiplication. In the product semiring \(R\times\mathbb B\), put

\[
D_R=\{(0_R,0)\}\cup(R\times\{1\}).
\]

Its zero and unit are \((0_R,0)\) and \((1_R,1)\). The sum of two elements with second coordinate one is \((r+s,1)\), their product is \((rs,1)\), addition of \((0_R,0)\) changes neither coordinate, and multiplication by \((0_R,0)\) gives \((0_R,0)\). Thus it is closed under both operations and contains the product zero and unit. Associativity, commutativity and distributivity restrict from the product. The map

\[
\iota_R:G(R)\longrightarrow D_R,
\qquad\iota_R(\tau)=(0_R,0),\qquad\iota_R(r^\bullet)=(r,1)
\]

is bijective. The preceding four cases show directly that it preserves both operations, zero and unit. It is a semiring isomorphism. In these coordinates \(e_R=(0_R,1)\) and \(\tau=(0_R,0)\), so their distinction is literal. [Secondary note, Proposition 2.1, p. 2.]

Two coordinate projections explain what the construction retains:

\[
p_R:G(R)\to R,\quad p_R(\tau)=0_R,\quad p_R(r^\bullet)=r;
\]
\[
\chi_R:G(R)\to\mathbb B,\quad\chi_R(\tau)=0,\quad\chi_R(r^\bullet)=1.
\]

They are unital semiring homomorphisms because \(p_R\) and \(\chi_R\) are the restrictions of the two product projections after \(\iota_R\). The first forgets the distinction between the two zero values; the second records whether a coefficient is present. Their pair is injective, with image precisely \(D_R\). In particular, neither projection alone contains all of \(G(R)\).

Multiplication by \(e_R\) is the map

\[
\nu_R(x)=e_Rx,\qquad \nu_R(\tau)=\tau,\quad\nu_R(r^\bullet)=e_R.
\]

It preserves addition and multiplication, and satisfies \(\nu_R^2=\nu_R\): the addition table gives additivity, and \(\nu_R(x)\nu_R(y)=e_R^2xy=e_Rxy\). Its image \(\{\tau,e_R\}\) is a Boolean semiring with its **own unit \(e_R\)**. The inclusion of this image in \(G(R)\) is not unit-preserving, because \(e_R\ne1_R^\bullet\). Thus calling this subset Boolean does not make \(G(R)\) a unital \(\mathbb B\)-algebra. For any unital semiring map \(f:\mathbb B\to G(R)\), the relation \(1+1=1\) would give \((1_R+1_R)^\bullet=1_R^\bullet\), hence \(1_R=0_R\) in \(R\), contradicting the hypothesis. [Original note, Propositions 1.3–1.4; secondary note, Corollary 2.6.]

Every ring map \(f:R\to R'\) has an exact lifted map

\[
G(f)(\tau)=\tau,\qquad G(f)(r^\bullet)=f(r)^\bullet.
\]

The defining tables verify addition and multiplication when both inputs are supported; whenever an input is \(\tau\), the same tables give the required identity or absorbing case. It preserves both distinguished identities. On each element,

\[
p_{R'}G(f)=fp_R,\qquad\chi_{R'}G(f)=\chi_R.
\]

The identity and composite formulas hold on \(\tau\) and on every \(r^\bullet\), proving functoriality. This supplies, in particular, the precise arithmetic square for \(\mathbb Z\hookrightarrow\mathbb C\) without identifying the two zeros. [Secondary note, Theorem 2.7; tau-base model, §1.]

## 3. The exact map to the present tau-base notation

The original note writes an element of the supported ring simply as \(r\), including its ring zero \(0_R\). The current model writes \(r^\bullet\) and \(e_R=0_R^\bullet\). The dictionary is

\[
\tau_{\rm original}\mapsto\tau_{\rm current},\qquad
r_{\rm original}\mapsto r^\bullet_{\rm current},\qquad
0_{R,\rm original}\mapsto e_{R,\rm current}.
\]

This is the semiring isomorphism obtained from the displayed tables, not an identification of \(e_R\) with \(\tau\).

Let \(\mathbf F_{1,\tau}\) mean the pointed multiplicative monoid \(\{\tau,1\}\), with absorber \(\tau\), together with the blueprint zero relation equating \(\tau\) to the empty sum. It imposes no relation \(1+1\equiv1\). Let \(B_R\) be the blueprint attached to the semiring \(G(R)\): its underlying multiplicative monoid is that of \(G(R)\), and two finite formal sums are related precisely when they have the same sum in \(G(R)\), including the empty sum. This construction is the semiring-to-blueprint framework of Oliver Lorscheid, checked in [arXiv:1103.1745v2](https://arxiv.org/abs/1103.1745v2), §1.1, Definitions 1.1–1.2, and §1.4. The structural morphism is

\[
\jmath_R:\mathbf F_{1,\tau}\to B_R,
\qquad\jmath_R(\tau)=\tau,\quad\jmath_R(1)=1_R^\bullet.
\]

It preserves multiplication because it sends the identity and absorber to the identity and absorber. It preserves every source pre-addition relation because its only generating zero relation is sent to the same zero relation in \(B_R\). Therefore it is a blueprint morphism. This uses Lorscheid's framework; neither it nor Deitmar's framework proves the programme's analytic estimates.

The only proper prime ideal of \(\{\tau,1\}\) is \(\{\tau\}\). Indeed a proper ideal cannot contain the identity, it must contain the absorber, and its complement \(\{1\}\) is multiplicatively closed. Every prime ideal of \(B_R\) contains \(\tau\) and omits \(1_R^\bullet\); hence its inverse image under \(\jmath_R\) is exactly \(\{\tau\}\). This proves the asserted map of spectra to the one-point base in the declared blueprint setting.

Do not confuse this base with the Boolean semiring. The pointed monoid is the same two-element multiplicative object, but the Boolean semiring additionally satisfies \(1+1=1\). The exact relation is the quotient adding that pre-addition relation; the structural map to \(B_R\) is already given above and is valid without imposing it.

The inspected 692-page predecessor source retains this base in equation **AKP1**, `14_CURRENT_KERNEL_AND_MULTIPLICITY_PROOFS.tex`, lines 7674–7688 (SHA-256 `9926c5b5670777548f15f3fd626a4237d2c10a26834f51ba2b466a3b3a349656`). It explicitly points to AT1–2a for the inherited full construction. The inspected historical `TAU_BASE_MODEL.md`, §§1–2, gives the complete structural maps above. This report supplies the missing DOI and human-source explanation; it does not alter AKP1.

## 4. Why the extra zero matters for two inputs

For the free semimodule \(G(R)^2\), every element has a unique support set \(A\subseteq\{1,2\}\): coordinate \(i\) belongs to \(A\) exactly when that coordinate is in the supported copy of \(R\), including its zero. Therefore there is a bijection

\[
G(R)^2\cong\bigsqcup_{A\subseteq\{1,2\}}R^A.
\]

On the right each copy is tagged by \(A\); the empty copy has one element. The inverse inserts \(\tau\) in coordinates outside \(A\). Componentwise multiplication by a supported scalar preserves \(A\); multiplication by \(\tau\) sends the element to the empty-support vector. The sum of \((A,x)\) and \((B,y)\) lies in the fibre \(A\cup B\), with value obtained by extending both vectors by ring zero to \(A\cup B\) and adding there. To verify this, at each coordinate the two inputs are either both absent, exactly one present, or both present; the three cases are exactly the operation table in §2. Cancellation in the last case leaves that coordinate present. This proves the bijection is an isomorphism with the stated semimodule structure. [Secondary note, Theorem 3.10, pp. 9–10.]

For example, \((\tau,e_R)\), \((e_R,\tau)\) and \((e_R,e_R)\) are three different zero-valued vectors: their supports are respectively \(\{2\}\), \(\{1\}\) and \(\{1,2\}\). The entirely absent vector is \((\tau,\tau)\). This is the concrete information retained by the programme's labelled coefficient diagrams. The general decomposition into semilattice-indexed groups belongs to the Clifford/Płonka lineage; the exact scalar and diagram formulation is credited and compared in `TAU_HUMAN_DEPENDENCIES.md`.

## 5. Human source arrows already present in the original notes

The statements in this table are **citation roles**, not unsupported claims of who first discovered all associated mathematics.

| Project occurrence | Human source | Exact role and present verification |
|---|---|---|
| Original note §1, first paragraph, TeX line 54 | Jonathan S. Golan, *Semirings and their Applications* (1999), chapters 1 and 6–8 | Semiring, ideal and congruence background. Publisher identity and chapter table checked. The precise historical first occurrence of external-zero adjoining has not been established from this book's full text. Cite Golan as background, not an authenticated priority claim for this exact construction. |
| Original note §4, line 434 | Golan, **chapter 11, “Semirings of Fractions,” pp. 129–134**, DOI `10.1007/978-94-015-9333-5_11`; chapter 18 for localization of semimodules | The original points to chapter 17, which the publisher identifies as *Free, Projective, and Injective Semimodules*. The new exposition must use the corrected locator. The project's displayed localization proof is explicit and remains separate from bibliographic authentication. |
| Original note §5, line 567 | Anton Deitmar, *Schemes over F₁* (2005); author preprint `math/0404185v7` | Monoid-scheme framework. Author, version and framework identified from the primary author preprint; not a source for the programme's analytic cohomology calculation. |
| Original note Remark 5.6, PDF p. 11, TeX lines 740–750 | Oliver Lorscheid, *The geometry of blueprints. Part I* (2012), checked arXiv v2 §§1.1 and 1.4; *A blueprinted view on F₁-geometry* (2016), cited §4.1.1 | Bridge from multiplicative monoids and additive relations to blueprints. The first note's locator “§4” for Part I is unsuitable for the checked v2, which has only §§1–3; use §§1.1 and 1.4 for the definitions and semiring embedding. The 2016 section was not independently read. The current presentation must explicitly include the empty-sum zero relation. No Boolean idempotent relation is silently inserted. |
| Original note §6, line 754 and bibliography | Jürgen Neukirch, *Algebraic Number Theory* (1999), chapters I–VII | Ring-of-integers, Dedekind-ideal, class-group and zeta background. Do not attribute a faulty project-specific scalar convention to Neukirch; see the historical correction below. |
| Secondary note §6, Proposition 6.2 | Tom M. Apostol, author of DLMF Chapter 25; **Apostol (1976), p. 264, formula (17)** for DLMF 25.11.14 | The value \(\zeta(-m,a)=-B_{m+1}(a)/(m+1)\), with \(a=1+t\). This is a human-source formula, not a new AI result. The DLMF equation and its explicit source pointer were read. |
| Secondary note §6, Proposition 6.2 | Arthur Erdélyi, Wilhelm Magnus, Fritz Oberhettinger and Francesco G. Tricomi, *Higher Transcendental Functions*, vol. I (1953), p. 26, formula (1.10.10), as explicitly cited in DLMF 25.11.18 | The identity \(\zeta'(0,a)=\log\Gamma(a)-\tfrac12\log(2\pi)\), used at \(a=1+t>0\). The DLMF formula and source pointer were read; the 1953 page was not independently read in this bounded task. |
| Secondary note §§5–6 | Apostol's DLMF Chapter 25, equations 25.11.10 and 25.11.17 | The Hurwitz specialization of the shifted Taylor and derivative identities. The general Dirichlet-series calculation in the project is a separate argument; the Hurwitz case must also cite this existing formula. |
| Secondary note §6 definition of the Hurwitz function | Adolf Hurwitz, 1882, as attributed by DLMF §25.11(i) | Historical function attribution. DLMF traces the function to Hurwitz; the original 1882 paper has not been independently inspected in this task, so the edge is recorded as source-reported, not primary-text checked. |
| Secondary note §8, number-field extension | James S. Milne, *Algebraic Number Theory*; Jürgen Neukirch, *Algebraic Number Theory* | Dedekind zeta continuation, Euler product and ideal theory. Exact analytic theorem/page dependencies still need the selected-edition check before claiming a fully closed genealogy. |

The original first note names no Clifford/Płonka literature. The later chapter 10A supplies it explicitly. The recursive report therefore joins the original project records to the later human attribution, without pretending the earlier notes already supplied those citations.

The secondary note's all-orders logarithmic derivatives invoke the “standard moment–cumulant formula” at source line 1318 without a named citation in its three-item bibliography. This attribution is now resolved by the accompanying [moment–cumulant source audit](TAU_CUMULANT_SOURCE.md): Peter McCullagh, *Tensor Methods in Statistics* (2018), §2.3.4, p. 38, equation (2.9), with the Speed–Rota lineage retained. The exact complex-series specialization and every sign are proved there and in the reader. Likewise the finite two-point “Stone” terminology is not a reason to claim that Marshall Stone proved the project's exact endpoint calculation; cite Stone duality when using that theory and retain the displayed finite calculation as the project's argument.

## 6. Historical corrections retained alongside the origin citation

The March first note's Definition 6.3 (PDF p. 12) permits the supported scalar zero when forming ideal classes. Taking both scalars equal to that zero collapses every lifted ideal to \(\{\tau,e_R\}\). Its following proof instead uses nonzero ring scalars. The March secondary record's Theorem 4.1 (PDF pp. 11–12) **already uses the correct nonzero ring scalars** and explicitly starts with nonzero ring ideals. This is a historical source correction, not a newly discovered failure of the current programme. Full statement, proof, and exact file identities are in `TAU_IDEAL_SCALING_CORRECTION.md`.

The historical reconstruction in the secondary note's Theorem 2.9 lists only binary additive relations in an uncontracted free semiring. The current tau-base model expressly includes the nullary relation \([\tau]=0\), citing the supplied structural formalization as a presentation correction. The exposition must state that relation as in §3; it must not copy an abbreviated historical presentation as if the zero-preservation issue did not exist. This report does not rerun the earlier full presentation audit.

## 7. Authentication, source retention and scope

The public Zenodo API records were obtained with HTTP 200 on 17 September 2026. Each deposited TeX and PDF was fetched from the record's returned file endpoint and checked against the record MD5. SHA-256 pins are:

| Object | Bytes | SHA-256 |
|---|---:|---|
| DOI 18976982, `globalization_note (1).tex` | 32585 | `fedf12a6bb2e1ecf878b0d6316274f1980c5d2365dd6aeaf83806f08c800f5f6` |
| DOI 18976982, `globalization_note.pdf`, 14 pages | 121560 | `3ff5fcb4e843b7d0ebe76044316c27bc2948c14dd4b83981d3f46687901a5023` |
| DOI 19120905, `split_zero_secondary_note.tex` | 54186 | `8e1aa2f934c49fc21e7a3d946ac6a465bc1a68896ec184afcb3d989cc9f8b364` |
| DOI 19120905, `split_zero_secondary_note.pdf`, 24 pages | 530183 | `8de0473e67f73da8f9273147a3bb70c2e7bce612de5b2da0118b7de9354ba761` |

The acquisition receipt retains the checked source identities. Both PDFs also have literature-cache records under their exact DOIs and SHA-256 values. These are audit evidence, not instructions to publish private corpus locations or metadata. The inspected pre-existing local copy of the first note has SHA-256 `ce06ac01c32e0452fe36121ac0f90e4eff8fad469b1cda7a6cf2d73116077a02`; its only textual differences from the public TeX are in the abstract and provenance paragraph. Its mathematical body agrees. The public file is the citation target.

The bibliography file `TAU_PROJECT_ORIGIN.bib` preserves deposited author credits and explains project authorship in notes. `TAU_HUMAN_DEPENDENCIES.bib` supplies the deeper human ancestors. Source authentication, formula verification, a proof of the present comparison map, and global historical priority are different claims: the first three have the bounded evidence specified here; global priority is not asserted.
