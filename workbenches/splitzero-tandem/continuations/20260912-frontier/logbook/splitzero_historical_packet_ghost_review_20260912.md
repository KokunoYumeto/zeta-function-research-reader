# Independent historical-packet review — 12 September 2026

Reviewed the complete mathematical text of `output/split_zero_rh_tandem_2026-09-12/tex/historical_packet_ghost.tex`, SHA256 `4D78A6CA7FDC2FC49BBAEA854899D6F84CB6F3460D1BFDD0C5A927BD70446E88`. Historical source provenance is being supplied by its separate lane; this review concerns the mathematical statements and all operator/kernel types. A second independent reviewer checked the group-algebra quotient and arithmetic saturation, including real pairs, repeated jets, and empty critical locus. No root TeX was edited and no Lean process was run.

The CRT, typed involutions, ghost spectrum, group-algebra kernel, arithmetic saturation, and reference weight formulas check correctly. No counterexample to a stated theorem was found. Two precision additions were sent to the integration author: make the source-metric transport explicit, and write the eta continuation as an undivided product identity before dividing on the real interval.

## Complete jets and typed involutions

The map T sends each polynomial to its full Taylor expansion at each selected root, including the factors 1/k!. The kernel in C[s] is the product of all pairwise coprime primary ideals, namely (h). The stated local inverse uses the truncated inverse of h_rho and is correct: a_rho h_rho is 1 modulo (s−rho)^m_rho and 0 modulo every other primary factor. Its multiplication by (s−rho)^k gives precisely the indicated basis vector. Thus T is an algebra isomorphism, not merely a vector-space coordinate count.

Multiplication by s transports to rho+N_rho on each full local algebra. The last column vanishes only at its actual nilpotence order. All multiplicities and the original generator are retained.

The maps C0,S0,H,K are well-defined because orders are constant on each conjugation/reflection orbit. C0,S0 permute whole local algebras without changing their degree; H substitutes −t_rho; K conjugates coefficients. They are commuting product-preserving involutions, with precisely K conjugate-linear.

For coefficient conjugation f#(s)=overline{f(overline{s})}, the kth Taylor coefficient at rho is the conjugate of the kth coefficient of f at conjugate(rho). Hence its transported map is C=C0K. For substitution f(1−s), the kth coefficient acquires (−1)^k and is evaluated at 1−rho, giving S=S0H. Conjugation fixes the indeterminate s and commutes with its multiplication operator as a conjugate-linear map. Substitution gives S A S=I−A. The relations C0N=NC0, S0N=NS0, and HN=−NH hold also on the final jet basis vector. The displayed C0=C K and S0=S H therefore give the exact relation between the historical complex-linear permutations and the actual arithmetic involutions.

## Historical ghost and group-algebra kernel

In the declared coefficient metric, C0 and S0 are commuting selfadjoint permutations. Consequently Gamma=C0−S0 is selfadjoint and Gamma²=2I−2C0S0=4P_−. On a single basis vector Gamma vanishes exactly when conjugate(rho)=1−rho. This assertion concerns that labelled basis vector; the theorem separately retains the additional zero eigenspaces on off-axis quartets.

On a nonreal off-axis quartet, the four displayed joint eigenvectors are orthogonal, have squared norm 4, and have eigenvalues epsilon−delta. Thus the full multiplicity-m block has Gamma eigenvalues +2 and −2 each m times and zero 2m times; rank P_−=2m and Tr(Gamma*Gamma)=8m. On a real off-axis pair C0=I and S0 interchanges the roots, yielding rank m and trace 4m. On a critical orbit C0=S0 at every jet degree. All cases agree with the statements.

For C[W] with basis (1,c,sigma,c sigma), the map to C[u]/(u²−1) has kernel a+e=0 and b+d=0. Its basis is exactly c−sigma and 1−c sigma, and multiplication by c exchanges these generators. Since Gamma²=4P_− and Gamma=Gamma P_−, the represented ideal image is P_−L_Z. The universal quotient is valid in the W-module category, before requiring A-invariance.

## Arithmetic saturation and its universal kernel

Write M=P_−L_Z and D=(1/2)I+iY+N. The exact generator is A=D+B. Reflection R preserves imaginary parts and jet indices, so D preserves both parity spaces while B interchanges them. On an off-axis orbit B is invertible and restricts to an isomorphism from P_− to P_+. For an arbitrary vector w=w_−+w_+ on that orbit, the explicit decomposition is

w=(w_−−D B⁻¹w_+)+A(B⁻¹w_+).

Its first summand lies in M and the argument of A lies in M. Moreover if Av lies in M for v in M, projecting to P_+ gives Bv=0, hence v=0. This proves M⊕AM=L_off on every off-axis orbit, with the nilpotent operator N fully present inside D.

On critical orbits M=0. Since A and every W permutation preserve L_off, the two-step sum is already invariant and therefore equals the smallest A-invariant subspace containing the ghost image. Every linear target map F satisfying F C0=F S0 and F A=A_target F kills M and AM and hence kills L_off. It factors uniquely through the critical-factor projection. That projection is also an algebra homomorphism and W-module map and intertwines the full arithmetic generator, so the same factorization is valid in each stated structured target category.

The polynomial map [f]_h↦[f]_(h_crit) is well-defined because h_crit divides h. Its kernel consists exactly of multiples of h_crit modulo h, matching the off-axis direct summand under T. If every root is critical, this map is the identity and the kernel is zero. If the critical locus is empty, h_crit=1 and the target is the zero algebra, exactly as explicitly stated in the fragment. Real orbits and repeated jets introduce no exception.

For comparison, the smaller W-module quotient genuinely need not carry A. On the real pair Z={0,1} with order one, M is spanned by e_0−e_1, but A(e_0−e_1)=−e_1 is outside M. The fragment's saturation gives M⊕AM=C² and therefore the zero arithmetic quotient, precisely resolving this obstruction. This example supports the necessity and the exactness of the stronger kernel; it does not replace the general proof.

## Reference metric and its exact source-metric comparison

In the declared local coefficient metric, A*=A_ss*+N*, so W_ref=A*+A−I=2B+N+N*. The selfadjoint permutation R anticommutes with B and commutes with N and N*. Its odd weight component is therefore 2B and its even component is N+N*. The original tesserine value c_(−+)=4(Re rho−1/2) is exactly 4B, giving the asserted factor c_(−+)/2. No repeated-root contribution is absent from the full reference weight.

The last reference-metric paragraph correctly warns that its numerical form is not automatically the source metric. To complete its typed crosswalk explicitly, let G_E be the actual theta-source Gram matrix in polynomial coordinates and put A_L=T A_E T⁻¹. Its transported Gram and weight are

G_L=(T⁻¹)*G_E T⁻¹,

W_(G_L)=(T⁻¹)*(A_E*G_E+G_E A_E−G_E)T⁻¹.

On L_Z the direct reference/source relation is

W_(G_L)=G_L W_ref+[A_L*,G_L].

This equality follows by expanding G_L(A_L*+A_L−I)+(A_L*G_L−G_L A_L*). It retains every actual metric entry and supplies the exact missing typed transport, rather than treating the chosen reference metric as the arithmetic one. These formulas were sent to the integration author as a precision addition.

Conjugation X↦TXT⁻¹ is an isomorphism between the associative endomorphism rings. Extending it to their split-zero semirings sends tau to tau and each supported X to its supported conjugate; it therefore preserves both supported zero and the external zero separately. The endomorphism rings need not be commutative, and the fragment correctly invokes their associative ring structures rather than a commutative-ring hypothesis.

## Eta continuation precision

The nonvanishing conclusion for real 0<s<1 is correct: the convergent paired alternating series has positive terms and positive sum, while 1−2^(1−s)<0. For the surrounding complex continuation sentence, the clean exact identity is

eta(s)=(1−2^(1−s))zeta(s).

It extends by analyticity from Re s>1 to Re s>0 with the removable value at s=1. The quotient has other removable denominator zeros at 1+2 pi i k/log 2 for nonzero integers k, so the prose should not implicitly treat division as ordinary pointwise division everywhere away from s=1. Dividing only on the stated real interval avoids all such points. This does not affect the theorem about real arithmetic zeros.

No theorem-level defect or universal-kernel counterexample was found. The two precision additions above complete the coordinate and continuation comparisons with exact maps and equations.

## Final addition verification

Re-read the corrected source, SHA256 `EB0475E1820A69626982BF114300D2A770EB30F4D8EE6F208F998E876CF40BD9`. Both precision additions are implemented correctly. The eta argument now proves uniform paired-series convergence on compact subsets of Re s>0, continues the product identity, and divides only on the real interval. The actual metric and weight now transport explicitly through T, with the exact commutator relation retained.

The additional descent algebra D={X in End_C(L_Z):X(L_off)⊆L_off} is a unital subalgebra. Its quotient action d:D→End_C(L_crit) is a surjective unital ring map: every critical endomorphism lifts by zero on the off-axis direct summand. Its kernel is exactly the embedded Hom_C(L_Z,L_off), since zero quotient action means every value of X lies in L_off. This range condition also guarantees such X already belongs to D. The displayed ring map therefore lifts to G(d), with A sent to the supported critical generator, Gamma sent to supported zero, and tau sent to tau. The zero critical target is consistent with the stated zero-algebra convention. No remaining defect was found in these additions.
