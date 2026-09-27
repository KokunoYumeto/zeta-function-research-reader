# The Yang–Mills workbench — paper, version 3

LaTeX source of *The Yang–Mills workbench: its results, with proofs, and its bridges*, version 3 (27 September 2026), a paper on the Zenodo record 10.5281/zenodo.22883643, *SU(2) lattice Yang–Mills: vacuum, energy, spectral bounds and continuum investigations*, the Yang–Mills part of the workbench `KokunoYumeto/yang-mills-interacting-workbench` (read at commit `fa79faf`). Prepared from an audit of the workbench by Claude (Anthropic), model `claude-opus-5-5`.

Version 3 is the text of version 2 with its framing corrected. It adds a section on the open directions with my assessment, and it states what each typed map of the side branches carries. No theorem, proof or number changed; Appendix C lists every change.

The main results: the strong-coupling gap bound for the Kogut–Susskind SU(2) Hamiltonian, uniform in the box and the spacing, for g² ≥ 3.6836 given the computed inputs of orders 3–5, and for g² ≥ 3.9781 with the order-2 inputs recomputed here; the girth form of the gauge-invariance Casimir inequality; the gap at complex coupling, on the full space, and an upper bound; the heat remainder with prefactor 2829/13; and the relaxation bounds into the complementary physical space.

Versions 1 and 2 and the audit notes they cite are in the branch history at commit `a90d9e5b`, folder `contrib/claude-ab/grind_20260925/` (`ym_reader/`). The scripts cited in the paper are in `../../checks/ym/`.

Build: `lualatex ymreader.tex` three times. The scripts need Python 3 with sympy, mpmath and numpy.

All results of the record hold at a fixed lattice spacing and strong bare coupling. The workbench does not claim a continuum mass gap.
