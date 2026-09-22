# Split-Zero cohomology and the zeta-function research programme

This project brings together complete mathematical papers, editable LaTeX proofs, formalization, calculations and human-source literature notes. Its central question is how to study the zeros of the Riemann zeta function through explicit arithmetic cohomology, spectral actions and quantitative metric estimates. The collection also retains the connected fluid, heat-flow, arithmetic-trace, complexity and thermal-geometry investigations that helped motivate the programme.

[Read the Zenodo collection](https://doi.org/10.5281/zenodo.22678085) · [Split-Zero mathematical workbench](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/README.md) · [Machine-readable workbench index](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/WORKBENCHES.json) · [Contribution guide](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/POLYCLANK_PARTICIPATION.md)

## The central construction

Split-Zero coefficients retain the internal zero of a ring and a separate symbol for absence. A zero element in a specified support fibre therefore stays in that fibre. The programme constructs the corresponding coefficient, quotient and homology maps rather than identifying these different objects without a map.

The analytic source is a theta complex `[V → B]`: theta summation maps the specified test functions into a function space, and cohomology is the quotient `B/ΘV` by those actual theta relations. Scaling acts by `D = −x∂x`. Mellin transformation connects this construction to `2ξ(s)`, where `ξ` is the completed Riemann zeta function. Finite spectral packets retain their full multiplicities and derivative data. Their source maps, quotient maps and least-norm metrics are calculated explicitly.

Deligne's Weil II motivates the cohomology–duality–weight-control approach. The finite-field theorem is not being asserted to apply automatically to this arithmetic construction. The [foundational programme guide](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/RESEARCH_PROGRAMMES.md) gives the original objects and maps.

## What is in the project

| Area | Contents and purpose | Read |
| --- | --- | --- |
| Split-Zero geometry and cohomology | Support-preserving coefficients, homology, source relations, Rees constructions, finite spectral jets, theta recovery and chain homotopies. These connect finite observations to the original infinite quotient. | [Foundations](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/RESEARCH_PROGRAMMES.md), [cohomology paper](https://zenodo.org/records/22865640/files/10-splitzero-cohomology-and-weight-control.pdf?download=1) |
| Arithmetic analytic estimates | Mellin and Gamma estimates, tensor and exterior constructions, orthogonal-polynomial kernels, Hankel–Toda determinants, residue and period maps, boundary compensation and growing-degree volume/covariance calculations. | [Cumulative Split-Zero reader](https://zenodo.org/records/22865640/files/92-splitzero-cited-receiver-reader.pdf?download=1), [proof companion](https://zenodo.org/records/22865640/files/94-splitzero-cited-receiver-companion.pdf?download=1), [corrected cumulative LaTeX](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/666ee448d5ecb0bf8a4888f3a2aceaaa5c74d6d8/workbenches/splitzero-tandem/continuations/20260921-historical-proof-citations/README.md) |
| Conductor and spectral geometry | Original relation maps, kernels, quotient volumes, real-period resonances, inverse spectra and finite observation bounds. Geometric examples keep their stated relation to the arithmetic problem. | [Native spectral and real-period papers](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/0fd693c844aad9117e30ec447c59864a28af10f3/workbenches/splitzero-tandem/continuations/20260921-native-spectral-real-pair/README.md), [directions and inverse-power papers](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/689a8f87e9c12b7a99b01b3123438c6751ee608f/workbenches/splitzero-tandem/continuations/20260921-directional-inverse-power/README.md) |
| Formalization and reproducibility | Lean sources for specified algebraic and homological interfaces; exact finite checkers, numerical and interval calculations, reproducible figures, manifests and verification records. Each retains its actual scope. | [Formal sources](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/main/formal/splitzero), [formalization account](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/formal/splitzero/DERIVED_MATHEMATICS.md) |
| Zeta literature and connected routes | Separate readers on zeta, fluid/Navier–Stokes mechanisms, de Bruijn–Newman heat flow, Connes/arithmetic traces, geometric complexity, and vacuum/thermal geometry. They preserve attempted connections as well as completed calculations. | [Zeta](https://zenodo.org/records/22865640/files/01-main-reader.pdf?download=1), [fluid](https://zenodo.org/records/22865640/files/02-fluid-reader.pdf?download=1), [heat](https://zenodo.org/records/22865640/files/03-heat-reader.pdf?download=1), [arithmetic traces](https://zenodo.org/records/22865640/files/04-connes-reader.pdf?download=1), [complexity](https://zenodo.org/records/22865640/files/05-gct-reader.pdf?download=1), [vacuum](https://zenodo.org/records/22865640/files/06-vacuum-reader.pdf?download=1) |
| Related calculations | Unified Flow studies specified black-hole, thermal, spectral-zeta and geometric-flow probes. The CUE map connects existing random-unitary-matrix, Mellin and finite-phase-space work. | [Unified Flow](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/main/workbenches/unified-flow), [calculation paper](https://zenodo.org/records/22865640/files/09-unified-flow-calculations.pdf?download=1), [CUE map](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/CUE_RESEARCH_MAP.md) |

## Results, sources and limits

The repository is an ongoing research programme, not a claimed proof or disproof of RH or the other major conjectures discussed in its connected notes. The individual papers identify their completed constructions, remaining estimates, actual hypotheses and verification. Finite observation bounds are not silently promoted to uniform bounds; geometric spectral examples are not silently identified with arithmetic zeros.

The mathematical text retains the original coordinates, masses, signs, multiplicities, relation spaces and metrics. Human citations and exact source locators stay with the arguments. [Clickable programme references](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/666ee448d5ecb0bf8a4888f3a2aceaaa5c74d6d8/workbenches/splitzero-tandem/continuations/20260921-historical-proof-citations/REFERENCES.md) lead to the actual proof files. A public reconstruction is not presented as the private original. A Lean check, finite regression and analytic proof remain distinct forms of evidence.

Zenodo preserves separately readable papers and their source archives; GitHub provides the working source collection. Each DOI and pinned commit identifies a specific included source cut. The [workbench index](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/WORKBENCHES.json), per-edition result maps and manifests retain dependencies and checking scope. Older source notes describe their own editions, not automatically the newest state of every calculation.

## Current publication update

[Published cumulative Zenodo edition](https://zenodo.org/records/22902002) (assigned DOI 10.5281/zenodo.22902002) retains the whole research programme and adds the 10-page original terminal-response paper, with complete LaTeX, human citations and exact proof links. All 77 earlier PDFs remain separate.

### Original terminal arithmetic response

The Split-Zero programme carries finite zero classes of the completed Riemann zeta function through its arithmetic theta source, quotient metric and conductor observation. This continuation calculates two distinct amplification rates in the response of the original terminal eigenclass, rather than only their product. For the two original boundary rows, log α = 2qψ(t_N) + O(k log q), while 0 ≤ log β = O(k + log q). The complete proofs retain the original four cutoffs and period restrictions.

Read the [10-page illustrated paper](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260922-terminal-response/TERMINAL_RESPONSE_READER.pdf), [complete reader LaTeX](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260922-terminal-response/TERMINAL_RESPONSE_READER.tex), [results and programme uses](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260922-terminal-response/RESULTS_20260922_027.md) and [machine-readable proof index](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260922-terminal-response/RESULT_INDEX.json).

In the actual observation metric, the terminal class approaches an explicitly constructed maximal isotropic hyperplane for the current form. Its canonically phased positive- and negative-current amplitudes have coherence deficit at most exp[−2qψ(t_N) + O(k log q)]. The diagonal current correction has the same absolute error bound. The original imaginary cross-coordinate remains in the exact current formula; its sign is not evaluated by these magnitude estimates. These are results on the full previously stated conductor domain, not a conclusion about RH.

Both complete derivations, all 15 owner files and the complete preceding source bank with seven additions are included. Full LaTeX, human citations, figure sources and the original verification reports accompany them. Exact finite checks and noninterval numerical diagnostics retain their separate scopes; no actual native-period numerical evaluation is claimed.

[Published cumulative Zenodo edition](https://zenodo.org/records/22901724) (assigned DOI 10.5281/zenodo.22901724) retains the whole research programme and adds the 65-page original-current and effective-cutoff paper, with complete LaTeX, human citations and exact proof links. All 76 earlier PDFs remain separate.

### Original arithmetic current and effective cutoff control

The Split-Zero programme studies the arithmetic theta source, its quotient and the original conductor observation. This edition connects the kernel-volume profile to the observed arithmetic-current growth profile through exact integral maps. Complete finite Gamma and localization estimates control actual source increments, every original kernel constraint, complete fixed subquotients and shrinking cutoff windows.

Read the [65-page illustrated paper](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260922-current-effective-cutoff/CURRENT_AND_CUTOFF_READER.pdf), [complete reader LaTeX](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260922-current-effective-cutoff/CURRENT_AND_CUTOFF_READER.tex), [results and programme uses](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260922-current-effective-cutoff/RESULTS_20260922_026.md) and [machine-readable proof index](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260922-current-effective-cutoff/RESULT_INDEX.json).

The two nonzero observed-current eigenvalues have opposite signs, with logarithmic magnitude qψ(t)+O(k log q). The intrinsic first-order evolution has a four-cutoff logarithmic condition-number coefficient 4 log(4/π)−1/2, with error O(k log q). Complete evolution retains the exact hidden-source Volterra term. Original metrics, admitted period, stipulated simple quartet, invariant rows and all four cutoffs remain in the proofs.

For the separately prescribed terminal eigenclass, RC35–44 imports the earlier conductor theorem with γ≥1000δ and its full original period restrictions. It proves the observed/full norm comparison, bounds the normalized marked current by exp[O(k log q)], and shows exponentially balanced weights in the two observed sign eigenspaces. The residual individual sign remains in the exact complex pairing RC32; it is not assigned by the two opposite eigenvalue signs. No RH conclusion is claimed.

Both incoming proofs, four complete receiving derivations, all 19 final owner files and the unchanged preceding source bank with 34 additions are included. Human-source equation TeX, exact source-use records, reproducible checks and the full editable reader accompany the publication. Reported finite and scalar checks retain their separate scopes; they are not native-period numerical evaluations.

[Published cumulative Zenodo edition](https://zenodo.org/records/22895296) (assigned DOI 10.5281/zenodo.22895296) retains the whole research programme and adds the 26-page complete original cutoff-profile paper, with full LaTeX, human citations and exact proof links. All 75 earlier PDFs remain separate.

### The original kernel across the complete cutoff window

The Split-Zero programme studies the arithmetic theta source, its quotient and the original conductor observation. This addition evaluates how the entire original kernel spectrum and volume change as the polynomial source cutoff moves across its window. It retains the original metric, fixed period, stipulated simple quartet and complete source minima. The earlier four-cutoff coefficient is recovered within this full profile.

Read the [26-page illustrated paper](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260922-cutoff-profile/CUTOFF_PROFILE_READER.pdf), [complete reader LaTeX](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260922-cutoff-profile/CUTOFF_PROFILE_READER.tex), [results and programme uses](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260922-cutoff-profile/RESULTS_20260922_025.md) and [machine-readable proof index](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260922-cutoff-profile/RESULT_INDEX.json).

The complete proofs cover every original kernel direction and cutoff, actual rank-one source increments, specified complete fixed subquotients, uniform moving-ratio Gamma and jet estimates, and a convergent elliptic endpoint correction through degree five. The half-volume cutoff is certified between 0.28581630680480845015 and 0.28581630680480845016. The measured phase is calculated for arbitrary cutoff pairs. Original heat estimates retain the full angle defect and conductor-to-invariant compression; the scalar smoothing error is bounded by a constant divided by q, with exact transport and physical Euler-constant bias.

The unchanged previous source bank, 25 new source blocks, four complete proof files, check scripts, original human-author equation TeX and reading-use records accompany the paper. Reported finite verification covers 866 exact checks, four negative controls and 16 independently certified incoming scalar intervals; the separate supplied 59-check report is not represented as replayed because its executable was absent. Individual complex arithmetic-current signs remain unfinished. This addition does not claim RH.

[Published cumulative Zenodo edition](https://zenodo.org/records/22893050) (assigned DOI 10.5281/zenodo.22893050) retains the whole research programme and adds the 35-page original-kernel coefficient and measured-frequency paper, with complete LaTeX, human citations and exact proof links. All 74 earlier PDFs remain separate.

### Original kernel coefficient and measured frequency return

[Read the 35-page paper](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260922-kernel-frequency/KERNEL_AND_FREQUENCY_READER.pdf) · [Complete LaTeX](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260922-kernel-frequency/KERNEL_AND_FREQUENCY_READER.tex) · [Results and earlier calculations strengthened](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260922-kernel-frequency/RESULTS_20260922_024.md) · [Machine-readable proof locations](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260922-kernel-frequency/RESULT_INDEX.json).

The Split-Zero programme studies the arithmetic theta source, its quotient and its observation through determinant and heat estimates. This edition evaluates the previously unassigned original kernel determinant coefficient on the retained fixed-period simple-quartet domain: k≡1 mod4, k≥17, q=(k+1)² and m=8k−16. At cutoffs q−1,q,2q−1,2q with signs +,+,−,−, its return is m C_boundary q+o(kq). Complete growing-jet and Gamma proofs support the evaluation, and the elliptic constant satisfies 10.83425590260233706 < 8 C_boundary < 10.83425590260233707 by outward integer arithmetic.

The paper controls the measured determinant uniformly over positive regularizers and the entire measured phase in integral norm, retaining both frequency ends. It proves sharp finite phase/derivative bounds and restores a missing outer factor two in the incoming two-response explanation without changing its displayed response combination. CK, PJ, EL, PT and SF proofs, editable LaTeX, checkers, exact reading records and human citations are included. The full 022 source bank is unchanged, followed by 48 blocks including the 023 first-layer work and all six new arrivals.

These results update the earlier kernel-coefficient status on this stated domain; the separate complex arithmetic-current values/signs remain unfinished. This is not a proof of RH. [Source identities and reading coverage](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260922-kernel-frequency/SOURCE_READING_USE_LEDGER.json) distinguish human sources, programme derivations, incoming claims and executed checks. All previous editions and whole-project descriptions remain intact.

[Published cumulative Zenodo edition](https://zenodo.org/records/22887380) (assigned DOI 10.5281/zenodo.22887380) retains the complete research programme and adds the 35-page arithmetic-probe and kernel-mass paper, with complete LaTeX, human citations and precise proof links. All 73 earlier PDFs remain separate.

### Arithmetic probes, kernel mass and the terminal metric correction

[Read the 35-page paper](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260922-arithmetic-probe-mass/ARITHMETIC_PROBE_MASS_READER.pdf) · [Complete LaTeX](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260922-arithmetic-probe-mass/ARITHMETIC_PROBE_MASS_READER.tex) · [Results and programme uses](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260922-arithmetic-probe-mass/RESULTS_20260922_022.md) · [Machine-readable proof locations](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260922-arithmetic-probe-mass/RESULT_INDEX.json).

The Split-Zero programme studies the arithmetic theta source, its quotient and its observation through determinant and heat estimates. This paper decomposes the original kernel determinant into positive successive observation layers and bounds the depth-eight remainder by 256E_k, using the earlier full-source estimate E_k=O_h(q). It sharpens the determinant interval obtained from the same kernel-mass samples, improves the filtered-mass multiplier from 5/4 to 9/8, and calculates a common realization metric from finite response data.

The paper also identifies the terminal correction between the hidden-coordinate and full-ambient minima. The former has the directed 2304E_k allowance; the latter requires the enclosure [-256E_k,2560E_k]. Canonical projective sections retain the physical action (k/2)v+iu and both complex current terms. Complete AP1–30, KM1–45 (including KM33a–b) and PEN1–27 proofs, illustrated reader LaTeX, checkers, 116 retained source blocks, human citations and precise earlier proof links accompany these results.

The actual native kq coefficient and separate current values/signs remain unevaluated; finite auxiliary checks do not assign them. The separate first-layer calculation is excluded. Whole-project descriptions and all earlier editions remain intact. [Human authors, source versions and reading coverage](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260922-arithmetic-probe-mass/SOURCE_READING_USE.md) and [earlier results strengthened or corrected](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260922-arithmetic-probe-mass/RECEIVER_UPDATES.md) are explicit.

[Published cumulative Zenodo edition](https://zenodo.org/records/22886386) (assigned DOI 10.5281/zenodo.22886386) retains the complete research programme and adds the 39-page original-observation recovery paper, with complete LaTeX, human citations and precise proof links. All 72 earlier PDFs remain separate.

### Finite recovery of the original observation

[Read the 39-page paper](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260922-original-observation-recovery/ORIGINAL_OBSERVATION_RECOVERY_READER.pdf) · [Complete LaTeX](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260922-original-observation-recovery/ORIGINAL_OBSERVATION_RECOVERY_READER.tex) · [Results and programme uses](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260922-original-observation-recovery/RESULTS_20260922_021.md) · [Machine-readable proof locations](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260922-original-observation-recovery/RESULT_INDEX.json).

The Split-Zero programme studies the arithmetic theta source, its quotient and its observation through determinant and heat estimates. This paper gives an exact spectral map from zero-frequency measured data to the original kernel angles, with finite rounding and determinant errors. It proves the sharp information loss of scalar data, identifies the scalar leading coefficient that retains the kq term, and bounds the bounded-power observation's 128-direction remainder by an explicit O(q) determinant. The polynomial quotient retains the full coefficient Gram, original poles, source maps and corrected complex currents.

Complete MR1–29, SD1–54 and BD1–31 proofs, illustrated reader LaTeX, checkers, inherited source blocks and human citations accompany it. Loewner realization work credits Zhang, Gosea and Antoulas, with Mayo and Antoulas retained as historical attribution; Feshbach–Schur, DLMF and Platt–Trudgian sources retain exact reading coverage. The actual native kq coefficient and separate current values/signs remain unevaluated. Auxiliary examples are not substituted for them. Canonical whole-project descriptions and all preceding editions remain intact; unfinished022work is excluded.

[Published cumulative Zenodo edition](https://zenodo.org/records/22884828) (assigned DOI 10.5281/zenodo.22884828) retains the complete research programme and adds the 62-page original-growth and measured-resolvent paper, with complete LaTeX, human provenance and precise proof links. All 71 earlier PDFs remain separate.

### Original growth, complete-row sampling and measured resolvents

[Read the 62-page paper](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260922-original-growth-resolvent/ORIGINAL_GROWTH_RESOLVENT_READER.pdf) · [Complete LaTeX](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260922-original-growth-resolvent/ORIGINAL_GROWTH_RESOLVENT_READER.tex) · [Results and programme uses](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260922-original-growth-resolvent/RESULTS_20260922_020.md) · [Machine-readable proof locations](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260922-original-growth-resolvent/RESULT_INDEX.json).

The Split-Zero programme studies the arithmetic theta source, its quotient and its observation through determinant and heat estimates. This paper calculates the full complex kernel correction recoverable from the measured resolvent, bounds complete-source metric errors by the ranks that contribute, and controls sampling of all original rows including lower-root coefficient errors. Relative growth estimates retain the complementary minimum and use a corrected circle for growing radii. A separate four-label arithmetic receiver calculation evaluates its first singular corrections and carries its metric and conductor maps explicitly.

Complete RM1–23, RG1–54, CS1–24, ES1–37 and received PR1–44 proofs, standalone LaTeX, figures, checkers, inherited proofs and human-source records accompany the paper. Dusson, Sigal and Stamm's Feshbach–Schur work, the named DLMF authors, Jensen's historical attribution, and Dirichlet's theorem in Ralf Stephan's credited translation retain precise sources and reading coverage. The native period-dependent kernel coefficient at order kq and individual complex-current signs remain unevaluated. Auxiliary receiver values and determinant signs are not substituted for them. The whole-project description and all preceding editions remain intact.

[Published cumulative Zenodo edition](https://zenodo.org/records/22884590) (assigned DOI 10.5281/zenodo.22884590) retains the complete research programme and adds the 37-page original-angle and full-word paper, with complete LaTeX, human provenance and precise proof links. All 70 earlier PDFs remain separate.

### The full original angle spectrum and determinant extraction

[Read the 37-page paper](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260921-original-angle-word/ORIGINAL_ANGLE_WORD_READER.pdf) · [Complete LaTeX](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260921-original-angle-word/ORIGINAL_ANGLE_WORD_READER.tex) · [Results and programme uses](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260921-original-angle-word/RESULTS_20260921_019.md) · [Machine-readable proof locations](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260921-original-angle-word/RESULT_INDEX.json).

The Split-Zero programme studies the original arithmetic theta source, its quotient and its observation through determinant and heat estimates. This paper determines the leading inverse-growth law for every original projection direction and exterior rank. It bounds the total downward movement of the centered angle spectrum across the complete cutoff window for both original Gamma source orders. The two source-innovation formulas are identified with their exact complex phase and mass, and actual source columns extract the determinant with a proved smaller-scale error. The complete long arithmetic word retains its collision kernel, resultant phase, all nonzero spectral directions and observed heat weights.

Complete AS1–64, FW1–49, RX1–20 and AD1–14 proofs, standalone LaTeX, reproducible figure sources, finite checks, inherited complete proofs and human-source records accompany the paper. The native period-dependent coefficient at order kq and separate complex-current signs remain unevaluated. The negative word-heat return is not assigned to that different current. Gu and Eisenstat's rank-revealing QR work is credited as context; the finite exchange arguments used here are proved directly. Original mathematical inputs retain their stated status. Earlier editions and the whole-project description remain intact; separate unsealed020 work is excluded.

[Published cumulative Zenodo edition](https://zenodo.org/records/22883955) (assigned DOI 10.5281/zenodo.22883955) retains the complete research programme and adds the 45-page invariant-determinant and arithmetic-collision paper, with complete LaTeX, human provenance and precise proof links. All 69 earlier PDFs remain separate.

### The original invariant determinant and an arithmetic collision

[Read the 45-page paper](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260921-invariant-collision/INVARIANT_DETERMINANT_COLLISION_READER.pdf) · [Complete LaTeX](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260921-invariant-collision/INVARIANT_DETERMINANT_COLLISION_READER.tex) · [Results and programme uses](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260921-invariant-collision/RESULTS_20260921_018.md) · [Machine-readable proof locations](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260921-invariant-collision/RESULT_INDEX.json).

The Split-Zero programme studies its original arithmetic theta source, quotient and observation through determinant and heat estimates. This paper calculates the kernel-volume return of a polynomial formed from the conductor's actual pivot-interior roots. Its collision quotient retains the metric it removes as an explicit graph term. The complete finite invariant determinant keeps every original row and nonideal relation; a sharper comparison for the same physical source supplies the stated O(q log q) transfer error.

Each complete relation added at a cutoff now has an exact split into new-source, observed and residual-kernel energies. The resulting positive loss factors keep all endpoint weights. Exact integer condensation calculates two scalar Gamma-reference examples, identified as reference examples rather than actual zeta data. Complete FI1–17, IC1–42, CI1–26 and CL1–18 proofs, standalone LaTeX, figures, checks, 48 inherited complete-source blocks and human provenance accompany the paper. Christian Krattenthaler's original determinant-calculus source and the named DLMF authors retain their precise citations. Original-period kernel allocation, independent proper-source comparisons and complex-current signs remain unevaluated. Imported analytic inputs retain their stated status; separate unsealed 019 work is not included. Earlier editions and the whole-project description remain intact.

[Published cumulative Zenodo edition](https://zenodo.org/records/22876297) (assigned DOI 10.5281/zenodo.22876297) retains the complete research programme and adds the 31-page moving-rational-family and observed-memory paper, with complete LaTeX, human provenance and precise proof links. All 68 earlier PDFs remain separate.

### Moving rational sources, arithmetic collisions and complete observed memory

[Read the 31-page paper](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260921-moving-rational-family/MOVING_RATIONAL_FAMILY_COMPLETE_READER.pdf) · [Complete LaTeX](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260921-moving-rational-family/MOVING_RATIONAL_FAMILY_COMPLETE_READER.tex) · [Results and programme uses](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260921-moving-rational-family/RESULTS_20260921_017.md) · [Machine-readable proof locations](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260921-moving-rational-family/RESULT_INDEX.json).

The Split-Zero programme studies the original arithmetic theta source, its quotient and its observation through determinant and heat estimates. This paper bounds the original kernel energy throughout source activation and calculates the complete late-memory return, keeping its actual mass and coupling blocks. Moving rational filters retain their least singular values and full observed heat. At collisions with the arithmetic spectrum, an explicit polynomial frame retains the full primary sector, any additional observation kernel and the corrected chain homotopy.

Complete KG1–42, MF1–42 and PC1–34 proofs, standalone LaTeX, three exact figure sources, received arguments, human citations and 39 inherited source blocks accompany the paper. The owner reports 581 exact and 1,193 numerical finite checks and inspection of all 31 pages; publication does not claim another checker replay. The full ultrasmall singular scale is restricted to canonical or critical activation, not activation one. Earlier monic-profile and zero-law inputs retain their stated status. Initial kernel allocation, the proper-source comparison pair and projected complex-current phases remain unevaluated. All previous editions and the whole-project description are retained.

[Published cumulative Zenodo edition](https://zenodo.org/records/22870109) (assigned DOI 10.5281/zenodo.22870109) retains the complete research programme and adds the 53-page canonical-memory and polynomial-filter paper, with complete LaTeX, human provenance and precise proof links. All 67 earlier PDFs remain separate.

### Canonical memory, colliding filters and original observed energy

[Read the 53-page paper](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260921-canonical-memory-filters/CANONICAL_MEMORY_FILTERS_COMPLETE_READER.pdf) · [Complete LaTeX](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260921-canonical-memory-filters/CANONICAL_MEMORY_FILTERS_COMPLETE_READER.tex) · [Results and programme uses](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260921-canonical-memory-filters/RESULTS_20260921_016.md) · [Machine-readable proof locations](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260921-canonical-memory-filters/RESULT_INDEX.json).

The Split-Zero programme studies the original arithmetic theta source, its quotient and its observation through determinant and heat estimates. This paper bounds the entire canonical memory below the kq scale, including at zero regularizer; calculates the energy changes of the original kernel and complementary quotient; and controls polynomial filters even when their poles coincide. Repeated eigenvalues retain their observation masses. Complete ME1–34, RF1–67, RM1–31 and BR1–9 proofs, the received continuation, exact figure sources and human citations accompany the paper. The earlier monic-profile and zero-law input retains its stated status; initial kernel allocation and native complex-current phases remain unevaluated. Earlier editions and the whole-project description remain intact.

[Published cumulative Zenodo edition](https://zenodo.org/records/22869444) (assigned DOI 10.5281/zenodo.22869444) retains the complete research programme and adds the 41-page critical source-activation and original arithmetic-action paper, with complete LaTeX, human provenance and precise proof links. All 66 earlier PDFs remain separate.

### Critical activation and the original observed arithmetic action

[Read the 41-page paper](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260921-critical-inverse-activation/CRITICAL_ACTIVATION_COMPLETE_READER.pdf) · [Complete LaTeX](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260921-critical-inverse-activation/CRITICAL_ACTIVATION_COMPLETE_READER.tex) · [Results and programme uses](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260921-critical-inverse-activation/RESULTS_20260921_015.md) · [Machine-readable proofs and source records](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260921-critical-inverse-activation/RESULT_INDEX.json).

The Split-Zero programme studies how the original theta source, its arithmetic quotient and its observation contribute to determinant and heat calculations. This addition calculates the inverse-power sector across its critical activation scale, retains every singular direction in the observed arithmetic action, and carries the resulting bounds into the original kernel and complementary determinants. Complete proofs HAR1–49, ACT1–48 and AK1–20, the received argument, original human sources, reproducible figures and verification records are included. The limiting coefficient retains the earlier monic-profile and zero-law source status; the initial canonical kernel determinant and native complex-current phases remain unevaluated. Earlier papers and the whole-project account are retained.

[Published cumulative Zenodo edition](https://zenodo.org/records/22868558) (assigned DOI 10.5281/zenodo.22868558) retains the complete research programme and adds the 61-page source-family and observed-heat paper, with complete LaTeX, original human sources and precise proof links. All 65 earlier PDFs, including the preceding inverse-quotient paper, remain separate.

### Original source families and complete observed heat: the 61-page proof

The [new paper](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260921-uniform-source-family/UNIFORM_SOURCE_FAMILY_COMPLETE_READER.pdf) studies how the original theta-source observation changes when its source weights vary. It bounds the actual activated two-column update while retaining its complex cross term, proves exact rational detection maps and a sharp observed fraction for the slow spectral space, and controls the observed heat while keeping its full memory term. The original kernel's remaining leading coefficient and complex-current phases are not claimed.

[Complete LaTeX](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260921-uniform-source-family/UNIFORM_SOURCE_FAMILY_COMPLETE_READER.tex) · [Results and their uses](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260921-uniform-source-family/RESULTS_20260921_014.md) · [Proof-location index](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260921-uniform-source-family/RESULT_INDEX.json) · [Complete original joint-source proof](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260921-uniform-source-family/JOINT_MINIMUM_COMPLETE.tex). All incoming mathematics, independent derivations, inherited proofs, human citations and check scripts accompany the reader. The preceding inverse-quotient paper remains intact.

[Published cumulative DOI edition](https://zenodo.org/records/22868393) (10.5281/zenodo.22868393) retains the whole research programme and adds the 44-page inverse-sector quotient paper, with complete LaTeX, inherited proofs and human-source records. All 64 earlier PDFs remain separately readable.

### Original inverse-sector quotient: the 44-page proof

The new [paper](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260921-inverse-quotient/INVERSE_QUOTIENT_COMPLETE_READER.pdf) constructs an explicit quotient of the programme's theta-source observation by controlled inverse powers of the spectral coordinate. It keeps the original relation, metric, kernel and four cutoffs, and proves that the kernel determinant's leading contribution is unchanged at the stated degree scale. It also calculates the effect of changing the source covariance and transfers the original heat and current formulas through the quotient. The initial angle of an already activated source remains explicit; the remaining full-kernel coefficient and current signs are not claimed here.

[Complete LaTeX](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260921-inverse-quotient/INVERSE_QUOTIENT_COMPLETE_READER.tex) · [Results and their uses](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260921-inverse-quotient/RESULTS_20260921_013.md) · [Machine-readable proof locations](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260921-inverse-quotient/RESULT_INDEX.json) · [Human sources and licences](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260921-inverse-quotient/THIRD_PARTY_NOTICES.md). All incoming and inherited proofs accompany the paper. The reported 188 exact checks and 21 numerical fixtures have their finite scope stated separately from the analytic arguments.

[Published cumulative DOI edition](https://zenodo.org/records/22867463) (10.5281/zenodo.22867463) retains the full project and adds the original-observation and actual-Xi papers as separate PDFs, with complete LaTeX and human-source records. The whole-project title and description remain in place.

The [28-page actual-Xi and uniform inverse-rate paper](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260921-actual-xi-uniform/ACTUAL_XI_UNIFORM_CONDUCTOR.pdf) supplies the exact Xi-jet pullback, a local interval certificate and both geometric inverse singular rates at the original growing Gamma cutoffs. [Complete LaTeX, source dependencies and citations](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260921-actual-xi-uniform/README.md) retain their stated domains; this is not a global RH conclusion.

Attribution correction for the [008 local-branch reader](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/7230c00b9f07dd222b2aea95427d67918f3a8cac/workbenches/splitzero-tandem/continuations/20260921-local-covariance-activation/008/REAL_PAIR_LOCAL_OBJECT.pdf): **Levent Alpöge** announced the originating construction, crediting Akhil and Fable in his [original announcement](https://x.com/__alpoge__/status/2079028340955197566). The ES source identifies Akhil Mathew and Claude Fable 5. [Tao's exposition](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/), the ES four-dimensional extension and the later conductor calculations have separate provenance. [The exact-role proof](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260921-actual-xi-uniform/ALPOGE_FABLE_ROLE.tex) gives the actual transport maps. The new paper restores this credit at its opening, in both figures and in its bibliography; the frozen 008 proof bytes are unchanged.

The [31-page original-observation paper](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260921-original-observation/ORIGINAL_OBSERVATION_COMPLETE_READER.pdf) calculates how growing inverse-power classes survive the original conductor observation. It gives their determinant coefficient, relative measured-heat control with an eventual positive four-cutoff trace return, and explicit observation bounds for detected eigenlines. [Complete LaTeX and prior proofs](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260921-original-observation/README.md), [results and uses](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260921-original-observation/RESULT_INDEX.json) and [exact proof links](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260921-original-observation/PROOF_LINKS.json) retain the human sources, original metrics and stated limits. The full-kernel strip-angle coefficient and individual native complex-current signs remain unassigned.

[Published cumulative DOI edition](https://zenodo.org/records/22867242) (10.5281/zenodo.22867242) includes the complete project, with the three new local-branch, covariance and activation papers as separate PDFs and their complete LaTeX sources. The project-wide title and description are unchanged in scope.

The [local-branch, conductor-covariance and source-activation papers](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260921-local-covariance-activation/README.md) are now available as three separate readers (18, 22 and 40 pages), with complete LaTeX, prior proofs, human citations, exact check receipts and reproducible figures. They calculate the coupled local spectral module, the original arithmetic covariance return, source activation and exact projected-current formulas. The smaller kernel coefficient and native current signs remain open in these editions. [Results and their uses](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260921-local-covariance-activation/RESULT_INDEX.json) and [direct proof links](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260921-local-covariance-activation/PROOF_LINKS.json) identify their precise scope.

[Published DOI edition](https://zenodo.org/records/22865966) (10.5281/zenodo.22865966) contains the cumulative source-link correction and the complete retained collection. Its title and description cover the whole project.

The [cumulative citation correction](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/666ee448d5ecb0bf8a4888f3a2aceaaa5c74d6d8/workbenches/splitzero-tandem/continuations/20260921-historical-proof-citations/README.md) links 35 historical references at 146 bibliography entries and 122 citation uses to 56 public proof locations. It includes the complete corrected LaTeX and restores four supporting sources. The equations and human credits are unchanged. This source correction does not claim newly compiled cumulative PDFs or a new mathematical result.

The [canonical-page rule](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/AGENTS.md) keeps this whole-project account ahead of edition-specific updates. Earlier reading notes below retain their original links and their own source-cut descriptions; they do not replace the account above.


<details>
<summary>Edition-specific reading notes and source references</summary>

<!-- historical-proof-citations:20260921 -->
## Find the cited Split-Zero proofs

[Corrected cumulative LaTeX and reference guide](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260921-historical-proof-citations/README.md) now give external proof links for the 35 previously unmatched historical references (146 bibliography entries). Links distinguish original public proofs from public reconstructions of private notes. Complete cited native-input sources are included; human credits and equations are retained. The existing mathematical readers and newest results below are unchanged.

<!-- inverse-power-directional-verified-doi:20260921 -->
## Read the inverse-power observation and resonance-direction papers

[Read the four-page Split-Zero inverse-power paper](https://zenodo.org/records/22865640) ([DOI 10.5281/zenodo.22865640](https://doi.org/10.5281/zenodo.22865640)); [read the separate 11-page resonance-direction paper](https://zenodo.org/records/22865640/files/105-splitzero-real-period-directions.pdf?download=1). The first constructs an exact conductor left inverse and a finite observation lower bound in the original metric. The second calculates every cutoff's resonance rays and the full inverse-spectrum transition along curved approaches to the certified real period.

[Complete source edition](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/689a8f87e9c12b7a99b01b3123438c6751ee608f/workbenches/splitzero-tandem/continuations/20260921-directional-inverse-power/README.md), [exact proof links](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/689a8f87e9c12b7a99b01b3123438c6751ee608f/workbenches/splitzero-tandem/continuations/20260921-directional-inverse-power/PROOF_LINKS.json), [results and their uses](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/689a8f87e9c12b7a99b01b3123438c6751ee608f/workbenches/splitzero-tandem/continuations/20260921-directional-inverse-power/RESULT_INDEX.json), and [complete LaTeX, supporting proofs and figures](https://zenodo.org/records/22865640/files/107-splitzero-directional-inverse-power-sources.zip?download=1) are available. Human citations and original check receipts are retained. The finite lower bound may tend to zero; the geometric family is not identified with arithmetic zeta zeros. Neither paper concludes RH.

The earlier 79-page native spectral and 22-page real-period papers remain separate downloads, as do all other earlier PDFs. Source ZIPs 93, 87 and 88 are retained exactly inside the new archive and remain separately downloadable from [the preceding DOI edition](https://zenodo.org/records/22865550).

<!-- directional-inverse-power:20260921 -->
## Resonance directions and inverse-power observation

[006: the 11-page resonance-direction paper](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260921-directional-inverse-power/006/REAL_PAIR_DIRECTIONAL_CONTINUATION.pdf) calculates every cutoff's original resonance rays and the full inverse-spectrum transition along curved approaches to the certified real period. [007: the four-page inverse-power paper](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260921-directional-inverse-power/007/Inverse_Power_Conductor_Observability_2026-09-21.pdf) constructs an exact left inverse of the original conductor on a specified growing space of inverse powers and proves a finite observation lower bound in the original metric.

[Full proofs and LaTeX](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260921-directional-inverse-power/README.md), [exact public proof links](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260921-directional-inverse-power/PROOF_LINKS.json), and [results and their uses](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260921-directional-inverse-power/RESULT_INDEX.json) preserve human citations and the complete earlier dependencies. The geometric family is not identified with arithmetic zeta zeros; the observation lower bound may tend to zero. Neither paper concludes RH.

<!-- spectral-real-period-verified-doi:20260921 -->
## Read the native spectral and real-period papers

[Read the 79-page Split-Zero native spectral paper](https://zenodo.org/records/22865550) ([DOI 10.5281/zenodo.22865550](https://doi.org/10.5281/zenodo.22865550)); [read the separate 22-page real-period paper](https://zenodo.org/records/22865550/files/103-splitzero-real-period.pdf?download=1). The first calculates the original conductor graph metric and isolates the remaining invariant-covariance estimates. The second certifies a positive real period of the original geometric coefficient family and computes its complete ES–Fable return.

[Complete source edition](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/0fd693c844aad9117e30ec447c59864a28af10f3/workbenches/splitzero-tandem/continuations/20260921-native-spectral-real-pair/README.md), [exact public proof links](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/0fd693c844aad9117e30ec447c59864a28af10f3/workbenches/splitzero-tandem/continuations/20260921-native-spectral-real-pair/PROOF_LINKS.json), [results and their uses](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/0fd693c844aad9117e30ec447c59864a28af10f3/workbenches/splitzero-tandem/continuations/20260921-native-spectral-real-pair/RESULT_INDEX.json), and [complete LaTeX and supporting proofs](https://zenodo.org/records/22865550/files/104-splitzero-spectral-real-period-sources.zip?download=1) are available. Human citations, all 38 sealed delivery files, and the original check receipts are preserved. Neither paper identifies this geometry with arithmetic zeta zeros or concludes RH.

All earlier PDFs remain available. The three preceding source ZIPs numbered 96, 98 and 101 are retained exactly inside the combined download and remain individually available in [the preceding DOI edition](https://zenodo.org/records/22865355). The other 97 earlier downloads remain separate.

<!-- native-spectral-real-pair:20260921 -->
## Native spectral geometry and the positive real-period return

Two separate completed editions are available: [003, the 79-page native spectral paper](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260921-native-spectral-real-pair/003/COMPLETE_NATIVE_SPECTRAL_READER.pdf), and [005, the 22-page real-period paper](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260921-native-spectral-real-pair/005/REAL_PAIR_005.pdf). The first calculates the original conductor graph metric, isolates its remaining invariant covariance terms, and identifies the singular direction and its original observation. The second certifies a positive real period in the original geometric coefficient family and calculates its complete ES–Fable inverse, marked outputs and cutoff-dependent spectra.

[Full proofs, LaTeX, citations and original check receipts](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260921-native-spectral-real-pair/README.md), [exact proof links](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260921-native-spectral-real-pair/PROOF_LINKS.json), and [results and their programme uses](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260921-native-spectral-real-pair/RESULT_INDEX.json) accompany both papers. The mathematical owners’ sealed files are retained exactly. Neither edition identifies the geometry with arithmetic zeta zeros or concludes RH. Earlier source editions are preserved.

<!-- kernel-degree-verified-doi:20260921 -->
## Read the Split-Zero kernel degree-step paper

[Read the 74-page paper on Zenodo](https://zenodo.org/records/22865355) ([DOI 10.5281/zenodo.22865355](https://doi.org/10.5281/zenodo.22865355)). It calculates exact degree changes of the arithmetic observation-kernel metric, retaining the full compression correction and every four-cutoff determinant factor. Programme citations are now clickable links to actual public proof files, including the sources directly beneath the diagram. The finite contraction is proved; the large-degree kq magnitude remains unevaluated.

[Full LaTeX](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/914b9aab530b7e6c1d112a236b51fa527c9c0538/workbenches/splitzero-tandem/continuations/20260921-kernel-degree-steps/COMPLETE_PROOFS.tex), [results and their uses](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/914b9aab530b7e6c1d112a236b51fa527c9c0538/workbenches/splitzero-tandem/continuations/20260921-kernel-degree-steps/RESULT_INDEX.json), [proof-link registry](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/914b9aab530b7e6c1d112a236b51fa527c9c0538/workbenches/splitzero-tandem/continuations/20260921-kernel-degree-steps/CITATION_LINKS.json), and [complete source archive](https://zenodo.org/records/22865355/files/101-splitzero-kernel-degree-sources.zip?download=1) are available. The archive contains all ten proof bodies and three cumulative LaTeX successors. Existing human attributions remain. Historical citations that still need an exact source match are listed in the registry.

Zenodo retains 98 earlier standalone files. Its preceding result index is preserved inside the new source archive and remains separately downloadable from the [preceding DOI edition](https://zenodo.org/records/22864870).

<!-- kernel-degree-steps:20260921 -->
## Exact degree changes in the Split-Zero kernel metric

The [74-page complete paper](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260921-kernel-degree-steps/COMPLETE_PROOFS.pdf) calculates how the metric of the arithmetic observation kernel changes when the allowed polynomial degree increases. It retains all reflected-node entries, the full correction after compression, and every factor in the four-cutoff determinant product. The calculation proves strict finite kernel contraction for the paired quartet; it does not determine the unresolved large-degree kq magnitude or settle RH.

Programme citations in this reader now link directly to public proof files. [Full LaTeX](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260921-kernel-degree-steps/COMPLETE_PROOFS.tex), [results and their uses](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260921-kernel-degree-steps/RESULT_INDEX.json), [human sources](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260921-kernel-degree-steps/SOURCE_USE_LEDGER.json), [the proof-link registry](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260921-kernel-degree-steps/CITATION_LINKS.json) and three complete cumulative LaTeX successors are included. The source archive preserves all ten complete proof bodies and restores two previously unpublished cited sources. The historical cumulative citations still awaiting an exact source match are identified in the registry, rather than assigned a guessed link.

<!-- original-kernel-verified-doi:20260921 -->
## Read the Split-Zero original-kernel proof edition

[Read the 49-page paper on Zenodo](https://zenodo.org/records/22864870) ([DOI 10.5281/zenodo.22864870](https://doi.org/10.5281/zenodo.22864870)). This edition calculates the metric determinant of the original arithmetic observation kernel, retaining all mixed relation terms. It includes full LaTeX, human citations, exact checks, the result/use index and three full cumulative source successors. The [matching GitHub source edition](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/5992ad50c0f2a06921f1fcaded7b4e38097c0739/workbenches/splitzero-tandem/continuations/20260920-original-kernel-mixed-determinants/README.md) is pinned to commit `5992ad50c0f2a06921f1fcaded7b4e38097c0739`. All three new Zenodo downloads were verified in full; the 96 previous downloads remain. The remaining large-degree kq coefficient is not evaluated by this edition.

<!-- original-kernel-mixed-determinants:20260920 -->
## Exact mixed relations in the arithmetic observation kernel

The Split-Zero programme represents finite zero-divisor classes of the completed zeta function in an arithmetic theta-source Hilbert space. The [49-page complete proof reader](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260920-original-kernel-mixed-determinants/COMPLETE_PROOFS.pdf) calculates the determinant of the original observation kernel after minimizing over all source representatives. It applies Akemann and Vernizzi’s finite determinant theorem with every mixed relation, source mass and coefficient-frame factor retained. The result identifies the exact Gamma matrix for the remaining large-degree kq calculation; it does not evaluate that coefficient or prove an RH conclusion. [Full LaTeX](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260920-original-kernel-mixed-determinants/COMPLETE_PROOFS.tex), [proof locators and programme use](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260920-original-kernel-mixed-determinants/RESULT_INDEX.json), [human sources](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260920-original-kernel-mixed-determinants/SOURCE_USE_LEDGER.json), all seven complete proof bodies, exact checks, reproducible illustration and three full cumulative source successors are included.

<!-- gamma-and-finite-derivative:20260920 -->
## Gamma bounds and a corrected finite derivative calculation

The Split-Zero programme needs reliable values and derivatives of the completed zeta function. The [complete new source edition](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260920-gamma-and-finite-derivative/README.md) proves the gamma inequality used in Arias de Reyna’s Taylor cutoff and replaces a printed global-monotonicity lemma that fails by an exact gamma-recurrence calculation. The finite replacement keeps the original function, derivative list, constants and error budgets, including the equality cases. [Full LaTeX proofs](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260920-gamma-and-finite-derivative/COMPLETE_PROOFS.tex), [proof locators and programme uses](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260920-gamma-and-finite-derivative/RESULT_INDEX.json), original human citations, the independent derivation, exact checks and an inspected diagram are included. This corrects a computational lemma; it is not an RH counterexample or certification of a whole implementation.

<!-- original-spectral-determinant:20260920 -->
## The original arithmetic determinant and its boundary term

The Split-Zero programme represents finite zero-divisor classes by polynomials in a theta-source Hilbert space. The [complete new calculation](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260920-original-spectral-determinant/README.md) uses the unchanged least-source-norm quotient metric. It calculates the full multiplication determinant as its complete root-polynomial term plus a positive term from both original boundary vectors, and returns that identity to the canonical action. It also proves eventual small-singular-value bounds; these are not zeta zeros or an RH conclusion. [Complete LaTeX proofs](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260920-original-spectral-determinant/COMPLETE_PROOFS.tex), [precise domains and uses](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260920-original-spectral-determinant/RESULT_INDEX.json), human citations, reproducible checks, an inspected diagram and three full cumulative source successors are included. No effective finite-degree threshold or individual projected-current sign is asserted.

<!-- polymath-finite-packet:20260920 -->
## A certified finite packet of the original theta heat flow

The Split-Zero programme starts with the theta source whose Mellin transform is 2xi. The [new complete calculation](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260920-polymath-finite-packet/README.md) applies Polymath’s effective de Bruijn–Newman approximation to this exact source, retaining the factor16, all derivative phases, the full zero divisor and its entire exterior factor. It certifies exactly one moving simple zero in (1/10,9/10)+i(507/4,513/4) for every t in [1023/4096,1025/4096]. A separate complete proof repairs intermediate source estimates while retaining their final constants. [All three proof bodies](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260920-polymath-finite-packet/COMPLETE_PROOFS.tex), [exact result domains and uses](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260920-polymath-finite-packet/RESULT_INDEX.json), human citations, checkers, an inspected coordinate illustration and three full cumulative LaTeX successors are included. This finite positive-time certificate does not settle the RH endpoint or all heights.

<!-- arithmetic-gaussian-return:20260920 -->
## Gaussian traces calculated in the original arithmetic quotient

The Split-Zero programme studies polynomial representatives of classes built from the theta function with Mellin transform 2xi. The [new complete calculation](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260920-gaussian-arithmetic-return/README.md) retains their actual arithmetic convolution norm and full relation polynomial. It transfers a Gamma reference calculation to that original measure, proves the quotient compression law, and evaluates the original four-cutoff signed Gaussian trace. In its stated five-orbit observation domain, the limit at t=1/1024 is below -657061/960000. This does not determine the remaining logarithmic terms or settle RH. [Both complete proofs](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260920-gaussian-arithmetic-return/COMPLETE_PROOFS.tex), [exact result domains and uses](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260920-gaussian-arithmetic-return/RESULT_INDEX.json), human citations, checkers, an inspected illustration and three full cumulative LaTeX successors are included.

<!-- heat-transport-arithmetic-volume:20260920 -->
## Heat flow on the theta source, and a sharp volume-to-heat bound

The Split-Zero programme starts with the theta source whose Mellin transform is 2xi, its full-zero-divisor source and the least-source-norm polynomial quotient. The [new complete calculations](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260920-heat-transport-arithmetic-volume/README.md) carry the de Bruijn–Newman flow through that exact theta construction, including its operators, relations, Fourier map, zero multiplicities and metrics. The original Toda determinant ratio now also bounds the change in the positive heat trace when the admitted polynomial degree increases, with no dimension multiplier. [Five complete proofs](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260920-heat-transport-arithmetic-volume/COMPLETE_PROOFS.tex), [two exact figures](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260920-heat-transport-arithmetic-volume/FIGURE_CAPTION.md), [results and their uses](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260920-heat-transport-arithmetic-volume/RESULT_INDEX.json), human citations, exact checkers and three full cumulative LaTeX successors are included. The remaining growing-degree arithmetic estimate is not asserted.

<!-- native-heat-action:20260920 -->
## Two heat observations of the original theta quotient

The Split-Zero programme uses the theta source with Mellin transform 2xi/h and the original least-source-norm metric on its finite polynomial quotient. The [new complete calculation](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260920-native-heat-action/README.md) computes both the holomorphic heat trace and the positive-metric heat trace of the same outgoing correction. Their small-heat-time difference recovers the existing arithmetic error bound, with explicit remainder estimates. The exact curvature calculation also gives a sharp heat-time threshold, including its sign-changing boundary example. [Four complete proofs](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260920-native-heat-action/COMPLETE_PROOFS.tex), [two labelled figures](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260920-native-heat-action/FIGURE_CAPTION.md), [results and their programme use](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260920-native-heat-action/RESULT_INDEX.json), human-source citations, exact checkers and three complete cumulative LaTeX successors are included. These finite results do not prove growing-degree arithmetic error decay or an RH conclusion.

<!-- native-spectral-action:20260920 -->
## The arithmetic error bound as a trace curvature

The Split-Zero programme uses the theta source with Mellin transform 2xi/h, its quotient by theta relations, and the source's least-norm metric on polynomial classes. The [new complete calculation](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260920-native-spectral-action/README.md) follows the exact rank-one correction from the attained selfadjoint compression to the original quotient multiplication operator. It computes every polynomial trace coefficient, the complete repeated-root endpoints, and the same arithmetic error bound as a mixed trace derivative in the original metric. [Four complete proofs](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260920-native-spectral-action/COMPLETE_PROOFS.tex), [the exact illustrated mechanism](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260920-native-spectral-action/FIGURE_CAPTION.md), [results and their programme use](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260920-native-spectral-action/RESULT_INDEX.json), point-of-use human citations, exact checkers and three complete cumulative source successors are included. The finite calculation does not establish growing-degree error decay or an RH conclusion.

<!-- native-secular-frame:20260920 -->
## Arithmetic spectra and recovery of a lost observation

The Split-Zero programme studies the theta source, its quotient by theta relations, and the arithmetic metric on finite polynomial observations. The [new complete source edition](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260920-native-secular-frame/README.md) calculates the exact rank-one difference between multiplication in that quotient and its attained self-adjoint compression. It retains every repeated-root pole, surviving factor, phase and physical jet unit, and identifies the correction with the existing arithmetic error bound. A separate pair of proofs locates where the marked-state observation loses one direction, recovers it with one cubic moment, and gives the full signed-orbit return with both original metrics. [Three complete LaTeX proofs](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260920-native-secular-frame/COMPLETE_PROOFS.tex), [results and their programme uses](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260920-native-secular-frame/RESULT_INDEX.json), human citations, exact checkers, two inspected mathematical figures and three complete cumulative source successors are included. These finite identities do not establish the remaining growing-degree estimate or RH.

<!-- semilocal-prolate-weil:20260920 -->
## Original theta sources and complete-Weil arithmetic tests

The [new complete source edition](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260920-semilocal-prolate-weil/README.md) applies the indexed human literature to the Split-Zero programme’s original theta source, quotient and arithmetic metric. It computes the finite-prime transfer and its quotient boundary term, the actual arithmetic recurrence defect, and the exact Hermite-seed constants and full truncation tails. Repeated-zero quotient jets retain their higher derivatives. The full-Weil calculation proves finite positivity with the unknown tail included and reproduces 45 positive determinant enclosures using the complete xi function. [Seven complete LaTeX proofs](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260920-semilocal-prolate-weil/COMPLETE_PROOFS.tex), [results and their programme uses](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260920-semilocal-prolate-weil/RESULT_INDEX.json), human citations, exact checkers, two mathematical figures and three complete cumulative source successors are included. The growing-degree arithmetic estimate remains unfinished; these results do not establish RH.

<!-- theta-transfer-current-precision:20260920 -->
## Original theta transfer and certified complex-current precision

The Split-Zero programme uses the theta source, its quotient by theta relations, and the arithmetic norm of finite polynomial classes. The [new complete source edition](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260920-theta-transfer-current-precision/README.md) proves how Burnol’s complete zero systems enter that original quotient, including Gamma factors and every multiplicity. It also calculates explicit arithmetic moment tolerances for the same quotient metric and fixed-kernel complex current. [Six complete LaTeX derivations](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260920-theta-transfer-current-precision/COMPLETE_PROOFS.tex), [a fully labelled mathematical diagram](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260920-theta-transfer-current-precision/FIGURE_CAPTION.md), [machine-readable results and programme uses](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260920-theta-transfer-current-precision/RESULT_INDEX.json), human-source citations, exact checkers and three updated full cumulative manuscripts are included. These finite formulas do not assign native moment values or establish the remaining growing-degree signed estimate.

<!-- native-moments-and-marked-observation:20260920 -->
## Arithmetic moment bounds and complete marked observations

The Split-Zero cohomology programme measures polynomial classes of its theta source in the original arithmetic convolution norm. The [new finite-moment proofs](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260920-native-moment-resolvents/README.md) bound the resolvent integrals entering that norm while retaining every complex cross-term phase. They carry the bounds through the same observation and conductor fibres and the four signed determinant endpoints. [Both complete LaTeX proofs](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260920-native-moment-resolvents/COMPLETE_PROOFS.tex), [an exact equation diagram](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260920-native-moment-resolvents/FIGURE_CAPTION.md), [machine-readable results and programme uses](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260920-native-moment-resolvents/RESULT_INDEX.json), human-source citations and all three cumulative manuscript successors are included. Actual native moment values and their growing-degree projected-current estimate remain to be calculated.

The [complete marked-observation edition](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260920-marked-observation-illustrated/README.md) proves the literal original coordinate maps, all inverse branches of the marked arithmetic orbit, recovery from every nonempty observable corner support and the exact eight-to-seven-to-three specialization. [Its entire illustrated cumulative LaTeX](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260920-marked-observation-illustrated/FABLE_TO_ORIGINAL_CONDUCTOR.tex) and [seven-figure HTML atlas source](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260920-marked-observation-illustrated/FABLE_VISUAL_ATLAS.html) retain the original mathematics and provenance. The [four additional source-kernel and observation diagrams](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260920-native-moment-resolvents/original_source_figures/FIGURE_CAPTIONS.md) have complete mathematical captions and proof locators. These source editions assert no RH conclusion or new Zenodo deposit.

<!-- original-observation-source-kernel:20260920 -->
## Finite arithmetic observation and its original source kernel

The Split-Zero programme forms finite observations of the theta-source quotient and equips them with the least source norm. The [complete new proof edition](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260920-original-observation-source-kernel/README.md) calculates constant-depth recovery of those observations, the full cofactor and coefficient-specialization maps, and an explicit Gaussian source kernel with its endpoint correction. It also carries the native metric bounds into singular-value estimates without changing the original observation or its kernel. [All eight complete proofs in LaTeX](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260920-original-observation-source-kernel/COMPLETE_PROOFS.tex), [machine-readable results](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260920-original-observation-source-kernel/RESULT_INDEX.json), the original standalone derivations, human citations, exact checks and three full cumulative TeX successors are included.

The evaluated source family is connected to the arithmetic quotient by the displayed theta map and the full polynomial minimum. This does not evaluate the remaining projected arithmetic-current asymptotic or establish an RH conclusion. No new Zenodo or Overleaf edition is claimed here.

<!-- native-parity-and-conductor-boundary:20260920 -->
## Native arithmetic metric bounds and the full conductor

The Split-Zero programme studies the theta source and its quotient by theta relations. Its finite arithmetic observations carry a metric defined by the least norm of an original source representative. The [new complete source edition](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260920-native-parity-conductor-return/README.md) calculates the even/odd change of variable into the Pollaczek weights, bounds that original metric by positive finite resolvent sums, and carries the same bounds into the full conductor map. The original convolution estimate gives an explicit truncation length for any prescribed four-endpoint determinant error. All signed-state coordinates, complex phases, masses and relation spaces are retained. [Complete LaTeX](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260920-native-parity-conductor-return/LITERATURE_RECEIVERS_COMPLETE.tex), [proof/use index](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260920-native-parity-conductor-return/RESULT_INDEX.json), [human-source citation map](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260920-native-parity-conductor-return/CITATION_USE_MAP.json) and three full cumulative TeX successors are included.

The [complete ES–Fable boundary/action edition](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260920-fable-boundary-action/README.md) gives the rational signed-frame connection, both complete factor-boundary charts, the selected-root collision spectrum and the exact original corner-quotient action. [Full cumulative proof](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260920-fable-boundary-action/FABLE_TO_ORIGINAL_CONDUCTOR.tex) and [programme identifiers](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260920-fable-boundary-action/PROGRAMME_ALIASES.md) accompany the original source derivation and exact check scripts.

The new bounds control resolvent-series truncation; they do not yet evaluate the native integrals or the remaining complex projected-current asymptotic. No RH conclusion or real-time fluid blowup is asserted. These are additive GitHub source editions; no new Zenodo or Overleaf edition is claimed.

<!-- exact-literature-and-signed-conductor:20260920 -->
## Original theta topology, arithmetic metrics and signed inverse states

The Split-Zero programme studies the theta source, its quotient by theta relations, and the arithmetic metric of finite observations of that quotient. The [new complete literature-derived proofs](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260920-original-theta-arithmetic-observation/README.md) establish closure of the original full theta image in its weighted-Schwartz topology, an exact Gamma-kernel lower bound for the joint three-vector arithmetic observation, and reconstruction of the native Gram matrix with its finite Jacobi boundary correction. Each proof identifies its human source and gives the exact receiving maps. [Complete LaTeX](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260920-original-theta-arithmetic-observation/LITERATURE_RECEIVERS_COMPLETE.tex) and [machine-readable proof/use index](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260920-original-theta-arithmetic-observation/RESULT_INDEX.json) are included, together with the three updated full cumulative manuscripts.

The [complete signed ES–Fable/conductor edition](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260920-fable-signed-states/README.md) retains its entire earlier inverse-map calculation and adds all eight signed states, their exact evaluation through the unchanged original weighted conductor, and the cover’s 192-element monodromy group. [Complete cumulative LaTeX](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260920-fable-signed-states/FABLE_TO_ORIGINAL_CONDUCTOR.tex) and [unambiguous programme result IDs](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260920-fable-signed-states/PROGRAMME_ALIASES.md) are available.

These are complete source editions, not a proof or disproof of RH. The remaining signed arithmetic cross-product asymptotic is not evaluated by these results. This GitHub update does not claim a new Zenodo or Overleaf edition.

<!-- fable-conductor:20260920 -->
## Four ES–Fable labels and the original weighted conductor

This complete source edition solves the inverse problem for the four-dimensional polynomial map used in the Erdős–Straus/Fable construction, then transports its fibres and escaping branches into the Split-Zero programme’s original weighted conductor. It gives all fibre multiplicities, the omitted values, all four singular values and the exact correction for the original translation action. The nonlinear map has escaping inverse branches; the original linear conductor remains invertible.

[Complete LaTeX proof](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260920-fable-conductor/FABLE_TO_ORIGINAL_CONDUCTOR.tex) · [Proofs, exact checks and human provenance](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260920-fable-conductor/README.md). This is a nineteen-file source edition, not an RH counterexample. The original ES construction, Alpöge’s example and the special-function literature are cited at their actual uses.

<!-- heat-literature-observed-class:20260920 -->
## Heat flow and the observed arithmetic class

This 25-page continuation calculates how the norm of the terminal polynomial class changes after imposing the programme’s original observation map. It evaluates a four-degree norm ratio, compares the same class in the arithmetic and Gamma-weighted metrics, and sharpens a conductor bound. The original zero multiplicities, source maps and complex phases remain in the formulas.

[Read the complete proof](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260920-heat-literature-observed-class/HEAT_LITERATURE_AND_OBSERVED_CLASS.pdf) · [Complete LaTeX](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260920-heat-literature-observed-class/HEAT_LITERATURE_AND_OBSERVED_CLASS.tex) · [Results and proof locators](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260920-heat-literature-observed-class/NEW_RESULTS_2026-09-20.md) · [Source package](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260920-heat-literature-observed-class/README.md) · [Remaining calculation](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260920-heat-literature-observed-class/CONTINUATION.md).

The exact uses of Burnol, Connes, Connes–Consani–Moscovici, Polymath, Platt–Trudgian and the cited special-function literature are documented in the proofs. Three complete cumulative LaTeX successors and the preceding proof providers accompany this edition. The remaining calculation is the signed cross product of the original projected vectors; the norm estimates alone do not give its phase or a conclusion about RH.

<!-- original-heat-source-endpoint:20260919 -->
## Original heat control and complete source endpoint

This 21-page proof bounds the growth of the original heat-comparison
constant and evaluates the common heat depth needed to control the
three original currents. It then calculates the complete finite-primary
source endpoint: its regular correction, left-block quotient, nilpotent
metric scales, critical first correction and arithmetic boundary maps.
The source cross terms and target minimum are retained. Actual native
allocations, proper-source target values and individual signs remain
open calculations.

[Read the 21-page proof](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260919-original-heat-source-endpoint/ORIGINAL_HEAT_AND_SOURCE_ENDPOINT.pdf) · [Complete LaTeX](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260919-original-heat-source-endpoint/ORIGINAL_HEAT_AND_SOURCE_ENDPOINT.tex) · [Six mathematical results](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260919-original-heat-source-endpoint/NEW_RESULTS_2026-09-19.md) · [Complete source package](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260919-original-heat-source-endpoint/README.md) · [Next calculation](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260919-original-heat-source-endpoint/CONTINUATION.md).

Full cited providers, three additive cumulative LaTeX successors,
136 finite heat/current diagnostics and 14 exact endpoint check groups
accompany the proofs. Human authors retain their point-of-use citations.
Earlier sealed editions remain unchanged; the new cumulative sources
have not been rendered into replacement PDFs.

<!-- native-precision-leakage:20260919 -->
## Native precision and quantitative kernel leakage

This seven-page proof sharpens the displaced covariance and complete
correlated return through the q/log q scale, computes the first marked
discrepancy on each admitted original period stratum, and gives an explicit
positive lower bound for leakage measured in the original kernel metric.
The inverse and all feedback blocks are retained. It also evaluates the
integer heat depth and its degree cost. The target Schur spectrum,
absolute allocations and individual projected signs remain unevaluated.

[Read the seven-page proof](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260919-native-precision-leakage/NATIVE_PRECISION_AND_LEAKAGE.pdf) · [Complete LaTeX](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260919-native-precision-leakage/NATIVE_PRECISION_AND_LEAKAGE.tex) · [Four mathematical results](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260919-native-precision-leakage/NEW_RESULTS_2026-09-19.md) · [Complete source package](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260919-native-precision-leakage/README.md) · [Next calculation](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260919-native-precision-leakage/CONTINUATION.md).

The package retains complete cited providers, three cumulative LaTeX
successors and 427 finite diagnostic checks. Analytic inputs retain
their cited proof status; the finite tests are not evaluations of
hypothetical zeta zeros. Human citations remain at their uses.

<!-- native-conductor-coprimality:20260919 -->
## Original conductor coprimality and the proper-source kernel

This seven-page proof shows that the original proper-source kernel
vanishes outside a specified finite exceptional set of admitted periods
on the original hypothetical simple-quartet domain. It gives an explicit
sufficient period bound, retaining the unit phase, branch and degree
congruence. The source Schur subtraction is removed on that domain;
the complete target minimum remains to be evaluated.

[Read the seven-page proof](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260919-native-conductor-coprimality/ORIGINAL_CONDUCTOR_COPRIMALITY.pdf) · [Complete LaTeX](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260919-native-conductor-coprimality/ORIGINAL_CONDUCTOR_COPRIMALITY.tex) · [Mathematical results](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260919-native-conductor-coprimality/NEW_RESULTS_2026-09-19.md) · [Complete source package](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260919-native-conductor-coprimality/README.md) · [Next calculation](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260919-native-conductor-coprimality/CONTINUATION.md).

The four incoming notes, current low-jet revision and its archived
predecessor, complete PCL argument, three cumulative LaTeX successors
and exact algebra/rank diagnostics accompany the proof. Platt and
Trudgian are cited for the finite-height input. Imported Gamma estimates
retain their stated written-proof status, not certification by finite
checks. No target determinant, individual projected sign or RH conclusion
is inferred from this source-kernel result.

<!-- corpus-cohomology-metric-receivers:20260919 -->
## Earlier Split-Zero constructions in the theta-cohomology programme

This 38-page proof constructs explicit maps from the original theta
complex into earlier split-support cohomology, arithmetic-boundary,
global-jet, source-inversion and holonomy constructions. It also quantifies
the heat depth required by the attained finite metric and errors in
the actual complex observation responses and three projected currents.
The original coordinates, full zero multiplicities and human citations
are retained. Individual projected signs, observation angles and the
seven separate absolute allocations remain to be calculated.

[Read the 38-page proof](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260919-corpus-cohomology-metric-receivers/CORPUS_RECEIVERS_AND_METRIC_CONTROL.pdf) · [Complete LaTeX](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260919-corpus-cohomology-metric-receivers/CORPUS_RECEIVERS_AND_METRIC_CONTROL.tex) · [Nine dated mathematical results](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260919-corpus-cohomology-metric-receivers/NEW_RESULTS_2026-09-19.md) · [Complete source package](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260919-corpus-cohomology-metric-receivers/README.md) · [Earlier sources and their exact maps](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260919-corpus-cohomology-metric-receivers/SOURCE_RECEIVERS.md) · [Next calculations](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260919-corpus-cohomology-metric-receivers/CONTINUATION.md).

Three complete cumulative LaTeX successors, 35 exact source providers
including full Deligne D032, explicit correction records and 156 finite
matrix diagnostics accompany the proof. Reading coverage is recorded
without claiming an exhaustive review of the earlier corpus.

<!-- circle-heat-original-metrics:20260919 -->
## Circle heat in the original arithmetic quotient metrics

This eight-page proof carries the earlier circle heat construction through
the original tensor source and its attained restriction and quotient
metrics, with an explicit finite error budget. It also controls the
metrics and induced singular values of Deligne’s nilpotent grades.
The original full-Gram constant is retained. In the simple-quartet case
there is one grade containing the entire metric; this does not calculate
cross-primary observation angles or establish arithmetic purity.

[Read the eight-page proof](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260919-circle-heat-original-metrics/HEAT_TO_ORIGINAL_QUOTIENT_METRICS.pdf) · [Complete LaTeX](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260919-circle-heat-original-metrics/HEAT_TO_ORIGINAL_QUOTIENT_METRICS.tex) · [Two dated mathematical results](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260919-circle-heat-original-metrics/NEW_RESULTS_2026-09-19.md) · [Complete source package](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260919-circle-heat-original-metrics/README.md) · [Next calculations](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260919-circle-heat-original-metrics/CONTINUATION.md).

The original circle paper, complete Deligne D032 text, three cumulative
LaTeX successors and 68 finite diagnostics accompany the proof. Human
sources retain their point-of-use citations.

<!-- full-window-source-products:20260919 -->
## Full-window source products and the retained arithmetic class

This 13-page continuation evaluates both source-response products and the
norm loss of the same retained terminal arithmetic class over degrees
`q−1` through `2q`. It proves the exact return to the observation quotient
and bounds the original kernel determinant over the complete window.
Source and class results retain every fixed original multiplicity;
conductor results retain the simple-quartet, fixed-period domain.
The remaining observation angles, phases and individual allocations
are identified explicitly; no RH conclusion is claimed.

[Read the 13-page paper](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260919-full-window-source-products/FULL_WINDOW_SOURCE_PRODUCTS.pdf) · [Complete LaTeX](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260919-full-window-source-products/FULL_WINDOW_SOURCE_PRODUCTS.tex) · [Five dated mathematical results](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260919-full-window-source-products/NEW_RESULTS_2026-09-19.md) · [Complete source package](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260919-full-window-source-products/README.md) · [Next calculations](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260919-full-window-source-products/WEB_CONTINUATION_PROMPT.md).

The package includes three complete cumulative LaTeX successors, complete
cited providers, the retained Deligne D032 text and 69 finite-identity
checks. Point-of-use human citations remain in the sources.

## Original sources

The construction originates in the [original paper dated 12 July 2025](https://zenodo.org/records/17555345), under its original title, and the broader programme already has a [Project Atlas dated 19 July 2026](https://zenodo.org/records/21443852). September 12 dates the later RH/cohomology repository strand, not the construction’s origin.

# Split-Zero cohomology: observation responses and the first determinant allocation

This 44-page continuation studies how an arithmetic class is measured after
passing through its original quotient and observation maps. It gives complete
proofs of the adjacent observation update, low-cutoff source-energy estimates,
parity estimates across the admitted cutoffs, and the first evaluated split of
a conductor determinant change between the kernel and observed quotient. It
also calculates the cost of trace-minimizing metrics relative to the original
metric and the observation coefficient of a marked defect.

The first determinant increment is now evaluated; the remaining full-window
allocations, individual projected signs, proper-source value and geometric
same-class construction remain unfinished. This edition does not claim a
proof or disproof of the Riemann hypothesis.

The dated bulletin identifies ten advances across the September 19 editions.
Human-source connections accompany the point-of-use citations in the proofs.

The complete reader LaTeX, five original proofs, three cumulative LaTeX
successors, complete decisive sources and full retained Deligne D032 text are
included. Earlier editions remain intact. This GitHub continuation is newer
than the unchanged [Zenodo edition](https://doi.org/10.5281/zenodo.22821108).

## Dated mathematical results

- [What changed on 19 September: ten dated advances and their scope](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260919-observation-responses-first-allocation/NEW_RESULTS_2026-09-19.md)
- [Direct links to the complete proofs behind those entries](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260919-observation-responses-first-allocation/DATED_PROOF_LINKS.md)
- [Human authors, source locators and use in these calculations](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260919-observation-responses-first-allocation/HUMAN_SOURCE_CONNECTIONS_2026-09-19.md)
- [Machine-readable dated result index](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260919-observation-responses-first-allocation/DATED_RESULTS_INDEX.json)

## Read the complete mathematics

- [44-page paper: observation responses and first determinant allocation](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260919-observation-responses-first-allocation/readers/44_PAGE_OBSERVATION_RESPONSES.pdf)
- [Complete LaTeX for the paper](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260919-observation-responses-first-allocation/arrival_04/assembly/ARRIVAL04_PROOF_READER.tex)
- [Three complete cumulative LaTeX successors](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/main/workbenches/splitzero-tandem/continuations/20260919-observation-responses-first-allocation/arrival_04/assembly/cumulative/)
- [140 results: exact claims, programme roles and dependencies](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260919-observation-responses-first-allocation/research_index/PROGRAM_INDEX.json)
- [5,507 formula locations](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260919-observation-responses-first-allocation/research_index/FORMULA_LOCATORS.json)
- [PDF and complete LaTeX identity map](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260919-observation-responses-first-allocation/PDF_LATEX_MAP.json)
- [Current continuation prompt](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260919-observation-responses-first-allocation/NEXT_CALCULATION.md)
- [Source provenance and integrity checks](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260919-observation-responses-first-allocation/PACKAGE_README.md)
- [Pierre Deligne: full retained English mathematical source](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260919-observation-responses-first-allocation/prior_intakes/supporting_sources/D032_FULL_EN.tex)

## Earlier guide (historical snapshot)

The following guide is retained verbatim; the reading links above identify this newer source edition.

# Split-Zero cohomology: absolute values and original-metric control

This 75-page continuation develops the Split-Zero programme for the Riemann
zeta function. It follows finite zero packets through theta-function sources,
polynomial quotients, period maps and their original metrics. The purpose is
to evaluate the complete arithmetic action and then calculate how it divides
among the original cohomological subspaces—not to infer those allocations
from ranks or a total determinant alone.

## Results and their use

| Calculation | What it supplies |
| --- | --- |
| Absolute Gamma baseline | An `O(log q)` baseline at every fixed multiplicity, completing the canonical action through `q/log q` while retaining the finite errors. |
| Full-primary trace minimum | The minimum over the complete primary decomposition, with equality/excess and original-metric coupling formulas. Primary angles are related to, not silently substituted for, observation projections. |
| Original coefficient sections | Exact transitions for every retained minor and native/arithmetic metric receivers, keeping conductor terms and cross blocks. |
| Tensor residues and periods | Full residue, boundary-energy and period-recovery maps, retaining both directions and the original source conventions. |
| Guinand–Weil comparison | An explicit nonzero correction to the programme's archived local comparison and the precise test-space inclusion. This corrects the local transcription; it does not claim a contradiction in the human authors' formulas. |
| Montgomery finite-part term | The complete Gamma/trivial-zero combination on its stated original domain, with regulator, pole and endpoint terms preserved. |

The A3R receiving formulas propagate these results into earlier calculations.
The corrected foundation LaTeX files travel with their complete historical
predecessors and reversible change records; no earlier paper is erased.

## What still needs calculation

The seven absolute allocations and eight signed observation-flag spectra,
the actual full-class projection energies `p1`, `p2`, `theta` and their
projected currents, the independent proper-source standard-window value,
and the geometric same-class Frobenius/image construction remain unfinished.
This is not a proof or disproof of the Riemann hypothesis.

## Readable sources and provenance

The PDF has its complete LaTeX. The package also includes complete accepted
proofs, bibliography companions, three cumulative LaTeX successors, the full
selected English mathematical source of Pierre Deligne's *The Weil Conjecture.
II*, and the original mathematical notes with their accepted/corrected scope.
An incoming note is not asserted wholesale merely because it is included.
Guinand, Weil, Montgomery, Deligne and all other cited human authors retain
their point-of-use attribution in the original sources and bibliographies.

The current machine-readable index has 132 result nodes and 5,344 formula
locations. It records exact claims, programme roles, dependencies and remaining
work. All mathematical TeX/PDF bytes are preserved. Portable metadata has
separate original and public hashes, and the package verifier checks file
identity, PDF/LaTeX pairing, formula destinations and reversible source changes.
These checks are not a new mathematical audit, compilation or Lean execution.

The provider inventory retains 43 source entries. One is an unbundled historical
archival container; its identity and complete scoped prerequisite sources are
recorded without publishing private paths or duplicating the full local archive.
The preceding 243-page and 95-page papers remain in their
[published edition](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/0562d35abb20ec87be85aba00a6206fcd843cd58/workbenches/splitzero-tandem/continuations/20260919-arithmetic-signs-marked-classes/).
The [Zenodo DOI edition](https://doi.org/10.5281/zenodo.22821108) is unchanged;
this continuation is published on GitHub only.

## Read this edition online

- [75-page paper: absolute values and original-metric control](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260919-absolute-values-original-metric/readers/75_PAGE_ABSOLUTE_VALUES.pdf)
- [Complete LaTeX for the paper](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260919-absolute-values-original-metric/arrival_03/assembly/ARRIVAL03_PROOF_READER.tex)
- [Three complete cumulative LaTeX successors](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260919-absolute-values-original-metric/arrival_03/assembly/cumulative)
- [Corrected foundation sources and preserved historical versions](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260919-absolute-values-original-metric/arrival_03/foundation_updates)
- [132 results: claims, programme roles and dependencies](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260919-absolute-values-original-metric/research_index/PROGRAM_INDEX.json)
- [5,344 formula locations](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260919-absolute-values-original-metric/research_index/FORMULA_LOCATORS.json)
- [Incoming-source classifications and accepted changes](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260919-absolute-values-original-metric/arrival_03/RESULT_INDEX.json)
- [PDF and complete LaTeX identity map](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260919-absolute-values-original-metric/PDF_LATEX_MAP.json)
- [Current directional and same-class calculations](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260919-absolute-values-original-metric/NEXT_CALCULATION.md)
- [Source provenance and integrity checks](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260919-absolute-values-original-metric/PACKAGE_README.md)
- [Pierre Deligne: full selected English mathematical source](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260919-absolute-values-original-metric/prior_intakes/supporting_sources/D032_FULL_EN.tex)

## Earlier guide (historical snapshot)

The following guide is retained verbatim; the reading links above identify this newer source edition.

# Split-Zero cohomology: arithmetic signs, marked classes and correlated responses

This edition develops the Split-Zero research programme for the Riemann zeta
function. The programme follows finite packets of zeros through theta-function
sources, polynomial quotients, period maps and their original quotient metrics.
Its aim is to calculate the signed arithmetic and analytic terms in the same
cohomological action, including the terms lost when one keeps only ranks or
total determinant sizes.

The September 19 edition has two separately readable papers: a 243-page
foundation and a 95-page continuation. The continuation is the best starting
point for the latest results; the foundation supplies its preceding complete
derivations. Both retain their bibliographies and point-of-use citations.

## What changed, and why it matters

| Calculation | Contribution to the programme |
| --- | --- |
| Signed arithmetic scalar | Evaluates the original source-order-one scalar through the `q/log q` correction and determines the actual simple-source sign. This does not assign the signs of its separate projected components. |
| Mixed and nonlinear return | Bounds their **sum**, retaining the original summands and signs. The bound is not asserted separately for either summand. |
| Correlated polynomial rows | Gives the corrected radial profile with summed `O(q)` error. Its deterministic row correction remains; the eight directional flags and seven absolute allocations still require evaluation. |
| Marked arithmetic classes | Supplies polynomial recovery, symmetric-power maps, period/metric receivers and growing-flag localization. The terminal–low cross block remains, and the fixed-degree cumulant result keeps its fixed-degree scope. |
| Complete retained class | Restores the low, conductor and native components in the original boundary and action maps, including all nine blocks and both leakage directions. The complete original EC source is included with its stated analytical verification scope. |
| Joint response ellipse | Describes the exact correlated two-response region and amplification bounds. The actual projection energies `p1`, `p2` and `theta`, and the individual projected arithmetic signs, remain to be calculated. |

The sections labelled ARU1–15 show precisely how the new calculations replace
or strengthen statements used earlier. The first paper also includes primitive
endpoint control, reflected-pair period calculations, two-window transport,
central-path transfer and the supported Zeta receiving interface to the
separately published EP817 work.

## What remains open

The seven absolute allocations, the actual directional spectra and projection
energies, the independent proper-source standard-window value, and the separate
analytic action's `O(q)` coefficient are unfinished. An arithmetic coefficient
is not substituted for that analytic coefficient. This edition does **not**
claim a proof or disproof of the Riemann hypothesis.

## Sources and reproducibility

The machine-readable index records 116 accepted result nodes, their programme
roles, dependencies, source types, acceptance scope and remaining calculations.
Its companion gives 4,956 formula locations. Complete proof sources, 32 pinned
decisive providers, both reader sources, three current cumulative LaTeX
successors and the continuation prompt accompany the papers.

Pierre Deligne's *The Weil Conjecture. II* is retained as the full selected
English mathematical LaTeX source, with its attribution and source identity.
Including that human source does not identify the programme's receiving maps
with Deligne's theorems: the papers give their particular maps and remaining
metric or analytic terms. All human-author citations in the accepted sources
are preserved. No unsupported translator attribution or blanket licence for
third-party sources is introduced.

Original mathematical TeX and PDF bytes are unchanged. Portable metadata
removes private workstation paths; a separate derivation manifest distinguishes
original identities from the downloadable metadata hashes. Input inventories
record lineage without publishing private conversations or the local corpus.
The package verifier checks file identities, formula-line destinations and
exact cumulative predecessor recovery; it is not a new mathematical audit or
a new Lean certification.

Earlier repository editions remain available. The existing
[Zenodo DOI edition](https://doi.org/10.5281/zenodo.22821108) is unchanged and
does not contain this new GitHub continuation.

## Read this edition online

- [Latest 95-page arithmetic continuation](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260919-arithmetic-signs-marked-classes/readers/95_PAGE_ARITHMETIC_CONTINUATION.pdf)
- [Complete LaTeX for the 95-page paper](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260919-arithmetic-signs-marked-classes/arrival_02/assembly/ARRIVAL02_PROOF_READER.tex)
- [243-page foundation paper](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260919-arithmetic-signs-marked-classes/readers/243_PAGE_FOUNDATION.pdf)
- [Complete LaTeX for the 243-page paper](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260919-arithmetic-signs-marked-classes/first_intake/assembly/MULTI_INTAKE_PROOF_READER.tex)
- [Three complete cumulative LaTeX successors](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260919-arithmetic-signs-marked-classes/arrival_02/assembly/cumulative)
- [Machine-readable results, dependencies and programme roles](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260919-arithmetic-signs-marked-classes/research_index/PROGRAM_INDEX.json)
- [4,956 formula locations](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260919-arithmetic-signs-marked-classes/research_index/FORMULA_LOCATORS.json)
- [Every PDF paired with its complete LaTeX](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260919-arithmetic-signs-marked-classes/PDF_LATEX_MAP.json)
- [The next directional and same-class calculations](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260919-arithmetic-signs-marked-classes/NEXT_CALCULATION.md)
- [Package verification and source identity guide](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260919-arithmetic-signs-marked-classes/PACKAGE_README.md)
- [Pierre Deligne: full selected English mathematical LaTeX](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260919-arithmetic-signs-marked-classes/first_intake/supporting_sources/D032_FULL_EN.tex)

## Earlier guide (historical snapshot)

The following guide is retained verbatim; the reading links above identify this newer source edition.

# Split-Zero cohomology: conductor, covariance and attained-profile calculations

This is the 18 September 2026 continuation of the Split-Zero research programme on the Riemann zeta function. The programme represents a finite packet of zeta zeros through arithmetic polynomial quotients and the norms of their original source functions. Its present calculation asks how the resulting determinant growth is divided between the original kernel, quotient and complementary-return maps, and how those signed contributions enter the same arithmetic action.

The new paper supplies complete proofs for conductor transport, lower-root covariance, attained polynomial minima and their joint degree profile. It does **not** prove the Riemann hypothesis. The signed arithmetic correction, individual allocations and the independent proper source's standard-window return remain to be calculated.

## What changed, and why it matters

Write $q=(a+1)^2$ for the original upper degree and retain both original source orders $s=1,a$. All bounds keep the fixed-data dependence and finite degree restrictions stated in the proofs.

- **Transport now costs $O(q)$.** The forward and complementary inverse exterior bounds hold at every admitted rank and cutoff, with the original quotient maps. This is small compared with the programme's $q\log a$ comparison scale.
- **The lower-root covariance is evaluated through its logarithmic term.** Its full $q^2$ and $aq$ coefficients, the term $+128q\log a$, and an $O(q)$ remainder are retained. The two source orders have different $aq$ coefficients.
- **The complete native total and every prefix are quantified.** The native total is $16C_{\partial}aq-128q\log a+O(q)$. Every prefix has its exact scalar centre with uniform $O(q)$ error; the selected growing prefix has leading size $8a^{5/2}$. That centre cannot be discarded at the finer comparison scale.
- **The attained row estimates use the original minimum.** The polynomial is minimized in its actual monic fibre before conductor transport; the old-relation Gram inverse remains. The proved envelope covers $2\le r\le q+32a$, with the separate low-row formulas preserved.
- **The covariance and row profiles are connected exactly.** Their identity gives a full weighted-row discrepancy of $O(q\log q)$ and a uniform mixed-determinant profile rate of $O(\log a/a)$. This controls the aggregate profile, not its separate signed allocations.
- **The complete action receives these calculations.** For the same original arithmetic correction,

$$
J_a-\delta^{\mathrm{ar}}_{a,1}=C_Bq^2+8q\log a+O(q).
$$

Neither $C_Bq^2$ nor the signed correction has been removed. The independent degree-$k$ proper source also retains its own metric and domain: its displacement is bounded, while its own standard-window value remains unfinished.

## Evidence and continuation

The 68-page proof supplement is accompanied by three complete cumulative LaTeX successors, the accepted proof fragments, and review and assembly records. The earlier 837-page paper and 263-page companion remain available unchanged. The public machine-readable index records 23 accepted results, their dependencies, exact proof locations, human-source keys, programme roles and three remaining calculations. This is a current-frontier index, not an exhaustive classification of every historical manuscript.

Human results are cited where used. In particular, the finite lower-bound calculation cites Gábor Szegő, *Orthogonal Polynomials*, fourth edition (1975), §12.3, equation (12.3.4), pp. 300–301. The exterior-projection step cites Russell Lyons, *Determinantal Probability Measures*, arXiv:math/0204325v4, Lemma 4.1, p. 12. The authored NIST DLMF chapters and Boyd–Vandenberghe source are credited for the specific formulas and methods used. The programme-specific comparisons are proved in the paper; no global novelty claim is made.

The next calculation retains all eight labelled flags and both original endpoints in the signed determinant return, propagates that value into the original arithmetic correction and action, and evaluates the independent proper source's own standard-window return. Aggregate estimates alone do not assign those signed values.

## Read the paper and continue the calculation

[Read the 68-page proof supplement](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260918-conductor-covariance-attained-profile/DUAL_WEB_PROOF_SUPPLEMENT.pdf).
[Complete cumulative LaTeX](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260918-conductor-covariance-attained-profile/cumulative/14_CURRENT_KERNEL_AND_MULTIPLICITY_PROOFS.tex).
[Exact next calculation](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260918-conductor-covariance-attained-profile/NEXT_CALCULATION.md).
[Package verification and provenance](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260918-conductor-covariance-attained-profile/SOURCE_PINS_AND_PUBLIC_DERIVATION.json).

[Machine-readable results and programme roles](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260918-conductor-covariance-attained-profile/research_index/PROGRAM_INDEX.json).
[Exact formula locations](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260918-conductor-covariance-attained-profile/research_index/FORMULA_LOCATORS.json).

This continuation is published as [DOI 10.5281/zenodo.22821108](https://zenodo.org/records/22821108), with the [68-page proof PDF](https://zenodo.org/records/22821108/preview/95-splitzero-conductor-covariance-proof.pdf?include_deleted=0) selected as its readable preview and a [focused 76-file source ZIP](https://zenodo.org/api/records/22821108/files/96-splitzero-conductor-covariance-sources.zip/content). The earlier 837-page paper and 263-page companion remain available unchanged.

## Earlier guide (historical snapshot)

The following guide is retained verbatim; the reading links above identify this newer source edition.

# Split-Zero cohomology: arithmetic periods, correlated tails and the complete return

This edition develops a cohomological research programme for the Riemann zeta function. Its calculations retain the original arithmetic source, quotient metrics, zero multiplicities, period maps and polynomial relations. The 837-page cumulative paper contains the continuing proof corpus; the separately readable 263-page companion collects the new tail and return calculations with their immediate supporting arguments.

The new calculations express the correlated polynomial tail as an exact Gram determinant, apply Szego's repeated-root polynomial-modification formula to the original Gamma measure, and carry the resulting maps through the signed profile, conductor restriction, independent degree-k source and complete arithmetic action. An existing low-polynomial estimate is transported through the exact inverse-dual map: this factor has an O(q) bound, with its finite constants retained. The remaining correlated tail, conductor contribution and arithmetic correction are not assigned an unproved asymptotic value. This is not a proof or disproof of the Riemann hypothesis.

This is also a corrected attribution edition. The papers now include the scoped point-of-use human-source repairs and bibliographic entries carried through the accepted source chain. The repair is documented without claiming that every historical attribution question has been resolved. Earlier editions remain available unchanged.

The source ZIP includes the complete controlling LaTeX, the two PDFs, source-use records, a machine-readable result/dependency/programme-role index, and formula locators. The index covers the current research frontier, not every claim in the historical archive. Local machine paths are converted to portable references with an explicit derivation record; protected reference texts and private conversations are excluded.

The frozen companion's front matter contains an older administrative sentence about an assigned historical-provenance task. That task has since been archived; the sentence does not describe a continuing assignment. Human sources used in new mathematics must continue to be cited at the point of use.

## Read this edition

[Read the complete 837-page cumulative paper](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260917-cited-full-tail-return/FULL_RECEIVER_CUMULATIVE_PROOFS.pdf).
[Read the separate 263-page proof companion](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260917-cited-full-tail-return/FULL_RECEIVER_PROOF_SUPPLEMENT.pdf).
[Complete cumulative LaTeX](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260917-cited-full-tail-return/14_CURRENT_KERNEL_AND_MULTIPLICITY_PROOFS.tex).
[Source and publication checks](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260917-cited-full-tail-return/PRIVACY_AND_CITATION_PRESERVATION.json).
[Reading guide and programme context](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260917-cited-full-tail-return/START_HERE.md).

[Machine-readable results and their programme roles](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260917-cited-full-tail-return/research_index/PROGRAM_INDEX.json).

This corrected edition is published as [DOI 10.5281/zenodo.22819902](https://zenodo.org/records/22819902), with the 837-page cumulative paper selected as its preview. The separate 263-page companion and complete source ZIP are also available in the [matching GitHub release](https://github.com/KokunoYumeto/zeta-function-research-reader/releases/tag/splitzero-cited-receiver-2026-09-17-9e3f86fa). The preceding [DOI edition](https://zenodo.org/records/22814080) remains available unchanged.

## Earlier guide (historical snapshot)

The following guide is retained verbatim; the reading links above identify this newer source edition.

<!-- mapping-torus-live-source:20260917 -->
Source correction, 17 September 2026: the [current mapping-torus chapter](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/satellites/19e_nonconstant_unit_fibre_k_theory.tex) now includes the proved forward-convention boundary and its Blackadar citation. [Exact scope, proof and edition history](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/source-corrections/20260917-mapping-torus-live-propagation/README.md). The archived PDFs and DOI edition retain their original bytes.

# Split-Zero cohomology: original periods, conductor transfer and mixed-state volumes

This edition develops the original mixed cohomology of the Split-Zero research programme through explicit period, conductor and Gamma-polynomial calculations. It proves a conductor vanishing-order domain for every fixed nonzero original amplitude, including the two exceptional limiting phases; an exact transfer between the two original connecting endpoints; and a finite bound for the corrected first Gamma row. A full conductor-dual construction transports the original restrictions and quotient metrics to numerator observations with controlled volume error. An exact kernel formula then expresses the complete eight-matrix mixed profile and all complementary returns in those original coordinates.

The 765-page cumulative paper includes the complete proofs and updates their earlier receiving formulas. The 103-page proof supplement reproduces the new arguments, their backward receivers and eleven complete immediate prerequisite sections; the cumulative source supplies the remaining foundations. Earlier editions and the original received sources remain in provenance. The large-degree estimates fix the original period. The first-row result retains every interior row, and the complete action retains its correlation identities. The remaining interior mixed-profile calculation is stated explicitly; this edition makes no claim to prove the Riemann hypothesis.

## Read this edition

[Read the complete 765-page cumulative paper](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260917-original-period-mixed-profile/15_CURRENT_MIXED_CONTROL_READER.pdf).
[Complete cumulative LaTeX](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260917-original-period-mixed-profile/14_CURRENT_KERNEL_AND_MULTIPLICITY_PROOFS.tex).
[Verification record](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260917-original-period-mixed-profile/12_VALIDATION.md).
[Current continuation and research context](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260917-original-period-mixed-profile/00_CONTINUE_HERE.md).
[Separate 103-page reader](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260917-original-period-mixed-profile/MIXED_PROFILE_PROOF_SUPPLEMENT.pdf).

[Read the published 765-page cumulative paper](https://zenodo.org/api/records/22814080/files/89-splitzero-original-period-mixed-profile-reader.pdf/content) · [DOI 10.5281/zenodo.22814080](https://doi.org/10.5281/zenodo.22814080) · [Complete public source ZIP](https://zenodo.org/api/records/22814080/files/90-splitzero-original-period-mixed-profile-sources.zip/content) · [All 91 individually clickable downloads](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/calculation_edition_20260917_original_period_mixed_profile/README.md). All 84 earlier downloads are retained unchanged.

Included reading companions: [103-page proof supplement](https://zenodo.org/api/records/22814080/files/91-splitzero-original-period-mixed-profile-supplement.pdf/content) · [36-page exposition and source provenance](https://zenodo.org/api/records/22814080/files/85-splitzero-exposition-provenance-reader.pdf/content) · [Exposition source package](https://zenodo.org/api/records/22814080/files/86-splitzero-exposition-provenance-sources.zip/content) · [Mapping-torus source clarification](https://zenodo.org/api/records/22814080/files/87-splitzero-mapping-torus-conventions.zip/content) · [Multiplier and module source clarification](https://zenodo.org/api/records/22814080/files/88-splitzero-multiplier-functoriality.zip/content).

<!-- multiplier-addendum:20260917 -->
## Later source correction

[Multiplier and module source clarification](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/source-corrections/20260917-multiplier-functoriality/README.md) · [Download the eight-file supplement](https://raw.githubusercontent.com/KokunoYumeto/zeta-function-research-reader/main/workbenches/splitzero-tandem/source-corrections/20260917-multiplier-functoriality/multiplier-source-clarification-2026-09-17.zip). The supplement resolves U10 for the identified finite-corner multiplier and constant-fibre uses, with full module, multiplier and corona proofs and precisely attributed source statements. The original 36-page companion and the mapping-torus correction remain unchanged. The Mingo–Phillips original-article inspection gap is explicitly retained.


## Earlier guide (historical snapshot)

The following guide is retained verbatim; the reading links above identify this newer source edition.

# Split-zero structures and the zeta-function programme: a mathematical exposition with human-source provenance

This companion introduces the split-zero/globalization-semiring research programme to mathematicians. It explains the support structure, the theta and Mellin quotient, complete zero jets, polynomial-exponential periods, and the original determinant and action calculations. Explicit comparison maps identify the theta quotient with Ralf Meyer's construction and state the precise relationship to the finite-field results of Pierre Deligne.

The 36-page reader explains the accepted moving-cutoff advance in the 726-page proof edition and displays the signed matrix allocation and complementary returns that remain to be calculated. The full proof archive is preserved. No proof of the Riemann hypothesis or historical novelty claim is made.

The package includes editable LaTeX, a 213-key BibTeX library, point-of-use citations, a human-source guide, recursive attribution records, six detailed globalization-semiring source reports, historical bibliography transcriptions, and an explicit unresolved-attribution register. Source records distinguish primary formula checks, authenticated identities, inherited reading reports and unresolved uses. AI assistance and the scope of verification are disclosed.

Begin with `RESEARCH_PROGRAMME.pdf` and `START_HERE.md`. The complete mathematical edition is [DOI 10.5281/zenodo.22803503](https://doi.org/10.5281/zenodo.22803503). Human readability, fair credit and a clear provenance record are the companion's editorial commitments.

## Read this edition

[Read the 36-page exposition and provenance companion](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260917-exposition-provenance/RESEARCH_PROGRAMME.pdf).
[Editable exposition LaTeX](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260917-exposition-provenance/RESEARCH_PROGRAMME.tex).
[Verification record](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260917-exposition-provenance/COVERAGE.md).
[Reading route and mathematical context](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260917-exposition-provenance/START_HERE.md).

The preceding [published DOI edition](https://zenodo.org/records/22803503) remains the 84-download edition until this continuation is deposited. Earlier papers and source editions are retained.

<!-- mapping-torus-addendum:20260917 -->
## Later source correction

[Mapping-torus convention correction](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/source-corrections/20260917-mapping-torus-conventions/README.md) · [Download the nine-file supplement](https://raw.githubusercontent.com/KokunoYumeto/zeta-function-research-reader/main/workbenches/splitzero-tandem/source-corrections/20260917-mapping-torus-conventions/mapping-torus-convention-addendum-2026-09-17.zip). The supplement resolves U09 for the identified historical catalogue entry and its inspected direct uses, with full even/odd boundary proofs and downstream reconciliation. The original 36-page companion remains unchanged as its dated edition; the other unresolved-source entries remain open.


## Earlier guide (historical snapshot)

The following guide is retained verbatim; the reading links above identify this newer source edition.

# Split-Zero cohomology: moving-cutoff estimates and growing-degree arithmetic volumes

This edition studies polynomial norms and quotient volumes constructed from the completed Riemann xi function. The source is the original measure obtained from 2 xi divided by the polynomial of a fixed complete zero packet; tensor powers, all zero orders, total mass and the maps into the cohomological quotient are retained. The calculation asks how the source norm compares with the norm of its original polynomial relations as both tensor order and admitted polynomial degree grow.

The 726-page cumulative paper contains the earlier Split-Zero construction and complete new proofs for a cutoff that follows the actual equilibrium support of the Gamma reference measure. Those estimates are carried through the original arithmetic coefficient maps, least-norm representatives, adjacent volume contractions and the full four-endpoint action. A separate 51-page supplement collects the new proofs and their immediate analytic prerequisites.

The new calculations give growing-degree asymptotics across the entire earlier degree band, an enlarged power-law degree range with its logarithmic approach to the endpoint, and explicit coefficient enclosures at part of the critical scale. Every displayed range retains its full domain and arithmetic constants. Earlier finite estimates and all their source text remain available. The construction does not establish the existence of an off-critical zero packet, evaluate the still-open signed mixed-state contributions, or prove or disprove the Riemann hypothesis.

The incoming post supplied mathematics in text, not a complete ZIP or compiled PDF. This is the subsequent locally assembled edition: full written proofs were reviewed at their recorded scope, both PDFs were built and their changed pages inspected, and 562 finite algebraic/diagnostic conditions were checked separately. The numerical fixtures are synthetic quartets and non-interval diagnostics, not certified computations of an actual arithmetic zero packet; no new Lean execution is claimed. Complete editable sources, source attribution and exact edition lineage accompany the readable PDFs.

## Read this edition

[Read the complete 726-page cumulative paper](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260917-moving-cutoff-growing-ratio/15_CURRENT_MIXED_CONTROL_READER.pdf).
[Complete cumulative LaTeX](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260917-moving-cutoff-growing-ratio/14_CURRENT_KERNEL_AND_MULTIPLICITY_PROOFS.tex).
[Verification record](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260917-moving-cutoff-growing-ratio/12_VALIDATION.md).
[Current continuation and research context](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260917-moving-cutoff-growing-ratio/00_CONTINUE_HERE.md).
[Separate 51-page reader](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260917-moving-cutoff-growing-ratio/GROWING_RATIO_PROOF_SUPPLEMENT.pdf).

[Read the published 726-page cumulative paper](https://zenodo.org/api/records/22803503/files/82-splitzero-moving-cutoff-reader.pdf/content) · [DOI 10.5281/zenodo.22803503](https://doi.org/10.5281/zenodo.22803503) · [Complete public source ZIP](https://zenodo.org/api/records/22803503/files/83-splitzero-moving-cutoff-sources.zip/content) · [All 84 individually clickable downloads](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/calculation_edition_20260917_moving_cutoff_growing_ratio/README.md). All 78 earlier downloads are retained unchanged.

## Earlier guide (historical snapshot)

The following guide is retained verbatim; the reading links above identify this newer source edition.

# Split-Zero cohomology: growing-degree arithmetic volume estimates

This research edition studies finite, full-multiplicity packets of zeros of the completed Riemann zeta function through the original theta-function source and its quotient by the original theta relations. It provides a cumulative reader, editable proofs, executable finite checks, and recoverable source provenance. Earlier mathematical chapters and the separate primitive connecting supplement remain available.

The new continuation estimates how the canonical quotient norms behave when the permitted polynomial degree grows faster than the finite packet dimension. A full-coefficient comparison retains the complete root polynomial and controls both the region around its roots and the two outer integration regions. An all-degree lower bound for the reference monic minimum is then carried back through the original arithmetic norms, relation fibres, determinant ratios, and adjacent contraction factors. The source mass, every zero order, and the original quotient metric are retained.

The edition also gives the explicit maps connecting these estimates to the earlier calculations. Where both apply, the new bounds are intersected with the stronger earlier fixed-proportion estimates. Changing the degree window yields four new determinant endpoints and the complete action with its original correlated terms, rather than reusing the endpoints of a different window.

An additional calculation reaches logarithmically corrected critical-power cutoffs. With packet dimension q, admissible tensor degree k, and fixed logarithmic exponent zeta greater than one third, the cutoff is r = floor(q k^(2(d−1)/3) / (log k)^zeta). Here d=2 for a simple quartet and d=3 for each fixed higher multiplicity. The proof retains the integer cutoff, root-radius guards, arithmetic comparison errors, and all endpoint terms. The uncorrected pure-power endpoint and zeta=one third are not claimed.

These results provide lower bounds on the canonical arithmetic allowances in the stated growing windows. They do not prove or disprove the Riemann hypothesis, exhibit an off-critical zero, or evaluate the separate mixed spectral profile and complementary quotient contributions of the broader programme.

The full new proofs and their receiving calculations received independent written reviews. The finite checker was replayed in ordinary and optimized Python, including deliberate-failure controls. Synthetic matrix fixtures and high-precision, non-interval Gamma-reference diagnostics are explicitly distinguished from computations on actual arithmetic zero packets. No new Lean certificate is claimed. The integrated reader has 692 pages; all new insertion sites and the nine-page standalone proof received layout review, without claiming a fresh review of every inherited page.

The incoming archive was a partial cumulative snapshot, with possible later additions. This edition preserves that qualification and records external historical references explicitly. Public provenance retains the mathematical sources while excluding private conversations and correspondence; the untouched originals remain in the local archive.

## Read this edition

[Read the complete 692-page cumulative paper](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260917-root-sensitive-growing-degree/15_CURRENT_MIXED_CONTROL_READER.pdf).
[Complete cumulative LaTeX](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260917-root-sensitive-growing-degree/14_CURRENT_KERNEL_AND_MULTIPLICITY_PROOFS.tex).
[Verification record](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260917-root-sensitive-growing-degree/12_VALIDATION.md).
[Current continuation and research context](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260917-root-sensitive-growing-degree/00_CONTINUE_HERE.md).
[Separate 9-page reader](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260917-root-sensitive-growing-degree/ROOT_SENSITIVE_GROWING_DEGREE_CORRECTED.pdf).

The preceding [published DOI edition](https://zenodo.org/records/22802593) remains the 78-download edition until this continuation is deposited. Earlier papers and source editions are retained.

## Earlier guide (historical snapshot)

The following guide is retained verbatim; the reading links above identify this newer source edition.

# Split-Zero cohomology: arithmetic volume estimates and shared quotient geometry

This research collection develops finite, full-multiplicity packets associated with zeros of the Riemann xi function inside the original theta-source quotient. It follows the maps from that arithmetic source to polynomial relations, least-norm representatives, quotient metrics and exterior spectral estimates. The complete source masses, Taylor units, zero orders, mixed pairings and coordinate maps remain part of the calculations.

The new continuation compares the original Gamma observations at different source orders, sharpens their finite comparison bounds using an explicitly derived equilibrium measure, and carries those estimates through the same connecting and invariant quotient spaces. Nested flags give a sharper finite error for the signed spectral-threshold representation while retaining the actual row contributions and complementary quotient returns.

The arithmetic action calculation also determines which terms can improve the proposed upper estimate: the correlated allocation terms cancel in the complete expression. Independent coarse and sharp estimates show that the particular canonical allowance on each fixed proportional degree window grows exponentially relative to the polynomial exterior benchmark. The collection therefore records both the proved estimates and why repeating that fixed-window strategy cannot resolve the intended comparison. A root-sensitive growing-degree calculation remains a separate continuation, not a result asserted here.

The cumulative PDF is the primary reading document. The downloadable source collection retains complete editable proofs, earlier receiving passages, the predecessor material and explicit provenance. Written mathematical review, exact finite checks and high-precision non-interval diagnostics are identified separately. This edition does not claim a proof or disproof of the Riemann hypothesis, an observed off-critical zero, new Lean certification or a numerical evaluation of the remaining actual-period spectra.

## Read this edition

[Read the complete 680-page cumulative paper](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260916-arithmetic-source-and-flag-continuation/15_CURRENT_MIXED_CONTROL_READER.pdf).
[Complete cumulative LaTeX](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260916-arithmetic-source-and-flag-continuation/14_CURRENT_KERNEL_AND_MULTIPLICITY_PROOFS.tex).
[Verification record](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260916-arithmetic-source-and-flag-continuation/12_VALIDATION.md).
[Current continuation and research context](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260916-arithmetic-source-and-flag-continuation/00_CONTINUE_HERE.md).

[Read the published 680-page cumulative paper](https://zenodo.org/api/records/22802593/files/77-splitzero-source-transport-reader.pdf/content) · [DOI 10.5281/zenodo.22802593](https://doi.org/10.5281/zenodo.22802593) · [Complete public source ZIP](https://zenodo.org/api/records/22802593/files/78-splitzero-source-transport-sources.zip/content) · [All 78 individually clickable downloads](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/calculation_edition_20260916_arithmetic_source_and_flag/README.md). All 76 earlier downloads are retained unchanged.

## Earlier guide (historical snapshot)

The following guide is retained verbatim; the reading links above identify this newer source edition.

# Split-Zero cohomology: source-volume estimates and boundary transport

**16 September source update:** [Read the current results and their purpose](workbenches/tau-programme-coordination/INTEGRATION_20260916.md) · [Complete source-order and arithmetic-action proofs](workbenches/splitzero-tandem/continuations/20260916-source-order-and-action/README.md) · [Uniform contraction and canonical-band continuation](workbenches/tau-exponential-contraction/RESEARCH_NOTE.md).

The new sources compare the original Gamma observations, calculate the complete arithmetic action, and show why its present bounded-proportion degree windows do not give a small enough canonical allowance. They include the sharp minimum rate and penalty-tail calculation, with original masses, relation fibres and all finite guards retained. PRs #36 and #37 are integrated; the expanded cumulative PDF is still being assembled. The DOI-linked PDFs below are the preceding frozen edition, not a claim that this new material is already in those PDFs.

## Published cumulative reader

[Read the delivered 549-page cumulative paper](https://zenodo.org/api/records/22773401/files/74-primitive-band-reader.pdf/content) · [Read the accepted 40-page source-band and boundary continuation](https://zenodo.org/api/records/22773401/files/75-primitive-band-supplement.pdf/content) · [DOI 10.5281/zenodo.22773401](https://doi.org/10.5281/zenodo.22773401) · [Exact current continuation](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/02e47c28b98912d3ea1ec1bf01a3a5ba44197e9f/workbenches/splitzero-tandem/continuations/20260915-primitive-band-continuation/00_CONTINUE_HERE.md).

- [549-page primitive_band](https://zenodo.org/api/records/22773401/files/74-primitive-band-reader.pdf/content) · [complete editable source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/02e47c28b98912d3ea1ec1bf01a3a5ba44197e9f/workbenches/splitzero-tandem/continuations/20260915-primitive-band-continuation) · [offline source ZIP](https://zenodo.org/api/records/22773401/files/76-primitive-band-sources.zip/content).
- [40-page source-band and boundary supplement](https://zenodo.org/api/records/22773401/files/75-primitive-band-supplement.pdf/content) · complete accepted eight-provider continuation, separately readable.

## The calculation and its purpose

Split-Zero pursues a proposed cohomological approach to Riemann zeta zeros
over tau, the programme's proposed absolute base. The calculation carries
the original conductor relations into Gamma-function Hilbert metrics and
the cohomological connecting map. Native refers to those original inner
products and their induced quotient metrics. Repeated factors, branch
intersections, coefficients, phases and fixed frames are retained.

The original period observation divides into its kernel K and invariant
residual V_A/K. Their total determinant growth is known, but the separate
leading allocations and common long connecting/invariant loss are still
being calculated. This edition supplies quantitative source estimates and
an exact residual-boundary construction for that calculation; it does not
report an exhibited off-critical-line zero.

## What the accepted continuation establishes

- **Complete translated relation bands (PSG/SGT).** A leading-monomial norm
  alone did not control the translated relations. The full relation Gram
  H_e now satisfies
  log det H_e=log F_(k,e,s)+2 d_e q log(4/pi)+o(kq),
  where q=(k+1)^2, d_e=8k+24+e, and F_(k,e,s) is the explicit product of
  the original moment coefficient, mass and Gamma factorial norms. The
  full original translation retains the explicit 2 d_e q log(4/pi)
  contribution and the remaining o(kq) error.
  Its complete low-degree kernel and reciprocal-symbol principal parts
  remain; no zero-free unit disk is assumed.
- **The original four primitive rows (PFG).** A nonzero minor from the four
  earliest independent moment rows supplies the finite lower bound, and
  the complete coefficient expansion supplies the upper bound. For the
  actual matrix W and Q=(k+5)^2, this evaluates
  log det(W* H_1 W)=4 log M_s+8 Q log Q+O_actual(Q)=o(kq).
  The four-row determinant is calculated, not discarded because its rank
  is small.
- **Return through the same primitive coordinates (PSR).** The exact identity
  Theta_e^(s)=(R_e^pol)^T diag(r!) P_e^Tay retains the full original
  relation coefficients and prescribed Taylor complement. The native
  coefficient matrix cancels against its actual inverse. Thus the source
  determinant difference between the two original Gamma orders is o(kq).
  The connecting-order difference is returned to the original compatibility
  terms chi_X-chi_Y, with the exact source ratio and both directed errors
  still present before the limit.
- **The surviving boundary quotient (RQB).** Let J be the original invariant
  source, Phi the stacked multiplication B_cof followed by the original
  target quotient, and L=ker Phi. The computed kernels prove the maps
  V/(J+L) -> W/W_inv -> im Phi/im(Phi J_0), taking
  [x] to [B_cof x] and then to [Phi x], are isomorphisms.
  Full nonreduced branch divisibility constrains L and the exact residual
  rank. The original target minimum over W_inv gives its Gamma metric Q_b,
  while the source minimum over J+L supplies its denominator.

The boundary calculation also gives the positive four-row update

    Q_b(n)=Q_b(n-1)+R_n* (I_4+L_inv,n)^(-1) R_n.

Its covariance retains all preceding lower and invariant columns. The
specified four-endpoint return yields

    V_b+V_inv+V_o=4 Fhat_j,    V_b,V_inv,V_o >= 0.

V_o is the remaining target quotient, not an omitted remainder. This
provides an aggregate upper bound and directed residual interval; it does
not assign an individual leading coefficient to V_b or V_inv.

## Remaining work and full reading objects

The next calculation is the common long connecting/invariant return and
its actual kernel/residual allocation. The source estimate, four-row bound,
coordinate maps and residual quotient above are established inputs, not
tasks to recreate. The original Gamma orders, relation coefficients,
quotient denominators, fixed-period restrictions and signed returns stay
in their stated domains. A stronger comparison being investigated beyond
the accepted source cut is not silently promoted to a proved result here.

The separate 40-page reader contains all eight provider sources and 203
original tagged equations: PDS/CIT/PDI and PSG/SGT/PFG/PSR/RQB, with full
intervening proofs. Its accepted intake records 173 identity/tag checks
over 55 pinned files and reuses the owner's all-40-page visual acceptance.
Those are source-integrity and prior-review scopes, not new numerical
experiments, PDF audits or Lean execution by this publication task.

The 549-page cumulative reader and [complete delivered editable sources](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/02e47c28b98912d3ea1ec1bf01a3a5ba44197e9f/workbenches/splitzero-tandem/continuations/20260915-primitive-band-continuation)
are the actual root-accepted integrated handoff. Their byte identities,
current prompt and source membership come from its receipts; this guide
does not substitute a research-position report for complete proofs.

## Source restoration and previous editions

The package has 21 physical files restoring 19 logical owner
files. Its large source map is carried in ordered gzip parts [11_SOURCE_MAP.json.gz.part01](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/02e47c28b98912d3ea1ec1bf01a3a5ba44197e9f/workbenches/splitzero-tandem/continuations/20260915-primitive-band-continuation/11_SOURCE_MAP.json.gz.part01), the
[manifest](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/02e47c28b98912d3ea1ec1bf01a3a5ba44197e9f/workbenches/splitzero-tandem/continuations/20260915-primitive-band-continuation/SOURCE_MAP_TRANSPORT.json), and the
[decoder](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/02e47c28b98912d3ea1ec1bf01a3a5ba44197e9f/workbenches/splitzero-tandem/continuations/20260915-primitive-band-continuation/restore_source_map.py). From the downloaded directory:

```text
python restore_source_map.py --folder RESTORED_19
```

The original logical source-map SHA-256 is `0ec0af1a8c91267390d06609d9edefac9418400b74498a199bb949ed89a1184a`;
the public logical SHA-256 is `65ec4ff61f73090dac40b4188048169ce7d87c281d79e0515a0ee8c2cfe27167`. The manifest
specifies exact restoration and recorded public locator transport.

The original/private predecessor source map and its published locator-only
derivative are different byte objects, recorded with different hashes. The
previous source asset73 restores the public derivative, not the original
private hash. Exact original predecessor restoration requires separately
supplied historical bytes matching that original identity. The current
decoder restores all 19 logical files independently of external
history; it does not fetch that predecessor map. Archive history keeps its
explicit unresolved-reference scope, and current source acceptance does
not claim unavailable historical bytes were recovered.

The [previous edition](https://doi.org/10.5281/zenodo.22772244) retains the 498-page
paper, its 13-page supplement and all 73 downloads unchanged. This edition
adds cumulative PDF74, separate 40-page PDF75 and complete ZIP76. All 76
downloads remain individually clickable; PDF74 is the pertinent preview.

- [Earlier 20260915 native conductor continuation source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/28e540812ca5d45e8943395e460799888b4e5348/workbenches/splitzero-tandem/continuations/20260915-native-conductor-continuation).
- [Earlier 20260915 native boundary continuation source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/0512b18d5479f3abc24ae654f8ffee4e5d53922e/workbenches/splitzero-tandem/continuations/20260915-native-boundary-continuation).
- [Earlier 20260915 allocation continuation source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/88cec321ccb455d1906d4abce7dc08bea6c7676d/workbenches/splitzero-tandem/continuations/20260915-allocation-continuation).
- [Earlier 20260915 dual metric continuation source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/b4076eb15afd6b036a8de62d67b88eef03efeb50/workbenches/splitzero-tandem/continuations/20260915-dual-metric-continuation).
- [Earlier 20260915 operator control continuation source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/36b2654e1d3324c6de24e324ec34bb3a98f67103/workbenches/splitzero-tandem/continuations/20260915-operator-control-continuation).
- [Earlier 20260915 first variation continuation source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/af5c17948c24f43494ea76d823322e8b3924b58d/workbenches/splitzero-tandem/continuations/20260915-first-variation-continuation).
- [Earlier 20260915 quotient moment continuation source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/bf39bac055b76ce755b91401b35570bb84d76d9a/workbenches/splitzero-tandem/continuations/20260915-quotient-moment-continuation).
- [Earlier exterior kernel continuation source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/dad07e28faa735104ddc0b137521620fc315e6fc/workbenches/splitzero-tandem/continuations/20260914-exterior-kernel-continuation).
- [Earlier conductor kernel continuation source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/41adc412ceb119ad9086b1f106e377f3de2d401a/workbenches/splitzero-tandem/continuations/20260914-conductor-kernel-continuation).
- [Earlier original kernel matrices source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/5817ef9027257375b6ff3de7048b3331077251e7/workbenches/splitzero-tandem/continuations/20260914-original-kernel-matrices).
- [Earlier original volumes source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/1c8ec52c85c173adc9f8403a8a26914955e2f5a9/workbenches/splitzero-tandem/continuations/20260914-original-volumes).
- [Earlier gamma growth source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/41f020e0475429943252e69a1b4edd849393c780/workbenches/splitzero-tandem/continuations/20260914-gamma-growth).
- [Earlier joint gamma schur source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/2be3b23974bf040f4ea06240b8a4b85372f7c71d/workbenches/splitzero-tandem/continuations/20260914-joint-gamma-schur).
- [Earlier original relation bulk source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/01fc8820e3a3ea69afa22b8ab1b0b5ca61869456/workbenches/splitzero-tandem/continuations/20260914-original-relation-bulk).
- [Earlier complete gamma return source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/01fc8820e3a3ea69afa22b8ab1b0b5ca61869456/workbenches/splitzero-tandem/continuations/20260914-complete-gamma-return).

[All 76 downloads and source identities](calculation_edition_20260915_primitive_band/README.md).

## Earlier reading guide — preserved historical edition

The following guide retains its original publication scope. The delivered
cumulative paper and separate 40-page continuation above are the current route.

# Split-Zero cohomology: source-volume estimates and boundary transport

[Start here: exact owner continuation](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260915-primitive-band-continuation/00_CONTINUE_HERE.md).

[Read the 549-page cumulative paper](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260915-primitive-band-continuation/15_CURRENT_MIXED_CONTROL_READER.pdf) · [Complete cumulative LaTeX](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260915-primitive-band-continuation/14_CURRENT_KERNEL_AND_MULTIPLICITY_PROOFS.tex) · [Verification scope](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260915-primitive-band-continuation/12_VALIDATION.md).

[75-page reader](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260915-primitive-band-continuation/01_GAMMA_READER.pdf): Historical Gamma reader; retained for its original chronology, not the current cumulative paper.

[40-page reader](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260915-primitive-band-continuation/18_PRIMITIVE_CONNECTING_READER.pdf): Separately readable complete eight-provider source-band and boundary-return proofs; the cumulative paper also carries their receiving maps. [Complete source](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260915-primitive-band-continuation/17_FULL_PRIMITIVE_CONNECTING_PROOFS.tex).

Split-Zero studies a proposed cohomological approach to the zeros of the
Riemann zeta function. Tau is the programme's absolute base object. The
calculation keeps its polynomial relations, quotient maps and original Gamma
inner products: repeated conductor factors, masses, phases and low-degree
kernels are not removed. The purpose of this continuation is to evaluate the
volume of those relations and carry that value into the cohomological source
and connecting map. No RH conclusion or programme completion is claimed.

## What was tried, why it was needed, and what works

The monic relation band gives a tractable starting determinant, but a leading
monomial alone does not determine the norm of the full translated relations.
PSG evaluates the monic relation band; SGT controls the full original conductor
translation, including its explicit 2 d_e q log(4/pi) contribution and the
remaining o(kq) error.
The exact translation retains its low-degree kernel and the complete principal
parts of its reciprocal symbol; a zero-free unit disk is not assumed.

For k=4l+1, q=(k+1)^2, d_e=8k+24+e and source order s=1 or k, retain the
actual first nonzero conductor moment mu_v and the original mass
M_s=(2 pi)^(s/2). With n_a=q+a-v, the finite comparison product is

    F_(k,e,s) = product_(a=0)^(d_e-1)
      |mu_v binom(q+a,v)|^2 M_s n_a! (s/2)_(n_a).

The full Gram of the translated relations satisfies

    log det H_e = log F_(k,e,s) + 2 d_e q log(4/pi) + o(kq).

The finite proofs retain the complete asymmetric error bounds and all the
original domain conditions before passing to this limit.

The primitive quotient also contains a four-row determinant. Its rank does
not make its magnitude negligible. PFG obtains a nonzero minor from the
earliest independent original moment rows, then bounds the complete
coefficient expansion. For Q=(k+5)^2 it proves

    log det(W* H_1 W) = 4 log M_s + 8 Q log Q + O_actual(Q).

PSR carries both estimates through the actual polynomial and Taylor-coordinate
maps. The entire native coefficient matrix cancels against its actual inverse;
the same ordered primitive-coordinate frames therefore remain for both Gamma
orders. The source determinant ratio has logarithm o(kq). For the connecting
metrics, the surviving leading difference is exactly the difference of the
original compatibility quantities X_e=chi_X-chi_Y:

    log(det H_conn,e^(k,k+4) / det H_conn,e^(1,1))
      = -X_e^(k,k+4) + X_e^(1,1) + o(kq).

This is not an evaluation of those remaining compatibility determinants.

## How the original geometry enters the boundary metric

RQB calculates the surviving boundary quotient rather than dropping it from
the connecting formula. For the original coefficient source V, invariant
subspace J, stacked multiplication map B_cof and kernel L of the original
target-quotient map Phi, it gives the exact isomorphisms

    V/(J+L) -> W/W_inv -> im(Phi)/im(Phi J_0),
    [x] -> [B_cof x] -> [Phi x].

The actual branch-polynomial valuations, including repeated factors,
determine the full kernels. The source and target quotient metrics are the
attained minima over their original relation spaces. Their Gamma row formulas,
fixed frames and positive four-row update are retained. The four-endpoint
return bounds a directed residual contribution through the exact aggregate
allocation; it does not assign either separate leading coefficient.

## Next mathematical calculation

Use these complete source estimates and maps in the common long connecting
and invariant return. Calculate its actual compatibility and residual
determinants, retaining both half-lines, every lower-evaluation minimum and
the full proper-source factors. The established source and four-row results
are inputs to that calculation, not proofs to recreate. The original signed
arithmetic return and its endpoint domains remain in force.

## Reading and evidence

The links below identify the exact root-accepted cumulative source cut and
each separately readable PDF with its own chronology. Full proofs remain in
the linked complete sources; this guide is a navigation and attempt summary,
not their replacement. Original proof-review, source-integrity, finite-test,
build and visual records retain their stated scope. No new mathematical or
PDF audit, arithmetic experiment or Lean execution is claimed by this source
publication. Local reference-only literature is not added.

## Reconstruct the complete logical edition

The accepted manifest contains 19 logical files, carried by 21 physical GitHub files. Every non-map logical body is unchanged. The full public source map uses 1 ordered gzip parts: [11_SOURCE_MAP.json.gz.part01](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260915-primitive-band-continuation/11_SOURCE_MAP.json.gz.part01).

Download the parts, [transport manifest](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260915-primitive-band-continuation/SOURCE_MAP_TRANSPORT.json), [decoder](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260915-primitive-band-continuation/restore_source_map.py) and all other declared logical files. Run `python restore_source_map.py --folder RESTORED_SOURCE` to create a separate folder with exactly the declared logical membership. The decoder verifies parts, aggregate and complete logical SHA-256 and refuses to overwrite different bytes. No excerpt replaces the complete source map.

The complete current edition restores locally without fetching historical bytes. The original historical source map is an explicitly external dependency: the predecessor public package restores its separately identified public locator derivative, not the private original hash. Historical and generated nonembedded aliases keep their declared scope. The current smaller map does not silently claim those original historical bytes are embedded.

[Previously published historical source package](https://zenodo.org/api/records/22772244/files/73-native-conductor-sources.zip/content) · [Its DOI record](https://zenodo.org/records/22772244). Both the original and public historical identities remain recorded in the source map.

The existing [DOI 10.5281/zenodo.22772244](https://doi.org/10.5281/zenodo.22772244) remains the 73-download edition, with its 498-page cumulative reader and separate 13-page supplement, until this newer source cut is published there. This source transaction does not change Zenodo, Overleaf or timers.

## Earlier source and edition guide (historical snapshot)

The following guide is preserved verbatim. Its reader and next-task statements belong to its own edition; the accepted reading list above is current.

# Split-Zero cohomology: conductor cohomology and primitive transport

[Read the 498-page cumulative paper](https://zenodo.org/api/records/22772244/files/71-native-conductor-reader.pdf/content) · [Read the later 13-page primitive/connecting supplement](https://zenodo.org/api/records/22772244/files/72-primitive-connecting-reader.pdf/content) · [DOI 10.5281/zenodo.22772244](https://doi.org/10.5281/zenodo.22772244) · [Exact current continuation](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/28e540812ca5d45e8943395e460799888b4e5348/workbenches/splitzero-tandem/continuations/20260915-native-conductor-continuation/00_CONTINUE_HERE.md).

- [498-page native_conductor](https://zenodo.org/api/records/22772244/files/71-native-conductor-reader.pdf/content) · [complete editable source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/28e540812ca5d45e8943395e460799888b4e5348/workbenches/splitzero-tandem/continuations/20260915-native-conductor-continuation) · [offline source ZIP](https://zenodo.org/api/records/22772244/files/73-native-conductor-sources.zip/content).
- [13-page primitive and connecting supplement](https://zenodo.org/api/records/22772244/files/72-primitive-connecting-reader.pdf/content) · complete later PDS/CIT/PDI proofs, separately readable.

## The problem and the new control

Split-Zero is a proposed cohomological approach to Riemann zeta zeros. It
studies arithmetic theta observations over tau, the programme's proposed
absolute base in its F1/Deligne direction. An original period observation has
a kernel K, the classes it sends to zero, and an invariant residual V_A/K.
The calculation asks how determinant growth divides between these two actual
parts and returns that control to the same arithmetic class and action form.
Here native means the original Gamma inner products and their induced
restriction and quotient metrics.

The lower-evaluation-corrected allocations remain

    S_K = sum_M w_M log(1+y_M/(1+x_M)),
    S_R = sum_M w_M log(1+x_M).

Their sum is already evaluated: (S_K+S_R)/(kq_k) tends to 16 C_partial, with
21.66851180520<16 C_partial<21.66851180521. The individual leading allocations
are still uncomputed; ranks do not assign them. Both half-lines, the original
minimum, quotient denominator and mixed pairings remain in the factorial
Gram ratios being estimated.

The cumulative paper now supplies:

- **Evaluated low boundary and high Euler terms.** WEL/BVC calculates the
  original low enlarged-boundary volume. The exact maps return its nonzero
  boundary form and full mixed numerator to the original metric, even where
  the enlarged quotient itself is zero. GKC/GVJ/GGE gives the graded complex,
  full Vandermonde transport and high Gamma Euler volume.
- **Native conductor and low cohomology.** CNC retains the nonreduced
  conductor, analytic division map, scalar alpha_A and its own coefficient
  torsion. LCA/LCC constructs the original low cohomology, primary connecting
  maps, native Grams and Schur quotients. LFC proves their short contraction
  bounds. Proper-source compatibility determinants remain when a full-space
  estimate is carried to the invariant source.
- **The original invariant row budget.** ITL/IRR/IF/FAB and NFR give the actual
  Gamma/division rows and two nonnegative four-by-four increments gamma_H,n
  and gamma_A,n. The loss retains their difference with end weights 1 and
  interior weights 2. For the same ordered generalized eigenvalues, the
  simultaneous budget bounds total log variation by beta_n and total angle
  variation by beta_n/2, where beta_n=4 log(1+rho_n D_0^(-1)rho_n*/(1+zeta_n)). D_0 is the
  full preceding original target Gram, not a selected model. The factor 4
  counts four target copies; there is no added image-rank factor.

## Separate primitive and connecting supplement

The later supplement contains all 66 equations and complete proofs PDS1-24,
CIT1-26 and PDI1-16. It is supplied separately, not silently inserted into
the fixed 498-page reader.

PDS constructs the original primitive quotient x=C_e^T w with native metric
G_e=conjugate((C_e* C_e)^(-1)), retaining its full analytic-source kernel.
The upper primitive space has codimension 3 in the lower. CIT calculates the
connecting target F_e by the attained minimum over the original lower gauges
and boundaries B_cof. PDI proves the concrete coordinate identity

    F_1 = F_0 R + B_cof A.

Here A is the solved coefficient correction, not a renamed conductor. The
image inclusion has codimension 3. The actual rank-one source and four-row
target corrections satisfy

    -log U_* <= Delta_tgt-Delta_src <= beta_next,
    Delta_tgt-Delta_src = o(kq_k).

The missing three-dimensional complement remains in full low cohomology.
The connecting-flag and low-cycle comparison errors are also proved at the
stated scales. These short corrections are completed results to use, not
the next research objective.

## What is still being calculated

The common long connecting/ITL loss remains its original quotient cross
ratio. CIT24-26 factors the complete sum log omega_conn,e + log omega_inv
through the common boundary chain, retaining the absolute Grams, original
source pullback and residual quotient Q_b. Its fixed-frame constants cancel
under the actual four-return signs; that cancellation does not assign the
long loss.

The continuation uses those full row recurrences and Schur pivots to obtain
a leading term or nontrivial interval at kq_k scale for one actual arithmetic
allocation, then the other through the exact total. It returns every bound
through the low metrics, unequal flags, proper-source and invariant-target
terms, CEP/alpha transfer and complete signed/action budget. The original
simple-quartet restrictions, fixed period/unit/branch, nonreduced coefficients,
source orders and source-specific endpoint domains remain. Degree k and
target degree j=k+4 use the paired orders (1,1) or (k,j). No moving-period
uniformity, missing inverse bound or RH conclusion is asserted.

## Complete sources, chronology and checks

[File14](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/28e540812ca5d45e8943395e460799888b4e5348/workbenches/splitzero-tandem/continuations/20260915-native-conductor-continuation/14_CURRENT_KERNEL_AND_MULTIPLICITY_PROOFS.tex) is the complete
editable cumulative paper; [file15](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/28e540812ca5d45e8943395e460799888b4e5348/workbenches/splitzero-tandem/continuations/20260915-native-conductor-continuation/15_CURRENT_MIXED_CONTROL_READER.pdf)
is its 498-page reader. [File17](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/28e540812ca5d45e8943395e460799888b4e5348/workbenches/splitzero-tandem/continuations/20260915-native-conductor-continuation/17_FULL_PRIMITIVE_CONNECTING_PROOFS.tex)
contains the complete later proofs, read together with their definitions and
providers in file14; [file18](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/28e540812ca5d45e8943395e460799888b4e5348/workbenches/splitzero-tandem/continuations/20260915-native-conductor-continuation/18_PRIMITIVE_CONNECTING_READER.pdf) is the
13-page supplement. Files09/10 are full receiving documents. This guide is
navigation, not a replacement for those proofs or the sole file00 prompt.

[Validation file12](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/28e540812ca5d45e8943395e460799888b4e5348/workbenches/splitzero-tandem/continuations/20260915-native-conductor-continuation/12_VALIDATION.md) records fourteen complete
providers, NCR/NFR receiving maps and ten insertion sources at 30 sites, plus
the separate later supplement. Full independent source/site reviews, exact
reversals, build/page checks and the root visual receipts retain their own
scope. The 8,547 mechanical source checks supplement those reviews. Finite
synthetic tests do not certify transcendental inputs. This publication
reuses completed checks and makes no new Lean-execution claim.

The ZIP and repository have 24 physical files restoring
19 logical owner files: eighteen direct files, ordered
gzip parts [11_SOURCE_MAP.json.gz.part01](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/28e540812ca5d45e8943395e460799888b4e5348/workbenches/splitzero-tandem/continuations/20260915-native-conductor-continuation/11_SOURCE_MAP.json.gz.part01), [11_SOURCE_MAP.json.gz.part02](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/28e540812ca5d45e8943395e460799888b4e5348/workbenches/splitzero-tandem/continuations/20260915-native-conductor-continuation/11_SOURCE_MAP.json.gz.part02), [11_SOURCE_MAP.json.gz.part03](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/28e540812ca5d45e8943395e460799888b4e5348/workbenches/splitzero-tandem/continuations/20260915-native-conductor-continuation/11_SOURCE_MAP.json.gz.part03), [11_SOURCE_MAP.json.gz.part04](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/28e540812ca5d45e8943395e460799888b4e5348/workbenches/splitzero-tandem/continuations/20260915-native-conductor-continuation/11_SOURCE_MAP.json.gz.part04), the [manifest](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/28e540812ca5d45e8943395e460799888b4e5348/workbenches/splitzero-tandem/continuations/20260915-native-conductor-continuation/SOURCE_MAP_TRANSPORT.json), and
the [decoder](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/28e540812ca5d45e8943395e460799888b4e5348/workbenches/splitzero-tandem/continuations/20260915-native-conductor-continuation/restore_source_map.py). From that downloaded directory:

```text
python restore_source_map.py --folder RESTORED_19
```

The complete logical source map contains 1296 distinct byte objects and 2591
source/path/role aliases. Retained original providers, reviews, diagnostics,
the 419-page predecessor and exact transformations preserve chronology.
The audit classified 249 historical-reference records. After recovery,
19 historical alias records remain unrecovered; they are not represented as
recovered bytes. All 19 current file bodies and all 17 predecessor file bodies
are complete, including the accepted proof bodies. Its original
logical SHA-256 is `d555e00303b9d25f42b51ce1539a5b20e9ab2bcd761c872835d5203659f819d9` and public logical
SHA-256 is `7844b96d3120b49afcd9b4c3a18c7cf3229c63d0fec1e67df3384c8fae5f9cfb`. Historical account locators are
the only public-content transport; gzip changes storage, not decoded bytes.

## Earlier editions

The [419-page predecessor](https://doi.org/10.5281/zenodo.22771246) and all 70 of its
downloads remain unchanged. This edition adds the separately readable
PDF 71 and PDF 72 and complete ZIP 73; PDF 71 is the pertinent preview. The
earlier reading guide below retains its historical scope.

- [Earlier 20260915 native boundary continuation source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/0512b18d5479f3abc24ae654f8ffee4e5d53922e/workbenches/splitzero-tandem/continuations/20260915-native-boundary-continuation).
- [Earlier 20260915 allocation continuation source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/88cec321ccb455d1906d4abce7dc08bea6c7676d/workbenches/splitzero-tandem/continuations/20260915-allocation-continuation).
- [Earlier 20260915 dual metric continuation source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/b4076eb15afd6b036a8de62d67b88eef03efeb50/workbenches/splitzero-tandem/continuations/20260915-dual-metric-continuation).
- [Earlier 20260915 operator control continuation source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/36b2654e1d3324c6de24e324ec34bb3a98f67103/workbenches/splitzero-tandem/continuations/20260915-operator-control-continuation).
- [Earlier 20260915 first variation continuation source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/af5c17948c24f43494ea76d823322e8b3924b58d/workbenches/splitzero-tandem/continuations/20260915-first-variation-continuation).
- [Earlier 20260915 quotient moment continuation source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/bf39bac055b76ce755b91401b35570bb84d76d9a/workbenches/splitzero-tandem/continuations/20260915-quotient-moment-continuation).
- [Earlier exterior kernel continuation source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/dad07e28faa735104ddc0b137521620fc315e6fc/workbenches/splitzero-tandem/continuations/20260914-exterior-kernel-continuation).
- [Earlier conductor kernel continuation source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/41adc412ceb119ad9086b1f106e377f3de2d401a/workbenches/splitzero-tandem/continuations/20260914-conductor-kernel-continuation).
- [Earlier original kernel matrices source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/5817ef9027257375b6ff3de7048b3331077251e7/workbenches/splitzero-tandem/continuations/20260914-original-kernel-matrices).
- [Earlier original volumes source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/1c8ec52c85c173adc9f8403a8a26914955e2f5a9/workbenches/splitzero-tandem/continuations/20260914-original-volumes).
- [Earlier gamma growth source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/41f020e0475429943252e69a1b4edd849393c780/workbenches/splitzero-tandem/continuations/20260914-gamma-growth).
- [Earlier joint gamma schur source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/2be3b23974bf040f4ea06240b8a4b85372f7c71d/workbenches/splitzero-tandem/continuations/20260914-joint-gamma-schur).
- [Earlier original relation bulk source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/01fc8820e3a3ea69afa22b8ab1b0b5ca61869456/workbenches/splitzero-tandem/continuations/20260914-original-relation-bulk).
- [Earlier complete gamma return source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/01fc8820e3a3ea69afa22b8ab1b0b5ca61869456/workbenches/splitzero-tandem/continuations/20260914-complete-gamma-return).

[All 73 downloads and source identities](calculation_edition_20260915_native_conductor/README.md).

## Earlier reading guide — preserved historical edition

The following is the unchanged prior guide. The 498-page paper and separate
13-page supplement above are the current reading route.

# Split-Zero cohomology: conductor cohomology and primitive transport

[Start here: exact owner continuation](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260915-native-conductor-continuation/00_CONTINUE_HERE.md).

[Read the 498-page cumulative paper](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260915-native-conductor-continuation/15_CURRENT_MIXED_CONTROL_READER.pdf) · [Complete cumulative LaTeX](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260915-native-conductor-continuation/14_CURRENT_KERNEL_AND_MULTIPLICITY_PROOFS.tex).

[Read the separate 13-page primitive supplement](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260915-native-conductor-continuation/18_PRIMITIVE_CONNECTING_READER.pdf) · [Its complete PDS/CIT/PDI proofs](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260915-native-conductor-continuation/17_FULL_PRIMITIVE_CONNECTING_PROOFS.tex) · [Verification scope](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260915-native-conductor-continuation/12_VALIDATION.md).

Split-Zero develops a proposed cohomological approach to the zeros of the
Riemann zeta function. Tau is the programme's absolute base object; the
proposed Deligne mixed-cohomology route remains active. Here "native" means
the original conductor and Gamma inner products, with repeated conductor
factors and low-degree data retained. This edition calculates the conductor's
low cohomology, boundary volumes and invariant row control. A separate later
supplement proves primitive-source and connecting-target transport. These
results advance the original mixed-state calculation. No RH conclusion or
programme completion is claimed.

## Two complete readers, with their chronology retained

The fixed 498-page cumulative reader adds fourteen complete providers:
WEL1-38 including 32a, BVC1-11, GKC1-33, GVJ1-8, GGE1-23, PCJ1-18,
CNC1-24, LCA1-41, LCC1-31, LFC1-22, ITL1-31, IRR1-27, IF1-41 and
FAB1-15. NCR1-18 and NFR1-5 prove their receiving maps. Ten full insertion
sources propagate the results at 30 actual sites in complete sources 09,
10 and 14. The sealed 419-page predecessor remains part of the lineage.

Files 17 and 18 separately supply all 66 numbered equations and complete
PDS1-24, CIT1-26 and PDI1-16 proofs, with a 13-page reader. These later
primitive and connecting results have not been silently inserted into the
fixed 498-page source cut. Read their full definitions and providers in
file 14 alongside the complete supplement source in file 17.

## Original mixed quantities and conductor cohomology

Keep the fixed actual hypothetical simple quartet, original five-orbit
period, amplitude, unit and logarithm branch. Retain k=4l+1>=9,
q_k=(k+1)^2, q'_k=(k-7)^2, Delta_k=16k-48, v=ord_0 E_A and
alpha_A=v!/mu_v. The actual v remains in every matrix and factorial,
including on the certified v<=32 locus. Gamma masses and weights remain
M_s=(2pi)^(s/2) and h_n,s=M_s n!(s/2)_n. At target degree j=k+4,
use the paired orders (s_0,s_1)=(1,1) or (k,j), not an unproved reuse of k.

After the full lower-evaluation minimum, the actual row allocations are

    S_K = sum_M w_M log(1+y_M/(1+x_M)),
    S_R = sum_M w_M log(1+x_M),
    S_K+S_R = sum_M w_M log(1+x_M+y_M).

The two end weights are 1 and the interior weights 2, for total weight 2q_k.
Their total is already evaluated:

    (S_K+S_R)/(kq_k) -> 16 C_partial,
    21.66851180520 < 16 C_partial < 21.66851180521.

Ranks do not assign either separate allocation. The original GPA/LVM/GVM
realization retains the two-half-line map W=[A P; R A P], cross terms,
phases, factorial weights, source minimum and full quotient denominator.

WEL/BVC evaluates the actual low enlarged-boundary volume with finite
asymmetric errors and its centered limit. The zero low enlarged quotient
does not remove its nonzero boundary form or the full mixed numerator
C_D^* H_B^+ C_D. High endpoints retain their exact domains, R_cov or the
actual edge tests; an eliminant zero alone assigns no rank.

GKC/GVJ/GGE gives the signed five-term graded complex, coefficient torsion,
Vandermonde transport and high Gamma Euler volume. CNC constructs the
native nonreduced conductor quotient complex with its analytic division
map and scalar alpha_A. Its own coefficient torsion is an exact determinant,
not the full graded complex's torsion copied into a different quotient.
PCJ/NCR retains proper-source companion corrections, source-kernel
restrictions and every compatibility determinant.

LCA/LCC computes low-cutoff cohomology, full primary-block connecting maps,
native Grams and Schur quotients. For e=0,1 the original H^1 dimension is
8k+24-3e+kappa_e, where kappa_e is the kernel dimension of the stated tail
matrix. The primitive connecting part has dimension 8k+24-3e; the low
inclusion has codimension 3+kappa_0-kappa_1, between 3 and 6. LFC proves
the two low contraction bounds through the original flags and fixed frames.
NCR/LCC installs them in the signed return, without assigning the surviving
common long determinant.

## Original invariant rows and simultaneous control

ITL/IRR/IF/FAB and NFR supply the invariant target loss at every endpoint
and intervening row. With d=q_j-v-1,

    log omega_n-log omega_(n-1) = gamma_H,n-gamma_A,n,
    gamma_H,n = log det(I_4+L_T,n)-log det(I_4+L_W,n) >= 0,
    gamma_A,n = log det(I_4+L_S,n)-log det(I_4+L_K,n) >= 0,
    L_inv = sum_(n=d+1)^(d+q_j+1) theta_n (gamma_H,n-gamma_A,n).

The end weights theta_n are 1 and interior weights 2. These are the actual
Gamma coefficient/analytic-division rows, using the entire preceding raw
Gram of each original flag, not generic matrix fixtures.

For the same ordered generalized eigenvalues lambda_i, FAB/NFR bounds
the sum of absolute row changes in log lambda_i by beta_n, and the sum
of absolute changes in arcosh(lambda_i^(-1/2)) by beta_n/2, where

    beta_n = 4 log(1+rho_n D_0^(-1) rho_n^*/(1+zeta_n)).

D_0, rho_n and zeta_n use the same full preceding lower Gram. The factor 4
counts the original target copies; no extra image-rank factor is inserted.
The complete signed return obeys |L_inv|<=sum theta_n beta_n. The common-
update error is O_actual(k log q_k), but the full compatibility ratio and
long signed return remain their original unevaluated determinants.

## What the separate primitive supplement proves

PDS identifies the primitive-source quotient x=C_e^T w with its full
analytic-source kernel and native metric conjugate((C_e^* C_e)^(-1)).
The upper primitive space has codimension three in the lower one. Its
fixed-coordinate rank-one metric correction is bounded by the original
finite product log U_*=O_actual(q_j)=o(kq_k), retaining all masses,
factorials, phase-dependent nodes and conductor coefficients.

CIT gives the original connecting matrix F_e, its attained lower-gauge and
boundary minimum, and full Schur metric H_conn,e. Its low-source comparison
keeps the exact proper-source difference -(chi_X-chi_Y) and the proved
O_actual(k log q_k) error. The e=1 comparison retains all four polynomial
constraints; later target rows use fixed coefficient flags.

PDI proves F_1=F_0 R+B_cof A, with A the solved coefficient correction,
and a codimension-three inclusion of the original connecting targets.
The actual rank-one source and four-row target increments give

    -log U_* <= Delta_image/source=Delta_tgt-Delta_src <= beta_next,
    Delta_image/source=o(kq_k).

The missing three-dimensional old complement stays in full low cohomology.
PDI controls the difference of the two fixed connecting returns by
6 log A_end=o(kq_k); CIT controls the full-low-cycle/connecting difference
by 2 kappa_e log A_end. These short corrections are completed results.

## Remaining common long loss and arithmetic allocation

The common connecting quotient cross ratio omega_conn,e remains to be
calculated. CIT24-26 relates it to the original ITL loss through the full
common boundary chain, retaining log omega_conn,e+log omega_inv, all
absolute Grams, the source pullback A_inv, residual quotient Q_b and fixed
frames. Four-return signs cancel the stated frame constants, not the
unknown common long loss.

Begin with this exact factorization and the complete CIT/IRR row recurrences.
Calculate the original full row entries and Schur pivots, retaining Q_b,
both half-lines, every lower-evaluation minimum, multiplier kernel and
proper-source/invariant-target determinant. Prove the transport to the
arithmetic rows after W before estimating it. Use the evaluated low boundary,
LFC corrections and FAB budget at their typed endpoints. An evaluated leading
term or nontrivial kq_k-scale interval for one allocation would constrain its
partner through the exact total. Neither a rank fraction nor an assumed small
inverse supplies that calculation.

Return each improvement through NBR/WNR, NCR/NFR, OAR/PMR and the full action
budget. Retain opposite primal/dual signs, unequal errors, both original low
metrics, CEP/alpha_A transfer, reference boundary, monic window, contraction
penalties, leakage, mixed pairing and the same nonzero arithmetic class.
Each theorem keeps its original fixed/moving-period, simple-quartet,
polar-width and source-by-source endpoint domain. The short primitive/low
corrections are inputs to this next calculation, not tasks to prove again.

## Reading, provenance and accepted verification scope

File 00 is the sole reviewed owner continuation. Files 14/15 are the fixed
complete cumulative source and reader; files 17/18 are the complete later
primitive source and separate reader. Complete receivers 09/10 retain all
providers and actual insertion sites. Files 01-08, 13 and 16 are unchanged;
file 01 remains historical. All 12 TeX files and all three PDFs stay exact
accepted bytes in public transport.

The owner records full independent proof/site reviews, build and visual
acceptance for the exact cumulative PDF and the separate supplement. Build,
reference, glyph and page-bound receipts retain their stated inspection
scopes. The source handoff's 8,547 mechanical checks supplement the full
reviews; they do not replace them. Normal/optimized finite fixtures do not
certify an actual transcendental period. No new Lean execution or publication-
side mathematical/PDF re-audit is claimed.

Display reversal recovers the accepted canonical sources; insertion reversal
recovers the complete sealed 419-page sources. The owner provenance map
records 1,296 distinct byte objects and 2,591 path/role aliases, exact earlier
deliveries, full provider wrappers, reviews, diagnostics and reversible
changes. Repeated bytes are stored once; the inherited map remains one exact
compressed object in the owner archive. Historical stale references remain
explicit, not silently certified as recovered bytes. Public locator derivatives
and any inherited public-object substitutions retain their actual recorded
original/public identities and limited scope. Broader provenance does not
silently add later mathematical work to this accepted edition.

## Reconstruct the complete logical edition

The actual accepted manifest contains 19 logical files,
carried by 24 physical GitHub files. Every non-map
logical file is unchanged. The complete public source map uses 4
ordered gzip parts: [11_SOURCE_MAP.json.gz.part01](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260915-native-conductor-continuation/11_SOURCE_MAP.json.gz.part01) · [11_SOURCE_MAP.json.gz.part02](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260915-native-conductor-continuation/11_SOURCE_MAP.json.gz.part02) · [11_SOURCE_MAP.json.gz.part03](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260915-native-conductor-continuation/11_SOURCE_MAP.json.gz.part03) · [11_SOURCE_MAP.json.gz.part04](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260915-native-conductor-continuation/11_SOURCE_MAP.json.gz.part04).

The [transport manifest](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260915-native-conductor-continuation/SOURCE_MAP_TRANSPORT.json) binds each part, their complete
stream and the logical map. Download all listed parts, the manifest,
[restore_source_map.py](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260915-native-conductor-continuation/restore_source_map.py) and the other logical files into
one directory. Run `python restore_source_map.py --folder RESTORED_SOURCE`
to create a separate folder with exactly the declared logical membership and
no transport helpers. The decoder checks each part, aggregate and logical
SHA-256 and refuses to overwrite different bytes. Its default command
restores only the full public source map. No raw file-11 or unsplit-gzip
GitHub leaf is claimed, and the public guide remains outside the flat folder.

The existing [DOI 10.5281/zenodo.22771246](https://doi.org/10.5281/zenodo.22771246) remains the 70-download,
419-page native-boundary edition until this source cut is separately published
there. This source transaction makes no Zenodo, Overleaf or timer changes.

## Earlier source and edition guide (historical snapshot)

The following guide is preserved verbatim. Its reader and next-task statements
belong to its own edition. The cumulative paper and separate supplement above
are the current accepted reading pair.

# Split-Zero cohomology: native boundary and polar transport

[Read the current 419-page paper](https://zenodo.org/api/records/22771246/files/69-native-boundary-reader.pdf/content) · [Published DOI 10.5281/zenodo.22771246](https://doi.org/10.5281/zenodo.22771246) · [Exact current continuation and next calculation](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/0512b18d5479f3abc24ae654f8ffee4e5d53922e/workbenches/splitzero-tandem/continuations/20260915-native-boundary-continuation/00_CONTINUE_HERE.md).

- [419-page native_boundary](https://zenodo.org/api/records/22771246/files/69-native-boundary-reader.pdf/content) · [complete editable source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/0512b18d5479f3abc24ae654f8ffee4e5d53922e/workbenches/splitzero-tandem/continuations/20260915-native-boundary-continuation) · [offline source ZIP](https://zenodo.org/api/records/22771246/files/70-native-boundary-sources.zip/content).

## The mathematical question

Split-Zero is a proposed cohomological approach to Riemann zeta zeros. It
studies arithmetic theta cohomology attached to a finite packet of those
zeros. Its original period observation has a kernel K, the
classes it sends to zero, and an invariant residual V_A/K. The programme
measures both in the original Gamma and arithmetic metrics and carries them
back to the same cohomological class and action form A*G+GA-kG. This is the
concrete F1/Deligne mixed-cohomology direction being pursued.
Here "native" means the original Gamma inner products and their induced
restriction and quotient metrics.

An exact total determinant growth is already evaluated. The remaining question
is how much belongs to the kernel and how much to the invariant residual.
With the actual lower-evaluation minimum retained, their increments are

    S_K = sum_M w_M log(1+y_M/(1+x_M)),
    S_R = sum_M w_M log(1+x_M).

The weights are 1 at the two ends and 2 inside, with total 2q. Their sum has
limit (S_K+S_R)/(kq) ->16 C_partial, where
21.66851180520<16 C_partial<21.66851180521. That evaluated total does not assign
either individual coefficient. The source orders remain 1 and k, q=(k+1)^2,
k=4l+1, and the four primal degrees are q-1,q,2q-1,2q with signs ++--.
Native dual endpoints use their actual reversed order.

The 419-page cumulative Split-Zero paper studies how the original Gamma and arithmetic observations divide between the period kernel K and its invariant residual V_A/K. All-multiplicity polar principal parts identify the native conductor quotient, with its induced metric, low flag and action leakage. Exact source-window maps retain their source kernels and ordered-log-spectrum losses. Complete boundary and enlarged-boundary maps return these observations through the same signed four-endpoint budget; neither rank alone nor a change of coordinates allocates the known total determinant growth between kernel and residual.

## What the new maps accomplish

- **Retain every pole and the original quotient.** Polar principal parts keep
  residues and higher-pole coefficients. Their full observation has kernel
  im(C_prim^T), where C_prim is the original q' by q conductor, q'=(k-7)^2.
  The complete conductor and all multiplicities remain in the quotient metric.
  A squarefree polynomial appears only in the separate calculation of action
  leakage. The explicit maps, not an identification of unrelated coordinates,
  connect those two uses.
- **Transport the actual high metric and low flag.** With the retained pole
  basis B_pole, the note calculates
  H_pole,N=B_pole^(-*) conjugate(Omega_N) B_pole^(-1),
  T_pole=alpha_A P Pi_k Z_exp,k J_k, and
  H_hi,N=T_pole* H_pole,N T_pole. The low-flag exact sequence, its Schur factor,
  and the complete CEP/alpha comparison are returned afterward. Selecting
  pole coordinates supplies no unproved uniform inverse estimate.
- **Carry source windows through their kernels.** The exact source-window maps
  identify the native quotient and its induced metric while retaining the
  source kernel and matched ordered-log-spectrum loss. WNR21 gives
  S_K=sum_h S_R,j_h - V_ker(Psi) + n_mult + o(kq), with j_h=k-d_h.
  Here n_mult is the original signed four-endpoint sum of log-positive
  reciprocal metric eigenvalues. Both V_ker(Psi) and n_mult still require
  quantitative evaluation; neither has been discarded as a coordinate cost.
- **Keep boundary and enlarged-boundary information.** Complete finite Bezout
  maps are built before quotienting, with all gauges and Gram matrices.
  Native source kernels and target invariant factors remain in their exact
  transport. The enlarged-boundary square retains the high-factorial bound;
  its high quotient is positive precisely off its exceptional set, and the
  low enlarged quotient is zero. The formulas do not take the logarithm of
  a zero determinant. Exact edge tests apply outside the certified full-width
  period range.

The preceding 317-page factorial route remains available in full. Both
half-lines enter W=[AP;RAP] and the original three Gram volumes D_U,D_K,D_E.
Kernel and residual use consecutive ratios D_K/D_U and
|det[Z_k,C_LVM]|^2 D_E/D_K, with the fixed right inverse
C_LVM=P_Y* (P_Y P_Y*)^(-1). Full-row pivot bounds retain unequal o(kq) errors.
The lower minimum, quotient denominator and coupled contributions are not
replaced by rank fractions.

## What remains to calculate

The current owner continuation calls for the actual factorial mixed-volume
or full-Schur-pivot allocations C_K and C_R: derive the original coupled-row
recurrence, including both half-lines, and obtain a leading value or strict
interval at kq scale. It also returns the polar low flag, action maps,
source-kernel volume and invariant spectral loss to the complete signed and
action budgets. The original F_L, F_W0, unequal flags, contractions, leakage,
CEP/alpha errors, correlated arithmetic comparison and mixed terms remain.

The fixed five-orbit period, unit and logarithm branch are retained. The
GPA/LVM/GVM comparison uses k>=29 and its stated small-parameter domain;
the enlarged-boundary calculation uses k>=37. The eventual source-window
estimate requires each nonzero-degree source j>=4096 and
j sqrt(delta^2+gamma^2)<=2^(-33)(j+1)^2. Its first eligible target congruent
to 1 modulo 4 is 4125 when the maximum shift is 28, still subject to that
quartet inequality. Arithmetic applications retain |u|>=R_* and the exact
period tests. These fixed-period statements do not assert moving-period
uniformity.

This fixed edition preserves the 317-page proofs, the 338-page source-only intermediate and thirteen complete new bodies: CFR, RPK, DFX, BGA, NBG, NKC, EBG, RPB, OW, NW, PLF, WNR and NBR, with 21 receiving-site insertions. Repeated poles, original orders 1,k, masses, factorials, fixed period, low flags, both half-lines, unequal errors and the full action budget remain. The separate kernel/residual factorial mixed-volume allocations, source-kernel volume and invariant spectral loss remain to be quantified. Later local companion continuations are not silently included. No RH conclusion, moving-period uniformity or unproved inverse bound is claimed.

## Full proofs and the accepted reading cut

[File14, complete editable paper](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/0512b18d5479f3abc24ae654f8ffee4e5d53922e/workbenches/splitzero-tandem/continuations/20260915-native-boundary-continuation/14_CURRENT_KERNEL_AND_MULTIPLICITY_PROOFS.tex)
and [file15, 419-page GitHub PDF](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/0512b18d5479f3abc24ae654f8ffee4e5d53922e/workbenches/splitzero-tandem/continuations/20260915-native-boundary-continuation/15_CURRENT_MIXED_CONTROL_READER.pdf)
are the current paper. Files09/10 are complete receiving documents, not
summaries. [File00](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/0512b18d5479f3abc24ae654f8ffee4e5d53922e/workbenches/splitzero-tandem/continuations/20260915-native-boundary-continuation/00_CONTINUE_HERE.md) is the sole continuation
prompt; this guide does not replace it.

[Validation file12](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/0512b18d5479f3abc24ae654f8ffee4e5d53922e/workbenches/splitzero-tandem/continuations/20260915-native-boundary-continuation/12_VALIDATION.md) records the accepted thirteen
complete proof bodies, their 21 receiving insertions, exact source reversals,
reader build and the completed 419-page rendering and visual checks. The
full CFR proof remains distinct from the narrower RPK interface review;
both full NBR and WNR proofs are present. RPK's 59 normal and 59 optimized
finite checks remain supplementary, not arithmetic or transcendental
certification. The 338-page intermediate is preserved as a source-only
stage, not another delivered visually accepted reader. This edition reuses
the owner's completed checks; it claims no new proof review, PDF audit or
Lean execution.

## Complete source archive and restoration

The repository and ZIP contain 20 physical files restoring all
17 logical owner files. Sixteen owner files are directly
readable. The large source-map file11 is transported losslessly through the
ordered gzip parts [11_SOURCE_MAP.json.gz.part01](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/0512b18d5479f3abc24ae654f8ffee4e5d53922e/workbenches/splitzero-tandem/continuations/20260915-native-boundary-continuation/11_SOURCE_MAP.json.gz.part01), [11_SOURCE_MAP.json.gz.part02](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/0512b18d5479f3abc24ae654f8ffee4e5d53922e/workbenches/splitzero-tandem/continuations/20260915-native-boundary-continuation/11_SOURCE_MAP.json.gz.part02), the
[transport manifest](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/0512b18d5479f3abc24ae654f8ffee4e5d53922e/workbenches/splitzero-tandem/continuations/20260915-native-boundary-continuation/SOURCE_MAP_TRANSPORT.json), and the
[restoration script](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/0512b18d5479f3abc24ae654f8ffee4e5d53922e/workbenches/splitzero-tandem/continuations/20260915-native-boundary-continuation/restore_source_map.py). Follow that manifest
to recover the complete `11_SOURCE_MAP.json`. The parts are consecutive byte
ranges of one gzip stream. Neither a nonexistent raw-file route nor an
unsplit gzip route is presented as a download.

From the directory containing the downloaded physical files, run:

```text
python restore_source_map.py --folder RESTORED_17
```

The command creates `RESTORED_17` with all seventeen logical owner files,
including the complete decoded source map, using the manifest's identities.

The source map retains 482 distinct byte objects and 734 original path/role
aliases, including the accepted current proof bodies in full, their reviews,
diagnostics and recoverable historical bytes. Two superseded historical
objects referenced at three old provenance edges are unavailable; the
accepted current proof bodies are present. Reversal claims concern the
recorded transformations whose required bytes are retained, not those two
missing historical objects. The original logical source-map SHA-256 is
`bbd528db3a0b1046985cdcdf76210e6c1f9846232968ffd59eff7669f42195a2`; its public logical SHA-256 is
`01b557e03fc7c749134d134be818dd89f7b849f565d08d3f06a66d75881355c7`. Historical account locators are the only
public-content transport. Gzip changes storage, not those decoded bytes.
Broader provenance is not blanket acceptance of every historical draft.
Later local companion and further invariant-target continuations are not
silently added to this fixed 419-page edition.

## Earlier editions and separate downloads

- [Earlier 20260915 allocation continuation source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/88cec321ccb455d1906d4abce7dc08bea6c7676d/workbenches/splitzero-tandem/continuations/20260915-allocation-continuation).
- [Earlier 20260915 dual metric continuation source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/b4076eb15afd6b036a8de62d67b88eef03efeb50/workbenches/splitzero-tandem/continuations/20260915-dual-metric-continuation).
- [Earlier 20260915 operator control continuation source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/36b2654e1d3324c6de24e324ec34bb3a98f67103/workbenches/splitzero-tandem/continuations/20260915-operator-control-continuation).
- [Earlier 20260915 first variation continuation source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/af5c17948c24f43494ea76d823322e8b3924b58d/workbenches/splitzero-tandem/continuations/20260915-first-variation-continuation).
- [Earlier 20260915 quotient moment continuation source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/bf39bac055b76ce755b91401b35570bb84d76d9a/workbenches/splitzero-tandem/continuations/20260915-quotient-moment-continuation).
- [Earlier exterior kernel continuation source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/dad07e28faa735104ddc0b137521620fc315e6fc/workbenches/splitzero-tandem/continuations/20260914-exterior-kernel-continuation).
- [Earlier conductor kernel continuation source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/41adc412ceb119ad9086b1f106e377f3de2d401a/workbenches/splitzero-tandem/continuations/20260914-conductor-kernel-continuation).
- [Earlier original kernel matrices source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/5817ef9027257375b6ff3de7048b3331077251e7/workbenches/splitzero-tandem/continuations/20260914-original-kernel-matrices).
- [Earlier original volumes source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/1c8ec52c85c173adc9f8403a8a26914955e2f5a9/workbenches/splitzero-tandem/continuations/20260914-original-volumes).
- [Earlier gamma growth source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/41f020e0475429943252e69a1b4edd849393c780/workbenches/splitzero-tandem/continuations/20260914-gamma-growth).
- [Earlier joint gamma schur source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/2be3b23974bf040f4ea06240b8a4b85372f7c71d/workbenches/splitzero-tandem/continuations/20260914-joint-gamma-schur).
- [Earlier original relation bulk source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/01fc8820e3a3ea69afa22b8ab1b0b5ca61869456/workbenches/splitzero-tandem/continuations/20260914-original-relation-bulk).
- [Earlier complete gamma return source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/01fc8820e3a3ea69afa22b8ab1b0b5ca61869456/workbenches/splitzero-tandem/continuations/20260914-complete-gamma-return).

The [preceding 68-download edition](https://doi.org/10.5281/zenodo.22760901) keeps its
317-page preview unchanged. This edition adds PDF 69 and ZIP 70. All 70 downloads
remain separately clickable, with the current 419-page paper as the preview.
The ZIP is a complete offline source package, not the reading preview.
Existing earlier mathematical sources and publication records are unchanged.

[All 70 downloads and source identities](calculation_edition_20260915_native_boundary/README.md).

## Earlier reading guide — preserved historical edition

The following text belongs to the preceding publication and retains its
historical scope. The 419-page guide above is the current route; no earlier
mathematical source is rewritten.

# Split-Zero cohomology: native boundary and polar transport

[Start here: exact current continuation](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260915-native-boundary-continuation/00_CONTINUE_HERE.md).

[Read the 419-page paper](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260915-native-boundary-continuation/15_CURRENT_MIXED_CONTROL_READER.pdf) · [Complete LaTeX proofs](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260915-native-boundary-continuation/14_CURRENT_KERNEL_AND_MULTIPLICITY_PROOFS.tex) · [Verification scope](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260915-native-boundary-continuation/12_VALIDATION.md).

Split-Zero develops a proposed cohomological approach to the zeros of the
Riemann zeta function. A fixed period observation divides its arithmetic
source into an observation kernel and invariant residual. Here "native"
means the original Gamma inner products; "polar" means residues and
higher-pole coefficients. This edition gives explicit maps between those
descriptions while retaining every original source and quotient factor.
Tau is the programme's absolute base object. The proposed Deligne
mixed-cohomology route remains active. No RH conclusion or programme
completion is claimed.

The accepted 419-page cumulative reader preserves the 317-page reader lineage
and the complete accepted 338-page source-only intermediate edition. It adds
13 complete bodies: CFR1-45, RPK1-32, DFX1-35, BGA1-23, NBG1-32, NKC1-17,
EBG1-33, RPB1-19, OW1-18, NW1-13, PLF1-19, WNR1-21 and NBR1-23. All occur
once in each complete source 09, 10 and 14. Twenty-one receiving-site
insertions carry the results through the earlier calculations. Original
numbering conventions and all unnumbered proofs remain.

## Exact quantities and native-to-polar maps

Retain the fixed actual simple quartet, original five-orbit period, amplitude,
unit and logarithm branch. Keep k=4l+1>=9, q=(k+1)^2, q'=(k-7)^2,
Delta=16k-48, v=ord_0 E_A, alpha_A=v!/mu_v, m=Delta-v and
t0=dim(K intersect L). Source orders remain 1 and k, with
h_n=M_s n!(s/2)_n and M_s=(2pi)^(s/2). The four primal signs at
q-1,q,2q-1,2q are (+,+,-,-); the complete dual transport reverses them.

The actual corrected-row allocations remain

    S_K = sum_M w_M log(1+y_M/(1+x_M)),
    S_R = sum_M w_M log(1+x_M),
    S_K+S_R = sum_M w_M log(1+x_M+y_M).

Both end rows have weight 1 and the interior rows weight 2, giving total
weight 2q. Every row uses the entire preceding lower-evaluation minimum.
The exact total is already evaluated:

    (S_K+S_R)/(kq) -> 16 C_partial,
    21.66851180520 < 16 C_partial < 21.66851180521.

This total and the individual ranks do not assign either separate allocation.
The fully coupled GPA/LVM/GVM factorial map W=[A P; R A P] keeps both
half-lines, their cross terms, phases and factorials. Its consecutive mixed
volume ratios and deterministic full-row pivot bounds remain the analytic
input, not generic positive matrices or freely chosen metrics.

RPK supplies the unit-independent eliminant radius, full principal-part
observation with all conductor multiplicities and exact action-leakage rank.
ASR's earlier full-support result keeps its chronology. RPB identifies the
conductor coefficient with scalar one and combines the two exterior domains
using R_cov=min(R_supp,R_rank). Elsewhere retain the actual edge tests: an
eliminant zero alone assigns no rank. The sharper v<=32 holds on the original
five-orbit locus, while the actual v remains in each matrix and factorial.

PLF/NBR connects the full polar observation to the same original residual
metrics. The principal-part map Pi_k has kernel im(C_prim^T), rank Delta
and all residue and higher-pole slots. Its fixed residual coordinates give

    H_pole,N = B_pole^(-*) conjugate(Omega_N) B_pole^(-1),
    T_pole = alpha_A P Pi_k Z_exp,k J_k,
    H_hi,N = T_pole^* H_pole,N T_pole.

The full low-flag exact sequence keeps low-observation rank v-t0 and its
Schur factor. Thus Phi=F_W0+S_R+delta_0 retains the complete finite
CEP/alpha_A bound. Polar coordinates do not provide an unproved uniform
inverse. The action detector's squarefree reduction is distinct from the
full multiplicity-preserving conductor quotient and its native metric.

## Native boundary and displaced-window control

The native multiplier calculation retains the full kernel of the multiplier
sum, its image metric and all coupled low-jet relations. NW/OW/WNR controls
all four actual source-displacement windows, including j=k-d_h. On its
source-by-source domain j>=4096 and
j sqrt(delta^2+gamma^2)<=2^(-33)(j+1)^2, WNR21 gives

    S_K = sum_h S_R,j_h - V_ker(Psi) + n_mult + o(kq).

The full coupled source-kernel return V_ker(Psi) and signed matched-relative-
metric loss n_mult remain unevaluated finite expressions. Earlier degrees
retain their complete outer determinant bounds. For d_max=28 the first
eligible congruent target is 4125, with the quartet inequality still required.

DFX/BGA/NBG/NKC gives the full four-component degree-four map, finite Bezout
inverse before quotients, compatible lower gauges and full compatibility Gram.
NBR supplies the subsequent source-kernel and invariant-target determinant
factors. EBG/RPB/NBR gives the native enlarged-gauge square and coupled
high-endpoint factorial bound. The low enlarged quotient is zero; no logarithm
of that zero quotient is used. The high numerator is positive exactly off
E_infinity, including the certified exterior domain. The boundary ranks
24k-24-v, 24k-23-v, 26k-13, 26k-13 keep signed mass-rank jump 4k+21+2v.

## Next calculation and complete arithmetic return

Estimate the separate actual mixed-volume sums C_K,C_R from the full relation
and invariant recurrences after W. Derive the actual Schur-pivot evolution,
including both half-lines, the lower-evaluation minimum and quotient
denominator. Use the RPK/PLF maps to locate the residual rows and mixed
coupling. A proved leading term or nontrivial kq-scale interval for one
allocation constrains its partner through the exact total. A failed pivot
profile calls for its precise defect or exceptional set, not an assumed
rank proportion or small inverse.

NBR19-23 and WNR15-20 carry improvements through both original low metrics,
unequal flag errors, CEP/alpha_A transfer, correlated arithmetic caps and
the signed mixed return. Retain the reference boundary, monic window, both
contraction penalties, leakage, mixed pairing and same nonzero arithmetic
class in the whole action budget. Kernel volume is not the full exterior
allowance. GPA/LVM/GVM retains k>=29 and its 2^(-33)q domain; EBG retains
its complete k>=37 domain; WNR retains its source-by-source eventual domain.
Arithmetic statements keep |u|>=R_*; polar full width uses R_cov or exact
coefficient tests. Fixed-period and moving-period statements remain distinct.

## Reading, provenance and verification scope

File 00 is the sole final reviewed owner continuation. File 15 is the current
419-page reader; file 14 is its complete editable LaTeX. Complete receivers
09/10 retain every accepted body and receiving site. Display reversal
recovers the accepted mathematical assembly; insertion reversal then recovers
the entire 338-page predecessor sources. Files 01-08, 13 and 16 are unchanged;
file 01 remains historical, not the current preview.

The owner records the exact final build, all 419 rendered pages, original
footer/page-bound checks and no unresolved visual finding. Root inspected
sheets 18-34 and individual long displays; the independent first-half review,
final contents-page review and inherited accepted body matches retain their
separate scopes. A 1.74977pt path-list warning was visually accepted without
clipping, equation collision or unreadable content. Complete source-only
checks and their diagnostics retain their stated scope; no
additional PDF is a visually accepted deliverable. The original RPK ZIP is
retained locally. Its complete public derivative changes only the named
nested predecessor locator metadata, with original/public member identities
recorded; all other member bodies remain exact. It is one of the two approved
container derivatives, not an unchanged opaque public archive. The loose
source, user handoff, 91-payload manifest and normal/optimized 59-check receipts
retain their provenance and stated scope. Finite checks do not certify an
actual transcendental period or replace analytic proofs. No new Lean execution
is claimed.

Logical file 11 remains the complete lossless provenance map, with 482
distinct byte objects and 734 original path/role aliases in the owner map.
Original object identities and provenance are retained by the recorded public
transport; the inherited map is stored once as exact compressed bytes.
The full CFR review is distinct from the narrower earlier RPK interface
review. Final NBR/WNR receipts retain their complete-source and receiving-site
scope. Inclusion of provenance does not enlarge accepted mathematical scope.
Two superseded historical byte objects remain unavailable at three old
reference edges, as disclosed in the source seal; the current accepted sources
and acceptance records are present. Those old gaps are not silently certified.
Later WEL/BVC, GKC/GVJ/GGE/PCJ, CNC/LCC and ITL/IRR/IF/FAB are excluded.

Publication reuses the owner's exact proof/source/visual acceptance. The
other 16 files, including both PDFs and all 11 complete TeX files, remain
byte-identical. Source-map public-locator transport and lossless compression
do not add a mathematical, source or PDF re-audit, or an RH claim.

## Reconstruct the complete source map

This edition has 17 logical source files, carried by
20 physical GitHub files. The other 16 logical files
are unchanged. The complete public file 11 exceeds the single-file transport
limit. Its gzip stream is supplied losslessly in 2 ordered
parts: [11_SOURCE_MAP.json.gz.part01](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260915-native-boundary-continuation/11_SOURCE_MAP.json.gz.part01) · [11_SOURCE_MAP.json.gz.part02](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260915-native-boundary-continuation/11_SOURCE_MAP.json.gz.part02).
The [reconstruction manifest](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260915-native-boundary-continuation/SOURCE_MAP_TRANSPORT.json) binds every part and the
complete stream; [restore_source_map.py](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260915-native-boundary-continuation/restore_source_map.py) joins and checks
them. Download all listed parts, manifest and decoder to one directory and
follow the manifest's instructions. The result is
the exact public 11_SOURCE_MAP.json, checked against its accepted byte count
and SHA-256; it is not a source-map excerpt. Neither raw file 11 nor an unsplit
gzip file is advertised as a physical GitHub leaf. With the other 16 accepted
files also present, run `python restore_source_map.py --folder RESTORED_17`
to create a separate folder containing exactly the 17 logical files and no
transport helpers. The publication guide remains outside the flat folder.

The existing [DOI 10.5281/zenodo.22760901](https://doi.org/10.5281/zenodo.22760901) remains the 68-download,
317-page edition until this source cut is separately published there. No
Zenodo, Overleaf or timer changes occur in this source transaction.

## Earlier source and edition guide (historical snapshot)

The following guide is preserved verbatim. Its reader and next-task statements
belong to its own edition. The 419-page reader above is current.

# Split-Zero cohomology: arithmetic row-energy allocation estimates

[Read the current 317-page paper](https://zenodo.org/api/records/22760901/files/67-allocation-reader.pdf/content) · [Published DOI 10.5281/zenodo.22760901](https://doi.org/10.5281/zenodo.22760901) · [Exact current continuation and next calculation](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/88cec321ccb455d1906d4abce7dc08bea6c7676d/workbenches/splitzero-tandem/continuations/20260915-allocation-continuation/00_CONTINUE_HERE.md).

- [317-page allocation](https://zenodo.org/api/records/22760901/files/67-allocation-reader.pdf/content) · [complete editable source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/88cec321ccb455d1906d4abce7dc08bea6c7676d/workbenches/splitzero-tandem/continuations/20260915-allocation-continuation) · [offline source ZIP](https://zenodo.org/api/records/22760901/files/68-allocation-sources.zip/content).

## What is being calculated, and why

Split-Zero studies arithmetic theta cohomology associated with a finite packet
of zeta-function zeros. The original period observation has a kernel K, the
classes it sends to zero, and an invariant residual V_A/K. The programme
measures those two contributions in the original Gamma and arithmetic metrics
and returns them to the same cohomological class and its quantitative action
form A*G+GA-kG. This is the concrete F1/Deligne mixed-cohomology direction under
investigation, not a conclusion obtained from a determinant representation alone.

The current question is how an already evaluated total determinant growth
divides between those two actual parts. The preceding 293-page paper constructed
their dual metrics, retaining the complete lower-evaluation space L and its
residual image W_0. The quotients K/(K intersect L) and (V_A/K)/W_0 keep their
induced metrics, and both low terms are returned afterward. This 317-page
edition preserves those proofs and adds six complete bodies with
113 tagged equations and their full receiving-source integrations.

The original degrees are q-1,q,2q-1,2q, where q=(k+1)^2 and k=4l+1.
The source orders remain 1 and k. All conductor coefficients, masses, factorials,
phases, lower evaluations, Schur denominators and mixed contributions remain.

The 317-page cumulative Split-Zero reader retains the original period observation, kernel K, invariant residual V_A/K and full lower-evaluation Gamma forms. A complete factorial-form comparison gives both half-line coefficient maps and consecutive kernel/residual Gram-volume ratios. Deterministic full-row pivot products estimate those actual volumes with unequal finite errors o(kq) on the proved fixed-period domain. Exact threshold pencils and finite enclosures concern the same two allocations. Their simultaneous affine coupling uses the evaluated total and returns both bounds through original low metrics, flag/transfer errors, arithmetic comparison and the entire signed/action budget.

## What was tried and what it establishes

- **Control the actual coupled rows (ACB).** The residual energy x_M and kernel
  energy y_M belong to the same preceding lower-evaluation minimum. Their
  increments are log(1+x_M) and log(1+y_M/(1+x_M)); together they give
  log(1+x_M+y_M). Component and joint-tail bounds retain that coupling.
- **Pass through the full factorial observation (GPA, LVM).** The original
  Gamma measure is compared with an explicit factorial moment matrix through
  every relation and quotient. A map W using both half-lines gives the complete
  Gram volumes D_U,D_K,D_E. The kernel and residual metrics use the consecutive
  ratios D_K/D_U and |det[Z_k,C]|^2 D_E/D_K. The fixed frame factor cancels
  only under the proved four-endpoint signs.
- **Estimate the complete volume with actual pivots (GVM).** Deterministic
  full-row pivot products P_A satisfy P_A<=D_A<=(2n_N)^(r_A)P_A.
  Every row from both half-lines and the full rank-one update are used.
  The two signed pivot-volume sums estimate the actual allocations with
  unequal errors of order O_actual(k log q+q log q)=o(kq). These are squared
  minors already; no extra factor 2 is inserted.
- **Give a second finite route to the same scalars (TSR).** Original quotient
  and restriction pencils give weighted threshold integrals and finite
  enclosures. Their operation count neither proves bit complexity nor certifies
  the original transcendental inputs.
- **Return both bounds together (SAR).** The exact total couples the two
  allocations affinely. The complete original low metrics, unequal flag and
  transfer errors, correlated arithmetic comparison and whole signed/action
  budget remain, including the receiving sites BRI6s, MRI4ac and OER28.

With endpoint weights 1 and interior weights 2, write

    S_K = sum_M w_M log(1+y_M/(1+x_M)),
    S_R = sum_M w_M log(1+x_M).

The total satisfies (S_K+S_R)/(kq) ->16 C_partial, with
21.66851180520 <16 C_partial<21.66851180521.
This evaluated total is not either individual coefficient.

## The next calculation

The sole owner prompt assigns the web lane the actual two-half-line factorial
mixed-volume/pivot estimate: write the original row recurrence after W,
including half-line coupling, and quantify how the relation and invariant
columns affect successive pivots. A leading value or strict interval at
kq scale for one allocation determines the other through the exact total.
A local companion lane pursues the bounded-degree invariant inverse and its
joint-compatible lower-evaluation correction; it is not an assumed estimate here.

GPA/LVM/GVM retain k>=29 and k sqrt(delta^2+gamma^2)<=2^(-33)q,
the fixed actual five-orbit period and its logarithm branch. Arithmetic
applications retain |u|>=R_*. Outside those domains the original formulas remain;
fixed-period estimates are not asserted uniform over moving periods.
The complete sources retain multiplicities and their own rank statements.

Six complete new proof bodies contain 113 tagged equations: ACB1-15, GPA1-23, LVM1-19, GVM1-10, TSR1-30 and SAR1-16. The next quantitative calculation is the actual two-half-line factorial mixed-volume/pivot allocation at kq scale; one coefficient and the exact total determine the other. The separate local invariant-inverse/gauge-correction lane is ongoing. Later KRC/BIM/FRE/MNT/IPE/NPB/DFX are outside this edition. Supplementary provenance is not blanket proof acceptance. The finite domains, fixed actual period, original orders 1,k and all errors remain. No moving-period uniformity, unproved inverse or programme completion is claimed.

## Complete proofs and verification scope

[File14, complete editable reader](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/88cec321ccb455d1906d4abce7dc08bea6c7676d/workbenches/splitzero-tandem/continuations/20260915-allocation-continuation/14_CURRENT_KERNEL_AND_MULTIPLICITY_PROOFS.tex)
and [file15, 317-page GitHub PDF](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/88cec321ccb455d1906d4abce7dc08bea6c7676d/workbenches/splitzero-tandem/continuations/20260915-allocation-continuation/15_CURRENT_MIXED_CONTROL_READER.pdf)
are the current paper. Files 09/10 are the complete receiving documents.
Files 02/03 and the other supplied sources retain the preceding mathematical
dependencies. [File00](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/88cec321ccb455d1906d4abce7dc08bea6c7676d/workbenches/splitzero-tandem/continuations/20260915-allocation-continuation/00_CONTINUE_HERE.md) remains the sole current
continuation prompt; this is a reading guide, not a competing instruction file.

[Validation file12](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/88cec321ccb455d1906d4abce7dc08bea6c7676d/workbenches/splitzero-tandem/continuations/20260915-allocation-continuation/12_VALIDATION.md) records independent proof
acceptance of the six complete bodies and actual receiving spans, exact
source reversals and the stable three-pass reader build. All 317 pages were
rendered, with every footer and off-page span checked. The owner visually
reviewed nine contact sheets covering fresh pages 2–10 and 294–317, including
the LVM8 display repair at page 302; inherited bodies match the accepted 293
reader. Auxiliary 427- and 414-page receiver PDFs are source-build checks,
not additional delivered visual acceptances. This edition reuses those
completed checks; no new proof review, PDF audit or Lean execution is claimed.

[Source map 11](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/88cec321ccb455d1906d4abce7dc08bea6c7676d/workbenches/splitzero-tandem/continuations/20260915-allocation-continuation/11_SOURCE_MAP.json) preserves complete sources,
reviews, diagnostics, previous versions and reversible changes. Broader
provenance does not grant blanket acceptance to historical drafts. Existing
formalization retains its revision-specific scope. Later KRC/BIM/FRE/MNT/IPE/NPB/DFX
work is outside this fixed edition. Preserved external FVR reports do not
certify unavailable full sources.

The original source-map SHA-256 is `6f7cc039f6e529f26a0113cc76a7d5a7578a3f14407eff1271512a63c03570c1`;
the public SHA-256 is `8ddfc8c6f3eba2147c7aeeb942ad495413c3917c1dda709eb6f71d670317de16`.
Only historical account locators are transported. The other sixteen files,
both PDFs and all eleven full TeX files remain exact accepted bytes.

## Earlier editions and downloads

- [Earlier 20260915 dual metric continuation source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/b4076eb15afd6b036a8de62d67b88eef03efeb50/workbenches/splitzero-tandem/continuations/20260915-dual-metric-continuation).
- [Earlier 20260915 operator control continuation source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/36b2654e1d3324c6de24e324ec34bb3a98f67103/workbenches/splitzero-tandem/continuations/20260915-operator-control-continuation).
- [Earlier 20260915 first variation continuation source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/af5c17948c24f43494ea76d823322e8b3924b58d/workbenches/splitzero-tandem/continuations/20260915-first-variation-continuation).
- [Earlier 20260915 quotient moment continuation source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/bf39bac055b76ce755b91401b35570bb84d76d9a/workbenches/splitzero-tandem/continuations/20260915-quotient-moment-continuation).
- [Earlier exterior kernel continuation source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/dad07e28faa735104ddc0b137521620fc315e6fc/workbenches/splitzero-tandem/continuations/20260914-exterior-kernel-continuation).
- [Earlier conductor kernel continuation source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/41adc412ceb119ad9086b1f106e377f3de2d401a/workbenches/splitzero-tandem/continuations/20260914-conductor-kernel-continuation).
- [Earlier original kernel matrices source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/5817ef9027257375b6ff3de7048b3331077251e7/workbenches/splitzero-tandem/continuations/20260914-original-kernel-matrices).
- [Earlier original volumes source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/1c8ec52c85c173adc9f8403a8a26914955e2f5a9/workbenches/splitzero-tandem/continuations/20260914-original-volumes).
- [Earlier gamma growth source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/41f020e0475429943252e69a1b4edd849393c780/workbenches/splitzero-tandem/continuations/20260914-gamma-growth).
- [Earlier joint gamma schur source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/2be3b23974bf040f4ea06240b8a4b85372f7c71d/workbenches/splitzero-tandem/continuations/20260914-joint-gamma-schur).
- [Earlier original relation bulk source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/01fc8820e3a3ea69afa22b8ab1b0b5ca61869456/workbenches/splitzero-tandem/continuations/20260914-original-relation-bulk).
- [Earlier complete gamma return source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/01fc8820e3a3ea69afa22b8ab1b0b5ca61869456/workbenches/splitzero-tandem/continuations/20260914-complete-gamma-return).

The [preceding 66-download edition](https://doi.org/10.5281/zenodo.22760598) retains
its 293-page preview unchanged. This edition adds PDF 67 and ZIP 68.
All 68 downloads remain separately clickable, with the current 317-page paper
as the preview. The source ZIP contains all seventeen flat files for offline
use. Every earlier mathematical source and publication record remains.

[All 68 downloads and source identities](calculation_edition_20260915_allocation/README.md).

## Earlier reading guide — preserved historical edition

The following text belongs to the preceding publication and retains its
historical scope. The 317-page guide above is the current route; no earlier
mathematical source is rewritten.

# Split-Zero cohomology: arithmetic row-energy allocation estimates

[Start here: exact current continuation](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260915-allocation-continuation/00_CONTINUE_HERE.md).

[Read the 317-page paper](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260915-allocation-continuation/15_CURRENT_MIXED_CONTROL_READER.pdf) · [Complete LaTeX proofs](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260915-allocation-continuation/14_CURRENT_KERNEL_AND_MULTIPLICITY_PROOFS.tex) · [Verification scope](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260915-allocation-continuation/12_VALIDATION.md).

Split-Zero studies the original theta cohomology of a selected zeta-zero
packet. Its specified period observation divides an arithmetic source into
the observation kernel and its invariant residual quotient. Their native
metrics give two coupled sums of Gamma row energies. This edition derives
finite bounds and exact matrix formulas for how the already evaluated total
is divided between those two parts. Tau remains the absolute base and the
proposed Deligne mixed-cohomology route remains active. No RH conclusion is
claimed.

The 317-page paper retains the complete 293-page predecessor and adds six
complete proof bodies with 113 tagged equations: ACB1-15, GPA1-23, LVM1-19,
GVM1-10, TSR1-30 and SAR1-16. These concern the same original kernel and
residual, not a replacement positive matrix or a freely chosen metric.

## The actual allocations and their exact total

Fix the actual simple quartet, five-orbit period, full amplitude unit and
logarithm branch. Retain k=4l+1, q=(k+1)^2, q'=(k-7)^2,
Delta=16k-48, v=ord_0 E_A and m=Delta-v. The original source orders are
s=1,k, with h_n=M_s n!(s/2)_n and M_s=(2pi)^(s/2). The actual intersection
t0=dim(K intersect L), every relation and residual column, factorial,
phase and both induced-metric denominators remain.

The four polynomial endpoints q-1,q,2q-1,2q have primal signs (+,+,-,-).
The native dual determinant return has the opposite orientation. For each
actual later row, x_M and y_M are its nonnegative residual and kernel
energies, calculated after the whole preceding lower-evaluation minimum.
The weighted sums are

    S_K = sum_M w_M log(1+y_M/(1+x_M)),
    S_R = sum_M w_M log(1+x_M),
    S_K+S_R = sum_M w_M log(1+x_M+y_M).

The two end rows have weight 1, the interior rows weight 2, and the total
weight is 2q. SAR gives the complete conjugate-inverse dictionary to the
original kernel and residual forms. The total is already evaluated:

    (S_K+S_R)/(kq) -> 16 C_partial,
    21.66851180520 < 16 C_partial < 21.66851180521.

This number does not assign either separate allocation. All low-volume
terms and unequal flag/CEP errors remain when returning to the original
kernel determinant F_K and residual determinant Phi.

## New finite estimates through full mixed volumes

ACB supplies component and joint-tail controls. GPA compares the full native
forms to an explicit factorial moment matrix through the same relation
columns. The two source centres Q_1=q' and Q_k=q'+(k-1)/4 remain distinct;
the signed allocation comparison has error O_actual(k log q).

LVM gives the exact two-half-line map W=[A P; R A P], retaining its roots,
phases and factorials. With the original full column matrices

    X_U=U_N,   X_K=[U_N,E_m Z_k],   X_E=[U_N,E_m],
    D_A=det((W X_A)* W X_A),

the kernel and residual volumes are consecutive ratios D_K/D_U and
|det[Z_k,C]|^2 D_E/D_K. The fixed frame scalar cancels only in the signed
four-endpoint return. Every mixed minor remains; the maximal-minor
comparison has an O(q) remainder.

GVM constructs deterministic full-row pivot products P_A without enumerating
all minors. At every step it uses the largest actual residual diagonal,
its fixed tie rule and the complete rank-one update across both half-lines:

    P_A <= D_A <= (2n_N)^(r_A) P_A.

The consecutive signed pivot-volume sums C_K,C_R approximate S_K,S_R with
the explicit unequal GPA/GVM errors, together of order
O_actual(k log q+q log q)=o(kq). The pivot products already use squared
minors; there is no extra factor 2. Their sum cancels the same intermediate
pivot volume. These are calculated finite reductions; the separate
large-k coefficients of the actual pivot products remain to be evaluated.

TSR independently represents the same finite scalars by exact threshold
spectral flows and supplies finite enclosures. Strict eigenvalue thresholds,
multiplicities and the original metrics remain. An operation count is not
a bit-complexity theorem or certification of transcendental input values.
Artificial finite examples test identities, not the actual-period limit.

## Return to the complete arithmetic quantity

SAR couples every improvement in either allocation to the other through
their evaluated total. It carries finite intervals through the original
low metrics, unequal flag/CEP errors, finite OAR/PMR domains, correlated
arithmetic source comparison, signed mixed return and whole-action budget.
The earlier receiving sites BRI6s, MRI4ac and OER28 contain these intervals.
The kernel determinant is not substituted for the complete exterior
allowance. Both contraction penalties, all mixed pairings, leakage and the
same nonzero arithmetic class remain.

The GPA/LVM/GVM finite estimates use k>=29 and
k sqrt(delta^2+gamma^2)<=2^(-33)q. Outside that domain the original OAR
formulas remain available. Arithmetic statements retain |u|>=R_* and the
original fixed actual period. No uniform moving-period assertion or
extension of simple-quartet ranks to higher multiplicity is made.

## Next calculation on these matrices

Estimate the actual separate C_K,C_R from the original relation and
invariant recursions after W is applied, including the term coupling both
half-lines. Retain every period/conductor coefficient, factorial weight,
mixed column and quotient denominator. An evaluated leading term or strict
kq-scale interval for one allocation would constrain the other through the
exact total. The completed reconstruction, matrix transports and finite
bounds above are inputs to this calculation, not tasks to redo.

## Reading and verification scope

File 00 is the single exact owner continuation. File 15 is the current
317-page paper; file 14 is its complete editable LaTeX. All six new proof
bodies appear once in 14 and once in each complete receiving source 09/10.
Their recorded reversal recovers every byte of the 293-page predecessor.
Files 01-08,13,16 are unchanged; file 01 remains a historical reader.

The owner records a source-stable three-pass XeLaTeX build, all 317 rendered
pages and checked footers, and no off-page text or remaining reader issues.
The fresh-page visual scope and unchanged-body comparisons are recorded.
The two receiver builds are source checks: their auxiliary PDFs are not
additional delivered visually accepted artifacts. File 16 retains the prior
revision-specific formal source evidence; no new Lean execution or analytic
kernel certification is claimed here.

File 11 is the full large provenance source map, not an excerpt. It retains
complete prior sources, reviews, diagnostics, reversible changes and the
external handoffs. The complete local OFV/ECL/EQR/RWC proofs keep their own
provenance; summaries of external FVR work do not certify missing sources.
Later KRC/BIM/FRE/MNT/IPE/NPB are excluded from this edition. Provenance
inclusion alone is not acceptance beyond the explicit six-provider scope.

Publication reuses the owner's full proof/source/visual acceptance. Only
private account locators in the source map are transported; the other 16
complete files, both PDFs and all 11 TeX files stay byte-identical. This
publication step adds no mathematical or PDF re-audit and no RH claim.

The existing [DOI 10.5281/zenodo.22760598](https://doi.org/10.5281/zenodo.22760598) remains the 66-download, 293-page edition until this source cut is separately published there. No Zenodo/Overleaf/timer changes occur in this source transaction.

## Earlier source and edition guide (historical snapshot)

The following guide is preserved verbatim. Its current-reader and next-task statements belong to its own edition. The 317-page reader above is current.

# Split-Zero cohomology: dual reconstruction and kernel-residual row energies

[Read the current 293-page paper](https://zenodo.org/api/records/22760598/files/65-dual-metric-reader.pdf/content) · [Published DOI 10.5281/zenodo.22760598](https://doi.org/10.5281/zenodo.22760598) · [Exact current continuation and next calculation](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/b4076eb15afd6b036a8de62d67b88eef03efeb50/workbenches/splitzero-tandem/continuations/20260915-dual-metric-continuation/00_CONTINUE_HERE.md).

- [293-page dual metric](https://zenodo.org/api/records/22760598/files/65-dual-metric-reader.pdf/content) · [complete editable source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/b4076eb15afd6b036a8de62d67b88eef03efeb50/workbenches/splitzero-tandem/continuations/20260915-dual-metric-continuation) · [offline source ZIP](https://zenodo.org/api/records/22760598/files/66-dual-metric-sources.zip/content).

## What this programme is trying to calculate

Split-Zero studies the arithmetic theta cohomology attached to a finite packet
of zeta-function zeros. Its original period observation has a kernel K: classes
that the specified observation sends to zero. The residual is the quotient
V_A/K. The research measures these two contributions in the original Gamma
and arithmetic metrics, then carries them back to the same cohomological class
and its quantitative action/control form A*G+GA-kG. This is the concrete
F1/Deligne mixed-cohomology direction being investigated; a determinant identity
alone is not an endpoint conclusion.

The four source degrees are q-1, q, 2q-1 and 2q, with q=(k+1)^2. The new
calculation retains the same conductor, period, complete source unit, masses,
factorials and lower evaluations. It uses both original source orders s=1,k.
The kernel belongs to that fixed original period observation, not an intersection
over unrelated periods. The low space L and its image W_0 in the residual
remain explicit: the newer dual calculation uses K/(K intersect L) and
(V_A/K)/W_0 with their actual induced metrics, then returns both low terms.

The preceding 238-page reader established the operator/control and full-window
formulas. This edition preserves those proofs and adds twelve complete bodies
with 241 tagged equations. Its advance is the exact dual reconstruction and
the compatible later rows, not a new choice of metric or a numerical model.

The 293-page Split-Zero reader constructs the original Gamma dual metric, its native kernel quotient and complementary residual restriction. Complete low-jet reconstruction and recurrence-compatible high jets retain all lower evaluations, conductor coefficients, masses and induced metrics. Two actual row energies determine the residual increment log(1+x_M) and kernel increment log(1+y_M/(1+x_M)). Their full common low-window term cancels under the original four signs. The total weighted row sum is evaluated and returned through the original arithmetic maps, with both low terms, exceptional periods and finite unequal errors retained.

## What was tried, what worked, and what remains

- **Keep the entire original relation and dual metric (RCF, RCM, DNE).**
  The conductor and lower evaluation columns enter the full least-norm
  extension. The kernel quotient and residual restriction retain their own
  induced metrics and the complete complex-linear dual maps.
- **Control the actual symbol poles and period exceptions (PEC, ACR, LBRE,
  ASR).** The positive exterior contribution is subleading at the stated fixed
  periods. Exact coefficient maps retain the low intersection and exceptional
  support cases; the exception set is not asserted empty.
- **Reconstruct the low jets and carry the result back (LJR, LRR, PBR).**
  The numerator constraints, Vandermonde map and Gamma basis give an explicit
  quotient Jacobian. Its full q log k contribution and fixed remainder are
  retained. The original low-space isometry returns the finite estimate to
  the kernel and residual with both low terms and unequal errors.
- **Extend using the actual recurrence (HJR, HCR).** Later jets obey the
  original polynomial recurrence and share one lower-evaluation coefficient
  vector. Both Schur denominators remain. The residual row energy x_M gives
  the increment log(1+x_M); the kernel energy y_M gives
  log(1+y_M/(1+x_M)). Their sum is log(1+x_M+y_M).
- **Cancel only through the proved four-sign identity.** The complete common
  low-window contribution cancels, including its fixed remainder. The combined
  weighted row sum is evaluated: its leading coefficient is the previously
  calculated 16 C_partial, between 21.66851180520 and 21.66851180521.
  This total does not assign either individual contribution.

The next calculation is the separate actual row-energy allocation between
kernel and residual. It must estimate x_M and y_M with their coupled denominator
1+x_M, then return through the original arithmetic action budget. Reconstructing
the compatible graph again would repeat completed work. Neither ranks nor the
known total provide the missing individual coefficient.

The simple-quartet lane retains k=4l+1 at least 9, 0&lt;delta&lt;1/2,
gamma&gt;2, the actual fixed five-orbit period and its logarithm branch.
Individual estimates retain their own stronger finite domains; fixed-period
estimates are not claimed uniformly over moving periods. The full multiplicity
algebra and original arithmetic domain remain in the complete sources.

The individual quantitative allocation between the original kernel and residual is still to be estimated. Neither rank nor the evaluated total assigns either individual leading coefficient. The twelve accepted new providers include the complete RCF/RCM/DNE/PEC and LJR/HJR/HCR bodies. Supplementary provenance does not enlarge their acceptance scope; external FVR full sources remain absent. SIC/NG and active allocation work are outside this sealed cut. No programme completion is claimed.

## Complete proofs and the scope of verification

The [complete reader LaTeX, file14](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/b4076eb15afd6b036a8de62d67b88eef03efeb50/workbenches/splitzero-tandem/continuations/20260915-dual-metric-continuation/14_CURRENT_KERNEL_AND_MULTIPLICITY_PROOFS.tex)
and [293-page GitHub PDF, file15](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/b4076eb15afd6b036a8de62d67b88eef03efeb50/workbenches/splitzero-tandem/continuations/20260915-dual-metric-continuation/15_CURRENT_MIXED_CONTROL_READER.pdf)
are the current paper. Files09/10 contain both full updated receiving documents.
Files02/03 and the other source files preserve the complete preceding proof
dependencies. [File00](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/b4076eb15afd6b036a8de62d67b88eef03efeb50/workbenches/splitzero-tandem/continuations/20260915-dual-metric-continuation/00_CONTINUE_HERE.md) is the sole current
continuation prompt; this page is a reading guide, not a replacement prompt.

[Validation file12](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/b4076eb15afd6b036a8de62d67b88eef03efeb50/workbenches/splitzero-tandem/continuations/20260915-dual-metric-continuation/12_VALIDATION.md) records the owner’s completed
three-pass build, rendering of all 293 pages, every-footer check and absence
of off-page text or reader diagnostics. Its exact visual receipt distinguishes
inherited matching bodies from the fresh pages reviewed. The separate 401- and
389-page receiver PDFs are compilation checks, not additional visually accepted
deliverables. This publication reuses those completed checks; it does not claim
a new proof review, PDF audit or Lean execution.

[Source map file11](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/b4076eb15afd6b036a8de62d67b88eef03efeb50/workbenches/splitzero-tandem/continuations/20260915-dual-metric-continuation/11_SOURCE_MAP.json) preserves all complete new
proofs, reviews, diagnostics, original sources and reversible transports.
Broad supplementary closure is provenance only, not acceptance of every
embedded draft. RCF/RCM/DNE now have the complete accepted bodies in this
edition; their older draft status belongs to the preserved preceding edition.
External FVR full TeX/PDF was absent, so its preserved summaries do not certify
those unseen files. Existing formalization keeps its exact revision-specific
scope. The separate SIC/NG note and active allocation work are not included.

The original source-map SHA-256 is `4ba6d00f4db523aa02643adbcd2a11ecf427246d2f6a6d7938b1ab7c4de544bf`;
the public SHA-256 is `49bc564a151a4bd3904d4c1940ec073e7d58834e8ae7cc68efbe51c0e6befa0e`. Only historical account
locators were transported. The other sixteen files, including both PDFs and
all eleven full LaTeX files, retain the exact accepted bytes.

## Earlier editions and downloads

- [Earlier 20260915 operator control continuation source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/36b2654e1d3324c6de24e324ec34bb3a98f67103/workbenches/splitzero-tandem/continuations/20260915-operator-control-continuation).
- [Earlier 20260915 first variation continuation source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/af5c17948c24f43494ea76d823322e8b3924b58d/workbenches/splitzero-tandem/continuations/20260915-first-variation-continuation).
- [Earlier 20260915 quotient moment continuation source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/bf39bac055b76ce755b91401b35570bb84d76d9a/workbenches/splitzero-tandem/continuations/20260915-quotient-moment-continuation).
- [Earlier exterior kernel continuation source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/dad07e28faa735104ddc0b137521620fc315e6fc/workbenches/splitzero-tandem/continuations/20260914-exterior-kernel-continuation).
- [Earlier conductor kernel continuation source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/41adc412ceb119ad9086b1f106e377f3de2d401a/workbenches/splitzero-tandem/continuations/20260914-conductor-kernel-continuation).
- [Earlier original kernel matrices source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/5817ef9027257375b6ff3de7048b3331077251e7/workbenches/splitzero-tandem/continuations/20260914-original-kernel-matrices).
- [Earlier original volumes source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/1c8ec52c85c173adc9f8403a8a26914955e2f5a9/workbenches/splitzero-tandem/continuations/20260914-original-volumes).
- [Earlier gamma growth source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/41f020e0475429943252e69a1b4edd849393c780/workbenches/splitzero-tandem/continuations/20260914-gamma-growth).
- [Earlier joint gamma schur source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/2be3b23974bf040f4ea06240b8a4b85372f7c71d/workbenches/splitzero-tandem/continuations/20260914-joint-gamma-schur).
- [Earlier original relation bulk source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/01fc8820e3a3ea69afa22b8ab1b0b5ca61869456/workbenches/splitzero-tandem/continuations/20260914-original-relation-bulk).
- [Earlier complete gamma return source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/01fc8820e3a3ea69afa22b8ab1b0b5ca61869456/workbenches/splitzero-tandem/continuations/20260914-complete-gamma-return).

The [preceding 64-download edition](https://doi.org/10.5281/zenodo.22760013) remains
unchanged with its 238-page preview. This edition adds PDF65 and ZIP66.
All 66 downloads remain separately clickable; the current 293-page paper is
the preview. Its source ZIP contains all seventeen flat files for offline use.
Earlier mathematical sources and publication records are preserved.

[All 66 downloads and source identities](calculation_edition_20260915_dual_metric/README.md).

## Earlier reading guide — preserved historical edition

The following text belongs to the preceding publication. Its current-reader
and next-calculation statements retain that historical scope. The 293-page
guide above is the current route; no earlier mathematical source is rewritten.

# Split-Zero cohomology: dual reconstruction and kernel-residual row energies

[Start here: exact current continuation](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260915-dual-metric-continuation/00_CONTINUE_HERE.md).

[Read the 293-page paper](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260915-dual-metric-continuation/15_CURRENT_MIXED_CONTROL_READER.pdf) · [Complete LaTeX proofs](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260915-dual-metric-continuation/14_CURRENT_KERNEL_AND_MULTIPLICITY_PROOFS.tex) · [Verification scope](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260915-dual-metric-continuation/12_VALIDATION.md).

Split-Zero studies the original theta cohomology of a selected zeta-zero
packet. A specified period observation divides the original arithmetic
source into its kernel and residual quotient. This edition calculates their
native dual metrics and how the same Gamma rows contribute to each part.
The Deligne mixed-cohomology programme is the research direction; tau remains
the absolute base. No RH conclusion or programme completion is claimed.

The 293-page reader retains the complete 238-page predecessor and 12 complete
new proof bodies with 241 tagged equations: RCF/RCM/DNE/PEC/ACR/LBRE/ASR,
PBR/LJR/LRR/HJR/HCR. The low reconstruction, compatible later jets and exact
four-endpoint cancellation are proved. Their separate quantitative kernel
and residual row-energy allocation is the remaining calculation.

## Original objects and domains

In the simple-quartet lane retain m=1, 0<delta<1/2, gamma>2, the full fixed
amplitude unit and the specified fixed five-orbit period, with |u|>=R_*.
Here k=4l+1>=9, q=(k+1)^2, Delta=16k-48, kernel rank r=8k-16 and residual
rank j=8k-32. The original Gamma source orders are s=1,k. The four source
degrees q-1,q,2q-1,2q carry signs (+,+,-,-). Every source mass, primary
point, factorial, phase, orientation and induced metric is retained.

Imported results keep their own finite domains: PMR uses k>=29 and
k sqrt(delta^2+gamma^2)<=2^(-33)q, with OAR's outer-root fallback otherwise;
OFV keeps its additional k>=257 requirement. Fixed-period conclusions are
not assertions uniform over arbitrary moving periods. The complete
all-multiplicity algebra is retained without assigning these m=1 ranks to it.

## What the dual construction now proves

The conductor uses all 81 actual period-dependent coefficients. Its symbol
E_A(z)=sum a_ab exp(b_ab z) retains
b_ab=4+(2a-8)delta+i(2b-8)gamma. If v is its first nonzero moment order,
then v<=80, alpha_A=v!/E_A^(v)(0), and the dual quotient has dimension
m_dual=Delta-v. DNE constructs its original metric

    D_N = T_N* [I-V_N(V_N*V_N)^(-1)V_N*] T_N.

The fixed reference G_exp is induced by the original coefficient form;
it is not chosen to improve an estimate. The complete coordinate pairings,
complex transposes and Hermitian adjoints connect this dual metric to the
native relation quotient. PEC bounds its positive logarithmic spectrum by
an explicit epsilon^vee_(N,s)=o(kq). Its pole-jet removal keeps the fixed
disk, exact codimension and constants before the stated limiting sequence.

Let L be the polynomials of degree below v, t0=dim(K intersect L), and
W0=Xi(L). The kernel and residual comparisons use the original maps B_K,J0:

    D_K,N = (B_K D_N^(-1) B_K*)^(-1),
    G_K   = (B_K G_exp^(-1) B_K*)^(-1),
    D_0,N = J0* D_N J0,       G_0 = J0* G_exp J0.

Their ranks are r-t0 and j-v+t0. Their negative logarithmic spectral sums
give nonnegative four-endpoint deficits A_K,A_0. The completed return is

    F_K^(s) = A_K + o(kq),     Phi_(k,s) = A_0 + o(kq),
    (A_K+A_0)/(kq) -> 16 C_partial,
    21.66851180520 < 16 C_partial < 21.66851180521.

The actual finite unequal error endpoints remain, rather than being replaced
by asymptotic notation in receivers. PBR retains both low contributions
through the exact induced-metric map (K+L)/K -> W0.

ACR calculates the common divisor and exceptional ranks from the actual
coefficient matrices. LBRE/ASR proves full support width(8,8) outside a
finite explicitly defined set of actual periods, with a sufficient radius.
That exception set is not declared empty. The support theorem does not
assign t0 or either individual residual rate.

## Completed reconstruction and full later-row allocation

LJR reconstructs the low endpoint using the full Vandermonde/product-jet map
V_beta^(-1) J_E B^T in the original Gamma basis, including
h_n=M_s n!(s/2)_n and every native quotient factor. Its squared singular
values are reciprocals of the relative dual eigenvalues. The full Jacobian
has log J=2 m_dual q log k+R_(k,s), with R_(k,s)=O_actual(kq).
The low reconstruction and that order estimate are completed results.

HJR extends the same lower-evaluation vector through the literal original
polynomial recurrence. Its full graph [I;H_N,s] produces

    D_cal,N = D_low + C_N* C_N,
    C_N = (I+Q_N Q_N*)^(-1/2) P_N.

The lower-evaluation conditioning factor is retained; taking the kernel
quotient retains the second Schur denominator as well. Later jets are not
replaced by unconstrained independent rows.

For each actual residual row h_M, the unchanged maps B=B_K and J=J0 give

    D_B,M=(B D_cal,M^(-1) B*)^(-1),   D_J,M=J* D_cal,M J,
    L_M=D_cal,M^(-1) B* D_B,M,
    x_M=h_M J D_J,M^(-1) J* h_M*,
    y_M=h_M L_M D_B,M^(-1) L_M* h_M*.

These nonnegative energies allocate the exact increment:

    g_R,M=log(1+x_M),
    g_K,M=log(1+y_M/(1+x_M)),
    g_M=g_R,M+g_K,M=log(1+x_M+y_M).

Sum M=q-1,...,2q-1 with endpoint weights 1 and interior weights 2 to obtain
S_R,S_K. Their total is already calculated:

    S_K+S_R = Delta q C_partial + o(kq).

The complete common low remainder and q log k term cancel in the exact
four-sign identity. The positive spectral terms remain in A_K=S_K-P_K
and A_0=S_R-P_0. Each compatible positive Gram increment, including actual
paired subquotients, is bounded by the full positive return without an
extra rank multiplier. All finite HJR24-27 endpoints are supplied.

HCR carries the two sums back to the original kernel and residual:

    F_K^(s)=S_K-E_s^flag+F_L^(s)-F_W0^(s),
    Phi_(k,s)=F_W0^(s)+S_R+delta_0,k,s.

Both low terms, unequal finite errors, correlated arithmetic deficits and
the same-class action budget remain. Total reflection phase vanishes while
the full mixed contribution 2|z_K|^2 is retained.

## What remains to calculate

Estimate the separate actual S_K,S_R, or a finite one-sided bound strong
enough for the existing arithmetic action inequality. Use the original
period/conductor coefficients, the compatible recurrence and actual x_M,y_M,
including their coupled denominator 1+x_M and both native reference metrics.
Their sum does not determine their individual allocation. The completed
reconstruction and full-window identities are inputs, not tasks to redo.
Exceptional periods and each original fixed-period domain remain explicit.

## Reading and verification scope

File 00 is the single exact owner continuation; file 14 is the complete
editable reader; files 09/10 are the complete receiving sources. Each new
proof body occurs once in each of those three sources. Their recorded
reversals recover the complete immutable 238-page edition. Files 01-08,13,16
retain preceding bytes; file 01 is historical, not the current paper.

The owner records three reader build passes and all 293 rendered pages,
all footer checks and no off-page text or reader diagnostics. The full
comparison distinguishes inherited matching bodies from freshly inspected
pages. Receiver 401/389-page builds are compile-only: their separate PDFs
are not delivered visually accepted artifacts. File 16 retains PR32-35's
formal sources and their revision-specific verification, not a new Lean run
or certification of these analytic estimates.

File 11 is the complete large provenance source map, not an excerpt. It
retains proof texts, reviews, diagnostics, scripts, logs, reversible source
transports and incoming handoffs. Its broad supplementary closure is
provenance only; acceptance is restricted to the listed complete providers
and precise receipts. Active allocation/energy drafts are excluded. Missing
external FIRST_VARIATION TeX/PDF is not certified by preserved summaries;
the supplied complete local proofs retain their own established scope.

Publication reuses the owner's complete source/proof/visual acceptance.
Only private account locators in the source map are transported; the other
16 complete sources, both PDFs and all 11 TeX files remain byte-identical.
No new source/PDF/mathematical audit, Lean execution or RH result is claimed.

The existing [DOI 10.5281/zenodo.22760013](https://doi.org/10.5281/zenodo.22760013) remains the 64-download, 238-page edition until this new source cut is separately published there. No Zenodo/Overleaf/timer changes occur in this source transaction.

## Earlier source and edition guide (historical snapshot)

The following guide is preserved verbatim. Its current-reader and next-task statements belong to its own edition. The 293-page reader above is current.

# Split-Zero cohomology: original operator, control budget and residual windows

[Read the current 238-page paper](https://zenodo.org/api/records/22760013/files/63-operator-control-reader.pdf/content) · [Published DOI 10.5281/zenodo.22760013](https://doi.org/10.5281/zenodo.22760013) · [Complete current continuation and next calculation](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36b2654e1d3324c6de24e324ec34bb3a98f67103/workbenches/splitzero-tandem/continuations/20260915-operator-control-continuation/00_CONTINUE_HERE.md).

- [238-page operator control](https://zenodo.org/api/records/22760013/files/63-operator-control-reader.pdf/content) · [complete editable source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/36b2654e1d3324c6de24e324ec34bb3a98f67103/workbenches/splitzero-tandem/continuations/20260915-operator-control-continuation) · [offline source ZIP](https://zenodo.org/api/records/22760013/files/64-operator-control-sources.zip/content).

## What this programme is trying to calculate

Split-Zero studies the arithmetic theta cohomology attached to a finite packet
of zeros of the zeta function, with every zero multiplicity retained. A specified
period observation sends some classes to zero. Its common kernel and boundary
complement are measured in the original Gamma and arithmetic metrics at the
four polynomial degrees q-1, q, 2q-1 and 2q. The kernel belongs to that original
period observation; it is not an intersection over different periods.

The research asks how these measured contributions return to the original
cohomological class and its quantitative control form A*G+GA-kG. This is the
concrete connection being pursued within the F1/Deligne mixed-cohomology
programme. It is not an assertion that a determinant identity alone settles RH.

The preceding 161-page edition evaluated the combined kernel-plus-residual
outer term. This edition keeps that entire paper and adds 15 full proof bodies
and 324 tagged equations, calculating the operator directions, residual graph,
same-class control budget and finite residual-window improvements below.

The 238-page Split-Zero reader calculates the original outer quotient in every relative-operator direction, the full residual relation graph in its native Schur metric, and the action/control budget for the same arithmetic class. It evaluates the outer coefficient, retains the nonzero original return radius and component phase terms, and proves full-rank consecutive residual windows with complete covariance and exterior expansions. All original domains, source orders, masses, phases, multiplicities and finite errors remain.

## What was tried, what worked, and what remains

- **Control every direction of the outer quotient (OOQ).** The scalar volume
  estimate was strengthened to an estimate for each relative-operator
  direction. The stated finite domain and errors are retained when this is
  restricted or returned through the original maps.
- **Use the actual residual relations (GIP, FEX, FGC, PCL, ROG, RDS).** The
  full relation graph, factorial-scaled fixed columns, pivot maps and weighted
  dual-symbol maps are explicit. Their native Schur metric retains the
  off-diagonal blocks, complete relation denominator and both low-volume
  corrections. Coefficient conditioning is not substituted for the Gamma metric.
- **Return the calculation to the same arithmetic class (MCE, MCP, RFX, OMR).**
  The original action/control budget now includes the boundary return,
  monic-norm window, contraction penalties and action leakage. Reflection
  cancels the total untilted phase, but the component pairings can be nonzero
  and opposite. Their positive mixed contribution is still present.
- **Evaluate the original outer coefficient (ECL).** The moving-endpoint
  formula and integer outward certificate give
  21.66851180520 &lt; 16 C_partial &lt; 21.66851180521. The coefficient belongs
  to the original outer calculation, not to an independently chosen model.
- **Improve the original return and residual bounds (EQR, RWC, OER).** EQR
  evaluates the original QGQ4 centre while retaining its nonzero error radius.
  RWC proves full rank for actual consecutive q-column windows and gives the
  complete conditioned covariance update and every exterior coefficient.
  OER returns the stronger finite bounds with their unequal errors. These
  strict finite improvements do not yet determine the residual kq-scale rate.

The active calculation in this edition is the actual conditioned residual
Phi/(kq), with the complete covariance and exterior coefficients retained,
and its contribution to the unchanged action budget. The original simple
quartet has m=1, k=4l+1 with l at least 1, q=(k+1)^2, c=k/2,
0&lt;delta&lt;1/2 and gamma&gt;2. Every original period branch |u| at least R_*
and the full unit 2xi/h remain. The source orders are 1 and k, with their
actual masses, phases, multiplicities and cross terms.

The results keep their individual domains: conductor k at least 9; OSP uses
epsilon=2^(-32), k at least 29 and k sqrt(delta^2+gamma^2) at most epsilon q/2;
OFV additionally requires k at least 257. Fixed-period estimates are not
asserted uniformly over arbitrary moving periods.

The actual residual rate Phi/(kq) and the remaining same-class quantitative control are active calculations in this edition. Strict finite improvements and the evaluated outer coefficient are not an RH exclusion. RCF/RCM/DNE drafts in the provenance map are explicitly unreviewed; absent external FVR full sources are not certified. Later PEC and other owner successors remain outside this immutable cut. No programme completion is claimed.

## Complete sources and the scope of verification

The [complete reader LaTeX, file 14](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36b2654e1d3324c6de24e324ec34bb3a98f67103/workbenches/splitzero-tandem/continuations/20260915-operator-control-continuation/14_CURRENT_KERNEL_AND_MULTIPLICITY_PROOFS.tex)
and [238-page GitHub PDF, file 15](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36b2654e1d3324c6de24e324ec34bb3a98f67103/workbenches/splitzero-tandem/continuations/20260915-operator-control-continuation/15_CURRENT_MIXED_CONTROL_READER.pdf)
are the current paper. Files 02, 09 and 10 retain the complete original,
joint and signed receiving notes. All four changed full sources can be
reversed to the complete predecessor. File 00 is the sole current research
continuation; this page is a reading guide, not a competing prompt.

[Validation file 12](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36b2654e1d3324c6de24e324ec34bb3a98f67103/workbenches/splitzero-tandem/continuations/20260915-operator-control-continuation/12_VALIDATION.md) records three clean XeLaTeX
passes, rendering of all 238 pages, 156 inherited RGB body matches, 21 contact
sheets for fresh pages, individual inspection of corrected page 170, and
checks of all footers. The other 237 final page images remained unchanged.
The 346/336-page receiver builds are compilation-only, not visually accepted
PDF deliverables. FEX records 587 finite checks per mode and 8 intended
rejection controls, with 69 imported payloads unchanged. These finite fixtures
are not actual xi periods or an infinite-family numerical certificate.
The ECL integer certificate has its stated normal/optimized replay records.
No new local Lean run or mathematical audit is claimed by this publication.

[Source map file 11](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36b2654e1d3324c6de24e324ec34bb3a98f67103/workbenches/splitzero-tandem/continuations/20260915-operator-control-continuation/11_SOURCE_MAP.json) includes complete accepted
proof/review material and separate RCF/RCM/DNE drafts explicitly marked
unreviewed. Those drafts are not accepted estimates. The external FVR full
TeX/PDF was absent; preserved summaries do not certify the unseen files.
Existing formalization and PR records retain their exact revision-specific
scope. Later owner calculations are not silently inserted into this edition.

The map's original SHA-256 is `6ff6bd07a3d35dda85992865542b5e28655f2cc670263333855e4a31c7e7c92d`; its public
SHA-256 is `417ed73665b0ada8288d413c0f77e93c78c84745d09581514a4caff580ab36d8`. Only private account locators
were transported for public distribution. The other sixteen files, including
both PDFs and all eleven LaTeX files, retain the exact accepted bytes.

## Earlier editions and downloads

- [Earlier 20260915 first variation continuation source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/af5c17948c24f43494ea76d823322e8b3924b58d/workbenches/splitzero-tandem/continuations/20260915-first-variation-continuation).
- [Earlier 20260915 quotient moment continuation source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/bf39bac055b76ce755b91401b35570bb84d76d9a/workbenches/splitzero-tandem/continuations/20260915-quotient-moment-continuation).
- [Earlier exterior kernel continuation source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/dad07e28faa735104ddc0b137521620fc315e6fc/workbenches/splitzero-tandem/continuations/20260914-exterior-kernel-continuation).
- [Earlier conductor kernel continuation source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/41adc412ceb119ad9086b1f106e377f3de2d401a/workbenches/splitzero-tandem/continuations/20260914-conductor-kernel-continuation).
- [Earlier original kernel matrices source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/5817ef9027257375b6ff3de7048b3331077251e7/workbenches/splitzero-tandem/continuations/20260914-original-kernel-matrices).
- [Earlier original volumes source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/1c8ec52c85c173adc9f8403a8a26914955e2f5a9/workbenches/splitzero-tandem/continuations/20260914-original-volumes).
- [Earlier gamma growth source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/41f020e0475429943252e69a1b4edd849393c780/workbenches/splitzero-tandem/continuations/20260914-gamma-growth).
- [Earlier joint gamma schur source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/2be3b23974bf040f4ea06240b8a4b85372f7c71d/workbenches/splitzero-tandem/continuations/20260914-joint-gamma-schur).
- [Earlier original relation bulk source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/01fc8820e3a3ea69afa22b8ab1b0b5ca61869456/workbenches/splitzero-tandem/continuations/20260914-original-relation-bulk).
- [Earlier complete gamma return source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/01fc8820e3a3ea69afa22b8ab1b0b5ca61869456/workbenches/splitzero-tandem/continuations/20260914-complete-gamma-return).

The [preceding 62-download edition](https://doi.org/10.5281/zenodo.22759785) remains
unchanged with its 161-page preview. This edition adds PDF 63 and ZIP 64.
All 64 downloads remain separately clickable. The current 238-page paper
is the Zenodo preview; its ZIP contains all seventeen flat source files for
offline use. Earlier mathematical sources and publication records are preserved.

[All 64 downloads and source identities](calculation_edition_20260915_operator_control/README.md).

## Earlier reading guide — preserved historical edition

The following text is preserved from the previous publication. Its current
reader and next-calculation statements belong to that earlier edition. The
238-page guide above is the current route; historical source, proof and
integration records retain their original scope.

# Split-Zero cohomology: original operator, control budget and residual windows

[Start here: current continuation](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260915-operator-control-continuation/00_CONTINUE_HERE.md).

[Read the238-page paper](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260915-operator-control-continuation/15_CURRENT_MIXED_CONTROL_READER.pdf) · [Complete LaTeX proofs](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260915-operator-control-continuation/14_CURRENT_KERNEL_AND_MULTIPLICITY_PROOFS.tex) · [Verification scope](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260915-operator-control-continuation/12_VALIDATION.md).

Split-Zero studies the original arithmetic theta cohomology attached to a
selected zeta-zero packet. A specified period observation loses a common
kernel K. The calculation measures that kernel and its boundary complement
in their original Gamma and arithmetic metrics at degrees q-1,q,2q-1,2q,
then carries the result through the existing cohomological signed return.

The research direction is the Deligne mixed-cohomology programme. The
simple-quartet lane retains m=1, k=4l+1 (l>=1), q=(k+1)^2, c=k/2,
0<delta<1/2, gamma>2, the full unit2xi/h, original period branches|u|>=R_*,
and the unchanged source orders s=1,k. R_* comes from that actual unit.
All-multiplicity algebra is retained without assigning these ranks to it.

## What this edition adds

The238-page reader retains the complete161-page predecessor and fifteen new
proof bodies: OOQ/GIP/MCE/MCP/RFX/OMR/PCL/ROG/RDS/FEX/FGC/ECL/EQR/RWC/OER.
Its324 new tagged equations are installed in the full reader and receivers.

OOQ controls every relative-operator direction of the same outer quotient,
not just its determinant average. Its eigenvalues satisfy
|log(lambda)-q C_partial/2|<=2 epsilon_k with
epsilon_k=O_(delta,gamma)(q^(3/4)+k log q)=o(q), on OOQ13's stated
eventual domain. A fixed rank-t restriction or quotient of that same target
has four-endpoint return t q C_partial with error<=4t epsilon_k.

GIP retains the entire original residual graph and relation denominator.
FEX/FGC gives the actual factorial-scaled columns and native mixed Schur
metric, including both low-volume corrections in
F_K=F_((K+L)/L)+F_L-F_((K+L)/K).
PCL/ROG gives actual coefficient/pivot maps and a controlled determinant-one
graph shear; RDS gives the exact weighted dual-symbol realization. These
maps do not replace the Gamma metric by a coefficient norm or drop a
finite-window complement.

ECL now evaluates the same outer first-variation coefficient:

    21.66851180520 < 16 C_partial < 21.66851180521.

The full moving-endpoint proof and integer outward certificate are supplied.
EQR updates the literal original QGQ4 centre, retaining its nonzero A/sqrt2
radius. This centre evaluation is not a limit of the actual W_k return.

RWC proves invertibility of the actual consecutive q-column windows using
the positive original quartet polynomial and Gamma orthogonality. It gives
the complete conditioned covariance update and every exterior coefficient:

    Phi_(k,s)=sum_(N=q-1,q) log(sum_(d=0)^j ||wedge^d Y_N||_HS^2).

Y_N includes the full original conditioning denominator and cross terms.
The new trace/determinant estimates strictly improve the earlier finite
first-increment lower bound. OER installs those bounds with PMR's range,
OAR's fallback and both unequal error endpoints. Finite strict growth has
not supplied the individual kq-scale residual coefficient.

MCE/MCP/RFX/OMR completes the same-arithmetic-class control connection.
The original A*G_N+G_N A-kG_N has relative eigenvalues epsilon_N,-epsilon_N
and zero. The surviving arithmetic exterior class supplies L_(h,k)<=epsilon_N.
The exact action budget retains the boundary return, monic-norm window and
both contraction penalties. Reflection makes the total untilted phase zero;
the kernel and boundary pairings may still be nonzero and opposite, leaving
the positive mixed contribution2|z_K|^2. No component or action leakage is
discarded when returning to that same arithmetic class.

The inherited OSP domain keeps epsilon=2^(-32), k>=29 and
k sqrt(delta^2+gamma^2)<=epsilon q/2; OFV additionally requires k>=257.
Conductor construction uses k>=9. Each theorem retains its own actual
finite domain; fixed-period or stated bounded-stratum results are not
asserted uniformly over arbitrary moving periods.

## What remains to calculate

The actual conditioned residual Phi_(k,s)/(kq) is still the next leading
metric calculation. Estimate its complete window covariance, an exterior
coefficient or compression, then return the full complement and induced
bound through OER and the unchanged action budget. The exact identities and
reductions above are completed inputs, not tasks to reconstruct again.

File11 includes full RCF/RCM/DNE continuation drafts, explicitly UNREVIEWED.
They are available for further calculation, not accepted estimates of this
edition. External FVR TeX/PDF was absent; preserved summaries do not certify
unseen sources. Complete local OFV/ECL/EQR/RWC proofs establish their own
stated results. No RH conclusion or programme completion is claimed.

## Reading and verification

File00 is the one exact current continuation; file14 is the complete editable
reader. Files09/10 are the complete joint/signed receivers; file02 has the
literal QGQ4 update. All four changed full TeX bodies reverse to the complete
161-page predecessor. File01 is historical, not the current preview.

The owner records three clean reader builds and all238 rendered pages:
156 inherited RGB body matches,21 fresh-page contact sheets, individually
corrected page170,237 other final images unchanged, all footers checked.
Receiver346/336-page compilations are compile-only, not visually accepted
delivered PDFs. FEX records587 checks per mode and8 intended rejections;
69 imported payloads remain exact. These are finite polynomial fixtures,
not actual xi periods or infinite-family certificates. No new local Lean
execution is asserted. Existing formalization and later merges retain their
own revision-specific records in file16 and the repository.

Publication reuses the complete owner proof/source/visual acceptance; it
does not repeat that audit. Only private account locators in the source map
are transported. The other16 files and all11 full TeX bodies are unchanged.

The existing [DOI10.5281/zenodo.22759785](https://doi.org/10.5281/zenodo.22759785) remains the62-download161-page edition until this new source cut is separately published there. No Zenodo/Overleaf/timer changes occur in this source transaction.

## Earlier source and edition guide (historical snapshot)

The following guide is preserved verbatim. Its current-reader and next-task statements belong to its own edition. The238-page reader above is current.

# Split-Zero cohomology: outer first variation and original residual metric

[Start here: the exact current owner continuation](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/af5c17948c24f43494ea76d823322e8b3924b58d/workbenches/splitzero-tandem/continuations/20260915-first-variation-continuation/00_CONTINUE_HERE.md).

[Read the current 161-page paper on GitHub](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/af5c17948c24f43494ea76d823322e8b3924b58d/workbenches/splitzero-tandem/continuations/20260915-first-variation-continuation/15_CURRENT_MIXED_CONTROL_READER.pdf) · [Read its published PDF](https://zenodo.org/api/records/22759785/files/61-first-variation-reader.pdf/content) · [Published DOI 10.5281/zenodo.22759785](https://doi.org/10.5281/zenodo.22759785).

- [161-page first variation](https://zenodo.org/api/records/22759785/files/61-first-variation-reader.pdf/content) · [complete editable source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/af5c17948c24f43494ea76d823322e8b3924b58d/workbenches/splitzero-tandem/continuations/20260915-first-variation-continuation) · [offline source ZIP](https://zenodo.org/api/records/22759785/files/62-first-variation-sources.zip/content).

The current 161-page reader evaluates the outer first variation in the original Gamma sources, constructs the fixed coefficient module and its exact original residual Schur metric, and propagates the combined kernel-plus-residual estimate through the arithmetic and signed cohomological return. Complete EIQ/QLG/OFV/FMC/OVR proofs and receiving statements retain the fixed original period, source orders 1 and k, full masses, phases, multiplicities and unequal finite errors.

## What is being calculated, and why

Split-Zero studies a finite arithmetic quotient associated with a selected
zeta-zero packet, its original theta cohomology and mixed-support maps. A
specified period observation has a common kernel K: the same kernel is
measured in the original source metrics at four degrees q-1, q, 2q-1 and 2q.
This is one fixed original period, not an intersection over different periods.
The aim is to calculate the contribution of that observation kernel and its
boundary complement to the original signed cohomological return.

The preceding 132-page edition expressed this kernel contribution as an outer
root-quotient term minus an explicit nonnegative residual-observation sum,
with both unequal finite error endpoints retained. Its moment comparison
identified seven same-source Gamma moment determinants to calculate. This
edition completes their first variation at the kq scale and constructs a fixed
coefficient module with the exact original residual metric still attached.

The main simple-quartet lane retains m=1, k=4l+1 with l>=1, q=(k+1)^2,
c=k/2, 0<delta<1/2, gamma>2 and every original branch |u|>=R_*.
The radius R_* comes from the actual quartet and full unit v_h=2xi/h.
The common kernel has rank r=8k-16 on this lane. The full multiplicity and
primary-coordinate algebra remains available without assigning this rank or
this metric conclusion to other multiplicities. The Gamma source orders are
the original s=1 and s=k; their masses, centres and coefficient phases remain.

## Completed outer first variation

OFV1-32 supplies the source-order recurrence, Gamma-to-exponential full-norm
comparison, scalar and growing-low determinant bounds, and high parity-block
estimate. EIQ1-33 and QLG1-32 provide the complete equilibrium density and
uniform finite-partition estimate used in that calculation. With

    Delta=q-(k-7)^2=16k-48,
    C_partial=4 log(4/pi)+2-2 I_(2,pi),
    I_(2,pi)=integral integral log|x-y| dmu_(2,pi)(x) dmu_(2,pi)(y),

the result for both original source orders is

    F_outer^(s)=Delta q C_partial+O_(delta,gamma)(q log q).

Here mu_(2,pi) is the proved EIQ equilibrium measure. The actual domain is
OSP23 together with k>=257: in particular epsilon=2^(-32), k>=29 and
k sqrt(delta^2+gamma^2)<=epsilon q/2 are retained. This eventual domain is
not confused with the conductor construction's earlier k>=9 domain.
The original period is fixed; no uniformity over moving periods is claimed.

## The original residual metric survives the coefficient construction

FMC1-38 constructs the rank-625 module over the original pure fifth powers,
its rank-125 invariant submodule, complete actual relation columns and a
terminating homogeneous reduction. The specified fixed-strip frame maps T_k
and T_k^(-1), including the residual map onto its image, have logarithmic
exterior cost O_actual(k^2)=o(kq) in every exterior rank. This estimate is
not assigned to the separate Vandermonde or degree-flag maps. The fixed
relation lists define actual-period constants; their full output for unknown
actual periods has not been numerically evaluated.

The exact map to the original source Gram G_N is

    J_k=N_k^transpose T_k^(-transpose),
    H_N=J_k* G_N J_k=[[H_11,N,H_12,N],[H_21,N,H_22,N]],
    Q_(Xi,N)^fix=H_11,N-H_12,N H_22,N^(-1) H_21,N.

The off-diagonal blocks and the full original Gamma metric are retained.
FMC27-28 gives the map to earlier certificate frames and the inherited period
Gram; FMC35-38 retains the primary-to-polynomial Vandermonde factor, literal
Lagrange interpolation and conductor degree-flag transition. Coefficient
conditioning therefore supplies explicit maps, not a replacement metric.

The equivalent ROQ constrained covariance uses the original certificate rows
D, relation rows C and source covariance R_N:

    Omega_N=D[R_N-R_N C*(C R_N C*)^(-1) C R_N]D*,
    Q_(Xi,N)=Omega_N^(-1).

Its exact nonnegative residual sum retains all original coefficients:

    Phi_(k,s)=log(1+eta_(q-1))
       +2 sum_(N=q)^(2q-2) log(1+eta_N)+log(1+eta_(2q-1))>=0.

## What the evaluated outer term proves for the original return

OVR1-11 carries the same residual through the source, arithmetic and signed
return maps. With Delta/k=16-48/k retained, it proves

    F_K^(s)+Phi_(k,s)=Delta q C_partial+R_(k,s),
    R_(k,s)=o(kq),
    (Phi_(k,k)-Phi_(k,1))/(kq) -> 0,
    (F_K^ar+Phi_(k,1))/(kq) -> 16 C_partial,
    (S_k^mix+Phi_(k,k))/(kq) -> 16 C_partial-C_Gamma/4.

These statements retain the two unequal signed finite error endpoints and
the original Gamma correction. The finite cap retains both actual first
positive-increment subtractions:

    F_K^(s)+Phi_(k,s)
       <=Delta(L_(s,q)+L_(s,q+1))-d_1-lambda_s.

Writing kappa_star=32 log(25 log3/(4pi)), OVR bounds each of the scaled kernel
and residual sequences between lower limit max(0,16 C_partial-kappa_star)
and upper limit min(kappa_star,16 C_partial). Their sum converges to
16 C_partial, and 0<=C_partial<=kappa_star/8. **This is not a proof that
either separate sequence has a limit.** The earlier finite pointwise KAF/AKS
minimum remains. Its asymptotic sourcewise ceiling is retained separately:
limsup F_K^a/(kq)<=kappa_star<25.02078097650 for a=sigma,0,ar.

## The current calculation

The next task is the leading contribution of Phi_(k,s) in its original metric,
using the complete ROQ constrained covariance or the equivalent FMC Schur
complement. Evaluated positive partial sums already yield valid finite
subtractions. A leading estimate must preserve the source-ideal graph,
kernel cross terms, complete relation denominator and all four endpoints.

Alongside it, the owner continuation asks for the exact quantitative connection
from the signed return to the canonical control of the same surviving
arithmetic class. The starting form is A*G_N+G_N A-kG_N, with its original
endpoint vectors, two nonzero eigenvalues, full radius and exterior spectral
defect. Its action, connection and boundary terms must be calculated in that
metric. A scalar volume estimate alone has not supplied an exclusion theorem.

The outer first variation is completed on its explicit eventual domain. The combined kernel-plus-residual leading value is established there; the separate residual and kernel leading values and the quantitative connection to the original control form remain active calculations. Coefficient conditioning does not replace the Gamma metric. No moving-period uniformity, RH exclusion or programme completion is claimed. Later outer-operator and control-form editions are not part of this sealed cut.

## Complete sources and recorded verification

[File14: complete editable proofs](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/af5c17948c24f43494ea76d823322e8b3924b58d/workbenches/splitzero-tandem/continuations/20260915-first-variation-continuation/14_CURRENT_KERNEL_AND_MULTIPLICITY_PROOFS.tex)
preserves the full 132-page predecessor and includes complete EIQ1-33,
QLG1-32, OFV1-32, FMC1-38 and OVR1-11. The receiving successors
[joint file09](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/af5c17948c24f43494ea76d823322e8b3924b58d/workbenches/splitzero-tandem/continuations/20260915-first-variation-continuation/09_UPDATED_JOINT_NOTE.tex) and
[signed file10](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/af5c17948c24f43494ea76d823322e8b3924b58d/workbenches/splitzero-tandem/continuations/20260915-first-variation-continuation/10_UPDATED_SIGNED_RETURN.tex) contain the complete
MRI4r-v and BRI6h-i refinements, retaining every earlier provider. Their
268/260-page builds establish compilation only, not visually accepted receiver
PDFs. [Arithmetic source file13](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/af5c17948c24f43494ea76d823322e8b3924b58d/workbenches/splitzero-tandem/continuations/20260915-first-variation-continuation/13_ARITHMETIC_MIXED_TRANSFER.tex)
retains the original correlated allowances and maps.

The delivered 161-page reader has the owner's full visual acceptance:
129 complete page images match the accepted predecessor; pages1,2,5 and
133-146 were inspected individually by the owner, and147-161 by an independent
reviewer. All footers were checked. The complete new written proofs and
receiving statements have their recorded independent acceptance.

FMC's diagnostic script records 30,634 exact checks in both normal and
optimized Python. These are finite fixtures, not actual zeta periods or the
full actual Groebner output. No new local Lean execution is claimed by this
edition. [File16](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/af5c17948c24f43494ea76d823322e8b3924b58d/workbenches/splitzero-tandem/continuations/20260915-first-variation-continuation/16_PR32_FORMAL_SOURCE_AND_PROOFS.md) preserves
its original complete four-module record: observed strict implementation
8e78bc7c240b04d297ade6afdadfd863e0c6db7b and final documentation/source head
9cec8482f2ecf978cf8bdb67b4c080b9dd74f5d6, with 33 local modules and 56 selected
transitive axiom targets. The appended PR34/35 report is historical coordination
at its stated inspected revisions, not a new whole-stack CI certificate.
Later integration status must come from the integration owner's exact receipts;
this reading index neither overwrites those records nor claims new checks.

[Validation12](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/af5c17948c24f43494ea76d823322e8b3924b58d/workbenches/splitzero-tandem/continuations/20260915-first-variation-continuation/12_VALIDATION.md) states these precise scopes.
[Source map11](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/af5c17948c24f43494ea76d823322e8b3924b58d/workbenches/splitzero-tandem/continuations/20260915-first-variation-continuation/11_SOURCE_MAP.json) distinguishes the original
SHA-256 `f3b01e7efc3f30858253db0626d60803598913465fefa27c194b855e33ab6226` from the public transported
SHA-256 `8ce030c567a5538e9afc77a61b655d0c23d1af4d1a8b40452cbd5584b47411c8`. Its metadata-only transport scope is:
891 literal historical private-account locator occurrences transported across802 values and8 path-valued keys. Mathematical bodies, original identities, numeric fields, source spans and other metadata unchanged. The other sixteen files and all eleven full TeX bodies
are unchanged by the publication transport.

The exact seventeen-file edition has one current continuation: original
owner00. This index is a reading guide, not a competing research prompt.
Later outer-operator and control-form drafts remain outside this sealed cut.

## Earlier complete source editions

- [Earlier 20260915 quotient moment continuation source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/bf39bac055b76ce755b91401b35570bb84d76d9a/workbenches/splitzero-tandem/continuations/20260915-quotient-moment-continuation).
- [Earlier exterior kernel continuation source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/dad07e28faa735104ddc0b137521620fc315e6fc/workbenches/splitzero-tandem/continuations/20260914-exterior-kernel-continuation).
- [Earlier conductor kernel continuation source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/41adc412ceb119ad9086b1f106e377f3de2d401a/workbenches/splitzero-tandem/continuations/20260914-conductor-kernel-continuation).
- [Earlier original kernel matrices source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/5817ef9027257375b6ff3de7048b3331077251e7/workbenches/splitzero-tandem/continuations/20260914-original-kernel-matrices).
- [Earlier original volumes source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/1c8ec52c85c173adc9f8403a8a26914955e2f5a9/workbenches/splitzero-tandem/continuations/20260914-original-volumes).
- [Earlier gamma growth source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/41f020e0475429943252e69a1b4edd849393c780/workbenches/splitzero-tandem/continuations/20260914-gamma-growth).
- [Earlier joint gamma schur source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/2be3b23974bf040f4ea06240b8a4b85372f7c71d/workbenches/splitzero-tandem/continuations/20260914-joint-gamma-schur).
- [Earlier original relation bulk source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/01fc8820e3a3ea69afa22b8ab1b0b5ca61869456/workbenches/splitzero-tandem/continuations/20260914-original-relation-bulk).
- [Earlier complete gamma return source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/01fc8820e3a3ea69afa22b8ab1b0b5ca61869456/workbenches/splitzero-tandem/continuations/20260914-complete-gamma-return).

The [earlier 60-download edition](https://doi.org/10.5281/zenodo.22759221) remains
unchanged with its 132-page preview. This edition adds PDF61 and ZIP62.
The actual human-readable preview is the current 161-page PDF61; ZIP62
contains the seventeen source files for offline use. Every earlier download
and mathematical source remains intact.

[All 62 downloads and source identities](calculation_edition_20260915_first_variation/README.md).

## Earlier source and edition guide (historical snapshot)

The following guide is preserved verbatim from the preceding publication
state. Its current-reader and next-calculation statements belong to that
edition. The outer first variation requested there is completed in the
161-page edition above. The original residual leading metric and the
control-form connection remain active mathematics. Historical source,
proof, publication and integration records retain their original scopes.

# Split-Zero cohomology: evaluated outer moments and the residual metric

[Start here: the current continuation](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260915-first-variation-continuation/00_CONTINUE_HERE.md).

[Read the current 161-page paper](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260915-first-variation-continuation/15_CURRENT_MIXED_CONTROL_READER.pdf) · [Complete editable proofs](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260915-first-variation-continuation/14_CURRENT_KERNEL_AND_MULTIPLICITY_PROOFS.tex).

This edition studies the original arithmetic theta source and the quotient
through which it represents cohomology classes associated with zeta zeros.
The calculation uses the actual period and the full amplitude unit to observe
that quotient. It asks how much of the original source metric survives in
the observation kernel, and how this affects the signed return to the same
arithmetic class. The Deligne mixed-cohomology programme is the research
direction. These estimates do not assert an RH proof or counterexample.

The preceding edition reduced this question to seven same-source Gamma moment
determinants and an actual residual covariance. This edition evaluates the
outer moment contribution and constructs fixed coefficient frames for the
remaining residual metric. All seventeen files and eleven full LaTeX bodies
are supplied directly; the complete 132-page predecessor is preserved.

## Original objects, not replacement metrics

Lambda_k is the tensor-degree-k period/unit-jet observation. K is its kernel
at the specified actual period, shared by the original source metrics; it is
not an intersection over periods. The source orders remain s=1,k, and the
four original degree endpoints are q-1,q,2q-1,2q with signs (1,1,-1,-1).
Full unit values, masses, phases, coordinates, primary multiplicities,
minimum sections, induced actions and action defects remain in the proofs.

The sharp metric lane uses a simple quartet: m=1, k=4l+1, l>=1,
q=(k+1)^2, c=k/2, 0<delta<1/2 and gamma>2. Every original period branch
with |u|>=R_* remains, with R_* computed from the given quartet and unit.
The conductor reduction uses k>=9. Separate all-multiplicity maps are
retained without assigning the simple-quartet metric ranks to other inputs.

F_K^(s) is the signed log-volume of the kernel at the four endpoints.
Phi_k,s is the positive residual-increment sum from the actual period
certificate rows and full constrained covariance:

    Phi_k,s = log(1+eta_(q-1))
              + 2 sum_(N=q)^(2q-2) log(1+eta_N)
              + log(1+eta_(2q-1)) >= 0.

The eta_N are specified covariance updates, not generic matrices or
numerical evaluations at invented period values.

## The outer moment calculation is now evaluated

OFV1-32 proves the first variation of all seven moment determinants,
including their scalar, growing-low and high even/odd blocks. Complete
EIQ1-33 equilibrium-density and QLG1-32 finite-partition proofs are included.
For both original source orders s=1,k, on OSP23's explicit eventual domain
and k>=257, the result is

    F_outer^(s) = Delta q C_partial + O_(delta,gamma)(q log q),
    Delta = 16k-48,
    C_partial = 4 log(4/pi) + 2 - 2 I_(2,pi).

I_(2,pi) is the double logarithmic energy of the proved EIQ density
mu_(2,pi), not an assigned constant from a different measure. The OSP domain
retains epsilon=2^(-32), k>=29 and
k sqrt(delta^2+gamma^2)<=epsilon q/2. Every source mass, centre and
polynomial-coordinate phase remains in the full first-variation proof.

OVR1-11 returns this evaluation to the original objects:

    F_K^(s) + Phi_k,s = Delta q C_partial + R_k,s,  R_k,s=o(kq),
    (Phi_k,k - Phi_k,1)/(kq) -> 0,
    (F_K^ar + Phi_k,1)/(kq) -> 16 C_partial,
    (S_mix + Phi_k,k)/(kq) -> 16 C_partial - C_Gamma/4.

The sum converges; no limit of either separate kernel or residual sequence
is assigned. The exact common finite cap retains both actual first-positive-
increment subtractions. With kappa_*=32 log(25 log(3)/(4 pi)), each scaled
sequence has lower limit at least max(0,16 C_partial-kappa_*) and upper
limit at most min(kappa_*,16 C_partial). Also 0<=C_partial<=kappa_*/8.

## The residual metric has an explicit fixed-frame construction

FMC1-38 constructs the fixed module over the original pure fifth powers:
rank 625, a rank-125 invariant submodule, full original relation columns and
a proved terminating homogeneous reduction. For a fixed actual period,
the specified fixed-strip frame maps T_k and T_k^(-1), including the
residual map onto its image, have all-rank logarithmic exterior cost
O_actual(k^2)=o(kq). This estimate is not assigned to the separate
Vandermonde or degree-flag maps; those retain their full factors.

The finite relation lists are defined by the proved construction, not
claimed numerically evaluated at unknown actual periods. The exact metric
transport is

    J_k = N_k^T T_k^(-T),
    H_N = J_k* G_N J_k = [[H_11,N, H_12,N], [H_21,N, H_22,N]],
    Q_Xi,N^fix = H_11,N - H_12,N H_22,N^(-1) H_21,N.

Thus the full Gamma Schur complement, inherited period Gram, primary-to-
polynomial Vandermonde factor, Lagrange interpolation and conductor degree
flag all remain explicit. Coefficient conditioning is not substituted for
the original Gamma metric.

## What remains to calculate

The active calculation is Phi_k,s/(kq) at the fixed original period,
using ROQ's full constrained covariance or the equivalent FMC Schur
complement. Its transport must retain CEP's low-degree correction and
complete source-ideal/kernel graph in the denominator. Actual partial
residual sums already give valid finite subtractions.

In parallel, the continuation asks for the exact relation between the signed
return and A*G_N+G_N A-kG_N, the canonical control form on the same surviving
arithmetic class. Original endpoint vectors, both nonzero eigenvalues,
boundary terms, action defects and multiplicities remain. A scalar volume
estimate alone has not supplied that exclusion inequality. Subsequent OOQ
outer-operator and MCE control-form calculations are outside this sealed cut.

## Complete sources and verification scope

- [14: complete current proofs](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260915-first-variation-continuation/14_CURRENT_KERNEL_AND_MULTIPLICITY_PROOFS.tex) preserves the full predecessor and EIQ/QLG/OFV/FMC/OVR.
- [09: joint receiver](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260915-first-variation-continuation/09_UPDATED_JOINT_NOTE.tex) and [10: signed-return receiver](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260915-first-variation-continuation/10_UPDATED_SIGNED_RETURN.tex) contain the complete providers and actual new MRI4r-v/BRI6h-i statements.
- [13: arithmetic mixed transfer](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260915-first-variation-continuation/13_ARITHMETIC_MIXED_TRANSFER.tex) retains the original arithmetic source and correlated deficits.
- [02: Gamma foundations](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260915-first-variation-continuation/02_FULL_GAMMA_PROOFS.tex) and [03: observation foundations](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260915-first-variation-continuation/03_FULL_OBSERVATION_PROOFS.tex) contain full earlier dependencies; files04-08 retain cyclic, period and kernel calculations.
- [16: formal source and integration history](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260915-first-variation-continuation/16_PR32_FORMAL_SOURCE_AND_PROOFS.md) preserves its preceding four-module proofs/CI record as an exact prefix and appends the complete dated PR34/35 report. Those historical observations are not a new whole-stack certificate.
- [01: preceding 75-page Gamma reader](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260915-first-variation-continuation/01_GAMMA_READER.pdf) is background, not the current 161-page paper.

[Validation](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260915-first-variation-continuation/12_VALIDATION.md) records the existing independent
proof and receiving acceptance. All 161 reader pages were rendered: 129 whole
page images match accepted predecessor images, and the other pages were
individually inspected; the full footer sequence was checked. The delivered
reader has no recorded layout/reference warnings. Receiver builds of 268/260 pages
remain compilation-only, not visually approved receiver PDFs.

FMC's 30,634 exact diagnostic checks passed normal and optimized Python for
their stated finite fixtures. They are not actual zeta-period evaluations
or the full actual Groebner output. No new local Lean execution is claimed.
The repository's actual merged revision and checks have separate receipts.
This transport reuses the accepted proofs and visuals; it does not repeat
mathematical, PDF, source or archive audits.

Only private account locators in the [source map](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260915-first-variation-continuation/11_SOURCE_MAP.json)
were transported. Original map SHA-256:
f3b01e7efc3f30858253db0626d60803598913465fefa27c194b855e33ab6226.
Public map SHA-256:
8ce030c567a5538e9afc77a61b655d0c23d1af4d1a8b40452cbd5584b47411c8.
891 literal historical private-account locator occurrences transported across802 values and8 path-valued keys. Mathematical bodies, original identities, numeric fields, source spans and other metadata unchanged. The other sixteen files, including
both PDFs and all eleven TeX bodies, are exact accepted delivery bytes.

The published [DOI 10.5281/zenodo.22759221](https://doi.org/10.5281/zenodo.22759221) retains its 60 downloads and
132-page PDF59 preview. This GitHub source cut is outside that frozen
edition until a separate DOI edition is actually published. This source
transaction makes no Zenodo, Overleaf or timer changes.

## Earlier source and edition guide (historical snapshot)

The following guide remains verbatim. Its earlier prompts and next steps
belong to their dated editions; the exact current prompt and 161-page paper
above provide current navigation without modifying preceding sources.

# Split-Zero cohomology: outer moments and residual observations

[Start here: the exact current owner continuation](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/bf39bac055b76ce755b91401b35570bb84d76d9a/workbenches/splitzero-tandem/continuations/20260915-quotient-moment-continuation/00_CONTINUE_HERE.md).

[Read the current 132-page paper on GitHub](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/bf39bac055b76ce755b91401b35570bb84d76d9a/workbenches/splitzero-tandem/continuations/20260915-quotient-moment-continuation/15_CURRENT_MIXED_CONTROL_READER.pdf) · [Read its published PDF](https://zenodo.org/api/records/22759221/files/59-quotient-moment-reader.pdf/content) · [Published DOI 10.5281/zenodo.22759221](https://doi.org/10.5281/zenodo.22759221).

- [132-page quotient kernel](https://zenodo.org/api/records/22759221/files/59-quotient-moment-reader.pdf/content) · [complete editable source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/bf39bac055b76ce755b91401b35570bb84d76d9a/workbenches/splitzero-tandem/continuations/20260915-quotient-moment-continuation) · [offline source ZIP](https://zenodo.org/api/records/22759221/files/60-quotient-moment-sources.zip/content).

The current 132-page reader adds complete CTV/ROQ/OSP/OAR/PMR proofs. The original kernel contribution is now expressed as seven same-source Gamma moment determinants minus the actual positive residual-increment sum, with two unequal o(kq) error endpoints in the stated fixed-period and eventual parameter domains. The seventeen-file package preserves the sole owner prompt, complete receiving proofs and unchanged recorded PR32 source/CI.

## What this calculation studies

Split-Zero follows a finite arithmetic quotient attached to a selected zeta-zero
packet, with its original theta cohomology and mixed-support maps. A specified
period observation loses a subspace K. The calculation measures that same
kernel in the original source metrics at four degrees q-1, q, 2q-1 and 2q.
The goal is its contribution to the original signed cohomological return,
not a conclusion inferred merely from the dimension of K.

The preceding conductor calculation gave a smaller root grid and controlled
the transport error by o(kq) for each fixed actual period. This edition
constructs the resulting outer quotient and residual observation explicitly.
It then compares the outer quotient with same-source power-weight moments.
The result is an explicit seven-determinant expression minus the actual
positive residual-increment sum, with both unequal finite error endpoints.

The main simple-quartet lane retains m=1, k=4l+1 with l>=1, q=(k+1)^2,
c=k/2, 0<delta<1/2 and gamma>2, at every original branch |u|>=R_*.
R_* is calculated from the actual quartet and full unit. The kernel dimension
is r=8k-16 on that domain; the full all-multiplicity geometry and primary
nilpotents remain without assigning that rank to other multiplicities.
For k>=9, the conductor construction retains all original coefficients,
periods and its nonzero moment denominator.

## Completed outer quotient and residual observation

CTV proves the original central-root factorization
P_k=P_(k-8) P_(partial,k), with every root unchanged. Multiplication by the
full P_(k-8) supplies the exact metric |P_(k-8)(y)|^2 dm_s(y), retaining
the original mass. The outer quotient has rank Delta=16k-48 and source
degrees Delta-1, Delta, q+Delta-1 and q+Delta. The lower-grid quantities
remain k'=k-8, q'=(k-7)^2, centre c'=c-4 and source order s=1 or k.
Every primary Vandermonde factor, affine phase, shifted endpoint and signed
monic-norm tail is retained.

ROQ builds the actual residual map Xi: V_A -> C^j, j=8k-32, from the
original certificate rows D=F^transpose. It retains the original boundary
basis, inherited period-word metric, pivot determinant, source metric and
full kernel-plus-ideal graph. Its constrained covariance is

    Omega_N = D [R_N - R_N C* (C R_N C*)^(-1) C R_N] D*,
    Q_(Xi,N) = Omega_N^(-1).

No generic residual matrix or rank-only volume is substituted. Its complete
positive cutoff-increment sum is

    Phi_(k,s) = F_(Xi,k)^(s)
      = log(1+eta_(q-1))
        + 2 sum_(N=q)^(2q-2) log(1+eta_N)
        + log(1+eta_(2q-1)) >= 0.

Each eta_N is given in the actual original coefficients and constrained
covariance update. OAR keeps both unequal signed error endpoints:

    F_K^(s) = F_(partial,k)^(s) - Phi_(k,s) + e_(k,s),
    -e_(k,s)^- <= e_(k,s) <= e_(k,s)^+,
    e_(k,s)^- = o(kq), e_(k,s)^+ = o(kq).

The kernel caps subtract the actual first positive residual increment.
Additional evaluated positive increments supply further finite subtractions;
the correlated arithmetic boundary and signed return retain those same signs.

## Comparison with seven original Gamma moment determinants

OSP compares the full original root-polynomial norms with same-source
power-weight norms, in every polynomial direction, including the entire
small-real-coordinate region. Its explicit eventual domain is

    epsilon = 2^(-32), k>=29,
    k sqrt(delta^2+gamma^2) <= epsilon q/2.

This domain is separate from the conductor's k>=9 domain. The original source
orders remain s=1 and k; no zero, period or source mass is replaced. In this
domain the proved comparison is

    |F_(partial,k)^(s) - F_(0,k)^(s)|
       <= c_k^circle = 4(q+Delta+1) E_k
       = O_(delta,gamma)(q) = o(kq).

F_(0,k)^(s) is the seven signed moment determinants written in OSP32, not seven
scalar moments. Each is constructed from the exact same-source moments

    mu_j^(s) = M_s [d^j/dz^j (cos z)^(-s/2)]_(z=0),
    D_a(Q;s) = det [mu_(2Q+i+j)^(s)]_(0<=i,j<a).

M_s is the full original source mass. OSP35 supplies the exact even/odd
factorization. PMR carries the additional comparison error into the original
arithmetic kernel, correlated boundary and signed mixed return:

    F_K^(s) = F_(0,k)^(s) - Phi_(k,s) + e_(k,s)^0,
    -e_(k,s)^(0,-) <= e_(k,s)^0 <= e_(k,s)^(0,+),
    e_(k,s)^(0,-) = o(kq), e_(k,s)^(0,+) = o(kq).

**The two finite error endpoints remain unequal.** PMR8 proves that interval
intersection alone preserves the previous outer-root finite endpoints exactly.
The moment comparison supplies a concrete analytic target; it does not by
itself tighten that previous interval. Evaluating additional actual residual
increments is the stated source of finite subtractions.

All these conductor and residual statements retain the fixed-period scope.
No moving-period uniformity or RH conclusion is asserted. The earlier AKS
finite pointwise minimum with KAF and its ceiling25.02078097650 remain valid.

## What remains to calculate

The next calculation is the kq-scale difference between all seven determinants
F_(0,k)^(s) and the actual residual sum Phi_(k,s). For the moment term, the
first variation compares q'=(k-7)^2 with q=(k+1)^2 at the original source
order. High parity blocks have dimension proportional to q; the growing low
blocks have dimension proportional to k and a different parameter ratio;
D_1(q;s) is scalar. The existing q^2 asymptotic alone gives no uniform
first-variation error estimate for those different regimes.

For the residual term, the exact period certificates and constrained covariance
updates already specify the sum. The full denominator, source-ideal terms and
kernel cross terms must remain in any estimate. **No unique limit or exact
leading value is asserted.** Newer first-variation and fixed-module-conditioning
drafts are not part of this sealed edition.

The exact outer quotient, residual covariance and same-source moment comparison are completed. The next calculation is their kq-scale first variation and actual residual sum. PMR8 proves that interval intersection alone does not tighten the preceding outer-root finite endpoints. No leading value, moving-period uniformity or RH conclusion is asserted; newer first-variation and fixed-module-conditioning drafts are excluded.

## Complete proofs, receivers and checked-source scope

[File14: complete current proofs](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/bf39bac055b76ce755b91401b35570bb84d76d9a/workbenches/splitzero-tandem/continuations/20260915-quotient-moment-continuation/14_CURRENT_KERNEL_AND_MULTIPLICITY_PROOFS.tex) preserves the full preceding
110-page development and adds complete CTV1-22, ROQ1-27, OSP1-35, OAR1-11
and PMR1-8 proofs. It is the editable source of the current 132-page reader.
[Arithmetic source transfer, file13](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/bf39bac055b76ce755b91401b35570bb84d76d9a/workbenches/splitzero-tandem/continuations/20260915-quotient-moment-continuation/13_ARITHMETIC_MIXED_TRANSFER.tex)
retains the original correlated source allowances and their exact maps.

[Joint receiver09](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/bf39bac055b76ce755b91401b35570bb84d76d9a/workbenches/splitzero-tandem/continuations/20260915-quotient-moment-continuation/09_UPDATED_JOINT_NOTE.tex) and
[signed receiver10](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/bf39bac055b76ce755b91401b35570bb84d76d9a/workbenches/splitzero-tandem/continuations/20260915-quotient-moment-continuation/10_UPDATED_SIGNED_RETURN.tex) retain all 31
preceding providers and the complete later proofs. Current receiving sites
are MRI4e-q and BRI6c-g, with new MRI4l-q and BRI6f-g carrying the complete
outer, moment and residual refinements. Their 249/240-page builds establish
compilation and source closure, not visual acceptance of receiver PDFs.
Those separate PDF builds are not delivered as visually accepted papers.

The current reader's complete 132 pages have the owner's visual acceptance:
106 body regions match the accepted predecessor; five opening pages and every
new page112-132 were inspected individually. All 132 footers were checked
visually and against sequential PDF text. Complete new written proofs and
receiving replacements have independent acceptance. The declared diagnostic
fixtures are not actual-zero or actual-period evaluations.

[File16: complete PR32 formal source and proofs](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/bf39bac055b76ce755b91401b35570bb84d76d9a/workbenches/splitzero-tandem/continuations/20260915-quotient-moment-continuation/16_PR32_FORMAL_SOURCE_AND_PROOFS.md)
is unchanged. It retains the four modules, full note, runner and successful
two-job CI at implementation8e78bc7c240b04d297ade6afdadfd863e0c6db7b and
unchanged checked source at finalhead9cec8482f2ecf978cf8bdb67b4c080b9dd74f5d6.
The recorded scope remains 33 local modules and 56 selected transitive axiom
targets. No new local Lean run or PR merge is claimed; the new analytic
estimates have written-proof scope.

[Validation](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/bf39bac055b76ce755b91401b35570bb84d76d9a/workbenches/splitzero-tandem/continuations/20260915-quotient-moment-continuation/12_VALIDATION.md) records these exact scopes.
[Source map](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/bf39bac055b76ce755b91401b35570bb84d76d9a/workbenches/splitzero-tandem/continuations/20260915-quotient-moment-continuation/11_SOURCE_MAP.json) distinguishes owner-original
SHA-256 `4375c0cbad44222cdb690cf6ad6ff4335173e542bfb90688358c26528a2e0c7f` from public transported SHA-256
`3c1f19a98303915846e65260894348f7ad6290ae7c2e1a22a3b74ee38d065a6c`. Its metadata-only transport scope is:
777 literal historical private-account locator occurrences transported across739 values and8 path-valued keys, including nested JSON. Full mathematical bodies, original source hashes and other metadata remain unchanged. Original embedded identities still identify pre-transport sources. The other sixteen files are unchanged.

This is exactly the accepted seventeen-file edition. The original owner00
remains the sole current continuation; this index creates no competing prompt.
The preceding 110-page, 97-page, 72-page and Gamma editions remain intact.

## Earlier complete source editions

- [Earlier exterior kernel continuation source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/dad07e28faa735104ddc0b137521620fc315e6fc/workbenches/splitzero-tandem/continuations/20260914-exterior-kernel-continuation).
- [Earlier conductor kernel continuation source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/41adc412ceb119ad9086b1f106e377f3de2d401a/workbenches/splitzero-tandem/continuations/20260914-conductor-kernel-continuation).
- [Earlier original kernel matrices source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/5817ef9027257375b6ff3de7048b3331077251e7/workbenches/splitzero-tandem/continuations/20260914-original-kernel-matrices).
- [Earlier original volumes source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/1c8ec52c85c173adc9f8403a8a26914955e2f5a9/workbenches/splitzero-tandem/continuations/20260914-original-volumes).
- [Earlier gamma growth source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/41f020e0475429943252e69a1b4edd849393c780/workbenches/splitzero-tandem/continuations/20260914-gamma-growth).
- [Earlier joint gamma schur source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/2be3b23974bf040f4ea06240b8a4b85372f7c71d/workbenches/splitzero-tandem/continuations/20260914-joint-gamma-schur).
- [Earlier original relation bulk source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/01fc8820e3a3ea69afa22b8ab1b0b5ca61869456/workbenches/splitzero-tandem/continuations/20260914-original-relation-bulk).
- [Earlier complete gamma return source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/01fc8820e3a3ea69afa22b8ab1b0b5ca61869456/workbenches/splitzero-tandem/continuations/20260914-complete-gamma-return).

The [earlier 58-download edition](https://doi.org/10.5281/zenodo.22758970) remains frozen
with its 110-page preview. This edition adds PDF59 and ZIP60. The actual
new browser preview is the current 132-page PDF59; ZIP60 supplies all seventeen
flat source files for offline use, not a substitute preview. Every earlier
mathematical/source file remains unchanged.

[All 60 downloads and source identities](calculation_edition_20260915_quotient_moments/README.md).

## Earlier source and edition guide (historical snapshot)

The following guide is retained verbatim from the preceding source/publication
state. Its current-reader and next-calculation statements describe its explicit
edition, not this new 60-download reading route. The original outer-root
quotient, residual covariance and moment comparison are now complete at the
scopes above. Their next leading-value calculations remain unfinished.
In particular, interval intersection alone does not tighten the earlier
outer-root finite endpoints. Earlier prompts, source identities, mathematics
and proof/CI scopes remain intact as provenance.

# Split-Zero cohomology: outer moments and residual observations

[Start here: the current continuation](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260915-quotient-moment-continuation/00_CONTINUE_HERE.md).

[Read the current 132-page paper](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260915-quotient-moment-continuation/15_CURRENT_MIXED_CONTROL_READER.pdf) · [Complete editable proof source](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260915-quotient-moment-continuation/14_CURRENT_KERNEL_AND_MULTIPLICITY_PROOFS.tex).

This seventeen-file edition studies the original arithmetic theta source,
its cohomological quotient and actual period/unit observation. Its subject
is the common kernel volume in the original four-endpoint source metrics.
The Deligne mixed-cohomology programme remains the research direction;
no RH conclusion is assigned by these calculations.

The exact owner prompt is the single current continuation. All eleven
LaTeX files retain their full mathematical proof inputs inline. The complete
110-page predecessor and its accepted proofs remain, with full CTV, ROQ,
OSP, OAR and PMR added. File16 retains the existing PR32 formal source,
written proofs and observed CI. No archive or missing local TeX provider
folder must be unpacked.

## Original objects and domains

Lambda_k is the specified tensor-degree-k period/unit-jet observation;
K is its kernel at the specified actual period, shared by the original
source metrics, not an intersection across periods. The canonical source
orders stay s=1,k. Full unit values, masses, phases, period branches,
primary multiplicities, minimum sections and action defects are retained.

The simple-quartet domain is m=1, k=4l+1 with l>=1, q=(k+1)^2,
0<delta<1/2, gamma>2 and every original branch with |u|>=R_*.
R_* is computed from the specified quartet and full unit. The completed
ranks are dim K=8k-16 and dim B_k=k^2-6k+17. The conductor reduction uses
k>=9. Separate all-multiplicity OCS/OMG maps retain their full primary
coordinates and nilpotents without assigning these simple-quartet ranks
to other inputs.

The original four source degrees are q-1,q,2q-1,2q with signs (1,1,-1,-1).
Their kernel metric-volume combination is

    F_K^(s) = log det H_0^(s) + log det H_1^(s)
              - log det H_q^(s) - log det H_(q+1)^(s).

## Completed quotient and moment reduction

CTV retains the literal real-coordinate factorization P_k=P_(k-8) P_boundary,k.
Multiplication by the complete P_(k-8) gives the exact induced metric
|P_(k-8)(y)|^2 dm_s(y), with the same full original mass. The outer quotient
has rank Delta=16k-48 and source degrees Delta-1,Delta,q+Delta-1,q+Delta.
All primary Vandermonde factors, affine phases and shifted endpoints remain.
The conductor and monic-norm tail errors are subleading at fixed actual period.

ROQ constructs the actual residual quotient Xi of rank 8k-32 from the
original period certificates. Its constrained covariance, full inherited
word metric, kernel-plus-ideal graph and ordered denominator remain explicit.
Its positive residual increments give the exact sum

    Phi_k,s = log(1+eta_(q-1))
              + 2 sum_(N=q)^(2q-2) log(1+eta_N)
              + log(1+eta_(2q-1)) >= 0.

The eta_N are calculated from the actual constrained covariance updates,
not assigned generic matrices or evaluated at invented period values.

OSP proves a full-norm comparison to same-source power-weight moments,
including the entire small-real-coordinate region. Its explicit eventual
domain is

    epsilon=2^(-32),     k>=29,
    k sqrt(delta^2+gamma^2) <= epsilon q/2.

On that domain the comparison error is O_(delta,gamma)(q)=o(kq) for the
fixed actual quartet, in both original source orders1,k. The moment building
blocks are

    mu_j^(s) = M_s [d^j/dz^j (cos z)^(-s/2)]_(z=0),
    D_a(Q;s) = det[mu_(2Q+i+j)^(s)]_(0<=i,j<a).

F_0,k^(s) is the complete signed seven-determinant expression of OSP32.
OSP35 supplies its exact even/odd factorization. The original source mass
M_s and every block dimension and power shift are retained.

OAR/PMR carry the unequal signed errors into the original arithmetic kernel,
correlated boundary and signed return. The current identity is

    F_K^(s) = F_0,k^(s) - Phi_k,s + e_0,k,s,
    -e_0,k,s^- <= e_0,k,s <= e_0,k,s^+,
    e_0,k,s^- = o(kq),     e_0,k,s^+ = o(kq).

The two finite error endpoints remain unequal. No leading moment or residual
value, unique limit or moving-period uniformity is assigned.

PMR8 proves that intersecting the moment-comparison interval retains the
previous outer-root finite endpoints exactly. That comparison alone does
not tighten them. Evaluating additional actual positive residual increments
does give the proved finite subtractions in OAR6-7; the current edition
does not substitute fixture evaluations for those actual quantities.

## The next calculation

Evaluate the first variation of all seven same-source Gamma moment
determinants and their difference with Phi at scale kq. Retain the original
source order s=1 or k and OSP35 parity factors: the high blocks have dimension
proportional to q, the growing low blocks have dimension proportional to k
with a different power-to-dimension ratio, and D_1(q;s) is scalar. Every
analytic estimate must match its actual parameter domain and control the
first-variation remainder; a q^2 asymptotic alone does not do that.

For the residual sum, retain ROQ's actual period coefficients, full constrained
covariances and the complete source-ideal/kernel cross terms in its denominator.
The previous outer-root comparison is already controlled. Establish the
fixed-period result before any moving-period extension. Newer first-variation
and fixed-module-conditioning drafts are separate and excluded from this
sealed edition.

## Complete proofs, receivers and verification

- [14: current full proof source](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260915-quotient-moment-continuation/14_CURRENT_KERNEL_AND_MULTIPLICITY_PROOFS.tex) preserves every preceding chapter and adds complete CTV1-22, ROQ1-27, OSP1-35, OAR1-11 and PMR1-8.
- [09: complete joint receiver](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260915-quotient-moment-continuation/09_UPDATED_JOINT_NOTE.tex) and [10: complete signed-return receiver](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260915-quotient-moment-continuation/10_UPDATED_SIGNED_RETURN.tex) retain every preceding full provider and the complete new bodies. Actual sites MRI4e-q and BRI6c-g carry the new intervals, arithmetic correlations, exact boundary complements and signed consequences; the recorded edits reconstruct the preceding entire sealed receiver bodies.
- [13: arithmetic mixed transfer](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260915-quotient-moment-continuation/13_ARITHMETIC_MIXED_TRANSFER.tex) retains the full original source and correlated deficits.
- [02: Gamma foundations](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260915-quotient-moment-continuation/02_FULL_GAMMA_PROOFS.tex) and [03: observation foundations](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260915-quotient-moment-continuation/03_FULL_OBSERVATION_PROOFS.tex) retain the full dependencies; files04-08 retain the preceding cyclic, period and kernel calculations.
- [16: PR32 formal source and written proofs](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260915-quotient-moment-continuation/16_PR32_FORMAL_SOURCE_AND_PROOFS.md) remains unchanged: four modules, complete note, runner and recorded CI at implementation8e78bc7c240b04d297ade6afdadfd863e0c6db7b and final head9cec8482f2ecf978cf8bdb67b4c080b9dd74f5d6. This is not a new Lean run or PR merge; analytic estimates retain written-proof scope.
- [01: previous 75-page Gamma reader](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260915-quotient-moment-continuation/01_GAMMA_READER.pdf) is background, not the current 132-page account.

[Validation](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260915-quotient-moment-continuation/12_VALIDATION.md) records full independent proof and
receiving acceptance. The 132-page reader's body regions on pages6-111 match
the accepted predecessor pages5-110; pages1-5 and112-132 were individually
inspected, and all footer numbers checked. Receiver builds249/240 have
compilation-only status, not receiver-PDF visual approval. Exact diagnostics
retain their stated fixture scopes, not actual-period or actual-zero
evaluation. This source-sharing preparation performs no new mathematical,
PDF, source or archive audit and no Lean execution.

Only provenance account locators in the [source map](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260915-quotient-moment-continuation/11_SOURCE_MAP.json)
were transported for public sharing. Original map SHA-256:
4375c0cbad44222cdb690cf6ad6ff4335173e542bfb90688358c26528a2e0c7f.
Public map SHA-256:
3c1f19a98303915846e65260894348f7ad6290ae7c2e1a22a3b74ee38d065a6c.
777 literal historical private-account locator occurrences transported across739 values and8 path-valued keys, including nested JSON. Full mathematical bodies, original source hashes and other metadata remain unchanged. Original embedded identities still identify pre-transport sources. The other sixteen files are
byte-identical to the accepted delivery, including both PDFs and all eleven
TeX files. Every preceding sealed source package is retained.

The existing [DOI 10.5281/zenodo.22758970](https://doi.org/10.5281/zenodo.22758970) keeps its 58 downloads and
110-page PDF57 preview. This current GitHub packet is outside that frozen
edition; no Zenodo files change in this source-sharing transaction.

## Earlier source and edition guide (historical snapshot)

The following guide remains verbatim. Its prompts, reductions, receiver scopes
and next steps belong to preceding editions. The exact current prompt and
132-page paper above supersede that navigation without altering any preceding
source file.

# Split-Zero cohomology: exterior conductor control and four-endpoint determinants

[Start here: the exact current owner continuation](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/dad07e28faa735104ddc0b137521620fc315e6fc/workbenches/splitzero-tandem/continuations/20260914-exterior-kernel-continuation/00_CONTINUE_HERE.md).

[Read the current 110-page paper on GitHub](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/dad07e28faa735104ddc0b137521620fc315e6fc/workbenches/splitzero-tandem/continuations/20260914-exterior-kernel-continuation/15_CURRENT_MIXED_CONTROL_READER.pdf) · [Read its published PDF](https://zenodo.org/api/records/22758970/files/57-exterior-kernel-reader.pdf/content) · [Published DOI 10.5281/zenodo.22758970](https://doi.org/10.5281/zenodo.22758970).

- [110-page exterior kernel](https://zenodo.org/api/records/22758970/files/57-exterior-kernel-reader.pdf/content) · [complete editable source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/dad07e28faa735104ddc0b137521620fc315e6fc/workbenches/splitzero-tandem/continuations/20260914-exterior-kernel-continuation) · [offline source ZIP](https://zenodo.org/api/records/22758970/files/58-exterior-kernel-sources.zip/content).

The current 110-page reader adds the complete RUI/CEP exterior-conductor proofs to the original kernel, residue, finite-bound and minimum-section constructions. It proves a subleading o(kq) error for the actual conductor transport at each fixed period, all four original endpoints and all actual exterior ranks. The seventeen-file package preserves the sole owner prompt, complete updated receivers and recorded PR32 source/CI.

## What this calculation studies

Split-Zero follows a finite arithmetic quotient attached to a selected zeta-zero
packet, together with its original theta cohomology and mixed-support maps.
The specified period observation loses a subspace K. The calculation measures
that same kernel using the original fixed-Gamma, tensor-Gamma and arithmetic
source metrics at four degrees: q-1, q, 2q-1 and 2q. This is K at the specified
period, not an intersection over periods.

The purpose is to determine the kernel contribution to the original signed
cohomological return. An actual conductor polynomial gives a concrete map to
a smaller root grid. Earlier work constructed its inverse; this edition proves
that its four-endpoint determinant error is subleading. The remaining work is
now an explicit difference of original total determinants and an actual
residual observation determinant, not the older conductor-conditioning problem.

The main simple-quartet lane retains m=1, k=4l+1 with l>=1, q=(k+1)^2,
c=k/2, 0<delta<1/2 and gamma>2, on each original branch |u|>=R_*.
R_* is calculated from the actual quartet and full unit, and dim K=r=8k-16
on this domain. The all-multiplicity geometry and primary nilpotents remain
in the sources; this simple-quartet rank is not assigned to other multiplicities.
For k>=9, the actual conductor uses all 81 biform coefficients, its first
nonzero moment denominator and the exact lower grid. No generic period
matrix or assumed nonzero minor replaces those data.

## The completed conductor estimate

RUI uses the original finite conductor's determinant-one property. On the
degree-N source, its complementary exterior norms satisfy

    ||wedge^t T^(-1)|| = ||wedge^(N+1-t) T||
       <= [C_v exp(B_sh(H_N+2))]^(N+1-t),
    T = B_(N+1)(partial).

All coefficient constants and the moment denominator remain in this bound.
CEP extends it through the original endpoint maps, the exact low-degree
relation graph and all actual exterior ranks. The precise current identity is

    F_K^(s) = T_k^(s) - F_(Xi,k)^(s) + E_(A,k)^(s),
    |E_(A,k)^(s)| <= epsilon_k^(s) = 2 sum_N E_N^(s) = o(kq).

Here s remains the original source order 1 or k, and

    T_k^(s) = sum_N sigma_N
                 (log det G_N^(s) - log det G'_(N-v)^(s)),
    F_(Xi,k)^(s) = sum_N sigma_N log det Q_(Xi,N)^(s),
    N = q-1, q, 2q-1, 2q; sigma = (1, 1, -1, -1).

G and G' are the original upper- and lower-grid total Grams; Q_Xi is the
actual residual observation quotient Gram. The lower grid keeps
k'=k-8, q'=(k-7)^2, Delta=q-q'=16k-48, centre c'=c-4 and cutoffs N-v.
Its source order is still the original s. The retained map
Xi: V_A -> V_A/K has rank 8k-32. Its rank does not determine its volume:
the full graph, cross terms, coefficients and original action defect remain.

The estimate o(kq) holds for each fixed actual period, at all four original
endpoints and all actual exterior ranks. It sharpens the previous AIE
O(kq) exterior error **for this actual conductor transport**. AIE's finite
inverse and exact quotient maps remain valid. This is not a general
improvement for unrelated maps, nor a uniform bound for moving periods.

## What remains to calculate

The next two quantities are T_k^(s) and F_(Xi,k)^(s), in their displayed
original combination. Relative to the lower grid's natural endpoints,
the shifts are Delta-v at the lower pair and 2Delta-v at the upper pair.
The next total-Gram calculation must retain these shifts, roots, masses and
centres and control the first variation. The existing q^2 leading estimate
does not itself supply that error bound.

The other calculation is the actual rank-(8k-32) Xi observation determinant,
or equivalently its full low-degree graph quotient with cross terms.
No leading coefficient is inferred from rank alone. Bounds on the actual
period-dependent constants would be needed for a moving-period extension;
such uniformity is not claimed in this edition.

AKS's preceding bound retains its finite pointwise minimum with the original
KAF estimate and first actual increment:

    d_1^(s) <= F_K^(s)
       <= min(2r log Z_(k,1),
              r(L_(s,q)+L_(s,q+1)) - d_1^(s)),
    limsup F_K^a/(kq) <= 32 log(25 log 3/(4 pi))
                      < 25.02078097650.

Here L_(s,j) denotes AKS's actual finite covariance bound. The original
fixed-Gamma, tensor-Gamma and arithmetic ratios share limit points.
**No unique limit or exact leading value is asserted.** The original q^2
baseline and finite centre with its nonzero error radius remain intact.

The actual conductor error is now proved subleading. The next calculations are the shifted upper/lower total-Gram difference and the retained original rank-(8k-32) Xi observation determinant in F_K=T-F_Xi+E_A. No unique leading value, moving-period uniformity or RH conclusion is asserted; later CTV/Xi drafts are outside this edition.

## Complete proofs, receivers and checked-source scope

[File14: complete current proofs](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/dad07e28faa735104ddc0b137521620fc315e6fc/workbenches/splitzero-tandem/continuations/20260914-exterior-kernel-continuation/14_CURRENT_KERNEL_AND_MULTIPLICITY_PROOFS.tex) contains all preceding chapters
and the complete RUI1-15 and CEP1-49 proofs; it is the editable source of the
current 110-page reader. The source/remainder square, omitted-root products,
determinant phase, ideal map, low-degree graph and action defect are explicit.
[Arithmetic source transfer, file13](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/dad07e28faa735104ddc0b137521620fc315e6fc/workbenches/splitzero-tandem/continuations/20260914-exterior-kernel-continuation/13_ARITHMETIC_MIXED_TRANSFER.tex)
retains the finite errors, correlated arithmetic allowances and source maps.

[Joint receiver09](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/dad07e28faa735104ddc0b137521620fc315e6fc/workbenches/splitzero-tandem/continuations/20260914-exterior-kernel-continuation/09_UPDATED_JOINT_NOTE.tex) and
[signed receiver10](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/dad07e28faa735104ddc0b137521620fc315e6fc/workbenches/splitzero-tandem/continuations/20260914-exterior-kernel-continuation/10_UPDATED_SIGNED_RETURN.tex) retain all 31
preceding providers and the complete OCF/OKM/OKA/OMG/AKS/AKJ/AKP/AIE/RUI/CEP
proofs. Their current receiving sites are MRI4e-k and BRI6c-e; newly installed
MRI4g-k and BRI6e carry the refined intervals and exact signed consequences.
The original theta primitive and corrected minimum section remain intact.
The 226/218-page receiver builds establish compilation and source closure,
not visual approval of receiver PDFs.

The delivered reader's full 110 pages have the owner's visual acceptance:
93 page images match the accepted predecessor, four changed earlier pages
were inspected individually, and every new page98-110 was inspected
individually. The complete new written proofs and receiving changes have
independent acceptance. Finite diagnostic fixtures exercise their declared
endpoint shapes; they are not evaluations at actual zeta zeros or periods.

[File16: complete PR32 formal source and proofs](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/dad07e28faa735104ddc0b137521620fc315e6fc/workbenches/splitzero-tandem/continuations/20260914-exterior-kernel-continuation/16_PR32_FORMAL_SOURCE_AND_PROOFS.md)
is unchanged. It preserves four new Lean modules, the full note, runner and
recorded successful two-job CI at implementation
8e78bc7c240b04d297ade6afdadfd863e0c6db7b, with unchanged checked source at final
head9cec8482f2ecf978cf8bdb67b4c080b9dd74f5d6. Its receipt covers 33 local modules
and 56 selected transitive axiom targets. The new analytic estimates have
written-proof scope; no new local Lean run or PR merge is claimed here.

[Validation](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/dad07e28faa735104ddc0b137521620fc315e6fc/workbenches/splitzero-tandem/continuations/20260914-exterior-kernel-continuation/12_VALIDATION.md) records these exact scopes.
[Source map](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/dad07e28faa735104ddc0b137521620fc315e6fc/workbenches/splitzero-tandem/continuations/20260914-exterior-kernel-continuation/11_SOURCE_MAP.json) distinguishes owner-original
SHA-256 `242ff297064007ffdb435cd36f6c0884e2a50bc58797237a0840428b37b829f1` from public transported SHA-256
`269397ca3e92a083c451cb9016cd9ccbcb1f769a455f057e3138611d547ed79c`. Its metadata-only transport scope is:
735 literal private-account locator occurrences transported across 698 values and eight path-valued review keys, including nested JSON. Full mathematical bodies, source hashes and other metadata stay unchanged; embedded original identities still identify the original sources. The other sixteen files are unchanged.

This is exactly the accepted seventeen-file edition and the sole current
owner prompt. No competing prompt is created. Later CTV/Xi drafts are not
included. Earlier 97-page, 72-page and Gamma editions remain immutable
historical sources, rather than the current next-calculation statement.

## Earlier complete source editions

- [Earlier conductor kernel continuation source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/41adc412ceb119ad9086b1f106e377f3de2d401a/workbenches/splitzero-tandem/continuations/20260914-conductor-kernel-continuation).
- [Earlier original kernel matrices source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/5817ef9027257375b6ff3de7048b3331077251e7/workbenches/splitzero-tandem/continuations/20260914-original-kernel-matrices).
- [Earlier original volumes source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/1c8ec52c85c173adc9f8403a8a26914955e2f5a9/workbenches/splitzero-tandem/continuations/20260914-original-volumes).
- [Earlier gamma growth source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/41f020e0475429943252e69a1b4edd849393c780/workbenches/splitzero-tandem/continuations/20260914-gamma-growth).
- [Earlier joint gamma schur source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/2be3b23974bf040f4ea06240b8a4b85372f7c71d/workbenches/splitzero-tandem/continuations/20260914-joint-gamma-schur).
- [Earlier original relation bulk source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/01fc8820e3a3ea69afa22b8ab1b0b5ca61869456/workbenches/splitzero-tandem/continuations/20260914-original-relation-bulk).
- [Earlier complete gamma return source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/01fc8820e3a3ea69afa22b8ab1b0b5ca61869456/workbenches/splitzero-tandem/continuations/20260914-complete-gamma-return).

The [earlier 56-download edition](https://doi.org/10.5281/zenodo.22758735) remains frozen
with its 97-page preview. This edition adds PDF57 and ZIP58. The actual
new browser preview is the current 110-page PDF57; ZIP58 supplies all seventeen
flat source files for offline use, not a substitute preview. Every earlier
mathematical/source file remains unchanged.

[All 58 downloads and source identities](calculation_edition_20260915_exterior_kernel/README.md).

## Earlier source and edition guide (historical snapshot)

The following guide is retained verbatim from the preceding source/publication
state. Its current-reader and next-calculation statements apply to its explicit
edition, not this new 58-download reading route. In particular, the preceding
97-page AIE O(kq) exterior bound is now sharpened to o(kq) for the actual
fixed-period conductor transport at all four endpoints; its original finite
maps remain valid. This does not assert the same refinement for other maps.
Earlier prompts, source identities, mathematical bodies and proof/CI scopes
remain as provenance.

# Split-Zero cohomology: exterior conductor control and four-endpoint determinants

[Start here: the current continuation](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260914-exterior-kernel-continuation/00_CONTINUE_HERE.md).

[Read the current 110-page paper](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260914-exterior-kernel-continuation/15_CURRENT_MIXED_CONTROL_READER.pdf) · [Complete editable proof source](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260914-exterior-kernel-continuation/14_CURRENT_KERNEL_AND_MULTIPLICITY_PROOFS.tex).

This seventeen-file package continues the calculation of the original
arithmetic theta source, its cohomological quotient and the actual period/unit
observation. The immediate subject is the volume of its common kernel in
the original four-endpoint metrics. The Deligne mixed-cohomology programme
remains the research direction; these calculations assert no RH conclusion.

The prompt is the owner's single exact continuation. All eleven LaTeX files
retain their complete mathematical proof inputs inline. File16 retains the
complete PR32 formal source, written proofs and reported existing CI.
No archive or missing local TeX provider folder must be unpacked.

## Original kernel and its source metrics

Lambda_k is the tensor-degree-k period/unit-jet observation at the specified
actual period. K is its kernel, shared by the three original source metrics,
not an intersection over different periods. B_k is its image. The source
metrics are fixed Gamma, tensor Gamma and arithmetic; their masses, full
unit values, phases, period branches and action defects remain.

The signed kernel volume is

    F_K^(s) = log det H_0^(s) + log det H_1^(s)
              - log det H_q^(s) - log det H_(q+1)^(s).

Each H_j is the compressed covariance of the actual original kernel frame.
The four source degrees are N=q-1,q,2q-1,2q, with signs (1,1,-1,-1).
The Gamma orders remain s=1,k.

On the simple-quartet domain m=1, k=4l+1 with l>=1, q=(k+1)^2,
0<delta<1/2, gamma>2 and every original branch with |u|>=R_*,

    dim B_k = k^2 - 6k + 17,     r = dim K = 8k - 16.

R_* is calculated from the specified quartet and full unit. The conductor
reduction below uses k>=9. The separate all-multiplicity OCS/OMG maps retain
primary coordinates, multiplicities, factorials, nilpotents and actual
stabilizers; the displayed simple-quartet ranks are not assigned elsewhere.

## Completed exterior conductor control

RUI1-15 uses the actual determinant-one finite conductor and complementary
exterior powers. CEP1-49 carries that control through the exact source/remainder
square, high-cutoff correction, low-degree relation graph and original quotient
metrics at all four endpoints and all actual exterior ranks. It proves

    F_K^(s) = T_k^(s) - F_Xi,k^(s) + E_A,k^(s),
    |E_A,k^(s)| <= epsilon_k^(s) = 2 sum_N E_N^(s) = o(kq).

The small-error statement holds at each fixed actual period, in both unchanged
source orders s=1,k. Every displayed coefficient constant and moment denominator
is retained. This is the completed conductor error estimate; moving-period
uniformity is not asserted.

Here T_k is the signed upper-total minus shifted lower-total Gram determinant:

    T_k^(s) = sum_N sigma_N
              (log det G_N^(s) - log det G'_(N-v)^(s)),

and F_Xi,k is the signed volume of the actual residual observation quotient

    Xi : V_A -> V_A/K,     rank Xi = 8k - 32,
    F_Xi,k^(s) = sum_N sigma_N log det Q_Xi,N^(s).

The lower root grid has k'=k-8, q'=(k-7)^2, Delta=q-q'=16k-48,
centre c'=c-4, and cutoff N-v; v is the first nonzero conductor moment order.
The lower source keeps the original order s. The complete source/remainder
map, omitted-root products, determinant phase, ideal graph, Gram matrices and
actual action defect remain in CEP.

The preceding three source metrics differ by o(kq). Their retained common
limit-point ceiling is

    limsup F_K/(kq) <= 32 log(25 log 3/(4 pi)) < 25.02078097650,

approximately 25.02078097649. The finite first-increment and covariance bounds,
arithmetic correlations, boundary complements and signed return are retained;
a bound does not assign the leading value.

## Next: the exact shifted totals and residual quotient

The next calculation is T_k^(s)-F_Xi,k^(s) at scale kq. The lower grid's
natural endpoints are shifted by Delta-v at the two lower cutoffs and
2Delta-v at the two upper cutoffs. Retain these exact shifts, root polynomials,
source masses and centres when calculating the total determinant and its
first variation. An existing q^2 asymptotic does not itself supply the needed
first-variation error.

Calculate Xi from the actual period coefficients and residual observation
rows, or use its proved equivalent full graph quotient with all low-degree
cross terms. Its rank alone does not determine its volume. The conductor
error is already o(kq) at fixed period; the remaining exact determinants are
the current work. No unique limit, leading coefficient or moving-period
extension has been assigned. Later CTV/Xi drafts are separate and excluded
from this sealed edition.

## Full proofs, receivers and verification

- [14: current complete proofs](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260914-exterior-kernel-continuation/14_CURRENT_KERNEL_AND_MULTIPLICITY_PROOFS.tex) retains all preceding chapters and adds full RUI1-15 and CEP1-49, alongside AKS1-52, AKJ1-25, AKP1-10 and AIE1-29.
- [09: complete joint receiver](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260914-exterior-kernel-continuation/09_UPDATED_JOINT_NOTE.tex) and [10: complete signed-return receiver](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260914-exterior-kernel-continuation/10_UPDATED_SIGNED_RETURN.tex) retain every preceding full provider and add complete RUI/CEP. Their actual MRI4e-k and BRI6c-e sites carry the finite bounds, correlated arithmetic complements and signed consequences. The recorded edits reconstruct the preceding entire sealed receiver bodies.
- [13: arithmetic mixed transfer](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260914-exterior-kernel-continuation/13_ARITHMETIC_MIXED_TRANSFER.tex) retains the original source, complete correlated deficits and signed maps.
- [02: Gamma foundations](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260914-exterior-kernel-continuation/02_FULL_GAMMA_PROOFS.tex) and [03: observation foundations](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260914-exterior-kernel-continuation/03_FULL_OBSERVATION_PROOFS.tex) supply the full preceding dependencies; files04-08 retain the cyclic, period and original kernel calculations.
- [16: PR32 formal sources and written proofs](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260914-exterior-kernel-continuation/16_PR32_FORMAL_SOURCE_AND_PROOFS.md) preserves all four modules, full note, runner and existing verification record: implementation 8e78bc7c240b04d297ade6afdadfd863e0c6db7b, final head 9cec8482f2ecf978cf8bdb67b4c080b9dd74f5d6, recorded 33 modules and 56 selected transitive axiom reports. This is not a new Lean run or PR merge; analytic estimates retain written-proof scope.
- [01: previous 75-page Gamma reader](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260914-exterior-kernel-continuation/01_GAMMA_READER.pdf) is background, not the current 110-page account.

[Validation](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260914-exterior-kernel-continuation/12_VALIDATION.md) records independent acceptance of
the full proofs, receivers and continuation. For the 110-page reader, 93
page images match previously accepted pages; the four changed earlier pages
and all 13 new pages were individually inspected. Receiver builds at 226
and 218 pages have compilation-only status, not receiver-PDF visual approval.
The exact RUI/CEP diagnostics are finite fixtures, not actual zeta-zero or
period evaluations. This source transport reuses the owner team's accepted
scope without another proof audit, PDF build or Lean execution.

Only provenance account locators in the [source map](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260914-exterior-kernel-continuation/11_SOURCE_MAP.json)
were transported for public sharing. Original map SHA-256:
242ff297064007ffdb435cd36f6c0884e2a50bc58797237a0840428b37b829f1.
Public map SHA-256:
269397ca3e92a083c451cb9016cd9ccbcb1f769a455f057e3138611d547ed79c.
735 literal private-account locator occurrences transported across 698 values and eight path-valued review keys, including nested JSON. Full mathematical bodies, source hashes and other metadata stay unchanged; embedded original identities still identify the original sources. The other sixteen files are
byte-identical to the accepted delivery, including both PDFs and all eleven
TeX files. Previous sealed source packages remain intact.

The existing [DOI 10.5281/zenodo.22758735](https://doi.org/10.5281/zenodo.22758735) keeps its 56 downloads and
97-page PDF55 preview. This current GitHub packet is outside that frozen
edition; no Zenodo files change in this source-sharing transaction.

## Earlier source and edition guide (historical snapshot)

The following guide is retained verbatim. Its prompts, error estimates,
receiver scopes and next steps belong to preceding editions. The exact
current prompt and 110-page paper above supersede that navigation without
altering any preceding source file.

# Split-Zero cohomology: conductor inverses and four-endpoint kernel control

[Start here: the exact current owner continuation](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/41adc412ceb119ad9086b1f106e377f3de2d401a/workbenches/splitzero-tandem/continuations/20260914-conductor-kernel-continuation/00_CONTINUE_HERE.md).

[Read the current 97-page paper on GitHub](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/41adc412ceb119ad9086b1f106e377f3de2d401a/workbenches/splitzero-tandem/continuations/20260914-conductor-kernel-continuation/15_CURRENT_MIXED_CONTROL_READER.pdf) · [Read its published PDF](https://zenodo.org/api/records/22758735/files/55-conductor-kernel-reader.pdf/content) · [Published DOI 10.5281/zenodo.22758735](https://doi.org/10.5281/zenodo.22758735).

- [97-page conductor kernel](https://zenodo.org/api/records/22758735/files/55-conductor-kernel-reader.pdf/content) · [complete editable source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/41adc412ceb119ad9086b1f106e377f3de2d401a/workbenches/splitzero-tandem/continuations/20260914-conductor-kernel-continuation) · [offline source ZIP](https://zenodo.org/api/records/22758735/files/56-conductor-kernel-sources.zip/content).

The current 97-page reader contains complete original kernel, conductor, residue and minimum-section proofs, with the sharper finite four-endpoint control and its retained KAF minimum. The seventeen-file package includes the exact current owner prompt, complete updated receivers and the complete PR32 formal source with written proofs and observed CI records. Original source metrics, unit jets, periods and multiplicities remain.

## What this calculation studies

Split-Zero studies a finite arithmetic quotient built from a selected zeta-zero
packet, together with the original theta cohomology and mixed-support maps.
This calculation follows the part of that quotient lost by a specified period
observation. That part is its kernel K. The same K is measured using the original
fixed-Gamma, tensor-Gamma and arithmetic source metrics, at four source degrees
q-1, q, 2q-1 and 2q. It is the kernel at the given period, not an intersection
over different periods.

The purpose is to calculate that kernel's contribution to the original signed
cohomological return. A conductor polynomial supplies an explicit coefficient
map into the kernel calculation. Here its inverse, degree information and metric
bounds are worked out in full, then returned to the existing joint and signed
receivers. The next step remains the actual leading determinant value, not the
introduction of a different observation or an assumed RH counterexample.

For the main simple-quartet lane, the source retains m=1, k=4l+1 with l>=1,
q=(k+1)^2, c=k/2, 0<delta<1/2 and gamma>2, on every original period branch
|u|>=R_*. The radius R_* is calculated from the actual quartet and full unit.
The proved kernel dimension is r=8k-16 on this domain. The full
all-multiplicity geometry and primary nilpotents remain in the sources;
that simple-quartet rank is not assigned to other multiplicities.

## What is now completed

For each original source s, the four compressed source Grams are
H_j^(s)=T_s^* (K_j^(s))^(-1) T_s, with T_s=C_s^(-1) I_K.
Their signed logarithmic determinant combination is

    F_K^(s) = log det H_0^(s) + log det H_1^(s)
              - log det H_q^(s) - log det H_(q+1)^(s).

AKS retains the first actual increment d_1^(s), its finite covariance bounds
L_(s,j), and the finite pointwise minimum with the previous KAF estimate:

    d_1^(s) <= F_K^(s)
       <= min(2r log Z_(k,1),
              r(L_(s,q)+L_(s,q+1)) - d_1^(s)).

The original fixed-Gamma, tensor-Gamma and arithmetic ratios have common limit
points and the sharper uniform upper ceiling

    limsup F_K^a/(kq) <= 32 log(25 log 3/(4 pi))
                      < 25.02078097650.

The complete original finite estimate is retained, not replaced by its
asymptotic ceiling. **No unique limit or exact leading value is asserted.**

AKJ proves the exact passage between the projector determinant and the
original conductor-frame determinant, including its endpoint-independent
denominator. It gives the residue inverse in the actual i^D D! primary
coefficients, the invisible primary ideals and the inclusion into K.
For k>=9, its conductor degree flag has O(k^2) deficit. All 81 actual biform
coefficients and the first nonzero moment denominator are retained.

AKP proves the theta primitive correction when changing a polynomial lift,
and the full corrected minimum-section/residual-Gram map. AIE gives a literal
finite conductor inverse, its actual coefficient-dependent norm, the
low-degree correction and exact quotient/exterior transfer. Its fixed-period
operator-log bound is O(q); exterior power keeps its rank multiplier and gives
O(kq), not a smaller volume error.

The finite inverse acts on coefficient representatives D<=q-1. At the larger
source endpoints, the same coefficient frame uses the original minimum-remainder
Gram G_N. The inverse bound does not silently substitute the source cutoff N
for the coefficient cutoff D. Original Gamma orders stay 1 and k, and source
masses, unit jets, phases, periods and all four endpoint roles remain explicit.

The conductor inverse and finite four-endpoint bounds are completed. Their operator-log O(q) estimate has a rank factor in the exterior metric, leaving O(kq) volume loss. The next calculation is the fixed-period leading common-kernel determinant in its original four minimum-remainder Grams. No unique limit, exact leading value or RH conclusion is asserted.

## Complete proofs, receiving maps and checked-source scope

[File14: complete current proofs](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/41adc412ceb119ad9086b1f106e377f3de2d401a/workbenches/splitzero-tandem/continuations/20260914-conductor-kernel-continuation/14_CURRENT_KERNEL_AND_MULTIPLICITY_PROOFS.tex) contains all thirteen preceding
chapters and the full AKS, AKJ, AKP and AIE developments; it is the editable
source of the current 97-page reader. [Arithmetic source transfer, file13](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/41adc412ceb119ad9086b1f106e377f3de2d401a/workbenches/splitzero-tandem/continuations/20260914-conductor-kernel-continuation/13_ARITHMETIC_MIXED_TRANSFER.tex)
retains the signed finite errors and source-comparison maps.
[Joint receiver09](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/41adc412ceb119ad9086b1f106e377f3de2d401a/workbenches/splitzero-tandem/continuations/20260914-conductor-kernel-continuation/09_UPDATED_JOINT_NOTE.tex) and
[signed receiver10](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/41adc412ceb119ad9086b1f106e377f3de2d401a/workbenches/splitzero-tandem/continuations/20260914-conductor-kernel-continuation/10_UPDATED_SIGNED_RETURN.tex) retain all 31
preceding full providers and append the complete OCF/OKM/OKA/OMG/AKS/AKJ/AKP/AIE
proofs. MRI4e-f and BRI6c-d now contain the new finite bounds, correlated
arithmetic complements and signed consequences. The 211/203-page receiver
builds establish source closure and compilation, not visual approval of new
receiver PDFs. All 97 pages of the delivered current reader have the owner's
complete visual acceptance.

[File16: complete PR32 formal source and proofs](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/41adc412ceb119ad9086b1f106e377f3de2d401a/workbenches/splitzero-tandem/continuations/20260914-conductor-kernel-continuation/16_PR32_FORMAL_SOURCE_AND_PROOFS.md)
contains the four new Lean modules, full written note, runner and recorded CI.
The recorded strict implementation is
8e78bc7c240b04d297ade6afdadfd863e0c6db7b; final documentation/source head
9cec8482f2ecf978cf8bdb67b4c080b9dd74f5d6 changes no checked Lean, runner, test
or workflow source. Both observed CI jobs passed, covering 33 local modules
and 56 selected transitive axiom reports. The finite section, residual Gram,
observed iterates and residue-annihilator statements have that checked scope.
The analytic estimates and polynomial-gcd dimension result retain written-proof
scope. No new local Lean run, actual zeta-zero evaluation or PR merge is claimed.

[Validation](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/41adc412ceb119ad9086b1f106e377f3de2d401a/workbenches/splitzero-tandem/continuations/20260914-conductor-kernel-continuation/12_VALIDATION.md) records these exact scopes.
[Source map](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/41adc412ceb119ad9086b1f106e377f3de2d401a/workbenches/splitzero-tandem/continuations/20260914-conductor-kernel-continuation/11_SOURCE_MAP.json) distinguishes owner-original
SHA-256 `cb9f2fb6ef611445529f7cb067d1cbec6a2edd60eb9f1b893e750787049b44c8` from public transported SHA-256
`2f774ae49790357ea1306254d1837937c6f4386d9e571c61789aaa8f347d1cd6`. Its metadata-only transport scope is:
722 literal private-account locator occurrences transported across 685 values and eight path-valued review keys, including nested JSON. Full mathematical bodies, source hashes and other metadata stay unchanged; embedded original identities still identify the original sources. The other sixteen files are unchanged.

This is exactly the accepted seventeen-file source edition. Its single current
prompt belongs to the mathematical owner; this index creates no competing
continuation prompt. The earlier sixteen-file edition, 72-page reader and
preceding Gamma reader remain intact as historical sources.

## Earlier complete source editions

- [Earlier original kernel matrices source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/5817ef9027257375b6ff3de7048b3331077251e7/workbenches/splitzero-tandem/continuations/20260914-original-kernel-matrices).
- [Earlier original volumes source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/1c8ec52c85c173adc9f8403a8a26914955e2f5a9/workbenches/splitzero-tandem/continuations/20260914-original-volumes).
- [Earlier gamma growth source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/41f020e0475429943252e69a1b4edd849393c780/workbenches/splitzero-tandem/continuations/20260914-gamma-growth).
- [Earlier joint gamma schur source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/2be3b23974bf040f4ea06240b8a4b85372f7c71d/workbenches/splitzero-tandem/continuations/20260914-joint-gamma-schur).
- [Earlier original relation bulk source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/01fc8820e3a3ea69afa22b8ab1b0b5ca61869456/workbenches/splitzero-tandem/continuations/20260914-original-relation-bulk).
- [Earlier complete gamma return source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/01fc8820e3a3ea69afa22b8ab1b0b5ca61869456/workbenches/splitzero-tandem/continuations/20260914-complete-gamma-return).

The [earlier 54-download edition](https://doi.org/10.5281/zenodo.22758480) remains frozen
with its 72-page preview. This edition adds PDF55 and ZIP56; the actual new
browser preview is the current 97-page PDF55. ZIP56 supplies all seventeen
flat source files for offline use, not a substitute preview. Every earlier
mathematical/source file remains unchanged.

[All 56 downloads and source identities](calculation_edition_20260914_conductor_kernel/README.md).

## Earlier source and edition guide (historical snapshot)

The following guide is retained verbatim from the preceding source/publication
state. Its current-reader and next-calculation statements apply to its explicit
edition, not this new 56-download reading route. The conductor inverse and
sharper finite kernel controls are now complete; the fixed-period leading
common-kernel determinant is the next calculation. Earlier prompts, source-map
identities, mathematical bodies and proof/CI scopes remain as provenance.

# Split-Zero cohomology: conductor kernel and sharpened arithmetic control

[Start here: the current continuation](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260914-conductor-kernel-continuation/00_CONTINUE_HERE.md).

[Read the current 97-page paper](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260914-conductor-kernel-continuation/15_CURRENT_MIXED_CONTROL_READER.pdf) · [Complete editable proof source](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260914-conductor-kernel-continuation/14_CURRENT_KERNEL_AND_MULTIPLICITY_PROOFS.tex).

This seventeen-file package continues the Split-Zero programme's calculation
of the original arithmetic theta source, its cohomological quotient and the
actual period/unit observation. Its immediate subject is the metric volume
of the common kernel. The Deligne mixed-cohomology programme remains the
research direction; no RH conclusion follows from these calculations.

The prompt is the owner's single exact continuation. All eleven LaTeX files
are directly available with their mathematical proof inputs inline. File16
also supplies the complete PR32 contribution with its source and verification
record. No archive or missing local TeX provider folder must be unpacked.

## The object being calculated

Lambda_k is the specified tensor-degree-k period/unit-jet observation.
Its kernel K consists of the vectors killed at the specified period; it is
not an intersection over different periods. B_k is its image. The three
source metrics are the original fixed Gamma, tensor Gamma and arithmetic
metrics. Their common kernel volume is the signed four-endpoint expression

    F_K = log det H_0 + log det H_1 - log det H_q - log det H_(q+1),

where each compressed covariance H_j is formed from the actual original
kernel frame and source metric. Its four source degrees are q-1, q, 2q-1, 2q.
The full masses, unit values, phases, period branches, action defects and
minimum-section corrections remain in those matrices.

On the simple-quartet domain m=1, k=4l+1 with l>=1, q=(k+1)^2,
0<delta<1/2, gamma>2, and every original branch with |u|>=R_*, the completed
rank calculation gives

    dim B_k = k^2 - 6k + 17,     r = dim K = 8k - 16.

Here R_* is calculated from the specified quartet and full unit. The
canonical Gamma orders remain s=1,k. These ranks are not assigned to other
multiplicities or period domains. The all-multiplicity OCS/OMG maps retain
their primary coordinates, multiplicities, factorials, nilpotents and actual
stabilizers.

## Completed controls and the next determinant

The three original kernel metrics differ by o(kq), so their scaled values
have common limit points. AKS sharpens the completed O(kq) estimate to

    0 <= liminf F_K/(kq) <= limsup F_K/(kq)
       <= 32 log(25 log 3/(4 pi)) < 25.02078097650.

The ceiling is approximately 25.02078097649. The exact first compressed
increment, finite covariance bounds, correlated arithmetic intervals and
boundary complement remain; the preceding KAF estimate is still a valid
term in the pointwise minimum.

AKJ identifies the projector and original conductor-frame determinants with
their precise endpoint-independent denominator. Its residue inverse retains
every actual primary coefficient; it computes the permanently invisible
primary ideals, the finite conductor inverse, the degree flag and the
residual observation rows. Detection by all iterates does not by itself
evaluate the one-step kernel volume.

AKP supplies the actual theta primitive and corrected minimum section. For
an entire column family X, its kernel residual is X-S_G Lambda X and its
full Gram is X* G X - (Lambda X)* Q_G (Lambda X). The fixed-section correction
and ordered determinant denominator remain in the calculation.

AIE gives the literal finite reciprocal-symbol inverse, the actual
coefficient-dependent operator bound, low-degree correction and the full
quotient/exterior transfer. Its operator logarithm is O(q) at a fixed period,
but exterior volume retains the rank multiplier r, giving O(kq). This is
not a proved o(kq) determinant error. The finite inverse applies to coefficient
degree D<=q-1; that cutoff must not be replaced by a larger source endpoint.

The next calculation is the **fixed-period leading value of the common
kernel F_K/(kq)** from the actual conductor and full residual observation
matrix, using their original minimum-remainder Grams at all four source
degrees. A unique limit and its value remain unassigned. Any extension to
moving periods requires its own exact control.

## Full proofs, receivers and formal sources

- [14: current complete proofs](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260914-conductor-kernel-continuation/14_CURRENT_KERNEL_AND_MULTIPLICITY_PROOFS.tex) retains the thirteen preceding full chapters and adds complete AKS1-52, AKJ1-25, AKP1-10 and AIE1-29.
- [13: arithmetic mixed transfer](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260914-conductor-kernel-continuation/13_ARITHMETIC_MIXED_TRANSFER.tex) retains the full original source and correlated deficits.
- [09: complete joint receiver](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260914-conductor-kernel-continuation/09_UPDATED_JOINT_NOTE.tex) and [10: complete signed-return receiver](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260914-conductor-kernel-continuation/10_UPDATED_SIGNED_RETURN.tex) contain the current MRI4e-f and BRI6c-d intervals and signed consequences. Both retain all 31 earlier full providers and append full OCF/OKM/OKA/OMG/AKS/AKJ/AKP/AIE bodies. The receiving edits are reversible.
- [16: PR32 formal sources and written proofs](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260914-conductor-kernel-continuation/16_PR32_FORMAL_SOURCE_AND_PROOFS.md) supplies all four new Lean modules, the full research note, runner and observed verification record. The implementation is pinned at 8e78bc7c240b04d297ade6afdadfd863e0c6db7b; final documentation/source head is 9cec8482f2ecf978cf8bdb67b4c080b9dd74f5d6. Both jobs were observed successful by the owner. This is reported existing CI, not a new Lean run or merge; the analytic asymptotic and polynomial-gcd dimension statements retain written-proof scope.
- [02: Gamma foundations](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260914-conductor-kernel-continuation/02_FULL_GAMMA_PROOFS.tex) and [03: observation foundations](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260914-conductor-kernel-continuation/03_FULL_OBSERVATION_PROOFS.tex) retain the complete earlier dependencies. Files04-08 retain the preceding cyclic, period and kernel calculations.
- [01: previous 75-page Gamma reader](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260914-conductor-kernel-continuation/01_GAMMA_READER.pdf) remains background, not the current 97-page account.

[Validation](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260914-conductor-kernel-continuation/12_VALIDATION.md) records completed owner and independent
proof review and visual inspection of all 97 reader pages. The complete
receivers built at 211 and 203 pages; those builds establish closure and
compilability, not visual approval of receiver PDFs. This publication-side
transport reuses those acceptances without another mathematical audit,
PDF build or Lean execution.

Only provenance account locators in the [source map](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260914-conductor-kernel-continuation/11_SOURCE_MAP.json)
were transported for public sharing. Original map SHA-256:
cb9f2fb6ef611445529f7cb067d1cbec6a2edd60eb9f1b893e750787049b44c8.
Public map SHA-256:
2f774ae49790357ea1306254d1837937c6f4386d9e571c61789aaa8f347d1cd6.
722 literal private-account locator occurrences transported across 685 values and eight path-valued review keys, including nested JSON. Full mathematical bodies, source hashes and other metadata stay unchanged; embedded original identities still identify the original sources. The other sixteen files are
byte-identical to the accepted delivery, including both PDFs, all eleven
TeX sources and the PR32 source/proof record.

The existing [DOI 10.5281/zenodo.22758480](https://doi.org/10.5281/zenodo.22758480) keeps its 54 downloads and
72-page PDF53 preview. This current GitHub packet is outside that frozen
edition; no Zenodo files change in this source-sharing transaction.

## Earlier source and edition guide (historical snapshot)

The following guide is retained verbatim. Its prompts, bounds, receiver
scopes and next-step descriptions belong to preceding editions. The exact
current prompt and 97-page paper above supersede that navigation without
altering any preceding source file.

# Split-Zero cohomology: original kernel matrices and bounded arithmetic control

[Start here: the exact current owner continuation](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/5817ef9027257375b6ff3de7048b3331077251e7/workbenches/splitzero-tandem/continuations/20260914-original-kernel-matrices/00_CONTINUE_HERE.md).

[Read the current 72-page paper on GitHub](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/5817ef9027257375b6ff3de7048b3331077251e7/workbenches/splitzero-tandem/continuations/20260914-original-kernel-matrices/15_CURRENT_MIXED_CONTROL_READER.pdf) · [Read its published PDF](https://zenodo.org/api/records/22758480/files/53-original-kernel-matrices-reader.pdf/content) · [Published DOI 10.5281/zenodo.22758480](https://doi.org/10.5281/zenodo.22758480).

- [72-page original kernel matrices](https://zenodo.org/api/records/22758480/files/53-original-kernel-matrices-reader.pdf/content) · [complete editable source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/5817ef9027257375b6ff3de7048b3331077251e7/workbenches/splitzero-tandem/continuations/20260914-original-kernel-matrices) · [offline source ZIP](https://zenodo.org/api/records/22758480/files/54-original-kernel-matrices-sources.zip/content).

The current 72-page reader contains thirteen complete proof chapters. KAF proves the absolute O(kq) original kernel bound; OCF/OKM/OKA give its actual finite frame, all four endpoint source metrics and action defect. OMG retains the full multiplicity geometry, source-dual maps and nilpotents. The sixteen-file package includes the exact current owner prompt and complete receivers updated through KAF.

The original observation Lambda retains the actual unit jets, periods, cyclic
average, tensor coordinates and primary nilpotents. Its kernel is the lost
part of this specified observation at the given period, not an intersection
over different periods. The source metrics and four endpoints stay attached
to that same kernel and its explicit action defect.

The principal volume conclusion is for m=1, k=4l+1 with l>=1, q=(k+1)^2,
0<delta<1/2 and gamma>2, on the original period domain |u|>=R_* and every
original logarithm branch. RPC calculates R_* from the actual quartet and
unit values. The proved five-orbit rank gives dim ker Lambda=8k-16 there.
All-multiplicity OMG maps, nilpotents and source-dual geometry remain in the
sources; this m=1 rank is not assigned to other multiplicities or period cases.

The absolute original kernel bound is now O(kq), uniformly on that domain:

    0 <= liminf F_K^a/(kq) <= limsup F_K^a/(kq) <= 16(4+10 log 2),
    a in {fixed Gamma, tensor Gamma, arithmetic}.

KAF retains the complete finite factorial bound and the arithmetic deficit
cap. AMT retains the signed finite source-comparison errors; the Gamma
difference is O_h(k^2 log(q+1))=o(kq), and the arithmetic/fixed-Gamma
difference is O_h(k^2)=o(kq). Consequently the three bounded ratios have the
same limit points along each allowed sequence. **No unique limit or exact
leading value is asserted.**

OCF/OKM/OKA construct the actual finite conductor and invariant coefficient
matrices, all pivot charts, the ordinary-transpose primal kernel frame,
conjugated Hermitian source metrics and complete action defect. The finite
four-endpoint determinant is supplied, not deferred to a proposed frame.
The canonical source orders stay s=1,k; the independent K=q+1 comparison
remains exploratory. Source masses and metric frame factors are retained
until their proved signed cancellations.

The finite frame and O(kq) bound are completed. The next calculation is the actual leading value of the common original kernel contribution F_K/(kq), with the original period dependence retained. The bounded ratios share limit points but no unique limit is asserted. The m=1 rank and volume domain is not assigned to higher multiplicities; later AKS/AKJ work is outside this edition.

## Complete current proofs and receivers

[File14: all thirteen current proof chapters](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/5817ef9027257375b6ff3de7048b3331077251e7/workbenches/splitzero-tandem/continuations/20260914-original-kernel-matrices/14_CURRENT_KERNEL_AND_MULTIPLICITY_PROOFS.tex) is the complete
editable source of the current 72-page reader. [File13: AMT source transfer](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/5817ef9027257375b6ff3de7048b3331077251e7/workbenches/splitzero-tandem/continuations/20260914-original-kernel-matrices/13_ARITHMETIC_MIXED_TRANSFER.tex)
supplies its complete finite source comparisons. [Current joint receiver09](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/5817ef9027257375b6ff3de7048b3331077251e7/workbenches/splitzero-tandem/continuations/20260914-original-kernel-matrices/09_UPDATED_JOINT_NOTE.tex)
and [current signed receiver10](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/5817ef9027257375b6ff3de7048b3331077251e7/workbenches/splitzero-tandem/continuations/20260914-original-kernel-matrices/10_UPDATED_SIGNED_RETURN.tex) are
now complete successors **through KAF**, with all31 provider bodies inlined
in each. Their 162/156-page source builds establish compilation and closure,
not visual review of new receiver PDFs. The current reader's 72 actual pages
have the owner's existing complete visual acceptance.

[Validation](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/5817ef9027257375b6ff3de7048b3331077251e7/workbenches/splitzero-tandem/continuations/20260914-original-kernel-matrices/12_VALIDATION.md) states those exact scopes.
[Source map](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/5817ef9027257375b6ff3de7048b3331077251e7/workbenches/splitzero-tandem/continuations/20260914-original-kernel-matrices/11_SOURCE_MAP.json) distinguishes owner-original
SHA-256 `bef0190adf4eb6638d76e85db79247f9602c737b97bf8dd1b342057e972f83bf` from public transported SHA-256
`91511a5af94f7f5fabdbaa479b9fff801c1b846839beeba07e2927e63b1114ed`. Its metadata-only transport scope is:
714 literal private-account locator occurrences transported across 677 values and eight path-valued review keys, including eight nested-JSON occurrences. All associated review content, proof bodies, formulae, numerical values and source hashes are unchanged. Embedded source hashes identify owner-original bytes, not the transported metadata. The other fifteen files are unchanged.

This is exactly the accepted sixteen-file source edition. Later AKS/AKJ
deliveries are not included or represented as accepted here. The single
current prompt belongs to the mathematical owner; this index creates no
competing continuation prompt. The prior fourteen-file prompt and original
75-page Gamma PDF remain historical sources, not the current reading route.

## Earlier complete source editions

- [Earlier original volumes source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/1c8ec52c85c173adc9f8403a8a26914955e2f5a9/workbenches/splitzero-tandem/continuations/20260914-original-volumes).
- [Earlier gamma growth source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/41f020e0475429943252e69a1b4edd849393c780/workbenches/splitzero-tandem/continuations/20260914-gamma-growth).
- [Earlier joint gamma schur source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/2be3b23974bf040f4ea06240b8a4b85372f7c71d/workbenches/splitzero-tandem/continuations/20260914-joint-gamma-schur).
- [Earlier original relation bulk source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/01fc8820e3a3ea69afa22b8ab1b0b5ca61869456/workbenches/splitzero-tandem/continuations/20260914-original-relation-bulk).
- [Earlier complete gamma return source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/01fc8820e3a3ea69afa22b8ab1b0b5ca61869456/workbenches/splitzero-tandem/continuations/20260914-complete-gamma-return).

The [earlier 52-download edition](https://doi.org/10.5281/zenodo.22757268) remains frozen
with its 75-page preview. This edition adds PDF53 and ZIP54; the actual new
browser preview is the current 72-page PDF53. ZIP54 supplies all sixteen
flat source files for offline use, not a substitute preview. Every earlier
mathematical/source file remains unchanged.

[All 54 downloads and source identities](calculation_edition_20260914_original_kernel_matrices/README.md).

## Earlier source and edition guide (historical snapshot)

The following guide is retained verbatim from the preceding source/publication
state. Its current-reader and next-calculation statements apply to its explicit
edition, not this new 54-download reading route. The O(kq) bound and exact finite
frame are now complete; the leading common-kernel value is the next calculation.
Earlier prompts, source-map identities, mathematical bodies and proof/CI scopes
remain as provenance and are not silently rewritten.

# Split-Zero cohomology: original kernel matrices and bounded control

[Start here: the current continuation](workbenches/splitzero-tandem/continuations/20260914-original-kernel-matrices/00_CONTINUE_HERE.md).

[Read the current 72-page paper](workbenches/splitzero-tandem/continuations/20260914-original-kernel-matrices/15_CURRENT_MIXED_CONTROL_READER.pdf) · [Complete editable proof source](workbenches/splitzero-tandem/continuations/20260914-original-kernel-matrices/14_CURRENT_KERNEL_AND_MULTIPLICITY_PROOFS.tex).

This sixteen-file package continues the Split-Zero programme's study of the
arithmetic theta source, its cohomological quotient and the actual period/unit
observation. The research direction is to calculate metric and action data
through those original maps, with the Deligne mixed-cohomology programme as
motivation. No RH conclusion follows from the calculations reported here.

The current prompt is the owner's exact continuation, not a new set of
instructions. All eleven LaTeX files are directly available with their proof
inputs inline; there is no archive or missing local provider folder to unpack.

## What is being calculated

Lambda_k is the specified tensor-degree-k period/unit-jet observation. Its
kernel is the subspace sent to zero by that observation; B_k is its image.
F_K is the signed kernel metric-volume combination at four source degrees
q-1, q, 2q-1 and 2q. Its matrices retain the original fixed Gamma, tensor Gamma
and arithmetic source metrics. Their masses, phases, period branches,
minimum-section corrections, primary nilpotents and action defects remain
in the complete proofs.

The simple-quartet calculation uses m=1, k=4l+1 with l>=1, q=(k+1)^2,
0<delta<1/2 and gamma>2. The finite R_* is calculated from the actual quartet
and unit values. For every original branch and |u|>=R_*, its period quadric
has five distinct cyclic orbit members and

    dim B_k = k^2 - 6k + 17,     dim ker Lambda_k = 8k - 16.

The canonical Gamma orders remain s=1,k. The older K=q+1 family is exploratory.
These rank statements are not extrapolated to other multiplicities or period
domains. The separate all-multiplicity geometry retains its original
Segre-Veronese ideal, period/unit map, graded source-dual algebra, nilpotents,
actual stabilizer and conductor degree 2(N-|H|), where N and H are the orbit
order and actual stabilizer specified in that proof.

## What is now complete, and what comes next

The three original kernel metrics differ by o(kq), with the full finite
signed arithmetic/Gamma comparisons retained. The new KAF calculation sharpens
the absolute bound to O(kq), and gives, on the stated domain, for each of the
fixed Gamma, tensor Gamma and arithmetic sources:

    0 <= liminf F_K/(kq) <= limsup F_K/(kq) <= 16(4+10 log 2).

The construction now supplies the fourteen-generator conductor recursion,
the exact 8k-16-dimensional kernel frame, every Christoffel-Darboux matrix
entry including confluent entries, the four endpoint determinant expression
and the full surviving action defect. These are completed inputs, not proposed
substitutes for the original observation.

The next calculation is the **actual leading value of the common kernel
F_K/(kq)** from those matrices. The completed source differences, O(kq) bound
and frame do not need to be rederived. A unique limit has not yet been proved
or assigned; the bound alone does not supply its value.

## Full proofs and receiving documents

- [14: current complete proofs](workbenches/splitzero-tandem/continuations/20260914-original-kernel-matrices/14_CURRENT_KERNEL_AND_MULTIPLICITY_PROOFS.tex) contains all thirteen reader chapters, including KAF, OCF, OKM, OKA and OMG.
- [13: arithmetic mixed transfer](workbenches/splitzero-tandem/continuations/20260914-original-kernel-matrices/13_ARITHMETIC_MIXED_TRANSFER.tex) retains the exact transported-kernel and minimum-lift maps and signed finite comparisons.
- [09: complete joint receiver](workbenches/splitzero-tandem/continuations/20260914-original-kernel-matrices/09_UPDATED_JOINT_NOTE.tex) and [10: complete signed-return receiver](workbenches/splitzero-tandem/continuations/20260914-original-kernel-matrices/10_UPDATED_SIGNED_RETURN.tex) now include the consequences through KAF. Each contains all 31 provider bodies at the original input locations, with reversible source transport.
- [02: full Gamma foundations](workbenches/splitzero-tandem/continuations/20260914-original-kernel-matrices/02_FULL_GAMMA_PROOFS.tex) and [03: full observation foundations](workbenches/splitzero-tandem/continuations/20260914-original-kernel-matrices/03_FULL_OBSERVATION_PROOFS.tex) retain the preceding analytic, arithmetic and observation proofs.
- Files04-08 retain the earlier cyclic-sector, orbit, period and mixed-control calculations; the exact current prompt maps their statements to the sharper results.
- [01: previous 75-page Gamma reader](workbenches/splitzero-tandem/continuations/20260914-original-kernel-matrices/01_GAMMA_READER.pdf) is retained as background, not as the current 72-page account.

[Validation](workbenches/splitzero-tandem/continuations/20260914-original-kernel-matrices/12_VALIDATION.md) and [source map](workbenches/splitzero-tandem/continuations/20260914-original-kernel-matrices/11_SOURCE_MAP.json)
record the completed owner and independent mathematical reviews and their
domains. All 72 pages of the current reader were visually inspected by that
team. The complete editable current reader builds to 72 pages; the two
receivers build to 162 and 156 pages. Those receiver builds establish source
closure and compilability, not visual approval of those longer PDFs.
Publication reuses these acceptances; it claims no new proof audit or Lean run.

Only provenance account locators in the source map were transported for public
sharing. Original map SHA-256:
`bef0190adf4eb6638d76e85db79247f9602c737b97bf8dd1b342057e972f83bf`.
Public map SHA-256:
`91511a5af94f7f5fabdbaa479b9fff801c1b846839beeba07e2927e63b1114ed`.
714 literal private-account locator occurrences transported across 677 values and eight path-valued review keys, including eight nested-JSON occurrences. All associated review content, proof bodies, formulae, numerical values and source hashes are unchanged. Embedded source hashes identify owner-original bytes, not the transported metadata. The other fifteen files are byte-identical
to the accepted owner delivery, including both PDFs and all eleven TeX sources.

The existing [DOI 10.5281/zenodo.22757268](https://doi.org/10.5281/zenodo.22757268) retains its 52 downloads and
75-page PDF51 preview. This successor is a current GitHub source-and-reader
package outside that frozen DOI edition; no Zenodo file changes here.

## Earlier source and edition guide (historical snapshot)

The following guide is retained verbatim. Its prompts, receiver scopes and
next-step descriptions belong to preceding editions. The current prompt and
72-page paper above supersede that navigation without altering earlier files.

# Split-Zero cohomology: original kernel control and source transport

[Start here: the owner's current continuation](workbenches/splitzero-tandem/continuations/20260914-original-kernel-web/00_CONTINUE_HERE.md).

[Latest arithmetic/Gamma transfer and completed kernel-difference calculation](workbenches/splitzero-tandem/continuations/20260914-original-kernel-web/13_ARITHMETIC_MIXED_TRANSFER.tex) · [Combined original mixed control](workbenches/splitzero-tandem/continuations/20260914-original-kernel-web/08_ORIGINAL_MIXED_CONTROL.tex).

This flat fourteen-file packet is the current editable research route. The
first link is the owner's exact single continuation prompt, not a newly
authored substitute. Its complete proof sources are directly available without
unpacking an archive. Earlier continuation prompts remain historical editions.

## What the original kernel and observation mean here

The observation Lambda_k is the actual original period/unit-jet map, with its
specified cyclic average, tensor image and primary nilpotents. The kernel is
the part lost by this observation. F_K and F_B are the associated original
kernel and boundary metric-volume quantities at the four endpoint degrees
q-1, q, 2q-1 and 2q. The source files retain the precise coefficient frames,
minimum-section corrections, metric determinants and source masses.

The fixed Gamma source, tensor Gamma source and arithmetic source keep their
own metrics and exact transport maps. Multiplication by the specified source
polynomial raises degree into its divisible-polynomial image; it is not
identified with the entire higher-degree source or assumed to preserve the
observation kernel. File13 proves the actual transported kernel, observation,
extra constraints and finite signed comparison bounds.

## Completed comparison and its exact domain

All-multiplicity OCS maps remain in the sources. The new explicit quadric-rank
and volume conclusions concern the simple quartet m=1, k=4l+1, q=(k+1)^2,
0<delta<1/2 and gamma>2. RPC supplies a finite R_* from the original quartet
and its actual amplitude. On every original logarithm branch, for |u|>=R_*,
the transformed quadric has five distinct cyclic orbit members and

    dim B_k = k^2 - 6k + 17,
    dim ker Lambda_k = 8k - 16.

These ranks are not assigned to higher primary multiplicities or other period
outcomes. The separately calculated invariant-quadric outcome retains its own
rank and test. The canonical Gamma orders remain s=1 and s=k; the earlier
independent K=q+1 family remains exploratory, not a replacement rule.

For the two Gamma sources, file13 proves the signed finite bounds for
Delta_K=F_K^(1)-F_K^(k), retaining all beta_k source masses before their four
signed copies cancel. It gives Delta_K=O(k^2 log q)=o(kq), uniformly on the
proved period domain. The actual arithmetic comparison also gives
F_K^ar-F_K^(1)=O_h(k^2), with its complete signed endpoint bounds retained.
Thus the three original kernel metrics differ by o(kq).

The exact boundary identity then yields

    (F_B^(1)-F_B^(k))/(kq) -> -C_Gamma/4,

and the actual arithmetic boundary has the same signed return relative to the
tensor-Gamma boundary through the original arithmetic transition. C_Gamma is
the positive equilibrium coefficient defined in the full Gamma sources.
The already proved q-squared limits remain F_K/q^2 -> 0 and F_B/q^2 -> C_B,
where C_B=9-8 log(2)+F(2,pi)>769/17010. These are the accepted source scopes,
not a new endpoint conclusion from this reading index.

The next calculation named by the owner is the **absolute common kernel
contribution at scale kq**, starting with F_K^(1)/(kq). The existing absolute
bound divided by kq still grows like log q. The source-difference estimate is
completed and is not being reissued as the next task. Period dependence,
uniformity domain and four endpoint determinants remain explicit.

## Where the complete results and receiver versions are

- [04: cyclic sectors and exact maps](workbenches/splitzero-tandem/continuations/20260914-original-kernel-web/04_CYCLIC_SECTORS.tex).
- [05: orbit alternatives, rank and invariant lifting](workbenches/splitzero-tandem/continuations/20260914-original-kernel-web/05_ORBIT_CONDUCTOR.tex).
- [06: actual period quadric and explicit orbit domain](workbenches/splitzero-tandem/continuations/20260914-original-kernel-web/06_ACTUAL_PERIOD_QUADRIC.tex).
- [07: original kernel-volume bounds](workbenches/splitzero-tandem/continuations/20260914-original-kernel-web/07_ORIGINAL_KERNEL_VOLUME_BOUND.tex).
- [08: combined leading mixed control](workbenches/splitzero-tandem/continuations/20260914-original-kernel-web/08_ORIGINAL_MIXED_CONTROL.tex).
- [13: later arithmetic transfer and kernel-difference result](workbenches/splitzero-tandem/continuations/20260914-original-kernel-web/13_ARITHMETIC_MIXED_TRANSFER.tex).
- [02: full Gamma foundations](workbenches/splitzero-tandem/continuations/20260914-original-kernel-web/02_FULL_GAMMA_PROOFS.tex) and [03: full observation foundations](workbenches/splitzero-tandem/continuations/20260914-original-kernel-web/03_FULL_OBSERVATION_PROOFS.tex).
- [09: joint receiver](workbenches/splitzero-tandem/continuations/20260914-original-kernel-web/09_UPDATED_JOINT_NOTE.tex) and [10: signed-return receiver](workbenches/splitzero-tandem/continuations/20260914-original-kernel-web/10_UPDATED_SIGNED_RETURN.tex) are complete successors updated through OPG/OPR. The subsequent refinements are in 04-08 and 13; their propagation through all receiver statements is not claimed to be complete.

[01: the previous 75-page Gamma reader](workbenches/splitzero-tandem/continuations/20260914-original-kernel-web/01_GAMMA_READER.pdf) is retained as a
historical reading copy. **It does not contain the newer results in 04-08 and
13.** [Validation scope](workbenches/splitzero-tandem/continuations/20260914-original-kernel-web/12_VALIDATION.md) records their source-only builds
and exact-source checks, not a new visual PDF review or new independent
mathematical audit. [Source map](workbenches/splitzero-tandem/continuations/20260914-original-kernel-web/11_SOURCE_MAP.json) retains original sources,
transports and attribution. The entire fourteen-file package remains flat.

Only the source map has a metadata-only privacy transport. Its owner-original
SHA-256 is `15d459e37007018d8d22007dd6483305f671bc88914cfa0e22d12ac007950eeb`; the public map
SHA-256 is `ae4d7ce31e63244c4297fa0477afb1c0236d17292662bb76cb8391d65d3c3b81`. The recorded scope
is: 502 exact private-account locator components transported; no keys, numerical values, proof bodies, formulae or source hashes changed. Embedded owner receipt hashes identify the original receipt bytes, not the transported metadata copy. The other thirteen files remain
byte-identical; the public map is not assigned its original file's hash.

The frozen [DOI 10.5281/zenodo.22757268](https://doi.org/10.5281/zenodo.22757268) still has exactly 52 downloads and
the original 75-page PDF51 preview. This new Git source packet is outside that
frozen edition; no Zenodo file or preview is changed here.

## Earlier source and edition guide (historical snapshot)

The following guide is retained verbatim from the preceding source/edition
state. Its continuation prompts and next-step statements describe those earlier
cuts. The current owner prompt above supersedes those prompts for this packet;
their exact source-time provenance and mathematical files remain unchanged.

# Split-Zero cohomology: original Gamma volumes and intrinsic spectral sums

[Read the 75-page Original Volumes paper](https://zenodo.org/api/records/22757268/files/51-original-gamma-volumes-reader.pdf/content) · [Published DOI 10.5281/zenodo.22757268](https://doi.org/10.5281/zenodo.22757268).

- [75-page original gamma volumes](https://zenodo.org/api/records/22757268/files/51-original-gamma-volumes-reader.pdf/content) · [complete editable source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/1c8ec52c85c173adc9f8403a8a26914955e2f5a9/workbenches/splitzero-tandem/continuations/20260914-original-volumes) · [offline source ZIP](https://zenodo.org/api/records/22757268/files/52-original-gamma-volumes-public-sources.zip/content).

The complete 75-page Original Volumes paper prints all fifteen providers in full: the original q-squared baseline, quantitative Gamma return, intrinsic full polynomial-times-Gamma density, exact endpoint masses and GMB original mixed-row map. Its complete source package additionally contains the separate full OPG/OPR original-observation continuation and the restored twelve-body dependency closure.

The paper retains the original packet, coordinate, roots, multiplicities,
dimensions and four endpoint roles. Here k=4l+1 is the tensor degree,
m is the primary multiplicity and `q=[1+k(m-1)](k+1)^2` is the finite cyclic
quotient dimension. The canonical Gamma source orders remain s=1 and s=k.
The independently proved K=q+1 family is exploratory, not a rule selecting
or replacing an order in the original construction.

The original fixed-source, tensor-source and arithmetic baseline has positive
q-squared coefficient C_B=9-8 log(2)+F(2,pi)>769/17010. The full Schur determinant
returns this to the combined original kernel/boundary volume; the individual
mixed terms are not separately assigned their sum's coefficient.

W is the original logarithmic Gamma determinant/product comparison. Its
quantitative return retains explicit asymmetric finite intervals and proves

    W = C_Gamma lq + O(l sqrt(q) + l^2),
    C_Gamma = 2 integral log(x) d rho_(2,pi)(x) - 4(2 log 2 - 1).

The complete preceding source defines the equilibrium density rho_(2,pi),
support and global minimizer. For fixed m>=2 the quantitative remainder is
o(q). At m=1 the actual finite centre is retained:

    (V^c-lq C_Gamma)/q -> partial_alpha L(2,pi)/8 - log(2)/4.

This centre is not set to zero. The actual centred quotient retains its proved
limsup radius A/sqrt(2), with the source's explicit L and A; no vanishing radius
is asserted. QRI9 retains the opposite sign to H and the arithmetic transition.

The intrinsic exterior/sum construction keeps the full polynomial-times-Gamma
density, coefficients, masses, centres and sum-fibre kernel. The exact endpoint
calculation identifies the exterior masses with original relation Grams. GMB
gives the original mixed-row and kernel maps with endpoint weights 1,2,...,2,1.
The full density is not replaced by its Gamma exponent alone.

## Complete editable continuation and source closure

[Original Observation Addendum (TeX)](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/1c8ec52c85c173adc9f8403a8a26914955e2f5a9/workbenches/splitzero-tandem/continuations/20260914-original-volumes/next_original_observation/Original_Observation_Addendum.tex) gives the complete OPG/OPR
continuation, actual period Gram matrices and section-corrected kernel formulas,
with its declared dependencies. It is **not inside the 75-page PDF**.
[The cumulative editable entry](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/1c8ec52c85c173adc9f8403a8a26914955e2f5a9/workbenches/splitzero-tandem/continuations/20260914-original-volumes/Cumulative_Original_Gamma_Proofs.tex) retains the complete preceding
proof closure. [Public source provenance](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/1c8ec52c85c173adc9f8403a8a26914955e2f5a9/workbenches/splitzero-tandem/continuations/20260914-original-volumes/PUBLIC_DERIVATION.json) records the twelve
complete dependency bodies restored here, including TW and FPK, which the
preceding sealed source package omitted. The older edition is unchanged;
its earlier completeness statements are not silently adopted for those omissions.

The original baseline and quantitative Gamma return are completed at their stated scales. The actual m=1 finite centre and nonzero limsup radius are retained. The next calculations concern the specified original period Grams, section-corrected kernel residuals and full polynomial-density contributions. Canonical orders remain s=1 and s=k; independent K=q+1 is exploratory, not an order-selection rule.

[The cut22 continuation prompt](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/1c8ec52c85c173adc9f8403a8a26914955e2f5a9/workbenches/splitzero-tandem/continuations/20260914-original-volumes/00_CONTINUE_THE_PROGRAMME.md) is preserved as that source
edition's exact provenance. This reading index does not issue a new or competing
continuation prompt; the mathematical owner maintains successor instructions.

## Earlier complete sources

- [Earlier gamma growth source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/41f020e0475429943252e69a1b4edd849393c780/workbenches/splitzero-tandem/continuations/20260914-gamma-growth).
- [Earlier joint gamma schur source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/2be3b23974bf040f4ea06240b8a4b85372f7c71d/workbenches/splitzero-tandem/continuations/20260914-joint-gamma-schur).
- [Earlier original relation bulk source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/01fc8820e3a3ea69afa22b8ab1b0b5ca61869456/workbenches/splitzero-tandem/continuations/20260914-original-relation-bulk).
- [Earlier complete gamma return source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/01fc8820e3a3ea69afa22b8ab1b0b5ca61869456/workbenches/splitzero-tandem/continuations/20260914-complete-gamma-return).

The [earlier 50-download edition](https://doi.org/10.5281/zenodo.22755297) remains frozen.
Its 37-, 15-, 33- and 46-page papers, the 1929-page compendium and complete source
snapshots retain their identities. This edition adds PDF51 and ZIP52; PDF51 is
the actual browser preview. ZIP52 is the complete offline source package,
including the separate source-only continuation, not a readable preview.

[All 52 downloads and source identities](calculation_edition_20260914_original_volumes/README.md).

## Earlier source and edition guide (historical snapshot)

The following guide is retained verbatim from before this DOI was issued.
References to current or front readers, exclusion from a frozen DOI and next
calculations describe their linked earlier source editions, including DOI
22755297, not the new 52-download edition above. The original baseline and
quantitative Gamma return are completed at the scopes stated above. Earlier
source-time proof/CI records and all mathematical bodies remain unchanged.

# Split-Zero cohomology: original Gamma volumes and intrinsic spectral sums

[Read the new 75-page Original Volumes paper](workbenches/splitzero-tandem/continuations/20260914-original-volumes/Original_Gamma_Volumes_and_Intrinsic_Spectral_Sums.pdf) · [Complete editable sources](workbenches/splitzero-tandem/continuations/20260914-original-volumes/README.md).

The paper prints all fifteen providers in full, retaining the original packet,
coordinate, roots, multiplicities, dimensions and four endpoint roles.
The original q-squared baseline and quantitative Gamma return are now evaluated;
the calculation proceeds to the actual original observation, rather than
repeating the leading Gamma-growth calculation.

Here k=4l+1 is the tensor degree, m is the primary multiplicity and
q=[1+k(m-1)](k+1)^2 is the finite cyclic quotient dimension. The canonical Gamma
source orders remain s=1 and s=k. The separately proved comparison family
K=q+1 is exploratory; it does not select or replace an order in the original
construction.

The fixed-source, tensor-source and arithmetic baseline has positive
q-squared coefficient C_B=9-8 log(2)+F(2,pi)>769/17010. The full Schur determinant
returns it to the combined original kernel/boundary volume; the coefficient is
not assigned separately to individual mixed terms.

For the original logarithmic Gamma comparison, the quantitative return gives

    W = C_Gamma lq + O(l sqrt(q) + l^2),

with explicit asymmetric finite intervals. For fixed m>=2 the remainder is
o(q). At m=1 the actual finite centre satisfies

    (V^c-lq C_Gamma)/q -> partial_alpha L(2,pi)/8 - log(2)/4.

This nonzero centre is retained. The actual centred quotient has proved
limsup radius A/sqrt(2), using the paper's explicit L and A; that radius is
not asserted to vanish. QRI9 carries the opposite sign to H and retains the
arithmetic transition scalar.

The intrinsic exterior/sum construction retains the full polynomial-times-Gamma
density, its coefficients, masses, centres and sum-fibre kernel. The endpoint
calculation identifies the exterior masses with original relation Grams.
GMB supplies the exact original mixed-row and kernel maps, including the
retained endpoint weights 1,2,...,2,1; a Gamma exponent alone is not substituted
for the complete density.

## Complete source-only continuation

[Original Observation Addendum (editable TeX)](workbenches/splitzero-tandem/continuations/20260914-original-volumes/next_original_observation/Original_Observation_Addendum.tex)
contains the complete OPG/OPR continuation and its dependency closure. It
computes actual observation columns, their coupled recurrence, the original
period Gram matrices and the section-corrected kernel residuals.
This addendum is **not inside the 75-page PDF** and is not advertised as a
second public PDF. [The cumulative editable entry](workbenches/splitzero-tandem/continuations/20260914-original-volumes/Cumulative_Original_Gamma_Proofs.tex)
also retains the complete preceding proof closure.

The complete source package retains the twelve restored full dependency
bodies, including TW and FPK, together with the restoration provenance.
These bodies are not replaced by excerpt summaries.

Next are quantitative bounds for the specified original period Grams and
their section-corrected kernel residuals, plus the full polynomial-density
contribution at ranks 0,1,q,q+1. The literal cyclic average, original period
matrix, full amplitude/Taylor unit and primary nilpotents remain attached
to these maps. No arbitrary projection, hand-selected order, vanishing
m=1 radius, completed endpoint conclusion or new Lean result is substituted.

This new source snapshot is **outside the frozen
[DOI 10.5281/zenodo.22755297](https://doi.org/10.5281/zenodo.22755297)**. That edition retains its 37-page preview
and all 50 downloads. Every earlier mathematical/source leaf and programme
entry remains unchanged; the new paper and complete addendum sources are added.

## Earlier source and edition guide (historical snapshot)

The following guide is retained verbatim from the earlier source/edition state.
Its baseline and finite-error tasks describe that earlier cut, not the
completed calculations above. Publication claims refer to their explicit
frozen editions. Older proof/CI scopes and exploratory comparisons retain
their source-time identities.

# Split-Zero cohomology: Gamma growth and arithmetic return

[Read the 37-page Gamma-growth paper](https://zenodo.org/api/records/22755297/files/49-gamma-growth-arithmetic-return-reader.pdf/content) · [Published DOI 10.5281/zenodo.22755297](https://doi.org/10.5281/zenodo.22755297).

- [37-page gamma growth arithmetic return](https://zenodo.org/api/records/22755297/files/49-gamma-growth-arithmetic-return-reader.pdf/content) · [complete editable source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/41f020e0475429943252e69a1b4edd849393c780/workbenches/splitzero-tandem/continuations/20260914-gamma-growth) · [offline source ZIP](https://zenodo.org/api/records/22755297/files/50-gamma-growth-public-sources.zip/content).

The complete 37-page Gamma-growth paper retains the earlier LET/PHT/HCT proofs and the new WGP/RWB/EIQ/GEL/WGR proofs. It proves finite bounds for the original Gamma comparison W, its positive leading equilibrium integral and its signed arithmetic return through the original maps.

Here k=4l+1 is the tensor degree, m is the primary multiplicity,
e=1+k(m-1), and q=e(k+1)^2=2n is the finite cyclic quotient dimension.
W_k is the original logarithmic Gamma determinant/product comparison.
Its finite bounds and leading growth are now proved:

    lq/64 <= W_k <= 6lq,
    W_k/(lq) -> C_Gamma > 0,
    C_Gamma = 2 integral log(x) d rho_(2,pi)(x) - 4(2 log 2 - 1).

The paper defines the exact equilibrium density rho_(2,pi), its unit mass,
support and global minimizer. It retains the source determinant integral,
the t=q^2 x coordinate map, every Jacobian and original arithmetic receiver.
In the original coordinates its signed return satisfies

    Delta_k^Gamma = -W_k + e_0 - e_q - e_(q+1) + delta_k^sigma,
    Delta_k^Gamma/(kq) -> -C_Gamma/4.

The leading W calculation is completed. The next calculations are the original baseline B_k^0 at its actual four degrees and the finite q-scale Gamma Hankel correction. The proved leading remainder is o(lq), not an o(q) Hankel remainder; no completed endpoint conclusion is asserted.

The original product also has a sharper signed expansion through the constant
scale. Its surviving terms and the original arithmetic allowances remain in
the next baseline and finite-q calculation; no leading W task is being repeated.

## Earlier complete sources

- [Earlier joint gamma schur source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/2be3b23974bf040f4ea06240b8a4b85372f7c71d/workbenches/splitzero-tandem/continuations/20260914-joint-gamma-schur).
- [Earlier original relation bulk source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/01fc8820e3a3ea69afa22b8ab1b0b5ca61869456/workbenches/splitzero-tandem/continuations/20260914-original-relation-bulk).
- [Earlier complete gamma return source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/01fc8820e3a3ea69afa22b8ab1b0b5ca61869456/workbenches/splitzero-tandem/continuations/20260914-complete-gamma-return).

The [earlier 48-download edition](https://doi.org/10.5281/zenodo.22754516) remains frozen.
Its 15-, 33- and 46-page papers and the 1929-page compendium remain unchanged.
This edition adds PDF49 and ZIP50; PDF49 is the actual browser preview.
ZIPs are complete offline sources, not readable previews.

[All 50 downloads and source identities](calculation_edition_20260914_gamma_growth/README.md).

## Earlier source and edition guide (historical snapshot)

The following guide is retained verbatim from before this DOI was issued.
References to “current”, “front” or exclusion from the frozen DOI describe
the explicitly linked earlier editions, including DOI 22754516, not the
new 50-download edition above. Older statements that leading W remains open
are historical: that calculation is proved in the 37-page paper. The original
baseline and finite q-scale remainder are the remaining calculations.
All mathematical bodies, source links, paper identities and proof/CI scopes
remain unchanged.

# Split-Zero cohomology: Gamma growth and arithmetic return

[Read the new 37-page Gamma growth paper](workbenches/splitzero-tandem/continuations/20260914-gamma-growth/Gamma_Growth_and_Arithmetic_Return.pdf) · [Complete editable sources](workbenches/splitzero-tandem/continuations/20260914-gamma-growth/README.md).

The leading Gamma calculation is now proved. The paper preserves the original
Gamma source, mass, four endpoint roles, primary multiplicities and exact
quotient/kernel/boundary maps. It includes the earlier complete LET/PHT/HCT
calculation and the new complete WGP/RWB/EIQ/GEL/WGR proofs.

Here k=4l+1 is the tensor degree, m is the primary multiplicity,
e=1+k(m-1), and q=e(k+1)^2=2n is the finite cyclic quotient dimension.
For original integers l,m at least one, the logarithmic Gamma comparison W_k
satisfies the exact finite bounds

    lq/64 <= W_k <= 6lq.

Its leading limit is proved, not merely observed:

    W_k/(lq) -> C_Gamma > 0,
    C_Gamma = 2 integral log(x) d rho_(2,pi)(x) - 4(2 log 2 - 1).

The paper gives the exact equilibrium density, mass and support and proves
the source determinant integral with its t=q^2 x coordinate map and Jacobian.
The signed Gamma contribution returns through the original arithmetic maps:

    Delta_k^Gamma = -W_k + e_0 - e_q - e_(q+1) + delta_k^sigma,
    Delta_k^Gamma/(kq) -> -C_Gamma/4.

The proved leading remainder is o(lq); an o(q) Hankel remainder is not claimed.
The original P product has a sharper signed expansion through the constant
scale. Next are the original baseline B_k^0 at its four actual degrees and the
finite q-scale Gamma correction, followed through the same arithmetic and
cohomology receiving maps. No completed endpoint conclusion or Lean result is
claimed by this source update.

This complete new source snapshot is **outside the frozen
[DOI 10.5281/zenodo.22754516](https://doi.org/10.5281/zenodo.22754516)**. That edition retains its 15-page preview
and all 48 downloads. The 15-, 33-, 46- and 1,929-page papers and their source
trees remain unchanged; the new 37-page paper is added, not substituted for them.

## Earlier source and edition guide (historical snapshot)

The following guide is preserved verbatim from before the Gamma-growth result.
Its statements that leading W remains open describe the earlier source cut,
not the completed calculation above. Earlier “current” publication claims
refer to their explicitly linked frozen editions. All existing programme
entries and proof/CI scopes retain their source-time identities.

# Split-Zero cohomology: complete Gamma return and original relation bounds

[Read the 15-page complete Gamma return](https://zenodo.org/api/records/22754516/files/47-complete-gamma-return-reader.pdf/content) · [Published DOI 10.5281/zenodo.22754516](https://doi.org/10.5281/zenodo.22754516).

- [15-page complete gamma return](https://zenodo.org/api/records/22754516/files/47-complete-gamma-return-reader.pdf/content) · [complete editable source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/01fc8820e3a3ea69afa22b8ab1b0b5ca61869456/workbenches/splitzero-tandem/continuations/20260914-complete-gamma-return) · [offline source ZIP](https://zenodo.org/api/records/22754516/files/48-complete-gamma-return-public-sources.zip/content).
- [33-page original relation bulk](https://zenodo.org/api/records/22754516/files/45-original-relation-bulk-reader.pdf/content) · [complete editable source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/01fc8820e3a3ea69afa22b8ab1b0b5ca61869456/workbenches/splitzero-tandem/continuations/20260914-original-relation-bulk) · [offline source ZIP](https://zenodo.org/api/records/22754516/files/46-original-relation-bulk-public-sources.zip/content).
- [46-page joint gamma schur](https://zenodo.org/api/records/22754516/files/43-joint-gamma-schur-reader.pdf/content) · [complete editable source](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/2be3b23974bf040f4ea06240b8a4b85372f7c71d/workbenches/splitzero-tandem/continuations/20260914-joint-gamma-schur) · [offline source ZIP](https://zenodo.org/api/records/22754516/files/44-joint-gamma-schur-public-sources.zip/content).

Three complete source snapshots develop Joint Gamma Schur continuation, original relation bulk control, and complete Gamma return. Their original definitions, proved finite estimates, receiving maps and recorded proof scopes remain in the separate editable sources.

The 15-page continuation is read first, followed by the 33-page bulk-control paper and the 46-page Joint Gamma Schur paper. Evaluating the positive product at the original growing indices, with finite remainders and the separately retained arithmetic allowances, remains unfinished; no leading W asymptotic or endpoint conclusion is asserted.

Here k is the tensor degree and q is the dimension of the finite cyclic
quotient. W is the remaining logarithmic Gamma determinant/product comparison:
the positive recurrence computes exp(W), but its growth at the original
indices still has to be evaluated. Hstar is the finite-input endpoint
expression returned by that comparison. The papers give the exact source
matrices, indices and endpoint maps, without changing these coordinates.

The exact relation is Hstar = -W + e0, with e0 in [-a0,b0]. The universal
interval contains the earlier exact-low interval; it does not tighten the
existing finite intersection. The positive recurrence computes exp(W) exactly.
The separate signed Gamma comparison has O(k)=o(q) error for each stated
fixed packet, and O(1) error for fixed multiplicity at least two.
The three papers retain their own complete proofs.

The [older 42-download edition](https://doi.org/10.5281/zenodo.22753338) remains frozen.
Its 1929-page compendium is retained, not replaced by a shorter summary.
The current edition adds PDF43/ZIP44, PDF45/ZIP46 and PDF47/ZIP48; PDF47 is
the actual browser preview. ZIPs are complete offline sources, not previews.

[All 48 downloads and source identities](calculation_edition_20260914_gamma_return/README.md).

## Earlier source and edition guide (historical snapshot)

The following guide is retained verbatim from the source-sharing snapshot before
the current DOI was issued. Its references to “current”, “front” and “outside
the frozen DOI” describe that earlier state and specifically DOI 22753338,
not the new 48-download edition above. The mathematical bodies, source links,
proof/CI scopes and older edition identities are unchanged.

# Split-Zero arithmetic cohomology

## Complete Gamma return and original relation bulk calculations

[Read the latest 15-page complete Gamma return](workbenches/splitzero-tandem/continuations/20260914-complete-gamma-return/Complete_Gamma_Return.pdf) · [Its complete editable sources](workbenches/splitzero-tandem/continuations/20260914-complete-gamma-return/README.md).

[Read the 33-page original relation bulk control](workbenches/splitzero-tandem/continuations/20260914-original-relation-bulk/Original_Relation_Bulk_Control.pdf) · [Its complete editable sources](workbenches/splitzero-tandem/continuations/20260914-original-relation-bulk/README.md).

[Read the preceding 46-page Joint Gamma Schur paper](workbenches/splitzero-tandem/continuations/20260914-joint-gamma-schur/Joint_Gamma_Schur_Continuation.pdf) · [Its source guide](workbenches/splitzero-tandem/continuations/20260914-joint-gamma-schur/README.md).

The programme compares the original theta-source arithmetic quotient with exact
Gamma sources while retaining all primary jets, mixed cross Grams, source masses
and four endpoint indices. The 33-page paper proves full inner/far-source control
and the degree-l metric-contrast calculation. The 15-page continuation supplies
the low scalar endpoint, weighted parity/Toda maps and a positive recurrence for
the complete universal centre W through exp(W). Its comparison errors are
O(k)=o(q), and O(1) for each fixed multiplicity at least two.

The exact translation is Hstar = -W + e0, with e0 in [-a0,b0]. The universal
interval contains the earlier exact-low interval; it does not tighten the
existing finite intersection. Its analytic value is a universal centre with
proved growing-family error. Evaluating the positive product at the original
growing indices, and returning the result through the separate arithmetic
allowances, remains the next calculation. No leading W asymptotic or endpoint
conclusion is asserted.

These are distinct complete working-source snapshots, **outside the frozen
[DOI 10.5281/zenodo.22753338](https://doi.org/10.5281/zenodo.22753338)**. Its 1,929-page edition, PDF preview and all
42 downloads remain unchanged. Each source tree includes its proof providers,
receiving successors, retained predecessors and stated verification scope.
Existing PR31 material remains a source snapshot, not a new merge or Lean claim.


## New working supplement: Joint Gamma Schur Return

[Read the complete 46-page paper](workbenches/splitzero-tandem/continuations/20260914-joint-gamma-schur/Joint_Gamma_Schur_Continuation.pdf) · [Editable sources and definitions](workbenches/splitzero-tandem/continuations/20260914-joint-gamma-schur/README.md).

This supplement compares the original theta-function source and its zero-jet
quotient with an explicit Gamma measure. The Gamma multiplication map, the full
mixed Schur block and its relation-valued minimum-section correction are retained.
The signed four-endpoint calculation returns the comparison to the original
arithmetic metric, including both asymmetric error allowances. Exact rational
finite-input certificates and the evaluated free determinant contribution are
included; the high relation-Gram and arithmetic growing-family estimate remains
open. PR31 material is a source snapshot, not a merge or new Lean-check claim.

This working supplement is **not included in the frozen [DOI 10.5281/zenodo.22753338](https://doi.org/10.5281/zenodo.22753338)**.
That published 1,929-page edition, its PDF preview and all 42 downloads remain
unchanged. The source guide states the precise maps, hypotheses, tests and
remaining calculation; this sharing step performs no new mathematics or build.


Start with [the accepted 1929-page public Split-Zero reader](https://zenodo.org/api/records/22753338/files/41-splitzero-cumulative-graph-public-reader.pdf/content)
and its [complete editable source and build guide](workbenches/splitzero-tandem/continuations/20260914-cumulative-graph/README.md).

The cumulative Split-Zero manuscript studies the original theta-function source, finite zero-jet algebras and source relations. It calculates the nonzero graph completion, the injective mixed quotient, two inverse corrections, relation-row bounds and the signed return to the original four-endpoint arithmetic determinant. Full zero multiplicities, original norms and maps are retained. The upper growth estimate as tensor degree increases remains unresolved; no proof of the Riemann hypothesis or new Lean kernel verification is claimed.

The [research guide](CURRENT_RESEARCH.md) explains the construction and next
arithmetic calculation. The [public-derivation ledger](workbenches/splitzero-tandem/continuations/20260914-cumulative-graph/PUBLIC_DERIVATION.md)
records locator-only presentation changes and exclusions. The public PDF was
rebuilt and reviewed as a derivative; it is not described as byte-identical to
the private delivery PDF. Complete mathematical source proofs remain preserved.
Raw private session records, reference-only literature and the raw owner ZIP
are not public payloads. Wrapper ZIPs are not duplicated as ordinary Git blobs.

The [preceding published recursive source-relations edition](https://doi.org/10.5281/zenodo.22739630) retains its PDF
preview and all 40 downloads. The [new published DOI 10.5281/zenodo.22753338](https://doi.org/10.5281/zenodo.22753338)
now provides [all 42 separate downloads](calculation_edition_20260914_cumulative_graph/README.md). The public Split-Zero PDF
is the actual browser preview; the [matching source ZIP](https://zenodo.org/api/records/22753338/files/42-splitzero-cumulative-graph-public-sources.zip/content) is an offline download.

The later mixed-boundary snapshot and unsealed later global manuscripts are outside this fixed cumulative graph source cut. Independently indexed working-source contributions retain their own proof and CI scopes. An unmerged contribution and its CI results are not silently assigned to this PDF.

## Current working sources





- [PR28: quotient, residue and period transport](workbenches/tau-split-integration/RESEARCH_NOTE.md) retains both transition defects in the original maps. Its eight actual merge-push workflows completed successfully; this is a status observation, not a newly performed full-log or analytic-proof review.



These working-source records retain their separately stated proof and CI scopes:

- [Canonical restriction and finite volume certificates](workbenches/tau-restriction-certificate-formal/RESEARCH_NOTE.md)
  compute how least-norm polynomial representatives change with degree and bound
  the resulting quotient-volume loss using finite matrix traces.
- [Specialization and curvature](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/a4a87844c257485ae6d669f5b3eb6d96b9e8b8d8/workbenches/tau-specialization-curvature-formal/RESEARCH_NOTE.md)
  interpolate those same representatives, retain the kernel and cokernel at the
  boundary, and turn determinant curvature into the finite trace certificate.
- [Theta source and Hochschild trace](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/a4a87844c257485ae6d669f5b3eb6d96b9e8b8d8/workbenches/tau-specialization-curvature-formal/HOCHSCHILD_COMPARISON.md)
  give the exact trace factorization, calculate which finite spectral blocks
  survive restriction to the critical line, and repair the boundary zero Fourier
  mode by retaining it before taking the explicit source-generated quotient.
- [Laplacian numerical-range bound](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/a4a87844c257485ae6d669f5b3eb6d96b9e8b8d8/workbenches/tau-specialization-curvature-formal/LAPLACIAN_PARABOLA.md)
  turns the original metric's measured action defect into a parabolic enclosure,
  without assuming an invariant metric or discarding repeated-zero jets.

PR26 and PR27 are merged working sources. The links for PR27 pin its reviewed
revision; its historical status files describe their original checkpoint.
Written analytic arguments and the selected Lean/finite checks have distinct
scopes. No uniform arithmetic upper estimate or RH conclusion is established.
The GitHub front and current DOI now share the accepted cumulative graph public PDF/source cut. The preceding recursive source-relations DOI and all 40 earlier downloads remain unchanged. Independent working sources retain their own proof and CI scopes.


## PR29: original residue detection and signed metric transfer

[PR29](https://github.com/KokunoYumeto/zeta-function-research-reader/pull/29) is normally merged at
`baef5c29f2bc36101eb74e7fe95c2d8c9e44bb8c`. Its 21 complete contributed files are verified,
and all 14,416 prior leaves, including the DOI mirror, remain unchanged.
The [signed metric-transfer note](workbenches/tau-arithmetic-metric-transfer/RESEARCH_NOTE.md)
and [residue guide](workbenches/tau-residue-rigidity/README.md) calculate
residue detection using the actual source generator, original relation-valued
metric variation, and the signed arithmetic log transfer. All fourteen
reviewed premerge checks and all ten actual merge-push runs were successful.
At the 18:36:16 UTC observation, the two new workflows also had complete
log/source/axiom and negative-control reconciliation: [metric transfer](https://github.com/KokunoYumeto/zeta-function-research-reader/actions/runs/34774694650)
covered 35 strict modules and 60 selected transitive axiom targets;
[residue rigidity](https://github.com/KokunoYumeto/zeta-function-research-reader/actions/runs/34774694642) covered
28 modules and 34 selected targets. The other eight runs have successful
conclusion observations, not a newly claimed full-log or mathematical audit.
These finite identities do not establish a uniform arithmetic bound, and the
contribution remains outside the frozen R57 DOI edition.

## Marked-product and signed four-endpoint working continuation

[Source guide](workbenches/tau-marked-product-four-endpoint/README.md) · [complete mathematical TeX](workbenches/tau-marked-product-four-endpoint/NOTE.tex) · [HTML source](workbenches/tau-marked-product-four-endpoint/index.html) · [provenance and exact changes](workbenches/tau-marked-product-four-endpoint/PUBLIC_PROVENANCE.md)

The aim is to calculate the actual arithmetic/Gamma correction on one common
source and connect the complete tensor packet to an explicit external family.
The reason for retaining the source maps is that auxiliary purity alone does
not control the original theta-source norm. The new note constructs the
rank-d^k external family and its marked-fibre map, retains the cyclic parameter
defect, derives the signed integral and its full relation-valued derivatives,
and proves a finite midpoint error bound. Full mass, Taylor units, repeated-zero
jets, supported zero versus absence, and the ordinary four endpoint degrees
are retained.

The positive endpoint-shell operators each have trace 2q, rank q+1, and
spectrum 1, 2 with multiplicity q-1, 1. The trace is not a rank-2q assertion.
The sealed source is unchanged; this clarification makes the operator meaning
explicit in this guide. A uniform arithmetic upper estimate remains unproved.
No RH/GRH conclusion, faithful Frobenius/metric transfer, or programme-wide
failure theorem is claimed.

[Fresh finite-check receipts](workbenches/tau-marked-product-four-endpoint/checks/PUBLIC_REPLAY.json) record 14 tests
passing in both Python modes and the intended negative controls. They are not
Lean or interval certificates. The [complete source/hash ledger](workbenches/tau-marked-product-four-endpoint/PUBLIC_FILE_CHANGES.json)
retains the public-privacy changes and discloses exclusion of the unreviewed
integration patch; both mathematical scripts and the full note remain included.

No existing GitHub Pages site was verified. The HTML link above is a source
file, not a claimed rendered online reader; no hosting provider or configuration
was added. This HTML/TeX working edition creates no PDF solely for a preview and
does not replace the [historical 765-page R57 DOI edition at the marked-source publication checkpoint](https://doi.org/10.5281/zenodo.22736292),
its preview, any of its 36 downloads, or its reading links. Its rendered-reader
link belongs in a later frozen edition only after a real route is verified.

## Supplementary accepted research sources: finite certification and mixed control

These two source packages supplement the ongoing research. They are outside the
fixed 821-page R62 paper and are not silently assigned to the historical 765-page
DOI. The main Split-Zero reading front remains unchanged.

### Original theta moments and finite Hankel certification

[Read the unchanged 47-page paper](workbenches/splitzero-tandem/continuations/20260913-accepted-followups/original-theta-certification/Tau_Theta_Hankel_Complete_Proofs.pdf) · [Distribution and scope](workbenches/splitzero-tandem/continuations/20260913-accepted-followups/original-theta-certification/PUBLIC_DISTRIBUTION.md)
· [Source and reproduction guide](workbenches/splitzero-tandem/continuations/20260913-accepted-followups/original-theta-certification/README.md)

The original theta integral, its mass, signed summands and both factors of two
are retained through the moment and logarithmic-coefficient maps. The supplied
certificate reports positive lower endpoints for all 32 pivots and 32 leading
determinants of the original 16-by-16 H15 and first-shift matrices. It uses 33
even moments M0 through M64, N=20, L=4, 1024-bit ball integration and the
independent 2^4096 integer grid with 1,400 endpoint pairs. The
[TC proof](workbenches/splitzero-tandem/continuations/20260913-accepted-followups/original-theta-certification/proofs/TC.tex), [nine supporting proof bodies](workbenches/splitzero-tandem/continuations/20260913-accepted-followups/original-theta-certification/support_reader/main.tex),
[analytic tail/integration contract](workbenches/splitzero-tandem/continuations/20260913-accepted-followups/original-theta-certification/calculation/CERTIFIED_ORIGINAL_THETA_HANKEL.md)
and [exact replay source](workbenches/splitzero-tandem/continuations/20260913-accepted-followups/original-theta-certification/verify_exact_rational.py) remain complete.
The finite certificate does not establish all-dimension positivity or RH;
this publication step does not rerun its mathematical checks.

All 111 owner-archive files remain byte-exact. The full 114-file
[public distribution](workbenches/splitzero-tandem/continuations/20260913-accepted-followups/original-theta-certification/DERIVATIVE_MANIFEST.json) preserves the original proofs
and evidence with [disclosed provenance](workbenches/splitzero-tandem/continuations/20260913-accepted-followups/original-theta-certification/PUBLIC_PROVENANCE.json).

### Deligne mixed-control continuation

[Read the Markdown overview](workbenches/splitzero-tandem/continuations/20260913-accepted-followups/deligne-mixed-control/DELIGNE_USAGE_OVERVIEW.md) · [Complete editable LaTeX reader](workbenches/splitzero-tandem/continuations/20260913-accepted-followups/deligne-mixed-control/COMPLETE_CONTROL_WORK.tex)
· [Source guide](workbenches/splitzero-tandem/continuations/20260913-accepted-followups/deligne-mixed-control/README.md) · [Public derivation](workbenches/splitzero-tandem/continuations/20260913-accepted-followups/deligne-mixed-control/PUBLIC_DERIVATION.md)

The complete seven-body reader develops [coefficient-face attachment](workbenches/splitzero-tandem/continuations/20260913-accepted-followups/deligne-mixed-control/sources/MCF.tex),
[spectral-jet tensor and dual filtrations](workbenches/splitzero-tandem/continuations/20260913-accepted-followups/deligne-mixed-control/sources/MW.tex),
the [length-two relative extension](workbenches/splitzero-tandem/continuations/20260913-accepted-followups/deligne-mixed-control/sources/MRE.tex), and the
[singular boundary connection and exact period determinant](workbenches/splitzero-tandem/continuations/20260913-accepted-followups/deligne-mixed-control/sources/BC.tex).
Each coefficient records absence separately from a supported zero; the maps
attach those masks to the original theta complex, retaining its boundary
primitives and the proper-source V/W kernel.
The arithmetic extension remains nonsplit; the added diagonal splitting is
not substituted for the original arithmetic action. The connection keeps both
polar orders and the metric comparison uses the original theta-source Gram.

The earlier [AW1--23](workbenches/splitzero-tandem/continuations/20260913-accepted-followups/deligne-mixed-control/sources/AW.tex) is included in full: AW7 gives the
window spectra, AW14 the final (2q-1) log kappa bound, and AW13 the stronger
full-spectrum expression. [SP8--10](workbenches/splitzero-tandem/continuations/20260913-accepted-followups/deligne-mixed-control/sources/SP.tex) gives the complementary
projection-overlap/common-range refinement, not a replacement claim of novelty
or universal dominance. The same-source operator correspondence, original
masses and separately typed AW isometry remain explicit. PR29's existing
secants, relation-valued derivatives and signed trace-power controls retain
their attribution. The [original marked-product note](workbenches/splitzero-tandem/continuations/20260913-accepted-followups/deligne-mixed-control/sources/MARKED_PRODUCT_ORIGINAL_NOTE.tex)
is preserved, with errata stated outside it.

Actual inertia, Stokes/extension maps and growing-family arithmetic estimates
remain work to do; no uniform bound or RH conclusion follows. All 36 accepted
public files are retained, with six disclosed locator-only evidence derivatives.
This is a source-only edition: no PDF is supplied or created, and no fresh
compilation or visual QA is claimed. Use the direct Markdown/LaTeX links above
for reading; its ZIP is an offline source archive, not a preview. Existing
rights, notices, earlier publications and reader roles remain unchanged.


## Earlier published reader introduction (historical)

The following earlier introduction records its own fixed source cut and DOI;
its use of “current” belongs to that historical edition.

# Split-Zero cohomology and arithmetic weight control

Start with [the 821-page R62 Split-Zero paper](https://zenodo.org/api/records/22738226/files/37-splitzero-periodized-residue-continuation-821p.pdf/content),
[published DOI 10.5281/zenodo.22738226](https://doi.org/10.5281/zenodo.22738226), and
[all 38 separate downloads](calculation_edition_20260913_periodized_residue/README.md).
The pertinent PDF is the actual Zenodo browser preview; the matching
[public source ZIP](https://zenodo.org/api/records/22738226/files/38-splitzero-periodized-residue-public-sources.zip/content) is an offline download, not a preview.

The 821-page R62 Split-Zero reader develops periodized source recovery and density, finite-circle curvature with quotient compensation, the circle/critical-observation diamond, and residue-constituent derivative and curvature formulas. It keeps the original theta-function source, zero multiplicities, source mass, coordinate S=k/2+iu and least-norm quotient metric. The uniform arithmetic growth estimate remains an active unresolved problem; no RH proof or closure is claimed.

Periodized observations recover the specified arithmetic source and identify
the relevant completed spaces. The finite-circle formulas calculate curvature
with the compensating quotient terms; the observation diamond compares circle
and critical-line maps. Residue-constituent formulas track derivatives and
curvature without dropping multiplicities, full source mass, signs or
orientations. These calculations expose what the remaining uniform arithmetic
growth estimate must control; they do not supply that unresolved bound.

The [research guide](CURRENT_RESEARCH.md), [editable source/build guide](workbenches/splitzero-tandem/continuations/20260913-periodized-residue/README.md)
and [public-derivative ledger](workbenches/splitzero-tandem/continuations/20260913-periodized-residue/PUBLIC_DERIVATION.md) retain the
proof dependencies, 47 complete source witnesses and exact privacy disclosures.
The source contains 4,926 files. Mathematical texts, the PDF and nested delivery
archives keep their accepted bytes. The raw owner ZIP is not a public payload.

This fixed PDF/public-source cut ends at R62. Later holonomy, mixed-control (TA/AT/AW), and original-theta certification cuts are separate and excluded. Separately indexed GitHub working sources, including PR29 and the marked-product continuation, retain their own proof, finite-check and CI scopes; their presence in this repository does not confer certification by this DOI.

The [historical 765-page DOI](https://doi.org/10.5281/zenodo.22736292) and all its 36
downloads remain unchanged; this successor adds only PDF37 and ZIP38.
The [attempt log](ATTEMPTS.md), [research programmes](RESEARCH_PROGRAMMES.md)
and [participation guide](POLYCLANK_PARTICIPATION.md) retain earlier routes,
partial results and active problems. Overleaf confirmations remain historical
and timers remain paused.



## Earlier published reader introduction (historical)

The following earlier introduction records its own fixed source cut and DOI;
its use of “current” belongs to that historical edition.

# Split-Zero arithmetic cohomology

Start with [the accepted 1624-page public Split-Zero reader](https://zenodo.org/api/records/22739630/files/39-splitzero-recursive-source-relations-public-reader.pdf/content)
and its [complete editable source and build guide](workbenches/splitzero-tandem/continuations/20260914-recursive-source-relations/README.md).

Split-Zero arithmetic cohomology studies the original theta-function source of finite zero packets, explicit source relations, signed metric control, restricted support and boundary propagation. The construction retains zero multiplicities, original source masses, coordinates and quotient maps. The signed finite approximation converges for each fixed source pair; tensor-uniform arithmetic control remains an active calculation. No proof of the Riemann hypothesis or new Lean kernel verification is claimed.

The [research guide](CURRENT_RESEARCH.md) explains the construction and next
arithmetic calculation. The [public-derivation ledger](workbenches/splitzero-tandem/continuations/20260914-recursive-source-relations/PUBLIC_DERIVATION.md)
records locator-only presentation changes and exclusions. The public PDF was
rebuilt and reviewed as a derivative; it is not described as byte-identical to
the private delivery PDF. Complete mathematical source proofs remain preserved.
Raw private session records, reference-only literature and the raw owner ZIP
are not public payloads. Wrapper ZIPs are not duplicated as ordinary Git blobs.

The [preceding published R62 edition](https://doi.org/10.5281/zenodo.22738226) retains its PDF
preview and all 38 downloads. The [new published DOI 10.5281/zenodo.22739630](https://doi.org/10.5281/zenodo.22739630)
now provides [all 40 separate downloads](calculation_edition_20260914_recursive_source_relations/README.md). The public Split-Zero PDF
is the actual browser preview; the [matching source ZIP](https://zenodo.org/api/records/22739630/files/40-splitzero-recursive-public-sources.zip/content) is an offline download.

Later full-packet formal-boundary, global-ray-monodromy, graph, relation-tail and generator-limit continuations are separate subsequent intakes, not material integrated into this fixed edition. Existing working sources retain their independent proof and CI scopes; their Lean or CI results are not attributed to this public PDF.


</details>
