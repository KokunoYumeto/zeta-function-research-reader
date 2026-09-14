# Bounded final challenge: original four-window and holonomy quantities

The continuation is `actual_compatible_bounds.tex` (HC1–HC15), to be included after `actual_holonomy_counterfactual.tex`. It uses the hypothetical actual divisor of `g=2ξ` throughout. No calibration polynomial, substituted arithmetic measure, assumed upper estimate, or proposed generic criterion is introduced.

## Exact retained lower residual

HC1–HC5 retain the two original length-q windows, the special q−1 boundary, every contraction factor, every phase, both actual norm ratios, and the complete trace lower bound. The result is the **equality**

`B_k = 4q log(D_h k) + R_k`,

where R_k is the sum of five displayed nonnegative pieces: full contraction penalties; phase contribution; excess of the actual rank-two control above L; the norm-window saving; and the trace saving. The constants are those of CJ.16–18, explicitly reproduced. In particular `D_h=δ/(2 C_h^win)<1/108`.

Threshold four is inherited. The authoritative segment already states both separate original windows at lines 4202–4228. The exact local source is `tex/consecutive_first_window_join.tex`: CJ.12–13 (lines 228–246) give the products and penalties; CJ.15–19 (lines 258–342) supply the original envelope, full norm constants, and both window lower estimates. This continuation does not attribute that threshold to itself.

## New actual four-window upper bound and its explicit numerical range

The original AU.24–31 upper calculation estimates a remainder representative from degree 2q−1. Its inverse geometric-series argument extends to degree 2q with all root repetitions. This adds exactly the needed final degree; the original map, measure, mass and raw-jet phase factors are proved in HC6–7.

For the original constants C_N of that argument,

`B_k ≤ q log C_(2q−1) + q log C_(2q)`.

With the original scalar expression U_k from AU.31, the new explicit actual bound is

`B_k ≤ Uhat_k = 2 U_k + q log 20`.

The coefficient factors are `A_(2q−1)^2 ≤ (2q/9)256^q` and `A_(2q)^2 ≤ (40q/9)256^q`. The remainder stays below degree q, so its original moment cutoff and U_k(T) are unchanged. Independent review confirmed the extension and constants. The exact adjacent A-ratio is retained in HC7; no false assertion that this ratio is below 20 at q=2 is used. The actual quartet range has q≥16.

Consequently the full original residual R_k lies in the explicit interval

`max(0, −4q log(D_hk)) ≤ R_k ≤ Uhat_k − 4q log(D_hk)`.

This interval has **strictly positive width for every k≥3**, proved without inserting numerical arithmetic moments: Uhat≥2a q², `a=αD+log256>1`, q>(2k), D_h<1, and log k≤k. Its width divided by q² tends to `2(αD+log256)>0`.

For the inherited Gamma comparison on the **same χ**, retain `T_N=V_N^ar/V_N^Γ` and the signed original correction

`DeltaΓ_k = log(T_(q−1)T_q/(T_(2q−1)T_2q))`.

Its exact compatible interval is

`max(0,4q log(D_hk)) − BΓ_k ≤ DeltaΓ_k ≤ Uhat_k − BΓ_k`.

No sign for DeltaΓ is asserted. This is a range permitted by the proved numerical bounds in original quantities. It is not a construction of an actual zero or a proof that every point is arithmetically realizable.

The exact source reads for this extension were `tex/arithmetic_volume_upper_route.tex`, lines 147–161 (AU.10–11) and 364–543 (AU.24–31), together with the already audited full source dependency. All substitution factors are explicit in HC6–7: x=(S−c)/(iT), source measure T m_k(Tx) dx, monic relation (iT)^−q χ(c+iTx), raw jets (iT)^d, and quotient determinant factor T^−q(q−1). These factors cancel only in the stated ratios.

## Additional actual relation between holonomy energy and endpoint volume

For each original phase and degree, HC12 uses the actual derivative-source energy

`J_N^D = ||D_(L,θ) R_(N,θ) G_(N,θ)^−1/2||_HS²`,

the actual adjacent generalized metric eigenvalue beta_N, and the actual endpoint contraction `e_N=log(V_N/V_(N+1))`. It proves

`L²/2 ≤ E_N ≤ (1+sqrt(beta_N))² J_N^D`,

`e_N ≥ 2 log max(1, L/sqrt(2J_N^D)−1)`.

All inverses exist at admitted degrees. `J_N^D≥(k/2)²q>0` follows from the original twisted derivative. The quotient minimum at N+1 proves the upper estimate; no commutation of adjacent metric matrices is assumed. Its moments have the exact degree cutoff 2N+2.

The endpoint weights 1,2,...,2,1 reconstruct the literal phase four-volume. HC13 sums the required energy-dependent endpoint losses with those exact weights. The source's proved phase Gram comparison then gives an actual upper budget `Uhat_k+2q log((1+η)/(1−η))`; averaging the original phase Grams instead gives error `2q log(1/(1−η²))`. For fixed η these are O(q), and do not erase the positive quadratic interval above. The full lattice residual and extreme lower bound 2k²δγ of HT17–18 remain present.

These statements relate actual derivative moments to the original endpoint volumes. They do not assume an upper growth estimate for those moments. Independent algebra review confirmed the factors, logarithm direction, domains, and endpoint multiplicities.

## Testing the sharper upper expressions in the supplied records

The supplied programme also retains exact finite determinant and relation-trace upper expressions. None is accompanied by an evaluated hypothetical arithmetic quartet or a proved asymptotic upper coefficient below four. This is a claim about the supplied proof records, not a theorem forbidding further estimates.

HC15 explicitly extends the actual lower-envelope determinant comparison to both original windows. Its upper expression U_(nu,k) has the **exact** error

`U_(nu,k)−B_k = log(V_(2q−1)/V_(2q−1)^nu) + log(V_(2q)/V_(2q)^nu) ≥ 0`.

The source moments in its numerator go through 2q; the explicitly defined comparison moments go through 4q. The proof uses the same affine remainder fibres and Loewner monotonicity, with the original unitful observation unchanged. The moment/Hadamard or optimized raw-minor upper expressions in the source add their specific nonnegative determinant losses; they do not evaluate these errors at the hypothetical packet.

The recovered relation trace/area material expressly lacks uniform bounds at segment lines 4723–4736 and 4795–4797. The final holonomy source retains the computed weighted-source eigenvalue κ and period choice; it does not prove a favourable κ-growth estimate. Its close gluing norm concerns C−C_theta and does not bound the differentiated theta boundary by the same number. The period curvature/finite-field degree statements bound the exact objects reconstructed in AUDIT.md; they do not supply an opposing estimate on the arithmetic source energies of HT14 or HC12.

Thus no supplied proved actual upper estimate closes the counterfactual by contradiction. The explicit scalar comparison demonstrates a nonempty allowed numerical range; the sharper finite expressions remain unevaluated at the hypothetical arithmetic packet. This does not claim the full arithmetic programme is impossible or that an off-line zero exists.

## Original cochain correction and validation

The independent parent reviewer found a genuine original-grading error in the first HT13 draft. It has been corrected in the author file: F_h has degree one, phi_h has degree zero, and the tensor primitive is degree k−1 with coefficient (−1)^(i−1). The tensor differential contributes the same sign, yielding the positive ith boundary. Two malformed square exponents in HT14 have also been corrected. The numeric energy and lattice inequalities were unaffected. The corrected original module hash is `74f8b45052c6f10d3d0ecd8a861336e2b66b19fd94ed26921889c22bf932c449` at this correction stage.

The combined wrapper `compile_compatible_check.tex` compiles the original corrected module and this continuation. Parent handles integrated PDF visual QA. This lane has run no Lean and performed no remote publication or global edits.

Final independent read by `balanced_audit` checked the complete written HC1–HC15 against CJ.9–19 and returned no mathematical correction. It verified the exact five-piece residual, the strict all-k interval width, metric sandwich order, all phase/endpoint weights, and the final comparison moment cutoffs. The final combined build has ten pages and no overfull boxes, undefined references, or warnings.

The subsequent independent `absolute_base` review accepted the mathematics and requested two final refinements. The original mass integral is now explicit before HC6. New HC12a proves the exact rank-one identity `e_N=log beta_N`, with the full `X*X`/`XX*` similarity and eigenvalue calculation; HC12 remains valid with this strengthening. The receipt is `INDEPENDENT_REVIEW_RECEIPT.md`. The stable final HC source SHA-256 is `a723e14fefb7ecb3b7b79a122c8f98cc631e42fdd30feda64f7446bf9872a141`.
