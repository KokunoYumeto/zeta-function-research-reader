# Canonical endpoint restriction control

Read `index.html` for the mathematical continuation; it is a self-contained
MathML reader. `NOTE.tex` and `RESEARCH_NOTE.md` are editable sources.
`HANDOFF.md` gives bounded targets for the parallel formalization.

The new object is the explicit adjoint of the original degree transport,
T_(i,j)=K_i G_j, with source restriction R_i T=P R_j. Its determinant and
singular-value spectrum calculate the existing endpoint-volume loss. A positive
full-jet minor expansion and convergent trace-moment enclosures provide finite
upper certificates, retaining the original e-valued theta relations.

Run the finite checks:

```sh
python check_restriction_control.py --json checks/normal.json
python -O check_restriction_control.py --json checks/optimized.json
```

`--inject-failure` must exit nonzero and is used as a negative control.
Fixtures are explicit finite Gaussian polynomial examples, not zeta packets.
No new Lean or arithmetic interval certificate is claimed. Uniform control of
the actual growing-degree restriction spectra remains unproved.

This package makes no remote repository changes.
