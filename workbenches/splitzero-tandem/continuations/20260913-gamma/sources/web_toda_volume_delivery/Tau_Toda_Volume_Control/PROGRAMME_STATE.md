# Programme state — source–boundary volume continuation

## Current object

Original tau-base marked arithmetic geometry; original infinite quotient G(Z)->Z; original theta complex, strong source topology, cyclic sum algebra C[S]/chi and its arithmetic inclusion with the full unit. The original canonical metric is evaluated at auxiliary tilt theta=0.

## Completed in this continuation

- Read the new formalization report and pinned PR #21 note. Retained exact depth pullbacks, derivative transition squares, all multiplier terms and the empty case; did not promote written CRT/monomial consequences into additional Lean declarations.
- Constructed two positive scalar Hankel determinants from the actual one-factor arithmetic Laplace transform M_h and the original relation filter.
- Proved det G_N = source determinant / relation determinant, with the source basis determinant and all coordinate phases retained.
- Derived both classical Toda identities on these exact inputs, and the difference formula for the determinant-line curvature.
- Constructed the actual boundary-valued derivative of the finite least-norm representative, and its rank-one outgoing/incoming curvature maps.
- Expressed the complex cross term in the rank-two control as the scalar `i(Tr((A-k/2)/i) - derivative log detG_N)`.
- Derived the exact scalar allowance and the two-step volume upper bound, retaining both losses and the minimal-degree endpoint.
- Combined with the preceding exterior theorem to derive a required minimum volume contraction for any positive aggregate spectral defect.
- Constructed the actual complex-dilation expression for M_h. For h=1, supplied the full exterior incomplete-gamma double sum and numerical initial data.

## Exact next analytic quantity

At N>=deg chi, compute the source recurrence coefficient a_(N+1) and the source/boundary volume ratio R_N=detG_(N-1)/detG_(N+1). A sufficient bound is

    epsilon_N <= sqrt(a_(N+1)) (R_N-1)/(2sqrt(R_N)).

The exact formula subtracts the consecutive-jump imbalance and the retained phase square. Therefore failure of this coarser estimate to be small does not preclude using the exact formula; neither failure is a statement about the supported scalar object being invalid.

For the quartet route, the degree lower bound and cubic exterior lower bound remain unchanged. No uniform subcubic upper estimate has been established.

## Verification

See CHECKS.md and checks/*.json. No remote mutation and no local Lean execution. Numerical arithmetic seed values are not certified intervals.
