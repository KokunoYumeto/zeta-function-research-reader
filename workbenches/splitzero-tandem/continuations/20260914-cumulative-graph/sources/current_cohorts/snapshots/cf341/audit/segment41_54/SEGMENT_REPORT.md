# Complete authoritative audit of shared-thread U0041–U0054

This directory supplies the full proof-source reports, verbatim user provenance, independently reviewed new calculations, and machine-checked original-record coverage for the 43 visible messages in `output/tau_f1_transcript_audit_2026-09-13/sources/audit_segment_U0041_U0054.md`. The source is 226,155 bytes, includes message lines 1–7810 and a terminal blank line, and has SHA-256 `4f6b4fd318308e561710bb24cd0f35b1b70b6507ba6be54b6f6d9b044ddbd1c4`.

The mathematics and user corrections were read completely in disjoint full-message ranges by a coordinated audit. No short conversation summary or later assistant compilation substitutes for this source. The verification script independently matched the complete body, role, node/message ID, and chain ordinal of all 43 messages against `transcript_records.json`. This is recorded in `checks_and_record_coverage.json`; the message texts were not inferred from headers or search hits.

## Complete reading and proof files

| Full range | Messages | Reader | Full report |
|---|---:|---|---|
| U0041–U0045, lines 1–2481 | 11 | audit41_45 | `part41_45.md` |
| U0046–U0050, lines 2482–4891 | 18 | audit46_50 | `part46_50.md` |
| U0051–U0052, lines 4892–6332 | 7 | audit51_52 | `part51_52.md` |
| U0053–U0054, lines 6333–7810 | 7 | purity_program | `part53_54_and_conormal_proof.md` |

The source-only independent checks are retained in `geometry_check.md`, `trace_scratch.md`, and `review_conormal.md`; the symmetric frontier proof was independently checked by the auditor's verifier and its separate composition-count verifier. The new mathematical conclusions are proved in full in their respective reports, rather than being premises supplied by these tests.

## The actual user correction and ensuing construction

U0041 requires typed morphisms carrying the whole original split construct and **infinite quotient** through every equation. U0042 identifies the distinct receiving supported zero e as central and asks what e and tau must do to decide RH. U0043 explicitly rejects merely repeating Weil II over its original base and instructs using that machinery on the tau base; U0044–U0045 insist that this corrected work be done. The complete U0043 text includes exploratory rhetorical discussion; it does not assert an actual off-line zeta zero. U0046 again requires using the existing formalized construct in the actual arithmetic cohomology. Later messages authorize continued mathematical work while formalization proceeds in parallel. Exact user texts and locators are preserved in the reports and verbatim files.

The assistant source does construct the absolute pointed-monoid/blueprint base, its structural maps with `G(Z)->Z` intact, a marked theta chart over that base, the original arithmetic quotient cohomology, a calculated adjoint object, residue maps into that adjoint, support-preserving tensor products, actual theta representative/boundary maps, positive source-induced interpolation metrics, exact residue dual transfer, the actual rank-two relation control, joint total-degree boundary layers, the signed symmetric cochain projector, finite sum-line pushforward, its relative algebra and matrix-valued arithmetic weight, its full nilpotent fibres and duality, and conormal derivative maps recovering the arithmetic Jacobian. They must not be described as absent. Each report states their exact categories, maps and coefficients.

The source's finite-field discussion initially gives fibrewise transport of Deligne's genuine upper/dual-lower/image operations. The corrected tau program subsequently computes the corresponding characteristic-zero arithmetic objects. Its adjoint construction does not, in these messages, establish the weight theorem on those objects: A1523 explicitly distinguishes its computed algebraic adjoint from involutive local Verdier duality or a global prime-sensitive geometric model. A1721, A1771, A1829, A1859, A1912 and A1959 explicitly record the unestimated arithmetic quantity. This is a finding from the original complete messages; it does not erase the constructions just enumerated.

## New proved restrictions inside these original objects

These formulas are the index to the full proofs, not replacements for them.

1. **Actual rank-two arithmetic relation control.** `part46_50.md` proves, in the original source Gram and with all multiplicities,
   \[
   \operatorname{Tr}(G_n^{-1}W_n)=0,\qquad
   \epsilon_n\ge\sum_{\rho\in Z}m_\rho|\Re\rho-\tfrac12|
   \]
   for a reflection-stable actual packet at every finite relation level. Its full proof uses the original invariant-subspace inclusions, induced Grams and projections, not a diagonal replacement of A. An actual quartet at distance delta and common multiplicity m therefore requires `epsilon_n>=4m delta` at every level. The report also constructs the correct map to the reflected packet when the input packet is not reflection stable.

2. **Actual symmetric interpolation frontier.** Section 7 of `part51_52.md` proves, on the genuine signed symmetric cochain image and its unscaled orbit coordinates,
   \[
   \Gamma_{k,M}\operatorname{Tr}\bigl(G_M^{\rm sym}
   (\mathcal C_{M+1}^{\rm sym}-\mathcal C_M^{\rm sym})\bigr)
   \ge\binom{k+d}{d+1}\sum_{i=1}^d(\Re\rho_i-\tfrac12)^2,
   \]
   \[
   \frac{\det\mathcal C_{M+1}^{\rm sym}}
   {\det\mathcal C_M^{\rm sym}}
   \ge1+\frac{\binom{k+d}{d+1}\sum_i(\Re\rho_i-\tfrac12)^2}
   {\Gamma_{k,M}}.
   \]
   Here all original algebraic multiplicities occur in the list of d roots; Gamma is the exact positive recurrence cost proved in A1859. The proof retains the nilpotent contribution as a nonnegative off-diagonal term, the full frontier inclusion, its source Gram and orbit factors. It also proves the exact signed frontier correlation and `Gamma lambda_sym>=k^2 delta^2`. No incompatible upper asymptotic is assumed.

3. **Original conormal/Jacobian map, including all fibres.** C1–C19 of `part53_54_and_conormal_proof.md` calculate the entire image and kernel of the A1959 map `delta_S:I/I^2≅E^k->E` and its arithmetic-unit multiple, as well as the actual mixed Jacobian source derivative. For an actual quartet with common multiplicity m, the ordered image ranks are `(4m)^k-(4(m-1))^k` and `4^k`. On the actual signed symmetric image they are
   \[
   \binom{4m+k-1}{k}-\binom{4(m-1)+k-1}{k},\qquad
   \binom{k+3}{3}.
   \]
   Full kernels, local monomial directions, factors m, local units, derivative coefficients 1/k, and the original support-zero maps are proved explicitly.

4. **Intrinsic symmetric arithmetic trace and same-sum fibres.** C14–C25 construct the exact Reynolds-trace and residue/Jacobian comparisons. They preserve the distinct intrinsic local occupation weights `D_n=product_i binom(m+n_i-1,n_i)` and the ordered orbit weights, joining them by an explicit central invertible coefficient map B. The resulting intrinsic trace has negative index
   \[
   \frac12\left[\binom{k+3}{3}-f_k\right],\quad
   f_k=0\ (k\text{ odd}),\quad f_k=k/2+1\ (k\text{ even}),
   \]
   and its entire nilpotent radical is retained. An exact isomorphism of the nonradical quotient to the invariant mixed-Jacobian image is proved, together with the original source representative `(product log x_i)P(D)(Theta phi_*)^{tensor k}`. The negative idempotent is not confused with its derivative jet when multiplicities exceed one.

   In particular the original symmetric square contains two distinct full occupation factors with the same sum eigenvalue 1, whose idempotent difference has trace value `-2m^2`. C22–C25 compute all such balanced fibres, including their nilpotents. These calculations make essential use of the relative algebra constructed by A1912; replacing the fibre by its sum eigenvalues alone would lose these exact arithmetic directions.

## Verification and corrected issues

`check_conormal_and_coverage.py` passes 24 exact conormal/image dimension cases and 32 exact quartet-inertia cases, including balanced-fibre counts. It independently matches all 43 complete visible messages to the original JSON records. Its calculations verify combinatorial identities and maps; it does not invent or certify an off-line zero. No Lean session was started.

Independent review caught and corrected three genuine exposition/type issues in the new conormal proof: reflection stability and the dagger descent are now stated explicitly; the induced Jacobian-image isomorphism has its **invariant image** as codomain; and no automatic Koszul cancellation is asserted. The iterated residue is explicitly ordered and the supertrace factor remains separate. It also corrected the claim that a negative idempotent itself lies in the Jacobian image: the exact source observation is `J B u`, and its residue pairing with u gives the negative trace. These corrections are recorded in the review.

No original-source edit, global manuscript edit, publication, or RH truth claim was made by this audit. The strongest new quantitative restrictions and full relative-fibre restrictions above are ready for the parent task's integration into the reconstructed program. The original problem remains active; this audit has not established a contradiction or a disproof of RH.
