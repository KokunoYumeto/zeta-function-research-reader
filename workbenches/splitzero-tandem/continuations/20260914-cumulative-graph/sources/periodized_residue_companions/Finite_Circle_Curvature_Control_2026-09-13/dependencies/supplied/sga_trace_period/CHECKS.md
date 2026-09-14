# Executed checks and their scope

## Current finite suite

`check_trace_period.py`: **18 methods passed** under normal Python and under `python -O`. Both records have zero errors and failures and match exactly. Sympy 1.14.0 was used. The test methods use unittest checks, not assertions disabled by optimization.

The three false controls—omitting the trace Jacobian, treating the differential range as an ideal, and erasing a repeated characteristic factor—were all rejected with exit code 1 in both modes. Commands and outputs are in `checks/negative-controls.json`.

The tests cover the complete monic residue pairing, diagonal coevaluation, trace radical, periodic diagonal maps, repeated-root homology dimensions, quantum/classical triangular trace comparison, coefficient gradients, Newton reconstruction, source conormal response, original metric congruence, constituent-period derivative and rank-one normal acceleration, finite Fourier Gram and contour orientation, and e/tau cases.

## Independent analytic calibrations

`period_numerics.py` used 35 decimal digits and direct mpmath ray quadrature for declared degree-two and degree-three complex polynomial fixtures. The computed complex determinants agree with the written closed formula to relative discrepancies approximately 6.2e-36 and 8.7e-36. These numbers are numerical discrepancies, **not rigorously enclosed errors**. No actual zeta-zero packet was asserted by those calibrations. The convergence and arbitrary-degree determinant statements rely on the written proof.

## Predecessor replay

The exponential delivery's **51 manifest entries** and the logarithmic-constituent delivery's **38 entries** verified against their files. Their unchanged **22-method** and **16-method** suites passed fresh normal and optimized runs, with matching reports. No parent files were modified. The first wrapper invocation assumed both manifests used the key `files`; the second used `entries`, which caused a wrapper KeyError. The corrected wrapper accepts the two recorded structures and was rerun in full; this is documented in the development note.

## Scope

These are finite exact regression tests, archive-integrity checks, and non-interval numerical calibrations. No new Lean execution, complete SGA/Deligne audit, general arithmetic moment enclosure, uniform purity bound, or RH proof is claimed.

The reader and add-only patch have separate machine-readable validation records. They concern presentation/integration, not mathematical theorem certification.
