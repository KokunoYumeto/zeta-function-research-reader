# Handoff: fixed-width source–relation transfer

Base inspected: main fa4be32f87a9a90f3c02a07f7790dea95a1e7b0f. Read PR #22 at 811210d24b80813a08972ca23f919db015383137, retaining its in-progress certificate status. Do not duplicate the original scalar, quotient, homology, conormal or Gram-trace library.

Finite targets:

1. Raw derivative Hermite coordinates: multiplication block (Xv)_j=zeta v_j+j v_(j-1), full factorial Vandermonde, exact kernel (Pi).
2. F_n invertibility from original orthogonality and positivity of Pi=psi^2. No uniform inverse estimate follows just from existence.
3. Construct Qhat_n by solving F_n d_n=v_(n+2q), then exact division by Pi. Prove orthogonality for Pi dmu and nu_n=-d_(n,0)omega_n>0.
4. K_n=(e_1,...,e_(2q-1),d_n), F_(n+1)=F_n K_n, determinant=-d_(n,0), and the full multiplication conjugacy.
5. B_n/D_n=detF_n/detV; detG_N=(product omega_(n..n+q-1))detV/detF_n. Keep all coordinate phases and raw factorials.
6. F_n'=F_n L_n-a_n v_(n-1)e_0^T. Deduce the phase via (log V_N)'=sum b_j+a_n e_0^T F_n^(-1)v_(n-1). Do not impose evenness on a tilted measure.
7. Z_j=psi Qhat_j-Q_(j+q), nu_j-omega_(j+q)=||Z_j||^2. Its quotient is -[Q_(j+q)], while psi Qhat_j is the original relation with the unit i^(-q) retained.
8. Reuse the rank-two radius to obtain equation (11) of RESEARCH_NOTE.md. Do not implement a second cohomology core.
9. The norm helper C[S]/chi_1^2 maps onto C[S]/chi_2. Keep its explicit kernel and derivative square. Do not substitute chi_1^r for the actual pullback of I^r.
10. Verified residual bound for finite solves; actual arithmetic enclosures remain an analytic input.

The same original base b_tau and infinite quotient G(Z)->Z remain. All supported maps retain their labels, e and tau. The true Taylor multiplier U and its derivative term are unchanged. The analytic target is epsilon=o(k q_k) for a fixed hypothetical off-line quartet with full multiplicities. No uniform estimate or new Lean execution is claimed here.
