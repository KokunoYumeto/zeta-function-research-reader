# Dated mathematical bulletin — 23 September 2026

This is the local Connes–Consani/lattice component of the cross-session programme bulletin. Publication remains held. The stable IDs below identify proved local sources; they are not claims of public publication. The broader corpus/SGA/Deligne goal remains active. Full proofs, rather than this bulletin, are in the cumulative LaTeX reader.

## SZ-20260923-201 — The complete Gamma carrier and its two bounds

Proof: `independent/HG_FULL_SUPPORT.tex`, HG1–41 and HG21a–c. Exact joint image in HR × HL, all zero-coordinate fibres, pointed-fibre support joins, product support meets, fold-defect composition, bounded sections and sheaf stalks. Root has read the complete independent proof. A typesetting typo in HG19 was repaired without changing the statement.

Human source: Alain Connes and Caterina Consani, [Absolute algebra and Segal's Gamma sets, v2](https://arxiv.org/abs/1502.05585v2), original F1_corr.tex, `functsum`, `sssalg`, `sssalg2`, `propspecz`. Original source bytes and intact archive verified in GAMMA_FF_SOURCE_RECEIPTS.json. The full carrier comes from The Clankers, [Split Support Geometry v11, Definition def:lattice-split](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/a2851f9eb352e7e4376bc629de86fa4ed9c1c434/workbenches/splitzero-tandem/foundations/split-support-geometry-v11/split_support_geometry_arithmetic_curve_v11.tex#L1226).

The comparison strengthens the earlier scalar transport by calculating the full L-valued fibres. The old absolute-value ball and the later all-subset module retain different higher-arity bounds even where their level-one values agree. No replacement of either bound is made.

## SZ-20260923-202 — Full support dimension of the later bounded module

Proof: SUPPORTED_RIEMANN_ROCH_SECTIONS.tex, SRR1–8; independent complete proof SUPPORT_DIMENSION_REVIEW.tex, SDR1–15. For finite L, the compulsory proper join-irreducible labelled zeros give the exact correction to the integer generator count. Infinite L has no finite generator set. Both complete proofs have been read by root; exact finite checks accompany them.

Human source: Connes–Consani, [Riemann–Roch for the ring Z, v1](https://arxiv.org/abs/2306.00456v1), original RRZ.tex, `xlem`, `defnsum`, `sequencebleft`. This extends their explicit integer construction to the full specified lattice module. It does not assume that this module is a newly established divisor cohomology theory.

## SZ-20260923-203 — Divisor tensor law, degree and the complete morphism category

Proof: SUPPORTED_DIVISOR_MULTIPLICATION.tex, SDM1–13, and independent/SDM_MORPHISM_EXTENSION.tex, SDM14 onward. The original finite divisor coefficients and archimedean constants are retained. Rational-radius modules and their filtered colimits compute the full relative Day smash; two irrational radii with rational product yield exactly the strict boundary. Every labelled zero remains. The intrinsic additive-idempotence test recovers minus the original degree, with its exact endpoint. Every abstract module morphism is classified by the complete split scalar set of global sections for D'−D; composition meets zero labels. All isomorphisms and all endomorphisms are calculated explicitly.

Human source: Connes–Consani's v2 paper above, `propspecz`, `propsmash1`, `propsmash2`, `proppic`, source lines938–1053. This transports and extends their divisor construction to the full lattice; it corrects the naive nonzero-section test, which would count supported zeros at every bound. The degree test, morphism proof and zero-fibre retention are written in full locally. Root independent review repaired the finite-stalk proof to exclude every violating valuation prime, including negative divisor coefficients.

## SZ-20260923-204 — Verified repair of the classical circle steps

Proof: independent/SOURCE_FORMULA_CORRECTIONS.tex, SFC1–10, root-read completely. The actual negative-binary endpoint is retained. The finite-circle minimum is min(1/4,3·2^(-m)) for m≥2, and the periodic dyadic grid supplies the covering argument. The original dimension conclusion remains valid.

Human source: Connes–Consani's RRZ.tex, `sequenceb` and `caseh1`, lines309–338. This corrects two intermediate steps without claiming the theorem is false. The initially suspected endpoint defect was retracted after exact substitution; the source's endpoint was correct.


## SZ-20260923-205 — Full-lattice arithmetic-site extension

Complete root-read proof: independent/ARITHMETIC_SITE_LATTICE_MAP.tex, ASL1–35.

Every characteristic-one map factors through the actual support map. K⊗_B L retains all labels through the complete family of lattice characters. Exact points, stalks, Frobenius and arithmetic pullback are constructed.

Sources and relation to earlier results: [Connes–Consani, Geometry of the Arithmetic Site, v1](https://arxiv.org/abs/1502.05580v1), source site618–622, structure2 626–659, defnpt685–690 and thmspz951–961; [The Clankers, Split Support Geometry v11, def:lattice-split](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/a2851f9eb352e7e4376bc629de86fa4ed9c1c434/workbenches/splitzero-tandem/foundations/split-support-geometry-v11/split_support_geometry_arithmetic_curve_v11.tex#L1226). This replaces earlier scalar-only coefficient transport by the full lattice map.


## SZ-20260923-206 — Complete finite-lattice tropical prime spectrum

Complete root-read proof: independent/TROPICAL_LATTICE_PRIME_SPECTRUM.tex, LSP1–37.

For L=Down(J), every prime of the antitone-function semiring is p_(j,U), where U is an upset of down(j) containing j. All prime inclusions, stalks, subtractive primes, full-base contractions and lattice-map naturality are proved. A chain with n join-irreducibles has n(n+1)/2 primes and dimension2n−2.

Sources and relation to earlier results: [Connes–Consani, Geometry of the Arithmetic Site, v1](https://arxiv.org/abs/1502.05580v1), characteristic-one coefficients331–407; ASL18–22 is the complete local connecting proof in this reader. This strengthens205 by retaining the ordinary tropical primes beyond evaluation kernels.


## SZ-20260923-207 — Complete absolute-curve point correspondence

Complete root-read proof: independent/ABSOLUTE_CURVE_FULL_SUPPORT.tex, ACF1–32.

The exact full-base pullback, all labelled zero branches, coherent nonzero root sequences, local archimedean/p-adic families, their overlap and the intermediate group-algebra coequalizer are computed. The generic-stalk discrepancy is connected by an explicit augmentation.

Sources and relation to earlier results: [Connes–Consani, On the Absolute Geometry of Spec Z and the Fargues–Fontaine curve, v1](https://arxiv.org/abs/2606.06604v1), prop12 356–370, classpla549ff, defnloc693–774, archimedean points1465–1500 and p-adic points1643–1659; [The Clankers, Split Support Geometry v11, def:lattice-split](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/a2851f9eb352e7e4376bc629de86fa4ed9c1c434/workbenches/splitzero-tandem/foundations/split-support-geometry-v11/split_support_geometry_arithmetic_curve_v11.tex#L1226).


## SZ-20260923-208 — The assembled spherical/tropical/full-support sheaf

Complete root-read proof: independent/FULL_SUPPORT_SHEAF_COMPARISON.tex, FSC1–34.

C=O_X×_(j_*O_D(e)) r^-1 T_L is computed on every open and stalk. Its spherical injection, fixed sheaf, support ideal, ring reflection and all intermediate quotient maps are proved. C→O_X has a unital sheaf section exactly for the two-element L. The pullback with support stalk G_L(Q) is retained separately from its exact supported image with stalk L.

Sources and relation to earlier results: [Connes–Consani, On the Absolute Geometry of Spec Z and the Fargues–Fontaine curve, v1](https://arxiv.org/abs/2606.06604v1) and [Connes–Consani, Geometry of the Arithmetic Site, v1](https://arxiv.org/abs/1502.05580v1), with exact inputs ASL32–35 and ACF1–10 in the same complete reader. This joins205 and207 and corrects the earlier candidate support-stalk identification.


## SZ-20260923-209 — Actual full-support Cartier unit quotient

Complete root-read proof: independent/FULL_LATTICE_CARTIER_QUOTIENT.tex, FCQ1–29.

The actual unit action fixes all z_λ. Equal-valuation addition is computed exactly: its upper endpoint is absent for residue F2 and present for larger residue fields. The cyclotomic source has algebraically closed residue field and retains the closed interval. All divisor bounds, scaling and support stalks are retained.

Sources and relation to earlier results: [Connes–Consani, Geometry of the Arithmetic Site, v1](https://arxiv.org/abs/1502.05580v1), hyper987–1001 and sheavesonspz1003–1024; Jean-Pierre Serre, Corps locaux, the cyclotomic valuation result identified in FCQ18. This extends the unit-quotient construction through the full base and corrects its finite-stage residue-F2 scope.


## SZ-20260923-210 — Original receiver locality and full tensor sectors

Complete root-read proof: independent/OPERATOR_LOCALITY_PRIME_RECEIVER.tex, OLR1–31.

The exact matrix p-locality criterion is proved and applied to every original spectral label and cutoff. Even centred tensor degrees retain phase-cancellation sectors; the original mass remains. The original nilpotent tensor kernel, compression-return identity and full lattice lifts are calculated.

Sources and relation to earlier results: [Connes–Consani, On the Absolute Geometry of Spec Z and the Fargues–Fontaine curve, v1](https://arxiv.org/abs/2606.06604v1), defnloc693–774. Original public receiver: [033, SBT1–23](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/3c78cfbd9e194d35117b33277c421c6564ce3dbf/workbenches/splitzero-tandem/continuations/20260923-full-prime-support/033/MIXED_PRIME_ENERGY_AND_BOUNDARY.tex). This strengthens the one-factor locality calculation; tensor cancellation does not establish arithmetic purity.


## SZ-20260923-211 — Every nilpotent ladder in the original metric

Complete root-read proof: independent/MIXED_TENSOR_NILPOTENT_LADDERS.tex, OLM1–28.

Every primitive projector, Jordan block multiplicity and ladder inverse is explicit. The unchanged power vectors have exact norm ε^(2a) a! d!/(d−a)! times the primitive norm. All complex exponential Gram entries, displacement energies, global singular values and support lifts are proved.

Sources and relation to earlier results: Exact programme inputs are OLR13 and OLR28–31 in this reader and the retained complete TDP derivation. No SGA or Deligne theorem is invoked here. This strengthens210 from kernel dimensions to the complete original-metric nilpotent object.
