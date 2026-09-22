# Split-Zero: escaping fibres and separated-zeta positivity

This research addition studies the supported-zero prime, the infinitesimal boundary of the original escaping inverse map, and the explicit formula for the separated quotient-counting zeta function. It retains both zero elements, all support sectors, the original observation metric, and the difference between algebraic trace and the signed arithmetic current.

Read [the complete proof edition](TAU_ZERO_PRIME_POSITIVITY.pdf), [its LaTeX source](TAU_ZERO_PRIME_POSITIVITY.tex), or the individual proofs below. [Sources and exact reading scope](SOURCES.md) records the prior programme results and human foundations. [The dated result bulletin](RESULTS_20260922.md) gives stable IDs and proof locators.

| Complete proof | Principal calculations |
|---|---|
| [Escaping fibre](ESCAPING_FIBRE_INFINITESIMAL_DERIVATION.md) | EFI1–EFI68: actual inverse map, double and triple collision schemes, trace signatures, supported prime contraction, exact pullback to the observed family and its cotangent differential. |
| [Infinitesimal positivity](INFINITESIMAL_SUPPORT_POSITIVITY_DERIVATION.md) | ISP1–ISP53: what vanishes and what survives, signed current, full operator derivative, full-support forms, endpoint-jet maps, exact trace versus matrix-norm defect. |
| [Non-Eulerian length distribution](NON_EULERIAN_LENGTH_DERIVATION.md) | NL1–NL18: exact quotient maps, convergent signed length distribution, negative atom and actual first derivative distribution with mixed-prime coefficients. |
| [Separated zeta explicit formula](SHIFTED_WEIL_POSITIVITY_DERIVATION.md) | SW1–SW42: continuation, gamma poles, reflection defect, corrected formula, exact negative test for the full shifted divisor, and the retained signed quotient and positive subspace. |
| [Full support reconstruction](FULL_SUPPORT_RECONSTRUCTION_DERIVATION.md) | FSR1–FSR36: actual base and spectrum, faithful joint branches, mixed kernel after linearization, all support-valued packet signatures. |
| [Finite Weil packet](WEIL_PACKET_DERIVATION.md) | WP1–WP57: every primary jet, actual observation multiplier, exact radical and diagonal form. |
| [Analytic Weil packet](WEIL_PACKET_ANALYTIC_DERIVATION.md) | WA1–WA30: complete contour and convergence proof for the actual entire test functions. |
| [Prime-norm comparison](TAU_WEIL_NORM_RECONSTRUCTION.md) | TN1–TN21: maps between the two quotient counts and the separate prime-weight Euler product, with its compensating archimedean distribution. |

The finite cover trace becomes positive semidefinite at a dual-number collision; the original matrix metric still detects the nilpotent, and its current has both signs. The separated numerical sheet is the Hurwitz family with endpoint zeta minus one. Its full-divisor pairing has an exact negative test using a real zero between minus twenty and minus nineteen. That is not a classical RH counterexample or a result about a critical-strip-only replacement pairing. The papers construct the exact defects and their connecting maps.

## Figures and reproducibility

![The actual escaping cover and its retained infinitesimal maps.](figures/25_escaping_trace.png)

![Three distinct forms at the same collision.](figures/26_infinitesimal_forms.png)

![Signed logarithmic lengths and the first infinitesimal arithmetic distribution.](figures/24_non_eulerian_lengths.png)

The corresponding Python sources reproduce these figures. Exact symbolic checks supplement the written proofs; their JSON reports state their scope. Run `python build_tau_positivity.py` with Pandoc and a LaTeX installation to rebuild the complete edition. Run the four `check_*.py` files to reproduce the finite algebra checks. Python dependencies are SymPy, NumPy and Matplotlib. No numerical zero search is used to establish the shifted-divisor countertest.
