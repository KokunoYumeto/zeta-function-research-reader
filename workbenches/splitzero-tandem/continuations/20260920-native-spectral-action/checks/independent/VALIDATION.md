# Exact finite validation

The complete proof is RANK_ONE_METRIC_CURVATURE.tex, MC1–MC35.

- TeX SHA-256: 355c050f66fa2676093291f455e5aef3b0ab6e350e35203de4ac64ddeed610ee.
- Main checker SHA-256: 65b054eca7aa6b8d2d59768ab4a847e789954e41e568be2c114968bc43760b95.
- Quartic checker SHA-256: 44bd51a74b74e5594a4bad3350504e1f575d8ea32e2142f276f22675b7d4136a.

Python with SymPy 1.13.1 was run with -B -X utf8 and again with -B -O -X utf8.

check_metric_curvature.py passed 213 exact identity checks and rejected 20 deliberately wrong formulas in each mode. It checks six nonidentity-metric complex examples in dimensions 2, 3 and 4, all signs and mixed terms, complete characteristic polynomials, the exact left and right resolvents, and the sharp aggregate example.

check_quartic_coefficient.py passed 10 exact identities and rejected 2 deliberately wrong formulas in each mode. It retains both the complex-phase and the sharp-real examples.

Totals per mode: **223 exact identity checks, 22 negative controls**.

Normal and optimized main receipts have the identical SHA-256 1fa66d5094390673df94b93d179fd6d6d70e7c6ed3830b1938ad97ebb4848551.

Normal and optimized quartic receipts have the identical SHA-256 fe03fce8c1f180dcb3129ea83a2cbd4530e40ff469b524fa6359815736a979a2.

The proofs, rather than these examples, establish the finite formulas for every matrix in their stated domains. The scripts do not certify a growing-packet asymptotic, any actual zeta zero, or any physical interpretation.

No TeX compilation, PDF generation, or visual validation was performed by this child; these tasks were outside its derivation-only assignment.
