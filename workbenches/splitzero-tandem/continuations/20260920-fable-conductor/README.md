# Four ES–Fable labels in the original weighted conductor

This source edition solves the inverse problem for the four-dimensional ES–Fable map and constructs its exact receiving maps in the original Split-Zero weighted conductor. The complete proofs are in **FABLE_TO_ORIGINAL_CONDUCTOR.tex**, equations FC1–71 and GF1–28; independent complete derivations and exact symbolic certificates accompany it.

The four distinguished Time/root labels remain separate. The full polynomial fibre in the chosen affine chart consists of seven points, representing seven of eight resultant-one factor-sign states over those four roots. All seven transported points map to the explicit polynomial `2i y_M` in the original conductor target. An exact escaping branch proves that this value is nonproper for the transported nonlinear map. The original linear conductor stays invertible, and the nonlinear map's full correction for the original translation action is computed.

The source preserves the original period matrix, Taylor unit, coefficients, quotient, Gamma masses, phases and operator. It does not assert a counterexample to RH or a failure of the linear inverse-exterior bound.

The global continuation classifies every fibre, including repeated roots, and gives the entire image complement as an explicit square-quartic surface. The nonproper-value locus is exactly `u0 Disc(H)=0`; its complement carries the actual finite degree-eight inverse correspondence. Each root of the literal original quartet gives two explicitly calculated signed states. Their common square-quartic limit has no preimage, and all eight escaping branches have an exact quarter-power distance law in a fixed original conductor norm.

At the earlier seven-point target, every exterior inverse and all four singular values are evaluated. Their rates are epsilon^-4, epsilon^-1, epsilon, epsilon^4 with complete positive original-metric constants. The limiting singular flags, fixed Fable-flag volume distortions, and exact cross-Gram slack between those flag volumes and the operator bound are proved. Differentiated conjugacy carries these results through the original conductor, retaining the actual factor controlled by audit equation (11).

## Reading and verification

- `FABLE_TO_ORIGINAL_CONDUCTOR.tex`: complete principal proof, including the global inverse classification, actual-quartet branches, both escape mechanisms, complete original-metric singular spectrum, flags and conductor return.
- `independent/FOUR_LABELS_AND_CONDUCTOR_ORDER.tex`: full labelled collision algebra and exact conductor order strata.
- `independent/ACTUAL_FOUR_PLANE_METRIC_AND_CONJUGACY.tex`: independent original-metric restriction, conjugacy and exhaustive fibre proof.
- `independent/TRANSLATION_DEFECT_OF_TRANSPORTED_MAP.tex`: full Jacobian and exact original-action correction.
- `independent/GLOBAL_FIBRE_AND_NONPROPER_LOCUS.tex`: complete global inverse, all multiplicity cases, exact image complement, nonproper locus and actual-quartet escape proof.
- `independent/ESCAPE_SPECTRUM_AND_METRIC.tex`: independent complete original-metric differential, exterior, singular-spectrum and flag-volume proof.
- Run `python verify_transport.py` for the labelled maps, full-degree rank, inverse recurrence and finite order-stratum checks.
- Run `python independent/verify_seven_fibre.py` for the complete polynomial identities, all seven points, both involutions and their factor-coordinate action. It also runs the imported original four-point determinant certificate. Python with SymPy is required; these checks use exact arithmetic, not floating-point sampling.
- Run `python independent/verify_global_fibre.py` for the full inverse parameterization, structural Jacobian proof, omitted surface and literal-quartet formulas.
- Run `python independent/verify_escape_spectrum.py` for an independently transcribed polynomial, both inverse products, all compound matrices and the exact velocity identity.
- `python derive_escape_differential.py` gives the root's separate full Laurent-matrix calculation and every compound leading coefficient.

## Provenance

The canonical 488-page Erdős–Straus reader, source version69, supplies the displayed quartic map and four distinguished points at theorem `explicit-four-time-Jacobian-collision`. The ES–Fable continuation supplies the four Time locales and their tetrahedral coordinate matrices. WCF1–6 supplies the unchanged original weighted conductor; NC1–5 and DFX4–5 supply its period and exponential maps. Exact citations and the canonical reader source hash appear in the proof. The seven-point fibre, missing eighth factor-sign state, explicit original-norm transport, escaping branch and translation correction are derived in this edition, not attributed to the original source.

The original three-dimensional Fable example was announced by Levent Alpöge and reproduced by Terence Tao. The source distinguishes that example from the later four-dimensional ES construction. The original Gamma polynomial dictionary retains the contributions of T. H. Koornwinder, R. Wong, R. Koekoek, R. F. Swarttouw and W. P. Reinhardt in NIST DLMF Chapter18.

Mathematical bulletin identifiers: SZ-20260920-001 through SZ-20260920-006. This packet contains nineteen files, including the manifest. Private logs and machine-specific source paths are excluded.
