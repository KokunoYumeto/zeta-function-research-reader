# The Erdős–Straus workbench: a reader of its results, with proofs

Prepared by Claude (Anthropic), model `claude-opus-5-5` (Opus 5.5), at maximum reasoning effort, 26 September 2026.

`esreader.pdf` (26 pages) is a dedicated reader of the Erdős–Straus workbench of The Clankers (`KokunoYumeto/erdos-straus-foundation` at commit `d20b32e`, and the Zenodo collection 10.5281/zenodo.20401937). It covers the 619-page archive of 31 August 2026, the 67- and 86-page supplements on bounded congruence transport, the 124-page ES/Fable reader and the continuation of 17–23 September. It states:

- the core, with full proofs: the shell criterion for every odd prime, the halved range of the least denominator, the residual-3 and residual-7 shells and their survivors, the reduction modulo 840, the Jacobi-symbol barrier, the least-class function, and four explicit families;
- the record primes of the least-class function and the finite data of the workbench's record-shell conjecture, recomputed;
- a section-by-section map of the archive, with page ranges and each section's bearing on the equation;
- the negative results with their exact scope, the overlaps with the author's other workbenches, and what remains open or was not checked.

Two statements go beyond the workbench:

- each of the four families meets all six classes modulo 840 that the classical reduction leaves open;
- the supplement's no-two-shears theorem holds for every prime p ≢ 2 (mod 3), not only p ≡ 1 (mod 12), and fails for some p ≡ 2 (mod 3).

**Status.** This version has not yet had an independent referee pass. One is planned after 30 September 2026, before the reader is deposited with the workbench's Zenodo collection. Appendix B says what was checked, and how.

Build: `lualatex esreader.tex`, twice. The scripts are in `../checks/es_reader/`; each runs in under 30 seconds with Python 3 and sympy.

The workbench does not claim a proof of the Erdős–Straus conjecture, and nothing in this reader proves or disproves it.
