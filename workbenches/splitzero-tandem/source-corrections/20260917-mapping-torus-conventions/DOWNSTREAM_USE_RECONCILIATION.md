# Exact downstream use reconciliation

Scope: the historical source statement `LITSTMT-20260830-0155` and its direct use in the nonconstant unit-fibre chapter, together with the actual finite-edge boundary, archimedean boundary and finite-set pullback formulas it feeds. This check reads the indicated current source bytes, not every archived copy or every Green-module construction.

## Inspected source identities

Relative to the mathematical repository's `tex/satellites/` directory:

| File | SHA256 | Reading scope |
|---|---|---|
| `19e_nonconstant_unit_fibre_k_theory.tex` | `ea8f5acb1c12b4cd66467f4a03c774c4d0147d7abdb3f68b21c6c2dd12bdea91` | Complete file, including finite-level transitions and both full boundary calculations |
| `19c_unstabilized_semilocal_one_zero_algebra.tex` | `0298d284fbca1abef7b0e2ce8fe7ccc9fd2d7257856b8f15f3d7480eff8ff05a` | Finite-edge orbit coordinates, convergence, quotient map, Green comparison and unit boundary; lines95–281 |
| `19f_finite_set_coherence.tex` | `e866c4b3e2c321ace1be3d69cd3ac8305b52689a4f00cb0b35e95f893e23acd1` | Old finite summands, orbit projections and full connecting square; lines409–580 |
| `19_primitive_defect_source_audit.tex` | `9d03fcc6795ef65d4d3b92f4d0ec7aa60c716514153f1f9f48abe4fe51f9a094` | Local finite-prime boundary theorem/proof; lines589–626 |

The original files are preserved. The changed source sentence occurs in 19e, lines101–105: it assigns `1-sigma_*` to the mapping-torus boundary without an explicit orientation qualification.

## The coefficient action and the torus coordinate agree

The chapter fixes Y=product over q in P excluding p of Z_q^units, g=(p)_(q not p), sigma(f)(y)=f(g^(-1)y), ell=log(p)>0, and the quotient relation(y,s)~(g y,s+ell). It defines Theta(G)(u)(y)=G([y,u ell]). Substitution at u=1 gives [y,ell]=[g^(-1)y,0], hence Theta(G)(1)=sigma(Theta(G)(0)). Thus its displayed torus is precisely the forward M_sigma with increasing u. No unnoticed inversion of sigma occurs in this identification.

Let j:C_0((0,1),C(Y))->M_sigma be the direct inclusion and ev0 the quotient. Write beta for the positive-circle Bott map pinned in the two source calculations. The exact sequence segment is

    0 -> K0(M_sigma) --ev0_*--> C(Y,Z)
      --(sigma_*-id)--> C(Y,Z) --j_* beta--> K1(M_sigma) -> 0,

because K1(C(Y))=0. The chapter supplies the profinite projection-rank and unitary-homotopy proofs of these coefficient groups. Define the two coordinates explicitly by ev0_*(x) on K0 and by the quotient map [f] |-> j_* beta([f]) on the coinvariants. Exactness makes them isomorphisms onto the invariant group and from the coinvariant group respectively.

Since im(sigma-id)=im(id-sigma) and their kernels agree literally, the identity on C(Y,Z) gives the same displayed kernel/cokernel groups. It also retains the actual generators u_O=1_O and v_O=[delta_x]. No sign is inserted in the K1 quotient coordinate. Pullback between the finite quotients commutes with sigma, j and beta, so both finite-level transition formulas remain unchanged, including the multiplicity L_m'/L_m. The same reasoning applies to the old-prime pullback [f] |-> [f composed with pi] in 19f: the map preserves the increasing suspension coordinate.

## The finite-edge minus sign is independently fixed

The extension of the one-zero orbit space by C_0(K_P times R) is a different, explicitly related extension. Its quotient K0 coordinate is the invariant rank function just fixed by ev0, so the torus boundary correction does not negate that input.

For a clopen subset E of Y/H,19e lifts its characteristic projection by

    x_E(a,t)=1_(q^(-1)E)(pr_p(a))/(1+exp(t)).

Its boundary value is1_(q^(-1)E). The orbit convergence condition uses t->-infinity, so the lift is continuous there and vanishes at the escaping +infinity end. On each selected unit fibre the positive exponential has argument2pi/(1+exp(t)), decreasing from2pi to0. The original generator v(t)=(t-i)/(t+i) has increasing argument: its logarithmic derivative is2i/(1+t^2), whose total argument increment is2pi. Therefore the lift's class is minus the retained positive generator, pointwise. The exact finite-edge map remains

    partial_p(h)=-h composed with q composed with pr_p.

This agrees with19c's pullback from the original local boundary calculation. It uses the positive exponential formula directly, not the mislabeled sign in the torus kernel/cokernel paragraph.

## Archimedean and assembled maps

For a clopen E in the retained half H_P^+, the archimedean lift is1_E(h)/(1+|w|), with generic coordinate a=sign(w)h and t=log|w|. Along either sign component, increasing t decreases the argument from2pi to0. The map is therefore -r_P^*h, as printed. This computation invokes no mapping-torus boundary sign.

Consequently the assembled map stays

    partial_P((h_p),h_infinity)=-sum_p iota_p(h_p)-r_P^*h_infinity.

Its kernel description and cokernel quotient in 19e retain exactly the same coordinates. The finite-set square in 19f also retains its minus signs: both sides evaluate a finite-place function after dropping p and forgetting the new-prime units, and evaluate the archimedean function on the old sign orbit. These pointwise equalities explicitly identify the morphisms; no appeal to mere nonidentity of the two extensions is used.

## Concrete correction scope

Replace the source paragraph's unqualified torus sign by the explicit forward-convention boundary sigma_*-id, and immediately state the fixed ev0 and j_* beta coordinates. Keep the existing invariant/coinvariant displays, all finite-level multiplicities, both edge minus signs and the full connecting square. Preserve the original source statement as historical evidence and append a correction record with the exact proof and source hashes. This is a bounded reconciliation of the named uses, not a global re-audit of every historical manuscript or the 726-page continuation.
