# Complete lifted actions and the original-quartet real-time boundary

The complete new proof is [FABLE_REAL_FLOW.tex](FABLE_REAL_FLOW.tex). This is an additive continuation of the [published signed-state edition](../20260920-fable-signed-states/README.md), read at commit `d73b545c7e70dd55fb8b58557f704666ba310626`. Its original polynomial, four Time labels, full factor signs and original weighted-conductor maps are retained.

## Results

**FRF-C: all complete lifts are classified.** For every constant complex matrix `M`, the unique polynomial vector field satisfying `DP X_M = M P` is `X_M = -adj(DP) M P / 2`. It is complete for every real time and every initial point if and only if it is complete for complex time, if and only if `M` is a scalar multiple of `diag(1,-1,-2,-3)`. The proof uses the exact entire fibre cardinalities to recover both invariant boundary divisors, then calculates their full linear tangency algebra. This goes beyond classifying equivariance under a linear source action: it also excludes a complete nonlinear lift outside the one permitted line.

**FRF-B: an explicit real-time orbit of the correctly transported original quartet has five escaping states.** Let `K` be the actual four-column marked matrix of FC15a, and let `R` be the original quartet action in its cardinal basis. The correct coefficient-coordinate matrix is `M = K R K^{-1}`, rather than `R` acting on the polynomial coefficient slots. A finite positive time `T`, defined explicitly in FRF29, gives the target orbit `Y(t) = K exp((t-T)R) K^{-1}(0,0,-3,2)`. The full interval before `T` avoids the leading-coefficient and discriminant divisors. At its endpoint, four signed states over the colliding N/T roots escape at rate `(T-t)^(-1/4)`, one excluded infinity sign escapes at rate `(T-t)^(-3)`, and the other three states have exactly evaluated finite limits. The original Gamma-norm leading constants are FRF35 and FRF36. The omitted sign becomes finite in the completed factor space; the other four escapes persist there.

**FRF-S: both directional spectra are determined.** At a bounded selected finite double root with inverse scale `|a| -> infinity`, the exact full differential has singular scales `|a|^3, |a|^2, 1, |a|^-5`. Along the literal real-time orbit these become `(T-t)^(-3/4), (T-t)^(-1/2), 1, (T-t)^(5/4)`. The excluded-sign trajectory has scales `(T-t)^(-4), (T-t)^(-1), (T-t), (T-t)^4`. The proof retains the full differential and exact exterior minors. Operator condition numbers and relative Gram condition numbers are stated separately. The determinant remains `-2` at every finite point.

**FRF-W: every excluded matrix has a bounded boundary-witness search.** When the leading-coefficient hyperplane is not invariant, a grid of 216 specified cubic targets contains an exact transverse witness. When it is invariant but `M` is outside the complete line, a grid of 59,319 specified repeated-root incidence parameters contains an exact simple-discriminant witness. This is a proof of a finite search bound, not a report that every grid point has been numerically scanned.

## Original conductor and arithmetic scope

The source and target maps are the provider's actual `Phi = X K^{-1}` and `Psi = Y K^{-1}`, with `T_A Phi = Psi`, original quotient and Gamma norms, and all conductor moments. These maps transport the new vector fields, real-time branches and norm constants exactly. The original translation matrix is separately retained as `K V_rho^T N_v (V_rho^T)^{-1} K^{-1}`; its unique nonlinear lift is also incomplete by FRF-C.

The fixed original conductor has its unchanged nonzero determinant and unchanged kernel `P_{v-1}`. Its coefficients are not selected to fit the nonlinear map. The transported arithmetic quotient action is distinguished from multiplication on untruncated target polynomials. Original Taylor-unit multiplication remains a separate invertible map, with its full factors retained in the metrics. Neither the native allocation tuple nor the original projected arithmetic cross-product asymptotic is evaluated by these results. No RH conclusion is claimed.

## Sources and verification

[Source ledger](SOURCE_LEDGER.md) separates inherited results, the newly reconciled original polynomial identity, and the added calculations. The original three-variable construction retains Alpöge/Fable attribution through Tao; the four-dimensional polynomial and distinguished representatives retain the canonical ES-reader attribution. No new extraction or exhaustive audit of the 488-page archive is claimed.

[Verification record](VERIFICATION.json) records the actual GitHub Actions execution. The first run passed **44 exact checks** in both ordinary and optimized Python, with byte-identical JSON output. Both deliberate false controls were rejected in both modes. The run verified the exact published provider blob as well. Analytic continuation, completeness, and limiting-norm conclusions are proved in the manuscript rather than inferred from those checks.

Run locally with SymPy 1.14.0:

```sh
python verify_real_flow.py > normal.json
python -O verify_real_flow.py > optimized.json
cmp normal.json optimized.json
python verify_real_flow.py --negative-control reverse-transverse-sign
python verify_real_flow.py --negative-control replace-transported-action
```

The last two commands are expected to exit with status 2 and report `false_claim_accepted: false`. The [scoped workflow](../../../../.github/workflows/fable-real-flow-exact.yml) uses only read permissions, the repository's existing pinned checkout action, and the pinned symbolic-algebra version. It neither publishes replacement historical editions nor writes to another contributor's source files.

This package supplies LaTeX and executable text sources. No PDF build or external peer review is asserted.
