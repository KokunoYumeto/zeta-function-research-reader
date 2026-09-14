# Independent review of the reflected relation and conormal refinement

The complete standalone source `work/endpoint_reflected_relation_fibre_product_20260913.tex`, RF.1–RF.17, was read directly at SHA256 `1acac595a7f89229569b8e28f63981bce4e072c623b39266af038a6b70671d52`. This review concerns its mathematical types, signs, constants, ideals, raw jets, kernel actions and support map. No source edits, compilation, PDF inspection or regression-checker reruns were performed.

There is one concrete prose defect at line 264, immediately before RF.15: “On the two kernel modules over A_chi” assigns a quotient-module structure that the norm kernel does not generally possess with its stated action. Both are modules over C[S]. The conormal kernel factors through A_chi; the norm kernel factors through A_(chi-dagger). Its natural polynomial action factors through A_chi exactly in the dagger-stable case. The precise proof and a counterexample appear below. The coordinating reviewer had already identified this defect; this independent reading confirms it. No additional mathematical defect was found in RF.1–RF.17. Every displayed formula and exact sequence is valid with the written hypotheses.

## RF.1–RF.4: involution, monic phase, and unchanged coordinates

Write `A=C[S]`, fix the actual integer k≥1 and c=k/2, and let χ be monic of degree q≥1. Coefficient conjugation acts antilinearly and fixes S. Since k is real,

`(f★)★(S) = overline(overline f(k−(k−S))) = f(S)`

and `(fg)★=f★g★`. The leading coefficient of `overlineχ(k−S)` is `(−1)^q`. Hence `χ†=(−1)^q χ★` is monic of degree q. Applying the same degree-q construction twice gives `(χ†)†=χ`. Also `(χ†)★=(−1)^q χ`, so

`(χχ†)★=χ★(χ†)★=(−1)^q χ† (−1)^q χ=χχ†`.

The coordinate map `Ψ:A→C[u]`, `Ψf=f(c+iu)`, is a complex algebra isomorphism. Its inverse is exactly substitution `u=(S−c)/i`. In particular this is an invertible change of the same polynomial; it does not discard the original real translation c or the complex factor i. The leading coefficient of Ψχ is `i^q`; therefore `ψ=i^(−q)Ψχ` is monic.

Coefficient conjugation in the target gives

`overline(Ψf)(u)=overline f(c−iu)=Ψ(f★)(u)`.

Thus `Ψχ★=(−i)^q overlineψ`, and multiplication by `(−1)^q` gives `Ψχ†=i^q overlineψ`. Multiplying by `Ψχ=i^qψ` yields the exact phase

`ΨN_χ = i^(2q) ψ overlineψ = (−1)^q ψ overlineψ`.

The factor `i^(2q)` is essential: the original norm polynomial N_χ evaluated on the spectral line can carry this sign. The real-u positive weight is `Π=ψ overlineψ`, not an unphased evaluation of N_χ. Π is monic of degree 2q, its coefficient conjugate equals itself by commutativity of the product, and Π(u)=|ψ(u)|² for real u.

Since Ψ is injective and `i^q≠0`, `χ†=χ` is equivalent to `overlineψ=ψ`. Substituting the definition of χ† proves the middle condition of RF.4 including `(−1)^q`. Under those equivalent conditions, `N_χ=χ²` and `Π=ψ²` follow by multiplication, with the original coordinate phase still present in ΨN_χ.

## RF.5: exact relation norm

For the specified polynomial Q, `Qtilde=ΨQ` retains all its coefficients under the stated coordinate substitution. Because Ψ is multiplicative,

`Ψ(χQ)=i^q ψ Qtilde`.

Taking the pointwise modulus on the real u axis gives `|i^q|² |ψ|² |Qtilde|²=Π |Qtilde|²`. Integrating both sides against the same original arithmetic density proves RF.5. It uses neither division by total mass nor a new measure. Polynomial integrability is the already stated arithmetic-source hypothesis, so the source norm and the transformed norm are both defined. This is a norm identity and an exact multiplication-operator conjugacy, not a growth bound for the quotient metric.

## RF.6–RF.9: reflected root multiplicities and raw-jet algebra

Let `a_λ=ord_λχ`, with value zero at unselected points. Factoring χ and applying its definition gives

`χ†(S)=(−1)^q ∏_α(k−S−overlineα)^(a_α)=∏_α(S−(k−overlineα))^(a_α)`.

Every one of the q reflected-factor minus signs has cancelled the explicit `(−1)^q`. Thus `b_λ=ord_λχ†=a_(k−overlineλ)` and `r_λ=a_λ+b_λ`. The reflected map is an involution on roots, so `Σa_λ=Σb_λ=q` and `Σr_λ=2q` even when original and reflected roots coincide.

Since `ΨN_χ=i^(2q)Π`, Ψ maps `(N_χ)` onto `(Π)` as ideals; the constant is a unit. It therefore induces RF.7, and substitution by Ψ inverse induces its inverse. There is no requirement to choose a square root or to assert dagger stability for this quotient comparison.

For each λ with r_λ>0, the raw-derivative block has coordinates d=0,…,r_λ−1. A polynomial has all those derivatives zero exactly when its Taylor polynomial begins at power r_λ of `(S−λ)`. Distinct root factors are coprime, so the common jet kernel is exactly `(N_χ)`. The source quotient and the direct sum of raw blocks both have dimension 2q. The induced map is therefore an algebra isomorphism with the block multiplication

`(v·w)_d=Σ_(j=0)^d binom(d,j) v_j w_(d−j)`.

The binomial factors are required because the coordinates are raw derivatives, not divided derivatives. The unit in a block is `(1,0,…,0)`. One can make the inverse entirely explicit without altering these coordinates: put `n_λ=N_χ/(S−λ)^(r_λ)`, let `t_λ` be the polynomial truncation of the Taylor series of `1/n_λ` at λ through degree r_λ−1, and set `e_λ=[n_λ t_λ]_(N_χ)`. Then

`J_N^(−1)(v) = [Σ_λ n_λ t_λ Σ_(d=0)^(r_λ−1) v_(λ,d)(S−λ)^d/d!]_(N_χ)`.

At λ, `n_λt_λ` is one modulo `(S−λ)^(r_λ)`; at every other root its jet is zero to the full required order. The inner Taylor polynomial has exactly the prescribed raw derivatives. These statements prove the inverse and retain all factorials and complete root orders.

For `ζ_λ=(λ−c)/i`, differentiating `P(c+iu)` exactly d times gives `(ΨP)^(d)(ζ_λ)=i^dP^(d)(λ)`. Differentiating SP gives `(SP)^(d)(λ)=λP^(d)(λ)+dP^(d−1)(λ)`, with the missing term set to zero at d=0. Thus RF.9 and the stated block M_S action preserve the full nilpotent chain and all phase factors.

The reflected raw-jet action can also be verified explicitly. If `λ*=k−overlineλ`, then

`(f★)^(d)(λ)=(−1)^d overline(f^(d)(λ*))`, and `ζ_(λ*)=overlineζ_λ`.

Multiplication by `i^d` from RF.9 turns the first expression into `(−i)^d overline(f^(d)(λ*))`, which is the coefficient conjugate of the corresponding u-coordinate raw derivative. Hence the coordinate and reflection maps intertwine exactly. This verifies the dagger phase at every jet order, not only at the roots themselves.

## RF.10–RF.11: the two precise kernel actions

The norm quotient is `A_N=A/(χχ†)`, and reduction modulo χ defines the surjective algebra homomorphism `π_N:A_N→A_χ`. Its kernel is the ideal `I_N=(χ)/(χχ†)`. The map

`iota_N:A/(χ†)→I_N`, `[f]↦[χf]`

is well-defined because adding a multiple of χ† changes χf by a multiple of N_χ. If its value is zero, divisibility `χχ† | χf` and cancellation in the polynomial domain imply `χ† | f`. Every kernel element has a representative divisible by χ. These facts prove injectivity, surjectivity onto the kernel and RF.10 as a C[S]-module sequence.

The corresponding conormal quotient is `A_2=A/(χ²)`, with kernel `I_2=(χ)/(χ²)`. The same cancellation proves the C[S]-module isomorphism `A/(χ)→I_2`, `[f]↦[χf]`, and RF.11. Both kernel dimensions are q. Neither multiplication-by-χ parametrization is asserted to be a unital algebra map.

Their annihilators for the original polynomial action are exactly

`Ann_A(I_N)=(χ†)`, and `Ann_A(I_2)=(χ)`.

For example, a polynomial p annihilates I_N precisely when it annihilates its cyclic generator [χ], equivalently when `χχ† | pχ`, equivalently `χ† | p`. Thus I_2 is naturally an A_χ-module. I_N is naturally an A_(χ†)-module. Its given A action descends to A_χ if and only if `(χ)⊆(χ†)`, meaning `χ† | χ`. Because their degrees and leading coefficients agree, this is equivalent to `χ†=χ`. The line before RF.15 must state both kernel modules are C[S]-modules, with the respective quotient actions specified if desired. This proves the strongest exact quotient-action criterion underlying the correction.

## RF.12–RF.15: gcd/lcm fibre product and complete local multiplicities

Put `g=gcd_monic(χ,χ†)`. Its order at λ is `min(a_λ,b_λ)`. The two defining ideals in RF.13 are `(χ²)` with order 2a_λ and `(χχ†)` with order a_λ+b_λ. Their gcd and lcm therefore have respective orders

`min(2a_λ,a_λ+b_λ)=a_λ+min(a_λ,b_λ)`,

`max(2a_λ,a_λ+b_λ)=a_λ+max(a_λ,b_λ)`.

These are exactly `d=χg` and `ell=χ²χ†/g`. There is no root deletion or repeated-root truncation in these polynomials. Divisibility gives `(χ²)∩(N_χ)=(ell)`. Dividing by d and applying the Euclidean algorithm to the remaining coprime factors gives `(χ²)+(N_χ)=(d)`.

The map `j:A/(ell)→A_2⊕A_N`, `[P]↦([P],[P])`, is therefore well-defined and injective. The difference map `t([P],[Q])=[P−Q]_(d)` is well-defined since d divides both moduli, and is surjective since `t([P],0)=[P]`. If `t([P],[Q])=0`, choose A,B with `P−Q=χ²A+N_χB`. Then the exact sign choice

`T=P−χ²A=Q+N_χB`

gives `j[T]=([P],[Q])`. This proves exactness directly. The kernel consists of pairs whose reductions to A/(d) agree; its componentwise product and unit agree with j. Hence j is a unital algebra isomorphism onto the stated fibre product. The map t is a C[S]-module map; it is not incorrectly labelled an algebra map.

Because χ divides d, the two fibre-product projections followed by the original arithmetic reduction modulo χ agree. Every residue map, multiplication-by-χ map, diagonal map and difference map commutes with M_S by multiplying its representative by S. Thus the action comparison in the theorem is exact, including nilpotent actions.

The kernel comparison in RF.15 follows with its original multiplication factors. The image of either kernel in A/(χg) is `(χ)/(χg)`. Cancellation gives its C[S]-module isomorphism `A/(g)→(χ)/(χg)`, `[f]↦[χf]`. Consequently the two domain parametrizations induce the ordinary quotient maps `A/(χ)→A/(g)←A/(χ†)`. No A_χ action on the second domain is needed or generally available.

For explicit local multiplicities, put x=S−λ and factor `χ=x^(a_λ)u_λ` with u_λ a local unit. Then the norm block is `C[x]/(x^(a_λ+b_λ))`, and its kernel is the ideal generated by `x^(a_λ)u_λ`; its dimension is b_λ. The conormal block is `C[x]/(x^(2a_λ))`, with kernel dimension a_λ. The common base block has length `a_λ+min(a_λ,b_λ)`; its kernel has dimension `min(a_λ,b_λ)`. Both coefficient maps in RF.15 reduce to the corresponding truncated block of that last length. The multiplier u_λ is the original nonzero factor from χ and remains in the multiplication-by-χ parametrization.

Writing γ=deg g, one also obtains `deg d=q+γ`, `deg ell=3q−γ`, and `(3q−γ)+(q+γ)=4q=dim(A_2⊕A_N)`. These dimensions agree with the exact sequence; they are a consequence of the fully proved ideal maps, not a substitute for them.

## Square-zero criterion and RF.16's reflected local unit

The conormal ideal squares to zero because every product contains χ². The norm ideal squares to zero only if its element [χ] has square zero. That condition is `χχ† | χ²`, which by cancellation gives `χ† | χ`; equal degree and monicity then force χ†=χ. Conversely that equality makes every product of two norm-kernel elements divisible by N_χ=χ². This proves the stated iff and agrees exactly with the quotient-action criterion above.

For g=1, let U,V denote the polynomials called u,v in the source's Bezout identity, so `Uχ+Vχ†=1`. This notation in the review keeps their type separate from the spectral coordinate u. The CRT map to `A_χ×A_(χ†)` has exact kernel `(χ)∩(χ†)=(N_χ)`. For representatives a,b, its inverse sends the pair to

`[a Vχ†+b Uχ]_(N_χ)`.

Modulo χ, the first coefficient Vχ† is one and the second summand vanishes. Modulo χ†, the first summand vanishes and Uχ is one. This proves the inverse and all signs. The reflected element `e_ref=[Uχ]` therefore has coordinates `(0,1)`, is nonzero, and satisfies `e_ref²=e_ref`.

The reflected kernel ideal is exactly the second CRT factor. Its unital algebra isomorphism is

`A_(χ†)→I_N`, `[b]↦[Uχ b]`, with `[1]↦e_ref`.

This multiplicative map is related to the earlier C[S]-module parametrization by the invertible multiplier U modulo χ†: it is `iota_N` composed with multiplication by [U]. Indeed [U] is the inverse of [χ] modulo χ†. Thus the ordinary product of A_(χ†) is not silently assigned to the map `[f]↦[χf]`. The source's explicit CRT inverse already supplies the correct unital map. Renaming the source Bezout polynomials U,V, or writing u(S),v(S), would be an optional clarity improvement; their existing declaration as polynomials is sufficient to identify the intended type.

## Explicit counterexample to the uncorrected module prose

This is a declared polynomial fixture, not an assertion about actual zeta zeros. Take k=2, c=1, q=1, and `χ(S)=S−(2+i)`. Reflection gives `χ†(S)=S−i`; these two factors are disjoint. In A_N, the nonzero element x=[χ] satisfies

`χ=χ†−2`, hence `χ·x=[χ²]=[χχ†−2χ]=−2x≠0`.

But χ represents zero in A_χ. Its original polynomial action on I_N therefore cannot factor through A_χ. This supplies a direct counterexample to the line before RF.15, with the exact nonzero action calculated.

The same fixture checks the original reflection phase without removing the c translation:

`Ψχ = −1+i(u−1)=i(u−1+i)`, `ψ=u−1+i`, `overlineψ=u−1−i`,

`Ψχ†=1+i(u−1)=i overlineψ`, and `ΨN_χ=−[(u−1)²+1]`.

Thus `Π=(u−1)²+1` is the actual positive relation-norm factor. The Bezout choice `U=−1/2`, `V=1/2` gives `e_ref=−[χ]/2`; the computed relation x²=−2x yields `e_ref²=e_ref`. All these relations agree with RF.3, RF.5, RF.10 and RF.16 while disproving only the broader base-module assertion.

## RF.17: the exact supported-zero map

For a fixed original support label λ_0, the relevant carrier is `{τ} ⊔ ({λ_0}×E)`. A linear map L:E→F induces the stated map `τ↦τ`, `(λ_0,x)↦(λ_0,Lx)`. Evaluation on τ and on each labelled vector proves functoriality. Within a labelled fibre, linearity gives preservation of vector addition and scalar action.

For any of the explicitly specified quotient or difference maps, a vector in its kernel is sent to the zero vector in its target, so its labelled image is `(λ_0,0)`. This does not change the vector's original source value. In the disjoint CRT case, `π_N(e_ref)=0` whereas `e_ref≠0`; hence its labelled image is supported zero and its external τ input remains external τ. These values are related by the actual quotient map, with their domains and multiplicative roles retained.

## Independent cross-check and conclusion

A second independent algebra reader checked RF.10–RF.16 at the same source hash. It confirmed the gcd/lcm root orders, exact lifting polynomial T, the square-zero iff criterion, the reflected ideal's unital map and the same RF.15 module-typing defect. It found no additional mathematical error and performed no source edits or checker/compiler reruns.

The proof is mathematically valid after correcting the single identified prose attribution of both kernels to A_χ-modules. The displayed maps themselves already have the correct C[S]-module types. The comparison retains all original root orders, coordinate phases, raw derivative factorials, reflected factors, kernel actions, local algebra unit and supported zero.
