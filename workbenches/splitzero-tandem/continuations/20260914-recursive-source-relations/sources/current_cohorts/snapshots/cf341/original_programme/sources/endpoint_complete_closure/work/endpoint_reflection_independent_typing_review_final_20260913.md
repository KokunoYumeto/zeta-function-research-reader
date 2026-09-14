# Final independent review of reflected relation kernels and every ideal power

The entire revised standalone source `work/endpoint_reflected_relation_fibre_product_20260913.tex`, all 489 lines and RF.1–RF.26, was read directly at SHA256 `0847a516e883e7814c414f4c1bc26abfc2dd4f8493b0aac384b109888c5dc749`. This final review validates the original reflection/jet/fibre-product construction, the corrected module wording, the explicit reflected semilinear maps, the transported product, every ideal-power dimension, the exact nilpotence index, the persistent full local algebras and the mixed-case lift.

No unresolved mathematical defect was found. The previously identified prose defect immediately before RF.15 is corrected in this source: both kernels are now described as C[S]-modules of the quotient maps to A_chi. RF.18 further supplies their exact annihilators and the precise criterion for the norm kernel's original action to factor through A_chi. The new conjugate-linear reflection map and the linear gcd/lcm refinement retain their respective action laws and domains.

The historical review `work/endpoint_reflection_independent_typing_review_20260913.md` is preserved unchanged at SHA256 `2af9df8b95cfd8cd5bd69f158eb7f4e16a489ae97092f3b52dc326aa77405dfd`. The full verified calculations for RF.1–RF.17 are included again below with the resolved wording; this final report does not require the historical report to supply their proofs. A separate independent algebra reader checked RF.21–RF.26 at the same revised source hash. No proof file was edited, and no compiler, mathematical checker, or PDF QA was run by this review. The coordinating agent owns the independent finite-fixture extensions and their execution records; no claim about those executions is made here.

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

For example, a polynomial p annihilates I_N precisely when it annihilates its cyclic generator [χ], equivalently when `χχ† | pχ`, equivalently `χ† | p`. Thus I_2 is naturally an A_χ-module. I_N is naturally an A_(χ†)-module. Its given A action descends to A_χ if and only if `(χ)⊆(χ†)`, meaning `χ† | χ`. Because their degrees and leading coefficients agree, this is equivalent to `χ†=χ`. The corrected line before RF.15 now states exactly that both kernels are C[S]-modules of the quotient maps to A_chi. RF.18 additionally proves their respective annihilators and the exact condition for descent of the original action. This closes the historical prose defect and proves the strongest exact quotient-action criterion underlying its correction.

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

## Explicit counterexample documenting the corrected historical module prose

This is a declared polynomial fixture, not an assertion about actual zeta zeros. Take k=2, c=1, q=1, and `χ(S)=S−(2+i)`. Reflection gives `χ†(S)=S−i`; these two factors are disjoint. In A_N, the nonzero element x=[χ] satisfies

`χ=χ†−2`, hence `χ·x=[χ²]=[χχ†−2χ]=−2x≠0`.

But χ represents zero in A_χ. Its original polynomial action on I_N therefore cannot factor through A_χ. This supplies a direct counterexample to the historical wording before RF.15, with the exact nonzero action calculated; the revised source has corrected that wording.

The same fixture checks the original reflection phase without removing the c translation:

`Ψχ = −1+i(u−1)=i(u−1+i)`, `ψ=u−1+i`, `overlineψ=u−1−i`,

`Ψχ†=1+i(u−1)=i overlineψ`, and `ΨN_χ=−[(u−1)²+1]`.

Thus `Π=(u−1)²+1` is the actual positive relation-norm factor. The Bezout choice `U=−1/2`, `V=1/2` gives `e_ref=−[χ]/2`; the computed relation x²=−2x yields `e_ref²=e_ref`. All these relations agree with RF.3, RF.5, RF.10 and RF.16 while disproving only the broader base-module assertion.

## RF.17: the exact supported-zero map

For a fixed original support label λ_0, the relevant carrier is `{τ} ⊔ ({λ_0}×E)`. A linear map L:E→F induces the stated map `τ↦τ`, `(λ_0,x)↦(λ_0,Lx)`. Evaluation on τ and on each labelled vector proves functoriality. Within a labelled fibre, linearity gives preservation of vector addition and scalar action.

For any of the explicitly specified quotient or difference maps, a vector in its kernel is sent to the zero vector in its target, so its labelled image is `(λ_0,0)`. This does not change the vector's original source value. In the disjoint CRT case, `π_N(e_ref)=0` whereas `e_ref≠0`; hence its labelled image is supported zero and its external τ input remains external τ. These values are related by the actual quotient map, with their domains and multiplicative roles retained.

## RF.18–RF.20: complete reflected kernel isomorphisms and scalar laws

The annihilators in RF.18 agree with the exact cancellation proof above: I_2 has annihilator (χ), and I_N has annihilator (χ†), for their unchanged C[S] actions. In particular the sentence about descent to A_chi refers to the existing polynomial action, rather than claiming that no separately transported module action could ever be defined.

The map F in RF.19 uses the coefficient parametrizations of the two kernel modules:

`F:I_2→I_N`, `F([χf]_(χ²))=[χ f★]_(N_χ)`.

If `[χf_1]=[χf_2]` modulo χ², cancellation gives χ dividing `f_1−f_2`. Applying star changes this divisibility to χ★ dividing `(f_1−f_2)★`; because χ★=(−1)^qχ†, it is equivalent to χ† dividing that difference. Multiplication by the unchanged χ then makes the two F images equal modulo N_χ. This proves well-definedness with the real phase `(−1)^q` retained as an invertible factor, not silently changing the defining polynomial.

For G, equality `[χh_1]=[χh_2]` modulo N_χ gives χ† dividing `h_1−h_2`. Its star image is divisible by `(χ†)★=(−1)^qχ`, so multiplication by χ makes the images equal modulo χ². Thus

`G:I_N→I_2`, `G([χh]_(N_χ))=[χ h★]_(χ²)`

is well-defined. Choosing the indicated coefficient representatives in the compositions gives

`GF([χf])=[χ(f★)★]=[χf]`, and `FG([χh])=[χ(h★)★]=[χh]`.

No reflection is being applied to the leading χ in these definitions; the map applies star to the coefficient parameter. This is why the inverse compositions have exactly the displayed sign and no extra `(−1)^q` scalar.

Star preserves addition and sends αf to `overlineα f★`. Therefore F and G are additive, conjugate-linear bijections. For any p∈C[S], the coefficient representative for p·[χf] is pf, and `(pf)★=p★f★`. Hence

`F(p(S)x)=p★(S)F(x)`.

Taking p=S gives S★=k−S and exactly `F M_S=(kI−M_S)F`. Taking p=α gives `F(αx)=overlineαF(x)`. The inverse G has the same reflected polynomial law by the same calculation. These are the full semilinear action identities. Neither F nor G is called a complex-linear C[S]-module isomorphism.

The labelled F map sends τ to τ and `(λ_0,x)` to `(λ_0,Fx)`. It preserves fibre addition and satisfies the reflected scalar law just established. Thus the new paragraph does not incorrectly apply RF.17's complex-linear scalar law to a conjugate-linear map. The original support label and external point remain fixed.

## RF.21: the actual coefficient product and its exact algebra map

The coefficient module A/(χ†) parametrizes the ideal I_N through iota_N. Its product transported from that ideal is

`[f] ⋄ [h] = [χfh]_(χ†)`.

Changing f by χ†a changes χfh by χ†(χah), and the same statement holds for h; therefore ⋄ is well-defined. It is complex bilinear and commutative. Direct substitution shows associativity:

`([f]⋄[h])⋄[j] = [χ²fhj] = [f]⋄([h]⋄[j])` modulo χ†.

The map iota_N obeys

`iota_N([f]⋄[h])=[χ²fh]_(N_χ)=[χf]_(N_χ)[χh]_(N_χ)`.

Together with its proved linear bijectivity, this is the exact algebra identification of the coefficient module equipped with ⋄ and the original ideal equipped with its actual product. It does not equip the ordinary quotient product on A/(χ†) with an unjustified algebra-map claim. In particular [1] need not be an identity for ⋄. When χ is invertible modulo χ†, the inverse class [χ]^(−1) is the ⋄ identity and maps to the CRT local unit described in RF.16. In the dagger-stable case, χ is zero modulo χ†, so ⋄ is identically zero, in agreement with the square-zero ideal.

The source explicitly refrains from assigning an algebra-isomorphism property to F. Indeed I_2 always has zero product, whereas I_N may have nonzero products; RF.19 and RF.20 specify the precise semilinear vector-space and action relation instead. The fibre product RF.14 remains the simultaneous algebra refinement.

## RF.22: every power with all original root orders

As an ideal of A_N, `I_N=(χ)/(N_χ)`. Its t-th algebraic ideal power is therefore the image of `(χ^t)`, for every integer t≥1. Under the full CRT algebra isomorphism, fix the original root λ, let z=S−λ, write a=a_λ and b=b_λ, and keep the original factor

`χ=z^a U_λ`, with `U_λ(λ)≠0`.

The actual block is `R_λ=C[S]/((S−λ)^(a+b))`. The class of U_λ is a unit: write it as `u_0+n` with u_0≠0 and n nilpotent, and use the finite inverse `u_0^(−1)Σ_j(−n/u_0)^j` through the nilpotence length. The original generator of the power is `z^(ta)U_λ^t`. Multiplication by the explicit invertible class U_λ^(−t) proves the equality of its generated ideal with `(z^(ta))`. This relates the original generator to the convenient basis without deleting the original factor or replacing the algebra.

If ta<a+b, the ideal has the independent basis `z^(ta),z^(ta+1),…,z^(a+b−1)`. If ta≥a+b, it is zero. The independence follows because monic division gives unique representatives with powers below a+b. Thus the exact block dimension is

`max(a+b−ta,0)=max(b−(t−1)a,0)`.

Summing over all distinct root blocks gives RF.22. For t=1 this sums to Σb=q, the dimension of I_N already proved by RF.10. At a=0<b the formula gives b for every t; at b=0<a it gives zero for every t≥1. Thus both one-sided root cases and all shared-root multiplicities are included in the formula.

## RF.23: nilpotence and its smallest exact exponent

If some reflected root has a=0<b, its block ideal is the whole nonzero R_λ for every t, so no power of I_N vanishes. Conversely suppose every b>0 has a>0. The b=0 blocks already vanish at t=1. In every remaining block, the exact vanishing condition is `ta≥a+b`, so its first zero power is

`ceil((a+b)/a)`.

There are finitely many blocks, and the index set b>0 is nonempty because q≥1. Taking the maximum of these exact thresholds is sufficient to annihilate every block. It is also necessary: if t is any smaller positive integer, at least one maximizing block has ta<a+b and remains nonzero by the displayed basis. Therefore RF.23 is the smallest exponent that kills the ideal, not merely an upper bound. Its denominators are positive precisely under the stated support condition. No expression with a=0 is evaluated.

This proves nilpotence if and only if every reflected root occurs among the original roots. The assertion concerns support inclusion, while the exact exponent retains the differing multiplicities. It does not equate support equality with χ†=χ. For the square-zero special case, the threshold is at most two precisely when b≤a at all roots. Since Σa=Σb=q, those inequalities force a=b at every root, reproducing the earlier dagger-stability criterion exactly.

## RF.24: persistent full local algebras and the actual idempotent

For each a>0 block, some finite threshold annihilates its ideal powers. A single finite t large enough for all such blocks therefore leaves only the blocks with a=0<b. In each of those blocks χ is a unit, so `(χ^t)=R_λ` for every t. Since the CRT decomposition is a finite algebra product, the intersection of all I_N^t is exactly the product of these unchanged full rings:

`I_N^infinity ≅ ∏_(a_λ=0<b_λ) C[S]/((S−λ)^(b_λ))`.

No radical quotient is taken. If b_λ>1, its nilpotent powers through order b_λ−1 remain in the persistent algebra. The isomorphism is the restriction of the original polynomial residue map, so the scalar action and multiplication-by-S action are the original ones in every retained block.

The local unit assertion also has a literal polynomial construction. Let

`N_ref=∏_(a_λ=0<b_λ)(S−λ)^(b_λ)`, and `N_vis=N_χ/N_ref`.

For a nonempty reflected-only set, N_ref and N_vis are coprime. Choose Bezout polynomials U_0,V_0 with `U_0 N_ref+V_0 N_vis=1`. Then

`epsilon_ref=[V_0 N_vis]_(N_χ)`

has residue one in every reflected-only full block and residue zero in all other full blocks. Hence `epsilon_ref²=epsilon_ref`; its ideal is exactly the persistent algebra, and it is the identity on that ideal. At a reflected-only root its complete raw jet is `(1,0,…,0)`, and at every other root it is the zero jet to the full order. All original χ factors occur in N_vis, so χ divides N_vis and `π_N(epsilon_ref)=0`. This proves the precise original quotient map behind the stated supported-zero image.

If the reflected-only set is empty, every positive-a block vanishes after a finite threshold, so the persistent ideal is zero. The source explicitly interprets the empty product as the zero algebra. The statement about a nonzero local unit is restricted to the nonempty case; no nonzero unit or reflected idempotent is claimed for the zero ideal.

## RF.25–RF.26: overlapping multiplicities and the representative-independent lift

Keep the original k=2 and c=1. Let `A=S−(2+i)` and `B=S−i`, so A=B−2. Reflection exchanges the two roots. With `χ=A²B`, the monic reflected polynomial is `χ†=AB²`: the order-two root reflects to i and the order-one root reflects to 2+i. Consequently

`g=AB`, `N_χ=A³B³`, `d=χg=A³B²`, and `ell=χ²χ†/g=A⁴B³`.

The exact product difference is

`χ²−N_χ=A⁴B²−A³B³=A³B²(A−B)=−2A³B²=−2d`.

It has degree five and is nonzero. Since N_χ has degree six, it cannot be divisible by N_χ. Thus [χ]² is nonzero in the norm algebra. Its cube is represented by A⁶B³, which is divisible by N_χ, so it is zero. The two root pairs (a,b) are (2,1) and (1,2); RF.22 therefore gives

`dim I_N=1+2=3`, `dim I_N²=0+1=1`, and `dim I_N³=0+0=0`.

Both roots are present in the original packet, so the persistent algebra is zero, while the exact nilpotence index is three. This retains the genuine distinction between square-zero and higher nilpotence without deleting either block.

For representatives with `P−Q=dR`, the displayed two formulas for T agree because

`(P+Rχ²/2)−(Q+RN_χ/2) = (P−Q)+R(χ²−N_χ)/2 = dR−dR=0`.

Thus `T=P+Rχ²/2=Q+RN_χ/2` reduces to P modulo χ² and Q modulo N_χ. The plus signs and the factor one-half are exactly correct.

The inverse map descends independently of representatives modulo ell. If P is replaced by `P+χ²U`, then R becomes `R+AU`, because χ²/d=A. The resulting T changes by

`χ²U+(AU)χ²/2 = χ²U(1+A/2)=χ²BU/2=ell U/2`.

If Q is replaced by `Q+N_χV`, then R becomes `R−BV`, because N_χ/d=B. With the first expression for T, its change is `−B Vχ²/2=−ell V/2`. Both changes are zero modulo ell. This proves directly that RF.26 is a well-defined inverse on the mixed fibre product, with the exact original moduli and all multiplication factors retained.

## Final validation and scope

The independent second algebra reader checked RF.21–RF.26 at the same final SHA256. It verified the transported product, every local ideal power, exact nilpotence thresholds, persistence of full reflected-only blocks, their local unit and zero quotient image, and both signs and representative changes in RF.26. Its conclusions agree with the complete direct reading and proofs above.

RF.1–RF.26 are mathematically valid as written at the pinned revised source. The historical module defect is closed. The new semilinear reflection maps do not replace the original C[S]-linear maps; their exact action laws are proved. The complete persistent algebra retains nilpotents and original multiplication-by-S, and its supported-zero image is obtained by the stated quotient. This review establishes polynomial-algebra claims and the existing literal relation-norm identity; it makes no zero-location, quotient-growth, interval-certificate, compiled-proof or PDF-layout claim.
