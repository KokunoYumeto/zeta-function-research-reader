# Full-packet formal boundary calculation

## Assigned scope

Prove the exact formal boundary comparison of the original full packet polynomial, with its original primitive constant, original theta Taylor unit, Jacobian, full primary multiplicities, ordered tensor factors, and mixed-support/source-leg labels. The original global polynomial is retained. No modification of the sealed cumulative edition or delivered web handoff is permitted.

## Sources read

- `work/marked_product_boundary_connection_20260913.tex`: original polynomial lattice, full connection, source map, original periods and metric.
- `work/rh_counterfactual_20260913/total_object/single_primary_boundary_control.tex`: complete homogeneous-primary calculation, contour signs, gamma factors, and multiplication defects.

## Work and decisions

- Defined the global completion as C[s][[u]], not C[[u]][s], and the local coefficient rings as C[[w]][[u]].
- Constructed the exact phase coordinate with an explicitly retained Nth-root branch and the degree-one Jacobian.
- Proved complete coefficientwise remainders, explicit cohomology inverse, and explicit chain homotopies.
- Derived all coefficients of the comparison matrix by formal residue substitution and monomial remainder, so no stationary-phase theorem is assumed.
- Proved the exact connection gauge identity and the unexpected constant determinant equal to the branch-weighted confluent Vandermonde determinant.
- Retained the original arithmetic and unit matrices by exact transport, with their marked multiplication formulas and their deformed Leibniz defects.
- Distinguished the unital coefficient algebra isomorphism from the Jacobian module map. Mixed-support labels are retained coefficientwise, with no unsupported claim that the Jacobian is a semiring morphism.
- Specified the full local multivariable ring separately from a mere u-completed algebraic tensor product. Successive one-variable contractions compute all ordered local tensor pieces.
- Constructed formal horizontal primary projectors and their marked CRT reductions, including the case of equal critical values.
- Retained the exact original L2(dx) theta Gram form through the phase-coordinate and full-unit maps.

## Independent verification

`formal_boundary_review` independently derived all core formulas before reading the draft. Its first complete source read passed the mathematical core and requested only two germ/nonempty-set wording corrections plus the explicitly addressed tensor-topology clarification.

`formal_boundary_exact_check` verified three rational unequal-multiplicity polynomials, including nonunit and negative phase-root branches. Its checks are algebra tests, not claims that those roots are zeros of xi. See `checks/README.md` and its exact JSON receipt.

The independent reviewer also derived a constructive analytic comparison through the original global rays. A companion proof is being written: ordinary global period monodromy has trace -1, whereas the formal primary period monodromy has trace minus the number of roots. For more than one selected root this proves the complete formal gauge cannot be convergent. The analytic period determinant in the original source is being checked before that proof is finalized.

## Remaining in this bounded task

- Final read of the corrected source and the extra projector/metric calculations.
- Complete and review the original-global-ray monodromy companion.
- Compile the standalone TeX and inspect source diagnostics.
- Return exact file hashes and proved scope to the coordinating agent for integration; no RH endpoint is claimed by this calculation.
