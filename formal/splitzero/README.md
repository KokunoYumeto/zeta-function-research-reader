# SplitZero: structural formalization

This is a bounded formalization of the owner's split-zero construction, not a claim that the entire Zeta programme or category equivalence is formalized. The source of truth for validation is an exact successful CI run at a named commit; initial scripts remain under development until then.

## Mathematical source and attribution

The construction and source-level theorems belong to the owner's research programme. The existing core is retrieved unchanged from `KokunoYumeto/modern-latex-manuscripts` commit `f7ff59b176c7dc3941babd4cb9272dffc653070d`, file `formalization/lean/classical_candidates_20260626/split_support_sidecar/SplitZero.lean`, Git blob `ff991f7383922e71cdf0e4a3bc85e89e18f808ef` (7,366 bytes). `prepare.py` fails on any mismatch.

The principal mathematical source is `satellites/14_globalization_cue_split_zero_and_shifted_sheets.tex`, Git blob `49318a578b96462384000afa16794cfd5fe492c1`, in Zeta commit `42d00e359b16d52ca71568ce5e3db5341949d929`. Its `lem:gcue-all-idempotents`, `lem:gcue-fibre-modules`, and `thm:gcue-ideal-lattice` are formalization targets, not newly discovered mathematics. The semimodule equivalence is already proved in the manuscript; only its forward construction and object-level reconstruction are covered here.

PR #3, head `37b2cc9b9baee3ffe25a7649314adb025302509f`, contains the later Rees and adelic-comparison continuation. Its opening Rees note was read for scope; none of its analytic claims or formal-equivalence claims is newly certified here.

## Included

- `SplitZeroExtension.lean`: universal ring-reflection factorization, intrinsic support/idempotent characterization, exact ideal classification and order isomorphism to non-bottom ideals.
- `SplitZeroFibres.lean`: support join-semilattice with bottom; actual additive groups and ring modules on fibres; coherent linear transports; fibre-map naturality; underlying-set decomposition and recovery of addition.
- `SplitZeroPresentation.lean`: an explicit Boolean semiring, uniqueness of the support character, a multiplicative-generator countermodel to the uncorrected presentation, and the corrected semiring-lift universal property.
- `Audit.lean`: explicit transitive axiom reports for 22 central declarations. The checker rejects missing, duplicate, or nonstandard reports. This is a selected-declaration audit, not a claim of globally auditing all Mathlib.

## Two precise manuscript qualifications

1. In `prop:gcue-product-reconstruction`, the quotient of the ordinary free monoid semiring needs the additional relation `[tau] = 0`. The printed relations alone admit the constant-one Boolean generator evaluation: every generator maps to one, all printed relations hold, but `[tau]` maps to one rather than zero. Adding `[tau] = 0` makes the proposed inverse preserve the semiring zero. The formal countermodel is at the multiplicative-generator level; a `RingCon` quotient is not constructed here.
2. The ideal-order isomorphism targets the non-bottom ideal poset. Arbitrary joins there are preserved, but in the full ambient ideal lattice only nonempty joins are preserved. In particular, lifting the zero ring ideal gives `{tau,e}`, not `{tau}`. The empty-join qualification is necessary.

No existing chapter text or frozen edition is changed automatically; these are explicit correction notes for review. The underlying construction is not discarded.

## Reproduction

Use Python 3.11+ and elan. From this directory:

```sh
python3 prepare.py
lake update
lake exe cache get
lake -KmaxJobs=1 build
lake env lean --trust=0 SplitZero.lean
for f in SplitZeroExtension.lean SplitZeroFibres.lean SplitZeroPresentation.lean; do
  lake env lean --trust=0 -DwarningAsError=true "$f"
done
lake env lean --trust=0 -DwarningAsError=true Audit.lean > Audit.log
python3 check_axioms.py Audit.log
```

Lean is pinned to 4.31.0 and Mathlib to `fabf563a7c95a166b8d7b6efca11c8b4dc9d911f`. No theorem is replaced by an assumed conclusion. The original source is kept separate and unchanged. Existing rights and attribution remain in force; this addition does not relicense the Zeta repository.
