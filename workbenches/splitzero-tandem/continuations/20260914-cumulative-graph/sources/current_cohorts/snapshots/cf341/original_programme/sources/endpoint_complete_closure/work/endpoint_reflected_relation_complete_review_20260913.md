# Reflected relation algebra: complete review and exact finite fixtures

The complete proof `endpoint_reflected_relation_fibre_product_20260913.tex`, RF.1–RF.17, was read at SHA-256 `1acac595a7f89229569b8e28f63981bce4e072c623b39266af038a6b70671d52`. The displayed formulas, ideal maps, original coordinate phases and root orders are correct. One prose statement at line 264 needs correction: the two kernels are called modules “over A_chi”. Their common coefficient ring is C[S]; only the first conormal kernel necessarily has the original A_chi action. The exact obstruction and the strongest valid quotient action are proved below. The root author has been notified; this reviewer did not edit the proof.

The complete independent companion `endpoint_reflection_independent_typing_review_20260913.md`, SHA-256 `2af9df8b95cfd8cd5bd69f158eb7f4e16a489ae97092f3b52dc326aa77405dfd`, was read in full. It independently checks every RF.1–RF.17 map and proves an explicit raw-jet inverse. It identifies the same prose defect and no additional one. Its further independent algebra reader agrees on RF.10–RF.16. This report supplies the full typed correction and the requested mixed, disjoint and stable examples with actual exact arithmetic results.

## Original reflection, norm and coordinate maps

Keep k≥1, c=k/2, S, and monic χ of degree q≥1 exactly as in the source. Put A=C[S]. Coefficient conjugation fixes the formal variable. The operation f★(S)=overline f(k−S) is additive and conjugate-linear: (af+bg)★=overline a f★+overline b g★. It is multiplicative and its square is the identity because k is real. The operation χ†=(−1)^qχ★ is defined on the selected monic degree-q polynomial; it is not being asserted to be a linear map on arbitrary polynomials of different degrees. Its leading coefficient is one. Applying the same degree-q operation twice returns χ. The two factors in Nχ★ each contribute (−1)^q, so Nχ★=Nχ.

The complex algebra map Ψf(u)=f(c+iu) has inverse F↦F((S−c)/i). It intertwines ★ with coefficient conjugation on C[u]:

\[
 \Psi(f^\star)(u)=\overline f(c-iu)=\overline{\Psi f}(u).
\]

Writing ψ=i^(−q)Ψχ gives exactly

\[
 \Psi\chi=i^q\psi,\quad
 \Psi\chi^\dagger=(-1)^q(-i)^q\overline\psi
                 =i^q\overline\psi,\quad
 \Psi N_\chi=i^{2q}\psi\overline\psi.
\]

Thus Π=ψ overlineψ is monic with real coefficients and Π(u)=|ψ(u)|² on the real axis. The original evaluation ΨNχ contains the factor i^(2q)=(−1)^q; this factor must not be replaced by one. The three RF.4 conditions are equivalent by the displayed identity for Ψχ† and injectivity of Ψ. Their consequence Nχ=χ² retains this original evaluation phase.

For any original polynomial Q, multiplicativity gives Ψ(χQ)=i^qψΨQ. The pointwise equality

\[
 |\chi(c+iu)Q(c+iu)|^2
   =|i^q|^2|\psi(u)\Psi Q(u)|^2
   =\Pi(u)|\Psi Q(u)|^2
\]

proves RF.5 upon integration against the same arithmetic density. No density, total mass, support or integration variable is changed. Finiteness is the polynomial integrability supplied by the stated original source construction. This equality proves the norm comparison without a claim about quotient-volume growth.

## Full root orders, raw jets and semilinear reflection

Let λ*=k−overlineλ. Factoring χ shows bλ=a_(λ*) and rλ=aλ+bλ. Each root factor contributes one minus sign per multiplicity under reflection, exactly cancelling the total (−1)^q in χ†. The map λ↦λ* is an involution; its fixed roots have Re λ=c and necessarily aλ=bλ. The Nχ root set and its rλ multiplicities are stable under it.

The map Ψ sends the ideal (Nχ) onto (Π), since its displayed leading factor is an invertible scalar. Consequently it induces a complex algebra isomorphism on the two quotient rings, with its inverse induced by the original inverse substitution.

For each λ retain all rλ raw derivatives. Their common kernel on A is (Nχ): vanishing of derivatives 0 through rλ−1 is equivalent to divisibility by (S−λ)^rλ, as follows from the Taylor expansion with factors 1/d!. Coprimality at distinct roots converts all those divisibilities into divisibility by their product. The quotient and all raw blocks have the same dimension 2q, proving surjectivity as well as injectivity. Leibniz gives the product coefficient binom(d,j). The units are (1,0,…,0). Thus RF.8 has a specified algebra structure, rather than merely an identification of vector-space dimensions.

With ζλ=(λ−c)/i, the exact differential and original S-action formulas are

\[
 (\Psi P)^{(d)}(\zeta_\lambda)=i^dP^{(d)}(\lambda),\qquad
 (SP)^{(d)}(\lambda)=\lambda P^{(d)}(\lambda)+dP^{(d-1)}(\lambda).
\]

The reflected action on these raw blocks is conjugate-linear and includes its own derivative sign:

\[
 (P^\star)^{(d)}(\lambda)=(-1)^d
       \overline{P^{(d)}(\lambda^*)},\qquad
 \zeta_{\lambda^*}=\overline{\zeta_\lambda}.
\]

Indeed differentiating overline P(k−S) d times gives the factor (−1)^d, while evaluating coefficient conjugation at k−λ is conjugating evaluation of P at k−overlineλ. Multiplying by i^d yields (−i)^d times that conjugated derivative, which is exactly the conjugate of the corresponding u-coordinate derivative. Reflection therefore intertwines the complete phase-weighted raw-jet maps, at every retained order. The explicit fixtures below check the entire matrices, including this conjugate-linear structure.

## The kernel action and the precise prose correction

The quotient map πN:A/(χχ†)→A/(χ) is a surjective algebra homomorphism. Its kernel IN=(χ)/(χχ†) has the coefficient-module isomorphism

\[
 A/(\chi^\dagger)\longrightarrow I_N,\quad[f]\longmapsto[\chi f].
\]

Well-definedness and injectivity follow from cancellation χχ†|χf iff χ†|f. Surjectivity onto the kernel follows by choosing a representative divisible by χ. All these statements concern the original A-action, and the map intertwines multiplication by S. The conormal counterpart I2=(χ)/(χ²) is identified in precisely the same way with A/(χ).

Their exact annihilators, proved on the cyclic generator [χ], are

\[
 \operatorname{Ann}_A(I_N)=(\chi^\dagger),\qquad
 \operatorname{Ann}_A(I_2)=(\chi).
\]

Thus the natural A-action on IN factors through Aχ=A/(χ) iff (χ)⊆(χ†), equivalently χ†|χ. Equal degree and monicity make this equivalent to χ†=χ. This proves the exact obstruction to the original prose and the available quotient action A/(χ†)→End_C(IN). No abstract nonexistence of some unrelated Aχ action is asserted; the issue is the stated original S-action.

The exact replacement is: “On the two kernel C[S]-modules of the quotient maps to A_chi, the comparison map has an especially explicit description.” RF.15 then remains unchanged. Its right-hand module A/(χ†) and left-hand module A/(χ) both map to A/(g) as A-modules. The common target also has an Aχ action because g divides χ. That fact does not give the right-hand source an Aχ action.

Multiplication-by-χ is correctly described as a module parametrization, not silently treated as an algebra map with the ordinary product on A/(χ†). Its exact transported product is

\[
 [f]\mathbin\diamond[h]=[\chi f h]_{\chi^\dagger},\qquad
 \iota_N([f]\diamond[h])=[\chi f]\,[\chi h].
\]

This is well-defined because altering either representative by a multiple of χ† alters χfh by a multiple of χ†. The identity follows by reducing χ²fh modulo χχ†. It supplies the precise algebra relation to the earlier module parametrization. In the coprime case χ is invertible modulo χ†; the resulting unital algebra isomorphism from the ordinary product uses the additional inverse multiplier exhibited below.

## Exact common refinement

At a fixed λ, the moduli χ² and Nχ have orders 2aλ and aλ+bλ. Their gcd has order aλ+min(aλ,bλ), and their lcm has order aλ+max(aλ,bλ). This proves the formulas d=χg and ℓ=χ²χ†/g with every original multiplicity. Divisibility gives the intersection (χ²)∩(Nχ)=(ℓ). Bezout on the factors divided by d gives the sum (χ²)+(Nχ)=(d).

Consequently the diagonal map j:A/(ℓ)→A/(χ²)⊕A/(Nχ) is injective, and the difference map t([P],[Q])=[P−Q]d is a well-defined, surjective A-module map. If P−Q=χ²U+NχV, the exact lifting polynomial is

\[
 T=P-\chi^2U=Q+N_\chi V.
\]

It has residues P modulo χ² and Q modulo Nχ. This proves ker t=im j, including both signs. The image is closed under the componentwise algebra product because its two residues modulo d agree. Its unit is (1,1); j is therefore a unital algebra isomorphism onto that fibre product. The difference map is only a module map. Each projection followed by reduction modulo χ agrees because χ divides d. Every arrow commutes with multiplication by S.

On the kernel ideals, reduction to A/(χg) sends [χf] to the same residue; cancellation identifies its image (χ)/(χg) with A/(g). This gives RF.15 with both literal χ multipliers retained. Writing γ=deg g, the exact dimensions are deg d=q+γ, deg ℓ=3q−γ and deg d+deg ℓ=4q, agreeing with the proved sequence.

Locally write χ=(S−λ)^a Uλ with Uλ(λ)≠0. The original unit Uλ remains in the kernel parametrization. The Nχ block has length a+b and its kernel is generated by (S−λ)^a Uλ, of dimension b. The conormal block has length 2a and kernel dimension a; the common base has length a+min(a,b) and kernel dimension min(a,b). These formulas include original-only roots (b=0) and reflected-only roots (a=0) without deleting either sector. The quotient rings associated with an absent root have dimension zero.

## Mixed overlap: complete polynomial fixture

Take the specified k=2 and c=1. Put

\[
 A=S-(2+i),\quad B=S-i,\quad A=B-2,\quad\chi=A^2B.
\]

Reflection exchanges the two roots and gives

\[
 \chi^\dagger=AB^2,\quad g=AB,\quad N_\chi=A^3B^3,
 \quad d=A^3B^2,\quad\ell=A^4B^3.
\]

The original expanded polynomials, useful for checking coefficient signs, are

\[
 \chi=S^3-(4+3i)S^2+(1+8i)S+4-3i,
\]
\[
 \chi^\dagger=S^3-(2+3i)S^2+(-3+4i)S+2+i,
 \qquad g=S^2-(2+2i)S-1+2i.
\]

At 2+i the orders (a,b) are (2,1); at i they are (1,2). The original conormal lengths are therefore (4,2), the norm lengths (3,3), the common-base lengths (3,2), and the refinement lengths (4,3). The exact sequence has dimensions

\[
 0\longrightarrow\C^7\longrightarrow\C^6\oplus\C^6
   \longrightarrow\C^5\longrightarrow0.
\]

It is the concrete algebra isomorphism

\[
 \mathbb C[S]/(A^4B^3)\simeq
 \mathbb C[S]/(A^4B^2)\mathbin{\times}_{\mathbb C[S]/(A^3B^2)}\mathbb C[S]/(A^3B^3).
\]

For complete explicit lifting, let representatives P,Q satisfy P−Q=dR. The identity −A/2+B/2=1 gives

\[
 P-Q=\chi^2(-R/2)+N_\chi(R/2),\qquad
 T=P+\tfrac12R\chi^2=Q+\tfrac12RN_\chi.
\]

The two equality signs follow by substituting χ²=dA, Nχ=dB and A−B=−2. These formulas prove the mixed fibre-product inverse directly. Changing the input representatives changes its result only by the lcm ideal already calculated.

The norm kernel has coefficient module C[S]/(AB²), whereas the conormal kernel has C[S]/(A²B). Their common image has coefficient module C[S]/(AB). The original χ-action on the norm generator has exact remainder

\[
 \chi^2-N_\chi=A^4B^2-A^3B^3=-2A^3B^2=-2d.
\]

This is nonzero modulo Nχ because d has degree five and Nχ degree six. Therefore the norm kernel is not square-zero and its original action cannot factor through Aχ. But χ³=A^6B^3 is divisible by Nχ. The kernel has exact nilpotence index three; its square has dimension one, generated by the class of d. This is a partially overlapping reflected example with a nontrivial common kernel, rather than an example confined to the two extreme cases.

With root ordering (2+i,i) and raw derivative ordering (0,1,2) in each block, the raw-jet matrix on 1,S,…,S^5 has determinant

\[
 (0!1!2!)^2(i-(2+i))^{3\cdot3}=4(-2)^9=-2048.
\]

All derivative phases i^d and all entries d immediately below the S-action block diagonal are preserved by the coordinate map. The executed fixture checks these complete matrices and the reflected conjugate-linear matrix, not merely their dimensions.

## Disjoint reflected sectors and their exact local unit

Keep k=2, c=1 and the same A,B, but take χ=A². Then χ†=B² and g=1. The norm algebra is C[S]/(A²B²), the conormal algebra C[S]/(A⁴), the common base C[S]/(A²), and the refinement C[S]/(A⁴B²). Their respective lengths are four, four, two and six. The original root has (a,b)=(2,0); its reflected root has (0,2). The raw-jet determinant, with two derivatives at each root, is (−2)^4=16.

The exact Bezout polynomials, denoted U,V here to distinguish them from the spectral coordinate u, are

\[
 U=(B+1)/4=(S+1-i)/4,\qquad
 V=(3-B)/4=(3-S+i)/4.
\]

Direct multiplication gives U A²+V B²=1. Consequently

\[
 e_{\rm ref}=[UA^2]_{A^2B^2},\qquad
 [P]\longmapsto([P]_{A^2},[P]_{B^2}),
\]

and the inverse of this CRT map sends (a,b) to [aVB²+bUA²]. Reducing the displayed expression modulo each factor proves both residues and hence the inverse. The element e_ref has coordinates (0,1), so is nonzero and idempotent. Its explicit polynomial is

\[
 UA^2=\tfrac14S^3-\tfrac34(1+i)S^2
             +(-\tfrac34+\tfrac32i)S+\tfrac74+\tfrac14i.
\]

The reflected kernel ideal has its own unit e_ref. Its unital algebra isomorphism from the ordinary ring C[S]/(B²) is [b]↦[UA²b]; it is the RF.10 module parametrization composed with multiplication by U. The element U is the inverse of χ modulo χ†. This proves the exact connection between the two types of maps.

The kernel is not nilpotent: it contains the nonzero idempotent e_ref, whose every positive power is itself. Projection to the original Aχ sends this idempotent to zero. Attaching the original support label λ0 sends (λ0,e_ref) to (λ0,0), while τ maps to τ. The nonzero source value, its supported-zero image and the external point remain in their specified domains.

## Reflection-stable pair and fixed-root cases

For χ=A²B², reflection preserves both orders, χ†=χ and g=χ. Now Nχ=d=ℓ=χ²=A⁴B⁴. The fibre product is the diagonal algebra C[S]/(χ²) over itself. Its norm and conormal kernels agree and have square zero. Their generators are nonzero since deg χ<deg χ². With four raw derivatives at each root, the determinant is

\[
 (0!1!2!3!)^2(-2)^{4\cdot4}=144\,65536=9437184.
\]

The additional fixed-root example χ=(S−(1+3i))³ has q=3 and is also dagger-stable because 2−overline(1+3i)=1+3i. Here ψ=(u−3)³, Π=(u−3)^6 and

\[
 \Psi N_\chi=i^6\Pi=-\Pi.
\]

This odd-degree example checks the phase even when all roots are fixed by reflection. The raw-jet block has length six and determinant 0!1!2!3!4!5!=34560. Both kernel ideals have square zero and nonzero generator. None of these examples is asserted to be an actual zeta-zero packet.

The source assumes q≥1. Hence both degree-q quotient algebras in the disjoint case are nonzero, making e_ref nonzero. The stable and coprime alternatives cannot occur simultaneously under these hypotheses: g=χ and g=1 would imply χ=1, contradicting q≥1. The excluded constant case is not silently included in the claim that the reflected idempotent is nonzero.

## Actual exact computation and its scope

The companion `endpoint_reflected_relation_fixtures_20260913.py` executed with SymPy 1.14.0 in ordinary Python mode and completed **106 checks, zero failures**. It uses exact rational and Gaussian-rational coefficients and explicit failures rather than assertions. No floating-point integration, compiler, Lean, arithmetic packet realization, or zero-location test is involved. No optimized-mode execution is claimed.

For each of the four fixtures, it builds all quotient residue matrices on the original monomial bases, the full raw derivative matrices, the coordinate substitution and inverse matrices, the original S multiplication matrices and the conjugate-linear reflection matrix. It checks RF.10 ranks and zero composition; RF.13 injectivity, surjectivity, zero composition and dimensions; the unit and S-action of the fibre-product algebra map; both original arithmetic reductions; the literal RF.15 χ-multiplier diagrams; square-zero and exact nilpotence where applicable; and the product transported by the RF.10 parametrization. The disjoint case additionally checks the actual Bezout identity, complete CRT inverse and nonzero idempotent residues. The nonreal degree-two test polynomial checks the pointwise relation-norm identity without dropping conjugation.

The full result is `endpoint_reflected_relation_fixtures_20260913.json`, SHA-256 `d9b06e8c0b878cc62f3fc93fcee77eafc1178d480303f652e8efc4b5d35bbab7`. It records each fixture’s expanded original-coordinate polynomials, root orders, dimensions, raw determinant and kernel-square remainder, together with every named result and the exact executed checker/source hashes. The source remains at the reviewed pre-correction hash above. A later prose repair requires a separate final-source comparison; these execution records must retain the source edition actually inspected.

The one concrete typing defect has an exact proved repair and explicit counterexamples. No correction to RF.1–RF.17’s displayed formulas, leading phases, derivative signs, kernel moduli, gcd/lcm multiplicities, CRT inverse, or supported-zero map was found.

## Exact reflected semilinear identification of the two kernels

There is also a direct bijection between the coefficient modules after retaining the reflected scalar action. This observation was supplied by the independent reviewer after the review above. Define

\[
 F:I_2\longrightarrow I_N,\qquad
 F([\chi f]_{\chi^2})=[\chi f^\star]_{\chi\chi^\dagger}.
\]

If two representatives χf and χg agree modulo χ², then χ divides f−g. Applying ★ makes χ★=(−1)^qχ† divide (f−g)★. Multiplication by χ therefore gives the same residue modulo χχ†, proving well-definedness. Conversely define

\[
 G:I_N\longrightarrow I_2,\qquad
 G([\chi h]_{\chi\chi^\dagger})=[\chi h^\star]_{\chi^2}.
\]

Agreement in the first domain means χ† divides the coefficient difference; its ★ image is divisible by (χ†)★=(−1)^qχ, so the second residue is independent of that difference. Applying ★ twice yields GF=id and FG=id, including every original factor χ. Both maps preserve addition and conjugate complex scalars. For the actual polynomial action,

\[
 F(p(S)[\chi f])=[\chi (pf)^\star]
   =p^\star(S)F([\chi f]),\qquad
 F M_S=(kI-M_S)F.
\]

Thus F is the exact reflected semilinear identification; RF.13–RF.15 give the separate C[S]-linear common refinement with the unreflected S-action. This proves a precise additional relation even when χ†≠χ prevents the original action on IN from factoring through Aχ. It does not assign an algebra isomorphism to F: in the mixed example every product within I2 is zero, while the square of the cyclic generator in IN is the explicitly nonzero −2d. The correct multiplicative structure for the IN coefficient parametrization is the diamond product proved above.

On the labelled carriers F has the lift τ↦τ and (λ0,x)↦(λ0,Fx). It preserves labelled addition and satisfies the exact scalar law F(αx)=overlineαF(x). This is a conjugate-linear fibre map, with the same external and supported-zero values retained. No complex-linearity claim is made for this lifted semilinear map.
