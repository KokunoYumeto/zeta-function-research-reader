# Human sources and exact verification scope

## Immediate source: Bruce Blackadar

Bruce Blackadar, *K-Theory for Operator Algebras*, first edition, Mathematical Sciences Research Institute Publications 5, Springer, 1986, [publisher DOI](https://doi.org/10.1007/978-1-4613-9572-0).

The exact historical PDF has SHA256 `dedcbf9363bd8ed23b2767f93c7e6e64b5c6011b3443a3bd25bbcbbd65e73b0b`, 10,413,048 bytes and 346 PDF pages. Printed p.156 is PDF p.164; printed p.131 is PDF p.139. Both were inspected visually. These are first-edition locators, not replacement page numbers from the corrected second edition.

Section 15.9 supplies the stable-extension push-forward through a tensor Hilbert module and a complemented embedding. Theorem 13.6.2 supplies stabilization. Blackadar explicitly attributes that theorem to **G. G. Kasparov**, compares it to the Morita-equivalence theorem of **Brown, Green and Rieffel**, and attributes the proof presented in his book to **Mingo and Phillips**. These are different intellectual roles; credit for the exposition does not absorb the antecedent credits.

## Original stabilization paper: G. G. Kasparov

G. G. Kasparov, *Hilbert C\*-modules: theorems of Stinespring and Voiculescu*, *Journal of Operator Theory* **4**(1), Summer 1980, 133–150. The [publisher record](https://jot.theta.ro/jot/archive/1980-004-001/1980-004-001-007.html) and [original paper](https://www.theta.ro/jot/archive/1980-004-001/1980-004-001-007.pdf) authenticate title, byline, volume and pages. The acquired PDF is 1,247,202 bytes, 18 pages, SHA256 `bc46e8350da616211ed5849bf78f2868355e5fe09030bced375a8b95b646809e`.

Theorem 1 and its consequence, printed p.137, identify adjointable operators with multipliers of compact module operators. Theorem 2, stated on p.138 and proved on pp.138–139, gives absorption of a countably generated Hilbert module by the standard module. The paper allows complex, real and “real” algebras and a compact second-countable acting group. This supplement uses the complex case with trivial group and the inner product linear in its second argument. These conventions and hypotheses were checked on pp.133–139; the bibliography on p.150 was also read. No claim is made to have audited the paper's later Stinespring/Voiculescu theorems.

## Proof presented in Blackadar: J. A. Mingo and W. J. Phillips

J. A. Mingo and W. J. Phillips, *Equivariant triviality theorems for Hilbert C\*-modules*, *Proceedings of the American Mathematical Society* **91**(2) (1984), 225–230, [DOI](https://doi.org/10.1090/S0002-9939-1984-0740176-0).

The proof-credit edge is explicit on Blackadar's printed p.131; his bibliography entry [MP], printed p.329 (PDF p.337), gives the work. The full initials, issue and DOI are corroborated by an [AMS published bibliography](https://www.ams.org/journals/proc/2001-129-12/S0002-9939-01-06164-0/?active=current). The original Mingo–Phillips article could not be fetched from AMS in this check (HTTP 403). Its theorem text has **not** been independently inspected here. The attribution is established; the original-paper verification remains a source-access gap.

## Relevant antecedents visible in Kasparov's original paper

The following edges were read in the original paper. They record human ancestry without turning every reference into an independently verified theorem application.

| Human source | Exact edge in Kasparov | Status in this supplement |
|---|---|---|
| **W. L. Paschke**, *Inner product modules over B\*-algebras*, Trans. Amer. Math. Soc. 182 (1973), 443–468 | Reference [10]; Hilbert-module definitions at pp.134–136 and the adjointable-operator lemma | Source-to-source attribution read; original Paschke paper not independently checked here. |
| **M. A. Rieffel**, *Induced representations of C\*-algebras*, Adv. Math. 13 (1974), 176–257 | Reference [14]; inner-product inequalities in Lemma 1, p.135 | Source-to-source attribution read; original paper not independently checked here. |
| **J. Dixmier and A. Douady**, *Champs continus d'espaces Hilbertiens et de C\*-algèbres*, Bull. Soc. Math. France 91 (1963), 227–284 | Reference [7]; Theorem 2 is described on p.138 as a generalization of their Theorem 4 | Historical antecedent explicitly identified; no original theorem verification claimed here. |
| **G. D. Mostow**, *Cohomology of topological groups and solvmanifolds*, Ann. Math. 73 (1961), 20–48 | Reference [9], §2.16, used for periodic vectors in the equivariant proof on p.138 | Recorded proof dependency of the general equivariant argument. The present trivial-group corner calculation does not require this approximation theorem. |
| **R. C. Busby**, *Double centralizers and extensions of C\*-algebras*, Trans. Amer. Math. Soc. 132 (1968), 79–99 | Reference [3]; multiplier definition on p.134 | Terminology and construction ancestry recorded. The original Busby paper is not freshly audited by this supplement. |

The names **W. F. Stinespring** and **D. Voiculescu** occur in Kasparov's title because other theorems in that paper concern their results. This supplement cites Kasparov's Theorems 1 and 2; the title alone does not establish an additional application of those later theorems. Kasparov's bibliography identifies Stinespring's *Positive functions on C\*-algebras*, Proc. Amer. Math. Soc. 6 (1955), 211–216, and Voiculescu's *A non-commutative Weyl-von Neumann theorem*, Rev. Roumaine Math. Pures Appl. 21 (1976), 97–113. They receive their named-result credit without an unsupported application claim.

## Existing programme dependency and newly written comparison

The inspected 19b/19d chapters also use **L. G. Brown, P. Green and M. A. Rieffel**, *Stable isomorphism and strong Morita equivalence of C\*-algebras*, *Pacific Journal of Mathematics* 71(2) (1977), 349–363, [DOI](https://doi.org/10.2140/pjm.1977.71.349). Their source remains credited in the companion bibliography. This supplement checks the finite-corner and constant-fibre multiplier step; it does not claim a new full audit of the separate Green-module/linking-algebra diagrams.

The unitary \(U(b\otimes c)=\mu_P(b)c\), its stabilized version and the representative-level corona composition are fully proved in the companion [calculation](MULTIPLIER_AND_MODULE_PROOF.md). They are an AI-assisted explanation in the programme's fixed coordinates, not a claim of new stabilization theory. Neither a verified bibliographic identity nor a source-to-source edge is presented as independent human peer review.
