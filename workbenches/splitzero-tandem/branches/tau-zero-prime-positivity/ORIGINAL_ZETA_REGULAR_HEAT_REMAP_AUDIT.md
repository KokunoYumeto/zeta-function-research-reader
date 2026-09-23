# Independent audit of the owner's original-zeta remap proof

23 September 2026. The complete owner source `ORIGINAL_ZETA_REGULAR_HEAT_REMAP.md`, OZR1–36, was read after completing the independent derivation RHR1–33 in `ORIGINAL_ZETA_REGULAR_HEAT_REVIEW.md`. No owner source was edited by this audit.

The initial complete reading identified the corrections below. A subsequent read during editing recorded owner-source SHA256 `23d73efb9e7604333622b83d36b5a42ac9c72a48fe4583c99190563060e1f7fa`; this intermediate hash is not a claim of final corrected-source acceptance.

## Corrections and exact scope

1. **Target coefficients in OZR13.** The derivatives of the gauge and coordinate are evaluated at the target point, whereas the source function and its spatial derivatives are evaluated after affine composition. Placing the target coefficients inside braces followed by composition is literally a different formula. The exact identities are
   \[
   \nabla_s\mathcal T_tf(s)=M_t(s)\{\chi_t'(s)f(\varphi_t(s))
   +\alpha(\nabla_zf)(\varphi_t(s))\},
   \]
   \[
   \nabla_s^2\mathcal T_tf(s)=M_t(s)\{((\chi_t'(s))^2+\chi_t''(s))f(\varphi_t(s))
   +2\alpha\chi_t'(s)(\nabla_zf)(\varphi_t(s))
   +\alpha^2(\nabla_z^2f)(\varphi_t(s))\}.
   \tag{ORA1}
   \]
   The following time-derivative line needs the same convention: its coefficients are \(\dot\varphi_t(s)\) and \(\dot\chi_t(s)\). OZR14 already has the correct intended polynomial coefficients. The owner also identified and is repairing the literal backslash-n-plus characters in that display.

2. **The OZR24 summation bound.** Its upper bound uses \(p-1\), although \(p\) previously denotes a complex test-pole location. Define \(M\) as the pole order of the test at that point and sum from \(j=0\) through \(M-1\). The formula is otherwise correct:
   \[
   \operatorname{Res}_p(Af'/f)
   =nA_0+\sum_{j=0}^{M-1}A_{-j-1}[h^j](u'/u).
   \tag{ORA2}
   \]

3. **Exceptional contact order.** The exact identity
   \[
   C R_f=(\partial_\theta-\tfrac14\partial_z^2)(Cf)
   \tag{ORA3}
   \]
   identifies the BT numerator residual with the original-zeta residual ratio. The contact multiplicity is the numerator order \(m=\operatorname{ord}(Cf)=d+e_z\). At the pulled target the raw order is \(m-e_s\), while the coefficient in OZR18 remains \(-m(m-1)/4\). Making this explicit prevents substituting the raw order into the numerator contact coefficient when the target is exceptional for \(C\).

4. **Source and target test domains in OZR20–21.** The source receiver \(R_\theta(B)\) requires the poles of \(B\) to avoid \(D_\theta\). For the target test \(A\), the precise requirement is
   \[
   \mathcal P(A)\cap\varphi_t^{-1}(D_\theta)=\varnothing,
   \quad\text{equivalently}\quad
   \mathcal P(A\circ\varphi_t^{-1})\cap D_\theta=\varnothing.
   \tag{ORA4}
   \]
   Avoiding the untransformed source divisor alone is insufficient. OZR26's Cauchy-pole domain must refer to the pulled-back moving divisor as well. Fixed-factor resonances remain admissible under the specified local finite part.

5. **Raw skew-defect locator.** The cited strict non-Hermitian defect is **OZK17**, not OZK20. The complete adjacent derivation OZK16–20 was checked for this locator. OZK17 gives the strictly positive series for \(R_{01}-R_{10}\); OZK20 instead gives the compensated coefficient-tower formula.

## Independently verified calculations

OZR4–10 agrees with RHR4–9, including the full exceptional unit product OZR9. Gamma recurrence supplies the factor two in its residue and every retained finite product. Multiplication by the nonzero unit and affine substitution give the stated valuation-shifted finite-jet isomorphisms. OZR11–12 retains precisely the additional regular-unit derivatives and the unit ratio needed in the raw original-zeta curvature and marked residue. The marking order remains independent of the raw and numerator valuations.

The intended residual OZR14 agrees term for term with independent RHR12, and all six equations and solutions OZR15–16 have the correct factors. The necessity test uses three legitimate original meromorphic solutions. Under those equations OZR17 follows exactly; ORA3 states its connection to the contact source without asserting a residual for the actual unmodified heat solution.

The locally finite signed-divisor identity OZR19 is correct even at collisions. In particular its last line does not require the three component divisors to be disjoint. Finite-part evaluation at the specified original spatial coordinate is invariant under the affine substitution. The stated rational decay and zero-count bound prove absolute tail convergence. Thus OZR21 is valid at its correctly typed domain ORA4.

The residue formula OZR23 has the correct sign both at infinity and at a fixed-divisor/test collision:
\[
\widetilde R^{\rm fp}(A)=
-\sum_{p\in\mathcal P(A)}\operatorname{Res}_p(A\widetilde\ell)
+2a\lim_{s\to\infty}s^2A(s)
+\sum_{p\in\mathcal P(A)}n_p\operatorname{FP}_pA.
\tag{ORA5}
\]
For a divisor point outside the test poles, the test-pole residues of its rational partial fraction sum to minus its evaluation. At a coincident test pole those residues contain all finite poles and sum to zero, requiring the final displayed correction. The linear gauge derivative contributes exactly the middle term by its coefficient of \(s^{-1}\) at infinity. The normal convergence argument isolates finitely many colliding terms before termwise contour residues, so it does not apply a genus-one product formula to the order-two gauged target.

For the Cauchy test the infinity coefficient is \(-1\). Its actual compensated divisor kernel is therefore the logarithmic kernel minus \(2a\), exactly as OZR28 states. The coordinate identity gives the factor \(\alpha^2\), and the imaginary linear-gauge terms cancel. A vanishing Cauchy denominator is a removable divided difference when the test poles remain outside the moving numerator divisor. The fixed-factor finite parts cancel in the compensated receiver. This does not assign a regular value to a genuine moving-zero/test-pole collision.

OZR30–33 gives the correct complete negative index. Reflection preserves the weights and makes the stated involution self-adjoint. The rational evaluation vectors lie in the weighted sequence space by the square-denominator bound. Orthogonality to the zero-infinity-coefficient subspace annihilates every positive derivative of its normally convergent Cauchy transform; constancy on the connected punctured plane then forces all residues to vanish. This proves the stated dense map with exactly fixed first coordinate. The bounded direct-sum form and finite-dimensional negative-frame approximation prove both inequalities for the index, including infinite index. The raw uncompensated original divisor is correctly excluded from that Hermitian index assertion.

The support carrier and linear lifts in OZR34–36 retain lower zero points separately from arbitrary values of functions on those points. Substitution verifies the two signed corrections in the full supported identity. No spectrum isomorphism, new boundary metric, or change to the original arithmetic initial datum is inferred from the complex-linear transport.

No further mathematical correction was identified in OZR1–36 during this complete reading. The corrected source was subsequently reread as recorded below.

## Corrected-source acceptance

The complete revised owner source OZR1–36 was reread, with SHA256
`d55770936f9815cbffa9546a7ce0d544851016e2f5febf2598d4909b06ba952f`.

All five listed repairs are present and correct. In particular OZR13 and its time derivative now evaluate every target coefficient at the target point and every source derivative at the affine image. OZR14 no longer contains the stray characters. The pole order in OZR24 is explicitly defined as M, the contact paragraph distinguishes the numerator multiplicity from the target raw order, the source/target test domains are explicit, and the skew-defect citation is OZK17. The additionally inserted full Gaussian profile and valuation-shifted jet quotient agree with the previously verified definitions and local isomorphism.

**Final audit result:** no further mathematical correction was found necessary in the corrected OZR1–36. The full signed-divisor trace, its finite-part extension, its infinity-residue sign, the compensated Cauchy comparison, and the full negative-index argument are verified on their stated domains. This acceptance does not assert the missing global positivity estimate for the original arithmetic family or an RH proof.

## Final base-map clarification

The revised paragraph after OZR36 was read and accepted in the final controlling source with SHA256
`cf4fa8ab726b83a056035f31c7f4c2be368dd2cf46fae11901b66601ab36c83d`.

It now specifies the coefficient-semiring map as the identity on S. Pullback under that identity sends each prime ideal to itself. Separately, OZR4 acts on the function space and retains its label set; no ring-spectrum map is inferred from this complex-linear transformation. This is the correct mathematical distinction: a labelled vector-space carrier is not thereby supplied with a ring multiplication or prime spectrum. The change clarifies the base map without changing any displayed equation or analytic conclusion. The previously recorded acceptance therefore applies to this final source hash.
