# Public-readable marked-product edition

This HTML/TeX edition presents the marked tau-base external packet family,
its explicit theta-source comparison, and the signed arithmetic/Gamma
four-endpoint calculation. It is a locally prepared derivative dated
13 September 2026. Its presence in a local package does not assert remote
publication, a new Lean formalization, or a uniform arithmetic upper bound.

Read `index.html` for the equations and proofs; `NOTE.tex` is the complete
editable mathematical source. This is an HTML/TeX edition without a pertinent
PDF. No PDF was created merely to occupy a preview slot. An eventual hosted
edition should link directly to its online HTML reader; a ZIP is an offline
download, not a readable preview.

## Source identity and attribution

The unchanged source archive is `Tau_Marked_Product_Four_Endpoint_2026-09-13.zip`.
Its exact SHA-256 is
`c26683faaa76aeb6c59beabcee0e8d70f5a34d45ff9ec9fd8bccd66ef79b2d73`.

The original `NOTE.tex` SHA-256 is
`40749e2a9d599a322e7b125eb43ad0878a066a51b61da52cc3bb2ffb94cbd841`.
The clarified `NOTE.tex` in this edition has SHA-256
`61765baf1013e1e80bc2a487ef30db6e7490a11392c5a08a1cc23c8f6ae89329`.

This remains a continuation of the source's Split-Zero programme. The
substantive inherited mathematical sources, exact source pins, theta
conventions, source/coefficient-defect distinction, and Deligne attribution
remain in `NOTE.tex`, `HANDOFF.md`, and `SOURCE_REVIEW.md`. Standard polynomial
division, tensor-complex signs, Schur complements, and midpoint estimates
are not presented as globally novel mechanisms. No attribution name was
inferred from a local account or filesystem.

## The four mathematical clarifications

1. Before (38), explicitly choose an auxiliary prime different from the
   characteristic and a **nontrivial** additive character for the
   Artin–Schreier sheaf. The smooth-leading-form calculation and its
   finite-field scope are unchanged.
2. In (49), (50), the row defining (52), and the relation-shell expressions
   in (58), consistently use `y` for the sum-frequency variable. The unrelated
   deformation parameter `u`, packet coordinates, and operators are unchanged.
3. After (64), say that the relative difference is self-adjoint and the
   relative arithmetic Gram is positive self-adjoint in the stated metric.
   The bound does not assume the difference is positive. Its coefficient
   `(8q+4)/(12m^2)` and all original metric factors are unchanged.
4. After (77), state the inherited positive-exponent log-coordinate Fourier
   transform and the full negative-exponent target basis. They give the
   displayed **plus** sign. That sign is not changed, and this convention is
   explicitly distinguished from the transform of `phi` in (10).

`PUBLIC_NOTE_CHANGES.diff` gives the complete literal mathematical-source
diff with package-relative labels. There are no other changes to `NOTE.tex`.
In particular, supported zero remains distinct from absence, the full Taylor
unit and nilpotent jets remain, no measure is normalized, and the ordinary
endpoint degrees remain `q-1,q,2q-1,2q`. The missing uniform arithmetic estimate
is still unproved; this edition asserts neither RH/GRH nor failure of the
marked programme.

## Public packaging and privacy changes

- Historical `INTAKE.json` mounted locators are replaced by basenames only.
  Every recorded byte count, line count, and source SHA-256 is unchanged.
  Its two `NOTE.tex` entries remain distinguished by their hashes. These are
  historical records, not claims of a fresh read of every inherited source.
- The two inherited negative-control logs retain their traceback content and
  intended failure, with the old mounted source path replaced by the
  package-relative `checks/check_math.py`.
- `SOURCE_REVIEW.md` explains that provenance transformation; `README.md`
  identifies this derivative and links to this record.
- The fully inspected derivative `build_reader.py` only rebuilds HTML, CSS,
  and its rendering receipt, using explicit UTF-8 and LF output. Automatic
  external-input harvesting, predecessor scanning, manifest generation, and
  source-archive writing were removed. This prevents a reader rebuild from
  overwriting historical provenance or the original archive. The reader
  navigation adds this record and the fresh finite-check receipt.
- `index.html` and `RENDER.json` were regenerated from the clarified note.
  The local renderer reports native MathML with zero equation fallbacks.
  Static checks verify the equation identifiers, local resource links,
  MathML well-formedness, and deterministic rebuild. No browser screenshot
  or visual-layout certification is claimed.
- `PUBLIC_FILE_CHANGES.json` records original and derivative hashes for every
  retained original payload, including byte-identical files. `MANIFEST.json`
  hashes every file in this edition except the manifest itself; a separate
  local seal records the manifest and archive hashes.

The complete selected text bodies were privacy-reviewed. No private account name,
account path, credential, external-input mount, or attribution inferred from
the machine is intentionally included. Public replay logs use package-relative
source paths and identify the interpreter by basename and version only.

## Explicitly excluded patch material

The source archive's `INTEGRATION.patch` is preserved privately but excluded
from this edition. Its SHA-256 is
`71e409697b8ce6becd89fa69b157e186613dcb933cbd439e9d43e0c7932294f6`.
It was not applied or accepted as a reviewed integration diff. The complete
mathematical note, reader, source records, and both mathematical scripts are
included, so excluding this patch does not remove the substantive research.

The associated inherited `PATCH_CHECK.json` is also excluded, because its
patch-application receipt does not establish review or application of that
patch in this derivative. Its SHA-256 is
`c56fa472ed53ac99eb83458c855a636e17208b07538c95b620370803212e584e`.

The source `MANIFEST.json` is replaced by a manifest of the actual public
edition rather than presented as if unchanged hashes described this derivative.
The original archive, original manifest, and original payloads are preserved.

## Execution and limits

`checks/check_math.py` is byte-identical to the source checker, SHA-256
`06c490c2b9674bb50a4668db58b5a2da75bb983111fa5490884c081e454a2e05`.
`checks/PUBLIC_REPLAY.json` and `checks/public-replay/` record fresh bounded
normal, optimized, and both intended negative-control runs on this edition.
The inherited execution record and logs remain separately identifiable.
The negative control tests the explicitly false identification of represented
zero with absence; it is not a general soundness test of every future change.

The numerical script and its inherited results are unchanged. They were
inspected, not rerun for this edition, and remain non-interval quadrature
illustrations without certified root multiplicity, rounding, tail, or final
sign. The finite symbolic checks do not establish the missing uniform bound,
an arithmetic Frobenius transfer, or a new primary-source or Lean audit.
