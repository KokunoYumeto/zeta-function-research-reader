# Independent review of the parent cutoff/theta proof

Reviewed in full: `work/tau_f1_transcript_audit_20260913/audit_early_context/NS_CUTOFF_THETA_SCALING.md`, SHA256 `42cea921e85843f5095ce633b0e8d39a44928cdf3ddb1917db53988aeb1d0744`.

Also read completely for this review: `output/split_zero_rh_tandem_2026-09-12/sources/Tau_Base_Cohomology_2026-09-12/NOTE.md`, SHA256 `d03e71ad18f187bd89880cb8ca6fc9c5d6f260b3de8e8e5702c27db97e7b63c3`.

No changes were made to either file. No algebraic correction was found in equations (1)–(13), including (3a)–(3c).

1. Equations (1)–(3) retain the two compact-support integration-by-parts signs. Substitution of the shifted Mellin variable gives \(((s-1/2)^2-1/4)=s(s-1)\), with exactly the multiplier \(r^{-1/2}\).
2. Equations (3a)–(3c) retain the unaveraged positive/negative theta factor of two and every cutoff product-rule term. The operator \(D\) preserves the stated even Schwartz space with zero value and zero integral.
3. Equations (4)–(6) keep viscosity fixed under the original constant parabolic map. The unaveraged angular integral introduces no extra factor of \(\lambda\). The chain lift's two legs are respectively \(\lambda^{1/2}U_{1/\lambda}\) and \(\lambda^{-1/2}U_\lambda\), and the differential's original minus sign is preserved.
4. Equation (7) is the complete truncated exponential on each actual local algebra; the coefficient convolution and each nilpotent term have the correct sign and factorial.
5. Equations (8)–(9) use the source's conjugate finite packet, reflected germ, residue orientation, and coefficient line. The factors \(\lambda^{s-1/2}\) and \(\lambda^{1/2-s}\) cancel exactly. Multiplication by \(G'\) commutes with the scalar germ, so the same cancellation proves the trace-contraction statement without eliminating nilpotents prematurely.
6. Equation (10) is equality of full autocorrelation test functions after the exact Haar-variable substitution. Consequently every retained local term of the source scalar is preserved, independent of any unknown sign.
7. Equation (11) follows from \(\partial_tu^\#=(\lambda'/\lambda)(u^\#+x\cdot\nabla_xu^\#)+\lambda s'\partial_su\) and the factor \(\lambda^3\) on all three terms of \(\mathcal N\). Thus the extra-force sign and coefficients are correct. Equation (12) cancels precisely the middle term when \(s'=\lambda^2\).
8. Equation (13) retains the extra \(+1/2\) in the uncentered theta target. Mellin integration by parts gives \(-s+1/2\); its full local-jet generator is \((1/2-\rho)I-N_\rho\).
9. The stated scope is correct: a transported concentration does not assert self-similarity of the fixed source solution; it does not set the source Weil scalar's sign; and time-varying coordinate transport does not inherit smooth forcing without the calculated extra term.

Two editorial precision suggestions were sent to the parent, without treating them as missing mathematics:

- Distinguish the Mellin variable from the source-time function, both currently called \(s\) in §6.
- Say explicitly that \(T_\lambda=\lambda^{1/2}U_{1/\lambda}\) is the centered transport. Its two scalar factors give \(\lambda\), canceling the original residue covariance factor \(a=1/\lambda\). The invariant pairing under \(T_\lambda\) must not be read as an invariant pairing under the original uncentered \(U_a\) action. The proof already contains this exact calculation.
