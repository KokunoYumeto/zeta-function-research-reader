# Stable primary cyclic lattice proof

Main includable file: tensor_primary_cyclic_lattice.tex.

SHA256: 7371F26AA05099D14D72D55999C9AF8605125A20DA017876B3E129775E2EFAAE.

The file begins with a section, has no preamble, uses standard amsmath/amssymb notation, and contains TCL.1–37 with full proofs. It is stable for embedding after the original tensor module.

## Exact source coverage

- TCL.1–5: the already specified local coefficient map, its actual prime localization, full original Taylor unit/inverse, original cyclic coefficient maps and their exact sum-action intertwining.
- TCL.6–13: primitive divided-power containing lattice, explicit splitting, original factorial image, full-unit transport, saturation, covariant action and complete matrix in the unchanged original monomial coordinates.
- TCL.14–20: exact integer factorial depths, coordinate quotient maps, original reduced cyclic kernel/image, distinct source/ambient nilpotency indices, all containing-lattice chains, exact Tor connecting maps and retained terminal scalar.
- TCL.21–27: the literal MFC chain carrier; scalar injection from Z/p^L, exact extension/contraction on the principal p-power subchain, all sum/intersection/product laws, support-preserving semiring map and the actual quotient-coordinate annihilator map. A bottom annihilator label does not replace its nonzero coefficient vector.
- TCL.28–32: the full lost source shift, original boundary-character masks, full-unit conjugation, exact period/source comparison, and the simultaneous depth/character labels through quotient and Tor.
- TCL.33–36: the actual quartet CRT polynomial's divided difference gives an inverse of every prime p≤k at stage k. The directed ring containing all retained split stages contains Q and has no positive-characteristic residue field. These are statements about that complete split stage; no extension of the already specified local specialization is invented.
- TCL.37: the last nonzero reduced cyclic image direction is an exact new kernel direction after reduction, and is character zero on the explicitly proved infinite congruence subsequence. It is not claimed to be an l-adic sheaf vector.

The finite-field sheaf calculation remains the sibling module. The present characteristic-p coefficient reduction never sets a nonzero integer equal to zero in characteristic-zero l-adic scalars.

## Validation and reviews

- Clean 10-page draft compile; no box or LaTeX warning.
- 25 exact packet cases; 164 exact prime-packet cases; independent symbolic divided-difference identities in degrees 1–9.
- General proofs are in the main TeX; finite checks and all cases are in check_cyclic_lattice.py and EXACT_CHECKS.json.
- Independent complete proof: review/cyclic_lattice_independent_review.tex, PCLR.1–29, clean five-page draft compile; SHA256 80F48C8DD0897BF945189BE4BA2B8D60C3E27B1F1D899846AD9221BD540EDC90.
- Independent complete main read and final hash pin: review/MAIN_REVIEW.md.
- Parent also completed a full mathematical read through TCL.37 and accepted all formulas and proofs.
- Durable provenance and choices: WORK_LOG.md.

No RH proof or disproof is asserted. The module and its exact maps are complete; no global file outside this subtask directory was edited.
