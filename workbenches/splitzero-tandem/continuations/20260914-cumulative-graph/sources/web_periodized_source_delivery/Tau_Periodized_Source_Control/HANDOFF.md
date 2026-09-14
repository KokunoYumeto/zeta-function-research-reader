# Focused handoff: source-faithful periodization

This continuation leaves formalization and main-branch integration to the parallel session. It builds on the original full-jet quotient interfaces and PR27's explicit distinction between the full theta source and the critical-only quotient.

## Completed written analytic statements

1. Exact diagonal logarithmic isometry, retaining Jacobian one and the weight k/2. The sum generator becomes -∂r+k/2.
2. Full circle source Gram, including its original zeroth mode; augmented zero coordinate has metric L^(-1), and the Connes source map retains the separate factor 1/2.
3. Source comparison
   `-(Mplus+Mminus)/(exp(aL)-1) <= M(L)-M <= (Mplus+Mminus)/(exp(aL)-1)`.
   Its proof is literal unfolded autocorrelation and weighted Cauchy–Schwarz.
4. Exact cyclic sampled moment formula
   `M_N(L)[a,b]=(2pi/L) sum_n m_h,k(2pi*n/L) conjugate(Pa(k/2+2pi*i*n/L))*Pb(...)`.
   It retains the complete relative Hilbert fibre. For k>=2 the convolution is positive everywhere, so every finite source Gram is positive for every L>0.
5. Exact all-period identity with the factor `(2pi)^delta/zeta(1+delta)` and a quantitative delta->0 bound. The averaging happens before inversion/quotient minimization.
6. Same-relation minimum comparison and the four-volume error `2q log((1+eta)/(1-eta))`.
7. Periodic Laplacian map with *both* terms `(D_L-k)B+B A` retained.
8. At fixed L and k>=2, Hilbert completion of the cyclic source has quotient precisely the values at sampled roots. Its kernel in C[S]/chi is `(p_L)/(chi)`, with p_L the squarefree product over sampled roots. The canonical periodic Grams decrease to the explicitly displayed sampled-value Gram. This is a further completion, not the original strong-Schwartz quotient or PR27's Schwartz critical quotient.
9. Finite frequency cutoff: omitted positive Gram is at most
   `(L/(2pi J))^(2p-1)/(2p-1) * H_p`, where H_p is the original weighted derivative Gram.

## Small bounded algebraic formalization targets

Use the already implemented weighted quotient construction. Do not replace J, chi, the source metric, or the source image by abstract unidentified matrices.

- Same constraint minimum: `(1-eta)M <= ML <= (1+eta)M` implies the same inequalities for `(J M^-1 J*)^-1` and `(J ML^-1 J*)^-1`. The analytic source supplies positive definiteness and full rank.
- Difference of the two constructed representative matrices lies in ker J; the existing monic relation-column map and quotient-kernel equality recover its actual source coefficients.
- Four determinant errors with two plus and two minus signs have total allowance `2q log((1+eta)/(1-eta))`.
- Exact operator identity:
  `(D^2-kD)R-R(A^2-kA)=(D-k)(DR-RA)+(DR-RA)A`.
- Augmented coefficient metric recovers full Fourier Gram, including `Z0*Z0/L`.
- Finite sampled quotient kernel: evaluation at the selected distinct roots has ideal kernel `(p_L)/(chi)`; repeated jets remain in that kernel.

The function-space estimates are written proofs, not Lean assumptions being represented as proved definitions. Parameter L is circle length; eta is a source-relative tolerance; p is derivative order; k is tensor degree; q is the unchanged cyclic dimension. These indices must not be merged.

## Current quantitative position

One common circle length chosen from the degree-(2q+2) source suffices for all endpoint matrices and two generator raises. A common finite Fourier cutoff then supplies a fully finite Gram comparison. With a fixed total tolerance eta<1, the resulting endpoint log-volume error is O(q), hence is negligible compared with q log k.

This does not bound the discrete arithmetic endpoint volumes from above. It gives a new exact/certifiable representation of them. Completing at a fixed circle first collapses a precisely computed kernel; it cannot be substituted for that growing finite-source problem. The existing four-volume lower threshold remains four.
