# Independent finite-Weyl formula audit

Bounded algebra audit, 12 September 2026. This record concerns the formulas supplied by the finite-Weyl author and PR20's full local `NOTE.tex`. The proposed new TeX and checker were not yet present when the direct proof below was written. This record will state the exact later reading scope if those files arrive. No authored proof source or delivered source was edited.

Let `h` be the original monic polynomial of degree `d>=1` over `C`, with `r` distinct roots; let `k>=1`, `P=C[s_1,...,s_k]`, `h_i=h(s_i)`, `I=(h_i)`, `E=P/I`, `A=P/I^2`, `n=d^k`, and `pi:A->E`. The case `h=1` is separate: the quotients vanish and formulas dividing by `d` do not apply. All factors below are in characteristic zero.

## Canonical remainder and exact defect

The unique representative of `p in E` with degree less than `d` in each original variable defines the complex-linear section `j:E->A`. Write `ell_i(p)` for its coefficient of `s_i^(d-1)`, retaining the full polynomial in all other variables. It is regarded as an element of `E` independent of `s_i`. Multiplication by `s_i` exceeds the rectangular degree bound in exactly this term. Monic division therefore gives the literal polynomial identity

`s_i rep(p) - rep(s_i p) = h_i rep(ell_i(p))`.

With `S=sum_i s_i`, `Z=M_[S]` on `E`, and `Zhat=M_[S]` on `A`, summing proves

`Zhat j - j Z = sum_i [h_i] j ell_i`.

The section is complex-linear; this identity does not call it an algebra section.

The product rule sends `I^2` into `I`, so `delta:A->E`, `delta[P]=[(1/k)sum_i partial_i P]`, is defined and satisfies

`delta(ab)=pi(a)delta(b)+pi(b)delta(a)`, `delta(S)=1`.

Let `D0=delta j`. Applying `delta` to the preceding section identity gives

`Z D0 - D0 Z = -Id_E + J`,

`J=(1/k)sum_i M_[h_i'] ell_i`.

Indeed the left derivative before rearrangement is `p+Z D0 p-D0 Zp`; the derivative of each conormal summand is `h_i' ell_i(p)/k`. These computations fix both the negative identity and the factor `1/k`.

## Complete correction spectrum

Set `P_i=M_[h_i'] ell_i/d`. The polynomial `h_i'` has degree `d-1` and leading coefficient `d`. Therefore `ell_i(h_i' a)=d a` whenever `a` is independent of `s_i`. This proves `P_i^2=P_i` with no root-separation assumption. Its image is `C h_i'` in the `i`th factor tensored with every other original factor. Its kernel consists of the polynomials of degree at most `d-2` in `s_i`; for `d=1` that kernel is zero.

Operators on distinct factors commute, so the `P_i` are commuting idempotents. The projectors

`Q_A=product_(i in A) P_i product_(i notin A)(1-P_i)`

are pairwise orthogonal algebraic idempotents, sum to the identity, and have ranks `(d-1)^(k-|A|)`. On their images `J=(d/k)sum_i P_i` is multiplication by `d|A|/k`. Consequently the multiplicity of `dj/k` is `binom(k,j)(d-1)^(k-j)`. Only positive multiplicities belong to the spectrum; when `d=1`, the sole eigenvalue is `1` with multiplicity one, using `0^0=1` in the multiplicity formula. In particular

`trace(J)=n`, `rank(J)=n-(d-1)^k`,

`ker(J)=intersection_i ker(ell_i)`.

Thus `trace(-Id+J)=0` exactly. Repeated roots do not change this canonical spectrum.

## Exact comparison with the full conormal row

Monic division identifies `I/I^2` with `E^k` by `iota(a)=sum_i h_i rep(a_i)`. Let

`C:E^k->E`, `C(a)=(1/k)sum_i h_i'a_i`,

`L:E->E^k`, `L(p)=(ell_i(p))_i`.

Then `delta iota=C` and `J=C L`. The full row has image ideal `H=(h_i')` in `E`. The quotient is the tensor product of `C[s]/(h,h')`; since `deg gcd(h,h')=d-r`,

`dim(E/H)=(d-r)^k`, `rank(C)=n-(d-r)^k`.

Its kernel has dimension `(k-1)n+(d-r)^k`. The kernel equality for `J` proves `ker(CL)=ker(L)`, so `C` restricted to `im L` is injective. Hence `im J` is explicitly embedded in `im C`, with vector-space codimension `(d-1)^k-(d-r)^k`. This is an exact factorization, not an identification of the two images as ideals.

Locally, if `h=z^m w(z)` with `w(0)!=0`, multiplication by `h'` sends `a=sum a_j z^j` to `m w(0)a_0 z^(m-1)` modulo `z^m`. PR20's statement about detecting the top coefficient requires this input/output correction: the conormal row reads the constant coefficient of its input and produces the top surviving coefficient. The map `ell_i` above really does extract a top coefficient, from a different, explicitly stated domain. On an ordered local block the full row rank is `product_i m_i-product_i(m_i-1)`, agreeing with PR20's numerical dimension formula.

## Full arithmetic unit

Let `Uhat` be the original invertible class in `A`, `U=pi(Uhat)`, and `beta=U^-1 delta(Uhat)`. In the arithmetic application `U=product_i [v_h(s_i)]`, with `v_h=g/h`; no such factor is assigned the value one. The transported section is

`j_U=M_Uhat j M_U^-1`.

It satisfies `pi j_U=Id`. Applying the product rule, with all multiplication operators in their stated rings, proves

`D_U=delta j_U=M_beta+M_U D0 M_U^-1`.

The multiplication operators for `S`, `beta`, and `U` commute on `E`; consequently

`[Z,D_U]=-Id+M_U J M_U^-1`.

For `k=1`, the correction is exactly

`M_[g'] ell M_U^-1`,

because `[g']=[v_h h']` modulo `h`. This identity retains the full arithmetic unit and every repeated-root jet; it does not replace `g'` by a root multiplicity or by `h'` alone.

## Quotient and derivative in one ring map

The map `Phi:A->E[epsilon]/epsilon^2`, `Phi(a)=pi(a)+epsilon delta(a)`, is a unital complex-algebra homomorphism. Multiplying its two coefficients gives the product rule above, and `delta(1)=0` fixes its unit. Using `A=j(E) direct-sum iota(E^k)` as complex vector spaces gives

`Phi(j(p)+iota(a))=p+epsilon(D0 p+C(a))`.

Its exact kernel is `iota(ker C)`, an ideal, and its exact image is

`{p+epsilon q : q-D0p in H}`.

The image is a subalgebra: the derivative modulo `H` is a well-defined derivation `E->E/H`, along the quotient map. It is not being treated as an ideal of the target dual-number algebra. The cokernel in the following dimension count is a complex-vector-space cokernel:

`dim ker Phi=(k-1)n+(d-r)^k`,

`dim im Phi=2n-(d-r)^k`,

`dim coker Phi=(d-r)^k`.

Thus `Phi` is onto exactly when `h` is squarefree. It is an isomorphism exactly when `k=1` and `h` is squarefree. When `d=1`, the map is onto for every `k`, has kernel dimension `k-1`, and is an isomorphism only for `k=1`. When `k=1` and `h=(s-rho)^d`, its image has dimension `d+1` and its kernel has dimension `d-1`. These cover the repeated and degree-one edge cases without deleting nilpotents.

The exact unit transport is `Phi(Uhat)=U(1+epsilon beta)`. Thus multiplying the retained source amplitude is transported through the same algebra map, rather than through an assumed descent of differentiation to `E`.

## Status

The formulas in the delegated task pass the direct independent proof audit. The source wording distinction and the positive-degree restriction are already recorded in the larger source-audit log. This file alone does not certify an as-yet-unread new TeX or checker, an analytic estimate, or an RH endpoint.

## Subsequent complete code and TeX reading

The new `scripts/check_conormal_finite_weyl.py` and `tex/conormal_finite_weyl.tex` subsequently appeared. I read the full checker and the whole TeX CW.1--40. The checker SHA256 at this audit was `07f1b37ad6451b4eee0aac4a88044fc1e04c4611fb7018e7101cc1358813f6b0`.

The implementation constructs the full monic `h`-adic remainder on the original tensor basis. Its first-thickening coordinates retain exactly total `h`-degree zero and one, so mixed and squared conormal terms have the required quotient. The derivative matrix is obtained by differentiating the original thickening basis polynomials, while the correction is independently formed from tensor top-coefficient extraction and multiplication by `h'`. Thus the primary commutator comparison is not an implementation echo.

The generator identities for `Phi` act on the entire source thickening and use multiplication by `s_i+epsilon/k` on the full dual-number target. Together with the unit test and the fact that the original variables generate the source algebra, these are sufficient finite algebra multiplicativity tests; a table of every pairwise basis product is unnecessary. The independent quotient-coordinate block identity gives the full image graph and conormal row. The direct `Uhat` multiplication on the thickening also tests the derivative of the unit, including degree-one quotients where the value of `U` alone would fail to retain it.

The nine fixtures retain degree-one quotients for `k=1,2,3`, a double root for `k=1,2,3`, a mixed repeated/simple cubic for `k=1,2`, and a squarefree quadratic for `k=2`. Additional local multiplication tests retain orders one through four and the nonconstant local unit `2+3w+w²`. These are real/rational fixtures. They do not test reflected conjugation, actual theta-unit values, or an analytic estimate; the checker's scope correctly excludes those claims. The checker does not use Python `assert`, and all comparison records raise on a failed condition. Its deliberate harness failure is separately requested by `--self-test-failure`.

The inspected normal receipt had 952 passing records: 905 exact and 47 negative controls. It matched the checker SHA above. Its recorded TeX SHA was `9fe33372eee47bd88aa4689eada8be3238f9bd50f6446202cffdbd39701ddbf6`, while the subsequently sampled live TeX was `34cadb5ae5f3deeff33723af93bf8c7060ad41d1a386b52badda70c33c823f87`. The source was still receiving author edits; the parent was notified to refresh final receipts against the settled source. I did not duplicate the parent's runtime runs or claim independently executed optimized-mode results.

The checker uses multiplication by the original `S`, whereas the TeX calls multiplication by `S-k/2` its `Z`. Every tested commutator and section defect is invariant under exactly this scalar shift: subtracting `(k/2)Id` on both source and target cancels by `pi j=Id` and by linearity. The unchanged identity is therefore a valid calibration of the centered presentation, with the coordinate comparison explicitly retained.

The additional TeX formulas were also checked: the metric transport of the weight in CW.21; the admitted original minimum numerator and its full arithmetic jet unit in CW.28; the changed section formula `J_M^sec=J_U+[Z,delta a_M]` and its trace in CW.30; the residue functional in CW.32 obtained from the coefficient of `1/s` in the complete partial-fraction expansion; the two distinct input maps using the same `g'` in CW.33--35; the global scaling-equivariant map `V->Q` in CW.37--38; and the fixed-support maps in CW.39--40. Their types, signs and factors agree with the preceding direct proof.

One wording correction remains in the version read. After CW.20, the phrase “they are Hermitian precisely when `P_i* G=G P_i`” follows displays of both the individual transported projectors and the transported sum correction. Each transported `P_i` is Hermitian precisely when `P_i*G=GP_i`; the transported `J` is Hermitian precisely when `J*G=GJ`. The latter need not force all the former equations. For a declared algebraic counterexample, take `k=d=2`, `h=s²`, original basis `(1⊗1,1⊗s,s⊗1,s⊗s)`,

`P1=diag(0,0,1,1)`, `P2=diag(0,1,0,1)`, `J=diag(0,1,1,2)`,

and the positive matrix

`G=[[1,0,0,0],[0,2,1,0],[0,1,2,0],[0,0,0,1]]`.

The matrix `G` commutes with `J` and does not commute with `P1` or `P2`. This is a finite metric calibration, not an assertion about a theta Gram matrix. The parent was sent the exact corrected sentence and this example. No checker implementation correction was found. No source file was edited by this reviewer.

## Final patch verification

The author has now replaced the ambiguous CW.20 sentence by the two exact individual and sum conditions. I inspected that final paragraph and all subsequent checker additions, without rerunning the parent's process.

- Final audited TeX SHA256: `6ca142ec052ad110e3c58ece4d81bf87a33fc18c8533c41deb863bceb300715a`.
- Final audited checker SHA256: `553f75acce9ab6d9390603ac916f62b8ed4e4e0880cc98e80d074155e4d38582`.

The checker now independently forms multiplication by `S-k/2` on both `E` and `E2`, tests its exact difference from the original sum, and checks the centered rectangular derivative intertwiner, canonical section defect, fixed-section commutator, unit-conjugated commutator and unit-conjugated section defect. All added equations retain the exact scalar `k/2` and have the signs of CW.12--13 and CW.25. The new negative control detects omission of that scalar from the actual coordinate operator, even though it cancels from the corresponding commutators.

The additional metric counterexample uses the matrices displayed in this report, verifies all four positive leading principal minors, verifies Hermiticity of the sum in that declared metric, and rejects Hermiticity of each individual projector. Since the displayed matrix is real symmetric, its positive leading principal minors prove positive definiteness. This calibration is explicitly distinguished from an actual theta metric.

There are no outstanding mathematical or implementation corrections in the audited files. I inspected the updated normal receipt: both source hashes match the final audited hashes above, and all 1,031 records pass, comprising 973 exact checks and 58 negative controls. The parent owns the optimized run and both deliberate-failure runs. Those additional runtime results should be cited from their final receipts, not inferred from this source audit. No source file was edited by this reviewer.

## Retained-unit enhancement: final checker edition

I inspected the final small checker enhancement. It now declares

`U_base=product_i(s_i+5)`, `n_U=sum_i(i+1)h_i` (zero-based indices), `U_poly=U_base+n_U`.

Thus the reduced multiplication operator on `E` is unchanged, while the full class on `E2` contains a specified nonzero conormal component. The additional comparison has the exact proof

`delta(n_U j(U^-1 u))=(delta n_U)U^-1 u`,

because `pi(n_U)=0`; it therefore correctly tests

`D_U-D_U_base=M_(partial_Sigma n_U) M_U^-1`.

The two added rejection checks detect deleting this nonzero component from the thickening and from the derivative. The one-variable definition is now the literal polynomial `g=h(s+5+h)`, retaining the same complete unit class used in that fixture. Its reduction `[g']=[h'(s+5+h)]=[h'(s+5)]` is exactly the residue identity being checked; the terms containing `h` have their declared destination modulo the original ideal. The centered intertwiner's additional sign-reversal rejection is also correct, since `pi` is nonzero and the coefficient field has characteristic zero.

- Final checker SHA256 superseding the prior checker hash: `307b9b879a46f56a8701e9f920a085e1a75257de8d931ae22efdff7ce8fac7a9`.
- TeX SHA256 remains `6ca142ec052ad110e3c58ece4d81bf87a33fc18c8533c41deb863bceb300715a`.
- Inspected matching normal receipt: **1,076/1,076** pass, comprising **991 exact checks and 85 negative controls**.

No outstanding mathematical or implementation correction was found in this final patch. Optimized and deliberate-failure runs remain the parent's separately recorded execution lane; this reviewer did not duplicate them.
