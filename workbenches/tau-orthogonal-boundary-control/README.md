# Orthogonal theta boundaries and rank-two control

Additive continuation of draft PR #11 at `d37eade4f9e6a82c1a88aeff710a3b851a34eb49`. New work is under the repository owner's SplitZero programme, with AI assistance. No original scalar definitions, formal modules, workflows or dependency pins are changed.

The note selects representatives by finite spans of the actual `D^j phi_*` inputs. Their control matrix has rank at most two, their next-level Gram update has rank one, and the exact source-kernel coordinate is retained by the original internal quotient. The arithmetic quotient, jets, extension class and finite trace are unchanged.

The supplied other-session homotopy theorem is correct. Its attached uncompiled-draft status is now superseded by successful PR #12 at `5d2772ea0a16d177ac3e01ff70394b90ba95a232`. The actual source and complete successful job log `103535438942` were read. This contribution uses PR #11's analytic integration and the precise formal interfaces now checked in #12, rather than duplicating those results. See `COORDINATION_UPDATE.md` for the certificate's boundaries.

Files:
- `RESEARCH_NOTE.md`: definitions, written proofs and exact comparison maps.
- `check_boundary_control.py`: thirteen finite exact regression tests and a deliberately failing control.
- `check-results.json`: local successful result.
- `VALIDATION.md`: reproduction and scope.
- `COORDINATION_UPDATE.md`: current formalization status and inspected source/job references.

The conversation delivery additionally contains the longer numbered LaTeX/HTML note, reading record, full logs, programme state and an exploratory computation of four actual theta-moment rows. That decimal computation is not an interval certificate.

A key result is that unscaled `G_m` and `W_m` both tend to zero while the actual cohomological packet survives. The relative control formula and the retained Hilbert/jet graph are therefore part of the result. No global purity, RH or GRH assertion is made.

Formalization handoff: retain the actual `cochainHomotopyEquiv` and quotient/retraction interfaces now checked in #12. Suitable new finite targets are the Schur-complement minimum identity, the rank-two contraction and its two-column factorization, the rank-one quotient-metric update, and the original support-changing lifts. Their finite checks do not certify the analytic theta input or density theorem. Earlier failed runs remain failed historical runs; the new source revision has its own inspected successful run.
