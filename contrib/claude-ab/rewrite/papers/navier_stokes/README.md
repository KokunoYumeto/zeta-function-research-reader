# The Navier–Stokes workbench — paper

LaTeX source of *The Navier–Stokes workbench: the exact radius of the Rindler shear series, and curvature rates for the map to Yang–Mills* (27 September 2026). Prepared from an audit of the workbench folder `navier-stokes/` of `KokunoYumeto/yang-mills-interacting-workbench` (commit `fa79faf`) by Claude (Anthropic), model `claude-opus-5-5`. The construction it audits is OpenAI's manuscript *Finite Time Blowup for Navier–Stokes*, whose main theorem is imported and not verified here.

Main results:

- the pole collision of the Rindler shear sector, certified in Arb ball arithmetic (Theorem 2.1);
- the hydrodynamic dispersion series has radius of convergence exactly k* = 0.389236400495165… c/ν, with the mode purely damped up to it (Theorem 2.2, computer-assisted, re-verified with a second interval library);
- coefficient asymptotics and the boundary sum (Corollary 2.3);
- conditionally on four named statements of the manuscript, the curvature rates for the map to Yang–Mills and Type II blowup with ‖u‖_{L³} ≳ τ^{−4h/3} (Theorem 3.1, Proposition 3.2).

This paper is the typeset version of the audit note `51_` and of its condensed record. The note is in the branch history at commit `a90d9e5b`, folder `contrib/claude-ab/grind_20260925/`. The scripts cited are in `../../checks/ns/`; `fig/fig_collision.py` computes the figure.

Build: `lualatex nspaper.tex` three times.
