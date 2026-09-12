# Orthogonal theta boundaries and rank-two control

Additive continuation of draft PR #11 at `d37eade4f9e6a82c1a88aeff710a3b851a34eb49`. New work is under the repository owner's SplitZero programme, with AI assistance. No original scalar definitions, formal modules, workflows or dependency pins are changed.

The note selects representatives by finite spans of the actual `D^j phi_*` inputs. Their control matrix has rank at most two, their next-level Gram update has rank one, and the exact source-kernel coordinate is retained by the original internal quotient. The arithmetic quotient, jets, extension class and finite trace are unchanged.

The supplied other-session homotopy theorem is correct; its Lean draft remains uncompiled. This contribution uses its integration in PR #11, rather than duplicating it as a new theorem.

Files:
- `RESEARCH_NOTE.md`: definitions, written proofs and exact comparison maps.
- `check_boundary_control.py`: thirteen finite exact regression tests and a deliberately failing control.
- `check-results.json`: local successful result.
- `VALIDATION.md`: reproduction and scope.

The conversation delivery additionally contains the longer numbered LaTeX/HTML note, reading record, full logs, programme state and an exploratory computation of four actual theta-moment rows. That decimal computation is not an interval certificate.

A key result is that unscaled `G_m` and `W_m` both tend to zero while the actual cohomological packet survives. The relative control formula and the retained Hilbert/jet graph are therefore part of the result. No global purity, RH or GRH assertion is made.

Formalization handoff: retain both cochain equations in the homotopy theorem. Suitable finite targets are the Schur-complement minimum identity, the rank-two contraction and its two-column factorization, the rank-one quotient-metric update, and the original support-changing lifts. Their finite checks do not certify the analytic theta input or density theorem. The existing failed tau-chart build is not relabelled successful.
