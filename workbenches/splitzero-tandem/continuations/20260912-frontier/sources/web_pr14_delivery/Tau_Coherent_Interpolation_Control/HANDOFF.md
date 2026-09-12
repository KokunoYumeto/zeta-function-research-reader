# Handoff: coherent interpolation and product boundary control

## Formalization status imported, not enlarged

PR #12 at `5d2772ea0a16d177ac3e01ff70394b90ba95a232` now checks the coefficient homotopy classification, specified quotient retraction/topology, section-change formula, and the indicated tau-chart dual maps. The current turn read its metadata and successful workflow-step summaries; it did not rerun Lean. No file on that branch is changed.

The analytic Mobius/Fourier construction and all analytic input hypotheses remain written proofs. This note does not replace the certified `sectionMap` or introduce a second quotient implementation.

## Other-session results accepted

The completed-square characterization of all finite-source Gram matrices is correct. So is the consequence that unrestricted matrices realize all positive metric rays once the correction rank reaches the packet dimension. The residue-dual metric ray and the exact spectral interpretation of unrestricted optimization are retained. They are the other session's results, not new results in this contribution.

## New bounded algebraic targets

1. **Full-jet constrained minimum.** For a positive Hermitian matrix M and surjective matrix J, define C=J M^{-1}J* and L=M^{-1}J*C^{-1}. Prove JL=I, L*ML=C^{-1}, and z*ML=0 for Jz=0. Then prove the exact Pythagoras formula for every solution of Jx=u. This is ordinary finite-dimensional linear algebra with explicit source maps.
2. **Original quotient interface.** For a monic polynomial h of degree d and invertible v in E=C[t]/(h), prove `ker(P -> v*[P])=h*P_n` on degree at most n+d, and connect its quotient to the existing internal quotient. A polynomial difference hP is an original theta boundary after the specified analytic map T_h; its split lift lands at supported zero.
3. **Packet naturality.** For coprime h,m, H=hm, construct the CRT injection i:E_h->E_H inserting zero residues at m. It is C[t]-linear and nonunital as a map of algebras. Prove s_H i=s_h and, for a common orthogonal boundary space, R_H i=R_h. Retain the Gram compression, not an incorrect inverse-compression interchange.
4. **Same-metric reflection.** Let C bar(C)=I, C* G C=bar(G), and A C=C(w I-bar(A)). Prove C*(A*G+GA-wG)C=-bar(A*G+GA-wG), then transfer an upper quadratic-form inequality to the lower inequality on the SAME G. Full Jordan blocks are allowed.
5. **Nested relation layer.** For L_M subset L_(M+1), let R_M be the orthogonal least-norm section of a fixed quotient, E_M=L_(M+1) cap L_M^perp, Y=P_E R_M, and C=(I-P_LM)(D R_M-R_M A). When the displayed defect is in L_(M+1), prove W=-(Y*C+C*Y) and G_M-G_(M+1)=Y*Y from the actual adjoint identity D*+D=wI. The rank bound is 2 dim(E_M).
6. **Total-degree product quotient.** In k variables use the actual ideal (h(t_1),...,h(t_k)), total degree at most M, and M>=k(d-1). Prove surjective remainder, dimension binomial(M+k,k)-d^k of its kernel, and next-layer dimension binomial(M+k,k-1). Keep variable-order division and all tensor differential signs.

These targets are connected to PR #12 through its quotient/reconstruction maps. They do not assert that formalizing the finite matrix identities proves the analytic density or arithmetic upper estimate.

## New analytic statements in the written note

- The true theta representative is exactly the constrained polynomial interpolant for the positive measure |(2 xi)/h(1/2+it)|^2 dt/(2 pi), with the local unit j_h((2 xi)/h) in its jet matrix.
- The single cyclic family D^j Theta(phi_*) is dense in ordinary L2(dx), proved through a measure with an exponential moment. This implies G_(h,n)->0 and divergence of all nonzero dual interpolation costs. The stronger quotient is NOT replaced by the zero Hilbert quotient; the comparison map and supported zero are retained.
- The canonical representatives commute with all finite-packet inclusions.
- Joint total-degree corrections in the actual product complex yield a new boundary-layer control formula, rather than merely tensoring k copies of an arbitrary metric.

## Exact source hypothesis boundary

The finite packet uses actual zeros with their FULL multiplicities, so v_h=(2 xi)/h is a unit at every selected centre. Partial orders would require a different jet map. The generator remains A=M_t. The coefficient Fourier measure remains dt/(2 pi). The norm of an orthogonal source vector is never assigned value one.

## Quantitative target now made explicit

Bound the generalized Hermitian form W_(k,M) relative to G_(k,M) on the jointly corrected arithmetic tensor family. Both matrices are calculated from exact finite moment matrices and next-relation-layer maps. A sublinear-in-k upper excess would combine with the SAME-metric reflection or the retained residue duality; no such bound is claimed in this note. Matrix rank, absolute norm decay, and unrestricted metric freedom do not replace that estimate.
