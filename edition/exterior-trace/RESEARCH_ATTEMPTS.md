# Research attempts: motivation, result and current limit

## Full zero jets instead of a list of eigenvalues

**Aim.** Represent the selected zeta zeros in the original theta construction without losing multiplicities, nilpotent directions or the invertible local factor of the completed zeta function.

**Reason.** Eigenvalues alone do not determine the quotient algebra or its metric when zeros repeat. The full polynomial quotient keeps the derivatives that a repeated zero requires.

**Result.** The reader gives the source-to-quotient maps, polynomial-division primitives and full-unit comparison maps. These are exact finite constructions. They do not supply a global estimate for the zeta zeros.

## Cyclic sums and the rank-two arithmetic control

**Aim.** Study sums of k spectral coordinates while retaining every repeated-root jet at each sum.

**Reason.** Tensor products contain many directions that do not arise from one polynomial in the total coordinate. The cyclic subspace isolates exactly that image, rather than identifying it with the whole symmetric tensor space.

**Result.** The annihilating polynomial is computed from the maximum local jet depth among colliding tuples. The least-norm source lift gives its Gram matrix. In the original weighted polynomial basis, the recurrence telescopes to two boundary terms, so the metric departure operator has rank at most two and trace zero. Its exact nonzero eigenvalues are +epsilon and -epsilon, with the cross term retained in epsilon.

**Limit.** Epsilon depends on the actual arithmetic moment matrix. A finite rank statement is not an asymptotic bound on its size.

## Exterior trace amplification

**Aim.** Accumulate positive real spectral excess without paying for an independent control error in every exterior direction.

**Reason.** The exterior lift of a rank-two trace-zero Hermitian operator still has largest eigenvalue epsilon. The determinant line of the complete positive spectral subspace sums the positive real departures from the centre.

**Result.** The written proof gives `L <= epsilon`, the determinant-volume identity, the exact source lift with its factorial, and the correction between cyclic-block and full-source metrics. An exact off-line quartet forces cubic growth of L for simple zeros and quartic growth for repeated zeros. The proof also records the empty exterior degree, the zero-control case, and the difference between an exact quartet and a larger containing packet.

**Limit.** The calculation identifies the arithmetic upper estimate that would rule out such growth; it has not produced that estimate. Finite synthetic Gram matrices test identities, not the missing arithmetic estimate.

## Diagonal coordinates and alternation

**Aim.** Relate the two-block exterior construction to the original diagonal coordinates, source norm and polynomial quotient.

**Reason.** A change to total and relative coordinates can expose the alternating factor, but it can also hide a unit, a Jacobian or a metric correction if those are dropped.

**Result.** Section 39 keeps the exact coordinate map, the relative factor and the source-energy identity. Section 40 explains why alternation of already symmetric k-blocks is not global alternation of all kp individual factors: for k at least two, the latter annihilates that symmetric image. The displayed maps establish the relation rather than treating the two constructions as interchangeable.

## Conormal layers and cyclic depth

**Aim.** Differentiate a relation before passing to a quotient where that relation vanishes, and retain its higher-order layers.

**Reason.** Differentiation lowers ideal order. Dropping the relation first would erase the conormal information and the extra multiplier term.

**Result.** PR21 formalizes the descended derivative between adjacent quotient levels, the commuting tower square, the polynomial chain rule and the finite degree extremum. The public research note supplies the longer monomial, collision and module-retraction calculations with explicit formulas. The post-merge Lean run passed on the actual main-branch revision.

**Limit.** The formal declarations have their stated finite algebraic scope. They do not certify the whole arithmetic packet construction or yield a bound for its large-k metric.

## How the continuation fits

Companion research readers have separate PDF, source and verification records. Their results are not attributed to this main-reader package merely because they belong to the same project. The publication manifest identifies the actual paired artifacts and immutable revisions. Earlier complete Stieltjes and sum-connection sources remain available in the unchanged previous downloads.
