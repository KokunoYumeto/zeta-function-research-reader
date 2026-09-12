# Independent complete QD review

Reviewed the full new quartet_dissipation_continuation.tex against the
original FE and AP formulas, including QD.1–15 and all three theorem proofs.
The reviewed source has SHA256
7f6e76ef6d6a7126eb52c4e02d0448f7d7d69b50c163f250f2a99ff096f1fea0.

No mathematical correction is outstanding. In particular the order of
H^-1, H, Omega^-1 in the original cross-pairing is correct; no commutation
of distinct positive matrices was used. The graph target is the actual
next relation layer and is onto by its leading coefficient and old-space
orthogonality. Domain reflection gives opposite blocks, hence the norm of
the sum with its adjoint equals the norm of one block, including zero ranks.
The full derivative cost is V(I+U*U)V*, not merely VV*. Its maximum
eigenvalue is bounded by its trace with all multiplicities retained.

The eigenvector constructed from the top local nilpotent exists even at
repeated zeros, and its k-fold tensor gives exactly 2k Re(rho)-k. The
resulting lower scalar is 4k^2 delta_*^2. The volume inequality direction
pi <= 1/(1+lambda), the strict positive cost denominators for delta_*>0,
and the two accumulated logarithm inequalities all check. The delta_*=0,
F=0 and E_+=0 cases are explicitly retained without division by zero.

For k=1, the actual layer has dimension one. The cross-map is the outer
product of its two original row maps. Its exact norm product and rank-one
inverse-metric determinant prove epsilon^2=(1-pi)chi and zeta=chi, including
the zero row cases. The divided logarithm is used only at chi>0. These are
finite actual-arithmetic identities; no limiting estimate is inferred.

Integration: place after AP and before the new Stieltjes/gamma continuations.
Add cross-references to the earlier general FE estimate, preserving its
original broader-scope factor4. Frozen releaseE remains unchanged.
