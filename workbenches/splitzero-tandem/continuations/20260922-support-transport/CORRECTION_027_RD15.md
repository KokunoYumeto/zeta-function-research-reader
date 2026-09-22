# Correction to edition 027, RD15: response and kernel coefficients

This correction accompanies the completed support-transport edition, SZ-20260922-028. Edition 027 remains available with its original sealed files; the statement below corrects its coefficient identification, not its source identity.

In [edition 027's RD15 calculation](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/40a766ed3a8e0eadd9947f591803255b6eecf184/workbenches/splitzero-tandem/continuations/20260922-terminal-response/RESPONSE_DENOMINATORS.md#L135), the retained four-cutoff response return is

\[
\mathcal R\log\alpha_{\mathrm{resp}}
=4[\psi(0)-\psi(1)]q+O_{h,\varpi}(k\log q).
\]

Its coefficient is approximately **0.7001820930008661000692458016103144595651326270615252**. The following identification in 027 with twice the established kernel coefficient is incorrect. The established kernel coefficient remains

\[
C_\partial=2J(1)
\approx1.3542819878252921328839897751538481839960652640769.
\]

The exact connection between the two profiles is

\[
C_\partial=8\int_0^1\psi(t)\,dt+4\psi(0)-8\psi(1).
\]

The full corrected proofs are [DF15–16](OBSERVED_DEFORMATION_AND_CURRENT.md#L151) and [EE47–48](EVOLUTION_EXTENSION_PROOF.md#L587), with the original profile map also retained in [RC12](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/5c69161ca70ee187f41df0bfe786e8b6eebed422/workbenches/splitzero-tandem/continuations/20260922-current-effective-cutoff/CUTOFF_CURRENT_CONNECTION.md#L100). The new [29-page reader](SUPPORT_TRANSPORT_READER.pdf), [reader LaTeX](SUPPORT_TRANSPORT_READER.tex), [results](RESULTS_20260922_028.md) and [research state](RESEARCH_STATE.json) carry the correction.

Read the old response result using the first displayed expression above, not the erroneous coefficient identification in the old bulletin or edition-specific description. No historical proof-bank bytes or PDFs were silently replaced. This correction does not assign the remaining signed arithmetic kernel-action coefficients or conclude RH.
