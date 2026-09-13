# Independent review of CC.25–52

The complete text from “The finite cyclic derivative and its exact Weyl correction” through the end of `work/cyclic_conormal_depth_continuation_20260912.tex` was read, including CC.25–52. Its definitions and dependencies CC.1–3 and CC.16–24 were also read. The comparison to the existing spectral-sum section was checked against `tex/spectral_sum_stieltjes_pair.tex`, SSP.1–10. The delivered cyclic NOTE's explicit packet-reflection hypothesis was checked in its lines 120–122. This review is mathematical; no Lean source or reported remote checker is certified here, and no TeX or release file was edited.

The finite Weyl relation, both first-jet maps, their invariant ranks, the full product Jacobian, all four trace-comparison blocks and the new two-factor invariant ideal are correct. The author was asked to make the packet-reflection hypothesis explicit: the initial CC.1 allowed arbitrary roots, whereas an involution of the same packet quotient requires closure under the specified reflection. The final candidate now states that hypothesis immediately after CC.1. Section 6 below also proves the exact map to the reflected packet before that closure is imposed. The final delta, including the complete all-depth parity extension CC.51a–51b, was read and passes. The accepted TeX SHA256 is `1182806be9a6e1ecde9b594a195a8cd3fa17b7259540fcd5617d044d06b05e79`. No mathematical defect remains in this review's scope.

## 1. Finite derivative, exact section and Weyl sign

Retain the chapter's monic scalar annihilator \(\chi_r(T)\), degree \(q_r\geq1\), and quotients \(C_r=\mathbb C[T]/(\chi_r)\). Its section \(s_r:C_r\to C_{r+1}\) uses the same unique monic remainder \(F_0\) of degree less than \(q_r\). It is a complex-linear map, and \(\rho_rs_r=I\). Thus \(d_r=\partial_rs_r\) is exactly the endomorphism \([F_0]\mapsto[F_0']\). The coefficient functional \(L_r(F)=[T^{q_r-1}]F_0\) and the corrected multiplication remainder are precisely

\[
(TF_0)_{\rm rem}=TF_0-\chi_r L_r(F).
\]

Applying \(d_r\) before and after multiplication gives

\[
d_rM_TF=[F_0+TF_0'-\chi_r'L_r(F)],\qquad
M_Td_rF=[TF_0'].
\]

Therefore \([M_T,d_r]=-I+[\chi_r']L_r\), with the displayed minus sign. Multiplication by the original \(b_r\in C_r\) commutes with \(M_T\), and the scalar \(k/2\) commutes with every endomorphism. This proves exactly

\[
[A_r^C-k/2,D_r^{\rm red}]=-I+\mathsf J_r,\qquad
\mathsf J_r=[\chi_r']L_r.
\]

The original derivative polynomial has degree \(q_r-1\), leading coefficient \(q_r\), so its class is nonzero and \(L_r([\chi_r'])=q_r\). The functional is nonzero because \(L_r([T^{q_r-1}])=1\). Hence \(\mathsf J_r\) has rank one, \(\mathsf J_r^2=q_r\mathsf J_r\), and trace \(q_r\). The trace cancels \(-\operatorname{Tr}I=-q_r\), as required by the finite commutator identity.

The retained arithmetic decomposition is well typed through the inclusion \(K_r\subseteq A_r\): CC.23 composed with \(s_r\) gives

\[
\delta_r\eta_{r+1}s_r
=\eta_r(d_r+M_{b_r})+\mathcal N_r.
\]

Here \(\mathcal N_r:C_r\to K_r\) is \(\mathbb C[T]\)-linear, so
\(M_S\mathcal N_r=\mathcal N_r M_T\). It contributes zero to the corresponding commutator into the full arithmetic algebra, while its value remains present in the derivative itself. Thus the full commutator is \(-\eta_r+\eta_r\mathsf J_r\), as claimed. No unwritten commutation of a derivative with the arbitrary algebraic retraction is used.

Finally, \([\chi_r]_{\chi_{r+1}}L_r(F)\) is a literal element of the higher scalar quotient. Its reduction is zero. Apply the original derivative to its full weighted image: the product rule gives a term containing \(\delta_rU_{r+1}\) times \([\chi_r]_{\chi_r}=0\), and the remaining term is \(U_r\alpha_r(\chi_r')L_r(F)\). This proves CC.28 on its declared two-depth domain. It does not differentiate an already-quotiented zero.

## 2. All coordinate jets, the sum jet and their kernels

Let \(E=P/I\), \(B_2=P/I^2\), \(c_i=[h'(s_i)]\), and retain the conormal isomorphism \(\iota:E^k\to I/I^2\). The coordinate derivative of \(h_i\widetilde v_i\), reduced modulo \(I\), is \(c_iv_i\) in coordinate \(i\) and zero in every other coordinate. This proves the full row, with its literal averaging factor,

\[
(v_i)\longmapsto(c_iv_i)_i\longmapsto\frac1k\sum_i c_iv_i.
\]

The image of the last row is exactly the ideal \((c_1,\ldots,c_k)\) because \(1/k\) is a nonzero scalar. Quotienting the original separate tensor factors by their derivative ideals identifies the cokernel with
\((\mathbb C[s]/(h,h'))^{\otimes k}\). If \(b=\deg\gcd(h,h')\), its dimension is \(b^k\), so the row has rank \(d^k-b^k\) and kernel dimension \((k-1)d^k+b^k\).

Each coordinate derivative sends \(I^2\) into \(I\). Its product rule along \(P/I^2\to P/I\) is precisely the multiplication rule of the square-zero extension \(E\oplus E^k\). Thus the all-coordinate jet and sum jet in CC.32 are unital algebra homomorphisms. The averaging algebra map is exactly

\[
\mathcal L(x,(v_i))=x+\epsilon\frac1k\sum_i v_i,
\]

and multiplying two elements verifies its algebra type directly. It gives \(J_S=\mathcal LJ_{\rm all}\), with no lost coefficient.

An element in either jet kernel has ordinary quotient zero, hence belongs to the conormal module. The previous coordinate derivative computation gives

\[
\ker J_S=\iota\ker\partial_N,
\qquad
\ker J_{\rm all}=\iota\left(\bigoplus_i\operatorname{ann}_E(c_i)\right).
\]

Multiplication by \(h'\) on \(\mathbb C[s]/(h)\) has cokernel dimension \(b\), and therefore kernel dimension \(b\); its other tensor factors are identities, giving \(\dim\operatorname{ann}_E(c_i)=bd^{k-1}\). The original monic expansion gives \(\dim B_2=(k+1)d^k\). Subtracting these respective kernel dimensions proves every image dimension in CC.33, including the squarefree isomorphism onto the full square-zero target. The bijective algebra map's inverse is automatically multiplicative: write two target elements as images, multiply those images, and apply the inverse.

The image formulas in CC.34 also retain the exact original section \(j\). Every lift of \(x\in E\) is uniquely \(j(x)+\iota(v)\), so its derivative is exactly \(d_0(x)+\partial_Nv\) or \(D_0(x)+(c_iv_i)_i\). This proves both inclusions of each displayed image formula and the precise inverse-image identity for \(\ker J_S\). The chapter does not assert that a diagonal section of the whole averaging target must preserve the actual jet image.

## 3. Invariant conormal dimensions and signs

Under the simultaneous action \((\sigma v)_i=\sigma(v_{\sigma^{-1}i})\), an invariant tuple is determined by its first component. That component is fixed by the stabilizer of index one. Conversely the stabilizer-fixed component determines each other component by a permutation carrying one to that index. If two such permutations are chosen, their quotient fixes index one and therefore fixes the initial component. These inverse maps prove CC.35 exactly.

A basis of invariant tensor powers is the set of unscaled orbit sums of basis words. Their occupation count gives

\[
\dim(E^k)^{S_k}=d\binom{d+k-2}{k-1},\qquad
\dim E^{S_k}=\binom{d+k-1}{k}.
\]

The row is equivariant. If an invariant vector has a preimage under an equivariant surjection, averaging that preimage with the retained factor \(1/k!\) gives an invariant preimage with the same image. This proves exactness of taking invariants in the row's cokernel sequence. The cokernel is consequently \((T_h^{\otimes k})^{S_k}\), with dimension \(\binom{b+k-1}{k}\) for \(b>0\), and zero for \(b=0\). Subtraction gives precisely both the invariant rank and kernel dimension in CC.36. At \(k=1\), the zero-fold tensor is \(\mathbb C\), and these formulas give the one-factor rank \(d-b\) and kernel dimension \(b\).

The stated fixture \(h=s^2,k=2\) passes directly: \(E\) has basis \(1,s_1,s_2,s_1s_2\), the contracted row is \(s_1v_1+s_2v_2\), its image has basis \(s_1,s_2,s_1s_2\), and its kernel dimension is \(8-3=5\). On invariants the conormal domain has dimension four and its image has basis \(s_1+s_2,s_1s_2\), giving kernel dimension two.

The cochain factor permutation contributes \(\operatorname{sgn}(\sigma)\) in degree \(k\). Multiplying it by the specified signed-chain averaging coefficient \(\operatorname{sgn}(\sigma)/k!\) gives exactly the ordinary invariant coefficient \(1/k!\). Its ordinary trace acquires the separate top-degree supertrace factor \((-1)^k\). The two signs have separate roles and are both retained.

## 4. Cyclic and product Jacobians through the same row

The exact original division \(\chi_1(S)=\sum_i h_iB_i\), differentiated with \(k^{-1}\sum_i\partial_i\), gives
\(\alpha_1(\chi_1')=k^{-1}\sum_i c_i[B_i]\). The terms containing an undifferentiated \(h_i\) vanish at the declared quotient. Thus

\[
\mathcal B(F)=([B_i]\alpha_1(F))_i,
\qquad
\partial_N\mathcal B(F)=\alpha_1(\chi_1'F)
\]

are well-defined module maps. The weighted relation \([U\chi_1F]_{I^2}\) depends only on the class of \(F\) modulo \(\chi_1\), because changing that representative introduces \(\chi_1^2\in I^2\). Its derivative is the declared weighted cyclic-Jacobian class. Since \(\alpha_1\) is injective, the composite kernel is the kernel of multiplication by \(\chi_1'\) in \(C_1\), which has one image dimension at each distinct sum and rank \(|\Lambda_k|\). This verifies CC.37 with its complete domain.

For the product observation, every component of
\(\mathcal P(v)=(v\prod_{j\ne i}c_j)_i\) contributes the identical value \(J_{\rm prod}v/k\) to the row. Their \(k\) terms therefore give exactly \(\partial_N\mathcal P= M_{J_{\rm prod}}\). Both the composite kernel and the intersection formula for \(\ker\mathcal P\) follow componentwise as stated; the factorization is equivariant.

In each one-variable original local factor, write \(h(\rho+z)=z^mu_\rho(z)\). Then, modulo \(z^m\),
\(h'(\rho+z)=m u_\rho(0)z^{m-1}\). The product over the original coordinates sends the input constant to the full socle monomial with nonzero coefficient \(\prod_i m_i u_{\rho_i}(0)\), and kills each local maximal ideal. Its kernel is exactly that ideal. Globally the finite product of local kernels is the nilradical, so the rank is \(a^k\) and kernel dimension \(d^k-a^k\). The stabilizer of an occupation acts trivially on its socle product, so one invariant image dimension survives per occupation, giving rank \(\binom{a+k-1}{k}\). This proves the invariant statement as well, without introducing a sign into the ordinary coefficient action.

For a conormal vector, the quotient of \(\iota(v)\) is zero; its weighted derivative consequently retains precisely \(U_1\partial_Nv\). Multiplication by \(U_1\) is invertible with inverse multiplication by the complete \(U_1^{-1}\), preserving the stated ranks and kernels without changing its Taylor coefficients. Thus CC.38–40 pass.

## 5. Residues, weighted traces and all four blocks

For every positively oriented finite root loop, the local factorization \(p=(T-\zeta)^mc\) gives \(p'/p=m/(T-\zeta)+c'/c\). The second term is holomorphic there. Its residue against \(F\) is therefore \(mF(\zeta)\), equal to the trace of the multiplication matrix on the full length-\(m\) local quotient, whose diagonal repeats \(F(\zeta)\) exactly \(m\) times. This proves CC.41. The functional is well-defined modulo \(p\), since changing a representative adds an entire polynomial differential. With the packet-reflection scope in Section 6, CC.42 follows by applying that identity to the displayed reflected product.

The one-variable arithmetic identity uses the literal factorization \(g'=h'v_h+hv_h'\), giving \(j_h(g')=h'\upsilon_h\). Its multiplication by the declared inverse \(\varepsilon_h=\upsilon_h^{-1}\) yields the exact unit cancellation in CC.43. Tensoring and expanding in the full separate-variable basis gives the product trace on every polynomial class, with no decomposability restriction.

Every entire \(f(S)\) preserves the cyclic submodule because it is a polynomial in the finite multiplication operator on each quotient. The generalized-sum exact sequence therefore gives the quotient trace with multiplicities \(a_{\lambda,r}-\ell_{\lambda,r}\). Applying the same logarithmic-derivative residue calculation proves CC.44.

For an arbitrary linear endomorphism \(M:A_r\to A_r\), the inverse coordinate maps are

\[
(c,v)\longmapsto\eta_rc+\iota_Kv,
\qquad
w\longmapsto(\Pi_rw,Q_rw).
\]

Conjugating \(M\) by these maps gives all four blocks in CC.45 with their exact domains: \(C_r\to C_r\), \(K_r\to C_r\), \(C_r\to K_r\), and \(K_r\to K_r\), respectively. Their two diagonal traces add to the full trace; the trace identity under coordinate changes follows from the finite sum proving \(\operatorname{Tr}(XY)=\operatorname{Tr}(YX)\).

The formula \([v]\mapsto[Mv]\) on the complementary quotient is well-defined precisely when \(M\eta_rC_r\subseteq\eta_rC_r\), equivalently \(Q_rM\eta_r=0\). In that case its representative on \(K_r\) is the lower-right block; otherwise that block is still the stated retraction-dependent compression. For a multiplier \(M_w\), applying this criterion to \(\eta_r1=U_r\) and multiplying by \(U_r^{-1}\) proves necessity of \(w\in\alpha_r(C_r)\). Closure of that subalgebra proves sufficiency. For \(w=f(S)\), module linearity makes both cross maps zero.

Multiplicativity of dagger gives the literal identity
\((\eta_rF)^\dagger\eta_rG=U_r^\dagger U_r\alpha_r(F^{\dagger_k}G)\). Inserting this full multiplier into all four proved blocks is exact. No quotient action for it is presumed from permutation invariance. Finally, evaluation of an original Hermitian form on the two sums \(\eta_rc+\iota_Kv\) and \(\eta_rc'+\iota_Kv'\) produces all four terms in CC.49; algebraic splitting alone supplies no orthogonality. CC.44–49 pass.

## 6. Reflection scope and the exact map for an arbitrary packet

The delivered NOTE explicitly assumes stability under \(\rho\mapsto1-\overline\rho\), with the original full orders. This is the hypothesis needed for the dagger paragraph to be an involution of each \(B_r\). CC.1's algebraic setup allows an arbitrary nonempty packet. The reflection paragraph should explicitly retain the delivered stability when it forms a pairing in the same quotient. This request was sent to the author before sealing.

There is also an exact comparison for every packet, so no unrelatedness follows from absence of stability. Define the original reflected monic polynomial

\[
h^\#(s)=(-1)^d\overline{h(1-\overline s)}
=\prod_\nu(s-(1-\overline{\rho_\nu}))^{m_\nu}.
\]

The conjugate-linear multiplicative bijection

\[
\mathfrak d_r:B_r(h)\longrightarrow B_r(h^\#),\qquad
[F]\longmapsto[\overline{F(1-\overline s_1,\ldots,1-\overline s_k)}]
\]

sends each original ideal generator to \((-1)^dh^\#(s_i)\), so it sends its exact power \(I(h)^r\) onto \(I(h^\#)^r\). Applying it twice gives the identity. It commutes with permutations and thus restricts to the invariant algebras. The reflected scalar sum set has values \(k-\overline\lambda\) with the same full collided exponents, and

\[
\chi_{h^\#,k,r}(T)
=(-1)^{q_r}\overline{\chi_{h,k,r}(k-\overline T)}.
\]

Consequently the corresponding scalar conjugate-linear algebra bijection \([F]\mapsto[\overline{F(k-\overline T)}]\) commutes with the two \(\alpha_r\) maps. When the original packet is reflection-stable, \(h^\#=h\); these exact comparison maps are precisely the same-quotient involutions used in CC.42 and CC.48. This supplies the full type of the reflection construction rather than silently extending its same-quotient scope to arbitrary packets.

## 7. Two-factor invariant ideal at every depth

Retain the invertible coordinates \(S=s_1+s_2\), \(R=s_1-s_2\), \(\Delta=R^2\), with the inverse factors \(1/2\). Expanding the literal original polynomial term by term proves the displayed \(H_0,H_1\) in CC.50 and the exact identities

\[
h(s_1)=H_0+RH_1,\qquad h(s_2)=H_0-RH_1.
\]

Taking the sum and difference with factors \(1/2\) proves both containments of \(I=(H_0,RH_1)\). No division by \(R\), \(H_1\), or \(\Delta\) occurs, so the identities retain their full diagonal fibre.

Every element of \(I^r\) is a sum of \(H_0^{r-j}R^jH_1^j a_j(S,R)\), for \(0\leq j\leq r\). If the sum is invariant, apply the exact averaging projection \((1+\sigma)/2\) to this expression, where \(\sigma R=-R\). For even \(j\), only the even part of \(a_j\) survives, giving
\(H_0^{r-j}\Delta^{j/2}H_1^j\) times a polynomial in \(S,\Delta\). For odd \(j\), only the odd part survives. That odd part is \(R\) times a polynomial in \(S,\Delta\), giving
\(H_0^{r-j}\Delta^{(j+1)/2}H_1^j\) times that polynomial. This proves

\[
I^r\cap\mathbb C[S,\Delta]
\subseteq
\left(H_0^{r-j}\Delta^{\lceil j/2\rceil}H_1^j:0\leq j\leq r\right).
\]

Conversely, when \(j\) is even the displayed generator is the original \(j\)-th ideal-power generator. When \(j\) is odd it is that original generator multiplied by \(R\). Thus every displayed generator is invariant and belongs to \(I^r\), proving the reverse containment. Every invariant quotient class has an invariant polynomial lift by the same averaging operation. Hence the natural algebra map from \(\mathbb C[S,\Delta]\) onto \(B_r^{S_2}\) has exactly the displayed ideal kernel. This proves CC.51 at every depth, including \(R=0\).

The scalar map \([F(T)]\mapsto[F(S)]\) has precisely the previously proved contracted ideal \((\chi_r)\) before taking its source quotient; its resulting arrow is the stated injection. The full symmetric Taylor product \(v_h((S+R)/2)v_h((S-R)/2)\) is exactly \(U_r\), so the weighted inclusion retains the same unit.

The comparison to SSP.9 is exact: that section defines \(H_0=A_0(-Z^2,\Delta)\), \(H_1=ZA_1(-Z^2,\Delta)\), which are respectively the even coefficient and the coefficient of \(R\) in this same unchanged polynomial under \(S=1+Z\). At depth one, (CC.51) becomes precisely \((H_0,\Delta H_1)\). Adjoining \(x=-Z^2\) retains \(Z\) and its relation, so the cyclic map is \(F(T)\mapsto F(1+Z)\) in the full SSP algebra; no inverse of the squaring map by itself is asserted.

For completeness, the following exact all-depth parity presentation was sent to the author as an optional extension of this comparison. Under those same quartet assumptions, let \(R_0=\mathbb C[x,\Delta]\). For even indices \(2a\leq r\) and odd indices \(2a+1\leq r\), define the unchanged-coefficient polynomials

\[
E_{2a}=A_0^{r-2a}\Delta^a(-x)^aA_1^{2a},\qquad
O_{2a+1}=A_0^{r-2a-1}\Delta^{a+1}(-x)^aA_1^{2a+1}.
\]

Substitution \(Z^2=-x\) into the proved ideal gives

\[
A_r\cong R_0[Z]/(Z^2+x,\ (E_{2a})_a,\ (ZO_{2a+1})_a).
\]

Before the last two sets of relations, division by the monic polynomial \(Z^2+x\) gives the free module \(R_0\oplus ZR_0\). Multiplying an even relation by \(c+Zd\) gives coefficients \((E_{2a}c,E_{2a}d)\); multiplying an odd relation by \(c+Zd\) gives \((-xO_{2a+1}d,O_{2a+1}c)\). Consequently the even and odd modules are exactly

\[
B_{e,r}=R_0/((E_{2a})_a,(xO_{2a+1})_a),\qquad
B_{o,r}=R_0/((E_{2a})_a,(O_{2a+1})_a),
\qquad A_r=B_{e,r}\oplus ZB_{o,r}.
\]

The quotient map \(\beta:B_{e,r}\to B_{o,r}\) and the module map \(\alpha:B_{o,r}\to B_{e,r}\), \([b]\mapsto[xb]\), are well-defined by those explicit ideals. They satisfy \(\alpha\beta=xI\), \(\beta\alpha=xI\), and the multiplication is exactly
\((a,b)(c,e)=(ac-\alpha(be),\beta(a)e+\beta(c)b)\). This follows by multiplying \((a+Zb)(c+Ze)\) and retaining \(Z^2=-x\). At \(r=1\) these are SSP.6–7. This addendum proves the parity modules at each original depth without deleting \(Z\), \(\Delta\), any relation, or a factor \((-x)^a\).

## 8. Split lifts and review scope

For every complex-linear map above, the proposed lift sends external absence \(\tau\) to \(\tau\) and supported \(v\) to supported \(Lv\). On supported inputs its additivity and scalar compatibility are the original linear identities; all cases with \(\tau\) follow from the declared additive-identity and absorbing-action rules. An algebra homomorphism also preserves supported products and its supported unit. Thus the first-jet maps have the claimed multiplicative lifts, whereas each derivative has its proved linear lift. A conormal class is sent to supported zero by the quotient and to its actual derivative class by the derivative or square-zero jet. These maps share the original thickening as their source, exactly as in CC.52.

No new arithmetic asymptotic is established by this review. It certifies the complete displayed finite algebra, coefficients, derivative and quotient types, invariant ideal, exact ranks and trace maps. The original interpolation metric and the quantitative next calculation remain those specified by the adjoining mathematical work.

## 9. Final candidate and complete delta acceptance

The final TeX candidate was read from disk and its SHA256 was independently computed as `1182806be9a6e1ecde9b594a195a8cd3fa17b7259540fcd5617d044d06b05e79`. The added reflection sentence near CC.1 explicitly retains the delivered reflection closure and full multiplicities. It resolves the hypothesis issue identified in Section 6. Moving the dagger formula to a display preserves the exact conjugate-linear map and all reflected coordinates.

The added CC.51a and CC.51b were read in full. Their polynomials preserve every factor \((-x)^a\), \(\Delta^a\), \(\Delta^{a+1}\), and the original \(A_0,A_1\). Their two coefficient ideals are exactly the even and odd ideals proved in Section 7 above. The map \(\beta_r^{\mathrm{par}}\) is the quotient map, while \(\gamma_r^{\mathrm{par}}\) is multiplication by the original \(x\), with its declared module type. Their composition identities and product sign follow from \(Z^2=-x\) and pass. These superscripts also prevent a collision with the logarithmic class \(\beta_r\). At \(r=1\), the formulas reduce literally to SSP.6–7. The full original arithmetic unit remains carried by the inverse coefficient maps.

The closing paragraph distinguishes the historical uncompiled draft, the separately recorded PR21 CI provenance and the present written proofs. This review makes no independent claim about PR21 CI or the author's reported compilation result; its own acceptance is the complete mathematical read and the computed TeX hash just stated. No Lean process was started, and no cumulative or frozen artifact was edited by this reviewer.
