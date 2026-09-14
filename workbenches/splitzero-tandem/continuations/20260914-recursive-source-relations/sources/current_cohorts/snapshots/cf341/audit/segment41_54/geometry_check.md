# Independent A1520 geometry and tensor check

Audit scope: ONLY transcript block A1520, with earlier definitions in the same source segment when needed. Source: `output/tau_f1_transcript_audit_2026-09-13/sources/audit_segment_U0041_U0054.md`, within lines 1–2481. No derivative notes or later continuation supplied evidence. Parent owns the complete user-input provenance and the global audit. This file records the bounded independent calculation, not a replacement mathematical programme.

Task received: “Independently audit ONLY A1520 … Need check claimed topological contraction c:P=widehat X×widehat X -> widehat(X×X), c_* coefficient stalk G(A)^2, derived boundary arms direct sum, tensor Q^⊗n and U_a action. Use transcript as source only, no later derivative notes. Do not recalc A_tau/res_sigma/derived right adjoint (root doing). Send rigorous validity limitations with source locators, especially counterexamples if any.”

## Verdict

The topological quotient map, coefficient stalk, vector-space derived boundary stalk, theta H0/H1 calculation, and algebraic tensor-power identification are valid for the objects actually displayed. The scaling action is valid for a>0. The finite-jet formula is valid at actual nontrivial zeros with the retained multiplicities, as specified in the preceding source lines 965–980. This does not establish the missing weight bound. The support Cartesian-product formula is a multilinear support operation; it is not a join-preserving map on the Cartesian product support lattice. Full proofs and exact qualifications follow.

## 1. The contraction is a continuous quotient map

Source: A1520 lines 1436–1477. Give X its stated topology, and give widehat X=X disjoint-union {sigma} the topology consisting of the empty set and U+ = U union {sigma}, U open in X. In particular {sigma} is open. P is explicitly the product of underlying topological spaces (lines 1449–1452), and X×X below consequently means the topological product.

Put B1=widehat X×{sigma}, B2={sigma}×widehat X and B=B1 union B2. Each Bi is open, hence B is open. Define c on X×X by c(x,y)=(x,y) and define c(b)=sigma_* for b in B. For any open W in X×X,

    c^(-1)(W union {sigma_*}) = B union W.

Write W as the union of open rectangles U_alpha×V_alpha contained in W. Then

    B union W = B union union_alpha(U_alpha+ × V_alpha+).

Every set on the right is open in P, proving continuity with the full inverse-image formula, including W=empty.

In fact c is a quotient map. Every nonempty open subset of P contains (sigma,sigma), since every nonempty basic product open contains that point. Therefore a subset of the target whose inverse image is open and nonempty must contain sigma_*. Its intersection W with X×X is open in X×X, because it is the intersection of the open inverse image with the subspace X×X. Thus the subset is W union {sigma_*}, exactly an open of the displayed target topology. This proves the universal topological collapse of B, and not merely a set map.

Qualification: this is the topological product explicitly chosen in the transcript. It is not automatically the underlying space of an algebraic fibre product. For example Spec(C)×Spec(C) as topological spaces is a singleton; the underlying space of Spec(C)×_Spec(Z)Spec(C)=Spec(C tensor_Z C) has distinct primes ker(mu_id) and ker(mu_conj), where mu_id(z tensor w)=zw and mu_conj(z tensor w)=z conjugate(w). They are distinct because i tensor 1−1 tensor i is in the first kernel and maps to 2i under the second map. The transcript explicitly avoids claiming the universal semiring-scheme fibre product in lines 1545–1547. Its chosen topological map is sound within that scope.

The word “contraction” here is justified as a quotient collapsing B. No deformation-retraction or homotopy claim is needed by the calculation.

## 2. The coefficient stalk is exactly G(A)×G(A)

Source: lines 1442–1446, 1481–1542. The semiring sheaf S_X is defined more fully in lines 120–138, with S_X(U+)=G(O_X(U)) and S_X({sigma})=G(0)=B_boolean. Its sheaf proof is valid: overlapping nonempty opens all meet sigma, so compatible local sections have a common absent/supported status; their amplitudes glue by the ordinary structure-sheaf axiom. For affine X, Gamma(widehat X,S_X)=G(A).

The target singleton {sigma_*} is a smallest open neighbourhood. Consequently

    (c_*A_P)_(sigma_*) = Gamma(B,A_P),
    A_P = pr_1^(-1)S_X × pr_2^(-1)S_X.

Let L1=pr_1^(-1)S_X. On B1 the first projection is a homeomorphism to widehat X, so L1|B1 identifies with S_X. On B2 the first projection is constant at sigma, so L1|B2 is the constant sheaf with value B_boolean. Every nonempty open of B2 contains its sigma corner; a locally constant section therefore has one common value, proving Gamma(B2,L1)=B_boolean. On B1 intersect B2 the stalk is B_boolean. The restriction from B1 is chi_A, whereas the restriction from B2 is the identity. The two-open sheaf equalizer is therefore

    Gamma(B,L1) = {(s,b) in G(A)×B_boolean : chi_A(s)=b}.

Projection (s,b)↦s and s↦(s,chi_A(s)) are mutually inverse semiring homomorphisms. Exchanging the arms gives Gamma(B,L2)=G(A). Finite products of sheaves are evaluated sectionwise, so the exact stalk is G(A)×G(A), including both absent elements and both supported zeros.

The arithmetic map is (p_A,p_A), and the stated diagonal satisfies

    pr_j circ (p_A,p_A) circ Delta = p_A, j=1,2.

This does not divide out a diagonal or replace the original norm domain; those maps have the domains and codomains claimed.

Terminology: S_X is a semiring sheaf, so “semiringed space” is more precise than “ringed space” at line 1547. This vocabulary issue does not invalidate its section maps.

## 3. The derived stalk is the sum of the two original cohomology complexes

Source: lines 1551–1576. Work in sheaves of vector spaces over the stated coefficient field. The inclusion i:X→widehat X is closed since {sigma} is open. V=i_*F has V_(sigma)=Gamma(empty,F)=0. Define K=pr_1^(-1)V direct-sum pr_2^(-1)V.

Restriction to B1 gives V direct-sum 0, restriction to B2 gives 0 direct-sum V, and restriction to their intersection gives 0. These statements follow from functoriality of inverse image: the projection transverse to each arm factors through the zero stalk V_(sigma).

Because {sigma_*} is a smallest open neighbourhood and B=c^(-1){sigma_*} is open,

    (Rc_*K)_(sigma_*) = RGamma(B,K|B).

To justify this derived identification explicitly, take an injective resolution of K. Restriction to the open subset B preserves injectives: it is right adjoint to exact extension by zero. Evaluation of c_* on the smallest neighbourhood is evaluation of that resolution on B. Therefore the resulting complex computes precisely RGamma(B,K|B).

The two-open derived Mayer–Vietoris triangle is

    RGamma(B,K) → RGamma(B1,K) direct-sum RGamma(B2,K)
                  → RGamma(B1 intersect B2,K) → RGamma(B,K)[1].

The third complex is zero. The middle complex is two copies of RGamma(widehat X,i_*F). A closed inclusion has exact direct image, and its direct image preserves injectives because i^(-1) is exact; moreover Gamma(widehat X,i_*F)=Gamma(X,F). Applying these facts to an injective resolution gives

    (Rc_*K)_(sigma_*) ≅ RGamma(X,F) direct-sum RGamma(X,F).

Thus there is no omitted intersection term or hidden shift in lines 1563–1576.

## 4. The theta kernel and cokernel agree with the claimed formulas

Source: lines 1583–1644. The intended finite topology of Y has open charts U_+={y_+,eta} and U_-={y_-,eta}, with intersection {eta}; this is the two-chart topology presupposed by lines 1607–1628. Its sheaf T has values V,V,B_script on these three smallest opens, with restriction maps Theta and I Theta. Each chart's sections functor is the evaluation at its smallest point, hence is exact. The augmented two-open Cech resolution therefore yields

    RGamma(Y,T) ≅ C_Theta = [V direct-sum V → B_script],
    d(phi,psi)=Theta(phi)−I Theta(psi).

Fourier transformation preserves V: evenness is preserved, Fourier phi at zero equals integral phi=0, and integral Fourier phi equals phi(0)=0 under the displayed convention. Poisson summation gives I Theta=Theta Fourier, so image d=Theta V. Therefore H1=B_script/Theta V exactly as in line 1637.

The H0 identification additionally uses injectivity of Theta, which is not proved in the displayed A1520 text but follows directly without an analytic completion. For every x>0 and phi in V, evenness gives Theta phi(x)=2 sum_(m≥1)phi(mx). Let mu be the integer Möbius function. Choose N>1. The Schwartz bound gives |phi(mnx)|≤C_(N,x)(mn)^(-N), so

    sum_(n,m≥1) |mu(n) phi(mnx)| < infinity.

Consequently the absolutely convergent sums may be rearranged:

    (1/2) sum_(n≥1) mu(n) Theta phi(nx)
      = sum_(k≥1) [sum_(n|k)mu(n)] phi(kx)
      = phi(x).

The divisor sum is 1 for k=1 and 0 for k>1, by the expansion of the product over the distinct prime divisors of k of (1−1). If Theta phi=0 then phi vanishes on x>0; evenness gives vanishing on x<0, and phi(0)=0 is already imposed. Thus Theta is injective. It follows that d(phi,psi)=0 precisely when phi=Fourier psi, proving the complete H0 formula of lines 1632–1634.

Applying the result in section 3 with X=Y, F=T now gives (R1 c_*K)_(sigma_*)=Q_Theta direct-sum Q_Theta, with no assumption identifying Y with Spec(Z). The transcript expressly disclaims that identification in lines 1650–1658.

## 5. Algebraic tensor cohomology and the exact boundary signs

Source: lines 1724–1759. Coefficients are explicitly vector spaces over C, and the tensor symbol is the algebraic tensor product. Let E=i_*T on widehat Y. Its stalk is zero at sigma and equals T elsewhere. The two opens U_+ union {sigma} and U_- union {sigma} cover widehat Y. Their intersection {eta,sigma} has smallest point eta; the first two smallest points are y_+,y_-. Thus every chart or chart intersection is acyclic for E, and its section diagram is again V,V,B_script.

For n factors, take the product chart cover in each coordinate and the associated n-fold Cech complex. Every product chart intersection has a smallest point, the tuple of its factorwise smallest points. Evaluation there is exact, and the external tensor sheaf's value at that tuple is the algebraic tensor product of the corresponding factor stalks. Consequently the multicomplex of sections has, in degree (epsilon_1,…,epsilon_n), exactly C_Theta^(epsilon_1) tensor … tensor C_Theta^(epsilon_n). Its totalization computes the derived sections, with the sign (-1)^(epsilon_1+…+epsilon_(j-1)) before the j-th differential. This proves the quasi-isomorphism and differential in lines 1731–1743 for every integer n≥1.

Its top degree is B_script^(tensor n). Degree n−1 is the direct sum of the n spaces with one factor V direct-sum V and all other factors B_script. On the j-th summand the differential is (-1)^(j−1) times identity tensor … tensor d tensor … tensor identity. Since image d=Theta V and multiplication by (-1)^(j−1) does not change a vector subspace, the full top boundary is precisely

    sum_(j=1)^n B_script^(tensor(j−1)) tensor Theta V
                  tensor B_script^(tensor(n−j)).

The canonical map B_script^(tensor n)→(B_script/Theta V)^(tensor n) is surjective and has exactly this kernel, by iterating right-exactness of tensor products over the field C. Hence its induced map on the displayed quotient is the inverse of

    [F1] tensor … tensor [Fn] ↦ [F1 tensor … tensor Fn]

in lines 1749–1756. No completed tensor product, Hausdorff quotient, closed-range assertion, topological Kunneth theorem, or nuclearity theorem has been proved by this argument. Those are different additional assertions and are not stated in A1520's tensor display.

## 6. The mask formula is separately join-preserving

Source: lines 1761–1765; earlier reconstruction conventions are lines 215–285. The map (J1,…,Jn)↦J1×…×Jn preserves unions in each argument separately and sends an empty argument to the empty set. Thus it is the right support law for a multilinear tensor map. On a fixed nonempty product mask, tensoring a zero vector in any factor gives the zero vector of that same receiving mask; reconstructing with that label gives a supported zero, not tau. If some mask is empty the target is the absent element.

It is not a join homomorphism from the Cartesian product of the mask lattices with componentwise joins. Already for n=2, take x=({1},{1}) and y=({2},{2}). The image of x join y is {1,2}×{1,2}, whereas image(x) union image(y) contains only (1,1) and (2,2). The mixed pairs (1,2),(2,1) make the failure explicit. Therefore treating line 1763 as a single linear morphism from the Cartesian product reconstructed additive object would be false. The separately multilinear reading is valid and is all that the external tensor construction requires.

The vector-space sheaf V_n alone does not record the distinction between absent and supported zero: zero is a single vector. That distinction belongs to the separately retained label diagram and reconstruction of lines 215–248. The two maps should be kept typed together; the tensor computation does not itself construct new label data from an unlabeled vector space.

## 7. The positive scaling action is a chain action

Source: lines 1767–1782. The required domain is a>0, since B_script consists of functions on R_(>0). For U_aF(x)=F(x/a), both U_a and U_(1/a) preserve the stipulated Schwartz spaces and V's evenness and two zero moments. The exact identities are

    Theta U_a = U_a Theta,
    Fourier(U_a phi)=a U_(1/a) Fourier(phi),
    U_a I = a I U_(1/a).

For the last identity, both sides applied to F at x equal (a/x)F(a/x). For the Fourier identity, substituting x=ay in the stated Fourier integral gives a Fourier(phi)(a xi), exactly a U_(1/a)Fourier(phi)(xi). The first identity follows term by term from the absolutely convergent theta series.

Therefore

    d(U_a phi, a U_(1/a)psi)
      = U_a Theta phi − a I U_(1/a)Theta psi
      = U_a[Theta phi−I Theta psi]
      = U_a d(phi,psi).

Composition satisfies T_a T_b=T_(ab) on both degrees, since the second-chart prefactors multiply to ab and U_(1/a)U_(1/b)=U_(1/(ab)); T_1 is the identity. This is the stated representation of R_(>0), with the factor a retained. Substitution x=ay in M(F)(s)=integral_0^infinity F(x)x^s dx/x gives M(U_aF)(s)=a^s M(F)(s). The same identities induce the diagonal action on every algebraic tensor power.

The A1520 scaling display omits the domain a>0, which is already required by its functions' domain R_(>0). At a=0 the formula is undefined; at a<0 it does not operate on functions whose domain is R_(>0). This is a necessary typing qualification, not a failure of the action on its intended group.

## 8. Finite jets: scope and exact operator

Source: A1520 lines 1784–1796, read with earlier lines 965–980 and 1234–1236. The earlier text specifies g(s)=2xi(s), actual nontrivial zeros rho, and their actual multiplicities m_rho, with g(rho+z)=u_rho(z)z^(m_rho), u_rho(0) nonzero. Thus O_(C,rho)/(g)=O_(C,rho)/(z^(m_rho)), retaining the original unit in the factorization even though its ideal is the same. Define N_rho to be multiplication by z in that local algebra; it obeys N_rho^(m_rho)=0.

Multiplication by a^s=a^rho exp((log a)z), a>0, induces exactly

    a^rho sum_(r=0)^(m_rho−1) ((log a)^r/r!) N_rho^r.

This is the finite polynomial meant by a^rho exp((log a)N_rho). On n copies of the same local quotient, the commuting operators N_(rho,j) act in their respective factors. Multiplying the n exponential polynomials gives

    a^(n rho) exp((log a) sum_(j=1)^n N_(rho,j)).

Every term of total nilpotent degree greater than n(m_rho−1) vanishes, so the last exponential is again a finite polynomial. This is exactly lines 1789–1793. If different zeros rho_j are chosen, the same calculation has scalar a^(sum_j rho_j) and nilpotent sum_j N_(rho_j,j); the displayed a^(n rho) pertains to the equal-rho block as stated.

The transcript's assertion of a pre-existing Mellin-jet map occurs at lines 1234–1236. A1520 itself does not write that map or prove its surjectivity; this is an omitted derivation in the displayed text, not evidence that the nilpotent formula fails. The exact construction and proof follow; these were independently checked by the bounded jets-check agent from the same transcript and the displayed definitions.

For an actual nontrivial zero rho and its actual multiplicity m=m_rho, define

    J_(rho,m)(F) = sum_(k=0)^(m−1) [(MF)^(k)(rho)/k!] z^k
                   in C[z]/(z^m).

The Mellin transform of a strong-Schwartz F is entire. For phi in V, smooth evenness and phi(0)=0 imply phi(x)=O(x^2) as x→0, whereas phi has Schwartz decay at infinity. Consequently Mphi(s)=integral_0^infinity phi(x)x^s dx/x is holomorphic on Re(s)>−2. In Re(s)>1, absolute convergence permits integration term by term in the theta sum and gives

    MTheta(phi)(s) = 2 zeta(s) Mphi(s).

The identity continues analytically to a neighbourhood of each nontrivial zero. Here zeta and xi have the same zero order: the factor (1/2)s(s−1)pi^(−s/2)Gamma(s/2) relating xi to zeta is holomorphic and nonzero at a point with 0<Re(s)<1. Hence the right side vanishes at rho to order at least m. This proves Theta V⊆ker J_(rho,m), so J descends to Q_Theta.

Surjectivity is already visible on C_c^infinity(R_(>0)), a subspace of B_script. Its coordinate functionals are

    L_k(F) = (1/k!) integral_0^infinity F(x)x^rho(log x)^k dx/x,
    0≤k<m.

If sum_k b_k L_k vanished on every compactly supported smooth F, the continuous function x^(rho−1)sum_k b_k(log x)^k/k! would vanish for all x>0. Indeed, a nonzero value would remain in an open complex half-plane after multiplication by a fixed scalar on a sufficiently small neighbourhood, and a nonnegative smooth bump supported there would have nonzero integral. As x^(rho−1) never vanishes and log maps R_(>0) onto R, the polynomial is zero and all b_k are zero. Thus the m coordinate functionals are independent. If their joint image were a proper vector subspace of C^m, a nonzero linear functional on C^m would annihilate it, contradicting this independence. The joint map is therefore surjective. The exact sequence is

    0 → ker(J_(rho,m))/Theta V → Q_Theta → C[z]/(z^m) → 0.

Under the scaling action,

    J_(rho,m)(U_a F)
      = [a^(rho+z) MF(rho+z)] modulo z^m
      = a^rho exp((log a)N_rho) J_(rho,m)(F).

Tensoring this surjection over C gives Q_Theta^(tensor n)→(C[z]/(z^m))^(tensor n), a surjection onto the full m^n-dimensional target with its factorwise nilpotents. This supplies the missing exact morphism behind the finite quotient language of lines 1784–1796.

The actual-zero restriction cannot be removed. Choose a nonzero nonnegative h in C_c^infinity((1,2)) and set

    phi(x)=h(|x|)−(1/2)h(|x|/2).

This phi is smooth, even, compactly supported away from zero, and has integral zero: the second summand's dilation factor 2 exactly cancels the coefficient 1/2. Thus phi belongs to V. But

    Mphi(s)=(1−2^(s−1)) Mh(s),
    MTheta(phi)(2)=−2 zeta(2) Mh(2) ≠ 0.

Therefore evaluation at rho=2 does not descend to Q_Theta, since a theta boundary would acquire a nonzero value. Calling a nonzero jet space at an arbitrary point a quotient of Q_Theta would be false.

The multiplicity restriction is also exact. At an actual nontrivial zero rho, choose h with sufficiently small positive support so that the values x^rho throughout its support lie in a single open complex half-plane after a fixed rotation. Then Mh(rho)≠0. Moreover |2^(rho−1)|=2^(Re rho−1)<1, so 1−2^(rho−1)≠0. The displayed phi consequently has Mphi(rho)≠0, and MTheta(phi) has vanishing order exactly m at rho. The jet map of any length greater than m therefore does not annihilate every theta boundary. Lengths at most m do descend; A1520's full local divisor quotient uses exactly the actual m.

No finite-jet quotient by itself supplies a lifted eigenvector in the uncompleted Q_Theta, which the transcript correctly states at line 1796.

## 9. Programme-level consequence

All calculations above are constructions of spaces, sheaves, algebraic cohomology, and explicit action maps. They provide no estimate of a weight, norm, or spectral real part. A1520 states that remaining limitation itself in lines 1798 and 1859. Its tensor isomorphism is therefore a valid construction relevant to a possible amplification programme; it does not on its own establish the additional analytic control needed for such an argument.

Status: completed topological, derived, theta-injectivity, tensor, mask, scaling, and finite-jet descent/surjectivity proofs. The only file modified by this bounded check is this scratch report. No Lean, package tests, remote source, or derivative mathematical note was used.
