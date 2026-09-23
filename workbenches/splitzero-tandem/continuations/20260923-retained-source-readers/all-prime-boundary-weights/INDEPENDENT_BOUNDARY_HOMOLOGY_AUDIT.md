# Independent check of BW13–24

Read ROOT_BOUNDARY_WEIGHT_HOMOLOGY.tex in full; the bounded mathematical
review concerns BW13–24. The finite Koszul contraction, balanced
transition maps, all-prime homology colimit, original idele action,
stated multiplicities, and labelled fibers are correct.

The proof of the Schwartz-boundary connecting map needs an explicit
sign-subgroup map. The element −1 acts trivially on the boundary
module V_r, but it generally acts nontrivially on the original
Schwartz test module T_r and its kernel J_r.

Let A=U_{−1}^{tensor r}, so A²=I, and let P_+=(I+A)/2.
For either original module M, write M^+=P_+M. The decomposition
M=M^+ direct-sum M^- is exact, and passing to the sign subgroup's
coinvariants is canonically the map P_+. Its kernel is M^-:
for v in M^-, v=(A−I)(−v/2). The averaging projector commutes
with every rational and idele dilation.

The full group is the direct product of the order-two sign group
and the free abelian positive-rational group. Over C, the trivial
module of the sign group is projective, by its averaging idempotent.
Its degree-zero projective resolution, tensored with the original
positive-prime Koszul resolution, therefore computes the full
group homology using the coefficient modules M^+.

Applying P_+ to BW19 gives the exact original sequence

    0 -> J_r^+ -> T_r^+ -> V_r -> 0.

In particular, an actual lift t of any boundary coefficient can
and should be replaced in the full-group connecting calculation
by t^+=(t+At)/2. Its boundary coefficient is unchanged because
the boundary action of −1 is trivial. The Koszul differential of
this averaged lift lies in J_r^+ and gives the stated full-group
connecting class. Changing the lift changes that class by a
kernel differential, exactly as required.

BW22 remains valid with any unaveraged test lift. If
u=(U_p^{tensor r}−I)t belongs to J_r, its averaged version is P_+u.
The difference u−P_+u is in the negative sign eigenspace and equals
(A−I)(−(u−P_+u)/2), so it has zero class in (J_r)_{Q×}.
Thus the original coefficient formula is preserved; the missing
averaging map completes its full-group justification.

For the infinite-resolution paragraph, an additional explicit
algebraic sentence makes the augmentation proof complete: the
all-prime Laurent ring R is free over each R_F on the Laurent
monomials in the other variables. Hence base change preserves the
finite Koszul exact sequence and resolves R/(t_p−1:p in F).
The filtered colimit of these quotient modules is C. The union
of the free Koszul modules is R tensor Lambda E, with the actual
ordered prime basis, giving the asserted free resolution.

The labelled maps BW23–24 preserve the entire support lattice.
They are lifts of linear maps, not a claim that amplitude
exactness deletes a support label. A full-group sign averaging
map itself also has this same-label lift; its amplitude factor
1/2 does not change the support coordinate.

The only additional source typo reported was the missing backslash
before quad in BW11. No new Frobenius, interior-cohomology, or
Riemann-hypothesis conclusion follows from this bounded check.
