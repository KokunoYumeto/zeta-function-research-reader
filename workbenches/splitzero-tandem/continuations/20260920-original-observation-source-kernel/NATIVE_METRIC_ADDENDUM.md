# SZ-20260920-022: receiver from the published native truncation

The complete proof `NATIVE_METRIC_SINGULAR_VALUE_BRACKETS.tex`, MS1–8, applies SZ-20260920-019's proved native resolvent truncation to the original mixed-action and inherited-period calculations. Both consecutive original minima are retained.

Write ε = L_N^sharp/(2J) < 1 for the proved truncation error and B_under for the fixed original B = ΛM_SI expressed in the truncated source and target metrics. Every singular value has the enclosure

\[
\sqrt{1-\epsilon}\,\sigma_j(B_{\rm under})
\le\sigma_j(B_{\rm original})
\le(1-\epsilon)^{-1/2}\sigma_j(B_{\rm under}).
\]

The original return block depends on the actual metric. Keeping it unchanged and using the exact rank-two cancellation gives σ_(j−2)(C_original) ≥ √(1−ε) σ_j(B_under), together with the corresponding original commutator bound. The period conversion is also enclosed: √(1−ε)ρ_under ≤ ρ_N ≤ ρ_under. A fixed exact reconstruction map has the same multiplicative norm enclosure.

These are finite, original-map results. The truncated matrices still contain the native integrals; their values must be evaluated or enclosed by the ongoing native-moment calculation. No arithmetic phase or sign is inferred from a singular value.

Proof source: complete TR1–10 in the [published native parity/conductor edition](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/ab45e221579a0d48ce2885b4ecdf1a6aefc24a20/workbenches/splitzero-tandem/continuations/20260920-native-parity-conductor-return). Its human input credits A. I. Aptekarev, G. López Lagomasino and A. Martínez-Finkelshtein, arXiv:1410.1261v1; the programme companion proves the exact transport to the actual arithmetic measure. The full TR proof was read and MS1–8 independently checked. This addendum leaves the earlier sealed source manifest unchanged.
