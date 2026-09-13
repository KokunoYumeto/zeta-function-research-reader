# Verification record

## New exact finite suite

`check_toda_volume.py`: 24 named methods pass in ordinary and optimized Python. The successful JSON records match. A separate deliberately failing 25th method fails under both modes. The implementation uses explicit exceptions/unittest checks, not Python assert statements for acceptance.

The suite constructs independent source moments, full quotient maps, canonical representatives, matrices and scalar determinants. It checks the two Toda equations, exact phase formula, full radius, source-boundary determinant quotient, curvature, mass factors, coordinate phases, minimal degree, repeated roots, parity qualifications, and the retained support labels.

The fixtures are rational Gaussian or finite atomic measures and algebraic packet polynomials. They are NOT certified zeta zeros or approximations silently substituted for them.

## Inherited source replay

All 34 entries of the previous exterior package's internal manifest verified. Its 22-method suite passed a fresh normal run. A combined command attempting a subsequent optimized replay timed out; no completed optimized inherited rerun is claimed. See `source_receipts/`.

## Numerical arithmetic input

`evaluate_seed.py` evaluates the actual h=1 theta mass and two derivatives at two precisions/cutoffs. It records no interval enclosures and no numerical omitted-tail certificate. The agreement of printed values is numerical evidence only. The complete infinite series and its convergence are proved in the note. The finite spectral quotient is zero for h=1.

## Reader and artifacts

HTML is rendered from the authored Markdown through Pandoc with MathML. The LaTeX is an editable source output; no PDF was produced. Reader checks and screenshots record visual inspection. No font files or external source corpus are distributed.

No new Lean certificate, uniform arithmetic bound, RH/GRH proof, or remote mutation is claimed.
