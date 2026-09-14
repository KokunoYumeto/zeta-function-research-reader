# SplitZero: maps, support fibres, ideals, and exact corrections

12 September 2026. The construction and existing manuscript results are attributed to the owner's research programme. This note gives proofs for the bounded structural package; it does not assert global priority or a completed analytic programme. Validation is tied to exact source hashes in `VALIDATION.json`.

## Conventions

For a commutative ring R, write G(R) for a supported copy of R together with one extra point tau. Supported elements add and multiply as in R. The point tau is the additive identity and multiplicative absorber. Write e for supported 0_R. Thus e is not tau, e+e=e, e*r=e for every supported r, and 1+e=1. None of the following statements requires R to be nontrivial.

## 1. Exact universal morphisms

Let p:G(R)->R send tau to 0 and supported r to r. Composition with p gives a bijection

Hom_ring(R,A) ≅ Hom_semiring(G(R),A)

for every commutative ring A. Indeed, for a semiring homomorphism h, the equation e+e=e implies h(e)+h(e)=h(e), hence h(e)=0 by cancellation. Therefore r↦h(r) is a unital ring map and factors h through p. Uniqueness follows from surjectivity of p. In particular, no semiring map G(R)->A to a ring is injective: it identifies e and tau.

Let B be the Boolean semiring. The support character chi:G(R)->B sends tau to 0 and every supported r to 1. It is unique: e=1+(-1) gives h(e)=1 for every unital semiring map h to B; then re=e gives h(r)=1. The map (p,chi):G(R)->R×B is injective with image exactly {(0,0)} union (R×{1}). The second coordinate distinguishes absence from a supported zero; the first distinguishes supported amplitudes.

Every ring map f:R->S lifts to G(f), fixing tau and acting by f on supported elements. Conversely, if H:G(R)->G(S) is a semiring map, p_S H factors through p_R as a unique ring map f. The support coordinate of H equals chi_R by uniqueness of the Boolean character. Thus H and G(f) have equal amplitude and support and are equal by joint injectivity. Consequently

Hom_semiring(G(R),G(S)) ≅ Hom_ring(R,S).

This identifies the morphisms without asserting G(R)≅R. In Lean the exact statements are `ringHomEquiv`, `coordinates_injective`, `coordinates_image`, and `splitHomEquiv`.

## 2. Intrinsic support and fibre modules

For any G(R)-semimodule M, put s(m)=e*m. The scalar identities imply

s(m+n)=s(m)+s(n),  s(s(m))=s(m),  m+s(m)=m,  s(m)+s(m)=s(m).

Conversely suppose y+y=y. Put v=(-1_R)*y. Since e=1_R+(-1_R), s(y)=y+v. Therefore y+s(y)=(y+y)+v=y+v=s(y), while absorption gives y+s(y)=y. Hence s(y)=y. Thus the support set L={l:s(l)=l} is exactly the additive-idempotent locus. Addition gives its join, l≤k iff l+k=k, and its least element is 0_M.

For l∈L, define M_l={m:s(m)=l}. This is an actual R-module: addition is inherited, its zero is l, inverse is m↦(-1_R)*m, and r acts as supported r. The essential identities are

s(m+n)=l+l=l,  m+l=m,  m+(-1_R)*m=l,  e*r=e.

For l≤k, T_lk(m)=m+k lies in M_k. It is additive because k+k=k. Every supported scalar fixes k, since r*k=r*(e*k)=(r*e)*k=e*k=k; hence T_lk is R-linear. Also T_ll=id and T_kn T_lk=T_ln by absorption and k+n=n.

A G(R)-linear map F commutes with s. Its support restriction preserves zero and joins by F(0)=0 and F(l+k)=F(l)+F(k); its fibre restriction is R-linear. Naturality is the literal equation F(m+k)=F(m)+F(k). Lean implements the fibre restrictions as `LinearMap`s and checks transport identity, composition and this naturality square.

Finally m↦(s(m),m) is a bijection with the disjoint union of the intrinsic fibres. If u=s(m)+s(n)=s(m+n), the reconstructed sum is

(m+u)+(n+u)=m+n+u=m+n.

The Lean package supplies the forward fibre construction and reconstruction for an existing semimodule. It does not yet construct the semimodule associated with every arbitrary abstract diagram or the complete categorical equivalence with natural isomorphisms. These are separate remaining implementation steps; the manuscript already proves the equivalence on paper.

## 3. Complete ideal classification

For I⊲R let I^G=p^(-1)(I)=I union {tau}. This contains e, so it is not the zero semiring ideal {tau}. Conversely, if J⊲G(R) differs from {tau}, choose a supported r∈J. Multiplication by e gives e∈J. Therefore J intersect R contains 0_R and is closed under addition and multiplication by arbitrary R-elements, hence is a ring ideal. The two constructions are mutually inverse and preserve inclusion. Thus

Ideal(R) ≅ {J∈Ideal(G(R)): J≠{tau}}

as ordered sets. Equivalently every J is either {tau} or uniquely I^G. The whole ideal poset has one additional bottom element below (0_R)^G={tau,e}. Lean constructs `nonzeroIdealOrderIso`, not merely a conditional theorem assuming the classification.

### Empty joins

The isomorphism preserves joins computed in the non-bottom ideal poset. In the ambient Ideal(G(R)), however, the empty join is {tau}, whereas the lift of the empty join from Ideal(R) is {tau,e}. Hence ambient empty joins are not preserved. Nonempty ambient joins are preserved because their supremum contains a lifted ideal and therefore e; it is still in the non-bottom subposet.

## 4. Correcting the monoid-semiring presentation

The printed presentation in chapter 14 takes the ordinary free monoid semiring N[M_R], where M_R is the multiplicative monoid of G(R), modulo

[a]+[b]=[a+b] for supported a,b,
[x]+[tau]=[x] for multiplicative generators x.

These relations do not imply [tau]=0. Evaluate every multiplicative generator at 1 in the Boolean semiring. This is unital and multiplicative; every displayed relation becomes 1+1=1, but [tau] maps to 1≠0. The free monoid-semiring universal property therefore gives a model of the relations in which the missing equation fails.

The repair is to add [tau]=0, or explicitly use a free construction already identifying the absorber with semiring zero. With the extra relation, the proposed inverse G(R)->Q preserves zero: tau maps to 0 and supported r to [r]. It preserves addition by the supported relation and the zero law, and multiplication and one by the monoid presentation. This inverse and evaluation Q->G(R) are identities on generators, hence mutual inverses.

The Lean file checks the multiplicative-generator countermodel and the corrected semiring-lift universal property. It does not construct the entire free monoid-semiring congruence quotient. No existing frozen reader text is silently rewritten.

## 5. Scope within the Zeta programme

Chapter 14 already gives the semimodule/linear-join-diagram result and ideal classification. PR #3's Rees continuation explicitly begins above that common support. The present work supplies reusable algebraic structure for that continuation; it does not certify its analytic, arithmetic-trace, purity or positivity claims. No RH statement is asserted.

The source acknowledges classical semiring/semimodule terminology and strong semilattices of groups. No exhaustive priority comparison has been completed. Attribution of this construction to the owner's programme, a new Lean implementation, and a claim of new mathematics are distinct assertions.

## Source records

KokunoYumeto. (2026a). *Split-zero support and shifted Dedekind sheets* [Research manuscript, chapter 14]. In *Riemann Zeta Function: Research Reader*. Commit 42d00e359b16d52ca71568ce5e3db5341949d929; blob 49318a578b96462384000afa16794cfd5fe492c1. https://github.com/KokunoYumeto/zeta-function-research-reader/blob/42d00e359b16d52ca71568ce5e3db5341949d929/satellites/14_globalization_cue_split_zero_and_shifted_sheets.tex

KokunoYumeto. (2026b). *Split support, Rees defects, and the completed arithmetic trace* [Draft research note, PR #3]. Commit 37b2cc9b9baee3ffe25a7649314adb025302509f. https://github.com/KokunoYumeto/zeta-function-research-reader/pull/3

KokunoYumeto. (2026c). *SplitZero.lean* [Lean source]. Blob ff991f7383922e71cdf0e4a3bc85e89e18f808ef. https://github.com/KokunoYumeto/modern-latex-manuscripts/blob/f7ff59b176c7dc3941babd4cb9272dffc653070d/formalization/lean/classical_candidates_20260626/split_support_sidecar/SplitZero.lean
