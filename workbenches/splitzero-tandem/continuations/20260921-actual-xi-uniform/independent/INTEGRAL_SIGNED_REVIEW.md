# Independent derivation of the complete defining-prime signed order

The complete proof is `INTEGRAL_SIGNED_REVIEW.tex`, ISR1–34 including ISR13a. The exact checker is `INTEGRAL_SIGNED_REVIEW.py`; its JSON certificate pins the final proof, this review, the current root PS source, received source, and ET source. These files are an independent mathematical derivation, not a publication receipt.

## Actual reading coverage

- Read the entire preserved `defining_prime_intake_20260920/DEFINING_PRIME_RECEIVED.md`; independently derived its equations (9)–(31). The separate collision/Gamma claims beyond those equations are outside this derivation.
- Read original FS13 and surrounding inverse-chart definitions, VA1's full original polynomial factors, and the entire RD1–29 residue/trace and original receiver equations from the current cumulative source.
- Read the entire root `PRIME_SPECIALIZATION_BODY.tex`, PS1–25, current SHA256 `da50d8ca7f0334fd0810473252946745dd70fad0e7c6bac2e677f84c02c56e4f`.
- Read the entire ET1–20 coefficient-ring, basis, conductor, and full signed multiplication definitions used by PS14. ET source SHA256 `deafefa5e21f54bae521bd21c63523ee3b64ad245735849c28246b673be730ac`.
- No newly downloaded literature or whole-corpus reading is claimed. Original human-source citations remain at the original FS/RD/ES-reader proofs and are cited in this independent source. The received continuation is identified as supplied mathematical work, not silently attributed to a classical author.

## Independent results

ISR1–3 prove pairwise distinctness of the four actual witness roots and classify every defining-prime valuation: one or two divisible denominators, each of valuation exactly one. The classification uses positivity and the exact reciprocal equation, not genericity.

ISR4–10 prove all rank-eight inclusion entries, the full quadratic integral closures including split factors, exact labelled Lagrange inverse, original residue, and integral residue self-duality. Every scalar unit remains in the formulas.

ISR11–13a prove that the algebra conductor is exactly the residue-dual lattice of the normalization, with branch ideal `p^m_i D_i O_i`. Its valuation is `3m_i + epsilon_i`, and its original eight generators are `A p^m_i f_i` and `A sigma f_i`. The full generator matrix is `diag(A Q diag(p^m), A Q)`, retaining all 64 rational entries. The index of E in O equals the index of the ideal in E; the full Smith factors also agree, through the perfect pairing `E/I × O/E -> Q_p/Z_p` supplied by the original residue.

ISR14–15 independently prove the entire multiplication-trace and residue-to-trace matrices, their determinants, the squared-index discriminant relation, and the normalization Gram. No nilpotent or complementary direction is discarded.

ISR16–17 prove every Smith factor on the complete one-divisible and two-divisible strata, including arbitrarily close unit pairs or a closer pair in the triple cluster. Their determinantal-ideal proof identifies every needed minor valuation.

ISR18–23 repair the nonunit-leading-coefficient case. If `p|S`, then only the one-divisible case can occur and the two unit denominators have original derivative valuations `-v_p(S)`. The original coefficient algebra therefore is not a finite integral order. Its eight coefficient columns form a fractional lattice, whose complete Smith list includes negative exponents. Its full integral closure still has the exact basis `sigma/p^floor(b^0/2)`. The shift-one model is a different integral order, with exact generic relation only after adjoining `eta^2 = S/(S-4)`. The original and shifted signs and the inverse map are retained. No unsaturated integral tensor product is declared normal after ramified base change.

ISR24–28 evaluate both exact 1201 witnesses, all rational quartic coefficients, all derivative fractions, all full units and their residues, every field/split classification, full Smith factors, conductor exponents, and both original FS13 signs at each of the four labels. The symbolic checker evaluates the complete original polynomial P at the original FS13 coordinates; it proves the resulting target exactly for both signs.

ISR29 proves the full nilpotent Jordan list and states the essential restriction `m>=2`. When the relation comes from a derivative, the residue characteristic must also not divide m. ISR30–31 prove the actual unit-scaled cofactor-field isomorphism, including the Hensel recurrence and the explicit first residue root `c=5 mod 1201` for the first witness.

ISR32–34 carry every inclusion, ideal generator, and multiplication to both original complex conductor receivers through the unchanged RD/GD substitution matrices and actual inverse-conductor recurrence. All original Gram factors remain in the full matrix formulas. Arithmetic and complex base changes are performed separately, never by assigning a p-adic valuation to a Gamma mass.

## Full root PS1–25 review

PS1–12 are established independently by ISR1–15, including equality of every Smith factor and the perfect finite pairing. The conductor generator matrix is checked as a complete matrix in both witnesses, not only through its determinant.

For PS14, ET1–3 give the exact coefficient inclusion `K(C0)=diag(1,-C0/5,C0^2/25)`. The actual witness has `D0=-p C0/5`; its reciprocal equation implies both original coefficient cubic relations. Thus evaluation at D0 and at p gives algebra maps from the two entire rank-24 signed algebras to the actual rank-eight algebra. The matrices are `(I,D0 I,D0^2 I)` and `(I,p I,p^2 I)`. Their products with K agree entry by entry. Their leading identity block proves surjectivity; solving for the first eight coordinates gives every kernel vector in PS15 and rank 16. Evaluation commutes with the unchanged r and sigma relations from ET11, so this is an algebra specialization, not only a vector-space square.

PS16 is exact. The specialized coefficient conductor has image `C0^2 E` because the P evaluation is surjective. Since I is an E-ideal, inclusion of this image is equivalent to membership of its scalar generator `C0^2` in I. The exact branch ideal from ISR11 makes that membership equivalent to `2v_p(C0) >= max_i(3m_i+epsilon_i)`. For one divisible denominator `v_p(C0)=1`, and a closer unit pair with gap n has branch exponent `3 floor(n/2)+(n mod 2)`; this is at most 2 precisely for n<=1. For two divisible denominators `v_p(C0)=2`; the closer pair has exponent `3 floor((n+1)/2)+((n+1) mod 2)`, at most 4 precisely for n<=2. All scalar units in the ideals are retained. Failure of this specific inclusion does not invalidate the commuting algebra specialization.

PS17–22 independently match every coefficient and residue computed in ISR24–28. The reduced primary blocks are only the collided components, with the other roots and signs still present. The original affine first-coordinate valuations are the exact negatives of half the derivative valuations for each separate sign.

PS23–24 use exactly the original receiver on each parity component. The determinant of the original generator matrix is `A^8(det V)^2 p^sum m`; its Hermitian Gram determinant therefore multiplies the original Gamma determinant by `|A|^16 |det V|^4 p^(2 sum m)`. Every factor is nonzero for both actual witnesses. This does not equate the source and target receiving metrics.

For PS25, the proposed minimum representative is `(v,conj(D0)v,conj(D0)^2 v)/(1+|D0|^2+|D0|^4)`. Multiplying by Pi_D proves the constraint. Its inner product with an arbitrary full kernel vector is exactly `v* Gamma (w0+D0 w1+D0^2 w2)/d_D = 0`. This gives the attained minimum and its unique full-kernel orthogonal correction. The checker proves the entire 8×8 attained Gram identity for an arbitrary full symbolic Gamma matrix, not only a diagonal metric or a scalar example.

For the source-to-target map in the final PS paragraph, let L be the original doubled conductor expressed in orthonormal coordinates for its two different metrics. The complete matrix is `(1,D0,D0^2) tensor L`; multiplying by its adjoint gives `d_D L L*`. Hence its eight nonzero singular values are exactly `sqrt(d_D)` times those of the original doubled conductor, with a 16-dimensional kernel. This verifies the full spectrum statement without substituting a changed metric.

## Verification scope

The exact checker covers symbolic residue inverses and the full FS13 polynomial return; both complete actual witness matrices; all normalization/residue/trace/conductor comparisons; every Smith factor on seventeen additional valuation patterns through gap order eight; six fractional-chart patterns through v_p(S)=6; nilpotent ranks for every m from 2 through 8; the entire rank-24 specialization square and full kernel bases; and PS25 with an arbitrary full symbolic receiving Gram. Those bounded samples supplement the general proofs in the source; they do not replace the proofs or assert new ES witnesses.

No original linear-conductor order jump, Frobenius action, zeta-zero trajectory, or RH endpoint is asserted by this finite arithmetic derivation.
