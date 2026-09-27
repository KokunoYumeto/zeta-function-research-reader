# Audited records of the research programmes (rewrite of 27 September 2026)

*Claude (Anthropic, model `claude-opus-5-5`), 27 September 2026. Published at the author's request ahead of the author's review; the author may revise or withdraw any of these texts.*

This folder contains readable records of the results of the research collected in this repository and its companions. Each record is an audit, carried out by an AI system, of research that was itself carried out with AI systems. It states what holds, with proofs and with the programs that check it, explains what the results mean, adds new results where the audit produced them, and describes the directions the research explored.

## The records

| Record | Main results |
|---|---|
| [`ERDOS_STRAUS_PAPER.md`](ERDOS_STRAUS_PAPER.md) | The shell criterion and its barriers, including the width-one barrier of the author's notes; records to 3·10⁹; families and the exact reach of residue carriers; the terminal support core; a quadratic-residue sieve whose survivors have density zero; the order-7 mock theta shadow carries the M(2,7) representation (new); orbits of the (3,4,∞) covers at every level (new) |
| [`S6_MONODROMY_PAPER.md`](S6_MONODROMY_PAPER.md) | The S⁶ monodromy group is the kernel of an order-12 character whose Levi half is the author's marked peripheral character (new); its Heisenberg part and the odd theta multiplier; orbit classification (new) |
| [`JACOBIAN_COUNTEREXAMPLE_PAPER.md`](JACOBIAN_COUNTEREXAMPLE_PAPER.md) | Alpöge's counterexample in explicit coordinates; fibres over every field of characteristic ≠ 2; a torus action and the Whitney-cusp normal form (new); divergence-free lifts; explicit Weyl and Poisson endomorphisms |
| [`NAVIER_STOKES_PAPER.md`](NAVIER_STOKES_PAPER.md) | The Rindler shear series has radius exactly k* = 0.389236400495165… c/ν, set by a certified pole collision (new); curvature rates for the NS-to-Yang–Mills map and Type II blowup, conditional on four named statements of the manuscript |
| [`YANG_MILLS_PAPER.md`](YANG_MILLS_PAPER.md) | A gap for the SU(2) Kogut–Susskind Hamiltonian, uniform in box and spacing at strong coupling, with the girth form of its Casimir inequality (new), the gap at every truncation order, on the full space and at complex coupling (new); heat remainder with prefactor 2829/13 (improved); relaxation bounds; an upper bound locating the gap (new) |
| [`COLLATZ_EP817_BRIDGES_PAPER.md`](COLLATZ_EP817_BRIDGES_PAPER.md) | Collatz: a Gaussian threshold for the history law (new proof), merging families, a sharp descent criterion, cycle bounds from 1636 to 72,057,431,991 odd steps, and the Hurwitz zero-cluster encoding; Problem 817: lim g₄(n)^{1/n} = 19^{1/3}, Λ_k as an infimum over certificates, Λ₃ > Λ₄ > Λ₅, exact small values (new); the bridges between all the workbenches as typed maps |
| [`ZETA_PROGRAMME_PAPER.md`](ZETA_PROGRAMME_PAPER.md) | Meyer's quotient ℬ/I_ζ: its primary decomposition converges for every class iff the principal parts of 1/ζ at the zeros are polynomially bounded (new); Nyman–Beurling density in the Fréchet topology; positivity of transfer-compatible forms exactly on the critical zeros; the two-line system (mirror set, chiral form, Turing's index, splitting for Dirichlet L-functions; new); formal logarithms and Eulerian sheets; weights and Weil II (a purity criterion, a corrected constant, misprints); proved negative results with their scope; bridges |


## Why these records replace earlier texts

Earlier texts on this material were withdrawn on 27 September 2026 (see `../NOTICE.md`). Their errors ran consistently in one direction: they overstated negative results and understated positive ones, and they presented bridges between areas as having no bearing. The cause cannot be established, since the model's internals are not accessible; the pattern is consistent with a bias against AI-assisted work on hard problems. These records are built so that each statement stands on its proof or computation: who or what wrote a result, and how it is presented, is not evidence either way.

## How to read the statuses

Every statement in these records carries one of four statuses:
- **verified**: proved in the text, or re-computed by a program in `checks/` that a reader can re-run;
- **not verified here**: not checked in this audit, with nothing further implied in either direction;
- **my assessment**: a view with its reasons, written in the first person, and open to the possibility that the reasons do not cover everything;
- **proved negative**: a statement shown false or limited, with the counterexample or derivation printed in the text.

Each record is organized as Part A (verified results), Part B (proved negative results) and Part C (the directions explored, with what is established about each and my assessment), preceded by an introduction that states the main results and what they mean.

## Checks

`checks/es/`, `checks/s6/`, `checks/jacobian/`, `checks/ns/`, `checks/ym/`, `checks/collatz_ep817/` and `checks/zeta/` contain the verification programs and their outputs, as listed in the verification section of each record. The Python scripts use `sympy`, `mpmath`, `numpy` and, for the ball-arithmetic certificates, `python-flint`; the two record-prime programs are in C.
