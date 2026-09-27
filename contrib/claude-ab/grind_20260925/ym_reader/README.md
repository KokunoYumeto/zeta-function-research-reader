# The Yang–Mills workbench: a reader of its results, with proofs

Prepared by Claude (Anthropic), model `claude-opus-5-5` (Opus 5.5), at maximum reasoning effort. Version 2, 27 September 2026, after one independent referee pass. Version 1 of 26 September is in the branch history.

`ymreader.pdf` (31 pages) is a dedicated reader of the Zenodo record 10.5281/zenodo.22883643, *SU(2) lattice Yang–Mills: vacuum, energy, spectral bounds and continuum investigations*. That record is the Yang–Mills part of the owner's workbench `KokunoYumeto/yang-mills-interacting-workbench`, read at commit `fa79faf`. The reader says:

- which of the record's 43 files, from five versions dated 8–21 September 2026, is current and which are superseded. The record's front `README.md` still describes the first version.
- what each document claims, and on which regime;
- the strong-coupling gap bound for the Kogut–Susskind SU(2) Hamiltonian, with its proof. The bound is uniform in the box and the spacing. It holds:
  - for g² ≥ 3.6836, given the computed inputs of orders 3–5;
  - for g² ≥ 3.9781 with the independently recomputed order-2 inputs, which covers the workbench's benchmark g² = 4.
- the heat-flow results of the latest edition. Every constant of the box-independent heat remainder is re-derived, and the prefactor is sharpened from 67896/169 to 2829/13. The benchmark table for relaxation into the whole complementary physical space is recomputed exactly from the stated inputs, and then sharpened.
- the earlier editions, the Jacobian-map, Navier–Stokes and S⁶ branches, the obstructions with their exact scope, and what remains open.

Further results, each with a proof, most found by the referee pass and checked:

- the gap persists at complex coupling, so the ground-state projection is analytic on a disk whose radius does not depend on the box;
- an upper bound on the gap: for g² ≥ 13 the gap lies in [2.9047, 3.00024]κ, and it has no first-order term;
- the gap on the full, not gauge-invariant, space: at least a quarter of the physical bound;
- the exact per-link constant of the Casimir inequality;
- the kinetic-row constants 30 and 48, derived and sharpened;
- the heat bound on every circle R ≤ α₅;
- the quantum line's first volume-uniform gap, which follows from the order-1 bound.

**Status.** An independent Claude instance refereed version 1 on 27 September 2026. It found no error that invalidates a stated result, and reported 2 major and 14 minor findings and results A–K. Each was verified before it was applied. Its report and programs are in `../checks/ym_reader/referee/`; the verification scripts are `../checks/ym_reader/ymr_referee_checks.py` and `ym_order2_threshold.py`. The referee's numerical order-3 computation is reported, not repeated. Nothing here has had a human specialist review. Appendix B says what was checked, and how.

**A later rounding correction.** On 27 September a rounding in §9.1 was corrected. With the referee's order-3 values, the conditional threshold is g² ≥ 3.7154 (exactly 3.71533…), not 3.7153 as first written.

**Build.** Run `lualatex ymreader.tex` twice. The scripts need Python 3 with sympy, mpmath and numpy.

All results of the record hold at fixed lattice spacing and strong bare coupling. The workbench does not claim a continuum mass gap, and nothing in this reader bears on that problem.
