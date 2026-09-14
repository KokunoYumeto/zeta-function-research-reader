# Review of the live coefficient update and original PC30 insertion

Reviewed 2026-09-13 by the independent coefficient reader. No source files were edited.

The complete original PC28–PC31 passage was read in `work/cumulative_next_edition_staging_20260913_v19/reader/tex/period_critical_kernel_bridge.tex`, lines 419–483. The entire new `PC30_coefficient_insertion.tex` was read at SHA-256 `d6f790227f29f9b33a18cf9a97e7382bcedc26ec1e0f0d5d8f8e6faaf740e8df`. Corrections to `tensor_primary_update.tex` were checked at SHA-256 `b3493b70b40ce3e0691e8aa974748f166e8b8e23ac723c4a929011e0e66845f7` against the earlier full proof reading.

## Corrected tensor fragment

The requested explicit rho-in-A hypothesis, coefficient-ring renaming including subscripts and tensor products, two exponent corrections, and the two multi-alignment environment changes are present. The newly added localization comparison is correct: a map to a field extends uniquely across the inversion of an element exactly when its image is nonzero. This proves the stated original coefficient-to-phase map and its exact obstruction at m=1,p=2. The surviving coefficient vector in that exceptional case has K=0, is multiplied by the retained nonzero unit, and has nilpotency index one. The finite-field phase statements retain p>m+1 and their actual denominator exclusions.

The previous proof-level acceptance of BPC.1–14 and BTF.8–11 applies to this corrected version. No further issue was found in the requested tensor-fragment corrections.

## Unequal-order local calculation PC30a–e

The new local map is precisely the restriction of the original weighted sum map PC29 to the specified ordered primary tuple. It retains the original sum coordinate S, all centers, unequal multiplicities m_i, and the full unit. With p greater than every order in that tuple, each individual b_i! is invertible. Therefore the full vector V_r, its unit multiple W_r, and the identity J^r=r!V_r are defined on the specified coefficient localization. The proof using a pivot in each total degree establishes a split containing lattice, and multiplication by the full unit transports the splitting exactly.

In those bases the original cyclic map is diagonal with entries r!. Consequently the quotient, saturation, free complement, specialized kernel and image, and Tor connecting map all follow by the same exact diagonal calculation already independently proved for TCL. The unequal capacities do not change that argument: every degree through D occurs by filling the capacities successively, and all retained pivot coefficients are units. The lower nilpotency witness J^d U=d!W_d for d=min(p-1,D) proves the precise image index; J^p=0 on the full tensor and J^(D+1)=0 supply the upper bound. The original reduced abstract cyclic source retains index D+1.

## Global residual collisions PC30f–g

For an existing coefficient map on the full one-factor CRT data, the retained polynomial identities and their inverses base change to the product of the original ordered local factors. Once the prime bound holds for every one-factor order, the local minimal polynomial at tuple rho is (X-mu)^e, with e=min(p,1+sum_i(m_rho_i-1)). Indeed the proved nilpotency witness forces this exponent. More explicitly, a polynomial whose vanishing order at mu is a<e is (X-mu)^a Q(X) with Q(mu) nonzero. Evaluating Q at mu+J is a unit: factor out Q(mu) and invert the remaining one plus nilpotent by its finite geometric series. Therefore such a polynomial cannot annihilate that factor.

On the product, simultaneous annihilation is the intersection of these principal ideals in the polynomial ring over k0, hence their least common multiple. Grouping equal residual sums takes the maximum of their exponents. The original reduced chi annihilates the product because its unreduced evaluation is the zero polynomial class in the retained algebra; therefore this least common multiple divides reduced chi. Finally, evaluation at the identity vector has exactly the same kernel as the multiplication operator, and multiplication by the full reduced unit is an automorphism. This proves precisely the ideal quotient (psi)/(reduced chi) and the weighted module isomorphism from k0[X]/(psi) to the actual image. No sum-stage CRT specialization is required by this proof.

Two corrections were sent for the recorded draft before final acceptance:

1. The global paragraph must explicitly assume p>m_rho for every rho in the entire one-factor set Z. The earlier bound p>max_i m_i belongs to one fixed tuple and does not cover other tuples automatically. Without that global hypothesis another order can exceed p, making the formula with min(p,D+1) false on that factor.
2. The product defining psi must range over attained residual sums, so each displayed maximum is over a nonempty set. State the empty-Z case separately, with psi=1 and the original zero source and image; otherwise the global maximum or a maximum over an unattained residual sum is undefined.

The local PC30a–e proofs pass. The global PC30f–g calculation passes with the explicitly described global prime bound and attained-sum domain; this receipt records the exact required repairs and does not claim they were present in the initial hash above.

## Final corrected-version verification

Read the corrected global paragraph and its formulas at final insertion SHA-256 `a2cbdd4cd71630e07751bfd9ca4e64af4a76834f84f24eda851dcac961c0472b`. It now explicitly assumes p>m_rho for every rho in Z, defines the attained residual-sum set, restricts the product to that set, and states the empty-Z case with psi=1 and zero source and image. Each maximum is explicitly nonempty, and the global inequality is correctly vacuous when Z is empty. Both requested repairs are present. Final result: proof-level PASS for PC30a–g at this hash and for the corrected tensor coefficient fragment at `b3493b70b40ce3e0691e8aa974748f166e8b8e23ac723c4a929011e0e66845f7`.

## Explicit minimal-polynomial proof and single-primary conclusion

Read the added finite-geometric-inverse proof in PC30f–g and re-pinned the insertion at SHA-256 `2035d2e0553d0019f2090c0395e87388f48366cabd8f059b651e6e83d61a07a2`. The argument factors a nonzero test polynomial as (X-mu)^e Q(X), evaluates Q at mu+J, and exhibits its inverse using the finite geometric series in its zero-constant nilpotent part. It proves exactly that the test polynomial annihilates the factor precisely when J^e=0. The original global prime bound, attained-sum range, empty-carrier convention, and exact kernel quotient remain present. PASS for this latest PC30 insertion.

Read every line of `single_primary_conclusion_update.tex` at SHA-256 `b84e1aef7d27468bb8135798e8b7e1dac310142fa3d87e173218f1f02933fd30`. The character average and its one-factor, m=1 and higher-tensor cases are exact. The source projector is the full-unit conjugate and its period intertwiner retains the inverse unit. The terminal character condition n divides k retains the original multiplication and dilation scalar. For the given phase specialization p>m+1, the additive factor cancels exactly when kc=0; the displayed inertia dimensions and Swan conductors follow from the complete ordered character decomposition. The terminal sheaf condition pn divides k in the c nonzero branch uses p coprime to n. All these cases retain the original source and finite-field scalar domains; the references to the exact coefficient and CRT extension tests do not assert an additional specialization.

One presentation repair was sent before final pin: the last paragraph introduces an undefined localized ring mathscr R and calls its torsion sum merely a quotient. It should use the defined BPC coefficient ring mathscr S and explicitly identify the quotient as Lambda_U/L_U. The full tensor cokernel also has the free complement and must not be identified with that torsion sum. The calculations themselves agree with the accepted BPC and BTF proofs.

Verified the corrected conclusion at final SHA-256 `00270df74a5e4cccb8b8bb78928a2299483688e2ffb0a5e571d0b5bafce6f16b`. It defines mathscr S=A localized at ker(alpha), names the image L_U and its saturation Lambda_U, identifies the torsion sum as Lambda_U/L_U, and explicitly retains the free complement in the full tensor quotient. The stated coefficient domains and references are unchanged. Final result: PASS for the complete single-primary conclusion at this hash. No outstanding issue remains in the reviewed fragments.
