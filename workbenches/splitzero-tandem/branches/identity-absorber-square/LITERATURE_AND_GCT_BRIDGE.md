# Monoid algebras, infinitesimals, and the GCT question

## The existing geometric construction

There is a standard construction directly matching the supported part of the present calculation. A group is a monoid, and the group algebra of the additive group of integers is
\[
k[\mathbb Z]=k[z,z^{-1}].
\]
Indeed its basis vector at \(n\) maps to \(z^n\), and the defining group-algebra multiplication \([n][m]=[n+m]\) becomes multiplication of Laurent powers. This gives inverse ring maps on their displayed bases. The support-forgetting map is the augmentation \(z\mapsto1\), with ideal \(I=(z-1)\). Its first-order quotient is exactly
\[
k[\mathbb Z]/I^2\cong k[\varepsilon]/\varepsilon^2,
\qquad z\mapsto1+\varepsilon.
\tag{LB1}
\]
The two inverse maps, including all negative powers and the exact kernel, are proved in [Primitive dual numbers](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/6af54ea3c8ef99127af327f3103e086c68d482c2/workbenches/splitzero-tandem/branches/identity-absorber-square/PRIMITIVE_DUAL_NUMBERS.md), DN4–DN8. The scheme \(\operatorname{Spec}k[z,z^{-1}]\) is the multiplicative group \(\mathbb G_{m,k}\); augmentation specifies its identity section. Thus LB1 is precisely its first infinitesimal neighbourhood at the identity. For \(k=\mathbb Z\), this is a neighbourhood of the identity section over \(\operatorname{Spec}\mathbb Z\), with the base retained.

This use of the squared ideal is the established construction in [Stacks, Section 37.5](https://stacks.math.columbia.edu/tag/05YW), Definition 37.5.1 and Lemma 37.5.2. Original TeX was read at [`more-morphisms.tex`, lines 671–770](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/more-morphisms.tex#L671). In particular, deriving dual numbers from this monoid/group algebra by its augmentation ideal is a concrete instance of existing infinitesimal geometry. A claim of historical novelty for that operation would be incorrect.

The external tau element adds an idempotent factor which remains part of the result:
\[
k[(S,+)]\cong k\times k[\mathbb Z],\qquad
k[(S,+)]/\mathcal J^2\cong k\times D_k.
\tag{LB2}
\]
The complete maps and inverses in DN4–DN12 prove this statement and distinguish the two support actions. Its second factor is LB1. The particular programme integration consists of the retained mixed-fold map DN15 and the exact operator receivers NI17–NI28. Those maps are fully derived here. A search of the entire historical literature for that particular combination has not been completed, so a priority claim for the combination is also not made.

## What the phrase in GCT means

The recollection has a precise primary source: Ketan D. Mulmuley, [*On P vs. NP, Geometric Complexity Theory, and the Flip I: a high level view*](https://arxiv.org/abs/0709.0748v1), 5 September 2007, Section 16, with the setup in Section 15. The original author archive was obtained from [arXiv source](https://arxiv.org/src/0709.0748v1); `main.tex`, lines 3938–4300, was read for this comparison.

That discussion seeks analogues of the Riemann hypothesis over finite fields in a quantized noncommutative setting, to support positivity for canonical bases of the specified nonstandard quantum groups. Section 15 identifies group embeddings connected with Kronecker and plethysm problems. Section 16 describes a mismatch between their generic and classical-specialization Hilbert functions, and reports that the desired RH extensions could not then be formulated. Its term *nonstandard* refers to that quantum-group setting. The statement is historical; this bounded source reading does not establish that no later formulation exists.

The present dual-number construction is an exact algebraic infinitesimal. It does not by itself define that GCT positivity theory. Nor does its name identify it with a hyperreal infinitesimal: in any field, \(a^2=0\) implies \(a=0\), whereas the nonzero dual-number element has square zero. This last distinction is an elementary algebraic calculation and leaves the proved ring, germ and operator maps intact.

## The bridge established in this collection

The map from the tau-derived algebra to the actual arithmetic representation is faithful:
\[
\mathbb C\times D_{\mathbb C}\hookrightarrow\operatorname{End}_{\mathbb C}(E),
\quad(k,a+b\eta)\mapsto k(I-\Pi_N)+a\Pi_N+bR_N.
\tag{LB3}
\]
It preserves the original metric and coefficient \(\epsilon_N\), sends the primitive to \(R_N\), and sends the two support identities to \(I\) and \(\Pi_N\). NI19–NI24 prove that the unchanged arithmetic space is projective over this full support algebra, and that restriction along \(D\to\mathbb C\times D\) produces the exact object
\[
\operatorname{Tor}^{D}_i(\mathbb C,E)
=\ker R_N/\operatorname{im}R_N\cong\ker W_N\quad(i\ge1).
\tag{LB4}
\]
The exact comparison with the original observation, including every product defect, is NI25–NI28. It reaches the same outgoing-column Gram matrix already used in the arithmetic current estimates. This is a proved connection to the objects underlying those bounds.

The collection has not constructed a map from those arithmetic objects to Mulmuley's nonstandard quantum coordinate algebras, or a canonical-basis positivity theorem for them. The published result therefore stops short of a GCT/RH formulation. The identified research direction is to compare an explicitly specified quantum algebra and its specialization maps with these retained support and deformation maps; the historic phrase alone supplies no such identification. The exact maps already proved remain available for that investigation.
