# The Erdős–Straus equation through residual shells — paper, version 4

LaTeX source of *The Erdős–Straus equation through residual shells. The workbench and the author's notes: their results, with proofs, and their bridges*, version 4 (27 September 2026). Prepared from an audit of the Erdős–Straus workbench of The Clankers and of the author's notes of April–June 2026 by Claude (Anthropic), model `claude-opus-5-5`.

Version 4 is the text of version 3 with its framing corrected, and with new results:

- density zero of the primes that satisfy the quadratic-residue condition from p + 1 (Proposition 6.8);
- the shadow of the notes' order-7 mixed mock vector carries the modular representation of the minimal model M(2,7) after conjugation and the twist by the character of η³ (Theorem 6.15, verified exactly in ℚ(ζ₁₆₈));
- the order-5 block carries the Fibonacci modular data (Proposition 6.16);
- the orbits of the (3,4,∞) monodromy covers at every level (Theorem 5.1, Corollary 5.2);
- the modular flow of a state on M₂(ℂ) and the Lorentz boost of the notes' Lorentzian geometry as the two real forms of one complex one-parameter group (Proposition 8.3), with two further propositions on the notes (8.1, 8.2).

Appendix C lists every change from version 3, including the corrections of content. Versions 1–3 and the audit notes they cite are in the branch history at commit `a90d9e5b`, folder `contrib/claude-ab/grind_20260925/` (`es_reader/`, note `50_`). The scripts cited in the paper are in `../../checks/es/`.

Build: `lualatex esreader.tex` three times. The preamble uses fontspec and unicode-math with TeX Gyre Pagella, TeX Gyre Pagella Math, TeX Gyre Heros and DejaVu Sans Mono, with a luaotfload fallback list for rare glyphs.

The workbench does not claim a proof of the Erdős–Straus conjecture, and nothing in this paper proves or disproves it.
