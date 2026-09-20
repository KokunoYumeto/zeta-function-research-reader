# Independent endpoint, multiplicity and phase check

The checked main proof was NATIVE_SPECTRAL_ACTION.tex, SA32–SA43. Its SHA-256 at the close of this check was 8a88c5c7a51d00f802646754427c80e3af668909f767a1b10e96104df6e61b47.

The independent complete calculations are in INDEPENDENT_ENDPOINT_CHECK.tex, EC1–EC15, SHA-256 6ea313e182d5707fb62805a925f9bcba762106dc0f3152a8d34a5a58ed45476f.

The new independent checker is check_endpoint_multiplicity_phase.py, SHA-256 64e90a2e7d47adee3d3b5e4917b8c1446e582703c55d27a4fa39a2e40216ea3d.

## Results

No correction to SA32–SA43 was found.

- SA41 holds at the nonzero Jordan endpoint M² = 0, M ≠ 0 in the requested two-dimensional example. The complete proof checks every polynomial and every derivative order: both sides are 2(-1)^n n! a_(2n)/3^n.
- The exact mass-three comparison metric for the quotient (u²+1)² has epsilon² = 3868/21, and both nonreal eigenvalues have size-two Jordan blocks. The original scaling aggregate is 4, not the distinct-only value 2, and its square is at most 3868/21.
- The generalized-eigenspace projection proof retains algebraic multiplicity even when the metric-orthogonal complement is not invariant.
- The determinant phase is i^q. The derivative phase is (-i)^n. Both follow from explicit matrix and divided-difference coordinate maps; no source metric was changed.

## Exact executions

The new checker passed 239 exact identities and rejected 6 wrong-formula controls, both in normal Python and with optimization enabled. It checks direct matrix traces against independent infinity-residue coefficients at both defective endpoints, full characteristic polynomials, comparison-measure Gram factors, and original-coordinate derivative phases. All guards are explicit exceptions.

The normal and optimized JSON outputs are identical and have SHA-256 0a1b4dc6cf6f6311e309599a79ea709043f4d26c50c6584646718f3f68344ed9.

The existing frozen MC proof and its checkers were not edited. No rendering, compilation, publication, arithmetic-zero assertion or asymptotic estimate was performed.
