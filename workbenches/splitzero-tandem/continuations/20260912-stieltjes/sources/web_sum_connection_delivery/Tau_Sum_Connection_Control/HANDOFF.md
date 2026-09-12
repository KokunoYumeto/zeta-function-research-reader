# Handoff: sum-fibre derivative and first conormal layer

This continues PR #17 and the supplied Kernel Layer Integration. It does not modify the other session's scalar, reconstruction, homotopy, or retraction sources.

## Existing inputs retained

- G(R), tau, e, the arithmetic projection p, and the original support-indexed internal quotient.
- The actual theta complex [V -> B], full packet h, g=2 xi, v_h=g/h, T_h, full jet unit, and finite canonical representatives.
- K=G^-1, V=AK+KA*-kK, and the source's original next-relation map. These are not reproved as new work here.

## New bounded algebraic targets

1. For P=C[s_1,...,s_k], I=(h(s_i)), construct pi:P/I^2 -> P/I and I/I^2 ~= (P/I)^k. Use monic division and retain all multiplicities. No squarefree assumption.
2. Define delta=(1/k)sum partial_i on P/I^2 with values in P/I. Prove well-definedness, the relative Leibniz rule, delta(S)=1, and its conormal row (a_i) -> (1/k)sum h'(s_i)a_i. This is a linear/derivation map, not a ring homomorphism. Its split-linear lift and the split ring quotient have distinct types.
3. For U with invertible image mod I, prove delta(U P)=U delta(P)+delta(U)pi(P). For the analytic finite Taylor unit U=prod(g/h)(s_i), this is the displayed complete jet equation. Do not set that unit to one.
4. For all r, delta:P/I^(r+1)->P/I^r and gr_I(delta)=(1/k)sum h_i' partial_eta_i. Retain factors alpha_i, the original k, and actual quotient maps.
5. Prove the product derivative identity modulo I: partial_1...partial_k(U P prod h_i)=U P prod h_i'. This is the product Jacobian of the same relation system.
6. Finite-dimensional projection connection: for j(u):E->H, W=j*j invertible, B=j*j', Gamma=W^-1B, N=(1-jW^-1j*)j', prove derivative decomposition, N*j=0, metric compatibility, and N*N=T-B*W^-1B. Under j -> j C(u), retain Gamma_C=C^-1 Gamma C+C^-1 C'.
7. The fixed-phase arithmetic specialization gives B=W'/2. This phase is an analytic input from g^dagger=g and h^dagger=(-1)^d h; do not assume it for a general complex frame.

## New analytic theorems, outside the finite certificate

Let a_h(t)=(g/h)(1/2+it)/sqrt(2pi), w=|a_h|^2, mu=int w. For a reflection-stable packet, I_h=int w'^2/w=4||log(x)F_h||^2 and int conjugate(a_h)a_h'=0. The actual k-fold sum amplitude Psi yields

    I_(h,k) + 4 int ||normal derivative of Psi||^2
      = mu^(k-1) I_h / k.

The exact mass is not assigned one. The full polynomial relative fibre has the constructed connection and positive normal matrix. The scalar contraction is not certified as a bound on the entire arithmetic control V_M relative to K_M.

## Direct source-to-trace equation

    J_h(log(x) Theta(phi)) = j_h(g') j_h(H_phi).

For phi=P(D)phi_*, pairing that value with the existing residue form is the arithmetic multiplication trace, with g=2xi and every zero multiplicity retained. This is the concrete analytic specialization of the conormal row, not a new H^1 endomorphism.

## Verification

Twenty exact SymPy test methods pass in normal and optimized Python. Both intentional-failure controls fail. Source manifest checks cover 31+53 entries. The attachment's 18-method suite was rerun in both modes. New numerical theta-seed quadrature is labeled non-rigorous numerics and is not a Lean or interval certificate. No existing formal source has been changed.
