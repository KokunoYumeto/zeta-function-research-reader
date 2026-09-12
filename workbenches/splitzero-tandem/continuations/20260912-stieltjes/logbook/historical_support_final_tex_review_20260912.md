# Independent final TeX comparison: historical support branches

Date: 2026-09-12. Reviewer: `/root/arithmetic_moment_exact`. Requested scope: compare the final `historical_support_branches.tex` with the complete B/I/M/A/O mathematics in `work/historical_next_responses_20260912.md`, inspect exact conversion provenance, and identify lost mathematics or typesetting hazards. No source file was edited and no PDF build was started; the root owns the cumulative build.

## Exact reviewed editions

| Artifact | SHA-256 |
|---|---|
| `output/split_zero_rh_tandem_2026-09-12/tex/historical_support_branches.tex` | `1c86f40bf9faa2d166e9c3dff1fb439eaac07cdeefa00b44e64404f28515842e` |
| `work/historical_next_responses_20260912.md` | `b82f645bb92a72d158bf875745483915d91d863512591ab46c623ae6d7fb7389` |
| Converter intermediate Markdown, as pinned in its receipt | `7ffc8dca3bc5b557c3f980c2531ca388fe7aef49a2b5701a5fdee7881cef348b` |

Read the exact converter `work/convert_historical_support_branches_20260912.py`, its receipt `work/historical_support_conversion_20260912/conversion_receipt.json`, and the historical source provenance `output/split_zero_rh_tandem_2026-09-12/sources/historical/next_responses/PROVENANCE.json`. The conversion receipt's report and final-fragment hashes match the current bytes. It selects complete report sections 2, 3, 4, 5, and 5a, converts 207 distinct inline mathematical tokens, supplies explicit carrier and measure-algebra verifications, and imports no KMS theorem. The source-provenance file pins the original SSD edition and complete response ranges separately; it is not falsely presented as the converter receipt.

Also read `work/frame_branch_independent_audit_20260912.md`, including the operator-algebraic continuation audit. That audit checks earlier report editions; this new report supplies the final-edition comparison. No claim of a fresh independent literature search is made.

## Completeness result

The final TeX retains every mathematical statement and proof in the selected B/I/M/A/O sections. In particular:

- B1–B5 retain the exact restricted carrier, amplitude-fixed classification, forward and reverse branch maps, kernel congruence, finite versus arbitrary zero-fibre joins, and the complete product classification for all maps between the original split carriers.
- I1–I10 retain the finite-generation formula for ideal joins, empty join, frame proof, surjective frame map `q`, bounded-lattice section `eta`, adjunction, exact congruence, ideal-point extension, two distinct lifts, descent equivalence, and nucleus fixed-point operations.
- M1–M2 retain the complete supremum construction in the probability measure algebra, atomlessness proof, atom/frame-point bijection and its inverse, the explicit dyadic Zorn branch, its countable continuity failure, the exact distinguished kernel pair upstairs, and the separate construction of such a witness for every ordinary branch.
- A1–A4 retain the atomic observation quotient, full kernel and nonatomic component, both maps of the product decomposition, local complements and units, discrete and atomless cases, the one-element lattice carrier, and the exact ring-reflection composition.
- O1–O4 retain the complete extension from Boolean branches to unital complex-linear star homomorphisms on `L^infty`, the inverse map on projections, uniform-density and contractivity arguments, positivity and norm one, bounded increasing net supremum construction, all three normality implications, the essential constancy proof on each atom, and the exact atomic mass factor `1/mu(a)`.

All 25 tagged display identifiers occur in exactly the same order in report and TeX:

`B1 B2 B3 B4 B5 I1 I2 I3 I4 I5 I6 I7 I8 I9 I10 M1 M2 A1 A2 A3 A4 O1 O2 O3 O4`.

Both contain nine explicitly labelled complete proof blocks, and TeX has nine matching square end markers. The other mathematical arguments, including B2/B5, the two-lift equality criterion, nucleus calculation, every-branch countable witness, and the increasing-net least-upper-bound argument, remain in full prose. These counts corroborate the manual section-by-section comparison; they do not independently prove completeness.

The selected TeX ends with the proved B1/O1/O2 connection. It does not carry over the report's forward pointer into the separately audited KMS lane, and its opening accurately says no external KMS classification or Morita equivalence is used as a theorem in this chapter. This is consistent with the explicitly scoped section extraction.

## Explicit type repairs verified in the final fragment

1. **Exact carrier:** the source remains `{(0,lambda):lambda in L} union {(r,1):r in R}`, not the whole product. The added paragraph proves closure under both restricted operations and identifies `G_B(R)` with `G(R)` in every support case.
2. **Ordinary versus continuous branches:** continuous means preservation of the specified arbitrary joins in the zero-amplitude fibre. The proof does not infer complete primeness from finite semiring operations.
3. **Section category:** `eta` is explicitly a bounded-lattice map and generally not a frame map. The quotient `q` is a frame map. Their precise relations are the adjunction, `q eta=id`, the two lifts, and the nucleus, all retained.
4. **Congruence and exact descent:** the branch extension on the ideal frame remains distinct from composition with `q` until arbitrary-join preservation is proved. Equalities on principal ideals do not replace equality on all ideals.
5. **Choice and measure hypotheses:** classical set theory and Zorn are stated explicitly. Completeness is proved for the actual probability measure algebra; no completeness claim about arbitrary unqualified measure algebras is imported.
6. **Trivial support target:** in the atomless observation the one-element target lattice has carrier isomorphic to the ordinary ring by the explicit map `Psi(r,*)=r`. The composition in A4 maps both original zeros to ordinary zero but does not identify them inside the original source. The earlier nontrivial split pair retains them as distinct.
7. **Boolean factor units:** the intervals use local tops `b_at,b_na` and local complement `u↦b∧¬u`; this avoids treating an interval as globally unital with top one.
8. **Full operator algebra:** O1 is proved for every `L^infty` function through uniform extension, not just its projections. O2 retains all bounded increasing nets, with the actual finite-measure supremum construction; normality is not silently replaced by an unproved sequential condition.
9. **Atomic mass:** O4 keeps `mu(a)^(-1)` and proves why a function is constant almost everywhere on that atom before evaluating it.

No sign, coordinate, denominator, exceptional carrier, or stated hypothesis was lost in the inline conversion.

## Static TeX review and layout scope

The current TeX has:

- 353 opening and 353 closing inline mathematical delimiters;
- 34 opening and 34 closing display delimiters;
- two matching `enumerate` environments and one matching `cases` environment;
- no raw Markdown backticks and no remaining non-ASCII mathematical characters;
- prefixed heading labels (`historical-support-...`), avoiding generic heading-anchor collisions;
- declared chapter-local equation identifiers, so their manual B/I/M/A/O names are not presented as globally unique cross-reference keys.

The current main preamble already supplies `tightlist`, `hyperref`, `xurl`, `amsmath`, and `amssymb`, covering the converter's `path`, `nolinkurl`, `square`, and mathematical display commands. The long hashes use `nolinkurl`, and paths use `path`.

No malformed command or delimiter hazard was found. The long unbroken classification displays B1, B5 and O1, and the long set/ideal identities I1 and I10, remain candidates for width inspection in the root's actual cumulative build. This review does not claim zero overflow or completed visual QA: those require the resulting compiler log and rendered PDF. The theorem/proof comparison itself passes on the pinned source bytes.
