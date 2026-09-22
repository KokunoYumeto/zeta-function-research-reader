# Split-Zero: escaping fibres and separated-zeta positivity

This research addition studies the supported-zero prime, the infinitesimal boundary of the original escaping inverse map, and the explicit formula for the separated quotient-counting zeta function. It retains both zero elements, all support sectors, the original observation metric, and the difference between algebraic trace and the signed arithmetic current.

This collection also proves the endpoint heat comparison, the exact ES metric and tetrahedral maps, finite and infinite shell operators, and the complete signed eight-state fibre with its omitted infinity point. Its Weil calculations retain the compensating analytic term and both finite involutions; the positive factor is not asserted to prove positivity of the whole Weil form.

Read [the complete proof edition](TAU_ZERO_PRIME_POSITIVITY.pdf), [its LaTeX source](TAU_ZERO_PRIME_POSITIVITY.tex), or the individual proofs below. [Sources and exact reading scope](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/173dbc6ed5a03235dbe7654f928f3692107db39b/workbenches/splitzero-tandem/branches/tau-zero-prime-positivity/SOURCES.md) records the prior programme results and human foundations. [The dated result bulletin](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/173dbc6ed5a03235dbe7654f928f3692107db39b/workbenches/splitzero-tandem/branches/tau-zero-prime-positivity/RESULTS_20260922.md) gives stable IDs and proof locators.

| Complete proof | Principal calculations |
|---|---|
| [Escaping fibre](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/173dbc6ed5a03235dbe7654f928f3692107db39b/workbenches/splitzero-tandem/branches/tau-zero-prime-positivity/ESCAPING_FIBRE_INFINITESIMAL_DERIVATION.md) | EFI1–EFI68: actual inverse map, double and triple collision schemes, trace signatures, supported prime contraction, exact pullback to the observed family and its cotangent differential. |
| [Infinitesimal positivity](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/173dbc6ed5a03235dbe7654f928f3692107db39b/workbenches/splitzero-tandem/branches/tau-zero-prime-positivity/INFINITESIMAL_SUPPORT_POSITIVITY_DERIVATION.md) | ISP1–ISP53: what vanishes and what survives, signed current, full operator derivative, full-support forms, endpoint-jet maps, exact trace versus matrix-norm defect. |
| [Non-Eulerian length distribution](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/173dbc6ed5a03235dbe7654f928f3692107db39b/workbenches/splitzero-tandem/branches/tau-zero-prime-positivity/NON_EULERIAN_LENGTH_DERIVATION.md) | NL1–NL18: exact quotient maps, convergent signed length distribution, negative atom and actual first derivative distribution with mixed-prime coefficients. |
| [Separated zeta explicit formula](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/173dbc6ed5a03235dbe7654f928f3692107db39b/workbenches/splitzero-tandem/branches/tau-zero-prime-positivity/SHIFTED_WEIL_POSITIVITY_DERIVATION.md) | SW1–SW42: continuation, gamma poles, reflection defect, corrected formula, exact negative test for the full shifted divisor, and the retained signed quotient and positive subspace. |
| [Full support reconstruction](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/173dbc6ed5a03235dbe7654f928f3692107db39b/workbenches/splitzero-tandem/branches/tau-zero-prime-positivity/FULL_SUPPORT_RECONSTRUCTION_DERIVATION.md) | FSR1–FSR36: actual base and spectrum, faithful joint branches, mixed kernel after linearization, all support-valued packet signatures. |
| [Finite Weil packet](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/173dbc6ed5a03235dbe7654f928f3692107db39b/workbenches/splitzero-tandem/branches/tau-zero-prime-positivity/WEIL_PACKET_DERIVATION.md) | WP1–WP57: every primary jet, actual observation multiplier, exact radical and diagonal form. |
| [Analytic Weil packet](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/173dbc6ed5a03235dbe7654f928f3692107db39b/workbenches/splitzero-tandem/branches/tau-zero-prime-positivity/WEIL_PACKET_ANALYTIC_DERIVATION.md) | WA1–WA30: complete contour and convergence proof for the actual entire test functions. |
| [Prime-norm comparison](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/173dbc6ed5a03235dbe7654f928f3692107db39b/workbenches/splitzero-tandem/branches/tau-zero-prime-positivity/TAU_WEIL_NORM_RECONSTRUCTION.md) | TN1–TN21: maps between the two quotient counts and the separate prime-weight Euler product, with its compensating archimedean distribution. |

The finite cover trace becomes positive semidefinite at a dual-number collision; the original matrix metric still detects the nilpotent, and its current has both signs. The separated numerical sheet is the Hurwitz family with endpoint zeta minus one. Its full-divisor pairing has an exact negative test using a real zero between minus twenty and minus nineteen. That is not a classical RH counterexample or a result about a critical-strip-only replacement pairing. The papers construct the exact defects and their connecting maps.

## Figures and reproducibility

![The actual escaping cover and its retained infinitesimal maps.](figures/25_escaping_trace.png)

![Three distinct forms at the same collision.](figures/26_infinitesimal_forms.png)

![Signed logarithmic lengths and the first infinitesimal arithmetic distribution.](figures/24_non_eulerian_lengths.png)

The corresponding Python sources reproduce these figures. Exact symbolic checks supplement the written proofs; their JSON reports state their scope. Run `python build_tau_positivity.py` with Pandoc and a LaTeX installation to rebuild the complete edition. Run the ten `check_*.py` files to reproduce the finite algebra checks. Python dependencies are SymPy, NumPy and Matplotlib. No numerical zero search is used to establish the shifted-divisor countertest.

## Quarter heat, tetrahedral transport, and the infinite shell

The added proofs identify the original target coordinate −1/4 with the endpoint trace receiver, transport its heat coefficient through the actual ES metric and tetrahedral frame, and construct the corresponding finite and infinite shell operators. The full multiplication maps, mixed blades, ambient kernels and explicit-formula correction are retained.

- [HEB1–HEB36: Complete original inverse curve, compactified infinitesimal, endpoint isometry and the compensating term in the full Weil identity. An admissible bump-derivative test retains its first jet at the collision and proves the compensating change.](HEAT_ENDPOINT_SIGN_BRIDGE.md)
- [PZS1–PZS38: The reflected sign, nilpotent residue obstruction, positive twist and exact observed-family comparison.](PRIME_ZERO_SIGN_DEFORMATION_DERIVATION.md)
- [ESQ1–ESQ68: Exact metric isometry, tetrahedral symmetry, multiplication embedding, collision algebra and original moving spatial metric.](ES_QUARTER_HEAT_TRACE_DERIVATION.md)
- [ESHL1–ESHL64: Spectral and matrix-algebra lifts, every shell sector, sharp infinite-dimensional positivity and retained finite-volume observables.](ES_SHELL_HEAT_LIFT_DERIVATION.md)
- [WEC1–WEC18: The actual four-evaluation correction in Weil’s formula is isometric to the original ES quarter form, with an explicit test section, kernel and involution-preserving map.](WEIL_ES_COMPENSATION_DERIVATION.md)
- [ESH1–ESH72: The original seven-point chart, its omitted infinity state, both full involutions and traces, and the complete eight-state heat collision with its length-four algebra and dual-number quotient.](EIGHT_STATE_HEAT_COMPARISON.md)

The positive lower bound applies to the specified shell operator for h > 1/8. It does not establish positivity of the classical Weil form: HEB28–HEB30 calculate the exact term transferred elsewhere in that form when its endpoint factor moves. The original zeta zeros are not shown to move onto the critical line by this construction.

![The exact shell lift and common sign crossing.](figures/28_shell_heat_sign.png)

[The dated results and proof locators](RESULTS_20260923.md) accompany the complete proofs. The six additional check scripts validate their finite identities; the infinite extension has a written proof.
