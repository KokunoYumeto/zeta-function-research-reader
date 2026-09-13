# Arithmetic frontier estimates and symmetric tensor control

An additive research continuation of the original split-zero/tau-base arithmetic
programme. Start with RESEARCH_NOTE.md or the rendered index.html. The source input
is PR #14 at `3bff1b2bd87dfa2592f65c5ccc231f6ee9541dfc`.

The principal new map is the actual relation-graph isomorphism `b=Tplus-R F`.
It supplies the Gram, relative boundary control, and source primitive of the next
layer. The signed symmetric cochain projector retains every repeated eigenline,
with its complementary trace kept. No arithmetic purity theorem is claimed.

Run finite regression checks:

```sh
python check_frontier_control.py --json checks/normal.json
python -O check_frontier_control.py --json checks/optimized.json
python check_frontier_control.py --negative-control
```

The last command is expected to fail. The tests use exact Gaussian moment models
and polynomial quotient algebras, not computed zeta roots or verified analytic
integrals. The written proofs and analytic dependency boundary are in the note.
