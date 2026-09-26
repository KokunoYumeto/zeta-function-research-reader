# The Yang–Mills workbench: a reader of its results, with proofs

Prepared by Claude (Anthropic), model `claude-opus-5-5` (Opus 5.5), at maximum reasoning effort, 26 September 2026.

`ymreader.pdf` (25 pages) is a dedicated reader of the Zenodo record 10.5281/zenodo.22883643, *SU(2) lattice Yang–Mills: vacuum, energy, spectral bounds and continuum investigations*. That record is the Yang–Mills part of the owner's workbench `KokunoYumeto/yang-mills-interacting-workbench`, read at commit `fa79faf`. The reader says:

- which of the record's 43 files, from five versions dated 8–21 September 2026, is current and which are superseded. The record's front `README.md` still describes the first version.
- what each document claims, and on which regime;
- the strong-coupling gap bound for the Kogut–Susskind SU(2) Hamiltonian, with its proof. The bound is uniform in the box and the spacing, and holds for g² ≥ 3.6836 given the computed inputs of orders 3–5, or for g² ≥ 4.0187 with independently checked inputs.
- the heat-flow results of the latest edition. Every constant of the box-independent heat remainder is re-derived, and the evenness and Cauchy steps are proved. The benchmark table for relaxation into the whole complementary physical space is recomputed exactly from the stated inputs.
- the earlier editions, the Jacobian-map, Navier–Stokes and S⁶ branches, the obstructions with their exact scope, and what remains open.

The reader also adds two small results. The heat bound holds on every circle R < α₅, not only R = 1/55. The quantum line's first volume-uniform gap κ(3 − 512ξ) follows from the order-1 bound.

**Status.** This version has not yet had an independent referee pass. One is planned before the reader is deposited with the record. Appendix B says what was checked, and how.

**Build.** Run `lualatex ymreader.tex` twice. The scripts are in `../checks/ym_reader/`.

All results of the record hold at fixed lattice spacing and strong bare coupling. The workbench does not claim a continuum mass gap, and nothing in this reader bears on that problem.
