# Certified theta moments and complete-jet resolvent control

This continuation adds five complete proof sections to the [earlier Split-Zero cohomology reader](../../README.md). It retains the original theta source, the factor `g=2xi`, both typed zeros, complete zero multiplicities, packet coordinates and source metrics. The PDF and editable source form a standalone cumulative reader, including the six complete dated source notes on which the analytic construction builds.

[Read the cumulative PDF](Split_Zero_Cohomology_and_Arithmetic_Weight_Control.pdf) · [Complete TeX](tex/main.tex) · [Exact public source manifest](PUBLIC_SOURCE_MANIFEST.json)

## New proved calculations

- [Actual arithmetic moments](tex/arithmetic_moments.tex): an absolutely convergent incomplete-gamma double series for every original theta Gram entry, an explicit bound for both infinite tails, and directed Arb enclosures of the actual six-by-six Gram matrix. All six principal determinants and original monic squared norms are certified positive. The default cutoff is seven and the largest analytic entry-tail bound is below `2.961369e-63`.
- [Finite and infinite resolvents](tex/kernel_resolvent.tex): the full confluent quadrature kernel, including centres coinciding with quadrature nodes; its exact terminal-resolvent metric; the genuine unbounded multiplication operator, its tail domain, and the signed finite/terminal/tail Schur identity.
- [Quantitative convergence](tex/kernel_convergence.tex): an explicit initial-resolvent rate from the original exponential moments, with every derivative and full finite-algebra transport retained. The proof gives the exact kernel of the projection to the off-line resolvent domain.
- [Metric departure and complete jets](tex/metric_departure.tex): the identity `epsilon_m^2 = 2 sum_rho m_rho (Re rho - 1/2)^2 + departure_Gm(A)` for the original reflection-stable rank-two sequence; exact Gram-ratio and condition-number bounds on every retained nilpotent chain.
- [Recovered historical packet ghost](tex/historical_packet_ghost.tex): the full original permutation calculation and its exact arithmetic saturation `P_- E + A(P_- E) = E_off`, including all multiplicities; typed conjugation, metric transport and Split-Zero endomorphism descent. The complete original response excerpt and hash/line provenance are included under `sources/historical/`.

The initial-resolvent bound must pass through the proved Schur formula to control the terminal quantity defining the arithmetic weight. That formula retains `q_n`, `kappa_n`, `a_n` and the actual tail denominator. The paper does not assert a bound that removes these factors, RH, or an infinite-degree purity conclusion.

## Reproduction

The complete proofs are in `tex/`. Generated full source appendices are in `build/source_*.tex`; their original Markdown and exact source revisions are retained in `sources/` and `build/source_receipt.json`. No literature-library export or private session log is required to build the reader.

Install XeLaTeX and the packages listed by `tex/main.tex`, with Cambria, Calibri and Consolas fonts. From this directory run:

```text
python scripts/build_reader.py
python scripts/check_arithmetic_moments.py
python -O scripts/check_arithmetic_moments.py
python scripts/check_metric_departure.py
python scripts/check_historical_packet_ghost.py
python checks/check_kernel_resolvent.py
```

The arithmetic moment checker requires python-flint/Arb (the recorded run uses version 0.9.0). The exact algebra checkers use SymPy. The source mathematical proofs are independent of the software checks; the interval moment enclosures are specific certified finite data supported by the proved tail estimate. Checker receipts distinguish these scopes. No new Lean execution is claimed.

`build/build_receipt.json` pins the contributed PDF and every included TeX input. `build/qa/visual_review.json` records page inspection of that exact PDF. Local machine paths in public review metadata have explicit corpus-relative aliases; source hashes and mathematical proof text remain identified. The selected public files and any metadata aliasing are recorded by the manifest.

The [research-state section](tex/research_conclusion.tex) gives the current exact sequence of maps and the next arithmetic calculation. PR #14's coherent tensor interpolation and the additional archived Hurwitz/Laurent reconstruction are being integrated separately after their own complete reviews; this source snapshot does not silently include those unfinished publication changes.
