# Bounded formalization handoff

This continues the supplied Kernel Layer Integration and Symmetric Frontier notes. Do not redefine G, e, tau, original Hom.total, internal quotients, or the checked homotopy library. The two source notes agree via K=C_inverse, U=F, D=Omega, E_layer=b_M, F_derivative=Omega^(-1)E_plus*.

## Priority targets with actual types

1. **Symmetric polynomial quotient, characteristic zero.** Let h in C[t] be monic. Define H0,H1 by the half-sum/odd quotient of h((S+r)/2). Construct the algebra equivalence (C[x,y]/(h(x),h(y)))^swap ~= C[S,Delta]/(H0,Delta H1). Map S->x+y, Delta->(x-y)^2. The proof uses actual even/odd decomposition, not radical ideals or a squarefree assumption. Carry weighted degree deg(S)=1, deg(Delta)=2.

2. **Primitive lifting.** A relation H0 A0+Delta H1 A1 maps to h(x)(A0+rA1)/2+h(y)(A0-rA1)/2. Lift it to the original tensor differential with a minus sign in its second primitive. Given fixed-order division, average coefficients before converting: this preserves the degree bounds. Use the existing relation quotient universal property to lift Phi, including e and tau.

3. **Free sum-action resolution.** For finite-dimensional E and A:E->E, construct 0->C[S] tensor E --SI-A--> C[S] tensor E -> E_A ->0. The augmentation is P tensor v ->P(A)v. Prove exactness by the displayed telescoping identity. The dual has SI-A^vee (transpose, not Hermitian adjoint) and computes Ext^1. The specified conjugation map connects linear dual to antidual.

4. **Finite resolvent residue.** Rational matrix (SI-A)^(-1), full nilpotent power expansion, and trace chi'/chi. This is a bounded finite algebra target; it does not establish the infinite Lefschetz trace.

5. **All-k nilpotent decomposition.** On product truncated polynomial modules, construct N=sum z_i, F(z^a)=sum a_i(m_i-a_i)z^(a-e_i), H=2degree-D. Prove the three sl2 commutators and the explicit diagonal Gram for which F=N*. Primitive ladder maps give the Jordan lengths. Symmetric subspaces retain all orbit factors and central occupation idempotents. The auxiliary Gram is only for decomposition; arithmetic Grams must be transported by U* G U with all cross terms.

6. **Finite interpolation compatibility.** For the actual polynomial source-coordinate map C and quotient-coordinate map U, prove M'=C* M C, J'=U^(-1)J C, K'=U^(-1)K(U^(-1))*, G'=U* G U. The unique minimum is the same representative. Do not assume the jet map is an algebra map: it includes multiplication by the retained unit upsilon.

## Analytic inputs outside these certificates
The actual theta range theorem, continuous global retraction, Mellin Plancherel realization, exponential moments of |g/h|^2, Fubini/disintegration, pointwise positivity of the fibre matrix, and any uniform arithmetic weight estimate need their analytic proofs. The note supplies the matrix-weight proof but the finite checker does not certify it.

## Evidence
The new script has 24 tests, including nonconstant units, repeated roots, exact Gaussian masses, preserved relative directions, nilpotent ladders, sum collisions, dual shifts/residue pairing, and external versus supported zero. It does not claim new Lean execution.
