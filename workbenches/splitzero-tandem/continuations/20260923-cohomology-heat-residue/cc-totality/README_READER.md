# Full lattice geometry in the Connes–Consani programme

The current cumulative component is [FULL_LATTICE_CC_READER.pdf](FULL_LATTICE_CC_READER.pdf), with complete build source [FULL_LATTICE_CC_READER.tex](FULL_LATTICE_CC_READER.tex). It develops divisors, arithmetic sites, absolute curves, twistor maps and spectral receivers over the entire split-support lattice. This local component belongs to the active Connes–Consani/SGA/Deligne synthesis. This is the frozen 103-page public component; later calculations are separate additions.

The controlling carrier is G_L(R) = {(0,λ): λ∈L} ∪ (R×{1_L}), for arbitrary bounded distributive L. Its operations are (r,λ)+(s,μ)=(r+s,λ∨μ) and (r,λ)(s,μ)=(rs,λ∧μ). The joint amplitude/support map retains every label, including τ=(0,0_L) and e=(0,1_L). The tropical extension K⊗_B L retains the complete support character family. The prime classification states its finite-L hypothesis explicitly. The sheaf fibre product uses these exact maps throughout.

## Proof map

| Source | Exact proof locators and contents |
|---|---|
| independent/ARITHMETIC_SITE_LATTICE_MAP.tex | ASL1–35: universal support map, tropical coefficients, points, stalks and Frobenius |
| independent/TROPICAL_LATTICE_PRIME_SPECTRUM.tex | LSP1–37: all finite-lattice tropical primes, localizations, naturality and prime contractions |
| independent/ABSOLUTE_CURVE_FULL_SUPPORT.tex | ACF1–32: complete base-labelled character object, local families and connecting maps |
| independent/FULL_SUPPORT_SHEAF_COMPARISON.tex | FSC1–34: exact sheaf fibre product, spherical injection, fixed sheaf and section obstruction |
| independent/HG_FULL_SUPPORT.tex | HG1–41 and HG21a–c: full Gamma carrier, cancellation and the two original bounds |
| SUPPORTED_RIEMANN_ROCH_SECTIONS.tex | SRR1–8: exact support dimension of the bounded section module |
| SUPPORTED_DIVISOR_MULTIPLICATION.tex and independent/SDM_MORPHISM_EXTENSION.tex | SDM1–21: divisor multiplication, degree, every morphism and every isomorphism |
| independent/FULL_LATTICE_CARTIER_QUOTIENT.tex | FCQ1–29: actual unit orbits, residue-F2 distinction and full support localization |
| independent/SOURCE_FORMULA_CORRECTIONS.tex | SFC1–10: verified circle repairs preserving the source dimension theorem |
| reader_fragments/TWISTOR_SPLIT_CHART_POINTS.tex | CSP1–28: complete labelled charts, real involution and signed maps |
| reader_fragments/SIGNED_HOPF_AND_ADAMS.tex | HA1–29: actual torsor morphisms and ordinary/equivariant Adams comparison |
| reader_fragments/TWISTOR_TO_ORIGINAL_BOUNDARY.tex | TOB1–29: original receiver, metrics, observation kernel and complete boundary window |
| reader_fragments/TWISTOR_PRIME_TRACE.tex | TPT1–28: labelled prime traces, determinants and exact receiver recovery |
| independent/OPERATOR_LOCALITY_PRIME_RECEIVER.tex | OLR1–31: locality, all tensor labels and complete nilpotent kernel |
| independent/MIXED_TENSOR_NILPOTENT_LADDERS.tex | OLM1–28: every Jordan block, primitive projector, ladder inverse and exponential Gram entry |

The mathematical owner reports reading all these proofs. Bounded original-literature reading coverage is stated separately in the sources and private use ledger; this reader does not claim exhaustive corpus reading or an established arithmetic purity theorem.

## Human sources and originating programme sources

Alain Connes and Caterina Consani: [Absolute algebra and Segal's Gamma sets, v2](https://arxiv.org/abs/1502.05585v2); [Riemann–Roch for the ring Z, v1](https://arxiv.org/abs/2306.00456v1); [Geometry of the Arithmetic Site, v1](https://arxiv.org/abs/1502.05580v1); [On the Absolute Geometry of Spec Z and the Fargues–Fontaine curve, v1](https://arxiv.org/abs/2606.06604v1); and [The Absolute Twistor Line, v1](https://arxiv.org/abs/2609.00299v1). Each application gives precise original-TeX locators. Original author sources and intact archives remain separately preserved; the present proofs are programme derivations.

The full lattice carrier is from The Clankers, [Split Support Geometry v11, Definition def:lattice-split](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/a2851f9eb352e7e4376bc629de86fa4ed9c1c434/workbenches/splitzero-tandem/foundations/split-support-geometry-v11/split_support_geometry_arithmetic_curve_v11.tex#L1226). The earlier scalar supported-zero prime-chain credit to Gemini 2.5 Pro is preserved. The original receiver and complete boundary map are in [programme result033, SBT1–23](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/3c78cfbd9e194d35117b33277c421c6564ce3dbf/workbenches/splitzero-tandem/continuations/20260923-full-prime-support/033/MIXED_PRIME_ENERGY_AND_BOUNDARY.tex). The accompanying publication manifest identifies this exact edition. The complete earlier TDP derivation is retained in inputs/TAU_DELiGNE_PRIME_MEMORY.tex as a local programme source, not an original Deligne source.

## Build, figures and verification

Run `pdflatex -interaction=nonstopmode -halt-on-error FULL_LATTICE_CC_READER.tex` three times for a fresh build from this directory; subsequent builds need enough passes for references to stabilize. All TeX inputs and figure PDFs are local relative paths. Required packages are listed in its preamble. The current build has103 pages. This directory and the combined source archive contain the complete TeX build inputs, figure sources and verification scripts; private correspondence, requests and reading logs are excluded.

Reproducible figures: draw_full_lattice_maps.py, draw_tensor_sectors.py, bind_sources_and_figures.py and render_support_dimension.py. Rendered PDF, PNG and SVG figures are retained. The first figure draws the exact three-element-chain specialization and all its prime-contraction fibres; the full proof treats arbitrary L where stated. render_cc_reader.py renders every page for inspection. The older bound-figure script also verifies original archives and requires requests/network access for that separate verification step.

CC_READER_QA_RECEIPT.json records actual review coverage, final file hashes and typesetting diagnostics. Independent finite checks supplement the complete proofs. The earlier25-page Gamma reader remains retained as a prior component. Wider corpus, SGA6, SGA7 and Deligne applications remain active work.
