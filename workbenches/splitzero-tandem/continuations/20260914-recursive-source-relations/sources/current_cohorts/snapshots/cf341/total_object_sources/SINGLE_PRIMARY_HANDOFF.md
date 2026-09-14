# Stable single-primary boundary proof

Main source: `single_primary_boundary_control.tex`.

SHA256: `80dcbc843df223a8b65fd92f728deba1b28e540c748e08dabbdf47a6f28958ea`.

This is one includable source containing the entire complex proof
SP.1–36 and the entire finite-field proof SPF.1–29. It begins with a
section, has no preamble, and uses amsmath, amssymb and mathrsfs.
The accompanying compile harness is not required in the user handoff
when the parent already provides a master document.

## Source pins

- `work/marked_product_boundary_connection_20260913.tex`:
  `6575b8e33ff00bef8b08e214b974b9bd1e966c3bed4b573c5ca274206a69e9fa`.
- `output/Deligne_Mixed_Control_Continuation_2026-09-13/sources/MARKED_PRODUCT_ORIGINAL_NOTE.tex`:
  `40749e2a9d599a322e7b125eb43ad0878a066a51b61da52cc3bb2ffb94cbd841`.
- The actual finite-field companion before exact embedding:
  `single_primary_finite_field/single_primary_finite_field.tex`,
  `538b2da5adf307b54396e46f0848a49c63f0d81072844d191768016255c4fd53`.
- The exact pre-embedding SP-only core reviewed independently:
  `b68000ac12f65176f112c42af282656cee9640bd472f0705d43613bc053e5f52`.

## Verified new calculation and its scope

For the actual complete primary packet h(s)=(s−rho)^m at t=0,
the proof retains s, the ascending monomial basis, Phi(0)=0,
the exact constant c=−(−rho)^(m+1)/(m+1), original ordered contours,
the arithmetic companion action, full Taylor unit, theta source,
support labels and represented zero versus external absence.

It proves the exact Pascal coordinate map, division and connection,
ordered Gamma-valued period matrix, full boundary monodromy,
zero original invariant space and zero finite-cover nilpotent
logarithm, with the irregular scalar retained. It reconstructs
the full arithmetic nilpotent on the marked fibre and gives its
explicit period transport, commutator and finite-cover lattice.
The source-unit map includes the complete multiplication derivative
defect. The metric calculation preserves the source Gram and the
exact enlarged-source relation kernel.

The finite-field section gives actual power-map projectors and an
isomorphism of the specified sheaf with its full Kummer/Gauss
decomposition. The common Artin–Schreier factor remains. It computes
original inertia invariants, Swan conductors, a cover killing all
inertia, and weight one by direct Gauss absolute-square calculation.

This is a completed subcase of the original mixed-support programme.
It does not narrow the overall research task to this subcase. The
source explicitly states that tensor characters can multiply to
the trivial character, so the one-factor vanishing is not passed
to tensor products. No arithmetic Frobenius intertwiner or RH
contradiction is asserted by this calculation.

## Review and validation receipts

- `single_primary_review/MAIN_REVIEW.md` records complete main review
  and a final bounded read of all later unit/remainder changes.
- `single_primary_review/single_primary_complex_review.tex` provides
  the independent full complex derivation.
- `single_primary_finite_field/review/character_review.md` records the
  independent projector, Frobenius, Gauss and ramification audit.
- `single_primary_finite_field/SOURCE_REVIEW.md` provides primary-source
  URLs and exact read locations for cohomological foundations.
- `single_primary_compile.log`: clean 12-page draft-mode compilation,
  no undefined references or layout warnings. No PDF was generated.
- `single_primary_symbolic_checks.json`: seven exact symbolic cases
  with rho indeterminate, checking the full coefficient formulas.
- `single_primary_finite_field/EXACT_CHECKS.json`: 1,872 exact
  original-phase trace cases, by integer cyclotomic polynomial
  reduction, and exact nontrivial Gauss absolute-square checks.
- `single_primary_assembly_receipt.json` records the exact hashes.

The downloaded primary-source book under the child's `sources/`
directory is a local research cache. Do not include that cache in
the public or user source handoff; the proof does not load it.
