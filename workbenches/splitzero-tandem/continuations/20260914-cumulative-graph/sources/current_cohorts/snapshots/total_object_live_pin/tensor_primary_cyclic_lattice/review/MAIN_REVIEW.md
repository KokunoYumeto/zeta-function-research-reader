# Independent review of the actual primary cyclic lattice

The entire main draft `tensor_primary_cyclic_lattice.tex`, TCL.1–27, was read at SHA256 `1828A7D0B7289CDBA819D71E76439270B31125BDE4EB3F3DCD2BEE77A167CEDD`.

No substantive mathematical defect was found. The derivation agrees with the independent complete proof `cyclic_lattice_independent_review.tex`, PCLR.1–29, SHA256 `80F48C8DD0897BF945189BE4BA2B8D60C3E27B1F1D899846AD9221BD540EDC90`.

## Checked maps and proofs

- The localized ring is the actual embedded single-primary coefficient ring localized at the kernel of its specified finite-field map. The image of that map is a finite field. No DVR assumption or extension of that map to the quartet CRT coefficient ring occurs.
- The original coordinates are retained by both invertible Pascal transformations. The original weighted source map is linear and cyclic-module linear; it is correctly distinguished from the unweighted unital ring map.
- Every divided-power coefficient denominator is a unit because its individual exponent is below p. The pivot functionals explicitly split the containing lattice in the full ordered algebra. The factorial matrix is calculated before any characteristic-p reduction.
- The full retained unit and its specified inverse transport both lattices, the complement, the projection and the quotient. No preservation of the original containing lattice by that unit is assumed.
- The saturation identity is proved using the explicit free complementary summand, not a PID argument.
- The quotient is the direct sum of the actual principal factorial quotients. The p-depths are the exact integer floor sums; principal p-power strictness follows by cancellation in the domain and the specified residue map.
- The reduced source, image and ambient actions are related by the literal specialized diagonal matrix. The abstract source has index K+1; the image, ambient algebra and divided-power containing lattice have index min(p,K+1). The reduced containing lattice has every divided-power block, including blocks absent from the cyclic image.
- The exact Tor sequence is computed from the displayed free resolution. It also applies to S/pS, without requiring that quotient to be a field or flat over S.
- The complete terminal scalar retains the actual a0^k and individual factorial denominators. Reduction does not kill the terminal basis monomial or identify it with external absence.
- The original MFC chain comparison has an actual coefficient injection Z/p^L→S/p^L, exact extension/contraction on the principal p-power subchain, sum/intersection/product formulas, a support-preserving semiring injection and the explicit support-to-ideal square. No all-ideal assertion about S/p^L occurs.
- The coordinate annihilator formula in TCL.27 is exact, including depth zero, where the coordinate class vanishes and its annihilator is the unit ideal. The e/absence distinction is retained by choosing L≥1.

## Corrections communicated

Three typesetting corrections were sent to the author: replace the comma in the TCL.8 pivot functional by multiplication spacing; restore the missing backslash in TCL.12 `qquad`; use an appropriate alignment environment for the multiple columns in TCL.26. These do not affect the checked algebra. The later main snapshot corrects the communicated TeX defects.

## Extended full read: TCL.28–36

I read every appended formula and proof through TCL.36 at main SHA256 `392CA4E23DDE6111785F5632608CE4F4961F7F0CAC1381101A9E99E32500F416`. I also read TP.25–26 and PAM.1–5 to check the original full-unit period projector and the actual quartet grid/idempotent source.

- TCL.28 gives the exact nilpotency K-p+1 on the lost abstract source chain; the kernel is not an ambient target submodule after specialization.
- TCL.29–32 use masks with the actual total character degree r+k modulo m+1. The full-unit conjugation direction U Q U^{-1} agrees with TP.26. The period map Π U^{-1}, its original Pascal coordinates, its retained phase scalar, the character-shift identities, and the Tor connecting map all agree exactly.
- TCL.33 uses actual quartet tensor centres kρ and (k-p)ρ+p(1-conjρ). Their difference is p(ρ+conjρ-1), nonzero under the retained counterfactual δ>0. Their stated PAM grid indices are correct.
- TCL.34 proves the inverse of p directly from the retained CRT representative e by the polynomial divided-difference identity. This does not depend on merely guessing which centre differences were inverted. Thus that whole CRT stage has no characteristic-p point when k≥p.
- TCL.35 repeats the same original idempotent argument for every prime q≤k, and TCL.36 consequently puts every rational prime inverse and then Q in the actual combined coefficient ring. Prime contraction proves the absence of all positive-characteristic residue fields of that union. This does not assert that a nonexistent global specialization killed an original arithmetic vector.
- The new note after TCL.27 correctly states that an annihilator's bottom support label does not replace its vector: a depth-L coordinate is a nonzero unit class with zero annihilator.

No mathematical defect was found in these additions. One indexing precision was sent: PAM displays degrees k≥2, so the stage union can start at degree 2, or degree 1 can explicitly be identified with the original quartet corner. Either convention yields the asserted rational subring since every rational prime is at least 2.

## TCL.37 and the corrected stage range

The author corrected the directed union to begin with degree 2. I also read TCL.37 completely: for m≥2 and k=pℓ, K≥p ensures W_p exists and J W_(p-1)=pW_p is nonzero over the characteristic-zero domain. Its reduction is zero, while the nonzero Wbar_(p-1) belongs to the reduced cyclic image because (p-1)! is a unit. Its character is p-1+k modulo N; character zero is exactly p(ℓ+1)≡1 modulo N. Since the retained prime p>N is coprime to N, the stated positive arithmetic progression of ℓ exists and is infinite. The text correctly makes this a coefficient-mask calculation and not a finite-field sheaf identification. All TCL.1–37 mathematics has therefore been reviewed and accepted.

## Independent proof validation

Final accepted main SHA256: `7371F26AA05099D14D72D55999C9AF8605125A20DA017876B3E129775E2EFAAE`.

I verified that hash directly from the final file, verified the degree-2 stage range and corrected display syntax, and inspected the final compilation log: ten draft pages, with no overfull/underfull box, LaTeX warning, or TeX error. The author's `EXACT_CHECKS.json` records passed exact checks for 25 packet cases, 164 prime-packet cases and divided-difference polynomial identities in degrees 1–9; it pins the same final source hash. These finite checks supplement the fully reviewed general proofs rather than replacing them.

Final disposition: all TCL.1–37 proofs and specified morphisms accepted; no mathematical correction remains outstanding. This acceptance concerns the actual local cyclic lattice, exact support/character maps and retained CRT specialization obstruction proved in the module. It makes no RH verdict.

The PCLR proof has a clean five-page `pdflatex -interaction=nonstopmode -halt-on-error -draftmode` compilation with no overfull/underfull box or LaTeX warning. Draft mode intentionally creates no PDF. This is a mathematical and TeX review, with no RH claim.
