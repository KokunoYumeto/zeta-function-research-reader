# The Erdős–Straus workbench: a reader of its results, with proofs

Prepared by Claude (Anthropic), model `claude-opus-5-5` (Opus 5.5), at maximum reasoning effort. Version 3, 27 September 2026: the author's unpublished notes added (Section 6), after two independent referee passes. Versions 1 (26 September) and 2 (27 September) are in the branch history.

`esreader.pdf` (47 pages) is a dedicated reader of the Erdős–Straus workbench of The Clankers. It covers `KokunoYumeto/erdos-straus-foundation` at commit `d20b32e` and the Zenodo collection 10.5281/zenodo.20401937, including:

- the 619-page archive (title page dated 30 August 2026);
- the 67- and 86-page supplements on bounded congruence transport;
- the 124-page ES/Fable reader;
- the continuation of 17–23 September.

It states:

- **The core, with full proofs:**
  - the shell criterion, which is the archive's divisor-shell bijection (Theorems 9.1 and 9.64), with the halved range of the least denominator added;
  - the residual-3 and residual-7 shells, and the fact that their survivors lie in the six hard classes modulo 840 (archive Corollary 10.7);
  - the classical reduction modulo 840;
  - the Jacobi-symbol barrier, with a sharper group form and a partial converse;
  - the least-class function;
  - fixed-divisor families, of which the archive's four explicit families are instances.
- **Recomputed data:** the record primes of the least-class function, now to 3·10⁹ by two independent programs, with no new strict record; and the finite data of the workbench's record-shell conjecture.
- **A section-by-section map of the archive,** with page ranges and each section's bearing on the equation.
- **The exact scope of the supplement's no-two-shears theorem.** It holds for every prime p ≢ 2 (mod 3). No weaker congruence hypothesis suffices. It fails only on a minority of the primes p ≡ 2 (mod 3): a set of upper relative density at most 0.335, and 5.24% of them below 10⁷.
- **A limit of the archive's carrier census.** Every carrier it uses is a polynomial identity on a residue class. By the Schinzel–Yamamoto obstruction, the 2,759,345,613,832,500 square rows of its final domain (1/1024 of it) can never be forced.
- **The author's unpublished notes (Section 6, new in version 3):**
  - the "terminal core" S₈₄₀ × Q₁₁ × Q₁₉ × Q₂₃ is proved to be exactly the support-zero core of the notes' certificates. Modulo 840·11·19·23, 550 further classes are covered by no single identity of Salez's seven families, so the core is not the residual locus;
  - nine quadratic-residue conditions on a counterexample. Two of them, from p+2 and 2p+1, certify the record prime 8,803,369. The referee added eight more;
  - the visible-box principle, with new shells R = 31, 47, 59, 71, 311;
  - the width-one barrier, facts on non-coprime and ramified shells, and the scope of the notes' identities and locks;
  - errors found in the notes, and their connections. Among these, the notes' "mixed mock functions" are Ramanujan's order-7 mock theta functions.
- **The rest:** the negative results with their exact scope, the overlaps with the author's other workbenches, and what remains open or was not checked.

**Status.**
- An independent Claude instance refereed version 1 on 27 September 2026. It reported five major and ten minor findings and seven implied results. Each was verified before it was applied, and one of the referee's numbers was corrected. Its report and programs are in `../checks/es_reader/referee/`, and the verification scripts in `../checks/es_reader/referee_verify/` and `../checks/es_reader/esr_referee_checks.py`.
- Section 6 rests on six reading passes over the author's notes and on this reader's own programs, in `../checks/es50/`. A second independent referee reported three major and fifteen minor findings and implied results, all verified and applied. Its report is in `../checks/es50/referee/`; the full record is note `50_`. Nothing here has had a human specialist review. Appendix B says what was checked, and how.

**Build.** Run `lualatex esreader.tex` twice. The Python scripts need Python 3 and sympy. The two C programs need a C compiler; the 3·10⁹ run takes about two minutes on two cores.

The workbench does not claim a proof of the Erdős–Straus conjecture, and nothing in this reader proves or disproves it.
