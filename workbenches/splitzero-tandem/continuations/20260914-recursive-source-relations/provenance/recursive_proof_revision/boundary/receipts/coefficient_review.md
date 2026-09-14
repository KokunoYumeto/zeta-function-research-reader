# Independent reading receipt: retained cyclic coefficient specialization

Reviewed 2026-09-13. Source: `work/rh_counterfactual_20260913/total_object/tensor_primary_boundary_control.tex`, SHA-256 `692b5fe8b3434974df0a38ff905d5d1bd456ffba3374c508cfed84df47d61f88`.

Read every line of TCL.1–20 (source lines 2023–2468) and TCL.33–37 with their surrounding proofs (lines 2745–2893). Also read the defining SPF.1 coefficient-datum paragraph in `single_primary_boundary_control.tex`, lines 654–687. The mathematical checks below are independent algebraic checks, not a compilation receipt. No source was edited.

## Result and hypotheses to retain

The reviewed claims are correct with their stated specified coefficient datum. The coefficient ring A must be the unital subring of C containing rho and all coefficients of the actual full Taylor unit and its inverse, with the given unital map alpha to the finite field k0. The construction uses that map; it does not prove that every chosen prime admits such a map. Set S=A localized at ker(alpha). Since the finite image is a field, this kernel is maximal. S is a characteristic-zero domain; p is nonzero and noninvertible, and every integer prime to p is invertible.

The algebraic formulas TCL.2–20 require m,k at least one and p>m. The inherited SPF datum is stronger: p>m+1, with 1/(m+1)! already retained in its ring. The character congruence and its infinitely many solutions in TCL.37 require p coprime to N=m+1; the inherited stronger inequality guarantees this. The parent update should retain that stronger inherited datum whenever the coefficient lattice and character statements appear together.

Two ambient qualifications must remain explicit. First, the torsion direct sum is the cokernel of f_U into the saturated cyclic lattice Lambda_U. The cokernel into the full tensor E_S also contains the free summand F_U. Second, d_r=v_p(r!) is the integer factorial exponent. The proof does not identify S as a discrete valuation ring, assign a valuation to arbitrary coefficients, or identify d_r with a module length over S.

## Exact algebra checks

The monic quotient E_S has the stated monomial basis. Translation between s_i and y_i=s_i-rho and between Z and T=Z-k rho has the displayed mutually inverse Pascal matrices. The identity a_j=g^(m+j)(rho)/(m+j)! follows by taking the coefficient of y^(m+j) in g(rho+y)=y^m(g/h)(rho+y). The recurrence for b_j proves the inverse of the full truncated unit, so multiplication by U is an automorphism that commutes with J and M. Thus f_U is a cyclic-module map with f_U(T^r)=U J^r, preserving its value U at one.

For each retained multi-index, all b_i! are units because b_i<m<p. Multinomial expansion gives J^r=r! V_r, with V_r the full sum of y^b divided by the product of b_i!. Direct multiplication gives J V_r=(r+1)V_(r+1). The chosen degree-r pivot has a unit coefficient and distinct r have distinct total degrees. Therefore the explicit pivot projection splits E_S as Lambda plus F. Multiplication by the full U transports this splitting, without assuming U Lambda=Lambda.

In the transported bases, f_U into Lambda_U is diagonal with entries 0!,1!,...,K!, all nonzero in the domain S. It is injective; its cokernel is the coordinatewise direct sum S/(r!). Inverting nonzero elements of S makes those entries units. The direct complement F_U remains injective under that localization, proving exactly that the intersection of the rational span of L_U with E_S is Lambda_U. This proves the saturation statement in its specified ambient space.

Counting multiples of p^a in 1,...,r gives d_r=sum_a floor(r/p^a). The remaining factor of r! is a unit of S, so (r!)=p^(d_r)S exactly. Cancellation in the domain and noninvertibility of p show strict containment between consecutive principal p-power ideals. The stated quotient coordinate maps apply the actual U inverse and the original pivot functional. They prove both the torsion quotient and the full E_S/L_U quotient, retaining F_U.

For either B=S/pS or the specified finite field k0, the basis splitting survives by its explicit inverse matrices. The coefficient r! is invertible for r<p and zero for r>=p. Thus the exact reduced kernel is the ideal (T^p) in B[T]/(T^(K+1)), with zero interpretation if K<p, and the image has the original basis W_0,...,W_min(K,p-1). This argument does not need B to be a field or a flat S-module.

On the original reduced cyclic source, multiplication by T has index K+1. On E_B, J^p=sum_i y_i^p=0 and J^(K+1)=0. For d=min(p-1,K), J^d=d! V_d has a unit pivot and is nonzero. Applying it to U gives the same lower bound on the image and on Lambda_U. This proves all four nilpotency-index rows, including the m=1 case K=0. The interval bases e_(j,t) have invertible rescaling factors for 1<=t<p; multiplication by J advances with coefficient one until the coefficient (j+1)p or the top-degree relation kills the next vector. The full reduced lattice therefore retains the later chains that the reduced cyclic map does not reach.

The resolution of the torsion cokernel by the two free modules has differential diag(r!). Tensoring that exact chosen resolution computes Tor directly. Its degree-one kernel has basis T^r for p<=r<=K. Inclusion of that kernel gives the displayed positive-sign connecting map and its exact image. No flatness of B is used.

At degree K only the monomial product_i y_i^(m-1) survives. Multiplication by U contributes exactly its constant a_0^k. Thus the terminal coefficient is K! a_0^k/((m-1)!)^k, with exact principal p-depth d_K. It vanishes under the given coefficient specialization exactly when K>=p. For m=1, K=0 at every k, so this vanishing never occurs.

## Original CRT obstruction and surviving character vector

In the stated off-critical quartet and for k>=p, both specified centers occur in the original ordered tensor family. Their difference is p(rho+conjugate(rho)-1)=2p delta, which is nonzero with the stated delta. The retained terminal CRT polynomial has values one and zero at these two distinct centers. The elementary polynomial divided difference belongs to the same coefficient ring, and multiplying it by the center difference gives one. Therefore the explicit element (rho+conjugate(rho)-1) times that divided difference is p inverse in the actual full-stage ring. That ring admits no unital characteristic-p specialization. This establishes an obstruction to extending the local coefficient map, not a vanishing assertion under an undefined global specialization.

Replacing p by any rational prime q<=k proves the same inverse in that degree-k stage. The increasing union of the subrings generated by all stages contains every prime inverse, hence Q. Its residue fields therefore have characteristic zero. This conclusion keeps the stated counterfactual quartet and its actual CRT idempotents; it is not a statement about all coefficient models of the family.

For m>=2 and k=p ell, W_(p-1) lies in the original reduced cyclic image because (p-1)! is a unit. It is nonzero, while J W_(p-1)=p W_p is nonzero over S and becomes zero after reduction. Its retained character label r+k at r=p-1 gives p(ell+1)=1 modulo N exactly. Since p>N in the inherited datum, p is invertible modulo N; that residue class has infinitely many positive ell. These are the stated local coefficient vectors and masks. The calculation does not set p to zero in a characteristic-zero l-adic sheaf representation.

No missing hypothesis or substantive error was found in these source ranges. The ambient-cokernel distinction, inherited stronger prime condition, factorial-depth interpretation, m=1 exception, and the nonextension of the specified coefficient map are essential when propagating the result into earlier calculations.
