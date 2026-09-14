# Independent final mathematical review of WDB

Date: 2026-09-13.
Reviewer: `/root/weil_ii_bootstrap_detail/dyadic_source_review`.
Result: **PASS** for the exact mathematical candidate identified below.

## Reviewed artifact

- File: `work/rh_counterfactual_20260913/total_object/weil_ii_dyadic_bootstrap.tex`.
- Bytes: **38182**.
- SHA-256: **e72509638eafe7a324ab6387f21ac0ed53327760d43938a499179df8116065d1**.
- Mathematical displays reviewed: WDB1–42, WDB13a and WDB30a, with all intervening definitions and proofs.
- The full first candidate and full revised candidate were read; the final simple-pole addition was then read separately and the candidate hash was checked from the filesystem. The final read's one output truncation at WDB17–18 was repaired by a separate complete read of that passage. Two final layout changes in WDB36 and WDB42 were then read and verified, as detailed below.

The source comparison and full derivations underlying this review are recorded in `weil_ii_dyadic_source_review.md`. Current local French and English S20 passages were compared with the controlling original scan. Printed pages 200, 202, 203 and 204 were inspected visually. A separate child reviewer independently checked the finite-cover trace and final twisted-dual pairing.

## Mathematical checks

1. **Quantifiers, conventions and twists.** B_k ranges over all curves, sheaves, weights and finite fields needed for its later application on the pencil base. The weight is consistently 2 log_q of the complex modulus. The auxiliary weight-zero sheaf is related to the original by an explicitly invertible rank-one twist, with the original weight restored in WDB29. An arbitrary scalar twist is correctly confined to the Weil-sheaf setting; it is not asserted to extend continuously to the profinite arithmetic Galois group.

2. **The base and strict earlier input.** The affine/projective passage uses the correct compact-support surjection. The strict bound 2.2.10 precedes the curve theorem in the source and is not deduced from that theorem. The final added sentence accounts for the possible simple pole in the geometrically constant irreducible case: cancellation by a numerator root would change that proved pole order. The strict bound is not silently replaced by a weak bound at the integer cutoff.

3. **Reality and published notation defects.** WDB13 correctly uses compact-support cohomology of the open fibre and ordinary cohomology with extension by zero on the proper fibre. WDB13a has the correct +1 Tate twist. Its argument proving reality of H_c^2 first, then H_c^0, then H_c^1 is noncircular. Component permutation is handled by the determinant of F^d with variable t^d. Both original printed defects are accurately identified and do not become errors in the new proof.

4. **The actual boundary quotient.** WDB16 is the correct vanishing-cycle exact sequence. The induced filtration in WDB17 is the intersection filtration on the special stalk. Therefore the exact associated-graded quotient in WDB18 is a graded piece of the generic/special cokernel, which injects into the vanishing cycles. The quotient A_{a,t} is consequently a genuine subquotient of those cycles. This does not assume that an arbitrary filtration remains exact.

5. **Integrality and the alternative.** WDB14–15 retain all three local geometries, the branch sign representation and the interior-node Tate twist. In WDB19 a nonzero quotient has a Frobenius eigenvalue of weight both integral and in b_a+Z, proving b_a integral. If all quotients vanish, every generization map is an isomorphism; the local inertia acts trivially, the constituent extends lisse to geometric P^1, and its H^1 vanishes. No bound is incorrectly imposed on its remaining arithmetic constant-fibre action. WDB21 and the corrected conjunction in WDB42 use integrality and the strict inequality together.

6. **Both cohomology levels and Leray.** WDB25 verifies the degree-zero and degree-two fibre bounds, then separately transfers them to the outer base cohomology groups. Constructible boundary stalks and component permutations are included. Only the middle base H^1 uses B_k, hence only one copy of the error appears. The passage to the Leray abutment requires subquotients and a finite filtration, not degeneration at E_2 or Frobenius semisimplicity.

7. **Preservation of the eigenvalue.** WDB27–28 give actual Kunneth and blow-up injections and retain the extra exceptional summand. The tensor-square nonvanishing proof is valid in odd cohomological degree because it concerns two factors of a product, not an exterior square or the cup square on one curve. WDB29 then computes the precise factor one half in the weight error.

8. **Removal of the hypotheses.** Finite-field extension preserves weights exactly. WDB30a supplies the multiplicity-weighted sheaf trace for every finite surjective map of smooth curves. Finite flatness follows from torsion-freeness over the target discrete valuation rings. The local fibre lengths sum to the degree, the unit/trace composite is degree times identity, and its scalar inverse gives a Frobenius-equivariant compact-cohomology retraction. Ramification, inseparable multiplicities, and degrees divisible by ell are not lost.

9. **Finite contradiction and duality.** WDB31 chooses a finite K with 2^(−K)<epsilon, including epsilon=1, epsilon>1 and dyadic boundary cases. The exact image pairing in WDB33 follows from the transpose compact-to-ordinary maps and their annihilators. The +1 twist makes its target the trivial coefficient field; WDB34 consequently uses alpha^(−1), with no missing q factor. The pure equality is for H^1(X,j_*F), while all H_c^1 is only given the upper bound.

10. **Mixed coefficients and the extension direction.** The smooth-target reduction and relative tame boundary base change are retained before WDB36–38. WDB39 is the correct long exact sequence. The revised prose correctly describes R^1 f_!F as an extension of the entire pure R^1 bar f_*j_*F of weight n+1 by the displayed boundary cokernel of weights at most n. The degree-zero and degree-at-least-two consequences have the correct direction and twists. The kernel reduction uses the preceding bound n+i−1, so it does not lose an index. WDB40 has the exact Poincare-dual twist by d, and WDB41 draws purity only for the specified compact-to-ordinary image.

## Corrections made during review

The author corrected the initially reversed extension wording after WDB39; made the integrality conjunction explicit in WDB42; retained the smooth-target reduction; expanded the cover trace and perfectness of the image pairing; supplied the affine/projective base argument and the complete reality argument with corrected Tate twist; and added the simple-pole noncancellation sentence. The nonstandard `longtwoheadrightarrow` command was replaced by the standard `twoheadrightarrow`.

## Scope and remaining production work

No mathematical defect requiring a correction remains in the reviewed candidate. This PASS is a check of the attributed exposition of Deligne's argument and its exact algebraic steps against the cited primary source. Its geometric and etale-cohomological inputs remain the explicitly cited results of Deligne and the underlying cohomology theory. It neither certifies an RH proof nor asserts that the Split-Zero programme already supplies a finite-field realization of the displayed sheaves and maps.

The first complete mathematical PASS covered 38169 bytes at SHA-256 `c96daca08e966e2fcb768c564e7d88ea44c4fcbfb860734dbe98d5d75469fb83`. The author then changed only the display layout of WDB36 and WDB42: the relative geometry was put into a gathered display and the concluding implication chains were split onto separate lines. This reviewer read both revised displays and reconstructed the prior file entirely in memory by replacing precisely those two displays with their previously reviewed contents. The reconstructed bytes hashed exactly to the prior candidate SHA-256. This confirms that all other bytes remained unchanged and that the final 38182-byte file at the hash above inherits the complete mathematical PASS.

The author reports a successful three-pass standalone XeLaTeX build producing ten pages without overfull or underfull boxes, undefined references, or missing glyphs. Compilation and visual layout verification are separate production work; this receipt does not claim those checks were run independently by this reviewer. Any subsequent change requires a corresponding hash addendum.
