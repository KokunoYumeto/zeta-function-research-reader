# Deligne weight control and arithmetic return maps

This local research repository contains the full weight-control reconstruction from Deligne's Weil II, its exact comparison with the recovered arithmetic and original Riemann zeta, and the preceding programme proofs on which those comparisons depend.

- [Focused complete reconstruction](DELIGNE_WEIGHT_CONTROL_FULL.md), with [TeX](DELIGNE_WEIGHT_CONTROL_FULL.tex).
- [Cumulative proof reader](RECONSTRUCTION_AND_WEIGHT_FULL.md), with [TeX](RECONSTRUCTION_AND_WEIGHT_FULL.tex).
- [Source coverage and transcription discrepancies](DELIGNE_FULL_READING_LOG.md).
- [Exact figure](deligne_weight_mechanism.png) and [reproducible source](draw_deligne_weight_mechanism.py).
- [Continuous original-source lift](proofs/GLOBAL_SHIFTED_ZETA_LIFT.md), [figure](global_shifted_lift.png), and [figure source](draw_global_shifted_lift.py).
- [The CC coefficient sheaf](proofs/CC_SHEAF_ORIGINAL_ZETA_COHOMOLOGY.md), [supported localization](proofs/CC_SUPPORTED_LOCALIZATION_AND_WEIGHT_MAPS.md), and [descended conic](proofs/CC_DESCENT_CONIC_AND_ZETA.md).
- [Exact Schwartz image and continuous inverse](proofs/EXACT_SCHWARTZ_SUMMATION_IMAGE.md), with its [independent complete derivation](proofs/EXACT_SCHWARTZ_IMAGE_INDEPENDENT_CHECK.md). The ordinary first cohomology is already the full Hausdorff original-zeta quotient.
- [Prime endpoint actions and earlier FR comparison](proofs/CC_ENDPOINT_DEFECT_ACTIONS.md), with the [complete prior FR source](sources/ORIGINAL_ZETA_RETURN_FR.tex).
- [Actual sphere sheaf and normal quotient](proofs/CC_SPHERE_PULLBACK_AND_NORMAL_DIRECTION.md), [map diagram](sphere_normal_receiver.png), and [reproducible source](draw_sphere_normal_receiver.py).
- [Exact inverse and endpoint diagram](exact_source_and_endpoints.png), with its [reproducible source](draw_exact_source_and_endpoints.py).
- [Actual connecting-map and weight comparison](proofs/CC_ACTUAL_WEIGHT_LIFT_COMPARISON.md), [coefficient-complex diagram](actual_sheaf_lift.png), and [reproducible source](draw_actual_sheaf_lift.py).
- [Derived direct image and winding](proofs/CC_DERIVED_DIRECT_IMAGE_AND_WINDING.md), with [diagram](derived_winding.png) and [reproducible source](draw_derived_winding.py).
- [Continuous duals and support maps](proofs/CC_CONTINUOUS_DUAL_INDEPENDENT.md), with the [original-zeta residue comparison](proofs/ORIGINAL_ZETA_RESIDUE_DUAL_AND_SUPPORT_MAPS.md).
- [Strong dual topology and completed residues](proofs/CC_STRONG_DUAL_TOPOLOGY_AND_JETS.md), with the [dual and residue diagram](continuous_dual.png) and [reproducible source](draw_continuous_dual.py).
- [Continuous support-dual sheaf](proofs/CC_CONTINUOUS_SUPPORT_DUAL_SHEAF.md), with its [current diagram](support_dual_current.png) and [reproducible source](draw_support_dual_current.py).
- [Ramified trace and completed original-zeta receiver](proofs/CC_RAMIFIED_TRACE_AND_RESIDUE_ACTION.md), with its [degree-factor diagram](ramified_trace.png) and [reproducible source](draw_ramified_trace.py).
- [Ordinary Verdier dual and its continuous comparison](proofs/CC_VERDIER_SUPPORT_INDEPENDENT.md), with the [exact defect and spectral comparison](dual_comparison_defect.png) and [reproducible source](draw_dual_comparison_defect.py).
- [Literal continuous-current inclusion and its Verdier target](proofs/CC_CURRENT_TO_VERDIER_COMPARISON.md), preserving both pole Gysin maps, endpoint blocks and mirror semilinearity.
- [Polynomial spectral lifting through that actual comparison](proofs/CC_POLYNOMIAL_SPECTRAL_LIFT.md), with its [explicit correction diagram](polynomial_spectral_lift.png) and [reproducible source](draw_polynomial_spectral_lift.py).
- [Original meromorphic divisor and full generator map](proofs/CC_GENERATOR_COKERNEL_AND_ORIGINAL_DIVISOR.md), with the [entire primal parameter family](proofs/PRIMAL_GENERATOR_FAMILY_INDEPENDENT.md), [diagram](primal_generator_family.png), and [reproducible source](draw_primal_generator_family.py).
- [Polynomial weights in the actual localization row](proofs/CC_LOCALIZATION_POLYNOMIAL_WEIGHTS.md), with the [full-kernel and boundary diagram](localization_spectral_weights.png), [reproducible source](draw_localization_spectral_weights.py).
- [Complete-module separation and the full normal inverse](proofs/CC_GLOBAL_MULTIPLIER_SEPARATION.md), with the [diagram](global_multiplier_separation.png), [reproducible source](draw_global_multiplier_separation.py).

- [Complete source extension and both actual obstruction components](proofs/CC_FULL_SOURCE_OBSTRUCTION_DECOMPOSITION.md), with the [exact annihilator and whole-module resolvent](proofs/CC_NORMAL_EXTENSION_ANNIHILATOR.md), [map diagram](full_source_obstruction.png), [reproducible source](draw_full_source_obstruction.py).

- [Actual nearby cycles and specialization](proofs/CC_LOCAL_NEARBY_CYCLES_AND_SPECIALIZATION.md), [local dual arrows and global pairing](proofs/CC_LOCAL_VANISHING_DUAL_ARROWS.md), and [signed Gysin receivers](proofs/CC_RESIDUE_GYSIN_RECEIVER_INDEPENDENT.md), with [diagram](local_residue_receiver.png), [reproducible source](draw_local_residue_receiver.py). The complete RTT, GTAH, GIQ and PCJ supporting proof files are included in `proofs`; their reading and use scopes are recorded separately.

`python build.py` verifies the individual proof hashes and rebuilds both Markdown readers. When Pandoc is available it also regenerates TeX. The figure scripts use Matplotlib, listed in requirements.txt; they write their PNG and SVG beside the script. The parent edition build report records PDF compilation and its exact inspection scope. The other drawing scripts retain the preceding reproducible figures; the historical clock-reader script is preserved for its figure-generation source, not as the current cumulative builder.

The supporting datum is τ〈Z1; no Z2〉. No arithmetic zero, addition, metric or coordinate is assigned to it. Calculations on its retained stalk, recovered arithmetic scheme, geometric fibres and costalks have explicitly different domains. Every completion factor, prime-power repetition, unit contribution and branch counter used in the receiving maps is retained. The CC coefficient-sheaf receiver and its exact comparison to the analytic zero quotient are constructed in the named proof. No RH proof or identification with Deligne's geometric weight-separation cross is claimed.

The continuous arithmetic-equivariant splitting on the full original Mellin quotient retains its explicitly constructed entire multiplier, all zero multiplicities, and quotient seminorm estimates. The translated extension has source-weight interval (0,2) and kernel-weight interval (2,4). The germ and whole-source eigenfunction boundaries retain their own exact receivers. The geometric additions derive the actual Tate class, the continuous comparison map, the explicit descended conic and its ramified fibre, and the CC coefficient sheaf's Fourier lift and supported localization maps. These constructions retain their different domains; no independently selected analytic boundary is presented as an obstruction to the user's geometric programme. All earlier proof parts remain in the cumulative reader.

The human author sources are cited at their public source records, not redistributed in this programme-source edition. The Deligne French witness is a local transcription, not original author TeX. The original Connes–Consani, Connes and Reich source identities, hashes, inspected ranges and reading limits remain recorded. ArXiv access is not treated as general redistribution permission. The included ORIGINAL_ZETA_RETURN_FR.tex is a prior programme proof, with its own human-source bibliography.

The private user transcript and unrelated audit material are not in this delivery repository. They remain preserved in the separate task logbook. Publication identity and verification are recorded by the parent edition README.
