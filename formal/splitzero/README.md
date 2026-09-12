# SplitZero: verified structural formalization

Four extension modules for the owner's split-zero construction: exact morphisms, semimodule support fibres, ideal classification, and a corrected presentation universal property.

## Verified checkpoint

GitHub Actions [run 34660929635](https://github.com/KokunoYumeto/zeta-function-research-reader/actions/runs/34660929635), job `103463090151`, succeeded for source commit `8196e4f4d4f09a8cfc8a4e8ce8683ded359adbf6`. The original core and all four extension modules built. Every extension source then passed a separate `lean --trust=0 -DwarningAsError=true` invocation; the original core was also checked with `--trust=0`. All **28 selected transitive axiom reports** passed the allowlist `propext`, `Classical.choice`, `Quot.sound`. This is not a claim of auditing every Mathlib declaration or the complete Zeta programme. Exact source hashes and artifact identity are in `VALIDATION.json`.

The nine synthetic checker tests in `test_axioms.py` passed locally against the downloaded successful artifact. They test missing/duplicate/extra reports and forbidden axioms; they are not mathematical proofs. The mathematical evidence is the Lean run.

## Source and authorship

The construction and source-level results are attributed to the owner's research programme. The original core is retrieved **unchanged** from `KokunoYumeto/modern-latex-manuscripts` commit `f7ff59b176c7dc3941babd4cb9272dffc653070d`, file `formalization/lean/classical_candidates_20260626/split_support_sidecar/SplitZero.lean`, Git blob `ff991f7383922e71cdf0e4a3bc85e89e18f808ef` (7,366 bytes). `prepare.py` rejects a byte mismatch.

The main mathematical source is Zeta chapter 14, `satellites/14_globalization_cue_split_zero_and_shifted_sheets.tex`, blob `49318a578b96462384000afa16794cfd5fe492c1`, at commit `42d00e359b16d52ca71568ce5e3db5341949d929`. Its support-idempotent, fibre-module and ideal-lattice statements are pre-existing manuscript results, not discoveries attributed to this implementation. See `MATHEMATICAL_NOTE.md` for proofs and source records.

Open PR #3, head `37b2cc9b9baee3ffe25a7649314adb025302509f`, develops the later Rees and adelic-comparison work. This package supplies part of its algebraic foundation; it does not certify the analytic comparisons, purity, positivity, or any RH claim. That PR and the frozen reader source remain unchanged.

## Modules

- `SplitZeroExtension.lean`: universal ring reflection; support equals the additive-idempotent locus; ideal classification and the order isomorphism onto non-bottom ideals.
- `SplitZeroFibres.lean`: a support join-semilattice with bottom; actual additive groups and R-modules on fibres; coherent linear transports and fibre-map naturality; disjoint-fibre decomposition and recovery of the original addition.
- `SplitZeroPresentation.lean`: Boolean support character and its uniqueness; a checked generator-level countermodel to the printed presentation; the corrected semiring-lift property.
- `SplitZeroMaps.lean`: no injective map into a ring; faithful amplitude/support coordinates with exact image; lifted ring maps; exact hom-set equivalence between split-to-split maps and ordinary ring maps.

The abstract reverse diagram construction and the full categorical equivalence are not yet implemented. The manuscript already proves them on paper. The formal countermodel is at the multiplicative-generator level; this package does not construct the free monoid-semiring congruence quotient.

## Two manuscript qualifications

1. The ordinary free monoid-semiring presentation in `prop:gcue-product-reconstruction` needs `[tau] = 0`. The printed relations alone admit the constant-one Boolean generator evaluation. Adding the missing zero relation makes the inverse a unital semiring map.
2. The ideal-order isomorphism targets the **non-bottom** ideal poset. In the full ambient ideal lattice, lifting preserves nonempty joins, not the empty join: lifting the zero ring ideal gives `{tau,e}`, not `{tau}`.

Neither correction discards the underlying construction. No global novelty or priority claim is inferred from successful formalization. Existing rights and attribution remain in force; the package does not relicense the surrounding repository.

## Reproduction

Requires Python 3.11+ and elan. From this directory:

```sh
python3 prepare.py
lake update
lake exe cache get
lake -KmaxJobs=1 build
lake env lean --trust=0 SplitZero.lean
for f in SplitZeroExtension.lean SplitZeroFibres.lean SplitZeroPresentation.lean SplitZeroMaps.lean; do
  lake env lean --trust=0 -DwarningAsError=true "$f"
done
lake env lean --trust=0 -DwarningAsError=true Audit.lean > Audit.log
python3 check_axioms.py Audit.log
python3 test_axioms.py -v
```

Lean is pinned to 4.31.0 and Mathlib to `fabf563a7c95a166b8d7b6efca11c8b4dc9d911f`. The code introduces no custom axiom or unfinished proof. The selected audit rejects nonstandard dependencies, including `sorryAx` and `Lean.ofReduceBool`.
