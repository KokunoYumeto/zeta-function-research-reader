# Independent review of the combined metric control and empty-packet endpoint

Reviewer: `/root/independent_review`; independent ACM9–13 subreview: `/root/independent_review/cr_spectral_check`. Date: 2026-09-13.

Both parent-owned source files were read in full: `combined_original_metric_control.tex` (ACM1–13) and `empty_packet_endpoint.tex` (EPE1–2). The original AW1–9, SP1–8 and MCF1–5 source paragraphs were consulted directly for their exact source spaces, metrics, coefficient inclusions, densities, masses, Fourier coordinate and endpoint convention. This is a bounded integration review, not a fresh audit of every inherited module.

## Mathematical checks

The reference identity has the original constant `c_{1/4}=sqrt(2 pi)` and retains the convolution mass. The AW-to-SP relation map is the original coefficient inclusion after multiplication by chi. Consequently the projection formulas, the signed four-endpoint operators and the metric derivative coincide literally on `P_{2q}`. The separate AW source isometry retains its original type, and its observation difference and kernel in ACM8 follow from the original injective cohomology and cyclic maps.

The full spectrum is `0^q,1^2,2^{q-1}`. The two rank projection sums give exactly `c_{q+2}-c_q+2 sum_{j=1}^{q-1}(c_{2q+2-j}-c_j)`; for `q=1` this is `c_3-c_1`. The intersection projection is bounded above by either positive window operator, so subtracting it preserves positivity and gives the trace-norm upper bound `4q-2s`. The sum of squared eigenvalues gives `8q-4-2 Tr(UW)`, and finite-dimensional Cauchy–Schwarz gives the stated second trace-norm bound. The midpoint subtraction uses the exactly vanishing trace of `U-W`. These facts prove both pointwise bounds for the same signed derivative.

All norms in that argument are in the original metric. The smooth positive Gram family and its inverse give continuous eigenvalues; the intersection dimension is Borel by the continuous-matrix rank strata. Thus the pointwise minimum is measurable and integrable. The relative-eigenvalue formula preserves its ordering since its derivative with respect to the positive relative eigenvalue is strictly positive. Its integral is the original logarithm, proving ACM12–13 without a universal ordering assumption on the two refinements. No new determinant-control result is incorrectly attributed to this integration.

For the empty packet, `F_1=Theta(phi_*)` belongs to the original source and has Mellin transform `g`. Its equation under `1(D)` is literal identity. Therefore `H(D)F_H=F_1` includes the empty endpoint in the original packet transition. The named source function is not a new quotient class: `E_1=0`, all maps with that zero amplitude domain are zero, and the source inclusion is precisely `Theta V -> B_H`. No inverse unit is imposed at that stage.

## Notation correction and hashes

The sole correction identified by both reviewers is to write `Tr((U_x-W_x)^2)` in ACM10, putting the square inside the trace parentheses. The original text `Tr(U_x-W_x)^2` can be read as the square of the trace; the proof and constant require the trace of the square. No algebraic constant or inequality error was found.

Fully read initial ACM SHA-256: `282e64fbc8b3a410eaf736053ad02c9881bf515526445059c8291e1eeac5c269`.

EPE mathematical PASS, SHA-256: `2c404f0a98922caadfc43dca541cbb218072f900166971c51e50e65af76e2b02`.

The corrected ACM10 line was read directly. Replacing only that parenthesis correction in memory reconstructs bytes whose SHA-256 is exactly the fully read initial ACM hash above; no other source change occurred. Both reviewers verified the corrected notation.

Final ACM mathematical PASS, SHA-256: `c2caa5a1bdd6fcc02794f4e112fd783cebb465048bd696002d417ca4b1550289`.

EPE's hash was rechecked and remains the PASS hash above. No outstanding issue remains in either bounded source. Compilation and cumulative artifact integration are parent-owned production checks.
