# What the exterior-power calculation establishes

[Read Section 38 in the current reader](../../reader.pdf#page=397) · [Full TeX proof](../../satellites/29t_alternating_packet_cost.tex) · [Frozen source edition DOI](https://doi.org/10.5281/zenodo.22728704)

We are studying finite packets of zeta zeros through their full polynomial
quotient, its tensor powers, and the original arithmetic inner products. The
symmetry projector matters: symmetric powers allow repeated spectral entries,
whereas exterior powers select subsets of the full multiplicity list. This
calculation determines exactly what that change retains and what it cancels.

For a packet of size d>=2 and exterior degree 1<=k<=d, let delta_i be the real part of
the ith spectral point minus one half. The complete second moment of the
k-element subset sums is

    binom(d-2,k-1) sum_i delta_i^2
      + binom(d-2,k-2) (sum_i delta_i)^2.

Binomial coefficients with a negative lower index are zero. The original
Hermitian control has the trace of its square equal to four times this
quantity plus twice its nonnegative metric departure. That departure retains
the strictly triangular part of the full operator, including surviving
nilpotents. No source metric, representative, factorial, or arithmetic unit
was replaced to obtain the formula.

The determinant line (k=d) sees only the total sum. Opposite real deviations
can cancel there completely, and its additive nilpotent part vanishes. Every
proper exterior degree (1<=k<d) retains a positive coefficient of the squared
individual deviations. A repeated root also leaves a nonzero nilpotent in
some sector of every proper exterior degree. Its exact sector index is
1+sum_rho ell_rho(m_rho-ell_rho), with all transition coefficients and CRT
maps given in the proof.

The same construction retains the full jet fibre after the Hilbert
representatives tend to zero: the graph closure is the product of the
alternating Hilbert space and its finite jet space. Even when determinant
control cancels, accumulated relative Gram loss still diverges. These are
explicit comparisons of the original operators and limits, not an RH
proof or disproof, and not an assumed uniform arithmetic upper estimate.

Read Section 38, pages 397-404, of the current 433-page main reader.
The source is satellites/29t_alternating_packet_cost.tex, equations EA.1-38.
The proof starts from the actual CT/JD/SS constructions in the separately
published 216-page continuation, DOI 10.5281/zenodo.22728704. Standard
conventions are linked directly to the Stacks Project and the indexed
Schur-Weyl source. The frozen DOI edition remains unchanged; this new section
belongs to the continuing main reader.

Verification is deliberately specific: written proofs received an independent
full-source review; 8,173 exact combinatorial/coordinate cases and 26 exact
companion-matrix/metric cases pass in ordinary and optimized Python. Five
deliberately false factor, coefficient, nilpotent, and inverse-compression
identities are rejected. Synthetic positive matrices are test fixtures, not
measured arithmetic Grams. This section is not claimed as newly Lean-checked.

Separately, PR18's five finite frontier modules are merged. The combined
kernel and transitive-dependency checks include 40 frontier targets, 68
integration targets and the inherited libraries. The new sum-connection
delivery (PR20), together with PR17's full sum-coordinate constructions, is
being integrated into the next tandem reader. Those incoming results are
not silently attributed to this exterior section or the frozen DOI.
