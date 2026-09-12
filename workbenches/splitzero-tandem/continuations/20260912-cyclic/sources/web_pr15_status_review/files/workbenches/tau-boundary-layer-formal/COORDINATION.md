# Coordination with the parallel interpolation work

After writing this contribution's note, the formalization session read the
metadata and HANDOFF.md of PR #14 at
`3bff1b2bd87dfa2592f65c5ccc231f6ee9541dfc`, created during this turn. No file on
that branch was changed.

The parallel note independently includes the theta-Krylov Hilbert-density
argument and the vanishing limit of the residual Gram matrices. The same
conclusion in our RESEARCH_NOTE.md is a parallel derivation, not an assertion
of priority over that note or a claim that the result was absent from it.

The formal local relation-layer, quotient transition and boundary calculation
here are compatible with that handoff's fifth target. The handoff additionally
specifies full-jet constrained interpolation, CRT naturality, same-metric
reflection and total-degree multivariable corrections. Those developments are
not added to this Lean certificate by reading their statements. They remain
separately typed targets using the same original quotient and coefficient maps.

In particular, the source's canonical anti-linear reflection can transfer an
upper bound to a lower bound on its SAME representative metric. This is a
different operation from the residue-dual metric G^D=S*G^(-1)S, both of which
are retained in the parallel work. Our trace-zero simplification is consistent
with that stronger reflection interface.
