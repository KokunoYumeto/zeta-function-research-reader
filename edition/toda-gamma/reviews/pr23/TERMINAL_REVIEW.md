# PR #23: independent terminal review

## Decision

Recommend merging the bounded finite formalization at exact head `c720f40530eed2f5969dbabe94dfd3fddc0f507f`, subject to the parent workflow's fresh head/draft check. No blocking mathematical, proof-coverage, or CI defect was found. Two wording corrections are nonblocking and should accompany any public summary; neither changes the checked theorems or the endpoint-selection formula.

This recommendation does not certify a quantitative arithmetic endpoint estimate, a real-zero assertion, or the Riemann hypothesis. The full arithmetic source construction, differentiation under the integrals, Toda identification, Jensen/root assembly in Lean, and asymptotic estimate remain outside these five files.

PR: https://github.com/KokunoYumeto/zeta-function-research-reader/pull/23

## Current revision and merge continuity

The full user paste was read. Fresh REST before/after reads retain the reported head. The PR is open/draft, `mergeable=true`, `mergeable_state=clean`. Current main is `b32ca2128e0deb0eec6eafb860776a5d6a28dcbb`. The compare is ahead by five commits and behind by one, with merge base `811210d24b80813a08972ca23f919db015383137`; the behind commit is the already-completed PR #22 merge ancestry.

The complete, nontruncated Git trees were independently compared by path and blob identity. Main-to-head has exactly fourteen added files, zero modified files, and zero deleted files. All fifteen files retained in the PR #22 review, including its four Lean modules, original-Gram dependency, selected manifest, strict parser, workflow, and rational checker, are byte-identical at this head. Thus the old statement about twenty-four additions is historical, not the current delta. No inherited implementation or publication file is overwritten. This tree continuity is stronger evidence than assuming the PR metadata's older `base_sha` is today's main.

## Complete terminal CI evidence

All ten check runs, all ten workflow jobs, and every step in every job are `completed/success`. Full decoded logs were freshly fetched, saved, hashed, and parsed locally. This was offline evidence analysis, not a local Lean execution.

| Run | Job | Workflow / event | Independently checked reports |
| --- | --- | --- | --- |
| 34723954535 | 103634685459 | Toda / push | Exact head checkout; 30 exact new raw reports; inherited 50/29/40/68/38/87/73 reports; structural 28 pass |
| 34723955979 | 103634690293 | Toda / PR | Same five source hashes; 30 exact new raw reports; all inherited reports and structural pass |
| 34723955963 | 103634690333 | Exterior / PR | 50 exact raw exterior reports; inherited 29/40/68/38/87/73; structural pass |
| 34723955964 | 103634690366 | Conormal / PR | 29 exact raw conormal reports; inherited 40/68/38/87/73; structural pass |
| 34723955978 | 103634690477 | Frontier / PR | 40/68/38/87/73; structural pass |
| 34723955971 | 103634690329 | Boundary integration / PR | 68/38/87/73; structural pass |
| 34723955972 | 103634690405 | Tau recovery / PR | 87/73; structural pass |
| 34723955986 | 103634690359 | Derived / PR | 73; structural pass |
| 34723955969 | 103634690299 | Synchronization / PR | 19 standard-axiom reports; structural pass |
| 34723955974 | 103634690696 | Structural / PR | 28 unique exact raw reports, standard axioms only |

The PR-event jobs ran test merge `4a23b04` (the log records merging this head into `811210d24b80813a08972ca23f919db015383137`), not today's main merge commit. The push job directly checked the exact head. Direct tree continuity above shows today's main contributes no differing file bytes to the proposed merge.

Both Toda jobs individually compile the four inherited exterior modules and all five new modules with `--trust=0 -DwarningAsError=true`, with actual per-module execution markers and successful steps. They check `SplitZeroMetricRestriction` first, run the new and inherited selected audits, rebuild inherited sources, compile the generated combined import, and complete every inherited audit. The log records Lean 4.31.0; the workflow's successful pinned-revision test retains Mathlib `fabf563a7c95a166b8d7b6efca11c8b4dc9d911f`. No package/build changes appear in the new delta.

The new checker and the inherited fail-closed parser were fully read. The selected manifest names exactly thirty unique declarations across all five modules, including the final trace composition. The inherited parser rejects missing, extra, duplicate, or nonstandard reports. Independent parsing of the complete raw logs confirms exactly that set, using only subsets of `propext`, `Classical.choice`, and `Quot.sound`. The inherited fifty names are likewise matched to the actual manifest, with exact raw coverage independently checked in the exterior job. Freshly fetched inherited manifests were used for the other exact report-set comparisons.

All five entire Lean files were read and comment-stripped scans find no `sorry`, `admit`, `axiom`, `unsafe`, `implemented_by`, or `native_decide`. Every reviewed source SHA-256 matches both Toda CI reports and the requested hashes. Selected counts include definitions and infrastructure, not thirty mathematical discoveries.

Both Toda jobs run all thirteen exact-rational methods normally and under `python -O`; successful JSON records match. They also run the twenty-five inherited harness tests in both modes, and their deliberate-failure controls fail in both modes. The full rational checker source was read. These are finite calibrations, not arithmetic interval calculations or independently replayed archive suites.

## Mathematical source review

All five new Lean files, the full manifest and checker, dedicated workflow, six workbench texts/scripts, and the inherited original-Gram theorem interface were inspected.

### Actual weighted source correction

`WeightedQuotientVolume.residual` literally constructs

    R = C - B H (B* M C).

The original `M` remains in every source/relation/quotient composite. From the explicit right-inverse identity `(B* M B) H = I`, the proof obtains `B* M R = 0`, then expands `R* M R` and cancels the correction against that orthogonality. This yields the asserted Schur residual before invoking Mathlib's determinant theorem. The statements are valid already as algebraic matrix identities; positivity and the arithmetic origin of M are separate caller obligations, not falsely constructed by the Lean file.

The determinant factor and ratio use the actual relation Gram `B* M B`; the ratio retains a nonzero determinant premise. The observation theorem uses the actual supplied `JB=0` to prove `JR=JC`. It does not assume that the quotient images of relations supply a nonzero denominator, replace M by a chosen favorable metric, or identify genuine higher relation ideals with powers of a first polynomial. The unweighted module is a valid parallel interface. General polynomial coefficient maps, monic basis-change determinant one, and integral entries remain written source inputs.

### Both losses and original-Gram composition

`TodaVolume.two_losses` is the exact identity

    a(1-M/P)(M/Q-1)-z^2
      = a(P-Q)^2/(4PQ) - a(2M-P-Q)^2/(4PQ) - z^2.

Its denominator assumptions, positive-volume upper bound, and equality characterization are correct. For positive a, equality in the squared bound is exactly `2M=P+Q` and `z=0`. Neither phase nor imbalance is silently set to zero. The first-admissible-degree result has its own supplied endpoint formula and does not invert an inadmissible predecessor. Common scaling is an explicit cancellation identity, not mass normalization.

`TodaTrace.original_gram_volume` actually calls inherited `TraceCertificate.original_gram_bound`, then calls `lower_forces_volume` with the absolute aggregate trace defect. It retains G and its genuine coordinate isometry, inclusion B, extraction L with LB=I, invariance AB=Ba, G-orthogonality of BL, the two-coordinate factorization of the original control, compressed trace zero, and compressed determinant `-e^2`. It adds the explicit identity `e^2=energy(...)`, not the desired aggregate bound as its only premise. No normality of A, invariant orthogonal complement, or discarded spectral block is introduced. The conclusion is precisely

    4PQ (2 Re tr(a)-w dim(E))^2 <= alpha(P-Q)^2.

### Endpoint-only selection: written proof is correct

For positive original norms/volumes, nonincreasing V, nonnegative allowances satisfying the local Toda bound, `n>=q` and integer `r>=1`, the written theorem is

    min_(0<=j<r) epsilon_(n+j)
      <= (omega_(n+r)/omega_n)^(1/(2r))
         * sinh(log(V_(n-1)V_n/(V_(n+r-1)V_(n+r)))/(2r)).

Set `x_j=log(V_(n+j-1)/V_(n+j+1))/2` and `A_j=sqrt(omega_(n+j+1)/omega_(n+j))`. If any x is zero, the nonnegative allowance at that degree is zero. Otherwise concavity of `log(sinh x)` gives the product inequality in the stated direction. The nonnegative finite minimum raised to r is bounded by the product of allowances. The recurrence product telescopes to the square root of the two norm endpoints; the sum of x telescopes to half the logarithm of the four volume endpoints. Taking the nonnegative r-th root gives exactly the displayed constants and indices. The r=1 formula reduces to the local bound. Empty windows and the empty arithmetic packet are excluded from this analytic criterion.

`VolumeWindow.norm_ratio_product` and `overlapping_log_telescope` formalize the two telescopes; finite averaging/selection is also checked. The particular sinh/Jensen product and final root assembly are not a Lean theorem. The documents explicitly say so; no formalized asymptotic or real-zero claim is being inferred from them.

For a packet consisting exactly of the quartet, the lower contribution and dimension used in the argument are properly qualified by the coordination text. The sufficient conditions `r>=c_h q_k`, `A=O_h(q_k)`, `B=o_h(q_k log k)` really imply an upper allowance `o(kq_k)`: `B/(2r)=o(log k)` and the ratio is bounded by `k^(-1+o(1))`. These arithmetic conditions are not proved here. Positivity, telescoping, and a Toda identity alone do not supply them.

## Exterior allowance and edge cases

The exact second-exterior formula is correct under the written positive-radius spectrum hypothesis, which entails q>=2. For `1<=p<=q`, put `r_p=choose(q-2,p-1)` and `D=choose(q,p)`, with out-of-range lower binomial indices interpreted as zero. The first additive control has r_p positive and r_p negative epsilon eigenvalues, plus D-2r_p zeros. For `0<=s<=D`, the maximal sum is s through s=r_p, then r_p through s=D-r_p, then D-s. This is exactly

    epsilon * min(s, r_p, D-s).

Reversing positive and negative choices attains the negative extremum. In particular s=0 and s=D give zero, and p=q has r_p=0, D=1, so every permitted second-degree allowance is zero. The q=4,p=2,s=2 example correctly gives 2epsilon. The regression covers q=2,...,5, p=1,...,q, and every permitted s, including the top-degree zero case.

At p=0 the first exterior space is the scalar line with zero additive control. The same capacity formula can be extended by `r_0=0` and `D_0=1`, but the displayed section explicitly starts at p=1 and the regression does not test p=0. For q=0 or q=1, the assumed spectrum with two nonzero opposite directions is impossible when epsilon>0; do not substitute negative upper binomial indices into the formula. The epsilon=0/degenerate cases instead have zero self-adjoint control and zero additive exterior control. The zero-dimensional arithmetic packet remains distinct from its exterior-degree-zero scalar line and from the nonzero analytic seed/mass, as the coordination text says.

## Nonblocking wording corrections

1. `workbenches/tau-toda-volume-formal/ENDPOINT_CRITERION.md:86` says the first exterior operator norm "is still epsilon" throughout `1<=p<=q`. At p=q the sole eigenvalue is zero. A precise replacement is: "Its operator norm is at most epsilon; it equals epsilon for 1<=p<=q-1 and is zero for p=q." This is a genuine endpoint wording error, not a defect in the exact second-step formula, the original upper bound, or a Lean theorem. Any public description should use the corrected qualification.
2. At line 72, "strictly preferable" should be "never larger, and potentially strictly smaller." The geometric mean equals the maximum when the recurrence values are all equal; the resulting upper bounds also coincide in zero-contraction cases. The earlier claimed inequality and sharpness statement remain correct.

The older research note's four-module count is expressly updated by `SOURCE_COORDINATES.md`; it is not an unresolved coverage issue. The old two-degree-window handoff is a valid weaker precursor, not a contradiction of the consecutive-window improvement in `ENDPOINT_CRITERION.md`.

## Evidence and action boundary

`FETCH_RECEIPT.json` binds before/after metadata, nontruncated trees, compare, check/run/job records, and ten complete logs. `AUX_FETCH_RECEIPT.json` binds the supplemental actual manifests. `ANALYSIS_RECEIPT.json` records exact coverage, all job/step statuses, source hashes, tree continuity, and inherited-byte checks. The terminal seal binds this report and all review inputs by SHA-256.

The first offline parser attempt rejected older locally serialized inherited-manifest bytes; it did not ignore that mismatch. The exact pinned Git blobs were then fetched directly, verified against the pinned tree, and used for the successful analysis. No target set or proof check was weakened.

No local Lean, heavy build, Git checkout, visible browser, remote write, draft change, merge, publication, reset, or child agent was used. PR #24 was neither reviewed nor changed. The selected Deligne source pages and inaccessible external archives were not independently re-audited in this bounded review. The parent workflow owns any authorized mutation and must recheck the exact head immediately before merge.
