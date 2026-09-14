# Complete final review of RF.1–RF.26 and exact kernel-power fixtures

The complete 489-line source `endpoint_reflected_relation_fibre_product_20260913.tex`, including every definition, proof and equation RF.1–RF.26, was read directly at SHA256 `0847a516e883e7814c414f4c1bc26abfc2dd4f8493b0aac384b109888c5dc749`. Its complete diff against the original RF.1–RF.17 source was also read. No unresolved mathematical defect was found. The only previously reported typing defect is corrected at source lines 264–265, and RF.18–RF.20 now prove the corresponding annihilators and exact reflected kernel isomorphisms.

The full independent review `endpoint_reflection_independent_typing_review_final_20260913.md`, SHA256 `b5a5d4663b3724782a450bc1cd977cc340a34bf9bdd9d3bdd7f0aa94ea7c036b`, was read completely. It supplies an additional complete proof-level review of all RF.1–RF.26, including the inverse raw-jet map with factorials and the representative-independent RF.26 lift. Its conclusions agree with this review. It reports no compiler, fixture execution or PDF visual inspection; its scope is mathematical source review.

The following sections give the precise source comparison, complete mathematical verification and an additional mixed example with a persistent nonreduced local algebra. All polynomials are declared finite algebra fixtures. They are not asserted to be annihilators of any particular arithmetic packet.

## Exact source revision and preservation

The original RF.1–RF.17 source is retained byte-for-byte as `endpoint_reflected_relation_review_input_RF1_17_20260913.tex`, SHA256 `1acac595a7f89229569b8e28f63981bce4e072c623b39266af038a6b70671d52`. The new source is copied exactly to `endpoint_reflected_relation_review_input_RF1_26_20260913.tex`, SHA256 `0847a516e883e7814c414f4c1bc26abfc2dd4f8493b0aac384b109888c5dc749`. Reversing the new section and the single wording correction reconstructs the exact old-source hash. The complete textual change is retained in `endpoint_reflected_relation_revision_20260913.diff`.

The first change replaces “On the two kernel modules over A_chi” by “On the two kernel C[S]-modules of the quotient maps to A_chi”. The second inserts the full section “Reflected kernel transport and every power of the norm kernel”, RF.18–RF.26. There is no other source change. In particular RF.1–RF.17, the original coordinate phases, raw derivative products, exact gcd/lcm maps, and the unchanged arithmetic density in RF.5 are preserved.

The historical complete review remains at SHA256 `a8dfad53905dfb7742b403401a7d0850e776c071478dbbab2a8485a674c512cd`, and the historical independent typing review remains at SHA256 `2af9df8b95cfd8cd5bd69f158eb7f4e16a489ae97092f3b52dc326aa77405dfd`. The original checker remains at SHA256 `3e174144a5661ae608090c8568c529b5f562e086fceef72935532b5d82351ee1`, and its 106-pass ordinary-mode result remains at SHA256 `d9b06e8c0b878cc62f3fc93fcee77eafc1178d480303f652e8efc4b5d35bbab7`. That result is historical and refers to the earlier source hash. It has not been rerun, relabelled or overwritten.

## Reflection, coordinates and complete jets: RF.1–RF.9

Let the polynomial ring be R=C[S], fix k≥1, c=k/2, and take χ monic of degree q≥1. The involution f★(S)=bar f(k−S) is conjugate-linear and multiplicative, and squares to the identity because k is real. The leading coefficient of χ★ is (−1)^q. Thus χ†=(−1)^qχ★ is monic, has degree q, and satisfies (χ†)†=χ. In addition, (χ†)★=(−1)^qχ, and hence (χχ†)★=χχ†.

The original coordinate map Ψ(f)(u)=f(c+iu) has inverse F↦F((S−c)/i). Coefficient conjugation gives Ψ(f★)=overline(Ψf). With ψ=i^(−q)Ψχ, the exact formulas are Ψχ=i^qψ, Ψχ†=i^q barψ and ΨNχ=i^(2q)ψbarψ. The polynomial Π=ψbarψ is real and monic, and Π(u)=|ψ(u)|² for real u. Applying the injective map Ψ proves χ†=χ if and only if barψ=ψ, including the explicit (−1)^q condition in the original coordinate. The factor i^(2q) remains essential in the norm polynomial's original-coordinate evaluation.

For any polynomial Q, Ψ(χQ)=i^qψΨQ. Taking pointwise absolute squares on real u gives |Ψ(χQ)|²=Π|ΨQ|² because |i^q|²=1. Integration against the same original m_h,k gives RF.5. The stated arithmetic-source construction supplies polynomial integrability. This derivation changes neither the measure nor its total mass.

If a_λ=ord_λχ, reflection gives b_λ=a_(k−barλ). Indeed each factor k−S−barα contributes one minus sign, and all q such signs cancel the leading (−1)^q. The norm polynomial therefore has the full order r_λ=a_λ+b_λ, and Σr_λ=2q. The ideal map Ψ(Nχ)=i^(2q)Π induces the quotient algebra isomorphism RF.7 since its scalar factor is a unit.

For RF.8, the raw jets P^(d)(λ), 0≤d<r_λ, vanish precisely when every (S−λ)^(r_λ) divides P. The factors at distinct λ are coprime, so the common kernel is (Nχ). The induced map is injective between spaces of dimension 2q and hence bijective. The explicit inverse uses n_λ=Nχ/(S−λ)^(r_λ), the degree-(r_λ−1) Taylor truncation t_λ of 1/n_λ at λ, and the polynomial sum

`Σ_λ n_λ t_λ Σ_(d=0)^(r_λ−1) v_(λ,d)(S−λ)^d/d!` modulo Nχ.

At its own root each n_λt_λ is one to the entire required order, and it vanishes to the required orders at the other roots. This proves the inverse with every factorial retained. Leibniz's rule supplies the raw-block product Σ binom(d,j)v_jw_(d−j). Differentiating ΨP gives the factor i^d in RF.9, and differentiating SP gives λv_d+d v_(d−1). Reflection on these same raw jets is (P★)^(d)(λ)=(−1)^d overline(P^(d)(k−barλ)); since ζ_(k−barλ)=barζ_λ, the factor i^d carries this to conjugation of the corresponding u jets. All original multiplicities and operator coefficients agree.

## The two kernels and their exact common algebra refinement: RF.10–RF.18

Reduction modulo χ maps A_N=R/(χχ†) onto A_χ=R/(χ). Its kernel I_N is (χ)/(χχ†), parametrized by iota_N:R/(χ†)→I_N, [f]↦[χf]. Cancellation in the polynomial domain proves well-definedness and injectivity: χχ† divides χf exactly when χ† divides f. Every kernel residue has a multiple-of-χ representative, so this is onto. Likewise I_2=(χ)/(χ²) is isomorphic as an R-module to R/(χ), by the literal same multiplier χ. Both dimensions are q.

The exact annihilators are Ann_R I_N=(χ†) and Ann_R I_2=(χ). A polynomial annihilates either cyclic module exactly when it kills its generator [χ]; polynomial cancellation gives the respective defining polynomial. Consequently the existing R-action on I_N descends to A_χ precisely when χ† divides χ, hence precisely when χ†=χ by equal degree and monicity. The corrected wording before RF.15 and RF.18 state exactly this criterion. An unrelated transported action is not being confused with the original multiplication-by-S action.

Let g=gcd_monic(χ,χ†), d=χg, and ℓ=χ²χ†/g. At every root their orders are a+min(a,b) and a+max(a,b). Thus (χ²)+(Nχ)=(d) by Bezout after dividing by the gcd, and (χ²)∩(Nχ)=(ℓ) by rootwise divisibility. The map j:R/(ℓ)→A_2⊕A_N, [P]↦([P],[P]), is injective. The R-linear difference map t([P],[Q])=[P−Q]_d is well-defined and onto. If P−Q=χ²U+NχV, then T=P−χ²U=Q+NχV maps to the pair. This proves exactness and supplies the inverse onto the fibre product.

The image is closed under componentwise multiplication and has the same unit, so j gives the stated algebra isomorphism A_2×_(R/d)A_N. The two maps to A_χ agree because χ divides d. All residue maps, the literal χ injections, j, and t commute with multiplication by S. The induced kernel maps are R/(χ)→R/(g)←R/(χ†), followed by the unchanged injection [f]↦[χf] into (χ)/(χg). The difference map is asserted to be an R-module map; the algebra assertion belongs to the diagonal injection and the fibre product.

I_2²=0 by its modulus χ². The condition I_N²=0 is equivalent to [χ]²=0, hence to χχ† dividing χ², hence to χ†=χ. For g=1, choose Uχ+Vχ†=1. The inverse CRT map sends (a,b) to [aVχ†+bUχ]_N, and e_ref=[Uχ] has residues (0,1). Thus e_ref²=e_ref, π_N(e_ref)=0, and its ideal is the full reflected factor. The unital algebra map R/(χ†)→I_N sends b to [Uχb], while the literal R-module parametrization sends f to [χf]. Their exact relation is multiplication by U, the inverse of χ modulo χ†. This identifies the two products without assigning the ordinary quotient multiplication to the wrong parametrization.

For a fixed support label λ_0, the carrier is {τ} disjoint-union ({λ_0}×E). The lift of a linear map L sends τ to τ and (λ_0,x) to (λ_0,Lx). Direct evaluation proves preservation of composition, fibre addition and scalar multiplication. A kernel vector maps to (λ_0,0), including the nonzero reflected idempotent under π_N. The original source vector and its receiving supported zero are related by that exact quotient map.

## Reflected semilinear transport and actual ideal product: RF.19–RF.21

The two coefficient parametrizations define F:I_2→I_N by [χf]_χ²↦[χf★]_N and G:I_N→I_2 by [χh]_N↦[χh★]_χ². In F, changing f by χr changes f★ by χ★r★=(−1)^qχ†r★, so the target χ multiple changes by a multiple of Nχ. In G, changing h by χ†r changes h★ by (−1)^qχr★, so the target changes by a multiple of χ². These prove both maps are well-defined. The two compositions are the identity because ★²=1 on the coefficient parameter. The initial multiplier χ is not reflected by either definition, so no extra phase occurs in the compositions.

For p∈R and x=[χf], F(px)=[χ(pf)★]=p★F(x). The special cases p=α and p=S give F(αx)=barαF(x) and FM_S=(kI−M_S)F. The identical argument gives the inverse law for G. The lifted map preserves τ and the original support label, adds fibre vectors, and conjugates scalar multiplication. These are the exact types of the bijections and operator intertwiners.

The product transported from I_N to its coefficient module R/(χ†) is [f]⋄[h]=[χfh]_χ†. Changing either representative by a multiple of χ† changes the result by such a multiple. It is bilinear and commutative, and associativity is the literal identity (f⋄h)⋄j=[χ²fhj]=f⋄(h⋄j). The injection satisfies iota_N(f⋄h)=[χ²fh]=[χf][χh]. Hence this precise diamond algebra is isomorphic to the kernel ideal. F's semilinear action statement does not claim that F preserves products between a zero-product conormal kernel and a norm kernel with a possibly different product.

## Every power, exact nilpotence exponent and persistent algebra: RF.22–RF.24

Since I_N is the principal ideal generated by [χ], its t-th ideal power is the image of (χ^t) for every integer t≥1. At an original or reflected root λ put z=S−λ, a=a_λ, b=b_λ and retain the factor χ=z^aU_λ with U_λ(λ)≠0. In R/(z^(a+b)), write U_λ=u_0+n with u_0≠0 and n nilpotent. The finite series u_0^−1Σ_(j=0)^(a+b−1)(−n/u_0)^j is its inverse. Consequently multiplication by the explicit unit U_λ^−t carries the original generator z^(ta)U_λ^t to z^(ta). This proves equality of the generated ideals and preserves the exact original factor.

The latter ideal has basis z^(ta),…,z^(a+b−1) if ta<a+b and is zero otherwise. Its dimension is max(a+b−ta,0)=max(b−(t−1)a,0). Summing over the finite full CRT decomposition proves RF.22 for every integer t≥1. A block with a=0<b persists at its full dimension b; one with b=0<a is already zero at t=1.

If any a=0<b occurs, its nonzero block prevents nilpotence. Otherwise every b>0 has a>0, and the first zero exponent in that block is ceil((a+b)/a). This is an exact threshold, since all preceding exponents leave the first basis vector nonzero. The maximum over b>0 is well-defined and nonempty since q≥1, and is the exact global nilpotence index RF.23. No denominator with a=0 is evaluated. If b≤a at every root, equal sums Σa=Σb=q force equality at every root; this recovers the earlier square-zero criterion.

Let E=∏_(a=0<b)(S−λ)^b and M=Nχ/E. If the reflected-only set is nonempty, E and M are coprime. A Bezout identity UM+VE=1 gives e=[UM]_N. Its residue is one in every full reflected-only block and zero in all other blocks, so e²=e. Every block with a>0 vanishes after a common finite threshold, whereas all the a=0 blocks remain unchanged. Thus the intersection of all ideal powers is exactly eA_N, and restriction of the CRT residue map identifies it with R/(E), equivalently with the product of the full reflected-only rings in RF.24. The inverse is b↦[eb]_N, with unit mapping to e. Since χ divides M, π_N(e)=0. Higher nilpotent orders inside E remain present. If E=1, the intersection is zero, exactly as specified by the source's empty-product convention.

## Mixed overlap, all signs and the common lift: RF.25–RF.26

Keep k=2, c=1, A=S−(2+i), B=S−i and A=B−2. For χ=A²B, reflection gives χ†=AB², g=AB, Nχ=A³B³, d=A³B² and ℓ=A⁴B³. The difference χ²−Nχ=A³B²(A−B)=−2d is a nonzero degree-five polynomial modulo the degree-six Nχ. Therefore [χ]²≠0. The cube χ³=A⁶B³ is divisible by Nχ. The two root order pairs (a,b)=(2,1),(1,2) give the complete ideal-power dimensions 3,1,0 and exact nilpotence index three.

If P−Q=dR, then T=P+Rχ²/2 equals Q+RNχ/2 because Nχ−χ²=2d. It has the desired residues P modulo χ² and Q modulo Nχ. The lift is independent of representatives modulo ℓ. Changing P to P+χ²U changes R to R+AU and changes T by χ²U(1+A/2)=χ²BU/2=ℓU/2. Changing Q to Q+NχV changes R to R−BV and changes T by −BVχ²/2=−ℓV/2. This proves the exact inverse map, including both signs and the factor one-half.

## Additional fixture: transient overlap and a persistent double-root algebra

Retain the same k,c,A,B and put C=S−(3+2i), D=S−(−1+2i). Reflection exchanges A with B and C with D. For χ=A²BC², q=5 and χ†=AB²D². Thus

`Nχ=A³B³C²D²`, `g=AB`, `d=A³B²C²`, and `ℓ=A⁴B³C⁴D²`.

At the four roots in the order A,B,C,D the pairs (a,b) are (2,1),(1,2),(2,0),(0,2). The first ideal-power dimensions are 5,3,2,2,… . The A and B contributions vanish by power three, the C contribution is already zero, and the D block of length two remains for every power. Therefore the persistent algebra is exactly C[S]/D² with its nonzero nilpotent class D.

There is a fully explicit original-coordinate idempotent. Set r=−1+2i and M=A³B³C², so Nχ=MD². At S=r,

`A(r)=−3+i`, `B(r)=−1+i`, `C(r)=−4`,

`M(r)=16(−3+i)^3(−1+i)^3=−1408+256i`,

`M'(r)/M(r)=3/(−3+i)+3/(−1+i)+2/(−4)=−29/10−9i/5`.

Define

`U(S)=[1+(29/10+9i/5)D]/(−1408+256i)` and `e=[M U]_N`.

The first two Taylor coefficients give MU≡1 modulo D²; MU is divisible by M. The two moduli are coprime, so e²=e, and e has precisely the persistent residues. The injection C[S]/D²→A_N is [b]↦[eb], and reduction modulo D² is its inverse onto eA_N. Multiplication follows from e²=e and eD²=0. The two vectors e,eD are independent because their reductions are 1,D; eD is nonzero, (eD)²=0 and e(eD)=eD. Thus the retained persistent double root is an actual two-dimensional algebra, including its nilpotent element. Also χ divides M, so π_N(e)=π_N(eD)=0.

Every-power membership has a closed formula. At the same r,

`χ(r)=16(−3+i)^2(−1+i)=−32+224i`,

`χ'(r)/χ(r)=2/(−3+i)+1/(−1+i)+2/(−4)=−8/5−7i/10`.

For every integer t≥1 put

`q_t=(−32+224i)^(-t)[1+t(8/5+7i/10)D]`.

The first-order Taylor product gives χ^t q_t≡1 modulo D². Therefore χ^t(e q_t)−e is divisible by D², and it is also divisible by M because e is. Coprimality gives χ^t(e q_t)=e in A_N for every t≥1. Multiplying this identity by arbitrary b proves that the entire persistent algebra lies in every I_N^t. The earlier block calculation proves the reverse inclusion in the intersection. This provides the literal ideal-membership lift with all constants and signs retained.

The independent typing reviewer separately read this complete added example and checked all four numerical constants by hand: (−3+i)^3=−18+26i, (−1+i)^3=2+2i and (−3+i)^2(−1+i)=−2+14i give the displayed values of M(r) and χ(r); the stated logarithmic derivatives give exactly the coefficients in U and q_t. That review confirmed the factors, all power dimensions, the unital persistent-algebra map, the nonzero square-zero element, and the every-power lift, without further executions or edits.

## Execution design and review boundaries

The separate new checker uses exact Gaussian-rational SymPy polynomial arithmetic and complete coefficient matrices. For each fixture its F matrix has columns [(2−S)^j]_χ†, so F(v)=C_F bar v; its G matrix uses the modulus χ. It checks C_G bar C_F=I and C_F bar C_G=I, the full S operator law, and a nonreal quadratic polynomial action. This detects conjugation and reflection-sign errors that a real-coefficient fixture would miss. It also checks representative independence through the literal χ injections and the actual transported diamond product.

Ideal-power dimensions are calculated independently as ranks of full multiplication-by-χ matrix powers in the 2q-dimensional norm quotient. The checker also compares those matrices with literal multiplication by χ^t and compares their ranks with the root-order formula, through the vanishing or stabilization threshold and additional powers. In persistent cases it constructs the exact Bezout idempotent, verifies the inverse CRT algebra map, retains the nonzero double-root nilpotent, and checks explicit χ^t ideal-membership lifts.

The fixtures are mixed overlap, disjoint double roots, dagger-stable paired double roots, a dagger-stable reflection-fixed triple root, and the mixed persistent example above. The historical checker and its 106-pass result are preserved as separate inputs. This review performs no Lean calculation, compiler run, cumulative source edit, arithmetic packet realization or PDF visual inspection. Root owns rendering and integration. Actual new execution modes, counts and all resulting hashes are recorded in the companion execution receipt and closure manifest.

## Completed actual execution records

The exact new checker SHA256 is `0eb1670a3928b2ba304646b02608c09a04a518be345fe43d143e8cf78f11add9`. Both executions used Python 3.13.9 and SymPy 1.14.0. The ordinary execution exited zero with 189 checks passed, zero failed, actual `sys.flags.optimize=0` and `__debug__=True`; its complete result is `endpoint_reflected_relation_power_fixtures_normal_20260913.json`, SHA256 `bc48e4fbdd7907638eff2adfbd84bc12cd965b22748be6239b297ea5326186ea`. The optimized execution also exited zero with 189 checks passed, zero failed, actual `sys.flags.optimize=1` and `__debug__=False`; its complete result is `endpoint_reflected_relation_power_fixtures_optimized_20260913.json`, SHA256 `03da6ccbf36d6bbae3de4db250108263386854984fe9a0f5914f1ffd65be2703`.

Each total contains 177 mathematical checks and 12 runtime/provenance checks. The mathematical checks include complete matrix powers through t=5 for the mixed case, t=4 for disjoint double roots, t=6 for the stable pair, t=5 for the stable fixed root, and t=7 for the mixed persistent case. The observed rank lists are respectively `(3,1,0,0,0)`, `(2,2,2,2)`, `(4,0,0,0,0,0)`, `(3,0,0,0,0)`, and `(5,3,2,2,2,2,2)`. These finite checks accompany the general every-integer proof above; the finite list itself is not used to assert the general theorem.

Two separate deliberate mode-mismatch probes were also executed. Ordinary Python supplied with expected mode 1 exited one; optimized Python supplied with expected mode 0 exited one. Each ended with the exact error `RuntimeError: runtime: actual optimization mode` at the explicit runtime check and wrote no result file. Thus the execution record verifies that the guard remains active under optimization. These are runtime-mode rejection probes, not mathematical mutation tests. Every source and historical companion pin was checked before and after each positive run. The final closure sealer additionally compares both complete exact result objects and rehashes all included inputs without rerunning the mathematics.
