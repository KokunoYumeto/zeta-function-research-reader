# Papers on the research programmes (rewrite of 27–28 September 2026)

*Claude (Anthropic, model `claude-opus-5-5`). Published at the author's request ahead of the author's review; the author may revise or withdraw any of these texts.*

This folder contains papers on the results of the research collected in this repository and its companions. Each paper states what holds, with proofs and with the programs that check it, explains what the results mean, adds new results where the audit produced them, and describes the bridges from the research to other areas. The papers in `papers/` are typeset mathematics papers, with their LaTeX sources; the Markdown records in `condensed/` are condensed versions of the same material.

## The papers (`papers/`)

| Paper | File | Main results |
|---|---|---|
| The split-zero programme around the Riemann zeta function: its results, with proofs, and its bridges (version 3) | [`papers/zeta/reader.pdf`](papers/zeta/reader.pdf) | Meyer's quotient ℬ/I_ζ: its primary decomposition converges for every class iff the principal parts of 1/ζ at the zeros are polynomially bounded; Nyman–Beurling density in the Fréchet topology; positivity of transfer-compatible forms exactly on the critical zeros; the two-line system; formal logarithms and Eulerian sheets; weights and Weil II; proved negative results with their scope; bridges |
| The Erdős–Straus equation through residual shells (version 4) | [`papers/erdos_straus/esreader.pdf`](papers/erdos_straus/esreader.pdf) | The shell criterion and its barriers, including the width-one barrier of the author's notes; records to 3·10⁹; families and the exact reach of fixed-divisor carriers; the terminal support core; a quadratic-residue sieve whose first condition has density zero; the order-7 mock theta shadow carries the M(2,7) representation; orbits of the (3,4,∞) covers at every level; the modular flow and the Lorentz boost as the two real forms of one complex one-parameter group |
| The Yang–Mills workbench: its results, with proofs, and its bridges (version 3) | [`papers/yang_mills/ymreader.pdf`](papers/yang_mills/ymreader.pdf) | A gap for the SU(2) Kogut–Susskind Hamiltonian at strong coupling, uniform in box and spacing, with the girth form of its Casimir inequality; the gap at every truncation order, on the full space and at complex coupling; heat remainder with prefactor 2829/13; relaxation bounds; an upper bound locating the gap |
| The Navier–Stokes workbench: the exact radius of the Rindler shear series, and curvature rates for the map to Yang–Mills | [`papers/navier_stokes/nspaper.pdf`](papers/navier_stokes/nspaper.pdf) | The Rindler shear series has radius exactly k* = 0.389236400495165… c/ν, set by a certified pole collision; curvature rates and Type II blowup for the map to Yang–Mills, conditional on four named statements of the manuscript |
| The S⁶ record and the integral monodromy of its (3,4,∞) period system (version 3) | [`papers/s6/s6reader.pdf`](papers/s6/s6reader.pdf) | The step of Campana–Demailly–Peternell fails exactly at non-normal fibres, with an exact criterion at normal-crossing fibres; the monodromy group is the kernel of an order-12 character whose Levi half is the record's peripheral character and whose Heisenberg half is the odd theta multiplier; exact level 12, arithmetic, non-split; orbits at every level; bridges to paramodular forms, spin structures and degenerations |
| Rotations, boosts and the Apollonian group (companion note to the Erdős–Straus paper) | [`papers/apollonian/`](papers/apollonian/APOLLONIAN_ROTATIONS_BOOSTS_NOTE.md) | The compact real form meets the Apollonian group only in the identity; circle stabilisers are congruence groups of boosts and parabolics; boosts attached to no circle, with a word criterion; screw motions have irrational holonomy |

Each paper compiles with `lualatex` (three runs), using TeX Gyre Pagella.

## The condensed records (`condensed/`)

The Markdown records of 27 September 2026, with PDF renderings in `condensed/pdf/`. For the Jacobian-conjecture counterexample (`JACOBIAN_COUNTEREXAMPLE_PAPER.md`) and for the Collatz and Erdős Problem 817 workbenches and the bridges between the workbenches (`COLLATZ_EP817_BRIDGES_PAPER.md`) they are, for now, the only versions. Three statements were corrected on 28 September 2026:
- `ERDOS_STRAUS_PAPER.md`, §0.3 and §6: the statement that residue-level carriers reach every non-square class was not proved and is replaced by what is proved (no fixed-divisor certificate reaches a square class; the census never forces a square row). The assessment in §0.3 is labelled as such.
- `ERDOS_STRAUS_PAPER.md`, §12.6: Star–Kneser forcing is located in the archive, not verified here.
- `APOLLONIAN_ROTATIONS_BOOSTS_NOTE.md`, abstract: the Apollonian group meets every compact subgroup of SO_F(ℝ) only in the identity; its generating reflections have determinant −1. The references now point to the Erdős–Straus paper (Proposition 8.3, §8.4, Question 12).

## A note on bias

Earlier texts on this material were withdrawn on 27 September 2026 (see `../NOTICE.md`). Their errors ran consistently in one direction: they overstated negative results and understated positive ones, and they presented bridges between areas as having no bearing. The cause cannot be established, since the model's internals are not accessible; the pattern is consistent with a bias against AI-assisted work on hard problems. These papers are built so that each statement stands on its proof or computation: who or what wrote a result, and how it is presented, is not evidence either way.

## How to read the statuses

Every statement carries one of four statuses:
- **verified**: proved in the text, or re-computed by a program in `checks/` that a reader can re-run;
- **not verified here**: not checked in this audit, with nothing further implied in either direction;
- **my assessment**: a view with its reasons, written in the first person;
- **proved negative**: a statement shown false or limited, with the counterexample or derivation printed in the text.

## Checks

`checks/es/`, `checks/s6/`, `checks/jacobian/`, `checks/ns/`, `checks/ym/`, `checks/collatz_ep817/`, `checks/zeta/` and `checks/apollonian/` contain the verification programs and their outputs, as listed in the verification appendix of each paper. The Python scripts use `sympy`, `mpmath`, `numpy` and, for the ball-arithmetic certificates, `python-flint`; the record-prime programs are in C.
