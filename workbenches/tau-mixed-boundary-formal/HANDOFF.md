# Mixed-boundary integration handoff

Use the original SplitZero modules and current branch state; do not re-adjoin a scalar zero or replace the full tensor source by its sum-generated cyclic subspace. This branch recovers the entire 19-file unfinished mixed-support/metric contribution and its ancestry, repairs proof errors, and adds a constructed boundary-kernel equivalence with the original support quotient maps. STATUS.md records the actual observed compiler checkpoint.

## Formal interfaces

`BoundarySocle.socleEquiv`: for injective f and injective multiplication by v on M, the actual quotient M/vM maps isomorphically to ker(v:M/(vf(M))->M/(vf(M))) by [x]->[f(x)]. Its inverse is proved; the desired equivalence is not an input.

`BoundarySocle.diagonalSocleEquiv`: arbitrary nonnegative exponent family n_i over a domain with v nonzero, on the actual diagonal lattice v^(n_i+1). Retains every ordered tensor index.

`sourceAction`, `targetAction`, `action_square`, `divide_intertwiner`: carry the actual source/receiving operator through the lattice and its quotient; a polynomial intertwiner before specialization suffices.

`BoundarySocleSupport.comparisonHom`, `original_square`, `total_injective`, `range_iff_supported_killed`: the same map on existing Relations.quotientDiagrams, with a genuine equality of original G(R)-linear total maps. The image is characterized by v^bullet*y=e*y, not by v^bullet*y=tau. No injectivity of arbitrary support transitions is assumed.

`present_empty_face`: an empty coefficient face under a nonbottom outer source/leg label still has that outer supported zero. It is not the empty finite sum at the global bottom.

Recovered `MixedSupportMetric.gathered_gram` retains every cross pairing after the original transports. `gathered_zero_iff` tests membership of the transported sum in the receiving relation submodule. `mixed_canonical_classes` uses actual original-boundary primitives of the canonical section changes.

## Apply to the source

For O=C[a][[v]], D=diag(v,...,v^m), choose f=D/v. The equivalence is C[a] tensor E_rho -> ker v, z^b -> v^b epsilon_b. The equation (rho I+v(N+aR)) D = D(rho I+N+a v^m R) supplies equivariance. At v=0 the Tor/kernel action is rho I+N; the ordinary quotient action is rho I. These are distinct, jointly retained terms.

For the single ordered tensor lattice use exponents k+|b| and f-exponents k+|b|-1, not only the sum-coordinate cyclic block. Do not identify its cone with the tensor product of individual cones without the extra comparison. Finite-field inertia and its character twists remain separate from the spectral nilpotent.

## Source correction and quantitative interface

The new ZIP has a hash-consistent missing MB20--44/46--47 body. Preserve it as historical input; the reconstruction here is not claimed to restore the absent prose verbatim. Attach the full original irregular connection and the unchanged arithmetic metric in any further period/specialization application.

The accepted SP1--13 source refines the general metric four-endpoint estimate from 2q to 2q-1 using an actual range intersection; retain that refinement with attribution. Its analytic integration and the tensor-uniform arithmetic estimate are not newly certified by this branch.
