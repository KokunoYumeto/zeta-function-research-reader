# SplitZero: scalars, morphisms, and intrinsic fibre modules

This is a bounded Lean formalization of **KokunoYumeto / u/lepthymo's split-zero
construction**, following chapter 14 of the Zeta research reader. It is not a
claim that the entire workbench is novel, or that its analytic, adelic, or zeta
claims have been formally proved. Related strong-semilattice constructions are
already acknowledged in the chapter; a literature-priority investigation is a
separate task from checking these statements.

## Sources and relation to the other work

- Main source: [`satellites/14_globalization_cue_split_zero_and_shifted_sheets.tex`](../../satellites/14_globalization_cue_split_zero_and_shifted_sheets.tex),
  inspected at commit `42d00e359b16d52ca71568ce5e3db5341949d929`.
- Earlier scalar implementation: `SplitZero.lean` in
  `KokunoYumeto/modern-latex-manuscripts`, commit
  `f7ff59b176c7dc3941babd4cb9272dffc653070d`, path
  `formalization/lean/classical_candidates_20260626/split_support_sidecar/`.
  `Core.lean` adapts that carrier and its operations; it is not counted as an
  independently invented construction.
- The pending split-support/Rees contribution, Zeta PR #3 at
  `37b2cc9b9baee3ffe25a7649314adb025302509f`, was inspected for alignment.
  Its Rees defects, filtered retractions, lattice amplifications, and actual
  adelic comparisons are **not** imported or asserted proved by this package.
  Neither that PR nor the manuscript main branch is automatically merged here.

No repository-wide licensing, mathematical authorship, or historical attribution
is changed by this workbench. The contribution is AI-assisted formalization and
proof repair under the construction author's direction.

## The completed statement boundaries

| Module | Exact content |
|---|---|
| `Core` | The split-zero commutative semiring, distinction of its two zeros, absence of additive cancellation to structural zero, collapse map, and the fact every homomorphism to a ring kills the supported zero. |
| `Hom` | Lifting coefficient homomorphisms; the ring-reflection universal property; recovery of all homomorphisms between split-zero rings, without assuming support preservation. |
| `Support` | Intrinsic additive-idempotent support, its join-semilattice with bottom, actual additive groups and coefficient-ring modules on the fibres, linear transport with identity/composition, and naturality for actual semimodule maps. |
| `Functoriality` | The disjoint-union carrier decomposition, bottom/join preservation, and identity/composition equations for skeleton and fibre maps. |
| `Reconstruction` | The unique Boolean support character and a countermodel to the uncontracted monoid-semiring presentation as printed. |
| `Presentation` | Unique extension of multiplicative assignments satisfying the **corrected** zero and supported-addition relations. |

These are general quantified statements, not finite regression tests. Definitions,
instances, elementary supporting lemmas, and mathematical theorems are all needed
in the code; an audit-target count must not be advertised as that many new theorems.
The reverse construction from arbitrary linear join diagrams, a bundled category
equivalence, localization classification, Rees theory, and analytic results remain
outside this formalized boundary.

## 1. Ring reflection and homomorphism recovery

Write `tau` for the semiring zero, `ofR r` for a supported scalar, and
`e = ofR 0`. Let `p : G(R) -> R` collapse both `tau` and `e` to arithmetic zero.
For commutative rings `R,A`, `ringHomEquiv` proves

    Hom_semiring(G(R), A) ≃ Hom_ring(R, A).

Proof: if `f` takes values in a ring, `e+e=e` gives `f(e)+f(e)=f(e)`, hence
`f(e)=0`. Restricting to the supported copy of `R` is therefore a unital ring
homomorphism, and every value of `f` is recovered by composing that restriction
with `p`. Uniqueness is immediate on the supported elements, and both maps send
the absent element to zero.

For commutative rings `R,S`, `homEquiv` proves the stronger support-recovery result

    Hom_ring(R, S) ≃ Hom_semiring(G(R), G(S)).

Proof: `G(S)` has `x+y=0` only when `x=y=0`. Since
`e = 1 + ofR(-1)`, a unital homomorphism `f` cannot send `e` to structural zero.
Since `(ofR r)*e=e`, it cannot send any supported element to structural zero.
Every `f(ofR r)` is thus uniquely `ofR(g(r))`. Apply the preceding ring-reflection
argument to `p_S ∘ f`; its restriction is the ring homomorphism `g`, and lifting
`g` recovers `f`. The code also checks identity and composition of lifting.

This does not identify `G(R)` with `R`: the collapse map identifies two distinct
elements, `tau` and `e`. The new support information matters precisely for its
semimodule structure.

## 2. Intrinsic fibres, rather than an assumed diagram

For any `G(R)`-semimodule `M`, define `epsilon(m)=e*m`. Then

    epsilon(m)=m  iff  m+m=m.

Indeed `m+epsilon(m)=m` follows from `1+e=1`, and `epsilon(m)` is idempotent
because `e+e=e`. Conversely, if `m+m=m`, the equation
`epsilon(m)=m+ofR(-1)*m` gives `m+epsilon(m)=epsilon(m)`; comparison with the
first identity gives `epsilon(m)=m`.

The fixed locus `L` is a join-semilattice, with join inherited from addition and
bottom the original zero. For `l in L`, the fibre `M_l={m: epsilon(m)=l}` has
zero `l`, addition inherited from `M`, inverse `ofR(-1)*m`, and scalar action
`r*m := ofR(r)*m`. The support equations prove closure and all module laws.

For `l <= m`, transport is `T_lm(x)=x+m`. The equations `m+m=m` and
`ofR(r)*m=m` prove linearity. Associativity and the support order give
`T_ll=id` and `T_mn ∘ T_lm=T_ln`. Every actual semimodule-linear map preserves
support and gives fibre-linear maps commuting with these transports. The code
proves preservation of bottom and joins and the identity/composition laws; it
does not replace those obligations with hypotheses.

## 3. Correction: an absent generator is not automatically the additive zero

In Proposition `gcue-product-reconstruction`, let `N[M_R]` mean the ordinary,
**uncontracted** free commutative monoid semiring on the multiplicative monoid
underlying `G(R)`. The printed relation families are

    [a]+[b]=[a+b]   (a,b in R),
    [x]+[tau]=[x]  (x in M_R).

They do **not** force `[tau]=0`. A multiplicative assignment sending every
generator to `1` in the Boolean semiring satisfies both families, since `1+1=1`,
but sends `[tau]` to `1`, not `0`. The assignment extends to the free monoid
semiring and descends through the stated relations. Consequently the canonical
evaluation quotient map to `G(R)` is not injective.

`reconstruction_relations_do_not_force_zero` checks the multiplicative
countermodel, both relation families, and its nonzero absent-generator image.
The Boolean semiring is implemented as `G(ZMod 1)`, the two-element split-zero
semiring over the trivial ring. The nontriviality of that semiring does not
require a nontrivial coefficient ring.

### Exact repair and proof

Add the relation

    [tau]=0.

The mixed-addition relations then follow from the additive identity. Evaluation
from the corrected quotient `Q` to `G(R)` is well-defined. Its inverse sends
`tau` to `0_Q` and each supported `r` to `[r]`. The corrected zero relation,
the supported-addition relations, and the monoid multiplication relations prove
this inverse preserves zero, one, addition, and multiplication. The two
composites are identities: one is immediate on the two cases of `G(R)`, and the
other fixes every monoid generator, which generates `Q` as a semiring. Thus the
corrected quotient is isomorphic to `G(R)`.

Alternatively, a contracted monoid-semiring convention can make `[tau]=0`
part of the definition, but that convention must be stated explicitly.

The Lean theorem `corrected_assignment_extends_uniquely` proves the exact
mapping property after this repair: any multiplicative assignment with
`f(tau)=0` and the supported-addition relations extends uniquely to a semiring
homomorphism from `G(R)`. The quotient and its isomorphism are proved above on
paper; an explicit Lean construction of that quotient is not claimed here.

## Reproduction and trust boundary

Lean is pinned to `v4.31.0`; Mathlib is pinned to
`fabf563a7c95a166b8d7b6efca11c8b4dc9d911f`.
From this directory:

```sh
python3 -m unittest -v test_check.py
python3 check.py --prepare
lake update
lake exe cache get
lake -KmaxJobs=1 build SplitZero
for source in SplitZero/*.lean; do
  lake env lean --trust=0 -DwarningAsError=true "$source"
done
lake env lean --trust=0 -DwarningAsError=true Audit.lean > Audit.log
python3 check.py --log Audit.log
```

The CI repeats these checks and verifies the resolved Mathlib commit. The audit
rejects absent reports, duplicate reports and any transitive axiom outside
`propext`, `Classical.choice`, `Quot.sound`. All source modules are compiled;
the name extractor covers this package's declared style, not arbitrary Lean
syntax, every compiler-generated constant, or all Mathlib declarations. It is
not an independent alternative kernel. Fresh validation is commit-specific;
use the workflow result linked from the PR, not the presence of this README, as
the execution record.

The first four-module checkpoint `328a2fb6df609ee164241ba4409f2ae884b0e5ca`
passed run `34661024492`. The subsequent coherence and corrected-presentation
extensions require their own successful run and must not inherit that narrower
checkpoint's status.
