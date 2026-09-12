# Formalization handoff

Reuse the original G, Hom.total, internal quotients and checked homotopy library. Do not change scalar definitions or dependency pins.

1. Prove the filtered invariant-quotient equivalence `(C[x,y]/(h(x),h(y)))^swap ~= C[S,Delta]/(H0,Delta H1)`, with S=x+y, Delta=(x-y)^2 and h((S+r)/2)=H0+rH1. Retain 1/2 factors and all nilpotents. The exact theta primitive is displayed in the note.
2. For finite E,A construct the free C[S] resolution SI-A with augmentation P tensor v ->P(A)v. Prove both exactness and the dual coker SI-A^vee. Transpose and antidual conjugation have separately specified maps.
3. Formalize the finite nilpotent raising/lowering operators and primitive decompositions. All arithmetic Grams remain U*G U, including cross-ladder terms; the explicit auxiliary diagonal Gram is not an arithmetic metric replacement.
4. Prove finite interpolation-coordinate identities M'=C*MC, J'=U^(-1)JC, K'=U^(-1)K(U^(-1))*, G'=U*GU. The full jet unit stays in J.
5. Lift all fixed-support maps through the original reconstruction and retain the receiving support index at which an original relation becomes e-zero. No active class is sent to tau merely because its amplitude vanishes.

The matrix-weight Fubini identity, theta range inputs, exponential bounds, and global control remain analytic tasks. The present note gives written proofs of the finite-degree norm identity, not a Lean certificate. Its nilpotent decomposition alone supplies no bound on real parts of arithmetic exponents.

The uploaded Kernel Layer Integration supplement agrees with the retained frontier construction and supplies a sharper rank bound; its results are treated as source results, not rediscovered here. This branch does not change that session's workbench or claim its formal verification as covering the new analytic statements.
