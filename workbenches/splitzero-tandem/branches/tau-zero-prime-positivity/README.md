# Split-Zero: escaping fibres and separated-zeta positivity



<!-- original-zeta-reconstruction-start -->

**Original-zeta receiving calculation.** The working meromorphic function is the original Riemann zeta, with its full Gamma/endpoints multiplier and its full trivial-zero and pole divisor retained. [TF1–42](FAITHFUL_THETA_COMPLETION_RETURN.md) proves the original labelled theta inverse and the actual heat-image defect. [UZ1–53](FAITHFUL_UNCOMPLETED_ZETA_HEAT.md) proves every exceptional-point fibre, jet, original-zeta heat term and reflection orientation. [OZC1–48](ORIGINAL_ZETA_COMPACT_WEIL_RECONSTRUCTION.md) rederives the compact contour and interval operator directly from zeta, including the left-cutoff Gamma boundary, and specifies exactly which compensated pairing the bounds concern. [OZH1–49](ORIGINAL_ZETA_HEAT_CONTACT_RECONSTRUCTION.md) rederives the actual meromorphic heat, rational signed trace, compact-test domain, contact drift and full causal arithmetic variation. The raw full divisor and the compensated Weil receiver are linked by their displayed correction, not identified. In particular the fixed-test trivial-zero sum converges exactly at translations at least 1/32 and equals the earlier R term; at zero translation it requires the proved cutoff compensation. [OZK1–38](ORIGINAL_ZETA_CAUCHY_RECONSTRUCTION.md) reconstructs the original signed Cauchy trace, its full Gamma correction, resonant finite parts, every finite matrix and its index, and the complete local heat jets. Its invertible map retains the raw trace and correction separately. These complete receiving proofs govern the interpretation of the retained auxiliary calculations below.

<!-- original-zeta-reconstruction-end -->





This research addition studies the supported-zero prime, the infinitesimal boundary of the original escaping inverse map, and the explicit formula for the separated quotient-counting zeta function. It retains both zero elements, all support sectors, the original observation metric, and the difference between algebraic trace and the signed arithmetic current.



This collection also proves the endpoint heat comparison, the exact ES metric and tetrahedral maps, finite and infinite shell operators, and the complete signed eight-state fibre with its omitted infinity point. Its Weil calculations retain the compensating analytic term and both finite involutions; the positive factor is not asserted to prove positivity of the whole Weil form.



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



The corresponding Python sources reproduce these figures. Exact symbolic checks supplement the written proofs; their JSON reports state their scope. Run `python build_tau_positivity.py` with Pandoc and a LaTeX installation to rebuild the complete edition. Run the accompanying `check_*.py` files to reproduce the finite algebra checks. Python dependencies are SymPy, NumPy and Matplotlib. No numerical zero search is used to establish the shifted-divisor countertest.



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



## Supported-zero Weil formula and actual holonomy



The full supported-zero theta now has a proved map from admissible Weil tests, a complete label-resolved trace identity, and a minimal Fourier-closed endpoint extension. The original signed cover has explicit infinity and heat monodromies, including a nonzero residue on the collision algebra. Averaging the native trace over its actual order-192 group gives a positive semidefinite form; the complete calculation retains its nonzero correction in the integrated Weil identity. These statements do not assert RH.



- [SZW1–SZW47: Full supported-zero prime, theta, divisor and fixed-support trace maps](SUPPORTED_ZERO_PRIME_WEIL_DERIVATION.md)

- [EHM1–EHM53: Actual eight-state monodromy and nonzero collision residue](EIGHT_STATE_HOLONOMY_DERIVATION.md)

- [HWA1–HWA38: Positive holonomy average and its exact integrated Weil correction](HOLONOMY_AVERAGING_WEIL_ENDPOINT_DERIVATION.md)



The three earlier complete background derivations are retained in [supporting proofs](supporting_proofs/TAU_PRIME_SPECTRUM_DERIVATION.md). All original coefficients, support labels and quotient kernels remain in the proofs.



## Class-field monodromy and the original collision



The Connes–Consani finite covers now receive an explicit quadratic quotient of the original signed frame cover. Its conductor-23 specialization, prime return maps, and integral model are calculated. The prime-orbit traces retain both orientations and the complete supported-zero trivial sector. The heat collision retains a nonzero filtered residue which the abelian character forgets.



- [PHW1–PHW25: oriented prime traces, inertia, character decomposition and supported endpoints](PRIME_HOLONOMY_SUPPORTED_WEIL_DERIVATION.md)

- [CBR1–CBR29: discriminant quotient, arithmetic cover and surviving infinitesimal residue](CLASS_FIELD_SIGNED_HOLONOMY_DERIVATION.md)



## Supported-zero identity and the exact residue-to-trace map



The original singlet algebra has supported zero as its own multiplicative identity and inverse. Its semilattice adjunctions and the actual invertible heat group are now calculated explicitly. The collision infinitesimal acts nontrivially on perfect residue duality; the Jacobian maps this duality to regular trace. On the actual Weil packet that same map identifies the trace radical with cotangent cohomology, retaining all amplitude jets and all supported endpoint corrections. No proof or disproof of RH is asserted.



- [ZH1–ZH26: intrinsic zero identity, heat flow and residue-generated actions](SUPPORTED_ZERO_HEAT_IDENTITY_DERIVATION.md)

- [RD1–RD31b: integral duality, Jacobian trace, cotangent radical and endpoint compensation](COLLISION_RESIDUE_DUALITY_DERIVATION.md)

- [HZ1–HZ29: supporting specialization maps and local persistence of zeros](supporting_proofs/TAU_HEAT_ZERO_LOCALIZATION_DERIVATION.md)



## Collision prism, integral extension, and supported spectrum



The retained collision algebra now carries the bounded prism with divisor 3+epsilon. Its quotient is exactly (Z/9)[T]/T². The original nilradical quotient is the nilradical (3,T) of this ring, and the divided residue detects its square (3T). The cotangent quotient keeps its larger extension and both connecting maps. All unsupported and arithmetic prime pullbacks are calculated explicitly.



- [EC1–EC48: the complete extension group and both connecting maps](NILRADICAL_COTANGENT_EXTENSION_CLASS_DERIVATION.md).

- [DP1–DP43: the bounded prism, its universal property, and both module specializations](DISTINGUISHED_COLLISION_PRISM_DERIVATION.md).

- [SG1–SG23: the supported spectrum, nilradical, Frobenius kernel, and divided derivation](SUPPORTED_PRISM_SPECTRUM_DERIVATION.md).



These results identify integral infinitesimal data; they do not establish positivity of the complete supported Weil form. The full earlier analytic formula and every support coordinate remain in this reader.



## The actual heat family and the complete arithmetic pairing



The original heat family now has a global rational-test trace with all zero multiplicities retained. Its Cauchy kernel evaluates the full supported-zero endpoints, the archimedean term and the prime sum separately. The actual time derivative introduces products of distinct prime contributions. The complete matrix positivity criterion is equivalent to RH; this equivalence does not assert that its matrices have been proved positive.



- [The global heat zero trace and its exact variation](ACTUAL_HEAT_ZERO_DISTRIBUTION_VARIATION.md).

- [The full supported arithmetic Cauchy pairing and first heat derivative](HEAT_CAUCHY_ARITHMETIC_DERIVATION.md).

- [The exact mixed-prime recurrence at every time-derivative order](HEAT_MIXED_PRIME_RECURRENCE.md).

- [The complete Cauchy–Weil positivity criterion and its proof](CAUCHY_WEIL_POSITIVITY_CRITERION.md).



The earlier finite-fibre, infinitesimal, integral-prismatic and supported-spectrum proofs remain in the collection. The new calculation preserves their distinction between a trace that vanishes and a nonzero infinitesimal element.



## Exact reflection index and the complete local-to-global comparison



The [reflection-index proof](CAUCHY_REFLECTION_INDEX_DERIVATION.md), NI1–32, determines the negative index of the full Cauchy form and every coefficient tail from the actual reflected zero pairs. The [finite-jet calculation](FINITE_JET_COMPLEMENT_AND_HEAT_TRUNCATION.md), FJ1–29, proves the exact exterior comparison, calculates the second and third original heat coefficients, and retains all endpoint corrections. Positivity of the full original form remains unresolved. Both new full proofs and the inspected reproducible diagram are included in the cumulative reader. The preceding algebraic, prismatic, supported-spectrum and arithmetic proofs are preserved.



## One fixed primitive test and the entire prime window



The [prime-operator calculation](PRIME_PROJECTOR_MOBIUS_DERIVATION.md), PM1–41, proves both distinct Fourier support corrections and their exact map into the full Weil formula. The [local estimate](PRIMITIVE_SHORT_SUPPORT_DERIVATION.md), PS1–21, gives a positive translation-difference remainder. The [fixed-test proof](UNIVERSAL_PRIMITIVE_TRANSLATION_CRITERION.md), UP1–35, constructs one compact test whose transform is nonzero at every possible off-critical zero. The [complete arithmetic calculation](PRIMITIVE_PRIME_WINDOW_DERIVATION.md), PW1–22, expresses its entire translated correlation through a fixed-width prime window and an explicit archimedean remainder. Its boundedness is equivalent to RH; that bound remains unresolved. All boundary coordinates and supported-zero labels remain explicit.



## Actual positive-real-time continuation



The complete [real-time proof](REAL_TIME_HEAT_TRACE_DERIVATION.md), RT1–30, strengthens the compact-test variation in this edition: the whole zero trace is smooth for the original real heat time t at least zero, with actual right derivatives at zero. RT16 identifies its first derivative with the full causal arithmetic distribution, and RT20–27 constructs every higher meromorphic derivative receiver. The contact comparison retains the unit and inter-zero terms. These results do not assert a common zero strip for negative or complex time and do not prove the remaining RH inequality. All original supported carriers remain present.





## Proved compact-interval and finite-translation bounds



The complete [compact-interval proof](FIRST_PRIME_FULL_WEIL_COERCIVITY.md), FC1–43, proves full Weil coercivity with constant 11509/600000 through support diameter 19/25, including prime 2 and both original endpoint moments. [FW1–21](FIRST_PRIME_WINDOW_BOUND.md) proves the every-rank matrix bound for centre diameter 583/800 and a strict two-test margin through the next prime gap. The same unchanged test now satisfies its required strict correlation bound for every positive translation through log 256, by [FP1–25](FINITE_PRIME_WINDOW_EXTENSION.md) and the complete [rational prime-power certificate, FPC1–14](FINITE_PRIME_WINDOW_COEFFICIENT_CERTIFICATE.md). [PT1–40](PRIME_TWO_HEAT_TAIL_DERIVATION.md) calculates the surviving mixed channel and proves a strictly negative full actual right heat derivative on the stated short interval after the prime-2 atom ends. These are exact portions of the original bound, retaining supported zero and every original arithmetic coefficient. The uniform inequality beyond log 256 remains unproved.



## Original-zeta Gaussian and affine continuation

The complete additions are [Gaussian translation](ORIGINAL_ZETA_GAUSSIAN_TRANSLATION_RECONSTRUCTION.md), OZG1–55, and [regular affine heat transport](ORIGINAL_ZETA_REGULAR_HEAT_REMAP.md), OZR1–36. Their full proofs, exact source comparisons and reproducible figures are integrated into the cumulative reader. Gaussian test smoothing retains the divergent trivial-zero sector with its finite-cutoff Gamma counterpart. Affine heat transport retains all exceptional local jets and the logarithmic kernel’s exact infinity contribution. Neither supplies the unresolved global arithmetic positivity bound.


## Original endpoint sectors and Gaussian prime boundary

Three complete additions reconstruct the original-zeta endpoint sectors, their augmented inverse and full divisor trace, and the actual Gaussian two-moment prime receiver. [Endpoint return](SECTORIAL_ENDPOINT_ZERO_TRACE_RETURN.md), [full filter inverse](SECTORIAL_FILTER_TRACE_DERIVATION.md), and [Gaussian arithmetic boundary](GAUSSIAN_ARITHMETIC_BOUNDARY_RETURN.md) include full proofs, original sources, retained exceptional factors, and reproducible figures. The arithmetic boundary supplies a proved all-zero residual detector. The full Weil sign and the global RH bound remain unproved.
