# Formalization handoff: sum-fibre connection

Continue the existing original G, e, tau, internal quotient and cochain library. Do not duplicate or modify the other session's core.

1. For P=C[s_1,...,s_k], I=(h(s_i)), construct P/I^2 -> P/I and I/I^2 ~= (P/I)^k by monic division, with no squarefree assumption.
2. Define delta=(1/k)sum partial_i: P/I^2 -> P/I. Prove well-definedness, the relative Leibniz rule, delta(S)=1, and the conormal row (a_i)->(1/k)sum h_i' a_i. The quotient is a ring map; delta is a linear derivation along it. Lift both at their correct types, retaining e and tau.
3. For the full invertible Taylor unit U, retain delta(U P)=U delta(P)+delta(U)pi(P). The actual analytic unit is prod(g/h)(s_i), not one.
4. Extend delta to P/I^(r+1)->P/I^r. On the associated graded, prove (1/k)sum h_i' partial_eta_i, with every exponent factor.
5. Prove the mixed derivative identity modulo I: partial_1...partial_k(U P prod h_i)=U P prod h_i'. Its arithmetic specialization is the full product Jacobian.
6. For a finite-dimensional moving injection j(u):E->H, W=j*j, B=j*j', Gamma=W^-1B, N=(1-jW^-1j*)j', prove derivative decomposition, orthogonality, metric compatibility, N*N=T-B*W^-1B, and the varying-frame formula Gamma_C=C^-1 Gamma C+C^-1 C'.

Analytic inputs not certified by these finite targets: the theta range theorem; Mellin Plancherel; the fixed phase g^dagger=g, h^dagger=(-1)^d h; differentiated product integrability; and the scalar convolution identity I_k+4||normal derivative||^2=mu^(k-1) I/k. The scalar estimate is not assigned to the whole relative matrix or to the source's arithmetic weight control without the remaining comparison.

The concrete source-to-trace identity is J_h(log(x) Theta(phi))=j_h(g')j_h(H_phi). It uses the actual Mellin derivative, then the retained original quotient. It is not an endomorphism of Q. The first conormal thickening is the source carrying that information before it becomes supported zero.

Twenty finite exact tests passed normally and under optimized Python; intentional failure controls failed. These are regression checks, not Lean certificates. No new Lean execution is claimed.
