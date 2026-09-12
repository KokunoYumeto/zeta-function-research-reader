# Tau boundary-layer formalization

Owner-workbench continuation of PR #12, based on the immutable checked head
5d2772ea0a16d177ac3e01ff70394b90ba95a232. No prior mathematical source is modified.

- `RESEARCH_NOTE.md`: complete finite boundary proofs, exact source-to-Lean scope,
  reflection and determinant refinements, Hilbert-density/tail theorem, and
  independent omitted-integer-tail estimate.
- `check_theta_norms.wl`: the independent arithmetic-input numerical calculation.
- `NUMERICAL_RECORD.json`: its result and explicit limitations.
- The five Lean modules and their manifest/checker are in `formal/splitzero`.

The dedicated `SplitZero boundary layer` workflow checks the new sources and
rechecks the prior tau/derived/structural declarations. A successful run on an
exact commit is required; read the PR validation record rather than assuming
that this README is a proof certificate. Local authoring execution was not
available; Lean execution is performed on GitHub Actions.

The full source analytics and all-n monic orthogonal recurrence are not implied
by the local finite-input Lean interface. The note marks analytic arguments,
formal interfaces, and numerical evaluations separately. No private transcript,
external source corpus, font file, or credential is included.
