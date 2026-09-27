# Four workbenches and where they meet: a reader of their results, with proofs

Prepared by Claude (Anthropic), model `claude-opus-5-5` (Opus 5.5), at maximum reasoning effort. Version 2, 27 September 2026. Version 1 of 25–26 September is in the branch history; it was published as the file `00-claude-opus-5-5-workbench-reader.pdf` of the Zenodo record 10.5281/zenodo.22977243.

`wbreader.pdf` (38 pages) reads four public workbenches of KokunoYumeto at fixed commits:

- `erdos-straus-foundation` at `d20b32e`;
- `collatz-workbench` at `caf04ff`;
- `erdos-problem-817-workbench` at `dbd0a93`;
- `yang-mills-interacting-workbench` at `fa79faf`, which also holds the Navier–Stokes, S⁶ and Jacobian-map material.

It states each workbench's results, proves the central ones in full, gives the negative results with their exact scope, and maps the intersections between the workbenches and with the split-zero zeta programme.

**What changed in version 2.** Dedicated readers were written afterwards for three of the Zenodo records behind this reader (`../es_reader/`, `../ym_reader/`, `../s6_reader/`). Each had one independent referee pass. Their findings that bear on statements made here were checked again against the sources and applied. Appendix A lists every change.

- **Erdős–Straus.** Three results that version 1 credited to the audit are proved in the workbench's 619-page archive, which version 1 had not read:
  - part (b) of the shell criterion, with its count (archive Theorems 9.1 and 9.64);
  - the classes of the two-shell survivors modulo 840 (Corollary 10.7);
  - the reduction modulo 840 through the shells R = 3 and R = 7 (Theorem 10.6).
  The survivor proposition is now stated modulo 840, with the step modulo 5.
- **Yang–Mills.**
  - The order-2 gap theorem holds with audited inputs for g² ≥ 3.9781, not only for g² ≥ 4.0187; this covers the workbench's benchmark g² = 4.
  - The heat prefactor 67896/169 can be replaced by 2829/13, and YM-02 is conditional on the order-3 to order-5 inputs.
  - A garbled sentence about the girth constant is rewritten.
  - The order-5 replay is described as one that the publication intake did not repeat.
- **S⁶.** The value set of the cubic in S6-5 is exact. S6-1 to S6-4 are no longer labelled "located", since their proofs were not seen.
- **Thresholds.** Two thresholds that the intersections section quoted as 4.02 and 3.68 are now given as 3.9781 and 3.6836; 3.68 had been rounded in the unsafe direction.
- **Further results.** The Erdős–Straus and Yang–Mills sections now end with the results the dedicated readers add, each with a pointer to its proof.

**Checks.**
- The statements carried over are checked by the scripts of the dedicated readers:
  - `../checks/es_reader/esr_referee_checks.py`;
  - `../checks/ym_reader/ymr_referee_checks.py`;
  - `../checks/ym_reader/ym_order2_threshold.py`.
- The archive's Theorems 9.1, 9.64 and 10.6, Corollary 10.7 and Proposition 10.2 were re-read at the cited pages for this version.
- The checks of version 1 are in `../checks/workbenches/`.

Nothing here has had a human specialist review.

**Build.** Run `lualatex wbreader.tex` twice.

Nothing in this reader proves or disproves the Erdős–Straus conjecture or the Collatz conjecture, or establishes or refutes a mass gap for the continuum Yang–Mills theory. None of the workbenches claims to.
