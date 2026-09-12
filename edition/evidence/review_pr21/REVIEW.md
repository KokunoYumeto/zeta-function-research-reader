# PR21 exact-head mathematical review

Reviewed head: `2abc351424ba87aeda948a5cfb846e15ed9373d1`.
Reviewed main: `4c5ce7a8575fa8b95df272116eb5783b2309cdb7`.
All eight added files were downloaded through exact-ref GitHub APIs and read completely. `FETCH_RECEIPT.json` binds their sizes, SHA-256 and Git blob identities; the compare is eight additions, zero modifications/deletions. No local Git or Lean execution.

## Mathematical conclusion

**Integrate at the proved scope. No mathematical correction is required.** Formal algebra, the complete written polynomial/retraction argument, and exact finite calibrations are separately identified. The note explicitly does not certify the uninspected analytic source archive, its moment enclosures, or a uniform arithmetic control estimate.

### Original quotient maps, not substitute carriers

`SplitZeroConormalTower.lean:20–103` defines `level I r=(I^r).restrictScalars R` and proves the ideal-power derivative by product induction. In the induction step, a lies in I^(r+1), b in I: aD(b) remains in I^(r+1), while D(a)b lies in I^r I. Base depth zero has target the whole ring. No characteristic-zero or radical-ideal assumption is used here.

`descended` at line47 calls the actual merged `SplitZero.RelationLayer.derivative`; `projection` at line57 calls its actual `transport`. These were checked directly against both complete inherited RelationLayer modules. The representative [x] maps to [Dx], and the two routes A/I^(r+2) to A/I^r agree on every representative. The conormal formula at line74 retains [aD(z)] because zD(a) belongs to I. The full multiplier rule at line89 preserves both terms. Full-ideal `top_level_zero` at line97 includes r=0 correctly: the unit ideal has every power equal to itself.

### Exact cyclic relation and unit comparison

`SplitZeroConormalTower.lean:106–173` uses the pullback of I^r along polynomial evaluation. Quotient injectivity follows from the same kernel defining that pullback; no injectivity of evaluation before quotient is assumed. The chain rule uses D(S)=1 explicitly. Its source is the original R-algebra and its target is the original quotient, not an assertion that the derivative acts on one fixed quotient. The cyclic square is checked on arbitrary polynomial representatives. `cyclic_unit_rule` retains the ambient term P(S)D(u); the proof does not pretend that term is cyclic.

The external formal dependency was checked at the pinned [Mathlib derivation source](https://github.com/leanprover-community/mathlib4/blob/fabf563a7c95a166b8d7b6efca11c8b4dc9d911f/Mathlib/RingTheory/Derivation/Basic.lean#L135): Cavalleri/Yang's `map_aeval` states the full chain rule with the multiplier D(S). The new D(S)=1 specialization therefore preserves, rather than changes, that convention.

### Attained degree and exact annihilator

`SplitZeroCyclicDepth.lean:17–124` proves equivalence of the floor-sum and quotient/remainder predicates, bounds the degree, and constructs attainment at a supplied maximal coordinate j. Positive multiplicities and positive depth occur exactly where needed. Attainment has an actual j, hence entails a nonempty index type; the written polynomial statement likewise assumes k>=1. General finite-index notation does not erase that hypothesis.

`RESEARCH_NOTE.md:69–140` correctly identifies the local ideal with (y_i^m_i), using invertibility of the other root factors. Its r-th power is a monomial ideal: a monomial y^a lies in it precisely when nonnegative integers b_i<=floor(a_i/m_i) can be chosen with sum b_i=r, equivalently when the floor-sum is at least r. Thus the displayed survivors are a basis, not just a spanning set. Writing a_i=m_iq_i+t_i gives the stated bound, and allocating r-1 to a maximal multiplicity attains it. In characteristic zero the literal multinomial coefficient of that survivor in (sum y_i)^(L_r-1) is nonzero. This proves exact nilpotency, not merely an upper bound.

The root-tuple ideals are pairwise comaximal; their local powers give the primary factors of the quotient by I^r. Consequently the minimal polynomial of S is the least common multiple of their (X-lambda)^L factors: exactly the maximum exponent over each collided sum. Restricting to the invariant algebra does not alter a polynomial relation of S, since that polynomial already lies there. The step inequality and the comparison L_r<=rL_1 imply all three displayed divisibilities with their stated direction. Polynomial integration proves surjectivity of the consecutive cyclic derivatives over C. Empty h=1 is separately evaluated; no empty maximum is taken.

The collision calibration max(5r,4r+3) yields 7,11,15,20,25 at r=1,...,5. The repeated double-root example yields 2r+1 rather than 3r for r>1. These are correctly labeled algebraic packets, not location claims about arithmetic zeros.

### Retraction, full unit and Gram terms

`RESEARCH_NOTE.md:142–158` gives an explicit module retraction. The full unit w has nonzero top nilpotent image because unit multiplication is invertible. On a primary component choose theta detecting that image. The coefficient of X^j in pi0(Nv) is theta(N^(ell-j)v): its constant term is zero and the remaining terms exactly shift pi0(v). Thus pi0 intertwines N with X. Its value c at w has nonzero constant term, and the displayed finite geometric inverse is valid modulo X^ell. Multiplication by c^-1 yields pi(P(N)w)=P(X), proving the stated left inverse and invariant kernel. The note does not claim an algebra retraction, orthogonal splitting, equality of cyclic and full traces, or cancellation of U-dagger U. No sign or scale correction is needed.

## Executed finite checks and certificate boundary

Source-reviewed `check_depth_models.py` was run normally and with `-O`. Eight methods passed in each mode, and the successful JSON bytes were identical. Both deliberate-negative runs had exactly nine tests, one intended failure, no errors, exit1. `finite_tests/TEST_RECEIPT.json` records commands and hashes. Only integer/rational arithmetic and bounded monomial/polynomial models are involved; these do not replace the general Lean proofs or written arguments.

The selected manifest contains 16 ConormalTower plus13 CyclicDepth targets, including definitions. `projection_mk`, `evaluation_mk` and `cyclicDerivative_mk` are compiled in the complete source but are not among the29 selected axiom reports; the scope language correctly says selected. No count is a claim of29 novel theorems. Exact-head CI and the inherited40/68/38/87/73/28 scopes are independently reviewed in `ci_review` before readiness.

## Routine integration maintenance

The new workflow currently has a push trigger only for its development branch, and PR triggers only for the new files. After exact-head integration, extend its trigger to main and inherited formal dependencies without changing any job, command, pin, permission, axiom allowlist or test. Run and inspect the resulting exact main-head CI. The original implementation/CI receipt and all failed development commits remain unchanged.

The note's starting `a4494fba` and coordination record explain their chronology; the current branch explicitly incorporates4c5ce7a. This is not a reason to rewrite historical source statements. No frozen edition, reader bytes, original equations or unrelated files are changed by this review.

## Completed independent CI review

The complete 137155-byte, 2153-line original job log was independently read through its lossless compact view. Its checkout is exactly `2abc351424ba87aeda948a5cfb846e15ed9373d1`, job `103617105475` in successful run `34717443909`. Lean reports version 4.31.0; the workflow verifies Mathlib commit `fabf563a7c95a166b8d7b6efca11c8b4dc9d911f`. Both new modules, all listed inherited modules, the joint import, and each axiom driver execute with `--trust=0 -DwarningAsError=true`; error propagation remains active across pipelines and the accumulated new-source status.

The raw 29 new transitive reports exactly equal the manifest-selected JSON reports and contain only `propext`, `Classical.choice`, and `Quot.sound` (or a subset, including none). Their two source hashes equal the downloaded source bytes. All 40/68/38/87/73 inherited selected reports obey the same allowlist, and the structural checker reports 28 selected declarations. These inherited report counts are not a claim that every inherited theorem was freshly reviewed mathematically. Successful complete job steps also evidence the normal and optimized 25-test inherited suites, the normal and optimized eight finite calibrations, and both deliberate-negative controls. The local follow-up harness receipts correctly describe 31 tests in each mode with one deliberately excluded non-fetched derived-tree manifest test, which did execute successfully in exact-head CI.

The read-only log auditor was rerun successfully after reading its entire source; it rehashed all 18 fetched source/dependency files and independently parsed every report. Earlier failed development run statuses remain recorded in `ci_review/HISTORY_RECEIPT.json`; no earlier log diagnosis is inferred from a status-only receipt. The full review is passed at its stated formal, written-algebraic, and finite-test boundaries.
