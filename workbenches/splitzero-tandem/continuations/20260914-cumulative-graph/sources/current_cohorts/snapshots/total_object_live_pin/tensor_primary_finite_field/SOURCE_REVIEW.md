# TPF source and review receipt

## Original source

The mathematical dependency is the actual SPF.1–29 single-primary sheaf calculation in ../single_primary_finite_field/single_primary_finite_field.tex, whose final scoped-source SHA256 is 538b2da5adf307b54396e46f0848a49c63f0d81072844d191768016255c4fd53. The parent integrates it into single_primary_boundary_control.tex.

SPF uses the same actual coefficient map, full Taylor class and inverse, original phase constant, geometric Frobenius, Kummer projector, and unscaled negative Gauss convention. TPF does not re-cache its primary-source book. The prior primary receipt is ../single_primary_finite_field/SOURCE_REVIEW.md.

## Primary Kunneth theorem independently verified

P. Deligne, SGA 4, Exposé XVII, *Cohomologie à supports propres*, subsection 5.4:

- [Primary text, edited SGA manuscript hosted by Fabrice Orgogozo](https://www.normalesup.org/~forgogozo/SGA4/17/17.pdf): version 71766d9, 2024-07-30.
- Read 5.4.2 on PDF pages 68–69, Theorem 5.4.3 and its proof on PDF pages 69–71, and finite-family formula 5.4.4.1 on PDF page 71. The original pagination markers in these passages run 367–371.
- Hypotheses are compactifiable morphisms, the stated fibre-product diagram, and the torsion coefficient sheaf at finite coefficient level. The theorem says its constructed proper-support Kunneth arrow is an isomorphism. The proof reduces by compactification and base change to the proper, geometric-point case and projection formula. Formula 5.4.4.1 supplies the finite ordered family.
- Here the source projection compactifies by P1×Gm→Gm and its k-fold product. Apply the theorem to finite coefficient levels, then pass to the l-adic system and invert ell, as specified in the main proof.
- [Readable transcription of the same French original](https://grothendiecksga.com/read/sga4/fr/XVII-5.html) was also checked against the researcher-hosted original text; the latter is the primary citation.

Other already verified primary references:

- [Katz, Gauss Sums, Kloosterman Sums, and Monodromy Groups](https://web.math.princeton.edu/~nmk/Katz-GKM.pdf), Sections 2.0–2.3 and 4.0–4.3.
- [Stacks Project 03PK, Kummer theory](https://stacks.math.columbia.edu/tag/03PK).
- [Stacks Project 0A3J, Artin–Schreier sequence](https://stacks.math.columbia.edu/tag/0A3J).

## Independent mathematical review

- review/tensor_review.md: complete TPF.1–33 audit and full independent derivation of inertia, unrestricted p|k cancellation, exact Frobenius label permutation, actual smaller-field power-map descent, orbit scalars, and gcd/Mobius orbit counts.
- review/terminal_character_review.md: exact inverse-pullback relation; terminal label chi_* inverse; orbit length d; characteristic-polynomial sign; scalar specialization and actual stage typing.
- review/common_model_m1_review.md: final full check and seal of TPF.36–55, the shared integral model, explicit identity Frobenius on its character factors, multiplicity-one unit survival, and the typed complex scalar comparison. Reviewer confirmed the final TeX hash 5c2fa0e144f74aea4f21604e986a36fd8b5f37ee4e8235a36a605b49eba32b95.
- Reviewer read TPF.36–50 and confirmed the shared integral projector model, both base changes, and canonical isotypic reconstruction. Adopted its precision suggestion that Frobenius on the first character-module factor is the identity; the actual Gauss line retains its computed Frobenius.
- The same reviewer checked the multiplicity-one Gauss-square identity, invariant scalar, and typed one-dimensional intertwining-ratio calculation.

The integral model is B=Z[zeta_N,1/N] and its ambient polynomial-form quotient. It is not the module of Kahler differentials of the truncated algebra. Its common idempotents base-change to the reduced coefficient-form lines and the original SPF l-adic projector lines. It does not supply an unspecified additive-character comparison or a field map between characteristic p and characteristic zero.

The factorial calculation is only on an actual marked stage admitting the specified coefficient homomorphism. A larger stage that inverts p has no such specialization; this is not described as a zero specialization.
